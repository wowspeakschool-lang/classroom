"""Super Minds 1 · Unit 7 · Get dressed — HW2, HW4, HW6, HW7 и тест юнита.

Выгрузка ShkolaApp, разбор — docs/SM1_разбор_u7_t4.md. Homework 1, 3, 5 в
выгрузке нет, номера уроков не сдвигаем (lesson_sort = K - 1).

Картинки одежды — одним набором на весь юнит (листы Л7.1, Л7.2): в тесте у
«соедини слова с картинками» картинок нет совсем, а стоковые фото домашек
(юбка, брюки на человеке, пиджак, туфли на шпильке) выбиваются по стилю.
Кадры героев мультфильма (char_*) и клипарт детей вырезаны из PDF HW7.
"""
from sm1_build import *

U = "u7"
UNIT = "Unit 7 · Get dressed"


def c(name):
    return img(U, name)


def yes_no(q, image, options, correct):
    return {"q": q, "type": "single", "image": image,
            "options": [{"text": o} for o in options], "correct": [correct]}


LESSONS = {
    # ------------------------------------------------------------------ HW2
    "u7_hw2": {
        "unit": U, "unit_title": UNIT, "unit_sort": 7,
        "lesson_title": "Homework 2", "lesson_sort": 1, "kind": "homework",
        # В выгрузке 23 блока + безномерной Embed. Не перенесены: блок 2 —
        # реклама для родителей («3 бесплатных урока»), декоративные смайлики
        # и стрелки (блоки 10, 12, 15). Тексты 4/5 и 7/8 сведены с видео.
        # Блоки 9, 18, 19 — Wordwall, обложки пустые: СОСТАВ МОЙ.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>Привет!</h2>"
                "<p>В этом уроке тебя ждут несколько интересных заданий!</p>"
                "<p>Выполни все упражнения, если хочешь выучить тему на все 100!</p>"
                "<p>В конце тебя будет ждать дополнительное задание. Если ты его "
                "сделаешь, получишь звание ГРОССМЕЙСТЕРА английского 💪 "
                "(это очень крутое звание в шахматах ♟)</p>"}),

            ("text", {"html":
                "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
                f'<p><img src="{c("grammar_this_these")}" alt="Do you like this / these?" '
                'style="max-width:100%"></p>'}),

            ("text", {"html":
                "<p>Мы начнём с видео, но прежде чем смотреть, как думаешь, какие "
                "предметы есть у главного героя?</p>"
                "<p>Посмотри видео один раз, внимательно слушай, что говорит персонаж, "
                "и проверь себя — угадал ли ты?</p>"
                "<p>Затем посмотри видео снова и повторяй за персонажами.</p>"}),

            # 4
            ("video", {"title": "Видео 1: что есть у героя?", "url": "", "provider": "file"}),

            # 5 — в выгрузке правые картинки не выгрузились (плейсхолдеры),
            # картинки наши: лист Л7.6
            ("match", {
                "title": "Сейчас посмотри видео ещё раз и соедини предложения и "
                         "подходящие картинки!",
                "pairs": [
                    {"left": "This is a flower.", "left_audio_tts": "This is a flower.",
                     "right": "one flower", "right_image": c("pic_flower")},
                    {"left": "This is a rabbit.", "left_audio_tts": "This is a rabbit.",
                     "right": "one rabbit", "right_image": c("pic_rabbit")},
                    {"left": "These are flowers.", "left_audio_tts": "These are flowers.",
                     "right": "many flowers", "right_image": c("pic_flowers")},
                    {"left": "These are rabbits.", "left_audio_tts": "These are rabbits.",
                     "right": "many rabbits", "right_image": c("pic_rabbits")},
                ],
            }),

            ("text", {"html":
                "<p>Посмотри ещё одно видео. Но прежде чем смотреть, попробуй угадать, "
                "какую одежду ты в нём увидишь? A T-shirt? A cap? Shoes?</p>"
                "<p>Теперь посмотри видео один раз, внимательно слушай, что говорят "
                "персонажи, и проверь себя — угадал ли ты?</p>"
                "<p>Затем посмотри видео снова и повторяй за персонажами.</p>"}),

            # 7
            ("video", {"title": "Видео 2: Do you like this cap?", "url": "", "provider": "file"}),

            ("match", {
                "title": "Сейчас посмотри видео ещё раз. Обрати внимание, какая одежда "
                         "нравится герою видео, и соедини вопрос с правильным ответом.",
                "pairs": [
                    {"left": "Do you like this cap?", "right": "Yes, I do.",
                     "right_audio_tts": "Yes, I do."},
                    {"left": "Do you like these socks?", "right": "No, I don't.",
                     "right_audio_tts": "No, I don't."},
                ],
            }),

            # 9 — Wordwall «выбери правильный вариант», обложка пустая. СОСТАВ МОЙ.
            ("quiz", {"title": "Теперь пришло время практики. Выбери правильный вариант ответа.",
                      "questions": [
                yes_no("Теперь пришло время практики! Выбери правильное слово.<br>"
                       "Do you like ___ T-shirt?", c("clothes_tshirt"), ["this", "these"], 0),
                yes_no("Do you like ___ jeans?", c("clothes_jeans"), ["this", "these"], 1),
                yes_no("Do you like ___ jacket?", c("clothes_jacket"), ["this", "these"], 0),
                yes_no("Do you like ___ shoes?", c("clothes_shoes"), ["this", "these"], 1),
                yes_no("Do you like ___ socks?", c("clothes_socks"), ["this", "these"], 1),
                yes_no("Do you like ___ skirt?", c("clothes_skirt"), ["this", "these"], 0),
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("well_done_smiley")}" alt="" style="height:160px"></p>'
                "<p>Отлично! Ты справился с половиной заданий. Ты — молодец.</p>"
                "<p>Внизу тебя ждут несколько вопросов, на которые нужно выбрать "
                "правильный ответ. Возле каждого вопроса тебя ждёт смайлик-подсказка.</p>"
                "<p>Ты справишься, я в тебя верю!</p>"}),

            # 11 — в выгрузке два блока «Тест» по одному вопросу (13 и 14)
            ("quiz", {"title": "Выбери правильный вариант ответа.", "questions": [
                yes_no("Выбери правильный вариант ответа.<br>Do you like this skirt? 👍",
                       c("clothes_skirt"), ["Yes, I do.", "Yes, I don't.", "No, I do."], 0),
                yes_no("Do you like these trousers? 👎",
                       c("clothes_trousers"), ["Yes, I don't.", "No, I do.", "No, I don't."], 2),
            ]}),

            ("text", {"html":
                "<p>А теперь давай расставим слова в правильном порядке, чтобы "
                "получились предложения.</p>"}),

            ("order", {"image": c("clothes_jacket"),
                       "words": ["Do", "you", "like", "this", "jacket?"],
                       "sentence": "Do you like this jacket?",
                       "audio_tts": "Do you like this jacket?"}),
            ("order", {"image": c("clothes_jeans"),
                       "words": ["Do", "you", "like", "these", "jeans?"],
                       "sentence": "Do you like these jeans?",
                       "audio_tts": "Do you like these jeans?"}),
            ("order", {"image": c("clothes_shoes"),
                       "words": ["Do", "you", "like", "these", "shoes?"],
                       "sentence": "Do you like these shoes?",
                       "audio_tts": "Do you like these shoes?"}),
            ("order", {"image": c("clothes_cap"),
                       "words": ["Do", "you", "like", "this", "cap?"],
                       "sentence": "Do you like this cap?",
                       "audio_tts": "Do you like this cap?"}),

            # 17 — текст 20 (с аудио-образцом) + запись голоса 21
            ("speaking", {
                "title": "Расскажи, какая одежда тебе нравится 🎤",
                "needs_review": True,
                "image": c("clothes_set_speaking"),
                "sample": "",
                "sample_tts": "I like this T-shirt. I like these jeans. I don't like this skirt.",
                "html":
                    "<p>Посмотри на картинку: на ней разные предметы одежды. "
                    "Расскажи, какая одежда тебе нравится, — запиши голосом.</p>"
                    "<p>Сначала послушай образец ответа.</p>"}),

            # 18 — Wordwall «дополнительное задание: выбери правильный вариант»,
            # обложка пустая. СОСТАВ МОЙ.
            ("quiz", {"title": "Дополнительное задание — выбери правильный вариант",
                      "questions": [
                yes_no("Ты выполнил все задания из основной части! А это дополнительное "
                       "задание — для настоящих чемпионов! Посмотри на смайлик и выбери "
                       "ответ.<br>Do you like this sweater? 👍",
                       c("clothes_sweater"), ["No, I don't.", "Yes, I do."], 1),
                yes_no("Do you like these shorts? 👎", c("clothes_shorts"),
                       ["No, I don't.", "Yes, I do."], 0),
                yes_no("Do you like this T-shirt? 👍", c("clothes_tshirt"),
                       ["No, I don't.", "Yes, I do."], 1),
                yes_no("Do you like these socks? 👎", c("clothes_socks"),
                       ["Yes, I do.", "No, I don't."], 1),
                yes_no("Do you like this cap? 👍", c("clothes_cap"),
                       ["Yes, I do.", "No, I don't."], 0),
            ]}),

            # 19 — Wordwall «перенеси вещи в подходящие столбики», обложка пустая.
            # СОСТАВ МОЙ: столбики this / these.
            ("sort", {"title": "Перенеси вещи в подходящие столбики: одна вещь — this, "
                               "пара или много — these",
                      "groups": [
                {"name": "this", "items": [
                    {"text": "cap", "image": c("clothes_cap")},
                    {"text": "skirt", "image": c("clothes_skirt")},
                    {"text": "jacket", "image": c("clothes_jacket")},
                    {"text": "T-shirt", "image": c("clothes_tshirt")},
                    {"text": "sweater", "image": c("clothes_sweater")},
                ]},
                {"name": "these", "items": [
                    {"text": "jeans", "image": c("clothes_jeans")},
                    {"text": "trousers", "image": c("clothes_trousers")},
                    {"text": "shoes", "image": c("clothes_shoes")},
                    {"text": "socks", "image": c("clothes_socks")},
                    {"text": "shorts", "image": c("clothes_shorts")},
                ]},
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>Поздравляю! Ты завершил домашнее задание, ты молодец!</h3>"
                "<p>Увидимся на занятии!</p>"}),
        ],
    },

    # ------------------------------------------------------------------ HW4
    "u7_hw4": {
        "unit": U, "unit_title": UNIT, "unit_sort": 7,
        "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework",
        # В выгрузке только часть (2) — интерактивное видео (мультфильм
        # «SM2ed Animated story video», Rutube, 1:39) с 9 заданиями по
        # таймкодам. Самих заданий в выгрузке нет (только тип и время), части
        # (1) нет совсем. Переносим видео; задания — в «доработать руками».
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_headphones")}" alt="" style="height:200px"></p>'
                "<h2>Привет!</h2>"
                "<p>Сегодня тебя ждёт мультфильм. Посмотри его внимательно — "
                "а потом посмотри ещё раз и повторяй за героями.</p>"}),

            ("video", {"title": "Мультфильм Unit 7", "url": "", "provider": "file"}),

            ("text", {"html":
                f'<p><img src="{shared("well_done_clap")}" alt="" style="height:180px"></p>'
                "<h3>Отличная работа!</h3>"
                "<p>Увидимся на занятии!</p>"}),
        ],
    },

    # ------------------------------------------------------------------ HW6
    "u7_hw6": {
        "unit": U, "unit_title": UNIT, "unit_sort": 7,
        "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework",
        # Все картинки урока в PDF не выгрузились (на их месте только кнопки
        # удаления): блок 2 (вероятно, реклама, как в HW2), карточка
        # «повторим» (блок 3), картинки узоров, картинка с девочками,
        # картинка «мои любимые вещи». Все — наши, листы Л7.3–Л7.5.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_book")}" alt="" style="height:200px"></p>'
                "<h2>Привет!</h2>"
                "<p>Сегодня мы выучим названия разных узоров, которые частенько "
                "встречаются на одежде.</p>"
                "<p>Тебя ждут интересные увлекательные упражнения, и ты будешь "
                "супер учеником, когда справишься с ними!</p>"}),

            # 2 — карточка блока 3 «Давай повторим» не выгрузилась, собрана заново
            ("text", {"html":
                "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
                '<table style="border-collapse:collapse;text-align:center"><tr>'
                + "".join(
                    f'<td style="padding:6px"><img src="{c("pattern_" + w)}" alt="" '
                    f'style="height:110px"><br><b>{w}</b></td>'
                    for w in ("stripes", "spots", "flowers", "plain", "zigzags"))
                + "</tr></table>",
                "audio_tts": "stripes, spots, flowers, plain, zigzags"}),

            ("match", {
                "title": "Для начала давай вспомним наши узоры. Соедини название с картинкой.",
                "pairs": [
                    {"left": w, "left_audio_tts": w,
                     "right": "узор " + w, "right_image": c("pattern_" + w)}
                    for w in ("stripes", "spots", "flowers", "plain", "zigzags")
                ],
            }),

            # 4 — в выгрузке «Выбери правильный вариант»: картинка с тремя
            # девочками (не выгрузилась) + описание → имя. Людей не рисуем,
            # поэтому наоборот: по описанию найти одежду девочки.
            ("quiz", {"title": "Прочитай описание и найди одежду девочки", "questions": [
                {"q": "Внимательно прочитай описание девочек и найди их одежду.<br>"
                      "<b>Anna</b>: She is wearing a plain skirt and a sweater with zigzags.",
                 "type": "single", "audio_tts": "She is wearing a plain skirt and a sweater with zigzags.",
                 "options": [{"image": c("outfit_lily")}, {"image": c("outfit_anna")},
                             {"image": c("outfit_kate")}], "correct": [1]},
                {"q": "<b>Lily</b>: She is wearing a shirt with spots and a skirt with flowers.",
                 "type": "single", "audio_tts": "She is wearing a shirt with spots and a skirt with flowers.",
                 "options": [{"image": c("outfit_lily")}, {"image": c("outfit_kate")},
                             {"image": c("outfit_anna")}], "correct": [0]},
                {"q": "<b>Kate</b>: She is wearing a T-shirt with stripes and a skirt with spots.",
                 "type": "single", "audio_tts": "She is wearing a T-shirt with stripes and a skirt with spots.",
                 "options": [{"image": c("outfit_anna")}, {"image": c("outfit_lily")},
                             {"image": c("outfit_kate")}], "correct": [2]},
            ]}),

            # 5 — ключ выгрузки «zigzagz» (опечатка), принимаем zigzags и zigzag
            ("gaps", {
                "title": "Внимательно посмотри на картинку. Это мои любимые вещи с узорами. "
                         "Прочитай их описание и впиши в пропуск название нужного узора.",
                "image": c("fav_clothes"),
                "text":
                    "Look! These are my favourite clothes.\n"
                    "It's a T-shirt with __flowers__.\n"
                    "They are shorts with __zigzags|zigzag__. They are red and white.\n"
                    "They are __plain__ trousers.\n"
                    "It's a sweater with __stripes__. It's black and white.\n"
                    "They are socks with __spots__. They are yellow.\n"
                    "I like my clothes!",
                "gaps_expected": 5,
            }),

            ("task", {
                "title": "Ура! Это последнее задание на сегодня",
                "needs_review": True,
                "html":
                    "<p>Письменно опиши свою любимую одежду с узорами (если у тебя "
                    "такой нет — можешь пофантазировать и описать выдуманную).</p>"
                    "<p>Используй предыдущее упражнение как пример.</p>"
                    "<p><i>It's a T-shirt with … They are …</i></p>"}),

            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>Поздравляю! Ты завершил домашнее задание, ты замечательный ученик!</h3>"
                "<p>За это лови сердечко ❤️</p>"
                "<p>Увидимся на занятии!</p>"}),
        ],
    },

    # ------------------------------------------------------------------ HW7
    "u7_hw7": {
        "unit": U, "unit_title": UNIT, "unit_sort": 7,
        "lesson_title": "Homework 7", "lesson_sort": 6, "kind": "homework",
        # Четыре блока «Тест» True/False сведены в один quiz (блок 2).
        # Блоки 7 и 8 — Wordwall (обложки пустые), СОСТАВ МОЙ.
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_highfive")}" alt="" style="height:200px"></p>'
                "<h2>👕 Привет, модник!</h2>"
                "<p>Это последняя домашка перед тестом! Выполни все задания, чтобы "
                "хорошенько подготовиться!</p>"}),

            ("quiz", {"title": "Посмотри на картинку и прочитай слово. Правильно (True) "
                               "или нет (False)?", "questions": [
                yes_no("Посмотри на картинку и прочитай слово. Правильно (True) или нет "
                       "(False)?<br><b>shoes</b>", c("clothes_shoes"), ["True", "False"], 0),
                yes_no("<b>trousers</b>", c("clothes_jacket"), ["True", "False"], 1),
                yes_no("<b>skirt</b>", c("clothes_shorts"), ["True", "False"], 1),
                yes_no("<b>sweater</b>", c("clothes_sweater"), ["True", "False"], 0),
            ]}),

            ("sort", {"title": "Разложи одежду по группам: ноги 🦿, туловище 👕 или голова 🧢.",
                      "groups": [
                {"name": "ноги 🦿", "items": [{"text": w} for w in
                    ("shorts", "trousers", "jeans", "skirt", "socks", "shoes")]},
                {"name": "туловище 👕", "items": [{"text": w} for w in
                    ("sweater", "jacket", "T-shirt")]},
                {"name": "голова 🧢", "items": [{"text": "baseball cap"}]},
            ]}),

            ("gaps", {
                "title": "Впиши this или these.",
                "text":
                    "1. Do you like __these__ shoes?\n"
                    "2. Do you like __this__ skirt?\n"
                    "3. Do you like __these__ jeans?\n"
                    "4. Do you like __this__ baseball cap?\n"
                    "5. Do you like __these__ socks?\n"
                    "6. Do you like __this__ jacket?",
                "gaps_expected": 6,
            }),

            ("quiz", {"title": "Посмотри на картинку и ответь на вопрос.", "questions": [
                yes_no("Посмотри на картинку и ответь на вопрос.<br>"
                       "Is he wearing a green sweater?", c("char_boy_blue_sweater"),
                       ["Yes, she is.", "No, she isn’t.", "Yes, he is.", "No, he isn’t."], 3),
                yes_no("Is he wearing trousers?", c("char_boy_red_jacket"),
                       ["Yes, she is.", "No, she isn’t.", "Yes, he is.", "No, he isn’t."], 2),
                yes_no("Is she wearing a purple skirt?", c("char_girl_green_sweater"),
                       ["Yes, she is.", "No, she isn’t.", "Yes, he is.", "No, he isn’t."], 0),
            ]}),

            ("speaking", {
                "title": "Что он/она носит? 🎤",
                "needs_review": True,
                "image": c("kids_thumbs_up"),
                "html":
                    "<p>Посмотри на картинку. Нажми на микрофон и расскажи: что он/она "
                    "носит?</p>"
                    "<p><i>Пример: He’s wearing a blue jacket, black trousers and white "
                    "shoes.</i></p>"}),

            # 7 — Wordwall «Впиши слова», обложка пустая. СОСТАВ МОЙ.
            ("exact_input", {"items": [
                {"image": c(f), "prompt": "Дополнительное задание! Посмотри на картинку и "
                                          "напиши слово" if i == 0 else
                                          "Посмотри на картинку и напиши слово",
                 "accept": acc, "audio_tts": acc[0]}
                for i, (f, acc) in enumerate([
                    ("clothes_jacket", ["jacket", "Jacket", "a jacket"]),
                    ("clothes_skirt", ["skirt", "Skirt", "a skirt"]),
                    ("clothes_socks", ["socks", "Socks"]),
                    ("clothes_tshirt", ["T-shirt", "t-shirt", "a T-shirt", "T shirt", "tshirt"]),
                    ("clothes_trousers", ["trousers", "Trousers"]),
                    ("clothes_cap", ["cap", "baseball cap", "Cap", "a cap"]),
                ])
            ]}),

            # 8 — Wordwall «Выбери правильный вариант», обложка пустая. СОСТАВ МОЙ.
            ("quiz", {"title": "Выбери правильный вариант", "questions": [
                yes_no("Выбери правильный вариант:<br>___ he wearing a jacket?",
                       c("char_boy_red_jacket"), ["Is", "Are", "Do"], 0),
                yes_no("She ___ wearing a green sweater.", c("char_girl_green_sweater"),
                       ["are", "is", "am"], 1),
                yes_no("Is he wearing a red sweater? — No, he ___.", c("char_boy_blue_sweater"),
                       ["is", "isn’t", "aren’t"], 1),
                yes_no("Is she wearing a skirt? — Yes, she ___.", c("char_girl_green_sweater"),
                       ["isn’t", "does", "is"], 2),
                yes_no("He is wearing a blue ___.", c("char_boy_blue_sweater"),
                       ["sweater", "skirt", "dress"], 0),
            ]}),

            ("text", {"html":
                f'<p><img src="{shared("well_done_jump")}" alt="" style="height:180px"></p>'
                "<h3>Молодец!</h3>"
                "<p>Ты повторил всю одежду, this/these и Is he/she wearing.</p>"
                "<p>Ты готов к тесту!</p>"}),
        ],
    },

    # ------------------------------------------------------------------ Test
    "u7_test": {
        "unit": U, "unit_title": UNIT, "unit_sort": 7,
        "lesson_title": "Unit 7 Test", "lesson_sort": 7, "kind": "test",
        # Блок 5 выгрузки (аудирование «Speaker 1–5 + Extra → картинки») не
        # перенесён: нет ни аудио, ни картинок, ни ответов — в доработку.
        # Стоковые фото людей (в т. ч. детей) заменены предметами, лист ЛТ7.1;
        # фото детей в speaking — сценой магазина (ЛТ7.2) и кадрами героев.
        "blocks": [
            ("exact_input", {"items": [
                {"prompt": f"Напиши по-английски: {ru}", "accept": acc, "audio_tts": acc[0]}
                for ru, acc in [
                    ("джинсы", ["jeans", "Jeans"]),
                    ("свитер", ["sweater", "Sweater"]),
                    ("пиджак, куртка", ["jacket", "Jacket"]),
                    ("юбка", ["skirt", "Skirt"]),
                    ("шорты", ["shorts", "Shorts"]),
                    ("бейсболка, кепка", ["baseball cap", "Baseball cap", "cap"]),
                    ("обувь", ["shoes", "Shoes"]),
                    ("носки", ["socks", "Socks"]),
                    ("футболка", ["T-shirt", "t-shirt", "T shirt", "tshirt"]),
                    ("брюки", ["trousers", "Trousers"]),
                ]
            ]}),

            ("match", {"title": "Соедини слова с картинками:", "pairs": [
                {"left": w, "left_audio_tts": w, "right": "картинка " + w,
                 "right_image": c(f)}
                for w, f in [("sweater", "clothes_sweater"), ("T-shirt", "clothes_tshirt"),
                             ("baseball cap", "clothes_cap"), ("jacket", "clothes_jacket"),
                             ("jeans", "clothes_jeans"), ("skirt", "clothes_skirt")]
            ]}),

            # 3 — в выгрузке пять блоков «Выбери правильный вариант» (выпадающие
            # списки в пропусках); здесь вопрос на каждый пропуск, варианты те же
            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                yes_no("Заполни пропуски — выбери подходящий вариант.<br>"
                       "A: Do you like ___ hat?<br>B: Yes, I do.",
                       c("clothes_hat_elephant"), ["these", "this"], 1),
                yes_no("A: Do you like this hat?<br>B: Yes, I ___.",
                       c("clothes_hat_elephant"), ["do", "like", "don't"], 0),
                yes_no("A: Do you like ___ socks?<br>B: No, I don't.",
                       c("clothes_socks_faces"), ["this", "these"], 1),
                yes_no("A: Do you like these socks?<br>B: No, I ___.",
                       c("clothes_socks_faces"), ["do", "don't"], 1),
                yes_no("Olivia is ___ a red sweater.", c("clothes_sweater_red"),
                       ["wear", "wears", "wearing"], 2),
                yes_no("A: ___ he watching TV?<br>B: No, he isn't.", c("obj_tv"),
                       ["Is", "Are", "Do"], 0),
                yes_no("A: Is he watching TV?<br>B: No, he ___.", c("obj_tv"),
                       ["is", "does", "isn't"], 2),
                yes_no("A: ___ Kate singing?<br>B: Yes, she is.", c("obj_microphone"),
                       ["Are", "Is", "Does"], 1),
                yes_no("A: Is Kate singing?<br>B: Yes, she ___.", c("obj_microphone"),
                       ["sing", "isn't", "is"], 2),
            ]}),

            ("order", {"image": c("obj_bikes"),
                       "words": ["Are", "Amy", "and Hannah", "riding", "bikes?"],
                       "sentence": "Are Amy and Hannah riding bikes?",
                       "audio_tts": "Are Amy and Hannah riding bikes?"}),
            ("order", {"image": c("clothes_shoes"),
                       "words": ["Do", "you", "like", "these", "shoes?"],
                       "sentence": "Do you like these shoes?",
                       "audio_tts": "Do you like these shoes?"}),
            ("order", {"image": c("obj_game_controllers"),
                       "words": ["They", "are", "playing", "computer", "games."],
                       "sentence": "They are playing computer games.",
                       "audio_tts": "They are playing computer games."}),
            ("order", {"image": c("clothes_shorts"),
                       "words": ["Do", "you", "like", "these", "shorts?"],
                       "sentence": "Do you like these shorts?",
                       "audio_tts": "Do you like these shorts?"}),
            ("order", {"image": c("obj_sandwich"),
                       "words": ["Is", "Bobby", "eating", "a", "sandwich?"],
                       "sentence": "Is Bobby eating a sandwich?",
                       "audio_tts": "Is Bobby eating a sandwich?"}),

            # 9 — текст к чтению (в выгрузке — описание блока 6)
            ("text", {"html":
                "<p><b>Прочитай текст и выбери правильный вариант ответа к вопросам 1–5.</b></p>"
                "<p>Today is a fun day! The children are at a fashion show at school.</p>"
                "<p>Look at Tom! He is wearing a brown jacket and blue trousers. His T-shirt "
                "is black. “Do you like my jacket?” Tom asks. “Yes, I do! It's cool!” says "
                "Emma.</p>"
                "<p>Emma is wearing a blue sweater and brown shorts. She is wearing blue "
                "shoes too. Her sweater is plain — no spots, no stripes!</p>"
                "<p>Lily is wearing a yellow dress. The dress has got flowers. “I love my "
                "dress!” says Lily. “Do you like these shoes?” She is wearing brown "
                "sandals.</p>"
                "<p>Ben is wearing a blue T-shirt and brown trousers. “Is Ben wearing a "
                "cap?” asks Emma. “No, he isn't,” says Tom. “But look at his bag! It's "
                "blue!”</p>"
                "<p>Sofia is wearing a blue jacket and a white shirt. Her trousers are blue "
                "and her shoes are pink. “I love pink!” says Sofia. “Pink is my favourite "
                "colour!”</p>"}),

            ("quiz", {"title": "Прочитай текст и выбери правильный вариант ответа", "questions": [
                {"q": "1. What colour is Tom's jacket?", "type": "single",
                 "options": [{"text": "A) black"}, {"text": "B) blue"}, {"text": "C) brown"}],
                 "correct": [2]},
                {"q": "2. What pattern has Emma's sweater got?", "type": "single",
                 "options": [{"text": "A) spots"}, {"text": "B) no pattern — it's plain"},
                             {"text": "C) stripes"}], "correct": [1]},
                {"q": "3. What has Lily's dress got?", "type": "single",
                 "options": [{"text": "A) stripes"}, {"text": "B) flowers"},
                             {"text": "C) zigzags"}], "correct": [1]},
                {"q": "4. Is Ben wearing a cap?", "type": "single",
                 "options": [{"text": "A) No, he isn't."}, {"text": "B) Yes, he is."},
                             {"text": "C) We don't know."}], "correct": [0]},
                {"q": "5. What colour are Sofia's shoes?", "type": "single",
                 "options": [{"text": "A) blue"}, {"text": "B) white"}, {"text": "C) pink"}],
                 "correct": [2]},
            ]}),

            ("speaking", {
                "title": "SPEAKING TASK · Part 1 🎤",
                "needs_review": True,
                "image": c("scene_clothes_shop"),
                "html":
                    "<p>Посмотри на картинку, расскажи, какая одежда тебе нравится "
                    "(используй this / these).</p>"
                    "<p><i>For example: I like this yellow dress.</i></p>"
                    "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>"}),

            ("speaking", {
                "title": "SPEAKING TASK · Part 2 🎤",
                "needs_review": True,
                "image": c("chars_three"),
                "html":
                    "<p>Посмотри на картинку. Выбери двоих ребят и расскажи, кто во что "
                    "одет.</p>"
                    "<p><i>For example: He is wearing a red jacket, a white T-shirt, brown "
                    "trousers and orange shoes.</i></p>"
                    "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>"}),
        ],
    },
}
