"""«Тетрадка пингвинёнка» — цветные материалы для печати (А4), решение Анны 09.11.2026:
дневник привычки на 7 дней с наклейками, лабиринты, найди отличия, бинго-лото, памятка для родителей.

python3 splat/tools/build_notebook.py
Картинки — уже готовые цветные из урока и сайта (media/lesson, media/site), новых генераций не нужно.
Результат — print/tetradka_*.pdf, все вместе — print/tetradka_pingvinyonka.pdf, превью — print/tetradka_*.png.
"""
import os, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
FONTS = os.path.join(ROOT, 'tools', 'fonts')
OUT = os.path.join(ROOT, 'print')
W, H = 1654, 2339            # А4 при 200 dpi
M = 110
INK = (45, 58, 92)
GREY = (110, 120, 145)
RED = (227, 38, 47)
BLUE = (42, 134, 214)
SKY = (234, 245, 255)
MINT = (31, 158, 139)
GOLD = (242, 168, 29)
SITE = 'classroom.wowteach.ru/splat'


def font(name, size, weight='Bold'):
    f = ImageFont.truetype(os.path.join(FONTS, name + '.ttf'), size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


def img(name):
    for d in ('lesson', 'site'):
        p = os.path.join(ROOT, 'media', d, name + '.webp')
        if os.path.exists(p):
            return Image.open(p).convert('RGBA')
    raise FileNotFoundError(name)


def put(p, name_or_img, box, angle=0, flip=False):
    """Вписать цветную картинку с прозрачностью в прямоугольник, по центру."""
    im = img(name_or_img) if isinstance(name_or_img, str) else name_or_img
    if flip:
        im = ImageOps.mirror(im)
    if angle:
        im = im.rotate(angle, expand=True, resample=Image.BICUBIC)
    x0, y0, x1, y1 = box
    k = min((x1 - x0) / im.width, (y1 - y0) / im.height)
    im = im.resize((max(1, int(im.width * k)), max(1, int(im.height * k))), Image.LANCZOS)
    p.paste(im, (int(x0 + (x1 - x0 - im.width) / 2), int(y0 + (y1 - y0 - im.height) / 2)), im)


def page(title, sub=None):
    p = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(p)
    d.rounded_rectangle((M, M, M + 210, M + 92), 14, fill=RED)
    d.text((M + 105, M + 38), 'SPLAT', font=font('Fredoka', 54), fill='white', anchor='mm')
    d.text((M + 105, M + 76), 'K I D S', font=font('Fredoka', 22), fill='white', anchor='mm')
    d.text((M + 240, M + 46), '×', font=font('Nunito', 44, 'Black'), fill=INK, anchor='mm')
    d.rounded_rectangle((M + 275, M + 14, M + 520, M + 80), 14, outline=INK, width=4)
    d.text((M + 397, M + 47), 'WowSpeak', font=font('Fredoka', 40), fill=INK, anchor='mm')
    d.text((W - M, M + 46), 'Тетрадка пингвинёнка', font=font('Nunito', 34, 'ExtraBold'), fill=BLUE, anchor='rm')
    size = 76
    while d.textlength(title, font=font('Nunito', size, 'Black')) > W - 2 * M and size > 40:
        size -= 2
    d.text((W // 2, M + 205), title, font=font('Nunito', size, 'Black'), fill=INK, anchor='mm')
    if sub:
        d.multiline_text((W // 2, M + 290), sub, font=font('Nunito', 36, 'Bold'), fill=GREY, anchor='mm', align='center', spacing=8)
    d.text((W // 2, H - M + 20), f'Игры, конкурс и бесплатный урок: {SITE}', font=font('Nunito', 28, 'Bold'), fill=(150, 158, 178), anchor='mm')
    return p, d


def sun(d, cx, cy, r, col=GOLD):
    for i in range(12):
        a = i * np.pi / 6
        d.line((cx + np.cos(a) * r * 1.25, cy + np.sin(a) * r * 1.25, cx + np.cos(a) * r * 1.7, cy + np.sin(a) * r * 1.7), fill=col, width=max(3, r // 6))
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)


def moon(d, cx, cy, r, bg='white', col=(70, 90, 160)):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)
    d.ellipse((cx - r + r * .55, cy - r - r * .15, cx + r + r * .55, cy + r - r * .15), fill=bg)


# ---------- 1. дневник привычки на 7 дней + лист наклеек ----------
def diary():
    p, d = page('Мой дневник: 7 дней с пингвинёнком', 'Почистил зубки утром и вечером — приклей наклейку\n(или нарисуй звёздочку) в кружок этого дня.')
    top, bot = M + 400, H - M - 120
    rh = (bot - top) // 8
    x_day, x_m, x_e = M + 40, M + 760, M + 1180
    # шапка таблицы
    sun(d, x_m, top + rh // 2 - 10, 30)
    d.text((x_m + 80, top + rh // 2 - 10), 'Утро', font=font('Nunito', 44, 'Black'), fill=INK, anchor='lm')
    moon(d, x_e, top + rh // 2 - 10, 32)
    d.text((x_e + 70, top + rh // 2 - 10), 'Вечер', font=font('Nunito', 44, 'Black'), fill=INK, anchor='lm')
    for i in range(7):
        y0 = top + (i + 1) * rh
        d.rounded_rectangle((M, y0 + 8, W - M, y0 + rh - 8), 34, fill=SKY if i % 2 == 0 else (244, 250, 255))
        d.text((x_day, y0 + rh // 2), f'День {i + 1}', font=font('Nunito', 50, 'Black'), fill=INK, anchor='lm')
        put(p, ['ph_stand', 'p_happy', 'ph_brush', 'p_wave', 'ph_stand', 'p_happy', 'ph_jump'][i], (x_day + 250, y0 + 18, x_day + 400, y0 + rh - 18))   # каждый день — пингвинёнок (Анна, 09.11.2026)
        for cx in (x_m + 60, x_e + 60):
            r = rh // 2 - 26
            d.ellipse((cx - r, y0 + rh // 2 - r, cx + r, y0 + rh // 2 + r), outline=(150, 190, 225), width=6, fill='white')
    pages = [p]
    # лист наклеек
    # наклейки по размеру кружка в дневнике (r_slot), чуть меньше него — чтобы влезали
    r_slot = rh // 2 - 26
    p2, d2 = page('Наклейки для дневника', 'Просто вырежи и приклей.\nМожно распечатать на бумаге-самоклейке.')
    names = ['p_happy', 'ph_stand', 'p_wave', 'ph_brush', 'ph_jump', 'magic_tooth', 'brush_paste', 'tube', 'cup', 'gift']
    cols, rows = 5, 6
    top, bot = M + 420, H - M - 100
    cw, ch = (W - 2 * M) // cols, (bot - top) // rows
    k = 0
    for r_ in range(rows):
        for c in range(cols):
            cx, cy = M + c * cw + cw // 2, top + r_ * ch + ch // 2
            r = r_slot - 8
            d2.ellipse((cx - r, cy - r, cx + r, cy + r), fill=[(255, 244, 205), (226, 246, 241), (232, 243, 255), (255, 236, 240)][(r_ + c) % 4])
            for a in range(0, 360, 12):   # пунктир по краю — где резать
                d2.arc((cx - r - 4, cy - r - 4, cx + r + 4, cy + r + 4), a, a + 6, fill=(170, 178, 196), width=3)
            put(p2, names[k % len(names)], (cx - r * .78, cy - r * .78, cx + r * .78, cy + r * .78))
            k += 1
    pages.append(p2)
    return pages


# ---------- 2. лабиринты ----------
def maze(cols, rows, seed):
    """Лабиринт «рекурсивным возвратом»: стены между клетками, один путь от входа до выхода."""
    rnd = random.Random(seed)
    walls = {(c, r): {'N', 'S', 'E', 'W'} for c in range(cols) for r in range(rows)}
    seen, stack = {(0, 0)}, [(0, 0)]
    step = {'N': (0, -1, 'S'), 'S': (0, 1, 'N'), 'E': (1, 0, 'W'), 'W': (-1, 0, 'E')}
    while stack:
        c, r = stack[-1]
        opts = [(k, c + dx, r + dy, back) for k, (dx, dy, back) in step.items() if (c + dx, r + dy) in walls and (c + dx, r + dy) not in seen]
        if not opts:
            stack.pop(); continue
        k, nc, nr, back = rnd.choice(opts)
        walls[(c, r)].discard(k); walls[(nc, nr)].discard(back)
        seen.add((nc, nr)); stack.append((nc, nr))
    return walls


def draw_maze(p, d, box, cols, rows, seed, start_img, end_img, col):
    x0, y0, x1, y1 = box
    cell = min((x1 - x0) / cols, (y1 - y0) / rows)
    ox, oy = x0 + (x1 - x0 - cell * cols) / 2, y0 + (y1 - y0 - cell * rows) / 2
    walls = maze(cols, rows, seed)
    d.rounded_rectangle((ox - 20, oy - 20, ox + cell * cols + 20, oy + cell * rows + 20), 30, fill=SKY)
    wdt = max(8, int(cell / 9))
    for (c, r), ws in walls.items():
        X, Y = ox + c * cell, oy + r * cell
        if 'N' in ws and not (c == 0 and r == 0): d.line((X, Y, X + cell, Y), fill=col, width=wdt)
        if 'W' in ws: d.line((X, Y, X, Y + cell), fill=col, width=wdt)
        if 'S' in ws and not (c == cols - 1 and r == rows - 1): d.line((X, Y + cell, X + cell, Y + cell), fill=col, width=wdt)
        if 'E' in ws: d.line((X + cell, Y, X + cell, Y + cell), fill=col, width=wdt)
    for c in range(cols + 1):   # аккуратные углы
        for r in range(rows + 1):
            X, Y = ox + c * cell, oy + r * cell
            d.ellipse((X - wdt / 2, Y - wdt / 2, X + wdt / 2, Y + wdt / 2), fill=col)
    s = cell * 1.5
    put(p, start_img, (ox - s * .2, oy - s - 10, ox + s * .9, oy - 10))
    put(p, end_img, (ox + cell * cols - s * .9, oy + cell * rows + 10, ox + cell * cols + s * .2, oy + cell * rows + s + 10))


def mazes():
    out = []
    for title, sub, cols, rows, seed, end, col in [
        ('Лабиринт 1: к зубной щётке', 'Дойди до щётки и назови её по-английски.', 6, 7, 3, 'brush_paste', BLUE),
        ('Лабиринт 2: к пасте SPLAT Kids', 'Дойди до пасты и назови её по-английски.', 8, 9, 11, 'tube', MINT),
        ('Лабиринт 3: домой, в Зубной замок', 'Самый длинный путь — домой, в Зубной замок!', 10, 11, 27, 'castle_lights', (120, 90, 200)),
    ]:
        p, d = page(title, sub)
        end_img = img(end)
        if end == 'castle_lights':   # замок — квадратный кусочек сцены в рамке
            c = end_img.crop((520, 40, 1160, 680)).convert('RGBA')
            mask = Image.new('L', c.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, c.width, c.height), 80, fill=255)
            c.putalpha(mask); end_img = c
        draw_maze(p, d, (M + 120, M + 640, W - M - 120, H - M - 330), cols, rows, seed, 'p_wave', end_img, col)
        out.append(p)
    return out


# ---------- 3. найди отличия ----------
def placer(bg):
    """at(name, x, низ, высота): ставит вещь по нижнему краю — будто она стоит на поверхности."""
    def at(name, x, bottom, h, flip=False, tint=None, cx=False):
        im = img(name)
        if tint is not None:
            r, g, b, a = im.split()
            hh, s_, v_ = Image.merge('RGB', (r, g, b)).convert('HSV').split()
            im = Image.merge('HSV', (hh.point(lambda q: (q + tint) % 256), s_, v_)).convert('RGB'); im.putalpha(a)
        if flip: im = ImageOps.mirror(im)
        k = h / im.height
        im = im.resize((int(im.width * k), int(h)), Image.LANCZOS)
        y = int(bottom - im.height / 2) if cx else int(bottom - im.height)   # cx: bottom — это центр по высоте
        bg.alpha_composite(im, (int(x - im.width / 2), y))
    return at


def scene_bath(v):
    """Ванная в Зубном замке (промпт 32)."""
    bg = Image.open(os.path.join(ROOT, 'media/site/bathroom.webp')).convert('RGBA'); at = placer(bg)
    if not v: at('tube', 250, 482, 120)                                  # 1: паста на верхней полке пропала
    at('magic_tooth', 390 if not v else 300, 604, 70)                    # 2: зубик на нижней полке переехал
    at('gift', 220 if not v else 410, 604, 85)
    at('cup', 735, 492, 80, tint=None if not v else 150)                 # 3: стаканчик жёлтый
    if v: at('snowball', 1080, 580, 60)                                  # 4: на табурете снежок
    at('ph_stand', 560, 850, 340, flip=bool(v))                          # 5: пингвинёнок повернулся
    return bg.convert('RGB')


def scene_fishing(v):
    """Рыбалка на льду (фон урока). Удочка как на слайде 14: крючок над лункой (61 %, 73 %)."""
    bg = Image.open(os.path.join(ROOT, 'media/lesson/ice_fishing.webp')).convert('RGBA'); at = placer(bg)
    at('backpack', 200, 760, 190, tint=None if not v else 40)            # 2: рюкзак другого цвета
    for k, (x, y) in enumerate([(330, 860), (440, 885), (250, 900)]):    # 3: рыбок на льду больше
        if k < 2 or v: at('fish', x, y, 55)
    if v: at('cup', 1390, 760, 85)                                       # 4: у лунки стаканчик
    if v: at('magic_tooth', 1500, 560, 70)                               # 5: на сугробе зубик
    pen = img('pb_fishing'); k = 0.6 * 941 / pen.height
    pen = pen.resize((int(pen.width * k), int(pen.height * k)), Image.LANCZOS)
    bg.alpha_composite(pen, (int(0.45 * 1672 - pen.width / 2), int(0.525 * 941 - pen.height / 2)))
    at('fish' if not v else 'tube', 1020, 687, 95 if not v else 110, cx=True)   # 1: на крючке паста вместо рыбки
    return bg.convert('RGB')


def scene_gate(v):
    """У ворот Зубного замка вечером (финал дня 7)."""
    bg = Image.open(os.path.join(ROOT, 'media/site/castle_night.webp')).convert('RGBA'); at = placer(bg)
    if v: at('magic_tooth', 290, 665, 60)                                # 2: на ёлке висит зубик
    at('gift', 1230, 810, 180, tint=None if not v else 60)              # 3: подарок другого цвета
    if v: at('cup', 1450, 860, 105)                                       # 4: в сугробе стаканчик
    if v: at('tube', 1020, 730, 135)                                     # 5: у ворот паста SPLAT Kids
    at('pb_stand' if v else 'p_happy', 560, 820, 340)                    # 1: в лапке щётка / нет
    return bg.convert('RGB')


def differences(scene, title='Найди 5 отличий'):
    p, d = page(title, 'Сравни две картинки и обведи, чем они отличаются.\nНазови по-английски всё, что видишь!')
    top = M + 400
    hh = (H - M - 120 - top - 40) // 2
    for i in range(2):
        sc = scene(i)
        box = (M, top + i * (hh + 40), W - M, top + i * (hh + 40) + hh)
        k = min((box[2] - box[0]) / sc.width, (box[3] - box[1]) / sc.height)
        sc = sc.resize((int(sc.width * k), int(sc.height * k)), Image.LANCZOS)
        x, y = int(box[0] + (box[2] - box[0] - sc.width) / 2), int(box[1] + (box[3] - box[1] - sc.height) / 2)
        mask = Image.new('L', sc.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, sc.width, sc.height), 36, fill=255)
        p.paste(sc, (x, y), mask)
    return [p]


# ---------- новые задания (Анна, 09.11.2026) ----------
def ring_dot(d, x, y, r=14):
    d.ellipse((x - r, y - r, x + r, y + r), fill='white', outline=INK, width=5)


def shadows():
    p, d = page('Найди тень', 'Соедини каждую картинку с её тенью.')
    names = ['magic_tooth', 'brush_paste', 'tube', 'cup', 'p_wave']
    order = [3, 0, 4, 1, 2]
    top, bot = M + 420, H - M - 120
    rh = (bot - top) // 5
    for i, n in enumerate(names):
        y0 = top + i * rh
        sq = rh - 60
        wd = sq * (1.7 if n == 'brush_paste' else 1)   # щётка длинная — ей шире рамка, чтобы не выглядела крошечной
        put(p, n, (M + 260 - wd / 2, y0 + 30, M + 260 + wd / 2, y0 + rh - 30))
        ring_dot(d, M + 540, y0 + rh // 2)
        sh = img(names[order[i]]); a = sh.split()[3]
        sil = Image.new('RGBA', sh.size, (120, 132, 160, 255)); sil.putalpha(a)
        wd = sq * (1.7 if names[order[i]] == 'brush_paste' else 1)
        put(p, sil, (W - M - 260 - wd / 2, y0 + 30, W - M - 260 + wd / 2, y0 + rh - 30))
        ring_dot(d, W - M - 540, y0 + rh // 2)
    return [p]


def odd_one():
    p, d = page('Что лишнее?', 'В каждом ряду одна картинка лишняя. Обведи её\nи расскажи, почему она лишняя.')
    rows = [['brush_paste', 'tube', 'cup', 'fish'], ['p_happy', 'boot', 'p_wave', 'ph_jump'],
            ['magic_tooth', 'brush', 'cake', 'tube'], ['snowball', 'icicle', 'tube', 'ice_cube']]
    top, bot = M + 420, H - M - 120
    rh = (bot - top) // 4
    cw = (W - 2 * M) // 4
    for r, row in enumerate(rows):
        y0 = top + r * rh
        d.rounded_rectangle((M, y0 + 14, W - M, y0 + rh - 14), 40, fill=[SKY, (244, 250, 255)][r % 2])
        for c, n in enumerate(row):
            put(p, n, (M + c * cw + 40, y0 + 50, M + (c + 1) * cw - 40, y0 + rh - 50))
    return [p]


def pattern():
    p, d = page('Продолжи ряд', 'Посмотри, что за чем идёт, и дорисуй в пустой клеточке.')
    rows = [['magic_tooth', 'brush', 'magic_tooth', 'brush', 'magic_tooth', None],
            ['cup', 'cup', 'tube', 'cup', 'cup', None],
            ['p_happy', 'fish', 'p_happy', 'fish', 'p_happy', None],
            ['tube', 'magic_tooth', 'magic_tooth', 'tube', 'magic_tooth', None]]
    top, bot = M + 420, H - M - 120
    rh = (bot - top) // 4
    cw = (W - 2 * M) // 6
    for r, row in enumerate(rows):
        y0 = top + r * rh
        for c, n in enumerate(row):
            x0 = M + c * cw
            box = (x0 + 12, y0 + rh // 2 - cw // 2 + 12, x0 + cw - 12, y0 + rh // 2 + cw // 2 - 12)
            if n:
                d.rounded_rectangle(box, 26, fill=SKY)
                put(p, n, (box[0] + 18, box[1] + 18, box[2] - 18, box[3] - 18), angle=-90 if n == 'brush' else 0)
            else:
                for k in range(0, 4):   # пунктирная клеточка
                    pass
                x_0, y_0, x_1, y_1 = box
                for t in range(int(x_0) + 10, int(x_1) - 10, 26):
                    d.line((t, y_0, t + 13, y_0), fill=(150, 170, 200), width=5); d.line((t, y_1, t + 13, y_1), fill=(150, 170, 200), width=5)
                for t in range(int(y_0) + 10, int(y_1) - 10, 26):
                    d.line((x_0, t, x_0, t + 13), fill=(150, 170, 200), width=5); d.line((x_1, t, x_1, t + 13), fill=(150, 170, 200), width=5)
    return [p]


def penguin_pairs():
    p, d = page('Найди пару', 'Найди одинаковых пингвинят и соедини их линией.')
    poses = ['p_happy', 'p_wave', 'ph_brush', 'ph_jump', 'p_sad', 'pb_fish']   # 6 пар — 12 пингвинят ровной сеткой (Анна, 09.11.2026)
    items = poses * 2
    random.Random(8).shuffle(items)
    top, bot = M + 400, H - M - 120
    cw, ch = (W - 2 * M) // 3, (bot - top) // 4
    for k, n in enumerate(items):
        c, r = k % 3, k // 3
        x0, y0 = M + c * cw, top + r * ch
        put(p, n, (x0 + 70, y0 + 25, x0 + cw - 70, y0 + ch - 25))
    return [p]


def hidden():
    """Найди спрятанные предметы (Анна, 09.11.2026): сцена — промпт 39, целые предметы для рамочек — промпт 40
    (тот же стиль, вырезаны tools/cut.py в media/print/hidden). На картинке предметы спрятаны, в рамочках — целые."""
    sc = Image.open(os.path.join(ROOT, 'media/print/hidden_scene_v4.webp')).convert('RGB')
    names = ['h_tooth', 'h_tube', 'h_cup', 'h_brush', 'h_penguin', 'h_fish']
    p, d = page('Найди спрятанные предметы', 'Найди на картинке всё, что нарисовано в рамочках внизу.\nНашёл — обведи и поставь галочку!')
    top = M + 380
    k = (W - 2 * M) / sc.width
    s2 = sc.resize((W - 2 * M, int(sc.height * k)), Image.LANCZOS)
    mask = Image.new('L', s2.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, s2.width, s2.height), 36, fill=255)
    p.paste(s2, (M, top), mask)
    y0 = top + s2.height + 40
    cw, chh = (W - 2 * M) // 3, (H - M - 110 - y0) // 2
    for i, n in enumerate(names):
        x0, yy = M + (i % 3) * cw, y0 + (i // 3) * chh
        d.rounded_rectangle((x0 + 12, yy + 10, x0 + cw - 12, yy + chh - 10), 30, outline=(124, 92, 170), width=6, fill='white')
        it = Image.open(os.path.join(ROOT, 'media/print/hidden', n + '.webp')).convert('RGBA')
        put(p, it, (x0 + 40, yy + 30, x0 + cw - 120, yy + chh - 30))
        cx, cy = x0 + cw - 70, yy + chh // 2
        d.rounded_rectangle((cx - 26, cy - 26, cx + 26, cy + 26), 8, outline=(124, 92, 170), width=5)   # клеточка для галочки
    return [p]


# ---------- 4. бинго-лото ----------
BINGO = [('tooth', 'magic_tooth'), ('toothbrush', 'brush'), ('toothpaste', 'tube'), ('cup', 'cup'), ('penguin', 'p_happy'),
         ('fish', 'fish'), ('boot', 'boot'), ('gift', 'gift'), ('backpack', 'backpack')]


def bingo():
    out = []
    # две страницы по две карточки 3×2 — у каждой свой набор из 6 картинок
    rnd = random.Random(5)
    sets = [rnd.sample(BINGO, 6) for _ in range(4)]
    for pg in range(2):
        p, d = page('Бинго-лото', 'Мама называет слово по-английски, малыш закрывает картинку\nпуговицей или фишкой. Закрыл всю карточку — кричи «Bingo!»')
        top = M + 420
        bh = (H - M - 120 - top - 50) // 2
        for b in range(2):
            items = sets[pg * 2 + b]
            y0 = top + b * (bh + 50)
            d.rounded_rectangle((M, y0, W - M, y0 + bh), 40, fill=[SKY, (226, 246, 241)][b])
            cw, chh = (W - 2 * M - 80) // 3, (bh - 80) // 2
            for i, (w, n) in enumerate(items):
                cx, cy = M + 40 + (i % 3) * cw, y0 + 40 + (i // 3) * chh
                d.rounded_rectangle((cx + 12, cy + 12, cx + cw - 12, cy + chh - 12), 30, fill='white')
                put(p, n, (cx + 50, cy + 50, cx + cw - 50, cy + chh - 50), angle=-90 if n == 'brush' else 0)
        out.append(p)
    # карточки ведущего
    p, d = page('Карточки для мамы', 'Вырежьте карточки, переверните и тяните по одной.\nНазывайте слово по-английски — малыш ищет картинку у себя.')
    top = M + 420
    cw, chh = (W - 2 * M) // 3, (H - M - 120 - top) // 3
    for i, (w, n) in enumerate(BINGO):
        cx, cy = M + (i % 3) * cw, top + (i // 3) * chh
        for a in range(0, 100, 3):   # пунктир — где резать
            pass
        d.rounded_rectangle((cx + 14, cy + 14, cx + cw - 14, cy + chh - 14), 26, outline=(170, 178, 196), width=4)
        put(p, n, (cx + 60, cy + 40, cx + cw - 60, cy + chh - 130), angle=-90 if n == 'brush' else 0)
        d.text((cx + cw // 2, cy + chh - 70), w, font=font('Nunito', 54, 'Black'), fill=INK, anchor='mm')
    out.append(p)
    return out


# ---------- 5. памятка для родителей ----------
TIPS = [
    ('Чистите вместе', 'Дети повторяют за взрослыми. Встаньте рядом у зеркала — и чистите зубы одновременно.'),
    ('Игра вместо уговоров', '«Помоги пингвинёнку прогнать микробов!» — сказка работает лучше, чем «надо».'),
    ('Песенка-таймер', 'Чистим, пока звучит любимая песенка: так легче дочистить до конца.'),
    ('Сначала игрушке', 'Пусть малыш «почистит зубки» мишке или кукле, а потом — себе.'),
    ('Выбор без выбора', 'Не «будешь чистить?», а «какой щёткой сегодня — синей или зелёной?»'),
    ('Свой ритуал', 'Одно и то же время и место каждый день: утром после завтрака, вечером перед сказкой.'),
    ('Хвалите за старание', 'Хвалите не за результат, а за попытку: «Ты сам почистил — какие чистые зубки!» Наклейка в дневник — маленький праздник. Если малыш отказывается, не спорьте: предложите игру или вернитесь к щётке через минуту.'),
    ('Вкусная паста', 'Детская паста со вкусом, который нравится ребёнку, такая как SPLAT Kids, превращает чистку в удовольствие. Сколько пасты и как часто — подскажет стоматолог.'),
]


def memo():
    p, d = page('Как чистить зубы без уговоров', 'Памятка для родителей')
    top = M + 380
    y = top
    ft, fx = font('Nunito', 40, 'Black'), font('Nunito', 32, 'Bold')
    for i, (t, txt) in enumerate(TIPS):
        d.ellipse((M, y, M + 76, y + 76), fill=[BLUE, MINT, GOLD, RED][i % 4])
        d.text((M + 38, y + 38), str(i + 1), font=font('Nunito', 42, 'Black'), fill='white', anchor='mm')
        d.text((M + 110, y + 8), t, font=ft, fill=INK, anchor='la')
        # перенос строк
        words, line, lines = txt.split(), '', []
        for w in words:
            if d.textlength(line + ' ' + w, font=fx) > W - 2 * M - 110 - 330 * (i < 2):
                lines.append(line); line = w
            else:
                line = (line + ' ' + w).strip()
        lines.append(line)
        for j, l in enumerate(lines):
            d.text((M + 110, y + 62 + j * 44), l, font=fx, fill=GREY, anchor='la')
        y += 62 + len(lines) * 44 + 34
    put(p, 'ph_brush', (W - M - 320, top - 30, W - M, top + 330))
    # английские фразы
    y += 10
    d.rounded_rectangle((M, y, W - M, y + 250), 36, fill=SKY)
    d.text((M + 40, y + 50), 'Говорите во время чистки по-английски:', font=font('Nunito', 38, 'Black'), fill=INK, anchor='lm')
    for j, (en, ru) in enumerate([('Take a toothbrush!', 'возьми щётку'), ('Brush, brush, brush!', 'чистим, чистим'), ('Smile!', 'улыбнись')]):
        d.text((M + 40, y + 115 + j * 50), en, font=font('Nunito', 36, 'Black'), fill=BLUE, anchor='lm')
        d.text((M + 520, y + 115 + j * 50), '— ' + ru, font=fx, fill=GREY, anchor='lm')
    return [p]


def main():
    os.makedirs(OUT, exist_ok=True)
    # бинго убрано (Анна, 09.11.2026)
    parts = [('dnevnik', diary()), ('labirinty', mazes()),
             ('otlichiya', differences(scene_bath) + differences(scene_fishing) + differences(scene_gate)),
             ('ten', shadows()), ('lishnee', odd_one()), ('ryad', pattern()), ('para', penguin_pairs()), ('spryatannoe', hidden()), ('pamyatka', memo())]
    allp = []
    for name, pages in parts:
        pages[0].save(os.path.join(OUT, f'tetradka_{name}.pdf'), resolution=200, save_all=True, append_images=pages[1:])
        for i, pg in enumerate(pages):
            pg.resize((W // 4, H // 4), Image.LANCZOS).save(os.path.join(OUT, f'tetradka_{name}{i + 1 if len(pages) > 1 else ""}.png'))
        allp += pages
    allp[0].save(os.path.join(OUT, 'tetradka_pingvinyonka.pdf'), resolution=200, save_all=True, append_images=allp[1:])
    print('готово:', ', '.join(f'{n} ({len(p)} стр.)' for n, p in parts))


if __name__ == '__main__':
    main()
