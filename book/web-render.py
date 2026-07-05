#!/usr/bin/env python3
"""Stage the Honkit web source into book/web-src.

Copies the root README.md and SUMMARY.md, book.json, and every seminar folder
(NN-*) into book/web-src, rendering each ```mermaid block to a PNG so Honkit needs
no browser plugin. Run from the repo root:  python3 book/web-render.py

Requires python3 (stdlib) and, for diagrams, mermaid-cli (mmdc). Without mmdc the
diagrams are left as code blocks and a warning is printed.
"""
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "book", "web-src")
MMDC = shutil.which("mmdc")
PUPPET = os.path.join(ROOT, "book", "puppeteer.json")
MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.S)


def render_mermaid(text, imgdir, stem):
    n = [0]

    def repl(m):
        n[0] += 1
        name = "%s-%d.png" % (stem, n[0])
        os.makedirs(imgdir, exist_ok=True)
        out_png = os.path.join(imgdir, name)
        mmd = out_png + ".mmd"
        with open(mmd, "w") as f:
            f.write(m.group(1))
        cmd = [MMDC, "-i", mmd, "-o", out_png, "-b", "white", "-t", "neutral", "-s", "3"]
        if os.path.exists(PUPPET):
            cmd += ["-p", PUPPET]
        subprocess.run(cmd, check=True)
        os.remove(mmd)
        return "\n![Diagram](img/%s)\n" % name

    return MERMAID_RE.sub(repl, text)


def stage(src_path, dst_path):
    with open(src_path) as f:
        text = f.read()
    if MERMAID_RE.search(text):
        if MMDC:
            stem = os.path.splitext(os.path.basename(src_path))[0]
            text = render_mermaid(text, os.path.join(os.path.dirname(dst_path), "img"), stem)
        else:
            sys.stderr.write("WARN mmdc not found; diagrams left as code in %s\n"
                             % os.path.relpath(src_path, ROOT))
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, "w") as f:
        f.write(text)


def main():
    if os.path.exists(SRC):
        shutil.rmtree(SRC)
    os.makedirs(SRC)
    for fn in ("README.md", "SUMMARY.md"):
        stage(os.path.join(ROOT, fn), os.path.join(SRC, fn))
    shutil.copy(os.path.join(ROOT, "book", "book.json"), os.path.join(SRC, "book.json"))
    for d in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, d)
        if os.path.isdir(p) and re.match(r"\d\d-", d):
            for fn in os.listdir(p):
                if fn.endswith(".md"):
                    stage(os.path.join(p, fn), os.path.join(SRC, d, fn))
    print("staged web source -> %s (mmdc=%s)" % (SRC, bool(MMDC)))


if __name__ == "__main__":
    main()
