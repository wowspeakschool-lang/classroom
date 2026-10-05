#!/usr/bin/env python3
"""Нарезка листов Go Getter 1 на отдельные картинки.

Лист — одна сгенерированная картинка с сеткой ячеек внутри. Скрипт находит
предмет каждой ячейки как связную фигуру и вырезает её целиком, потом кладёт
webp в media/gg1/uN/. Сцены (grid 1x1) просто масштабируются.

Почему не режем ровно по сетке. Генератор часто выводит предмет за свою
ячейку: купол медузы заходил в ячейку осьминога, луч звезды и хвост конька —
в ряд выше, так же вылезали вентилятор, щётка и зонт. Резать по линии значит
отрезать им верхушку, а резать с запасом — тащить в карточку кусок соседа.
Поэтому строим маску непустых пикселей, гасим линии сетки, размечаем связные
области и отдаём ячейке те из них, которые лежат в ней большей частью.

Переприменяем: файлы всегда переписываются заново.

  python3 tools/gg1_cut.py --src <папка с листами> [--only Л8.4 Л8.5]
"""
import argparse, os, sys
from collections import deque
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CARD = 400          # длинная сторона карточки, px (диапазон проекта 180-420)
SCENE = 880         # длинная сторона сцены, px (диапазон 760-900)
Q_CARD, Q_SCENE = 82, 80
PAD = 0.02          # поле вокруг предмета, доля стороны ячейки
WHITE = 244         # ниже этого предмет, выше — фон листа
MIN_PART = 0.004    # область меньше 0.4% ячейки — мусор, не предмет

# лист: (номер листа, юнит, строк, колонок, имена ячеек слева направо сверху вниз)
# None вместо имени — ячейку пропустить (пустая клетка листа).
# Файл листа ищется в --src по номеру: «Л0.1.png», «L0.1.webp», «0.1.jpg» —
# Анна подписывает присланные картинки номером листа.
SHEETS = [
    # --- UNIT 0 · GET STARTED! ---
    ("Л0.1", "u0", 3, 3, ["obj_book", "obj_coloured_pencil", "obj_notebook",
                          "obj_pen", "obj_pencil", "obj_pencil_case",
                          "obj_sharpener", "obj_rubber", "obj_ruler"]),
    ("Л0.2", "u0", 3, 3, ["obj_scissors", "obj_sandwich", "obj_bag",
                          "obj_bin", "obj_board", "obj_chair",
                          "obj_clock", "obj_desk", "obj_apple"]),
    ("Л0.3", "u0", 2, 3, ["col_red_pen", "col_blue_bag", "col_yellow_ruler",
                          "col_green_notebook", "col_pink_pencil_case", "col_orange_bag"]),
]


def sheet_file(src, sid):
    """Файл листа по его номеру: Л0.1 / L0.1 / 0.1 с любым расширением картинки."""
    num = sid[1:]
    stems = {sid, "L" + num, num}
    for f in sorted(os.listdir(src)):
        stem, ext = os.path.splitext(f)
        if stem in stems and ext.lower() in (".png", ".webp", ".jpg", ".jpeg"):
            return os.path.join(src, f)
    return None


def _line_is_clean(vals, spread=18):
    """Строгая проверка для чистки краёв готовой карточки.

    Нестрогая (85-90% светлых точек) годится, чтобы найти линию сетки внутри
    листа: предмет местами её пересекает. Но для края карточки она губительна:
    строка с кончиком антенны — это белое поле и несколько синих пикселей,
    то есть «почти всё светлое», и чистка снимала шапочку по строчке за раз.
    У настоящего поля тёмных точек нет вовсе.
    """
    if not vals:
        return False
    if min(vals) < 185:
        return False
    g = sorted(vals)
    return g[min(len(g) - 1, int(len(g) * 0.95))] - g[int(len(g) * 0.05)] <= spread


def _line_is_divider(vals, share=0.85, spread=20):
    """Похожа ли линия на разделитель сетки.

    Судим по разбросу без крайних значений: min/max ловил единичный тёмный
    пиксель (тень предмета, пересёкшего линию) и браковал линию целиком.
    Между двумя пастельными ячейками шов вообще не белый, а серый 200-240,
    поэтому важен не цвет, а ровность линии по всей длине.
    """
    if not vals:
        return False
    good = sorted(g for g in vals if 185 <= g <= 255)
    if len(good) < share * len(vals):
        return False
    lo = good[max(0, int(len(good) * 0.05))]
    hi = good[min(len(good) - 1, int(len(good) * 0.95))]
    return hi - lo <= spread


def divider_band(grey, pos, vertical, search, lo=None, hi=None):
    """Полоса разделителя рядом с расчётной границей ячейки, или None.

    lo/hi ограничивают отрезок линии. Это важно: вертикальная линия проходит
    через все ряды листа, и достаточно одному предмету наехать на неё в своём
    ряду, чтобы вся линия перестала считаться разделителем. Поэтому границу
    ищем отдельно для каждой ячейки, на её собственном отрезке.
    """
    px = grey.load()
    w, h = grey.size
    limit = w if vertical else h
    span = h if vertical else w
    lo = 0 if lo is None else max(0, lo)
    hi = span if hi is None else min(span, hi)
    step = max(1, (hi - lo) // 200)

    def line(i):
        if vertical:
            return [px[i, y] for y in range(lo, hi, step)]
        return [px[x, i] for x in range(lo, hi, step)]

    hit = None
    for d in range(search + 1):
        for i in (pos - d, pos + d):
            if 0 < i < limit - 1 and _line_is_divider(line(i)):
                hit = i
                break
        if hit is not None:
            break
    if hit is None:
        return None
    # Полосу не расширяем без края: у пастельных ячеек фон сам по себе ровный,
    # и разделитель «разрастался», съедая картинку. 2% считались от всего
    # листа, а не от ячейки — полоса выходила в 50 px, и клин вставал внутри
    # ячейки: у дельфина отрезало нос. Разделитель — это несколько пикселей.
    grow = max(3, round(span * 0.005))
    a = b = hit
    while a > hit - grow and a > 0 and _line_is_divider(line(a - 1)):
        a -= 1
    while b < hit + grow and b < limit - 1 and _line_is_divider(line(b + 1)):
        b += 1
    return a, b


def best_seam(grey, pos, vertical, search, lo, hi):
    # Если ровной линии нет (предмет пересекает её во многих местах, как брызги
    # дельфинов у самого шва), всё равно нужна опорная граница: берём в окне
    # поиска самый ровный столбец или строку — шов ровнее картинки по обе
    # стороны от него.
    px = grey.load()
    w, h = grey.size
    limit = w if vertical else h
    step = max(1, (hi - lo) // 150)

    def spread(i):
        if vertical:
            vals = sorted(px[i, y] for y in range(lo, hi, step))
        else:
            vals = sorted(px[x, i] for x in range(lo, hi, step))
        a = vals[int(len(vals) * 0.1)]
        b = vals[min(len(vals) - 1, int(len(vals) * 0.9))]
        return b - a

    best, score = pos, None
    for d in range(-search, search + 1):
        i = pos + d
        if 0 < i < limit - 1:
            sc = spread(i)
            if score is None or sc < score:
                best, score = i, sc
    return best, best


def label_parts(mask, w, h):
    """Разметить связные области маски. Возвращает (метки, список областей)."""
    labels = [0] * (w * h)
    parts = []
    for start in range(w * h):
        if not mask[start] or labels[start]:
            continue
        n = len(parts) + 1
        labels[start] = n
        q = deque([start])
        x0 = x1 = start % w
        y0 = y1 = start // w
        size = 0
        while q:
            i = q.popleft()
            size += 1
            x, y = i % w, i // w
            x0, x1 = min(x0, x), max(x1, x)
            y0, y1 = min(y0, y), max(y1, y)
            for j in (i - 1 if x else -1, i + 1 if x + 1 < w else -1,
                      i - w if y else -1, i + w if y + 1 < h else -1):
                if j >= 0 and mask[j] and not labels[j]:
                    labels[j] = n
                    q.append(j)
        parts.append({"size": size, "box": (x0, y0, x1 + 1, y1 + 1)})
    return labels, parts


def shave_edge(im, depth=4):
    """НЕ ИСПОЛЬЗУЕТСЯ. Снять с краёв ровную кромку, отличающуюся от соседних
    пикселей. Идея не сработала: у фотографии крайняя строка законно отличается
    от того, что в восьми пикселях внутрь (небо, вода, градиент), и правило
    начинало срезать саму картинку. Оставлено как след неудачной попытки.

    После всех обрезок у части карточек оставалась полоска шириной 1-3 px:
    остаток поля листа. Цвет у неё бывает любой — от серого до почти белого,
    поэтому судим не по цвету, а по двум признакам сразу: полоса ровная по
    всей длине и заметно отличается от линии в восьми пикселях внутрь.
    """
    px = im.load()
    w, h = im.size

    def line(side, d):
        if side == "l":
            return [px[d, y] for y in range(h)]
        if side == "r":
            return [px[w - 1 - d, y] for y in range(h)]
        if side == "t":
            return [px[x, d] for x in range(w)]
        return [px[x, h - 1 - d] for x in range(w)]

    def flat(vals):
        g = sorted(sum(v) / 3 for v in vals)
        return g[int(len(g) * 0.05)], g[min(len(g) - 1, int(len(g) * 0.95))], sum(g) / len(g)

    cut = {"l": 0, "r": 0, "t": 0, "b": 0}
    for side in "lrtb":
        span = w if side in "lr" else h
        for d in range(min(depth, span // 6)):
            lo, hi, avg = flat(line(side, d))
            if hi - lo > 18:
                break
            if abs(avg - flat(line(side, d + 8))[2]) <= 8:
                break
            cut[side] = d + 1
    if not any(cut.values()):
        return im
    return im.crop((cut["l"], cut["t"], w - cut["r"], h - cut["b"]))


def cut_foreign_strip(im, depth=0.25):
    # Последняя проверка карточки: не осталось ли вдоль края куска чужой
    # картинки. Признак — ровный шов, а за ним область, непохожая на то, что
    # внутри. Ищем глубоко, до четверти стороны: у фотографий во весь кадр
    # полоса соседа бывает широкой, и прежние чистки её не доставали.
    w, h = im.size
    px = im.load()

    def scan(side):
        size = w if side in "lr" else h
        across = h if side in "lr" else w
        limit = max(2, int(size * depth))
        step = max(1, across // 160)
        means, flats = [], []
        for d in range(limit + int(size * 0.15) + 2):
            if side == "l":
                vals = [px[d, y] for y in range(0, h, step)]
            elif side == "r":
                vals = [px[w - 1 - d, y] for y in range(0, h, step)]
            elif side == "t":
                vals = [px[x, d] for x in range(0, w, step)]
            else:
                vals = [px[x, h - 1 - d] for x in range(0, w, step)]
            n = len(vals)
            means.append([sum(v[i] for v in vals) / n for i in range(3)])
            g = sorted(sum(v) / 3 for v in vals)
            flats.append(g[min(n - 1, int(n * 0.9))] - g[int(n * 0.1)])
        # префиксные суммы по средним, чтобы не пересчитывать полосы
        pref = [[0.0, 0.0, 0.0]]
        for m in means:
            pref.append([pref[-1][i] + m[i] for i in range(3)])

        def avg(a, b):
            b = min(b, len(means))
            k = max(1, b - a)
            return [(pref[b][i] - pref[a][i]) / k for i in range(3)]

        best = 0
        inner_w = max(4, int(size * 0.15))
        min_strip = max(2, int(size * 0.015))
        for d in range(min_strip, limit):
            if flats[d] > 18:
                continue
            # Шов между ячейками светлый и бесцветный — белый или серый.
            # Без «светлый» правило резало по контуру самой фигуры (у
            # прямоугольника отрезало половину карточки), без «бесцветный» —
            # по ровному пастельному фону: у мыши между коробками от
            # карточки оставалась полоска в середине.
            mr, mg, mb = means[d]
            if (mr + mg + mb) / 3 < 225:
                continue
            if max(mr, mg, mb) - min(mr, mg, mb) > 12:
                continue
            outer, inner = avg(0, d), avg(d + 1, d + 1 + inner_w)
            # кусок соседа — это картинка, а не поле: если за швом почти белое,
            # резать нечего. Без этого у щётки срезало щетину — над ней белое
            # поле, и оно отличалось от синей ручки достаточно, чтобы сойти
            # за чужую картинку.
            if sum(outer) / 3 > 232:
                continue
            if sum(abs(a - b) for a, b in zip(outer, inner)) > 36:
                best = d + 1
        return best

    cut = {side: scan(side) for side in "lrtb"}
    if not any(cut.values()):
        return im
    x0, y0 = cut["l"], cut["t"]
    x1, y1 = w - cut["r"], h - cut["b"]
    if x1 - x0 < w * 0.5 or y1 - y0 < h * 0.5:
        return im
    return im.crop((x0, y0, x1, y1))


def cut_off_line(im, depth=10):
    """Срезать край до серой линии сетки, если она прячется в нескольких
    пикселях от края (снаружи от неё бывает белая кромка, и построчная
    чистка до линии не доходит)."""
    px = im.load()
    w, h = im.size

    def grey(vals):
        return _line_is_clean([sum(v) / 3 for v in vals], spread=16)

    left = right = top = bottom = 0
    for d in range(min(depth, w // 4)):
        if grey([px[d, y] for y in range(h)]):
            left = d + 1
        if grey([px[w - 1 - d, y] for y in range(h)]):
            right = d + 1
    for d in range(min(depth, h // 4)):
        if grey([px[x, d] for x in range(w)]):
            top = d + 1
        if grey([px[x, h - 1 - d] for x in range(w)]):
            bottom = d + 1
    if not (left or right or top or bottom):
        return im
    return im.crop((left, top, w - right, h - bottom))


def strip_lines(im, limit=10):
    """Снять с краёв ровные светлые линии — остатки сетки."""
    px = im.load()
    w, h = im.size
    left, right, top, bottom = 0, w, 0, h

    def line(vals):
        # строго: ни одной тёмной точки, иначе снимаем кончик предмета
        return _line_is_clean([sum(v) / 3 for v in vals], spread=16)

    for _ in range(limit):
        if right - left < 8 or bottom - top < 8:
            break
        moved = False
        if line([px[left, y] for y in range(top, bottom)]):
            left += 1; moved = True
        if line([px[right - 1, y] for y in range(top, bottom)]):
            right -= 1; moved = True
        if line([px[x, top] for x in range(left, right)]):
            top += 1; moved = True
        if line([px[x, bottom - 1] for x in range(left, right)]):
            bottom -= 1; moved = True
        if not moved:
            break
    return im.crop((left, top, right, bottom))


def drop_strays(im, thr=WHITE):
    """Убрать с краёв обрывок соседней картинки.

    Бывает, что предметы соседних ячеек касаются друг друга в месте, где
    линия сетки прервана: осьминог с медузой, черепаха с коньком, сапоги
    с зонтом. Тогда это одна связная фигура, и в карточку попадает край
    чужого предмета — тонкий и отделённый чистым просветом.
    """
    w, h = im.size
    g = im.convert("L").point(lambda v: 0 if v >= thr else 255)
    px = g.load()
    # по краям кадра может остаться вертикальная линия сетки: она даёт тёмную
    # точку в каждой строке, и «пустых» строк не находится вовсе. Поэтому
    # профиль считаем по середине кадра, отступив по 6% с каждой стороны.
    mx, my = round(w * 0.06), round(h * 0.06)
    xs = list(range(mx, w - mx, max(1, w // 300)))
    ys = list(range(my, h - my, max(1, h // 300)))
    need_x, need_y = max(3, len(xs) // 50), max(3, len(ys) // 50)
    rows = [sum(1 for x in xs if px[x, y]) >= need_x for y in range(h)]
    cols = [sum(1 for y in ys if px[x, y]) >= need_y for x in range(w)]

    def cut(flags, size):
        thin, gap = size * 0.25, size * 0.008
        i = 0
        while i < size and not flags[i]:
            i += 1
        j = i
        while j < size and flags[j]:
            j += 1
        if j - i > thin or j >= size:
            return 0
        k = j
        while k < size and not flags[k]:
            k += 1
        return j if k - j >= gap and k < size else 0

    top, left = cut(rows, h), cut(cols, w)
    bottom, right = h - cut(rows[::-1], h), w - cut(cols[::-1], w)
    if right - left < w * 0.4 or bottom - top < h * 0.4:
        return im
    return im.crop((left, top, right, bottom))


def trim_white(im, pad, thr=WHITE):
    box = im.convert("L").point(lambda v: 0 if v >= thr else 255).getbbox()
    if box is None:
        return im
    w, h = im.size
    return im.crop((max(0, box[0] - pad), max(0, box[1] - pad),
                    min(w, box[2] + pad), min(h, box[3] + pad)))


def add_margin(im, pad):
    # Чистки края снимают и ровное белое поле вокруг предмета — он упирается
    # в край и выглядит срезанным, даже когда цел. Поэтому у предметов на
    # белом поле возвращаем его обратно: рисуем кадр чуть больше и кладём
    # предмет в середину. Фотографий во весь кадр это не касается.
    w, h = im.size
    px = im.load()
    # белый ли фон — судим по углам: по краям уже может лежать сам предмет,
    # и среднее по всей рамке тогда занижено, а поле всё равно нужно
    c = max(6, min(w, h) // 20)
    corners = []
    for cx in (0, w - c):
        for cy in (0, h - c):
            corners += [px[x, y] for x in range(cx, cx + c) for y in range(cy, cy + c)]
    if min(sum(v) / 3 for v in corners) < 235:
        return im
    out = Image.new("RGB", (w + 2 * pad, h + 2 * pad), (255, 255, 255))
    out.paste(im, (pad, pad))
    return out


def cut_sheet(sheet, rows, cols):
    """Вернуть список вырезанных ячеек листа (None там, где ячейка пуста)."""
    W, H = sheet.size
    grey = sheet.convert("L")
    cw, ch = W / cols, H / rows
    # окно поиска линии: у части листов сетка заметно смещена относительно
    # расчётной границы (в Л7.3 — на 30 px), при 4% линия не находилась вовсе
    search = max(6, round(min(cw, ch) * 0.08))

    # границы ищем для каждой ячейки на её отрезке линии
    vband = {}      # (колонка-граница, ряд) -> полоса
    hband = {}      # (ряд-граница, колонка) -> полоса
    for c in range(1, cols):
        for r in range(rows):
            vband[(c, r)] = divider_band(grey, round(c * cw), True, search,
                                         round(r * ch), round((r + 1) * ch))
    for r in range(1, rows):
        for c in range(cols):
            hband[(r, c)] = divider_band(grey, round(r * ch), False, search,
                                         round(c * cw), round((c + 1) * cw))

    k = max(1, round(min(W, H) / 400))           # разметку ведём на уменьшенной копии
    sw, sh = W // k, H // k
    # Уменьшаем по самому тёмному пикселю окрестности, а не усреднением:
    # антенна рации шириной в восемь пикселей при усреднении светлела, теряла
    # связь с корпусом, оставалась отдельной фигурой — и предмет резало по
    # линии. Для маски важно не «какого цвета в среднем», а «есть ли тут хоть
    # что-то непустое».
    # Окно минимума держим маленьким (3 px): при большом тёмные пиксели
    # предмета расползаются в полосу разделителя, она перестаёт гаситься,
    # и весь лист слипается в одну фигуру — у маяка в карточке оставался
    # только луч.
    small = grey.filter(ImageFilter.MinFilter(3)).resize(
        (sw, sh), Image.NEAREST) if k > 1 else grey
    px = small.load()
    mask = [px[x, y] < WHITE for y in range(sh) for x in range(sw)]

    # Линии сетки гасим, иначе они соединяют все ячейки в одну область.
    # Но гасим только светлые пиксели полосы: там, где предмет переходит через
    # линию (плавник акулы, луч звезды, антенна рации, хвост кошки), он темнее
    # разделителя, и его надо оставить. Иначе перешедшая часть отрывается от
    # предмета, становится отдельной областью, достаётся соседней ячейке — и
    # предмет выходит обрезанным по линии.
    for (c, r), band in vband.items():
        if band:
            y0, y1 = round(r * ch) // k, min(sh, round((r + 1) * ch) // k + 1)
            for x in range(max(0, band[0] // k - 1), min(sw, band[1] // k + 2)):
                for y in range(y0, y1):
                    if px[x, y] >= 185:
                        mask[y * sw + x] = False
    for (r, c), band in hband.items():
        if band:
            x0, x1 = round(c * cw) // k, min(sw, round((c + 1) * cw) // k + 1)
            for y in range(max(0, band[0] // k - 1), min(sh, band[1] // k + 2)):
                for x in range(x0, x1):
                    if px[x, y] >= 185:
                        mask[y * sw + x] = False

    labels, parts = label_parts(mask, sw, sh)
    for p in parts:
        p["cells"] = {}

    for y in range(sh):
        r = min(rows - 1, int(y * k / ch))
        for x in range(sw):
            n = labels[y * sw + x]
            if n:
                c = min(cols - 1, int(x * k / cw))
                p = parts[n - 1]
                p["cells"][(r, c)] = p["cells"].get((r, c), 0) + 1

    cell_px = (sw * sh) / (rows * cols)
    out = []
    for r in range(rows):
        for c in range(cols):
            own = [p for p in parts
                   if p["size"] >= MIN_PART * cell_px
                   and max(p["cells"].items(), key=lambda kv: kv[1])[0] == (r, c)]
            boxes = [p["box"] for p in own]
            # Фигура, которая почти вся лежит в своей ячейке, — это предмет
            # с выступом (антенны раций заходят к соседу на 14%), и резать его
            # по линии нельзя. Фигура, размазанная между двумя ячейками, —
            # это слипшиеся соседи (две фотографии во весь кадр), и её режем.
            solo = [p["box"] for p in own
                    if p["cells"].get((r, c), 0) >= 0.75 * p["size"]]
            if not boxes:
                # ячейка залита картинкой во весь кадр (фото блюда, интерьер):
                # своей отдельной фигуры у неё нет, она слилась с соседней.
                # Для таких режем просто по сетке.
                bl, br = vband.get((c, r)), vband.get((c + 1, r))
                bt, bb = hband.get((r, c)), hband.get((r + 1, c))
                x0 = 0 if c == 0 else (bl[1] + 1 if bl else round(c * cw))
                x1 = W if c + 1 == cols else (br[0] if br else round((c + 1) * cw))
                y0 = 0 if r == 0 else (bt[1] + 1 if bt else round(r * ch))
                y1 = H if r + 1 == rows else (bb[0] if bb else round((r + 1) * ch))
                # у залитых ячеек нет белого поля, по которому видно чужой
                # кусок, поэтому от внутренних границ отступаем на 1.2%:
                # полоска соседа снизу была заметна, а потеря края фото — нет
                inset = round(min(cw, ch) * 0.012)
                if c: x0 += inset
                if c + 1 < cols: x1 -= inset
                if r: y0 += inset
                if r + 1 < rows: y1 -= inset
                piece = sheet.crop((x0, y0, x1, y1))
                out.append(piece if piece.size[0] > 8 and piece.size[1] > 8 else None)
                continue
            x0 = min(b[0] for b in boxes) * k
            y0 = min(b[1] for b in boxes) * k
            x1 = max(b[2] for b in boxes) * k
            y1 = max(b[3] for b in boxes) * k
            # За свою ячейку предмет может выступать — плавник акулы, луч звезды,
            # антенна рации уходят за линию в пустое поле соседа. Но если сосед
            # сам залит картинкой во весь кадр (у дельфинов справа пляж), за
            # линию заезжать нельзя: в карточку попадёт чужая картинка.
            over_x, over_y = cw * 0.18, ch * 0.18
            x0 = max(x0, round(c * cw - over_x)); x1 = min(x1, round((c + 1) * cw + over_x))
            y0 = max(y0, round(r * ch - over_y)); y1 = min(y1, round((r + 1) * ch + over_y))

            gp = grey.load()

            def neighbour_is_empty(band, side):
                # пусто ли у соседа сразу за линией, на отрезке этой ячейки
                if not band:
                    return False
                d = round(min(cw, ch) * 0.05)
                if side in "lr":
                    xs = (range(max(0, band[0] - d), band[0]) if side == "l"
                          else range(band[1] + 1, min(W, band[1] + 1 + d)))
                    ys = range(round(r * ch), round((r + 1) * ch), 4)
                else:
                    ys = (range(max(0, band[0] - d), band[0]) if side == "t"
                          else range(band[1] + 1, min(H, band[1] + 1 + d)))
                    xs = range(round(c * cw), round((c + 1) * cw), 4)
                pts = [(x, y) for x in xs for y in ys]
                if not pts:
                    return False
                # «пусто» — это не просто светло: пляж у дельфинов тоже светлый.
                # Пустое поле ещё и ровное, поэтому смотрим и на разброс.
                vals = sorted(gp[x, y] for x, y in pts)
                light = sum(1 for v in vals if v >= 235)
                lo = vals[int(len(vals) * 0.05)]
                hi = vals[min(len(vals) - 1, int(len(vals) * 0.95))]
                return light >= 0.7 * len(vals) and hi - lo <= 14

            # там, где ровной линии не нашлось, берём самый ровный столбец окна:
            # без опорной границы выступ в 18% пускает в карточку кусок соседа
            bl, br = vband.get((c, r)), vband.get((c + 1, r))
            bt, bb = hband.get((r, c)), hband.get((r + 1, c))
            ys = (round(r * ch), round((r + 1) * ch))
            xs = (round(c * cw), round((c + 1) * cw))
            if c and not bl:
                bl = best_seam(grey, round(c * cw), True, search, *ys)
            if c + 1 < cols and not br:
                br = best_seam(grey, round((c + 1) * cw), True, search, *ys)
            if r and not bt:
                bt = best_seam(grey, round(r * ch), False, search, *xs)
            if r + 1 < rows and not bb:
                bb = best_seam(grey, round((r + 1) * ch), False, search, *xs)
            # режем по середине полосы, а не по её ближнему краю: если полоса
            # всё же шире самой линии, ближний край стоит внутри ячейки
            def mid(b):
                return (b[0] + b[1]) // 2

            if bl and not neighbour_is_empty(bl, "l"):
                x0 = max(x0, mid(bl) + 1)
            if br and not neighbour_is_empty(br, "r"):
                x1 = min(x1, mid(br))
            if bt and not neighbour_is_empty(bt, "t"):
                y0 = max(y0, mid(bt) + 1)
            if bb and not neighbour_is_empty(bb, "b"):
                y1 = min(y1, mid(bb))

            # свою фигуру ограничитель не режет — только возвращаем её в кадр
            if solo:
                x0 = min(x0, max(round(c * cw - over_x), min(b[0] for b in solo) * k))
                y0 = min(y0, max(round(r * ch - over_y), min(b[1] for b in solo) * k))
                x1 = max(x1, min(round((c + 1) * cw + over_x), max(b[2] for b in solo) * k))
                y1 = max(y1, min(round((r + 1) * ch + over_y), max(b[3] for b in solo) * k))
            pad = round(min(cw, ch) * PAD)
            if os.environ.get("SM3_DEBUG"):
                print(f"    отладка ячейки r{r}c{c}: box=({x0},{y0},{x1},{y1}) "
                      f"solo={len(solo)} из {len(own)} фигур, "
                      f"bt={bt} bb={bb} bl={bl} br={br}", file=sys.stderr)
            piece = sheet.crop((max(0, x0 - pad), max(0, y0 - pad),
                                min(W, x1 + pad), min(H, y1 + pad)))
            # сначала обрезать поля, иначе обрывок соседа прячется у края и
            # не опознаётся; потом снять его; потом вернуть ровное поле
            piece = trim_white(piece, 0)
            piece = strip_lines(piece)
            piece = drop_strays(piece)
            out.append(add_margin(trim_white(strip_lines(piece), pad), pad))
    return out


def fit(im, side):
    im = im.copy()
    im.thumbnail((side, side), Image.LANCZOS)
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="папка с листами")
    ap.add_argument("--only", nargs="*", help="резать только эти листы")
    ap.add_argument("--preview", help="куда положить контрольный лист-превью")
    ap.add_argument("--cells", nargs="*", help="переписать только эти карточки")
    ap.add_argument("--plain", action="store_true",
                    help="без чисток края: ячейка режется по сетке и обрезается "
                         "только по содержимому. Чистки хороши там, где сосед "
                         "заезжает в кадр, но у предмета с тонким верхом "
                         "(антенна, щетина, кораллы) они срезают верхушку.")
    args = ap.parse_args()

    made, previews, empty = [], [], []
    for sid, unit, rows, cols, names in SHEETS:
        if args.only and sid not in args.only:
            continue
        path = sheet_file(args.src, sid)
        if not path:
            print(f"  нет листа {sid} в {args.src}", file=sys.stderr)
            continue
        sheet = Image.open(path).convert("RGB")
        outdir = os.path.join(ROOT, "media", "gg1", unit)
        os.makedirs(outdir, exist_ok=True)
        if args.cells and not any(n in args.cells for n in names if n):
            continue
        scene = rows == 1 and cols == 1
        pieces = [sheet] if scene else cut_sheet(sheet, rows, cols)
        for i, name in enumerate(names):
            if name is None:
                continue
            if args.cells and name not in args.cells:
                continue
            piece = pieces[i] if i < len(pieces) else None
            if piece is None:
                empty.append(f"{sid} ячейка {i + 1} ({name})")
                continue
            # серая линия сетки остаётся и на ячейках, нарезанных по сетке
            # (фото во весь кадр), поэтому край чистим у всех кусков
            if not args.plain:
                piece = strip_lines(cut_off_line(cut_foreign_strip(piece)))
            out = fit(piece, SCENE if scene else CARD)
            dst = os.path.join(outdir, f"{name}.webp")
            out.save(dst, "WEBP", quality=Q_SCENE if scene else Q_CARD, method=6)
            made.append((sid, os.path.relpath(dst, ROOT), out.size, os.path.getsize(dst)))
            previews.append((name, out))

    for sid, rel, size, nbytes in made:
        print(f"{sid:6} {rel:44} {size[0]}x{size[1]:<5} {nbytes / 1024:6.0f} КБ")
    print(f"\nвсего файлов: {len(made)}")
    for line in empty:
        print("  пусто:", line)

    if args.preview and previews:
        cols_p, cell = 6, 240
        rows_p = (len(previews) + cols_p - 1) // cols_p
        sheet = Image.new("RGB", (cols_p * cell, rows_p * cell), "white")
        for n, (_, im) in enumerate(previews):
            t = fit(im, cell - 16)
            sheet.paste(t, ((n % cols_p) * cell + (cell - t.size[0]) // 2,
                            (n // cols_p) * cell + (cell - t.size[1]) // 2))
        sheet.save(args.preview, quality=88)
        print("превью:", args.preview)


if __name__ == "__main__":
    main()
