#!/usr/bin/env python3
"""Build the PDFs from the Markdown sources.

    python tools/build_pdfs.py --all            # every chapter PDF + the full book
    python tools/build_pdfs.py --chapter 20     # one chapter only
    python tools/build_pdfs.py --full           # full book only

Output goes to build/pdf/ (chapters/NN-slug.pdf and AQM1_PHS4102_Notes.pdf).
The CI workflow copies that folder into the site as /pdf/.

Needs: pandoc >= 3.1, a LaTeX install (pdflatex, tcolorbox, tikz not needed),
and pdftocairo-made figure PDFs in docs/assets/figures/ (kept in the repo).
"""
import argparse
import concurrent.futures as cf
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
OUT = os.path.join(ROOT, "build", "pdf")
PDFDIR = os.path.join(ROOT, "tools", "pdf")
BOOK_TITLE = "Advanced Quantum Mechanics I (PHS 4102)"
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

ADM_RE = re.compile(r'^(\s*)(?:!!!|\?\?\?\+?)\s+(\S+)(?:\s+"(.*)")?\s*$')


# ---------------------------------------------------------------- front matter
def split_front(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for ln in m.group(1).split("\n"):
        k, _, v = ln.partition(":")
        meta[k.strip()] = v.strip().strip('"')
    return meta, text[m.end():]


def chapters():
    out = []
    for f in sorted(glob.glob(os.path.join(DOCS, "0*", "[0-9][0-9]-*.md"))):
        meta, body = split_front(open(f, encoding="utf-8").read())
        out.append(dict(path=f, stem=os.path.splitext(os.path.basename(f))[0],
                        part=int(meta.get("part", 0)), num=int(meta.get("chapter", 0)),
                        title=meta.get("title", ""), body=body))
    return out


# ---------------------------------------------------------------- admonitions
def tex_escape(s):
    for a, b in [("\\", "\\textbackslash{}"), ("&", "\\&"), ("%", "\\%"), ("_", "\\_"),
                 ("#", "\\#"), ("$", "\\$"), ("{", "\\{"), ("}", "\\}")]:
        s = s.replace(a, b)
    return s


def escape_title(title):
    """Escape LaTeX specials in the text parts of a box title, leave $...$ math alone."""
    parts = re.split(r"(\$[^$]*\$)", title)
    return "".join(p if p.startswith("$") else
                   p.replace("&", "\\&").replace("%", "\\%").replace("#", "\\#").replace("_", "\\_")
                   for p in parts)


def convert_admonitions(lines):
    """Rewrite '!!! type "Title"' blocks (indented content) as pandoc fenced divs."""
    out, h = _adm(lines, 0)
    return out


def _adm(lines, base):
    """Process lines. Admonitions may be indented (inside list items); their content
    is everything indented 4 more spaces than the '!!!' line. Returns (lines, height)."""
    res = []
    i = 0
    height = 0
    while i < len(lines):
        m = ADM_RE.match(lines[i])
        if m:
            ind = m.group(1)
            typ, title = m.group(2), m.group(3) or ""
            need = ind + "    "
            j = i + 1
            block = []
            while j < len(lines):
                ln = lines[j]
                if ln.strip() == "":
                    block.append("")
                    j += 1
                    continue
                if ln.startswith(need):
                    block.append(ln[len(need):])
                    j += 1
                    continue
                break
            while block and block[-1] == "":
                block.pop()
            inner, ih = _adm(block, 0)
            colons = ":" * (3 + ih)
            title = escape_title(title).replace('"', "'")
            res.append("")
            res.append('%s%s {.adm type="%s" title="%s"}' % (ind, colons, typ, title))
            res.append("")
            res.extend((ind + l) if l.strip() else "" for l in inner)
            res.append("")
            res.append(ind + colons)
            res.append("")
            height = max(height, ih + 1)
            i = j
            continue
        res.append(lines[i])
        i += 1
    return res, height


# ---------------------------------------------------------------- links, figures
def fix_links(body, ch, all_chapters, only_this):
    stems = {c["stem"] for c in all_chapters}

    def link(m):
        text, target = m.group(1), m.group(2)
        mm = re.match(r"(?:\.\./[^/]+/|\./)?([0-9]{2}-[^/#)]*)\.md(?:#(.*))?$", target)
        if not mm:
            return m.group(0)
        stem, anchor = mm.group(1), mm.group(2)
        if stem not in stems:
            return text
        if only_this and stem != ch["stem"]:
            return text  # another chapter: keep the words, drop the link
        return "[%s](#%s)" % (text, anchor if anchor else "ch-" + stem)
    body = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, body)

    # figures: SVG for the web, PDF for print
    def fig(m):
        name = m.group(1)
        return "![](%s)" % os.path.join(DOCS, "assets", "figures", name + ".pdf")
    body = re.sub(r"!\[\]\([^)]*?assets/figures/([^)/]+)\.svg\)(?:\{[^}]*\})?", fig, body)
    # explicit anchor on the chapter heading
    body = re.sub(r"^(# .*?)\s*$", lambda m: m.group(1) + " {#ch-%s}" % ch["stem"], body, count=1, flags=re.M)
    return body


PANDOC = ["pandoc", "-f", "markdown+tex_math_dollars+raw_tex+fenced_divs+pipe_tables+header_attributes-auto_identifiers-smart-yaml_metadata_block",
          "-t", "latex", "--wrap=none", "--lua-filter", os.path.join(PDFDIR, "adm.lua"),
          "--columns=60"]


def md_to_tex(md):
    r = subprocess.run(PANDOC, input=md, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("pandoc failed:\n" + r.stderr)
    if r.stderr.strip():
        print("  pandoc:", r.stderr.strip()[:200])
    return r.stdout


def chapter_tex(ch, all_chapters, only_this):
    body = fix_links(ch["body"], ch, all_chapters, only_this)
    body = "\n".join(convert_admonitions(body.split("\n")))
    return md_to_tex(body)


# ---------------------------------------------------------------- documents
def preamble(lhead, rhead):
    base = open(os.path.join(PDFDIR, "preamble_base.tex"), encoding="utf-8").read()
    extra = open(os.path.join(PDFDIR, "preamble_extra.tex"), encoding="utf-8").read()
    return (base + extra +
            "\n\\lhead{\\textbf{%s}}\n\\rhead{%s}\n" % (tex_escape(lhead), tex_escape(rhead)))


def compile_tex(tex, name, outdir, passes=1):
    os.makedirs(outdir, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        open(os.path.join(td, name + ".tex"), "w", encoding="utf-8").write(tex)
        for _ in range(passes):
            r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                               cwd=td, capture_output=True, text=True)
            if r.returncode != 0:
                log = r.stdout
                i = log.find("\n!")
                print("LaTeX failed for", name, "\n", log[max(0, i):i + 900])
                open(os.path.join(outdir, name + ".failed.tex"), "w", encoding="utf-8").write(tex)
                return False
        shutil.copy(os.path.join(td, name + ".pdf"), os.path.join(outdir, name + ".pdf"))
        logdir = os.path.join(ROOT, "build", "logs")
        os.makedirs(logdir, exist_ok=True)
        shutil.copy(os.path.join(td, name + ".log"), os.path.join(logdir, name + ".log"))
    return True


def build_chapter(ch, all_chapters):
    body = chapter_tex(ch, all_chapters, only_this=True)
    tex = (preamble(BOOK_TITLE, ch["title"]) + "\n\\begin{document}\n" +
           "\\thispagestyle{fancy}\n" + body + "\n\\end{document}\n")
    ok = compile_tex(tex, ch["stem"], os.path.join(OUT, "chapters"), passes=2)
    print(("built " if ok else "FAILED ") + ch["stem"])
    return ok


def part_info():
    info = {}
    for d in sorted(glob.glob(os.path.join(DOCS, "0*", "index.md"))):
        meta, body = split_front(open(d, encoding="utf-8").read())
        mt = re.search(r"^# Part [IVX]+: (.*)$", body, re.M)
        title = mt.group(1).strip() if mt else os.path.basename(os.path.dirname(d))
        scope = body.split("## Chapters")[0]
        scope = re.sub(r"^# .*$", "", scope, flags=re.M).strip()
        info[os.path.basename(os.path.dirname(d))] = (title, scope)
    return info


def build_full(all_chapters):
    info = part_info()
    parts = {}
    for c in all_chapters:
        parts.setdefault(os.path.basename(os.path.dirname(c["path"])), []).append(c)
    pieces = []
    for pdir in sorted(parts):
        title, scope = info.get(pdir, (pdir, ""))
        scope_tex = md_to_tex(scope).strip().replace("\n\n", " ")
        pieces.append("\\partheading{%s}{%s}\n" % (tex_escape(title), scope_tex))
        for c in parts[pdir]:
            pieces.append(chapter_tex(c, all_chapters, only_this=False))
            pieces.append("\n")
    head = (
        "\\title{\\vspace{-1cm}\\textbf{\\textcolor{primary}{%s}}\\\\\\large Complete Lecture Notes \\& Worked Problems}\n"
        "\\author{}\n\\date{}\n" % tex_escape(BOOK_TITLE))
    tex = (preamble(BOOK_TITLE, "Exam Revision Notes") + head + "\n\\begin{document}\n\\maketitle\n"
           "\\tableofcontents\n\\vspace{0.5cm}\\hrule\\vspace{0.5cm}\n" + "".join(pieces) + "\n\\end{document}\n")
    ok = compile_tex(tex, "AQM1_PHS4102_Notes", OUT, passes=3)
    print(("built " if ok else "FAILED ") + "AQM1_PHS4102_Notes")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--chapter", type=int, action="append")
    ap.add_argument("-j", type=int, default=4)
    a = ap.parse_args()
    chs = chapters()
    ok = True
    if a.all or a.chapter:
        todo = [c for c in chs if a.all or c["num"] in a.chapter]
        with cf.ThreadPoolExecutor(a.j) as ex:
            res = list(ex.map(lambda c: build_chapter(c, chs), todo))
        ok = ok and all(res)
    if a.all or a.full:
        ok = build_full(chs) and ok
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
