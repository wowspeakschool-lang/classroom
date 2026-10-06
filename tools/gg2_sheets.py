#!/usr/bin/env python3
"""Листы картинок Go Getter 2 — один источник для промптов и для нарезки.

Каждый лист описан один раз: юнит, сетка, стилевой регистр и ячейки (ключ
файла + что нарисовать). Отсюда собирается docs/GG2_листы_промптов.md, и
отсюда же нарезка берёт таблицу «лист → имена карточек»: порядок ячеек в
промпте и порядок имён при нарезке — один и тот же список.

Номер листа — сквозной номер по порядку в SHEETS (у GG3 нумерация
продолжается, см. tools/gg3_sheets.py). После отправки Анне номера
заморожены: новые листы дописываются только в конец списка, выброшенный
лист остаётся с пометкой, номер не переиспользуется.

  python3 tools/gg2_sheets.py            пересобрать docs/GG2_листы_промптов.md
  python3 tools/gg2_sheets.py --check    только проверить (дубли ключей, размер сетки)

Стиль и формулировки — те же, что у GG1 (tools/gg1_sheets.py в ветке
claude/gg1), чтобы курсы выглядели одной серией. Люди разрешены (решение
Анны 05.10.2026: «генерируй что нужно») — стилизованные 3D-персонажи, не фото.
"""
import argparse, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NO_PEOPLE = "No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere."
NO_TEXT = "Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere."
WHITE_BG = "Plain flat pure white background, no shadow on the background."

STYLE = {
    # предметные карточки — узнаваемость важнее
    "object": "Realistic 3D render, soft studio lighting from the top-left, clean product-style "
              "but friendly and colourful, generic design, not resembling any real product. " + WHITE_BG,
    # животные и символы — мультяшный глянец
    "cartoon": "Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid "
               "saturated colours, soft even light from the top-left. " + WHITE_BG,
    # места и сцены без людей — полу-мультяшный 3D, фон — сама сцена
    "scene": "Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated "
             "colours, warm soft light, everything clearly visible and easy to recognise.",
    # люди на белом — как карточки
    "people": "Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive "
              "faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated "
              "colours, soft even light from the top-left. " + WHITE_BG,
    # сцены с людьми
    "people_scene": "Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive "
                    "faces, stylised and clearly not photorealistic, soft rounded shapes, vivid "
                    "saturated colours, warm soft light, everything clearly visible and easy to recognise.",
}
PEOPLE = {"people", "people_scene"}
SCENES = {"scene", "people_scene"}

REGISTER_RU = {"people": "персонажи на белом", "people_scene": "сцены с персонажами",
               "object": "предметы, реалистичный 3D", "cartoon": "мультяшный глянец",
               "scene": "места и сцены, без людей"}

GRID = ("A sheet of {n} separate {what} arranged in a clean grid of {cols_w} and {rows_w}, "
        "equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. "
        "Every {item} is complete and centred in its cell with a generous empty margin, not touching any "
        "other {item} or the edge of the sheet, nothing crossing between cells.")

ROW_NAMES = ["Row 1", "Row 2", "Row 3"]


def size_line(rows, cols):
    if rows == cols == 1:
        return "Output size: 2048 x 1365 px, landscape."
    if rows == cols:
        return "Output size: 2048 x 2048 px, each cell at least 600 px."
    if cols > rows:
        return "Output size: 2048 x 1365 px, each cell at least 600 px." if (cols, rows) == (3, 2) \
            else "Output size: 2048 x 1024 px, each cell at least 600 px."
    return "Output size: 1365 x 2048 px, each cell at least 600 px."


# (юнит, строк, колонок, регистр, заголовок, пояснение для Анны, ячейки[(ключ, описание)], доп. строка)
# Ключ — имя файла в media/gg2/<юнит>/ без расширения.
SHEETS = [
    # ---------------- UNIT 0 (тест) ----------------
    ("u0", 1, 1, "people_scene", "Комната подростка",
     "Тест Unit 0, SPEAKING I. Вопросы остаются как в выгрузке: Where is the boy? Where is his bag? "
     "What has he got on his shelves? Can the boy play the guitar?", [
        ("u0_scene_bedroom",
         "a cosy teenager's bedroom. A boy of about thirteen sits on his bed playing a small guitar. "
         "A mobile phone lies on the bed beside him. Next to the bed stands a tall bookshelf with books "
         "and a green plant in a pot. A dartboard and two colourful picture posters hang on the wall. "
         "A yellow school backpack lies on the floor next to the bookshelf"),
    ], None),
    ("u0", 2, 3, "object", "Слова теста Unit 0",
     "По желанию: картинки-подсказки к блоку 1 теста (впиши слово).", [
        ("u0_skateboard", "a skateboard with colourful wheels"),
        ("u0_armchair", "a soft cosy armchair"),
        ("u0_wardrobe", "a wooden wardrobe for clothes with two doors"),
        ("u0_shelves", "three wooden wall shelves with books and a small plant"),
        ("u0_draw", "an open sketchbook with a drawing of a house and a tree, colour pencils beside it"),
        ("u0_february", "a wall calendar page with a snowflake picture on top and a plain grid of empty day squares"),
    ], None),

    # ---------------- UNIT 1 ----------------
    ("u1", 3, 3, "object", "Школьные предметы",
     "Словарь Homework 1, тест. Каждый предмет — набором вещей.", [
        ("u1_subj_art", "a paint palette with brushes and paint tubes"),
        ("u1_subj_computer", "a computer monitor with a keyboard and a mouse"),
        ("u1_subj_english", "a stack of school books with a small British flag on a stand"),
        ("u1_subj_french", "a school book, a small Eiffel Tower souvenir and a small French flag on a stand"),
        ("u1_subj_geography", "a globe and a folded paper map"),
        ("u1_subj_history", "an old paper scroll, a sand timer and a small ancient stone column"),
        ("u1_subj_maths", "a calculator with blank buttons, a ruler and a set square"),
        ("u1_subj_music", "an acoustic guitar with a small keyboard and floating music notes"),
        ("u1_subj_pe", "a football, a basketball, a pair of trainers and a whistle"),
    ], None),
    ("u1", 3, 3, "object", "Наука и школьные вещи",
     "Science + школьные принадлежности (Homework 1, 7, тест).", [
        ("u1_subj_science", "a glass flask with green liquid, a microscope and a horseshoe magnet"),
        ("u1_calculator", "a pocket calculator with blank buttons"),
        ("u1_dictionary", "a thick hardcover dictionary"),
        ("u1_laptop", "an open laptop"),
        ("u1_map", "an unfolded world map"),
        ("u1_paints", "a box of watercolour paints with a brush"),
        ("u1_pencil_case", "a zipped pencil case"),
        ("u1_rubber", "a rubber eraser"),
        ("u1_ruler", "a plastic ruler with plain tick marks"),
    ], None),
    ("u1", 3, 3, "object", "Вещи, обед, дорога",
     "Школьные вещи (Homework 1) и еда / дорога в школу (Homework 2, 5, 7).", [
        ("u1_scissors", "a pair of scissors with rounded tips"),
        ("u1_trainers", "a pair of trainers"),
        ("u1_school_bag", "a school backpack"),
        ("u1_pencil", "a yellow pencil with a pink eraser tip"),
        ("u1_chicken_chips", "chicken and chips on a plate"),
        ("u1_fish_chips", "fish and chips in a paper cone"),
        ("u1_lunch_box", "an open lunch box with a sandwich, an apple and a carton of juice"),
        ("u1_school_bus", "a yellow school bus"),
        ("u1_tv", "a flat TV on a stand"),
    ], None),
    ("u1", 3, 3, "scene", "Места в школе",
     "Словарь Homework 5. Без людей.", [
        ("u1_canteen", "a school canteen with a serving counter, trays and tables"),
        ("u1_classroom", "a classroom with desks, chairs and a board"),
        ("u1_computer_room", "a computer room with rows of computers"),
        ("u1_gym", "a school gym with climbing bars, mats and a basketball hoop"),
        ("u1_hall", "a school hall with a row of lockers along the wall"),
        ("u1_library", "a school library with tall bookshelves and a reading table"),
        ("u1_playground", "a school playground with a slide, swings and a hopscotch court"),
        ("u1_staff_room", "a staff room with a big table, piles of exercise books and coffee mugs"),
        ("u1_sports_school", "a modern school building with a big basketball court in front"),
    ], None),
    ("u1", 3, 3, "object", "Хобби",
     "Homework 3–7: do ballet, play chess… Каждое хобби — набором вещей.", [
        ("u1_ballet", "ballet pointe shoes and a pink tutu"),
        ("u1_karate", "a white karate kimono with a black belt"),
        ("u1_pottery", "a pottery wheel with a clay pot"),
        ("u1_basketball", "a basketball hoop and a basketball"),
        ("u1_chess", "a chessboard with chess pieces"),
        ("u1_football", "a football in front of a small goal"),
        ("u1_tennis", "a tennis racket and a tennis ball"),
        ("u1_painting", "an easel with a painting of flowers"),
        ("u1_music", "big headphones and a small music player"),
    ], None),
    ("u1", 3, 3, "people_scene", "Стив и его школа",
     "Homework 5 (2): картинки к «верно/неверно» про Стива; последняя — Лили (Homework 6). Вместо фото детей.", [
        ("u1_steve", "Steve, a cheerful eleven-year-old boy with red hair and a green school jumper, standing in front of his school"),
        ("u1_steve_late", "Steve hurrying through the classroom door, a round wall clock above the door"),
        ("u1_steve_maths", "Steve at the board in a maths lesson, the board covered with simple sums"),
        ("u1_steve_art", "Steve at an easel in an art lesson, looking bored"),
        ("u1_steve_lunch", "Steve carrying a lunch tray in the school canteen"),
        ("u1_steve_pe", "Steve running happily in a P.E. lesson in the school gym"),
        ("u1_steve_basketball", "Steve playing basketball with his classmates"),
        ("u1_tennis_players", "two children playing tennis on a tennis court"),
        ("u1_lily_bus", "Lily, a girl of eleven with a backpack, waiting at a bus stop with two friends"),
    ], "Steve is the same boy in cells 1-7: red hair, green school jumper."),
    ("u1", 2, 3, "people_scene", "Марк, интервью",
     "Homework 6: Марк и «верно/неверно»; Homework 4: интервью. Вместо фото.", [
        ("u1_mark", "Mark, a smiling boy of eleven with dark curly hair and a blue hoodie"),
        ("u1_history_lesson", "a history lesson: pupils at their desks, a teacher pointing at a picture of a castle"),
        ("u1_mark_science", "Mark doing a science experiment with colourful flasks"),
        ("u1_kids_football", "children playing football in a school yard"),
        ("u1_mark_chess", "Mark playing chess at a table"),
        ("u1_interview", "a young woman reporter with a microphone interviewing a man on a city street"),
    ], "Mark is the same boy in cells 1, 3 and 5: dark curly hair, blue hoodie."),
    ("u1", 2, 2, "people_scene", "Клуб, балет, дорога в школу",
     "Homework 4 (Карен в шахматном клубе), Homework 7 (составь предложение).", [
        ("u1_karen_chess_club", "a girl of eleven talking to a friendly male teacher at a chess club table with chessboards"),
        ("u1_ballet_girl", "a girl doing ballet in a dance studio"),
        ("u1_walk_to_school", "a boy with a backpack walking to school along a path"),
        ("u1_football_morning", "a group of children playing football on a green field in the morning"),
    ], None),
    ("u1", 1, 1, "people_scene", "Школьная столовая",
     "Тест Unit 1, SPEAKING I. Вопросы остаются: Where are the students? How many students can you see?…", [
        ("u1_scene_canteen",
         "two friendly school students in school uniforms, a boy and a girl, sitting at a table in a bright "
         "school canteen and smiling. On the table: a tray with apples, bananas and oranges, two sandwiches, "
         "a glass of orange juice and a bottle of water. A serving counter with food in the background"),
    ], None),

    # ---------------- UNIT 2 ----------------
    ("u2", 3, 3, "object", "Еда 1",
     "Словарь Homework 1.", [
        ("u2_apple", "a red apple"),
        ("u2_biscuits", "a small pile of round biscuits"),
        ("u2_bread", "a loaf of bread"),
        ("u2_cereal", "a bowl of breakfast cereal with milk"),
        ("u2_cheese", "a wedge of yellow cheese"),
        ("u2_chicken", "a roast chicken on a plate"),
        ("u2_chips", "a portion of chips"),
        ("u2_fish", "a whole fish on a plate with a lemon slice"),
        ("u2_fruit", "a bowl of mixed fruit"),
    ], None),
    ("u2", 3, 3, "object", "Еда 2",
     "Словарь Homework 1.", [
        ("u2_ham", "slices of ham on a small board"),
        ("u2_meat", "a raw steak on a board"),
        ("u2_orange_juice", "a glass of orange juice with an orange beside it"),
        ("u2_pancakes", "a stack of pancakes"),
        ("u2_pasta", "a plate of spaghetti with tomato sauce"),
        ("u2_potato", "two potatoes"),
        ("u2_rice", "a bowl of white rice"),
        ("u2_salad", "a bowl of green salad"),
        ("u2_sandwich", "a sandwich cut in half"),
    ], None),
    ("u2", 3, 3, "object", "Еда 3 и блюда",
     "Словарь Homework 1; три блюда Сьюзи — Homework 5.", [
        ("u2_sausage", "two sausages"),
        ("u2_tomato", "a red tomato"),
        ("u2_tuna", "an open tin of tuna"),
        ("u2_vegetables", "a pile of fresh vegetables"),
        ("u2_water", "a bottle of water and a glass of water"),
        ("u2_yoghurt", "a small pot of yoghurt with a spoon"),
        ("u2_english_breakfast", "an English breakfast on a plate: sausages, two fried eggs, a grilled tomato and beans"),
        ("u2_fish_and_chips", "fish and chips on a plate"),
        ("u2_chicken_rice", "chicken and rice on a plate"),
    ], None),
    ("u2", 3, 3, "object", "Еда 4",
     "Словарь Homework 2.", [
        ("u2_butter", "a block of butter on a dish"),
        ("u2_chocolate", "a bar of chocolate, partly unwrapped"),
        ("u2_egg", "two eggs"),
        ("u2_flour", "a paper bag of flour with a little flour spilled"),
        ("u2_lemon", "a lemon"),
        ("u2_milk", "a glass of milk and a milk carton"),
        ("u2_strawberry", "three strawberries"),
        ("u2_sugar", "a sugar bowl with sugar cubes"),
        ("u2_banana", "a bunch of bananas"),
    ], None),
    ("u2", 2, 3, "object", "Ёмкости",
     "Словарь Homework 3, Homework 7.", [
        ("u2_bar_of_chocolate", "a bar of chocolate"),
        ("u2_bottle_of_water", "a bottle of water"),
        ("u2_can_of_cola", "a can of cola with plain colours"),
        ("u2_carton_of_juice", "a carton of juice"),
        ("u2_jar_of_jam", "a jar of strawberry jam"),
        ("u2_packet_of_biscuits", "a packet of biscuits"),
    ], None),
    ("u2", 3, 3, "people_scene", "Герои Unit 2",
     "Вместо фото людей: Макс (Homework 1), Аня (Homework 2), Том и Мэтт (Homework 2), кафе (Homework 4), "
     "Сьюзи (Homework 5), Пенни с папой (Homework 6), хот-доги и тосты (Homework 7).", [
        ("u2_max", "Max, a boy of eleven, eating a red apple"),
        ("u2_anya_pancakes", "Anya, a girl of twelve in an apron, holding a plate of pancakes with banana and cream"),
        ("u2_tom_matt_list", "two young men, Tom and Matt, sitting on a sofa and writing a shopping list"),
        ("u2_cafe_waiter", "a waiter taking an order from two girls at a café table with menus"),
        ("u2_susie", "Susie, a smiling British girl of twelve, holding a plate of fish and chips"),
        ("u2_penny_breakfast", "Penny, a girl of ten, and her dad at the kitchen table at breakfast: an egg, bread with ham and a glass of milk"),
        ("u2_hot_dog_cart", "a girl buying a hot dog from a friendly man at a hot dog cart in a park"),
        ("u2_toast", "French toast on a plate next to a toaster"),
        ("u2_three_meals", "three plates in a row on a table: breakfast with cereal, lunch with soup and a sandwich, dinner with chicken and rice"),
    ], None),
    ("u2", 1, 1, "people_scene", "Семейный завтрак",
     "Тест Unit 2, SPEAKING I. Вопросы остаются: How many people…? What food can you see? Is there any cheese?", [
        ("u2_scene_breakfast",
         "a family of four having breakfast at a kitchen table in the morning: mum, dad, a girl and a boy. "
         "On the table: bread, a plate of cheese, eggs, butter, a bowl of fruit, a jug of orange juice, "
         "a carton of milk and cups of tea"),
    ], None),

    # ---------------- UNIT 3 ----------------
    ("u3", 2, 3, "object", "Гаджеты 1",
     "Словарь Homework 1, тест.", [
        ("u3_mobile_phone", "a smartphone"),
        ("u3_computer", "a desktop computer: a monitor and a computer tower"),
        ("u3_laptop", "an open laptop"),
        ("u3_camera", "a digital camera"),
        ("u3_tablet", "a tablet"),
        ("u3_tv", "a flat TV"),
    ], None),
    ("u3", 2, 3, "object", "Гаджеты 2",
     "Словарь Homework 1, тест.", [
        ("u3_headphones", "a pair of headphones"),
        ("u3_keyboard", "a computer keyboard"),
        ("u3_mouse", "a computer mouse"),
        ("u3_printer", "a printer with a sheet of paper"),
        ("u3_screen", "a computer screen with a bright colourful picture"),
        ("u3_speakers", "a pair of speakers"),
    ], None),
    ("u3", 3, 3, "people", "Что делаем с гаджетами",
     "Словарь Homework 1 (2); последние две — Джек (Homework 1) и Сара (Homework 2).", [
        ("u3_chat_online", "a boy chatting online on a laptop, chat bubbles on the screen"),
        ("u3_download_song", "a girl downloading a song on her phone, a music note and a download arrow above the phone"),
        ("u3_send_email", "a girl sending an email from a laptop, an envelope flying out of the screen"),
        ("u3_surf_internet", "a boy surfing the Internet on a tablet with colourful pictures on the screen"),
        ("u3_take_selfie", "a girl taking a selfie with her phone, smiling"),
        ("u3_talk_phone", "a boy talking on the phone"),
        ("u3_text_friend", "a girl texting a friend, message bubbles above the phone"),
        ("u3_jack", "Jack, a little boy in a yellow hat, holding a phone with a laptop and headphones beside him"),
        ("u3_sarah", "Sarah, a girl in a yellow jumper, checking her phone in the morning, sitting on her bed"),
    ], None),
    ("u3", 3, 3, "people", "Эмоции",
     "Homework 3: соедини эмоцию с картинкой; две последние — к открытым вопросам 18 и 19.", [
        ("u3_worried", "a worried boy with wide-open eyes and a slightly open mouth"),
        ("u3_angry", "an angry red-haired girl with frowning eyebrows"),
        ("u3_happy", "a happy girl with pigtails, smiling broadly"),
        ("u3_tired", "a tired girl yawning"),
        ("u3_scared", "a scared boy hiding behind his hands"),
        ("u3_sad", "a sad boy with a tear on his cheek"),
        ("u3_bored", "a bored girl resting her chin on her hand"),
        ("u3_bored_students", "a group of bored teenage students sitting in a lecture hall"),
        ("u3_worried_woman", "a worried woman holding her head with both hands"),
    ], "Every person is shown head and shoulders, facing the viewer, the emotion is very clear."),
    ("u3", 3, 3, "cartoon", "Зверята: что они делают",
     "Homework 2: соедини действие с персонажем, составь предложение.", [
        ("u3_cat_sitting", "a cat sitting"),
        ("u3_fox_running", "a fox running"),
        ("u3_animals_eating", "a rabbit and a hedgehog eating at a little table"),
        ("u3_animals_reading", "a bear cub and a puppy reading a book together"),
        ("u3_bunny_dancing", "a bunny dancing"),
        ("u3_dog_not_jumping", "a puppy sitting on a chair looking at a phone"),
        ("u3_kittens_crying", "two kittens crying"),
        ("u3_bear_panda_walking", "a bear and a panda walking side by side"),
        ("u3_pandas_not_cleaning", "two pandas sitting on the floor next to a mop and a bucket, not cleaning"),
    ], None),
    ("u3", 1, 2, "cartoon", "Зверята: эмоции",
     "Homework 3, открытые вопросы 15–16.", [
        ("u3_cat_tired", "a tired cat stretched out on a sofa"),
        ("u3_angry_bird", "an angry little blue songbird with ruffled feathers, frowning and stamping its foot, an ordinary bird, not resembling any famous cartoon or game character"),
    ], None),
    ("u3", 2, 3, "people_scene", "Герои Unit 3",
     "Вместо фото: селфи (Homework 1, 2), Гарри и Лили (Homework 6), звонок (Homework 4), "
     "изобретатель (Homework 5), видеозвонок (тест).", [
        ("u3_selfie_teens", "three teenagers taking a selfie together in a park"),
        ("u3_harry", "Harry, a boy of twelve with curly hair, holding a tablet"),
        ("u3_lily", "Lily, a girl of twelve with a bob haircut, holding a phone"),
        ("u3_phone_call", "a boy and a girl talking to each other on the phone, each in their own room"),
        ("u3_inventor", "a boy building an electronic gadget at a desk with a laptop and headphones"),
        ("u3_video_call", "a girl on a video call on a laptop, her grandparents waving on the screen"),
    ], None),
    ("u3", 1, 1, "people_scene", "У бассейна",
     "Homework 2, задание 17: три предложения «да» и три «нет» по картинке.", [
        ("u3_scene_pool",
         "a busy outdoor swimming pool on a sunny day: a boy and a girl jumping into the water, a woman "
         "reading on a sun lounger, a man eating an ice cream, two children playing with a ball, a dog "
         "sleeping in the shade and a cat watching the birds"),
    ], None),
    ("u3", 1, 1, "people_scene", "Завтрак с гаджетами",
     "Тест Unit 3, SPEAKING I. Вопросы остаются: What is each person doing? Who is using headphones?", [
        ("u3_scene_gadgets_breakfast",
         "a family of four at the breakfast table, everybody busy with a gadget: a girl with a tablet, "
         "mum looking at her phone, a teenage boy with headphones and a phone, dad typing on a laptop"),
    ], None),

    # ---------------- UNIT 4 ----------------
    ("u4", 2, 3, "scene", "Природа 1",
     "Словарь Homework 1, тест.", [
        ("u4_beach", "a sandy beach with the sea"),
        ("u4_desert", "a desert with sand dunes"),
        ("u4_forest", "a green forest"),
        ("u4_island", "a small green island in the sea"),
        ("u4_lake", "a calm lake among hills"),
        ("u4_mountain", "a tall mountain with a snowy top"),
    ], None),
    ("u4", 2, 3, "scene", "Природа 2",
     "Словарь Homework 1, тест.", [
        ("u4_river", "a river flowing through a valley"),
        ("u4_sea", "the open sea with waves"),
        ("u4_volcano", "a volcano with smoke coming out"),
        ("u4_waterfall", "a waterfall"),
        ("u4_city", "a big city with tall buildings"),
        ("u4_town", "a small town with houses and a church"),
    ], None),
    ("u4", 2, 3, "object", "Какое? Цена, риск, высота",
     "Словарь Homework 2.", [
        ("u4_cheap", "a single small coin next to a simple paper price tag"),
        ("u4_expensive", "a sparkling diamond ring next to a gold price tag"),
        ("u4_dangerous", "a shark fin in the water next to a red warning triangle"),
        ("u4_safe", "a bicycle helmet, knee pads and elbow pads"),
        ("u4_high", "a very tall thin tower"),
        ("u4_low", "a very low little garden fence"),
    ], None),
    ("u4", 2, 2, "object", "Какое? Трудность, интерес",
     "Словарь Homework 2.", [
        ("u4_easy", "a puzzle of just two big pieces"),
        ("u4_difficult", "a huge complicated puzzle with hundreds of tiny pieces"),
        ("u4_exciting", "a roller coaster with a big loop"),
        ("u4_boring", "a grey rainy window with a ticking clock and a pile of grey papers on the sill"),
    ], None),
    ("u4", 3, 3, "cartoon", "Какой? Животные",
     "Словарь Homework 3; тигр — Homework 3, задание 8.", [
        ("u4_beautiful", "a beautiful butterfly on a flower"),
        ("u4_fast", "a cheetah running fast"),
        ("u4_friendly", "a friendly puppy wagging its tail"),
        ("u4_funny", "a funny monkey pulling a face"),
        ("u4_intelligent", "an owl in glasses reading a book"),
        ("u4_strong", "an ant carrying a huge crumb"),
        ("u4_kind", "a bear sharing a pot of honey with a little rabbit"),
        ("u4_tiger", "a tiger looking back over its shoulder"),
        ("u4_slow", "a slow tortoise"),
    ], None),
    ("u4", 2, 3, "object", "Спорт на природе",
     "Homework 7 (1), задание 23.", [
        ("u4_kayaking", "a kayak and a paddle"),
        ("u4_climbing", "a climbing rope, carabiners and a helmet next to a rock"),
        ("u4_parachute", "an open parachute in the sky"),
        ("u4_sailing", "a sailing boat"),
        ("u4_fishing", "a fishing rod with a float"),
        ("u4_cycling", "a mountain bike"),
    ], None),
    ("u4", 3, 3, "people_scene", "Герои Unit 4",
     "Вместо фото: Платон (Homework 1), Джейк и Майкл (Homework 2), Зак и Ленни (Homework 6), "
     "Дэн (Homework 7), сцены отдыха (Homework 7 (1), задания 19–21), кино (Homework 4).", [
        ("u4_plato", "Plato, a Greek boy of twelve, standing on a hill above a white island town by the blue sea"),
        ("u4_jake_michael", "two teenage boys, Jake and Michael, in a kayak for two on a lake near a wooden jetty"),
        ("u4_zak_lenny", "two boys at a fast-food table: one eating a hamburger, the other eating pizza"),
        ("u4_dan_laptop", "a boy reading on a laptop at his desk, wearing headphones"),
        ("u4_kayak_river", "two teenagers kayaking on a river"),
        ("u4_bike_forest", "a girl cycling on a forest path"),
        ("u4_boat_lake", "a family in a rowing boat on a lake"),
        ("u4_cinema", "a group of friends watching a film at the cinema with popcorn"),
        ("u4_hiking_family", "a family walking in the mountains with backpacks"),
    ], None),
    ("u4", 1, 1, "scene", "Три картины",
     "Homework 3, задания 7, 10, 11: картины Рокко, Большого Эла и Карлы.", [
        ("u4_three_paintings",
         "three framed paintings hanging side by side on a gallery wall, clearly different in size: on the "
         "left a medium painting of messy childish scribbles, in the middle a small painting of a funny cat, "
         "on the right the biggest painting of a neat landscape with mountains and a lake"),
    ], None),

    # ---------------- UNIT 5 ----------------
    ("u5", 3, 3, "scene", "Город 1",
     "Словарь Homework 1, тест. Узнаваемо без вывесок.", [
        ("u5_bank", "a bank building with columns and a cash machine"),
        ("u5_cafe", "a small café with tables and umbrellas outside"),
        ("u5_cinema", "a cinema building with a big poster frame and film reels decoration"),
        ("u5_hotel", "a tall hotel with a revolving door and a luggage trolley outside"),
        ("u5_hospital", "a hospital with an ambulance in front and a red cross on the wall"),
        ("u5_library", "a library building with stone steps and big windows showing bookshelves"),
        ("u5_museum", "a museum with columns and a big dinosaur skeleton visible through the glass"),
        ("u5_park", "a city park with trees, a pond and benches"),
        ("u5_restaurant", "a restaurant with tables laid with white tablecloths behind big windows"),
    ], None),
    ("u5", 3, 3, "scene", "Город 2",
     "Словарь Homework 1, тест.", [
        ("u5_supermarket", "a supermarket with shopping trolleys outside"),
        ("u5_clothes_shop", "a clothes shop with clothes on hangers in the window"),
        ("u5_stadium", "a football stadium"),
        ("u5_theatre", "a theatre with a red curtain visible through the open doors"),
        ("u5_sports_centre", "a sports centre with a running track"),
        ("u5_swimming_pool", "an indoor swimming pool"),
        ("u5_post_office", "a post office with a red post box in front"),
        ("u5_police_station", "a police station with a police car in front and a blue lamp above the door"),
        ("u5_train_station", "a train station with a train at the platform"),
    ], None),
    ("u5", 2, 3, "scene", "Город 3, дома и музей",
     "Homework 5, 6.", [
        ("u5_shopping_centre", "a big modern shopping centre"),
        ("u5_film_studio", "a film studio with a big camera, lights and a set"),
        ("u5_theme_park", "a theme park with a big wheel and a roller coaster"),
        ("u5_small_house", "a small house"),
        ("u5_big_house", "a big house"),
        ("u5_interesting_museum", "a museum hall with a huge dinosaur skeleton"),
    ], None),
    ("u5", 2, 3, "scene", "Какой город",
     "Homework 6, задание 4: пары прилагательных.", [
        ("u5_busy_street", "a busy street full of cars and buses"),
        ("u5_quiet_street", "a quiet empty street with trees"),
        ("u5_clean_cinema", "a clean cinema hall with neat rows of red seats"),
        ("u5_dirty_cinema", "a dirty cinema hall with popcorn and cups on the floor"),
        ("u5_old_stadium", "an old stadium with broken seats"),
        ("u5_new_stadium", "a shiny new stadium"),
    ], None),
    ("u5", 1, 2, "scene", "Город раньше и сейчас",
     "Homework 6, задание 5: кадр учебника в выгрузке обрезан — вместо него. Один и тот же город.", [
        ("u5_town_past", "a small town street a hundred years ago: old shops, horse carts and gas lamps"),
        ("u5_town_now", "the same town street today: modern shops, cars, a bus stop and a café"),
    ], "Both pictures show the same street from the same viewpoint."),
    ("u5", 1, 1, "people_scene", "Улица с кафе",
     "Тест Unit 5, SPEAKING I (вместо фото улицы с людьми).", [
        ("u5_scene_street",
         "an old European street on a sunny day: a café with tables outside where people are drinking "
         "coffee, a bakery, a small bookshop, a bicycle by a lamp post and flower boxes on the windows"),
    ], None),
    ("u5", 1, 3, "scene", "Где ты был",
     "По желанию: Homework 3, задание 4.", [
        ("u5_garden", "a garden with flower beds"),
        ("u5_park_small", "a small park with a bench"),
        ("u5_kitchen", "a kitchen"),
    ], None),

    # ---------------- UNIT 6 ----------------
    ("u6", 3, 3, "people", "Профессии 1",
     "Словарь Homework 1, тест.", [
        ("u6_artist", "an artist painting at an easel"),
        ("u6_builder", "a builder in a hard hat laying bricks"),
        ("u6_bus_driver", "a bus driver at the wheel of a bus"),
        ("u6_chef", "a chef in a white hat stirring a pot"),
        ("u6_doctor", "a doctor with a stethoscope"),
        ("u6_farmer", "a farmer with a basket of eggs next to a tractor"),
        ("u6_footballer", "a footballer kicking a ball"),
        ("u6_nurse", "a nurse holding a thermometer and a bandage"),
        ("u6_office_worker", "an office worker at a desk with a computer"),
    ], None),
    ("u6", 2, 3, "people", "Профессии 2",
     "Словарь Homework 1, тест.", [
        ("u6_pilot", "a pilot in uniform in front of a plane"),
        ("u6_police_officer", "a police officer with a radio"),
        ("u6_shop_assistant", "a shop assistant at a till"),
        ("u6_singer", "a singer with a microphone"),
        ("u6_teacher", "a teacher at a board with a globe on the desk"),
        ("u6_vet", "a vet examining a cat on a table"),
    ], None),
    ("u6", 1, 1, "people_scene", "Семья убирает дом",
     "Тест Unit 6, SPEAKING I. Вопросы остаются: How many people? What is each person doing?", [
        ("u6_scene_cleaning",
         "a family cleaning their living room together: mum ironing, dad washing the window, a girl "
         "carrying a basket of washing, a boy picking up toys, and a cat watching from the sofa"),
    ], None),

    # ---------------- UNIT 7 ----------------
    ("u7", 2, 3, "object", "Транспорт 1",
     "Словарь Homework 1.", [
        ("u7_car", "a car"),
        ("u7_boat", "a rowing boat with oars"),
        ("u7_bike", "a bicycle"),
        ("u7_bus", "a city bus"),
        ("u7_motorbike", "a motorbike"),
        ("u7_plane", "a passenger plane"),
    ], None),
    ("u7", 2, 3, "object", "Транспорт 2",
     "Словарь Homework 1.", [
        ("u7_taxi", "a yellow taxi"),
        ("u7_train", "a passenger train"),
        ("u7_tram", "a tram"),
        ("u7_underground", "an underground train in a tunnel"),
        ("u7_lorry", "a lorry"),
        ("u7_school_bus", "a yellow school bus at a bus stop with its door open"),
    ], None),
    ("u7", 2, 3, "people_scene", "Как едем",
     "Словарь Homework 1 (2).", [
        ("u7_arrive", "a train arriving at a station platform, people waiting"),
        ("u7_get_on", "people getting on a bus through its open doors"),
        ("u7_get_off", "people getting off a train onto the platform"),
        ("u7_leave", "a train leaving the station, a woman waving goodbye"),
        ("u7_take_bus", "a boy taking a bus at a bus stop"),
        ("u7_on_foot", "a girl walking to school on foot"),
    ], None),
    ("u7", 2, 3, "people_scene", "На каникулах",
     "Homework 3, 6.", [
        ("u7_restaurant", "a family eating pizza at a restaurant"),
        ("u7_take_photos", "a girl taking photos with a camera"),
        ("u7_museum", "children visiting a museum with a statue and paintings"),
        ("u7_hotel", "a family with suitcases arriving at a hotel reception"),
        ("u7_souvenir", "a boy buying a souvenir at a stall with magnets and small towers"),
        ("u7_sightseeing", "tourists with a map going sightseeing in front of an old tower"),
    ], None),
    ("u7", 2, 3, "object", "Вещи в поездку",
     "Homework 2, 6. Телефон, планшет и фотоаппарат — с листов Unit 3.", [
        ("u7_guidebook", "a guidebook"),
        ("u7_sun_hat", "a sun hat with flowers"),
        ("u7_suitcase", "a suitcase"),
        ("u7_socks", "a pair of socks"),
        ("u7_passport", "a passport"),
        ("u7_sunglasses", "a pair of sunglasses"),
    ], None),
    ("u7", 1, 1, "scene", "Открытый чемодан",
     "Homework 2, задание 17: что положили в чемодан.", [
        ("u7_scene_suitcase",
         "an open suitcase on a bedroom floor with things scattered around it, every item clearly separate: "
         "a guidebook, a sun hat, a pair of socks, a camera, a passport, sunglasses, a toothbrush, a towel "
         "and a tube of sun cream"),
    ], None),
    ("u7", 3, 3, "people_scene", "Герои Unit 7",
     "Вместо фото и обрезанных картинок: Homework 1 (Энзо), 2 (составь предложение), 6 (Пенни, фото на память, автобус).", [
        ("u7_tim_pizza", "a boy, Tim, eating pizza at a pizzeria"),
        ("u7_dad_coffee", "a dad drinking coffee in the kitchen"),
        ("u7_tina_hat", "a girl, Tina, wearing a sun hat with flowers"),
        ("u7_mum_stan_shop", "a mum and her son Stan in a supermarket"),
        ("u7_enzo", "Enzo, a fourteen-year-old boy, travelling on the underground in New York with his school bag"),
        ("u7_penny_skateboard", "Penny, a girl of twelve, on a skateboard"),
        ("u7_dad_photos", "a dad taking pictures of his two children on holiday by the sea"),
        ("u7_kids_off_bus", "children getting off a school bus"),
        ("u7_everest", "mountain climbers with tents near a snowy mountain top"),
    ], None),
    ("u7", 1, 1, "people_scene", "В аэропорту",
     "Тест Unit 7, SPEAKING I. Вопросы остаются: Where are the people? What are they wearing? Plane or train?", [
        ("u7_scene_airport",
         "a family of three - a dad, a mum and a child - standing at the big window of an airport with "
         "a suitcase, planes on the airfield outside"),
    ], None),

    # ---------------- UNIT 8 ----------------
    ("u8", 3, 3, "scene", "Мероприятия",
     "Словарь Homework 1.", [
        ("u8_barbecue", "a barbecue grill with sausages and smoke in a garden"),
        ("u8_birthday_party", "a birthday table with a cake with candles, balloons and presents"),
        ("u8_concert", "a concert stage with a microphone, lights and speakers"),
        ("u8_dance_show", "a dance show stage with a curtain and spotlights"),
        ("u8_football_match", "a football stadium with a ball on the pitch"),
        ("u8_fancy_dress", "a rail of fancy dress costumes: a cape, a wizard hat, a mask and a crown"),
        ("u8_picnic", "a picnic blanket on the grass with a basket and sandwiches"),
        ("u8_play", "a theatre stage with a red curtain and a castle set"),
        ("u8_sleepover", "sleeping bags and pillows on a bedroom floor with a torch and fairy lights"),
    ], None),
    ("u8", 3, 3, "people_scene", "Что делают на празднике",
     "Словарь Homework 1 (2); последние две — Homework 1 (3).", [
        ("u8_talent_competition", "a girl singing in a talent competition on a stage, judges holding up score cards"),
        ("u8_cook_food", "a boy cooking food in the kitchen"),
        ("u8_get_presents", "a girl getting presents at her birthday party"),
        ("u8_sing_birthday", "children singing Happy Birthday around a cake with candles"),
        ("u8_sleep_floor", "two children sleeping in sleeping bags on the floor"),
        ("u8_competition", "children taking part in a running competition"),
        ("u8_wear_costume", "a boy wearing a superhero costume"),
        ("u8_sleepover_girls", "three girls having a sleepover with pillows and popcorn"),
        ("u8_anna", "Anna, a smiling girl of twelve with long dark hair"),
    ], None),
    ("u8", 3, 3, "people_scene", "Планы: be going to",
     "Homework 2 (1), задания 5–13; Homework 3, задания 6 и 10.", [
        ("u8_grandma_cottage", "a grandmother's cottage with a garden and a bench"),
        ("u8_sakura", "blossoming cherry trees with Mount Fuji in the distance"),
        ("u8_homework_girl", "a girl doing her homework at a desk in the evening"),
        ("u8_paint_bedroom", "a half-painted pink bedroom wall with a paint roller and a bucket"),
        ("u8_beach_holiday", "a beach with a palm tree and a sun lounger"),
        ("u8_cinema_tonight", "a cinema hall with red seats and popcorn"),
        ("u8_boy_reading", "a boy reading a book on his bed"),
        ("u8_armful_clothes", "a girl carrying a big armful of clothes"),
        ("u8_shop_window", "a clothes shop window with dresses and jackets on hangers"),
    ], None),
    ("u8", 2, 3, "object", "Музыка",
     "Homework 3: вместо игры Wordwall «types of music» (состав мой).", [
        ("u8_rock", "an electric guitar and an amplifier"),
        ("u8_pop", "a sparkly microphone with little stars"),
        ("u8_classical", "a violin with sheet music"),
        ("u8_rap", "one boombox with a baseball cap lying on top of it, both together as one single object"),
        ("u8_jazz", "a shiny golden saxophone"),
        ("u8_country", "a banjo and a cowboy hat"),
    ], None),
    ("u8", 2, 3, "object", "Билеты и подарки",
     "Homework 3, 6.", [
        ("u8_concert_tickets", "two concert tickets with a star picture"),
        ("u8_flowers", "a bouquet of flowers with a heart-shaped card"),
        ("u8_bowling", "bowling pins and a bowling ball"),
        ("u8_restaurant_table", "a restaurant table with plates, cutlery and a candle"),
        ("u8_cinema_tickets", "two cinema tickets with a box of popcorn"),
        ("u8_invitation", "a party invitation card decorated with balloons"),
    ], None),
    ("u8", 1, 3, "people_scene", "Забеги",
     "Homework 5, задание 4: соедини картинки с забегами из постера «Running for fun!».", [
        ("u8_winter_run", "Winter Run: children running on a snowy forest path, a pot of hot soup at the finish"),
        ("u8_fun_races", "Fun Races: children in an egg-and-spoon race and a sack race at a school sports field, a basketball hoop behind"),
        ("u8_costume_run", "Costume Run: children in capes and masks running along a park path"),
    ], None),
    ("u8", 1, 1, "people_scene", "День рождения",
     "Тест Unit 8, SPEAKING I. Вопросы остаются: What event is this? How many people? What are they wearing?", [
        ("u8_scene_birthday",
         "a birthday party at home: a girl blowing out the candles on a cake, four friends in party hats "
         "around the table, presents, balloons, sandwiches, cups of juice"),
    ], None),
]

UNIT_TITLES = {"u0": "Unit 0", "u1": "Unit 1", "u2": "Unit 2", "u3": "Unit 3", "u4": "Unit 4",
               "u5": "Unit 5", "u6": "Unit 6", "u7": "Unit 7", "u8": "Unit 8", "final": "Final Test"}


def prompt(sheet):
    unit, rows, cols, reg, title, note, cells, extra = sheet
    if rows == cols == 1:
        body = [f"One single picture filling the frame: {cells[0][1]}."]
    else:
        what = "illustrations" if reg in SCENES else "picture cards"
        item = "picture" if reg in SCENES else "item"
        words = {1: "one", 2: "two", 3: "three"}
        cols_w = f"{words[cols]} column" + ("s" if cols > 1 else "")
        rows_w = f"{words[rows]} row" + ("s" if rows > 1 else "")
        body = [GRID.format(n=len(cells), what=what, cols_w=cols_w, rows_w=rows_w, item=item)]
        for r in range(rows):
            row = cells[r * cols:(r + 1) * cols]
            body.append(f"{ROW_NAMES[r]}, left to right: " + "; ".join(d for _, d in row) + ".")
    if extra:
        body.append(extra)
    if reg not in PEOPLE:
        body.append(NO_PEOPLE)
    return "\n".join(body + [STYLE[reg] + " " + NO_TEXT, size_line(rows, cols)])


def check(sheets):
    errors, seen = [], {}
    for n, (unit, rows, cols, reg, title, note, cells, extra) in enumerate(sheets, 1):
        if rows * cols != len(cells):
            errors.append(f"лист {n}: сетка {cols}×{rows}, а ячеек {len(cells)}")
        if cols > 3 or rows > 3:
            errors.append(f"лист {n}: больше трёх колонок/рядов")
        for key, _ in cells:
            if key in seen:
                errors.append(f"лист {n}: ключ {key} уже есть в листе {seen[key]}")
            seen[key] = n
    return errors


def render(sheets, head, start=1):
    out, cur, total = [head], None, 0
    for n, sheet in enumerate(sheets, start):
        unit, rows, cols, reg, title, note, cells, extra = sheet
        if unit != cur:
            k = sum(1 for s in sheets if s[0] == unit)
            out.append(f"\n---\n\n# {UNIT_TITLES[unit].upper()} — листов: {k}\n")
            cur = unit
        kind = "одна картинка" if rows == cols == 1 else f"{len(cells)} карт., сетка {cols}×{rows}"
        out.append(f"### Лист {n} · {title} — {kind}, {REGISTER_RU[reg]}")
        if note:
            out.append(note)
        out.append("```\n" + prompt(sheet) + "\n```\n")
        total += len(cells)
    out.insert(1, f"\n**Листы {start}–{start + len(sheets) - 1}: всего {len(sheets)}, картинок {total}.**\n")
    return "\n".join(out)


HEAD = """# Go Getter 2 — ЛИСТЫ ПРОМПТОВ НА КАРТИНКИ

Собирается из `tools/gg2_sheets.py` — **правится там**, не здесь.

Один промпт = один лист. Генерирует Анна, присылает в чат с подписью номера
листа («Лист 7»). Номера сквозные на GG2 и GG3: у GG2 листы 1–{last}, у GG3
дальше (`docs/GG3_листы_промптов.md`). Номер не переиспользуется.

Каждый промпт самодостаточный: сетка, порядок ячеек по рядам, стиль, запрет
текста и размер уже внутри — копируется целиком.

Стиль тот же, что у GG1: предметы — реалистичный 3D, животные — мультяшный
глянец, места и люди — 3D-мультяшные (Pixar-like), люди стилизованные, не фото.
Людей рисуем (решение Анны 05.10.2026); на листах без людей это прописано в
промпте.

## Чего не генерируем

| Что | Откуда |
|---|---|
| Кадры учебника: Anna, Max, Hammy, Carla, Rocco, Big Al, Mrs Dee, Billy и Patti, карты, билеты, постеры, таблицы | вырезаются из PDF выгрузки — по ним сверяются ответы |
| Карточки методиста с текстом (правила, тексты для чтения) | переносим текстом |
| Приветствия, похвалы, прощания | `media/shared/` |
| Фото реальных людей, Микки Маус, Гарфилд, Angry Birds, Стич | не берём — вместо них листы «Герои» |
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    errors = check(SHEETS)
    if errors:
        for e in errors:
            print("·", e, file=sys.stderr)
        sys.exit(1)
    if args.check:
        print(f"листов {len(SHEETS)}, картинок {sum(len(s[6]) for s in SHEETS)}, всё сходится")
        return
    doc = os.path.join(ROOT, "docs", "GG2_листы_промптов.md")
    with open(doc, "w", encoding="utf-8") as f:
        f.write(render(SHEETS, HEAD.replace("{last}", str(len(SHEETS)))))
    print("записан", os.path.relpath(doc, ROOT))


if __name__ == "__main__":
    main()
