# -*- coding: utf-8 -*-
"""Вторая партия картинок от Анны 19.11.2026 — в media/."""
import os, sys
from PIL import Image
sys.path.insert(0, 'builds/kartinki/gg1_12112026')
from listy import podgotovit

IMG = '/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/images'
PARY = [
    ('9.webp',  'media/gg2/u1/dictionary.webp'),
    ('10.webp', 'media/gg2/u1/ruler.webp'),
    ('11.webp', 'media/gg2/u3/book_download_song.webp'),
    ('12.webp', 'media/gg2/u3/book_video_chat.webp'),
    ('13.webp', 'media/gg2/u3/camera.webp'),
]
for src, dst in PARY:
    im = podgotovit(os.path.join(IMG, src))
    p = int(max(im.size) * 0.06)
    holst = Image.new('RGB', (im.width + 2*p, im.height + 2*p), 'white')
    holst.paste(im, (p, p))
    holst.thumbnail((760, 760), Image.LANCZOS)
    holst.save(dst, 'WEBP', quality=90)
    print(dst, holst.size, os.path.getsize(dst)//1024, 'KB')
