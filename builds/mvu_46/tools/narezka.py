"""Нарезка листа с прозрачным фоном на отдельные картинки.

python3 builds/mvu_46/tools/narezka.py <лист.png|webp> <папка> имя1 имя2 ...
Имена — по строкам, слева направо. Каждая картинка: обрезка по альфе,
прозрачное поле 8 % от большей стороны, webp q88.
"""
import sys, os
import numpy as np
from PIL import Image
from scipy import ndimage

src, out, names = sys.argv[1], sys.argv[2], sys.argv[3:]
im = Image.open(src).convert('RGBA')
a = np.array(im)[:, :, 3] > 24
# склеиваем близкие кусочки (искры у книги, шнурки) в один предмет
grown = ndimage.binary_dilation(a, iterations=4)
lab, n = ndimage.label(grown)
big, small = [], []
for sl in ndimage.find_objects(lab):
    h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
    (big if h * w >= im.width * im.height * 0.004 else small).append(sl)
# мелочь (искры, блики) прицепляем к ближайшему крупному предмету
box = [[s[0].start, s[0].stop, s[1].start, s[1].stop] for s in big]
for s in small:
    cy, cx = (s[0].start + s[0].stop) / 2, (s[1].start + s[1].stop) / 2
    def d(b):
        dy = max(b[0] - cy, 0, cy - b[1]); dx = max(b[2] - cx, 0, cx - b[3])
        return dx * dx + dy * dy
    b = min(box, key=d)
    if d(b) < (im.width * 0.06) ** 2:
        b[0] = min(b[0], s[0].start); b[1] = max(b[1], s[0].stop)
        b[2] = min(b[2], s[1].start); b[3] = max(b[3], s[1].stop)
objs = [(slice(b[0], b[1]), slice(b[2], b[3])) for b in box]
if len(objs) != len(names):
    sys.exit(f'нашлось {len(objs)} предметов, а имён {len(names)}')
# строки: группируем по центру по вертикали
objs.sort(key=lambda s: (s[0].start + s[0].stop) / 2)
rows, cur = [], [objs[0]]
for s in objs[1:]:
    c = (s[0].start + s[0].stop) / 2
    pc = (cur[-1][0].start + cur[-1][0].stop) / 2
    if abs(c - pc) < im.height * 0.15:
        cur.append(s)
    else:
        rows.append(cur); cur = [s]
rows.append(cur)
order = [s for r in rows for s in sorted(r, key=lambda s: s[1].start)]
os.makedirs(out, exist_ok=True)
arr = np.array(im)
for sl, name in zip(order, names):
    piece = arr[sl].copy()
    p = Image.fromarray(piece)
    bb = p.getbbox()
    p = p.crop(bb)
    m = int(max(p.size) * 0.08)
    c = Image.new('RGBA', (p.width + 2 * m, p.height + 2 * m), (0, 0, 0, 0))
    c.paste(p, (m, m))
    c.save(os.path.join(out, name + '.webp'), quality=88, method=6)
    print(name, c.size)
