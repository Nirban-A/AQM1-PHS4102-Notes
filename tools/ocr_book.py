"""OCR a scanned PDF page by page with tesseract (run inside the claudeProject conda env).

Usage: python tools/ocr_book.py BOOK.pdf OUT_DIR [--first N] [--last N] [--dpi 300] [--jobs 4]

Writes OUT_DIR/page_0001.txt ... and OUT_DIR/all.txt (pages separated by a marker line).
Resumable: pages whose txt file already exists are skipped.
"""
import argparse
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor

import pymupdf

TESS = os.path.join(sys.prefix, "Library", "bin", "tesseract.exe")
TESSDATA = os.path.join(sys.prefix, "share", "tessdata")


def ocr_page(args):
    pdf, n, out_dir, dpi = args
    out = os.path.join(out_dir, f"page_{n:04d}.txt")
    if os.path.exists(out):
        return n
    with pymupdf.open(pdf) as doc, tempfile.TemporaryDirectory() as tmp:
        img = os.path.join(tmp, "p.png")
        doc[n - 1].get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY).save(img)
        env = dict(os.environ, TESSDATA_PREFIX=TESSDATA, OMP_THREAD_LIMIT="1")
        res = subprocess.run(
            [TESS, img, "stdout", "-l", "eng", "--psm", "6"],
            capture_output=True, env=env,
        )
    with open(out, "w", encoding="utf-8") as f:
        f.write(res.stdout.decode("utf-8", errors="replace"))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("out_dir")
    ap.add_argument("--first", type=int, default=1)
    ap.add_argument("--last", type=int, default=0)
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()

    os.makedirs(a.out_dir, exist_ok=True)
    with pymupdf.open(a.pdf) as doc:
        total = len(doc)
    last = a.last or total
    pages = range(a.first, last + 1)
    tasks = [(a.pdf, n, a.out_dir, a.dpi) for n in pages]
    done = 0
    with ProcessPoolExecutor(a.jobs) as ex:
        for _ in ex.map(ocr_page, tasks):
            done += 1
            if done % 25 == 0 or done == len(tasks):
                print(f"{done}/{len(tasks)} pages", flush=True)

    with open(os.path.join(a.out_dir, "all.txt"), "w", encoding="utf-8") as f:
        for n in range(1, total + 1):
            p = os.path.join(a.out_dir, f"page_{n:04d}.txt")
            if os.path.exists(p):
                f.write(f"\n=== PAGE {n} ===\n")
                f.write(open(p, encoding="utf-8").read())


if __name__ == "__main__":
    main()
