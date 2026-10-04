#!/usr/bin/env python3
"""Картинка к блоку 2 теста Unit 3: восемь пар «занятие — часы».

В выгрузке на этом месте стоял коллаж из фотостока вперемешку с клипартом,
с фотографиями детей. Собираем свой: занятия — наши карточки, циферблаты —
tools/gen_clocks.py.

Часы генератору не отдаём. В gen_clocks.py записано, почему: из двенадцати
сгенерированных циферблатов правильными вышло пять, стрелка рисуется на глаз.
Здесь время задано парой (часы, минуты) в имени файла и посчитано по углу.

    python3 tools/sm3_day_times.py            # media/sm3/u3/scene_day_times.webp
    python3 tools/sm3_day_times.py --check    # только сказать, чего не хватает
"""
import argparse, io, os, sys

from PIL import Image, ImageDraw

try:
    import pymupdf
except ImportError:
    sys.exit("нужен pymupdf: pip install pymupdf")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U3 = os.path.join(ROOT, "media", "sm3", "u3")

# (картинка занятия, циферблат, как читается — для проверки глазами)
# Первые пять — те, на которых держатся пропуски в задании. Последние три
# отвлекающие: 6:30 рядом с 6:00, 7:45 рядом с 7:15 — так и задумано.
PAIRS = [
    ("chore_walk_dog",    "clock_quarter_past_seven", "take the dog for a walk · 7:15"),
    ("day_homework",      "clock_six_oclock",         "do homework · 6:00"),
    ("day_bedtime",       "clock_half_past_ten",      "go to bed · 10:30"),
    ("chore_tidy_up",     "clock_half_past_eight",    "clean my room · 8:30"),
    ("day_play_outside",  "clock_eleven_oclock",      "play with friends · 11:00"),
    ("day_family_dinner", "clock_half_past_six",      "have dinner · 6:30 (отвлекающая)"),
    ("chore_wash_up",     "clock_quarter_to_eight",   "wash up · 7:45 (отвлекающая)"),
    ("day_flute",         "clock_quarter_past_three", "play the flute · 3:15 (отвлекающая)"),
]

COLS, ROWS = 2, 4
CELL_W, CELL_H = 430, 190      # карточка пары
PAD = 14                       # поле вокруг карточек
GAP = 12
BG = (247, 244, 238)
CARD = (255, 255, 255)
EDGE = (226, 221, 212)


def load_activity(name: str) -> Image.Image:
    path = os.path.join(U3, name + ".webp")
    return Image.open(path).convert("RGB")


def load_clock(name: str, side: int) -> Image.Image:
    """SVG циферблат в картинку. Рисуем с запасом и ужимаем — края чище."""
    doc = pymupdf.open(os.path.join(U3, name + ".svg"))
    page = doc[0]
    # get_pixmap ширины не принимает — масштаб считаем от размера страницы
    zoom = side * 2 / page.rect.width
    pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
    im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
    return im.resize((side, side), Image.LANCZOS)


def fit(im: Image.Image, box_w: int, box_h: int) -> Image.Image:
    """Вписать, сохранив пропорции: карточки дел не квадратные."""
    im = im.copy()
    im.thumbnail((box_w, box_h), Image.LANCZOS)
    return im


def missing() -> list:
    out = []
    for act, clock, _ in PAIRS:
        if not os.path.exists(os.path.join(U3, act + ".webp")):
            out.append(f"media/sm3/u3/{act}.webp")
        if not os.path.exists(os.path.join(U3, clock + ".svg")):
            out.append(f"media/sm3/u3/{clock}.svg")
    return out


def build() -> Image.Image:
    W = PAD * 2 + CELL_W * COLS + GAP * (COLS - 1)
    H = PAD * 2 + CELL_H * ROWS + GAP * (ROWS - 1)
    sheet = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(sheet)

    inner = 14                       # поле внутри карточки
    clock_side = CELL_H - inner * 2
    act_w = CELL_W - clock_side - inner * 3

    for i, (act, clock, _) in enumerate(PAIRS):
        cx = PAD + (i % COLS) * (CELL_W + GAP)
        cy = PAD + (i // COLS) * (CELL_H + GAP)
        draw.rounded_rectangle([cx, cy, cx + CELL_W, cy + CELL_H],
                               radius=16, fill=CARD, outline=EDGE, width=2)

        a = fit(load_activity(act), act_w, CELL_H - inner * 2)
        sheet.paste(a, (cx + inner + (act_w - a.width) // 2,
                        cy + (CELL_H - a.height) // 2))

        c = load_clock(clock, clock_side)
        sheet.paste(c, (cx + CELL_W - inner - clock_side,
                        cy + (CELL_H - clock_side) // 2))
    return sheet


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="только проверить файлы")
    ap.add_argument("--out", default=os.path.join(U3, "scene_day_times.webp"))
    args = ap.parse_args()

    gone = missing()
    if gone:
        print("не хватает картинок:")
        for g in gone:
            print("  ", g)
        print("\nлист Л3.10 режется так: python3 tools/sm3_cut.py --src <папка с листами>")
        if not args.check:
            sys.exit(1)
        return
    if args.check:
        print("все восемь пар на месте")
        return

    sheet = build()
    sheet.save(args.out, "WEBP", quality=86, method=6)
    print(f"{args.out}  {sheet.width}x{sheet.height}")
    for _, _, label in PAIRS:
        print("  ", label)


if __name__ == "__main__":
    main()
