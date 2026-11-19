# -*- coding: utf-8 -*-
"""Картинки юнита 1 Go Getter 3 (по рабочей тетради)."""
import os, sys
from PIL import Image
sys.path.insert(0, 'builds/kartinki/gg1_12112026')
from listy import podgotovit

S = '/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/'
PARY = [
    (S+'gg3u1/chore_dishwasher.png',  'media/gg3/u1/chore_dishwasher.webp'),
    (S+'gg3u1/chore_vacuum.png',      'media/gg3/u1/chore_vacuum.webp'),
    (S+'gg3u1b/chore_feed_pet_b.png', 'media/gg3/u1/chore_feed_pet.webp'),
    (S+'gg3u1/chore_set_table.png',   'media/gg3/u1/chore_set_table.webp'),
    (S+'gg3u1/fam_bed.png',           'media/gg3/u1/fam_bed.webp'),
    (S+'gg3u1/fam_cat.png',           'media/gg3/u1/fam_cat.webp'),
    (S+'gg3u1b/fam_dishes_b.png',     'media/gg3/u1/fam_dishes.webp'),
    (S+'gg3u1b/fam_phone_b.png',      'media/gg3/u1/fam_phone.webp'),
]
for src, dst in PARY:
    im = podgotovit(src)
    p = int(max(im.size) * 0.05)
    holst = Image.new('RGB', (im.width + 2*p, im.height + 2*p), 'white')
    holst.paste(im, (p, p))
    holst.thumbnail((900, 900), Image.LANCZOS)
    holst.save(dst, 'WEBP', quality=88)
    print(dst, holst.size, os.path.getsize(dst)//1024, 'KB')
