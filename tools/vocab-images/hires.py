"""Картинки 512×512 из той же нарезки (решение 16.10.2026).

Очистка фона (clean_png и исключения в cut.py) настроена на 300×300, и
перенастраивать её незачем: маску прозрачности берём у готовой картинки 300,
а цвет — из той же вырезки листа, снятой вдвое крупнее (600, та же геометрия
×2), и обе сводим к 512. Деталей в 512 столько, сколько есть в листе: рисунок
мельче 576 точек увеличивается, крупнее — уменьшается.

    hires.make(cut_module, sheet, path)   # после cut(sheet, path): out/<лист>/*.png → out512/<лист>/
"""
import os
import numpy as np
from PIL import Image
import lib

SIZE = 512


def _square2(obj, size=300, pad=6):
    """Как lib.to_square, но вдвое крупнее и с той же раскладкой."""
    ow, oh = obj.size
    s = min(1.0, (size - pad * 2) / max(ow, oh)) * 2
    obj = obj.resize((max(1, round(ow * s)), max(1, round(oh * s))), Image.LANCZOS)
    canvas = Image.new('RGBA', (size * 2, size * 2), (255, 255, 255, 0))
    canvas.paste(obj, ((size * 2 - obj.width) // 2, (size * 2 - obj.height) // 2), obj)
    return canvas


def make(cut_module, sheet, path, out='out', raw='out_raw600', dst='out512'):
    orig = lib.to_square
    lib.to_square = _square2
    try:
        cut_module.cut(sheet, path, out=raw, raw=True)
    finally:
        lib.to_square = orig
    os.makedirs(f'{dst}/{sheet}', exist_ok=True)
    for f in sorted(os.listdir(f'{out}/{sheet}')):
        lo = Image.open(f'{out}/{sheet}/{f}').convert('RGBA')
        a = lo.getchannel('A').resize((SIZE, SIZE), Image.BICUBIC)
        rp = f'{raw}/{sheet}/{f}'
        if os.path.exists(rp) and lo.size == (300, 300):
            hi = Image.open(rp).convert('RGBA')
            # под рисунком в вырезке — сам лист (белый); где вырезка пустая, берём цвет из 300
            base = lo.resize((SIZE, SIZE), Image.LANCZOS)
            hi = hi.resize((SIZE, SIZE), Image.LANCZOS)
            rgb = Image.composite(hi, base, hi.getchannel('A').point(lambda v: 255 if v > 0 else 0))
        else:  # нарисовано скриптом (цифры, знаки) или чужого размера — просто крупнее
            rgb = lo.resize((SIZE, SIZE), Image.LANCZOS)
        im = rgb.convert('RGB').convert('RGBA')
        im.putalpha(a)
        im.save(f'{dst}/{sheet}/{f}')
