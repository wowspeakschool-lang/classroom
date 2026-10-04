#!/usr/bin/env python3
"""Сборка уроков Super Minds 3: блоки → SQL, с проверкой до заливки.

Уроки описываются питоновскими структурами ниже, скрипт собирает из них
миграцию и сам проверяет payload по списку из CLAUDE.md: правильный вариант
указывает на задуманный, нет дублей в вариантах, правые значения match
уникальны, склейка order совпадает с предложением, число пропусков в gaps
совпадает с задуманным, каждая ссылка на картинку есть в media/.

  python3 tools/sm3_build.py --lesson u1_hw1          проверить и показать SQL
  python3 tools/sm3_build.py --lesson u1_hw1 --sql файл.sql
"""
import argparse, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = "@@MEDIA@@"
MEDIA_URL = "https://classroom.wowteach.ru/media/"

SUBJECTS = [
    ("English", "английский", "subj_english"),
    ("Maths", "математика", "subj_maths"),
    ("Geography", "география", "subj_geography"),
    ("I.T.", "информационные технологии", "subj_it"),
    ("Music", "музыка", "subj_music"),
    ("Science", "наука", "subj_science"),
    ("Art", "изобразительное искусство", "subj_art"),
    ("P.E.", "физкультура", "subj_pe"),
    ("History", "история", "subj_history"),
]


U2_FOOD = [
    ("apple juice", "яблочный сок", "food_apple_juice"),
    ("rolls", "булочки", "food_bread_rolls"),
    ("cheese", "сыр", "food_cheese"),
    ("water", "вода", "food_water"),
    ("soup", "суп", "food_soup"),
    ("vegetables", "овощи", "food_vegetables"),
    ("lemonade", "лимонад", "food_lemonade"),
    ("salad", "салат", "food_salad"),
]


U3_CHORES = [
    ("tidy up", "убираться", "chore_tidy_up"),
    ("do the shopping", "ходить за покупками", "chore_do_shopping"),
    ("take the dog for a walk", "выгуливать собаку", "chore_walk_dog"),
    ("wash up", "мыть посуду", "chore_wash_up"),
    ("sweep", "подметать", "chore_sweep"),
    ("cook", "готовить", "chore_cook"),
    ("dry the dishes", "вытирать посуду", "chore_dry_dishes"),
    ("feed the dog", "кормить собаку", "chore_feed_dog"),
]


U3_DAYS = [
    ("Monday", "понедельник"),
    ("Tuesday", "вторник"),
    ("Wednesday", "среда"),
    ("Thursday", "четверг"),
    ("Friday", "пятница"),
    ("Saturday", "суббота"),
    ("Sunday", "воскресенье"),
]


U3_JOBS = [
    ("firefighter", "пожарный", "job_firefighter"),
    ("cleaner", "уборщик", "job_cleaner"),
    ("vet", "ветеринар", "job_vet"),
    ("police officer", "полицейский", "job_police"),
    ("teacher", "учитель", "job_teacher"),
    ("security guard", "охранник", "job_security"),
    ("ambulance driver", "водитель скорой помощи", "job_ambulance_driver"),
    ("shopkeeper", "продавец", "job_shopkeeper"),
    ("nurse", "медсестра", "job_nurse"),
]


U4_TOWN = [
    ("bank", "банк", "town_bank"),
    ("tower", "башня", "town_tower"),
    ("map", "карта", "town_map"),
    ("library", "библиотека", "town_library"),
    ("market square", "торговая площадь", "town_market"),
    ("supermarket", "супермаркет", "town_supermarket"),
    ("bus station", "автобусная остановка", "town_bus_station"),
    ("sports centre", "спортивный центр", "town_sports_centre"),
    ("car park", "парковка", "town_car_park"),
    ("funfair", "парк с аттракционами", "town_funfair"),
    ("go straight", "идти прямо", "arrow_straight"),
    ("turn left", "повернуть налево", "arrow_left"),
    ("turn right", "повернуть направо", "arrow_right"),
]


U5_SEA = [
    ("seal", "тюлень", "sea_seal"),
    ("dolphin", "дельфин", "sea_dolphin"),
    ("anchor", "якорь", "sea_anchor"),
    ("turtle", "черепаха", "sea_turtle"),
    ("shell", "ракушка", "sea_shell"),
    ("octopus", "осьминог", "sea_octopus"),
    ("seahorse", "морской конёк", "sea_seahorse"),
    ("starfish", "морская звезда", "sea_starfish"),
    ("jellyfish", "медуза", "sea_jellyfish"),
    ("to dive", "нырять", "sea_diving_gear"),
]


U6_GADGETS = [
    ("mobile phone", "мобильный телефон", "gad_phone"),
    ("tablet", "планшет", "gad_tablet"),
    ("laptop", "ноутбук", "gad_laptop"),
    ("torch", "фонарик", "gad_torch"),
    ("walkie-talkie", "рация", "gad_walkie_talkies"),
    ("lift", "лифт", "gad_lift"),
    ("games console", "игровая приставка", "gad_console"),
    ("electric toothbrush", "электрическая зубная щётка", "gad_toothbrush"),
    ("electric fan", "вентилятор", "gad_fan"),
]


def img(unit, name):
    return f"{MEDIA}sm3/{unit}/{name}.webp"


def svg(unit, name):
    """Часы Unit 3 лежат в svg — их рисует tools/gen_clocks.py, а не генератор."""
    return f"{MEDIA}sm3/{unit}/{name}.svg"


def shared(name):
    return f"{MEDIA}shared/{name}.webp"


def quiz_ru_to_en(words, per_question=4):
    """Вопросы «как по-английски».

    Отвлекающие берём по кругу от самого слова, а не первые из списка: иначе
    во всех вопросах стоят одни и те же три варианта, и правильный вычисляется
    исключением, не читая вопроса.
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
    return {"questions": qs}


LESSONS = {
    "u1_hw1": {
        "unit": "u1",
        "unit_title": "Unit 1 · School",
        "unit_sort": 1,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>Привет! 👋</h2>"
                "<p>Сегодня мы повторим названия школьных предметов и дни недели.</p>"
                "<p>Сначала выучим слова, потом разберёмся с расписанием. Поехали!</p>"}),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": img("u1", f)}
                for en, ru, f in SUBJECTS
            ]}),

            ("match", {"pairs": [
                {"left_image": img("u1", f), "right": en, "right_audio_tts": en}
                for en, ru, f in SUBJECTS
            ]}),

            ("quiz", quiz_ru_to_en(SUBJECTS)),

            ("exact_input", {"items": [
                {"prompt": f"Напиши по-английски: {ru}", "accept": [en, en.lower()], "audio_tts": en}
                for en, ru, f in SUBJECTS
            ]}),

            ("text", {"html":
                "<h3>Расписание на неделю</h3>"
                "<p>Внимательно изучи расписание. Столбцы — это дни недели, слева направо: "
                "понедельник, вторник, среда, четверг, пятница. Поднос с обедом делит день "
                "на уроки <b>до обеда</b> и <b>после обеда</b>.</p>"
                f'<p><img src="{img("u1", "scene_timetable")}" alt="Timetable" style="max-width:100%"></p>'}),

            ("gaps", {
                "title": "Определи, какой день описан, и впиши его название",
                "mode": "type",
                "text":
                    "1. This is what I've got today. P.E., English and Music before lunch. "
                    "I.T. and History after lunch. Today is __Wednesday__.\n"
                    "2. This is what I've got today. Science, Art and English before lunch. "
                    "Maths and Geography after lunch. Today is __Friday__.\n"
                    "3. This is what I've got today. Maths, English and Geography before lunch. "
                    "Music and History after lunch. Today is __Monday__.",
                "gaps_expected": 3,
            }),

            ("order", {
                "words": ["When", "have", "you", "got", "English?", "On", "Mondays.", "After", "Maths."],
                "sentence": "When have you got English? On Mondays. After Maths.",
                "audio_tts": "When have you got English? On Mondays. After Maths.",
            }),

            ("speaking", {
                "title": "Расскажи про свой любимый предмет 🎤",
                "html": "<p>Нажми на микрофон и расскажи, какой предмет тебе нравится и когда он у тебя.</p>"
                        "<p><i>Например: I like Art. I've got Art on Tuesdays.</i></p>",
                "needs_review": True,
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>Отличная работа! 🎉</h3><p>До встречи на уроке!</p>"}),
        ],
    },
    "u1_hw2": {
        "unit": "u1",
        "unit_title": "Unit 1 \u00b7 School",
        "unit_sort": 1,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_book")}" alt="" style="height:200px"></p>'
                "<h2>\u041f\u0440\u0438\u0432\u0435\u0442! 👋</h2>"
                "<p>\u0421\u0435\u0433\u043e\u0434\u043d\u044f \u0442\u044b \u0431\u0443\u0434\u0435\u0448\u044c \u043c\u043d\u043e\u0433\u043e \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0441 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f\u043c\u0438: "
                "\u0432\u043f\u0438\u0448\u0435\u0448\u044c \u043f\u0440\u043e\u043f\u0443\u0449\u0435\u043d\u043d\u044b\u0435 \u0441\u043b\u043e\u0432\u0430 \u0438 \u0440\u0430\u0441\u0441\u0442\u0430\u0432\u0438\u0448\u044c \u0441\u043b\u043e\u0432\u0430 \u043f\u043e \u043f\u043e\u0440\u044f\u0434\u043a\u0443, "
                "\u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043b\u0443\u0447\u0438\u043b\u0438\u0441\u044c \u0432\u0435\u0440\u043d\u044b\u0435 \u0444\u0440\u0430\u0437\u044b.</p>"
                "<p>\u0423\u0434\u0430\u0447\u0438!</p>"}),

            ("gaps", {
                "title": "\u0421\u0430\u0440\u0430 \u0438 \u0410\u0434\u0430\u043c \u0440\u0430\u0441\u0441\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0442 \u043e \u0441\u0435\u0431\u0435. "
                         "\u041f\u0435\u0440\u0435\u0442\u0430\u0449\u0438 \u0441\u043b\u043e\u0432\u0430 \u0432 \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0438",
                "mode": "drag",
                "text":
                    "Adam:\n"
                    "I love __reading__ books in English.\n"
                    "I'm good at __writing__ stories, hey!\n"
                    "I love __learning__ about lots of things.\n"
                    "We learn at school all __day__.\n\n"
                    "Sarah:\n"
                    "I love __working__ on paper.\n"
                    "I think Art's just __great__!\n"
                    "I really like my __teachers__.\n"
                    "That's why I'm never __late__!",
                "gaps_expected": 8,
            }),

            ("order", {
                "words": ["I", "like", "speaking", "English.", "I'm", "good", "at", "it."],
                "sentence": "I like speaking English. I'm good at it.",
                "audio_tts": "I like speaking English. I'm good at it.",
            }),

            ("order", {
                "words": ["I", "don't", "like", "learning", "Maths."],
                "sentence": "I don't like learning Maths.",
                "audio_tts": "I don't like learning Maths.",
            }),

            ("order", {
                "words": ["I", "love", "studying", "history.", "I", "love", "my", "teacher", "too."],
                "sentence": "I love studying history. I love my teacher too.",
                "audio_tts": "I love studying history. I love my teacher too.",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>\u041e\u0442\u043b\u0438\u0447\u043d\u043e! \u0414\u043e\u043c\u0430\u0448\u043d\u0435\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435 \u0433\u043e\u0442\u043e\u0432\u043e 🌟</h3>"
                "<p>\u0422\u044b \u043c\u043e\u043b\u043e\u0434\u0435\u0446, \u0432\u0441\u0442\u0440\u0435\u0442\u0438\u043c\u0441\u044f \u043d\u0430 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u043c \u0443\u0440\u043e\u043a\u0435 :)</p>"}),
        ],
    },
    "u1_hw3": {
        "unit": "u1",
        "unit_title": "Unit 1 \u00b7 School",
        "unit_sort": 1,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_highfive")}" alt="" style="height:200px"></p>'
                "<h2>\u041f\u0440\u0438\u0432\u0435\u0442! \u0414\u0430\u0432\u0430\u0439 \u043f\u0440\u0438\u0441\u0442\u0443\u043f\u0438\u043c \u043a \u0434\u043e\u043c\u0430\u0448\u043d\u0435\u043c\u0443 \u0437\u0430\u0434\u0430\u043d\u0438\u044e :)</h2>"
                "<p>\u0421\u0435\u0433\u043e\u0434\u043d\u044f \u0442\u044b \u0441\u0430\u043c \u0431\u0443\u0434\u0435\u0448\u044c \u043f\u0438\u0441\u0430\u0442\u044c \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u2014 \u043f\u043e \u0442\u043e\u043c\u0443, \u0447\u0442\u043e \u0433\u043e\u0432\u043e\u0440\u044f\u0442 \u0440\u0435\u0431\u044f\u0442\u0430.</p>"}),

            ("task", {
                "title": "Look, read and write sentences \u00b7 Tim",
                "needs_review": True,
                "html":
                    "<p>\u0422\u0438\u043c \u0440\u0430\u0441\u0441\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043e \u0448\u043a\u043e\u043b\u0435. \u0421\u043c\u0430\u0439\u043b\u0438\u043a \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442, \u043a\u0430\u043a \u043e\u043d \u043a \u044d\u0442\u043e\u043c\u0443 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0441\u044f: "
                    "😁 \u2014 <i>like</i>, 😖 \u2014 <i>don\u2019t like</i>, 😁😁 \u2014 <i>love</i>. "
                    "\u0417\u0430\u043f\u0438\u0448\u0438 \u043f\u043e\u043b\u043d\u044b\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f.</p>"
                    "<ol>"
                    "<li>😁 Speaking English. Good at it. \u2014 "
                    "<i>\u043e\u0431\u0440\u0430\u0437\u0435\u0446: I like speaking English. I\u2019m good at it.</i></li>"
                    "<li>😖 History. Not my favourite subject.</li>"
                    "<li>😁😁 Listening to music.</li>"
                    "</ol>",
            }),

            ("task", {
                "title": "Look, read and write sentences \u00b7 Anna",
                "needs_review": True,
                "html":
                    "<p>\u0422\u0435\u043f\u0435\u0440\u044c \u0410\u043d\u043d\u0430. \u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0430\u0439 \u043d\u0443\u043c\u0435\u0440\u0430\u0446\u0438\u044e \u2014 4, 5, 6.</p>"
                    "<ol start=\"4\">"
                    "<li>😖 Learning Maths.</li>"
                    "<li>😁 Geography. Very good at it.</li>"
                    "<li>😁😁 Studying History. Love my teacher too.</li>"
                    "</ol>",
            }),

            ("task", {
                "title": "Look and write sentences",
                "needs_review": True,
                "html":
                    "<p>\u0413\u0430\u043b\u043e\u0447\u043a\u0430 \u2714 \u2014 \u043d\u0440\u0430\u0432\u0438\u0442\u0441\u044f, \u043a\u0440\u0435\u0441\u0442\u0438\u043a \u2716 \u2014 \u043d\u0435 \u043d\u0440\u0430\u0432\u0438\u0442\u0441\u044f. "
                    "\u041d\u0430\u043f\u0438\u0448\u0438 \u043f\u0440\u043e \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435.</p>"
                    "<ol>"
                    "<li>Jim \u00b7 playing football \u00b7 \u2716 \u2014 "
                    "<i>\u043e\u0431\u0440\u0430\u0437\u0435\u0446: Jim doesn\u2019t like playing football.</i></li>"
                    "<li>Claire \u00b7 singing \u00b7 \u2716</li>"
                    "<li>Mary \u00b7 playing the piano \u00b7 \u2714</li>"
                    "<li>Sam \u00b7 reading \u00b7 \u2714</li>"
                    "<li>Lisa \u00b7 watching TV \u00b7 \u2716</li>"
                    "</ol>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_clap")}" alt="" style="height:180px"></p>'
                "<h3>Good job! Thank you!</h3>"
                "<p>\u0423\u0447\u0438\u0442\u0435\u043b\u044c \u043f\u0440\u043e\u0432\u0435\u0440\u0438\u0442 \u0442\u0432\u043e\u0438 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0438 \u043d\u0430\u043f\u0438\u0448\u0435\u0442, \u0447\u0442\u043e \u043f\u043e\u043b\u0443\u0447\u0438\u043b\u043e\u0441\u044c \u043b\u0443\u0447\u0448\u0435 \u0432\u0441\u0435\u0433\u043e.</p>"}),
        ],
    },
    "u1_hw4": {
        "unit": "u1",
        "unit_title": "Unit 1 · School",
        "unit_sort": 1,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_rocket")}" alt="" style="height:200px"></p>'
                "<h2>Привет! Готов к новому домашнему заданию?</h2>"}),

            ("text", {"html":
                "<h3>Давай повторим правило!</h3>"
                "<p>Мы используем <b>have to</b>, когда говорим о правилах и о том, "
                "что мы <b>должны</b> делать.</p>"
                "<div style=\"border-left:4px solid #2E9E4F;padding:8px 14px;margin:10px 0\">"
                "<p><i>Language focus</i></p>"
                "<p>You <b>have to wear</b> a uniform.<br>"
                "You <b>have to climb</b> like me.<br>"
                "You <b>have to clean</b> your eyes like this.<br>"
                "You can’t? I see. Hehe!</p></div>"}),

            ("match", {
                "title": "Соедини картинку с предложением",
                "pairs": [
                    {"left_image": img("u1", "haveto_be_on_time"),
                     "right": "You have to arrive at school before nine o’clock.",
                     "right_audio_tts": "You have to arrive at school before nine o'clock."},
                    {"left_image": img("u1", "haveto_brush_teeth"),
                     "right": "You have to brush your teeth after a meal.",
                     "right_audio_tts": "You have to brush your teeth after a meal."},
                    {"left_image": img("u1", "haveto_wash_hands"),
                     "right": "You have to wash your hands before a meal.",
                     "right_audio_tts": "You have to wash your hands before a meal."},
                    {"left_image": img("u1", "haveto_wear_uniform"),
                     "right": "You have to get dressed before you can go to school.",
                     "right_audio_tts": "You have to get dressed before you can go to school."},
                    {"left_image": img("u1", "haveto_clean_shoes"),
                     "right": "You have to clean your shoes before you go and play.",
                     "right_audio_tts": "You have to clean your shoes before you go and play."},
                    {"left_image": img("u1", "haveto_do_homework"),
                     "right": "You have to do your homework before you go and play.",
                     "right_audio_tts": "You have to do your homework before you go and play."},
                ],
            }),

            ("task", {
                "title": "Write about you",
                "needs_review": True,
                "html":
                    "<p>Напиши про себя. Используй <b>before</b>, <b>after</b>, "
                    "<b>every day</b> или <b>every week</b>.</p>"
                    "<p><b>At school</b></p>"
                    "<ol><li>I have to …</li><li>I …</li><li>…</li></ol>"
                    "<p><b>At home</b></p>"
                    "<ol><li>I have to …</li><li>I …</li><li>…</li></ol>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_medal")}" alt="" style="height:180px"></p>'
                "<h3>Super duper! Nice job!</h3>"}),
        ],
    },
    "u1_hw5": {
        "unit": "u1",
        "unit_title": "Unit 1 · School",
        "unit_sort": 1,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_book")}" alt="" style="height:200px"></p>'
                "<h2>Добро пожаловать в домашнее задание!</h2>"
                "<p>Сегодня мы вспомним историю, с которой познакомились на уроке, "
                "и выполним по ней задания.</p>"
                "<p>Для начала прочитай текст ещё раз — вспомни, в какое приключение "
                "попали Lucy и Ben.</p>"}),

            ("text", {"html":
                "<h3>Ben and Lucy in the library</h3>"
                f'<p><img src="{img("u1", "story_library_1")}" alt="Кадры 1–6" style="max-width:100%"></p>'
                f'<p><img src="{img("u1", "story_library_2")}" alt="Кадры 7–8" style="max-width:100%"></p>'}),

            ("quiz", {"questions": [{
                "q": "Who is Mr Williams?",
                "type": "single",
                "options": [{"text": "teacher"}, {"text": "librarian"}, {"text": "shop assistant"}],
                "correct": [1],
            }]}),

            ("truefalse", {
                "title": "Выбери «верно» или «неверно» для каждого предложения. Не торопись!",
                "statements": [
                    {"text": "Ben and Lucy are in the library.", "answer": True},
                    {"text": "The book is easy to read.", "answer": False},
                    {"text": "The book is in code.", "answer": True},
                    {"text": "The librarian, Mr Williams, helps the explorers to read the code.",
                     "answer": False},
                    {"text": "Lucy finds the secret to the book.", "answer": True},
                    {"text": "Horax understands the code.", "answer": False},
                ],
            }),

            ("task", {
                "title": "А теперь задание посложнее!",
                "needs_review": True,
                "html":
                    "<p>Мы узнали, что Lucy и Ben могут прочесть книгу с помощью секретной записки. "
                    "А сможешь ли ты расшифровать их послание, используя код?</p>"
                    f'<p><img src="{img("u1", "story_code")}" alt="Код" style="max-width:100%"></p>'
                    "<p>Запиши в поле ниже, что получилось.</p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("congrats_popper")}" alt="" style="height:180px"></p>'
                "<h3>Ура! Ты справился с домашней работой 🎉</h3>"
                "<p>Ты молодец! Увидимся на занятии.</p>"}),
        ],
    },
    "u1_hw6": {
        "unit": "u1",
        "unit_title": "Unit 1 · School",
        "unit_sort": 1,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        # Раскраску («послушай запись и раскрась картинку») Анна просила убрать
        # из заданий — блок выброшен, приветствие переписано без обещания раскраски.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_laptop")}" alt="" style="height:200px"></p>'
                "<h2>Привет!</h2>"
                "<p>Сегодня ты будешь много работать с текстом. Скорее приступай к заданиям :)</p>"}),

            ("text", {"html":
                "<h3>Puzzles are great fun</h3>"
                "<p>Прочитай историю Оливера — она понадобится в обоих заданиях.</p>"
                f'<p><img src="{img("u1", "story_oliver")}" alt="История Оливера" style="max-width:100%"></p>'}),

            ("gaps", {
                "title": "Вставь пропущенные слова так, чтобы предложения совпали с рассказом",
                "mode": "drag",
                "text":
                    "1. The children think Oliver is silly because he doesn't like "
                    "__football and computer games__.\n"
                    "2. Oliver thinks stories are boring because they don't have "
                    "__numbers and dates__.\n"
                    "3. Oliver can say what __day__ it is when he looks at a date.\n"
                    "4. The children think Oliver is a __computer__.\n"
                    "5. Oliver wants to start a __puzzle club__ at school.\n"
                    "6. Everyone __likes__ Oliver's idea.",
                "gaps_expected": 6,
            }),

            ("truefalse", {
                "title": "Отметь верные и неверные утверждения",
                "statements": [
                    {"text": "The boys and girls think Oliver is different.", "answer": True},
                    {"text": "Oliver likes sitting under a tree and thinking.", "answer": True},
                    {"text": "Oliver likes listening to Ms Sanders’ stories.", "answer": False},
                    {"text": "Ms Sanders writes the date of her birthday on the board.", "answer": True},
                    {"text": "The computer and Oliver say different days.", "answer": False},
                    {"text": "Mike wants to learn to do the same thing as Oliver.", "answer": True},
                ],
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_jump")}" alt="" style="height:180px"></p>'
                "<h3>Урааа, ты справился, поздравляю!</h3><p>До скорой встречи!</p>"}),
        ],
    },
    "u1_hw7": {
        "unit": "u1",
        "unit_title": "Unit 1 · School",
        "unit_sort": 1,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        # Обе части выгрузки, «Homework 7 (1)» и «(2)», в одном уроке:
        # две части одной домашки — это один урок.
        # Раскраска «раскрась фигуры по цветам» заменена на match теми же
        # парами — раскраски Анна просила убрать. Обе игры Wordwall (робот
        # идёт к названной фигуре; робот идёт к ячейке с верным ответом)
        # пересобраны quiz'ами — СОСТАВ МОЙ.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_highfive")}" alt="" style="height:200px"></p>'
                "<h2>Привет!</h2>"
                "<p>Сегодня ты будешь много работать с геометрическими фигурами, "
                "а потом составишь интервью и ответишь на вопросы.</p>"
                "<p>Задания самые разные и очень интересные — удачи :)</p>"}),

            ("exact_input", {"items": [
                {"image": img("u1", "shape_pentagon"),
                 "prompt": "1. Напиши название фигуры",
                 "accept": ["pentagon", "Pentagon", "a pentagon"], "audio_tts": "pentagon"},
                {"image": img("u1", "shape_hexagon"),
                 "prompt": "2. Напиши название фигуры",
                 "accept": ["hexagon", "Hexagon", "a hexagon"], "audio_tts": "hexagon"},
                {"image": img("u1", "shape_triangle"),
                 "prompt": "3. Напиши название фигуры",
                 "accept": ["triangle", "Triangle", "a triangle"], "audio_tts": "triangle"},
            ]}),

            ("match", {
                "title": "Соедини каждую иллюстрацию с названием объекта, который на ней изображён",
                "pairs": [
                    {"left_image": img("u1", "shapepic_cat"), "right": "cat", "right_audio_tts": "cat"},
                    {"left_image": img("u1", "shapepic_person"), "right": "person", "right_audio_tts": "person"},
                    {"left_image": img("u1", "shapepic_boat"), "right": "boat", "right_audio_tts": "boat"},
                    {"left_image": img("u1", "shapepic_snake"), "right": "snake", "right_audio_tts": "snake"},
                ],
            }),

            ("match", {
                "title": "У каждой фигуры свой цвет. Соедини фигуру с её названием",
                "pairs": [
                    {"left_image": img("u1", "shape_square"), "right": "blue square",
                     "right_audio_tts": "a blue square"},
                    {"left_image": img("u1", "shape_circle"), "right": "green circle",
                     "right_audio_tts": "a green circle"},
                    {"left_image": img("u1", "shape_pentagon"), "right": "yellow pentagon",
                     "right_audio_tts": "a yellow pentagon"},
                    {"left_image": img("u1", "shape_triangle"), "right": "red triangle",
                     "right_audio_tts": "a red triangle"},
                    {"left_image": img("u1", "shape_rectangle"), "right": "orange rectangle",
                     "right_audio_tts": "an orange rectangle"},
                ],
            }),

            ("quiz", {"questions": [
                {"q": "Find the hexagon.", "type": "single",
                 "options": [{"image": img("u1", "shape_pentagon")}, {"image": img("u1", "shape_hexagon")},
                             {"image": img("u1", "shape_square")}, {"image": img("u1", "shape_circle")}],
                 "correct": [1]},
                {"q": "Find the rectangle.", "type": "single",
                 "options": [{"image": img("u1", "shape_triangle")}, {"image": img("u1", "shape_circle")},
                             {"image": img("u1", "shape_rectangle")}, {"image": img("u1", "shape_hexagon")}],
                 "correct": [2]},
                {"q": "Find the circle.", "type": "single",
                 "options": [{"image": img("u1", "shape_circle")}, {"image": img("u1", "shape_square")},
                             {"image": img("u1", "shape_pentagon")}, {"image": img("u1", "shape_triangle")}],
                 "correct": [0]},
                {"q": "Find the square.", "type": "single",
                 "options": [{"image": img("u1", "shape_rectangle")}, {"image": img("u1", "shape_hexagon")},
                             {"image": img("u1", "shape_triangle")}, {"image": img("u1", "shape_square")}],
                 "correct": [3]},
            ]}),

            ("match", {
                "title": "Составь интервью: соедини вопросы с ответами",
                "pairs": [
                    {"left": "What’s your favourite subject, Kate?",
                     "right": "Science. I love it."},
                    {"left": "What do you like about it?",
                     "right": "We do fun activities in the Science, and I love doing them."},
                    {"left": "How many Science lessons do you have a week?",
                     "right": "Three, but I’d like to have it every day."},
                    {"left": "Have you got Science today?",
                     "right": "Let me think. It’s Wednesday. Yes, I’ve got Science after Maths."},
                    {"left": "Do lots of students like Science?",
                     "right": "No, not many children like it. They think it’s difficult."},
                    {"left": "What’s the favourite subject in your class?",
                     "right": "For most of my classmates it’s English. They love it."},
                ],
            }),

            ("truefalse", {
                "title": "Верно или неверно?",
                "statements": [
                    {"text": "Kate’s favourite subject is Chemistry.", "answer": False},
                    {"text": "On Wednesdays she has Science.", "answer": True},
                    {"text": "She has three Science lessons every week.", "answer": True},
                    {"text": "Kate’s classmates love Science.", "answer": False},
                    {"text": "Kate tells that Science lessons are boring.", "answer": False},
                ],
            }),

            ("quiz", {"questions": [
                {"q": "What is Kate’s favourite subject?", "type": "single",
                 "options": [{"text": "English"}, {"text": "Maths"},
                             {"text": "Science"}, {"text": "History"}],
                 "correct": [2]},
                {"q": "How many Science lessons has Kate got a week?", "type": "single",
                 "options": [{"text": "one"}, {"text": "three"},
                             {"text": "five"}, {"text": "every day"}],
                 "correct": [1]},
                {"q": "Which lesson comes before Science on Wednesday?", "type": "single",
                 "options": [{"text": "Art"}, {"text": "Music"},
                             {"text": "Maths"}, {"text": "P.E."}],
                 "correct": [2]},
                {"q": "What is the favourite subject in Kate’s class?", "type": "single",
                 "options": [{"text": "Science"}, {"text": "English"},
                             {"text": "Geography"}, {"text": "I.T."}],
                 "correct": [1]},
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("well_done_smiley")}" alt="" style="height:180px"></p>'
                "<h3>Ты справился со всеми заданиями, поздравляю!</h3>"
                "<p>Теперь можешь смело отдыхать :)</p>"}),
        ],
    },
    "u1_test": {
        "unit": "u1",
        "unit_title": "Unit 1 · School",
        "unit_sort": 1,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        # Нумерация блоков как в выгрузке: один match, пять «выбери правильный
        # вариант», пять «составь предложение», запись голоса.
        # «Выбери правильный вариант» отдельного типа у нас нет — делаем quiz'ом,
        # по вопросу на каждый пропуск, предложение целиком в тексте вопроса.
        "blocks": [
            ("match", {
                "title": "Соедини слова с картинками",
                "pairs": [
                    {"left_image": img("u1", "subj_art"), "right": "Art", "right_audio_tts": "Art"},
                    {"left_image": img("u1", "subj_english"), "right": "English", "right_audio_tts": "English"},
                    {"left_image": img("u1", "subj_geography"), "right": "Geography", "right_audio_tts": "Geography"},
                    {"left_image": img("u1", "subj_science"), "right": "Science", "right_audio_tts": "Science"},
                    {"left_image": img("u1", "subj_history"), "right": "History", "right_audio_tts": "History"},
                    {"left_image": img("u1", "subj_maths"), "right": "Maths", "right_audio_tts": "Maths"},
                ],
            }),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: ___ he like eating chocolate?", "type": "single",
                 "options": [{"text": "Do"}, {"text": "Does"}, {"text": "Is"}], "correct": [1]},
                {"q": "B: Yes, he ___.", "type": "single",
                 "options": [{"text": "do"}, {"text": "does"}, {"text": "like"}], "correct": [1]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: Do you ___ wear uniform to school?", "type": "single",
                 "options": [{"text": "have"}, {"text": "have to"}, {"text": "do"}], "correct": [1]},
                {"q": "B: No, we ___.", "type": "single",
                 "options": [{"text": "don’t"}, {"text": "have"}, {"text": "do"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "Sarah ___ swimming.", "type": "single",
                 "options": [{"text": "like"}, {"text": "doesn’t like"}, {"text": "doesn’t likes"}],
                 "correct": [1]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: Do you ___ watching TV?", "type": "single",
                 "options": [{"text": "like"}, {"text": "likes"}], "correct": [0]},
                {"q": "B: Yes, I do. But today I ___ do my homework before I can watch TV.",
                 "type": "single",
                 "options": [{"text": "have"}, {"text": "has to"}, {"text": "have to"}], "correct": [2]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: What do you like ___?", "type": "single",
                 "options": [{"text": "do"}, {"text": "doing"}], "correct": [1]},
                {"q": "B: I like ___ computer games.", "type": "single",
                 "options": [{"text": "play"}, {"text": "playing"}], "correct": [1]},
            ]}),

            ("order", {
                "words": ["Alice", "has", "to", "walk", "to school."],
                "sentence": "Alice has to walk to school.",
                "audio_tts": "Alice has to walk to school.",
            }),

            ("order", {
                "words": ["July", "doesn’t", "like", "studying", "Geography."],
                "sentence": "July doesn’t like studying Geography.",
                "audio_tts": "July doesn't like studying Geography.",
            }),

            ("order", {
                "words": ["We", "love", "reading", "about", "knights and queens."],
                "sentence": "We love reading about knights and queens.",
                "audio_tts": "We love reading about knights and queens.",
            }),

            # в выгрузке имя написано с опечаткой — «Ccaspar»
            ("order", {
                "words": ["Caspar", "has", "to", "tidy up", "his room."],
                "sentence": "Caspar has to tidy up his room.",
                "audio_tts": "Caspar has to tidy up his room.",
            }),

            ("order", {
                "words": ["Eliot", "and Noah", "hate", "playing", "tennis."],
                "sentence": "Eliot and Noah hate playing tennis.",
                "audio_tts": "Eliot and Noah hate playing tennis.",
            }),

            ("speaking", {
                "title": "SPEAKING TASK 🎤",
                "needs_review": True,
                "html":
                    "<p>Расскажи о любимых и нелюбимых школьных предметах (5–7 предложений). "
                    "Запиши свой ответ, нажав на кнопку микрофона.</p>"
                    "<p><i>For example:<br>I love learning English.<br>"
                    "I hate Maths. It’s boring.<br>I like studying Music.</i></p>",
            }),
        ],
    },
    "u2_hw1": {
        "unit": "u2",
        "unit_title": "Unit 2 · Food",
        "unit_sort": 2,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        # Обе части выгрузки в одном уроке: «(1)» — словарный тренажёр на восемь
        # слов, «(2)» — задания. Кроссворд Wordwall («посмотри на картинки и
        # напиши слово») пересобран exact_input'ом с теми же картинками —
        # СОСТАВ МОЙ.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>Привет-привет!</h2>"
                "<p>Готов к домашнему заданию? Тогда давай начинать :)</p>"}),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": img("u2", f)}
                for en, ru, f in U2_FOOD
            ]}),

            ("exact_input", {"items": [
                {"image": img("u2", f), "prompt": "Посмотри на картинку и напиши слово",
                 "accept": [en, en.lower(), en.capitalize()], "audio_tts": en}
                for en, ru, f in U2_FOOD
            ]}),

            ("gaps", {
                "title": "Заполни пропуски словами из кроссворда",
                "mode": "drag",
                "text":
                    "1. Can I have two chicken __rolls__, please?\n"
                    "2. Carrots and potatoes are __vegetables__.\n"
                    "3. It’s usually yellow or white. — __cheese__!\n"
                    "4. You wash your face with it, and you can drink it. — __water__!\n"
                    "5. You drink this, it’s sweet. — __apple juice__!\n"
                    "6. It’s usually hot and you need a spoon to eat it. — __soup__!",
                "gaps_expected": 6,
            }),

            ("sequence", {
                "title": "Составь диалог — расставь реплики по порядку",
                "items": [
                    {"text": "I’m hungry."},
                    {"text": "Would you like a chicken roll?"},
                    {"text": "No, thanks. I don’t like chicken."},
                    {"text": "Would you like a cheese sandwich?"},
                    {"text": "Yes, please. I’d love one."},
                ],
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>Супер!</h3>"
                "<p>Большое спасибо за домашнее задание. Ты отлично поработал сегодня. "
                "Увидимся на уроке!</p>"}),
        ],
    },
    "u2_hw2": {
        "unit": "u2",
        "unit_title": "Unit 2 · Food",
        "unit_sort": 2,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        # Обе части выгрузки одним уроком. Видео в выгрузке нет — блок стоит
        # пустым, методисту останется вставить ссылку (строка в файле
        # «доработать руками»). Из двух почти одинаковых заданий на запись
        # голоса про одну и ту же картинку оставлено одно.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>Привет-привет!</h2>"
                "<p>Ну что, готов к новой домашней работе? Она тебя уже ждёт. "
                "Давай начинать!</p>"}),

            ("video", {"title": "Посмотри видео и найди ответ на вопрос: What are they cooking? 🍰",
                       "url": "", "provider": "youtube"}),

            ("quiz", {"questions": [{
                "q": "What are they cooking?",
                "type": "single",
                "options": [{"text": "cupcakes"}, {"text": "candies"},
                            {"text": "a cake"}, {"text": "a pizza"}],
                "correct": [2],
            }]}),

            ("match", {
                "title": "Соедини картинку с описанием 🧾",
                "pairs": [
                    {"left_image": img("u2", "tray_potatoes_peas_onions"),
                     "right": "There are some potatoes. There are some peas. There are some onions."},
                    {"left_image": img("u2", "tray_milk_lemonade_juice"),
                     "right": "There is some milk. There is some lemonade. There is some orange juice."},
                    {"left_image": img("u2", "tray_biscuits_cake_chocolate"),
                     "right": "There are some biscuits. There is some cake. There is some chocolate."},
                    {"left_image": img("u2", "tray_cake_biscuits_sandwiches"),
                     "right": "There is some cake. There are some biscuits. There are some sandwiches."},
                    {"left_image": img("u2", "tray_peas_potatoes_nuts"),
                     "right": "There are some peas. There are some potatoes. There are some nuts."},
                    {"left_image": img("u2", "tray_water_juice_milk"),
                     "right": "There is some water. There is some apple juice. There is some milk."},
                ],
            }),

            ("gaps", {
                "title": "Прочитай диалог и вставь some или any",
                "mode": "drag",
                "image": img("u2", "lunchbox_roll_water"),
                "text":
                    "Kate: Guess what’s in my lunch box!\n"
                    "Alice: There’s __some__ bread. I think there’s a roll.\n"
                    "Kate: That’s right. What’s in it?\n"
                    "Alice: Is there __any__ chicken?\n"
                    "Kate: No, there isn’t. I don’t like chicken.\n"
                    "Alice: OK, there isn’t __any__ chicken. Is there __any__ cheese?\n"
                    "Kate: Cheese? Yes, there is. I love cheese.\n"
                    "Alice: Is there anything else in your lunch box?\n"
                    "Kate: Yes, there’s __some__ water too.",
                "gaps_expected": 5,
            }),

            ("task", {
                "title": "Напиши к каждому предложению вопрос и отрицание",
                "needs_review": True,
                "html":
                    "<p><i>Образец:</i><br>There is some cheese.<br>"
                    "Is there any cheese?<br>There isn’t any cheese.</p>"
                    "<ol><li>There are some rolls.</li><li>There is some salad.</li>"
                    "<li>There are some vegetables.</li><li>There is some soup.</li></ol>",
            }),

            ("speaking", {
                "title": "Посмотри на картинку и расскажи, что на ней есть, а чего нет 🎤",
                "needs_review": True,
                "image": img("u2", "scene_picnic"),
                "html": "<p>Используй <b>there is</b> / <b>there are</b> и "
                        "<b>there isn’t</b> / <b>there aren’t</b>.</p>",
            }),

            ("match", {
                "title": "Соедини картинку с описанием корзинки хозяина 🍎 🥦 🥕",
                "pairs": [
                    {"left_image": img("u2", "basket_vegetables_only"),
                     "right": "There are some vegetables in my basket, but there isn’t any fruit."},
                    {"left_image": img("u2", "basket_fruit_only"),
                     "right": "There’s some fruit in my basket, but there aren’t any vegetables."},
                    {"left_image": img("u2", "basket_mixed"),
                     "right": "There’s some fruit and there are some vegetables in my basket."},
                ],
            }),

            ("gaps", {
                "title": "Корзинка Дэйзи: вставь some или any, is или are",
                "mode": "drag",
                "image": img("u2", "basket_bananas_juice"),
                "text":
                    "__Are__ there __any__ bananas in your basket? "
                    "Yes, there __are__ __some__ bananas.\n"
                    "__Is__ there __any__ apple juice in your basket? "
                    "Yes, there __is__ __some__ apple juice.\n"
                    "__Are__ there __any__ tomatoes? No, there __aren’t__ __any__ tomatoes.",
                "gaps_expected": 12,
            }),

            ("gaps", {
                "title": "Песня про пикник: впиши продукты из списка ребят",
                "mode": "drag",
                "text":
                    "Let’s make a picnic!\n"
                    "It’s going to be such fun.\n"
                    "We’re going to go shopping,\n"
                    "For a picnic in the sun.\n"
                    "Are there any __tomatoes__?\n"
                    "Is there any __jam__?\n"
                    "Yes, there are lots of yummy things,\n"
                    "For me and my friend Pam!",
                "gaps_expected": 2,
            }),

            ("task", {
                "title": "Второй куплет придумай сам",
                "needs_review": True,
                "html":
                    "<p>Впиши те продукты, которые пригодятся на пикнике тебе:</p>"
                    "<p><i>Are there any …?<br>Is there any …?<br>"
                    "Yes, there are lots of yummy things,<br>"
                    "These sandwiches look good!</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_clap")}" alt="" style="height:180px"></p>'
                "<h3>Спасибо тебе большое за твои старания!</h3>"
                "<p>Ты огромный молодец. Увидимся на уроке 😊</p>"}),
        ],
    },
    "u2_hw3": {
        "unit": "u2",
        "unit_title": "Unit 2 · Food",
        "unit_sort": 2,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        # Блок 4 в выгрузке — «соедини предложения ящериц с картинками», но
        # картинок там не было ни одной, а горошек у нас есть, хлеб с сыром и
        # мухи — нет. Сделан пропусками на те же три реплики: отрабатываются
        # ровно те обороты, ради которых задание и стояло.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_rocket")}" alt="" style="height:200px"></p>'
                "<h2>Привет, самый лучший ученик!</h2>"
                "<p>Готов к новой домашней работе? Давай начинать!</p>"}),

            ("video", {"title": "Посмотри видео и найди ответ на вопрос: What time is it?",
                       "url": "", "provider": "youtube"}),

            ("text", {"html":
                "<p>Посмотри видео <b>два раза</b>:</p>"
                "<ol><li>Первый раз просто послушай.</li>"
                "<li>Во второй раз повторяй все предложения за нашими ящерицами 🦎</li></ol>"}),

            ("quiz", {"questions": [{
                "q": "What time is it?",
                "type": "single",
                "options": [{"text": "it’s seven o’clock"}, {"text": "it’s twelve o’clock"},
                            {"text": "it’s six o’clock"}, {"text": "it’s nine o’clock"}],
                "correct": [2],
            }]}),

            ("gaps", {
                "title": "Вспомни, что говорили ящерицы, и вставь нужные слова",
                "mode": "drag",
                "text":
                    "__How about__ some peas?\n"
                    "__Shall we__ have some bread with cheese?\n"
                    "__I’d like__ some flies.",
                "gaps_expected": 3,
            }),

            ("gaps", {
                "title": "Прочитай диалог и вставь нужные слова",
                "mode": "drag",
                "text":
                    "Jack: __Shall__ we make a sandwich for lunch?\n"
                    "Sara: __Good__ idea.\n"
                    "Jack: How __about__ a chicken sandwich?\n"
                    "Sara: __OK__.\n"
                    "Jack: Shall we __have__ some salad with it?\n"
                    "Sara: Yes, please! I like chicken with salad.",
                "gaps_expected": 5,
            }),

            ("sequence", {
                "title": "Составь диалог — расставь реплики по порядку",
                "items": [
                    {"text": "Shall we make a pizza?"},
                    {"text": "Good idea! How about an onion and carrot one?"},
                    {"text": "Yuk! How about cheese and tomato?"},
                    {"text": "OK."},
                ],
            }),

            ("sequence", {
                "title": "И ещё один диалог",
                "items": [
                    {"text": "Shall we have sandwiches for lunch?"},
                    {"text": "OK. How about sausage sandwiches?"},
                    {"text": "Great idea. Oh no! There aren’t any sausages in the fridge."},
                    {"text": "How about egg sandwiches, then?"},
                ],
            }),

            ("sequence", {
                "title": "И последний",
                "items": [
                    {"text": "I’m thirsty. Can I have a drink, please?"},
                    {"text": "Yes, of course. How about lemonade?"},
                    {"text": "Sorry. I don’t like that."},
                    {"text": "That’s OK. How about apple juice?"},
                    {"text": "Yes, please. I like juice."},
                ],
            }),

            ("speaking", {
                "title": "Поддержи диалог 🎤",
                "needs_review": True,
                "html":
                    "<p>Посмотри видео и поддержи разговор:</p>"
                    "<ul><li>согласись на идею поесть суп;</li>"
                    "<li>вырази сожаление, что нет томатов;</li>"
                    "<li>согласись поесть другой суп.</li></ul>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_medal")}" alt="" style="height:180px"></p>'
                "<h3>Отличная работа!</h3>"
                "<p>Большое тебе спасибо за твой труд :) Ты отлично постарался. "
                "До встречи на уроке 😊</p>"}),
        ],
    },
    "u2_hw4": {
        "unit": "u2",
        "unit_title": "Unit 2 · Food",
        "unit_sort": 2,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_highfive")}" alt="" style="height:200px"></p>'
                "<h2>Привет-привет, самый лучший ученик!</h2>"
                "<p>Сегодня будем вспоминать историю, которую читали на уроке. "
                "Ну что, готов начинать?</p>"}),

            ("video", {"title": "Послушай аудио и найди ответ на вопрос: What happened to Buster?",
                       "url": "", "provider": ""}),

            ("text", {"html":
                "<h3>Ben and Lucy and the golden apple</h3>"
                f'<p><img src="{img("u2", "story_buster")}" alt="Кадры истории" style="max-width:100%"></p>'}),

            ("quiz", {"questions": [{
                "q": "What happened to Buster?",
                "type": "single",
                "options": [{"text": "The dog bit him."}, {"text": "Horax and Zelda hurt him."},
                            {"text": "The snake bit him."}],
                "correct": [2],
            }]}),

            ("quiz", {"title": "Выбери правильный вариант", "questions": [
                {"q": "Ben and Lucy want to go to the ___.", "type": "single",
                 "options": [{"text": "school"}, {"text": "library"}, {"text": "village"}],
                 "correct": [2]},
                {"q": "An old man tells them to go to the ___ at the top of the mountain.",
                 "type": "single",
                 "options": [{"text": "cellar"}, {"text": "waterfall"}, {"text": "village"}],
                 "correct": [1]},
                {"q": "Only the golden ___ can help Buster.", "type": "single",
                 "options": [{"text": "tomato"}, {"text": "orange"}, {"text": "apple"}],
                 "correct": [2]},
                {"q": "Horax and Zelda want to ___ the apple, too.", "type": "single",
                 "options": [{"text": "take"}, {"text": "eat"}, {"text": "cook"}],
                 "correct": [0]},
                {"q": "The children write ___ in the book.", "type": "single",
                 "options": [{"text": "an apple"}, {"text": "the letter"}, {"text": "an idea"}],
                 "correct": [1]},
            ]}),

            ("gaps", {
                "title": "Что ещё мог сказать Бен? Соедини начало и конец предложений",
                "mode": "drag",
                "text":
                    "Shall we __call the police__?\n"
                    "Let’s __take him to the vet__.\n"
                    "We can __make some tea for Buster__.\n"
                    "Do you want __any help__?",
                "gaps_expected": 4,
            }),

            ("speaking", {
                "title": "Расскажи историю от лица Бена 🎤",
                "needs_review": True,
                "html":
                    "<p>Представь, что ты Бен, и расскажи историю от его лица — так, "
                    "будто она происходит прямо сейчас. Обязательно скажи, что ты "
                    "чувствуешь и о чём думаешь 😊</p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("congrats_popper")}" alt="" style="height:180px"></p>'
                "<h3>Отличная работа!</h3>"
                "<p>Все задания выполнены. Ты большущий молодец 😊</p>"}),
        ],
    },
    "u2_hw5": {
        "unit": "u2",
        "unit_title": "Unit 2 · Food",
        "unit_sort": 2,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        # Два задания из выгрузки сюда не попали: «послушай аудио и соедини
        # картинку с её номером» и «соедини людей и блюда» — у первого нет ни
        # картинок, ни записи, у второго в выгрузке пусты обе колонки. Оба
        # вынесены строками в файл «доработать руками».
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_headphones")}" alt="" style="height:200px"></p>'
                "<h2>Привет-привет!</h2>"
                "<p>Ну что, готов к новой домашней работе? Давай начинать 😊</p>"}),

            ("video", {"title": "Послушай диалоги Ким и Дэниэля, а потом Тома и Мэри",
                       "url": "", "provider": ""}),

            ("gaps", {
                "title": "Впиши пропущенные слова ⏬",
                "mode": "drag",
                "text":
                    "Kim: __What’s the matter__, Daniel?\n"
                    "Daniel: It’s my head. It hurts.\n"
                    "Kim: Shall I get you some medicine?\n"
                    "Daniel: No, it’s OK. It’s not too bad.\n\n"
                    "Tom: What are you doing, Mary?\n"
                    "Mary: I want this book. It’s really good.\n"
                    "Tom: Shall I help you?\n"
                    "Mary: No, thanks. __I think__ __I’ve got it__.",
                "gaps_expected": 3,
            }),

            ("video", {"title": "Послушай образец к игре «I spy with my little eye»",
                       "url": "", "provider": ""}),

            ("speaking", {
                "title": "Поиграем в «I spy with my little eye» 🎤",
                "needs_review": True,
                "image": img("u2", "scene_i_spy"),
                "html":
                    "<p>Назови первую букву и сам предмет, который не подписан — "
                    "рядом с ним стоит пустая строчка. Начинай так:</p>"
                    "<p><i>I spy with my little eye something beginning with…</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>Большое тебе спасибо за отличную работу!</h3>"
                "<p>Ты прекрасно поработал сегодня. Так держать! Теперь можно отдохнуть :)</p>"}),
        ],
    },
    "u2_hw6": {
        "unit": "u2",
        "unit_title": "Unit 2 \u00b7 Food",
        "unit_sort": 2,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        # Блок 4 в выгрузке стоял без картинок (правая колонка пустая) —
        # подставлены наши карточки частей растения из Л2.6.
        # Блок 7 в выгрузке «Текст» с прикреплённым аудио-образцом; у нас это
        # пустой медиа-блок, чтобы номера блоков совпадали с выгрузкой.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>\u041f\u0440\u0438\u0432\u0435\u0442!</h2>"
                "<p>\u041a\u0430\u043a \u0442\u0432\u043e\u0438 \u0434\u0435\u043b\u0430? \u0422\u044b \u0431\u043e\u043b\u044c\u0448\u043e\u0439 \u043c\u043e\u043b\u043e\u0434\u0435\u0446, \u0447\u0442\u043e \u0440\u0435\u0448\u0438\u043b \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0434\u043e\u043c\u0430\u0448\u043d\u044e\u044e \u0440\u0430\u0431\u043e\u0442\u0443. "
                "\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u043b\u0435\u0442\u0438\u0442 \u043d\u0435\u0437\u0430\u043c\u0435\u0442\u043d\u043e, \u0442\u044b \u043a\u0430\u043a \u0432\u0441\u0435\u0433\u0434\u0430 \u0441\u043e \u0432\u0441\u0435\u043c \u0441\u043f\u0440\u0430\u0432\u0438\u0448\u044c\u0441\u044f. \u0412\u043f\u0435\u0440\u0451\u0434!</p>"
                "<p>\u0414\u0430\u0432\u0430\u0439 \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0438\u043c \u0432\u0438\u0434\u0435\u043e \u043f\u0440\u043e \u0441\u044a\u0435\u0434\u043e\u0431\u043d\u044b\u0435 \u0447\u0430\u0441\u0442\u0438 \u0440\u0430\u0441\u0442\u0435\u043d\u0438\u0439. \u041f\u043e\u043a\u0430 \u0431\u0443\u0434\u0435\u0448\u044c \u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c, "
                "\u043d\u0430\u0439\u0434\u0438 \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u043e\u0440\u0430\u043d\u0436\u0435\u0432\u044b\u0439 \u043f\u0440\u043e\u0434\u0443\u043a\u0442 \u0432 \u0432\u0438\u0434\u0435\u043e \u0438 \u0437\u0430\u043f\u043e\u043c\u043d\u0438 \u0435\u0433\u043e!</p>"}),

            ("video", {"title": "\u0412\u0438\u0434\u0435\u043e: \u0441\u044a\u0435\u0434\u043e\u0431\u043d\u044b\u0435 \u0447\u0430\u0441\u0442\u0438 \u0440\u0430\u0441\u0442\u0435\u043d\u0438\u0439",
                       "url": "", "provider": ""}),

            ("task", {
                "title": "What orange vegetable is in the video?",
                "needs_review": True,
                "html":
                    "<p>\u0421\u0430\u043c\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u043e\u0442\u0432\u0435\u0442 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441: "
                    "<i>What orange vegetable is in the video?</i></p>",
            }),

            ("match", {
                "title": "\u0412\u0441\u043f\u043e\u043c\u043d\u0438 \u0432\u0438\u0434\u0435\u043e \u0438 \u0441\u043e\u0435\u0434\u0438\u043d\u0438 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u044a\u0435\u0434\u043e\u0431\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 \u0441 \u0435\u0451 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u043e\u0439",
                "pairs": [
                    {"left_image": img("u2", "part_roots"),  "right": "roots",  "right_audio_tts": "roots"},
                    {"left_image": img("u2", "part_seeds"),  "right": "seeds",  "right_audio_tts": "seeds"},
                    {"left_image": img("u2", "part_stems"),  "right": "stems",  "right_audio_tts": "stems"},
                    {"left_image": img("u2", "part_leaves"), "right": "leaves", "right_audio_tts": "leaves"},
                    {"left_image": img("u2", "part_fruit"),  "right": "fruit",  "right_audio_tts": "fruit"},
                ],
            }),

            ("gaps", {
                "title": "\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u0439 \u043f\u0438\u0441\u044c\u043c\u043e \u041c\u0430\u0440\u043a\u0430 \u0438 \u043f\u043e\u0441\u0442\u0430\u0432\u044c \u0441\u043b\u043e\u0432\u0430 \u043d\u0430 \u0441\u0432\u043e\u0438 \u043c\u0435\u0441\u0442\u0430 \u2b07",
                "mode": "drag",
                "text":
                    "Dear Penny,\n\n"
                    "Tonight, we\u2019re having a nice dinner. There\u2019s a delicious salad "
                    "with spinach and lettuce \u2014 __leaves__. There\u2019s also a delicious "
                    "soup with asparagus \u2014 __stems__. We have some chicken with pumpkin "
                    "__seeds__. We also have a salad with __roots__: carrots and beetroot. "
                    "There\u2019s also a glass of __fruit__ juice for me with strawberries "
                    "and mango \u2014 my favourite.\n\n"
                    "What\u2019s for dinner at your home?\n\nMark",
                "gaps_expected": 5,
            }),

            ("gaps", {
                "title": "\u0418\u0437 \u043a\u0430\u043a\u0438\u0445 \u0447\u0430\u0441\u0442\u0435\u0439 \u0440\u0430\u0441\u0442\u0435\u043d\u0438\u0439 \u0434\u0435\u043b\u0430\u044e\u0442 \u044d\u0442\u0438 \u0431\u043b\u044e\u0434\u0430 \u0438 \u043d\u0430\u043f\u0438\u0442\u043e\u043a? \u0412\u043f\u0438\u0448\u0438 \u0438\u0445",
                "text":
                    "soup: __stems|leaves|seeds|roots__, __leaves|stems|seeds|roots__\n"
                    "juice: __fruit|fruits|stems|leaves|roots__, __stems|leaves|roots|fruit|fruits__\n"
                    "salad: __fruit|fruits|leaves|seeds|roots|stems__, "
                    "__seeds|leaves|fruit|fruits|roots|stems__",
                "gaps_expected": 6,
            }),

            ("video", {"title": "\u041f\u043e\u0441\u043b\u0443\u0448\u0430\u0439 \u043e\u0431\u0440\u0430\u0437\u0435\u0446 \u2014 \u0432 \u043d\u0451\u043c \u0433\u043e\u0432\u043e\u0440\u0438\u0442\u0441\u044f \u043e \u0436\u0438\u0432\u043e\u0442\u043d\u043e\u043c, \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0435 \u043d\u0435\u0442 :)",
                       "url": "", "provider": ""}),

            ("speaking", {
                "title": "\u0422\u0435\u043f\u0435\u0440\u044c \u2014 \u0442\u0432\u043e\u044f \u043e\u0447\u0435\u0440\u0435\u0434\u044c \U0001f3a4",
                "needs_review": True,
                "image": img("u2", "scene_who_eats_what"),
                "html":
                    "<p>\u0412\u044b\u0431\u0435\u0440\u0438 \u0434\u0432\u0443\u0445 \u0436\u0438\u0432\u043e\u0442\u043d\u044b\u0445 \u0441 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0438 \u0440\u0430\u0441\u0441\u043a\u0430\u0436\u0438, "
                    "\u043a\u0430\u043a\u0438\u043c\u0438 \u0447\u0430\u0441\u0442\u044f\u043c\u0438 \u0440\u0430\u0441\u0442\u0435\u043d\u0438\u0439 \u043b\u044e\u0431\u0438\u0442 \u043f\u0438\u0442\u0430\u0442\u044c\u0441\u044f \u043a\u0430\u0436\u0434\u043e\u0435 \u0438\u0437 \u043d\u0438\u0445.</p>"
                    "<p><i>\u041e\u0431\u0440\u0430\u0437\u0435\u0446: The rabbit eats roots. It likes carrots.</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>\u0421\u0443\u043f\u0435\u0440! \u0421\u043f\u0440\u0430\u0432\u0438\u043b\u0441\u044f \u0441\u043e \u0432\u0441\u0435\u043c\u0438 \u0437\u0430\u0434\u0430\u043d\u0438\u044f\u043c\u0438.</h3>"
                "<p>\u041e\u0433\u0440\u043e\u043c\u043d\u043e\u0435 \u0442\u0435\u0431\u0435 \u0441\u043f\u0430\u0441\u0438\u0431\u043e. \u0422\u044b \u043e\u0442\u043b\u0438\u0447\u043d\u043e \u043f\u043e\u0440\u0430\u0431\u043e\u0442\u0430\u043b \U0001f60a \u0423\u0432\u0438\u0434\u0438\u043c\u0441\u044f \u043d\u0430 \u0437\u0430\u043d\u044f\u0442\u0438\u0438!</p>"}),
        ],
    },
    "u2_hw7": {
        "unit": "u2",
        "unit_title": "Unit 2 \u00b7 Food",
        "unit_sort": 2,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        # Обе картинки заданий вырезаны из PDF выгрузки: сцена в столовой
        # (блок 3) и семья Джона за ужином (блок 4).
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_highfive")}" alt="" style="height:200px"></p>'
                "<h2>\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u0434\u043e\u043c\u0430\u0448\u043d\u0435\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435!</h2>"}),

            ("sequence", {
                "title": "\u0420\u0430\u0441\u0441\u0442\u0430\u0432\u044c \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0432 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u043c \u043f\u043e\u0440\u044f\u0434\u043a\u0435, \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043b\u0443\u0447\u0438\u043b\u0441\u044f \u0434\u0438\u0430\u043b\u043e\u0433. \u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430: \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u043c \u0441 \u0444\u0440\u0430\u0437\u044b \u00abHello. Can I help you?\u00bb",
                "items": [
                    {"text": "A: Hello. Can I help you?",
                     "audio_tts": "Hello. Can I help you?"},
                    {"text": "B: I\u2019d like a pizza with cheese, mushrooms and onions, please.",
                     "audio_tts": "I'd like a pizza with cheese, mushrooms and onions, please."},
                    {"text": "A: Sorry, we haven\u2019t got any mushrooms.",
                     "audio_tts": "Sorry, we haven't got any mushrooms."},
                    {"text": "B: No mushrooms? Have you got any peppers?",
                     "audio_tts": "No mushrooms? Have you got any peppers?"},
                    {"text": "A: Let me see. Yes, we\u2019ve got peppers.",
                     "audio_tts": "Let me see. Yes, we've got peppers."},
                    {"text": "B: That\u2019s great. Can I have some tomatoes, too?",
                     "audio_tts": "That's great. Can I have some tomatoes, too?"},
                    {"text": "A: OK, so that\u2019s pizza with cheese, onions, peppers and tomatoes.",
                     "audio_tts": "OK, so that's pizza with cheese, onions, peppers and tomatoes."},
                ],
            }),

            ("task", {
                "title": "\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0438 \u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443 \u0438 \u0441\u043e\u0441\u0442\u0430\u0432\u044c \u0434\u0438\u0430\u043b\u043e\u0433",
                "needs_review": True,
                "html":
                    f'<p><img src="{img("u2", "scene_canteen_order")}" alt="" style="max-width:100%"></p>'
                    "<p>\u041c\u043e\u0436\u0435\u0448\u044c \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435 \u043a\u0430\u043a \u043f\u0440\u0438\u043c\u0435\u0440.</p>"
                    "<p><b>Assistant:</b> <i>Hello! Can I help you?</i><br>"
                    "<b>Boy:</b> \u2026</p>",
            }),

            ("gaps", {
                "title": "\u042d\u0442\u043e \u0441\u0435\u043c\u044c\u044f \u0414\u0436\u043e\u043d\u0430. \u041f\u0440\u043e\u0447\u0438\u0442\u0430\u0439 \u0440\u0430\u0441\u0441\u043a\u0430\u0437 \u043e \u0435\u0433\u043e \u0443\u0436\u0438\u043d\u0435 \u0438 \u0437\u0430\u043f\u043e\u043b\u043d\u0438 \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0438 \u2b07",
                "mode": "drag",
                "image": img("u2", "scene_john_dinner"),
                "text":
                    "My __favourite__ dinner is chicken, peas and __chips__. "
                    "I have __dinner__ at 7 __o\u2019clock__. I __don\u2019t__ like fish and rice.",
                "gaps_expected": 5,
            }),

            ("speaking", {
                "title": "\u0420\u0430\u0441\u0441\u043a\u0430\u0436\u0438 \u043e \u0441\u0432\u043e\u0451\u043c \u0443\u0436\u0438\u043d\u0435 \U0001f3a4",
                "needs_review": True,
                "html":
                    "<p>\u041d\u0430\u0436\u043c\u0438 \u043d\u0430 \u043c\u0438\u043a\u0440\u043e\u0444\u043e\u043d \u0438 \u0440\u0430\u0441\u0441\u043a\u0430\u0436\u0438 \u043e \u0441\u0432\u043e\u0451\u043c \u0443\u0436\u0438\u043d\u0435. "
                    "\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439 \u0440\u0430\u0441\u0441\u043a\u0430\u0437 \u0414\u0436\u043e\u043d\u0430 \u043a\u0430\u043a \u043f\u0440\u0438\u043c\u0435\u0440.</p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_jump")}" alt="" style="height:180px"></p>'
                "<h3>\u0422\u044b \u0441\u043f\u0440\u0430\u0432\u0438\u043b\u0441\u044f \u0441\u043e \u0432\u0441\u0435\u043c\u0438 \u0437\u0430\u0434\u0430\u043d\u0438\u044f\u043c\u0438, \u0442\u0430\u043a \u0434\u0435\u0440\u0436\u0430\u0442\u044c!</h3>"}),
        ],
    },
    "u2_test": {
        "unit": "u2",
        "unit_title": "Unit 2 \u00b7 Food",
        "unit_sort": 2,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        # Нумерация блоков как в выгрузке: два match, пять «выбери правильный
        # вариант» (у нас quiz, по вопросу на каждый пропуск), пять «составь
        # предложение», две записи голоса. Картинки к match в выгрузке не было —
        # правая колонка пустая, подставлены наши карточки листов Л2.2 и Л2.3.
        "blocks": [
            ("match", {
                "title": "Соедини слова с картинками",
                "pairs": [
                    {"left_image": img("u2", "food_bread_rolls"), "right": "Rolls", "right_audio_tts": "rolls"},
                    {"left_image": img("u2", "food_vegetables"), "right": "Vegetables", "right_audio_tts": "vegetables"},
                    {"left_image": img("u2", "food_soup"), "right": "Soup", "right_audio_tts": "soup"},
                    {"left_image": img("u2", "food_water"), "right": "Water", "right_audio_tts": "water"},
                    {"left_image": img("u2", "food_peas"), "right": "Peas", "right_audio_tts": "peas"},
                    {"left_image": img("u2", "food_salad"), "right": "Salad", "right_audio_tts": "salad"},
                ],
            }),

            ("match", {
                "title": "Соедини слова с картинками",
                "pairs": [
                    {"left_image": img("u2", "food_pineapple"), "right": "Pineapple", "right_audio_tts": "pineapple"},
                    {"left_image": img("u2", "food_cheese"), "right": "Cheese", "right_audio_tts": "cheese"},
                    {"left_image": img("u2", "food_sausages"), "right": "Sausages", "right_audio_tts": "sausages"},
                    {"left_image": img("u2", "food_onions"), "right": "Onions", "right_audio_tts": "onions"},
                ],
            }),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: ___ any oranges?", "type": "single",
                 "options": [{"text": "Are there"}, {"text": "Is there"}], "correct": [0]},
                {"q": "B: No, ___.", "type": "single",
                 "options": [{"text": "there aren’t"}, {"text": "there isn’t"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: ___ there any water?", "type": "single",
                 "options": [{"text": "Is"}, {"text": "Are"}], "correct": [0]},
                {"q": "B: Yes, there ___.", "type": "single",
                 "options": [{"text": "is"}, {"text": "are"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "There are ___ onions on the table.", "type": "single",
                 "options": [{"text": "some"}, {"text": "any"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: Have we got ___ sandwiches?", "type": "single",
                 "options": [{"text": "any"}, {"text": "some"}], "correct": [0]},
                {"q": "B: Sorry, we haven’t got ___.", "type": "single",
                 "options": [{"text": "any"}, {"text": "some"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: ___ any pizza in the fridge?", "type": "single",
                 "options": [{"text": "Is there"}, {"text": "Are there"}], "correct": [0]},
                {"q": "B: Yes, ___.", "type": "single",
                 "options": [{"text": "there is"}, {"text": "there are"}], "correct": [0]},
            ]}),

            ("order", {
                "words": ["Shall", "we", "make", "some", "soup?"],
                "sentence": "Shall we make some soup?",
                "audio_tts": "Shall we make some soup?",
            }),

            ("order", {
                "words": ["How", "about", "some", "orange", "juice?"],
                "sentence": "How about some orange juice?",
                "audio_tts": "How about some orange juice?",
            }),

            ("order", {
                "words": ["Can", "I", "have", "some", "cheese", "sandwiches?"],
                "sentence": "Can I have some cheese sandwiches?",
                "audio_tts": "Can I have some cheese sandwiches?",
            }),

            ("order", {
                "words": ["We", "haven\u2019t", "got", "any", "pineapple", "juice."],
                "sentence": "We haven\u2019t got any pineapple juice.",
                "audio_tts": "We haven't got any pineapple juice.",
            }),

            ("order", {
                "words": ["I\u2019d", "like", "some", "lemonade,", "please."],
                "sentence": "I\u2019d like some lemonade, please.",
                "audio_tts": "I'd like some lemonade, please.",
            }),

            ("speaking", {
                "title": "SPEAKING TASK \u00b7 Part 1 \U0001f3a4",
                "needs_review": True,
                "html":
                    "<p>Расскажи о еде, которую ты любишь и не любишь. "
                    "Запиши свой ответ, нажав на кнопку микрофона.</p>"
                    "<p><i>For example:<br>My favourite food is\u2026<br>"
                    "I don\u2019t like eating\u2026</i></p>",
            }),

            ("speaking", {
                "title": "SPEAKING TASK \u00b7 Part 2 \U0001f3a4",
                "needs_review": True,
                "image": img("u2", "scene_cafe_menu"),
                "html":
                    "<p>Посмотри на картинку, ознакомься с меню. Затем составь диалог "
                    "посетителя и официанта и разыграй его. Запиши свой ответ, нажав "
                    "на кнопку микрофона.</p>"
                    "<p><i>For example:<br>"
                    "A: Would you like a chicken roll?<br>"
                    "B: No, thanks. I don\u2019t like chicken.<br>"
                    "A: Would you like a cheese sandwich?<br>"
                    "B: Yes, please. I\u2019d love one.</i></p>",
            }),
        ],
    },
    "u3_hw1": {
        "unit": "u3",
        "unit_title": "Unit 3 \u00b7 At home",
        "unit_sort": 3,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        # Обе части выгрузки одним уроком: «(1)» — словарный тренажёр на восемь
        # дел по дому, «(2)» — задания. Блок 8 в выгрузке был «Картинка» со
        # сканом образца («Write about you»); у нас это текст — так читается
        # лучше, а содержание то же.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>Привет-привет!</h2>"
                "<p>Сегодня мы будем изучать слова, которые ты проходил на уроке. "
                "Чем ты любишь заниматься дома? Выполни задания, повтори слова "
                "и ответь на вопрос :) Готов начать?</p>"}),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": img("u3", f)}
                for en, ru, f in U3_CHORES
            ]}),

            ("quiz", quiz_ru_to_en(U3_CHORES)),

            ("exact_input", {"items": [
                # en уже строчными, поэтому en.lower() дал бы дубль в accept
                {"image": img("u3", f), "prompt": "Посмотри на картинку и напиши, что здесь делают",
                 "accept": [en, en.capitalize()], "audio_tts": en}
                for en, ru, f in U3_CHORES
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("good_luck_clover")}" alt="" style="height:180px"></p>'
                "<h3>Это дополнительная часть домашней работы</h3>"
                "<p>Здесь тебя ждут очень интересные задания. Её можно выполнить "
                "по желанию — но если ты всё-таки её сделаешь, будет просто отлично \U0001f60a</p>"}),

            ("match", {
                "title": "Посмотри внимательно на слова и соедини первую часть фразы со второй",
                "pairs": [
                    {"left": "sweep", "right": "the floor", "right_audio_tts": "sweep the floor"},
                    {"left": "wash", "right": "up", "right_audio_tts": "wash up"},
                    {"left": "do", "right": "the shopping", "right_audio_tts": "do the shopping"},
                    {"left": "tidy", "right": "up your room", "right_audio_tts": "tidy up your room"},
                    {"left": "cook", "right": "the dinner", "right_audio_tts": "cook the dinner"},
                    {"left": "dry", "right": "the dishes", "right_audio_tts": "dry the dishes"},
                    {"left": "take", "right": "the dog for a walk",
                     "right_audio_tts": "take the dog for a walk"},
                    {"left": "feed", "right": "the dog", "right_audio_tts": "feed the dog"},
                ],
            }),

            ("match", {
                "title": "Молодец! Давай ещё потренируемся — соедини картинки с названиями",
                "pairs": [
                    {"left_image": img("u3", "chore_tidy_up"), "right": "tidy up",
                     "right_audio_tts": "tidy up"},
                    {"left_image": img("u3", "chore_sweep"), "right": "sweep",
                     "right_audio_tts": "sweep"},
                    {"left_image": img("u3", "chore_feed_dog"), "right": "feed the dog",
                     "right_audio_tts": "feed the dog"},
                    {"left_image": img("u3", "chore_dry_dishes"), "right": "dry the dishes",
                     "right_audio_tts": "dry the dishes"},
                    {"left_image": img("u3", "chore_do_shopping"), "right": "do the shopping",
                     "right_audio_tts": "do the shopping"},
                    {"left_image": img("u3", "chore_wash_up"), "right": "wash up",
                     "right_audio_tts": "wash up"},
                ],
            }),

            ("text", {"html":
                "<h3>WOW! Ты справился с основными заданиями. Осталось ещё одно \u2014 прочитай образец</h3>"
                "<p><b>Write about you.</b></p>"
                "<p><i>I like taking the dog for a walk. I don\u2019t like tidying up.</i></p>"}),

            ("task", {
                "title": "Теперь расскажи про себя!",
                "needs_review": True,
                "html":
                    "<p>Что ты любишь и не любишь делать по дому? Ориентируйся на образец выше.</p>"
                    "<p>Не забудь рассказать свой текст на уроке :)</p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_clap")}" alt="" style="height:180px"></p>'
                "<h3>Вот и всё, домашняя работа выполнена!</h3>"
                "<p>Огромное спасибо за твой труд. Увидимся на занятии!</p>"}),
        ],
    },
    "u3_hw2": {
        "unit": "u3",
        "unit_title": "Unit 3 \u00b7 At home",
        "unit_sort": 3,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        # Шесть «сколько времени на картинке?» в выгрузке опирались на фотографии
        # электронных часов из интернета (одна с водяным знаком стока, одна —
        # футболка с принтом). Те же шесть времён нарисованы своим табло,
        # tools/gen_clocks.py. Стрелочные циферблаты блока 3 — оттуда же.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_rocket")}" alt="" style="height:200px"></p>'
                "<h2>Привет!</h2>"
                "<p>Сегодня тебя ждёт много интересных заданий. Удачи тебе!</p>"
                "<p>Готов начать? Внимательно посмотри видео.</p>"}),

            ("video", {"title": "Видео: который час?", "url": "", "provider": ""}),

            ("match", {
                "title": "Посмотри видео ещё раз и соедини картинки с описанием",
                "pairs": [
                    {"left_image": svg("u3", "clock_quarter_past_eight"),
                     "right": "It\u2019s quarter past eight",
                     "right_audio_tts": "It's quarter past eight"},
                    {"left_image": svg("u3", "clock_half_past_eight"),
                     "right": "It\u2019s half past eight",
                     "right_audio_tts": "It's half past eight"},
                    {"left_image": svg("u3", "clock_quarter_past_five"),
                     "right": "It\u2019s quarter past five",
                     "right_audio_tts": "It's quarter past five"},
                    {"left_image": svg("u3", "clock_quarter_to_seven"),
                     "right": "It\u2019s quarter to seven",
                     "right_audio_tts": "It's quarter to seven"},
                    {"left_image": svg("u3", "clock_half_past_six"),
                     "right": "It\u2019s half past six",
                     "right_audio_tts": "It's half past six"},
                    {"left_image": svg("u3", "clock_twelve_oclock"),
                     "right": "It\u2019s twelve o\u2019clock",
                     "right_audio_tts": "It's twelve o'clock"},
                ],
            }),

            ("text", {"html":
                "<h3>Супер! Ты прекрасно справляешься!</h3>"
                "<p>Давай ещё немного потренируемся. Посмотри на картинки "
                "и опиши время, которое на них указано.</p>"}),

            ("task", {
                "title": "Сколько времени на картинке?",
                "needs_review": True,
                "html":
                    f'<p><img src="{svg("u3", "digital_two_fifteen")}" alt="" style="height:150px"></p>'
                    "<p>Опиши время по-английски.</p>",
            }),

            ("task", {
                "title": "Сколько времени на картинке?",
                "needs_review": True,
                "html":
                    f'<p><img src="{svg("u3", "digital_eleven_oclock")}" alt="" style="height:150px"></p>'
                    "<p>Опиши время по-английски.</p>",
            }),

            ("task", {
                "title": "Сколько времени на картинке?",
                "needs_review": True,
                "html":
                    f'<p><img src="{svg("u3", "digital_twelve_forty_five")}" alt="" style="height:150px"></p>'
                    "<p>Опиши время по-английски.</p>",
            }),

            ("task", {
                "title": "Сколько времени на картинке?",
                "needs_review": True,
                "html":
                    f'<p><img src="{svg("u3", "digital_nine_thirty")}" alt="" style="height:150px"></p>'
                    "<p>Опиши время по-английски.</p>",
            }),

            ("task", {
                "title": "Сколько времени на картинке?",
                "needs_review": True,
                "html":
                    f'<p><img src="{svg("u3", "digital_five_forty_five")}" alt="" style="height:150px"></p>'
                    "<p>Опиши время по-английски.</p>",
            }),

            ("task", {
                "title": "Сколько времени на картинке?",
                "needs_review": True,
                "html":
                    f'<p><img src="{svg("u3", "digital_eight_oclock")}" alt="" style="height:150px"></p>'
                    "<p>Опиши время по-английски.</p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>SUPER! Ты сделал все основные задания!</h3>"
                "<p>У меня есть для тебя ещё одно задание. Оно дополнительное, "
                "но если ты его сделаешь, получишь дополнительную \u2b50</p>"}),

            ("task", {
                "title": "Опиши свой день по времени",
                "needs_review": True,
                "html":
                    "<p>Напиши своё расписание и расскажи его учителю на уроке.</p>"
                    "<p><i>Пример:<br>I go to school at 8:30.<br>"
                    "I have lunch at 12 o\u2019clock.</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_jump")}" alt="" style="height:180px"></p>'
                "<h3>Ты справился, молодец!</h3>"
                "<p>Встретимся на уроке :)</p>"}),
        ],
    },
    "u3_hw3": {
        "unit": "u3",
        "unit_title": "Unit 3 \u00b7 At home",
        "unit_sort": 3,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        # Блок 3 «Диаграмма» — у нас hotspot: точки стоят ровно на оранжевых
        # кружках самой картинки (посчитаны по пикселям, а не на глаз).
        # Две картинки выгрузки не взяты: фотография игрушечного Базза Лайтера
        # и Микки-Маус с надписью BYE — чужие персонажи.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_headphones")}" alt="" style="height:200px"></p>'
                "<h2>Привет!</h2>"
                "<p>Сегодня мы послушаем с тобой песню и сделаем несколько "
                "интересных заданий. Удачи тебе!</p>"}),

            ("video", {"title": "Итак, поехали! Послушай песню. Кто главный герой?",
                       "url": "", "provider": ""}),

            ("hotspot", {
                "title": "Послушай песню ещё раз и выбери подходящее время для каждой картинки",
                "mode": "label",
                "image": img("u3", "scene_astronaut_day"),
                "points": [
                    {"x": 4.2,  "y": 7.1,  "text": "quarter to three",
                     "audio_tts": "quarter to three"},
                    {"x": 72.6, "y": 5.1,  "text": "nine o\u2019clock",
                     "audio_tts": "nine o'clock"},
                    {"x": 6.5,  "y": 56.7, "text": "half past nine",
                     "audio_tts": "half past nine"},
                    {"x": 38.3, "y": 60.1, "text": "half past ten",
                     "audio_tts": "half past ten"},
                    {"x": 70.6, "y": 57.0, "text": "half past three",
                     "audio_tts": "half past three"},
                ],
            }),

            ("gaps", {
                "title": "МОЛОДЕЦ! Послушай песню ещё раз и вставь пропущенные слова \u2b07",
                "mode": "drag",
                "text":
                    "1. She __gets up__ at quarter to three.\n"
                    "2. She __is at her door__ at nine o\u2019clock.\n"
                    "3. She __is in her spaceship__ at half past nine.\n"
                    "4. She __is on the moon__ at half past ten.\n"
                    "5. She __is back home__ at half past three.\n"
                    "6. She __works__ at night.",
                "gaps_expected": 6,
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_medal")}" alt="" style="height:180px"></p>'
                "<h3>Здорово! Ты сделал все основные задания!</h3>"
                "<p>У меня для тебя есть ещё одно задание. Оно дополнительное, "
                "но если ты его сделаешь, будешь ПРОСТО ГУРУ английского!</p>"}),

            ("task", {
                "title": "Представь, что ты пилот космического корабля!",
                "needs_review": True,
                "html":
                    "<p>Внимательно прочитай пример ниже и заполни его по-своему. "
                    "Опиши свой день!</p>"
                    "<p><i>I\u2019m in my spaceship. It\u2019s \u2026<br>"
                    "I\u2019m the pilot and \u2026<br>"
                    "It\u2019s \u2026, I\u2019m on the moon.<br>"
                    "\u2026 . \u2026 .</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_smiley")}" alt="" style="height:180px"></p>'
                "<h3>Ты справился, молодец!</h3>"
                "<p>Не забудь показать свой ответ на уроке учителю — он даст тебе "
                "дополнительный балл. BYE :)</p>"}),
        ],
    },
    "u3_hw4": {
        "unit": "u3",
        "unit_title": "Unit 3 \u00b7 At home",
        "unit_sort": 3,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        # Обе части выгрузки одним уроком. Нумерация блоков 1-11 совпадает
        # с частью «(1)»; словарный тренажёр на дни недели из части «(2)»
        # вставлен блоками 12-14, перед прощанием.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_laptop")}" alt="" style="height:200px"></p>'
                "<h2>Привет!</h2>"
                "<p>Сегодня мы повторим с тобой тему <b>Time</b>. Тебя ждёт много "
                "крутых упражнений для тренировки. Поехали!</p>"}),

            ("match", {
                "title": "Первое задание: сопоставь время с картинками",
                "pairs": [
                    {"left_image": svg("u3", "clock_twenty_to_four"),
                     "right": "It\u2019s twenty to four.",
                     "right_audio_tts": "It's twenty to four."},
                    {"left_image": svg("u3", "clock_quarter_past_three"),
                     "right": "It\u2019s quarter past three.",
                     "right_audio_tts": "It's quarter past three."},
                    {"left_image": svg("u3", "clock_half_past_six"),
                     "right": "It\u2019s half past six.",
                     "right_audio_tts": "It's half past six."},
                    {"left_image": svg("u3", "clock_quarter_to_five"),
                     "right": "It\u2019s quarter to five.",
                     "right_audio_tts": "It's quarter to five."},
                    {"left_image": svg("u3", "clock_six_oclock"),
                     "right": "It\u2019s six o\u2019clock.",
                     "right_audio_tts": "It's six o'clock."},
                    {"left_image": svg("u3", "clock_quarter_past_eight"),
                     "right": "It\u2019s quarter past eight.",
                     "right_audio_tts": "It's quarter past eight."},
                ],
            }),

            ("text", {"html":
                "<h3>Внимательно прочитай правило!</h3>"
                f'<p><img src="{img("u3", "rule_adverbs_time")}" alt="Adverbs for time" '
                'style="max-width:100%"></p>'}),

            ("order", {
                "words": ["I", "always", "brush", "my", "teeth", "after", "dinner."],
                "sentence": "I always brush my teeth after dinner.",
                "audio_tts": "I always brush my teeth after dinner.",
            }),

            ("order", {
                "words": ["My", "father", "never", "goes", "to", "bed", "early."],
                "sentence": "My father never goes to bed early.",
                "audio_tts": "My father never goes to bed early.",
            }),

            ("order", {
                "words": ["My", "sister", "usually", "does", "lots", "of", "homework",
                          "at", "the weekend."],
                "sentence": "My sister usually does lots of homework at the weekend.",
                "audio_tts": "My sister usually does lots of homework at the weekend.",
            }),

            ("order", {
                "words": ["My", "mother", "sometimes", "does", "the shopping", "on", "Fridays."],
                "sentence": "My mother sometimes does the shopping on Fridays.",
                "audio_tts": "My mother sometimes does the shopping on Fridays.",
            }),

            ("order", {
                "words": ["My", "brother", "always", "goes", "to", "bed", "at", "ten",
                          "o\u2019clock."],
                "sentence": "My brother always goes to bed at ten o\u2019clock.",
                "audio_tts": "My brother always goes to bed at ten o'clock.",
            }),

            ("text", {"html":
                "<h3>Прочитай новое правило!</h3>"
                f'<p><img src="{img("u3", "table_family_chores")}" alt="" '
                'style="max-width:100%"></p>'
                "<p><b>Always</b> \u2714\u2714\u2714 \u00b7 <b>Usually</b> \u2714\u2714 \u00b7 "
                "<b>Sometimes</b> \u2714 \u00b7 <b>Never</b> \u2716</p>"}),

            ("gaps", {
                "title": "Прочитай правило ещё раз и выполни упражнение \u2b07",
                "mode": "drag",
                "text":
                    "1. I __never__ feed the cat.\n"
                    "2. Mum __usually__ dries the dishes.\n"
                    "3. Dad __always__ washes up.\n"
                    "4. My brother __sometimes__ dries the dishes.\n"
                    "5. My sister __never__ washes up.\n"
                    "6. My brother __never__ feeds the cat.\n"
                    "7. I __never__ cook.",
                "gaps_expected": 7,
            }),

            ("task", {
                "title": "Напиши 6 предложений про свою семью",
                "needs_review": True,
                "html":
                    "<p>Молодец! Ты выполнил все основные задания. Осталось последнее \u2014 "
                    "оно необязательное, но если ты его сделаешь, будешь СУПЕР КРУТЫМ учеником!</p>"
                    "<p><i>Например: Mum cooks every day. Dad always feeds the dog.</i></p>",
            }),

            ("flashcards", {"title": "Дни недели", "cards": [
                {"text": en, "translation": ru, "audio_tts": en} for en, ru in U3_DAYS
            ]}),

            ("quiz", {"title": "Как это по-английски?", "questions": [
                {"q": f"Как по-английски \u00ab{ru}\u00bb?", "type": "single",
                 "options": [{"text": o} for o in sorted(
                     [en] + [U3_DAYS[(i + k) % len(U3_DAYS)][0] for k in (1, 2, 3)])],
                 "correct": [sorted(
                     [en] + [U3_DAYS[(i + k) % len(U3_DAYS)][0] for k in (1, 2, 3)]).index(en)]}
                for i, (en, ru) in enumerate(U3_DAYS)
            ]}),

            ("exact_input", {"items": [
                {"prompt": f"Напиши по-английски: {ru}", "accept": [en, en.lower()],
                 "audio_tts": en}
                for en, ru in U3_DAYS
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>Поздравляю! Ты завершил домашнее задание!</h3>"
                "<p>Ты замечательный ученик. За это лови звёздочку :) "
                "Увидимся на занятии!</p>"}),
        ],
    },
    "u3_hw5": {
        "unit": "u3",
        "unit_title": "Unit 3 \u00b7 At home",
        "unit_sort": 3,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        # Кадры истории (1-6, 7-8) и картинка к тесту (кадры 1, 3, 6, 8)
        # вырезаны из PDF выгрузки: в редакторе оба блока «Картинка» пустые.
        # В выгрузке опечатка «tommorow» — на самом кадре истории написано
        # tomorrow, так и залито.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_highfive")}" alt="" style="height:200px"></p>'
                "<h2>HELLO! Рад тебя видеть!</h2>"
                "<p>Сегодня мы вспомним с тобой историю, которую ты смотрел на уроке. "
                "Поехали!</p>"}),

            ("text", {"html":
                "<h3>Прочитай историю!</h3>"
                f'<p><img src="{img("u3", "story_letter_f_1")}" alt="" style="max-width:100%"></p>'}),

            ("text", {"html":
                f'<p><img src="{img("u3", "story_letter_f_2")}" alt="" style="max-width:100%"></p>'}),

            ("order", {
                "words": ["Let\u2019s", "look", "for", "it", "tomorrow", "morning."],
                "sentence": "Let\u2019s look for it tomorrow morning.",
                "audio_tts": "Let's look for it tomorrow morning.",
            }),

            ("order", {
                "words": ["Let\u2019s", "wait", "for", "dark."],
                "sentence": "Let\u2019s wait for dark.",
                "audio_tts": "Let's wait for dark.",
            }),

            ("order", {
                "words": ["I", "don\u2019t", "like", "this", "village."],
                "sentence": "I don\u2019t like this village.",
                "audio_tts": "I don't like this village.",
            }),

            ("order", {
                "words": ["Let\u2019s", "go", "soon."],
                "sentence": "Let\u2019s go soon.",
                "audio_tts": "Let's go soon.",
            }),

            ("order", {
                "words": ["What", "a", "mess!"],
                "sentence": "What a mess!",
                "audio_tts": "What a mess!",
            }),

            ("quiz", {"questions": [
                {"q": "Look at pictures 1 and 3. What\u2019s the same about Ben and Zelda?",
                 "type": "single",
                 "image": img("u3", "story_letter_f_quiz"),
                 "options": [{"text": "They are angry."}, {"text": "They are tired."},
                             {"text": "They are hungry."}],
                 "correct": [1]},
            ]}),

            ("quiz", {"questions": [
                {"q": "Look at picture 8. What\u2019s the same about Lucy and Ben?",
                 "type": "single",
                 "image": img("u3", "story_letter_f_quiz"),
                 "options": [{"text": "They are sad."}, {"text": "They are angry."},
                             {"text": "They are excited."}],
                 "correct": [2]},
            ]}),

            ("quiz", {"questions": [
                {"q": "Look at pictures 6 and 8. What\u2019s different about Lucy?",
                 "type": "single",
                 "image": img("u3", "story_letter_f_quiz"),
                 "options": [{"text": "First she is happy, then she is unhappy."},
                             {"text": "First she is unhappy, then she is happy."},
                             {"text": "First she is scared, then she is not tired."}],
                 "correct": [1]},
            ]}),

            ("task", {
                "title": "Answer the questions about the story",
                "needs_review": True,
                "html":
                    "<ol>"
                    "<li>What time do Horax and Zelda go home?</li>"
                    "<li>Where does Ben look for the letter first?</li>"
                    "<li>Where does Lucy find the letter?</li>"
                    "<li>What is the second letter?</li>"
                    "</ol>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>Ты со всем справился!</h3>"
                "<p>ЛОВИ ЗВЁЗДОЧКУ! Увидимся на уроке! Bye!</p>"}),
        ],
    },
    "u3_hw6": {
        "unit": "u3",
        "unit_title": "Unit 3 \u00b7 At home",
        "unit_sort": 3,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        # Обе страницы сказки вырезаны из PDF: в редакторе блоки «Картинка»
        # пустые. Блоки 7 и 8 в выгрузке были «Текст» — у нас открытые
        # вопросы, ребёнку нужно место для ответа.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_book")}" alt="" style="height:200px"></p>'
                "<h2>ПРИВЕТ-ПРИВЕТ!</h2>"
                "<p>Сегодня мы с тобой будем читать сказку. Ты любишь сказки?</p>"
                "<p>Как думаешь, кто главный герой истории? Прочитай текст ниже "
                "и ответь на вопрос :)</p>"}),

            ("text", {"html":
                f'<p><img src="{img("u3", "story_shoemaker_1")}" '
                'alt="The shoemaker and the elves" style="max-width:100%"></p>'}),

            ("text", {"html":
                f'<p><img src="{img("u3", "story_shoemaker_2")}" alt="" style="max-width:100%"></p>'}),

            ("truefalse", {
                "title": "Прочитай предложения и скажи, это правда (True) или неправда (False)",
                "statements": [
                    {"text": "The shoemaker works a lot of hours.", "correct": True},
                    {"text": "The shoemaker works hard but has little money.", "correct": True},
                    {"text": "Every morning he finds new shoes on the table.", "correct": True},
                    {"text": "The elves work after 5 o\u2019clock in the morning.", "correct": False},
                    {"text": "The shoemaker makes nice clothes for the elves to thank them.",
                     "correct": True},
                    {"text": "The elves still make shoes for the shoemaker.", "correct": False},
                ],
            }),

            ("gaps", {
                "title": "Расставь слова на свои места \u2b07",
                "mode": "drag",
                "text":
                    "There is a __shoemaker__ who works very hard. One night, he cuts some "
                    "__leather__ and leaves it on the kitchen table. In the morning, there are "
                    "ten pairs of beautiful shoes. The __next__ morning there are twenty pairs "
                    "of beautiful shoes. Every night, he leaves leather on the table and "
                    "__every__ morning there are beautiful new shoes. Soon, everyone in the town "
                    "wants more shoes from the shoemaker. But the shoemaker __doesn\u2019t__ know "
                    "who makes the shoes. One night he hides under a table and sees five elves "
                    "making shoes. They are wearing __old__ clothes. The shoemaker makes nice "
                    "clothes for the elves. The elves take the clothes but they don\u2019t come "
                    "back to make new shoes. The shoemaker doesn\u2019t mind because he wants "
                    "the elves to be __happy__.",
                "gaps_expected": 7,
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_clap")}" alt="" style="height:180px"></p>'
                "<h3>Молодец! Ты отлично справляешься!</h3>"
                "<p>Осталось последнее задание. Оно дополнительное, но если ты его "
                "сделаешь, получишь \u2b50</p>"}),

            ("task", {
                "title": "Кто твой любимый сказочный герой?",
                "needs_review": True,
                "html": "<p>Напиши его имя.</p>",
            }),

            ("task", {
                "title": "Опиши день своего героя",
                "needs_review": True,
                "html":
                    "<p>Используй выражения из текста сказки.</p>"
                    "<p><i>Например: William wakes up at 8 o\u2019clock and brushes his teeth. "
                    "He has breakfast at 9 o\u2019clock\u2026</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>SUPER! Ты выполнил все задания!</h3>"
                "<p>Ты БОЛЬШОЙ МОЛОДЕЦ! Увидимся на уроке!</p>"}),
        ],
    },
    "u3_hw7": {
        "unit": "u3",
        "unit_title": "Unit 3 \u00b7 At home",
        "unit_sort": 3,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        # Обе части выгрузки одним уроком. «Найди пару» из части «(1)» не
        # дублируется: то же задание (картинка - слово) стоит блоком 5 из
        # части «(2)». В выгрузке профессия написана двояко — «fire fighter»
        # в части (1) и «firefighter» в части (2); оставлено firefighter.
        # Образец «A Police Officer's Diary» в выгрузке был картинкой-сканом;
        # у нас он текстом — читается лучше, содержание то же.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_rocket")}" alt="" style="height:200px"></p>'
                "<h2>Привет!</h2>"
                "<p>Сегодня мы повторим с тобой профессии, которые ты изучил на занятии. "
                "Тебя ждёт много интересных заданий. Готов начать?</p>"}),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": img("u3", f)}
                for en, ru, f in U3_JOBS
            ]}),

            ("exact_input", {"items": [
                {"image": img("u3", f), "prompt": "Посмотри на картинку и напиши профессию",
                 "accept": [en, en.capitalize()], "audio_tts": en}
                for en, ru, f in U3_JOBS
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("good_luck_clover")}" alt="" style="height:180px"></p>'
                "<h3>HELLO! Добро пожаловать в дополнительное домашнее задание!</h3>"
                "<p>Сегодня мы повторим слова, которые ты изучал на уроке. "
                "Готов начать тренироваться?</p>"}),

            ("match", {
                "title": "Внимательно посмотри на картинки и соедини слова с подходящими изображениями",
                "pairs": [
                    {"left_image": img("u3", f), "right": en, "right_audio_tts": en}
                    for en, ru, f in U3_JOBS
                ],
            }),

            ("match", {
                "title": "МОЛОДЕЦ! Давай ещё потренируемся \u2014 прочитай описание "
                         "и выбери соответствующую профессию",
                "pairs": [
                    {"left": "cleaner", "right": "This person cleans the town.",
                     "right_audio_tts": "This person cleans the town."},
                    {"left": "police officer", "right": "This person helps people.",
                     "right_audio_tts": "This person helps people."},
                    {"left": "teacher", "right": "This person teaches people.",
                     "right_audio_tts": "This person teaches people."},
                    {"left": "vet", "right": "This person looks after animals.",
                     "right_audio_tts": "This person looks after animals."},
                    {"left": "firefighter", "right": "This person stops fire.",
                     "right_audio_tts": "This person stops fire."},
                    {"left": "ambulance driver",
                     "right": "This person takes ill people to hospital.",
                     "right_audio_tts": "This person takes ill people to hospital."},
                ],
            }),

            ("text", {"html":
                "<h3>УРА! Осталось последнее задание \u2014 внимательно прочитай текст</h3>"
                "<p><b>Project.</b> Choose a job that people do at night. "
                "Write a diary for their day or night.</p>"
                "<p><b>A Police Officer\u2019s Diary</b><br><i>Night</i><br>"
                "6 o\u2019clock \u2014 I wake up and have breakfast.<br>"
                "7 o\u2019clock \u2014 I feed the dog and then I cycle to work.<br>"
                "9 o\u2019clock \u2014 I usually have a break and drink some tea.<br>"
                "12 o\u2019clock \u2014 I have a sandwich for lunch.<br>"
                "5 o\u2019clock \u2014 I finish work and I sometimes have dinner "
                "with the other police officers.</p>"}),

            ("task", {
                "title": "Выбери работу, которую люди выполняют по ночам",
                "needs_review": True,
                "html":
                    f'<p><img src="{img("u3", "scene_night_jobs")}" alt="" style="max-width:100%"></p>'
                    "<p>Опиши график работы как в примере выше. "
                    "Не забудь показать свой текст учителю :)</p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_jump")}" alt="" style="height:180px"></p>'
                "<h3>Ура! Ты выполнил все задания!</h3>"
                "<p>ТЫ СУПЕР КРУТ! BYE :)</p>"}),
        ],
    },
    "u3_test": {
        "unit": "u3",
        "unit_title": "Unit 3 \u00b7 At home",
        "unit_sort": 3,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        # Нумерация блоков как в выгрузке: match, «заполни пропуски» по картинке,
        # пять «выбери правильный вариант» (у нас quiz, чтобы сохранить неверные
        # варианты), пять «составь предложение», запись голоса.
        # Картинки к блоку 1 в выгрузке не было — взяты наши карточки дел по дому.
        # В выгрузке опечатка «I olay with my friends» — залито play.
        "blocks": [
            ("match", {
                "title": "Соедини слова с картинками",
                "pairs": [
                    {"left_image": img("u3", "chore_tidy_up"), "right": "Tidy up",
                     "right_audio_tts": "tidy up"},
                    {"left_image": img("u3", "chore_walk_dog"), "right": "Take the dog for a walk",
                     "right_audio_tts": "take the dog for a walk"},
                    {"left_image": img("u3", "chore_do_shopping"), "right": "Do the shopping",
                     "right_audio_tts": "do the shopping"},
                    {"left_image": img("u3", "chore_wash_up"), "right": "Wash up",
                     "right_audio_tts": "wash up"},
                    {"left_image": img("u3", "chore_sweep"), "right": "Sweep",
                     "right_audio_tts": "sweep"},
                ],
            }),

            ("gaps", {
                "title": "Посмотри на картинку и заполни пропуски \u2b07",
                "mode": "drag",
                "image": img("u3", "scene_day_times"),
                "text":
                    "1. I __take the dog for a walk__ at quarter past seven.\n"
                    "2. I __do homework__ at six o\u2019clock.\n"
                    "3. I go to bed at __half past ten__.\n"
                    "4. I clean my room at __half past eight__.\n"
                    "5. I play with my friends at __eleven o\u2019clock__.",
                "gaps_expected": 5,
            }),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: I think you like ___ up your room.", "type": "single",
                 "options": [{"text": "tidying"}, {"text": "tidy"}, {"text": "wash"}],
                 "correct": [0]},
                {"q": "B: No, I ___ like it.", "type": "single",
                 "options": [{"text": "don\u2019t"}, {"text": "do"}, {"text": "does"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: I like ___ the dog for a walk. B: Me too.", "type": "single",
                 "options": [{"text": "taking"}, {"text": "take"}, {"text": "walk"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: What time do you go to bed? B: At ___ past eleven.", "type": "single",
                 "options": [{"text": "half"}, {"text": "quarter"}], "correct": [0]},
                {"q": "B: At half past ___.", "type": "single",
                 "options": [{"text": "11"}, {"text": "10"}, {"text": "12"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "I have breakfast at quarter ___ eight.", "type": "single",
                 "options": [{"text": "to"}, {"text": "half"}, {"text": "past"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "I ___ sweep the floor at the weekend. I like it a lot!", "type": "single",
                 "options": [{"text": "always"}, {"text": "never"}], "correct": [0]},
            ]}),

            ("order", {
                "words": ["Do", "you", "like", "doing", "shopping?"],
                "sentence": "Do you like doing shopping?",
                "audio_tts": "Do you like doing shopping?",
            }),

            ("order", {
                "words": ["I", "don\u2019t", "like", "washing", "up."],
                "sentence": "I don\u2019t like washing up.",
                "audio_tts": "I don't like washing up.",
            }),

            ("order", {
                "words": ["My mum", "and", "I", "cook", "dinner", "at", "half", "past", "six."],
                "sentence": "My mum and I cook dinner at half past six.",
                "audio_tts": "My mum and I cook dinner at half past six.",
            }),

            ("order", {
                "words": ["I", "sometimes", "tidy", "up", "my", "room."],
                "sentence": "I sometimes tidy up my room.",
                "audio_tts": "I sometimes tidy up my room.",
            }),

            ("order", {
                "words": ["Do", "you", "always", "wash", "your", "clothes?"],
                "sentence": "Do you always wash your clothes?",
                "audio_tts": "Do you always wash your clothes?",
            }),

            ("speaking", {
                "title": "SPEAKING TASK \U0001f3a4",
                "needs_review": True,
                "html":
                    "<p>Расскажи о распорядке своего дня (5\u20137 предложений). "
                    "Запиши свой ответ, нажав на кнопку микрофона.</p>"
                    "<p><i>For example: I take my dog for a walk at 8 o\u2019clock.</i></p>",
            }),
        ],
    },
    "u4_hw1": {
        "unit": "u4",
        "unit_title": "Unit 4 \u00b7 In the town",
        "unit_sort": 4,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        # В выгрузке это только словарный тренажёр на 13 слов, без заданий.
        # Прощание дописано: урок ребёнок открывает отдельно, а в выгрузке
        # у тренажёра концовки не бывает вовсе.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>Привет! How are you?</h2>"
                "<p>Сегодня мы выучим слова, которые ты изучил на занятии. Поехали!</p>"}),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": img("u4", f)}
                for en, ru, f in U4_TOWN
            ]}),

            ("quiz", quiz_ru_to_en(U4_TOWN)),

            ("exact_input", {"items": [
                {"image": img("u4", f), "prompt": "Посмотри на картинку и напиши слово",
                 "accept": [en, en.capitalize()], "audio_tts": en}
                for en, ru, f in U4_TOWN
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>Отлично! Слова выучены.</h3>"
                "<p>Увидимся на уроке!</p>"}),
        ],
    },
    "u4_hw2": {
        "unit": "u4",
        "unit_title": "Unit 4 \u00b7 In the town",
        "unit_sort": 4,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        # В выгрузке 11 блоков, у нас 12: картинка города вынесена отдельным
        # блоком 9, иначе внутри задания она ужимается до 220 px и подписи
        # CINEMA, LIBRARY не прочитать. Дальше номера сдвинуты на один.
        # К шести «составь предложение» подставлены наши картинки предлогов —
        # в выгрузке их не было.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_highfive")}" alt="" style="height:200px"></p>'
                "<h2>HELLO! Добро пожаловать в домашнее задание!</h2>"
                "<p>Сегодня мы будем повторять предлоги. Внимательно посмотри видео "
                "и сделай задания ниже.</p>"}),

            ("video", {"title": "Видео: предлоги места", "url": "", "provider": ""}),

            ("order", {
                "image": img("u4", "prep_cat_under_sofa"),
                "words": ["The", "cat", "is", "under", "the", "sofa."],
                "sentence": "The cat is under the sofa.",
                "audio_tts": "The cat is under the sofa.",
            }),

            ("order", {
                "image": img("u4", "prep_cat_dog_opposite"),
                "words": ["The", "cat", "is", "opposite", "the", "dog."],
                "sentence": "The cat is opposite the dog.",
                "audio_tts": "The cat is opposite the dog.",
            }),

            ("order", {
                "image": img("u4", "prep_cat_below_shelf"),
                "words": ["The", "cat", "is", "below", "the", "shelf."],
                "sentence": "The cat is below the shelf.",
                "audio_tts": "The cat is below the shelf.",
            }),

            ("order", {
                "image": img("u4", "prep_fox_in_front_of_box"),
                "words": ["The", "fox", "is", "in front of", "the", "box."],
                "sentence": "The fox is in front of the box.",
                "audio_tts": "The fox is in front of the box.",
            }),

            ("order", {
                "image": img("u4", "prep_mouse_between_boxes"),
                "words": ["The", "mouse", "is", "between", "the", "boxes."],
                "sentence": "The mouse is between the boxes.",
                "audio_tts": "The mouse is between the boxes.",
            }),

            ("order", {
                "image": img("u4", "prep_monkey_behind_tree"),
                "words": ["The", "monkey", "is", "behind", "the", "tree."],
                "sentence": "The monkey is behind the tree.",
                "audio_tts": "The monkey is behind the tree.",
            }),

            ("text", {"html":
                "<h3>Посмотри на картинку — какие места есть в городе?</h3>"
                f'<p><img src="{img("u4", "scene_town_prepositions")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("quiz", {"title": "Выбери правильный вариант", "questions": [
                {"q": "1. The cinema is ___ the library.", "type": "single",
                 "options": [{"text": "opposite"}, {"text": "between"}], "correct": [0]},
                {"q": "2. The tower is ___ the cinema.", "type": "single",
                 "options": [{"text": "behind"}, {"text": "above"}], "correct": [0]},
                {"q": "3. The park is ___ the school.", "type": "single",
                 "options": [{"text": "opposite"}, {"text": "near"}], "correct": [0]},
                {"q": "4. The boat is ___ the bridge.", "type": "single",
                 "options": [{"text": "below"}, {"text": "above"}], "correct": [0]},
                {"q": "5. The sports centre is ___ the cinema and the cafe.", "type": "single",
                 "options": [{"text": "between"}, {"text": "in front of"}], "correct": [0]},
                {"q": "6. The castle is ___ the sports centre.", "type": "single",
                 "options": [{"text": "behind"}, {"text": "opposite"}], "correct": [0]},
            ]}),

            ("task", {
                "title": "Напиши три предложения про свой город",
                "needs_review": True,
                "html":
                    "<p>СУПЕР! Ты прекрасно со всем справляешься. У меня есть для тебя "
                    "ещё одно задание — оно дополнительное, но если ты его сделаешь, "
                    "получишь дополнительную \u2b50</p>"
                    "<p><i>Например: The cinema is behind the shop.</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_jump")}" alt="" style="height:180px"></p>'
                "<h3>УРА! У тебя получилось!</h3>"
                "<p>Не забудь показать свой текст на занятии. Увидимся!</p>"}),
        ],
    },
    "u4_hw3": {
        "unit": "u4",
        "unit_title": "Unit 4 \u00b7 In the town",
        "unit_sort": 4,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        # Блок 3 «Диаграмма» — у нас hotspot: точки стоят у номеров (1)-(4)
        # на самой картинке, координаты посчитаны по оранжевым цифрам.
        # Шаблон песни для блока 4 в выгрузке был картинкой-сканом; у нас он
        # текстом — читается лучше, содержание то же.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_headphones")}" alt="" style="height:200px"></p>'
                "<h2>Привет!</h2>"
                "<p>Сегодня мы послушаем с тобой песню и сделаем несколько интересных "
                "заданий. Удачи тебе!</p>"}),

            ("video", {"title": "Итак, поехали! Послушай песню. Кто главный герой?",
                       "url": "", "provider": ""}),

            ("hotspot", {
                "title": "Послушай песню ещё раз и расставь пропущенные слова. "
                         "Осторожно: в задании ДВА ЛИШНИХ СЛОВА!",
                "mode": "label",
                "image": img("u4", "song_lost_in_town"),
                "points": [
                    {"x": 19.0, "y": 11.4, "text": "Opposite", "audio_tts": "opposite"},
                    {"x": 23.0, "y": 41.0, "text": "below", "audio_tts": "below"},
                    {"x": 18.0, "y": 46.0, "text": "near", "audio_tts": "near"},
                    {"x": 18.0, "y": 66.8, "text": "in front of", "audio_tts": "in front of"},
                ],
                "extras": ["between", "above"],
            }),

            ("task", {
                "title": "Придумай свою версию песни",
                "needs_review": True,
                "html":
                    "<p>У меня для тебя есть ещё одно задание. Оно дополнительное, "
                    "но если ты его сделаешь, будешь ПРОСТО ГУРУ английского!</p>"
                    "<p>Послушай песню ещё раз и заполни пропуски своими местами в городе:</p>"
                    "<p><i>Opposite the \u2026,<br>In the \u2026,<br>"
                    "I\u2019m looking for the \u2026<br>But it\u2019s not there.</i></p>"
                    "<p><i>Just below the \u2026,<br>Near the \u2026,<br>"
                    "My map says there\u2019s a \u2026<br>But there is not.</i></p>"
                    "<p><i>In front of the \u2026,<br>In the \u2026,<br>"
                    "There\u2019s a place<br>Where people always meet.</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_smiley")}" alt="" style="height:180px"></p>'
                "<h3>Ты справился, молодец!</h3>"
                "<p>Не забудь показать свой ответ на уроке учителю — он даст тебе "
                "дополнительный балл. BYE :)</p>"}),
        ],
    },
    "u4_hw4": {
        "unit": "u4",
        "unit_title": "Unit 4 \u00b7 In the town",
        "unit_sort": 4,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        # В выгрузке 16 блоков, у нас 12: пять блоков «Верно/неверно» с одним
        # утверждением каждый сведены в один блок с пятью. У нас truefalse на
        # то и рассчитан, а пять кнопок «Проверить» подряд ребёнку ни к чему.
        # Правило Language focus в выгрузке было картинкой-сканом — у нас текст.
        # В выгрузке «sports center», в словаре юнита «sports centre» —
        # оставлено centre.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_highfive")}" alt="" style="height:200px"></p>'
                "<h2>Hi! Happy to see you!</h2>"
                "<p>Сегодня тебя ждёт много интересных заданий. Готов начать?</p>"}),

            ("text", {"html":
                "<h3>Внимательно прочитай правило</h3>"
                "<p><b>Language focus.</b> Use <b>be going to</b> + <b>infinitive of "
                "purpose</b> to tell someone where you are going and why you are going "
                "there.</p>"
                "<p><i>Where are you going?</i> \u2014 I <b>am going to</b> the market "
                "<b>to buy</b> some fruit and vegetables.<br>"
                "<i>Where is he / she going?</i> \u2014 He / she <b>is going to</b> the "
                "sports centre <b>to play</b> table tennis.<br>"
                "<i>Where are we / they going?</i> \u2014 We / they <b>are going to</b> "
                "the caf\u00e9 <b>to have</b> lunch.</p>"
                "<p>А теперь перейдём к заданиям!</p>"}),

            ("order", {
                "words": ["Mandy", "is", "going", "to", "the", "square", "to meet",
                          "her", "cousin."],
                "sentence": "Mandy is going to the square to meet her cousin.",
                "audio_tts": "Mandy is going to the square to meet her cousin.",
            }),

            ("order", {
                "words": ["Richard and Pierre", "are", "going", "to the", "cinema",
                          "to watch", "a new", "film."],
                "sentence": "Richard and Pierre are going to the cinema to watch a new film.",
                "audio_tts": "Richard and Pierre are going to the cinema to watch a new film.",
            }),

            ("order", {
                "words": ["Serge", "is", "going", "to the", "library", "to get",
                          "some books", "for his science project."],
                "sentence": "Serge is going to the library to get some books for his science project.",
                "audio_tts": "Serge is going to the library to get some books for his science project.",
            }),

            ("order", {
                "words": ["Martina", "is", "going", "to the", "market", "to buy",
                          "a birthday present", "for her sister."],
                "sentence": "Martina is going to the market to buy a birthday present for her sister.",
                "audio_tts": "Martina is going to the market to buy a birthday present for her sister.",
            }),

            ("order", {
                "words": ["Emma", "is", "going", "to the", "sports centre", "to go", "swimming."],
                "sentence": "Emma is going to the sports centre to go swimming.",
                "audio_tts": "Emma is going to the sports centre to go swimming.",
            }),

            ("order", {
                "words": ["We", "are", "going", "to the", "caf\u00e9", "to drink",
                          "some", "milkshakes."],
                "sentence": "We are going to the caf\u00e9 to drink some milkshakes.",
                "audio_tts": "We are going to the cafe to drink some milkshakes.",
            }),

            ("text", {"html":
                "<h3>Молодец! А теперь прочитай внимательно текст</h3>"
                f'<p><img src="{img("u4", "postcard_ali")}" alt="Reading: a postcard" '
                'style="max-width:100%"></p>'}),

            ("truefalse", {
                "title": "Прочитай открытку выше. Выбери «верно», если предложение "
                         "верное, и «неверно», если нет",
                "statements": [
                    {"text": "It\u2019s the second (2nd) week of Ali\u2019s school trip.",
                     "correct": False},
                    {"text": "Ali\u2019s hotel is next to a museum.", "correct": False},
                    {"text": "The tower isn\u2019t a new building.", "correct": True},
                    {"text": "Below the tower there is a square.", "correct": True},
                    {"text": "There aren\u2019t any paintings by famous artists in the museum.",
                     "correct": False},
                ],
            }),

            ("task", {
                "title": "Напиши 3\u20136 предложений про свои планы",
                "needs_review": True,
                "html":
                    "<p>Ура! Ты уже так много сделал. У меня для тебя ещё одно задание: "
                    "представь, что ты отправился в путешествие.</p>"
                    "<p><i>Например:<br>I\u2019m going to the market to\u2026<br>"
                    "I\u2019m going to the park to\u2026</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>Ты просто СУПЕРКРУТ!</h3>"
                "<p>Настоящий гуру английского. Так держать :) Увидимся на уроке!</p>"}),
        ],
    },
    "u4_hw5": {
        "unit": "u4",
        "unit_title": "Unit 4 \u00b7 In the town",
        "unit_sort": 4,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        # Блок 4 в выгрузке — «Заполни пропуски» с двумя лишними словами.
        # Наш gaps в режиме drag строит набор только из верных ответов, лишних
        # слов в нём не бывает. Поэтому режим «впиши», а все семь слов (с двумя
        # лишними) названы в заголовке — задумка сохранена.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_book")}" alt="" style="height:200px"></p>'
                "<h2>Привет-привет!</h2>"
                "<p>Сегодня мы вспомним историю, которую ты смотрел на уроке. "
                "Кто в ней главный герой?</p>"
                "<p>Прочитай историю ниже и сделай задания к ней.</p>"}),

            ("text", {"html":
                f'<p><img src="{img("u4", "story_pirate_ship_1")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("text", {"html":
                f'<p><img src="{img("u4", "story_pirate_ship_2")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("gaps", {
                "title": "Прочитай текст ещё раз и впиши слова в пропуски по смыслу. "
                         "Слова: letter \u00b7 dog \u00b7 near \u00b7 going \u00b7 high \u00b7 "
                         "cat \u00b7 museum. Два слова лишние!",
                "text":
                    "1. Lucy and Ben are going to the tower to get the next __letter__.\n"
                    "2. Lucy and Ben have got their __dog__ with them.\n"
                    "3. Look, the tower\u2019s over there, the school\u2019s __near__.\n"
                    "4. \u2018Lucy! Where are you __going__?\u2019\n"
                    "5. Lucy and Ben are really __high__ on the Pirate Ship.",
                "gaps_expected": 5,
            }),

            ("sequence", {
                "title": "Молодец! Расставь предложения в правильном порядке по смыслу",
                "items": [
                    {"text": "Ben and Lucy know that the tower is near the market square."},
                    {"text": "Ben wants to go to the funfair. Lucy says, \u2018We\u2019re going "
                             "to the tower.\u2019"},
                    {"text": "Then Lucy doesn\u2019t go to the tower. She goes to the funfair."},
                    {"text": "Ben and Lucy go on the Pirate Ship. They are above the tower."},
                    {"text": "Horax and Zelda are in the tower. It\u2019s the wrong place."},
                ],
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_clap")}" alt="" style="height:180px"></p>'
                "<h3>Ура! Ты со всем справился!</h3>"
                "<p>Увидимся на уроке :)</p>"}),
        ],
    },
    "u4_hw6": {
        "unit": "u4",
        "unit_title": "Unit 4 \u00b7 In the town",
        "unit_sort": 4,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        # Обе страницы диалога вырезаны из PDF: в редакторе блоки «Картинка»
        # пустые. Клипарт с двумя читающими детьми из выгрузки не взят —
        # он декоративный, вместо него наша картинка в приветствии.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_book")}" alt="" style="height:200px"></p>'
                "<h2>ПРИВЕТ-ПРИВЕТ!</h2>"
                "<p>Сегодня мы с тобой будем читать. Какая твоя любимая книга?</p>"
                "<p>Прочти диалог с начала до конца и выбери наиболее подходящий "
                "вариант ответа.</p>"}),

            ("text", {"html":
                f'<p><img src="{img("u4", "dialog_paul_daisy_1")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("text", {"html":
                f'<p><img src="{img("u4", "dialog_paul_daisy_2")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("order", {
                "words": ["Let\u2019s", "look", "at", "the", "map."],
                "sentence": "Let\u2019s look at the map.",
                "audio_tts": "Let's look at the map.",
            }),

            ("order", {
                "words": ["Can", "you", "see", "the", "museum?"],
                "sentence": "Can you see the museum?",
                "audio_tts": "Can you see the museum?",
            }),

            ("order", {
                "words": ["Where", "are", "we", "going", "now?"],
                "sentence": "Where are we going now?",
                "audio_tts": "Where are we going now?",
            }),

            ("order", {
                "words": ["We\u2019re", "going", "on", "Sunday."],
                "sentence": "We\u2019re going on Sunday.",
                "audio_tts": "We're going on Sunday.",
            }),

            ("order", {
                "words": ["Let\u2019s", "go", "to", "the", "funfair."],
                "sentence": "Let\u2019s go to the funfair.",
                "audio_tts": "Let's go to the funfair.",
            }),

            ("order", {
                "words": ["There\u2019s", "a", "park", "opposite", "the", "market", "square."],
                "sentence": "There\u2019s a park opposite the market square.",
                "audio_tts": "There's a park opposite the market square.",
            }),

            ("task", {
                "title": "Напиши свои два диалога",
                "needs_review": True,
                "html":
                    "<p>SUPER! Давай ещё потренируемся. Прочитай диалоги ещё раз, выбери "
                    "два из них и напиши свои варианты по этому образцу.</p>"
                    "<p><i>Например:<br>Anya: Can you see the museum?<br>"
                    "Masha: Yes, it\u2019s near the market square.</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>SUPER! Ты выполнил все задания!</h3>"
                "<p>Ты БОЛЬШОЙ МОЛОДЕЦ! Увидимся на уроке!</p>"}),
        ],
    },
    "u4_hw7": {
        "unit": "u4",
        "unit_title": "Unit 4 · In the town",
        "unit_sort": 4,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        # Обе части выгрузки, «Homework 7 (1)» и «(2)», одним уроком: прощание
        # первой части и приветствие второй сведены в один блок-перемычку 6,
        # поэтому блоков 18, а не 19. Картинка-пример из части (1) (скан
        # учебника) переписана текстом — блок 4.
        # В выгрузке описание «You can see how the aeroplanes can fly» стояло
        # у skyscraper, а «People can check traffic in the sky there» — у
        # airport tower наоборот. Небоскрёбу ни одно не подходит, поэтому
        # у airport tower оставлено про небо, а небоскрёбу написано своё.
        # Игра Wordwall «going to SM3» (Quiz, multiple choice) пересобрана
        # блоком quiz на наших картинках — СОСТАВ МОЙ.
        # Предлоги в выгрузке шли без картинок — подставлены наши; «the box»
        # у кошки заменено на «the shelf» по картинке.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>HELLO! Добро пожаловать в домашнее задание!</h2>"
                "<p>Сегодня мы повторим с тобой слова, которые ты изучал на уроке!</p>"
                "<p>Готов начать тренироваться?</p>"}),

            ("match", {
                "title": "Внимательно посмотри на картинки и соедини слова "
                         "с подходящими изображениями",
                "pairs": [
                    {"left_image": img("u4", "tower_lighthouse"), "right": "lighthouse",
                     "right_audio_tts": "lighthouse"},
                    {"left_image": img("u4", "tower_skyscraper"), "right": "skyscraper",
                     "right_audio_tts": "skyscraper"},
                    {"left_image": img("u4", "tower_control"), "right": "airport tower",
                     "right_audio_tts": "airport tower"},
                    {"left_image": img("u4", "tower_clock"), "right": "clock tower",
                     "right_audio_tts": "clock tower"},
                ],
            }),

            ("match", {
                "title": "МОЛОДЕЦ! Давай ещё потренируемся. "
                         "Прочитай описание и выбери подходящее здание",
                "pairs": [
                    {"left": "It’s very tall and old. It shows the time.",
                     "right": "clock tower", "right_audio_tts": "clock tower"},
                    {"left": "People can check the traffic in the sky there.",
                     "right": "airport tower", "right_audio_tts": "airport tower"},
                    {"left": "It keeps boats safe.",
                     "right": "lighthouse", "right_audio_tts": "lighthouse"},
                    {"left": "It’s very tall. People work in offices there.",
                     "right": "skyscraper", "right_audio_tts": "skyscraper"},
                ],
            }),

            ("text", {"html":
                "<h3>УРА! ОСТАЛОСЬ ПОСЛЕДНЕЕ ЗАДАНИЕ! ВНИМАТЕЛЬНО ПРОЧИТАЙ ЕГО!</h3>"
                "<p>Which tall buildings do you want to visit? Why? Write sentences.</p>"
                "<p><i>Например: I want to visit a clock tower so that I can see "
                "how big the clock in it is.</i></p>"}),

            ("task", {
                "title": "Напиши, какие места ты бы хотел посетить! Почему?",
                "needs_review": True,
                "html":
                    "<p>Внимательно посмотри на пример выше и приступай к заданию!</p>"
                    "<p>Не забудь показать свой текст учителю на уроке!</p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("hello_rocket")}" alt="" style="height:180px"></p>'
                "<h3>Ты на финишной прямой! Остался последний рывок!</h3>"
                "<p>Сегодня мы повторим всё, что ты изучил :) ПОЕХАЛИ!</p>"}),

            ("gaps", {
                "title": "Впиши above, near, below, opposite, next to, in front of",
                "image": img("u4", "prep_cat_below_shelf"),
                "text": "The cat is __below__ the shelf.",
                "gaps_expected": 1,
            }),

            ("gaps", {
                "title": "Впиши above, near, below, opposite, next to, in front of",
                "image": img("u4", "prep_ball_above_table"),
                "text": "The ball is __above__ the table.",
                "gaps_expected": 1,
            }),

            ("gaps", {
                "title": "Впиши above, near, below, opposite, next to, in front of",
                "image": img("u4", "prep_teddy_next_to_ball"),
                "text": "The bear is __next to__ the ball.",
                "gaps_expected": 1,
            }),

            ("gaps", {
                "title": "Впиши above, near, below, opposite, next to, in front of",
                "image": img("u4", "prep_elephant_in_front_of_chair"),
                "text": "The elephant is __in front of__ the chair.",
                "gaps_expected": 1,
            }),

            ("gaps", {
                "title": "Впиши above, near, below, opposite, next to, in front of",
                "image": img("u4", "prep_mouse_near_tv"),
                "text": "The mouse is __near__ the TV.",
                "gaps_expected": 1,
            }),

            ("gaps", {
                "title": "Впиши above, near, below, opposite, next to, in front of",
                "image": img("u4", "prep_cats_opposite"),
                "text": "The white cat is __opposite__ the grey cat.",
                "gaps_expected": 1,
            }),

            ("text", {"html":
                "<h3>SUPER! С первым заданием ты справился!</h3>"
                "<p>Теперь давай вспомним конструкцию <b>to be going to</b>. "
                "Сделай задание ниже!</p>"}),

            ("quiz", {
                "title": "Посмотри на картинку и выбери, куда и зачем он идёт",
                "questions": [
                    {"q": "1. Where is he going and why?",
                     "type": "single",
                     "image": img("u4", "going_cinema"),
                     "options": [{"text": "He’s going to the cinema to watch a film."},
                                 {"text": "He’s going to the library to read a book."},
                                 {"text": "He’s going to the market square to buy apples."}],
                     "correct": [0]},
                    {"q": "2. Where is she going and why?",
                     "type": "single",
                     "image": img("u4", "going_library"),
                     "options": [{"text": "She’s going to the library to borrow a book."},
                                 {"text": "She’s going to the café to have a milkshake."},
                                 {"text": "She’s going to the sports centre to go swimming."}],
                     "correct": [0]},
                    {"q": "3. Where are they going and why?",
                     "type": "single",
                     "image": img("u4", "going_sports_centre"),
                     "options": [{"text": "They’re going to the sports centre to go swimming."},
                                 {"text": "They’re going to the supermarket to buy some bread."},
                                 {"text": "They’re going to the cinema to watch a film."}],
                     "correct": [0]},
                    {"q": "4. Where is he going and why?",
                     "type": "single",
                     "image": img("u4", "going_cafe"),
                     "options": [{"text": "He’s going to the café to have a milkshake."},
                                 {"text": "He’s going to the bank to get some money."},
                                 {"text": "He’s going to the library to borrow a book."}],
                     "correct": [0]},
                    {"q": "5. Where is she going and why?",
                     "type": "single",
                     "image": img("u4", "going_supermarket"),
                     "options": [{"text": "She’s going to the supermarket to do the shopping."},
                                 {"text": "She’s going to the funfair to have fun."},
                                 {"text": "She’s going to the café to have a milkshake."}],
                     "correct": [0]},
                    {"q": "6. Where are they going and why?",
                     "type": "single",
                     "image": img("u4", "going_market"),
                     "options": [{"text": "They’re going to the market square to buy a present."},
                                 {"text": "They’re going to the bus station to take a bus."},
                                 {"text": "They’re going to the sports centre to play football."}],
                     "correct": [0]},
                ],
            }),

            ("text", {"html":
                "<h3>Ты хорошо справляешься!</h3>"
                "<p>А теперь посмотри на картинку ниже! Какие места изображены на ней?</p>"
                f'<p><img src="{img("u4", "scene_town_prepositions")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("task", {
                "title": "Посмотри на картинку ещё раз и опиши её!",
                "needs_review": True,
                "html":
                    "<p>Напиши 4–5 предложений о том, где что находится.</p>"
                    "<p><i>Например: The cinema is next to the sports centre …</i></p>",
            }),

            ("task", {
                "title": "Напиши свой диалог — дополнительное задание",
                "needs_review": True,
                "html":
                    "<p>Мы почти на финишной прямой. Посмотри внимательно на карту города "
                    "выше и на диалог ниже! Попробуй написать такой же диалог, используя "
                    "свои имена и слова.</p>"
                    "<p><i>Vic: Hi, Daisy! I’m in town, next to the school. "
                    "I’m looking for the new café. Can you tell me where it is?<br>"
                    "Daisy: No problem! Can you see the sports centre? The café is next "
                    "to it, opposite the bus station.<br>"
                    "Vic: Oh, I know! It’s near the cinema.<br>"
                    "Daisy: That’s right!<br>"
                    "Vic: Thank you!</i></p>"
                    "<p>Это задание дополнительное, но добавит 3 балла к контрольной "
                    "работе в конце юнита! ;)</p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>Good Job! Ты большой молодец!</h3>"
                "<p>Теперь ты точно готов к тесту! Желаю удачи — у тебя обязательно "
                "всё получится!</p>"}),
        ],
    },
    "u4_test": {
        "unit": "u4",
        "unit_title": "Unit 4 · In the town",
        "unit_sort": 4,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        # Нумерация блоков как в выгрузке: match, шесть «выбери правильный
        # вариант» (у нас quiz, чтобы сохранить неверные варианты), пять
        # «составь предложение», две записи голоса.
        # Картинок к пропускам в выгрузке были клипарты из стока — взяты наши
        # карточки предлогов, а существительные в предложениях подогнаны под
        # картинку (было «the cat is near the house», стало «the mouse is near
        # the TV»). Набор предлогов и неверные варианты сохранены.
        # В блоке 5 у выгрузки верным помечено «borrow a book» при картинке с
        # футбольным мячом — явная описка. Собрано по нашей картинке со
        # спортивным центром: верно «go swimming», лишние варианты оставлены.
        "blocks": [
            ("match", {
                "title": "Соедини слова с картинками",
                "pairs": [
                    {"left_image": img("u4", "town_library"), "right": "Library",
                     "right_audio_tts": "library"},
                    {"left_image": img("u4", "town_bus_station"), "right": "Bus station",
                     "right_audio_tts": "bus station"},
                    {"left_image": img("u4", "town_map"), "right": "Map",
                     "right_audio_tts": "map"},
                    {"left_image": img("u4", "town_bank"), "right": "Bank",
                     "right_audio_tts": "bank"},
                    {"left_image": img("u4", "town_market"), "right": "Market square",
                     "right_audio_tts": "market square"},
                    {"left_image": img("u4", "town_tower"), "right": "Tower",
                     "right_audio_tts": "tower"},
                ],
            }),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "The mouse is ___ the TV.", "type": "single",
                 "image": img("u4", "prep_mouse_near_tv"),
                 "options": [{"text": "near"}, {"text": "opposite"}, {"text": "below"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "The ball is ___ the table.", "type": "single",
                 "image": img("u4", "prep_ball_above_table"),
                 "options": [{"text": "above"}, {"text": "below"}, {"text": "opposite"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "The mouse is ___ the boxes.", "type": "single",
                 "image": img("u4", "prep_mouse_between_boxes"),
                 "options": [{"text": "between"}, {"text": "above"}, {"text": "near"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "He ___ the sports centre.", "type": "single",
                 "options": [{"text": "is going to"}, {"text": "going to"}, {"text": "go to"}],
                 "correct": [0]},
                {"q": "He is going to the sports centre to ___.", "type": "single",
                 "image": img("u4", "going_sports_centre"),
                 "options": [{"text": "go swimming"}, {"text": "borrow a book"},
                             {"text": "buy some apples"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "The dog is ___ the cat.", "type": "single",
                 "image": img("u4", "prep_cat_dog_opposite"),
                 "options": [{"text": "opposite"}, {"text": "above"}, {"text": "near"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "The picture is ___ the window.", "type": "single",
                 "image": img("u4", "prep_picture_below_window"),
                 "options": [{"text": "below"}, {"text": "above"}, {"text": "between"}],
                 "correct": [0]},
            ]}),

            ("order", {
                "words": ["The tree", "is", "opposite", "the house."],
                "sentence": "The tree is opposite the house.",
                "audio_tts": "The tree is opposite the house.",
            }),

            ("order", {
                "words": ["I’m", "going", "to", "the park", "to ride", "my bike."],
                "sentence": "I’m going to the park to ride my bike.",
                "audio_tts": "I'm going to the park to ride my bike.",
            }),

            ("order", {
                "words": ["We", "are", "going", "to", "the library."],
                "sentence": "We are going to the library.",
                "audio_tts": "We are going to the library.",
            }),

            ("order", {
                "words": ["The", "bank", "is", "between", "two", "trees."],
                "sentence": "The bank is between two trees.",
                "audio_tts": "The bank is between two trees.",
            }),

            ("order", {
                "words": ["Julia", "is", "going", "to", "the", "supermarket."],
                "sentence": "Julia is going to the supermarket.",
                "audio_tts": "Julia is going to the supermarket.",
            }),

            ("speaking", {
                "title": "SPEAKING TASK \U0001f3a4 Part 1",
                "needs_review": True,
                "image": img("u4", "scene_town_busy"),
                "html":
                    "<p>Посмотри на картинку и опиши её, используя предлоги места "
                    "(4–5 предложений).</p>"
                    "<p><i>For example: The library is near the shopping centre. "
                    "The bench is between two small trees.</i></p>"
                    "<p>Запиши свой ответ, нажав на кнопку микрофона.</p>",
            }),

            ("speaking", {
                "title": "SPEAKING TASK \U0001f3a4 Part 2",
                "needs_review": True,
                "image": img("u4", "scene_town_busy"),
                "html":
                    "<p>Посмотри на картинку и опиши, кто куда направляется и зачем "
                    "(4–5 предложений).</p>"
                    "<p><i>For example: They are going to the market square to buy "
                    "some apples.</i></p>"
                    "<p>Запиши свой ответ, нажав на кнопку микрофона.</p>",
            }),
        ],
    },
    "u5_hw1": {
        "unit": "u5",
        "unit_title": "Unit 5 · Under the sea",
        "unit_sort": 5,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        # В выгрузке это только словарный тренажёр на 10 слов, без заданий.
        # Приветствие и прощание дописаны: урок ребёнок открывает отдельно.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>Привет! Сегодня мы ныряем под воду \U0001f30a</h2>"
                "<p>Выучим слова про море и его обитателей. Поехали!</p>"}),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": img("u5", f)}
                for en, ru, f in U5_SEA
            ]}),

            ("quiz", quiz_ru_to_en(U5_SEA)),

            ("exact_input", {"items": [
                {"image": img("u5", f), "prompt": "Посмотри на картинку и напиши слово",
                 "accept": ([en, en.capitalize()] if not en.startswith("to ")
                            else [en, en.capitalize(), en[3:], en[3:].capitalize()]),
                 "audio_tts": en}
                for en, ru, f in U5_SEA
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>Отлично! Слова выучены.</h3>"
                "<p>Увидимся на уроке!</p>"}),
        ],
    },
    "u5_hw2": {
        "unit": "u5",
        "unit_title": "Unit 5 · Under the sea",
        "unit_sort": 5,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        # Обе части выгрузки, «Homework 2 (1)» и «(2)», одним уроком: прощание
        # первой части и приветствие второй сведены в блок-перемычку 8,
        # поэтому блоков 13, а не 14.
        # К «составь предложение» подставлены наши картинки мест — в выгрузке
        # там стояли фотографии из стока с людьми. У последнего предложения
        # убрана подсказка «(назад)»: в блоке сборки она была бы отдельной
        # плиткой со словом «ago (назад)».
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_highfive")}" alt="" style="height:200px"></p>'
                "<h2>Привет! Как здорово, что ты решил сделать домашнюю работу!</h2>"
                "<p>Она будет небольшая и интересная. Вперёд!</p>"}),

            ("video", {"title": "Видео: was / were", "url": "", "provider": ""}),

            ("order", {
                "image": img("u5", "place_restaurant"),
                "words": ["He", "was", "at", "the", "restaurant", "yesterday."],
                "sentence": "He was at the restaurant yesterday.",
                "audio_tts": "He was at the restaurant yesterday.",
            }),

            ("order", {
                "image": img("u5", "place_museum"),
                "words": ["They", "weren’t", "in", "the", "museum", "last", "week."],
                "sentence": "They weren’t in the museum last week.",
                "audio_tts": "They weren't in the museum last week.",
            }),

            ("order", {
                "image": img("u5", "place_park"),
                "words": ["She", "wasn’t", "in", "the", "park", "last", "weekend."],
                "sentence": "She wasn’t in the park last weekend.",
                "audio_tts": "She wasn't in the park last weekend.",
            }),

            ("order", {
                "image": img("u5", "place_hospital"),
                "words": ["The", "dog", "was", "in", "hospital", "yesterday."],
                "sentence": "The dog was in hospital yesterday.",
                "audio_tts": "The dog was in hospital yesterday.",
            }),

            ("order", {
                "image": img("u5", "place_supermarket"),
                "words": ["They", "were", "in", "the", "supermarket", "two", "days", "ago."],
                "sentence": "They were in the supermarket two days ago.",
                "audio_tts": "They were in the supermarket two days ago.",
            }),

            ("quiz", {"title": "Выбери правильный вариант ответа", "questions": [
                {"q": "1. She ___ at school yesterday.", "type": "single",
                 "options": [{"text": "was"}, {"text": "were"}], "correct": [0]},
                {"q": "2. They ___ at the restaurant, they were at the café.",
                 "type": "single",
                 "options": [{"text": "weren’t"}, {"text": "were"}, {"text": "was"},
                             {"text": "wasn’t"}],
                 "correct": [0]},
                {"q": "3. Mathew was sick yesterday, so he ___ in the hospital.",
                 "type": "single",
                 "options": [{"text": "was"}, {"text": "were"}, {"text": "wasn’t"},
                             {"text": "weren’t"}],
                 "correct": [0]},
                {"q": "4. Maria and Peter ___ at the cinema yesterday, they liked the film!",
                 "type": "single",
                 "options": [{"text": "were"}, {"text": "weren’t"}, {"text": "was"},
                             {"text": "wasn’t"}],
                 "correct": [0]},
                {"q": "5. There ___ cats in the box next to the supermarket, "
                      "they were very cold!",
                 "type": "single",
                 "options": [{"text": "were"}, {"text": "was"}], "correct": [0]},
                {"q": "6. I ___ at school yesterday, it was Sunday!", "type": "single",
                 "options": [{"text": "wasn’t"}, {"text": "was"}, {"text": "were"},
                             {"text": "weren’t"}],
                 "correct": [0]},
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("good_luck_clover")}" alt="" style="height:180px"></p>'
                "<h3>Отличная работа! Самое время отдохнуть :)</h3>"
                "<p>А потом — вторая половина задания. Готов? Давай начинать!</p>"}),

            ("gaps", {
                "title": "Впиши was, wasn’t, were или weren’t так, чтобы "
                         "получился связный текст",
                "text":
                    "Yesterday __was__ a busy day! We __were__ in the park in the morning. "
                    "There __was__ a football match, but there __weren’t__ many goals. "
                    "Only one! In the afternoon we __were__ at my cousin’s house. "
                    "There __were__ cheese sandwiches, but there __wasn’t__ any cake "
                    "this time. In the evening we __were__ at the cinema for that new film "
                    "about life under the sea. It __was__ interesting! We all __were__ very "
                    "tired at the end of the day.",
                "gaps_expected": 10,
            }),

            ("task", {
                "title": "Перепиши предложения в прошедшем времени, используя was или were",
                "needs_review": True,
                "html":
                    "<p>1. There is a small shark too.<br>"
                    "2. I’m scared!<br>"
                    "3. We’re at the beach.<br>"
                    "4. There are dolphins, seals and turtles in the sea.<br>"
                    "5. It’s hot.<br>"
                    "6. I’m in the sea in my new swimsuit.</p>",
            }),

            ("task", {
                "title": "Напиши, где ты был(а) в каждый из дней недели",
                "needs_review": True,
                "html":
                    "<p><i>Например:<br>On Monday I was at the swimming pool.<br>"
                    "On Tuesday I was in the supermarket.</i></p>"
                    "<p>Прояви фантазию — предложения можно просто придумать.</p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_clap")}" alt="" style="height:180px"></p>'
                "<h3>Ты отлично потрудился!</h3>"
                "<p>Спасибо тебе большое. Увидимся на уроке :)</p>"}),
        ],
    },
    "u5_hw3": {
        "unit": "u5",
        "unit_title": "Unit 5 · Under the sea",
        "unit_sort": 5,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        # Блок 2 — песня Crocorox, в выгрузке плеер пустой: аудио вписывает
        # методист, строка в «доработать руками».
        # Шаблон стихотворения из блока 4 выгрузки у нас внутри самого задания:
        # отдельным текстовым блоком он стоял бы после вопроса, а ребёнку
        # нужен перед ответом.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_headphones")}" alt="" style="height:200px"></p>'
                "<h2>Привет-привет! Давай скорее приступать к домашней работе!</h2>"
                "<p>Сначала послушай песню, а потом дополни предложения.</p>"}),

            ("gaps", {
                "title": "Послушай песню и дополни предложения",
                "mode": "drag",
                "audio": "",
                "text":
                    "1. The octopus was sad.\n"
                    "2. The __Crocorox__ was bad.\n"
                    "3. The __turtle__ hid inside its shell.\n"
                    "4. The __starfish__ were all very scared.",
                "gaps_expected": 3,
            }),

            ("gaps", {
                "title": "Прочитай и дополни предложения",
                "text":
                    "1. Its face was pretty. No, it wasn’t. It was ugly.\n"
                    "2. Its eyes were small. Yes, __they were__.\n"
                    "3. Its teeth were short. No, __they weren’t__. "
                    "They __were long__.\n"
                    "4. Its face was square. Yes, __it was__.\n"
                    "5. There were scales on its head. Yes, __there were__.",
                "gaps_expected": 5,
            }),

            ("task", {
                "title": "Нарисуй своё страшное морское животное",
                "needs_review": True,
                "html":
                    "<p>Закончи стихотворение о нём, а потом напиши о других морских "
                    "животных. Не забудь показать рисунок учителю :)</p>"
                    "<p><i>Its face …<br>Its eyes …<br>Its teeth …<br>"
                    "The dolphins were …<br>The seals were …<br>…</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_smiley")}" alt="" style="height:180px"></p>'
                "<h3>Great job! Thank you!</h3>"
                "<p>Увидимся на уроке :)</p>"}),
        ],
    },
    "u5_hw4": {
        "unit": "u5",
        "unit_title": "Unit 5 · Under the sea",
        "unit_sort": 5,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        # Блоки один в один с выгрузкой: приветствие, двенадцать пропусков,
        # «найди пару» на шесть вопросов и ответов, прощание.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_laptop")}" alt="" style="height:200px"></p>'
                "<h2>Привет! Какой ты молодец, что делаешь домашнюю работу :)</h2>"
                "<p>Сегодня потренируем was, were, wasn’t и weren’t.</p>"}),

            ("gaps", {
                "title": "Заполни пропуски с помощью was, were, wasn’t или weren’t",
                "text":
                    "1. «Where __was__ Anne yesterday?» — «She __was__ "
                    "at the park with her friends.»\n"
                    "2. «__Was__ Ed at school last week?» — «No, he "
                    "__wasn’t__. He __was__ at home because he was sick.»\n"
                    "3. «__Were__ my keys on the table?» — «No, they "
                    "__weren’t__.»\n"
                    "4. «__Was__ Sylvia at the birthday party?» — «Yes, "
                    "she __was__. She was very happy.»\n"
                    "5. «__Were__ your friends on the beach?» — «No, they "
                    "__weren’t__. It was too cold.»\n"
                    "6. «Where __were__ Joe and Bill on Saturday afternoon?» — "
                    "«I think they were at the cinema.»",
                "gaps_expected": 12,
            }),

            ("match", {
                "title": "Найди ответы на вопросы",
                "pairs": [
                    {"left": "Was Jack at the swimming pool?",
                     "right": "No, he wasn’t. It wasn’t open.",
                     "right_audio_tts": "No, he wasn't. It wasn't open."},
                    {"left": "Were your brother and sister on the beach at the weekend?",
                     "right": "Yes, they were. They were in the sea too.",
                     "right_audio_tts": "Yes, they were. They were in the sea too."},
                    {"left": "Where were you on Sunday, Louise?",
                     "right": "I was at home all day. I was tired.",
                     "right_audio_tts": "I was at home all day. I was tired."},
                    {"left": "Were your grandparents in the garden, Liz?",
                     "right": "No, they weren’t. It was too hot to do gardening.",
                     "right_audio_tts": "No, they weren't. It was too hot to do gardening."},
                    {"left": "Were there seahorses and starfish in the sea?",
                     "right": "Yes, there were! Lots of them. They were beautiful!",
                     "right_audio_tts": "Yes, there were! Lots of them. They were beautiful!"},
                    {"left": "Was there a clock on the tower in the square?",
                     "right": "Yes, there was. A very old one.",
                     "right_audio_tts": "Yes, there was. A very old one."},
                ],
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_medal")}" alt="" style="height:180px"></p>'
                "<h3>Ты большой молодец!</h3>"
                "<p>Спасибо за твои старания! Увидимся на уроке.</p>"}),
        ],
    },
    "u5_hw5": {
        "unit": "u5",
        "unit_title": "Unit 5 · Under the sea",
        "unit_sort": 5,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        # В выгрузке 11 блоков, у нас 6: шесть блоков «верно/неверно» с одним
        # утверждением каждый сведены в один (блок 4) — наш truefalse на то и
        # рассчитан. Обе страницы истории вырезаны из PDF выгрузки: в редакторе
        # блоки «Картинка» стояли пустыми.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_book")}" alt="" style="height:200px"></p>'
                "<h2>Привет! Вперёд к новым знаниям!</h2>"
                "<p>Прочитай историю и сделай задания к ней.</p>"}),

            ("text", {"html":
                f'<p><img src="{img("u5", "story_giant_shell_1")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("text", {"html":
                f'<p><img src="{img("u5", "story_giant_shell_2")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("truefalse", {
                "title": "Выбери true (верно) или false (неверно)",
                "statements": [
                    {"text": "The next letter is in the giant shell.", "answer": True},
                    {"text": "Lucy can’t get her arm out of the giant shell.",
                     "answer": False},
                    {"text": "The shark was in Horax’s cage.", "answer": True},
                    {"text": "The shark likes Horax and Zelda.", "answer": False},
                    {"text": "The octopus can’t help the children.", "answer": False},
                    {"text": "The fish make the letter S.", "answer": True},
                ],
            }),

            ("sequence", {
                "title": "Расставь предложения в правильном порядке по смыслу",
                "items": [
                    {"text": "First Lucy and Ben dive down to a giant shell."},
                    {"text": "Ben can’t see a letter in the shell."},
                    {"text": "Then Ben can’t get his arm out of the shell."},
                    {"text": "They see Horax and Zelda and the shark."},
                    {"text": "The shark doesn’t get the children. It follows Horax "
                             "and Zelda."},
                    {"text": "The octopus helps Ben to get his arm out."},
                    {"text": "Finally the children look at the fish and see the letter S."},
                ],
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>Спасибо! Ты огромный молодец!</h3>"
                "<p>Увидимся на занятии :)</p>"}),
        ],
    },
    "u5_hw6": {
        "unit": "u5",
        "unit_title": "Unit 5 · Under the sea",
        "unit_sort": 5,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        # Блоков столько же, сколько в выгрузке. Обе страницы рассказа «Saved by
        # dolphins» вырезаны из PDF: в редакторе блок «Картинка» стоял пустым,
        # он один и держал обе страницы. Шесть вопросов к рассказу в выгрузке
        # были картинкой-сканом — перенесены текстом.
        "blocks": [
            ("text", {"html":
                "<h3>Read the story:</h3>"
                f'<p><img src="{img("u5", "story_dolphins_1")}" alt="" '
                'style="max-width:100%"></p>'
                f'<p><img src="{img("u5", "story_dolphins_2")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("task", {
                "title": "Read the story again and answer the questions",
                "needs_review": True,
                "html":
                    "<p>1. Who are they? <i>— Kylie Morgan and her dad</i><br>"
                    "2. Where are they?<br>"
                    "3. What does Kylie see?<br>"
                    "4. What dangerous animal does Kylie’s dad see?<br>"
                    "5. How many teeth does it have?<br>"
                    "6. Why do the dolphins swim around Kylie?</p>",
            }),

            ("truefalse", {
                "title": "Read the story and choose: True or False",
                "statements": [
                    {"text": "The dolphins hit their tails on the water to scare the sharks.",
                     "answer": True},
                    {"text": "The dolphins get close to Kylie to protect her.", "answer": True},
                    {"text": "The white shark plays with the dolphins.", "answer": False},
                    {"text": "Sharks aren’t dangerous animals.", "answer": False},
                    {"text": "The dolphins save Kylie from the shark.", "answer": True},
                ],
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>Great job!</h3>"
                "<p>Увидимся на уроке :)</p>"}),
        ],
    },
    "u5_hw7": {
        "unit": "u5",
        "unit_title": "Unit 5 · Under the sea",
        "unit_sort": 5,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        # Блоков столько же, сколько в выгрузке. Шесть фотографий из учебника
        # заменены нашим листом (tools/sm3_u5_eco_sheet.py), пляж «тогда и
        # сейчас» — нашей парой картинок в одном файле: в блоке пропусков
        # картинка одна.
        # В блоке 5 выгрузки у шестого вопроса верным отмечен «bad», хотя в
        # поле «пропущенные слова» стоит «good» — проверено по кружку в PDF.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>Привет! Как твои дела?</h2>"
                "<p>Самое время начинать домашнюю работу!</p>"}),

            ("task", {
                "title": "Посмотри на картинки и закончи предложения",
                "needs_review": True,
                "image": img("u5", "eco_six_pictures"),
                "html":
                    "<p><i>Pictures …, … and … make me feel happy "
                    "because …<br>"
                    "Pictures …, … and … make me feel angry "
                    "because …</i></p>",
            }),

            ("gaps", {
                "title": "Посмотри на картинки и заполни пропуски: is / isn’t, "
                         "aren’t, was / were",
                "image": img("u5", "beach_then_now"),
                "text":
                    "In 1990 …\n"
                    "1. The beach __was__ clean.\n"
                    "2. People __were__ in the sea.\n"
                    "3. There __were__ fish and dolphins in the sea too.\n"
                    "4. Paul __was__ happy.\n"
                    "Today …\n"
                    "5. The beach __isn’t__ clean.\n"
                    "6. There __is__ rubbish on the beach.\n"
                    "7. There __aren’t__ any fish in the sea.\n"
                    "8. Paul __isn’t__ happy.",
                "gaps_expected": 8,
            }),

            ("sort", {
                "title": "Вставь слова в подходящую колонку",
                "groups": [
                    {"name": "Climate change", "items": [
                        {"text": "world getting hotter"},
                        {"text": "floods"},
                        {"text": "poles melting"},
                    ]},
                    {"name": "Pollution", "items": [
                        {"text": "plastic bags"},
                        {"text": "sea creatures eat plastic"},
                        {"text": "big boats"},
                    ]},
                ],
            }),

            ("quiz", {"title": "Выбери правильный вариант", "questions": [
                {"q": "1. Sea plants give us ___.", "type": "single",
                 "options": [{"text": "oxygen"}, {"text": "pollution"}], "correct": [0]},
                {"q": "2. Cities by the sea are in danger because there is ___ water "
                      "in the sea.", "type": "single",
                 "options": [{"text": "more"}, {"text": "less"}], "correct": [0]},
                {"q": "3. ___ water is bad for corals.", "type": "single",
                 "options": [{"text": "Hot"}, {"text": "Cold"}], "correct": [0]},
                {"q": "4. Fish are losing their homes because coral ___.", "type": "single",
                 "options": [{"text": "is turning white"}, {"text": "has beautiful colours"}],
                 "correct": [0]},
                {"q": "5. Sea creatures die because ___ eat plastic.", "type": "single",
                 "options": [{"text": "they"}, {"text": "we"}], "correct": [0]},
                {"q": "6. Big boats are ___ for our seas.", "type": "single",
                 "options": [{"text": "bad"}, {"text": "good"}], "correct": [0]},
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("congrats_popper")}" alt="" style="height:180px"></p>'
                "<h3>Всё просто отлично! Ты большой молодец!</h3>"
                "<p>Спасибо тебе :)</p>"}),
        ],
    },
    "u5_hw8": {
        "unit": "u5",
        "unit_title": "Unit 5 · Under the sea",
        "unit_sort": 5,
        "lesson_title": "Homework 8",
        "lesson_sort": 7,
        "kind": "homework",
        # В выгрузке 9 блоков, у нас 10: дописано прощание — в выгрузке урок
        # обрывался картинкой. Приветствие дописано в блок 1.
        # Все четыре картинки вырезаны из PDF: в редакторе блоки «Картинка»
        # стояли пустыми. Таблица «составь предложения» (блок 8 выгрузки) была
        # серым сканом, обрезанным снизу, — перенесена текстом; третья строка
        # в скане видна не целиком, взято то, что читается.
        "blocks": [
            ("text", {"html":
                "<h2>Привет! Сегодня читаем про морских животных</h2>"
                "<p>Посмотри на картинку: кого ты узнаёшь?</p>"
                f'<p><img src="{img("u5", "scene_sea_playground")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("text", {"html":
                "<h3>Read the text:</h3>"
                f'<p><img src="{img("u5", "reading_megalodon")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("quiz", {"title": "Выбери подходящий вариант", "questions": [
                {"q": "Extinct animals are ones that ___ now.", "type": "single",
                 "options": [{"text": "do not live"}, {"text": "live"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Выбери подходящий вариант", "questions": [
                {"q": "Megalodons were ___.", "type": "single",
                 "options": [{"text": "sharks"}, {"text": "dolphins"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Выбери подходящий вариант", "questions": [
                {"q": "Megalodons were very ___.", "type": "single",
                 "options": [{"text": "big"}, {"text": "small"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Выбери подходящий вариант", "questions": [
                {"q": "Megalodons were ___.", "type": "single",
                 "options": [{"text": "fast"}, {"text": "slow"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Выбери подходящий вариант", "questions": [
                {"q": "Megalodons were in ___.", "type": "single",
                 "options": [{"text": "many different places"}, {"text": "only one place"}],
                 "correct": [0]},
            ]}),

            ("task", {
                "title": "Составь предложения по таблице",
                "needs_review": True,
                "html":
                    "<p>Выбери по одному слову из каждого столбика и запиши "
                    "получившиеся предложения.</p>"
                    "<p><i>1. There — was / were / weren’t — many seahorses / "
                    "many octopuses / many starfish — at / in / on — the sea. / "
                    "the garden. / the bath.<br>"
                    "2. The — owl / puffin / lion — was / were / wasn’t — "
                    "in / next to / opposite — the school. / a net. / the beach.<br>"
                    "3. Where — was — it — at — four o’clock?</i></p>",
            }),

            ("text", {"html":
                "<h3>А вот как можно рассказать о морском животном</h3>"
                f'<p><img src="{img("u5", "project_turtles")}" alt="" '
                'style="max-width:100%"></p>'
                "<p>Пригодится на уроке :)</p>"}),

            ("text", {"html":
                f'<p><img src="{shared("well_done_jump")}" alt="" style="height:180px"></p>'
                "<h3>Отличная работа!</h3>"
                "<p>Увидимся на занятии.</p>"}),
        ],
    },
    "u5_test": {
        "unit": "u5",
        "unit_title": "Unit 5 · Under the sea",
        "unit_sort": 5,
        "lesson_title": "Test",
        "lesson_sort": 8,
        "kind": "test",
        # Нумерация блоков как в выгрузке: match, шесть «выбери правильный
        # вариант» (у нас quiz, чтобы сохранить неверные варианты), пять
        # «составь предложение», запись голоса. Картинок к match в выгрузке
        # не было — взяты наши карточки.
        "blocks": [
            ("match", {
                "title": "Соедини слова с картинками",
                "pairs": [
                    {"left_image": img("u5", "sea_dolphin"), "right": "dolphin",
                     "right_audio_tts": "dolphin"},
                    {"left_image": img("u5", "sea_seal"), "right": "seal",
                     "right_audio_tts": "seal"},
                    {"left_image": img("u5", "sea_turtle"), "right": "turtle",
                     "right_audio_tts": "turtle"},
                    {"left_image": img("u5", "sea_anchor"), "right": "anchor",
                     "right_audio_tts": "anchor"},
                    {"left_image": img("u5", "sea_starfish"), "right": "starfish",
                     "right_audio_tts": "starfish"},
                    {"left_image": img("u5", "sea_seahorse"), "right": "seahorse",
                     "right_audio_tts": "seahorse"},
                ],
            }),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "Millions of years ago ___ dinosaurs.", "type": "single",
                 "options": [{"text": "there were"}, {"text": "there was"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: ___ you in the sea, Julia?", "type": "single",
                 "options": [{"text": "Were"}, {"text": "Was"}], "correct": [0]},
                {"q": "B: No, I ___.", "type": "single",
                 "options": [{"text": "wasn’t"}, {"text": "was"}, {"text": "weren’t"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: Was Paul in the cinema? B: ___", "type": "single",
                 "options": [{"text": "Yes, he was."}, {"text": "No, he was."},
                             {"text": "Yes, he wasn’t."}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: Where ___ you on Saturday, Lucas?", "type": "single",
                 "options": [{"text": "were"}, {"text": "was"}], "correct": [0]},
                {"q": "B: I ___ in the supermarket.", "type": "single",
                 "options": [{"text": "was"}, {"text": "were"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "Lily and Ella ___ in the park,", "type": "single",
                 "options": [{"text": "weren’t"}, {"text": "wasn’t"}], "correct": [0]},
                {"q": "… they ___ in the sports centre.", "type": "single",
                 "options": [{"text": "were"}, {"text": "was"}], "correct": [0]},
            ]}),

            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                {"q": "A: ___ Charlotte in the swimming pool on Monday?", "type": "single",
                 "options": [{"text": "Was"}, {"text": "Were"}], "correct": [0]},
                {"q": "B: No, she ___.", "type": "single",
                 "options": [{"text": "wasn’t"}, {"text": "was"}, {"text": "weren’t"}],
                 "correct": [0]},
            ]}),

            ("order", {
                "words": ["Max", "was", "at", "the beach."],
                "sentence": "Max was at the beach.",
                "audio_tts": "Max was at the beach.",
            }),

            ("order", {
                "words": ["There", "was", "a house", "behind", "the swimming pool."],
                "sentence": "There was a house behind the swimming pool.",
                "audio_tts": "There was a house behind the swimming pool.",
            }),

            ("order", {
                "words": ["Was", "Mina", "in", "a boat?"],
                "sentence": "Was Mina in a boat?",
                "audio_tts": "Was Mina in a boat?",
            }),

            ("order", {
                "words": ["Were", "there", "seahorses", "in", "the sea?"],
                "sentence": "Were there seahorses in the sea?",
                "audio_tts": "Were there seahorses in the sea?",
            }),

            ("order", {
                "words": ["Where", "were", "you", "at", "6 o’clock", "yesterday?"],
                "sentence": "Where were you at 6 o’clock yesterday?",
                "audio_tts": "Where were you at 6 o'clock yesterday?",
            }),

            ("speaking", {
                "title": "SPEAKING TASK \U0001f3a4",
                "needs_review": True,
                "html":
                    "<p>Ответь на вопросы:</p>"
                    "<p>1. Where were you yesterday?<br>"
                    "2. Where was your mum 2 hours ago?<br>"
                    "3. Where were you two days ago?<br>"
                    "4. Where was your friend last Sunday?<br>"
                    "5. Where were you last summer?</p>"
                    "<p>Запиши свой ответ, нажав на кнопку микрофона.</p>",
            }),
        ],
    },
    "u6_hw1": {
        "unit": "u6",
        "unit_title": "Unit 6 · Gadgets",
        "unit_sort": 6,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        # Обе части выгрузки одним уроком: «(1)» — словарный тренажёр на 9 слов,
        # «(2)» — дополнительная часть. Блоки 1-4 — тренажёр, 5 — перемычка,
        # 6-8 — вторая часть.
        # Цены в выгрузке ребёнок смотрел на развороте учебника. У нас свой лист
        # (tools/sm3_u6_prices.py): на картинке магазина ценники пустые, а
        # дорисовать их на место нельзя — ценник у зубной щётки стоит под радио.
        # Поэтому режим «впиши», неверные варианты (345, 25, 120, 110) не нужны:
        # ребёнок складывает, а не выбирает.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_rocket")}" alt="" style="height:200px"></p>'
                "<h2>Привет! А ты любишь гаджеты и всякие технологии?</h2>"
                "<p>Выполни все задания, чтобы выучить слова на 100%!</p>"}),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": img("u6", f)}
                for en, ru, f in U6_GADGETS
            ]}),

            ("quiz", quiz_ru_to_en(U6_GADGETS)),

            ("exact_input", {"items": [
                {"image": img("u6", f), "prompt": "Посмотри на картинку и напиши слово",
                 "accept": [en, en.capitalize()], "audio_tts": en}
                for en, ru, f in U6_GADGETS
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("good_luck_clover")}" alt="" style="height:180px"></p>'
                "<h3>А теперь — вторая, дополнительная часть</h3>"
                "<p>Выполнив эти задания, ты станешь МЕГА крутым учеником!</p>"
                "<p>Посмотри на ценники и впиши в пропуски, сколько стоит покупка.</p>"}),

            ("gaps", {
                "title": "Посмотри на цены и впиши суммы (только число)",
                "image": img("u6", "shop_prices"),
                "text":
                    "1. A: Hello, can I help you? B: Yes, I’d like a laptop, please. "
                    "A: That’s £__325__.\n"
                    "2. A: Hello, can I help you? B: Yes, I’d like a games console, "
                    "please. A: That’s £__200__.\n"
                    "3. A: Hello, can I help you? B: Yes, I’d like a torch and an "
                    "electric toothbrush, please. A: That’s £__20__.\n"
                    "4. A: Hello, can I help you? B: Yes, I’d like a tablet and a "
                    "walkie-talkie, please. A: That’s £__115__.",
                "gaps_expected": 4,
            }),

            ("task", {
                "title": "Напиши, какие гаджеты есть у тебя",
                "needs_review": True,
                "html":
                    "<p>Молодец! Ты справился. А это — твоё последнее задание.</p>"
                    "<p><i>Например: I’ve got a tablet and a torch.</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>Ура, ты выполнил все задания — ты супер ученик!</h3>"
                "<p>За это держи звёздочку. До встречи на занятии!</p>"}),
        ],
    },
    "u6_hw2": {
        "unit": "u6",
        "unit_title": "Unit 6 · Gadgets",
        "unit_sort": 6,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        # Блоков столько же, сколько в выгрузке. К «составь предложение» и к
        # «выбери правильный вариант» подставлены наши парные картинки —
        # в выгрузке их не было. К «мультики и книги» и к «PE и математика»
        # пары нет, эти блоки без картинки.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_laptop")}" alt="" style="height:200px"></p>'
                "<h2>Привет, добро пожаловать в домашнее задание!</h2>"
                "<p>Сегодня мы посмотрим видео и выполним упражнения. А в конце тебя "
                "ждёт дополнительное задание — оно по желанию, но ты будешь МЕГА крут, "
                "когда справишься с ним!</p>"}),

            ("video", {"title": "Видео: сравнительная степень прилагательных",
                       "url": "", "provider": ""}),

            ("sort", {
                "title": "Распредели прилагательные: к каким прибавляем -er, "
                         "а к каким ставим more перед прилагательным?",
                "groups": [
                    {"name": "+ er", "items": [
                        {"text": "big"}, {"text": "small"}, {"text": "easy"},
                        {"text": "cheap"}, {"text": "happy"}, {"text": "fast"},
                    ]},
                    {"name": "more …", "items": [
                        {"text": "interesting"}, {"text": "beautiful"},
                        {"text": "expensive"}, {"text": "dangerous"},
                    ]},
                ],
            }),

            ("order", {
                "image": img("u6", "pair_tv_watch"),
                "words": ["A TV", "is", "more", "expensive", "than", "a watch."],
                "sentence": "A TV is more expensive than a watch.",
                "audio_tts": "A TV is more expensive than a watch.",
            }),

            ("order", {
                "image": img("u6", "pair_cake_cookie"),
                "words": ["A cake", "is", "bigger", "than", "a cookie."],
                "sentence": "A cake is bigger than a cookie.",
                "audio_tts": "A cake is bigger than a cookie.",
            }),

            ("order", {
                "image": img("u6", "pair_plane_bicycle"),
                "words": ["A plane", "is", "faster", "than", "a bike."],
                "sentence": "A plane is faster than a bike.",
                "audio_tts": "A plane is faster than a bike.",
            }),

            ("order", {
                "image": img("u6", "pair_football_golfball"),
                "words": ["Football", "is", "more", "interesting", "than", "golf."],
                "sentence": "Football is more interesting than golf.",
                "audio_tts": "Football is more interesting than golf.",
            }),

            ("order", {
                "words": ["Cartoons", "are", "funnier", "than", "books."],
                "sentence": "Cartoons are funnier than books.",
                "audio_tts": "Cartoons are funnier than books.",
            }),

            ("quiz", {"title": "Выбери правильный вариант ответа", "questions": [
                {"q": "A tiger is ___ than a cat.", "type": "single",
                 "image": img("u6", "pair_tiger_cat"),
                 "options": [{"text": "stronger"}, {"text": "more strong"},
                             {"text": "more stronger"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Выбери правильный вариант ответа", "questions": [
                {"q": "An elephant is ___ than a mouse.", "type": "single",
                 "image": img("u6", "pair_elephant_mouse"),
                 "options": [{"text": "bigger"}, {"text": "biger"}, {"text": "more big"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Выбери правильный вариант ответа", "questions": [
                {"q": "A butterfly is ___ than a caterpillar.", "type": "single",
                 "image": img("u6", "pair_butterfly_caterpillar"),
                 "options": [{"text": "more beautiful"}, {"text": "more beautifuller"},
                             {"text": "beautifuller"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Выбери правильный вариант ответа", "questions": [
                {"q": "PE is ___ than Maths.", "type": "single",
                 "options": [{"text": "funnier"}, {"text": "more funny"},
                             {"text": "funnyer"}],
                 "correct": [0]},
            ]}),

            ("quiz", {"title": "Выбери правильный вариант ответа", "questions": [
                {"q": "A computer is ___ than a torch.", "type": "single",
                 "image": img("u6", "pair_computer_torch"),
                 "options": [{"text": "more expensive"}, {"text": "expensiver"},
                             {"text": "more expensiver"}],
                 "correct": [0]},
            ]}),

            ("speaking", {
                "title": "Дополнительное задание \U0001f3a4",
                "needs_review": True,
                "html":
                    "<p>Его можно сделать по желанию. Но если сделаешь, будешь "
                    "нереально крут!</p>"
                    "<p>Ниже картинка с двумя собачками — Lucky и Mister. Скажи "
                    "3–4 предложения, сравнивая их. Не забудь про сравнительную "
                    "степень прилагательных.</p>"
                    "<p><i>Например: Lucky is more beautiful than Mister.</i></p>",
            }),

            ("text", {"html":
                f'<p><img src="{img("u6", "scene_two_dogs")}" alt="" '
                'style="max-width:100%"></p>'}),

            ("text", {"html":
                f'<p><img src="{shared("congrats_popper")}" alt="" style="height:180px"></p>'
                "<h3>Вау, поздравляю! Ты завершил всё домашнее задание — "
                "ты просто МЕГА КРУТ!</h3>"
                "<p>Увидимся на занятии ;)</p>"}),
        ],
    },
    "u6_hw3": {
        "unit": "u6",
        "unit_title": "Unit 6 · Gadgets",
        "unit_sort": 6,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        # Блоков столько же, сколько в выгрузке. Блок 3 («Диаграмма») собран
        # нашим hotspot: точки стоят на кружках-подсказках, а не на самих
        # кнопках — кнопки мелкие и стоят вплотную, номера налезали бы друг
        # на друга.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_headphones")}" alt="" style="height:200px"></p>'
                "<h2>Привет-привет! Давай начинать домашнюю работу :)</h2>"
                "<p>Послушай песню и исправь предложения.</p>"}),

            ("task", {
                "title": "Послушай песню и исправь предложения",
                "needs_review": True,
                "audio": "",
                "html":
                    "<p><i>My gadget is smaller than yours. → My gadget is bigger "
                    "than yours.</i></p>"
                    "<p>My gadget is uglier than yours. → …<br>"
                    "My gadget is older than yours. → …<br>"
                    "My gadget is cheaper than yours. → …</p>",
            }),

            ("hotspot", {
                "title": "Послушай песенку ещё раз. Посмотри на гаджет и подпиши, "
                         "что происходит, когда нажимаешь каждую кнопку",
                "mode": "label",
                "image": img("u6", "scene_four_button_gadget"),
                "points": [
                    {"x": 11.0, "y": 16.0, "text": "torch comes on",
                     "audio_tts": "torch comes on"},
                    {"x": 83.0, "y": 18.0, "text": "plays a song",
                     "audio_tts": "plays a song"},
                    {"x": 12.0, "y": 64.0, "text": "fan comes on",
                     "audio_tts": "fan comes on"},
                    {"x": 83.0, "y": 65.0, "text": "phone someone",
                     "audio_tts": "phone someone"},
                ],
            }),

            ("gaps", {
                "title": "Заверши диалоги о гаджете",
                "text":
                    "1. A: What happens when you press the red button?\n"
                    "B: The torch comes on. I use it to __see everything__.\n"
                    "2. A: What happens when you press the blue button?\n"
                    "B: The __song__ comes on. I use it to __have fun__.\n"
                    "3. A: What happens when you press the brown button?\n"
                    "B: The __fan__ comes on. I use it to __feel colder__.\n"
                    "4. A: What happens when you press the green button?\n"
                    "B: The __phone__ comes on. I use it to __phone someone__.",
                "gaps_expected": 7,
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_smiley")}" alt="" style="height:180px"></p>'
                "<h3>Ты отлично потрудился!</h3>"
                "<p>Самое время отдохнуть :)</p>"}),
        ],
    },
    "u6_hw4": {
        "unit": "u6",
        "unit_title": "Unit 6 · Gadgets",
        "unit_sort": 6,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        # Блоки один в один с выгрузкой.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_highfive")}" alt="" style="height:200px"></p>'
                "<h2>Привет, добро пожаловать в домашнее задание!</h2>"
                "<p>Сегодня мы посмотрим видео и выполним упражнения. А в конце тебя "
                "ждёт дополнительное задание — оно по желанию, но ты будешь МЕГА крут, "
                "когда справишься с ним!</p>"
                "<p>Для начала посмотри видео ниже и ответь на вопрос устно: "
                "<b>Who is the fastest — the boy, the girl or Hammy?</b></p>"}),

            ("video", {"title": "Видео: превосходная степень прилагательных",
                       "url": "", "provider": ""}),

            ("order", {
                "words": ["I’m", "the", "strongest!"],
                "sentence": "I’m the strongest!",
                "audio_tts": "I'm the strongest!",
            }),

            ("order", {
                "words": ["I’m", "the", "most", "intelligent!"],
                "sentence": "I’m the most intelligent!",
                "audio_tts": "I'm the most intelligent!",
            }),

            ("sort", {
                "title": "Отлично! Теперь распредели прилагательные по категориям",
                "groups": [
                    {"name": "the … + est", "items": [
                        {"text": "fast"}, {"text": "cheap"}, {"text": "big"},
                        {"text": "small"}, {"text": "funny"}, {"text": "old"},
                    ]},
                    {"name": "the most …", "items": [
                        {"text": "interesting"}, {"text": "dangerous"},
                        {"text": "expensive"}, {"text": "beautiful"},
                        {"text": "boring"}, {"text": "exciting"},
                    ]},
                ],
            }),

            ("gaps", {
                "title": "Поставь прилагательные из скобок в превосходную форму "
                         "(«самый …»). Первый пропуск уже заполнен как образец",
                "text":
                    "Jack can run, he can run very fast, he’s the fastest (fast) boy "
                    "in school. And Jane tells jokes like no one else, she’s "
                    "__the funniest__ (funny) and she’s cool. Robert’s "
                    "__the happiest__ (happy) — a friendly boy, he laughs and smiles "
                    "all day, while Sally’s __the quietest__ (quiet), she doesn’t "
                    "speak up, she says she’s got nothing to say. __The best__ (good) "
                    "student in our year is Beth McBeth — she’s with me, "
                    "I’m going to tell her everything and introduce Class 6C.",
                "gaps_expected": 4,
            }),

            ("task", {
                "title": "Дополнительное задание — ответь на вопросы письменно",
                "needs_review": True,
                "html":
                    "<p>Его можно сделать по желанию. Но если сделаешь, будешь нереально "
                    "крут и получишь дополнительную ⭐</p>"
                    "<p>1. Who is the funniest person in your class? "
                    "<i>Например: Alex is the funniest person in my class.</i><br>"
                    "2. Who is the oldest person in your class?<br>"
                    "3. Who is the youngest person in your class?<br>"
                    "4. Who is best at drawing in your class?<br>"
                    "5. Who is the most intelligent person in your class?</p>",
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>Поздравляю, ты завершил домашнее задание! Ты просто супер!</h3>"
                "<p>Увидимся на занятии ;)</p>"}),
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
                    want = next((en for en, r, _ in SUBJECTS if r == ru.group(1)), None)
                    if want and texts[q["correct"][0]] != want:
                        errors.append(f"{where}, вопрос {n}: correct указывает на «{texts[q['correct'][0]]}», "
                                      f"а ждём «{want}»")

        if btype == "match":
            rights = [p["right"] for p in payload["pairs"]]
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
        for link in re.findall(r"@@MEDIA@@([^\"'\\s)<]+)", json.dumps(payload, ensure_ascii=False)):
            path = os.path.join(ROOT, "media", link)
            if not os.path.exists(path):
                errors.append(f"блок {i} ({btype}): нет файла media/{link}")


# ---------- SQL ----------

def sql_for(key, lesson):
    out = [
        "-- Super Minds 3 · " + lesson["unit_title"] + " · " + lesson["lesson_title"],
        "-- собрано tools/sm3_build.py --lesson " + key,
        "do $mig$",
        "declare",
        "  v_course uuid;",
        "  v_unit   uuid;",
        "  v_lesson uuid;",
        "  v_media  text := 'https://classroom.wowteach.ru/media/';",
        "begin",
        "  select id into v_course from classroom_courses where title = 'Super Minds 3';",
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
    ap.add_argument("--lesson", required=True)
    ap.add_argument("--sql", help="записать SQL в файл")
    ap.add_argument("--chunks", metavar="LESSON_ID",
                    help="печатать вставки блоков кусками по три, готовыми для "
                         "execute_sql (длинный do-блок отваливается по таймауту)")
    ap.add_argument("--per-chunk", type=int, default=3)
    args = ap.parse_args()

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
