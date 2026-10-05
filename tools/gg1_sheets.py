#!/usr/bin/env python3
"""Листы картинок Go Getter 1 — один источник для промптов и для нарезки.

Каждый лист описан один раз: номер, юнит, сетка, стилевой регистр и ячейки
(ключ файла + что нарисовать). Отсюда собирается docs/GG1_листы_промптов.md,
и отсюда же tools/gg1_cut.py берёт таблицу «лист → имена карточек». Так
промпт и нарезка не могут разойтись: порядок ячеек в промпте и порядок имён
при нарезке — один и тот же список.

  python3 tools/gg1_sheets.py            пересобрать docs/GG1_листы_промптов.md
  python3 tools/gg1_sheets.py --check    только проверить (дубли ключей, размер сетки)

Ключ None — ячейка в нарезку не идёт. Картинка, которая уже есть в другом
юните, второй раз не рисуется — блок ссылается на неё по старому ключу.
"""
import argparse, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC = os.path.join(ROOT, "docs", "GG1_листы_промптов.md")

NO_PEOPLE = "No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere."
NO_TEXT = "Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere."
WHITE_BG = "Plain flat pure white background, no shadow on the background."

STYLE = {
    # предметные карточки — узнаваемость важнее (регистр предметов SM3)
    "object": "Realistic 3D render, soft studio lighting from the top-left, clean product-style "
              "but friendly and colourful, generic design, not resembling any real product. " + WHITE_BG,
    # животные и символы действий — мультяшный глянец
    "cartoon": "Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid "
               "saturated colours, soft even light from the top-left. " + WHITE_BG,
    # сцены и комнаты — полу-мультяшный 3D, фон — сама сцена
    "scene": "Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated "
             "colours, warm soft light, everything clearly visible and easy to recognise.",
}

REGISTER_RU = {"object": "реалистичный 3D", "cartoon": "мультяшный глянец", "scene": "сцены, полу-мультяшный 3D"}

GRID_CARDS = ("A sheet of {n} separate {what} in a clean {cols}x{rows} grid, equal cells separated by "
              "thin light-grey gutters, each cell a complete standalone picture, nothing crossing "
              "between cells, each subject centred with a generous empty margin on all sides, never "
              "touching the cell edges:")


def size_line(rows, cols):
    if rows == cols:
        return "Output size: 2048 x 2048 px, each cell at least 650 px."
    if cols > rows:
        return "Output size: 2048 x 1365 px, each cell at least 650 px." if cols == 3 and rows == 2 \
            else "Output size: 2048 x 1024 px, each cell at least 650 px."
    return "Output size: 1365 x 2048 px, each cell at least 650 px."


# (номер, юнит, строк, колонок, регистр, заголовок, пояснение для Анны, ячейки[(ключ, описание)])
SHEETS = [
    # ---------------- UNIT 0 ----------------
    ("Л0.1", "u0", 3, 3, "object", "В рюкзаке", None, [
        ("obj_book", "a closed hardcover school book"),
        ("obj_coloured_pencil", "one coloured pencil, bright red, lying diagonally"),
        ("obj_notebook", "a spiral notebook with a plain cover"),
        ("obj_pen", "a ballpoint pen with its cap"),
        ("obj_pencil", "a yellow graphite pencil with a pink eraser tip"),
        ("obj_pencil_case", "a zipped fabric pencil case"),
        ("obj_sharpener", "a small plastic pencil sharpener"),
        ("obj_rubber", "a rectangular rubber eraser"),
        ("obj_ruler", "a plastic ruler with plain tick marks"),
    ]),
    ("Л0.2", "u0", 3, 3, "object", "Класс и школьные вещи", None, [
        ("obj_scissors", "a pair of children's scissors with rounded tips"),
        ("obj_sandwich", "a sandwich cut in half showing cheese and lettuce"),
        ("obj_bag", "a school backpack with two straps"),
        ("obj_bin", "a plastic waste bin"),
        ("obj_board", "a green classroom chalkboard in a wooden frame, completely blank"),
        ("obj_chair", "a wooden school chair"),
        ("obj_clock", "a round wall clock with plain tick marks and no numbers"),
        ("obj_desk", "a wooden school desk"),
        ("obj_apple", "a shiny red apple with a leaf"),
    ]),
    ("Л0.3", "u0", 2, 3, "object", "Цветные вещи",
     "Для теста Unit 0: «My pen is red», «My bag is blue»… Одна вещь — один цвет.", [
        ("col_red_pen", "a bright red ballpoint pen"),
        ("col_blue_bag", "a bright blue school backpack"),
        ("col_yellow_ruler", "a bright yellow plastic ruler with plain tick marks"),
        ("col_green_notebook", "a bright green spiral notebook"),
        ("col_pink_pencil_case", "a bright pink zipped pencil case"),
        ("col_orange_bag", "a bright orange school backpack"),
    ]),

    # ---------------- UNIT 1 ----------------
    # Семья — люди; ждём решения Анны. Флаги рисует скрипт.
    ("Л1.1", "u1", 2, 3, "scene", "Места",
     "Где ты? — at a party, at school, in the garden, in the park, at home, in the library.", [
        ("place_party", "a party table with a birthday cake with candles, colourful balloons, wrapped presents and a garland, nobody there"),
        ("place_school", "a school building from outside with a big clock on the front and a yellow school bus parked in front"),
        ("place_garden", "a garden with flower beds, a watering can, an apple tree and a wooden fence"),
        ("place_park", "a park with a path, a bench, green trees and a street lamp"),
        ("place_home", "a cosy family house from outside with a red roof, a front door and a little front garden"),
        ("place_library", "a library room with tall bookshelves full of books and an open book on a reading table"),
    ]),
    ("Л1.2", "u1", 2, 3, "scene", "Сцены к заданиям Unit 1",
     "Вместо фото людей в Homework 6 и в тесте: что делают — показываем вещами.", [
        ("beach_loungers", "a sunny beach with two empty sun loungers, a striped umbrella and a suitcase beside them"),
        ("dog_in_bed", "a sleepy dog curled up on a soft pillow in a dog bed, an alarm clock beside it"),
        ("home_armchair_laptop", "a cosy armchair with an open laptop on it, a floor lamp and a window behind"),
        ("game_console_sofa", "a sofa with two game controllers on it facing a TV with a colourful game picture"),
        ("tablet_suitcase", "a tablet lying on top of a packed suitcase covered with travel stickers"),
        ("superhero_mug", "a big coffee mug with a red heart on it and a small red superhero cape draped next to it"),
    ]),

    # ---------------- UNIT 2 ----------------
    ("Л2.1", "u2", 3, 3, "object", "Одежда 1", None, [
        ("clothes_coat", "a long warm winter coat with buttons"),
        ("clothes_jeans", "a pair of blue jeans"),
        ("clothes_shoes", "a pair of black school shoes"),
        ("clothes_skirt", "a pleated skirt"),
        ("clothes_tshirt", "a plain T-shirt"),
        ("clothes_trousers", "a pair of smart dark trousers"),
        ("clothes_boots", "a pair of brown boots"),
        ("clothes_cap", "a baseball cap"),
        ("clothes_dress", "a summer dress"),
    ]),
    ("Л2.2", "u2", 3, 3, "object", "Одежда 2", None, [
        ("clothes_hoodie", "a hoodie with a hood and a front pocket"),
        ("clothes_jacket", "a zipped jacket"),
        ("clothes_shirt", "a button-up shirt with a collar"),
        ("clothes_jumper", "a knitted jumper"),
        ("clothes_tracksuit", "a tracksuit: a zipped top and matching trousers laid side by side"),
        ("clothes_gloves", "a pair of warm gloves"),
        ("clothes_scarf", "a long knitted scarf"),
        ("clothes_shorts", "a pair of shorts"),
        ("clothes_trainers", "a pair of trainers"),
    ]),
    ("Л2.3", "u2", 2, 2, "object", "Топ и раскладки",
     "Раскладки — вместо мальчика и девочки в одежде («Her jacket is grey…»). Цвета в промпте важны: по ним задание.", [
        ("clothes_top", "a sleeveless top"),
        ("outfit_her", "a neat flat-lay outfit seen from above: a grey jacket, a pink jumper, blue jeans and brown boots"),
        ("outfit_his", "a neat flat-lay outfit seen from above: a blue cap, a green hoodie, black trousers and white trainers"),
        ("items_flatlay", "a neat flat-lay seen from above: a cap, a mobile phone, a shirt, jeans, trainers and a skateboard"),
    ]),
    ("Л2.4", "u2", 2, 3, "object", "Прилагательные и супер-рюкзак",
     "Пары: big/small, long/short, new/old, cool/boring, too big.", [
        ("adj_big_small", "a very big T-shirt and a very small T-shirt side by side"),
        ("adj_long_short", "a very long scarf and a very short scarf side by side"),
        ("adj_new_old", "a shiny new trainer and a worn old dirty trainer side by side"),
        ("adj_cool_boring", "a bright cool cap with a lightning bolt next to a plain grey boring cap"),
        ("adj_too_big", "a huge jacket hanging on a tiny coat hanger, much too big for it"),
        ("super_backpack", "a red backpack with small wheels and a little pocket with a cat peeking out of it"),
    ]),
    ("Л2.5", "u2", 2, 2, "scene", "this / that / these / those",
     "Близко — крупно на переднем плане, далеко — маленькое в глубине комнаты. Ячейки: this, these, that, those.", [
        ("dem_this", "one T-shirt very close in the foreground, a long empty room behind"),
        ("dem_these", "three T-shirts very close in the foreground, a long empty room behind"),
        ("dem_that", "one small T-shirt far away at the end of a long empty room"),
        ("dem_those", "three small T-shirts far away at the end of a long empty room"),
    ]),
    ("Л2.6", "u2", 2, 3, "object", "Гаджеты", None, [
        ("gadget_games_console", "a games console with a controller"),
        ("gadget_mobile_phone", "a smartphone"),
        ("gadget_mountain_bike", "a mountain bike"),
        ("gadget_laptop", "an open laptop"),
        ("gadget_skateboard", "a skateboard"),
        ("gadget_tablet", "a tablet"),
    ]),

    # ---------------- UNIT 3 ----------------
    ("Л3.1", "u3", 2, 3, "scene", "Комнаты", None, [
        ("room_bathroom", "a bathroom with a bath, a washbasin, a mirror and a towel"),
        ("room_bedroom", "a bedroom with a bed and pillow and a bedside table with a lamp"),
        ("room_kitchen", "a kitchen with a cooker, a fridge, a table and a pot"),
        ("room_garage", "a garage with its door open and a car inside"),
        ("room_garden", "a garden in front of a house with grass, flowers and a tree"),
        ("room_living_room", "a living room with a sofa, a TV, a rug and a floor lamp"),
    ]),
    ("Л3.2", "u3", 2, 3, "object", "Части дома и угощение",
     "floor, door, wall, window + бутерброд и чай для фраз гостя (Homework 4).", [
        ("part_floor", "a square piece of wooden parquet floor seen at an angle"),
        ("part_door", "a wooden front door with a handle"),
        ("part_wall", "a piece of painted brick wall"),
        ("part_window", "a window with a white frame and curtains"),
        ("phrase_sandwich", "a sandwich on a plate"),
        ("phrase_here_you_are", "a cup of tea and biscuits on a small tray"),
    ]),
    ("Л3.3", "u3", 3, 3, "object", "Мебель 1", None, [
        ("furn_armchair", "a soft armchair"),
        ("furn_bath", "a bath on little legs"),
        ("furn_bed", "a bed with a duvet and a pillow"),
        ("furn_table", "a dining table"),
        ("furn_fridge", "a fridge"),
        ("furn_sofa", "a sofa"),
        ("furn_wardrobe", "a wardrobe with two doors"),
        ("furn_carpet", "a patterned carpet seen at an angle"),
        ("furn_cushion", "a decorative cushion"),
    ]),
    ("Л3.4", "u3", 3, 3, "object", "Мебель 2 и фразы гостя", None, [
        ("furn_lamp", "a floor lamp"),
        ("furn_plant", "a plant in a pot"),
        ("furn_poster", "a poster with a picture of a rocket pinned to a wall"),
        ("furn_tv", "a TV on a low stand"),
        ("furn_bookcase", "a bookcase full of books"),
        ("furn_shower", "a shower cabin with a glass door"),
        ("phrase_come_in", "an open front door with a doormat in front of it"),
        ("phrase_upstairs", "a wooden staircase going up"),
        ("phrase_shoes", "a pair of trainers on a doormat by a door"),
    ]),

    # ---------------- UNIT 4 ----------------
    # Части тела и волосы — ждём решения Анны.
    ("Л4.1", "u4", 2, 3, "cartoon", "Характер — зверята", None, [
        ("pers_clever", "an owl wearing glasses reading a book"),
        ("pers_friendly", "a happy puppy waving its paw"),
        ("pers_funny", "a laughing monkey"),
        ("pers_helpful", "a hedgehog carrying an apple to share"),
        ("pers_nice", "a kitten giving a flower"),
        ("pers_sporty", "a bunny in trainers holding a ball"),
    ]),
    ("Л4.2", "u4", 1, 2, "scene", "Сцены к Homework 3 и 4",
     "Два монстра — вместо кадра со Шреком.", [
        ("scene_two_monsters", "two friendly green cartoon monsters standing side by side, one tall and thin, one short and round"),
        ("scene_alarm_clock", "an alarm clock with plain tick marks, its hands at half past nine, on a bedside table next to a school backpack, morning light"),
    ]),

    # ---------------- UNIT 5 ----------------
    ("Л5.1", "u5", 3, 3, "cartoon", "Глаголы 1", "Действие без людей — предметом или животным.", [
        ("verb_act", "comedy and tragedy theatre masks on a small stage with red curtains"),
        ("verb_climb", "a monkey climbing up a tree trunk"),
        ("verb_cook", "a frying pan with eggs on a cooker and a pot of vegetables"),
        ("verb_dive", "a diving mask, a snorkel and flippers under water with bubbles"),
        ("verb_fix", "a spanner and a screwdriver next to a bicycle with a loose chain"),
        ("verb_fly", "a small colourful bird flying"),
        ("verb_jump", "a kangaroo jumping high"),
        ("verb_read", "an open book with a bookmark"),
        ("verb_ride", "a bicycle"),
    ]),
    ("Л5.2", "u5", 2, 3, "cartoon", "Глаголы 2", None, [
        ("verb_sing", "a microphone with music notes floating around it"),
        ("verb_run", "a cheetah running fast"),
        ("verb_swim", "a dolphin swimming in the waves"),
        ("verb_write", "a pen writing lines in a notebook"),
        ("verb_skateboard", "a skateboard jumping off a ramp"),
        ("verb_draw", "a palette, a brush, coloured pencils and a drawing of a house"),
    ]),
    ("Л5.3", "u5", 3, 3, "object", "Вещи к заданиям Unit 5", None, [
        ("obj_newspaper", "a folded newspaper"),
        ("obj_screwdriver", "a screwdriver"),
        ("obj_goggles", "swimming goggles"),
        ("obj_guitar", "an acoustic guitar"),
        ("obj_crayons_drawing", "wax crayons next to a child's drawing of a sun and a tree"),
        ("obj_mixing_bowl", "a mixing bowl with a whisk and vegetables beside it"),
        ("obj_broken_laptop", "an open laptop with a screwdriver lying next to it"),
        ("obj_french_flag", "a small French flag on a little stand"),
        ("obj_book_stack", "a stack of books with an apple on top"),
    ]),
    ("Л5.4", "u5", 2, 3, "cartoon", "Чем заняться: play / ride / make", None, [
        ("coll_play_piano", "piano keys with music notes above them"),
        ("coll_ride_horse", "a horse with a saddle in a meadow"),
        ("coll_make_cupcakes", "cupcakes with cream and a piping bag"),
        ("coll_play_football", "a football in front of a goal"),
        ("coll_ride_bike", "a bicycle with a helmet hanging on the handlebars"),
        ("coll_make_poster", "a big poster sheet with paints and brushes around it"),
    ]),
    ("Л5.5", "u5", 2, 3, "cartoon", "Собаки, хомяк и мишки",
     "Три мишки — варианты ответа в Homework 6: верный — с голубыми глазами.", [
        ("animal_labrador", "a friendly labrador sitting"),
        ("animal_beagle_puppy", "a beagle puppy running"),
        ("animal_hamster", "a hamster"),
        ("teddy_black_eyes", "a teddy bear with black button eyes"),
        ("teddy_torn", "an old torn teddy bear with one eye missing"),
        ("teddy_blue_eyes", "a teddy bear with new bright blue eyes"),
    ]),

    # ---------------- UNIT 6 ----------------
    ("Л6.1", "u6", 3, 3, "cartoon", "Распорядок дня 1", "Действие — предметом, без людей.", [
        ("da_get_up", "a ringing alarm clock on a bedside table next to an unmade bed, morning sun"),
        ("da_go_to_school", "a school building with a backpack on the path in front"),
        ("da_go_to_bed", "a bed with a pillow and a duvet, the moon in the window"),
        ("da_have_a_shower", "a shower head with running water, soap and a towel"),
        ("da_have_breakfast", "a bowl of cereal with milk, a glass of juice and toast"),
        ("da_have_lunch", "a lunch box with a sandwich and an apple"),
        ("da_have_dinner", "a plate with dinner and a candle, evening"),
        ("da_have_lessons", "a school desk with textbooks in front of a green board with simple chalk drawings of shapes"),
        ("da_do_homework", "a notebook with a pencil and a textbook on a desk"),
    ]),
    ("Л6.2", "u6", 3, 3, "cartoon", "Распорядок дня 2", None, [
        ("da_hang_out_with_friends", "three scooters leaning on a bench in a park"),
        ("da_listen_to_music", "headphones with music notes"),
        ("da_tidy_my_room", "a mop, a box of toys and a pile of folded clothes"),
        ("da_watch_tv", "a TV with a remote control"),
        ("obj_tennis", "two tennis rackets and a ball by a net"),
        ("obj_late_clock", "an alarm clock with little legs running away"),
        ("obj_busy_planner", "a diary covered with sticky notes and a phone"),
        ("obj_gym", "a treadmill and dumbbells"),
        ("obj_school_canteen", "a school lunch on a tray"),
    ]),
    ("Л6.3", "u6", 3, 3, "object", "Майк и Даша, еда и игры", None, [
        ("md_pizza", "a pizza"),
        ("md_basketball", "a basketball by a hoop"),
        ("md_new_york", "a city skyline with tall skyscrapers"),
        ("md_ballet", "a pair of pink ballet pointe shoes"),
        ("md_pancakes", "a stack of pancakes with berries"),
        ("md_maths", "an open maths notebook with a ruler, a protractor and a calculator"),
        ("obj_computer_games", "a game controller in front of a monitor with a game"),
        ("obj_family_dinner", "a dinner table laid with four plates"),
        ("obj_ice_cream_chocolate", "a chocolate ice cream cone"),
    ]),

    # ---------------- UNIT 7 ----------------
    ("Л7.1", "u7", 3, 3, "cartoon", "Дикие животные 1", None, [
        ("animal_bird", "a small bright bird on a branch"),
        ("animal_butterfly", "a butterfly with open wings"),
        ("animal_crocodile", "a green crocodile, whole body, side view"),
        ("animal_elephant", "a grey elephant with its trunk up"),
        ("animal_fish", "a goldfish"),
        ("animal_fly", "a friendly little fly"),
        ("animal_frog", "a green frog"),
        ("animal_giraffe", "a giraffe, whole body"),
        ("animal_kangaroo", "a kangaroo with a baby in its pouch"),
    ]),
    ("Л7.2", "u7", 3, 3, "cartoon", "Дикие животные 2", None, [
        ("animal_lion", "a lion with a big mane"),
        ("animal_monkey", "a monkey hanging from a vine"),
        ("animal_snake", "a snake curled up"),
        ("animal_spider", "a spider on its web"),
        ("animal_tiger", "a tiger"),
        ("animal_whale", "a blue whale, side view, with a water spout"),
        ("animal_cat", "a grey cat"),
        ("animal_rabbit", "a white and grey rabbit with leaves and carrots"),
        ("adj_cute", "a fluffy kitten with big eyes"),
    ]),
    ("Л7.3", "u7", 2, 3, "cartoon", "Какие они? И котята", None, [
        ("adj_dangerous", "a shark with its mouth open"),
        ("adj_fast", "a cheetah running with speed lines"),
        ("adj_slow", "a snail"),
        ("adj_strong", "a gorilla lifting a big log"),
        ("adj_ugly", "a warty toad"),
        ("kittens_basket", "a basket with six kittens: three black, two black and white, one grey"),
    ]),
    ("Л7.4", "u7", 1, 3, "scene", "Сцены Unit 7", None, [
        ("scene_shark", "a shark swimming under water among small fish"),
        ("scene_zoo_ticket_office", "a zoo ticket office window with tickets on the counter"),
        ("scene_cafe_counter", "a cafe counter with a cheese sandwich on a plate and a till"),
    ]),

    # ---------------- UNIT 8 ----------------
    ("Л8.1", "u8", 3, 3, "object", "Спорт 1", "Спорт — инвентарём, без людей.", [
        ("sport_badminton", "a badminton racket and a shuttlecock"),
        ("sport_basketball", "a basketball by a hoop"),
        ("sport_cycling", "a racing bicycle"),
        ("sport_football", "a football and a goal"),
        ("sport_hockey", "an ice hockey stick and a puck on ice"),
        ("sport_ice_skating", "a pair of white figure skates on ice"),
        ("sport_roller_skating", "a pair of roller skates"),
        ("sport_sailing", "a sailing boat on the water"),
        ("sport_skateboarding", "a skateboard on a ramp"),
    ]),
    ("Л8.2", "u8", 3, 3, "object", "Спорт 2 и здоровье", None, [
        ("sport_skiing", "skis and poles in the snow"),
        ("sport_swimming", "a swimming pool with lane ropes, goggles and a swimming cap"),
        ("sport_table_tennis", "table tennis bats and a ball on a table"),
        ("sport_taekwondo", "a white taekwondo uniform folded with a black belt"),
        ("sport_tennis", "a tennis racket and a yellow ball"),
        ("sport_volleyball", "a volleyball by a net"),
        ("sport_windsurfing", "a windsurfing board with a sail on a wave"),
        ("life_brush_teeth", "a toothbrush with toothpaste and a glass"),
        ("life_drink_water", "a glass and a bottle of water"),
    ]),
    ("Л8.3", "u8", 3, 3, "cartoon", "Погода", None, [
        ("weather_sunny", "a bright sun in a blue sky"),
        ("weather_cloudy", "fluffy grey and white clouds"),
        ("weather_rainy", "a dark cloud with rain and puddles below"),
        ("weather_snowy", "snow falling on snowy ground"),
        ("weather_windy", "a tree bending in the wind with leaves flying"),
        ("weather_foggy", "fog over a field and trees"),
        ("weather_hot", "a blazing sun and a thermometer with the red line very high"),
        ("weather_cold", "a thermometer with the line very low and icicles"),
        ("weather_warm", "a gentle sun over a spring meadow with flowers"),
    ]),
    ("Л8.4", "u8", 2, 2, "scene", "Времена года", "Одно и то же дерево в четыре времени года.", [
        ("season_spring", "the same tree in spring with pink blossom"),
        ("season_summer", "the same tree in summer, full green leaves"),
        ("season_autumn", "the same tree in autumn with orange leaves falling"),
        ("season_winter", "the same tree in winter, bare branches covered with snow"),
    ]),
    ("Л8.5", "u8", 2, 3, "cartoon", "Здоровый образ жизни", None, [
        ("life_do_exercise", "dumbbells, trainers and a skipping rope"),
        ("life_fruit_vegetables", "a bowl of fruit and vegetables"),
        ("life_bed_early", "a bed, the moon in the window, an alarm clock on the bedside table"),
        ("life_have_friends", "two puppies playing together"),
        ("life_sleep", "a pillow and a duvet with a crescent moon above"),
        ("life_healthy_heart", "a heart shape made of fruit, a dumbbell and a water bottle"),
    ]),

    # ---------------- FINAL TEST ----------------
    ("ЛФ.1", "final", 1, 2, "scene", "Гостиные к финальному тесту",
     "Левая — для «диаграммы» (подписать вещи), правая — для чтения: кот под креслом, лампа на шкафу, напитки на столе, большое закрытое окно.", [
        ("final_living_room", "a living room with two armchairs, a bookcase by the window, a rug, a small coffee table, a cabinet and pictures on the wall"),
        ("final_living_room_cat", "a living room with a cat under an armchair, a lamp on top of a cupboard, drinks on a table and a big closed window"),
    ]),
    ("ЛФ.2", "final", 2, 3, "object", "Вещи к финальному тесту", None, [
        ("final_grapes", "a bunch of grapes"),
        ("final_car", "a small red car"),
        ("final_boot", "one brown boot"),
        ("final_chairs", "three chairs in a row"),
        ("final_computer", "a desktop computer with a keyboard"),
        ("final_radio", "an old-fashioned radio"),
    ]),
]


def prompt(sheet):
    sid, unit, rows, cols, reg, title, note, cells = sheet
    style = STYLE[reg]
    if rows == cols == 1:
        _, desc = cells[0]
        body = [f"One single scene filling the frame: {desc}."]
    else:
        what = "illustrations" if reg == "scene" else "picture cards"
        head = GRID_CARDS.format(n=len(cells), what=what, rows=rows, cols=cols)
        if reg != "scene":
            head = head.replace("standalone picture,", "standalone picture on pure white,")
        items = "; ".join(f"{i}) {d}" for i, (_, d) in enumerate(cells, 1))
        body = [head, items + "."]
    return "\n".join(body + [NO_PEOPLE, style + " " + NO_TEXT, size_line(rows, cols)])


def check():
    errors, seen = [], {}
    for sid, unit, rows, cols, reg, title, note, cells in SHEETS:
        if rows * cols != len(cells):
            errors.append(f"{sid}: сетка {rows}×{cols}, а ячеек {len(cells)}")
        if cols > 3:
            errors.append(f"{sid}: больше трёх колонок")
        for key, _ in cells:
            if key and key in seen:
                errors.append(f"{sid}: ключ {key} уже есть в {seen[key]}")
            seen[key] = sid
    return errors


HEAD = """# Go Getter 1 — ЛИСТЫ ПРОМПТОВ НА КАРТИНКИ

Собирается из `tools/gg1_sheets.py` — **правится там**, не здесь: тот же
список ячеек режет `tools/gg1_cut.py`, и промпт с нарезкой не расходятся.

Один промпт = один лист с сеткой. Генерирует Анна, присылает в чат с
подписью номера листа (Л0.1, Л2.3, ЛФ.1…), лист режется на карточки webp в
`media/gg1/uN/`. Номер листа не переиспользуется: выброшенный лист оставляет
пустой номер.

Каждый промпт самодостаточный — сетка, стиль, запрет людей и текста, размер
внутри, копируется целиком. Ячейки нумеруются слева направо, сверху вниз.

## Правила (те же, что у SM3 — см. `docs/SM3_листы_промптов.md`)

1. **Людей нет нигде** — ни детей, ни рук, ни лиц, ни силуэтов.
2. **Не больше 3 колонок** — иначе ячейка мельче 512 px и мылит при нарезке.
3. **Никаких узнаваемых товаров** — `generic design, not resembling any real product`.
4. **Один стилевой регистр на лист**: предметы — реалистичный 3D, животные и
   символы действий — мультяшный глянец, комнаты и места — полу-мультяшные сцены.

## Чего не генерируем

| Что | Откуда |
|---|---|
| Кляксы цветов (Unit 0) | скрипт `tools/gg1_colours.py`, svg |
| Флаги стран (Unit 1) | скрипт, svg — генератор путает полосы и звёзды |
| Циферблаты (Unit 6) | скрипт, svg — генератор путает стрелки |
| Обучающие карточки методиста, картинки учебника | вырезаются из PDF выгрузки (`tools/gg1_pdf_frames.py`) |
| Фото без людей из выгрузки (Лондон, Париж, библиотека, парк) | из PDF выгрузки |
| Приветствия, похвалы, прощания | `media/shared/`; Микки, Минни, Шрек, Чип и Дейл, Мистер Бин из выгрузки не берём |
| Вещь, которая уже нарисована в другом юните | берётся по старому ключу (ручка из Л0.1, кроссовки из Л2.2, животные Unit 7 в финальном тесте…) |

## 🟥 Ждут решения Анны — листов пока нет

* **Unit 1 · семья** (mum, dad, granny, cousin…) — это люди.
* **Unit 4 · части тела, лицо, волосы** — то же.
"""


def render():
    out = [HEAD]
    unit_names = {"u0": "UNIT 0 · GET STARTED!", "u1": "UNIT 1", "u2": "UNIT 2", "u3": "UNIT 3",
                  "u4": "UNIT 4", "u5": "UNIT 5", "u6": "UNIT 6", "u7": "UNIT 7", "u8": "UNIT 8",
                  "final": "FINAL TEST"}
    cur = None
    total = 0
    for sheet in SHEETS:
        sid, unit, rows, cols, reg, title, note, cells = sheet
        if unit != cur:
            n = sum(1 for s in SHEETS if s[1] == unit)
            out.append(f"\n---\n\n# {unit_names[unit]} — листов: {n}\n")
            cur = unit
        kind = "сцена" if rows == cols == 1 else f"{len(cells)} карт. ({cols}×{rows})"
        out.append(f"### {sid} · {title} — {kind}, {REGISTER_RU[reg]}")
        if note:
            out.append(note)
        out.append("```\n" + prompt(sheet) + "\n```\n")
        total += len([c for c in cells if c[0]])
    out.insert(1, f"\n**Всего листов: {len(SHEETS)}, картинок: {total}.**\n")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    errors = check()
    if errors:
        for e in errors:
            print("·", e, file=sys.stderr)
        sys.exit(1)
    if args.check:
        print(f"листов {len(SHEETS)}, всё сходится")
        return
    with open(DOC, "w", encoding="utf-8") as f:
        f.write(render())
    print("записан", os.path.relpath(DOC, ROOT))


if __name__ == "__main__":
    main()
