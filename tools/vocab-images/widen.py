"""Расширение полос рядов до соседних полос (подписей): светлые пряди, тени и ноги
не дотягивают до порога 200, и полоса по профилю обрезала их. Заданные руками границы
(не совпадающие с краем полосы) не трогаем — там нарочно отрезана влипшая подпись."""
import numpy as np
from PIL import Image
import lib

def _bands(path):
    a = lib.min_rgb_of(Image.open(path))
    ink = (a < 200).sum(1) > 3
    out, s = [], None
    for y, v in enumerate(ink):
        if v and s is None: s = y
        if not v and s is not None:
            if y - s > 4: out.append((s, y))
            s = None
    if s is not None: out.append((s, len(ink)))
    return out, a.shape[0]

def widen(path, y0, y1):
    bs, H = _bands(path)
    for i, (a, b) in enumerate(bs):
        if abs(a - y0) <= 3:
            y0 = (bs[i - 1][1] + 2) if i > 0 else 0
        if abs(b - y1) <= 3:
            y1 = (bs[i + 1][0] - 2) if i + 1 < len(bs) else H
    return y0, y1

_row, _row_x = lib.row, lib.row_x
def row(sheet, y0, y1, *a, **k):
    y0, y1 = widen(sheet, y0, y1); return _row(sheet, y0, y1, *a, **k)
def row_x(sheet, y0, y1, *a, **k):
    y0, y1 = widen(sheet, y0, y1); return _row_x(sheet, y0, y1, *a, **k)
