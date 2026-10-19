# -*- coding: utf-8 -*-
"""Размеры картинок курса — ищем мыльные.

    python3.13 tools/img_sizes.py media/sm0 [порог]

Печатает всё, что меньше порога по большей стороне (по умолчанию 300 px),
от самых мелких. Такие картинки на карточке или в варианте ответа мылятся;
их выносим в файл «доработать руками» с промптом на перерисовку.
"""
import os, sys
from PIL import Image

root = sys.argv[1]
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 300
rows = []
for dirpath, _, files in os.walk(root):
    for f in files:
        if not f.lower().endswith(('.webp', '.png', '.jpg', '.jpeg', '.gif')):
            continue
        p = os.path.join(dirpath, f)
        try:
            w, h = Image.open(p).size
        except Exception as e:
            print(f'  !! не открылась {p}: {e}')
            continue
        rows.append((max(w, h), w, h, p))
rows.sort()
small = [r for r in rows if r[0] < limit]
for m, w, h, p in small:
    print(f'{w:>5}×{h:<5} {p}')
print(f'\nвсего картинок {len(rows)}, меньше {limit} px по большей стороне: {len(small)}')
