# CS-Seminars ebook build.
# Run from the repo root:  make -C book epub
#
# Prereqs:
#   pandoc            (brew install pandoc)
#   mermaid-cli       (npm install -g @mermaid-js/mermaid-cli)  -> provides mmdc
#   epubcheck         (brew install epubcheck)  optional, for validation

ROOT   := ..
BUILD  := build
EPUB   := $(BUILD)/cs-seminars.epub
COVER  := cover.png

.PHONY: epub check clean

epub: $(BUILD)/book.md
	cd $(ROOT) && pandoc book/$(BUILD)/book.md \
	  --metadata-file=book/metadata.yaml \
	  --css=book/epub.css \
	  --toc --toc-depth=1 \
	  $(if $(wildcard $(COVER)),--epub-cover-image=book/$(COVER),) \
	  -o book/$(EPUB)
	@echo "built book/$(EPUB)"

$(BUILD)/book.md:
	cd $(ROOT) && python3 book/preprocess.py

check: epub
	epubcheck $(EPUB)

clean:
	rm -rf $(BUILD)
