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
import os, shutil, sys
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
    "ЛТ5.2": (1, 2, [("u5/t_piano", "u5/t_order_piano"), "u5/t_homework"], CARD, 82),
    "ЛТ1.2": (2, 3, ["u1/t_pencil_case", "u1/t_desk_chair", ("u1/t_notebook", "u1/t_blue_notebook"),
                     "u1/t_yellow_desk", "u1/t_wooden_desk", "u1/t_pencil_case_open"], CARD, 82),
    "ЛТ2.2": (2, 3, ["u2/t_plane", "u2/t_yellow_ball", "u2/t_bike",
                     "u2/t_green_train", "u2/t_purple_monster", "u2/t_toys"], CARD, 82),
    "Л6.1": (3, 3, ["u6/room_bathroom", "u6/room_bedroom", "u6/room_living_room",
                    "u6/room_hall", "u6/room_dining_room", "u6/room_kitchen",
                    "u6/room_stairs", "u6/room_cellar", "u6/house_outside"], CARD, 82),
    "ЛТ6.1": (2, 2, ["u6/test_frog_piano", "u6/test_park_empty",
                     "u6/test_kitten_kitchen", "u6/test_books_bedroom"], CARD, 80),
    "ЛТ3.1": (3, 3, ["u3/animal_elephant", "u3/animal_rat", "u3/animal_lizard",
                     "u3/animal_frog", "u3/animal_spider", "u3/animal_dog",
                     "u3/animal_cat", "u3/animal_duck", "u3/animal_donkey"], CARD, 82),
    "ЛТ6.2": (2, 3, ["u6/test_pears", "u6/test_lizard", "u6/test_plane",
                     "u6/test_crocodile", "u6/test_bikes", "u6/test_dogs"], CARD, 82),
    "ЛТ3.2": (1, 3, ["u3/test_dogs", "u3/test_dog_desk", "u3/test_cat"], CARD, 82),
    "Л6.2": (1, 1, ["u6/haunted_house"], SCENE, 80),
    "Л7.1": (3, 3, ["u7/clothes_tshirt", "u7/clothes_sweater", "u7/clothes_jacket",
                    "u7/clothes_skirt", "u7/clothes_shorts", "u7/clothes_jeans",
                    "u7/clothes_trousers", "u7/clothes_socks", "u7/clothes_shoes"], CARD, 82),
    "Л7.2": (2, 2, ["u7/clothes_cap", "u7/clothes_hat_elephant",
                    "u7/clothes_socks_faces", "u7/clothes_sweater_red"], CARD, 82),
    "Л7.3": (2, (3, 2), ["u7/pattern_stripes", "u7/pattern_spots", "u7/pattern_flowers",
                         "u7/pattern_plain", "u7/pattern_zigzags"], CARD, 82),
    "Л7.4": (1, 3, ["u7/outfit_anna", "u7/outfit_lily", "u7/outfit_kate"], CARD, 82),
    "Л7.5": (1, 1, ["u7/fav_clothes"], 760, 82),
    "Л7.6": (2, 2, ["u7/pic_flower", "u7/pic_rabbit", "u7/pic_flowers", "u7/pic_rabbits"], CARD, 82),
    "ЛТ7.1": (2, (3, 2), ["u7/obj_tv", "u7/obj_microphone", "u7/obj_bikes",
                          "u7/obj_game_controllers", "u7/obj_sandwich"], CARD, 82),
    "ЛТ7.2": (1, 1, ["u7/scene_clothes_shop"], SCENE, 80),
    "ЛТ4.1": (3, 3, ["u4/food_chicken", "u4/food_cheese_sandwich", "u4/food_cake",
                     "u4/food_sausage", "u4/food_banana", "u4/food_steak",
                     "u4/food_pizza", "u4/food_ice_cream", "u4/food_milk"], CARD, 82),
    "ЛТ4.2": (2, 2, ["u4/food_apple_banana", "u4/food_peas_carrots",
                     "u4/food_chicken_carrots", "u4/food_orange_juice"], CARD, 82),
    "Л8.1": (3, 3, ["u8/body_head", "u8/body_arms", "u8/body_hand",
                    "u8/body_fingers", "u8/body_leg", "u8/body_knee",
                    "u8/body_foot", "u8/body_toes", "u8/body_teddy"], CARD, 82),
    "Л8.2": (2, 3, ["u8/move_forwards", "u8/move_backwards", "u8/move_sideways",
                    "u8/move_step", "u8/move_stretch", "u8/move_jump"], CARD, 82),
    "Л8.3": (2, 3, ["u8/ab_can_ski", "u8/ab_cat_dance", "u8/ab_bear_cant_ride_bike",
                    "u8/ab_dog_swim", "u8/kite_sky", "u8/robot_beep"], CARD, 82),
    "Л8.4": (2, 2, ["u8/monster", "u8/t_dog_football", "u8/t_cat_guitar", "u8/inventors_robot"], CARD, 82),
    "Л9.1": (2, 2, ["u9/place_mountains", "u9/place_countryside", "u9/place_beach", "u9/place_city"], CARD, 82),
    "Л9.2": (1, 3, ["u9/place_theme_park", "u9/place_campsite", "u9/place_lake"], CARD, 82),
    "ЛТ9.1": (2, 3, ["u9/act_paint_picture", "u9/act_listen_music", "u9/act_catch_fish",
                     "u9/act_take_photo", "u9/act_look_shells", "u9/act_make_sandcastle"], CARD, 82),
    "Л9.3": (1, 1, ["u9/hw3_where_photos"], 760, 82),
    "ЛФ.1": (1, 3, ["ft/ft_eraser", "ft/ft_bike", "ft/ft_chicken"], CARD, 82),
    "Л9.4": (1, 3, ["u9/act_eat_ice_cream", "u9/act_read_book", "u9/act_play_guitar"], CARD, 82),
    "Л6.3": (1, 3, ["u6/hw3_rats", "u6/hw3_cars", "u6/hw3_go_kart"], CARD, 82),
    "Л7.7": (2, (3, 2), ["u7/outfit_kate", "u7/outfit_tom", "u7/outfit_any",
                         "u7/outfit_sam", "u7/football_ball"], CARD, 82),
    "Л8.5": (2, 3, ["u8/move_he_stretches_forwards", "u8/move_she_jumps_forwards",
                    "u8/move_she_stretches_sideways", "u8/move_she_jumps_backwards",
                    "u8/move_he_runs_sideways", "u8/move_she_steps_forwards"], CARD, 82),
}

# Стоковые картинки тестов, которые по разбору заменяются ячейками уже нарезанных
# листов: копия под старым именем, чтобы не трогать уроки.
ALIASES = {
    "ЛТ5.2": {"u5/t_computer_games": "u5/act_computer_games", "u5/t_football": "u5/act_play_football",
              "u5/t_watch_tv": "u5/act_watch_tv", "u5/t_order_watch_tv": "u5/act_watch_tv"},
    "ЛТ1.2": {"u1/t_book": "u1/school_book", "u1/t_rubber": "u1/school_rubber",
              "u1/t_pencil": "u1/school_pencil"},
}


def content_mask(a):
    """Не-белое: хоть один канал темнее 238 или заметный цвет."""
    rgb = a[..., :3].astype(int)
    dark = rgb.min(axis=2) < 238
    sat = rgb.max(axis=2) - rgb.min(axis=2) > 18
    return dark | sat


FORCED = []   # split() резал без белого просвета — там нужна чистка обрывков


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
        # чистого просвета нет (предметы почти касаются) — режем по самому
        # «тонкому» месту около ожидаемой границы сетки, ±12% ширины
        FORCED.append(True)
        span, gaps = hi - lo, []
        for k in range(1, parts):
            c = lo + span * k // parts
            w = span * 12 // 100
            j = c - w + int(np.argmin(profile[c - w:c + w]))
            gaps.append((0, j, j + 1))
    cuts = [lo] + [x for g in gaps for x in (g[1], g[2])] + [hi]
    return [(cuts[i], cuts[i + 1]) for i in range(0, len(cuts), 2)]


def drop_edge_scraps(mask, share=0.08, k=4):
    """Обрывок соседа у края ячейки: связное пятно, которое касается края и
    весит меньше share всего содержимого (хвост крокодила у велосипедов на
    ЛТ6.2 — он касается травы, поэтому просвета нет). Пятна ищутся на сетке,
    уменьшенной в k раз, обходом в ширину — без scipy."""
    h, w = mask.shape
    hs, ws = (h + k - 1) // k, (w + k - 1) // k
    pad = np.zeros((hs * k, ws * k), bool)
    pad[:h, :w] = mask
    small = pad.reshape(hs, k, ws, k).any(axis=(1, 3))
    label = np.zeros(small.shape, int)
    comps, n = [], 0
    for y0, x0 in zip(*np.where(small)):
        if label[y0, x0]:
            continue
        n += 1
        label[y0, x0] = n
        queue, size, edge = [(y0, x0)], 0, False
        while queue:
            y, x = queue.pop()
            size += 1
            if x in (0, ws - 1) or y in (0, hs - 1):
                edge = True
            for yy, xx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= yy < hs and 0 <= xx < ws and small[yy, xx] and not label[yy, xx]:
                    label[yy, xx] = n
                    queue.append((yy, xx))
        comps.append((n, size, edge))
    total = sum(c[1] for c in comps)
    drop = [c[0] for c in comps if c[2] and c[1] < total * share]
    if not drop:
        return mask
    gone = np.isin(label, drop).repeat(k, 0).repeat(k, 1)[:h, :w]
    return mask & ~gone


def trim(img, mask, pad=0.03, scraps=False):
    # Край ячейки по построению проходит вплотную к содержимому, поэтому мелкое
    # пятно у края — обычно своя деталь (нотка у микрофона). Обрывки соседа
    # ищем только там, где ячейку пришлось резать без белого просвета.
    kept = drop_edge_scraps(mask) if scraps else mask
    if (kept != mask).any():
        # обрывок мог остаться внутри рамки (трава тянется до края) — белим его
        a = np.asarray(img).copy()
        a[mask & ~kept] = 255
        img = Image.fromarray(a)
    mask = kept
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


# Картинки, которые собираются из уже нарезанных карточек: ряд одинаковой высоты.
ROWS = {
    "Л7.7": ("u7/hw3_four_outfits", ["u7/outfit_kate", "u7/outfit_tom", "u7/outfit_any", "u7/outfit_sam"]),
}


def compose_row(dst, srcs, height=360, gap=40, q=82):
    ims = [Image.open(os.path.join(ROOT, "media", "sm1", s + ".webp")).convert("RGB") for s in srcs]
    ims = [im.resize((round(im.width * height / im.height), height), Image.LANCZOS) for im in ims]
    w = sum(im.width for im in ims) + gap * (len(ims) + 1)
    row = Image.new("RGB", (w, height + 2 * gap), "white")
    x = gap
    for im in ims:
        row.paste(im, (x, gap)); x += im.width + gap
    return save(row, dst, SCENE, q)


def cut(name, src):
    rows, cols, names, size, q = SHEETS[name]
    img = Image.open(src).convert("RGB")
    a = np.asarray(img)
    m = content_mask(a)
    # шум по краю листа (полутон рамки) не должен склеивать полосы
    m[:4, :] = m[-4:, :] = False; m[:, :4] = m[:, -4:] = False
    out = []
    cells = []
    per_row = cols if isinstance(cols, tuple) else (cols,) * rows
    FORCED.clear()
    bands = split(m.sum(axis=1), rows)
    rows_forced = bool(FORCED)
    for (y0, y1), n in zip(bands, per_row):
        band = m[y0:y1]
        FORCED.clear()
        for (x0, x1) in split(band.sum(axis=0), n):
            cells.append((x0, y0, x1, y1, rows_forced or bool(FORCED)))
    if len(cells) != len(names):
        raise SystemExit(f"{name}: ячеек {len(cells)}, а имён {len(names)}")
    for (x0, y0, x1, y1, forced), rel in zip(cells, names):
        if rel is None:
            continue
        piece = img.crop((x0, y0, x1, y1))
        piece = trim(piece, m[y0:y1, x0:x1], scraps=forced)
        for r in (rel if isinstance(rel, tuple) else (rel,)):
            path, wh = save(piece, r, size, q)
            out.append((r, wh, os.path.getsize(path)))
    if name in ROWS:
        dst, srcs = ROWS[name]
        path, wh = compose_row(dst, srcs)
        out.append((dst + "  ← " + ", ".join(srcs), wh, os.path.getsize(path)))
    for dst, src in ALIASES.get(name, {}).items():
        a = os.path.join(ROOT, "media", "sm1", src + ".webp")
        b = os.path.join(ROOT, "media", "sm1", dst + ".webp")
        shutil.copyfile(a, b)
        out.append((dst + "  ← " + src, Image.open(b).size, os.path.getsize(b)))
    return out


def main():
    if sys.argv[1:] == ["--list"]:
        for k, (r, c, n, s, q) in SHEETS.items():
            print(f"{k:6} {r}×{c if isinstance(c, int) else '+'.join(map(str, c))}  {', '.join('/'.join(x) if isinstance(x, tuple) else (x or '—') for x in n)}")
        return
    name, src = sys.argv[1], sys.argv[2]
    for rel, wh, sz in cut(name, src):
        print(f"  {rel:28} {wh[0]}×{wh[1]}  {sz // 1024} КБ")


if __name__ == "__main__":
    main()
