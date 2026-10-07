#!/usr/bin/env python3
"""Нарезка листов-сеток SM1 на карточки: media/sm1/<юнит>/<имя>.webp.

Лист режется не по ровной сетке, а по самым широким белым просветам: сначала
ищутся (rows-1) самых широких горизонтальных просветов, потом в каждой полосе
(cols-1) вертикальных. Предмет, который заехал за «свою» клетку, так не
обрезается — граница проходит там, где реально пусто. Потом каждая карточка
обрезается по содержимому с полем 3% и сжимается в webp.

  python3 tools/sm1_cut.py Л5.1 /путь/к/листу.webp      нарезать один лист
  python3 tools/sm1_cut.py --list                        что знает скрипт

Лист в таблице SHEETS: имя → (строки, колонки, [юнит/имя по ячейкам слева
направо, сверху вниз], размер по длинной стороне, качество). None вместо имени —
ячейку пропустить. Сцена (1×1) просто обрезается по полям и масштабируется.
"""
import os, sys
from PIL import Image
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARD, SCENE = 400, 880

SHEETS = {
    "Л5.1": (2, 3, ["u5/act_go_swimming", "u5/act_go_climbing", "u5/act_go_running",
                    "u5/act_go_sledging", "u5/act_go_surfing", "u5/act_go_skiing"], CARD, 82),
    "ЛТ5.1": (2, 3, ["u5/act_ride_pony", "u5/act_watch_tv", "u5/act_play_football",
                     "u5/act_computer_games", "u5/act_ride_bike", "u5/act_hide_and_seek"], CARD, 82),
    "ЛТ1.1": (2, 3, ["u1/school_book", "u1/school_pen", "u1/school_rubber",
                     "u1/school_pencil", "u1/school_bag", "u1/school_ruler"], CARD, 82),
    "ЛТ2.1": (2, 3, ["u2/toy_doll", "u2/toy_kite", "u2/toy_go_kart",
                     "u2/toy_monster", "u2/toy_car", "u2/toy_train"], CARD, 82),
    # коллаж «где занимаются спортом» — лист целиком, точки блока по центрам сетки
    "Л5.2": (1, 1, ["u5/sport_places"], SCENE, 80),
}


def content_mask(a):
    """Не-белое: хоть один канал темнее 238 или заметный цвет."""
    rgb = a[..., :3].astype(int)
    dark = rgb.min(axis=2) < 238
    sat = rgb.max(axis=2) - rgb.min(axis=2) > 18
    return dark | sat


def split(profile, parts):
    """Границы parts полос по (parts-1) самым широким пустым промежуткам."""
    filled = profile > 0
    idx = np.where(filled)[0]
    if parts == 1 or len(idx) == 0:
        return [(idx[0], idx[-1] + 1)] if len(idx) else []
    lo, hi = idx[0], idx[-1] + 1
    gaps, start = [], None
    for i in range(lo, hi):
        if not filled[i] and start is None:
            start = i
        elif filled[i] and start is not None:
            gaps.append((i - start, start, i)); start = None
    gaps = sorted(sorted(gaps, reverse=True)[:parts - 1], key=lambda g: g[1])
    if len(gaps) < parts - 1:
        raise SystemExit(f"нашлось {len(gaps) + 1} полос вместо {parts}")
    cuts = [lo] + [x for g in gaps for x in (g[1], g[2])] + [hi]
    return [(cuts[i], cuts[i + 1]) for i in range(0, len(cuts), 2)]


def trim(img, mask, pad=0.03):
    ys, xs = np.where(mask)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    p = int(max(y1 - y0, x1 - x0) * pad)
    return img.crop((max(x0 - p, 0), max(y0 - p, 0), min(x1 + p, img.width), min(y1 + p, img.height)))


def save(img, rel, size, q):
    img = img.convert("RGB")
    k = size / max(img.size)
    if k < 1:
        img = img.resize((round(img.width * k), round(img.height * k)), Image.LANCZOS)
    path = os.path.join(ROOT, "media", "sm1", rel + ".webp")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "WEBP", quality=q, method=6)
    return path, img.size


def cut(name, src):
    rows, cols, names, size, q = SHEETS[name]
    img = Image.open(src).convert("RGB")
    a = np.asarray(img)
    m = content_mask(a)
    # шум по краю листа (полутон рамки) не должен склеивать полосы
    m[:4, :] = m[-4:, :] = False; m[:, :4] = m[:, -4:] = False
    out = []
    cells = []
    for (y0, y1) in split(m.sum(axis=1), rows):
        band = m[y0:y1]
        for (x0, x1) in split(band.sum(axis=0), cols):
            cells.append((x0, y0, x1, y1))
    if len(cells) != len(names):
        raise SystemExit(f"{name}: ячеек {len(cells)}, а имён {len(names)}")
    for (x0, y0, x1, y1), rel in zip(cells, names):
        if rel is None:
            continue
        piece = img.crop((x0, y0, x1, y1))
        piece = trim(piece, m[y0:y1, x0:x1])
        path, wh = save(piece, rel, size, q)
        out.append((rel, wh, os.path.getsize(path)))
    return out


def main():
    if sys.argv[1:] == ["--list"]:
        for k, (r, c, n, s, q) in SHEETS.items():
            print(f"{k:6} {r}×{c}  {', '.join(x or '—' for x in n)}")
        return
    name, src = sys.argv[1], sys.argv[2]
    for rel, wh, sz in cut(name, src):
        print(f"  {rel:28} {wh[0]}×{wh[1]}  {sz // 1024} КБ")


if __name__ == "__main__":
    main()
