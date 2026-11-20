#!/usr/bin/env python3
"""Build the news-image-20261120 entry: a one-page newspaper front page
summarising Friday 20 November 2026 world news. Deterministic, no network.
Draws everything with PIL shapes; writes entry.png (1024x1024)."""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
CARD = (255, 255, 255)
INK = (26, 26, 26)
NAVY = (20, 33, 61)
RED = (180, 35, 24)
GOLD = (176, 141, 60)
LINE = (200, 192, 175)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def star_points(cx, cy, r_out, r_in, n=5, rot=-90):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def make_art(w, h, bg, draw_fn):
    """Draw art on its own tile so nothing spills outside the art area."""
    tile = Image.new("RGB", (w, h), bg)
    td = ImageDraw.Draw(tile)
    draw_fn(td, w, h)
    return tile


def draw_scales(d, w, h):
    cx = w // 2
    top = 12
    base_y = h - 20
    d.rectangle([cx - 52, base_y, cx + 52, base_y + 10], fill=NAVY)
    d.rectangle([cx - 5, top + 18, cx + 5, base_y], fill=NAVY)
    d.ellipse([cx - 9, top + 6, cx + 9, top + 24], fill=GOLD)
    d.rectangle([cx - 108, top + 22, cx + 108, top + 28], fill=NAVY)
    for sgn in (-1, 1):
        px = cx + sgn * 92
        d.line([px, top + 28, px - 26, top + 66], fill=NAVY, width=3)
        d.line([px, top + 28, px + 26, top + 66], fill=NAVY, width=3)
        d.polygon([(px - 30, top + 66), (px + 30, top + 66), (px, top + 92)],
                  fill=GOLD, outline=NAVY)


def draw_flags(d, w, h):
    fw, fh = (w - 40) // 3, 62
    fy = (h - fh) // 2 - 4
    ux = 10
    for i in range(7):
        d.rectangle([ux, fy + i * fh // 7, ux + fw, fy + (i + 1) * fh // 7],
                    fill=RED if i % 2 == 0 else (255, 255, 255))
    d.rectangle([ux, fy, ux + fw * 2 // 5, fy + fh * 4 // 7], fill=NAVY)
    for r in range(3):
        for c in range(4):
            d.ellipse([ux + 6 + c * 13, fy + 6 + r * 12,
                       ux + 11 + c * 13, fy + 11 + r * 12], fill=(255, 255, 255))
    cx = ux + fw + 10
    d.rectangle([cx, fy, cx + fw, fy + fh], fill=(222, 41, 16))
    d.polygon(star_points(cx + 20, fy + 20, 13, 5), fill=(255, 222, 0))
    for sx, sy in ((cx + 44, fy + 11), (cx + 53, fy + 22), (cx + 51, fy + 36),
                   (cx + 40, fy + 43)):
        d.polygon(star_points(sx, sy, 5, 2), fill=(255, 222, 0))
    rx = cx + fw + 10
    d.rectangle([rx, fy, rx + fw, fy + fh // 3], fill=(255, 255, 255))
    d.rectangle([rx, fy + fh // 3, rx + fw, fy + 2 * fh // 3], fill=(0, 57, 166))
    d.rectangle([rx, fy + 2 * fh // 3, rx + fw, fy + fh], fill=(213, 0, 50))
    for fx in (ux, cx, rx):
        d.rectangle([fx, fy, fx + fw, fy + fh], outline=(120, 120, 120), width=1)


def draw_tower(d, w, h):
    cx = w // 2
    top, bot = 4, h - 6
    d.rectangle([0, bot - 22, w, bot], fill=(214, 205, 188))
    for bx, bw, bh in ((6, 34, 52), (w - 46, 40, 66), (w - 96, 30, 40)):
        d.rectangle([bx, bot - bh, bx + bw, bot], fill=(150, 142, 126))
    d.polygon([(cx - 42, bot), (cx - 30, top + 14), (cx + 26, top),
               (cx + 40, bot)], fill=(58, 84, 128))
    d.polygon([(cx - 30, top + 14), (cx + 26, top), (cx + 20, top + 20),
               (cx - 24, top + 32)], fill=(38, 58, 92))
    for i in range(4):
        yy = top + 38 + i * 12
        d.line([cx - 36, yy, cx + 36, yy], fill=(140, 170, 205), width=2)
    bx, by = cx + 4, top + 52
    d.polygon(star_points(bx, by, 26, 11, n=8), fill=(255, 140, 0))
    d.polygon(star_points(bx, by, 15, 6, n=8), fill=(255, 220, 0))
    for dx, dy in ((-16, 34), (16, 70), (-8, 76)):
        d.rectangle([cx + dx, top + dy, cx + dx + 10, top + dy + 7], fill=(20, 20, 20))
    d.rectangle([cx - 48, bot - 4, cx + 48, bot], fill=NAVY)


def draw_cyclone(d, w, h):
    cx, cy = w // 2 - 30, h // 2 - 4
    d.rectangle([0, h - 26, w, h], fill=(70, 130, 180))
    d.rectangle([0, h - 31, w, h - 26], fill=(222, 200, 150))
    for r, a0, a1, col in ((44, 20, 300, (90, 120, 160)),
                           (33, 80, 340, (70, 100, 145)),
                           (22, 140, 20, (50, 80, 125)),
                           (12, 200, 60, (35, 60, 105))):
        d.arc([cx - r, cy - r, cx + r, cy + r], a0, a1, fill=col, width=5)
    d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=(35, 60, 105))
    for rx in range(10, w - 6, 22):
        d.line([rx, 8, rx - 5, 22], fill=(90, 120, 160), width=3)
    for hx in (w - 62, w - 38):
        d.rectangle([hx, h - 48, hx + 16, h - 31], fill=(180, 60, 40))
        d.polygon([(hx - 2, h - 48), (hx + 8, h - 57), (hx + 18, h - 48)],
                  fill=NAVY)


def draw_chart(d, w, h):
    base = h - 16
    bars = [20, 30, 26, 40, 36, 52]
    bw = (w - 30) // len(bars)
    cols = [(120, 150, 190), (90, 125, 175), (120, 150, 190),
            (70, 105, 160), (46, 82, 140), (20, 60, 110)]
    for i, bh in enumerate(bars):
        bx = 16 + i * bw
        d.rectangle([bx, base - bh, bx + bw - 8, base], fill=cols[i])
    pts = [(16, base - 20), (16 + 2 * bw, base - 30),
           (16 + 3 * bw, base - 26), (w - 20, base - 52)]
    d.line(pts, fill=RED, width=4)
    ax, ay = w - 20, base - 52
    d.polygon([(ax, ay), (ax - 16, ay + 2), (ax - 3, ay + 13)], fill=RED)
    d.line([8, base, w - 8, base], fill=NAVY, width=3)
    d.text((14, 4), "+17%", font=font(SANS_B, 22), fill=RED)
    d.text((w - 14, 4), "$1.8T", font=font(SANS_B, 22), fill=NAVY, anchor="ra")


ART_BG = (255, 255, 255)


def panel(img, x, y, w, h, kicker, headline, summary, art_fn, bg):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD,
                        outline=LINE, width=2)
    art_h = 96
    tile = make_art(w - 4, art_h, bg, art_fn)
    img.paste(tile, (x + 2, y + 2))
    d.line([x + 14, y + art_h + 10, x + w - 14, y + art_h + 10], fill=LINE, width=1)
    ty = y + art_h + 18
    d.text((x + 16, ty), kicker, font=font(SANS_B, 15), fill=RED)
    ty += 23
    hf = font(SERIF_B, 24)
    for ln in wrap(d, headline, hf, w - 32):
        d.text((x + 16, ty), ln, font=hf, fill=INK)
        ty += 30
    ty += 2
    sf = font(SANS, 17)
    for ln in wrap(d, summary, sf, w - 32):
        d.text((x + 16, ty), ln, font=sf, fill=(60, 60, 60))
        ty += 22


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 152], fill=GOLD)
    d.text((W // 2, 14), "THE WORLD TODAY", font=font(SANS_B, 22),
           fill=GOLD, anchor="ma")
    d.text((W // 2, 42), "FRIDAY 20 NOVEMBER 2026", font=font(SERIF_B, 58),
           fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 112), "Six stories that defined the day  •  From The Hague to Shenzhen",
           font=font(SANS, 20), fill=(200, 210, 230), anchor="ma")

    # ---- Lead story: ICJ Rohingya ruling ----
    lx, ly, lw, lh = 24, 164, 976, 232
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=10, fill=CARD,
                        outline=LINE, width=2)
    tile = make_art(300, lh - 4, (222, 232, 240), draw_scales)
    img.paste(tile, (lx + 2, ly + 2))
    tx = lx + 330
    d.text((tx, ly + 18), "THE HAGUE  •  TOP STORY", font=font(SANS_B, 16), fill=RED)
    hf = font(SERIF_B, 36)
    ty = ly + 46
    for ln in wrap(d, "UN COURT: MYANMAR COMMITTED GENOCIDE", hf, lw - 330 - 24):
        d.text((tx, ty), ln, font=hf, fill=INK)
        ty += 43
    ty += 4
    sf = font(SANS, 20)
    summary = ("The International Court of Justice rules Myanmar committed "
               "genocide against the Rohingya in its 2017 campaign — the "
               "court's first such finding against a state.")
    for ln in wrap(d, summary, sf, lw - 330 - 24):
        d.text((tx, ty), ln, font=sf, fill=(60, 60, 60))
        ty += 27

    # ---- Rows of two panels ----
    pw, ph = 476, 244
    panel(img, 24, 406, pw, ph, "SHENZHEN  •  DIPLOMACY",
          "TRUMP, XI AND PUTIN MEET",
          "First three-way summit ends with a four-point peace "
          "declaration, including nuclear disarmament talks.",
          draw_flags, (255, 255, 255))
    panel(img, 524, 406, pw, ph, "RIYADH  •  CONFLICT",
          "MISSILE HITS RIYADH'S TALLEST TOWER",
          "Suspected Houthi strike damages the PIF Tower, home of "
          "Saudi Arabia's $900bn fund. No injuries.",
          draw_tower, (238, 238, 232))
    panel(img, 24, 662, pw, ph, "ODISHA, INDIA  •  WEATHER",
          "CYCLONE AKVAN STRIKES EAST COAST",
          "Landfall near Gopalpur with gusts to 90 km/h and heavy "
          "rain; more than 300,000 people evacuated.",
          draw_cyclone, (208, 226, 240))
    panel(img, 524, 662, pw, ph, "WALL STREET  •  MARKETS",
          "ANTHROPIC'S RECORD IPO SOARS 17%",
          "The AI firm's $81.3bn listing — the largest ever — "
          "values it at about $1.8 trillion on debut.",
          draw_chart, (255, 255, 255))

    # ---- Footer: also today ----
    fy = 918
    d.rectangle([0, fy, W, H], fill=NAVY)
    d.text((24, fy + 12), "ALSO TODAY", font=font(SANS_B, 18), fill=GOLD)
    ff = font(SANS, 18)
    d.text((24, fy + 38),
           "S&P 500 falls 2%, a fifth straight loss  •  Europe ready for talks "
           "with Russia on Ukraine",
           font=ff, fill=(225, 230, 240))
    d.text((24, fy + 64),
           "COP31 climate talks enter final days in Antalya  •  13,000 protest "
           "in Tokyo",
           font=ff, fill=(225, 230, 240))

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
