#!/usr/bin/env python3
"""Go Getter 1 · Unit 7 · Animals — уроки (разбор: docs/GG1_разбор/u7.md).

Дикие животные, can / can't, Present Simple (отрицание и вопросы), покупка
билета, прилагательные (cute, dangerous…), домашние питомцы. Картинки
животных и прилагательных — листы Л7.1–Л7.4; карточки методиста, Hammy,
таблица, рояль, мячи и коллаж животных — кадры из выгрузки.
"""
from gg1_lib import *  # noqa: F401,F403

U = "u7"
U7 = {"unit": U, "unit_title": "Unit 7 · Animals", "unit_sort": 7}


def u(name):
    return img(U, name)


U7_ANIMALS = vocab([
    ("bird", "птица", "animal_bird"),
    ("butterfly", "бабочка", "animal_butterfly"),
    ("crocodile", "крокодил", "animal_crocodile"),
    ("elephant", "слон", "animal_elephant"),
    ("fish", "рыба", "animal_fish"),
    ("fly", "муха", "animal_fly"),
    ("frog", "лягушка", "animal_frog"),
    ("giraffe", "жираф", "animal_giraffe"),
    ("kangaroo", "кенгуру", "animal_kangaroo"),
    ("lion", "лев", "animal_lion"),
    ("monkey", "обезьяна", "animal_monkey"),
    ("snake", "змея", "animal_snake"),
    ("spider", "паук", "animal_spider"),
    ("tiger", "тигр", "animal_tiger"),
    ("whale", "кит", "animal_whale"),
])

U7_ADJ = vocab([
    ("cute", "милый", "adj_cute"),
    ("dangerous", "опасный", "adj_dangerous"),
    ("fast", "быстрый", "adj_fast"),
    ("slow", "медленный", "adj_slow"),
    ("strong", "сильный", "adj_strong"),
    ("ugly", "уродливый", "adj_ugly"),
])

CHAMPION = ("Ты выполнил все задания из основной части! А это дополнительное задание — "
            "для настоящих чемпионов! ")
REVIEW = "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"


def animal(en):
    return u(next(p for e, r, p in U7_ANIMALS if e == en))


def forms(*answers):
    """Варианты написания: краткая форма с прямым и типографским апострофом."""
    out = []
    for a in answers:
        out += [a, a.replace("'", "’")]
    return list(dict.fromkeys(out))


LESSONS = {
    # Homework 1 (1) — словарный тренажёр «дикие животные», (2) — задания. Один урок.
    "u7_hw1": {
        **U7,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Добро пожаловать в домашнее задание! В этом уроке тебя "
                  "ждут упражнения на отработку новых слов про диких животных. Выполни все, если "
                  "хочешь выучить тему на все 100! А в конце тебя ждут дополнительные задания — "
                  "выполнишь их, и будешь нереально крут!</p>"),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U7_ANIMALS
            ]}),

            ("quiz", quiz_ru_to_en(U7_ANIMALS)),

            ("match", {"title": "Найди пару", "pairs": [
                {"left": en, "right": ru, "left_audio_tts": en}
                for en, ru, p in U7_ANIMALS[:8]
            ]}),

            ("match", {"title": "И ещё: найди пару", "pairs": [
                {"left": en, "right": ru, "left_audio_tts": en}
                for en, ru, p in U7_ANIMALS[8:]
            ]}),

            # «Заполни пропуски» тренажёра: какие буквы пропускала платформа, не видно — свои
            ("exact_input", {"title": "Впиши слово целиком: некоторые буквы пропущены", "items": [
                {"prompt": gapped(en), "accept": [en, en.capitalize()], "image": u(p)}
                for en, ru, p in U7_ANIMALS
            ]}),

            ("text", {"html": "<h3>Добро пожаловать во вторую часть домашнего задания! 👋</h3>"
                              "<p>Выполни все задания, чтобы хорошенько запомнить новые слова! "
                              "Выполнив их, ты станешь МЕГА крутым учеником!</p>"
                              + REVIEW + pic(u("card_wild_animals"), "Wild Animals")}),

            ("match", {"title": "Итак, первое задание — соедини животных с их умениями. Выполняй "
                                "задание внимательно, не торопись ;)", "pairs": [
                {"left": "It can fly.", "right": "bird", "right_audio_tts": "bird"},
                {"left": "It can swim, but it can't walk.", "right": "whale", "right_audio_tts": "whale"},
                {"left": "It can climb trees.", "right": "monkey", "right_audio_tts": "monkey"},
                {"left": "It can jump, but it can't swim.", "right": "kangaroo",
                 "right_audio_tts": "kangaroo"},
                {"left": "It can jump and swim.", "right": "frog", "right_audio_tts": "frog"},
                {"left": "It can run fast, but it can't fly.", "right": "tiger", "right_audio_tts": "tiger"},
            ]}),

            ("task", {
                "title": "Загадка 🐾",
                "needs_review": True,
                "image": u("animals_collage"),
                "html": "<p>Загадай какое-нибудь животное и опиши его, не называя. На уроке загадай "
                        "его своим одноклассникам и учителю.</p>"
                        "<p><i>Смотри, это моя загадка: It's black and white. It likes bamboo. "
                        "It's big and cute. It can climb trees. What animal is it?</i></p>",
            }),

            # Wordwall «Match up · gg1 7.1» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини картинку и слово ⭐", "pairs": [
                {"left_image": animal(en), "right": en, "right_audio_tts": en}
                for en in ["crocodile", "elephant", "giraffe", "lion", "snake", "spider", "butterfly"]
            ]}),

            # Wordwall «Anagram · GG1 7.1» — СОСТАВ МОЙ
            ("exact_input", {"title": "Впиши слова: буквы перепутались ⭐", "items": [
                {"prompt": anagram(en), "accept": [en, en.capitalize()], "image": animal(en)}
                for en in ["monkey", "tiger", "whale", "frog", "kangaroo", "fly"]
            ]}),

            bye("<h3>Поздравляю! Ты завершил домашнее задание. Ты — МЕГА КРУТ! 🎉</h3>"
                "<p>Жду тебя на уроке!</p>", "congrats_popper"),
        ],
    },

    # Present Simple: отрицание
    "u7_hw2": {
        **U7,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня мы с тобой закрепим знания, полученные на уроке, и "
                  "ты без проблем сможешь использовать время Present Simple в отрицательных "
                  "предложениях. В конце тебя будет ждать дополнительное упражнение — для самых "
                  "смелых и самых сильных учеников 💪</p>", "hello_book"),

            ("text", {"html": REVIEW + pic(u("card_ps_negative"), "Present Simple — Negative")}),

            ("text", {"html": "<p>Посмотри на картинку и попробуй угадать: <b>Does Hammy go to "
                              "school?</b> Посмотри видео и проверь, угадал ли ты. Повторяй вопросы "
                              "и ответы за героями, чтобы хорошенько запомнить правила.</p>"
                              + pic(u("hammy"), "Hammy", 220)}),

            ("video", {"title": "Does Hammy go to school?", "url": "", "provider": "youtube"}),

            mcq("Теперь пришло время практики! Выбери правильный вариант. Смотри на значок перед "
                "предложением: ❌ — отрицательное предложение, ✅ — утвердительное", [
                ("✅ My puppy ___ TV.", ["likes", "like", "doesn't like", "don't like"], "likes"),
                ("❌ Cats ___ cupcakes.", ["don't eat", "eats", "eat", "doesn't eat"], "don't eat"),
                ("✅ My friend ___ in the garden.", ["plays", "play", "don't play", "doesn't play"],
                 "plays"),
                ("❌ My sister ___ her room.", ["doesn't tidy", "don't tidy", "tidies", "tidy"],
                 "doesn't tidy"),
                ("✅ Joe and Adam ___ after school.",
                 ["hang out", "don't hang out", "doesn't hang out", "hangs out"], "hang out"),
                ("❌ We ___ to school on Sundays.", ["don't go", "go", "goes", "doesn't go"], "don't go"),
            ]),

            ("gaps", {
                "title": "Впиши в пропуски слова, раскрыв скобки. Тебе нужна отрицательная форма. "
                         "Посмотри, как это сделано в первом предложении",
                "mode": "type",
                "text": "1. My pet doesn't like (not like) apples.\n"
                        "2. I __don't tidy|do not tidy|don’t tidy__ (not tidy) my room every day.\n"
                        "3. We __don't watch|do not watch|don’t watch__ (not watch) TV before dinner.\n"
                        "4. My little sister __doesn't go|does not go|doesn’t go__ (not go) to school.\n"
                        "5. You __don't like|do not like|don’t like__ (not like) pop music.\n"
                        "6. My cousin __doesn't speak|does not speak|doesn’t speak__ (not speak) French.",
                "gaps_expected": 5,
            }),

            ("task", {
                "title": "Исправь предложения по таблице ✏️",
                "needs_review": True,
                "image": u("table_routines"),
                "html": "<p>Внимательно посмотри на таблицу: в предложениях ниже ошибки! Перепиши "
                        "их так, чтобы они соответствовали таблице.</p>"
                        "<p><i>Например: Jen, Alex and Dad get up early. — в таблице совсем наоборот! "
                        "Правильно: Jen, Alex and Dad don't get up early.</i></p>"
                        "<ol><li>Dad gets up early.</li><li>Jen and Alex don't play computer games.</li>"
                        "<li>Mum and Dad play computer games.</li>"
                        "<li>Mum doesn't listen to classical music.</li>"
                        "<li>Jen listens to classical music.</li></ol>",
            }),

            ("task", {
                "title": "Задание со звёздочкой ⭐ (дополнительный балл)",
                "needs_review": True,
                "html": "<p>Напиши 3 предложения о себе и 3 предложения о своём члене семьи, друге "
                        "или даже учителе! Что вы обычно НЕ делаете в повседневной жизни?</p>"
                        "<p><i>Посмотри, это мои предложения: I don't get up at 6 o'clock. I don't "
                        "watch TV in the morning. I don't read a magazine before sleeping. My best "
                        "friend Anna doesn't get up at 10 o'clock. She doesn't play computer games "
                        "before school. She doesn't have lunch at 8 o'clock in the evening.</i></p>"
                        "<p>Обрати внимание на вспомогательный глагол, когда я рассказываю о своей "
                        "подруге ;)</p>",
            }),

            # Wordwall «Match up · GG1 unit 7.2» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини начало и конец предложения ⭐", "pairs": [
                {"left": "I", "right": "don't like snakes."},
                {"left": "My brother", "right": "doesn't eat fish."},
                {"left": "Elephants", "right": "don't fly."},
                {"left": "A kangaroo", "right": "doesn't swim."},
                {"left": "We", "right": "don't go to school on Sundays."},
            ]}),

            # Wordwall «Quiz · gg1 7.2» — СОСТАВ МОЙ
            mcq("Выбери правильный вариант ⭐", [
                ("Monkeys ___ live in the sea.", ["don't", "doesn't"], "don't", animal("monkey")),
                ("A lion ___ eat grass.", ["doesn't", "don't"], "doesn't", animal("lion")),
                ("Fish ___ walk.", ["don't", "doesn't"], "don't", animal("fish")),
                ("A snake ___ have legs.", ["doesn't", "don't"], "doesn't", animal("snake")),
                ("Giraffes ___ eat meat.", ["don't", "doesn't"], "don't", animal("giraffe")),
                ("My cat doesn't ___ milk.", ["like", "likes"], "like", u("animal_cat")),
            ]),

            bye("<h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3>"
                "<p>Увидимся на занятии!</p>", "well_done_star"),
        ],
    },

    # Present Simple: вопросы и краткие ответы
    "u7_hw3": {
        **U7,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня мы с тобой закрепим знания, полученные на уроке, и "
                  "ты без проблем сможешь задавать вопросы в Present Simple. В конце тебя будет ждать "
                  "дополнительное упражнение — для самых смелых и самых сильных учеников 💪</p>",
                  "hello_highfive"),

            ("text", {"html": REVIEW + pic(u("card_ps_questions"), "Present Simple — Questions")}),

            ("text", {"html": "<p>Ребята рассказывают, как они обычно проводят выходные. Попробуй "
                              "угадать: <b>What has Hammy got in his hands?</b> Посмотри видео и "
                              "проверь, угадал ли ты. Повторяй вопросы и ответы за героями, чтобы "
                              "хорошенько запомнить правила.</p>" + pic(u("hammy"), "Hammy", 200)}),

            ("video", {"title": "What has Hammy got in his hands?", "url": "", "provider": "youtube"}),

            mcq("Настало время практики! Внимательно прочитай предложения и выбери правильный "
                "вариант. Удачи!", [
                ("___ you know Mari?", ["Do", "Does"], "Do"),
                ("___ Tom live in a house with a garden?", ["Do", "Does"], "Does"),
                ("___ your friends speak English?", ["Do", "Does"], "Do"),
                ("___ your mum make nice cakes?", ["Do", "Does"], "Does"),
                ("___ I sing well?", ["Do", "Does"], "Do"),
                ("___ you and your sister like cats?", ["Do", "Does"], "Do"),
            ]),

            ("match", {"title": "Все вопросы и ответы растерялись… Помоги им найти друг друга! "
                                "Читай внимательно ;)", "pairs": [
                {"left": "Do you know Mari?", "right": "Yes, I do."},
                {"left": "Does Tom live in a house with a garden?", "right": "Yes, he does."},
                {"left": "Do your friends speak English?", "right": "No, they don't."},
                {"left": "Does your mum make nice cakes?", "right": "Yes, she does."},
                {"left": "Do I sing well?", "right": "No, you don't."},
                {"left": "Do you and your sister like cats?", "right": "Yes, we do."},
            ]}),

            order("Do you speak Chinese?",
                  title="Ты уже на финишной прямой! Расставь слова в правильном порядке так, чтобы "
                        "получился вопрос. Главное, не торопись ;)"),
            order("Do you like chocolate?", title="Расставь слова так, чтобы получился вопрос"),
            order("Do your friends play football on Saturdays?",
                  title="Расставь слова так, чтобы получился вопрос"),
            order("Do you tidy your room at the weekend?",
                  title="Расставь слова так, чтобы получился вопрос"),
            order("Does your dad go to the gym?", title="Расставь слова так, чтобы получился вопрос"),

            ("task", {
                "title": "Интервью с другом 🎙️",
                "needs_review": True,
                "html": "<p>Представь, что тебе нужно взять интервью у своего лучшего друга или "
                        "подруги. Какие вопросы ты бы придумал(а)? Напиши как минимум 3 вопроса "
                        "(но чем больше, тем лучше). Удачи, у тебя всё получится!</p>"
                        "<p><i>Посмотри, это мои вопросы: Do you sing well? Do you speak any foreign "
                        "languages? Does your best friend like playing with you?</i></p>",
            }),

            # Wordwall «Labelled diagram · gg1 7.3» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини вопросы про животных с ответами ⭐", "pairs": [
                {"left": "Do birds fly?", "right": "Yes, they do."},
                {"left": "Does a whale walk?", "right": "No, it doesn't."},
                {"left": "Does a monkey climb trees?", "right": "Yes, it does."},
                {"left": "Do snakes have legs?", "right": "No, they don't."},
            ]}),

            # Wordwall «Unjumble · gg1 7.3» — СОСТАВ МОЙ
            order("Does a frog jump?", title="Расставь слова в правильном порядке ⭐",
                  image=animal("frog")),
            order("Do lions sleep all day?", title="Расставь слова в правильном порядке ⭐",
                  image=animal("lion")),
            order("Does your cat like fish?", title="Расставь слова в правильном порядке ⭐",
                  image=u("animal_cat")),

            bye("<h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3>"
                "<p>Увидимся на занятии!</p>", "well_done_clap"),
        ],
    },

    # Покупка билета, в кафе
    "u7_hw4": {
        **U7,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        "blocks": [
            hello("<h2>Привет-привет! 👋</h2><p>Хочу похвалить тебя за твой труд! Ты молодец, что "
                  "решил сделать домашнюю работу. Вперёд :)</p>", "hello_rocket"),

            ("text", {"html": REVIEW + pic(u("card_buying_ticket"), "Buying a Ticket")}),

            mcq("Прочитай диалог и выбери правильный ответ", [
                ("A: Can I help you? B: ___ a ticket to the museum, please?",
                 ["Can I have", "Would you like"], "Can I have"),
                ("A: ___ you like a guide?", ["Would", "Do"], "Would"),
                ("B: No, ___.", ["thanks", "please"], "thanks"),
                ("A: That's £8.50, please. B: Here ___.", ["you are", "are you"], "you are"),
                ("A: ___ your tickets. B: Thank you.", ["Here are", "They're"], "Here are"),
            ]),

            ("sequence", {"title": "Поставь предложения в диалоге в правильном порядке",
                          "image": u("scene_cafe_counter"), "items": [
                {"text": "Attendant: Can I help you?"},
                {"text": "Customer: Yes. Can I have a sandwich, please?"},
                {"text": "Attendant: Yes, OK. Would you like cheese in it?"},
                {"text": "Customer: Yes, please."},
                {"text": "Attendant: That's £3.25, please."},
                {"text": "Customer: Here you are."},
                {"text": "Attendant: Thank you. And here's your sandwich."},
                {"text": "Customer: Thanks. Have a nice day!"},
            ]}),

            # в выгрузке лишние цифры-сноски «3», «9» и пропуск «T___» — исправлено
            ("gaps", {
                "title": "Заполни пропуски в диалоге. Можешь использовать слова из предыдущих упражнений",
                "mode": "type",
                "text": "A: Hello. Can __I__ help you?\n"
                        "B: Hi. Can I __have__ two tickets for the cinema, please?\n"
                        "A: Sure. Would you __like__ a bag of popcorn?\n"
                        "B: Yes, please. Good __idea__!\n"
                        "A: That's £15, __please__.\n"
                        "B: __Here__ you are.\n"
                        "A: Here __are__ your tickets and here's the popcorn. Enjoy the film!\n"
                        "B: __Thanks|Thank you__.",
                "gaps_expected": 8,
            }),

            ("speaking", {
                "title": "В кассе зоопарка 🎤",
                "image": u("scene_zoo_ticket_office"),
                "html": "<p>Представь, что ты в кассе зоопарка покупаешь билеты для своей семьи. "
                        "Нажми на микрофон и разыграй диалог.</p>"
                        "<p><i>Пример: Hello! Can I have three tickets to the zoo, please? — That's "
                        "eighteen pounds fifty. — Here you are. — Thank you. Here are your tickets!</i></p>",
                "needs_review": True,
            }),

            # в выгрузке прощание стоит перед записью голоса — у нас последним
            bye("<h3>Спасибо тебе большое за отличную работу! 🎉</h3><p>Увидимся на уроке!</p>",
                "well_done_medal"),
        ],
    },

    # Homework 5 (1) — тренажёр «прилагательные», (2) — задания про акул. Один урок.
    "u7_hw5": {
        **U7,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Время для домашнего задания! Сначала выучим новые слова — "
                  "какими бывают животные. Let's go!</p>", "hello_headphones"),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U7_ADJ
            ]}),

            ("quiz", quiz_ru_to_en(U7_ADJ)),

            ("match", {"title": "Соедини картинку и слово", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en} for en, ru, p in U7_ADJ
            ]}),

            ("text", {"html": "<h3>Вторая часть домашнего задания 👋</h3>" + REVIEW
                              + pic(u("card_adjectives"), "Adjectives")}),

            true_false("Посмотри на картинку и выбери, верно утверждение или нет", [
                ("It's fast.", True, u("animal_cat")),
                ("It's strong.", False, u("animal_fish")),
                ("It's dangerous.", True, u("animal_lion")),
                ("It's cute.", False, u("animal_spider")),
                ("It's ugly.", True, u("adj_ugly")),
                ("It's slow.", False, u("animal_tiger")),
            ]),

            ("quiz", {"title": "Какие слова описывают акул лучше всего? Отметь их", "questions": [{
                "q": "Sharks are… / Sharks have got…",
                "type": "multiple",
                "image": u("adj_dangerous"),
                "options": [{"text": t} for t in ["dangerous", "cute face", "fast", "strong",
                                                  "big ears", "lots of teeth", "long body"]],
                "correct": [0, 2, 3, 5, 6],
            }]}),

            # в выгрузке статья — разворот учебника с фото человека; у нас текстом
            ("text", {"html":
                "<p><b>Прочитай текст и выполни задания ниже.</b></p>"
                + pic(u("scene_shark"), "Sharks", 240)
                + "<h3>All about sharks</h3>"
                "<p><b>Are all sharks dangerous to people?</b><br><i>No, they aren't. Most sharks are "
                "not dangerous to us, but we are very dangerous to sharks! Why? Sharks don't often eat "
                "people, but in some countries people eat sharks.</i></p>"
                "<p><b>So, what do sharks usually eat?</b><br><i>They eat fish and other sea animals. "
                "They sometimes eat other sharks.</i></p>"
                "<p><b>Are they clever? What can they do?</b><br><i>Sharks are strong and they are fast "
                "swimmers. They can see and smell under water very well.</i></p>"
                "<p><b>Can they hear?</b><br><i>Good question. It's amazing. They haven't got ears like "
                "ours, but they can hear fish from hundreds of kilometres away!</i></p>"}),

            mcq("Прочитай текст и выбери правильные варианты ответов", [
                ("Sharks aren't ___ dangerous to people.", ["often", "sometimes"], "often"),
                ("People ___ a problem for sharks.", ["are", "aren't"], "are"),
                ("Sharks don't often eat ___.", ["other sharks", "sea animals"], "other sharks"),
                ("They ___ very good eyes.", ["have got", "haven't got"], "have got"),
                ("They ___ hear very well.", ["can", "can't"], "can"),
            ]),

            ("task", {
                "title": "Прочитай текст ещё раз и ответь на вопросы",
                "needs_review": True,
                "html": "<ol><li>What do sharks usually eat?</li><li>Do they often eat people?</li>"
                        "<li>Can they smell well?</li><li>What can they hear?</li></ol>",
            }),

            bye("<h3>Отличная работа! Спасибо тебе большое! 🎉</h3><p>Увидимся на занятии!</p>",
                "well_done_jump"),
        ],
    },

    # Домашние питомцы: аудио и письмо
    "u7_hw6": {
        **U7,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        "blocks": [
            hello("<h2>Привет! 👋</h2><p>Готов к домашней работе? Тогда вперёд!</p>", "hello_laptop"),

            listening("Послушай аудио: Эмма рассказывает о своих домашних питомцах."),

            # в выгрузке тест с пустыми вариантами ответа и без аудио — у нас ответ
            # проверяет учитель; строка в доработать
            ("task", {
                "title": "Какое домашнее животное есть у Эммы?",
                "needs_review": True,
                "html": "<p>Послушай аудио выше и напиши, какое домашнее животное есть у Эммы.</p>",
            }),

            ("task", {
                "title": "Послушай ещё раз и ответь на вопросы",
                "needs_review": True,
                "html": "<ol><li>Where are the pets?</li><li>Are they brothers or sisters?</li>"
                        "<li>What colour is Ted's favourite pet?</li><li>What do they need every day?</li>"
                        "<li>Where does their special food come from?</li></ol>",
            }),

            mcq("А теперь выбери правильный вариант ответа", [
                ("There are ___ pets.", ["two", "three"], "two"),
                ("The pets ___ easy to look after.", ["aren't", "are"], "aren't"),
                ("They ___ oranges.", ["don't like", "like"], "don't like"),
                ("Ted has got some ___.", ["rabbits", "hamsters"], "rabbits"),
            ]),

            # письмо в выгрузке — картинкой из учебника; у нас текстом
            ("text", {"html":
                "<p><b>Прочитай письмо и выбери верные ответы.</b></p>"
                + pic(u("kittens_basket"), "Kittens", 220)
                + "<p><i>Hi Sam,<br>I know you like cats. Well, our cat has got some kittens. Would you "
                "like one? They are cute. Three are black, two are black and white and one is grey. "
                "They haven't got names. They are very young!<br>Kittens are easy to look after. They "
                "don't go for walks! They sleep a lot and they don't eat much. They're very friendly "
                "too.<br>Can you ask your mum and dad? Let me know.<br>Ben</i></p>"}),

            # в выгрузке верным отмечено «There are three», а котят 3 + 2 + 1 = шесть — исправлено
            mcq("Прочитай письмо и выбери верные ответы", [
                ("Does Sam like cats?", ["Yes, he does.", "No, he doesn't."], "Yes, he does."),
                ("How many kittens are there?", ["There are six.", "There are three."], "There are six."),
                ("Have they got names?", ["No, they haven't.", "Yes, they have."], "No, they haven't."),
                ("Do they eat a lot?", ["No, they don't.", "Yes, they do."], "No, they don't."),
                ("Can Sam have a kitten?", ["We don't know.", "Yes, he can."], "We don't know."),
            ]),

            ("task", {
                "title": "Письмо другу ✉️",
                "needs_review": True,
                "html": "<p>Напиши короткое письмо другу про своих домашних животных или животных в "
                        "зоопарке (50–70 слов).</p>"
                        "<p><i>Пример: Hi Tom! How are you? I'm great! I want to tell you about my pets. "
                        "I've got a dog and a goldfish. My dog's name is Rex. He's big and friendly. He "
                        "likes running and playing in the park. My goldfish doesn't have a name. It's "
                        "small and orange. Do you have a pet? Bye! Anna</i></p>",
            }),

            bye("<h3>Супер-пупер! Хорошая работа. Спасибо тебе :) 🎉</h3><p>Увидимся на занятии!</p>",
                "well_done_smiley"),
        ],
    },

    # Present Simple: все формы — подготовка к тесту
    "u7_hw7": {
        **U7,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        "blocks": [
            hello("<h2>Привет! 👋</h2><p>Здорово, что ты решил сделать домашнюю работу.</p>",
                  "hello_wave"),

            mcq("Выбери правильную форму глагола", [
                ("A cat ___ milk.", ["likes", "liks", "like"], "likes"),
                ("Lions ___ in Africa.", ["live", "lives", "livs"], "live"),
                ("My dog ___ in the garden every day.", ["plays", "play", "plais"], "plays"),
                ("Elephants ___ plants.", ["eat", "eats", "eates"], "eat"),
                ("He ___ a pet rabbit.", ["has", "have", "haves"], "has"),
            ]),

            # в выгрузке — открытый вопрос; ответы однозначные, поэтому проверка автоматическая
            ("exact_input", {
                "title": "Перепиши предложения — сделай их отрицательными. Пример: I like milk. → "
                         "I don't like milk.",
                "items": [
                    {"prompt": "A snake likes milk.",
                     "accept": forms("A snake doesn't like milk.", "A snake doesn't like milk",
                                     "A snake does not like milk.", "A snake does not like milk")},
                    {"prompt": "My cat lives in the jungle.",
                     "accept": forms("My cat doesn't live in the jungle.", "My cat doesn't live in the jungle",
                                     "My cat does not live in the jungle.",
                                     "My cat does not live in the jungle")},
                    {"prompt": "Tigers eat grass.",
                     "accept": forms("Tigers don't eat grass.", "Tigers don't eat grass",
                                     "Tigers do not eat grass.", "Tigers do not eat grass")},
                    {"prompt": "I have a wild animal at home.",
                     "accept": forms("I don't have a wild animal at home.", "I don't have a wild animal at home",
                                     "I do not have a wild animal at home.",
                                     "I do not have a wild animal at home")},
                    {"prompt": "Dogs fly.",
                     "accept": forms("Dogs don't fly.", "Dogs don't fly", "Dogs do not fly.",
                                     "Dogs do not fly")},
                ],
            }),

            ("gaps", {
                "title": "Впиши пропущенные слова: do / does / don't / doesn't",
                "mode": "drag",
                "text": "1. A: __Do__ you have a pet? B: Yes, I __do__. I have a dog.\n"
                        "2. A: __Do__ cats like milk? B: Yes, they __do__.\n"
                        "3. A: __Does__ your dog like cats? B: No, it __doesn't__.\n"
                        "4. A: Where __do__ lions live? B: They live in Africa.\n"
                        "5. A: __Do__ snakes drink milk? B: No, they __don't__.",
                "gaps_expected": 9,
            }),

            ("speaking", {
                "title": "Ответь на вопросы 🎤",
                "html": "<ol><li>Do you have a pet?</li><li>What does your pet eat?</li>"
                        "<li>Do crocodiles live in your house?</li><li>Does your friend go to school?</li>"
                        "<li>Do your parents have a car?</li></ol>",
                "needs_review": True,
            }),

            # Wordwall «Wordsearch · gg1 7.1» (в задании «нажми на слово, затем на картинку») — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Найди название каждого животного: соедини слово и "
                                           "картинку ⭐", "pairs": [
                {"left": en, "right_image": animal(en), "left_audio_tts": en}
                for en in ["bird", "fish", "fly", "frog", "kangaroo", "monkey", "tiger", "whale"]
            ]}),

            # Wordwall «Quiz · gg1 7.2» — СОСТАВ МОЙ
            mcq("Выбери правильный вариант ⭐", [
                ("Crocodiles ___ live in the desert.", ["don't", "doesn't"], "don't", animal("crocodile")),
                ("An elephant ___ fly.", ["doesn't", "don't"], "doesn't", animal("elephant")),
                ("Butterflies ___ eat meat.", ["don't", "doesn't"], "don't", animal("butterfly")),
                ("A spider ___ have wings.", ["doesn't", "don't"], "doesn't", animal("spider")),
                ("My rabbit doesn't ___ fish.", ["eat", "eats"], "eat", u("animal_rabbit")),
            ]),

            # Wordwall «Quiz · gg1 7.3» — СОСТАВ МОЙ
            mcq("Выбери правильный вариант ⭐", [
                ("___ giraffes eat leaves? — Yes, they do.", ["Do", "Does"], "Do", animal("giraffe")),
                ("___ a kangaroo jump? — Yes, it does.", ["Does", "Do"], "Does", animal("kangaroo")),
                ("Does a whale live in the sea? — Yes, it ___.", ["does", "do"], "does", animal("whale")),
                ("Do frogs fly? — No, they ___.", ["don't", "doesn't"], "don't", animal("frog")),
                ("___ your cat like milk? — Yes, it does.", ["Does", "Do"], "Does", u("animal_cat")),
            ]),

            bye("<h3>Ты проделал отличную работу! Молодец 💕</h3><p>Уверена, ты справишься с тестом "
                "на все сто! Удачи!</p>", "good_luck_clover"),
        ],
    },

    "u7_test": {
        **U7,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        "blocks": [
            # какие буквы пропускала платформа, в выгрузке не видно — свои, слово пишем целиком
            ("exact_input", {"title": "Впиши слово целиком: некоторые буквы пропущены", "items": [
                {"prompt": gapped(en), "accept": [en, en.capitalize()], "image": animal(en)}
                for en in ["bird", "butterfly", "crocodile", "elephant", "fly", "giraffe", "monkey",
                           "snake", "spider", "whale"]
            ]}),

            mcq("Прочитай предложение и выбери пропущенное слово", [
                ("He ___ to school at the weekend.", ["doesn't go", "don't go"], "doesn't go",
                 u("school_walk")),
            ]),
            # в выгрузке «on Saturday? but» — опечатка, исправлено на запятую
            mcq("Прочитай диалог и выбери пропущенное слово", [
                ("A: I ___ do my homework at the weekend. And you?", ["don't", "doesn't"], "don't"),
                ("B: I ___ my homework on Saturday, but I don't do it on Sunday.", ["do", "does"], "do"),
                ("B: I do my homework on Saturday, but I ___ it on Sunday.", ["don't do", "doesn't do"],
                 "don't do"),
            ]),
            mcq("Прочитай предложение и выбери пропущенное слово", [
                ("My friend Alice and I ___ play computer games after school, we play football.",
                 ["don't", "doesn't"], "don't"),
            ]),
            mcq("Прочитай диалог и выбери пропущенное слово", [
                ("A: ___ she play the piano?", ["Does", "Do"], "Does", u("piano")),
                ("A: Does she ___ the piano?", ["play", "plays"], "play"),
                ("B: No, she ___.", ["doesn't", "don't"], "doesn't"),
                ("B: She ___ the guitar instead.", ["plays", "play"], "plays"),
            ]),
            mcq("Прочитай диалог и выбери пропущенное слово", [
                ("A: What ___ your brother do to relax?", ["does", "do"], "does"),
                ("A: What does your brother ___ to relax?", ["do", "does", "dos"], "do"),
                ("B: He ___ to music. And you?", ["listens", "listen", "listenes"], "listens"),
                ("A: I usually ___ swimming.", ["go", "gos", "goes"], "go"),
            ]),

            order("He doesn't play computer games on weekdays.",
                  title="Расставь слова в правильном порядке"),
            order("I don't have lunch at school.", title="Расставь слова в правильном порядке"),
            order("Do you play the guitar?", title="Расставь слова в правильном порядке"),
            order("Does she do any sport?", title="Расставь слова в правильном порядке",
                  image=u("sport_balls")),
            order("What does she have for dinner?", title="Расставь слова в правильном порядке"),

            # картинка письма в выгрузке повреждена — текст составлен заново по ответам, ТЕКСТ МОЙ
            ("text", {"html":
                "<h3>READING</h3><p>Прочитай письмо Мии подруге и выбери правильные ответы.</p>"
                + pic(u("animal_rabbit"), "Coco", 200)
                + "<p><i>Hi Olivia,<br>How are you? I'm fine. I have great news! We have a new pet. "
                "It's a small rabbit and her name is Coco. She is white and grey and she is very cute. "
                "Coco doesn't eat meat or fish. She eats leaves and vegetables. She drinks about one "
                "litre of water in a week. Every day my brother walks Coco in the garden — she loves "
                "it! I wanted a cat too, but we don't have one because my mum doesn't like cats.<br>"
                "Write soon!<br>Mia</i></p>"}),

            mcq("READING. Выбери правильный ответ", [
                ("What animal is Coco?", ["a hamster", "a rabbit", "a cat"], "a rabbit"),
                ("What colour is Coco?", ["brown and white", "grey and black", "white and grey"],
                 "white and grey"),
                ("What does Coco eat?", ["meat", "leaves and vegetables", "fish"], "leaves and vegetables"),
                ("How much water does Coco drink in a week?", ["1 litre", "2 litres", "5 litres"],
                 "1 litre"),
                ("Who walks Coco in the garden?", ["Mia", "her mum", "her brother"], "her brother"),
                ("Why doesn't Mia's family have a cat?",
                 ["Cats are dangerous.", "Mia doesn't like cats.", "Her mum doesn't like cats."],
                 "Her mum doesn't like cats."),
            ]),

            listening("LISTENING. Прослушай объявление в Лондонском зоопарке."),

            ("gaps", {
                "title": "LISTENING. Перетащи пропущенные числа и слова",
                "mode": "drag",
                "text": "1. Adult ticket: £__18.50__.\n"
                        "2. Child ticket: £__9.30__.\n"
                        "3. The zoo opens at __10__ am.\n"
                        "4. There are over __700__ animals in the zoo.\n"
                        "5. The café is next to the __giraffes__.\n"
                        "6. There is a big __elephant__ family in the zoo.\n"
                        "7. A guide costs £__4.20__.",
                "gaps_expected": 7,
            }),

            ("speaking", {
                "title": "SPEAKING TASK 🎤",
                "html": "<p>Представь, что ты собираешься брать интервью у своего друга. Составь "
                        "3 вопроса для интервью. Запиши свой ответ, нажав на кнопку микрофона 🙌</p>"
                        "<p><i>Пример: Do you listen to music? What sport do you like?</i></p>",
                "needs_review": True,
            }),
        ],
    },
}
