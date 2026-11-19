# -*- coding: utf-8 -*-
"""Картинки от Анны 19.11.2026 + принятые из нашей партии — в media/."""
import os, shutil, sys
from PIL import Image
sys.path.insert(0, 'builds/kartinki/gg1_12112026')
from listy import podgotovit

IMG = '/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/images'
GOT = '/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/gen/prinyato'

# от Анны: предмет (отбелить фон, обрезать) или сцена (оставить как есть)
OT_ANNY = [
    ('4.webp', 'media/gg1/u2/near_trainers.webp',  'predmet'),
    ('5.webp', 'media/gg1/u5/verb_fly.webp',       'scena'),
    ('6.webp', 'media/gg1/u3/room_garden.webp',    'scena'),
    ('7.webp', 'media/gg1/u5/verb_swim.webp',      'scena'),
    ('8.webp', 'media/gg1/u2/near_tracksuit.webp', 'predmet'),
]
NASHI = [
    ('gg2__u3__headphones.webp',       'media/gg2/u3/headphones.webp'),
    ('gg2__u3__book_boy_selfie.webp',  'media/gg2/u3/book_boy_selfie.webp'),
    ('gg2__u3__book_pets_site.webp',   'media/gg2/u3/book_pets_site.webp'),
    ('gg2__u3__book_text_hi.webp',     'media/gg2/u3/book_text_hi.webp'),
    ('gg2__u5__book_dog_2.webp',       'media/gg2/u5/book_dog_2.webp'),
]

for src, dst, vid in OT_ANNY:
    put = os.path.join(IMG, src)
    if vid == 'predmet':
        im = podgotovit(put)
        p = int(max(im.size) * 0.06)
        holst = Image.new('RGB', (im.width + 2*p, im.height + 2*p), 'white')
        holst.paste(im, (p, p)); im = holst
        im.thumbnail((760, 760), Image.LANCZOS)
    else:
        im = Image.open(put).convert('RGB')
        im.thumbnail((1000, 1000), Image.LANCZOS)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im.save(dst, 'WEBP', quality=90)
    print(dst, im.size, os.path.getsize(dst)//1024, 'KB')

for src, dst in NASHI:
    im = Image.open(os.path.join(GOT, src)).convert('RGB')
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im.save(dst, 'WEBP', quality=90)
    print(dst, im.size, os.path.getsize(dst)//1024, 'KB')
