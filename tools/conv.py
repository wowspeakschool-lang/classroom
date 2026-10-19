# -*- coding: utf-8 -*-
"""PNG → webp в media/. Таблица на юнит, по строке на картинку.

Файл `conv_uN.py` рядом со сборкой юнита:

    import sys; sys.path.insert(0, '/home/user/classroom/tools')
    from conv import run

    TABLE = [
        # исходник в папке PNG,  имя в media/,  ширина, качество
        ('hw2_p02_0', 'card_can',   900, 88),
        ('hw2_p04_0', 'pen_tree',   500, 82),
    ]
    run(TABLE, 'u1img', 'sm3/u1')

Размеры: карточка 180–420 px, сцена 760–900 px, служебные 200 px.
Качество: 88 для карточек с мелким текстом, 78–82 для объектов и фото.
"""
from PIL import Image
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def save(im, path, width, q):
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.convert('RGB').save(path, 'WEBP', quality=q, method=6)
    return os.path.getsize(path)


def run(table, src_dir, media_rel, ext='png'):
    """table — [(исходник, имя, ширина, качество)]; media_rel — 'sm3/u1'."""
    dst = f'{ROOT}/media/{media_rel}'
    os.makedirs(dst, exist_ok=True)
    total = 0
    for src, name, w, q in table:
        n = save(Image.open(f'{src_dir}/{src}.{ext}'), f'{dst}/{name}.webp', w, q)
        total += n
        print(f'  {name:18} {n // 1024:>4} КБ')
    print(f'{len(table)} файлов, {total / 1024:.0f} КБ → media/{media_rel}/')
    return total
