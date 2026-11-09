"""Шаблоны для конкурса рисунков (А4, для печати): раскраска, обведи по пунктиру, соедини точки,
дорисуй половинку, дай пингвинёнку то, что нужно.

python3 splat/tools/build_print.py
Исходники — контурные картинки Анны (GPT): media/print/coloring_src.png, media/print/outlines_src.png.
Результат — print/*.pdf (по листу) и print/shablony_konkurs.pdf (все пять), превью — print/*.png.
"""
import math, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi
from skimage.measure import find_contours
from skimage.morphology import skeletonize
from collections import deque

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
FONTS = os.path.join(ROOT, 'tools', 'fonts')
OUT = os.path.join(ROOT, 'print')
W, H = 1654, 2339            # А4 при 200 dpi
M = 110                      # поля
INK = (45, 58, 92)
RED = (227, 38, 47)
BLUE = (42, 134, 214)
HASHTAG = '#ДомДляПингвинёнка'


def font(name, size, weight='Bold'):
    f = ImageFont.truetype(os.path.join(FONTS, name + '.ttf'), size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


def lines_of(img):
    """Чёрные линии рисунка: True там, где линия."""
    return np.asarray(img.convert('L')) < 128


def items(src):
    """Режем контурный лист на предметы: построчно, слева направо."""
    m = lines_of(src)
    lab, n = ndi.label(ndi.binary_dilation(m, iterations=25))
    boxes = [s for s in ndi.find_objects(lab) if (s[0].stop - s[0].start) * (s[1].stop - s[1].start) > m.size * .01]
    boxes.sort(key=lambda s: ((s[0].start + s[0].stop) // 2 // (m.shape[0] // 2), s[1].start))
    out = []
    for s in boxes:
        y0, y1, x0, x1 = s[0].start, s[0].stop, s[1].start, s[1].stop
        out.append(src.convert('L').crop((x0, y0, x1, y1)))
    return out


def page(title, task):
    """Лист: шапка с логотипами, заголовок и задание; низ — имя, возраст, хештег."""
    p = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(p)
    # логотипы
    f1, f2 = font('Fredoka', 54), font('Fredoka', 22)
    d.rounded_rectangle((M, M, M + 210, M + 92), 14, fill=RED)
    d.text((M + 105, M + 38), 'SPLAT', font=f1, fill='white', anchor='mm')
    d.text((M + 105, M + 76), 'K I D S', font=f2, fill='white', anchor='mm')
    d.text((M + 240, M + 46), '×', font=font('Nunito', 44, 'Black'), fill=INK, anchor='mm')
    d.rounded_rectangle((M + 275, M + 14, M + 520, M + 80), 14, outline=INK, width=4)
    d.text((M + 397, M + 47), 'WowSpeak', font=font('Fredoka', 40), fill=INK, anchor='mm')
    d.text((W - M, M + 46), 'Конкурс рисунков', font=font('Nunito', 34, 'ExtraBold'), fill=BLUE, anchor='rm')
    # заголовок и задание
    d.text((W // 2, M + 190), title, font=font('Nunito', 82, 'Black'), fill=INK, anchor='mm')
    d.multiline_text((W // 2, M + 285), task, font=font('Nunito', 38, 'Bold'), fill=(90, 102, 130), anchor='mm', align='center', spacing=10)
    # низ
    fy = H - M - 40
    fn = font('Nunito', 40, 'ExtraBold')
    d.text((M, fy - 60), 'Имя ______________________   Возраст ______', font=fn, fill=INK, anchor='ls')
    d.text((M, fy + 10), f'Сфотографируйте и отправьте: {HASHTAG} · classroom.wowteach.ru/splat', font=font('Nunito', 28, 'Bold'), fill=(120, 130, 155), anchor='ls')
    return p, d


def paste_fit(p, img, box, mask=None):
    """Вписать картинку (линии чёрные на белом) в прямоугольник box, по центру."""
    x0, y0, x1, y1 = box
    k = min((x1 - x0) / img.width, (y1 - y0) / img.height)
    im = img.resize((max(1, int(img.width * k)), max(1, int(img.height * k))), Image.LANCZOS)
    px, py = x0 + (x1 - x0 - im.width) // 2, y0 + (y1 - y0 - im.height) // 2
    p.paste(Image.new('RGB', im.size, 'black'), (px, py), Image.eval(im.convert('L'), lambda v: 255 - v))
    return px, py, k


# ---------- 1. раскраска + надпись SPLAT на тюбике (просьба Анны) ----------
def coloring():
    src = Image.open(os.path.join(ROOT, 'media/print/coloring_src.png')).convert('L')
    # SPLAT вдоль тюбика: контурные буквы, чтобы их тоже можно было раскрасить
    t = Image.new('L', (260, 90), 0)
    ImageDraw.Draw(t).text((130, 45), 'SPLAT', font=font('Fredoka', 44), fill=255, anchor='mm', stroke_width=0)
    edge = (ndi.binary_dilation(np.asarray(t) > 128, iterations=3) & ~(np.asarray(t) > 128))
    lay = Image.fromarray((edge * 255).astype('uint8')).rotate(68, expand=True, resample=Image.BICUBIC)
    a = np.asarray(src).copy()
    lx, ly = 630 - lay.width // 2, 905 - lay.height // 2
    sub = a[ly:ly + lay.height, lx:lx + lay.width]
    sub[np.asarray(lay) > 110] = 0
    src = Image.fromarray(a)
    p, d = page('Раскрась пингвинёнка', 'Пингвинёнок чистит зубки щёткой и пастой SPLAT Kids.\nРаскрась его и назови по-английски: penguin, toothbrush, toothpaste, cup.')
    paste_fit(p, src, (M, M + 360, W - M, H - M - 150))
    return p


# ---------- 2. обведи по пунктиру ----------
def dotted(img, box, d, step=30, r=6):
    """Сплошные линии → точки вдоль средней линии (обходим скелет линии от точки к точке)."""
    m = lines_of(img)
    sk = skeletonize(m)
    x0, y0, x1, y1 = box
    k = min((x1 - x0) / img.width, (y1 - y0) / img.height)
    ox, oy = x0 + (x1 - x0 - img.width * k) / 2, y0 + (y1 - y0 - img.height * k) / 2
    seen = np.zeros_like(sk)
    placed = []
    H_, W_ = sk.shape
    for y, x in zip(*np.nonzero(sk)):
        if seen[y, x]:
            continue
        # обход в ширину по скелету: точка ставится через каждые step пикселей пути
        q = deque([(y, x, 0)]); seen[y, x] = True
        while q:
            cy, cx, dist = q.popleft()
            if dist % step == 0:
                X, Y = ox + cx * k, oy + cy * k
                if all((X - a) ** 2 + (Y - b) ** 2 > (step * k * .6) ** 2 for a, b in placed):
                    placed.append((X, Y))
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < H_ and 0 <= nx < W_ and sk[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True; q.append((ny, nx, dist + 1))
    for X, Y in placed:
        d.ellipse((X - r, Y - r, X + r, Y + r), fill=(110, 120, 145))


def gray(img, v=200):
    a = np.asarray(img.convert('L'))
    return Image.fromarray(np.where(a < 128, v, 255).astype('uint8'))


def trace(its):
    tooth, brush, tube, cup, peng, bub = its
    p, d = page('Обведи по пунктиру', 'Обведи щётку, зубик и стаканчик по точкам,\nа потом раскрась. Скажи по-английски, что получилось!')
    rows = [brush, tooth, cup]
    top, bot = M + 380, H - M - 170
    hh = (bot - top) // 3
    for i, it in enumerate(rows):
        y0 = top + i * hh
        paste_fit(p, gray(it, 150), (M, y0 + 40, M + 330, y0 + hh - 40))          # образец
        dotted(it, (M + 420, y0 + 10, W - M, y0 + hh - 10), d, step=max(10, int(min(it.width, it.height) / 14)))
        d.text((M + 165, y0 + hh - 20), 'образец', font=font('Nunito', 26, 'Bold'), fill=(150, 158, 178), anchor='ms')
    return p


# ---------- 3. соедини точки ----------
def outline_points(img, n):
    """n точек на равном шаге по внешнему контуру предмета (по часовой стрелке, с верхней точки)."""
    m = lines_of(img)
    fill = ndi.binary_fill_holes(ndi.binary_closing(m, iterations=3))
    c = max(find_contours(np.pad(fill, 2).astype(float), .5), key=len)[:, ::-1] - 2   # (x, y)
    seg = np.hypot(*np.diff(c, axis=0).T)
    t = np.concatenate([[0], np.cumsum(seg)])
    i0 = int(np.argmin(c[:, 1]))                          # начинаем с самой верхней точки
    want = (t[i0] + np.linspace(0, t[-1], n, endpoint=False)) % t[-1]
    pts = [tuple(c[np.searchsorted(t, w).clip(0, len(c) - 1)]) for w in want]
    # по часовой стрелке (в экранных координатах площадь > 0)
    area = sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))
    return pts if area > 0 else [pts[0]] + pts[1:][::-1]


def dots(its):
    tooth, brush, tube, cup, peng, bub = its
    p, d = page('Соедини точки', 'Веди линию от 1 до последней цифры — и узнаешь, кто спрятался.\nСчитай вслух: one, two, three…')
    fnum = font('Nunito', 34, 'ExtraBold')
    for it, n, box in [(tooth, 22, (M + 40, M + 420, W // 2 - 20, H - M - 260)), (tube, 16, (W // 2 + 60, M + 420, W - M - 40, H - M - 260))]:
        x0, y0, x1, y1 = box
        k = min((x1 - x0) / it.width, (y1 - y0) / it.height)
        ox, oy = x0 + (x1 - x0 - it.width * k) / 2, y0 + (y1 - y0 - it.height * k) / 2
        pts = outline_points(it, n)
        cx = np.mean([q[0] for q in pts]); cy = np.mean([q[1] for q in pts])
        for i, (x, y) in enumerate(pts):
            X, Y = ox + x * k, oy + y * k
            r = 13
            d.ellipse((X - r, Y - r, X + r, Y + r), fill=INK)
            vx, vy = x - cx, y - cy; l = math.hypot(vx, vy) or 1
            d.text((X + vx / l * 42, Y + vy / l * 42), str(i + 1), font=fnum, fill=BLUE if i == 0 else INK, anchor='mm')
    return p


# ---------- 4. дорисуй половинку ----------
def half(its):
    tooth, brush, tube, cup, peng, bub = its
    p, d = page('Дорисуй половинку', 'Пингвинёнок нарисовал только половину.\nДорисуй вторую — зубик и тюбик пасты одинаковые с двух сторон!')
    for it, box in [(tooth, (M, M + 440, W // 2 - 30, H - M - 230)), (tube, (W // 2 + 30, M + 440, W - M, H - M - 230))]:
        a = np.asarray(it)
        ys, xs = np.nonzero(a < 128)
        axis = int((xs.min() + xs.max()) / 2)
        a2 = a.copy(); a2[:, axis + 2:] = 255
        px, py, k = paste_fit(p, Image.fromarray(a2), box)
        X = px + axis * k
        for y in range(int(py) - 20, int(py + it.height * k) + 20, 34):
            d.line((X, y, X, y + 16), fill=(160, 170, 190), width=5)
    return p


# ---------- 5. дай пингвинёнку то, что нужно ----------
def give(its):
    tooth, brush, tube, cup, peng, bub = its
    p, d = page('Дай пингвинёнку то, что нужно', 'Пингвинёнок хочет почистить зубки, а лапки пустые.\nНарисуй ему щётку и пасту SPLAT Kids. Скажи: toothbrush, toothpaste!')
    paste_fit(p, peng, (M + 150, M + 420, W - M - 150, H - M - 470))
    d.text((W // 2, H - M - 400), 'Подсказка:', font=font('Nunito', 34, 'ExtraBold'), fill=(150, 158, 178), anchor='mm')
    paste_fit(p, gray(brush, 170), (W // 2 - 420, H - M - 370, W // 2 - 40, H - M - 190))
    paste_fit(p, gray(tube, 170), (W // 2 + 80, H - M - 380, W // 2 + 300, H - M - 180))
    return p


def main():
    os.makedirs(OUT, exist_ok=True)
    its = items(Image.open(os.path.join(ROOT, 'media/print/outlines_src.png')))
    assert len(its) == 6, len(its)
    pages = [('raskraska', coloring()), ('obvedi', trace(its)), ('soedini_tochki', dots(its)), ('dorisuy_polovinku', half(its)), ('day_pingvinyonku', give(its))]
    for name, pg in pages:
        pg.save(os.path.join(OUT, name + '.pdf'), resolution=200)
        pg.resize((W // 4, H // 4), Image.LANCZOS).save(os.path.join(OUT, name + '.png'))
    pages[0][1].save(os.path.join(OUT, 'shablony_konkurs.pdf'), resolution=200, save_all=True, append_images=[pg for _, pg in pages[1:]])
    print('готово:', ', '.join(n for n, _ in pages))


if __name__ == '__main__':
    main()
