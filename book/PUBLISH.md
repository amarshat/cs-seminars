# Publishing runbook (KDP)

The book is one combined free volume. This is the checklist and the paste-ready listing fields for Kindle Direct Publishing.

## Pre-flight checklist

- [ ] All planned seminars committed and gauntlet-clean (no open BLOCKER/MAJOR in `ignore/reviews`).
- [ ] Wide tables retrofitted so nothing squeezes on a reflowable Kindle.
- [ ] `make -C book epub` builds and `make -C book check` passes epubcheck with no errors.
- [ ] Cover present at `book/cover.png` (1600x2560). Regenerate with `python3 book/make_cover.py` after editing it.
- [ ] Rights pass done (see below).
- [ ] Opened the EPUB in Kindle Previewer and checked a phone size and an e-ink size: diagrams render as images, chapters break correctly, no clipped code or tables.
- [ ] Release `date` set in `book/metadata.yaml`.

## KDP listing fields (paste-ready)

- **Title:** CS-Seminars
- **Subtitle:** Reading the Classics of Computer Science
- **Author:** Amar Akshat
- **Language:** English
- **Description:** Some of the ideas that hold up your stack were written down decades ago: logical clocks, the relational model, supervision trees, replicated state machines, the transaction concept. The systems you ship this week are still arguments these papers started, but the papers themselves are hard to walk into. CS-Seminars is a set of modern graduate seminars on those foundational works. Each one reconstructs a classic paper, puts it back in its own time, and tests its ideas against the systems we build today. It reads the classics not as history but as answers to questions that never went away: how independent components coordinate, how a system stays correct when parts of it fail, where trust should live, and how to keep complexity survivable. Every chapter was written from the primary source and checked by an adversarial panel of domain experts, so the reconstructions are faithful and the modern comparisons are precise rather than decorative. Free, under a Creative Commons license.
- **Keywords (up to 7):** distributed systems; computer science classics; software architecture; consensus and replication; database transactions; fault tolerance; systems engineering
- **Categories (2):** Computers & Technology > Computer Science; Computers & Technology > Networking & Cloud Computing
- **DRM:** No (the commentary is CC BY 4.0).

## Making it free on Kindle

KDP's minimum list price is $0.99; you cannot set $0.00 directly. Use price-matching:

1. Publish the EPUB free somewhere public (GitHub Releases and/or your own site; optionally Smashwords, which distributes free).
2. List on KDP at $0.99.
3. Ask Amazon (via the KDP author help "report a lower price" flow) to price-match the Kindle edition to the free listing. They generally match to $0.00.
4. Do NOT enroll in KDP Select. Select requires Amazon exclusivity, which conflicts with offering the book free elsewhere.

## Rights pass (before publishing)

The book quotes the primary sources at length. Short quotations for transformative commentary are fair use, but do one deliberate pass:

- [ ] Every quoted passage is short relative to the source and clearly serves the surrounding commentary.
- [ ] Every quote is attributed inline, and every source has a full citation in its seminar's reading list.
- [ ] The copyright page states the CC BY 4.0 license for the commentary and the fair-use basis for the quotations.
- [ ] Consolidated bibliography assembled (or the per-seminar reading lists confirmed complete), since a published book is expected to carry full references.

## After launch

- Attach the EPUB to a tagged GitHub Release so the free copy has a stable home.
- If you correct anything, rebuild, re-run epubcheck, and upload the new EPUB to KDP; it propagates to buyers as an update.
