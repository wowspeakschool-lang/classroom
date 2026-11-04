"""Нарезка листов Анны и подготовка фонов для вводного урока 13+.

python3 builds/mvu_13plus/tools/cut.py <номер> <файл> [<файл> …]
  scene  — фон/сцена: webp 1536 по ширине, q82
  sheet  — лист предметов на белом: делим по белым промежуткам на строки и
           столбцы, белый фон от краёв делаем прозрачным, webp q88.
Имена предметов — в SHEETS ниже, построчно слева направо.
"""
import sys, os
from collections import deque
import numpy as np
from PIL import Image

OUT = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'media', 'mvu_13plus')
OUT = os.path.normpath(OUT)

SCENES = {1: 'room1_living', 2: 'room2_study', 3: 'room3_lab', 4: 'door_open',
          12: 'street', 21: 'crime_scene', 9: 'schoolbag_open', 10: 'fridge_open'}
SHEETS = {
    5: ['family_photo', 'schoolbag', 'passport', 'fruit_bowl', 'football', 'bus',
        'cinema_tickets', 'umbrella', 'cat'],
    6: ['wardrobe', 'suitcase', 'map', 'first_aid_kit', 'novel', 'wanted_poster',
        'wallet', 'laptop', 'binoculars'],
    7: ['trophy', 'stethoscope', 'microphone', 'smartphone', 'graduation_cap',
        'seismograph', 'magnifying_glass', 'scroll', 'time_capsule', 'billboard'],
    8: ['fam_grandfather', 'fam_grandmother', 'fam_father', 'fam_mother',
        'fam_aunt', 'fam_uncle', 'fam_boy', 'fam_girl'],
    11: ['athlete', 'sport_swim', 'sport_tennis', 'sport_bike'],
    13: ['w_sunny', 'w_rainy', 'w_snowy', 'w_windy', 'w_cloudy'],
    14: ['cl_coat', 'cl_shorts', 'cl_scarf', 'cl_sandals', 'cl_swimsuit', 'cl_boots',
         'cl_hat', 'cl_gloves', 'cl_sunglasses'],
    15: ['an_cat', 'an_horse', 'an_cow', 'an_sheep', 'an_rabbit', 'an_dog',
         'an_hamster', 'an_pig', 'an_chicken'],
    16: ['hol_airport', 'hol_castle', 'hol_beach'],
    17: ['geo_river', 'geo_mountains', 'geo_desert', 'geo_waterfall', 'geo_island',
         'geo_forest', 'tr_sightseeing', 'tr_camping', 'tr_ferry'],
    18: ['suspect_1', 'suspect_2', 'suspect_3', 'suspect_4'],
    19: ['food_spicy', 'food_crunchy', 'food_sour', 'food_sweet', 'food_bitter',
          'food_salty'],
    20: ['dis_volcano', 'dis_flood', 'dis_earthquake', 'dis_wildfire',
         'dis_hurricane', 'dis_tsunami'],
    22: ['fut_travel', 'fut_graduation', 'fut_doctor', 'fut_band'],
}
WHITE = 238   # для поиска границ предметов на листе
BG = 250      # фон листа — 254; блики на белых предметах темнее, их не трогаем


def runs(mask1d, min_gap, min_len):
    """Отрезки, где есть не-белое, разделённые белыми промежутками ≥ min_gap."""
    idx = np.where(mask1d)[0]
    if not len(idx):
        return []
    out, s, p = [], idx[0], idx[0]
    for i in idx[1:]:
        if i - p > min_gap:
            out.append((s, p + 1)); s = i
        p = i
    out.append((s, p + 1))
    return [r for r in out if r[1] - r[0] >= min_len]


# замкнутые просветы фона убираем только у этих (у остальных белое внутри — блики)
HOLES = {'schoolbag', 'stethoscope', 'trophy', 'umbrella', 'billboard', 'cat'}


def transparent(im, holes=True):
    """Белый фон, связанный с краем, → прозрачный (белое внутри предмета остаётся)."""
    a = np.asarray(im.convert('RGB')).astype(int)
    h, w, _ = a.shape
    white = (a.min(axis=2) >= BG)
    seen = np.zeros((h, w), bool)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if white[y, x] and not seen[y, x]:
                seen[y, x] = True; q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if white[y, x] and not seen[y, x]:
                seen[y, x] = True; q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and white[ny, nx] and not seen[ny, nx]:
                seen[ny, nx] = True; q.append((ny, nx))
    # замкнутые островки чистого белого (просвет между лямкой и рюкзаком) — тоже фон
    pure = ((a.min(axis=2) >= 240) & ~seen) if holes else np.zeros((h, w), bool)
    for (y, x) in zip(*np.where(pure)):
        if seen[y, x] or not pure[y, x]:
            continue
        comp, q2 = [(y, x)], deque([(y, x)]); pure[y, x] = False
        while q2:
            cy, cx = q2.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < h and 0 <= nx < w and pure[ny, nx]:
                    pure[ny, nx] = False; comp.append((ny, nx)); q2.append((ny, nx))
        if len(comp) >= 150:
            for cy, cx in comp:
                seen[cy, cx] = True
    # чужие обрывки (кусок соседнего предмета) — оставляем только крупные куски
    solid = ~seen
    lab = np.zeros((h, w), np.int32); sizes = [0]
    for (y, x) in zip(*np.where(solid)):
        if lab[y, x]:
            continue
        k = len(sizes); lab[y, x] = k; n = 1; q2 = deque([(y, x)])
        while q2:
            cy, cx = q2.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < h and 0 <= nx < w and solid[ny, nx] and not lab[ny, nx]:
                    lab[ny, nx] = k; n += 1; q2.append((ny, nx))
        sizes.append(n)
    big = max(sizes)
    keep = np.array([s >= big * 0.03 for s in sizes])
    seen = seen | ~keep[lab]
    # светлая кайма по краю: два шага съедаем почти-белые пиксели, граничащие с фоном
    light = a.min(axis=2) >= 225
    for _ in range(3):
        nb = np.zeros_like(seen)
        nb[1:] |= seen[:-1]; nb[:-1] |= seen[1:]; nb[:, 1:] |= seen[:, :-1]; nb[:, :-1] |= seen[:, 1:]
        seen = seen | (nb & light)
    alpha = np.where(seen, 0, 255).astype(np.uint8)
    # мягкий край: на границе полупрозрачность по светлоте
    rgba = np.dstack([a.astype(np.uint8), alpha])
    return Image.fromarray(rgba, 'RGBA')


COL_GAP = {7: 3}


def cut_sheet(path, names, pad=12, col_gap=18):
    im = Image.open(path).convert('RGB')
    a = np.asarray(im)
    ink = a.min(axis=2) < WHITE
    rows = runs(ink.sum(axis=1) > 40, 6, 40)
    boxes = []
    for (y0, y1) in rows:
        cols = runs(ink[y0:y1].sum(axis=0) > 3, col_gap, 40)
        for (x0, x1) in cols:
            sub = ink[y0:y1, x0:x1]
            ys = np.where(sub.any(axis=1))[0]
            boxes.append((x0, y0 + ys[0], x1, y0 + ys[-1] + 1))
    if len(boxes) != len(names):
        print(f'!! {path}: нашлось {len(boxes)} предметов, ждали {len(names)}')
        for b in boxes: print('   ', b)
        return False
    for b, n in zip(boxes, names):
        x0, y0, x1, y1 = b
        c = im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad)))
        t = transparent(c, n in HOLES)
        bb = t.getchannel('A').getbbox()
        t = t.crop((max(0, bb[0] - 6), max(0, bb[1] - 6), min(t.width, bb[2] + 6), min(t.height, bb[3] + 6)))
        t.save(os.path.join(OUT, n + '.webp'), 'WEBP', quality=88, method=6)
        print(f'{n}: {t.size}')
    return True


def scene(path, name):
    im = Image.open(path).convert('RGB')
    if im.width > 1536:
        im = im.resize((1536, round(im.height * 1536 / im.width)), Image.LANCZOS)
    im.save(os.path.join(OUT, name + '.webp'), 'WEBP', quality=82, method=6)
    print(f'{name}: {im.size}')


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    n = int(sys.argv[1])
    for p in sys.argv[2:]:
        if n in SCENES:
            scene(p, SCENES[n])
        else:
            cut_sheet(p, SHEETS[n], col_gap=COL_GAP.get(n, 18))
