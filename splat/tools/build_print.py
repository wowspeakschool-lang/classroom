"""Шаблоны для конкурса рисунков (А4, для печати) — четыре варианта задания («соедини точки» убран, Анна 09.11.2026).

python3 splat/tools/build_print.py
Исходники — контурные картинки Анны (GPT, 09.11.2026) в media/print:
  coloring_v2.png — раскраска, trace_v2.png — пунктир, outlines_v2.png — зубик, тюбик, пингвинёнок, щётка.
Результат — print/*.pdf (по листу) и print/shablony_konkurs.pdf (все пять), превью — print/*.png.

Лист устроен так (Анна, 09.11.2026): вверху строка «как участвовать», крупно «Вариант N. Название»,
одна строка объяснения, дальше только задание — без образцов, подсказок и ответов: лист фотографируют
и отправляют на конкурс. Внизу — имя и возраст.
"""
import math, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from splat_logo import draw_logo
from scipy import ndimage as ndi
from skimage.measure import find_contours

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
FONTS = os.path.join(ROOT, 'tools', 'fonts')
SRC = os.path.join(ROOT, 'media', 'print')
OUT = os.path.join(ROOT, 'print')
W, H = 1654, 2339            # А4 при 200 dpi
M = 110                      # поля
INK = (45, 58, 92)
GREY = (110, 120, 145)
RED = (227, 38, 47)
BLUE = (42, 134, 214)
HASHTAG = '#МойПингвинёнокSPLAT'
TOP = M + 400                # где начинается задание
BOTTOM = H - M - 150         # где кончается


def font(name, size, weight='Bold'):
    f = ImageFont.truetype(os.path.join(FONTS, name + '.ttf'), size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


def lines_of(img):
    return np.asarray(img.convert('L')) < 128


def items(src, n):
    """Режем контурный лист на предметы: построчно, слева направо."""
    m = lines_of(src)
    lab, _ = ndi.label(ndi.binary_dilation(m, iterations=25))
    boxes = [s for s in ndi.find_objects(lab) if (s[0].stop - s[0].start) * (s[1].stop - s[1].start) > m.size * .01]
    boxes.sort(key=lambda s: ((s[0].start + s[0].stop) // 2 // (m.shape[0] // 2), s[1].start))
    assert len(boxes) == n, len(boxes)
    return [src.convert('L').crop((s[1].start, s[0].start, s[1].stop, s[0].stop)) for s in boxes]


def page(n, title, task):
    p = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(p)
    # логотипы
    draw_logo(d, M, M, 92)   # общий логотип — tools/splat_logo.py
    d.text((W - M, M + 46), 'Конкурс рисунков', font=font('Nunito', 34, 'ExtraBold'), fill=BLUE, anchor='rm')
    # как участвовать — маленькой строкой
    d.rounded_rectangle((M, M + 125, W - M, M + 185), 30, fill=(238, 246, 255))
    d.text((W // 2, M + 155), f'Выполни задание, сфотографируй лист и отправь: {HASHTAG} или classroom.wowteach.ru/splat',
           font=font('Nunito', 25, 'Bold'), fill=GREY, anchor='mm')
    # вариант и объяснение
    size = 76
    while d.textlength(f'Вариант {n}. {title}', font=font('Nunito', size, 'Black')) > W - 2 * M and size > 40:
        size -= 2
    d.text((W // 2, M + 255), f'Вариант {n}. {title}', font=font('Nunito', size, 'Black'), fill=INK, anchor='mm')
    d.text((W // 2, M + 335), task, font=font('Nunito', 38, 'Bold'), fill=GREY, anchor='mm')
    # имя и возраст
    d.text((M, H - M - 30), 'Имя ______________________   Возраст ______', font=font('Nunito', 42, 'ExtraBold'), fill=INK, anchor='ls')
    return p, d


def place(img, box):
    """Куда и в каком масштабе вписать картинку в прямоугольник (по центру)."""
    x0, y0, x1, y1 = box
    k = min((x1 - x0) / img.width, (y1 - y0) / img.height)
    return x0 + (x1 - x0 - img.width * k) / 2, y0 + (y1 - y0 - img.height * k) / 2, k


def paste_fit(p, img, box):
    ox, oy, k = place(img, box)
    im = img.resize((max(1, int(img.width * k)), max(1, int(img.height * k))), Image.LANCZOS)
    p.paste(Image.new('RGB', im.size, 'black'), (int(ox), int(oy)), Image.eval(im.convert('L'), lambda v: 0 if v > 235 else 255 - v))   # светлый фон картинки — в чистый белый


# ---------- вариант 1. раскраска ----------
def v1(its):
    p, d = page(1, 'Раскраска', 'Раскрась пингвинёнка, щётку и пасту SPLAT Kids.')
    paste_fit(p, Image.open(os.path.join(SRC, 'coloring_v2.png')), (M, TOP, W - M, BOTTOM))
    return p


# ---------- вариант 2. обведи по пунктиру ----------
def v2(its):
    p, d = page(2, 'Обведи по пунктиру', 'Обведи щётку, пасту, зубик и стаканчик, а потом раскрась.')
    paste_fit(p, Image.open(os.path.join(SRC, 'trace_v2.png')), (M, TOP, W - M, BOTTOM))
    return p


# ---------- вариант 3. соедини точки — три картинки ----------
def outline_points(img, n):
    """n точек на равном шаге по внешнему контуру предмета, по часовой стрелке с верхней точки."""
    m = lines_of(img)
    fill = ndi.binary_fill_holes(ndi.binary_closing(m, iterations=4))
    c = max(find_contours(np.pad(fill, 2).astype(float), .5), key=len)[:, ::-1] - 2   # (x, y)
    seg = np.hypot(*np.diff(c, axis=0).T)
    t = np.concatenate([[0], np.cumsum(seg)])
    i0 = int(np.argmin(c[:, 1] + c[:, 0] * 1e-3))
    want = (t[i0] + np.linspace(0, t[-1], n, endpoint=False)) % t[-1]
    pts = [tuple(c[np.searchsorted(t, w).clip(0, len(c) - 1)]) for w in want]
    area = sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))
    return pts if area > 0 else [pts[0]] + pts[1:][::-1]


def dot_figure(d, it, n, box, fnum):
    ox, oy, k = place(it, box)
    pts = outline_points(it, n)
    cx = np.mean([q[0] for q in pts]); cy = np.mean([q[1] for q in pts])
    for i, (x, y) in enumerate(pts):
        X, Y = ox + x * k, oy + y * k
        d.ellipse((X - 11, Y - 11, X + 11, Y + 11), fill=INK)
        vx, vy = x - cx, y - cy; l = math.hypot(vx, vy) or 1
        d.text((X + vx / l * 36, Y + vy / l * 36), str(i + 1), font=fnum, fill=INK, anchor='mm')


def v3(its):
    tooth, tube, peng, brush = its
    p, d = page(3, 'Соедини точки', 'Соедини точки по порядку от 1 и узнай, что спряталось.')
    fnum = font('Nunito', 30, 'ExtraBold')
    mid = (TOP + BOTTOM) // 2 + 60
    dot_figure(d, tooth, 18, (M + 60, TOP + 60, W // 2 - 40, mid - 40), fnum)
    dot_figure(d, tube, 16, (W // 2 + 80, TOP + 60, W - M - 60, mid - 40), fnum)
    dot_figure(d, brush, 20, (M + 80, mid + 40, W - M - 80, BOTTOM - 40), fnum)
    return p


# ---------- вариант 4. дорисуй половинку ----------
def left_half(it, keep_text=False):
    """Оставляем левую половину предмета. У тюбика надпись SPLAT KIDS не режем: её буквы — мелкие
    детали в середине тюбика, они остаются целиком, дорисовать нужно только сам тюбик."""
    a = np.asarray(it).copy()
    m = a < 128
    ys, xs = np.nonzero(m)
    axis = int((xs.min() + xs.max()) / 2)
    keep = np.zeros_like(m)
    if keep_text:
        lab, n = ndi.label(m)
        h = m.shape[0]
        for i, s in enumerate(ndi.find_objects(lab), 1):
            sh = s[0].stop - s[0].start
            if sh < h * .2 and s[0].start > h * .2 and s[0].stop < h * .75:
                keep |= lab == i
    cut = np.zeros_like(m); cut[:, axis + 3:] = True
    a[cut & ~ndi.binary_dilation(keep, iterations=2)] = 255   # вся правая половина — белая, иначе остаётся серый след
    return Image.fromarray(a), axis


def v4(its):
    tooth, tube, peng, brush = its
    p, d = page(3, 'Дорисуй половинку', 'Дорисуй вторую половинку зубика и тюбика пасты.')
    for it, box, kt in [(tooth, (M, TOP + 40, W // 2 - 30, BOTTOM - 40), False), (tube, (W // 2 + 30, TOP + 40, W - M, BOTTOM - 40), True)]:
        im, axis = left_half(it, kt)
        ox, oy, k = place(it, box)
        paste_fit(p, im, box)
        X = ox + axis * k
        for y in range(int(oy) - 20, int(oy + it.height * k) + 20, 34):
            d.line((X, y, X, y + 16), fill=(170, 178, 196), width=5)
    return p


# ---------- вариант 5. дай пингвинёнку то, что нужно ----------
def v5(its):
    tooth, tube, peng, brush = its
    p, d = page(3, 'Дай пингвинёнку то, что нужно', 'Нарисуй в лапках у пингвинёнка щётку и пасту SPLAT Kids.')
    paste_fit(p, peng, (M + 80, TOP + 40, W - M - 80, BOTTOM - 40))
    return p


def main():
    os.makedirs(OUT, exist_ok=True)
    its = items(Image.open(os.path.join(SRC, 'outlines_v2.png')), 4)
    pages = [('raskraska', v1(its)), ('obvedi', v2(its)), ('day_pingvinyonku', v5(its))]
    for name, pg in pages:
        pg.save(os.path.join(OUT, name + '.pdf'), resolution=200)
        pg.resize((W // 4, H // 4), Image.LANCZOS).save(os.path.join(OUT, name + '.png'))
    pages[0][1].save(os.path.join(OUT, 'shablony_konkurs.pdf'), resolution=200, save_all=True, append_images=[pg for _, pg in pages[1:]])
    print('готово:', ', '.join(n for n, _ in pages))


if __name__ == '__main__':
    main()
