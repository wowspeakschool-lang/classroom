# -*- coding: utf-8 -*-
"""Приветствия и прощания Go Getter: обрезка, поле, webp."""
import os, sys
from PIL import Image
sys.path.insert(0, 'builds/kartinki/gg1_12112026')
from listy import podgotovit

S = '/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/'
PARY = [
    (S+'gg_privet2/gg_hello_1b.png', 'media/shared/gg/hello_teen_wave.webp'),
    (S+'gg_privet/gg_hello_2.png',   'media/shared/gg/hello_highfive.webp'),
    (S+'gg_privet2/gg_hello_3b.png', 'media/shared/gg/hello_laptop.webp'),
    (S+'gg_privet2/gg_hello_6b.png', 'media/shared/gg/hello_backpack.webp'),
    (S+'gg_privet3/gg_hello_7.png',  'media/shared/gg/hello_books.webp'),
    (S+'gg_privet3/gg_hello_8.png',  'media/shared/gg/hello_girl_wave.webp'),
    (S+'gg_privet/gg_bye_1.png',     'media/shared/gg/bye_trophy.webp'),
    (S+'gg_privet/gg_bye_2.png',     'media/shared/gg/bye_medal.webp'),
    (S+'gg_privet/gg_bye_3.png',     'media/shared/gg/bye_thumb.webp'),
    (S+'gg_privet/gg_bye_4.png',     'media/shared/gg/bye_popper.webp'),
    (S+'gg_privet2/gg_bye_5b.png',   'media/shared/gg/bye_certificate.webp'),
    (S+'gg_privet/gg_bye_6.png',     'media/shared/gg/bye_star.webp'),
]
for src, dst in PARY:
    im = podgotovit(src)
    p = int(max(im.size) * 0.05)
    holst = Image.new('RGB', (im.width + 2*p, im.height + 2*p), 'white')
    holst.paste(im, (p, p))
    holst.thumbnail((600, 600), Image.LANCZOS)
    holst.save(dst, 'WEBP', quality=90)
    print(dst, holst.size, os.path.getsize(dst)//1024, 'KB')
