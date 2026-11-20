# -*- coding: utf-8 -*-
"""Пары «предмет и предмет» со стрелкой на нужный: карточки прилагательных GG1 юнит 2."""
import sys, os
from PIL import Image, ImageDraw

SRC = sys.argv[1]           # папка с картинками от Анны
OUT = '/home/user/classroom/media/gg1/u2'
W, H = 1000, 700
POLE = 40
KRASNYJ = (211, 47, 47)


def polozhit(holst, put, vysota, centr_x, niz_y):
    im = Image.open(put).convert('RGBA')
    k = vysota / im.height
    im = im.resize((max(1, int(im.width * k)), vysota), Image.LANCZOS)
    x, y = centr_x - im.width // 2, niz_y - im.height
    holst.alpha_composite(im, (x, y))
    return (x, y, im.width, im.height)


def strelka(d, cx, verh_y):
    """Красная стрелка сверху вниз, остриё у верхнего края предмета."""
    konec = verh_y - 12
    nachalo = max(20, konec - 130)
    # белая обводка, чтобы стрелка читалась и на красном предмете
    d.line([(cx, nachalo), (cx, konec - 26)], fill=(255, 255, 255), width=22)
    d.polygon([(cx - 38, konec - 36), (cx + 38, konec - 36), (cx, konec + 8)], fill=(255, 255, 255))
    d.line([(cx, nachalo), (cx, konec - 26)], fill=KRASNYJ, width=14)
    d.polygon([(cx - 30, konec - 34), (cx + 30, konec - 34), (cx, konec)], fill=KRASNYJ)


def para(a_put, a_vys, b_put, b_vys, imena):
    """Две картинки рядом; две версии: стрелка на левую, стрелка на правую."""
    for celi, imya in zip((0, 1), imena):
        holst = Image.new('RGBA', (W, H), (255, 255, 255, 255))
        a = polozhit(holst, a_put, a_vys, W // 4, H - POLE)
        b = polozhit(holst, b_put, b_vys, W * 3 // 4, H - POLE)
        d = ImageDraw.Draw(holst)
        cel = a if celi == 0 else b
        strelka(d, cel[0] + cel[2] // 2, cel[1])
        holst.convert('RGB').save(os.path.join(OUT, imya + '.webp'), 'WEBP', quality=90)
        print('готово', imya)


para(os.path.join(SRC, '3.webp'), 520, os.path.join(SRC, '3.webp'), 250, ('adj_big', 'adj_small'))
para(os.path.join(SRC, '5.webp'), 520, os.path.join(SRC, '7.webp'), 250, ('adj_long', 'adj_short'))
para(os.path.join(SRC, '4.webp'), 300, os.path.join(SRC, '6.webp'), 300, ('adj_new', 'adj_old'))
para(os.path.join(SRC, '8.webp'), 330, os.path.join(SRC, '9.webp'), 330, ('adj_cool', 'adj_boring'))
