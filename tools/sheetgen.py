# -*- coding: utf-8 -*-
"""Контактный лист картинок из выгрузки: python3 sheetgen.py u6img hw3 [cols]"""
from PIL import Image, ImageDraw
import sys, glob, os
d, pref = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 5
names = sorted(glob.glob(f'{d}/{pref}*.png'))
cell, lab = 300, 22
rows = (len(names) + cols - 1) // cols
s = Image.new('RGB', (cols * cell, rows * (cell + lab)), 'white')
dr = ImageDraw.Draw(s)
for i, p in enumerate(names):
    im = Image.open(p).convert('RGB'); im.thumbnail((cell - 10, cell - 10))
    x = (i % cols) * cell + (cell - im.width) // 2
    y = (i // cols) * (cell + lab) + (cell - im.height) // 2
    s.paste(im, (x, y))
    dr.text(((i % cols) * cell + 4, (i // cols) * (cell + lab) + cell + 3),
            os.path.basename(p)[:-4] + f' {Image.open(p).width}x{Image.open(p).height}', fill='black')
out = f'{d}/sheet_{pref}.png'
s.save(out); print(out, s.size, len(names))
