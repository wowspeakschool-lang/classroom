#!/usr/bin/env python3
"""Go Getter 1 · Unit 2 · My things — уроки (разбор: docs/GG1_разбор/u2.md).

Одежда, прилагательные, this / that / these / those, too, вопросы с to be и
краткие ответы, личные вопросы, гаджеты. Картинки одежды — листы Л2.1–Л2.6;
фото вещей со стрелкой «далеко / близко» в тесте — из выгрузки.
"""
from gg1_lib import *  # noqa: F401,F403

U = "u2"
U2 = {"unit": U, "unit_title": "Unit 2 · My things", "unit_sort": 2}


def u(name):
    return img(U, name)


U2_CLOTHES = vocab([
    ("coat", "пальто", "clothes_coat"),
    ("jeans", "джинсы", "clothes_jeans"),
    ("shoes", "обувь", "clothes_shoes"),
    ("skirt", "юбка", "clothes_skirt"),
    ("T-shirt", "футболка", "clothes_tshirt"),
    ("trousers", "брюки", "clothes_trousers"),
    ("boots", "сапоги", "clothes_boots"),
    ("cap", "кепка", "clothes_cap"),
    ("dress", "платье", "clothes_dress"),
    ("hoodie", "толстовка с капюшоном", "clothes_hoodie"),
    ("jacket", "куртка", "clothes_jacket"),
    ("shirt", "рубашка", "clothes_shirt"),
    ("jumper", "свитер", "clothes_jumper"),
    ("tracksuit", "спортивный костюм", "clothes_tracksuit"),
    ("gloves", "перчатки", "clothes_gloves"),
    ("scarf", "шарф", "clothes_scarf"),
    ("shorts", "шорты", "clothes_shorts"),
    ("trainers", "кроссовки", "clothes_trainers"),
    ("top", "топ", "clothes_top"),
])

U2_ADJ = vocab([
    ("big", "большой", "adj_big_small"),
    ("small", "маленький", "adj_big_small"),
    ("long", "длинный", "adj_long_short"),
    ("short", "короткий", "adj_long_short"),
    ("new", "новый", "adj_new_old"),
    ("old", "старый", "adj_new_old"),
    ("cool", "классный", "adj_cool_boring"),
    ("boring", "скучный", "adj_cool_boring"),
    ("too", "слишком", "adj_too_big"),
])

CHAMPION = ("Ты выполнил все задания из основной части! А это дополнительное задание — "
            "для настоящих чемпионов! ")
REVIEW = "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"


def clothes(en):
    return u(next(p for e, r, p in U2_CLOTHES if e == en))


LESSONS = {
    # Homework 1 (1) — словарный тренажёр «одежда», (2) — задания. Один урок.
    "u2_hw1": {
        **U2,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня мы учим слова про одежду. Выполни все "
                  "задания, чтобы выучить их на все 100!</p>"),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U2_CLOTHES
            ]}),

            ("match", {"title": "Соедини картинку и слово", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in U2_CLOTHES[:10]
            ]}),

            ("match", {"title": "И ещё: соедини картинку и слово", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in U2_CLOTHES[10:]
            ]}),

            ("quiz", quiz_ru_to_en(U2_CLOTHES[:10])),

            ("exact_input", {"title": "Посмотри на картинку и напиши слово по-английски", "items": [
                {"prompt": ru, "accept": list(dict.fromkeys([en, en.lower(), en.capitalize()])), "image": u(p),
                 "audio_tts": en}
                for en, ru, p in U2_CLOTHES[10:]
            ]}),

            ("text", {"html": "<h3>Добро пожаловать во вторую часть домашнего задания! 👋</h3>"
                              + REVIEW + pic(u("card_clothes"), "Clothes")}),

            ("match", {"title": "Найди пары", "pairs": [
                {"left": en, "right": ru, "left_audio_tts": en}
                for en, ru, p in U2_CLOTHES[:10]
            ]}),

            # в выгрузке — клипарт с детьми, у нас сгенерированная картинка с той же одеждой
            ("gaps", {
                "title": "Посмотри на картинку и впиши название одежды",
                "mode": "type",
                "image": u("kids_outfits"),
                "text": "1. Her __jacket__ is grey.\n"
                        "2. Her __jumper__ is pink.\n"
                        "3. Her __jeans__ are blue.\n"
                        "4. Her __boots__ are brown.\n"
                        "5. His __cap__ is blue.\n"
                        "6. His __hoodie__ is green.\n"
                        "7. His __trousers__ are black.\n"
                        "8. His __shoes|trainers__ are white.",
                "gaps_expected": 8,
            }),

            ("speaking", {
                "title": "Моя одежда 🎤",
                "html": "<p>А теперь нажми на микрофон и перечисли, какая одежда у тебя есть.</p>"
                        "<p><i>Пример: I've got a blue T-shirt, black jeans and white trainers.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Gameshow quiz · Copy of GG1 2.1 clothes» — СОСТАВ МОЙ
            mcq(CHAMPION + "Что на картинке? ⭐", [
                ("What's this?", ["a skirt", "a dress", "a top"], "a dress", clothes("dress")),
                ("What's this?", ["a jumper", "a hoodie", "a jacket"], "a hoodie", clothes("hoodie")),
                ("What are these?", ["trainers", "boots", "shoes"], "boots", clothes("boots")),
                ("What are these?", ["shorts", "trousers", "jeans"], "shorts", clothes("shorts")),
                ("What's this?", ["a scarf", "a cap", "a coat"], "a scarf", clothes("scarf")),
                ("What are these?", ["gloves", "shoes", "trainers"], "gloves", clothes("gloves")),
            ]),

            # Wordwall «Quiz · GG1 2.1 It is They are» — СОСТАВ МОЙ
            mcq("It is или They are? Выбери правильный вариант ⭐", [
                ("___ a T-shirt.", ["It's", "They're"], "It's", clothes("T-shirt")),
                ("___ trousers.", ["They're", "It's"], "They're", clothes("trousers")),
                ("___ a coat.", ["It's", "They're"], "It's", clothes("coat")),
                ("___ jeans.", ["They're", "It's"], "They're", clothes("jeans")),
                ("The skirt ___ blue.", ["is", "are"], "is", clothes("skirt")),
                ("The trainers ___ white.", ["are", "is"], "are", clothes("trainers")),
            ]),

            bye("<h3>Ура, ты выполнил все задания, ты большой молодец! 🎉</h3>"
                "<p>Увидимся на занятии!</p>", "well_done_star"),
        ],
    },

    # Homework 2 (1) — тренажёр «прилагательные», (2) — this / that / these / those, too.
    "u2_hw2": {
        **U2,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На занятии мы выучили много новых слов! Выполни все "
                  "задания, чтобы запомнить их на все 100!</p>", "hello_book"),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U2_ADJ
            ]}),

            ("quiz", quiz_ru_to_en(U2_ADJ)),

            ("match", {"title": "Соедини слова с противоположным значением", "pairs": [
                {"left": "big", "right": "small"},
                {"left": "long", "right": "short"},
                {"left": "new", "right": "old"},
                {"left": "cool", "right": "boring"},
            ]}),

            ("gaps", {
                "title": "Заполни пропуски",
                "mode": "drag",
                "text": "This jacket is __too__ big for the hanger.\n"
                        "My scarf is very __long__.\n"
                        "These trainers are __old__ and dirty.\n"
                        "My new cap is __cool__!\n"
                        "This T-shirt is very __small__.\n"
                        "That grey cap is __boring__.",
                "gaps_expected": 6,
            }),

            ("text", {"html": "<h3>Hello! 👋</h3><p>На занятии мы говорили о предметах, которые "
                              "находятся далеко или близко. Повторим?</p>" + REVIEW
                              + pic(u("card_adjectives"), "Adjectives")
                              + pic(u("card_this_that"), "this / that / these / those")
                              + pic(u("card_too"), "too")}),

            # в выгрузке правые половины пустые — картинки наши (Л2.5), СОСТАВ МОЙ
            ("match", {"title": "Соедини слово и картинку", "pairs": [
                {"left": "This", "right_image": u("dem_this")},
                {"left": "These", "right_image": u("dem_these")},
                {"left": "That", "right_image": u("dem_that")},
                {"left": "Those", "right_image": u("dem_those")},
            ]}),

            ("sort", {"title": "Какие слова означают, что предмет далеко, а какие — близко?",
                      "groups": [
                          {"name": "Далеко", "items": [{"text": "That"}, {"text": "Those"}]},
                          {"name": "Близко", "items": [{"text": "This"}, {"text": "These"}]},
                      ]}),

            ("sort", {"title": "Какие слова означают, что предмет один, а какие — что их много?",
                      "groups": [
                          {"name": "Один", "items": [{"text": "This"}, {"text": "That"}]},
                          {"name": "Много", "items": [{"text": "These"}, {"text": "Those"}]},
                      ]}),

            ("speaking", {
                "title": "Моя одежда и чужая 🎤",
                "html": "<p>Нажми на микрофон и опиши свою и чужую одежду. Используй this / that / "
                        "these / those и прилагательные (new, old, big, small, cool).</p>"
                        "<p><i>Пример: This is my new T-shirt. It's cool. Those are my old shoes. "
                        "They're small. These trainers are blue.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Quiz · This That These Those» — СОСТАВ МОЙ
            mcq("Давай теперь поиграем с этими словами! Выбери правильное слово", [
                ("___ T-shirt is blue.", ["This", "That", "These", "Those"], "This", u("dem_this")),
                ("___ T-shirt is far away.", ["This", "That", "These", "Those"], "That", u("dem_that")),
                ("___ T-shirts are new.", ["This", "That", "These", "Those"], "These", u("dem_these")),
                ("___ T-shirts are blue.", ["This", "That", "These", "Those"], "Those", u("dem_those")),
            ]),

            # Wordwall «Find the match · gg1 2.2» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини слово и перевод ⭐", "pairs": [
                {"left": en, "right": ru, "left_audio_tts": en} for en, ru, p in U2_ADJ
            ]}),

            # Wordwall «Unjumble · GG1 2.2» — СОСТАВ МОЙ
            order("These jeans are blue.", title="Расставь слова в правильном порядке ⭐"),
            order("That dress is too long.", title="Расставь слова в правильном порядке ⭐"),
            order("Those trainers are new!", title="Расставь слова в правильном порядке ⭐"),

            bye("<h3>У тебя отлично получилось! 🎉</h3><p>Увидимся на занятии! Bye!</p>",
                "well_done_jump"),
        ],
    },

    "u2_hw3": {
        **U2,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На занятии мы учились задавать вопросы! "
                  "Потренируемся ещё?</p>", "hello_highfive"),

            ("text", {"html": REVIEW + pic(u("card_questions_be"), "Вопросы с to be")
                              + pic(u("card_short_answers"), "Short answers")}),

            mcq("Поставь в конце предложения правильный знак: ? или .", [
                ("Is he French ___", ["?", "."], "?"),
                ("My brother is eight years old ___", ["?", "."], "."),
                ("Are you a student ___", ["?", "."], "?"),
                ("Is Lee your friend ___", ["?", "."], "?"),
                ("I'm cool ___", ["?", "."], "."),
                ("Are they happy ___", ["?", "."], "?"),
            ]),

            ("text", {"html": "<p><b>Посмотри на картинку: это Даг и Кит.</b></p>"
                              + pic(u("comic_kit_dug"), "Kit and Dug")}),

            # в выгрузке «ответь на вопросы из предыдущего задания» — а вопросы про картинку
            ("match", {"title": "Посмотри на картинку и ответь на вопросы", "pairs": [
                {"left": "Is Kit a cat?", "right": "Yes, she is."},
                {"left": "Is she black?", "right": "No, she isn't."},
                {"left": "Are Kit and Dug friends?", "right": "Yes, they are."},
                {"left": "Is Dug's suit blue and red?", "right": "Yes, it is."},
                {"left": "Are they at school?", "right": "No, they aren't."},
                {"left": "Is his suit too small?", "right": "No, it isn't."},
            ]}),

            order("What is your name?", title="Составь вопрос"),
            order("Are you eleven?", title="Составь вопрос"),
            order("Is your best friend ten?", title="Составь вопрос"),

            ("speaking", {
                "title": "В магазине 🎤",
                "html": "<p>Представь, что ты в магазине. Задай вопросы про одежду и ответь на них.</p>"
                        "<p><i>Пример: Is this jacket new? — Yes, it is. Are these shoes too big? — "
                        "No, they aren't. Is the dress too small? — Yes, it is.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Match up · gg1 2.3 photocopiable ex 1» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини вопросы с ответами ⭐", "pairs": [
                {"left": "Are you a student?", "right": "Yes, I am."},
                {"left": "Is she your sister?", "right": "No, she isn't."},
                {"left": "Are they OK?", "right": "Yes, they are."},
                {"left": "Is it your bag?", "right": "Yes, it is."},
                {"left": "Is he French?", "right": "No, he isn't."},
                {"left": "Are we late?", "right": "No, we aren't."},
                {"left": "Am I right?", "right": "Yes, you are."},
            ]}),

            # Wordwall «Unjumble · GG1 2.3» — СОСТАВ МОЙ
            order("Is this jacket new?", title="Расставь слова в правильном порядке ⭐"),
            order("Are these your shoes?", title="Расставь слова в правильном порядке ⭐"),

            bye("<h3>Отличная работа! 🎉</h3><p>Увидимся на занятии! Bye!</p>", "well_done_clap"),
        ],
    },

    "u2_hw4": {
        **U2,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На занятии мы много говорили о нас самих, учились задавать "
                  "вопросы и отвечать на них. Закрепим?</p>", "hello_laptop"),

            ("text", {"html": REVIEW + pic(u("card_personal_info"), "Personal information")}),

            ("gaps", {
                "title": "Девочка по имени Нэнси попала на телешоу! Во время разговора с ведущим "
                         "возникли помехи, и некоторые фразы было не слышно. Восстанови их!",
                "mode": "drag",
                "image": u("nancy_show"),
                "text": "Man: Hi. Welcome to the show. __What's your name?__\n"
                        "Nancy: My name's Nancy.\n"
                        "Man: Where are you from?\n"
                        "Nancy: __London, England.__\n"
                        "Man: __How old are you?__\n"
                        "Nancy: I'm eleven.\n"
                        "Man: What's your favourite sport?\n"
                        "Nancy: __Swimming. I love it.__\n"
                        "Man: Who's your favourite actor?\n"
                        "Nancy: __Asa Butterfield.__",
                "gaps_expected": 5,
            }),

            mcq("Выбери правильное вопросительное слово", [
                ("___ is your name?", ["What", "Who"], "What"),
                ("___ are you from?", ["Where", "What"], "Where"),
                ("___ old are you?", ["How", "Where"], "How"),
                ("___ is your favourite sports person?", ["Who", "Where"], "Who"),
                ("___ is your favourite film?", ["What", "Who"], "What"),
            ]),

            ("match", {"title": "Соедини вопросы из предыдущего задания с ответами", "pairs": [
                {"left": "What is your name?", "right": "I'm Danny."},
                {"left": "Where are you from?", "right": "Manchester, England."},
                {"left": "How old are you?", "right": "Ten."},
                {"left": "Who is your favourite sports person?",
                 "right": "Renato Sanches. He's from Portugal."},
                {"left": "What is your favourite film?", "right": "The Incredibles."},
            ]}),

            # в выгрузке статья — страница учебника с фото детей; у нас текстом
            ("text", {"html":
                "<p><b>В школе появилась новая ученица — Эмма. Прочитай статью о ней.</b></p>"
                + pic(u("emma_new_girl"), "Emma", 220)
                + "<p><b>Welcome, Emma!</b> <i>by Ben Carter</i></p>"
                "<p><i>Emma is new to our school. She's ten, and she's from Cardiff, Wales. Her "
                "favourite sport is tennis, and her favourite book is The Hobbit. Her favourite "
                "singer is Alicia Keys. Welcome to our school, Emma!</i></p>"}),

            ("gaps", {
                "title": "Какие вопросы задавали Эмме, чтобы написать эту статью? Допиши их",
                "mode": "type",
                "text": "1. How old are you?\n"
                        "2. Where __are you from__?\n"
                        "3. What __is your favourite sport|'s your favourite sport__?\n"
                        "4. What __is your favourite book|'s your favourite book__?\n"
                        "5. Who __is your favourite singer|'s your favourite singer__?",
                "gaps_expected": 4,
            }),

            ("task", {
                "title": "Задание со звёздочкой ⭐",
                "needs_review": True,
                "html": "<p>Если ты его выполнишь, станешь настоящим мастером английского языка! "
                        "Ответь на вопросы из предыдущего задания:</p>"
                        "<ol><li>How old are you?</li><li>Where are you from?</li>"
                        "<li>What is your favourite sport?</li><li>What is your favourite book?</li>"
                        "<li>Who is your favourite singer?</li></ol>",
            }),

            bye("<h3>У тебя отлично получилось! 🎉</h3><p>Увидимся на занятии! Bye!</p>",
                "well_done_smiley"),
        ],
    },

    "u2_hw5": {
        **U2,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На занятии ты нарисовал свой суперрюкзак. Расскажешь мне "
                  "про него? Но сначала давай вспомним некоторые слова и соединим половинки "
                  "друг с другом.</p>", "hello_rocket"),

            ("match", {"title": "Соедини половинки слов", "pairs": [
                {"left": "back", "right": "pack"},
                {"left": "games", "right": "console"},
                {"left": "mobile", "right": "phone"},
                {"left": "mountain", "right": "bike"},
                {"left": "laptop", "right": "computer"},
                {"left": "skate", "right": "board"},
            ]}),

            # статья учебника — с фото мальчика; у нас картинки Л2.3/Л2.4 и текст
            ("text", {"html":
                "<p><b>Прочитай статью про суперрюкзак Джейми.</b></p>"
                + pic(u("jamie_super_backpack"), "Jamie", 240)
                + "<p><i>Jamie Cooper's 13. He's from Liverpool in the UK. Jamie's super backpack is "
                "our gadget of the week. Why? Read on.</i></p>"
                + pic(u("super_backpack"), "Super backpack", 220)
                + "<p><i>What's in the picture? Yes, that's right. It's a red backpack. It's a super "
                "backpack! It's very, very cool. Look again. This super backpack is also a mountain "
                "bike. It's small but it isn't too small. It's fantastic! And that's not all. Think "
                "about it. You're in the park with your friends. You're cold and your jumper is at "
                "home. No problem. This super backpack is a big jacket too. What about your other "
                "things? Don't worry! Super backpack is just the right size for your laptop computer, "
                "your mobile phone, your new games and other favourites. There's even a pocket for a "
                "small pet like my cat Fiona. How cool is that?</i></p>"}),

            ("task", {
                "title": "Мой суперрюкзак 🎒",
                "needs_review": True,
                "html": "<p>Теперь пришло время рассказать про суперрюкзак, который ты нарисовал! "
                        "А если ты ещё и прикрепишь фотографию своего рисунка, будет вообще здорово!</p>"
                        "<p><i>Пример: My super backpack is blue. It's big but it isn't too big. "
                        "It's a skateboard too! There's a pocket for my mobile phone.</i></p>",
            }),

            bye("<h3>Ух ты! Вот это рюкзак! 🎉</h3><p>Он и правда СУПЕРрюкзак! "
                "До встречи на занятии! Bye!</p>", "well_done_medal"),
        ],
    },

    "u2_hw6": {
        **U2,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На занятии ты написал пару предложений про свой любимый "
                  "предмет. Расскажешь? Но сначала давай вспомним, какие бывают любимые предметы.</p>",
                  "hello_headphones"),

            ("hotspot", {
                "title": "Подпиши названия предметов на картинке",
                "mode": "label",
                "image": u("icons_favourite_things"),
                "points": [
                    {"x": 32.0, "y": 26.0, "text": "trainers"},
                    {"x": 80.0, "y": 26.0, "text": "backpack"},
                    {"x": 32.0, "y": 58.0, "text": "mountain bike"},
                    {"x": 80.0, "y": 58.0, "text": "hoodie"},
                    {"x": 32.0, "y": 91.0, "text": "mobile phone"},
                    {"x": 80.0, "y": 91.0, "text": "games console"},
                ],
                "extras": [],
            }),

            listening("Послушай, о чём говорят Люк и Роза. Потом выполни задания ниже."),

            ("quiz", {"title": "Какие предметы упоминают Люк и Роза? Отметь все", "questions": [{
                "q": "Luke and Rosa talk about…",
                "type": "multiple",
                "options": [{"text": t} for t in ["hoodie", "mountain bike", "games console",
                                                  "skateboard", "backpack", "trainers",
                                                  "mobile phone"]],
                "correct": [1, 2, 3, 5, 6],
            }]}),

            # в выгрузке у этих четырёх вопросов варианты ответа пустые, а аудио нет —
            # ответы проверяет учитель; строка в доработать
            ("task", {
                "title": "Послушай аудио ещё раз и допиши предложения",
                "needs_review": True,
                "html": "<ol><li>Luke's ______ is new.</li>"
                        "<li>Rosa's favourite colour is ______.</li>"
                        "<li>Luke's trainers are ______.</li>"
                        "<li>Rosa's favourite thing is her ______.</li></ol>",
            }),

            ("speaking", {
                "title": "Моя любимая вещь 🎤",
                "html": "<p>Теперь твоя очередь! Расскажи о своей любимой вещи. Не забудь ответить "
                        "на вопросы: What is your name? What is your favourite thing? What is your "
                        "favourite colour? В качестве образца можешь использовать аудио выше.</p>",
                "needs_review": True,
            }),

            bye("<h3>Спасибо тебе за интересный рассказ! 🎉</h3><p>Увидимся на занятии! Bye!</p>",
                "well_done_trophy"),
        ],
    },

    "u2_hw7": {
        **U2,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На следующем занятии тебя ждёт очень интересный тест! "
                  "Давай подготовимся к нему получше?</p>", "hello_book"),

            # в выгрузке во втором вопросе отмечено fantastic — исправлено на boring
            mcq("Найди лишнее слово и отметь его", [
                ("T-shirt / boots / shoes", ["T-shirt", "boots", "shoes"], "T-shirt"),
                ("cool / fantastic / boring", ["cool", "fantastic", "boring"], "boring"),
                ("backpack / top / dress", ["backpack", "top", "dress"], "backpack"),
                ("long / big / top", ["long", "big", "top"], "top"),
                ("jacket / skirt / coat", ["jacket", "skirt", "coat"], "skirt"),
            ]),

            ("hotspot", {
                "title": "Посмотри на картинку и соедини слова с предметами",
                "mode": "label",
                "image": u("boy_skater"),
                "points": [
                    {"x": 55.0, "y": 7.0, "text": "cap"},
                    {"x": 88.0, "y": 30.0, "text": "mobile phone"},
                    {"x": 76.0, "y": 38.0, "text": "shirt"},
                    {"x": 60.0, "y": 70.0, "text": "jeans"},
                    {"x": 78.0, "y": 92.0, "text": "trainers"},
                    {"x": 22.0, "y": 72.0, "text": "skateboard"},
                ],
                "extras": [],
            }),

            mcq("Выбери правильный вариант ответа", [
                ("My shoes ___ too small.", ["are", "is"], "are"),
                ("___ T-shirt isn't big.", ["This", "These"], "This"),
                ("What ___ it?", ["is", "are"], "is"),
                ("___ are my brothers.", ["Those", "That"], "Those"),
                ("Her boots ___ cool.", ["are", "is"], "are"),
                ("___ they your books?", ["Are", "Is"], "Are"),
            ]),

            ("sequence", {"title": "Расставь предложения так, чтобы получился диалог", "items": [
                {"text": "Hello, I'm Benjamin. What's your name?"},
                {"text": "Hi. I'm Jackie. I'm from England. Where are you from?"},
                {"text": "I'm from England too. How old are you?"},
                {"text": "Eleven. Are you 11 too?"},
                {"text": "No, I'm not. I'm 12. What's your favourite book?"},
                {"text": "Harry Potter, Book One."},
            ]}),

            ("speaking", {
                "title": "Моя любимая футболка 🎤",
                "html": "<p>Нажми на микрофон и опиши свою любимую футболку или топ.</p>"
                        "<p><i>Пример: This is my favourite top. It's blue with red squares, yellow "
                        "triangles and green lines. I love it!</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Crossword · Go Getter 1 Unit 2.1 Clothes» — СОСТАВ МОЙ
            ("exact_input", {"title": CHAMPION + "Впиши слова ⭐", "items": [
                {"prompt": f"{len(en)} букв", "accept": [en, en.capitalize()],
                 "image": clothes(en), "audio_tts": en}
                for en in ["jacket", "skirt", "trousers", "jumper", "scarf", "tracksuit"]
            ]}),

            # Wordwall «Match up · Unit 2.2 Adjectives» — СОСТАВ МОЙ
            ("match", {"title": "Соедини ⭐", "pairs": [
                {"left_image": u("adj_big_small"), "right": "big and small"},
                {"left_image": u("adj_long_short"), "right": "long and short"},
                {"left_image": u("adj_new_old"), "right": "new and old"},
                {"left_image": u("adj_cool_boring"), "right": "cool and boring"},
                {"left_image": u("adj_too_big"), "right": "too big"},
            ]}),

            # Wordwall «Match up · gg1 2.3 photocopiable ex 1» (та же игра, что в
            # Homework 3) — здесь другие пары, СОСТАВ МОЙ
            ("match", {"title": "Соедини вопросы с ответами ⭐", "pairs": [
                {"left": "What's your name?", "right": "My name's Lucas."},
                {"left": "How old are you?", "right": "I'm eleven."},
                {"left": "Where are you from?", "right": "I'm from Spain."},
                {"left": "What's your favourite music?", "right": "Rock, I think!"},
                {"left": "Who's your favourite singer?", "right": "Alicia Keys."},
            ]}),

            bye("<h3>У тебя отлично получилось! 🎉</h3><p>Уверена, ты справишься с тестом "
                "на все сто! Удачи!</p>", "good_luck_clover"),
        ],
    },

    "u2_test": {
        **U2,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        "blocks": [
            # в выгрузке пропуск — одна буква; у нас слово целиком
            ("exact_input", {"title": "Посмотри на картинку и впиши слово целиком", "items": [
                {"prompt": hint, "accept": list(dict.fromkeys([en, en.lower()])), "image": clothes(en)}
                for hint, en in [("T-_h_rt", "T-shirt"), ("sk_rt", "skirt"), ("dr_s_", "dress"),
                                 ("tro_s_rs", "trousers"), ("je_ns", "jeans"), ("co_t", "coat")]
            ]}),

            mcq("Прочитай диалог и выбери пропущенные слова. Стрелка показывает, далеко вещь или близко", [
                ("A: ___ is my hoodie. B: Nice! Is it new?", ["That", "This", "These", "Those"],
                 "That", u("far_hoodie")),
                ("A: That is my ___. B: Nice! Is it new?", ["hoodie", "jacket", "T-shirt"], "hoodie"),
            ]),
            mcq("Прочитай диалог и выбери пропущенные слова", [
                ("A: Whose ___ are these? B: They are mine.", ["trainers", "boots", "trousers"],
                 "trainers", u("near_trainers")),
                ("A: Whose trainers are ___? B: They are mine.", ["these", "those", "this", "that"],
                 "these"),
            ]),
            mcq("Прочитай диалог и выбери пропущенные слова", [
                ("A: ___ isn't my tracksuit. B: Whose is it then?", ["This", "That", "These", "Those"],
                 "This", u("near_tracksuit")),
                ("A: This isn't my ___. B: Whose is it then?", ["tracksuit", "trousers"], "tracksuit"),
            ]),
            mcq("Прочитай диалог и выбери пропущенные слова", [
                ("A: ___ is Alex's favourite cap. B: No, it's not! It's mine!",
                 ["That", "This", "These", "Those"], "That", u("far_cap")),
                ("A: That is Alex's favourite ___. B: No, it's not! It's mine!",
                 ["cap", "top", "hat"], "cap"),
            ]),
            mcq("Прочитай диалог и выбери пропущенные слова", [
                ("A: Are ___ your friends' boots? B: I'm not sure.", ["those", "these", "that", "this"],
                 "those", u("far_boots")),
                ("A: Are those your friends' ___? B: I'm not sure.", ["boots", "trainers", "shoes"],
                 "boots"),
            ]),

            order("What is your favourite colour?", title="Расставь слова в правильном порядке",
                  image=u("pencils_heart")),
            order("Are you David Smith's brother?", ["Are", "you", "David Smith's", "brother?"],
                  title="Расставь слова в правильном порядке", image=u("brothers_highfive")),
            order("These boots are too small.", title="Расставь слова в правильном порядке",
                  image=u("boot_black")),
            order("What is your favourite film?", title="Расставь слова в правильном порядке",
                  image=u("cinema")),
            order("Is Anna your best friend?", title="Расставь слова в правильном порядке",
                  image=u("best_friends_girls")),

            # в выгрузке текст — картинкой
            ("text", {"html":
                "<h3>READING</h3><p>Прочитай текст.</p>"
                "<p><i>Today I'm packing my backpack for a school trip. My new red T-shirt is in my "
                "backpack. My old jeans are in my backpack too. My favourite hoodie is too big — "
                "it's not in my backpack. My boots are too old. They are not in my backpack. My phone "
                "and my keys are in my backpack. My tablet is too big — it's not in my backpack. My "
                "small pencil case is in my backpack.</i></p>"}),

            ("sort", {"title": "READING. Распредели вещи по двум столбикам", "groups": [
                {"name": "В рюкзаке", "items": [{"text": t} for t in
                                               ["T-shirt", "jeans", "phone", "keys", "pencil case"]]},
                {"name": "Не в рюкзаке", "items": [{"text": t} for t in ["hoodie", "boots", "tablet"]]},
            ]}),

            listening("LISTENING. Прослушай Эмму: она показывает свои школьные вещи."),

            ("gaps", {
                "title": "LISTENING. Перетащи правильное прилагательное в каждый пропуск",
                "mode": "drag",
                "text": "1. The school bag is __new__.\n"
                        "2. The school shoes are __black__.\n"
                        "3. The favourite jumper is __red__.\n"
                        "4. The old trainers are __boring__.\n"
                        "5. The cap is __cool__.",
                "gaps_expected": 5,
            }),

            ("speaking", {
                "title": "SPEAKING TASK 🎤",
                "image": u("kevin_birthday"),
                "html": "<p>Посмотри на картинку и ответь на вопросы. Запиши свой ответ, нажав на "
                        "кнопку микрофона 🙌</p>"
                        "<ol><li>This is Kevin and his family. Are they in the garden?</li>"
                        "<li>Where are they?</li><li>How old is Kevin?</li>"
                        "<li>Who is Emma? Who is Charles?</li>"
                        "<li>Look at Kevin. Where are Kevin and his family from?</li>"
                        "<li>Where is Giorgio from?</li></ol>",
                "needs_review": True,
            }),
        ],
    },
}
