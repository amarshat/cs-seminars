#!/usr/bin/env python3
"""Generate the Kindle cover (book/cover.png) with Pillow.

KDP wants a portrait cover around 1600x2560. This draws a bold typographic cover:
the title "Still Running" over a small constellation of connected ideas (the
book's through-line), with the subtitle and author. Edit the constants and run:
python3 book/make_cover.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 2560
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cover.png")

TITLE = ("STILL", "RUNNING")
SUB = "How the Classic Papers of Computer Science Explain the Systems We Build Today"
KICKER = "A CS-SEMINARS BOOK"
AUTHOR = "AMAR AKSHAT"

BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
SERIF = "/System/Library/Fonts/NewYork.ttf"
REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

GOLD = (240, 180, 40)
PAPER = (245, 243, 236)


def font(path, size):
    for p in (path, BOLD, REG):
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def center(d, y, text, fnt, fill, track=0):
    if track:
        ws = [d.textlength(c, font=fnt) for c in text]
        x = (W - (sum(ws) + track * (len(text) - 1))) / 2
        for c, w in zip(text, ws):
            d.text((x, y), c, font=fnt, fill=fill)
            x += w + track
    else:
        d.text(((W - d.textlength(text, font=fnt)) / 2, y), text, font=fnt, fill=fill)


def wrap(d, text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def gradient(top, bot):
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3))
        for x in range(W):
            px[x, y] = c
    return img


def main():
    img = gradient((26, 20, 64), (6, 8, 16))   # indigo to near-black
    d = ImageDraw.Draw(img)

    center(d, 250, KICKER, font(BOLD, 40), GOLD, track=10)
    center(d, 470, TITLE[0], font(BLACK, 240), PAPER)
    center(d, 760, TITLE[1], font(BLACK, 240), PAPER)
    d.line([(W / 2 - 300, 1080), (W / 2 + 300, 1080)], fill=GOLD, width=4)
    for i, ln in enumerate(wrap(d, SUB, font(SERIF, 52), 1180)):
        center(d, 1140 + i * 66, ln, font(SERIF, 52), (206, 210, 230))

    # constellation of connected ideas: the through-line
    nodes = [
        (300, 1500), (520, 1720), (760, 1560), (980, 1780), (1180, 1560),
        (1320, 1820), (440, 1980), (700, 2020), (960, 2000), (1180, 2020),
        (820, 1400), (560, 1420),
    ]
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 6), (1, 7),
             (3, 8), (5, 9), (2, 10), (10, 4), (11, 0), (11, 2), (6, 7), (8, 9)]
    for a, b in edges:
        d.line([nodes[a], nodes[b]], fill=(70, 78, 120), width=3)
    for i, (x, y) in enumerate(nodes):
        r = 30 if i % 4 == 0 else 20
        col = GOLD if i % 4 == 0 else (150, 170, 220)
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)

    center(d, 2360, AUTHOR, font(BOLD, 60), PAPER, track=6)
    img.save(OUT, "PNG")
    print("wrote %s (%dx%d)" % (OUT, W, H))


if __name__ == "__main__":
    main()
