"""Нарезка листов Prepare 5: python3 cut.py <лист> <картинка> [<лист> <картинка> ...]
Ряды — по профилю строк (полоса рисунков, за ней полоса подписей). Внутри ряда —
кластеры по зазору (12 → 6 → 3); не сошлось — границы по самым пустым колонкам
около равных долей ряда. Выход: out/<лист>/<term>.png."""
import sys, os
import numpy as np
from PIL import Image
sys.path.insert(0, '..')
from lib import row, row_x, clusters_of, min_rgb_of, fname
from sheets import S

# Сцены с белым содержимым (лёд, снег): фон вырезается вместе с ним — заливаем сцену целиком
FILL = {'spectacular', 'snowstorm', 'recover', 'modern', 'clear up', 'come out', 'ancient', 'power', 'pump', 'crop', 'habitat', 'landscape', 'boarding school', 'break up', 'do well', 'do badly', 'environment', 'classroom', 'lunchtime', 'textbook', 'timetable', 'whiteboard', 'reach', 'sail', 'tour', 'on board', 'block', 'comment', 'follow', 'like', 'post', 'share', 'tag', 'take down', 'barbecue', 'bite', 'freeze', 'fry', 'grill', 'steam'}

# Листы, где генератор разложил картинки иначе, чем в промпте
# Границы клеток вручную: {лист: {номер ряда: [границы]}}; граница-ступенька (y, x_выше, x_ниже)
CUTS = {}

IMAGES = '/tmp/claude-0/-home-user-classroom/d4a2a0a4-519c-5b81-af84-18451bfcf9dd/images'

LAYOUT_SHEET = {}

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
            if prev_pic and y0 - prev < 15:
                y0 = y0 + 20 + int(np.argmin(c[y0 + 20:y0 + 90]))
            else:
                # светлые пряди и тени не дотягивают до порога 200 — берём весь белый
                # промежуток до предыдущей полосы (подписи), он гарантированно пустой
                y0 = max(0, prev + 2)
            nxt = bs[i + 1][0] if i + 1 < len(bs) else len(c)
            rows.append((y0, max(y1, nxt - 2)))
        prev, prev_pic = y1, pic
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

def erase_glued_captions(path):
    """Подпись вплотную к рисунку попадает в его полосу. Стираем её: связные куски
    тёмного цвета, целиком лежащие в нижних 50 px такой полосы и не выше 42 px, —
    это буквы. Части рисунка, заходящие в полосу, связаны с рисунком и остаются."""
    from scipy.ndimage import label
    im = Image.open(path).convert('RGB'); a = min_rgb_of(im)
    bs = bands(path); H = a.shape[0]; changed = False; arr = np.array(im)
    for i, (y0, y1) in enumerate(bs):
        if y1 - y0 <= 60: continue
        nxt = bs[i + 1] if i + 1 < len(bs) else None
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
    path = erase_glued_captions(path)
    title, note, items = S[sheet - 1]
    lay = LAYOUT_SHEET.get(sheet) or LAYOUT[len(items)]
    rows = split_rows(path, bands(path), len(lay))
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
            if len(clusters_of(path, y0, y1, 150, 235, g)[4]) == n:
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
    print(f'лист {sheet} {title}:'); print('\n'.join(report))

if __name__ == '__main__':
    a = sys.argv[1:]
    for i in range(0, len(a), 2):
        cut(int(a[i]), a[i + 1])
