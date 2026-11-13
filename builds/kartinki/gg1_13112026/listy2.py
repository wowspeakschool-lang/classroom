# -*- coding: utf-8 -*-
"""Два составных листа GG1 из сгенерированных картинок (13.11.2026).

u8/four_trees  — четыре дерева по временам года, под каждым поле под кружок hotspot
u5/fruits_dance — две сцены с номерами 1 и 2 (как в тексте задания)

python3.13 builds/kartinki/gg1_13112026/listy2.py
"""
import os, sys
from PIL import Image, ImageChops, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'builds', 'kartinki', 'gg1_12112026'))
from listy import podgotovit            # отбеливание фона заливкой от краёв + обрезка

SYR = os.path.join(ROOT, 'builds', 'kartinki', 'gg1_13112026', 'syrye')
OUT = os.path.join(ROOT, 'builds', 'kartinki', 'gg1_13112026', 'listy')
os.makedirs(OUT, exist_ok=True)
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def otbelit_fon(im, porog=238):
    """Сплошное добеливание светлого фона.

    Для деревьев безопасно: светло-серых деталей в них нет, а у части
    картинок фон уходит в бледно-серый прямоугольник, который заливка
    от краёв не достаёт.
    """
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            if min(r, g, b) >= porog:
                px[x, y] = (255, 255, 255)
    bg = Image.new('RGB', im.size, 'white')
    bbox = ImageChops.difference(im, bg).convert('L').point(lambda v: 255 if v > 8 else 0).getbbox()
    return im.crop(bbox) if bbox else im


def derevya(cell=520, gap=90, polka=120):
    """2×2, под каждым деревом белая полка под кружок с подписью."""
    files = ['u8__tree_spring', 'u8__tree_summer', 'u8__tree_autumn', 'u8__tree_winter']
    w = gap + 2 * (cell + gap)
    row = cell + polka
    h = gap + 2 * (row + gap)
    sheet = Image.new('RGB', (w, h), 'white')
    tochki = []
    for i, f in enumerate(files):
        im = otbelit_fon(podgotovit(os.path.join('builds/kartinki/gg1_13112026/syrye', f + '.png')))
        im.thumbnail((cell, cell), Image.LANCZOS)
        x0 = gap + (i % 2) * (cell + gap)
        y0 = gap + (i // 2) * (row + gap)
        sheet.paste(im, (x0 + (cell - im.width) // 2, y0 + (cell - im.height)))
        tochki.append((round(100 * (x0 + cell / 2) / w, 1),
                       round(100 * (y0 + cell + polka * 0.45) / h, 1)))
    return sheet, tochki


def fruty_tanec(cell=620, gap=70, shapka=110):
    """Две сцены в ряд, над каждой номер — как в тексте задания (1 и 2)."""
    files = ['u5__fd_fruit_stall_v2', 'u5__fd_dancing_couple']
    w = gap + 2 * (cell + gap)
    h = shapka + cell + gap
    sheet = Image.new('RGB', (w, h), 'white')
    d = ImageDraw.Draw(sheet)
    font = ImageFont.truetype(FONT, 72)
    for i, f in enumerate(files):
        im = podgotovit(os.path.join('builds/kartinki/gg1_13112026/syrye', f + '.png'))
        im.thumbnail((cell, cell), Image.LANCZOS)
        x0 = gap + i * (cell + gap)
        sheet.paste(im, (x0 + (cell - im.width) // 2, shapka + (cell - im.height) // 2))
        d.text((x0 + cell / 2, shapka / 2), str(i + 1), fill=(40, 40, 40), font=font, anchor='mm')
    return sheet


if __name__ == '__main__':
    sheet, tochki = derevya()
    p = os.path.join(OUT, 'u8__four_trees.webp')
    sheet.save(p, 'WEBP', quality=90)
    print('four_trees', sheet.size, os.path.getsize(p) // 1024, 'KB', 'точки:', tochki)

    sheet = fruty_tanec()
    p = os.path.join(OUT, 'u5__fruits_dance.webp')
    sheet.save(p, 'WEBP', quality=90)
    print('fruits_dance', sheet.size, os.path.getsize(p) // 1024, 'KB')
