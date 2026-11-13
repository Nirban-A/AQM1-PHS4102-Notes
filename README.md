# AQM1-PHS4102-Notes

Lecture notes for **Advanced Quantum Mechanics I (PHS 4102)**: 39 chapters in five parts, converted from the handwritten notebook, with completed solutions, intuition, study notes and exam tips added.

Live site: <https://nirban-a.github.io/AQM1-PHS4102-Notes/>

## How it works

- Every chapter is one Markdown file in `docs/NN-part-name/NN-chapter-name.md`. Math is LaTeX between `$...$` (inline) and `$$...$$` (display).
- Edit any chapter (on GitHub, in the browser, or locally) and push to `main`. The GitHub Actions workflow rebuilds the site and **all PDFs** (one per chapter plus the full book), so the "Download PDF" buttons always give the latest text.
- The original LaTeX notes and PDF are kept in `legacy/` for reference.

## One-time GitHub setup

1. Create the repository `AQM1-PHS4102-Notes` and push this folder to the `main` branch.
2. In the repository go to **Settings > Pages** and set **Source** to **GitHub Actions**.
3. Push (or run the workflow from the **Actions** tab). The site appears at the URL above after a few minutes.

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve                      # http://127.0.0.1:8000
```

Equations load MathJax from a CDN, so the preview needs internet access.

## Building the PDFs locally

Needs `pandoc` (3.1 or newer) and a LaTeX installation (pdflatex with tcolorbox, pgf, fancyhdr, enumitem).

```bash
python tools/build_pdfs.py --all          # all chapters + full book -> build/pdf/
python tools/build_pdfs.py --chapter 20   # one chapter
python tools/build_pdfs.py --full         # the full book only
```

## Layout

| Path | Contents |
|---|---|
| `docs/` | The chapters (Markdown), part overview pages, figures (`assets/figures/`), CSS and MathJax config |
| `overrides/main.html` | Adds the PDF download buttons to every chapter page |
| `tools/build_pdfs.py` | Markdown to PDF (pandoc + LaTeX), used by the workflow |
| `tools/convert_tex.py` | One-off converter that produced the chapters from `legacy/`. It refuses to run again unless forced |
| `ToTakeCareLater.md` | Known overlaps and planned clean-ups |
| `CLAUDE.md` | Conventions for editing the notes (also read by Claude Code) |
