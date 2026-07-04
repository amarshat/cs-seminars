#!/usr/bin/env python3
"""Generate the Kindle cover (book/cover.png) with Pillow.

KDP wants a portrait cover around 1600x2560. This draws a clean typographic
cover: title, subtitle, a small supervision-tree motif, and the author. Edit the
constants below to taste, then run:  python3 book/make_cover.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 2560
INK = (16, 21, 28)
PAPER = (244, 241, 234)
GOLD = (214, 164, 65)
DIM = (120, 110, 88)

TITLE = "CS-Seminars"
SUBTITLE = "Reading the Classics of Computer Science"
KICKER = "MARGIN NOTES ON THE FOUNDATIONAL PAPERS"
AUTHOR = "Amar Akshat"

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "cover.png")

SANS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/SFNSDisplay.ttf",
]
SERIF = [
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
    "/System/Library/Fonts/Supplemental/Palatino.ttc",
]


def font(paths, size):
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def center(draw, y, text, fnt, fill, spacing=0):
    if spacing:
        widths = [draw.textlength(c, font=fnt) for c in text]
        total = sum(widths) + spacing * (len(text) - 1)
        x = (W - total) / 2
        for c, w in zip(text, widths):
            draw.text((x, y), c, font=fnt, fill=fill)
            x += w + spacing
    else:
        w = draw.textlength(text, font=fnt)
        draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)


def main():
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)

    # thin inset frame, manuscript feel
    d.rectangle([70, 70, W - 70, H - 70], outline=GOLD, width=4)

    center(d, 300, KICKER, font(SANS, 40), GOLD, spacing=8)
    center(d, 470, TITLE, font(SANS, 200), PAPER)
    center(d, 760, SUBTITLE, font(SERIF, 62), (210, 205, 194))

    # supervision-tree motif: root, two supervisors, four workers
    nodes = {
        "r": (800, 1180),
        "a": (600, 1420), "b": (1000, 1420),
        "w1": (470, 1680), "w2": (700, 1680),
        "w3": (900, 1680), "w4": (1130, 1680),
    }
    edges = [("r", "a"), ("r", "b"), ("a", "w1"), ("a", "w2"),
             ("b", "w3"), ("b", "w4")]
    for u, v in edges:
        d.line([nodes[u], nodes[v]], fill=DIM, width=4)
    for key, (x, y) in nodes.items():
        rad = 34 if key == "r" else 24
        d.ellipse([x - rad, y - rad, x + rad, y + rad], fill=GOLD, outline=INK, width=4)

    # authors band: the through-line, shown small
    band = "Armstrong  .  Hewitt  .  Hoare  .  Lamport  .  Liskov  .  Gray  .  and more"
    center(d, 2050, band, font(SERIF, 40), (170, 165, 152))

    d.line([(W / 2 - 140, 2300), (W / 2 + 140, 2300)], fill=GOLD, width=3)
    center(d, 2360, AUTHOR, font(SANS, 66), PAPER)

    img.save(OUT, "PNG")
    print("wrote %s (%dx%d)" % (OUT, W, H))


if __name__ == "__main__":
    main()
