#!/usr/bin/env python3
"""Нарезка листов Super Minds 3 на отдельные картинки.

Лист — одна сгенерированная картинка с сеткой ячеек внутри. Скрипт находит
предмет каждой ячейки как связную фигуру и вырезает её целиком, потом кладёт
webp в media/sm3/uN/. Сцены (grid 1x1) просто масштабируются.

Почему не режем ровно по сетке. Генератор часто выводит предмет за свою
ячейку: купол медузы заходил в ячейку осьминога, луч звезды и хвост конька —
в ряд выше, так же вылезали вентилятор, щётка и зонт. Резать по линии значит
отрезать им верхушку, а резать с запасом — тащить в карточку кусок соседа.
Поэтому строим маску непустых пикселей, гасим линии сетки, размечаем связные
области и отдаём ячейке те из них, которые лежат в ней большей частью.

Переприменяем: файлы всегда переписываются заново.

  python3 tools/sm3_cut.py --src <папка с листами> [--only Л8.4 Л8.5]
"""
import argparse, os, sys
from collections import deque
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CARD = 400          # длинная сторона карточки, px (диапазон проекта 180-420)
SCENE = 880         # длинная сторона сцены, px (диапазон 760-900)
Q_CARD, Q_SCENE = 82, 80
PAD = 0.02          # поле вокруг предмета, доля стороны ячейки
WHITE = 244         # ниже этого предмет, выше — фон листа
MIN_PART = 0.004    # область меньше 0.4% ячейки — мусор, не предмет

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
    ("90.webp", "Л1.6",  "u1", 1, 1, ["scene_timetable"]),
    ("91.webp", "Л1.9",  "u1", 1, 1, ["scene_class_corners"]),
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
    ("92.webp", "Л2.11", "u2", 1, 1, ["scene_cafe_menu"]),
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
    ("93.webp", "Л4.1",  "u4", 1, 1, ["scene_town_square"]),
    ("94.webp", "Л4.2",  "u4", 3, 3, ["town_bank", "town_tower", "town_map",
                                      "town_library", "town_market", "town_supermarket",
                                      "town_bus_station", "town_sports_centre", "town_car_park"]),
    ("95.webp", "Л4.3",  "u4", 2, 2, ["town_funfair", "arrow_straight",
                                      "arrow_left", "arrow_right"]),
    ("96.webp", "Л4.4",  "u4", 2, 3, ["prep_cat_under_sofa", "prep_cat_dog_opposite",
                                      "prep_cat_below_shelf", "prep_fox_in_front_of_box",
                                      "prep_mouse_between_boxes", "prep_monkey_behind_tree"]),
    ("97.webp", "Л4.5",  "u4", 2, 3, ["prep_ball_above_table", "prep_teddy_next_to_ball",
                                      "prep_elephant_in_front_of_chair", "prep_mouse_near_tv",
                                      "prep_cats_opposite", "prep_picture_below_window"]),
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
    ("98.webp", "Л8.6",  "u8", 2, 3, ["landmark_great_wall", "landmark_taj_mahal", "landmark_sphinx",
                                      "landmark_amazon", "landmark_opera_house", "landmark_stadium"]),
    ("99.webp", "Л8.8",  "u8", 2, 3, ["wonder_grand_canyon", "wonder_rio", "wonder_aurora",
                                      "wonder_everest", "wonder_reef", "wonder_victoria_falls"]),
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
    ("100.webp", "Л9.6", "u9", 2, 3, ["old_punch_booth", "old_donkey", "old_steam_train",
                                      "old_bathing_boots", "old_ice_cart", "old_picnic_basket"]),
    ("101.webp", "Л9.7", "u9", 1, 3, ["old_crowded_beach", "modern_train", "modern_flipflops"]),
    ("102.webp", "Л9.8", "u9", 1, 1, ["scene_weather_board"]),
    ("103.webp", "Л9.9", "u9", 1, 1, ["scene_camping_storm"]),
    ("104.webp", "Л9.10","u9", 1, 1, ["scene_holiday_plans"]),
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


def _line_is_divider(vals, share=0.85, spread=20):
    """Похожа ли линия на разделитель сетки.

    Судим по разбросу без крайних значений: min/max ловил единичный тёмный
    пиксель (тень предмета, пересёкшего линию) и браковал линию целиком.
    Между двумя пастельными ячейками шов вообще не белый, а серый 200-240,
    поэтому важен не цвет, а ровность линии по всей длине.
    """
    if not vals:
        return False
    good = sorted(g for g in vals if 185 <= g <= 255)
    if len(good) < share * len(vals):
        return False
    lo = good[max(0, int(len(good) * 0.05))]
    hi = good[min(len(good) - 1, int(len(good) * 0.95))]
    return hi - lo <= spread


def divider_band(grey, pos, vertical, search, lo=None, hi=None):
    """Полоса разделителя рядом с расчётной границей ячейки, или None.

    lo/hi ограничивают отрезок линии. Это важно: вертикальная линия проходит
    через все ряды листа, и достаточно одному предмету наехать на неё в своём
    ряду, чтобы вся линия перестала считаться разделителем. Поэтому границу
    ищем отдельно для каждой ячейки, на её собственном отрезке.
    """
    px = grey.load()
    w, h = grey.size
    limit = w if vertical else h
    span = h if vertical else w
    lo = 0 if lo is None else max(0, lo)
    hi = span if hi is None else min(span, hi)
    step = max(1, (hi - lo) // 200)

    def line(i):
        if vertical:
            return [px[i, y] for y in range(lo, hi, step)]
        return [px[x, i] for x in range(lo, hi, step)]

    hit = None
    for d in range(search + 1):
        for i in (pos - d, pos + d):
            if 0 < i < limit - 1 and _line_is_divider(line(i)):
                hit = i
                break
        if hit is not None:
            break
    if hit is None:
        return None
    # полосу не расширяем без края: у пастельных ячеек фон сам по себе ровный,
    # и разделитель «разрастался» на сотню пикселей, съедая картинку
    grow = max(4, round(span * 0.02))
    a = b = hit
    while a > hit - grow and a > 0 and _line_is_divider(line(a - 1)):
        a -= 1
    while b < hit + grow and b < limit - 1 and _line_is_divider(line(b + 1)):
        b += 1
    return a, b


def best_seam(grey, pos, vertical, search, lo, hi):
    # Если ровной линии нет (предмет пересекает её во многих местах, как брызги
    # дельфинов у самого шва), всё равно нужна опорная граница: берём в окне
    # поиска самый ровный столбец или строку — шов ровнее картинки по обе
    # стороны от него.
    px = grey.load()
    w, h = grey.size
    limit = w if vertical else h
    step = max(1, (hi - lo) // 150)

    def spread(i):
        if vertical:
            vals = sorted(px[i, y] for y in range(lo, hi, step))
        else:
            vals = sorted(px[x, i] for x in range(lo, hi, step))
        a = vals[int(len(vals) * 0.1)]
        b = vals[min(len(vals) - 1, int(len(vals) * 0.9))]
        return b - a

    best, score = pos, None
    for d in range(-search, search + 1):
        i = pos + d
        if 0 < i < limit - 1:
            sc = spread(i)
            if score is None or sc < score:
                best, score = i, sc
    return best, best


def label_parts(mask, w, h):
    """Разметить связные области маски. Возвращает (метки, список областей)."""
    labels = [0] * (w * h)
    parts = []
    for start in range(w * h):
        if not mask[start] or labels[start]:
            continue
        n = len(parts) + 1
        labels[start] = n
        q = deque([start])
        x0 = x1 = start % w
        y0 = y1 = start // w
        size = 0
        while q:
            i = q.popleft()
            size += 1
            x, y = i % w, i // w
            x0, x1 = min(x0, x), max(x1, x)
            y0, y1 = min(y0, y), max(y1, y)
            for j in (i - 1 if x else -1, i + 1 if x + 1 < w else -1,
                      i - w if y else -1, i + w if y + 1 < h else -1):
                if j >= 0 and mask[j] and not labels[j]:
                    labels[j] = n
                    q.append(j)
        parts.append({"size": size, "box": (x0, y0, x1 + 1, y1 + 1)})
    return labels, parts


def shave_edge(im, depth=4):
    """НЕ ИСПОЛЬЗУЕТСЯ. Снять с краёв ровную кромку, отличающуюся от соседних
    пикселей. Идея не сработала: у фотографии крайняя строка законно отличается
    от того, что в восьми пикселях внутрь (небо, вода, градиент), и правило
    начинало срезать саму картинку. Оставлено как след неудачной попытки.

    После всех обрезок у части карточек оставалась полоска шириной 1-3 px:
    остаток поля листа. Цвет у неё бывает любой — от серого до почти белого,
    поэтому судим не по цвету, а по двум признакам сразу: полоса ровная по
    всей длине и заметно отличается от линии в восьми пикселях внутрь.
    """
    px = im.load()
    w, h = im.size

    def line(side, d):
        if side == "l":
            return [px[d, y] for y in range(h)]
        if side == "r":
            return [px[w - 1 - d, y] for y in range(h)]
        if side == "t":
            return [px[x, d] for x in range(w)]
        return [px[x, h - 1 - d] for x in range(w)]

    def flat(vals):
        g = sorted(sum(v) / 3 for v in vals)
        return g[int(len(g) * 0.05)], g[min(len(g) - 1, int(len(g) * 0.95))], sum(g) / len(g)

    cut = {"l": 0, "r": 0, "t": 0, "b": 0}
    for side in "lrtb":
        span = w if side in "lr" else h
        for d in range(min(depth, span // 6)):
            lo, hi, avg = flat(line(side, d))
            if hi - lo > 18:
                break
            if abs(avg - flat(line(side, d + 8))[2]) <= 8:
                break
            cut[side] = d + 1
    if not any(cut.values()):
        return im
    return im.crop((cut["l"], cut["t"], w - cut["r"], h - cut["b"]))


def cut_foreign_strip(im, depth=0.25):
    # Последняя проверка карточки: не осталось ли вдоль края куска чужой
    # картинки. Признак — ровный шов, а за ним область, непохожая на то, что
    # внутри. Ищем глубоко, до четверти стороны: у фотографий во весь кадр
    # полоса соседа бывает широкой, и прежние чистки её не доставали.
    w, h = im.size
    px = im.load()

    def scan(side):
        size = w if side in "lr" else h
        across = h if side in "lr" else w
        limit = max(2, int(size * depth))
        step = max(1, across // 160)
        means, flats = [], []
        for d in range(limit + int(size * 0.15) + 2):
            if side == "l":
                vals = [px[d, y] for y in range(0, h, step)]
            elif side == "r":
                vals = [px[w - 1 - d, y] for y in range(0, h, step)]
            elif side == "t":
                vals = [px[x, d] for x in range(0, w, step)]
            else:
                vals = [px[x, h - 1 - d] for x in range(0, w, step)]
            n = len(vals)
            means.append([sum(v[i] for v in vals) / n for i in range(3)])
            g = sorted(sum(v) / 3 for v in vals)
            flats.append(g[min(n - 1, int(n * 0.9))] - g[int(n * 0.1)])
        # префиксные суммы по средним, чтобы не пересчитывать полосы
        pref = [[0.0, 0.0, 0.0]]
        for m in means:
            pref.append([pref[-1][i] + m[i] for i in range(3)])

        def avg(a, b):
            b = min(b, len(means))
            k = max(1, b - a)
            return [(pref[b][i] - pref[a][i]) / k for i in range(3)]

        best = 0
        inner_w = max(4, int(size * 0.15))
        min_strip = max(2, int(size * 0.015))
        for d in range(min_strip, limit):
            if flats[d] > 18:
                continue
            # шов между ячейками всегда светлый. Без этого условия правило
            # резало по собственному контуру фигуры: у оранжевого
            # прямоугольника и синего квадрата срезало половину карточки.
            if sum(means[d]) / 3 < 200:
                continue
            outer, inner = avg(0, d), avg(d + 1, d + 1 + inner_w)
            # кусок соседа — это картинка, а не поле: если за швом почти белое,
            # резать нечего. Без этого у щётки срезало щетину — над ней белое
            # поле, и оно отличалось от синей ручки достаточно, чтобы сойти
            # за чужую картинку.
            if sum(outer) / 3 > 232:
                continue
            if sum(abs(a - b) for a, b in zip(outer, inner)) > 36:
                best = d + 1
        return best

    cut = {side: scan(side) for side in "lrtb"}
    if not any(cut.values()):
        return im
    x0, y0 = cut["l"], cut["t"]
    x1, y1 = w - cut["r"], h - cut["b"]
    if x1 - x0 < w * 0.5 or y1 - y0 < h * 0.5:
        return im
    return im.crop((x0, y0, x1, y1))


def cut_off_line(im, depth=10):
    """Срезать край до серой линии сетки, если она прячется в нескольких
    пикселях от края (снаружи от неё бывает белая кромка, и построчная
    чистка до линии не доходит)."""
    px = im.load()
    w, h = im.size

    def grey(vals):
        return _line_is_divider([sum(v) / 3 for v in vals], share=0.9, spread=16)

    left = right = top = bottom = 0
    for d in range(min(depth, w // 4)):
        if grey([px[d, y] for y in range(h)]):
            left = d + 1
        if grey([px[w - 1 - d, y] for y in range(h)]):
            right = d + 1
    for d in range(min(depth, h // 4)):
        if grey([px[x, d] for x in range(w)]):
            top = d + 1
        if grey([px[x, h - 1 - d] for x in range(w)]):
            bottom = d + 1
    if not (left or right or top or bottom):
        return im
    return im.crop((left, top, w - right, h - bottom))


def strip_lines(im, limit=10):
    """Снять с краёв ровные светлые линии — остатки сетки."""
    px = im.load()
    w, h = im.size
    left, right, top, bottom = 0, w, 0, h

    def line(vals):
        return _line_is_divider([sum(v) / 3 for v in vals], share=0.9, spread=16)

    for _ in range(limit):
        if right - left < 8 or bottom - top < 8:
            break
        moved = False
        if line([px[left, y] for y in range(top, bottom)]):
            left += 1; moved = True
        if line([px[right - 1, y] for y in range(top, bottom)]):
            right -= 1; moved = True
        if line([px[x, top] for x in range(left, right)]):
            top += 1; moved = True
        if line([px[x, bottom - 1] for x in range(left, right)]):
            bottom -= 1; moved = True
        if not moved:
            break
    return im.crop((left, top, right, bottom))


def drop_strays(im, thr=WHITE):
    """Убрать с краёв обрывок соседней картинки.

    Бывает, что предметы соседних ячеек касаются друг друга в месте, где
    линия сетки прервана: осьминог с медузой, черепаха с коньком, сапоги
    с зонтом. Тогда это одна связная фигура, и в карточку попадает край
    чужого предмета — тонкий и отделённый чистым просветом.
    """
    w, h = im.size
    g = im.convert("L").point(lambda v: 0 if v >= thr else 255)
    px = g.load()
    # по краям кадра может остаться вертикальная линия сетки: она даёт тёмную
    # точку в каждой строке, и «пустых» строк не находится вовсе. Поэтому
    # профиль считаем по середине кадра, отступив по 6% с каждой стороны.
    mx, my = round(w * 0.06), round(h * 0.06)
    xs = list(range(mx, w - mx, max(1, w // 300)))
    ys = list(range(my, h - my, max(1, h // 300)))
    need_x, need_y = max(3, len(xs) // 50), max(3, len(ys) // 50)
    rows = [sum(1 for x in xs if px[x, y]) >= need_x for y in range(h)]
    cols = [sum(1 for y in ys if px[x, y]) >= need_y for x in range(w)]

    def cut(flags, size):
        thin, gap = size * 0.25, size * 0.008
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

    top, left = cut(rows, h), cut(cols, w)
    bottom, right = h - cut(rows[::-1], h), w - cut(cols[::-1], w)
    if right - left < w * 0.4 or bottom - top < h * 0.4:
        return im
    return im.crop((left, top, right, bottom))


def trim_white(im, pad, thr=WHITE):
    box = im.convert("L").point(lambda v: 0 if v >= thr else 255).getbbox()
    if box is None:
        return im
    w, h = im.size
    return im.crop((max(0, box[0] - pad), max(0, box[1] - pad),
                    min(w, box[2] + pad), min(h, box[3] + pad)))


def cut_sheet(sheet, rows, cols):
    """Вернуть список вырезанных ячеек листа (None там, где ячейка пуста)."""
    W, H = sheet.size
    grey = sheet.convert("L")
    cw, ch = W / cols, H / rows
    # окно поиска линии: у части листов сетка заметно смещена относительно
    # расчётной границы (в Л7.3 — на 30 px), при 4% линия не находилась вовсе
    search = max(6, round(min(cw, ch) * 0.08))

    # границы ищем для каждой ячейки на её отрезке линии
    vband = {}      # (колонка-граница, ряд) -> полоса
    hband = {}      # (ряд-граница, колонка) -> полоса
    for c in range(1, cols):
        for r in range(rows):
            vband[(c, r)] = divider_band(grey, round(c * cw), True, search,
                                         round(r * ch), round((r + 1) * ch))
    for r in range(1, rows):
        for c in range(cols):
            hband[(r, c)] = divider_band(grey, round(r * ch), False, search,
                                         round(c * cw), round((c + 1) * cw))

    k = max(1, round(min(W, H) / 400))           # разметку ведём на уменьшенной копии
    sw, sh = W // k, H // k
    small = grey.resize((sw, sh), Image.LANCZOS)
    px = small.load()
    mask = [px[x, y] < WHITE for y in range(sh) for x in range(sw)]

    # Линии сетки гасим, иначе они соединяют все ячейки в одну область.
    # Но гасим только светлые пиксели полосы: там, где предмет переходит через
    # линию (плавник акулы, луч звезды, антенна рации, хвост кошки), он темнее
    # разделителя, и его надо оставить. Иначе перешедшая часть отрывается от
    # предмета, становится отдельной областью, достаётся соседней ячейке — и
    # предмет выходит обрезанным по линии.
    for (c, r), band in vband.items():
        if band:
            y0, y1 = round(r * ch) // k, min(sh, round((r + 1) * ch) // k + 1)
            for x in range(max(0, band[0] // k - 1), min(sw, band[1] // k + 2)):
                for y in range(y0, y1):
                    if px[x, y] >= 185:
                        mask[y * sw + x] = False
    for (r, c), band in hband.items():
        if band:
            x0, x1 = round(c * cw) // k, min(sw, round((c + 1) * cw) // k + 1)
            for y in range(max(0, band[0] // k - 1), min(sh, band[1] // k + 2)):
                for x in range(x0, x1):
                    if px[x, y] >= 185:
                        mask[y * sw + x] = False

    labels, parts = label_parts(mask, sw, sh)
    for p in parts:
        p["cells"] = {}

    for y in range(sh):
        r = min(rows - 1, int(y * k / ch))
        for x in range(sw):
            n = labels[y * sw + x]
            if n:
                c = min(cols - 1, int(x * k / cw))
                p = parts[n - 1]
                p["cells"][(r, c)] = p["cells"].get((r, c), 0) + 1

    cell_px = (sw * sh) / (rows * cols)
    out = []
    for r in range(rows):
        for c in range(cols):
            boxes = [p["box"] for p in parts
                     if p["size"] >= MIN_PART * cell_px
                     and max(p["cells"].items(), key=lambda kv: kv[1])[0] == (r, c)]
            if not boxes:
                # ячейка залита картинкой во весь кадр (фото блюда, интерьер):
                # своей отдельной фигуры у неё нет, она слилась с соседней.
                # Для таких режем просто по сетке.
                bl, br = vband.get((c, r)), vband.get((c + 1, r))
                bt, bb = hband.get((r, c)), hband.get((r + 1, c))
                x0 = 0 if c == 0 else (bl[1] + 1 if bl else round(c * cw))
                x1 = W if c + 1 == cols else (br[0] if br else round((c + 1) * cw))
                y0 = 0 if r == 0 else (bt[1] + 1 if bt else round(r * ch))
                y1 = H if r + 1 == rows else (bb[0] if bb else round((r + 1) * ch))
                # у залитых ячеек нет белого поля, по которому видно чужой
                # кусок, поэтому от внутренних границ отступаем на 1.2%:
                # полоска соседа снизу была заметна, а потеря края фото — нет
                inset = round(min(cw, ch) * 0.012)
                if c: x0 += inset
                if c + 1 < cols: x1 -= inset
                if r: y0 += inset
                if r + 1 < rows: y1 -= inset
                piece = sheet.crop((x0, y0, x1, y1))
                out.append(piece if piece.size[0] > 8 and piece.size[1] > 8 else None)
                continue
            x0 = min(b[0] for b in boxes) * k
            y0 = min(b[1] for b in boxes) * k
            x1 = max(b[2] for b in boxes) * k
            y1 = max(b[3] for b in boxes) * k
            # За свою ячейку предмет может выступать — плавник акулы, луч звезды,
            # антенна рации уходят за линию в пустое поле соседа. Но если сосед
            # сам залит картинкой во весь кадр (у дельфинов справа пляж), за
            # линию заезжать нельзя: в карточку попадёт чужая картинка.
            over_x, over_y = cw * 0.18, ch * 0.18
            x0 = max(x0, round(c * cw - over_x)); x1 = min(x1, round((c + 1) * cw + over_x))
            y0 = max(y0, round(r * ch - over_y)); y1 = min(y1, round((r + 1) * ch + over_y))

            gp = grey.load()

            def neighbour_is_empty(band, side):
                # пусто ли у соседа сразу за линией, на отрезке этой ячейки
                if not band:
                    return False
                d = round(min(cw, ch) * 0.05)
                if side in "lr":
                    xs = (range(max(0, band[0] - d), band[0]) if side == "l"
                          else range(band[1] + 1, min(W, band[1] + 1 + d)))
                    ys = range(round(r * ch), round((r + 1) * ch), 4)
                else:
                    ys = (range(max(0, band[0] - d), band[0]) if side == "t"
                          else range(band[1] + 1, min(H, band[1] + 1 + d)))
                    xs = range(round(c * cw), round((c + 1) * cw), 4)
                pts = [(x, y) for x in xs for y in ys]
                if not pts:
                    return False
                # «пусто» — это не просто светло: пляж у дельфинов тоже светлый.
                # Пустое поле ещё и ровное, поэтому смотрим и на разброс.
                vals = sorted(gp[x, y] for x, y in pts)
                light = sum(1 for v in vals if v >= 235)
                lo = vals[int(len(vals) * 0.05)]
                hi = vals[min(len(vals) - 1, int(len(vals) * 0.95))]
                return light >= 0.7 * len(vals) and hi - lo <= 14

            # там, где ровной линии не нашлось, берём самый ровный столбец окна:
            # без опорной границы выступ в 18% пускает в карточку кусок соседа
            bl, br = vband.get((c, r)), vband.get((c + 1, r))
            bt, bb = hband.get((r, c)), hband.get((r + 1, c))
            ys = (round(r * ch), round((r + 1) * ch))
            xs = (round(c * cw), round((c + 1) * cw))
            if c and not bl:
                bl = best_seam(grey, round(c * cw), True, search, *ys)
            if c + 1 < cols and not br:
                br = best_seam(grey, round((c + 1) * cw), True, search, *ys)
            if r and not bt:
                bt = best_seam(grey, round(r * ch), False, search, *xs)
            if r + 1 < rows and not bb:
                bb = best_seam(grey, round((r + 1) * ch), False, search, *xs)
            if bl and not neighbour_is_empty(bl, "l"):
                x0 = max(x0, bl[1] + 1)
            if br and not neighbour_is_empty(br, "r"):
                x1 = min(x1, br[0])
            if bt and not neighbour_is_empty(bt, "t"):
                y0 = max(y0, bt[1] + 1)
            if bb and not neighbour_is_empty(bb, "b"):
                y1 = min(y1, bb[0])
            pad = round(min(cw, ch) * PAD)
            piece = sheet.crop((max(0, x0 - pad), max(0, y0 - pad),
                                min(W, x1 + pad), min(H, y1 + pad)))
            # сначала обрезать поля, иначе обрывок соседа прячется у края и
            # не опознаётся; потом снять его; потом вернуть ровное поле
            piece = trim_white(piece, 0)
            piece = strip_lines(piece)
            piece = drop_strays(piece)
            out.append(trim_white(strip_lines(piece), pad))
    return out


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

    made, previews, empty = [], [], []
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
        pieces = [sheet] if scene else cut_sheet(sheet, rows, cols)
        for i, name in enumerate(names):
            if name is None:
                continue
            piece = pieces[i] if i < len(pieces) else None
            if piece is None:
                empty.append(f"{sid} ячейка {i + 1} ({name})")
                continue
            # серая линия сетки остаётся и на ячейках, нарезанных по сетке
            # (фото во весь кадр), поэтому край чистим у всех кусков
            piece = strip_lines(cut_off_line(cut_foreign_strip(piece)))
            out = fit(piece, SCENE if scene else CARD)
            dst = os.path.join(outdir, f"{name}.webp")
            out.save(dst, "WEBP", quality=Q_SCENE if scene else Q_CARD, method=6)
            made.append((sid, os.path.relpath(dst, ROOT), out.size, os.path.getsize(dst)))
            previews.append((name, out))

    for sid, rel, size, nbytes in made:
        print(f"{sid:6} {rel:44} {size[0]}x{size[1]:<5} {nbytes / 1024:6.0f} КБ")
    print(f"\nвсего файлов: {len(made)}")
    for line in empty:
        print("  пусто:", line)

    if args.preview and previews:
        cols_p, cell = 6, 240
        rows_p = (len(previews) + cols_p - 1) // cols_p
        sheet = Image.new("RGB", (cols_p * cell, rows_p * cell), "white")
        for n, (_, im) in enumerate(previews):
            t = fit(im, cell - 16)
            sheet.paste(t, ((n % cols_p) * cell + (cell - t.size[0]) // 2,
                            (n // cols_p) * cell + (cell - t.size[1]) // 2))
        sheet.save(args.preview, quality=88)
        print("превью:", args.preview)


if __name__ == "__main__":
    main()
