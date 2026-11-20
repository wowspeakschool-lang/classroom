"""Полоска стола под шкафом (room2_v2) — кладётся поверх шкафа, чтобы свечение было только сверху и справа (замечание 65).
Берётся из самой комнаты: всё, что ниже нижнего края шкафа (край стола), без ноутбука.
    python3 builds/mvu_13plus/tools/front_desk.py"""
import os, json
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'rooms_v2', 'room2_study_v2_src.webp')
OUT = os.path.join(HERE, '..', '..', '..', 'media', 'mvu_13plus', 'rooms')
EDGE = [(0, 553), (120, 543), (245, 531), (293, 528), (360, 528)]   # нижний край шкафа (как в cut_rooms.POLY)
X1, Y0, Y1 = 360, 500, 600
room = Image.open(SRC).convert('RGBA'); W, H = room.size
a = np.zeros((Y1 - Y0, X1), np.uint8)
xs, ys = zip(*EDGE)
for x in range(X1):
    yl = np.interp(x, xs, ys) - 1
    a[max(0, int(yl) - Y0):, x] = 255
# ноутбук стоит перед полоской — его не закрываем
meta = json.load(open(os.path.join(OUT, 'rooms.json')))
L = meta['laptop']; lx, ly, lw, lh = [round(L[k] / 100 * s) for k, s in (('x', W), ('y', H), ('w', W), ('h', H))]
la = np.asarray(Image.open(os.path.join(OUT, 'room2_v2_laptop.webp')).convert('RGBA').resize((lw, lh)))[..., 3]
for yy in range(Y0, Y1):
    for xx in range(lx, min(X1, lx + lw)):
        if ly <= yy < ly + lh and la[yy - ly, xx - lx] > 0: a[yy - Y0, xx] = 0
crop = room.crop((0, Y0, X1, Y1)); crop.putalpha(Image.fromarray(a))
crop.save(os.path.join(OUT, 'room2_v2_front_desk.webp'), quality=90, lossless=False)
print(dict(x=0.0, y=round(Y0 / H * 100, 3), w=round(X1 / W * 100, 3), h=round((Y1 - Y0) / H * 100, 3)))
