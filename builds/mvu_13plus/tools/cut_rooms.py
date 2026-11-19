"""Вырезки предметов из новых комнат (вариант «а», 12.11): предмет вырезается из самой комнаты
и кладётся поверх на то же место — со свечением. Выход: media/mvu_13plus/rooms/<комната>_<предмет>.webp + rooms.json с рамками в %."""
import os, sys, json
from collections import deque
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from boxes import BOXES
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'rooms_v2'); OUT = os.path.join(HERE, '..', '..', '..', 'media', 'mvu_13plus')
os.makedirs(os.path.join(OUT, 'rooms'), exist_ok=True)
RECT = {'map', 'wanted_poster'}
# шкаф сливается с тёмной стеной — режем по контуру, заданному руками (точки в пикселях комнаты)
POLY = {'wardrobe': [(0, 78), (88, 72), (96, 60), (140, 46), (170, 40), (205, 44), (240, 66), (270, 100), (293, 126), (293, 528), (245, 531), (120, 543), (0, 553)]}
# низ шкафа — по краю стола (стол его закрывает); ноутбук вычитаем по его контуру (замечание 50)
MINUS = {'wardrobe': ['laptop']}          # прямоугольные — режем рамкой, без нейросети
ROOM = {'room1_living_v2_src': 'room1_v2', 'room2_study_v2_src': 'room2_v2', 'room3_lab_v2_src': 'room3_v2'}
only = set(sys.argv[1:])
sess = None
def nn(im):
    global sess
    from rembg import remove, new_session
    if sess is None:
        import onnxruntime as ort
        so = ort.SessionOptions(); so.enable_cpu_mem_arena = False; so.enable_mem_pattern = False
        sess = new_session('birefnet-general', sess_opts=so)
    t = np.asarray(remove(im, session=sess)).copy()
    a = t[..., 3]; a[a < 50] = 0
    solid = a > 0; h, w = solid.shape; lab = np.zeros((h, w), np.int32); sizes = [0]
    for (y, x) in zip(*np.where(solid)):
        if lab[y, x]: continue
        k = len(sizes); lab[y, x] = k; n = 1; q = deque([(y, x)])
        while q:
            cy, cx = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < h and 0 <= nx < w and solid[ny, nx] and not lab[ny, nx]: lab[ny, nx] = k; n += 1; q.append((ny, nx))
        sizes.append(n)
    big = max(sizes); keep = np.array([z >= big * 0.05 for z in sizes]); keep[0] = False
    t[..., 3] = np.where(keep[lab], a, 0)
    return Image.fromarray(t, 'RGBA')
def tick(cut):
    # галочка — в правый верхний угол видимой части предмета (замечание 46), в % от рамки
    a = np.array(cut)[..., 3] > 60; ys, xs = np.where(a); w, h = cut.size
    if not len(xs): return dict(tx=90, ty=10)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    top = ys <= y0 + (y1 - y0) * .25          # самый правый край верхней четверти предмета, а не угол рамки
    xr = xs[top].max()
    return dict(tx=round((xr - (xr - x0) * .06) / w * 100, 1), ty=round((y0 + (y1 - y0) * .06) / h * 100, 1))
meta = json.load(open(os.path.join(OUT, 'rooms', 'rooms.json'))) if os.path.exists(os.path.join(OUT, 'rooms', 'rooms.json')) else {}
if '--ticks' in sys.argv:
    for oid, m in meta.items():
        m.update(tick(Image.open(os.path.join(OUT, 'rooms', f"{m['room']}_{oid}.webp")).convert('RGBA')))
    json.dump(meta, open(os.path.join(OUT, 'rooms', 'rooms.json'), 'w'), indent=1); print('ticks'); sys.exit()
for src, boxes in BOXES.items():
    room = Image.open(os.path.join(SRC, src + '.webp')).convert('RGB'); W, H = room.size
    name = ROOM[src]
    room.save(os.path.join(OUT, name + '.webp'), quality=84)
    for oid, (x0, y0, x1, y1) in boxes.items():
        if only and oid not in only: continue
        crop = room.crop((x0, y0, x1, y1))
        if oid in POLY:
            from PIL import ImageDraw
            cut = crop.convert('RGBA'); m = Image.new('L', crop.size, 0)
            ImageDraw.Draw(m).polygon([(x - x0, y - y0) for x, y in POLY[oid]], fill=255)
            for other in MINUS.get(oid, []):
                ob = boxes[other]; oc = Image.open(os.path.join(OUT, 'rooms', f'{name}_{other}.webp')).getchannel('A')
                hole = Image.new('L', crop.size, 0); hole.paste(oc, (ob[0] - x0, ob[1] - y0))
                from PIL import ImageFilter, ImageChops
                m = ImageChops.subtract(m, hole.point(lambda v: 255 if v > 20 else 0).filter(ImageFilter.MaxFilter(5)))
            cut.putalpha(m)
        else:
            cut = crop.convert('RGBA') if oid in RECT else nn(crop)
        cut.save(os.path.join(OUT, 'rooms', f'{name}_{oid}.webp'), quality=90)
        meta[oid] = dict(room=name, x=round(x0 / W * 100, 2), y=round(y0 / H * 100, 2), w=round((x1 - x0) / W * 100, 2), h=round((y1 - y0) / H * 100, 2), **tick(cut))
        json.dump(meta, open(os.path.join(OUT, 'rooms', 'rooms.json'), 'w'), indent=1)
        print(oid, flush=True)
print('done')
