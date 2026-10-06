#!/usr/bin/env python3
"""Go Getter 1 · Unit 3 · My home — уроки (разбор: docs/GG1_разбор/u3.md).

Комнаты и части дома, мебель, there is / there are, there isn't / aren't и
вопросы, предлоги места, фразы гостя, апострофы. Картинки слов — листы
Л3.1–Л3.5 (tools/gg1_sheets.py), стул и стол — из Unit 0. Карточки методиста,
сцены учебника и фото без людей — кадры из выгрузки (tools/gg1_pdf_frames.py),
доработка части кадров — tools/gg1_u3_frames.py.
"""
from gg1_lib import *  # noqa: F401,F403

U = "u3"
U3 = {"unit": U, "unit_title": "Unit 3 · My home", "unit_sort": 3}


def u(name):
    return img(U, name)


def alts(*answers):
    """Варианты ответа для пропуска: с прямым и с типографским апострофом."""
    out = []
    for a in answers:
        out += [a, a.replace("'", "’")]
    return "|".join(dict.fromkeys(out))


U3_ROOMS = vocab([
    ("bathroom", "ванная комната", u("room_bathroom")),
    ("bedroom", "спальня", u("room_bedroom")),
    ("kitchen", "кухня", u("room_kitchen")),
    ("garage", "гараж", u("room_garage")),
    ("garden", "сад", u("room_garden")),
    ("living room", "гостиная", u("room_living_room")),
    ("floor", "пол", u("part_floor")),
    ("door", "дверь", u("part_door")),
    ("wall", "стена", u("part_wall")),
    ("window", "окно", u("part_window")),
])

# стул и письменный стол — те же картинки, что в Unit 0 (листов на них в Unit 3 нет)
U3_FURN = vocab([
    ("armchair", "кресло", u("furn_armchair")),
    ("bath", "ванна", u("furn_bath")),
    ("bed", "кровать", u("furn_bed")),
    ("chair", "стул", img("u0", "obj_chair")),
    ("desk", "письменный стол", img("u0", "obj_desk")),
    ("table", "стол", u("furn_table")),
    ("fridge", "холодильник", u("furn_fridge")),
    ("sofa", "диван", u("furn_sofa")),
    ("wardrobe", "шкаф", u("furn_wardrobe")),
])

U3_THINGS = vocab([
    ("carpet", "ковёр", u("furn_carpet")),
    ("cushion", "декоративная подушка", u("furn_cushion")),
    ("lamp", "лампа", u("furn_lamp")),
    ("plant", "растение", u("furn_plant")),
    ("poster", "плакат", u("furn_poster")),
    ("TV", "телевизор", u("furn_tv")),
])

PREPS = [("on", "prep_on"), ("under", "prep_under"), ("in", "prep_in"),
         ("behind", "prep_behind"), ("next to", "prep_next_to"),
         ("in front of", "prep_in_front_of")]

CHAMPION = ("Ты выполнил все задания из основной части! А это дополнительное задание — "
            "для настоящих чемпионов! ")
REVIEW = "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"


def word_pic(en):
    return next(p for e, r, p in U3_ROOMS + U3_FURN + U3_THINGS if e == en)


def cards(words):
    return ("flashcards", {"cards": [
        {"text": en, "translation": ru, "audio_tts": en, "image": p} for en, ru, p in words]})


def pic_match(title, words):
    return ("match", {"title": title, "pairs": [
        {"left_image": p, "right": en, "right_audio_tts": en} for en, ru, p in words]})


def spell(title, words, how):
    """Впиши слово по картинке: подсказка — анаграмма или слово с пропусками."""
    return ("exact_input", {"title": title, "items": [
        {"prompt": how(en), "accept": list(dict.fromkeys([en, en.capitalize() if en.islower() else en])),
         "image": p, "audio_tts": en} for en, ru, p in words]})


LESSONS = {
    # Homework 1: (1) тренажёр «части дома», (2) тренажёр «предметы в доме»,
    # (3) задания. Один урок.
    "u3_hw1": {
        **U3,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня мы учим слова про дом: комнаты, части дома и "
                  "мебель. Выполни все задания, чтобы выучить их на все 100!</p>"),

            cards(U3_ROOMS),
            pic_match("Соедини картинку и слово", U3_ROOMS),
            ("quiz", quiz_ru_to_en(U3_ROOMS)),
            spell("Расшифруй слово и впиши его",
                  [w for w in U3_ROOMS if w[0] in ("bathroom", "bedroom", "kitchen", "garage",
                                                   "garden", "window")], anagram),

            cards(U3_FURN),
            pic_match("Соедини картинку и слово", U3_FURN),
            ("quiz", quiz_ru_to_en(U3_FURN)),
            spell("Вставь пропущенные буквы и впиши слово целиком", U3_FURN, gapped),

            ("text", {"html": "<h3>Привет! Как поживаешь? (How are you doing?)</h3>"
                              "<p>Сегодня мы с тобой закрепим то, что изучали на уроке!</p>"
                              + pic(u("card_parts_of_house"), "Parts of the house")
                              + pic(u("card_inside_house"), "Inside the house")}),

            # утверждения общие, картинка — дом в разрезе
            true_false("Посмотри на картинку и для каждого утверждения выбери: верно или неверно. "
                       "Удачи! У тебя всё получится!", [
                ("We usually have dinner in the bathroom.", False, u("house_cutaway_family")),
                ("I do my homework in the kitchen.", False),
                ("Sam and Mark play computer games in the garage.", False),
                ("I brush my teeth in the bathroom.", True),
                ("I go to bed in my bedroom.", True),
            ]),

            # в выгрузке «dinning room» — исправлено
            ("match", {"title": "Соедини предметы интерьера с комнатами, где они обычно находятся",
                       "pairs": [
                           {"left": "armchair", "right": "living room"},
                           {"left": "table", "right": "dining room"},
                           {"left": "fridge", "right": "kitchen"},
                           {"left": "bath", "right": "bathroom"},
                           {"left": "bed", "right": "bedroom"},
                           {"left": "car", "right": "garage"},
                       ]}),

            ("gaps", {
                "title": "Здесь нас ждёт небольшой рассказ, в котором кто-то украл слова. "
                         "Поможешь вставить пропущенные слова?",
                "mode": "drag",
                "image": u("photo_house"),
                "text": "I live with my parents in a big __house__. The room I like most of all is "
                        "our __living room__. There are so many things to do in this room. There is "
                        "a big __bookcase__ and I can take any book I like from it. We often spend "
                        "time watching films on __TV__. We sit on the comfortable __sofa__ which is "
                        "opposite the TV. My dad keeps his car in the __garage__ and I like to help "
                        "him with our __garden__ at the weekend.",
                "gaps_expected": 7,
            }),

            ("video", {"title": "Посмотри видео и попробуй догадаться, о каких комнатах "
                                "рассказывается. Повторяй слова за рассказчиком!",
                       "url": "", "provider": "youtube"}),

            ("text", {"html": pic(shared("well_done_jump"), height=180)
                      + "<h3>Ты уже так много сделал сегодня! Большой отличник!</h3>"
                        "<p>Попробуем выполнить кое-что ещё?</p>"}),

            ("speaking", {
                "title": "Давай проверим наши силы? 🎤",
                "html": "<p>Расскажи, в каком доме ты хотел бы жить. Что бы ты поставил или "
                        "купил в каждую комнату?</p>"
                        "<p><i>Пример: I want a big house with a garden. In my bedroom there is a "
                        "big bed and a wardrobe. In the living room there is a sofa and a TV.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «gg1-31» (обложка пустая, тип не виден) — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини слова с картинкой ⭐", "pairs": [
                {"left_image": word_pic(en), "right": en, "right_audio_tts": en}
                for en in ["door", "window", "sofa", "wardrobe", "garden", "fridge", "garage",
                           "armchair"]
            ]}),

            # Wordwall «gg1-31» (обложка пустая, тип не виден) — СОСТАВ МОЙ
            spell("Впиши слова ⭐", [w for w in U3_ROOMS + U3_FURN
                                    if w[0] in ("wall", "floor", "door", "bed", "chair",
                                                "table", "bath", "sofa")], anagram),

            bye("<h3>Молодец! До скорых встреч! 🎉</h3><p>Увидимся на занятии!</p>",
                "well_done_trophy"),
        ],
    },

    # Homework 2: (1) there is / there are, (2) предлоги места. Один урок.
    "u3_hw2": {
        **U3,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        "blocks": [
            hello("<h2>Привет, герой! 👋</h2><p>Сегодня мы с тобой повторяем материал нашего "
                  "урока! Проверяем наши знания! Удачи!</p>", "hello_highfive"),

            ("text", {"html": REVIEW + pic(u("card_there_is_are"), "There is / There are")}),

            ("video", {"title": "Посмотри видео, вспомни правила", "url": "",
                       "provider": "youtube"}),

            ("sort", {"title": "Распредели слова между двумя колонками: что идёт с there is, "
                               "а что — с there are?", "groups": [
                {"name": "There is", "items": [{"text": t} for t in
                                               ["a book", "an armchair", "a carpet", "a curtain"]]},
                {"name": "There are", "items": [{"text": t} for t in
                                                ["desks", "chairs", "lamps", "cushions"]]},
            ]}),

            mcq("А теперь давай потренируемся! Выбери правильный ответ", [
                ("There ___ a fridge in the kitchen.", ["is", "are"], "is"),
                ("There ___ many toys in the toy box.", ["is", "are"], "are"),
                ("There ___ five apples on the table.", ["is", "are"], "are"),
                ("There ___ a big dog in the garden.", ["is", "are"], "is"),
                ("There ___ three birds in the tree.", ["is", "are"], "are"),
                ("There ___ tasty cookies in the oven.", ["is", "are"], "are"),
                ("There ___ six chairs in the classroom.", ["is", "are"], "are"),
            ]),

            ("task", {
                "title": "Комнаты в моём доме ✍",
                "needs_review": True,
                "html": "<p>А какие комнаты есть в твоём доме? Напиши, используя there is / "
                        "there are.</p><p><i>Пример: There are 3 bedrooms. There is 1 kitchen.</i></p>",
            }),

            ("text", {"html": "<h3>Добро пожаловать во вторую часть домашнего задания! 👋</h3>"
                              "<p>Давай повторим предлоги места:</p>"
                              + pic(u("card_prepositions"), "Prepositions of place")}),

            # логотип на экране телевизора закрашен (tools/gg1_u3_frames.py)
            mcq("Посмотри на картинку и выбери правильный ответ", [
                ("There is a cat ___ the sofa.", ["on", "under"], "on", u("prepositions_living_room")),
                ("There are two dogs ___ the table.", ["under", "behind"], "under",
                 u("prepositions_living_room")),
                ("There is a toy plane ___ the box.", ["in", "in front of"], "in",
                 u("prepositions_living_room")),
                ("There is a picture ___ the wall.", ["on", "under"], "on",
                 u("prepositions_living_room")),
                ("There is a guitar ___ the plant.", ["next to", "in"], "next to",
                 u("prepositions_living_room")),
                ("There is a backpack ___ the TV.", ["in front of", "between"], "in front of",
                 u("prepositions_living_room")),
                ("There is a window ___ the sofa.", ["behind", "next to"], "behind",
                 u("prepositions_living_room")),
            ]),

            ("task", {
                "title": "Опиши картинку ✍",
                "needs_review": True,
                "image": u("kids_bedroom"),
                "html": "<p>Опиши картинку. Используй There is / There are и предлоги места.</p>"
                        "<p><i>Пример: There is a skateboard under the bed.</i></p>",
            }),

            ("task", {
                "title": "Задание со звёздочкой ⭐",
                "needs_review": True,
                "image": u("photo_bedroom"),
                "html": "<p>Для тех, кто хочет знать больше! Расскажи нам о своей комнате.</p>"
                        "<p><b>Tell me about your bedroom:</b></p>"
                        "<p><i>Пример: There is a bed …</i></p>",
            }),

            # Wordwall «Match up · GG1 U 3.2 prepositions» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини слова с картинкой ⭐", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en} for en, p in PREPS]}),

            # Wordwall «Quiz · GG1 3.2.» — СОСТАВ МОЙ
            mcq("Выбери правильный вариант ⭐", [
                (f"The ball is ___ the box.", [e for e, _ in PREPS], en, u(p))
                for en, p in [PREPS[3], PREPS[0], PREPS[5], PREPS[2], PREPS[4], PREPS[1]]
            ]),

            bye("<h3>На сегодня твоё путешествие в страну ДЗ подошло к концу! 🎉</h3>"
                "<p>Ты отлично со всем справился! До скорых встреч!</p>", "well_done_clap"),
        ],
    },

    # Homework 3: (1) there isn't / aren't, вопросы; (2) порядок слов, Итан, спальня.
    "u3_hw3": {
        **U3,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        "blocks": [
            hello("<h2>Привет-привет! 👋</h2><p>Наше путешествие по стране ДЗ продолжается! "
                  "Давай начнём нашу домашнюю работу!</p>", "hello_book"),

            ("text", {"html": REVIEW + pic(u("card_there_isnt_questions"),
                                           "There isn't / There aren't / Questions")}),

            ("video", {"title": "Посмотри видео и вспомни, о чём мы с тобой узнали на уроке!",
                       "url": "", "provider": "youtube"}),

            # в выгрузке «five desks» — на картинке два круглых стола, исправлено
            mcq("Посмотри на картинку с урока в стране ДЗ и выбери правильные ответы", [
                ("___ seven students in the classroom.", ["There are", "There is"], "There are",
                 u("classroom_scene")),
                ("___ a teacher in the classroom.", ["There is", "There are"], "There is",
                 u("classroom_scene")),
                ("___ a board in the classroom.", ["There is", "There are"], "There is",
                 u("classroom_scene")),
                ("___ two tables in the classroom.", ["There are", "There is"], "There are",
                 u("classroom_scene")),
            ]),

            # в выгрузке — пропуски с перетаскиванием и лишними словами; у нас вопрос
            # на каждое предложение из тех же четырёх слов
            mcq("Посмотри на картинку и выбери: are, is, aren't или isn't", [
                (q, ["are", "is", "aren't", "isn't"], ok, u("kids_room_two_beds"))
                for q, ok in [
                    ("There ___ 2 bikes in the picture.", "aren't"),
                    ("There ___ four pencils in the picture.", "are"),
                    ("There ___ three cushions on the bed.", "aren't"),
                    ("There ___ a teddy bear.", "is"),
                    ("There ___ a dog under the table.", "isn't"),
                    ("There ___ a rabbit on the bed.", "isn't"),
                    ("There ___ two computers on the desk.", "aren't"),
                    ("There ___ three posters on the wall.", "are"),
                    ("There ___ four books on the shelf.", "are"),
                    ("There ___ two presents on the bed.", "aren't"),
                ]
            ]),

            ("task", {
                "title": "Задание для самых-самых ⭐",
                "needs_review": True,
                "image": u("two_living_rooms"),
                "html": "<p>Посмотри на картинку, задай вопросы и напиши ответы (5–6 предложений).</p>"
                        "<p><i>Пример: Is there a dog in picture 2? — No, there isn't.</i></p>",
            }),

            # Wordwall «Complete the sentence · GG1 unit 3.3 there isn't/there aren't» — СОСТАВ МОЙ
            ("gaps", {
                "title": CHAMPION + "Вставь isn't или aren't ⭐",
                "mode": "drag",
                "text": "1. There __isn't__ a dog in my bedroom.\n"
                        "2. There __aren't__ any plants in the kitchen.\n"
                        "3. There __isn't__ a TV in the bathroom.\n"
                        "4. There __aren't__ any chairs in the garden.\n"
                        "5. There __isn't__ a car in the garage.\n"
                        "6. There __aren't__ any books on the desk.",
                "gaps_expected": 6,
            }),

            # Wordwall «Unjumble · gg1 3.3 photocopiable ex 2» — СОСТАВ МОЙ
            order("Is there a sofa in the living room?", title="Расставь слова в правильном порядке ⭐"),
            order("There aren't any posters on the wall.",
                  title="Расставь слова в правильном порядке ⭐"),
            order("Are there any chairs in the kitchen?",
                  title="Расставь слова в правильном порядке ⭐"),

            # вторая часть; рекламный баннер «Новогодний челлендж» из выгрузки выброшен
            ("text", {"html": pic(shared("hello_wave"), height=180)
                      + "<h3>Добро пожаловать во вторую часть! 👋</h3>"
                        "<p>Давай с тобой вспомним сначала There is / There are. Расставь слова по "
                        "порядку, чтобы получились целые предложения!</p>"}),

            order("There are four books on the shelf.",
                  ["There", "are", "four books", "on", "the shelf."], title="Составь предложение"),
            order("Where is the living room?", ["Where", "is", "the living room?"],
                  title="Составь предложение"),
            order("It is next to the bathroom.", ["It", "is", "next to", "the bathroom."],
                  title="Составь предложение"),
            order("There is my bedroom.", ["There", "is", "my bedroom."], title="Составь предложение"),
            order("Is there a garden in the house?", ["Is", "there", "a garden", "in", "the house?"],
                  title="Составь предложение"),

            # в выгрузке видео к этому заданию нет вовсе — блок пустой
            ("video", {"title": "Посмотри видео про дом Итана", "url": "", "provider": "youtube"}),

            # «What is their…» — исправлено на there
            ("task", {
                "title": "Посмотри видео и ответь на вопросы ✍",
                "needs_review": True,
                "html": "<ol><li>What is there in their living room?</li>"
                        "<li>Is there a kitchen?</li>"
                        "<li>What is there in Ethan's bedroom?</li>"
                        "<li>What rooms are there in the house?</li></ol>",
            }),

            true_false("Посмотри на картинку и выбери: верно или неверно", [
                ("There is a bed.", True, u("messy_bedroom")),
                ("There are books.", True),
                ("There is a TV.", False),
                ("There is a computer.", True),
                ("There is a desk in the room.", False),
            ]),

            ("speaking", {
                "title": "Моя комната 🎤",
                "image": u("bedroom_rocket"),
                "html": "<p>Нажми на микрофон и расскажи, что есть у тебя в комнате.</p>"
                        "<p><i>Например: There is a bed. There are 2 chairs.</i></p>",
                "needs_review": True,
            }),

            bye("<h3>Ну что же! Держи свой приз и до скорых встреч! 🎉</h3>"
                "<p>Мы с тобой хорошо постарались!</p>", "well_done_medal"),
        ],
    },

    # Homework 4: фразы гостя
    "u3_hw4": {
        **U3,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        "blocks": [
            hello("<h2>Привет! 👋</h2><p>Как здорово, что ты решился взяться за домашнюю "
                  "работу. Поехали!</p>", "hello_rocket"),

            ("text", {"html": REVIEW + pic(u("card_guest_phrases"), "Принимаем гостя")}),

            # в выгрузке левая колонка пустая — картинки наши (Л3.2, Л3.4), СОСТАВ МОЙ
            ("match", {"title": "Соедини картинку и подходящую фразу", "pairs": [
                {"left_image": u("phrase_come_in"), "right": "Hello, please, come in."},
                {"left_image": u("phrase_sandwich"), "right": "Would you like a sandwich?"},
                {"left_image": u("room_bathroom"), "right": "Where is the bathroom?"},
                {"left_image": u("phrase_upstairs"), "right": "It's upstairs."},
                {"left_image": u("phrase_shoes"), "right": "Where are my shoes?"},
                {"left_image": u("phrase_here_you_are"), "right": "Here you are."},
            ]}),

            ("sequence", {"title": "Представь, что ты говоришь со своим другом. Расставь "
                                   "предложения по порядку!", "items": [
                {"text": "Hello, please, come in!"},
                {"text": "Hello, thank you!"},
                {"text": "Where is the bathroom? I need to wash my hands."},
                {"text": "It's upstairs, next to the bedroom."},
                {"text": "Let me show you."},
                {"text": "Come to the living room after that."},
                {"text": "Would you like some tea or coffee?"},
                {"text": "Yes, please!"},
                {"text": "OK, let's go upstairs!"},
            ]}),

            # в выгрузке в банке были лишние слова (go in, want, see, Should, run) —
            # у нашего блока банк только из ответов
            ("gaps", {
                "title": "А теперь давай потренируемся! Вставь пропущенные слова в диалог",
                "mode": "drag",
                "image": u("kids_at_door"),
                "text": "A: Hello! Please, __come in__.\n"
                        "B: Thank __you__!\n"
                        "A: Would you __like__ a cup of __tea__?\n"
                        "B: Yes, __please__, yummy!\n"
                        "A: Where's the __bedroom__?\n"
                        "B: __Let__ me __show__ you!",
                "gaps_expected": 8,
            }),

            ("speaking", {
                "title": "Небольшой challenge ⭐",
                "image": u("phrase_come_in"),
                "html": "<p>Узнай у преподавателя значение слова challenge! Получишь звёздочку, "
                        "если справишься.</p>"
                        "<p>Представь, что ты пришёл в новый дом к своему другу и очень хочешь "
                        "посмотреть его комнату. Составь диалог между вами и запиши его.</p>",
                "needs_review": True,
            }),

            bye("<h3>Ты — молодец! Со всем отлично справился! 🎉</h3><p>До скорой встречи!</p>",
                "well_done_star"),
        ],
    },

    # Homework 5: (1) тренажёр carpet, cushion…, (2) задания. Один урок.
    "u3_hw5": {
        **U3,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        "blocks": [
            hello("<h2>Привет! 👋</h2><p>Добро пожаловать в мир домашнего задания! Сегодня мы "
                  "будем усердно работать, чтобы получить большую звёздочку! Сначала повтори "
                  "слова, с которыми познакомился на уроке.</p>", "hello_headphones"),

            cards(U3_THINGS),
            pic_match("Соедини картинку и слово", U3_THINGS),
            ("quiz", quiz_ru_to_en(U3_THINGS)),
            # у TV gapped() не прячет ни одной буквы — подсказка своя
            spell("Вставь пропущенные буквы и впиши слово целиком", U3_THINGS,
                  lambda en: "T _" if en == "TV" else gapped(en)),

            ("text", {"html": REVIEW + pic(u("card_vocab_carpet"), "Vocabulary")}),

            mcq("Выбери правильный ответ", [
                ("We usually put it on the floor to make our feet warm.",
                 ["carpet", "cushion", "TV"], "carpet"),
                ("We watch it with our friends or family.", ["TV", "poster", "carpet"], "TV"),
                ("We put it on the wall to make it beautiful.", ["poster", "TV", "cushion"],
                 "poster"),
                ("We use it when we need more light.", ["lamp", "cushion", "poster"], "lamp"),
                ("You need to water it regularly.", ["plant", "TV", "cushion"], "plant"),
            ]),

            ("text", {"html":
                "<p><b>Прочитай текст, а потом выбери «Верно» или «Неверно».</b></p>"
                + pic(u("plane_house"), "Plane house")
                + "<p><i>Most people live in a flat or house, some people live in tree houses, old "
                "castles, abandoned lighthouses and even caves but my family is different because "
                "we live in the airplane! Can you imagine?! It is located near a forest here in the "
                "USA and I love it, everything is so green and clean. My father is an engineer and "
                "he loves planes. Of course it only looks like a plane because inside we have "
                "everything we need to live a normal life. There is electricity, running water and "
                "there are a lot of windows! Because we live far from the city, there are some "
                "spectacular views from any window of our unusual home. There is a bathroom and two "
                "bedrooms, one for my parents and the other for me. Mine is at the back of the "
                "plane. It's really very cosy and comfortable. There is also a living room and a "
                "kitchen. It's always funny when my friends come and visit. They like the idea of "
                "living in a plane and so do I. Anyway, I'm sending you some photos. I hope you "
                "like them.</i></p>"}),

            ("truefalse", {"title": "Верно или неверно?", "statements": [
                {"text": "The family lives in a tree.", "correct": False},
                {"text": "The plane is located in Australia.", "correct": False},
                {"text": "The girl's father is a mechanic.", "correct": False},
                {"text": "They have everything they need inside the house.", "correct": True},
                {"text": "They live far away from the city.", "correct": True},
                {"text": "There are five bedrooms in their home.", "correct": False},
                {"text": "The girl loves the idea of living in a plane.", "correct": True},
                {"text": "Her bedroom is very comfortable.", "correct": True},
            ]}),

            ("speaking", {
                "title": "Задание со звёздочкой ⭐",
                "image": u("house_cutaway"),
                "html": "<p>Не обязательно делать, но будет очень здорово, если ты нас порадуешь "
                        "своими успехами! Расскажи нам о своём доме и вещах, которые у тебя есть.</p>"
                        "<ul><li>How many rooms are there in your house?</li>"
                        "<li>Which one is your favourite?</li>"
                        "<li>What is there in your bedroom?</li></ul>",
                "needs_review": True,
            }),

            bye("<h3>Ты справился со всеми заданиями, молодец! 🎉</h3><p>Увидимся на занятии!</p>",
                "well_done_smiley"),
        ],
    },

    # Homework 6: дом Нэнси (аудио), апострофы
    "u3_hw6": {
        **U3,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        "blocks": [
            hello("<h2>Добро пожаловать! 👋</h2><p>Сегодня тебя ждут интересные задания, "
                  "поехали!</p>", "hello_laptop"),

            listening("Послушай диалог. О чём он?"),

            mcq("О чём диалог? Выбери правильный ответ", [
                ("The dialogue is about…", ["Nancy's new house", "Nancy's bedroom",
                                            "Nancy's family"], "Nancy's new house"),
            ]),

            # верных версий в выгрузке нет — зависят от аудио, проверяет учитель
            ("task", {
                "title": "Послушай ещё раз. Перепиши предложения, чтобы они стали верными ✍",
                "needs_review": True,
                "html": "<ol><li>In Nancy's house there are five rooms.</li>"
                        "<li>The bathroom is upstairs.</li>"
                        "<li>There are two bedrooms.</li>"
                        "<li>There's a TV in Nancy's bedroom.</li></ol>",
            }),

            # в выгрузке три варианта без картинок, верный — третий; картинки домов
            # из учебника вставит методист (строка в доработать)
            ("quiz", {"title": "Выбери дом Нэнси. Если нужно — можно прослушать диалог ещё раз",
                      "questions": [{
                          "q": "Which is Nancy's house?", "type": "single",
                          "options": [{"text": "House 1"}, {"text": "House 2"}, {"text": "House 3"}],
                          "correct": [2],
                      }]}),

            ("gaps", {
                "title": "Исправь текст — добавь апострофы. Впиши в каждый пропуск слово "
                         "с апострофом, используй картинку с правилом",
                "mode": "type",
                "image": u("card_apostrophes"),
                "text": "In my dream bedroom __" + alts("there's") + "__ (theres) a big bed. __"
                        + alts("It's") + "__ (Its) blue. Next to the bed __" + alts("there's")
                        + "__ (theres) a table with a lamp. On the floor __" + alts("there's")
                        + "__ (theres) a big carpet. It's red, yellow and orange. There __"
                        + alts("aren't") + "__ (arent) any plants in the room but there are lots "
                        "of posters and photos of my friends. There __" + alts("isn't")
                        + "__ (isnt) a TV but __" + alts("there's") + "__ (theres) a computer.",
                "gaps_expected": 7,
            }),

            ("task", {
                "title": "Комната моей мечты ✍",
                "needs_review": True,
                "image": u("house_cutaway_cartoon"),
                "html": "<p>Теперь напиши о своей комнате мечты. Используй текст из предыдущего "
                        "задания как пример.</p>",
            }),

            bye("<h3>Ура, ты справился с домашним заданием, ты — супер ученик! 🎉</h3>"
                "<p>Увидимся на занятии!</p>", "well_done_trophy"),
        ],
    },

    # Homework 7: повторение юнита
    "u3_hw7": {
        **U3,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Добро пожаловать в мир домашнего задания! Давай "
                  "приступим к повторению.</p>", "hello_wave"),

            ("gaps", {
                "title": "Заполни пропуски: there is / there are. Это могут быть вопросы, "
                         "отрицания или утверждения",
                "mode": "type",
                "text": "1. __" + alts("There is", "There's") + "__ a table in the kitchen. (+)\n"
                        "2. __Is there__ a phone on the table? (?)\n"
                        "3. __" + alts("There aren't", "There are not") + "__ two beds in the "
                        "bedroom. (−)\n"
                        "4. __" + alts("There is", "There's") + "__ a desk in the bedroom. (+)\n"
                        "5. __" + alts("There isn't", "There is not") + "__ a rat behind the "
                        "door. (−)\n"
                        "6. __Are there__ four people at home? (?)",
                "gaps_expected": 6,
            }),

            # в выгрузке строчная буква и точка отдельным словом — нормализовано
            order("There isn't a ruler on the table.",
                  ["There", "isn't", "a ruler", "on", "the table."],
                  title="Составь предложения из слов — расставь слова по порядку"),
            order("Are there any students in the classroom?",
                  ["Are", "there", "any", "students", "in", "the classroom?"],
                  title="Составь предложение"),
            order("Is there a television in your bedroom?",
                  ["Is", "there", "a television", "in", "your bedroom?"],
                  title="Составь предложение"),

            # «Is there any games console?» в выгрузке — исправлено на «a games console»
            ("gaps", {
                "title": "Заверши диалог, используя there, isn't, a, any",
                "mode": "drag",
                "image": u("photo_modern_house"),
                "text": "Sally: This is my new house. There's __a__ big garden.\n"
                        "Marina: Are there __any__ trees in the garden?\n"
                        "Sally: No, there aren't __any__ trees. The garden is too small for trees. "
                        "But the house is big.\n"
                        "Marina: Is your bedroom big?\n"
                        "Sally: Yes, it is. There's a bed, a desk and a chair. __There__ are four "
                        "posters on the wall too.\n"
                        "Marina: Is there __a__ games console?\n"
                        "Sally: No, there __isn't__, but there's a computer!",
                "gaps_expected": 6,
            }),

            # в выгрузке фото людей у двери — у нас нарисованная сцена Л3.5;
            # лишние слова банка (Where, thank you, give, want, welcome) не переносятся
            ("gaps", {
                "title": "Вставь пропущенные слова в диалог",
                "mode": "drag",
                "image": u("scene_guests_door"),
                "text": "A: Hello. Please __come__ in.\n"
                        "B: Thank you.\n"
                        "A: __Would__ you like a sandwich?\n"
                        "B: Yes, __please__. Where's the bathroom, please?\n"
                        "A: It's __upstairs__. It's next to Andrew's bedroom. __Let__ me show you.\n"
                        "B: Thanks.",
                "gaps_expected": 5,
            }),

            ("task", {
                "title": "Задание для самых-самых ⭐",
                "needs_review": True,
                "image": u("kids_bedroom"),
                "html": "<p>Расскажи нам про комнату своей мечты! Напиши 4–5 предложений.</p>",
            }),

            # Wordwall «Anagram · GG1 3.1 Anagram» — СОСТАВ МОЙ
            spell(CHAMPION + "Расшифруй и впиши слова ⭐",
                  [w for w in U3_ROOMS + U3_FURN
                   if w[0] in ("kitchen", "bedroom", "garden", "wardrobe", "armchair", "fridge")],
                  anagram),

            # Wordwall «Quiz · Prepositions of place (GG1 3.2)» — СОСТАВ МОЙ
            mcq("Посмотри на картинку и выбери правильный вариант ⭐", [
                (q, ["on", "under", "in", "behind", "next to", "in front of"], ok,
                 u("prepositions_living_room"))
                for q, ok in [
                    ("Where is the trophy? It's ___ the shelf.", "on"),
                    ("Where is the lamp? It's ___ the sofa.", "next to"),
                    ("Where is the fish bowl? It's ___ the small table.", "on"),
                    ("Where are the dogs? They're ___ the coffee table.", "under"),
                    ("Where is the plane? It's ___ the box.", "in"),
                    ("Where is the window? It's ___ the sofa.", "behind"),
                ]
            ]),

            # Wordwall «Quiz · gg1 3.3 photocopiable ex 1» — СОСТАВ МОЙ
            mcq("Выбери правильный вариант ⭐", [
                ("___ a TV in your bedroom?", ["Is there", "Are there"], "Is there"),
                ("___ any plants in the kitchen?", ["Is there", "Are there"], "Are there"),
                ("There ___ any posters on the wall.", ["isn't", "aren't"], "aren't"),
                ("There ___ a lamp on the desk.", ["isn't", "aren't"], "isn't"),
                ("Is there a garden? — No, there ___.", ["isn't", "aren't"], "isn't"),
                ("Are there two bedrooms? — Yes, there ___.", ["is", "are"], "are"),
            ]),

            bye("<h3>Ты здорово потрудился! 🎉</h3><p>До скорой встречи в нашей World of "
                "Homework! Удачи на тесте!</p>", "good_luck_clover"),
        ],
    },

    "u3_test": {
        **U3,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        "blocks": [
            # в выгрузке левая колонка пустая — картинки наши, СОСТАВ МОЙ
            ("match", {"title": "Соедини слова и картинки", "pairs": [
                {"left_image": u("prep_on"), "right": "on the box"},
                {"left_image": u("room_living_room"), "right": "living room"},
                {"left_image": u("furn_wardrobe"), "right": "wardrobe"},
                {"left_image": u("prep_in_front_of"), "right": "in front of the box"},
                {"left_image": u("furn_shower"), "right": "shower"},
                {"left_image": u("part_window"), "right": "window"},
            ]}),

            # в выгрузке пропуск — одна буква; у нас слово целиком
            ("exact_input", {"title": "Посмотри на картинку, вставь пропущенные буквы и впиши "
                                      "слово целиком", "items": [
                {"prompt": hint, "accept": acc, "image": u(p)}
                for hint, acc, p in [
                    ("un_er the tree", ["under the tree", "under", "Under the tree", "Under"],
                     "photo_presents_tree"),
                    ("l_mp", ["lamp", "Lamp"], "photo_lamp"),
                    ("c_rp_t", ["carpet", "Carpet"], "furn_carpet"),
                    ("gar_en", ["garden", "Garden"], "photo_garden"),
                    ("b_dro_m", ["bedroom", "Bedroom"], "photo_bedroom_2"),
                    ("arm_hair", ["armchair", "Armchair"], "photo_armchair"),
                ]
            ]}),

            # опечатки выгрузки (recoon, garege) исправлены
            mcq("Прочитай диалог и выбери пропущенное слово", [
                ("A: ___ there a raccoon on my head? B: Yes, there is. And there's a squirrel too.",
                 ["Is", "Are"], "Is", u("raccoon_squirrel")),
                ("A: Is there a raccoon on my head? B: ___, there is. And there's a squirrel too.",
                 ["Yes", "No"], "Yes"),
                ("A: ___ there two clowns on the table? B: Yes, there are.", ["Is", "Are"], "Are",
                 u("clowns")),
                ("A: Are there two clowns on the table? B: Yes, there ___.",
                 ["are", "aren't", "is", "isn't"], "are"),
                ("A: Is ___ a unicorn in the kitchen? B: No, there isn't.", ["there", "here"],
                 "there", u("unicorn")),
                ("A: Is there a unicorn in the kitchen? B: ___, there isn't.", ["Yes", "No"], "No"),
                ("A: ___ there a big pink elephant in the garage? B: Yes, there is! But there isn't "
                 "a big pink elephant in the house!", ["Is", "Are"], "Is", u("pink_elephant")),
                ("A: Is there a big pink elephant in the garage? B: ___, there is! But there isn't "
                 "a big pink elephant in the house!", ["Yes", "No"], "Yes"),
                ("A: ___ you like an ice cream sandwich? B: Yes, please!", ["Would", "Do"], "Would",
                 u("ice_cream_sandwich")),
            ]),

            order("There isn't a jellyfish on the table.",
                  ["There", "isn't", "a jellyfish", "on", "the table."],
                  title="Расставь слова в правильном порядке", image=u("jellyfish")),
            order("There aren't four funny dragons in the garden.",
                  ["There", "aren't", "four", "funny dragons", "in", "the garden."],
                  title="Расставь слова в правильном порядке", image=u("dragon")),
            order("There isn't a small green alien in the garage.",
                  ["There", "isn't", "a small green", "alien", "in", "the garage."],
                  title="Расставь слова в правильном порядке", image=u("alien")),
            order("There are twenty lazy cats in my grandma's bedroom.",
                  ["There", "are", "twenty lazy cats", "in", "my grandma's", "bedroom."],
                  title="Расставь слова в правильном порядке", image=u("cat_sofa")),
            order("There is a crazy blue monster in my bedroom.",
                  ["There", "is", "a crazy blue", "monster", "in", "my bedroom."],
                  title="Расставь слова в правильном порядке", image=u("blue_monster")),

            # в выгрузке текст — картинкой
            ("text", {"html":
                "<h3>READING</h3><p>Прочитай описание комнаты подростка.</p>"
                "<p><i>This is my bedroom. There is a bed next to the window. There is a small desk "
                "in front of the bed. My laptop is on the desk. There is a wardrobe behind the "
                "door. There are two posters on the wall. There aren't any plants in my room. My "
                "skateboard is under the bed. There isn't a TV in my bedroom — I watch films in the "
                "living room.</i></p>"}),

            ("truefalse", {"title": "READING. Правда или неправда?", "statements": [
                {"text": "The bed is next to the window.", "correct": True},
                {"text": "The desk is behind the bed.", "correct": False},
                {"text": "The laptop is on the desk.", "correct": True},
                {"text": "There are three posters on the wall.", "correct": False},
                {"text": "There are plants in the bedroom.", "correct": False},
                {"text": "The skateboard is under the bed.", "correct": True},
                {"text": "There is a TV in the bedroom.", "correct": False},
            ]}),

            listening("LISTENING. Прослушай 5 коротких описаний."),

            ("match", {"title": "LISTENING. Соедини каждый номер с названием комнаты в доме",
                       "pairs": [
                           {"left": "Description 1", "right": "kitchen"},
                           {"left": "Description 2", "right": "living room"},
                           {"left": "Description 3", "right": "bathroom"},
                           {"left": "Description 4", "right": "bedroom"},
                           {"left": "Description 5", "right": "garage"},
                       ]}),

            ("speaking", {
                "title": "SPEAKING TASK 🎤",
                "image": u("kids_room_test"),
                "html": "<p>Посмотри на картинку и опиши её. Эти вопросы могут тебе помочь. "
                        "Запиши свой ответ, нажав на кнопку микрофона 🙌</p>"
                        "<ol><li>Where is the guitar?</li><li>Where is the teddy bear?</li>"
                        "<li>How many boxes are there on the wardrobe?</li>"
                        "<li>Where is the book?</li><li>Where is the school bag?</li>"
                        "<li>Where is the skateboard?</li><li>Where is the ball?</li>"
                        "<li>How many books are there on the shelf?</li>"
                        "<li>Where is the chair?</li><li>Where is the carpet?</li>"
                        "<li>How many lamps are there in the room?</li></ol>",
                "needs_review": True,
            }),
        ],
    },
}
