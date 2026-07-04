# Building the ebook

This directory turns the seminar Markdown into a single reflowable EPUB for Kindle. The same Markdown still serves the GitBook web version; nothing here changes the source chapters.

## What it produces

One combined volume, *CS-Seminars: Reading the Classics of Computer Science*, with each seminar as a part and each chapter starting a new page. Diagrams are rasterized to PNG (Kindle cannot run Mermaid). Cross-chapter links become internal anchors.

## Prerequisites

- **pandoc** (`brew install pandoc`) - Markdown to EPUB3.
- **mermaid-cli** (`npm install -g @mermaid-js/mermaid-cli`) - provides `mmdc`, renders diagrams. Without it the build still runs but leaves diagram placeholders.
- **epubcheck** (`brew install epubcheck`), optional - validates the EPUB before you upload it.

## Build

From the repo root:

```
make -C book epub      # produces book/build/cs-seminars.epub
make -C book check      # runs epubcheck on it
make -C book clean      # removes build output
```

The build reads chapter order from the top-level `SUMMARY.md`, so a new seminar is picked up automatically once it is listed there.

## How it works

`preprocess.py` assembles `book/build/book.md`: front matter, then every chapter in `SUMMARY.md` order, with Mermaid blocks rendered to `book/build/img/*.png` and `NN-file.md` links rewritten to `#anchors`. The Makefile then runs pandoc with `metadata.yaml`, `epub.css`, and the cover. Build output under `book/build/` is gitignored.

## Still to do before publishing

- **Cover.** KDP requires one. Drop a `book/cover.png` here (ideal 1600x2560, JPG or PNG). A clean typographic cover is fine. Until it exists the build simply omits the cover.
- **Wide-table pass.** A few existing chapters use three- or four-column comparison tables (Armstrong ch6 and ch7, Hoare ch6, Liskov ch6). On a reflowable Kindle these get squeezed. Either narrow them, turn them into prose or definition lists, or render them as images. Going forward the Kindle-ready rule and the Ebook/Production reviewer keep new chapters clean.
- **Bibliography.** Consolidate the per-seminar reading lists into one references section at the back, with full citations.
- **Rights pass.** The book quotes the primary sources at length. Short quotes for transformative commentary are fair use, but do one pass to confirm each quote is scoped and attributed, and that every source has a full citation.
- **KDP metadata.** Title, subtitle, author, description (from `metadata.yaml`), up to 7 keywords, 2 categories (Computers & Technology). Fill the release `date` in `metadata.yaml`.

## Making it actually free on Kindle

KDP's minimum price is $0.99; you cannot set $0.00 directly. Two real paths:

1. **Price-match to free (recommended).** Publish the EPUB free somewhere public (GitHub Releases, your own site, Smashwords), then ask Amazon to price-match the Kindle edition to $0.00. This keeps it free everywhere and needs no exclusivity.
2. **KDP Select free-promo days.** Five free days per 90-day enrollment, but Select requires Amazon exclusivity, so you could not also offer the EPUB free elsewhere.

Given the CC BY license and the goal of a free book, path 1 fits best: ship the EPUB free from the repo's Releases and let Amazon match it.
