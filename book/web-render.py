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
STATIC = os.path.join(ROOT, "book", "web-static")
MMDC = shutil.which("mmdc")
PUPPET = os.path.join(ROOT, "book", "puppeteer.json")
MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.S)

# Public base URL of the deployed GitHub Pages site. Used for sitemap.xml and
# robots.txt so Google can crawl and index every seminar page.
BASE_URL = "https://amarshat.github.io/cs-seminars/"
# Matches the markdown links in SUMMARY.md, e.g. [1. The problem](path/to/file.md).
SUMMARY_LINK_RE = re.compile(r"\]\(([^)]+\.md)\)")


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


def md_to_url(rel):
    """Map a SUMMARY.md link target to its built Honkit URL, relative to BASE_URL.

    Honkit renders README.md -> index.html in its own directory, and any other
    foo.md -> foo.html.
    """
    rel = rel.lstrip("./")
    if rel == "README.md":
        return ""
    if rel.endswith("/README.md"):
        return rel[: -len("README.md")] + "index.html"
    return rel[:-3] + ".html" if rel.endswith(".md") else rel


def build_sitemap():
    """Generate sitemap.xml from the page list in SUMMARY.md."""
    with open(os.path.join(ROOT, "SUMMARY.md")) as f:
        targets = SUMMARY_LINK_RE.findall(f.read())
    seen, urls = set(), []
    for t in targets:
        u = BASE_URL + md_to_url(t)
        if u not in seen:
            seen.add(u)
            urls.append(u)
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lines.append("  <url><loc>%s</loc></url>" % u)
    lines.append("</urlset>\n")
    with open(os.path.join(SRC, "sitemap.xml"), "w") as f:
        f.write("\n".join(lines))
    return len(urls)


def copy_static():
    """Copy committed static assets (Google verification, robots.txt) into SRC root."""
    if not os.path.isdir(STATIC):
        return
    for fn in os.listdir(STATIC):
        shutil.copy(os.path.join(STATIC, fn), os.path.join(SRC, fn))


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
    copy_static()
    n = build_sitemap()
    print("staged web source -> %s (mmdc=%s, sitemap urls=%d)" % (SRC, bool(MMDC), n))


if __name__ == "__main__":
    main()
