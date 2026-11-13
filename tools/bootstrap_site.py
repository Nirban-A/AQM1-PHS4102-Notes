#!/usr/bin/env python3
"""One-off: write mkdocs.yml, the home page and the part index pages from
tools/structure.json (produced by convert_tex.py). Safe to re-run; it only
overwrites those generated files, never the chapter pages."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open(os.path.join(ROOT, "tools", "structure.json"), encoding="utf-8"))
ROMAN = ["I", "II", "III", "IV", "V", "VI"]

def tex_text(s):
    s = s.replace("\\textbf{***}", "***")
    s = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", s)
    s = s.replace('\\"o', "ö").replace("\\'e", "é").replace("$\\tfrac12$", "½")
    s = re.sub(r"\$([^$]*)\$", lambda m: "$" + m.group(1) + "$", s)
    s = s.replace("~", " ")
    return s.strip()

part_titles = {m["part"]: m["title"] for m in meta}

# part index pages
for m in meta:
    p = os.path.join(ROOT, "docs", m["dir"], "index.md")
    lines = ["---\ntitle: \"Part %s: %s\"\n---\n" % (ROMAN[m["part"] - 1], m["title"]),
             "# Part %s: %s\n" % (ROMAN[m["part"] - 1], m["title"]), tex_text(m["scope"]) + "\n", "## Chapters\n"]
    for c in m["chapters"]:
        lines.append("%d. [%s](%s)" % (c["num"], c["title"], os.path.basename(c["path"])))
    open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")

# nav
nav = ["nav:", "  - Home: index.md"]
for m in meta:
    nav.append("  - \"Part %s: %s\":" % (ROMAN[m["part"] - 1], m["title"]))
    nav.append("    - Overview: %s/index.md" % m["dir"])
    for c in m["chapters"]:
        nav.append("    - \"%d. %s\": %s" % (c["num"], c["title"].replace('"', "'"), c["path"]))

cfg = """site_name: Advanced Quantum Mechanics I (PHS 4102)
site_description: Complete lecture notes and worked problems for Advanced Quantum Mechanics I (PHS 4102)
site_url: https://nirban-a.github.io/AQM1-PHS4102-Notes/
repo_url: https://github.com/nirban-a/AQM1-PHS4102-Notes
repo_name: nirban-a/AQM1-PHS4102-Notes
edit_uri: edit/main/docs/

theme:
  name: material
  custom_dir: overrides
  language: en
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: teal
      toggle:
        icon: material/weather-night
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: teal
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.top
    - navigation.footer
    - navigation.indexes
    - toc.follow
    - search.suggest
    - search.highlight
    - content.action.edit

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.arithmatex:
      generic: true
  - attr_list
  - md_in_html
  - tables
  - footnotes
  - toc:
      permalink: true
      toc_depth: 3

extra_javascript:
  - javascripts/mathjax.js
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

extra_css:
  - stylesheets/extra.css

exclude_docs: |
  assets/figures/*.pdf

""" + "\n".join(nav) + "\n"
open(os.path.join(ROOT, "mkdocs.yml"), "w", encoding="utf-8").write(cfg)

# home page
home = ["# Advanced Quantum Mechanics I (PHS 4102)\n",
        "Complete lecture notes and worked problems, converted from the handwritten lecture notebook and arranged in five parts.\n",
        "Items in coloured boxes marked as *Complete Solution*, *Intuition*, *Study Note*, *Memory Rule*, *Exam Tip*, *Verification* and *Common mistakes* are additions that were not written out in the notebook.\n",
        "<a class=\"md-button md-button--primary\" href=\"pdf/AQM1_PHS4102_Notes.pdf\">Download the full notes (PDF)</a>\n",
        "## Contents\n"]
for m in meta:
    home.append("### [Part %s: %s](%s/index.md)\n" % (ROMAN[m["part"] - 1], m["title"], m["dir"]))
    for c in m["chapters"]:
        home.append("%d. [%s](%s)" % (c["num"], c["title"], c["path"]))
    home.append("")
open(os.path.join(ROOT, "docs", "index.md"), "w", encoding="utf-8").write("\n".join(home) + "\n")
