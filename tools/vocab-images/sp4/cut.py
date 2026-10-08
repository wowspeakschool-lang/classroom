"""Нарезка листов Spotlight 4: python3 cut.py <лист> <картинка> [<лист> <картинка> ...]
Ряды — по профилю строк (полоса рисунков, за ней полоса подписей). Внутри ряда —
кластеры по зазору (12 → 6 → 3); не сошлось — границы по самым пустым колонкам
около равных долей ряда. Выход: out/<лист>/<term>.png."""
import sys, os
import numpy as np
from PIL import Image
sys.path.insert(0, '..')
from lib import row, row_x, clusters_of, min_rgb_of, fname
from sheets import S
import lib
# фон — только чисто-белое и бесцветное; белое внутри рисунка остаётся
lib.BG_MIN, lib.BG_GREY, lib.KEEP_SOFT = 250, 8, True

# Сцены с белым содержимым (лёд, снег): фон вырезается вместе с ним — заливаем сцену целиком
FILL_OLD = None  # заливка дыр больше не нужна: её заменил строгий порог фона
FILL = set()
# вырезать зажатый белый фон (не везде: белое внутри пузырей пропадало)
# белое, которое чистка кусков фона не трогает: облачка, снег, разметка, облака у края сцены
KEEP_WHITE = {'lemon meringue', 'ingredients', 'injection', 'tin', 'dairy', 'beanstalk', 'national park', 'sandy', 'cloudy', 'sight', 'Paris', 'Greece', 'Canada',
              'always', 'never', 'make sure', 'almost', 'Bon voyage', 'Excuse me', 'resolution'}
# ровно-белое внутри рисунка своё (облака в окне, мяч): снимаем только куски, выходящие наружу
PURE_EDGE = {'curtain', 'play sports', 'wake up'}
# сцены, где фон застрял между фигурами и под ногами: чистим жёстче
EXTRA = {'ski', 'zoo keeper', 'clean', 'wake up', 'postman', 'plump', 'carry', 'oats'}
HOLES = {'key', 'cherry', 'basket', 'oats', 'carry', 'plump', 'postman'}
# белая одежда без контура у края (халат): закрываем маску на N пикселей
CLOSE = {}
PURE_MN, PURE_MIN = 251, 120
# нарисованная тень под предметом: светлое тёплое пятно снаружи тёмного контура.
# Идём от прозрачного края по светлому, только в нижней половине и не глубже SHADOW_D
SHADOW_D = 30
NO_SHADOW = {'fleece', 'beanstalk', 'crew', 'cloudy', 'Greece', 'Florida', 'Germany', 'parade'}

# Листы, где генератор разложил картинки иначе, чем в промпте
# Границы клеток вручную: {лист: {номер ряда: [границы]}}; граница-ступенька (y, x_выше, x_ниже)
CUTS = {19: {1: [338, 694, (806, 1019, 1032)]},
        12: {1: [415, 808, (670, 1236, 1162)]},
        13: {0: [(200, 392, 366), 642, 993, 1322]},
        6: {0: [283, 526, (215, 910, 896), 1238], 1: [391, (660, 756, 738), 1116]},
        7: {1: [400, (800, 757, 765), 1112]}}

IMAGES = '/tmp/claude-0/-home-user-classroom/d4a2a0a4-519c-5b81-af84-18451bfcf9dd/images'

LAYOUT_SHEET = {}
ROW_TOP = {18: {0: 0}}
# мелкие отдельные детали — часть смысла (пустые кружки недели): не выкидывать как крошки
EDGE_D = 6
# рваный белый край (парус, стена): маску сглаживаем — закрываем рваные выемки, дыры, срезаем зубцы
SMOOTH = {'crew': 14, 'wake up': 18}
CUT_BOTTOM = {'sound': 0.83}  # остаток подписи под рисунком
NO_SPECK = {'usually', 'sometimes', 'never'}

LAYOUT = {6: [3, 3], 7: [4, 3], 8: [4, 4], 9: [5, 4], 10: [5, 5], 11: [4, 4, 3], 12: [4, 4, 4], 13: [5, 4, 4]}

def bands(path):
    a = min_rgb_of(Image.open(path))
    ink = (a < 200).sum(1) > 3
    out, s = [], None
    for y, v in enumerate(ink):
        if v and s is None: s = y
        if not v and s is not None:
            if y - s > 4: out.append((s, y))
            s = None
    if s is not None: out.append((s, len(ink)))
    return out

def split_rows(path, bs, n_rows):
    """Полосы рисунков — выше 60 px. Если полоса началась вплотную к предыдущей,
    в её верх влипла подпись прошлого ряда: срезаем по самой пустой строке под ней."""
    c = (min_rgb_of(Image.open(path)) < 200).sum(1)
    rows, prev, prev_pic = [], -100, False
    for i, (y0, y1) in enumerate(bs):
        pic = y1 - y0 > 60
        if pic:
            if prev_pic and y0 - prev < 25:
                y0 = y0 + 20 + int(np.argmin(c[y0 + 20:y0 + 90]))
            else:
                # светлые пряди и тени не дотягивают до порога 200 — берём весь белый
                # промежуток до предыдущей полосы (подписи), он гарантированно пустой
                y0 = max(0, prev + 2)
            nxt = bs[i + 1][0] if i + 1 < len(bs) else len(c)
            rows.append((y0, max(y1, nxt - 2)))
        prev, prev_pic = y1, pic
    # подписи ряда вплотную к рисункам следующего — две полосы слиплись в одну:
    # режем самую высокую по самой пустой строке в её середине
    # высокая подпись (две строки) сошла за полосу рисунка — выкидываем самые низкие полосы
    while len(rows) > n_rows:
        k = min(range(len(rows)), key=lambda i: rows[i][1] - rows[i][0])
        if rows[k][1] - rows[k][0] > 120: break
        del rows[k]
    while len(rows) < n_rows:
        k = max(range(len(rows)), key=lambda i: rows[i][1] - rows[i][0])
        a0, a1 = rows[k]; h = a1 - a0
        lo, hi = a0 + int(h * .35), a0 + int(h * .65)
        cut = lo + int(np.argmin(c[lo:hi]))
        rows[k:k + 1] = [(a0, cut), (cut + 1, a1)]
    if len(rows) != n_rows:
        raise SystemExit(f'рядов {len(rows)} вместо {n_rows}: {bs}')
    return rows

def column_cuts(path, y0, y1, n):
    a = min_rgb_of(Image.open(path))[y0:y1] < 235
    c = a.sum(0); xs = np.where(c > 0)[0]; L, R = xs.min(), xs.max()
    cuts = []
    for k in range(1, n):
        mid = L + (R - L) * k / n; w = (R - L) / n * 0.25
        lo, hi = int(mid - w), int(mid + w)
        cuts.append(lo + int(np.argmin(c[lo:hi])))
    return cuts, [int(c[x]) for x in cuts]

def erase_glued_captions(path, rows=None):
    """Подпись вплотную к рисунку попадает в его полосу. Стираем её: связные куски
    тёмного цвета, целиком лежащие в нижних 50 px такой полосы и не выше 42 px, —
    это буквы. Части рисунка, заходящие в полосу, связаны с рисунком и остаются."""
    from scipy.ndimage import label
    im = Image.open(path).convert('RGB'); a = min_rgb_of(im)
    bs = rows or bands(path); H = a.shape[0]; changed = False; arr = np.array(im)
    for i, (y0, y1) in enumerate(bs):
        y1 = min(y1, H - 3)
        if y1 - y0 <= 60: continue
        nxt = bs[i + 1] if i + 1 < len(bs) and not rows else None
        if nxt and nxt[1] - nxt[0] <= 60 and nxt[0] - y1 < 25: continue  # подпись отдельно
        s0 = max(y0, y1 - 62)
        lab, n = label(a[y0:y1 + 3] < 235)
        for k in range(1, n + 1):
            ys, xs = np.where(lab == k)
            px = arr[y0:y1 + 3][lab == k].astype(int)
            grey = (px.max(1) - px.min(1)).mean() < 25  # буквы чёрные; капли, перья — цветные
            if ys.min() + y0 >= s0 and ys.max() - ys.min() <= 52 and a[y0:y1 + 3][lab == k].min() < 80 and grey:
                arr[y0:y1 + 3][lab == k] = 255; changed = True
    if not changed: return path
    out = '/tmp/claude-0/-home-user-classroom/d4a2a0a4-519c-5b81-af84-18451bfcf9dd/scratchpad/clean_' + os.path.basename(path) + '.png'
    Image.fromarray(arr).save(out); return out

# Предметы с нарисованной мягкой тенью рядом: оставляем только то, что внутри контура
OUTLINE_ONLY = set()

def outline_only(png):
    from scipy.ndimage import binary_dilation, binary_erosion, binary_fill_holes
    im = np.array(Image.open(png).convert('RGBA'))
    dark = (im[..., :3].min(2) < 80) & (im[..., 3] > 0)
    solid = binary_erosion(binary_fill_holes(binary_dilation(dark, iterations=3)), iterations=2)
    from scipy.ndimage import label
    lab, n = label(solid)
    if n > 1:  # крапинки тени снаружи контура — отдельные мелкие куски
        sizes = np.bincount(lab.ravel()); sizes[0] = 0
        solid = lab == sizes.argmax()
    im[..., 3] = np.where(solid, 255, 0).astype(np.uint8)
    Image.fromarray(im).save(png)

def cut(sheet, path, out='out'):
    title, note, items = S[sheet - 1]
    lay = LAYOUT_SHEET.get(sheet) or LAYOUT[len(items)]
    rows = split_rows(path, bands(path), len(lay))
    for ri, y in ROW_TOP.get(sheet, {}).items():  # мелкая полоса над рисунком (кружки недели) — не подпись
        rows[ri] = (y, rows[ri][1])
    # подписи, слипшиеся со следующим рядом, сидят внизу полос ряда — стираем по рядам
    path = erase_glued_captions(path, rows)
    k = 0; report = []
    for ri, ((y0, y1), n) in enumerate(zip(rows, lay)):
        words = [t for _, t, _ in items[k:k + n]]; k += n
        d = f'{out}/{sheet}'
        ok = False
        if ri in CUTS.get(sheet, {}):
            row_x(path, y0, y1, words, d, CUTS[sheet][ri], fill=tuple(w for w in words if w in FILL), fill_thr=253, fill_close=8)
            report.append(f'  ряд {y0}-{y1}: {n} шт, границы вручную {CUTS[sheet][ri]}'); continue
        need_fill = tuple(w for w in words if w in FILL)
        if need_fill:
            for g in (12, 6, 3):
                cl = clusters_of(path, y0, y1, 150, 235, g)[4]
                if len(cl) == n:
                    cuts = [(a['x1'] + b['x0']) // 2 for a, b in zip(cl, cl[1:])]
                    row_x(path, y0, y1, words, d, cuts, fill=need_fill, fill_thr=253, fill_close=8)
                    report.append(f'  ряд {y0}-{y1}: {n} шт, зазор {g}, заливка {need_fill}'); ok = True; break
        for g in (() if ok else (12, 6, 3)):
            cl = clusters_of(path, y0, y1, 150, 235, g)[4]
            ws = [k['x1'] - k['x0'] for k in cl]
            # кластеры разной ширины — это половинки одной картинки и две слипшиеся
            if len(cl) == n and max(ws) < 1.7 * min(ws):
                row(path, y0, y1, words, d, gap=g, min_area=150); ok = True
                report.append(f'  ряд {y0}-{y1}: {n} шт, зазор {g}'); break
        if not ok:
            cuts, ink = column_cuts(path, y0, y1, n)
            row_x(path, y0, y1, words, d, cuts, fill=need_fill, fill_thr=253, fill_close=8)
            report.append(f'  ряд {y0}-{y1}: {n} шт, ПО КОЛОНКАМ {cuts} чернил {ink}')
    # перерисованные отдельными картинками — images_map.txt: "<картинка> <лист>:<слово>"
    imgdir = os.path.dirname(path) if 'clean_' not in path else IMAGES
    for line in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images_map.txt')):
        f, _, rest = line.strip().partition(' ')
        if ':' in rest and int(rest.split(':')[0]) == sheet:
            word = rest.split(':', 1)[1]; src = os.path.join(IMAGES, f + '.webp')
            from widen import row as wrow
            y0, y1 = bands(src)[0]
            wrow(src, y0, y1, [word], f'{out}/{sheet}', gap=400, min_area=150)
            report.append(f'  {word}: заменён картинкой {f}')
    for _, t, _ in items:
        if t in OUTLINE_ONLY:
            outline_only(f'{out}/{sheet}/{fname(t)}'); report.append(f'  {t}: по контуру')
    for _, t, _ in items:
        p = f'{out}/{sheet}/{fname(t)}'
        if os.path.exists(p) and t not in OUTLINE_ONLY:
            clean_png(p)
        if os.path.exists(p) and t in CLOSE:
            from scipy.ndimage import binary_closing, binary_fill_holes
            im = np.array(Image.open(p).convert('RGBA'))
            m = binary_fill_holes(binary_closing(im[..., 3] > 40, iterations=CLOSE[t]))
            im[m & (im[..., 3] <= 40), :3] = 255; im[m, 3] = 255
            Image.fromarray(im).save(p)
    for _, t, _ in items:
        p = f'{out}/{sheet}/{fname(t)}'
        if t in SMOOTH and os.path.exists(p):
            from scipy.ndimage import binary_closing, binary_opening, binary_fill_holes, gaussian_filter
            im = np.array(Image.open(p).convert('RGBA')).astype(float)
            r = SMOOTH[t]; yy, xx = np.mgrid[-r:r + 1, -r:r + 1]; disk = xx ** 2 + yy ** 2 <= r * r
            m0 = im[..., 3] > 40
            m = binary_fill_holes(binary_closing(np.pad(m0, r), structure=disk))[r:-r, r:-r]
            m = binary_opening(m, structure=disk[::2, ::2]) | (m0 & (im[..., :3].min(-1) < 200))
            add = m & ~m0
            dark = im[..., :3].max(-1) < 30  # пустое поле квадрата — без цвета
            im[add & dark, :3] = 250
            im[add, 3] = 255
            soft = gaussian_filter(m.astype(float), 1.2)
            im[..., 3] = np.where(m, np.minimum(255, np.maximum(im[..., 3], soft * 255)), 0)
            im[..., 3] = np.minimum(im[..., 3], soft * 255 + 0)
            Image.fromarray(im.clip(0, 255).astype(np.uint8)).save(p)
            report.append(f'  {t}: край сглажен')
    print(f'лист {sheet} {title}:'); print('\n'.join(report))


def clean_png(p, peel=12, pale=188, grey=30, speck=0.004, pure=250):
    """Белая кайма и крошки после вырезки: снимаем по контуру светлые бесцветные
    пиксели (не глубже peel), выкидываем мелкие островки отдельно от рисунка."""
    from scipy.ndimage import label, binary_dilation
    im = np.array(Image.open(p).convert('RGBA')).astype(np.int32)
    rgb, a = im[..., :3], im[..., 3]
    mn, mx = rgb.min(-1), rgb.max(-1)
    # фон листа — ровный 252-255 без оттенка; нарисованное белое (паруса, снег, скафандр)
    # с фактурой и тоном. Любой такой ровный кусок крупнее PURE_MIN — фон, где бы ни лежал:
    # между ногами, в кольце ключа, между стеблями
    if not p.endswith(tuple(f'/{fname(w)}' for w in KEEP_WHITE)):
        lab, n = label((a > 40) & (mn >= PURE_MN) & (mx - mn <= 4))
        if n:
            sz = np.bincount(lab.ravel()); sz[0] = 0
            big = np.where(sz >= PURE_MIN)[0]
            if p.endswith(tuple(f'/{fname(w)}' for w in PURE_EDGE)):
                big = np.intersect1d(big, np.unique(lab[binary_dilation(a <= 40, iterations=2)]))
            a[np.isin(lab, big)] = 0
    if not p.endswith(tuple(f'/{fname(w)}' for w in NO_SHADOW)):
        from scipy.ndimage import distance_transform_edt
        out = a <= 40
        ys = np.where((~out).any(1))[0]
        if len(ys):
            y_mid = ys[0] + (ys[-1] - ys[0]) * 0.5
            light = (~out) & (mn >= 140) & (rgb.sum(-1) >= 3 * 180) & (mx - mn <= 90)
            light[:int(y_mid)] = False
            labl, _ = label(light)
            touch = np.unique(labl[binary_dilation(out, iterations=2) & light]); touch = touch[touch > 0]
            a[np.isin(labl, touch) & (distance_transform_edt(~out) <= SHADOW_D)] = 0
    whitish = (mn >= pale) & (mx - mn <= grey)
    for _ in range(peel):
        solid = a > 128
        edge = solid & binary_dilation(~solid)
        hit = edge & whitish
        if not hit.any():
            break
        a[hit] = 0
    # мягкий край: светлым пикселям у контура — частичная прозрачность
    solid = a > 128
    edge = solid & binary_dilation(~solid)
    soft = edge & (mn >= 190)
    a[soft] = np.minimum(a[soft], np.clip((255 - mn[soft]) * 4, 60, 255))
    # дырки: зажатый между руками и предметами чистый фон, обведённый контуром
    lab, n = label((a > 128) & (mn >= 238) & (mx - mn <= 14))
    for i in range(1, n + 1):
        c = lab == i
        if c.sum() < 60 or mn[c].mean() < pure:
            continue
        ring = binary_dilation(c, iterations=3) & ~c
        if p.endswith(tuple(f'/{fname(w)}' for w in HOLES)):  # только по списку: белое внутри пузырей и бумаги — тоже «дырка»
            a[c] = 0
    # куски фона, отрезанные от края тенью или землёй: светлое и бесцветное,
    # связанное с прозрачным краем через светло-серое
    if not p.endswith(tuple(f'/{fname(w)}' for w in KEEP_WHITE)):
        from scipy.ndimage import distance_transform_edt
        out = a <= 40
        M = (~out) & (mn >= 215) & (mx - mn <= 20)
        labm, _ = label(M)
        touch = np.unique(labm[binary_dilation(out) & M]); touch = touch[touch > 0]
        T = np.isin(labm, touch)
        dist = distance_transform_edt(~out)
        a[T & (((mn >= 245) & (mx - mn <= 10)) | ((mn >= 225) & (dist <= 6)))] = 0
    if p.endswith(tuple(f'/{fname(w)}' for w in EXTRA)):
        out = a <= 40
        W = (~out) & (mn >= 244) & (mx - mn <= 10)
        labw, nw = label(W); sz = np.bincount(labw.ravel())
        a[np.isin(labw, [i for i in range(1, nw + 1) if sz[i] >= 60])] = 0
        out = a <= 40
        M = (~out) & (mn >= 232) & (mx - mn <= 14)
        labm, _ = label(M)
        touch = np.unique(labm[binary_dilation(out) & M]); touch = touch[touch > 0]
        a[np.isin(labm, touch)] = 0
    # кайма: у края рисунок акварельно переходит в белый. Вычитаем белый из цвета
    # цвет не трогаем (иначе серое у белых предметов темнеет в кольцо), только прозрачность:
    # чем белее пиксель у края, тем прозрачнее
    from scipy.ndimage import distance_transform_edt
    near = (a > 40) & (distance_transform_edt(a > 40) <= EDGE_D)
    if near.any():
        c = rgb[near].astype(float)
        al = np.clip((255 - c.min(-1)) / 255 * 1.6, 0, 1)  # белое → 0, насыщенное и тёмное → 1
        al = np.where(c.min(-1) < 120, 1, al)
        a[near] = np.minimum(a[near], (al * 255).astype(np.int32))
    # полупрозрачное светлое за контуром: на тёмном фоне читается серой каймой — убираем целиком
    rgb2 = im[..., :3]; mn2, mx2 = rgb2.min(-1), rgb2.max(-1)
    a[(a < 235) & (mn2 >= 140) & (mx2 - mn2 <= 70)] = 0
    for w, frac in CUT_BOTTOM.items():
        if p.endswith(f'/{fname(w)}'): a[int(a.shape[0] * frac):] = 0
    lab, n = label(a > 40)
    if n > 1 and not p.endswith(tuple(f'/{fname(w)}' for w in NO_SPECK)):
        sizes = np.bincount(lab.ravel()); sizes[0] = 0
        big = sizes.max()
        small = np.isin(lab, np.where((sizes < speck * a.size) & (sizes < big))[0])
        a[small] = 0
    im[..., 3] = a
    Image.fromarray(im.astype(np.uint8), 'RGBA').save(p)

if __name__ == '__main__':
    a = sys.argv[1:]
    for i in range(0, len(a), 2):
        cut(int(a[i]), a[i + 1])
