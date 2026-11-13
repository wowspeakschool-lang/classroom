# -*- coding: utf-8 -*-
"""SM0 юнит 4: картинка «все хобби» — лист из шести занятий курса.

Было: `kids_group.webp` — четверо детей танцуют, то есть одно хобби на всю
картинку, а задание просит назвать все (замечание Анны 13.11.2026).
Берём те же шесть картинок, по которым ребёнок только что слушал и выбирал
в блоке 5: swimming · reading · dancing · football · running · painting.

python3.13 builds/kartinki/sm0_hobbies.py
"""
import os, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'builds', 'kartinki', 'gg1_12112026'))
from listy import podgotovit

FILES = ['swimming', 'reading', 'dancing', 'football', 'running', 'painting']
CELL, GAP, COLS = 420, 70, 3


def sobrat():
    rows = (len(FILES) + COLS - 1) // COLS
    w = GAP + COLS * (CELL + GAP)
    h = GAP + rows * (CELL + GAP)
    sheet = Image.new('RGB', (w, h), 'white')
    for i, n in enumerate(FILES):
        im = podgotovit(os.path.join('media/sm0/new', n + '.webp'))
        im.thumbnail((CELL, CELL), Image.LANCZOS)
        x = GAP + (i % COLS) * (CELL + GAP) + (CELL - im.width) // 2
        y = GAP + (i // COLS) * (CELL + GAP) + (CELL - im.height) // 2
        sheet.paste(im, (x, y))
    return sheet


if __name__ == '__main__':
    s = sobrat()
    p = os.path.join(ROOT, 'media', 'sm0', 'new', 'hobbies_6.webp')
    s.save(p, 'WEBP', quality=90)
    print(s.size, os.path.getsize(p) // 1024, 'KB')
