# Нарезка листов картинок урока 3 (белый фон, предметы разнесены) → media/reading10/u3/*.webp
import sys, numpy as np
from PIL import Image
SRC, OUT = sys.argv[1], sys.argv[2]
def bands(mask, axis, gap):
    p = mask.any(axis=axis); res = []; on = False; st = 0; blank = 0
    for k, v in enumerate(p):
        if v:
            if not on: on, st = True, k
            blank = 0
        elif on:
            blank += 1
            if blank > gap: res.append((st, k - blank + 1)); on = False
    if on: res.append((st, len(p)))
    return [b for b in res if b[1] - b[0] > 20]
def items(path, gap=25):
    im = Image.open(path).convert('RGB'); a = np.asarray(im).astype(int)
    mask = (a.min(axis=2) < 232) | (a.max(axis=2) - a.min(axis=2) > 18)
    out = []
    for r0, r1 in bands(mask, 1, gap):
        sub = mask[r0:r1]
        for c0, c1 in bands(sub, 0, gap):
            m2 = mask[r0:r1, c0:c1]; rr = np.where(m2.any(axis=1))[0]
            out.append((c0, r0 + rr[0], c1, r0 + rr[-1] + 1))
    return im, out
def save(im, box, name, maxs=720):
    c = im.crop(box)
    a = np.asarray(c).astype(int); lo = a.min(axis=2); sat = a.max(axis=2) - lo
    t = np.clip((lo - 236) / 12.0, 0, 1) * (sat < 14)  # почти белое и бесцветное → белое, с мягким переходом
    a = (a + (255 - a) * t[..., None]).astype('uint8'); c = Image.fromarray(a)
    w, h = c.size; pad = int(max(w, h) * 0.08)
    bg = Image.new('RGB', (w + 2 * pad, h + 2 * pad), 'white'); bg.paste(c, (pad, pad))
    if max(bg.size) > maxs: bg.thumbnail((maxs, maxs), Image.LANCZOS)
    bg.save(f'{OUT}/{name}.webp', quality=85); print(name, bg.size)
if len(sys.argv) > 3: SHEETS = {}
else: SHEETS = {'1.webp': ['pen', 'egg', 'umbrella', 'cup', 'kit', 'red_paint'],
          '2.webp': ['sun', 'map', 'mat', 'pot', 'pan'],
          '4.webp': ['cat', 'rat', 'dog', 'pig']}
for f, names in SHEETS.items():
    im, bx = items(f'{SRC}/{f}')
    if len(bx) != len(names): print('!!', f, len(bx), bx); continue
    for b, n in zip(bx, names): save(im, b, n)
for f, n in ((() if len(sys.argv) > 3 else (('3.webp', 'run'), ('5.webp', 'kid')))):
    im, bx = items(f'{SRC}/{f}', gap=80)
    x0 = min(b[0] for b in bx); y0 = min(b[1] for b in bx); x1 = max(b[2] for b in bx); y1 = max(b[3] for b in bx)
    save(im, (x0, y0, x1, y1), n, maxs=900)

# --- вторая партия (20.11): листы героев и сцены ---
if len(sys.argv) > 3 and sys.argv[3] == 'geroi':
    for f, who in (('9.webp', 'sam'), ('8.webp', 'dan')):
        im, bx = items(f'{SRC}/{f}', gap=40)
        cols = {}
        for b in bx: cols.setdefault(b[0] // 300, []).append(b)
        groups = sorted(cols.values(), key=lambda g: min(b[0] for b in g))
        print(who, len(bx), 'частей', len(groups), 'поз')
        for g, pose in zip(groups, ['stand', 'wave', 'surprised', 'phone']):
            save(im, (min(b[0] for b in g), min(b[1] for b in g), max(b[2] for b in g), max(b[3] for b in g)), f'{who}_{pose}', maxs=900)
    for f, n in (('6.webp', 'scene_phone'), ('7.webp', 'scene_cup')):
        im = Image.open(f'{SRC}/{f}').convert('RGB'); im.thumbnail((1400, 1400), Image.LANCZOS); im.save(f'{OUT}/{n}.webp', quality=82); print(n, im.size)
