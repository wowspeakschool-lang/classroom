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
    # --- UNIT 1 · SCHOOL ---
    ("8.webp",  "Л1.1",  "u1", 1, 1, ["scene_classroom_cover"]),
    ("9.webp",  "Л1.2",  "u1", 3, 3, ["subj_english", "subj_maths", "subj_geography",
                                      "subj_it", "subj_music", "subj_science",
                                      "subj_art", "subj_pe", "subj_history"]),
    ("10.webp", "Л1.3",  "u1", 2, 3, ["haveto_be_on_time", "haveto_brush_teeth", "haveto_wash_hands",
                                      "haveto_wear_uniform", "haveto_clean_shoes", "haveto_do_homework"]),
    ("11.webp", "Л1.4",  "u1", 2, 3, ["shape_triangle", "shape_square", "shape_circle",
                                      "shape_rectangle", "shape_pentagon", "shape_hexagon"]),
    ("12.webp", "Л1.5",  "u1", 2, 2, ["shapepic_cat", "shapepic_person",
                                      "shapepic_boat", "shapepic_snake"]),
    # --- UNIT 2 · FOOD ---
    ("72.webp", "Л2.1",  "u2", 1, 1, ["scene_food_cover"]),
    ("14.webp", "Л2.2",  "u2", 3, 3, ["food_apple_juice", "food_bread_rolls", "food_cheese",
                                      "food_water", "food_soup", "food_vegetables",
                                      "food_lemonade", "food_salad", "food_peas"]),
    ("15.webp", "Л2.3",  "u2", 1, 3, ["food_pineapple", "food_sausages", "food_onions"]),
    ("16.webp", "Л2.4",  "u2", 2, 3, ["tray_potatoes_peas_onions", "tray_milk_lemonade_juice",
                                      "tray_biscuits_cake_chocolate", "tray_cake_biscuits_sandwiches",
                                      "tray_peas_potatoes_nuts", "tray_water_juice_milk"]),
    ("17.webp", "Л2.5",  "u2", 2, 3, ["basket_vegetables_only", "basket_fruit_only", "basket_mixed",
                                      "basket_bananas_juice", "lunchbox_roll_water", "fridge_shelves"]),
    ("18.webp", "Л2.6",  "u2", 2, 3, ["part_roots", "part_stems", "part_leaves",
                                      "part_seeds", "part_fruit", "part_plant_diagram"]),
    ("73.webp", "Л2.7",  "u2", 2, 3, ["dish_leaf_salad", "dish_asparagus_soup", "dish_roast_pumpkin",
                                      "dish_carrot_beetroot", "dish_berry_smoothie", None]),
    ("20.webp", "Л2.8",  "u2", 1, 1, ["scene_picnic"]),
    ("21.webp", "Л2.9",  "u2", 1, 1, ["scene_pizzeria"]),
    ("22.webp", "Л2.10", "u2", 1, 1, ["scene_dinner_table"]),
    ("74.webp", "Л2.12", "u2", 1, 1, ["scene_who_eats_what"]),
    # --- UNIT 3 · HOME / TIME / JOBS ---
    ("23.webp", "Л3.1",  "u3", 1, 1, ["scene_house_cutaway"]),
    ("24.webp", "Л3.2",  "u3", 2, 3, ["chore_tidy_up", "chore_do_shopping", "chore_walk_dog",
                                      "chore_wash_up", "chore_sweep", "chore_cook"]),
    ("25.webp", "Л3.3",  "u3", 1, 2, ["chore_dry_dishes", "chore_feed_dog"]),
    ("28.webp", "Л3.6",  "u3", 3, 3, ["job_firefighter", "job_cleaner", "job_vet",
                                      "job_police", "job_teacher", "job_security",
                                      "job_ambulance_driver", "job_shopkeeper", "job_nurse"]),
    ("29.webp", "Л3.7",  "u3", 1, 1, ["scene_kitchen_after_chores"]),
    ("30.webp", "Л3.8",  "u3", 1, 1, ["scene_night_jobs"]),
    ("31.webp", "Л3.9",  "u3", 1, 1, ["scene_daily_routine"]),
    # --- UNIT 5 · UNDER THE SEA ---
    ("32.webp", "Л5.1",  "u5", 1, 1, ["scene_sea_cover"]),
    ("33.webp", "Л5.2",  "u5", 3, 3, ["sea_seal", "sea_dolphin", "sea_anchor",
                                      "sea_turtle", "sea_shell", "sea_octopus",
                                      "sea_seahorse", "sea_starfish", "sea_jellyfish"]),
    ("34.webp", "Л5.3",  "u5", 2, 2, ["sea_diving_gear", "sea_shark", "sea_shoal", "sea_coral"]),
    ("35.webp", "Л5.4",  "u5", 3, 3, ["place_restaurant", "place_museum", "place_park",
                                      "place_supermarket", "place_hospital", "place_cinema",
                                      "place_beach", "place_pool", "place_garden"]),
    ("36.webp", "Л5.5",  "u5", 2, 3, ["eco_warming", "eco_flood", "eco_polar_bear",
                                      "eco_plastic_water", "eco_fish_bag", "eco_ship_smoke"]),
    ("37.webp", "Л5.6",  "u5", 2, 2, ["reef_healthy", "reef_bleached",
                                      "megalodon_scale", "museum_extinct"]),
    ("38.webp", "Л5.7",  "u5", 1, 2, ["beach_clean_then", "beach_polluted_now"]),
    ("39.webp", "Л5.8",  "u5", 2, 3, ["good_dolphins", "good_planting", "good_turtle_free",
                                      "bad_rubbish_beach", "bad_turtle_bag", "bad_cut_forest"]),
    # --- UNIT 6 · GADGETS ---
    ("40.webp", "Л6.1",  "u6", 1, 1, ["scene_gadgets_desk"]),
    ("54.webp", "Л6.2",  "u6", 3, 3, ["gad_phone", "gad_tablet", "gad_laptop",
                                      "gad_torch", "gad_walkie_talkies", "gad_lift",
                                      "gad_console", "gad_toothbrush", "gad_fan"]),
    ("42.webp", "Л6.3",  "u6", 2, 3, ["pair_tv_watch", "pair_cake_cookie", "pair_plane_bicycle",
                                      "pair_football_golfball", "pair_tiger_cat", "pair_elephant_mouse"]),
    ("55.webp", "Л6.4",  "u6", 2, 2, ["pair_butterfly_caterpillar", "pair_computer_torch",
                                      "pair_two_phones", "pair_two_consoles"]),
    ("44.webp", "Л6.5",  "u6", 2, 3, ["cave_pigments", "cave_lamp", "cave_ceiling_bats",
                                      "cave_twig", "cave_charcoal", "cave_bowl_brush"]),
    ("45.webp", "Л6.6",  "u6", 1, 1, ["scene_two_dogs"]),
    ("56.webp", "Л6.7",  "u6", 1, 1, ["scene_gadget_shop"]),
    ("47.webp", "Л6.8",  "u6", 1, 1, ["scene_two_torches"]),
    ("48.webp", "Л6.9",  "u6", 1, 1, ["scene_four_button_gadget"]),
    ("49.webp", "Л6.10", "u6", 1, 1, ["scene_garden_count"]),
    ("80.webp", "Л6.11", "u6", 1, 2, ["gad_lift_hall", "gad_radio"]),
    # --- UNIT 7 · HEALTH ---
    ("50.webp", "Л7.1",  "u7", 1, 1, ["scene_surgery"]),
    ("51.webp", "Л7.2",  "u7", 2, 3, ["med_stethoscope", "med_thermometer", "med_bandage",
                                      "med_medicine", "med_first_aid_box", "med_water_jug"]),
    ("52.webp", "Л7.3",  "u7", 2, 3, ["past_ate", "past_drank", "past_woke_up",
                                      "past_went", "past_came", "past_felt_better"]),
    ("53.webp", "Л7.4",  "u7", 2, 3, ["habit_swimming", "habit_walking", "habit_picnic",
                                      "habit_screen_late", "habit_phone_in_bed", "habit_ice_creams"]),
    # --- UNIT 4 · IN THE TOWN ---
    ("75.webp", "Л4.6",  "u4", 3, 2, ["going_cafe", "going_cinema", "going_library",
                                      "going_market", "going_sports_centre", "going_supermarket"]),
    ("76.webp", "Л4.7",  "u4", 2, 2, ["tower_lighthouse", "tower_skyscraper",
                                      "tower_control", "tower_clock"]),
    ("77.webp", "Л4.8",  "u4", 1, 1, ["scene_town_map"]),
    ("83.webp", "Л4.9",  "u4", 1, 1, ["scene_town_street"]),
    ("79.webp", "Л4.10", "u4", 1, 1, ["scene_town_corner"]),
    # --- UNIT 8 · COUNTRIES ---
    ("57.webp", "Л8.1",  "u8", 1, 1, ["scene_travel_desk"]),
    ("81.webp", "Л8.2",  "u8", 2, 3, ["country_egypt", "country_chile", "country_mexico",
                                      "country_china", "country_spain", "country_india"]),
    ("84.webp", "Л8.3",  "u8", 2, 2, ["country_argentina", "country_australia",
                                      "country_brazil", "country_turkey"]),
    ("85.webp", "Л8.4",  "u8", 2, 3, ["flag_egypt", "flag_argentina", "flag_chile",
                                      "flag_mexico", "flag_spain", "flag_china"]),
    ("86.webp", "Л8.5",  "u8", 2, 2, ["flag_india", "flag_turkey", "flag_brazil", "flag_australia"]),
    ("60.webp", "Л8.7",  "u8", 1, 2, ["landmark_moai", "landmark_pyramid"]),
    ("58.webp", "Л8.9",  "u8", 1, 2, ["travel_compass_map", "travel_suitcase_camera"]),
    ("59.webp", "Л8.10", "u8", 1, 1, ["scene_time_machine"]),
    # --- UNIT 9 · WEATHER ---
    ("61.webp", "Л9.1",  "u9", 1, 1, ["scene_storm_window"]),
    ("62.webp", "Л9.2",  "u9", 2, 3, ["weather_thunderstorm", "weather_rainy", "weather_cloudy",
                                      "weather_windy", "weather_foggy", "weather_sunny"]),
    ("63.webp", "Л9.3",  "u9", 2, 2, ["weather_lightning", "clothes_boots",
                                      "clothes_raincoat", "clothes_umbrella"]),
    ("64.webp", "Л9.4",  "u9", 2, 3, ["plan_sleep", "plan_watch_tv", "plan_cook",
                                      "plan_tennis", "plan_kite", "plan_ride_horse"]),
    ("65.webp", "Л9.5",  "u9", 2, 3, ["going_buy_car", "going_vet", "going_play_piano",
                                      "going_order_pizza", "going_watch_tv", "going_rainy_day"]),
    # --- FINAL TEST ---
    ("66.webp", "ЛФ.1",  "ft", 1, 1, ["scene_final_hall"]),
    ("67.webp", "ЛФ.2",  "ft", 2, 3, ["act_swimming", "act_guitar", "act_cycling",
                                      "act_shopping", "act_football", "act_baking"]),
    ("68.webp", "ЛФ.3",  "ft", 3, 3, ["opt_tennis", "opt_football", "opt_swimming",
                                      "opt_school_bus", "opt_bicycle", "opt_walking",
                                      "opt_kitchen", "opt_garden", "opt_bedroom"]),
    ("82.webp", "ЛФ.4",  "ft", 3, 3, ["cake_7", "cake_9", "cake_10",
                                      "gift_bicycle", "gift_console", "gift_puppy",
                                      "bowl_soup", "bowl_salad", "bowl_fruit"]),
    ("70.webp", "ЛФ.5",  "ft", 2, 3, ["riddle_cheese", "riddle_stomach", "riddle_coffee",
                                      "riddle_cinema", "riddle_dolphin", "riddle_soup"]),
    ("71.webp", "ЛФ.6",  "ft", 1, 2, ["riddle_lift", "riddle_supermarket"]),
]


def _uniform_light(vals, share=0.85):
    """Похожа ли линия на разделитель сетки.

    Строгого «вся линия одного тона» мало: сосед может переползти через линию
    (медуза заходила в ячейку осьминога), и в этом месте она прерывается.
    Поэтому считаем линию разделителем, если ровными и светлыми оказались
    хотя бы 85% её точек.
    """
    if not vals:
        return False
    grey = [sum(px) / 3 for px in vals]
    good = [g for g in grey if 185 <= g <= 252]
    if len(good) < share * len(grey):
        return False
    return max(good) - min(good) <= 14


def find_divider(im, pos, vertical, search):
    """Найти настоящую линию сетки рядом с расчётной границей ячейки.

    Возвращает (начало, конец) полосы разделителя или None, если линии нет —
    так бывает, когда предмет вылез за свою ячейку и перекрыл её собой.
    """
    px = im.load()
    w, h = im.size
    limit = w if vertical else h
    span = h if vertical else w

    def line(i):
        if vertical:
            return [px[i, y] for y in range(0, span, max(1, span // 200))]
        return [px[x, i] for x in range(0, span, max(1, span // 200))]

    hit = None
    for d in range(0, search + 1):
        for i in (pos - d, pos + d):
            if 0 < i < limit - 1 and _uniform_light(line(i)):
                hit = i
                break
        if hit is not None:
            break
    if hit is None:
        return None
    a = b = hit
    while a > 0 and _uniform_light(line(a - 1)):
        a -= 1
    while b < limit - 1 and _uniform_light(line(b + 1)):
        b += 1
    return a, b


def strip_divider(im, limit=8):
    """Снять с краёв ровные серые линии разделителя, если они остались.

    Обрезка по содержимому их не берёт: линия серая (около 230), а порог белого
    выше. Линия отличается тем, что она однородная по всей длине, — по этому и ловим.
    """
    px = im.load()
    w, h = im.size

    def line_is_divider(vals):
        flat = [v for p in vals for v in p]
        if not flat:
            return False
        lo, hi = min(flat), max(flat)
        return hi - lo <= 12 and 190 <= sum(flat) / len(flat) <= 252

    left, right, top, bottom = 0, w, 0, h
    for _ in range(limit):
        if right - left < 8 or bottom - top < 8:
            break
        moved = False
        if line_is_divider([px[left, y] for y in range(top, bottom)]):
            left += 1; moved = True
        if line_is_divider([px[right - 1, y] for y in range(top, bottom)]):
            right -= 1; moved = True
        if line_is_divider([px[x, top] for x in range(left, right)]):
            top += 1; moved = True
        if line_is_divider([px[x, bottom - 1] for x in range(left, right)]):
            bottom -= 1; moved = True
        if not moved:
            break
    return im.crop((left, top, right, bottom))


def content_box(im, thr=244):
    """Границы содержимого: всё, что темнее порога хотя бы по одному каналу."""
    g = im.convert("L").point(lambda v: 0 if v >= thr else 255)
    return g.getbbox()


def drop_strays(im, thr=244):
    """Убрать с краёв обрывки соседней ячейки.

    Когда предмет соседа подходит к линии сетки вплотную, линия в этом месте
    прерывается, ячейка режется по расчётной границе — и в карточку попадает
    полоска чужой картинки. Отличается она тем, что тонкая и отделена от
    предмета чистым белым просветом.
    """
    w, h = im.size
    g = im.convert("L").point(lambda v: 0 if v >= thr else 255)
    px = g.load()
    # одиночного тёмного пикселя мало: по краю ячейки идут остатки линии сетки,
    # и строка из одной такой точки считалась бы содержимым — тогда просвета
    # между обрывком и предметом не находится вовсе.
    xs = list(range(0, w, max(1, w // 300)))
    ys = list(range(0, h, max(1, h // 300)))
    need_x = max(3, len(xs) // 50)
    need_y = max(3, len(ys) // 50)
    rows = [sum(1 for x in xs if px[x, y]) >= need_x for y in range(h)]
    cols = [sum(1 for y in ys if px[x, y]) >= need_y for x in range(w)]

    def cut(flags, size):
        """сколько снять с начала: тонкий кусок содержимого + просвет за ним"""
        thin, gap = size * 0.14, size * 0.008
        i = 0
        while i < size and not flags[i]:
            i += 1
        j = i
        while j < size and flags[j]:
            j += 1
        if j - i > thin or j >= size:
            return 0
        k = j
        while k < size and not flags[k]:
            k += 1
        return j if k - j >= gap and k < size else 0

    top = cut(rows, h)
    bottom = h - cut(rows[::-1], h)
    left = cut(cols, w)
    right = w - cut(cols[::-1], w)
    if right - left < w * 0.5 or bottom - top < h * 0.5:
        return im
    return im.crop((left, top, right, bottom))


def cut_cell(sheet, r, c, rows, cols):
    """Вырезать ячейку, отступив ровно по линии сетки.

    Фиксированный отступ в процентах не годится: у морского конька, звезды,
    медузы, вентилятора, щётки, зонта и дельфина край предмета подходит к линии
    вплотную, и отступ срезал им хвосты. Поэтому линию ищем, а не угадываем;
    не нашли (предмет вылез за свою ячейку) — режем по расчётной границе,
    ничего не отрезая.
    """
    w, h = sheet.size
    cw, ch = w / cols, h / rows
    search = max(4, round(min(cw, ch) * 0.04))

    def edge(idx, total, size, vertical):
        pos = round(idx * size)
        if idx == 0:
            return 0
        if idx == total:
            return w if vertical else h
        band = find_divider(sheet, pos, vertical, search)
        return band  # (a, b) или None

    left = edge(c, cols, cw, True)
    right = edge(c + 1, cols, cw, True)
    top = edge(r, rows, ch, False)
    bottom = edge(r + 1, rows, ch, False)

    x0 = 0 if c == 0 else (left[1] + 1 if left else round(c * cw))
    x1 = w if c + 1 == cols else (right[0] if right else round((c + 1) * cw))
    y0 = 0 if r == 0 else (top[1] + 1 if top else round(r * ch))
    y1 = h if r + 1 == rows else (bottom[0] if bottom else round((r + 1) * ch))

    cell = sheet.crop((x0, y0, x1, y1))
    cell = strip_divider(cell)
    for _ in range(2):          # обрывков у края бывает два подряд
        cell = drop_strays(cell)
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
