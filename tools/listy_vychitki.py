# -*- coding: utf-8 -*-
"""Контактные листы для вычитки картинок: python3.13 tools/listy_vychitki.py gg2

Картинка показана в том размере, в каком её увидит ребёнок на платформе
(карточка ~200 px, сцена ~400 px), под ней — имя файла и реальный размер.
Листы кладутся в docs/vychitka/kartinki/<курс>_listy/ (в git не идут,
пересобираются из media/).
"""
from PIL import Image, ImageDraw, ImageFont
import sys, os, math, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CELL, LAB, COLS, PER_SHEET = 250, 34, 6, 24

try:
    F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
except OSError:
    F = ImageFont.load_default()


def sheet(files, path, title):
    rows = math.ceil(len(files) / COLS)
    im = Image.new('RGB', (COLS * CELL + 20, rows * (CELL + LAB) + 50), (225, 228, 232))
    d = ImageDraw.Draw(im)
    d.text((10, 14), title, fill=(0, 0, 0), font=F)
    for i, f in enumerate(files):
        r, c = divmod(i, COLS)
        x, y = 10 + c * CELL, 40 + r * (CELL + LAB)
        d.rectangle([x, y, x + CELL - 6, y + CELL - 6], fill=(255, 255, 255), outline=(170, 175, 180))
        t = Image.open(f).convert('RGBA')
        bg = Image.new('RGBA', t.size, (255, 255, 255, 255))
        bg.alpha_composite(t)
        t = bg.convert('RGB')
        w, h = t.size
        disp = 400 if max(w, h) >= 700 else 200          # сцена / карточка
        nw, nh = int(w * disp / max(w, h)), int(h * disp / max(w, h))
        k = min((CELL - 14) / nw, (CELL - 14) / nh, 1.0)
        nw, nh = max(1, int(nw * k)), max(1, int(nh * k))
        im.paste(t.resize((nw, nh), Image.LANCZOS), (x + (CELL - 6 - nw) // 2, y + (CELL - 6 - nh) // 2))
        d.text((x + 4, y + CELL - 2), os.path.basename(f), fill=(10, 10, 10), font=F)
        d.text((x + 4, y + CELL + 13), f'{w}x{h}', fill=(90, 90, 90), font=F)
    im.save(path, quality=92)
    return path


def main(course):
    out = os.path.join(ROOT, 'docs/vychitka/kartinki', course + '_listy')
    os.makedirs(out, exist_ok=True)
    files = sorted(glob.glob(os.path.join(ROOT, 'media', course, '**', '*.webp'), recursive=True))
    groups = {}
    for f in files:
        groups.setdefault(os.path.basename(os.path.dirname(f)), []).append(f)
    for g, fl in sorted(groups.items()):
        for i in range(0, len(fl), PER_SHEET):
            n = i // PER_SHEET + 1
            print(sheet(fl[i:i + PER_SHEET], os.path.join(out, f'{course}_{g}_{n}.jpg'),
                        f'{course} / {g}  —  лист {n}'))


if __name__ == '__main__':
    main(sys.argv[1])
