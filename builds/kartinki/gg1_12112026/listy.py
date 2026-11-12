# -*- coding: utf-8 -*-
"""Составные листы GG1 из уже готовых картинок курса.

Генератору такие листы не поручаем (CLAUDE.md): ровную сетку и группу предметов
он не держит. Собираем скриптом из отдельных картинок, которые уже стоят в курсе.

python3.13 builds/kartinki/gg1_12112026/listy.py
"""
import os
from PIL import Image, ImageChops, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(ROOT, 'builds', 'kartinki', 'gg1_12112026', 'listy')
os.makedirs(OUT, exist_ok=True)

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def podgotovit(path):
    """Отбелить фон и обрезать по содержимому.

    Отбеливаем ТОЛЬКО фон — заливкой от краёв. Сплошная проверка «светлый
    серый → белый» съедала блики на самом предмете: у слона на спине
    появлялись белые пятна.
    """
    im = Image.open(os.path.join(ROOT, path)).convert('RGB')
    w, h = im.size
    seeds = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1),
             (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)]
    for s in seeds:
        r, g, b = im.getpixel(s)
        if min(r, g, b) > 170:
            ImageDraw.floodfill(im, s, (255, 255, 255), thresh=45)
    bg = Image.new('RGB', im.size, 'white')
    bbox = ImageChops.difference(im, bg).convert('L').point(lambda v: 255 if v > 8 else 0).getbbox()
    return im.crop(bbox) if bbox else im


def strelka(im, ot, k, cvet=(200, 30, 30)):
    """Красная стрелка внутри картинки (как на готовой `body_ears`)."""
    w, h = im.size
    x1, y1 = int(ot[0] * w), int(ot[1] * h)
    x2, y2 = int(k[0] * w), int(k[1] * h)
    d = ImageDraw.Draw(im)
    tol = max(3, int(min(w, h) * 0.018))
    d.line([(x1, y1), (x2, y2)], fill=cvet, width=tol)
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    L = tol * 4
    for s in (2.6, -2.6):
        d.line([(x2, y2), (x2 + L * math.cos(ang + s), y2 + L * math.sin(ang + s))], fill=cvet, width=tol)
    return im


def list_setka(files, cols, cell, nomera=False, gap=None, strelki=None):
    rows = (len(files) + cols - 1) // cols
    gap = gap if gap is not None else int(cell * 0.18)
    polya = int(cell * 0.28) if nomera else 0   # поле слева под цифру
    cw = cell + gap
    sheet = Image.new('RGB', (polya + cols * cw + gap, rows * cw + gap), 'white')
    d = ImageDraw.Draw(sheet)
    font = ImageFont.truetype(FONT, int(cell * 0.2))
    for i, f in enumerate(files):
        im = podgotovit(f)
        if strelki and f in strelki:
            im = strelka(im, *strelki[f])
        im.thumbnail((cell, cell), Image.LANCZOS)
        cx = polya + gap + (i % cols) * cw + (cell - im.width) // 2
        cy = gap + (i // cols) * cw + (cell - im.height) // 2
        sheet.paste(im, (cx, cy))
        if nomera:
            d.text((gap // 2, cy + im.height // 2 - int(cell * 0.14)), str(i + 1),
                   fill=(40, 40, 40), font=font)
    return sheet


def list_ryad_s_polkoy(files, cell=400, gap=72, polka=130):
    """Ряд предметов, под каждым — пустое поле под кружок hotspot.

    Возвращает лист и координаты кружков в процентах — их потом ставим
    в payload блока, чтобы метки не закрывали предметы.
    """
    w = gap + len(files) * (cell + gap)
    h = gap + cell + polka
    sheet = Image.new('RGB', (w, h), 'white')
    tochki = []
    for i, f in enumerate(files):
        im = podgotovit(f)
        im.thumbnail((cell, cell), Image.LANCZOS)
        cx = gap + i * (cell + gap) + (cell - im.width) // 2
        sheet.paste(im, (cx, gap + (cell - im.height) // 2))
        tochki.append((round(100 * (gap + i * (cell + gap) + cell / 2) / w, 1),
                       round(100 * (gap + cell + polka * 0.45) / h, 1)))
    return sheet, tochki


ZADANIYA = {
    # Ю5 ДЗ5 бл.2 (gaps): 1 — глаза, 2 — уши, 3 — нос. Подписи только цифрами,
    # английских слов на картинке быть не должно (ответ ребёнок пишет сам).
    'u5/senses_icons.webp': dict(
        files=['media/gg1/u4/body_eyes.webp', 'media/gg1/u4/body_ears.webp', 'media/gg1/u4/body_nose.webp'],
        cols=1, cell=380, nomera=True,
        # у «ушей» стрелки уже нарисованы в самой картинке — носу рисуем такую же
        strelki={'media/gg1/u4/body_nose.webp': ((0.16, 0.86), (0.40, 0.63))}),
    # Ю6 ДЗ1 бл.10 (task «Мой день»): картинка украшает задание.
    'u6/routine_icons.webp': dict(
        files=['media/gg1/u6/da_get_up.webp', 'media/gg1/u6/da_have_breakfast.webp',
               'media/gg1/u6/da_go_to_school.webp', 'media/gg1/u6/da_have_lessons.webp',
               'media/gg1/u6/da_do_homework.webp', 'media/gg1/u6/da_go_to_bed.webp'],
        cols=3, cell=400, nomera=False),
    # Ю7 ДЗ1 бл.11 (task «Загадка»): шесть диких животных курса.
    'u7/animals_collage.webp': dict(
        files=['media/gg1/u7/animal_elephant.webp', 'media/gg1/u7/animal_lion.webp',
               'media/gg1/u7/animal_giraffe.webp', 'media/gg1/u7/animal_crocodile.webp',
               'media/gg1/u7/animal_kangaroo.webp', 'media/gg1/u7/animal_tiger.webp'],
        cols=3, cell=400, nomera=False),
}

# Ю0 ДЗ3 бл.6 (hotspot «подпиши предметы»): пять предметов класса в ряд.
RYAD = {
    'u0/diagram_classroom.webp': ['media/gg1/u0/obj_bin.webp', 'media/gg1/u0/obj_board.webp',
                                  'media/gg1/u0/obj_chair.webp', 'media/gg1/u0/obj_clock.webp',
                                  'media/gg1/u0/obj_desk.webp'],
}

if __name__ == '__main__':
    for name, cfg in ZADANIYA.items():
        sheet = list_setka(cfg['files'], cfg['cols'], cfg['cell'], cfg['nomera'], strelki=cfg.get('strelki'))
        p = os.path.join(OUT, name.replace('/', '__'))
        sheet.save(p, 'WEBP', quality=90)
        print(name, sheet.size, os.path.getsize(p) // 1024, 'KB')
    for name, files in RYAD.items():
        sheet, tochki = list_ryad_s_polkoy(files)
        p = os.path.join(OUT, name.replace('/', '__'))
        sheet.save(p, 'WEBP', quality=90)
        print(name, sheet.size, os.path.getsize(p) // 1024, 'KB', 'точки:', tochki)
