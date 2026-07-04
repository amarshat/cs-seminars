#!/usr/bin/env python3
"""Assemble the CS-Seminars chapters into one Kindle-ready Markdown file.

Pipeline:
  1. Read SUMMARY.md for chapter order (skips the root README; the preface
     replaces it).
  2. Prepend the front matter (copyright, preface).
  3. Render every ```mermaid block to a PNG via mermaid-cli (mmdc) and swap in
     an image reference. If mmdc is not installed, keep a visible placeholder
     plus the source and warn, so the build still completes.
  4. Give each source file a stable anchor id and rewrite cross-file
     [text](NN-file.md) links to internal #anchors.
  5. Write the combined Markdown to book/build/book.md for pandoc.

Run from the repo root:  python3 book/preprocess.py
Requires: python3 (stdlib only). For diagrams: mermaid-cli (mmdc), installed
via `npm install -g @mermaid-js/mermaid-cli`.
"""
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "book", "build")
IMGDIR = os.path.join(BUILD, "img")
OUT = os.path.join(BUILD, "book.md")
FRONT = [
    os.path.join(ROOT, "book", "frontmatter", "00-copyright.md"),
    os.path.join(ROOT, "book", "frontmatter", "01-preface.md"),
]
BACK = [
    os.path.join(ROOT, "book", "backmatter", "98-about.md"),
]
MMDC = shutil.which("mmdc")
LINK_RE = re.compile(r"\]\(([^)]+\.md)(?:#[^)]*)?\)")
MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.S)


def slug(path):
    rel = os.path.relpath(path, ROOT)[:-3]  # drop .md
    return re.sub(r"[^a-z0-9]+", "-", rel.lower()).strip("-")


def chapters_from_summary():
    files = []
    with open(os.path.join(ROOT, "SUMMARY.md")) as f:
        for line in f:
            m = re.search(r"-\s*\[[^\]]*\]\(([^)]+\.md)\)", line)
            if not m:
                continue
            p = os.path.normpath(os.path.join(ROOT, m.group(1)))
            if os.path.basename(p) == "README.md" and os.path.dirname(p) == ROOT:
                continue  # root README; the preface replaces it
            files.append(p)
    return files


FENCE_RE = re.compile(r"^(```|~~~)")
HEAD_RE = re.compile(r"^(#{1,6})(\s.*)$")


def shift_headings(md, keep_first_h1):
    """Push every heading down one level, skipping fenced code. If keep_first_h1,
    the first heading (a seminar or section title) stays put and becomes a
    top-level TOC entry, with everything under it nested below."""
    out, in_fence, seen = [], False, False
    for ln in md.split("\n"):
        if FENCE_RE.match(ln):
            in_fence = not in_fence
            out.append(ln)
            continue
        m = None if in_fence else HEAD_RE.match(ln)
        if m:
            if keep_first_h1 and not seen:
                out.append(ln)
            else:
                h = m.group(1)
                out.append((h + "#" if len(h) < 6 else h) + m.group(2))
            seen = True
        else:
            out.append(ln)
    return "\n".join(out)


def render_mermaid(md, src):
    counter = [0]

    def repl(m):
        counter[0] += 1
        code = m.group(1)
        name = "%s-%d.png" % (slug(src), counter[0])
        out_png = os.path.join(IMGDIR, name)
        if MMDC:
            mmd = os.path.join(IMGDIR, name + ".mmd")
            with open(mmd, "w") as fh:
                fh.write(code)
            # neutral theme + white background render legibly in grayscale;
            # scale up so the raster is crisp on high-dpi Kindles.
            subprocess.run(
                [MMDC, "-i", mmd, "-o", out_png, "-b", "white",
                 "-t", "neutral", "-s", "3"],
                check=True,
            )
            os.remove(mmd)
            return "\n![Diagram](img/%s)\n" % name
        sys.stderr.write("WARN mmdc not found; diagram left as placeholder in %s\n"
                         % os.path.relpath(src, ROOT))
        return "\n> Diagram (install mermaid-cli to render):\n>\n> ```\n%s```\n" % code

    return MERMAID_RE.sub(repl, md)


def main():
    os.makedirs(IMGDIR, exist_ok=True)
    sources = FRONT + chapters_from_summary() + BACK
    idmap = {os.path.normpath(s): slug(s) for s in sources}
    front_back = {os.path.normpath(p) for p in FRONT + BACK}
    parts = []
    for s in sources:
        with open(s) as f:
            md = f.read()
        sid = idmap[os.path.normpath(s)]
        # Nest the TOC: seminar READMEs and front/back keep their title at the top
        # level; chapters demote by one so the chapter title becomes an H2 under
        # its seminar. A depth-2 TOC then shows chapters nested under seminars.
        keep_h1 = (os.path.basename(s) == "README.md"
                   or os.path.normpath(s) in front_back)
        md = shift_headings(md, keep_h1)
        # attach a stable id to the first heading (any level) so links can target it
        md = re.sub(r"^(#{1,6}\s+.+?)\s*$", r"\1 {#" + sid + "}", md, count=1, flags=re.M)
        base = os.path.dirname(s)

        def rewrite_link(m, _base=base, _src=s):
            tgt = os.path.normpath(os.path.join(_base, m.group(1)))
            if tgt in idmap:
                return "](#%s)" % idmap[tgt]
            sys.stderr.write("WARN unresolved link %s in %s\n"
                             % (m.group(1), os.path.relpath(_src, ROOT)))
            return m.group(0)

        md = LINK_RE.sub(rewrite_link, md)
        md = render_mermaid(md, s)
        parts.append(md)

    with open(OUT, "w") as f:
        f.write("\n\n".join(parts))
    print("wrote %s (%d sections, mmdc=%s)" % (OUT, len(sources), bool(MMDC)))


if __name__ == "__main__":
    main()
