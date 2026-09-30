#!/usr/bin/env python3
"""Нарезка листов Super Minds 3 на отдельные картинки.

Лист — одна сгенерированная картинка с сеткой ячеек внутри. Скрипт делит её
по сетке, обрезает поля каждой ячейки, вписывает в квадрат и кладёт webp
в media/sm3/uN/. Сцены (grid 1x1) просто масштабируются.

Переприменяем: файлы всегда переписываются заново.

  python3 tools/sm3_cut.py --src <папка с листами> [--only Л8.4 Л8.5]
"""
import argparse, os, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CARD = 400          # длинная сторона карточки, px (диапазон проекта 180-420)
SCENE = 880         # длинная сторона сцены, px (диапазон 760-900)
Q_CARD, Q_SCENE = 82, 80
PAD = 0.02          # поле вокруг предмета, доля стороны ячейки

# лист: (файл, юнит, строк, колонок, имена ячеек слева направо сверху вниз)
# None вместо имени — ячейку пропустить (пустая клетка листа)
SHEETS = [
    ("73.webp", "Л2.7",  "u2", 2, 3, ["dish_leaf_salad", "dish_asparagus_soup", "dish_roast_pumpkin",
                                      "dish_carrot_beetroot", "dish_berry_smoothie", None]),
    ("74.webp", "Л2.12", "u2", 1, 1, ["scene_who_eats_what"]),
    ("76.webp", "Л4.7",  "u4", 2, 2, ["tower_lighthouse", "tower_skyscraper",
                                      "tower_control", "tower_clock"]),
    ("77.webp", "Л4.8",  "u4", 1, 1, ["scene_town_map"]),
    ("81.webp", "Л8.2",  "u8", 2, 3, ["country_egypt", "country_chile", "country_mexico",
                                      "country_china", "country_spain", "country_india"]),
    ("84.webp", "Л8.3",  "u8", 2, 2, ["country_argentina", "country_australia",
                                      "country_brazil", "country_turkey"]),
    ("85.webp", "Л8.4",  "u8", 2, 3, ["flag_egypt", "flag_argentina", "flag_chile",
                                      "flag_mexico", "flag_spain", "flag_china"]),
    ("86.webp", "Л8.5",  "u8", 2, 2, ["flag_india", "flag_turkey", "flag_brazil", "flag_australia"]),
    ("82.webp", "ЛФ.4",  "ft", 3, 3, ["cake_7", "cake_9", "cake_10",
                                      "gift_bicycle", "gift_console", "gift_puppy",
                                      "bowl_soup", "bowl_salad", "bowl_fruit"]),
]


def content_box(im, thr=244):
    """Границы содержимого: всё, что темнее порога хотя бы по одному каналу."""
    g = im.convert("L").point(lambda v: 0 if v >= thr else 255)
    return g.getbbox()


def cut_cell(sheet, r, c, rows, cols):
    w, h = sheet.size
    x0, x1 = round(c * w / cols), round((c + 1) * w / cols)
    y0, y1 = round(r * h / rows), round((r + 1) * h / rows)
    cell = sheet.crop((x0, y0, x1, y1))
    # разделители сетки — светло-серые линии по краю ячейки, срезаем 1.5%
    m = round(min(cell.size) * 0.015)
    cell = cell.crop((m, m, cell.size[0] - m, cell.size[1] - m))
    box = content_box(cell)
    if box is None:                      # ячейка пустая — белая клетка листа
        return None
    pad = round(min(cell.size) * PAD)
    box = (max(box[0] - pad, 0), max(box[1] - pad, 0),
           min(box[2] + pad, cell.size[0]), min(box[3] + pad, cell.size[1]))
    return cell.crop(box)


def fit(im, side):
    im = im.copy()
    im.thumbnail((side, side), Image.LANCZOS)
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="папка с листами")
    ap.add_argument("--only", nargs="*", help="резать только эти листы")
    ap.add_argument("--preview", help="куда положить контрольный лист-превью")
    args = ap.parse_args()

    made, previews = [], []
    for fname, sid, unit, rows, cols, names in SHEETS:
        if args.only and sid not in args.only:
            continue
        path = os.path.join(args.src, fname)
        if not os.path.exists(path):
            print(f"  нет файла: {path}", file=sys.stderr)
            continue
        sheet = Image.open(path).convert("RGB")
        outdir = os.path.join(ROOT, "media", "sm3", unit)
        os.makedirs(outdir, exist_ok=True)
        scene = rows == 1 and cols == 1
        for i, name in enumerate(names):
            if name is None:
                continue
            piece = cut_cell(sheet, i // cols, i % cols, rows, cols) if not scene else sheet
            if piece is None:
                print(f"  {sid} ячейка {i+1}: пусто, пропущено")
                continue
            out = fit(piece, SCENE if scene else CARD)
            dst = os.path.join(outdir, f"{name}.webp")
            out.save(dst, "WEBP", quality=Q_SCENE if scene else Q_CARD, method=6)
            made.append((sid, os.path.relpath(dst, ROOT), out.size, os.path.getsize(dst)))
            previews.append((f"{name}", out))

    for sid, rel, size, nbytes in made:
        print(f"{sid:6} {rel:44} {size[0]}x{size[1]:<5} {nbytes/1024:6.0f} КБ")
    print(f"\nвсего файлов: {len(made)}")

    if args.preview and previews:
        cols = 6
        cell = 240
        rows = (len(previews) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * cell, rows * cell), "white")
        for n, (_, im) in enumerate(previews):
            t = fit(im, cell - 16)
            x = (n % cols) * cell + (cell - t.size[0]) // 2
            y = (n // cols) * cell + (cell - t.size[1]) // 2
            sheet.paste(t, (x, y))
        sheet.save(args.preview, quality=88)
        print("превью:", args.preview)


if __name__ == "__main__":
    main()
