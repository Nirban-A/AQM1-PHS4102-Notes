#!/usr/bin/env python3
"""Convert the combined LaTeX notes (legacy/AQM1_PHS4102_Notes.tex) into one
Markdown file per section (chapter), plus SVG figures and a nav snippet.

One-off bootstrap tool: after the first run the Markdown files in docs/ are the
source of truth and are edited by hand.

Usage:  python tools/convert_tex.py [--only N]      (N = global section number)
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "legacy", "AQM1_PHS4102_Notes.tex")
DOCS = os.path.join(ROOT, "docs")
FIGDIR = os.path.join(DOCS, "assets", "figures")
CACHE = os.path.join(ROOT, ".figcache")

PART_DIRS = [
    "01-foundations",
    "02-symmetry-angular-momentum",
    "03-tensor-operators",
    "04-time-independent-approximations",
    "05-time-dependent-perturbation",
]

DISPLAY_ENVS = ["align*", "gather*", "align", "gather", "equation*", "equation", "multline*"]

TAG_TYPES = [
    ("Study Note", "studynote"),
    ("Intuition", "intuition"),
    ("Exam Tip", "examtip"),
    ("Complete Solution", "solution"),
    ("Verification", "verification"),
    ("Memory Rule", "memory"),
    ("Common mistakes", "mistakes"),
    ("Alternate method", "studynote"),
]


# ----------------------------------------------------------------------------
# small helpers
# ----------------------------------------------------------------------------
def match_brace(s, i):
    """s[i] == '{'; return index of the matching '}'."""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return j
        j += 1
    raise ValueError("unbalanced brace at %d: %r" % (i, s[i : i + 60]))


def plain(t):
    """TeX title -> plain text (for nav labels, file names, front matter)."""
    t = re.sub(r"\\texorpdfstring\{([^{}]*)\}\{[^{}]*\}", r"\1", t)
    rep = [
        (r"\tfrac12", "1/2"), (r"\tfrac{1}{2}", "1/2"), (r"\to", " to "),
        (r"\otimes", " x "), (r"\ell", "l"), (r"\hat", ""), (r"\vec", ""),
        (r"\tfrac", ""), (r"\dagger", "+"), (r"\\", ""), ("\\,", " "),
    ]
    t = t.replace('\\"o', "ö").replace("\\'e", "é").replace('\\"u', "ü").replace('\\"a', "ä")
    t = t.replace("\\&", "&").replace("\\'a", "á")
    for a, b in rep:
        t = t.replace(a, b)
    t = t.replace("$", "")
    t = re.sub(r"[{}\\]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def slugify(t, maxwords=6):
    t = unicodedata.normalize("NFKD", plain(t)).encode("ascii", "ignore").decode().lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    parts = [p for p in t.split("-") if p and p not in ("the", "and", "of", "a", "in")]
    return "-".join(parts[:maxwords])


# ----------------------------------------------------------------------------
# parse the master file into parts and chapters
# ----------------------------------------------------------------------------
def load_chapters():
    s = open(SRC, encoding="utf-8").read()
    body = s.split("\\begin{document}", 1)[1].rsplit("\\end{document}", 1)[0]
    preamble = s.split("\\begin{document}", 1)[0]
    parts = []
    # split at \partheading{TITLE}{SCOPE}
    idx = [m.start() for m in re.finditer(r"^\\partheading\{", body, re.M)]
    for pi, st in enumerate(idx):
        en = idx[pi + 1] if pi + 1 < len(idx) else len(body)
        chunk = body[st:en]
        a = chunk.index("{")
        b = match_brace(chunk, a)
        title = chunk[a + 1 : b]
        c = chunk.index("{", b)
        d = match_brace(chunk, c)
        scope = chunk[c + 1 : d]
        rest = chunk[d + 1 :]
        secs = []
        sidx = [m.start() for m in re.finditer(r"^\\section\{", rest, re.M)]
        for si, ss in enumerate(sidx):
            se = sidx[si + 1] if si + 1 < len(sidx) else len(rest)
            sec = rest[ss:se]
            a = sec.index("{")
            b = match_brace(sec, a)
            secs.append({"title": sec[a + 1 : b], "text": sec[b + 1 :]})
        parts.append({"title": title, "scope": scope, "sections": secs})
    return preamble, parts


# ----------------------------------------------------------------------------
# figures
# ----------------------------------------------------------------------------
def figure_preamble(preamble):
    keep = []
    for line in preamble.split("\n"):
        if line.startswith("\\definecolor") or line.startswith("\\usetikzlibrary"):
            keep.append(line)
    return (
        "\\documentclass[border=4pt]{standalone}\n"
        "\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n"
        "\\usepackage{xcolor}\n\\usepackage{tikz}\n" + "\n".join(keep) + "\n"
    )


def build_figure(tikz_src, name, fpre):
    os.makedirs(FIGDIR, exist_ok=True)
    os.makedirs(CACHE, exist_ok=True)
    h = hashlib.sha1((fpre + tikz_src).encode()).hexdigest()[:12]
    svg = os.path.join(FIGDIR, name + ".svg")
    pdf = os.path.join(FIGDIR, name + ".pdf")
    cached = os.path.join(CACHE, h + ".pdf")
    if not os.path.exists(cached):
        with tempfile.TemporaryDirectory() as td:
            tex = os.path.join(td, "f.tex")
            open(tex, "w", encoding="utf-8").write(
                fpre + "\\begin{document}\n" + tikz_src + "\n\\end{document}\n"
            )
            r = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "f.tex"],
                cwd=td, capture_output=True, text=True,
            )
            if r.returncode != 0 or not os.path.exists(os.path.join(td, "f.pdf")):
                print("FIGURE FAILED", name, "\n", r.stdout[-1500:])
                raise SystemExit(1)
            shutil.copy(os.path.join(td, "f.pdf"), cached)
    shutil.copy(cached, pdf)
    subprocess.run(["pdftocairo", "-svg", pdf, svg], check=True)


# ----------------------------------------------------------------------------
# math extraction
# ----------------------------------------------------------------------------
class Stash:
    def __init__(self):
        self.items = {}
        self.n = 0

    def put(self, kind, content):
        self.n += 1
        key = "%sZZ%dZZ" % (kind, self.n)
        self.items[key] = content
        return key


def extract_math(s, st):
    """Replace math by placeholders: MATHIZZnZZ (inline), MATHDZZnZZ (display),
    MATHEZZnZZ (raw environment display)."""
    out = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c == "\\" and s.startswith("\\[", i):
            j = s.index("\\]", i + 2)
            out.append("\n\n" + st.put("MATHD", s[i + 2 : j]) + "\n\n")
            i = j + 2
            continue
        if c == "\\" and s.startswith("\\begin{", i):
            m = re.match(r"\\begin\{([a-z]+\*?)\}", s[i:])
            env = m.group(1)
            if env in DISPLAY_ENVS:
                end = "\\end{%s}" % env
                j = s.index(end, i)
                out.append("\n\n" + st.put("MATHE", s[i : j + len(end)]) + "\n\n")
                i = j + len(end)
                continue
        if c == "\\":
            out.append(s[i : i + 2])
            i += 2
            continue
        if c == "$":
            if s.startswith("$$", i):
                j = s.index("$$", i + 2)
                out.append("\n\n" + st.put("MATHD", s[i + 2 : j]) + "\n\n")
                i = j + 2
                continue
            j = i + 1
            while True:
                if s[j] == "\\":
                    j += 2
                    continue
                if s[j] == "$":
                    break
                j += 1
            out.append(st.put("MATHI", s[i + 1 : j]))
            i = j + 1
            continue
        out.append(c)
        i += 1
    return "".join(out)


def clean_math(m, table=False):
    m = re.sub(r"(?<!\\)%.*", "", m)  # tex comments
    m = m.strip()
    if table:
        m = m.replace("\\|", "\\Vert ").replace("|", "\\vert ")
    return m


# ----------------------------------------------------------------------------
# main per-chapter conversion
# ----------------------------------------------------------------------------
def tabular_to_array(block, st):
    """tabular with vertical rules (C-G tables) -> math array placeholder."""
    m = re.match(r"\\begin\{tabular\}\{([^}]*)\}(.*)\\end\{tabular\}", block, re.S)
    spec, inner = m.group(1), m.group(2)
    spec = spec.replace("@{}", "")
    rows = []
    for row in re.split(r"\\\\", inner):
        row = row.strip()
        if not row:
            continue
        hl = ""
        while row.startswith("\\hline"):
            hl += "\\hline "
            row = row[len("\\hline"):].strip()
        cells = []
        for cell in row.split("&"):
            cell = cell.strip()
            mm = re.fullmatch(r"\$(.*)\$", cell, re.S)
            if mm:
                cell = mm.group(1)
            elif cell:
                cell = "\\text{%s}" % cell
            cells.append(cell)
        rows.append(hl + " & ".join(cells))
    arr = "\\begin{array}{%s}\n%s\n\\end{array}" % (spec, " \\\\\n".join(rows))
    return "\n\n" + st.put("MATHD", arr) + "\n\n"


def convert_chapter(ch, ctx):
    """ch: dict(title, text, num, part, key). Returns markdown body (no heading)."""
    st = Stash()
    text = ch["text"]
    # comments
    text = re.sub(r"^[ \t]*%.*\n?", "", text, flags=re.M)
    # figures
    figs = []

    def figsub(m):
        figs.append(m.group(0))
        name = "%s-fig%d" % (ch["key"], len(figs))
        build_figure(m.group(0), name, ctx["fpre"])
        return "\n\nFIGZZ%sZZ\n\n" % name

    text = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", figsub, text, flags=re.S)
    # tabular with vertical rules -> math arrays
    text = re.sub(
        r"\\begin\{tabular\}\{[^}]*\|[^}]*\}.*?\\end\{tabular\}",
        lambda m: tabular_to_array(m.group(0), st), text, flags=re.S)
    # rule-less tabulars: protect math with table-safe bars
    def table_sub(m):
        blk = m.group(0)
        tst = []
        def mm(mo):
            tst.append(clean_math(mo.group(1), table=True))
            return "\x00%d\x00" % (len(tst) - 1)
        blk2 = re.sub(r"\$(.*?)\$", mm, blk, flags=re.S)
        blk2 = re.sub(r"\x00(\d+)\x00", lambda mo: st.put("MATHI", tst[int(mo.group(1))]), blk2)
        return blk2
    text = re.sub(r"\\begin\{tabular\}.*?\\end\{tabular\}", table_sub, text, flags=re.S)
    # math
    text = extract_math(text, st)
    for k, v in list(st.items.items()):
        st.items[k] = clean_math(v)

    # drop layout-only commands
    text = re.sub(r"\\renewcommand\{\\arraystretch\}\{[^}]*\}", "", text)
    text = re.sub(r"\\(vspace|hspace)\*?\{[^}]*\}", "", text)
    text = re.sub(r"\\(noindent|small|footnotesize|centering|medskip|bigskip|smallskip|newpage|clearpage|hrule|hfill)\b", "", text)
    text = re.sub(r"\\begin\{center\}|\\end\{center\}", "\n\n", text)
    text = text.replace("\\ ", " ")
    text = re.sub(r"\\qed\b", "\u220e", text)

    # headings
    heads = []  # (level, texnum, anchor-or-None, title)

    def head_sub(m):
        level = {"subsection": 2, "subsubsection": 3}[m.group(1)]
        a = m.start(2) - 1
        full = m.group(0)
        return full  # placeholder, replaced below
    out = []
    pos = 0
    lines = text.split("\n")
    # process heading commands line by line (they are always at line start)
    new_lines = []
    sub = 0
    subsub = 0
    last = ("sec", None)
    for ln in lines:
        mm = re.match(r"\\(subsection|subsubsection)\{", ln)
        if mm:
            a = ln.index("{")
            b = match_brace(ln, a)
            title = ln[a + 1 : b]
            tail = ln[b + 1 :]
            if mm.group(1) == "subsection":
                sub += 1
                subsub = 0
                num = "%d.%d" % (ch["num"], sub)
                lvl = 2
            else:
                subsub += 1
                num = "%d.%d.%d" % (ch["num"], sub, subsub)
                lvl = 3
            lab = re.search(r"\\label\{([^}]*)\}", tail)
            anchor = None
            if lab:
                anchor = lab.group(1).replace(":", "-").replace("_", "-")
                ctx["labels"][lab.group(1)] = (ch, num, anchor)
                tail = tail.replace(lab.group(0), "")
            title = re.sub(r"\\texorpdfstring\{((?:[^{}]|\{[^{}]*\})*)\}\{(?:[^{}]|\{[^{}]*\})*\}", r"\1", title)
            new_lines.append("\n\nHEADZZ%dZZ%sZZ%sZZ %s\n\n%s" % (lvl, num, anchor or "", title, tail))
            continue
        lab = re.fullmatch(r"\s*\\label\{([^}]*)\}\s*", ln)
        if lab:
            continue  # section-level labels are handled in phase 1
        new_lines.append(ln)
    text = "\n".join(new_lines)
    text = re.sub(r"\\paragraph\{", r"\\textbf{", text)

    # custom boxes -> markers
    def box_sub(m):
        kind = m.group(1)
        a = m.end() - 1
        b = match_brace(text_ref[0], a)
        return None
    # do boxes by manual scan (nested braces in titles)
    res = []
    i = 0
    while i < len(text):
        mo = re.compile(r"\\begin\{(thm|prob)\}\{").search(text, i)
        if not mo:
            res.append(text[i:])
            break
        res.append(text[i : mo.start()])
        a = mo.end() - 1
        b = match_brace(text, a)
        title = text[a + 1 : b]
        res.append("\n\nADMSTARTZZ %s\n\nADMTITLEZZ %s\n\n" % (mo.group(1), title))
        i = b + 1
    text = "".join(res)
    text = re.sub(r"\\end\{(thm|prob)\}", "\n\nADMENDZZ\n\n", text)

    # study-tag paragraphs -> admonition markers
    text = re.sub(r"[ \t]*\n?[ \t]*(\\textbf\{\*\*\*)", r"\n\n\1", text)
    paras = re.split(r"\n[ \t]*\n+", text)
    paras = [p.strip("\n") for p in paras if p.strip()]
    outp = []
    i = 0

    def is_display_only(p):
        return re.fullmatch(r"\s*(MATH[DE]ZZ\d+ZZ\s*)+(\\tag\{[^}]*\})?\s*", p) is not None

    while i < len(paras):
        p = paras[i]
        if p.lstrip().startswith("\\textbf{***"):
            a = p.index("{")
            b = match_brace(p, a)
            label = p[a + 1 : b][3:].strip().rstrip(":").strip()
            rest = p[b + 1 :].strip()
            if not label:
                label = "Note"
            typ, base = "studynote", label
            for name, t in TAG_TYPES:
                if label.lower().startswith(name.lower()):
                    typ, base = t, name
                    break
            else:
                print("  unknown tag label:", label)
            if "ZZ" in label:  # math inside the label: keep it out of the title
                qual = label[len(base):].strip()
                title = base
                rest = "\\textit{%s:} %s" % (qual, rest)
            else:
                title = label if label != base else base
            blk = ["ADMSTARTZZ %s" % typ, "ADMTITLEZZ %s" % title, rest]
            prev = rest
            i += 1
            while i < len(paras):
                q = paras[i]
                if q.lstrip().startswith("\\textbf{***") or q.startswith(("ADMSTARTZZ", "ADMENDZZ", "ADMTITLEZZ", "HEADZZ", "FIGZZ")):
                    break
                cont = False
                if is_display_only(q):
                    cont = True
                elif is_display_only(prev) and re.match(r"[a-z(]", q.lstrip()):
                    cont = True
                elif prev.rstrip().endswith(":") and re.match(r"\\begin\{(itemize|enumerate)\}", q.lstrip()):
                    cont = True
                elif re.match(r"\\begin\{(itemize|enumerate)\}", prev.lstrip()) and re.match(r"[a-z]", q.lstrip()):
                    cont = True
                if not cont:
                    break
                blk.append(q)
                prev = q
                i += 1
            blk.append("ADMENDZZ")
            outp.append("\n\n".join(blk))
            continue
        outp.append(p)
        i += 1
    text = "\n\n".join(outp)

    # section references
    text = re.sub(r"Section~\\ref\{([^}]*)\}", lambda m: "XREFZZ%sZZ" % m.group(1).replace(":", "_"), text)
    text = text.replace("\\emph{", "\\textit{")

    # ---------------------------------------------------------- pandoc
    r = subprocess.run(
        ["pandoc", "-f", "latex", "-t", "markdown-smart-simple_tables-multiline_tables-grid_tables+pipe_tables-raw_html-fenced_divs-link_attributes-header_attributes-citations-escaped_line_breaks",
         "--wrap=none"],
        input=text, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr)
        raise SystemExit(1)
    if r.stderr.strip():
        print("  pandoc:", r.stderr.strip()[:300])
    md = r.stdout
    return md, st, figs


def postprocess(md, st, ch, ctx):
    lines = md.split("\n")
    out = []
    depth = 0
    # admonition marker handling
    i = 0
    stack = []

    def ind():
        return "    " * len(stack)

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s.startswith("ADMSTARTZZ"):
            kind = s.split()[1]
            base = ln[: len(ln) - len(ln.lstrip())]
            # next non-blank line is the title
            j = i + 1
            while lines[j].strip() == "":
                j += 1
            assert lines[j].strip().startswith("ADMTITLEZZ"), (lines[j])
            title = lines[j].strip()[len("ADMTITLEZZ"):].strip()
            title = title.replace('"', "\u201d")
            out.append(ind() + base + ('!!! %s "%s"' % (kind, title) if title else "!!! %s" % kind))
            out.append("")
            stack.append(kind)
            i = j + 1
            continue
        if s == "ADMENDZZ":
            stack.pop()
            out.append("")
            i += 1
            continue
        if s.startswith("HEADZZ"):
            m = re.match(r"HEADZZ(\d)ZZ([\d.]+)ZZ([^Z]*)ZZ\s*(.*)", s)
            lvl, num, anchor, title = int(m.group(1)), m.group(2), m.group(3), m.group(4)
            h = "#" * lvl + " %s %s" % (num, title)
            if anchor:
                h += " { #%s }" % anchor
            out.append("")
            out.append(h)
            out.append("")
            i += 1
            continue
        out.append((ind() + ln) if ln.strip() else "")
        i += 1
    assert not stack, "unclosed admonition"
    md = "\n".join(out)

    # figures
    def figsub(m):
        name = m.group(1)
        return "![](%s){ .fig }" % os.path.relpath(
            os.path.join(FIGDIR, name + ".svg"), os.path.dirname(ch["path"])).replace("\\", "/")
    md = re.sub(r"FIGZZ([A-Za-z0-9_-]+)ZZ", figsub, md)

    # math restore (line-aware indentation for display math)
    def restore_line(line):
        mm = re.match(r"^(\s*)(MATH[DE]ZZ\d+ZZ)\s*$", line)
        if mm:
            pre, key = mm.group(1), mm.group(2)
            body = st.items[key]
            body = "\n".join(l for l in body.split("\n") if l.strip())
            if key.startswith("MATHD"):
                txt = "$$\n" + body + "\n$$"
            else:
                txt = body
            return "\n".join(pre + l for l in txt.split("\n"))
        def inl(mo):
            body = st.items[mo.group(0)]
            body = re.sub(r"\s+", " ", body).strip()
            return "$" + body + "$"
        line = re.sub(r"MATHIZZ\d+ZZ", inl, line)
        if "MATHDZZ" in line or "MATHEZZ" in line:
            # display placeholder glued to text (should be rare)
            def disp(mo):
                key = mo.group(0)
                b = "\n".join(l for l in st.items[key].split("\n") if l.strip())
                return "\n$$\n" + b + "\n$$\n" if key.startswith("MATHD") else "\n" + b + "\n"
            line = re.sub(r"MATH[DE]ZZ\d+ZZ", disp, line)
        return line
    md = "\n".join(restore_line(l) for l in md.split("\n"))

    # cross references
    def refsub(m):
        lab = m.group(1).replace("_", ":")
        tch, num, anchor = ctx["labels"][lab]
        rel = os.path.relpath(tch["path"], os.path.dirname(ch["path"])).replace("\\", "/")
        if tch is ch:
            rel = ""
        link = rel + ("#" + anchor if anchor else "")
        return "[Section %s](%s)" % (num, link) if link else "Section %s" % num
    md = re.sub(r"XREFZZ([A-Za-z0-9_:\-]*)ZZ", refsub, md)

    # cosmetic
    md = md.replace("\u00a0", " ")
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", type=int, default=None)
    ap.add_argument("--force", action="store_true", help="overwrite chapters even if the site was already bootstrapped")
    args = ap.parse_args()
    marker = os.path.join(ROOT, "tools", ".bootstrapped")
    if os.path.exists(marker) and not args.force:
        sys.exit("The Markdown chapters are now the source of truth; re-running would overwrite your edits.\n"
                 "Use --force only if you really want to regenerate them from legacy/.")

    preamble, parts = load_chapters()
    fpre = figure_preamble(preamble)
    ctx = {"labels": {}, "fpre": fpre}

    # phase 1: numbering, file paths, section labels
    num = 0
    chapters = []
    for pi, part in enumerate(parts):
        for sec in part["sections"]:
            num += 1
            key = "%02d-%s" % (num, slugify(sec["title"]))
            ch = dict(title=sec["title"], text=sec["text"], num=num, part=pi + 1, key=key)
            ch["path"] = os.path.join(DOCS, PART_DIRS[pi], key + ".md")
            lab = re.search(r"\\label\{([^}]*)\}", sec["text"].split("\\subsection", 1)[0])
            if lab:
                ctx["labels"][lab.group(1)] = (ch, str(num), None)
            ch["labels_in_text"] = re.findall(r"\\subsection\{.*?\}\\label\{([^}]*)\}", sec["text"])
            chapters.append(ch)
    # subsection labels are registered during conversion, but refs need them first:
    # do a cheap pre-pass numbering subsections
    for ch in chapters:
        sub = 0
        for ln in ch["text"].split("\n"):
            if re.match(r"\\subsection\{", ln):
                sub += 1
                lab = re.search(r"\\label\{([^}]*)\}", ln)
                if lab:
                    anchor = lab.group(1).replace(":", "-").replace("_", "-")
                    ctx["labels"][lab.group(1)] = (ch, "%d.%d" % (ch["num"], sub), anchor)
    # labels on the line after \subsection
    for ch in chapters:
        sub = 0
        lines = ch["text"].split("\n")
        for k, ln in enumerate(lines):
            if re.match(r"\\subsection\{", ln):
                sub += 1
                nxt = lines[k + 1] if k + 1 < len(lines) else ""
                lab = re.fullmatch(r"\s*\\label\{([^}]*)\}\s*", nxt)
                if lab:
                    anchor = lab.group(1).replace(":", "-").replace("_", "-")
                    ctx["labels"][lab.group(1)] = (ch, "%d.%d" % (ch["num"], sub), anchor)

    nav = []
    for pi, part in enumerate(parts):
        os.makedirs(os.path.join(DOCS, PART_DIRS[pi]), exist_ok=True)
        idx = os.path.join(DOCS, PART_DIRS[pi], "index.md")
        # part index page: scope + chapter list written after chapters
    for ch in chapters:
        if args.only and ch["num"] != args.only:
            continue
        print("chapter %d: %s" % (ch["num"], plain(ch["title"])))
        md, st, figs = convert_chapter(ch, ctx)
        body = postprocess(md, st, ch, ctx)
        title_md = ch["title"]
        title_md = re.sub(r"\\texorpdfstring\{((?:[^{}]|\{[^{}]*\})*)\}\{(?:[^{}]|\{[^{}]*\})*\}", r"\1", title_md)
        tst = Stash()
        t2 = extract_math(title_md, tst)
        r = subprocess.run(["pandoc", "-f", "latex", "-t", "markdown-smart", "--wrap=none"],
                           input=t2, capture_output=True, text=True)
        t3 = r.stdout.strip()
        t3 = re.sub(r"MATHIZZ\d+ZZ", lambda m: "$" + clean_math(tst.items[m.group(0)]) + "$", t3)
        fm = "---\ntitle: %s\npart: %d\nchapter: %d\nsource_book: \nsource_section: \nexam_asked: []\ntopics: []\n---\n\n" % (
            json.dumps(plain(ch["title"]), ensure_ascii=False), ch["part"], ch["num"])
        os.makedirs(os.path.dirname(ch["path"]), exist_ok=True)
        open(ch["path"], "w", encoding="utf-8").write(fm + "# %d %s\n\n" % (ch["num"], t3) + body)

    # part pages + nav description
    meta = []
    for pi, part in enumerate(parts):
        meta.append({
            "part": pi + 1, "dir": PART_DIRS[pi], "title": part["title"], "scope": part["scope"],
            "chapters": [dict(num=c["num"], title=plain(c["title"]),
                              path=os.path.relpath(c["path"], DOCS).replace("\\", "/"))
                         for c in chapters if c["part"] == pi + 1],
        })
    json.dump(meta, open(os.path.join(ROOT, "tools", "structure.json"), "w"), indent=1, ensure_ascii=False)
    if not args.only:
        open(marker, "w").write("chapters generated from legacy/AQM1_PHS4102_Notes.tex\n")


if __name__ == "__main__":
    main()
