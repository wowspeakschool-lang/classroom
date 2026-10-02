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


def img(unit, name):
    return f"{MEDIA}sm3/{unit}/{name}.webp"


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
