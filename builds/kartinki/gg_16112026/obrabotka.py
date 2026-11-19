# -*- coding: utf-8 -*-
"""GG1 и GG2, партия 16.11.2026: отбелить фон у предметов, обрезать, поле, webp.

python3.13 -I builds/kartinki/gg_16112026/obrabotka.py <папка с png> <папка вывода>
"""
import os, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'builds', 'kartinki', 'gg1_12112026'))
from listy import podgotovit

SYR, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

# сцены не обрезаем по предмету и храним крупнее
SCENY = ('place_', 'room_', 'photo_', 'school_walk', 'tom_lucy_rex', 'verb_swim',
         'book_dog', 'book_boy', 'book_dad', 'book_download', 'book_pets',
         'book_text', 'book_video', 'english_class')

for name in sorted(os.listdir(SYR)):
    if not name.endswith('.png'):
        continue
    scena = any(s in name for s in SCENY)
    put = os.path.relpath(os.path.join(SYR, name), ROOT)
    if scena:
        im = Image.open(os.path.join(SYR, name)).convert('RGB')
        maks, pole = 1000, 0.0
    else:
        im = podgotovit(put)
        maks, pole = 760, 0.06
    if pole:
        p = int(max(im.size) * pole)
        holst = Image.new('RGB', (im.width + 2 * p, im.height + 2 * p), 'white')
        holst.paste(im, (p, p))
        im = holst
    im.thumbnail((maks, maks), Image.LANCZOS)
    dst = os.path.join(OUT, name.replace('.png', '.webp'))
    im.save(dst, 'WEBP', quality=90)
    print(name[:-4], im.size, os.path.getsize(dst) // 1024, 'KB')
