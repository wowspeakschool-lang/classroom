"""Стирает куски подписей, попавшие под рисунок: всё ниже последнего пустого ряда
в нижней трети картинки. python3 fix_fragments.py — переприменяемый."""
import numpy as np
from PIL import Image
FILES = ['out512/20/appealing.png', 'out512/20/balanced.png']
for f in FILES:
    a = np.array(Image.open(f).convert('RGBA'))
    rows = (a[..., 3] > 40).sum(1)
    empty = [y for y in range(int(a.shape[0] * .66), a.shape[0]) if rows[y] == 0]
    gap = next((y for y in empty if rows[y:].sum() and rows[y:].sum() < 0.03 * (a[..., 3] > 40).sum()), None)
    if gap is None: print(f, 'чисто'); continue
    a[gap:, :, 3] = 0
    Image.fromarray(a).save(f); print(f, 'стёрто ниже', gap)
