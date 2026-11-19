# -*- coding: utf-8 -*-
"""Третья партия картинок от Анны 19.11.2026: клавиатура, планшет, собака «next to» и «behind»."""
import os, sys
from PIL import Image
sys.path.insert(0, 'builds/kartinki/gg1_12112026')
from listy import podgotovit

IMG = '/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/images'

# предметы на белом фоне — обрезаем и добавляем поле
PREDMETY = [
    ('14.webp', 'media/gg2/u3/keyboard.webp'),
    ('15.webp', 'media/gg2/u3/tablet.webp'),
]
for src, dst in PREDMETY:
    im = podgotovit(os.path.join(IMG, src))
    p = int(max(im.size) * 0.06)
    holst = Image.new('RGB', (im.width + 2*p, im.height + 2*p), 'white')
    holst.paste(im, (p, p))
    holst.thumbnail((760, 760), Image.LANCZOS)
    holst.save(dst, 'WEBP', quality=90)
    print(dst, holst.size, os.path.getsize(dst)//1024, 'KB')

# сцены — только уменьшаем
SCENY = [
    ('16.webp', 'media/gg2/u5/book_dog_3.webp'),
    ('17.webp', 'media/gg2/u5/book_dog_5.webp'),
]
for src, dst in SCENY:
    im = Image.open(os.path.join(IMG, src)).convert('RGB')
    im.thumbnail((1000, 1000), Image.LANCZOS)
    im.save(dst, 'WEBP', quality=88)
    print(dst, im.size, os.path.getsize(dst)//1024, 'KB')
