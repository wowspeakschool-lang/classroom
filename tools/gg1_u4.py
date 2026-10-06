#!/usr/bin/env python3
"""Go Getter 1 · Unit 4 · Look at me — уроки (разбор: docs/GG1_разбор/u4.md).

Лицо, тело, волосы, have got / has got (утверждение, отрицание, вопросы),
притяжательные, извинения, черты характера. Картинки слов — листы Л4.1–Л4.6
(мультяшные дети, сгенерированы); карточки методиста и мультяшные картинки
учебника — кадры из PDF выгрузки (tools/gg1_pdf_frames.py). Фото людей и
копирайтных персонажей (Микки, Шрек, Минни) не берём: Шрек заменён двумя
монстрами, Бонзо, бабушка, класс и дети на площадке — сгенерированные.
"""
from gg1_lib import *  # noqa: F401,F403

U = "u4"
U4 = {"unit": U, "unit_title": "Unit 4 · Look at me", "unit_sort": 4}


def u(name):
    return img(U, name)


# В выгрузке у обоих тренажёров HW1 поле «Определение» пустое — переводы наши.
U4_FACE = vocab([
    ("eyes", "глаза", "body_eyes"),
    ("nose", "нос", "body_nose"),
    ("mouth", "рот", "body_mouth"),
    ("hair", "волосы", "body_hair"),
    ("foot", "стопа", "body_foot"),
    ("hand", "кисть руки", "body_hand"),
    ("teeth", "зубы", "body_teeth"),
    ("ears", "уши", "body_ears"),
])

U4_HAIR = vocab([
    ("red hair", "рыжие волосы", "hair_red"),
    ("spiky hair", "торчащие волосы (ёжиком)", "hair_spiky"),
    ("wavy hair", "волнистые волосы", "hair_wavy"),
    ("dark hair", "тёмные волосы", "hair_dark"),
    ("curly hair", "кудрявые волосы", "hair_curly"),
    ("straight hair", "прямые волосы", "hair_straight"),
    ("blond hair", "светлые волосы (блонд)", "hair_blond"),
    ("fair hair", "русые волосы", "hair_fair"),
])

U4_BODY = vocab([
    ("arm", "рука (от плеча)", "body_arm"),
    ("hand", "кисть руки", "body_hand"),
    ("foot", "стопа", "body_foot"),
    ("leg", "нога", "body_leg"),
    ("head", "голова", "body_head"),
    ("fingers", "пальцы рук", "body_fingers"),
    ("toes", "пальцы ног", "body_toes"),
    ("body", "тело", "body_body"),
    ("neck", "шея", "body_neck"),
    ("feet", "ступни", "body_feet"),
])

U4_PERS = vocab([
    ("clever", "умный", "pers_clever"),
    ("friendly", "дружелюбный", "pers_friendly"),
    ("funny", "смешной, весёлый", "pers_funny"),
    ("helpful", "отзывчивый", "pers_helpful"),
    ("sporty", "спортивный", "pers_sporty"),
    ("nice", "приятный, добрый", "pers_nice"),
])

CHAMPION = ("Ты выполнил все задания из основной части! А это дополнительное задание — "
            "для настоящих чемпионов! ")
REVIEW = "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"
ORDER = "Расставь слова в правильном порядке"


def listen_write(words, title="Послушай и впиши слово"):
    """«Послушай и впиши» тренажёра: слово звучит, подсказка — перевод."""
    return ("exact_input", {"title": title, "items": [
        {"prompt": ru, "accept": list(dict.fromkeys([en, en.capitalize()])), "audio_tts": en}
        for en, ru, p in words
    ]})


def hair_quiz(items):
    """«Выбери 2 слова, подходящие под описание волос»: два верных из четырёх."""
    qs = []
    for picture, opts, ok in items:
        qs.append({"q": "Посмотри на картинку. Выбери 2 слова, подходящие под описание волос.",
                   "type": "multiple", "image": u(picture),
                   "options": [{"text": o} for o in opts],
                   "correct": [opts.index(o) for o in ok]})
    return ("quiz", {"title": "Какие у них волосы?", "questions": qs})


LESSONS = {
    # Homework 1 (1) — тренажёр «лицо и тело», (2) — тренажёр «волосы», (3) — задания.
    # Один урок, блоки подряд.
    "u4_hw1": {
        **U4,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня мы учим слова про лицо, тело и волосы. Выполни все "
                  "задания, чтобы выучить их на все 100!</p>"),

            # тренажёр «лицо и тело»
            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U4_FACE
            ]}),
            ("match", {"title": "Найди пары", "pairs": [
                {"left": en, "right": ru, "left_audio_tts": en} for en, ru, p in U4_FACE
            ]}),
            ("quiz", quiz_ru_to_en(U4_FACE)),
            listen_write(U4_FACE),

            # тренажёр «волосы»
            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U4_HAIR
            ]}),
            ("match", {"title": "Соедини картинку и слово", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en} for en, ru, p in U4_HAIR
            ]}),
            ("quiz", quiz_ru_to_en(U4_HAIR)),
            listen_write(U4_HAIR),

            # задания
            ("text", {"html": "<h3>Добро пожаловать в третью часть домашнего задания! 👋</h3>"
                              + REVIEW + pic(u("card_face_body"), "Face, Body & Hair")}),

            # в выгрузке «Открытый вопрос» — у нас с автопроверкой
            ("gaps", {
                "title": "Посмотри на картинку и напиши названия частей лица. Например, 1 — ear",
                "mode": "type",
                "image": u("face_numbers"),
                "text": "1 — __ear|ears__\n"
                        "2 — __hair__\n"
                        "3 — __eye|eyes__\n"
                        "4 — __nose__\n"
                        "5 — __teeth|tooth__\n"
                        "6 — __mouth__",
                "gaps_expected": 6,
            }),

            # в выгрузке правая колонка пустая — картинки наши (Л4.3)
            ("match", {"title": "Соедини слово и картинку", "pairs": [
                {"left": en, "right_image": u("body_" + en), "left_audio_tts": en}
                for en in ["eyes", "teeth", "ears", "nose"]
            ]}),

            hair_quiz([
                ("kid_short_blond", ["long", "short", "red", "blond"], ["short", "blond"]),
                ("kid_spiky_red", ["red", "straight", "spiky", "black"], ["spiky", "red"]),
                ("kid_curly_black", ["wavy", "black", "blond", "curly"], ["curly", "black"]),
                ("kid_long_black", ["black", "short", "long", "blond"], ["long", "black"]),
            ]),

            order("short straight blond hair", title=ORDER),
            order("big blue eyes", title=ORDER),
            order("long curly brown hair", title=ORDER),
            order("short wavy red hair", title=ORDER),

            ("speaking", {
                "title": "Глаза и волосы 🎤",
                "html": "<p>Выбери одного из членов семьи. Нажми на микрофон и расскажи, какие у него "
                        "глаза и волосы.</p><p><i>Пример: small brown eyes, long straight red hair</i></p>",
                "needs_review": True,
            }),

            # Wordwall «GG1 U4 4.1 face» (обложка пустая) — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини слова с картинками ⭐", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in U4_FACE if en in ("eyes", "nose", "mouth", "hair", "teeth", "ears")
            ]}),

            # Wordwall «gg1 4.1» (обложка пустая) — СОСТАВ МОЙ: слова из перепутанных букв
            ("exact_input", {"title": "Впиши слова: собери слово из букв ⭐", "items": [
                {"prompt": anagram(en), "accept": [en, en.capitalize()], "image": u(p), "audio_tts": en}
                for en, ru, p in U4_FACE
            ]}),

            bye("<h3>Ты справился со всеми заданиями, ты большой молодец! 🎉</h3>"
                "<p>Увидимся на занятии! Goodbye!</p>", "well_done_star"),
        ],
    },

    # Homework 2 (1) — тренажёр «тело», (2) — have got / has got. Один урок.
    "u4_hw2": {
        **U4,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>В домашнем задании мы вспомним, что проходили на уроке, и у "
                  "нас будет путешествие в страну грамматики 😉</p>", "hello_book"),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U4_BODY
            ]}),
            ("match", {"title": "Соедини картинку и слово", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en} for en, ru, p in U4_BODY
            ]}),
            ("quiz", quiz_ru_to_en(U4_BODY)),
            listen_write(U4_BODY),

            ("text", {"html":
                "<h3>Have got / has got</h3>"
                "<p>Для начала вспомним правило. <b>Have got / has got</b> нужны, чтобы сказать, что у "
                "нас что-то есть или, наоборот, нет.</p>"
                "<ul><li><b>have got</b> — с местоимениями I, we, you, they и с множественным числом;</li>"
                "<li><b>has got</b> — с местоимениями he, she, it и в 3-м лице единственного числа.</li></ul>"
                "<p>Сейчас посмотри видео и вспомни, о чём мы говорили на уроке 😉</p>"}),
            ("video", {"title": "Have got / has got", "url": "", "provider": "youtube"}),

            ("text", {"html": REVIEW + pic(u("card_have_got"), "have got")}),

            ("gaps", {
                "title": "Давай теперь потренируемся! Вставь have got / haven't got / has got / hasn't got",
                "mode": "drag",
                "text": "1. Mary __has got__ a car, but she __hasn't got__ a motorbike.\n"
                        "2. John and Mary __have got__ blue eyes and dark hair, they are twins.\n"
                        "3. Samantha __hasn't got__ a cat, but she __has got__ a dog, she is a dog lover.\n"
                        "4. My sisters __have got__ dark hair.\n"
                        "5. My mother __has got__ a small head and big ears.\n"
                        "6. Alex __hasn't got__ a big face, his face is small.\n"
                        "7. Trevor __hasn't got__ a mobile phone, he sends emails.",
                "gaps_expected": 9,
            }),

            order("I have got a lot of money.", ["I", "have got", "a lot of", "money."],
                  title="Давай расставим слова по порядку, чтобы получились предложения!"),
            order("She has got brown hair and blue eyes.",
                  ["She", "has got", "brown hair", "and", "blue eyes."], title=ORDER),
            order("My sisters have got computers.", ["My", "sisters", "have got", "computers."],
                  title=ORDER),
            order("Students have got books and copy-books.",
                  ["Students", "have got", "books", "and copy-books."], title=ORDER),
            order("My dog has got a bone.", ["My dog", "has got", "a bone."], title=ORDER),
            order("They have got a large family.", ["They", "have got", "a large", "family."],
                  title=ORDER),

            ("task", {
                "title": "Что есть у Molly и Nick?",
                "needs_review": True,
                "html": pic(u("venn_have_got"), "Have got: Nick and Molly")
                        + "<p>Посмотри на картинку и напиши предложения о том, что есть у Molly и Nick. "
                        "Подсказка: используй have got / has got.</p>"
                        "<ol><li>What has Molly got?</li><li>What has Nick got?</li>"
                        "<li>What have they got?</li></ol>",
            }),

            ("speaking", {
                "title": "Мой рюкзак 🎤",
                "html": "<p>Нажми на микрофон и ответь на вопрос: <b>What have you got in your school bag "
                        "today?</b></p><p><i>Пример: I've got two books, a pencil case and a bottle of "
                        "water.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Quiz · GG1 4.2» — СОСТАВ МОЙ
            mcq(CHAMPION + "Выбери правильный вариант ⭐", [
                ("I ___ two brothers.", ["have got", "has got"], "have got"),
                ("She ___ long curly hair.", ["has got", "have got"], "has got"),
                ("My dog ___ big ears.", ["has got", "have got"], "has got"),
                ("We ___ a cat. We've got a dog.", ["haven't got", "hasn't got"], "haven't got"),
                ("Tom ___ a bike. He walks to school.", ["hasn't got", "haven't got"], "hasn't got"),
                ("They ___ blue eyes.", ["have got", "has got"], "have got"),
            ]),

            # Wordwall «Unjumble · gg1 4.2» — СОСТАВ МОЙ
            order("He has got spiky hair.", title=ORDER + " ⭐"),
            order("We haven't got a car.", title=ORDER + " ⭐"),
            order("My cat has got green eyes.", title=ORDER + " ⭐"),

            bye("<h3>Ты большой молодец сегодня! 🎉</h3><p>Ты получаешь звёздочку за прекрасный "
                "результат! До новых встреч!</p>", "well_done_star"),
        ],
    },

    "u4_hw3": {
        **U4,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hey there! 👋</h2><p>Привет, дорогой друг! Сегодня мы продолжим увлекательное "
                  "путешествие в мир английского языка и будем вместе упражняться в новой теме! "
                  "Удачи!</p>", "hello_highfive"),

            ("text", {"html": REVIEW + pic(u("card_have_got_questions"), "have got: вопросы")}),

            ("hotspot", {
                "title": "Давай вспомним слова, которые учили! Подпиши части тела на картинке",
                "mode": "label",
                "image": u("girl_jumping"),
                "points": [
                    {"x": 44.3, "y": 31.7, "text": "nose"},
                    {"x": 41.4, "y": 14.7, "text": "blond hair"},
                    {"x": 54.3, "y": 34.0, "text": "mouth"},
                    {"x": 66.9, "y": 32.6, "text": "ear"},
                    {"x": 34.7, "y": 85.2, "text": "leg"},
                    {"x": 64.9, "y": 76.2, "text": "foot"},
                    {"x": 5.6, "y": 25.4, "text": "finger"},
                    {"x": 47.0, "y": 41.5, "text": "neck"},
                ],
                "extras": [],
            }),

            ("text", {"html": pic(shared("well_done_medal"), height=180)
                              + "<h3>Какой ты молодец! Лови награду! 🏅</h3>"
                              "<p>И приступим к кое-чему новенькому 😉</p>"}),

            ("video", {"title": "Посмотри видео и запомни, как мы задаём вопросы с have got",
                       "url": "", "provider": "youtube"}),

            # в выгрузке «Mrs. Smiths» — исправлено
            ("match", {"title": "Давай найдём ответы на вопросы. Соедини половинки", "pairs": [
                {"left": "Have you got a brother?", "right": "No, I haven't. But I've got a sister."},
                {"left": "Has she got an interesting book?",
                 "right": "Yes, she has. It's about Harry Potter."},
                {"left": "Has your mother got a car?", "right": "No, she hasn't. She usually takes a taxi."},
                {"left": "Has Mrs Smith got a beautiful garden?",
                 "right": "Yes, she has. There are lots of different flowers."},
                {"left": "Has your friend got a skateboard?", "right": "Yes, he has. He loves it."},
                {"left": "Has your family got a big house?",
                 "right": "No, we haven't. We live in a small flat near the station."},
            ]}),

            # в выгрузке — кадр из «Шрека» и открытый вопрос; у нас два монстра (Л4.2),
            # вопросы переписаны под картинку — ТЕКСТ МОЙ
            ("text", {"html": "<p><b>Посмотри на картинку. Это монстры Зог (Zog) и Боб (Bob). "
                              "Зог высокий, Боб круглый.</b></p>"
                              + pic(u("scene_two_monsters"), "Zog and Bob", 300)
                              + "<p><i>Пример: Has Zog got three legs? — No, he hasn't.</i></p>"}),
            mcq("Посмотри на Зога и Боба и выбери правильный ответ", [
                ("Have Zog and Bob got green skin?", ["Yes, they have.", "No, they haven't."],
                 "Yes, they have."),
                ("Has Zog got a long neck?", ["Yes, he has.", "No, he hasn't."], "Yes, he has."),
                ("Has Bob got long hair?", ["Yes, he has.", "No, he hasn't."], "No, he hasn't."),
                ("Have they got big eyes?", ["Yes, they have.", "No, they haven't."], "Yes, they have."),
                ("Has Bob got a big mouth?", ["Yes, he has.", "No, he hasn't."], "Yes, he has."),
                ("Has Zog got short legs?", ["Yes, he has.", "No, he hasn't."], "No, he hasn't."),
            ]),

            order("Has Zog got a long neck?", title="Расставь слова по порядку, чтобы получились вопросы",
                  image=u("scene_two_monsters")),
            order("Has Bob got a big head?", title="Расставь слова по порядку, чтобы получились вопросы"),
            order("Have they got big eyes?", title="Расставь слова по порядку, чтобы получились вопросы"),
            order("Have they got green skin?", title="Расставь слова по порядку, чтобы получились вопросы"),

            ("speaking", {
                "title": "Ответь на вопросы 🎤",
                "html": "<p>Мы тобой гордимся! Давай выполним ещё одно задание. Нажми на микрофон и "
                        "ответь на вопросы:</p>"
                        "<ol><li>Have you got a pet? Which one?</li><li>Has your mother got dark hair?</li>"
                        "<li>Has your father got a car?</li><li>Have you got any brothers or sisters?</li>"
                        "<li>Has your friend got an interesting book?</li></ol>",
                "needs_review": True,
            }),

            # Wordwall «Quiz · gg1 4.3 have got?» — СОСТАВ МОЙ
            mcq(CHAMPION + "Выбери правильный вариант ⭐", [
                ("___ you got a sister?", ["Have", "Has"], "Have"),
                ("___ your dad got a car?", ["Has", "Have"], "Has"),
                ("Has she got blue eyes? — Yes, she ___.", ["has", "have", "is"], "has"),
                ("Have they got a dog? — No, they ___.", ["haven't", "hasn't", "aren't"], "haven't"),
                ("___ it got a long tail?", ["Has", "Have"], "Has"),
                ("Have you got curly hair? — No, I ___.", ["haven't", "hasn't", "don't"], "haven't"),
            ]),

            # Wordwall «Quiz · GG1 4.3 Possessives» — СОСТАВ МОЙ
            mcq("Выбери правильное слово ⭐", [
                ("I've got a cat. ___ cat is black.", ["My", "Your", "Its"], "My"),
                ("You've got a new bike. ___ bike is cool.", ["Your", "Our", "Their"], "Your"),
                ("He's got a sister. ___ sister is ten.", ["His", "Her", "Its"], "His"),
                ("She's got a dog. ___ dog is funny.", ["Her", "His", "Our"], "Her"),
                ("The dog has got big ears. ___ ears are brown.", ["Its", "Their", "Our"], "Its"),
                ("We've got a house. ___ house is big.", ["Our", "Their", "Your"], "Our"),
                ("They've got a car. ___ car is red.", ["Their", "Our", "Its"], "Their"),
            ]),

            bye("<h3>Спасибо тебе за твою усердную работу! 🎉</h3><p>До новых встреч! Bye!</p>",
                "well_done_clap"),
        ],
    },

    "u4_hw4": {
        **U4,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        "blocks": [
            hello("<h2>Welcome back! 👋</h2><p>Добро пожаловать на страничку домашнего задания! Будем "
                  "проверять твои силы и знания, полученные на уроке! Do your best! (Постарайся!)</p>",
                  "hello_laptop"),

            ("text", {"html": REVIEW + pic(u("card_sorry"), "Sorry about that!")}),

            ("sequence", {
                "title": "Мы должны быть вежливыми! Фразы с урока нам в этом помогут. Расставь "
                         "предложения в диалоге по порядку",
                "image": u("broken_cup"),
                "items": [
                    {"text": "Oh no, my favourite cup is broken!"},
                    {"text": "I'm so sorry."},
                    {"text": "That's all right. I have a new one."},
                ],
            }),
            # в выгрузке — фото девочки с будильником; у нас сгенерированный будильник
            ("sequence", {
                "title": "Расставь предложения в диалоге по порядку",
                "image": u("scene_alarm_clock"),
                "items": [
                    {"text": "Jane! It's 9:30! You're late again!"},
                    {"text": "Sorry about that."},
                    {"text": "It's OK, be careful next time!"},
                ],
            }),
            # в выгрузке — фото детей; у нас сгенерированная площадка
            ("sequence", {
                "title": "Расставь предложения в диалоге по порядку",
                "image": u("kids_hurt"),
                "items": [
                    {"text": "Are you OK? I hurt you…"},
                    {"text": "It's OK."},
                    {"text": "Are you sure?"},
                    {"text": "I'm fine."},
                ],
            }),

            # в выгрузке во втором вопросе A: «I'm fine.» — исправлено на извинение;
            # отвлекающие, которые тоже подходили по смыслу, заменены
            mcq("Выбери правильный ответ", [
                ("A: I'm sorry. B: ___", ["That's all right.", "I'm fine.", "Are you OK?"],
                 "That's all right."),
                ("A: I'm so sorry. B: ___", ["That's all right.", "Sorry, my mistake.", "Are you OK?"],
                 "That's all right."),
                ("A: Are you OK? B: ___", ["Yes, I'm fine.", "No problem.", "That's all right."],
                 "Yes, I'm fine."),
                ("A: Sorry about that! B: ___", ["No problem!", "I'm OK.", "I'm fine."], "No problem!"),
            ]),

            ("gaps", {
                "title": "Вставь в пропуски слова, чтобы получились диалоги",
                "mode": "drag",
                "image": u("sorry_boy"),
                "text": "1. A: I can't find my phone! B: I've got it! __Sorry__ about that! "
                        "A: That's __all right__.\n"
                        "2. A: Ohhh! I'm so __sorry__! B: It's OK! A: Are you __sure__? B: Yes, I'm __fine__!\n"
                        "3. A: These aren't my keys. B: Sorry, my __mistake__. Here you are. "
                        "A: No __problem__!",
                "gaps_expected": 7,
            }),

            ("video", {"title": "Посмотри видео про Генри и Эмму и ответь: верно или неверно",
                       "url": "", "provider": "youtube"}),
            ("truefalse", {"title": "Верно или неверно? (по видео)", "statements": [
                {"text": "Henry hurts his cat.", "correct": False},
                {"text": "Emma opens Henry's parcel.", "correct": True},
                {"text": "Mother spills orange juice.", "correct": False},
                {"text": "Henry drives his toy car into Emma's toys.", "correct": True},
                {"text": "Henry eats his sweet.", "correct": False},
            ]}),

            ("speaking", {
                "title": "Что ты скажешь? 🎤",
                "html": "<p>Представь, что бы ты сказал в этих случаях. Нажми на микрофон и ответь:</p>"
                        "<ol><li>You break your mum's cup.</li><li>You forget to call your friend back.</li>"
                        "<li>You are late for school.</li><li>You don't buy a present for your friend.</li></ol>",
                "needs_review": True,
            }),

            bye("<h3>Ура! У тебя всё получилось! 🎉</h3><p>Great job! Увидимся на занятии!</p>",
                "well_done_jump"),
        ],
    },

    "u4_hw5": {
        **U4,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        "blocks": [
            hello("<h2>Welcome to the HOMEWORK world! 👋</h2><p>Добро пожаловать в мир домашнего "
                  "задания! Сегодня мы будем читать и выполнять интересные задания по тексту!</p>",
                  "hello_rocket"),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U4_PERS
            ]}),

            ("text", {"html": REVIEW + pic(u("card_personality"), "Personality adjectives")}),

            ("gaps", {
                "title": "Впиши пропущенные слова",
                "mode": "drag",
                "text": "1. Max is very __clever__. He always reads books and gets good marks at school.\n"
                        "2. Maria has got a lot of friends. She is __friendly__.\n"
                        "3. Antonio always makes me laugh. He is very __funny__.\n"
                        "4. Dan is usually __helpful__. He helps me with homework.\n"
                        "5. My family is __sporty__. We regularly play tennis and go to the gym.",
                "gaps_expected": 5,
            }),

            # в выгрузке — страница учебника с фото детей; у нас только текст
            ("text", {"html":
                "<p><b>Давай прочитаем текст про Тима и выполним задания!</b></p>"
                "<p><i>Hi. My name's Tim. I'm eleven and I'm from London. I've got two brothers, three "
                "sisters and … ten cousins! My favourite hobby is reading and I've got a lot of books on "
                "my desk. I've got a bike and a skateboard, but I'm not very sporty. My best friend is "
                "good at football. His name is Max and he's very nice. Max is my neighbour too. Our "
                "favourite place is his garden. We've got a little house in a tree! Max has got a "
                "sister. Her name is Lucy and she's very clever. Max and I are not very good at Maths, "
                "but she is very helpful! I like Lucy!</i></p>"}),

            ("truefalse", {"title": "Прочитай текст ещё раз и выбери: верно или неверно", "statements": [
                {"text": "Tim is twenty years old.", "correct": False},
                {"text": "There are seven children in his family.", "correct": False},
                {"text": "He's got lots of books on his desk.", "correct": True},
                {"text": "Tim is really sporty.", "correct": False},
                {"text": "Max is good at football.", "correct": True},
                {"text": "Max lives far away from Tim.", "correct": False},
                {"text": "Lucy is very helpful.", "correct": True},
                {"text": "Max and Tim have got a big house in a tree.", "correct": False},
            ]}),

            ("gaps", {
                "title": "Заполни пропуски нужными словами",
                "mode": "drag",
                "text": "1. Tim's hobby is __reading__.\n"
                        "2. I've got a bike and a __skateboard__.\n"
                        "3. My best __friend__ is good at football.\n"
                        "4. Our favourite place is his __garden__.\n"
                        "5. Max and Tim are not very good at __Maths__.",
                "gaps_expected": 5,
            }),

            ("task", {
                "title": "Мой характер ✍️",
                "needs_review": True,
                "html": "<p>А теперь напиши о своём характере и о характере своего лучшего друга.</p>"
                        "<p><i>Пример: I'm friendly and helpful. I'm sporty too. My best friend is funny "
                        "and clever. We're nice people!</i></p>",
            }),

            bye("<h3>Спасибо тебе за твои ответы! 🎉</h3><p>See you soon! До скорой встречи!</p>",
                "well_done_smiley"),
        ],
    },

    "u4_hw6": {
        **U4,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня нас ждут приключения в стране Listening! Мы будем "
                  "слушать, смотреть разные интересные видео и узнавать новые вещи!</p>",
                  "hello_headphones"),

            listening("Наше первое задание — послушать и запомнить как можно больше о Дарле (Darla)."),

            ("gaps", {
                "title": "А теперь заполни пропуски нужным словом. Ты можешь прослушать аудио ещё раз",
                "mode": "type",
                "text": "1. Darla is from Dublin, __Ireland__.\n"
                        "2. She's got a __long__ face.\n"
                        "3. Her hair is red and __curly__.\n"
                        "4. Darla gets good marks at school — she's __clever__.\n"
                        "5. Her dog's got big brown __eyes__.\n"
                        "6. He's got a funny __little__ face.",
                "gaps_expected": 6,
            }),

            ("video", {"title": "What is she like?", "url": "", "provider": "youtube"}),
            ("task", {
                "title": "What is she like?",
                "needs_review": True,
                "html": "<p>Посмотри видео и запиши как можно больше слов, которые помогут рассказать о "
                        "характере.</p>",
            }),

            ("sort", {"title": "Распредели слова по двум колонкам: Good или Bad", "groups": [
                {"name": "Good", "items": [{"text": t} for t in
                                           ["cheerful", "hardworking", "famous", "nice", "funny",
                                            "lovely", "helpful"]]},
                {"name": "Bad", "items": [{"text": t} for t in ["rude", "lazy", "shy"]]},
            ]}),

            # в выгрузке рядом картинка с Минни Маус — её не берём, текст оставили
            ("text", {"html":
                "<p><b>Нам предстоит подготовиться к сложному заданию — мы будем рассказывать о нашем "
                "любимом герое. Прочитай текст и ответь на вопросы.</b></p>"
                "<p><i>My favourite cartoon character is Minnie Mouse. She is a mouse and she can talk. "
                "I like Minnie because she is always nice to her friends. Minnie Mouse's best friends "
                "are Mickey Mouse, Pluto, Donald Duck and Goofy. Minnie likes to wear a bow in her hair, "
                "pretty dresses, white gloves and colourful shoes. Today, she has a pink bow in her "
                "hair. She is wearing a blue dress and pink shoes.</i></p>"}),
            ("task", {
                "title": "Запиши свои ответы на вопросы",
                "needs_review": True,
                "html": "<ol><li>What can Minnie Mouse do?</li><li>What is she like?</li>"
                        "<li>What does she like to wear?</li></ol>",
            }),

            ("speaking", {
                "title": "Мой любимый герой 🎤",
                "html": "<p>Мы уже умеем описывать любимых героев. Давай попробуем сделать это устно! "
                        "Вспомни своего любимого героя и скажи о нём 3–4 предложения.</p>"
                        "<p><b>Tell me about your favourite cartoon character.</b></p>",
                "needs_review": True,
            }),

            bye("<h3>Спасибо большое тебе за ответы! Ты молодец! 🎉</h3><p>До новых встреч!</p>",
                "well_done_medal"),
        ],
    },

    "u4_hw7": {
        **U4,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На следующем уроке тебя ожидает тест. Давай сегодня "
                  "постараемся к нему получше подготовиться!</p>", "hello_book"),

            # в выгрузке — фото клоуна; у нас сгенерированный Бонзо (Л4.6)
            ("gaps", {
                "title": "Вначале вспомним части тела. Впиши слова",
                "mode": "type",
                "image": u("clown_bonzo"),
                "text": "Look at Bonzo's face! He's got big __ears__, big brown __eyes__, a big red "
                        "__mouth__ and very white __teeth__. His __nose__ is red and he's got grey "
                        "__curly__ hair.",
                "gaps_expected": 6,
            }),

            ("gaps", {
                "title": "Подбери подходящую по смыслу фразу",
                "mode": "drag",
                "text": "A: I love golf and football. B: __You're sporty__.\n"
                        "A: I've got a lovely present for my best friend. B: __You're nice__.\n"
                        "A: I've got good marks at school. B: __You're clever__.\n"
                        "A: I help my brother with his homework. B: __You're helpful__.\n"
                        "A: I speak to everyone. B: __You're friendly__.\n"
                        "A: I tell good jokes. B: __You're funny__.",
                "gaps_expected": 6,
            }),

            ("gaps", {
                "title": "И-и-и… немножечко грамматики! Заполни пропуски",
                "mode": "drag",
                "text": "A: __Have__ you got wavy hair? B: __Yes__, I have.\n"
                        "A: __Has__ Maria __got__ long blond hair? B: No, she __hasn't__.\n"
                        "A: __Have__ you and Alex got blue eyes? B: Yes, we __have__.\n"
                        "A: __Have__ Jane and I got white teeth? B: No, you __haven't__.",
                "gaps_expected": 9,
            }),

            ("gaps", {
                "title": "Вспомним притяжательные прилагательные. Заполни пропуски",
                "mode": "drag",
                "image": u("card_possessives"),
                "text": "We've got wavy hair. __Our__ hair is wavy.\n"
                        "The dog has got short legs. __Its__ legs are short.\n"
                        "The students have got good marks. __Their__ marks are good.\n"
                        "Jack and I have got brown hair. __Our__ hair is brown.\n"
                        "You and Anna have got a nice brother. __Your__ brother is nice.",
                "gaps_expected": 5,
            }),

            ("text", {"html": pic(shared("well_done_trophy"), height=180)
                              + "<h3>Ну что же! Теперь ты готов к тесту на все 100% 🎉</h3>"}),

            # в выгрузке таблица — картинкой; у нас таблицей в тексте
            ("task", {
                "title": "Задание со звёздочкой ⭐",
                "needs_review": True,
                "html": "<p>Напиши о своей подруге Веронике, посмотрев на табличку ниже.</p>"
                        "<table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\">"
                        "<tr><td>Name</td><td>Veronica</td></tr>"
                        "<tr><td>Personality</td><td>helpful</td></tr>"
                        "<tr><td>Eyes</td><td>big, green</td></tr>"
                        "<tr><td>Hair</td><td>long, straight, brown</td></tr>"
                        "<tr><td>Bedroom ✓</td><td>a bed, a wardrobe, a desk, a chair</td></tr>"
                        "<tr><td>Bedroom ✗</td><td>a carpet, a television</td></tr>"
                        "</table>"
                        "<p><i>Начало: My friend's name is Veronica. She is helpful. She has got…</i></p>",
            }),

            # Wordwall «Match up · GG1 4.1 MATCH UP» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини ⭐", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in [U4_BODY[0], U4_BODY[3], U4_BODY[4], U4_BODY[8],
                                  U4_HAIR[1], U4_HAIR[4]]
            ]}),

            # Wordwall «True or false · 4.2 have got/has got» — СОСТАВ МОЙ
            ("truefalse", {"title": "Предложение написано правильно? Выбери верно или неверно ⭐",
                           "statements": [
                {"text": "She has got long hair.", "correct": True},
                {"text": "They has got a big house.", "correct": False},
                {"text": "I have got two sisters.", "correct": True},
                {"text": "My dog have got big ears.", "correct": False},
                {"text": "We haven't got a car.", "correct": True},
                {"text": "He haven't got a bike.", "correct": False},
            ]}),

            # Wordwall «Match up · GG1 4.3 Have *** got...?» — СОСТАВ МОЙ
            ("match", {"title": "Соедини вопрос и ответ ⭐", "pairs": [
                {"left": "Have you got a pet?", "right": "Yes, I have."},
                {"left": "Has she got blue eyes?", "right": "Yes, she has."},
                {"left": "Has he got curly hair?", "right": "No, he hasn't."},
                {"left": "Have they got a car?", "right": "No, they haven't."},
                {"left": "Has it got big ears?", "right": "Yes, it has."},
                {"left": "Have we got time?", "right": "Yes, we have."},
            ]}),

            bye("<h3>Ты отлично справился с заданиями, молодец! 🎉</h3><p>Удачи на тесте!</p>",
                "good_luck_clover"),
        ],
    },

    "u4_test": {
        **U4,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        "blocks": [
            # в выгрузке правая колонка пустая — картинки наши (Л4.3–Л4.5)
            ("match", {"title": "Соедини слова и картинки", "pairs": [
                {"left": "eyes", "right_image": u("body_eyes")},
                {"left": "fingers", "right_image": u("body_fingers")},
                {"left": "toes", "right_image": u("body_toes")},
                {"left": "spiky", "right_image": u("hair_spiky")},
                {"left": "teeth", "right_image": u("body_teeth")},
                {"left": "curly", "right_image": u("hair_curly")},
            ]}),

            # в выгрузке пропуск — буква, картинки — клипарт и два фото; у нас слово целиком
            # и дети Л4.1
            ("exact_input", {"title": "Посмотри на картинку и впиши слово целиком", "items": [
                {"prompt": hint, "accept": [en, en.capitalize()], "image": u("pers_" + en)}
                for hint, en in [("c_ev_r", "clever"), ("fr_endl_", "friendly"), ("f_n_y", "funny"),
                                 ("hel_ful", "helpful"), ("n_ce", "nice"), ("sp_rty", "sporty")]
            ]}),

            # в выгрузке «haves fgot», «thi is» — опечатки исправлены
            mcq("Прочитай диалоги и выбери пропущенные слова", [
                ("A: ___ your brother got big feet?", ["Has", "Have", "Haves"], "Has", u("body_feet")),
                ("A: Has your brother got big feet? B: No, he ___.", ["hasn't", "haven't", "has", "have"],
                 "hasn't"),
                ("A: ___ they got homework today?", ["Have", "Has", "Haves"], "Have", u("homework_diary")),
                ("A: Have they got homework today? B: Yes, they ___.", ["have", "has", "haven't", "hasn't"],
                 "have"),
                ("Jane ___ a cat, but she has got a rabbit.", ["hasn't got", "haven't got"], "hasn't got",
                 u("rabbit")),
                ("Jane hasn't got a cat, but she ___ got a rabbit.", ["has", "have", "haves"], "has"),
            ]),
            mcq("Выбери пропущенное слово", [
                ("This is Jane and this is ___ cat.", ["her", "their", "our"], "her"),
                ("We have a book. This is ___ book.", ["our", "their", "her"], "our"),
                ("They have a car. This is ___ car.", ["their", "our", "her"], "their"),
                ("My granny ___ curly hair.", ["has got", "have got", "haves got"], "has got",
                 u("granny_curly")),
                ("A: ___ you got an English class today?", ["Have", "Has", "Haves"], "Have",
                 u("english_class")),
                ("A: Have you got an English class today? B: No, but we ___ an Art class.",
                 ["have got", "got", "has got"], "have got"),
            ]),

            order("My best friend hasn't got a bike.", ["My", "best friend", "hasn't", "got", "a bike."],
                  title=ORDER, image=u("bike_yellow")),
            order("We've got a new English teacher.", ["We've", "got", "a new", "English", "teacher."],
                  title=ORDER, image=u("teacher_board")),
            # в выгрузке скейт с принтом Минни Маус — без картинки
            order("My parents haven't got a skateboard.", ["My", "parents", "haven't", "got", "a skateboard."],
                  title=ORDER),
            order("Juan has got blue eyes.", ["Juan", "has", "got", "blue", "eyes."],
                  title=ORDER, image=u("boy_cap")),
            # в выгрузке «Mt sisters» — исправлено
            order("My sisters have got blond hair.", ["My sisters", "have", "got", "blond", "hair."],
                  title=ORDER, image=u("sisters_blond")),

            ("gaps", {
                "title": "READING. Посмотри на картинку, прочитай описание и перетащи правильное слово "
                         "в каждый пропуск",
                "mode": "drag",
                "image": u("tom_lucy_rex"),
                "text": "This is my friend Tom. He's ten years old. Tom has got short, __blond__ hair. "
                        "He has got big blue __eyes__. He's tall and very __sporty__ — he plays football "
                        "every day. He's very __friendly__ and helpful. Tom has got a sister. Her name is "
                        "Lucy. She has got long, __curly__ hair. It's not straight. Lucy is very "
                        "__clever__ — she likes maths and she can read very well. Tom and Lucy have got a "
                        "dog. Its name is Rex. Rex has got big ears, a small __nose__ and four white feet. "
                        "He's a very __funny__ dog!",
                "gaps_expected": 8,
            }),

            listening("LISTENING. Послушай рассказ девочки о её младшей сестре Мие (Mia)."),
            mcq("LISTENING. Выбери правильный ответ", [
                ("How old is Mia?", ["6", "7", "8"], "7"),
                ("What kind of hair has Mia got?",
                 ["curly and blond", "straight and dark", "wavy and red"], "curly and blond"),
                ("What colour are her eyes?", ["blue", "brown", "green"], "green"),
                ("Mia is…", ["funny and friendly", "funny and clever", "clever and sporty"],
                 "funny and clever"),
                ("Has Mia got a pet?", ["Yes, she has a dog.", "Yes, she has a goldfish.", "No, she hasn't."],
                 "Yes, she has a goldfish."),
            ]),

            ("speaking", {
                "title": "SPEAKING TASK 🎤",
                "image": u("monsters_six"),
                "html": "<p>Посмотри на картинку, выбери монстра и опиши его. Запиши свой ответ, нажав "
                        "на кнопку микрофона 🙌</p>"
                        "<p><i>Пример: My favourite monster has got three eyes. He has got twenty teeth, "
                        "two legs and two arms.</i></p>",
                "needs_review": True,
            }),
        ],
    },
}
