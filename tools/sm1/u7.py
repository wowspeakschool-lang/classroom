"""Super Minds 1 · Unit 7 · Get dressed — HW1–HW7 и тест юнита.

Выгрузка ShkolaApp, разбор — docs/SM1_разбор_u7_t4.md. HW1, HW3, HW5 и
часть (1) HW4 догружены 07.10.2026 в корень папки SM1 (второй заход);
lesson_sort = K - 1.

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


# =================================================================== второй заход
# Догружено 07.10.2026: HW1 (1)+(2), HW3, HW4 (1), HW5.

def hello(html, image="hello_wave"):
    return ("text", {"html":
        f'<p><img src="{shared(image)}" alt="" style="height:200px"></p>' + html})


def bye(html, image="well_done_star"):
    return ("text", {"html":
        f'<p><img src="{shared(image)}" alt="" style="height:180px"></p>' + html})


def pic(name, alt="", width="100%"):
    return f'<p><img src="{c(name)}" alt="{alt}" style="max-width:{width}"></p>'


def order(sentence, words, image=None):
    b = {"words": words, "sentence": sentence, "audio_tts": sentence}
    if image:
        b["image"] = image
    return ("order", b)


def listen_quiz(words, title="Послушай слово и выбери его"):
    """«Послушай» тренажёра: верный вариант на позиции i % 4 (варианты не
    перемешиваются при показе)."""
    n = len(words)
    qs = []
    for i, (en, ru, _) in enumerate(words):
        wrong = [words[(i + k) % n][0] for k in range(1, 4)]
        pos = i % 4
        opts = wrong[:pos] + [en] + wrong[pos:]
        qs.append({"q": title, "type": "single", "audio_tts": en,
                   "options": [{"text": o} for o in opts], "correct": [pos]})
    return {"questions": qs}


# Слова словарного тренажёра HW1 (1) — в его порядке. Картинки — листы Л7.1,
# Л7.2 (стоковые фото тренажёра не берём).
CLOTHES = [
    ("jeans", "джинсы", "clothes_jeans"),
    ("sweater", "свитер", "clothes_sweater"),
    ("jacket", "пиджак, куртка", "clothes_jacket"),
    ("skirt", "юбка", "clothes_skirt"),
    ("shorts", "шорты", "clothes_shorts"),
    ("baseball cap", "бейсболка, кепка", "clothes_cap"),
    ("shoes", "обувь", "clothes_shoes"),
    ("socks", "носки", "clothes_socks"),
    ("T-shirt", "футболка", "clothes_tshirt"),
    ("trousers", "брюки", "clothes_trousers"),
]

# ------------------------------------------------------------------ HW1
# (1) — словарный тренажёр (10 слов: Карточки, Запомни, Послушай, Найди пару;
# «дополнительные» Unscramble / Fill in / Final test тренажёра не переносим —
# как в других юнитах). (2) — дополнительная часть: повторение, рисунок +
# запись голоса, две игры Wordwall (обложки пустые, СОСТАВ МОЙ).
# Бл. 2 части (2) — реклама для родителей, не переносим.
LESSONS["u7_hw1"] = {
    "unit": U, "unit_title": UNIT, "unit_sort": 7,
    "lesson_title": "Homework 1", "lesson_sort": 0, "kind": "homework",
    "blocks": [
        hello("<h2>Добро пожаловать в домашнее задание! 👋</h2>"
              "<p>В этом уроке тебя ждут задания на отработку новых слов — мы "
              "выучим, как по-английски называется одежда. Выполни все задания, если "
              "хочешь выучить тему на все 100!</p>"
              "<p>После того как завершишь все задания, тебя ждёт дополнительная "
              "часть — её можно выполнить по желанию, НО если ты выполнишь её, то "
              "будешь нереально крут!</p>"),
        ("flashcards", {"title": "Запомни слова. Нажми на карточку, чтобы увидеть перевод",
                        "cards": [{"text": en, "translation": ru, "audio_tts": en,
                                   "image": c(f)} for en, ru, f in CLOTHES]}),
        ("quiz", quiz_ru_to_en(CLOTHES)),
        ("quiz", listen_quiz(CLOTHES)),
        ("match", {"title": "Найди пару: соедини слово и перевод", "pairs": [
            {"left": en, "left_audio_tts": en, "right": ru} for en, ru, f in CLOTHES]}),

        # 6 — перемычка: прощание (1) + приветствие (2)
        ("text", {"html":
            f'<p><img src="{shared("well_done_clap")}" alt="" style="height:160px"></p>'
            "<h3>Отлично! Слова выучены 💪</h3>"
            "<p>Добро пожаловать в дополнительную часть домашнего задания! Здесь тебя "
            "ждут интересные упражнения. Их можно выполнить по желанию.</p>"
            "<p>НО если ты выполнишь их, то будешь большим молодцом!</p>"}),

        ("text", {"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
                  + pic("vocab_clothes", "Vocabulary — Clothes")}),

        # 8 — в выгрузке холст для рисования + запись голоса
        ("speaking", {
            "title": "Нарисуй себя в любимой одежде 🎨🎤",
            "needs_review": True,
            "image": c("kids_drawing_sample"),
            "html":
                "<p>Нарисуй себя в любимой одежде (не забудь раскрасить!) и покажи "
                "рисунок своему учителю на уроке.</p>"
                "<p>Нажми на микрофон и перечисли, какую одежду ты нарисовал.</p>"
                "<p><i>Пример: a blue T-shirt, blue shorts, green shoes.</i></p>"}),

        # 9 — Wordwall «Соедини слова с картинками», обложка пустая. СОСТАВ МОЙ.
        ("match", {"title": "Ты выполнил все задания из основной части! А это "
                            "дополнительное задание — для настоящих чемпионов! "
                            "Соедини слова с картинками:",
                   "pairs": [{"left_image": c(f), "right": en, "right_audio_tts": en}
                             for en, ru, f in CLOTHES[:6]]}),

        # 10 — Wordwall «Впиши слова», обложка пустая. СОСТАВ МОЙ.
        ("exact_input", {"items": [
            {"image": c(f), "prompt": "Впиши слова: что на картинке?" if i == 0 else
                                      "Что на картинке?",
             "accept": acc, "audio_tts": acc[0]}
            for i, (f, acc) in enumerate([
                ("clothes_shoes", ["shoes", "Shoes"]),
                ("clothes_socks", ["socks", "Socks"]),
                ("clothes_tshirt", ["T-shirt", "t-shirt", "T shirt", "tshirt", "a T-shirt"]),
                ("clothes_trousers", ["trousers", "Trousers"]),
                ("clothes_sweater", ["sweater", "Sweater", "a sweater"]),
                ("clothes_jeans", ["jeans", "Jeans"]),
            ])
        ]}),

        bye("<h3>Поздравляю! Ты завершил домашнее задание, ты молодец!</h3>"
            "<p>За это лови сердечко 💗</p>"
            "<p>Увидимся на занятии!</p>"),
    ],
}

# ------------------------------------------------------------------ HW3
# Бл. 2 — реклама для родителей, не переносим. Кадры героев мультфильмов
# (Mabel, Darius, Gravity Falls) — из PDF, как в выгрузке. Фото четырёх
# взрослых в бл. 11–13 брать нельзя — заменены комплектами одежды (Л7.7),
# аудио к бл. 10–11 в выгрузке нет: текст наш, размечен audio_tts, СОСТАВ МОЙ.
# Бл. 14 — две игры Wordwall, обложки пустые: СОСТАВ МОЙ.
HW3_NAMES = [("Kate", "outfit_kate"), ("Tom", "outfit_tom"),
             ("Any", "outfit_any"), ("Sam", "outfit_sam")]
HW3_SCRIPT = ("Kate is wearing a red sweater, a white skirt and red boots. "
              "Tom is wearing a black coat, a white shirt and black jeans. "
              "Any is wearing a pink sweater and a red skirt. "
              "Sam is wearing a grey T-shirt, red shorts and a cap.")

LESSONS["u7_hw3"] = {
    "unit": U, "unit_title": UNIT, "unit_sort": 7,
    "lesson_title": "Homework 3", "lesson_sort": 2, "kind": "homework",
    "blocks": [
        hello("<h2>Добро пожаловать в домашнее задание! 👋</h2>"
              "<p>Впереди тебя ждут несколько интересных видео и увлекательных "
              "упражнений, а также 1 дополнительное задание, которое можно выполнить "
              "по желанию.</p>"
              "<p>За каждое задание ты будешь получать ⭐️. Собери максимальное "
              "количество звёздочек и стань ЧЕМПИОНОМ!</p>"),

        ("text", {"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
                  + pic("grammar_is_he_wearing", "Grammar 2 — Is he/she wearing …?")}),

        ("text", {"html":
            "<p>Мы начнём с видео, но прежде чем смотреть, как думаешь, во что одеты "
            "главные персонажи видео? A T-shirt? A skirt? A cap?</p>"
            "<p>Теперь посмотри видео один раз, внимательно слушай, что говорит "
            "персонаж, и проверь себя — угадал ли ты?</p>"
            "<p>Затем посмотри видео снова и повторяй за персонажами.</p>"}),

        # 4
        ("video", {"title": "Видео 1: She's wearing a pink jumper and a purple skirt",
                   "url": "", "provider": "file"}),

        ("match", {"title": "Сейчас посмотри видео ещё раз и соедини предложения и "
                            "подходящие картинки! За это задание ты получишь 1 ⭐️.",
                   "pairs": [
            {"left": "He's wearing a white T-shirt.",
             "left_audio_tts": "He's wearing a white T-shirt.",
             "right": "Darius", "right_image": c("char_darius")},
            {"left": "She's wearing a pink jumper.",
             "left_audio_tts": "She's wearing a pink jumper.",
             "right": "Mabel", "right_image": c("char_mabel_card")},
        ]}),

        ("text", {"html":
            "<p>Посмотри ещё одно видео. Но сначала посмотри на картинку и угадай, о "
            "каких персонажах будем смотреть видео.</p>"
            + pic("gf_family_party", "", "480px") +
            "<p>Теперь посмотри видео один раз и проверь себя — угадал ли ты?</p>"
            "<p>Затем посмотри видео снова и повторяй за персонажами.</p>"}),

        # 7
        ("video", {"title": "Видео 2: Gravity Falls", "url": "", "provider": "file"}),

        ("match", {"title": "Сейчас посмотри видео ещё раз и соедини вопрос с правильным "
                            "ответом. Так ты сможешь получить ещё 1 ⭐️.",
                   "pairs": [
            {"left": "Is Dipper wearing a cap?", "right": "Yes, he is.",
             "right_audio_tts": "Yes, he is."},
            {"left": "Is Mabel wearing a yellow sweater?", "right": "No, she isn’t.",
             "right_audio_tts": "No, she isn't."},
        ]}),

        # 9 — аудио в выгрузке пустое; наш текст для озвучки, СОСТАВ МОЙ
        ("text", {"html":
            f'<p><img src="{shared("well_done_smiley")}" alt="" style="height:140px"></p>'
            "<p>Молодец!</p>"
            "<p>Теперь время практики. Внизу ты найдёшь картинку с одеждой четырёх "
            "ребят. Прослушай аудио и соедини имена с одеждой. Это задание "
            "оценивается в целых 2 ⭐️⭐️.</p>",
            "audio": "", "audio_tts": HW3_SCRIPT}),

        ("match", {"title": "Прослушай аудио и отметь, где чья одежда (соедини имя и "
                            "картинку).",
                   "pairs": [{"left": n, "right": "одежда " + n, "right_image": c(f)}
                             for n, f in HW3_NAMES]}),

        ("text", {"html":
            "<p>Отлично! Ты справился с большей частью заданий. Ты — молодец.</p>"
            "<p>Посмотри ещё раз на картинку из предыдущего задания и ответь на "
            "вопросы ниже. За это задание ты получишь 2 ⭐️⭐️.</p>"}),

        # 12 — в выгрузке ответы не отмечены; ключ — по нашей картинке
        ("quiz", {"title": "Ответь на вопросы", "questions": [
            yes_no("Is Tom wearing a grey T-shirt?", c("hw3_four_outfits"),
                   ["Yes, he is.", "No, he isn't."], 1),
            yes_no("Is Kate wearing a white skirt?", c("hw3_four_outfits"),
                   ["No, she isn't.", "Yes, she is."], 1),
            yes_no("Is Sam wearing a cap?", c("hw3_four_outfits"),
                   ["Yes, he is.", "No, he isn't."], 0),
            yes_no("Is Any wearing a red sweater?", c("hw3_four_outfits"),
                   ["Yes, she is.", "No, she isn't."], 1),
        ]}),

        # 13 — образец ответа (аудио) в выгрузке пустой
        ("speaking", {
            "title": "Опиши одного из героев 🎤",
            "needs_review": True,
            "image": c("gf_mabel_dipper"),
            "sample": "",
            "sample_tts": "This is Mabel. She is wearing a pink sweater and a purple skirt.",
            "html":
                "<p>Посмотри на картинку. На ней герои мультфильма Gravity Falls — "
                "Mabel и Dipper. Опиши одного из героев.</p>"
                "<p>Сначала послушай пример ответа.</p>"}),

        # 14 — Wordwall «Заполни пропуски», обложка пустая. СОСТАВ МОЙ.
        ("gaps", {
            "title": "Ты выполнил все задания из основной части! А это дополнительное "
                     "задание — для настоящих чемпионов! Заполни пропуски: is или isn't.",
            "text":
                "1. __Is__ Dipper wearing a cap? — Yes, he is.\n"
                "2. Is Mabel wearing a yellow sweater? — No, she __isn't|isn’t|is not__.\n"
                "3. Darius __is__ wearing a white T-shirt.\n"
                "4. Is Mabel wearing a purple skirt? — Yes, she __is__.\n"
                "5. Is Dipper wearing a dress? — No, he __isn't|isn’t|is not__.",
            "gaps_expected": 5,
        }),

        # 15–16 — Wordwall «Расставь слова в правильном порядке», обложка пустая.
        # СОСТАВ МОЙ.
        order("Is Mabel wearing a pink sweater?",
              ["Is", "Mabel", "wearing", "a", "pink", "sweater?"], c("char_mabel_card")),
        order("He is wearing a white T-shirt.",
              ["He", "is", "wearing", "a", "white", "T-shirt."], c("char_darius")),

        bye("<h3>Поздравляю! Ты завершил домашнее задание, ты молодец!</h3>"
            "<p>Жду тебя на занятии!</p>", "hello_wave"),
    ],
}

# ------------------------------------------------------------------ HW4
# (1) — история «The cap» (аудио, кадры, задания), (2) — интерактивное видео
# «SM2ed Animated story video» (Rutube, 1:39) с 9 заданиями по таймкодам;
# содержимого заданий видео в выгрузке нет. Прощание (1) и приветствие (2)
# сведены в перемычку. Бл. 2 части (1) — реклама для родителей.
CAP_ORDER = ["My cap isn't here.", "Look! Gary's wearing my cap.",
             "That's my cap, Gary.", "No, it's my cap.",
             "Oh no! That's my cap!", "I'm very sorry, Gary."]

LESSONS["u7_hw4"] = {
    "unit": U, "unit_title": UNIT, "unit_sort": 7,
    "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework",
    "blocks": [
        hello("<h2>Привет! 👋</h2>"
              "<p>Сегодня мы с тобой послушаем и прочитаем рассказ о наших "
              "супердрузьях!</p>"
              "<p>В конце урока тебя ждёт интерактивное видео — оно дополнительное, "
              "его можно сделать по желанию, но ты будешь МЕГА крут, когда "
              "справишься с ним!</p>", "hello_headphones"),

        ("text", {"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
                  + pic("story_cap_phrases", "Story — The Cap (Key Phrases)")}),

        # 3 — аудио истории в выгрузке пустое
        ("text", {"html":
            "<p>Твоё первое задание — послушать аудио и выполнить тест под ним.</p>"
            + pic("story_cap_cover", "The cap", "480px") +
            "<p>Но сначала попробуй угадать, какое приключение ждёт наших Супердрузей "
            "в этот раз. Название истории — <b>The cap</b>. Может, что-то случится с "
            "кепкой?</p>"
            "<p>Прослушай аудио и узнай, угадал ли ты.</p>",
            "audio": ""}),

        # 4 — в выгрузке ответ не отмечен; посчитано по тексту истории: название 1,
        # кадры 1 (1), 2 (2), 3 (2), 4 (1), 7 (1) = 8
        ("quiz", {"title": "Сколько раз звучит слово cap?", "questions": [
            {"q": "Прослушай историю ещё раз. Посчитай, сколько раз звучит слово "
                  "<b>cap</b>, и выбери правильный ответ. (Название истории тоже "
                  "считается.)", "type": "single", "image": c("cap_yellow_clipart"),
             "options": [{"text": "8"}, {"text": "10"}, {"text": "4"}, {"text": "6"}],
             "correct": [0]},
        ]}),

        ("text", {"html":
            "<p>Внимательно прочитай историю и выполни упражнение, которое ты увидишь "
            "сразу после рассказа.</p>"
            + pic("story_cap_1_4", "The cap, 1–4") + pic("story_cap_5_8", "The cap, 5–8")}),

        ("sequence", {"title": "Сейчас прочитай текст ещё раз и выполни задание — расставь "
                               "предложения в правильном порядке, как они идут в рассказе! "
                               "У тебя получится!",
                      "image": c("cap_yellow_clipart"),
                      "items": [{"text": t, "audio_tts": t} for t in CAP_ORDER]}),

        # 7 — перемычка: прощание (1) + приветствие (2)
        ("text", {"html":
            f'<p><img src="{shared("well_done_clap")}" alt="" style="height:160px"></p>'
            "<h3>Поздравляю! Основная часть готова, ты замечательный ученик! ✨</h3>"
            "<p>А теперь — дополнительное задание: мультфильм. Посмотри его "
            "внимательно, а потом посмотри ещё раз и повторяй за героями.</p>"}),

        # 8
        ("video", {"title": "Мультфильм Unit 7", "url": "", "provider": "file"}),

        bye("<h3>Отличная работа!</h3>"
            "<p>Жду тебя на занятии!</p>", "well_done_trophy"),
    ],
}

# ------------------------------------------------------------------ HW5
# Бл. 2 — реклама для родителей (и ещё раз на стр. 17), не переносим. Фото
# фокусника (бл. 4) — стоковое, не берём. Бл. 6 (отметь одежду героев
# видео: trousers, skirt, shorts, cap, jeans, shoes, sweater, jacket) — ответы
# не отмечены, видео нет: в урок не положен, в доработку. Фото людей к
# «расставь слова» заменены нашими картинками и клипартом из PDF.
# Бл. 14 — две игры Wordwall, обложки пустые: СОСТАВ МОЙ.
TFN = ["True", "False", "Not stated"]

LESSONS["u7_hw5"] = {
    "unit": U, "unit_title": UNIT, "unit_sort": 7,
    "lesson_title": "Homework 5", "lesson_sort": 4, "kind": "homework",
    "blocks": [
        hello("<h2>Добро пожаловать в домашнее задание! 👋</h2>"
              "<p>Тебя ждут интересные упражнения и увлекательное видео, а также "
              "ДОПОЛНИТЕЛЬНОЕ задание, которое можно выполнить ПО ЖЕЛАНИЮ и получить "
              "дополнительные кристаллы 💎.</p>"
              "<p>Чтобы стать ЧЕМПИОНОМ — собери все кристаллы, которые ты будешь "
              "получать за выполнение каждого упражнения.</p>"),

        ("text", {"html":
            "<p>Сейчас тебе нужно посмотреть видео и выполнить задание.</p>"
            "<p>Главные герои видео выступают на шоу талантов и показывают фокусы с "
            "помощью одежды. Как думаешь, какие фокусы они показывают?</p>"
            "<p>Посмотри видео и узнай, угадал ли ты 🎩</p>"}),

        # 3
        ("video", {"title": "Видео: шоу талантов", "url": "", "provider": "file"}),

        ("text", {"html":
            "<p>Внимательно посмотри на картинку.</p>"
            + pic("party_scene_names", "Emma, Ken, Lara, Paul") +
            "<p>Под картинкой есть предложения. Прочитай их и скажи, это правда "
            "(True) или неправда (False). Если по картинке нельзя определить, правда "
            "это или неправда, выбери <b>Not stated</b>.</p>"
            "<p>За это задание ты можешь заработать 2 💎💎</p>"}),

        # 5 — в выгрузке ответы не отмечены (и нет кнопки Not stated); ключ — по
        # картинке: Lara сидит за столом, ног не видно → Not stated
        ("quiz", {"title": "True, False или Not stated?", "questions": [
            yes_no("Emma is watching TV.", c("party_scene_names"), TFN, 0),
            yes_no("Ken is playing a game.", c("party_scene_names"), TFN, 0),
            yes_no("Lara is wearing pink jeans.", c("party_scene_names"), TFN, 2),
            yes_no("Paul is playing computer games.", c("party_scene_names"), TFN, 1),
            yes_no("Ken is wearing a yellow sweater.", c("party_scene_names"), TFN, 0),
            yes_no("Emma is wearing a green T-shirt.", c("party_scene_names"), TFN, 1),
        ]}),

        ("text", {"html":
            "<p>А в следующем упражнении мы с тобой потренируемся составлять "
            "предложения.</p>"
            "<p>Расставь слова в правильном порядке, чтобы получилось предложение. "
            "Тебя ждут 6 таких предложений. Составь их и получи 2 💎💎</p>"}),

        # 7–12
        order("Anna is wearing a blue skirt.",
              ["Anna", "is", "wearing", "a", "blue", "skirt."], c("outfit_anna")),
        order("What is Bob doing?", ["What", "is", "Bob", "doing?"], c("boy_singing")),
        order("Are Amy and Hannah riding bikes?",
              ["Are", "Amy and Hannah", "riding", "bikes?"], c("obj_bikes")),
        order("Emma and Tom are watching TV.",
              ["Emma and Tom", "are", "watching", "TV."], c("watching_tv_clipart")),
        order("Is Sam eating a sandwich?",
              ["Is", "Sam", "eating", "a sandwich?"], c("obj_sandwich")),
        order("Is Oscar playing football?",
              ["Is", "Oscar", "playing", "football?"], c("football_ball")),

        # 13 — текст и запись голоса (бл. 11–12 выгрузки)
        ("speaking", {
            "title": "Прочитай вслух 🎤",
            "needs_review": True,
            "image": c("emma_singing"),
            "sample": "",
            "sample_tts": "Emma is my best friend. Emma is wearing a pink T-shirt, green "
                          "trousers and black shoes. She is singing.",
            "html":
                "<p>Посмотри! На картинке моя подруга. Её зовут Эмма!</p>"
                "<p>Посмотри на картинку и прочитай описание девочки. Нажми на микрофон "
                "и запиши, как ты читаешь текст вслух. За это задание ты получишь "
                "3 💎💎💎</p>"
                "<p><b>Emma is my best friend.<br>Emma is wearing a pink T-shirt, green "
                "trousers and black shoes.<br>She is singing.</b></p>"}),

        ("task", {
            "title": "Нарисуй своего друга",
            "needs_review": True,
            "html":
                "<p>Нарисуй своего друга, опиши его и покажи рисунок на уроке. Используй "
                "предыдущее упражнение как пример.</p>"
                "<p>Напиши 3–5 предложений. За это задание ты получишь 4 💎💎💎💎</p>"
                "<p><i>My best friend is … He/She is wearing … He/She is …</i></p>"}),

        # 15 — Wordwall «Впиши слова», обложка пустая. СОСТАВ МОЙ.
        ("exact_input", {"items": [
            {"image": c(f), "prompt": (
                "Ты выполнил все задания из основной части! А это дополнительное "
                "задание — для настоящих чемпионов! Впиши слово с -ing.<br>" if i == 0
                else "") + p, "accept": acc}
            for i, (f, p, acc) in enumerate([
                ("watching_tv_clipart", "Emma and Tom are ___ TV. (watch)", ["watching"]),
                ("boy_singing", "Bob is ___. (sing)", ["singing"]),
                ("obj_sandwich", "Sam is ___ a sandwich. (eat)", ["eating"]),
                ("obj_bikes", "Amy and Hannah are ___ bikes. (ride)", ["riding"]),
                ("football_ball", "Oscar is ___ football. (play)", ["playing"]),
                ("emma_singing", "Emma is ___ a pink T-shirt. (wear)", ["wearing"]),
            ])
        ]}),

        # 16 — Wordwall «Выбери правильный вариант», обложка пустая. СОСТАВ МОЙ.
        ("quiz", {"title": "Выбери правильный вариант", "questions": [
            yes_no("Выбери правильный вариант:<br>Emma ___ watching TV.",
                   c("party_scene_names"), ["is", "are", "am"], 0),
            yes_no("___ Ken playing a game? — Yes, he is.", c("party_scene_names"),
                   ["Are", "Is", "Do"], 1),
            yes_no("Is Paul eating cake? — Yes, he ___.", c("party_scene_names"),
                   ["isn't", "does", "is"], 2),
            yes_no("Lara ___ playing football. She's playing a computer game.",
                   c("party_scene_names"), ["is", "isn't", "aren't"], 1),
            yes_no("Ken is ___ a yellow sweater.", c("party_scene_names"),
                   ["wear", "wearing", "wears"], 1),
        ]}),

        bye("<h3>Поздравляю! Ты завершил домашнее задание! Молодец!</h3>"
            "<p>За прохождение домашнего задания держи ещё 1 дополнительный 💎</p>"
            "<p>Жду тебя на занятии!</p>", "well_done_medal"),
    ],
}

LESSONS = {k: LESSONS[k] for k in
           ["u7_hw1", "u7_hw2", "u7_hw3", "u7_hw4", "u7_hw5", "u7_hw6", "u7_hw7", "u7_test"]}
