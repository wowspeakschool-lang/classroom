# -*- coding: utf-8 -*-
"""Очередь 2 GG1: отбелить фон, обрезать, добавить поле, сохранить webp."""
import os, sys
from PIL import Image, ImageChops, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'builds', 'kartinki', 'gg1_12112026'))
from listy import podgotovit

SYR = os.path.join(ROOT, 'builds', 'kartinki', 'gg1_13112026', 'syrye2')
OUT = os.path.join(ROOT, 'builds', 'kartinki', 'gg1_13112026', 'gotovo2')
os.makedirs(OUT, exist_ok=True)
MAX = 760          # карточка: храним с запасом
POLE = 0.06        # поле по краям от большей стороны

for name in sorted(os.listdir(SYR)):
    if not name.endswith('.png'):
        continue
    im = podgotovit(os.path.join('builds/kartinki/gg1_13112026/syrye2', name))
    p = int(max(im.size) * POLE)
    holst = Image.new('RGB', (im.width + 2 * p, im.height + 2 * p), 'white')
    holst.paste(im, (p, p))
    holst.thumbnail((MAX, MAX), Image.LANCZOS)
    dst = os.path.join(OUT, name.replace('.png', '.webp'))
    holst.save(dst, 'WEBP', quality=90)
    print(name[:-4], holst.size, os.path.getsize(dst) // 1024, 'KB')
