#!/usr/bin/env python3
"""Go Getter 1 · Unit 5 · I can do it — уроки (разбор: docs/GG1_разбор/u5.md).

Глаголы действия, коллокации make / play / ride, can / can't, вопросы с can и
краткие ответы, предложения Let's… / We can…, органы чувств и язык жестов,
кружок починки мишек. Картинки глаголов и вещей — листы Л5.1–Л5.6; карточки
методиста и иллюстрации учебника (пляж a–h, Оливер и Сара, Superdug, мишка-шифр)
— кадры из выгрузки (tools/gg1_pdf_frames.py). Фото людей из выгрузки не берём.
"""
from gg1_lib import *  # noqa: F401,F403

U = "u5"
U5 = {"unit": U, "unit_title": "Unit 5 · I can do it", "unit_sort": 5}


def u(name):
    return img(U, name)


# Словарь Homework 1 (1) — 14 слов + draw с карточки методиста.
U5_VERBS = vocab([
    ("act", "выступать на сцене", "verb_act"),
    ("climb", "лазать, карабкаться", "verb_climb"),
    ("cook", "готовить еду", "verb_cook"),
    ("dive", "нырять", "verb_dive"),
    ("fix", "чинить", "verb_fix"),
    ("fly", "летать", "verb_fly"),
    ("jump", "прыгать", "verb_jump"),
    ("read", "читать", "verb_read"),
    ("ride", "ездить верхом, кататься", "verb_ride"),
    ("sing", "петь", "verb_sing"),
    ("run", "бегать", "verb_run"),
    ("swim", "плавать", "verb_swim"),
    ("write", "писать", "verb_write"),
    ("skateboard", "кататься на скейтборде", "verb_skateboard"),
    ("draw", "рисовать", "verb_draw"),
])

CHAMPION = ("Ты выполнил все задания из основной части! А это дополнительное задание — "
            "для настоящих чемпионов! ")
REVIEW = "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"


def verb(en):
    return u(next(p for e, r, p in U5_VERBS if e == en))


def quiz_ru_en(words):
    """quiz_ru_to_en, но верный вариант идёт по кругу: на этом наборе общий
    помощник ставил его первым в шести вопросах из восьми."""
    out = quiz_ru_to_en(words)
    for i, q in enumerate(out["questions"]):
        opts = q["options"]
        ok = opts.pop(q["correct"][0])
        opts.insert(i % (len(opts) + 1), ok)
        q["correct"] = [opts.index(ok)]
    return out


def ask(*variants):
    """Ответ-предложение: с вопросительным знаком и без, как напишет ребёнок."""
    out = []
    for v in variants:
        out += [v, v.rstrip("?").rstrip()]
    return list(dict.fromkeys(out))


LESSONS = {
    # Homework 1 (1) — словарный тренажёр «глаголы действия», (2) — задания. Один урок.
    "u5_hw1": {
        **U5,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Давай скорее приступим к домашнему заданию! Сегодня "
                  "мы учим глаголы действия — слова, которые рассказывают, что мы умеем делать.</p>"),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U5_VERBS
            ]}),

            ("match", {"title": "Соедини картинку и слово", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in U5_VERBS[:8]
            ]}),

            ("match", {"title": "И ещё: соедини картинку и слово", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in U5_VERBS[8:]
            ]}),

            ("quiz", quiz_ru_en(U5_VERBS[:8])),

            ("exact_input", {"title": "Посмотри на картинку и напиши слово по-английски", "items": [
                {"prompt": ru, "accept": list(dict.fromkeys([en, en.capitalize()])), "image": u(p),
                 "audio_tts": en}
                for en, ru, p in U5_VERBS[8:]
            ]}),

            ("text", {"html": "<h3>Добро пожаловать во вторую часть домашнего задания! 👋</h3>"
                              + REVIEW + pic(u("card_action_verbs"), "Action verbs")}),

            # в выгрузке «Найди пару a–h» под картинкой учебника — у нас подписи прямо на ней
            ("hotspot", {
                "title": "Посмотри на картинку. Подпиши, кто что делает (буквы a–h)",
                "mode": "label",
                "image": u("beach_actions"),
                "points": [
                    {"x": 73.0, "y": 6.0, "text": "fly"},
                    {"x": 30.0, "y": 32.5, "text": "ride"},
                    {"x": 58.0, "y": 44.5, "text": "dive"},
                    {"x": 73.0, "y": 30.0, "text": "swim"},
                    {"x": 7.0, "y": 67.0, "text": "draw"},
                    {"x": 41.5, "y": 60.0, "text": "jump"},
                    {"x": 43.0, "y": 78.0, "text": "run"},
                    {"x": 72.0, "y": 75.0, "text": "skateboard"},
                ],
                "extras": [],
            }),

            # в выгрузке буквы — на фото людей (дайвер, актёр, певец, повар); у нас буквы текстом
            ("exact_input", {"title": "Убери две лишние буквы, чтобы найти глаголы действия. "
                                      "Запиши слова, которые нашёл. Пример: D I R V S E → dive",
                             "items": [
                {"prompt": "A E C T M", "accept": ["act", "Act"]},
                {"prompt": "I S I R N G", "accept": ["sing", "Sing"]},
                {"prompt": "C O R O A K", "accept": ["cook", "Cook"]},
                {"prompt": "W O R I T D E", "accept": ["write", "Write"]},
            ]}),

            ("gaps", {
                "title": "Посмотри на картинку и заполни пропуски",
                "mode": "drag",
                "image": u("verbs_objects"),
                "text": "1. read a newspaper (пример)\n"
                        "2. __fix__ a wardrobe with a screwdriver\n"
                        "3. __write__ with a pen\n"
                        "4. __run__ in new trainers\n"
                        "5. __swim__ with goggles",
                "gaps_expected": 4,
            }),

            ("speaking", {
                "title": "Мои любимые действия 🎤",
                "html": "<p>Нажми на микрофон и назови несколько действий, которые ты больше всего "
                        "любишь.</p><p><i>Пример: run, swim, fix.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «gg1-unit-51» (обложка пустая) — СОСТАВ МОЙ
            mcq(CHAMPION + "Выбери подходящее слово ⭐", [
                ("A kangaroo can ___.", ["jump", "fly", "write"], "jump", verb("jump")),
                ("A bird can ___.", ["fly", "cook", "read"], "fly", verb("fly")),
                ("A dolphin can ___.", ["swim", "climb", "sing"], "swim", verb("swim")),
                ("A monkey can ___ a tree.", ["climb", "dive", "act"], "climb", verb("climb")),
                ("A cheetah can ___ fast.", ["run", "write", "fix"], "run", verb("run")),
                ("I can ___ a book.", ["read", "ride", "jump"], "read", verb("read")),
            ]),

            # Wordwall «gg1-51-verbs» (обложки нет) — СОСТАВ МОЙ
            ("exact_input", {"title": "Впиши слово ⭐", "items": [
                {"prompt": gapped(en), "accept": [en, en.capitalize()], "image": verb(en),
                 "audio_tts": en}
                for en in ["cook", "sing", "dive", "fix", "write", "skateboard"]
            ]}),

            bye("<h3>Ты большой молодец! 🎉</h3><p>Увидимся на занятии!</p>", "well_done_star"),
        ],
    },

    "u5_hw2": {
        **U5,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>На уроке мы с тобой познакомились с новым глаголом "
                  "<b>CAN</b>. Сегодня будем выполнять разные задания, чтобы попрактиковаться "
                  "в этой теме.</p>", "hello_highfive"),

            ("text", {"html": REVIEW + pic(u("card_can"), "can / can't")}),

            # в выгрузке видео было загружено в редактор, но в файл не попало
            ("video", {"title": "Посмотри видео", "url": "", "provider": "youtube"}),

            # клипарт учебника: мультяшные дети, не фото
            ("gaps", {
                "title": "Посмотри на картинку и подумай, что ребята умеют и не умеют делать. "
                         "Впиши в пропуски can или can't",
                "mode": "drag",
                "image": u("oliver_sarah"),
                "text": "1. Sarah __can't__ dance.\n"
                        "2. Oliver __can__ play video games.\n"
                        "3. Oliver __can't__ play basketball.\n"
                        "4. Oliver __can__ climb.\n"
                        "5. Sarah __can't__ paint.\n"
                        "6. Sarah __can__ swim.\n"
                        "7. Sarah __can__ play tennis.\n"
                        "8. Sarah __can't__ ride a bike.\n"
                        "9. Sarah __can__ write.\n"
                        "10. Oliver __can't__ sing.",
                "gaps_expected": 10,
            }),

            ("gaps", {
                "title": "Вспомним животных и подумаем, что мы умеем делать как они. Заполни пропуски",
                "mode": "drag",
                "text": "1. You can't __jump__ like a monkey.\n"
                        "2. She can't __fly__ like a butterfly.\n"
                        "3. My dad can't __run__ like a cheetah.\n"
                        "4. My mom can __stomp__ like an elephant.\n"
                        "5. My sister can __swim__ like a fish.",
                "gaps_expected": 5,
            }),

            # в выгрузке опечатки «flya plane» и «eat carrot» — исправлено
            ("gaps", {
                "title": "А теперь подумаем, что животные умеют и не умеют делать. "
                         "Заполни пропуски словами can или can't",
                "mode": "drag",
                "text": "1. A monkey __can't__ fly, but it __can__ climb a tree.\n"
                        "2. A bird __can__ fly, but it __can't__ play volleyball.\n"
                        "3. An elephant __can__ run, but it __can't__ sing a song.\n"
                        "4. A kangaroo __can__ jump, but it __can't__ play the guitar.\n"
                        "5. A frog __can't__ speak English, but it __can__ jump.\n"
                        "6. A mouse __can__ run fast, but it __can't__ ride a bike.\n"
                        "7. A spider __can't__ fly a plane, but it __can__ make a web.\n"
                        "8. A rabbit __can't__ write an e-mail, but it __can__ eat carrots.\n"
                        "9. A bee __can't__ swim, but it __can__ make honey.",
                "gaps_expected": 18,
            }),

            ("task", {
                "title": "Что я умею 📝",
                "needs_review": True,
                "html": "<p>Напиши несколько предложений о том, что ты уже умеешь делать.</p>"
                        "<p><i>Пример: I can swim. I can ride a bike. I can't play the piano.</i></p>",
            }),

            # Wordwall «gg1-52» TRUE / FALSE (обложка пустая) — СОСТАВ МОЙ, по картинке Оливера и Сары
            true_false(CHAMPION + "Посмотри на картинку с Оливером и Сарой. Верно или неверно? ⭐", [
                ("Oliver can play the drums.", True, u("oliver_sarah")),
                ("Oliver can skateboard.", False),
                ("Oliver can rollerblade.", True),
                ("Sarah can sing.", True),
                ("Sarah can ride a bike.", False),
                ("Oliver can play video games.", True),
            ]),

            # Wordwall «gg1-52 make play ride» (обложка пустая) — СОСТАВ МОЙ
            ("sort", {"title": "Расставь занятия к подходящим глаголам ⭐", "groups": [
                {"name": "make", "items": [{"text": t} for t in ["a poster", "cupcakes", "a cake"]]},
                {"name": "play", "items": [{"text": t} for t in
                                           ["football", "computer games", "the piano", "tennis"]]},
                {"name": "ride", "items": [{"text": t} for t in ["a bike", "a horse"]]},
            ]}),

            bye("<h3>Отличная работа! 🎉</h3><p>See you soon!</p>", "well_done_jump"),
        ],
    },

    "u5_hw3": {
        **U5,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Здорово, что ты решил сделать домашнюю работу. "
                  "Ты большой молодец!</p>", "hello_book"),

            ("text", {"html": REVIEW + pic(u("card_can_questions"), "Can questions & short answers")}),

            # в выгрузке открытый вопрос; ответ однозначный — проверяем автоматически
            ("exact_input", {"title": "Прочитай предложения и напиши к ним вопросы. "
                                      "Пример: They can swim. → Can they swim?", "items": [
                {"prompt": "I can draw.", "accept": ask("Can you draw?")},
                {"prompt": "Tom can run fast.", "accept": ask("Can Tom run fast?")},
                {"prompt": "May can sing well.", "accept": ask("Can May sing well?")},
                {"prompt": "We can help.", "accept": ask("Can we help?", "Can you help?")},
                {"prompt": "The cat can climb.", "accept": ask("Can the cat climb?")},
            ]}),

            # комикс учебника Superdug — рисованные персонажи
            ("task", {
                "title": "Посмотри на картинку и ответь на вопросы",
                "needs_review": True,
                "image": u("superdug_beach"),
                "html": "<p><i>Пример: Can Kit and Dug see the boat? — Yes, they can.</i></p>"
                        "<ol><li>Can the boy and girl swim?</li><li>Can their mum swim?</li>"
                        "<li>Can Dug swim?</li><li>Can the small dog help?</li>"
                        "<li>Can Dug help?</li></ol>",
            }),

            ("task", {
                "title": "Напиши вопросы из слов ниже и ответь на них",
                "needs_review": True,
                "html": "<p><i>Пример: you / fix a bike? → Can you fix a bike? Yes, I can.</i></p>"
                        "<ol><li>you / play volleyball?</li><li>your mum / speak English?</li>"
                        "<li>your classmates / speak Spanish?</li><li>you / ride a horse?</li>"
                        "<li>your best friend / play the piano?</li></ol>",
            }),

            ("gaps", {
                "title": "Посмотри на картинки и заполни пропуски нужными словами",
                "mode": "drag",
                "image": u("fruits_dance"),
                "text": "1. A: Can you __see__ those red apples?\n"
                        "B: Yes, I __can__.\n"
                        "A: Help me, please? I'm too short.\n"
                        "B: No problem.\n"
                        "2. A: __Can__ they __dance__?\n"
                        "B: Yes, they can.\n"
                        "A: Can the girl play __the piano__ too?\n"
                        "B: No, she __can't__.",
                "gaps_expected": 6,
            }),

            ("speaking", {
                "title": "Спроси друга 🎤",
                "html": "<p>Задай 3 вопроса другу про его умения и ответь на них. Нажми на микрофон.</p>"
                        "<p><i>Пример: Can you swim? Yes, I can. Can you sing? No, I can't. Can you ride "
                        "a horse? No, I can't, but my sister can.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Find the match · GG1 5.3» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Выбери подходящий ответ ⭐", "pairs": [
                {"left": "Can you swim?", "right": "Yes, I can."},
                {"left": "Can he fly?", "right": "No, he can't."},
                {"left": "Can they cook?", "right": "Yes, they can."},
                {"left": "Can she sing?", "right": "No, she can't."},
                {"left": "Can it jump?", "right": "Yes, it can."},
                {"left": "Can we play football here?", "right": "No, we can't."},
            ]}),

            # Wordwall «Unjumble · GG1 Unit 5.3» — СОСТАВ МОЙ
            order("Can your sister ride a horse?", title="Расставь слова в правильном порядке ⭐"),
            order("What can your dog do?", title="Расставь слова в правильном порядке ⭐"),
            order("Yes, she can.", title="Расставь слова в правильном порядке ⭐"),

            bye("<h3>Ты проделал отличную работу! 🎉</h3><p>Здорово! Молодец!</p>", "well_done_clap"),
        ],
    },

    "u5_hw4": {
        **U5,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Привет-привет! Самое время приступить к домашней работе!</p>",
                  "hello_rocket"),

            ("text", {"html": REVIEW + pic(u("card_suggestions"), "Making suggestions")}),

            # в выгрузке «Let's see — our bikes»: исправлено на ride
            ("match", {"title": "Соедини части предложений", "pairs": [
                {"left": "Let's play", "right": "football after school."},
                {"left": "We can watch", "right": "my new DVD."},
                {"left": "Let's go", "right": "to the park."},
                {"left": "We can make", "right": "chocolate cupcakes."},
                {"left": "Let's ride", "right": "our bikes."},
            ]}),

            # в выгрузке пропуск — окончание слова (t…hat); у нас слово целиком
            ("gaps", {
                "title": "Заверши предложения нужными словами",
                "mode": "drag",
                "text": "1. Let's do __that__! 😊\n"
                        "2. It's not a __good__ idea. ☹️\n"
                        "3. Great __idea__! 😊\n"
                        "4. I'm not __sure__. 😐",
                "gaps_expected": 4,
            }),

            ("sequence", {"title": "Расположи предложения в нужном порядке, чтобы получился диалог",
                          "items": [
                {"text": "Hi! Let's play in the garden."},
                {"text": "No, not the garden again. We can go to the park."},
                {"text": "Yes, the park's a great idea. We can play football."},
                {"text": "I'm not sure about football."},
                {"text": "Why not?"},
                {"text": "We haven't got a ball."},
            ]}),

            ("task", {
                "title": "Напиши небольшие диалоги по картинкам",
                "needs_review": True,
                "image": u("suggestion_scenes"),
                "html": "<p>A предлагает (We can… / Let's…), B отвечает — смайлик подсказывает как: "
                        "😊 соглашается, 😐 сомневается, ☹️ отказывается.</p>"
                        "<ol><li>A: play a game / B: 😊<br><i>Пример: A: We can play a game! "
                        "B: Great idea!</i></li>"
                        "<li>A: watch that / B: 😐</li>"
                        "<li>A: go there / B: ☹️</li></ol>",
            }),

            bye("<h3>Отличная работа! 🎉</h3><p>Увидимся на занятии!</p>", "well_done_smiley"),
        ],
    },

    "u5_hw5": {
        **U5,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Давай приступать к домашней работе!</p>", "hello_wave"),

            # в выгрузке пропуск — буквы внутри слова (e…s); у нас слово целиком
            ("gaps", {
                "title": "Посмотри на картинки и заверши предложения",
                "mode": "type",
                "image": u("senses_icons"),
                "text": "1. You can see people with your __eyes__.\n"
                        "2. You can hear music with your __ears__.\n"
                        "3. You can smell flowers with your __nose__.",
                "gaps_expected": 3,
            }),

            # в выгрузке фото двух женщин — у нас рисованная сцена (Л5.6)
            ("gaps", {
                "title": "Прочитай текст и заполни пропуски нужными словами",
                "mode": "drag",
                "image": u("sign_language_friends"),
                "text": "Look at these women. They can't __hear__, but they can make words with their "
                        "__hands__. It's a special sign language. They can use it to speak to their "
                        "__friends__ and family.",
                "gaps_expected": 3,
            }),

            # в выгрузке текст — картинкой с фото девочки; у нас текстом и рисованная сцена
            ("text", {"html":
                "<p><b>Прочитай текст.</b></p>"
                + pic(u("jasmine_sweep"), "Jasmine and Sweep", 240)
                + "<p><i>Twelve-year-old Jasmine and her best friend are always together. Her best "
                "friend isn't a girl or a boy. He's a very special dog, called Sweep. Jasmine is an "
                "ordinary girl but she's got a problem – she can't hear. Think about it. She can't hear "
                "people, she can't hear music or the TV. She can't even hear cars in the street. It is "
                "sometimes very dangerous for her. But Jasmine is OK, because she's got Sweep, and "
                "Sweep is her ears! Sweep is a special 'hearing dog'. He can help Jasmine a lot. These "
                "days Jasmine can meet all her friends and hang out with them after school. Her parents "
                "can relax because Sweep is with her and she's safe.</i></p>"}),

            mcq("Выбери лучшее название для текста", [
                ("What is the best title for the text?",
                 ["A dog helps a girl called Jasmine.", "A girl called Jasmine helps her pet dog.",
                  "A dog called Sweep has got a problem."], "A dog helps a girl called Jasmine."),
            ]),

            mcq("Выбери правильный вариант", [
                ("Sweep is ___.", ["a dog", "a boy"], "a dog"),
                ("___ can't hear.", ["Jasmine", "Sweep"], "Jasmine"),
                ("Jasmine has got ___.", ["lots of friends", "one friend"], "lots of friends"),
                ("Jasmine ___ visit people.", ["can", "can't"], "can"),
                ("Jasmine's mum and dad ___ always with her.", ["aren't", "are"], "aren't"),
            ]),

            ("match", {"title": "Соедини, чтобы получились предложения", "pairs": [
                {"left": "Jasmine has", "right": "got a problem."},
                {"left": "Sweep is Jasmine's", "right": "ears."},
                {"left": "Sweep can", "right": "help Jasmine."},
                {"left": "Jasmine's best friend", "right": "is a dog."},
                {"left": "Jasmine's parents", "right": "are happy."},
                {"left": "Jasmine is safe", "right": "with Sweep."},
            ]}),

            ("speaking", {
                "title": "Какие языки ты знаешь? 🎤",
                "html": "<p>Нажми на микрофон и расскажи, какие языки ты знаешь и какие хочешь "
                        "выучить.</p><p><i>Пример: I can speak Polish and English. I can't speak "
                        "Spanish, but I want to learn it. I think sign language is interesting.</i></p>",
                "needs_review": True,
            }),

            bye("<h3>Хорошая работа! 🎉</h3><p>Увидимся на следующем уроке!</p>", "well_done_medal"),
        ],
    },

    "u5_hw6": {
        **U5,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Самое время выполнять домашнюю работу!</p>", "hello_headphones"),

            ("exact_input", {"title": "Что это? Поставь буквы в правильном порядке", "items": [
                {"prompt": "Подставь буквы по номерам: 4 1 9 2 5 / 8 7 3 6",
                 "accept": ["teddy bear", "Teddy bear", "Teddy Bear", "teddy-bear", "teddybear"],
                 "image": u("teddy_code"), "audio_tts": "teddy bear"},
            ]}),

            # аудио про кружок починки мишек в выгрузку не попало; фото швеи не берём
            listening("Послушай рассказ о кружке и выполни задания ниже."),

            mcq("Послушай и выбери правильный вариант ответа", [
                ("At this club you can ___.", ["fix an old teddy bear", "make a new teddy bear"],
                 "fix an old teddy bear"),
            ]),

            # в выгрузке варианты пустые, отмечен третий; по рассказу у мишки новые голубые глаза
            ("quiz", {"title": "Послушай и выбери правильного мишку", "questions": [{
                "q": "Which teddy bear is it?",
                "type": "single",
                "options": [{"image": u("teddy_black_eyes")}, {"image": u("teddy_torn")},
                            {"image": u("teddy_blue_eyes")}],
                "correct": [2],
            }]}),

            mcq("Выбери правильный вариант ответа", [
                ("What is the girl's name? Her name is ___.", ["Sarah", "Erin"], "Sarah"),
                ("Is the teddy bear Tommy's or his sister's? It's ___.", ["his sister's", "Tommy's"],
                 "his sister's"),
                ("Can Sarah fix it?", ["Yes, she can.", "No, she can't."], "Yes, she can."),
                ("What colour are the new eyes?", ["They're blue.", "They're black."], "They're blue."),
            ]),

            ("task", {
                "title": "Объявление о школьном кружке 📝",
                "needs_review": True,
                "html": "<p>Напиши короткое объявление о школьном кружке (40–60 слов). Расскажи, чем "
                        "там занимаются, когда встречаются и кто может прийти.</p>"
                        "<p><i>Пример: Come to the Football Club! You can play football and have fun "
                        "with friends. We meet on Mondays and Wednesdays at 4 o'clock. You can be a boy "
                        "or a girl, but you must be 8–12 years old. We can run, jump and play together. "
                        "See you there!</i></p>",
            }),

            bye("<h3>Огромное спасибо тебе за работу! 🎉</h3><p>Увидимся на занятии!</p>",
                "congrats_popper"),
        ],
    },

    "u5_hw7": {
        **U5,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Рада тебя видеть на домашнем задании! Сегодня ты проверишь, "
                  "как хорошо ты запомнил материал Unit 5. Готов? Поехали! 🚀</p>", "hello_laptop"),

            # в выгрузке фото (прыгун, скалолазка, руки) — у нас картинки глаголов
            ("exact_input", {"title": "Что они умеют делать? Напиши глаголы действия", "items": [
                {"prompt": "Какое это действие?", "accept": [en, en.capitalize()], "image": verb(en)}
                for en in ["fly", "jump", "write", "climb", "cook", "skateboard"]
            ]}),

            mcq("Выбери правильное слово", [
                ("___ a picture", ["draw", "read"], "draw", verb("draw")),
                ("___ the guitar", ["play", "ride"], "play", u("obj_guitar")),
                ("___ a cupcake", ["make", "play"], "make", u("coll_make_cupcakes")),
                ("___ a book", ["read", "sing"], "read", verb("read")),
                ("___ a bike", ["ride", "dive"], "ride", u("coll_ride_bike")),
                ("___ computer games", ["play", "act"], "play"),
            ]),

            # в выгрузке «Sam and Joe can swim fast» — в таблице swim без fast, исправлено
            ("gaps", {
                "title": "Посмотри на таблицу. Дополни предложения словами can, can't, and или but",
                "mode": "drag",
                "image": u("table_can"),
                "text": "Anna can swim and she can run fast.\n"
                        "Tom __can__ run fast __and__ he can fix a bike.\n"
                        "Sam and Joe can swim __but__ they __can't__ fix a bike.\n"
                        "Tom and Anna __can__ run fast.",
                "gaps_expected": 5,
            }),

            ("speaking", {
                "title": "Что я умею и не умею 🎤",
                "html": "<p>Нажми на микрофон и расскажи, что ты умеешь и что не умеешь делать. "
                        "Используй can и can't.</p><p><i>Пример: I can swim and ride a bike, but I can't "
                        "fix a bike.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Match up · GG1 unit 5.1» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини слово и перевод ⭐", "pairs": [
                {"left": en, "right": ru, "left_audio_tts": en}
                for en, ru, p in U5_VERBS if en in ("act", "climb", "dive", "fix", "ride", "sing",
                                                    "write", "skateboard")
            ]}),

            # Wordwall «Complete the sentence · GG1 Language test 5.2 / 5.5 / 5.6» — СОСТАВ МОЙ
            ("gaps", {
                "title": "Заполни пропуски словами can или can't ⭐",
                "mode": "drag",
                "text": "1. Fish __can__ swim, but they __can't__ walk.\n"
                        "2. I __can't__ fly, but I __can__ run fast.\n"
                        "3. A: __Can__ your brother ride a horse? B: No, he __can't__.",
                "gaps_expected": 6,
            }),

            # Wordwall «Quiz · GG1 5.3» — СОСТАВ МОЙ
            mcq("Выбери правильный ответ ⭐", [
                ("Can you swim? — Yes, I ___.", ["can", "can't", "am"], "can"),
                ("Can your dad cook? — No, he ___.", ["can't", "can", "isn't"], "can't"),
                ("___ they play the piano?", ["Can", "Are", "Cans"], "Can"),
                ("Can she ride a bike? — Yes, ___ can.", ["she", "he", "her"], "she"),
                ("What can your dog do? — It ___ run fast.", ["can", "cans", "is"], "can"),
                ("Can the birds sing? — Yes, ___.", ["they can", "they can't", "it can"], "they can"),
            ]),

            bye("<h3>Молодец! 🎉</h3><p>Ты справился со всеми заданиями и показал, как хорошо знаешь "
                "тему. Ты настоящая звезда! ⭐ До встречи на уроке!</p>", "well_done_star"),
        ],
    },

    "u5_test": {
        **U5,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        "blocks": [
            # в выгрузке картинок у пар нет — наши (Л5.1, Л5.2)
            ("match", {"title": "Соедини слова и картинки", "pairs": [
                {"left": en, "right_image": verb(en)}
                for en in ["cook", "swim", "fly", "write", "sing", "read"]
            ]}),

            # в выгрузке пропуск — одна буква, фото людей; у нас слово целиком и картинки-предметы
            ("exact_input", {"title": "Посмотри на картинку и впиши сочетание целиком", "items": [
                {"prompt": hint, "accept": list(dict.fromkeys([ans, ans.capitalize()])), "image": u(p)}
                for hint, ans, p in [
                    ("pl_y the p_ano", "play the piano", "coll_play_piano"),
                    ("r_d_ the h_rse", "ride the horse", "coll_ride_horse"),
                    ("m_ke c_pcakes", "make cupcakes", "coll_make_cupcakes"),
                    ("pl_y footb_ll", "play football", "coll_play_football"),
                    ("r_d_ a bike", "ride a bike", "coll_ride_bike"),
                    ("m_ke a p_ster", "make a poster", "coll_make_poster"),
                ]
            ]}),

            # в выгрузке варианты Could / do — тоже грамматичны, заменены
            mcq("Прочитай диалог и выбери пропущенное слово", [
                ("A: ___ you make a poster? B: No, I can't.", ["Can", "Cans", "Is"], "Can",
                 u("coll_make_poster")),
                ("A: Can you make a poster? B: No, I ___.", ["can't", "can", "don't"], "can't"),
                ("A: What ___ you and your brother do? B: We can play the guitar.",
                 ["can", "cans", "is"], "can", u("obj_guitar")),
                ("A: What can you and your brother do? B: We ___ play the guitar.",
                 ["can", "are", "have"], "can"),
                ("Joanna ___ draw, but she can't write yet.", ["can", "cans", "do"], "can",
                 u("obj_crayons_drawing")),
                ("Joanna can draw, but she ___ write yet.", ["can't", "cans", "haven't"], "can't"),
                ("His aunt ___ ride a horse. She's old.", ["can't", "don't", "can"], "can't",
                 u("coll_ride_horse")),
                ("A: ___ you cook well? B: Yes, I can.", ["Can", "Has", "Does"], "Can",
                 u("obj_mixing_bowl")),
                ("A: Can you cook well? B: Yes, I ___.", ["can", "can't", "have"], "can"),
            ]),

            order("Can your brother fix that computer?",
                  ["Can", "your brother", "fix", "that", "computer?"],
                  title="Расставь слова в правильном порядке", image=u("obj_broken_laptop")),
            order("Can Betty's dog run fast?", ["Can", "Betty's dog", "run", "fast?"],
                  title="Расставь слова в правильном порядке", image=u("animal_beagle_puppy")),
            order("Max and his friends can't speak French.",
                  ["Max and", "his friends", "can't", "speak", "French."],
                  title="Расставь слова в правильном порядке", image=u("obj_french_flag")),
            order("The students can't read difficult words.",
                  ["The students", "can't", "read", "difficult", "words."],
                  title="Расставь слова в правильном порядке", image=u("obj_book_stack")),
            order("What can your hamster do?", ["What", "can", "your", "hamster", "do?"],
                  title="Расставь слова в правильном порядке", image=u("animal_hamster")),

            ("gaps", {
                "title": "READING. Прочитай рекламу спортивного клуба и впиши пропущенный глагол. "
                         "Используй слова из списка",
                "mode": "drag",
                "text": "1. You can __swim__ in the swimming pool every Monday.\n"
                        "2. You can __ride__ a bike in the park on Tuesday.\n"
                        "3. You can __climb__ on the climbing wall on Wednesday.\n"
                        "4. On Thursday, you can sing and __dance__ in the music room.\n"
                        "5. On Friday, you can __draw__ and paint pictures of the city.",
                "gaps_expected": 5,
            }),

            listening("LISTENING. Прослушай рассказ Джека о себе и своей сестре Лили."),

            ("sort", {"title": "LISTENING. Перетащи каждое умение в нужный столбик", "groups": [
                {"name": "Jack can", "items": [{"text": t} for t in
                                               ["ride a bike", "swim", "dive", "play football"]]},
                {"name": "Lily can", "items": [{"text": t} for t in
                                               ["sing", "play the piano", "draw", "ride a horse"]]},
            ]}),

            # в выгрузке «Can you father skateboard?» — исправлено
            ("speaking", {
                "title": "SPEAKING TASK 🎤",
                "html": "<p>Ответь на вопросы. Запиши свой ответ, нажав на кнопку микрофона 🙌</p>"
                        "<ol><li>Can you swim?</li><li>Can you cook well?</li>"
                        "<li>What can your best friend do?</li><li>Can your brother play the piano?</li>"
                        "<li>Can your father skateboard?</li><li>Can your teacher fix the computer?</li>"
                        "<li>What can kangaroos do?</li><li>Can penguins fly?</li>"
                        "<li>Can your mother drive a car?</li><li>Can your grandpa climb?</li>"
                        "<li>Can you ride a bike?</li><li>Can your classmates speak English?</li></ol>",
                "needs_review": True,
            }),
        ],
    },
}
