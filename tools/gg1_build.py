#!/usr/bin/env python3
"""Сборка уроков Go Getter 1: блоки → SQL, с проверкой до заливки.

Копия tools/sm3_build.py для GG1 (общий сборщик не дорабатываем — курсы живут
отдельно). Уроки описываются питоновскими структурами ниже, скрипт собирает из
них миграцию и сам проверяет payload по списку из CLAUDE.md: правильный
вариант указывает на задуманный, нет дублей в вариантах, правые значения match
уникальны, склейка order совпадает с предложением, число пропусков в gaps
совпадает с задуманным, каждая ссылка на картинку есть в media/.

  python3 tools/gg1_build.py --list                   все уроки и что не готово
  python3 tools/gg1_build.py --lesson u0_hw1          проверить и показать SQL
  python3 tools/gg1_build.py --lesson u0_hw1 --sql migrations/gg1_u0_hw1.sql
  python3 tools/gg1_build.py --lesson u0_hw1 --chunks <lesson_id> --per-chunk 7

Выгрузка — ShkolaApp (docs/GG1_выгрузка_файлы.md). Игры Wordwall пересобраны
штатными блоками: в заголовке у таких блоков нет пометки, она стоит в
комментарии «СОСТАВ МОЙ» и строкой в docs/GG1_доработать_руками.md.
"""
import argparse, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = "@@MEDIA@@"
MEDIA_URL = "https://classroom.wowteach.ru/media/"
COURSE = "Go Getter 1"


def img(unit, name):
    return f"{MEDIA}gg1/{unit}/{name}.webp"


def colour(name):
    """Кляксы цветов рисует tools/gg1_colours.py — svg, а не генератор."""
    return f"{MEDIA}gg1/u0/colour_{name}.svg"


def shared(name):
    return f"{MEDIA}shared/{name}.webp"


def pic(src, alt="", height=None):
    style = f"height:{height}px" if height else "max-width:100%"
    return f'<p><img src="{src}" alt="{alt}" style="{style}"></p>'


# Все словари, по которым строятся вопросы «как по-английски», — сюда же
# смотрит проверка: correct должен указывать на английскую пару русского слова.
VOCAB = []


def vocab(rows):
    VOCAB.extend(rows)
    return rows


def quiz_ru_to_en(words, per_question=4, title=None):
    """Вопросы «как по-английски».

    Отвлекающие берём по кругу от самого слова, а не первые из списка: иначе
    во всех вопросах стоят одни и те же три варианта, и правильный вычисляется
    исключением, не читая вопроса. Варианты по алфавиту — позиция верного
    ответа от вопроса к вопросу меняется сама.
    """
    qs = []
    n = len(words)
    for i, (en, ru, _) in enumerate(words):
        wrong = [words[(i + k) % n][0] for k in range(1, per_question)]
        options = sorted([en] + wrong, key=str.lower)
        qs.append({
            "q": f"Как по-английски «{ru}»?",
            "type": "single",
            "options": [{"text": o} for o in options],
            "correct": [options.index(en)],
        })
    out = {"questions": qs}
    if title:
        out = {"title": title, **out}
    return out


def choose(title, items):
    """«Выбери правильный вариант» отдельного типа у нас нет — quiz по вопросу
    на пропуск. items: (предложение с ___, [варианты], верный)."""
    return ("quiz", {"title": title, "questions": [
        {"q": q, "type": "single", "options": [{"text": o} for o in opts],
         "correct": [opts.index(ok)]}
        for q, opts, ok in items]})


def order(sentence, words=None):
    words = words or sentence.split(" ")
    return ("order", {"words": words, "sentence": sentence, "audio_tts": sentence})


def hello(html, picture="hello_wave"):
    return ("text", {"html": pic(shared(picture), height=200) + html})


def bye(html="<h3>Поздравляю! Ты завершил домашнее задание, ты замечательный ученик! 🎉</h3>"
             "<p>Увидимся на занятии!</p>", picture="well_done_trophy"):
    return ("text", {"html": pic(shared(picture), height=180) + html})


# ---------- словари ----------

U0_COLOURS = vocab([
    ("black", "чёрный", "black"),
    ("blue", "синий", "blue"),
    ("brown", "коричневый", "brown"),
    ("green", "зелёный", "green"),
    ("grey", "серый", "grey"),
    ("orange", "оранжевый", "orange"),
    ("pink", "розовый", "pink"),
    ("purple", "фиолетовый", "purple"),
    ("red", "красный", "red"),
    ("white", "белый", "white"),
    ("yellow", "жёлтый", "yellow"),
])

# Словарь Homework 3 (1) — 13 слов. Картинки: листы Л0.1 и Л0.2.
U0_CLASSROOM = vocab([
    ("bin", "мусорное ведро", "obj_bin"),
    ("board", "доска", "obj_board"),
    ("chair", "стул", "obj_chair"),
    ("clock", "часы", "obj_clock"),
    ("desk", "парта", "obj_desk"),
    ("coloured pencil", "цветной карандаш", "obj_coloured_pencil"),
    ("notebook", "тетрадь", "obj_notebook"),
    ("pen", "ручка", "obj_pen"),
    ("sharpener", "точилка", "obj_sharpener"),
    ("rubber", "ластик", "obj_rubber"),
    ("ruler", "линейка", "obj_ruler"),
    ("scissors", "ножницы", "obj_scissors"),
    ("pencil case", "пенал", "obj_pencil_case"),
])

U0_NUMBERS = [
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
    "Eighteen", "Nineteen", "Twenty",
]
U0_NUMBERS_ASKED = {1, 4, 7, 10, 13, 15, 18, 20}     # пустые окошки в выгрузке

U0 = {"unit": "u0", "unit_title": "Unit 0 · Get started!", "unit_sort": 0}


LESSONS = {
    "u0_hw1": {
        **U0,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        "blocks": [
            hello("<h2>Добро пожаловать! 👋</h2>"
                  "<p>Сегодня тебя ждёт много интересных упражнений!</p>"
                  "<p>В конце тебя будет ждать дополнительное задание. Если ты его сделаешь, "
                  "получишь дополнительную звёздочку! ⭐</p>"
                  "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"
                  + pic(img("u0", "card_greetings"), "Greetings & Introductions")),

            # в выгрузке «Медиафайл» пустой — видео с алфавитом вставит методист
            ("video", {"title": "Для начала посмотри видео! Обязательно повторяй буквы из видео, "
                                "постарайся запомнить — так ты быстрее выучишь алфавит!",
                       "url": "", "provider": "youtube"}),

            ("match", {
                "title": "Супер! А теперь помоги растерявшимся буковкам найти продолжения, "
                         "чтобы получились слова — у тебя получится!",
                "pairs": [
                    {"left": "c", "right": "upcake"},
                    {"left": "m", "right": "usic"},
                    {"left": "s", "right": "port"},
                    {"left": "a", "right": "pple"},
                    {"left": "h", "right": "obby"},
                    {"left": "n", "right": "ame"},
                ],
            }),

            ("sequence", {
                "title": "Отлично, а теперь задание посложнее. Мы только что составили слова — "
                         "расставь их в алфавитном порядке ;)",
                "items": [{"text": w, "audio_tts": w}
                          for w in ["apple", "cupcake", "hobby", "music", "name", "sport"]],
            }),

            # «Составь предложение» ×4: вопросы, которые могут задать новые друзья
            order("What's your name?"),
            order("How old are you?"),
            order("Where are you from?"),
            order("What is your hobby?"),

            ("speaking", {
                "title": "Расскажи о себе 🎤",
                "html": "<p>Прекрасная работа! Запиши небольшой рассказ на английском о себе, "
                        "воспользуйся шаблоном:</p>"
                        "<p><i>My name is…<br>I'm … years old.<br>I'm from…<br>My hobby is…</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Match up · gg1 0.1» — СОСТАВ МОЙ
            ("match", {
                "title": "Ты выполнил все задания из основной части! А это дополнительное "
                         "задание — для настоящих чемпионов! Соедини вопросы с ответами ⭐",
                "pairs": [
                    {"left": "What's your name?", "right": "My name's Tom."},
                    {"left": "How old are you?", "right": "I'm ten."},
                    {"left": "Where are you from?", "right": "I'm from Poland."},
                    {"left": "What is your hobby?", "right": "My hobby is football."},
                    {"left": "How do you spell that?", "right": "T-O-M."},
                    {"left": "Nice to meet you!", "right": "Nice to meet you too!"},
                ],
            }),

            # Wordwall «Unjumble · GG1 0.1» — СОСТАВ МОЙ
            ("order", {
                "title": "Расставь в правильном порядке ⭐",
                "words": ["Hello!", "My", "name's", "Anna.", "Nice", "to", "meet", "you!"],
                "sentence": "Hello! My name's Anna. Nice to meet you!",
                "audio_tts": "Hello! My name's Anna. Nice to meet you!",
            }),

            bye(),
        ],
    },

    # Homework 2 (1) — словарный тренажёр «цвета», (2) — задания. Один урок.
    "u0_hw2": {
        **U0,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        "blocks": [
            hello("<h2>Привет! 👋</h2>"
                  "<p>Сейчас мы с тобой повторим цвета. Выполни все задания, чтобы выучить "
                  "слова на 100%!</p>"
                  + pic(img("u0", "card_colours"), "Colours"), "hello_book"),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": colour(c)}
                for en, ru, c in U0_COLOURS
            ]}),

            ("match", {"title": "Соедини цвет и слово", "pairs": [
                {"left_image": colour(c), "right": en, "right_audio_tts": en}
                for en, ru, c in U0_COLOURS
            ]}),

            ("quiz", quiz_ru_to_en(U0_COLOURS)),

            ("exact_input", {"items": [
                {"prompt": f"Напиши по-английски: {ru}", "accept": [en, en.capitalize()],
                 "image": colour(c), "audio_tts": en}
                for en, ru, c in U0_COLOURS
            ]}),

            # перемычка: прощание первой части + приветствие второй
            ("text", {"html":
                "<h3>Цвета выучены! 🎨</h3>"
                "<p>Добро пожаловать во вторую часть домашнего задания! Тебя ждёт много "
                "интересных упражнений, а в конце — дополнительное задание: сделаешь его — "
                "получишь звёздочку! ⭐</p>"
                + pic(img("u0", "card_numbers"), "Numbers 1–100")}),

            ("text", {"html":
                "<p>Ты уже справился с несколькими заданиями! Посмотри на картинку — "
                "в следующем задании она понадобится.</p>"
                + pic(img("u0", "scene_zoo_colours"), "Zoo painting")}),

            ("match", {
                "title": "Посмотри на картинку и соедини начало и конец предложений по смыслу. "
                         "У тебя получится!",
                "pairs": [
                    {"left": "The elephants are", "right": "grey."},
                    {"left": "The zebras are", "right": "black and white."},
                    {"left": "The sky is", "right": "blue."},
                    {"left": "The oranges are", "right": "orange."},
                    {"left": "The lemons are", "right": "yellow."},
                    {"left": "The trees are", "right": "green."},
                    {"left": "The flamingoes are", "right": "pink."},
                    {"left": "The flowers are", "right": "red."},
                ],
            }),

            # «Медиафайл» пустой — видео с числами вставит методист
            ("video", {"title": "А теперь посмотри видео! Обязательно повторяй цифры и числа, "
                                "постарайся запомнить — они тебе очень пригодятся!",
                       "url": "", "provider": "youtube"}),

            ("gaps", {
                "title": "Прекрасная работа! Напиши числа словами в окошки",
                "mode": "type",
                "text": "\n".join(
                    f"{n} = __{w}|{w.lower()}__" if n in U0_NUMBERS_ASKED else f"{n} = {w}"
                    for n, w in enumerate(U0_NUMBERS, start=1)),
                "gaps_expected": len(U0_NUMBERS_ASKED),
            }),

            ("speaking", {
                "title": "Опиши картинку 🎤",
                "image": img("u0", "scene_zoo_colours"),
                "html": "<p>Опиши, что видишь на картинке. Нажми на микрофон и составь "
                        "3–4 предложения.</p><p><i>Пример: The lemons are yellow.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Find the match · GG1 Numbers 0.2» — СОСТАВ МОЙ.
            # Отвлекающие — пары -teen/-ty, на них показывает карточка методиста.
            choose("Ты выполнил все задания из основной части! А это дополнительное задание — "
                   "для настоящих чемпионов! Выбери подходящую цифру ⭐", [
                ("thirteen", ["3", "13", "30"], "13"),
                ("fifty", ["15", "5", "50"], "50"),
                ("twelve", ["12", "20", "2"], "12"),
                ("forty", ["14", "40", "4"], "40"),
                ("eighteen", ["80", "8", "18"], "18"),
                ("a hundred", ["10", "1000", "100"], "100"),
            ]),

            # Wordwall «Labelled diagram · GG1 0.2 Colors» — СОСТАВ МОЙ: та же картина,
            # что в задании выше, метки — цвета.
            ("hotspot", {
                "title": "Соедини: перетащи название цвета на картинку ⭐",
                "mode": "label",
                "image": img("u0", "scene_zoo_colours"),
                "points": [
                    {"x": 33.0, "y": 55.0, "text": "grey", "audio_tts": "grey"},
                    {"x": 57.0, "y": 40.0, "text": "pink", "audio_tts": "pink"},
                    {"x": 72.0, "y": 70.0, "text": "black and white", "audio_tts": "black and white"},
                    {"x": 47.0, "y": 80.0, "text": "red", "audio_tts": "red"},
                    {"x": 13.0, "y": 37.0, "text": "orange", "audio_tts": "orange"},
                    {"x": 88.0, "y": 50.0, "text": "yellow", "audio_tts": "yellow"},
                    {"x": 62.0, "y": 11.0, "text": "blue", "audio_tts": "blue"},
                    {"x": 77.0, "y": 22.0, "text": "green", "audio_tts": "green"},
                ],
                "extras": [],
            }),

            bye(),
        ],
    },

    # Homework 3 (1) — словарный тренажёр «школьные вещи», (2) — задания. Один урок.
    "u0_hw3": {
        **U0,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        "blocks": [
            hello("<h2>Привет! 👋</h2>"
                  "<p>Сейчас мы с тобой выучим новые слова — школьные принадлежности. "
                  "Выполни все задания, чтобы выучить слова на 100%!</p>"
                  + pic(img("u0", "card_in_my_bag"), "In my bag + Classroom objects"),
                  "hello_laptop"),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": img("u0", f)}
                for en, ru, f in U0_CLASSROOM
            ]}),

            ("match", {"title": "Соедини картинку и слово", "pairs": [
                {"left_image": img("u0", f), "right": en, "right_audio_tts": en}
                for en, ru, f in U0_CLASSROOM[:7]
            ]}),

            ("match", {"title": "И ещё раз — соедини картинку и слово", "pairs": [
                {"left_image": img("u0", f), "right": en, "right_audio_tts": en}
                for en, ru, f in U0_CLASSROOM[7:]
            ]}),

            ("quiz", quiz_ru_to_en(U0_CLASSROOM)),

            ("text", {"html":
                "<h3>Слова выучены! ✏️</h3>"
                "<p>Добро пожаловать во вторую часть домашнего задания! В конце тебя будет "
                "ждать дополнительное задание: сделаешь его — получишь звёздочку! ⭐</p>"}),

            # «Медиафайл» пустой — видео про множественное число вставит методист
            ("video", {"title": "А теперь посмотри видео! Повторяй слова и внимательно следи "
                                "за окончаниями — как образуют множественное число разные слова.",
                       "url": "", "provider": "youtube"}),

            ("sort", {
                "title": "Класс! Посмотри видео ещё раз и распредели слова по колонкам: "
                         "к каким словам нужно добавить s, а к каким es?",
                "groups": [
                    {"name": "+s", "items": [{"text": w} for w in
                                             ["apple", "pencil", "notebook", "egg"]]},
                    {"name": "+es", "items": [{"text": w} for w in
                                              ["box", "sandwich", "bus", "brush"]]},
                ],
            }),

            ("text", {"html":
                "<p>Супер, двигаемся дальше! Давай вспомним правило про артикли <b>a</b> и "
                "<b>an</b>. Внимательно посмотри на зелёную рамочку, а затем выполни "
                "упражнение — ты сможешь!</p>"
                + pic(img("u0", "look_a_an"), "a book, a pencil, an apple, an umbrella")
                + pic(img("u0", "card_a_an"), "a / an")}),

            choose("Выбери правильный вариант: a или an?", [
                ("1. ___ apple", ["a", "an"], "an"),
                ("2. ___ pencil", ["a", "an"], "a"),
                ("3. ___ sandwich", ["a", "an"], "a"),
                ("4. ___ notebook", ["a", "an"], "a"),
                ("5. ___ egg", ["a", "an"], "an"),
                ("6. ___ box", ["a", "an"], "a"),
            ]),

            ("hotspot", {
                "title": "Эти слова тебе уже знакомы — давай быстренько соединим слова с "
                         "картинками! Сможешь? ;)",
                "mode": "label",
                "image": img("u0", "diagram_classroom"),
                "points": [
                    {"x": 25.0, "y": 27.0, "text": "bin", "audio_tts": "bin"},
                    {"x": 68.0, "y": 25.0, "text": "board", "audio_tts": "board"},
                    {"x": 13.0, "y": 72.0, "text": "chair", "audio_tts": "chair"},
                    {"x": 46.0, "y": 76.0, "text": "clock", "audio_tts": "clock"},
                    {"x": 83.0, "y": 70.0, "text": "desk", "audio_tts": "desk"},
                ],
                "extras": [],
            }),

            ("text", {"html":
                "<p>А теперь соберём всё вместе — внимательно посмотри на зелёную рамочку, "
                "а затем выполни упражнение. Ты сможешь!</p>"
                + pic(img("u0", "look_its_theyre"), "It's a pencil. They're pencils.")}),

            choose("Выбери правильный вариант: It's или They're? Пример: It's a bin.", [
                ("1. ___ clocks.", ["It's", "They're"], "They're"),
                ("2. ___ a board.", ["It's", "They're"], "It's"),
                ("3. ___ a desk.", ["It's", "They're"], "It's"),
                ("4. ___ chairs.", ["It's", "They're"], "They're"),
                ("5. ___ bins.", ["It's", "They're"], "They're"),
            ]),

            ("text", {"html":
                "<p>Давай вспомним, какие фразы нам могут пригодиться на уроке.</p>"
                + pic(img("u0", "card_classroom_language"), "Classroom language")}),

            ("match", {
                "title": "Поработаешь немного переводчиком? Соедини фразы на английском "
                         "с переводом",
                "pairs": [
                    {"left": "Close your books.", "right": "Закройте книги."},
                    {"left": "Open your books.", "right": "Откройте книги."},
                    {"left": "Look (at the photo).", "right": "Посмотрите (на фото)."},
                    {"left": "Listen (to the story).", "right": "Послушайте (историю)."},
                    {"left": "Read (the text).", "right": "Прочитайте (текст)."},
                    {"left": "Write (your name).", "right": "Напишите (своё имя)."},
                    {"left": "Can you help me?", "right": "Можете мне помочь?"},
                    {"left": "Can you repeat?", "right": "Можете повторить?"},
                    {"left": "I'm ready.", "right": "Я готов."},
                    {"left": "What is … in English?", "right": "Как будет … по-английски?"},
                ],
            }),

            ("task", {
                "title": "Что в твоём рюкзаке? 🎒",
                "needs_review": True,
                "html": "<p>Прекрасная работа! Напиши список того, что есть в твоём школьном "
                        "рюкзаке.</p><p><i>Например: a pen, a notebook, two pencils…</i></p>",
            }),

            # Wordwall «Выбери подходящее слово» — обложка пустая, СОСТАВ МОЙ
            ("quiz", {
                "title": "Ты выполнил все задания из основной части! А это дополнительное "
                         "задание — для настоящих чемпионов! Выбери подходящее слово ⭐",
                "questions": [
                    {"q": "What's this?", "image": img("u0", "obj_book"), "type": "single",
                     "options": [{"text": "a book"}, {"text": "a bag"}, {"text": "a board"}],
                     "correct": [0]},
                    {"q": "What's this?", "image": img("u0", "obj_pencil"), "type": "single",
                     "options": [{"text": "a pen"}, {"text": "a pencil case"}, {"text": "a pencil"}],
                     "correct": [2]},
                    {"q": "What's this?", "image": img("u0", "obj_sandwich"), "type": "single",
                     "options": [{"text": "a ruler"}, {"text": "a sandwich"}, {"text": "a sharpener"}],
                     "correct": [1]},
                    {"q": "What's this?", "image": img("u0", "obj_apple"), "type": "single",
                     "options": [{"text": "a apple"}, {"text": "an apple"}],
                     "correct": [1]},
                    {"q": "What's this?", "image": img("u0", "obj_bag"), "type": "single",
                     "options": [{"text": "a bag"}, {"text": "a bin"}, {"text": "a book"}],
                     "correct": [0]},
                ],
            }),

            # Wordwall «Соедини слова с картинками» — обложка пустая, СОСТАВ МОЙ
            ("match", {"title": "Соедини слова с картинками ⭐", "pairs": [
                {"left_image": img("u0", f), "right": en, "right_audio_tts": en}
                for en, f in [("scissors", "obj_scissors"), ("ruler", "obj_ruler"),
                              ("rubber", "obj_rubber"), ("clock", "obj_clock"),
                              ("desk", "obj_desk"), ("notebook", "obj_notebook")]
            ]}),

            bye(),
        ],
    },

    "u0_test": {
        **U0,
        "lesson_title": "Test",
        "lesson_sort": 3,
        "kind": "test",
        "blocks": [
            ("exact_input", {"title": "Впиши недостающие буквы", "items": [
                {"prompt": p, "accept": [w], "image": im, "audio_tts": w}
                for p, w, im in [
                    ("b _ _ k", "book", img("u0", "obj_book")),
                    ("p _ n", "pen", img("u0", "obj_pen")),
                    ("b _ g", "bag", img("u0", "obj_bag")),
                    ("ch _ _ r", "chair", img("u0", "obj_chair")),
                    ("r _ d", "red", colour("red")),
                    ("bl _ _", "blue", colour("blue")),
                ]]}),

            choose("Вставь правильное слово", [
                ("1. This is ___ pen.", ["a", "an"], "a"),
                ("2. This is ___ orange bag.", ["a", "an"], "an"),
                ("3. These are ___.", ["book", "books"], "books"),
                ("4. I have a pencil case. This is ___ pencil case.", ["your", "my"], "my"),
                ("5. You have a bag. Is this ___ bag?", ["my", "your"], "your"),
            ]),

            order("This is my bag."),
            order("I have a pen."),
            order("These are my books."),
            order("Is this your pencil?"),
            order("This is an orange ruler."),

            ("text", {"html":
                "<h3>READING</h3>"
                "<p>Прочитай короткие представления.</p>"
                "<p>Hi! I'm Anna. My pen is red.<br>"
                "Hello! My name's Tom. My bag is blue.<br>"
                "I'm Olivia. My ruler is yellow.<br>"
                "Hello! I'm Daniel. My notebook is green.<br>"
                "Hi! My name's Sophie. My pencil case is pink.</p>"}),

            ("match", {"title": "Соедини имя человека с его предметом", "pairs": [
                {"left": "Anna", "right_image": img("u0", "col_red_pen")},
                {"left": "Tom", "right_image": img("u0", "col_blue_bag")},
                {"left": "Olivia", "right_image": img("u0", "col_yellow_ruler")},
                {"left": "Daniel", "right_image": img("u0", "col_green_notebook")},
                {"left": "Sophie", "right_image": img("u0", "col_pink_pencil_case")},
            ]}),

            # аудио учителя в выгрузке нет — строка в docs/GG1_доработать_руками.md
            ("gaps", {
                "title": "LISTENING. Прослушай учителя на аудио и впиши пропущенное слово "
                         "(число или цвет)",
                "mode": "type",
                "audio": "",
                "text": "1. Open your book. Page __forty|40__.\n"
                        "2. Look at picture __twelve|12__.\n"
                        "3. The new pencil case is __purple__.\n"
                        "4. There are __twenty|20__ chairs in the classroom.\n"
                        "5. The teacher's bag is __brown__.",
                "gaps_expected": 5,
            }),

            ("speaking", {
                "title": "SPEAKING 🎤",
                "image": img("u0", "test_classroom"),
                "html": "<p>Внимательно посмотри на картинку. Нажми на микрофон и ответь на "
                        "вопросы.</p><ol><li>What can you see?</li><li>What colour is the bag?</li>"
                        "<li>What is on the desks?</li><li>How many books can you see?</li>"
                        "<li>What is your favourite colour?</li></ol>",
                "needs_review": True,
            }),
        ],
    },
}


# ---------- проверка ----------

def check(lesson, errors):
    for i, (btype, payload) in enumerate(lesson["blocks"], start=1):
        where = f"блок {i} ({btype})"

        if btype == "quiz":
            for n, q in enumerate(payload["questions"], start=1):
                # вариант бывает картинкой, а не текстом — сравниваем по тому,
                # что в нём есть, иначе проверка на дубли падает на картинках
                texts = [o.get("text", o.get("image", "")) for o in q["options"]]
                if len(set(texts)) != len(texts):
                    errors.append(f"{where}, вопрос {n}: повторяются варианты")
                for c in q["correct"]:
                    if not 0 <= c < len(texts):
                        errors.append(f"{where}, вопрос {n}: correct вне списка вариантов")
                # правильный вариант должен быть именно английским словом из пары
                ru = re.search(r"«(.+?)»", q["q"])
                if ru:
                    want = next((en for en, r, _ in VOCAB if r == ru.group(1)), None)
                    if want and texts[q["correct"][0]] != want:
                        errors.append(f"{where}, вопрос {n}: correct указывает на «{texts[q['correct'][0]]}», "
                                      f"а ждём «{want}»")

        if btype == "match":
            rights = [p.get("right", p.get("right_image")) for p in payload["pairs"]]
            if len(set(rights)) != len(rights):
                errors.append(f"{where}: правые значения повторяются — такой блок надо делать quiz")

        if btype == "order":
            glued = " ".join(payload["words"])
            if glued != payload["sentence"]:
                errors.append(f"{where}: склейка слов «{glued}» не совпадает с предложением "
                              f"«{payload['sentence']}»")

        if btype == "gaps":
            found = len(re.findall(r"__[^_]+__", payload["text"]))
            want = payload.get("gaps_expected")
            if want is not None and found != want:
                errors.append(f"{where}: пропусков {found}, а задумано {want}")

        if btype == "exact_input":
            for it in payload["items"]:
                if not it["accept"]:
                    errors.append(f"{where}: пустой список accept")

    # ссылки на картинки
    for i, (btype, payload) in enumerate(lesson["blocks"], start=1):
        for link in re.findall(r"@@MEDIA@@([^\"'\\\s)<]+)", json.dumps(payload, ensure_ascii=False)):
            path = os.path.join(ROOT, "media", link)
            if not os.path.exists(path):
                errors.append(f"блок {i} ({btype}): нет файла media/{link}")


# ---------- SQL ----------

def sql_for(key, lesson):
    out = [
        f"-- {COURSE} · " + lesson["unit_title"] + " · " + lesson["lesson_title"],
        "-- собрано tools/gg1_build.py --lesson " + key,
        "do $mig$",
        "declare",
        "  v_course uuid;",
        "  v_unit   uuid;",
        "  v_lesson uuid;",
        "  v_media  text := 'https://classroom.wowteach.ru/media/';",
        "begin",
        f"  select id into v_course from classroom_courses where title = '{COURSE}';",
        "",
        "  insert into classroom_units (course_id, title, sort_order)",
        f"  select v_course, '{lesson['unit_title']}', {lesson['unit_sort']}",
        "  where not exists (select 1 from classroom_units",
        f"                    where course_id = v_course and title = '{lesson['unit_title']}');",
        f"  select id into v_unit from classroom_units",
        f"   where course_id = v_course and title = '{lesson['unit_title']}';",
        "",
        "  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)",
        f"  select v_unit, '{lesson['lesson_title']}', '{lesson['kind']}',",
        f"         {90 if lesson['kind'] == 'test' else 60}, false, {lesson['lesson_sort']}",
        "  where not exists (select 1 from classroom_lessons",
        f"                    where unit_id = v_unit and title = '{lesson['lesson_title']}');",
        f"  select id into v_lesson from classroom_lessons",
        f"   where unit_id = v_unit and title = '{lesson['lesson_title']}';",
        "",
        "  delete from classroom_blocks where lesson_id = v_lesson;",
        "",
        "  insert into classroom_blocks (lesson_id, type, payload, sort_order) values",
    ]
    rows = []
    for n, (btype, payload) in enumerate(lesson["blocks"]):
        clean = {k: v for k, v in payload.items() if k != "gaps_expected"}
        js = json.dumps(clean, ensure_ascii=False)
        rows.append(f"    (v_lesson, '{btype}', replace($blk${js}$blk$, '@@MEDIA@@', v_media)::jsonb, {n})")
    out.append(",\n".join(rows) + ";")
    out += ["end", "$mig$;"]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lesson")
    ap.add_argument("--list", action="store_true", help="все уроки и что в них не готово")
    ap.add_argument("--sql", help="записать SQL в файл")
    ap.add_argument("--chunks", metavar="LESSON_ID",
                    help="печатать вставки блоков кусками, готовыми для execute_sql "
                         "(длинный do-блок отваливается по таймауту)")
    ap.add_argument("--per-chunk", type=int, default=3)
    args = ap.parse_args()

    if args.list:
        for key, lesson in LESSONS.items():
            errors = []
            check(lesson, errors)
            state = "готов" if not errors else f"{len(errors)} замечаний"
            print(f"{key:<10} {lesson['unit_title']} · {lesson['lesson_title']:<11} "
                  f"{len(lesson['blocks']):>2} блоков · {state}")
            for e in errors:
                print("     ·", e)
        return
    if not args.lesson:
        ap.error("нужен --lesson или --list")

    lesson = LESSONS[args.lesson]
    errors = []
    check(lesson, errors)
    if errors:
        print("Проверка не прошла:", file=sys.stderr)
        for e in errors:
            print("  ·", e, file=sys.stderr)
        sys.exit(1)

    print(f"Проверка пройдена: {len(lesson['blocks'])} блоков, "
          f"типы: {', '.join(t for t, _ in lesson['blocks'])}", file=sys.stderr)
    if args.chunks:
        rows = []
        for n, (btype, payload) in enumerate(lesson["blocks"]):
            clean = {k: v for k, v in payload.items() if k != "gaps_expected"}
            js = json.dumps(clean, ensure_ascii=False)
            rows.append(f"('{args.chunks}', '{btype}', replace($blk${js}$blk$, "
                        f"'@@MEDIA@@', '{MEDIA_URL}')::jsonb, {n})")
        for i in range(0, len(rows), args.per_chunk):
            print("-- кусок", i // args.per_chunk + 1)
            print("insert into classroom_blocks (lesson_id, type, payload, sort_order) values")
            print(",\n".join(rows[i:i + args.per_chunk]))
            print("returning sort_order, type;\n")
        return

    sql = sql_for(args.lesson, lesson)
    if args.sql:
        with open(args.sql, "w", encoding="utf-8") as f:
            f.write(sql + "\n")
        print("SQL записан в", args.sql, file=sys.stderr)
    else:
        print(sql)


if __name__ == "__main__":
    main()
