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
HOLES = {'schoolbag', 'stethoscope', 'trophy', 'umbrella', 'billboard', 'cat',
         'an_rabbit', 'an_pig', 'an_chicken', 'an_horse', 'an_hamster', 'an_dog', 'an_cat',
         'sport_bike'}
# светящееся (солнце): прозрачность по светлоте, а не резкой маской
SOFT = {'w_sunny', 'w_windy'}


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


COL_GAP = {7: 3, 20: 5}


# листы-карточки со скруглёнными углами: режем по самой карточке и скругляем сами
CARD_SHEETS = {16, 17, 20, 22}
# у этих нейросеть съедает часть картинки (вода, ветер, тучи) — старый способ
OLD = {'sport_swim', 'w_rainy', 'w_snowy', 'w_cloudy', 'family_photo', 'wanted_poster'}
# портреты срезаны ровно снизу — ниже края одежды ничего не оставляем
FLAT_BOTTOM = ('fam_', 'suspect_')
_SESSION = None
# BiRefNet заметно чище isnet (бахрома шарфа, кудри), но ~45 с и ~9 ГБ памяти на картинку
NN_MODEL = os.environ.get('NN_MODEL', 'birefnet-general')


def nn_cut(im):
    """Вырезка фона нейросетью (rembg, BiRefNet) + снятие белой каймы с краёв."""
    global _SESSION
    from rembg import remove, new_session
    if _SESSION is None:
        _SESSION = new_session(NN_MODEL)
    t = remove(im.convert('RGB'), session=_SESSION)
    a = np.asarray(t).astype(float)
    al = a[..., 3:4] / 255.0
    rgb = a[..., :3]
    # полупрозрачный край смешан с белым фоном — вычитаем белое обратно
    safe = np.maximum(al, 0.05)
    un = (rgb - (1 - al) * 255.0) / safe
    edge = (al > 0) & (al < 0.98)
    rgb = np.where(edge, np.clip(un, 0, 255), rgb)
    alpha = a[..., 3]
    alpha = np.where(alpha < 60, 0, alpha)
    # мелкие отдельные пятнышки (крошки соседних предметов, тени) — убираем
    solid = alpha > 0
    h, w = solid.shape
    lab = np.zeros((h, w), np.int32); sizes = [0]
    for (y, x) in zip(*np.where(solid)):
        if lab[y, x]:
            continue
        k = len(sizes); lab[y, x] = k; n = 1; q = deque([(y, x)])
        while q:
            cy, cx = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < h and 0 <= nx < w and solid[ny, nx] and not lab[ny, nx]:
                    lab[ny, nx] = k; n += 1; q.append((ny, nx))
        sizes.append(n)
    big = max(sizes)
    keep = np.array([z >= big * 0.02 for z in sizes]); keep[0] = False
    alpha = np.where(keep[lab], alpha, 0)
    return Image.fromarray(np.dstack([rgb, alpha]).astype(np.uint8), 'RGBA')


def card(im, inset=4):
    """Карточка-сцена: внутренний прямоугольник без белых краёв + свои ровные скругления."""
    from PIL import ImageDraw
    a = np.asarray(im.convert('RGB'))
    # сама карточка — самый крупный связный кусок не-белого; огрызки соседних отбрасываем
    ink = a.min(axis=2) < 235
    h0, w0 = ink.shape
    lab = np.zeros((h0, w0), np.int32); best, bestk, k = 0, 0, 0
    for (y, x) in zip(*np.where(ink)):
        if lab[y, x]:
            continue
        k += 1; lab[y, x] = k; n = 1; q = deque([(y, x)])
        while q:
            cy, cx = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < h0 and 0 <= nx < w0 and ink[ny, nx] and not lab[ny, nx]:
                    lab[ny, nx] = k; n += 1; q.append((ny, nx))
        if n > best:
            best, bestk = n, k
    ys, xs = np.where(lab == bestk)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    white = ~(lab == bestk)
    # срезаем края, пока на краю больше 25 % не-карточки (скругления исходника)
    while y1 - y0 > 20 and white[y0, x0:x1].mean() > 0.25: y0 += 1
    while y1 - y0 > 20 and white[y1 - 1, x0:x1].mean() > 0.25: y1 -= 1
    while x1 - x0 > 20 and white[y0:y1, x0].mean() > 0.25: x0 += 1
    while x1 - x0 > 20 and white[y0:y1, x1 - 1].mean() > 0.25: x1 -= 1
    c = im.convert('RGB').crop((x0 + inset, y0 + inset, x1 - inset, y1 - inset))
    w, h = c.size
    r = int(min(w, h) * 0.12)
    big = Image.new('L', (w * 4, h * 4), 0)
    ImageDraw.Draw(big).rounded_rectangle((0, 0, w * 4 - 1, h * 4 - 1), r * 4, fill=255)
    c.putalpha(big.resize((w, h), Image.LANCZOS))
    return c


def cut_sheet(path, names, pad=24, col_gap=18, sheet_no=0):
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
    # куски одного предмета, разрезанные тонким местом (шея, ручка), — склеиваем
    merged = True
    while merged:
        merged = False
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a0, b0 = boxes[i], boxes[j]
                xo = min(a0[2], b0[2]) - max(a0[0], b0[0])
                gap = max(a0[1], b0[1]) - min(a0[3], b0[3])
                ar = lambda b: (b[2] - b[0]) * (b[3] - b[1])
                if xo > 0 and gap < 40 and min(ar(a0), ar(b0)) < 0.15 * max(ar(a0), ar(b0)):
                    boxes[i] = (min(a0[0], b0[0]), min(a0[1], b0[1]), max(a0[2], b0[2]), max(a0[3], b0[3]))
                    del boxes[j]; merged = True; break
            if merged:
                break
    if len(boxes) != len(names):
        print(f'!! {path}: нашлось {len(boxes)} предметов, ждали {len(names)}')
        for b in boxes: print('   ', b)
        return False
    for b, n in zip(boxes, names):
        x0, y0, x1, y1 = b
        c = im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad)))
        if sheet_no in CARD_SHEETS:
            t = card(c)
        elif n in SOFT:
            a = np.asarray(c).astype(int)
            al = np.clip((255 - a.min(axis=2)) * 4, 0, 255).astype(np.uint8)
            from PIL import ImageFilter
            # «закрытие» заливает белый блик в середине, мягкое свечение по краю остаётся
            cl = Image.fromarray(al).filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.MinFilter(21))
            if n == 'w_sunny':   # у ветра блика нет, «закрытие» там рисует квадраты
                al = np.maximum(al, np.asarray(cl))
            t = Image.fromarray(np.dstack([a.astype(np.uint8), al]), 'RGBA')
        elif n in OLD:
            t = transparent(c, n in HOLES)
        else:
            t = nn_cut(c)
            if n.startswith(FLAT_BOTTOM):
                ink = np.asarray(c.convert('RGB')).min(axis=2) < 235
                rows = np.where(ink.mean(axis=1) > 0.4)[0]
                if len(rows):
                    al = np.asarray(t).copy(); al[rows[-1] + 1:, :, 3] = 0
                    t = Image.fromarray(al, 'RGBA')
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
            cut_sheet(p, SHEETS[n], col_gap=COL_GAP.get(n, 18), sheet_no=n)
