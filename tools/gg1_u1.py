#!/usr/bin/env python3
"""Go Getter 1 · Unit 1 · Family and friends — уроки (разбор: docs/GG1_разбор/u1.md).

Семья, глагол to be (+ / −), страны и национальности, знакомство.
Фото реальных людей из выгрузки заменены сгенерированными персонажами (листы
Л1.2–Л1.6), флаги рисует tools/gg1_flags.py.
"""
from gg1_lib import *  # noqa: F401,F403

U = "u1"
U1 = {"unit": U, "unit_title": "Unit 1 · Family and friends", "unit_sort": 1}


def u(name):
    return img(U, name)


def flag(country):
    return f"{MEDIA}gg1/u1/flag_{country}.svg"


# ---------- словари ----------

# Словарь Homework 1 (1). В выгрузке «granddad», на карточке методиста и в
# Homework 7 — «grandad»: берём одно написание, как в учебнике.
U1_FAMILY = [
    ("mother", "мать", "fam_mother"),
    ("mum", "мама", "fam_mother"),
    ("father", "отец", "fam_father"),
    ("dad", "папа", "fam_father"),
    ("parents", "родители", "fam_parents"),
    ("grandparents", "бабушка и дедушка", "fam_grandparents"),
    ("grandfather", "дедушка", "fam_grandfather"),
    ("grandad", "дед", "fam_grandfather"),
    ("grandmother", "бабушка", "fam_grandmother"),
    ("granny", "бабуля", "fam_grandmother"),
    ("son", "сын", "fam_son"),
    ("daughter", "дочь", "fam_daughter"),
    ("aunt", "тётя", "fam_aunt"),
    ("uncle", "дядя", "fam_uncle"),
    ("cousin", "двоюродный брат / сестра", "fam_cousin"),
]

# В тесте «как по-английски» только полные слова: «мама» с вариантом mother
# среди неверных — ловушка, а не проверка.
U1_FAMILY_FORMAL = vocab([w for w in U1_FAMILY
                          if w[0] not in ("mum", "dad", "grandad", "granny")])

U1_COUNTRIES = [
    ("Poland", "Polish", "poland"),
    ("France", "French", "france"),
    ("the UK", "British", "uk"),
    ("Spain", "Spanish", "spain"),
    ("Italy", "Italian", "italy"),
    ("China", "Chinese", "china"),
    ("the USA", "American", "usa"),
]

CHAMPION = ("Ты выполнил все задания из основной части! А это дополнительное задание — "
            "для настоящих чемпионов! ")


LESSONS = {
    # Homework 1 (1) — словарный тренажёр, (2) — задания. Один урок.
    "u1_hw1": {
        **U1,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        "blocks": [
            hello("<h2>Добро пожаловать в домашнее задание! 👋</h2>"
                  "<p>В этом уроке тебя ждут упражнения на отработку новых слов! "
                  "Выполни все, если хочешь выучить тему на все 100!</p>"
                  + pic(u("fam_family"), "Family")),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U1_FAMILY
            ]}),

            ("match", {"title": "Соедини картинку и слово", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in U1_FAMILY_FORMAL
            ]}),

            ("quiz", quiz_ru_to_en(U1_FAMILY_FORMAL)),

            ("match", {"title": "Как сказать то же самое по-домашнему? Соедини пары", "pairs": [
                {"left": "mother", "right": "mum"},
                {"left": "father", "right": "dad"},
                {"left": "grandmother", "right": "granny"},
                {"left": "grandfather", "right": "grandad"},
            ]}),

            # перемычка: начало второй части
            ("text", {"html":
                "<h3>Hello! 👋</h3>"
                "<p>На занятии мы говорили о членах семьи, повторим? Приступим!</p>"
                "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"
                + pic(u("card_family"), "Unit 1 Family")}),

            # в выгрузке — фото семьи из учебника, у нас сгенерированная сцена
            ("hotspot", {
                "title": "Посмотри на семью Салли — Салли в середине, в джинсовом комбинезоне. "
                         "Где кто? Подпиши",
                "mode": "label",
                "image": u("scene_sally_family"),
                "points": [
                    {"x": 10.0, "y": 60.0, "text": "Sally's grandfather"},
                    {"x": 24.0, "y": 57.0, "text": "Sally's grandmother"},
                    {"x": 38.0, "y": 55.0, "text": "Sally's father"},
                    {"x": 51.0, "y": 52.0, "text": "Sally's mother"},
                    {"x": 78.0, "y": 68.0, "text": "Sally's sister"},
                    {"x": 90.0, "y": 60.0, "text": "Sally's brother"},
                ],
                "extras": ["Sally's cousin"],
            }),

            ("gaps", {
                "title": "Посмотри на семейное древо Марка. Заполни предложения одним словом",
                "mode": "type",
                "image": u("tree_mark"),
                "text": "Alan: Nick is my father. He's David's __father__ too.\n"
                        "Holly: Ruth is my __aunt__. Steven and I are Mark's __cousins__. "
                        "I am Helen and Rob's __daughter__.\n"
                        "Steven: Holly is my __sister__. I'm Helen's __son__.",
                "gaps_expected": 6,
            }),

            ("match", {
                "title": "Найди половинки слов и составь слова, обозначающие членов семьи",
                "pairs": [
                    {"left": "daught", "right": "er"},
                    {"left": "cous", "right": "in"},
                    {"left": "unc", "right": "le"},
                    {"left": "grand", "right": "ad"},
                    {"left": "au", "right": "nt"},
                    {"left": "gran", "right": "ny"},
                    {"left": "s", "right": "on"},
                ],
            }),

            ("speaking", {
                "title": "Моя семья 🎤",
                "html": "<p>Нажми на микрофон и перечисли членов твоей семьи.</p>"
                        "<p><i>Пример: This is my family: my mum, my dad, my granny…</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Anagram · 1.1 Family words (GG1)» — СОСТАВ МОЙ
            ("exact_input", {
                "title": CHAMPION + "Собери слово из букв ⭐",
                "items": [
                    {"prompt": anagram(en), "accept": [en, en.capitalize()],
                     "image": u(p), "audio_tts": en}
                    for en, ru, p in U1_FAMILY_FORMAL[:8]
                ],
            }),

            # Wordwall «Match up · gg1 1.1» — СОСТАВ МОЙ
            ("match", {"title": "Соедини пары ⭐", "pairs": [
                {"left": en, "right": ru, "left_audio_tts": en}
                for en, ru, p in U1_FAMILY
                if en in ("mum", "dad", "granny", "son", "daughter", "aunt", "uncle", "cousin")
            ]}),

            bye("<h3>У тебя отлично получилось! 🎉</h3><p>Увидимся на занятии!</p>"),
        ],
    },

    "u1_hw2": {
        **U1,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2>"
                  "<p>На занятии мы выучили новый глагол: <b>to be</b>. Давай потренируемся "
                  "и будем использовать его правильно? Приступим!</p>", "hello_book"),

            ("text", {"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"
                              + pic(u("card_to_be"), "to be")}),

            mcq("Посмотри на картинку и выбери правильный вариант ответа", [
                ("Look! We ___ at a party.", ["are", "am", "is"], "are", u("place_party")),
                ("Kate ___ 5 today.", ["is", "am", "are"], "is"),
                ("I ___ happy.", ["am", "is", "are"], "am"),
            ]),

            mcq("Посмотри на картинку и выбери правильный вариант ответа", [
                ("She ___ a teacher.", ["is", "am", "are"], "is", img("u4", "english_class")),
                ("He ___ a student.", ["is", "am", "are"], "is"),
                ("They ___ at school.", ["are", "am", "is"], "are"),
            ]),

            ("gaps", {
                "title": "Заполни пропуски словами am, is или are",
                "mode": "drag",
                "text": "Harry: Hi. I am Harry.\n"
                        "Jack: Hi, Harry. I __am__ Jack. You __are__ in class 2 with me. Welcome!\n"
                        "Harry: Thanks.\n"
                        "Jack: This is Tony. He __is__ my classmate. We are best friends too. "
                        "Mrs Lee and Mr Brown __are__ my favourite teachers.",
                "gaps_expected": 4,
            }),

            ("match", {"title": "Соедини полную и краткую формы", "pairs": [
                {"left": "we are", "right": "we're"},
                {"left": "Tom is", "right": "Tom's"},
                {"left": "I am", "right": "I'm"},
                {"left": "he is", "right": "he's"},
                {"left": "she is", "right": "she's"},
                {"left": "they are", "right": "they're"},
                {"left": "you are", "right": "you're"},
            ]}),

            ("speaking", {
                "title": "Мой друг 🎤",
                "html": "<p>Нажми на микрофон, представься и расскажи о своём друге или подруге. "
                        "Используй глагол to be (I'm, He's, She's) и местоимения my, your, his, her.</p>"
                        "<p><i>Пример: Hi! I'm Anna. I'm ten. This is my friend. His name's Tom. "
                        "He's eleven. His mum is Maria.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «gg1 1.2 to be» (обложка пустая) — СОСТАВ МОЙ
            mcq(CHAMPION + "Выбери правильный вариант ⭐", [
                ("I ___ eleven years old.", ["am", "is", "are"], "am"),
                ("My granny ___ seventy.", ["is", "am", "are"], "is"),
                ("We ___ at school.", ["are", "is", "am"], "are"),
                ("You ___ my best friend.", ["are", "is", "am"], "are"),
                ("His name ___ Lucas.", ["is", "are", "am"], "is"),
                ("My cousins ___ from Spain.", ["are", "is", "am"], "are"),
            ]),

            # Wordwall «gg1» (обложка пустая) — СОСТАВ МОЙ
            ("gaps", {
                "title": "Заполни пропуски ⭐",
                "mode": "drag",
                "text": "This is my sister. __Her__ name __is__ Lucy. She is eight.\n"
                        "My brother and I __are__ at home today.\n"
                        "Tom, is this __your__ bag?\n"
                        "This is Ben. __His__ mum is a teacher.\n"
                        "__My__ name is Anna and I __am__ ten.",
                "gaps_expected": 7,
            }),

            bye("<h3>У тебя отлично получилось! 🎉</h3><p>Увидимся на занятии! Bye!</p>",
                "well_done_medal"),
        ],
    },

    "u1_hw3": {
        **U1,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На занятии мы узнали много нового! Повторим?</p>",
                  "hello_highfive"),

            ("text", {"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"
                              + pic(u("card_to_be_negative"), "to be: отрицательная форма")
                              + pic(u("card_countries"), "Countries & Nationalities")}),

            order("My friends aren't at home.", ["My", "friends", "aren't", "at home."],
                  title="Расставь слова в предложении в правильном порядке"),
            order("You aren't right.", ["You", "aren't", "right."],
                  title="Расставь слова в предложении в правильном порядке"),
            order("I'm not a superhero.", ["I'm", "not", "a superhero."],
                  title="Расставь слова в предложении в правильном порядке"),
            order("Ben isn't my friend.", ["Ben", "isn't", "my", "friend."],
                  title="Расставь слова в предложении в правильном порядке"),
            order("She isn't my aunt.", ["She", "isn't", "my", "aunt."],
                  title="Расставь слова в предложении в правильном порядке"),
            order("They aren't my cousins.", ["They", "aren't", "my", "cousins."],
                  title="Расставь слова в предложении в правильном порядке"),

            true_false("Посмотри на картинку и скажи: верно или неверно", [
                ("He's a teacher.", False, u("tf_boy_backpack")),
                ("He isn't ready for school.", True),
                ("She isn't eleven.", True, u("tf_girl_ten")),
                ("She's at school.", False),
                ("They aren't happy.", True, u("tf_boys_bench")),
                ("They're at home.", False),
            ]),

            ("match", {"title": "Соедини название страны и национальность", "pairs": [
                {"left": c, "left_image": flag(f), "right": n, "right_audio_tts": n}
                for c, n, f in U1_COUNTRIES
            ]}),

            ("gaps", {
                "title": "Заполни пропуски словами my, your, his или her",
                "mode": "drag",
                "text": "Hanna: This is __my__ brother. __His__ name is Alex. "
                        "The present is for Granny. __Her__ name is Sophie.\n"
                        "Alex: This is __your__ present, Granny.",
                "gaps_expected": 4,
            }),

            ("speaking", {
                "title": "Откуда вы? 🎤",
                "html": "<p>Нажми на микрофон и расскажи, откуда ты и твоя семья.</p>"
                        "<p><i>Пример: I'm Polish. I'm not British. My granny is Spanish, "
                        "she isn't French. My cousins are Italian.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «gg1 1.3» (обложка пустая) — СОСТАВ МОЙ. Пары страна ↔
            # национальность уже были в блоке 10, здесь — флаг ↔ страна.
            ("match", {"title": CHAMPION + "Чей это флаг? Соедини флаг и страну ⭐", "pairs": [
                {"left_image": flag(f), "right": c, "right_audio_tts": c}
                for c, n, f in U1_COUNTRIES
            ]}),

            # Wordwall «1.3 be quiz» (обложка пустая) — СОСТАВ МОЙ
            mcq("Выбери правильный вариант ⭐", [
                ("She ___ British. She's Spanish.", ["isn't", "aren't", "am not"], "isn't"),
                ("I ___ twelve. I'm ten.", ["am not", "isn't", "aren't"], "am not"),
                ("We ___ from France.", ["aren't", "isn't", "am not"], "aren't"),
                ("My brother ___ at home.", ["isn't", "aren't", "am not"], "isn't"),
                ("They ___ my cousins.", ["aren't", "isn't", "am not"], "aren't"),
                ("It ___ my bag.", ["isn't", "aren't", "am not"], "isn't"),
            ]),

            bye("<h3>Отличная работа! 🎉</h3><p>Увидимся на занятии! Bye!</p>", "well_done_jump"),
        ],
    },

    "u1_hw4": {
        **U1,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На занятии мы учились приветствовать и представлять "
                  "друг друга по-английски. Повторим?</p>"),

            ("text", {"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"
                              + pic(u("card_introductions"), "Introductions")}),

            ("hotspot", {
                "title": "Заполни диалог: что говорит Джилл? Подпиши облачка",
                "mode": "label",
                "image": u("comic_jill_1"),
                "points": [
                    {"x": 54.0, "y": 27.0, "text": "Hi, Mum!"},
                    {"x": 66.0, "y": 53.0, "text": "This is Amy."},
                ],
                "extras": ["Sorry, Mum!", "It's OK, Mum!", "I'm Amy.", "Here you are, Amy."],
            }),

            ("hotspot", {
                "title": "Продолжение: что говорят мама Джилл и Эми? Подпиши облачка",
                "mode": "label",
                "image": u("comic_jill_2"),
                "points": [
                    {"x": 68.0, "y": 17.0, "text": "Hello, Amy."},
                    {"x": 65.0, "y": 69.0, "text": "Nice to meet you, Mrs Wilson."},
                ],
                "extras": ["Thank you, Amy.", "You're Amy.", "Nice to meet you, Jill."],
            }),

            ("gaps", {
                "title": "Заполни пропуски",
                "mode": "drag",
                "image": u("teens_skatepark"),
                "text": "Thomas: Hi, Stella, __this is__ Frankie. __He's__ my cousin.\n"
                        "Stella: __Hi__, Frankie. Nice __to meet you__.\n"
                        "Frankie: __Nice__ to meet you too, Stella.",
                "gaps_expected": 5,
            }),

            ("gaps", {
                "title": "Какие фразы лучше всего подойдут, чтобы получился диалог?",
                "mode": "drag",
                "text": "May: __Hi, Auntie Sue.__\n"
                        "Auntie Sue: Oh, hello, May!\n"
                        "May: And this is Nancy. __She's my best friend at school.__\n"
                        "Auntie Sue: Hello, Nancy. __Nice to meet you.__\n"
                        "Nancy: Hello, Mrs Smith. __Nice to meet you too.__",
                "gaps_expected": 4,
            }),

            ("speaking", {
                "title": "Знакомство 🎤",
                "html": "<p>Представь, что ты знакомишь своего друга с мамой. Нажми на микрофон "
                        "и разыграй знакомство.</p>"
                        "<p><i>Пример: Hi, Mum! This is my friend Tom. He's my classmate. "
                        "— Nice to meet you, Mrs Brown!</i></p>",
                "needs_review": True,
            }),

            bye("<h3>У тебя отлично получилось! 🎉</h3><p>Увидимся на занятии! Bye!</p>",
                "well_done_clap"),
        ],
    },

    "u1_hw5": {
        **U1,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        "blocks": [
            hello("<h2>Привет-привет! 👋</h2><p>Готов к новому домашнему заданию? Вперёд!</p>",
                  "hello_rocket"),

            # Тексты чтения учебника (Silvia, Nick, Bea) в выгрузку не попали —
            # блок «Найди пару» в ней пустой. Тексты составлены по ответам
            # следующих двух заданий; ТЕКСТ МОЙ, строка в доработать.
            ("text", {"html":
                "<p><b>Прочитай, что ребята рассказывают о себе 😃</b></p>"
                "<p><b>Silvia:</b> Hi. My name's Silvia. I'm 12 and I'm British. "
                "My brother is 9. My dad is Spanish. Ellie is my aunt — she's Spanish too. "
                "Bea is my friend. Sweep is a dog. He's our dog!</p>"
                "<p><b>Nick:</b> Hello! I'm Nick. I'm British. I'm at a party today — "
                "it's my cousin's birthday. My mum and dad are at the party too.</p>"
                "<p><b>Bea:</b> Hi! I'm Bea. My mother is Italian and my father is British. "
                "We aren't at school today. My granny and my grandad are in the park "
                "and my sister and my mother are in the garden.</p>"}),

            ("match", {"title": "Прочитай тексты ещё раз и соедини части предложений", "pairs": [
                {"left": "Hi. My name's", "right": "Silvia."},
                {"left": "I'm", "right": "12."},
                {"left": "My brother is", "right": "9."},
                {"left": "Ellie is", "right": "my aunt."},
                {"left": "Bea is", "right": "my friend."},
                {"left": "Sweep is", "right": "a dog."},
            ]}),

            ("gaps", {
                "title": "Заполни пропуски словами British, Italian или Spanish",
                "mode": "drag",
                "text": "1. Silvia is __British__.\n"
                        "2. Nick is __British__.\n"
                        "3. Silvia's dad is __Spanish__.\n"
                        "4. Aunt Ellie is __Spanish__.\n"
                        "5. Bea's mother is __Italian__.\n"
                        "6. Bea's father is __British__.",
                "gaps_expected": 6,
            }),

            ("exact_input", {
                "title": "Догадайся, какое слово пропущено, и впиши его целиком",
                "items": [
                    {"prompt": "I'm at a p… today.", "accept": ["party"],
                     "image": u("place_party"), "audio_tts": "I'm at a party today."},
                    {"prompt": "We aren't at s… today.", "accept": ["school"],
                     "image": u("place_school"), "audio_tts": "We aren't at school today."},
                    {"prompt": "My sister and my mother are in the g….", "accept": ["garden"],
                     "image": u("place_garden"),
                     "audio_tts": "My sister and my mother are in the garden."},
                    {"prompt": "My granny and my grandad are in the p….", "accept": ["park"],
                     "image": u("place_park"),
                     "audio_tts": "My granny and my grandad are in the park."},
                ],
            }),

            ("speaking", {
                "title": "Где сейчас твоя семья? 🎤",
                "html": "<p>Нажми на микрофон и расскажи, где сейчас члены твоей семьи и друзья.</p>"
                        "<p><i>Пример: My mum is at home. My dad is at school. My brother is in "
                        "the park. My friends are on holiday.</i></p>",
                "needs_review": True,
            }),

            bye("<h3>Отличная работа! 🎉</h3><p>Ещё увидимся!</p>", "well_done_smiley"),
        ],
    },

    "u1_hw6": {
        **U1,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На занятии мы сделали много интересных заданий! "
                  "Повторим?</p>", "hello_headphones"),

            listening("Послушай аудио: Роб рассказывает о своём друге Викторе и кузине Мел. "
                      "Потом выполни задания ниже."),

            true_false("Послушай аудио и скажи: верно или неверно", [
                ("Rob and Victor are best friends.", True, u("rob_victor_console")),
                ("They're at Rob's house.", False),
                ("Rob's mum and Victor's mum are best friends.", True),
                ("Rob's on holiday.", True, u("rob_mel_holiday")),
                ("Rob and Mel are in the UK.", False),
                ("Rob and Mel are cousins.", True),
            ]),

            ("gaps", {
                "title": "Послушай аудио и впиши информацию в пропуски",
                "mode": "type",
                "text": "Rob — Age: 10 — Nationality: __British__\n"
                        "Victor — Age: __10|ten__ — Nationality: __French__\n"
                        "Mel — Age: __12|twelve__ — Nationality: __American__",
                "gaps_expected": 5,
            }),

            ("task", {
                "title": "Я и мой лучший друг ✍",
                "needs_review": True,
                "html": "<p>Напиши короткий рассказ о себе и своём лучшем друге (40–60 слов). "
                        "Расскажи об имени, возрасте, откуда вы, и о семье.</p>"
                        "<p><i>Пример: Hi! My name's Anna. I'm ten years old. I'm from Poland. "
                        "I'm Polish. My best friend is Tom. He's eleven. He's British. We're "
                        "classmates. My mum's name is Maria and my dad's name is Peter. Tom's "
                        "sister is Lucy. We love our families!</i></p>",
            }),

            bye("<h3>Так держать! 🎉</h3><p>Увидимся на занятии! Bye!</p>", "well_done_star"),
        ],
    },

    "u1_hw7": {
        **U1,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На следующем занятии тебя ждёт очень интересный тест. "
                  "А сейчас давай повторим то, что мы прошли?</p>", "hello_laptop"),

            ("match", {"title": "Найди пару", "pairs": [
                {"left": "mum", "right": "dad"},
                {"left": "aunt", "right": "uncle"},
                {"left": "mother", "right": "father"},
                {"left": "brother", "right": "sister"},
                {"left": "son", "right": "daughter"},
                {"left": "granny", "right": "grandad"},
            ]}),

            ("exact_input", {
                "title": "Посмотри на картинку и впиши недостающее слово целиком",
                "items": [
                    {"prompt": "She is from P….", "accept": ["Poland", "poland"],
                     "image": u("she_poland"), "audio_tts": "She is from Poland."},
                    {"prompt": "He is in the g….", "accept": ["garden"],
                     "image": u("he_garden"), "audio_tts": "He is in the garden."},
                    {"prompt": "She is A….", "accept": ["American", "american"],
                     "image": u("she_american"), "audio_tts": "She is American."},
                    {"prompt": "They are at s….", "accept": ["school"],
                     "image": u("they_school"), "audio_tts": "They are at school."},
                    {"prompt": "Paris is in F….", "accept": ["France", "france"],
                     "image": u("place_paris"), "audio_tts": "Paris is in France."},
                    {"prompt": "She's at h….", "accept": ["home"],
                     "image": u("place_home"), "audio_tts": "She's at home."},
                ],
            }),

            ("gaps", {
                "title": "Впиши положительную (+) или отрицательную (−) форму глагола to be. "
                         "Используй полные формы, не сокращения",
                "mode": "type",
                "text": "My best friends __are__ Maya and Jane. (+)\n"
                        "Maya __is__ Italian. (+)\n"
                        "Jane and I __are not__ Italian. (−)\n"
                        "We __are__ from the UK. (+)\n"
                        "I __am not__ in the UK in this photo. (−)",
                "gaps_expected": 5,
            }),

            ("gaps", {
                "title": "Заполни пропуски словами из списка",
                "mode": "drag",
                "text": "A: Jack, __this__ __is__ my friend, Harry.\n"
                        "B: __Hi__, Harry. __Nice__ to meet you.\n"
                        "C: Hi, Jack. Nice to __meet__ you __too__.",
                "gaps_expected": 6,
            }),

            mcq("Выбери правильный вариант ответа", [
                ("This is Jack, and this is ___ cousin.", ["Jack", "Jack's", "her"], "Jack's"),
                ("This is Clara, and this is ___ best friend, Nadia.", ["his", "Nadia's", "her"], "her"),
                ("Hi, Mum! This is ___ best friend, Nina.", ["your", "his", "my"], "my"),
            ]),

            ("speaking", {
                "title": "Расскажи о себе 🎤",
                "html": "<p>Нажми на микрофон и расскажи о себе: имя, возраст, откуда ты, твоя семья.</p>"
                        "<p><i>Пример: Hi! I'm Anna. I'm ten years old. I'm from Poland. I'm Polish. "
                        "This is my family: my mum, my dad and my brother. My granny is Spanish. "
                        "We're in the park today.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Labelled diagram · GG1 1.1 Family tree» — СОСТАВ МОЙ,
            # по дереву Марка из Homework 1
            ("hotspot", {
                "title": CHAMPION + "Это семейное древо Марка. Кто они для Марка? ⭐",
                "mode": "label",
                "image": u("tree_mark"),
                "points": [
                    {"x": 45.0, "y": 70.0, "text": "grandfather"},
                    {"x": 67.0, "y": 70.0, "text": "grandmother"},
                    {"x": 33.0, "y": 32.0, "text": "father"},
                    {"x": 6.0, "y": 50.0, "text": "mother"},
                    {"x": 58.0, "y": 32.0, "text": "uncle"},
                    {"x": 68.0, "y": 48.0, "text": "aunt"},
                    {"x": 80.0, "y": 15.0, "text": "cousin"},
                ],
                "extras": ["brother", "son"],
            }),

            # Wordwall «Quiz · GG1 1.2 to be affirmative» — СОСТАВ МОЙ
            mcq("Выбери правильный вариант ⭐", [
                ("My dad ___ a doctor.", ["is", "am", "are"], "is"),
                ("I ___ from Poland.", ["am", "is", "are"], "am"),
                ("Tom and Ben ___ brothers.", ["are", "is", "am"], "are"),
                ("Her name ___ Sophie.", ["is", "are", "am"], "is"),
                ("We ___ in the garden.", ["are", "am", "is"], "are"),
            ]),

            # Wordwall «Quiz · GG1 1.3 to be negative» — СОСТАВ МОЙ
            mcq("И ещё раз: выбери правильный вариант ⭐", [
                ("I ___ eleven. I'm ten.", ["am not", "isn't", "aren't"], "am not"),
                ("My aunt ___ British. She's Italian.", ["isn't", "aren't", "am not"], "isn't"),
                ("We ___ at school today.", ["aren't", "isn't", "am not"], "aren't"),
                ("The dog ___ in the garden.", ["isn't", "aren't", "am not"], "isn't"),
                ("My cousins ___ from China.", ["aren't", "isn't", "am not"], "aren't"),
            ]),

            bye("<h3>Отличная работа! 🎉</h3><p>Удачи на тесте! Bye!</p>", "good_luck_clover"),
        ],
    },

    "u1_test": {
        **U1,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        "blocks": [
            ("exact_input", {
                "title": "Впиши слово целиком — недостающие буквы заменены чёрточками",
                "items": [
                    {"prompt": f"{gapped(en)} — {ru}", "accept": [en, en.capitalize()],
                     "image": u(p)}
                    for en, ru, p in U1_FAMILY_FORMAL
                    if en not in ("grandparents",)
                ],
            }),

            mcq("Прочитай диалог и выбери пропущенное слово", [
                ("A: Who's ___ best friend?", ["your", "you"], "your", u("t1_dog_best_friend")),
                ("B: My dog ___ my best friend!", ["is", "are"], "is"),
            ]),

            mcq("Прочитай диалог и выбери пропущенное слово", [
                ("A: Where ___ your friend?", ["is", "are"], "is", u("t1_friend_home")),
                ("B: My friend ___ at home.", ["is", "are"], "is"),
            ]),

            mcq("Прочитай диалог и выбери пропущенное слово", [
                ("A: Happy Birthday, Anna! Here's ___ present. — B: Thank you.",
                 ["your", "you"], "your", u("t1_birthday")),
            ]),

            mcq("Прочитай и выбери пропущенное слово", [
                ("Robin ___ in the garden.", ["isn't", "aren't", "am not"], "isn't",
                 u("t1_robin_library")),
                ("He ___ in the library.", ["is", "am", "are"], "is"),
            ]),

            mcq("Прочитай и выбери пропущенное слово", [
                ("My friends ___ from Poland.", ["aren't", "isn't"], "aren't",
                 u("t1_french_friends")),
                ("My friends aren't from ___.", ["Poland", "Polish"], "Poland"),
                ("They ___ French.", ["are", "is", "am"], "are"),
            ]),

            order("My classmates aren't at school.", title="Расставь слова в правильном порядке",
                  image=u("t1_classmates_park")),
            # в выгрузке «on holidays» — исправлено, см. доработать руками
            order("Our neighbours are on holiday.", title="Расставь слова в правильном порядке",
                  image=u("t1_neighbours_beach")),
            order("My dad is the best.", title="Расставь слова в правильном порядке",
                  image=u("t1_super_dad")),
            order("Mary's family is from London.", title="Расставь слова в правильном порядке",
                  image=u("place_london")),
            order("Tommy isn't in the park.", title="Расставь слова в правильном порядке",
                  image=u("place_park")),

            # в выгрузке рассказ — картинкой, у нас текстом
            ("text", {"html":
                "<h3>READING</h3><p>Прочитай рассказ Марко о его семье и выбери правильный ответ.</p>"
                "<p><i>Hello! I'm Marco. I'm from Italy. This is my family album. My mother's name "
                "is Sofia. She's a teacher. My father's name is Paolo. He's a doctor. My sister is "
                "Lucia. She's eight years old. My brother Leo is fourteen. My grandparents live in "
                "France. My grandfather is French. My grandmother is Italian. We are on holiday in "
                "Spain now. It's our favourite country!</i></p>"}),

            mcq("READING. Выбери правильный ответ", [
                ("Where is Marco from?", ["Spain", "Italy", "France"], "Italy"),
                ("Sofia is Marco's…", ["mother", "sister", "aunt"], "mother"),
                ("What's his father's job?", ["a teacher", "a doctor", "a father"], "a doctor"),
                ("How old is Marco's brother?", ["8", "14", "18"], "14"),
                ("His grandfather is…", ["French", "Italian", "British"], "French"),
                ("Where are they on holiday?", ["in Italy", "in France", "in Spain"], "in Spain"),
            ]),

            listening("LISTENING. Прослушай Эмму и реши: правда или неправда?", u("t1_emma_park")),

            ("truefalse", {"title": "LISTENING. Правда или неправда?", "statements": [
                {"text": "Emma is twelve years old.", "correct": False},
                {"text": "Emma is from the UK.", "correct": True},
                {"text": "Her brother's name is Max.", "correct": True},
                {"text": "Max is eleven years old.", "correct": False},
                {"text": "Her best friend is from Spain.", "correct": False},
                {"text": "They are at the park.", "correct": True},
            ]}),

            ("speaking", {
                "title": "SPEAKING TASK 🎤",
                "html": "<p>Ответь на вопросы. Запиши свой ответ, нажав на кнопку микрофона 🙌</p>"
                        "<ol><li>What's your name?</li><li>Where are you from?</li>"
                        "<li>How old are you?</li><li>What's your mum's name?</li>"
                        "<li>What's your dad's name?</li><li>What's your best friend's name?</li>"
                        "<li>How old is your best friend?</li></ol>",
                "needs_review": True,
            }),
        ],
    },
}
