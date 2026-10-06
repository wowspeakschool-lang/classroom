#!/usr/bin/env python3
"""Go Getter 1 · Unit 6 · My day — уроки (разбор: docs/GG1_разбор/u6.md).

Распорядок дня, Present Simple (he / she + -s), наречия частотности, дни
недели, время по часам, месяцы, before / after. Действия — предметом, без
людей (листы Л6.1–Л6.2), Майк и Даша — Л6.3–Л6.4; карточки методиста, таблицы
учебника и рисованные иллюстрации — кадры из выгрузки. Циферблаты рисует
tools/gg1_clocks.py (svg): стрелки должны стоять точно.
"""
from gg1_lib import *  # noqa: F401,F403

U = "u6"
U6 = {"unit": U, "unit_title": "Unit 6 · My day", "unit_sort": 6}


def u(name):
    return img(U, name)


def clock(hhmm):
    """Циферблат tools/gg1_clocks.py, «0445» → 4:45."""
    return f"{MEDIA}gg1/{U}/clock_{hhmm}.svg"


U6_DAY = vocab([
    ("get up", "вставать", "da_get_up"),
    ("go to school", "ходить в школу", "da_go_to_school"),
    ("have lessons", "учиться на уроках", "da_have_lessons"),
    ("have breakfast", "завтракать", "da_have_breakfast"),
    ("have lunch", "обедать", "da_have_lunch"),
    ("have dinner", "ужинать", "da_have_dinner"),
    ("have a shower", "принимать душ", "da_have_a_shower"),
    ("do my homework", "делать домашнее задание", "da_do_homework"),
    ("tidy my room", "убираться в комнате", "da_tidy_my_room"),
    ("hang out with my friends", "тусоваться с друзьями", "da_hang_out_with_friends"),
    ("listen to music", "слушать музыку", "da_listen_to_music"),
    ("watch TV", "смотреть телевизор", "da_watch_tv"),
    ("go to bed", "ложиться спать", "da_go_to_bed"),
])

CHAMPION = ("Ты выполнил все задания из основной части! А это дополнительное задание — "
            "для настоящих чемпионов! ")
REVIEW = "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"
EXTRA = ("<p>В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых "
         "сильных учеников 💪</p>")
BYE = "<h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"


def day(en):
    return u(next(p for e, r, p in U6_DAY if e == en))


def hide_vowels(phrase):
    """Тест, блок 1: «впиши недостающие буквы». Какие буквы скрывала выгрузка,
    не видно — прячем гласные, кроме первой буквы слова."""
    return " ".join(w[0] + "".join("_" if c in "aeiou" else c for c in w[1:])
                    for w in phrase.split(" "))


def accept(phrase):
    return list(dict.fromkeys([phrase, phrase[0].upper() + phrase[1:], phrase.lower(),
                               phrase.capitalize()]))


LESSONS = {
    # Homework 1 (1) — словарный тренажёр «распорядок дня», (2) — задания. Один урок.
    "u6_hw1": {
        **U6,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>В этом уроке тебя ждут упражнения на отработку новых "
                  "слов — про то, что мы делаем каждый день. Выполни все, если хочешь выучить "
                  "тему на все 100!</p>"),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U6_DAY
            ]}),

            ("match", {"title": "Соедини картинку и фразу", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in U6_DAY[:7]
            ]}),

            ("match", {"title": "И ещё: соедини картинку и фразу", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in U6_DAY[7:]
            ]}),

            ("quiz", quiz_ru_to_en(U6_DAY)),

            ("exact_input", {"title": "Посмотри на картинку и напиши фразу по-английски", "items": [
                {"prompt": ru, "accept": accept(en), "image": u(p), "audio_tts": en}
                for en, ru, p in U6_DAY if en in ("get up", "have breakfast", "go to school",
                                                  "have lunch", "listen to music", "go to bed")
            ]}),

            ("text", {"html": "<h3>Добро пожаловать во вторую часть домашнего задания! 👋</h3>"
                              "<p>Выполни все задания, чтобы хорошенько запомнить новые слова — "
                              "и ты станешь МЕГА крутым учеником!</p>" + REVIEW
                              + pic(u("card_daily_activities"), "Daily activities")}),

            ("gaps", {
                "title": "Вставь глаголы в предложения по смыслу",
                "mode": "drag",
                "image": u("girl_routine"),
                "text": "1. I __have__ lessons.\n"
                        "2. I __get up__ in the morning.\n"
                        "3. I __do__ my homework.\n"
                        "4. I __go__ to bed.\n"
                        "5. I __hang__ out with my friends.",
                "gaps_expected": 5,
            }),

            ("match", {"title": "Соедини начало и продолжение фраз. Не торопись 😉", "pairs": [
                {"left": "listen to", "right": "music"},
                {"left": "tidy my", "right": "room"},
                {"left": "have", "right": "lessons"},
                {"left": "have a", "right": "shower"},
                {"left": "do my", "right": "homework"},
                {"left": "go to", "right": "school"},
                {"left": "watch", "right": "TV"},
                {"left": "hang out with", "right": "my friends"},
            ]}),

            ("task", {
                "title": "Мой день ✍️",
                "needs_review": True,
                "html": pic(u("routine_icons"), "Daily routine", 220)
                        + "<p>Напиши список того, что ты делаешь каждый день.</p>"
                          "<p><i>Пример: I get up. I have breakfast. I go to school…</i></p>",
            }),

            # Wordwall «Соедини: gg1unit-61» (обложка пустая) — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини фразу и перевод ⭐", "pairs": [
                {"left": en, "right": ru, "left_audio_tts": en} for en, ru, p in U6_DAY
            ]}),

            # Wordwall «Впиши фразы: GG1 U6 6.1 Daily activities» (обложка пустая) — СОСТАВ МОЙ
            ("exact_input", {"title": "Впиши фразы по-английски ⭐", "items": [
                {"prompt": ru, "accept": accept(en), "image": u(p), "audio_tts": en}
                for en, ru, p in U6_DAY if en in ("have a shower", "have dinner", "have lessons",
                                                  "do my homework", "tidy my room", "watch TV")
            ]}),

            bye("<h3>Поздравляю! Ты завершил домашнее задание. Ты — МЕГА КРУТ! 🎉</h3>"
                "<p>Жду тебя на уроке!</p>", "congrats_popper"),
        ],
    },

    "u6_hw2": {
        **U6,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня мы закрепим знания, полученные на уроке, и ты без "
                  "проблем сможешь использовать время Present Simple.</p>" + EXTRA, "hello_book"),

            ("text", {"html": REVIEW + pic(u("card_present_simple"), "Present Simple")}),

            ("text", {"html": "<p>Макс и Хэмми рассказывают, как они проводят время перед сном. "
                              "Посмотри на картинку и попробуй угадать: <b>What movies does Hammy "
                              "like watching before sleeping?</b> 😴</p>"
                              + pic(u("hammy_bedtime"), "Hammy", 240)
                              + "<p>Посмотри видео и проверь, угадал ли ты. Повторяй вопросы и "
                                "ответы за героями, чтобы хорошенько запомнить правила.</p>"}),

            ("video", {"title": "Max and Hammy: before bed", "url": "", "provider": "youtube"}),

            mcq("Выбери правильный вариант. Внимательно смотри на главное слово!", [
                ("Jen ___ TV after dinner.", ["watches", "watch"], "watches"),
                ("Alex ___ his homework in his room.", ["does", "do"], "does"),
                ("Lucas and Alex ___ football in the park.", ["play", "plays"], "play"),
                ("Jen and Alex ___ late.", ["get up", "gets up"], "get up"),
                ("Lucas's mum ___ to music in the kitchen.", ["listens", "listen"], "listens"),
                ("Lucas ___ to school with Jen and Alex.", ["goes", "go"], "goes"),
            ]),

            ("gaps", {
                "title": "Впиши правильную форму глагола. Смотри, как в первой строке — это пример!",
                "mode": "type",
                "text": "I / You / We / They — He / She / It\n"
                        "play — plays\n"
                        "__do__ — does\n"
                        "draw — __draws__\n"
                        "__drink__ — drinks\n"
                        "__look__ — looks\n"
                        "wash — __washes__\n"
                        "__carry__ — carries",
                "gaps_expected": 6,
            }),

            ("gaps", {
                "title": "Впиши в пропуски слова, раскрыв скобки. Посмотри, как это сделано в первом предложении!",
                "mode": "type",
                "text": "0. I usually walk (walk) to school but my friend always rides (ride) his bike.\n"
                        "1. My brother and I __like__ (like) juice but my sister __drinks__ (drink) milk.\n"
                        "2. Mum and Dad __watch__ (watch) TV and my sister and I __play__ (play) "
                        "computer games after dinner.\n"
                        "3. Rob __tidies__ (tidy) his room and he __helps__ (help) in the kitchen too.\n"
                        "4. Sue __has__ (have) sandwiches for lunch. She __eats__ (eat) them in the classroom.\n"
                        "5. I __hang out__ (hang out) with my friends after school. Then I __have__ (have) dinner.\n"
                        "6. Harry __does__ (do) his homework and then he __watches__ (watch) TV.",
                "gaps_expected": 12,
            }),

            ("task", {
                "title": "Обо мне и о друге ✍️",
                "needs_review": True,
                "html": "<p>Напиши 3 предложения о себе и 3 предложения о своём члене семьи, друге или "
                        "даже учителе! Чем вы занимаетесь каждый день?</p>"
                        "<p><i>Посмотри, это мои предложения: I get up at 9 o'clock. I watch TV in the "
                        "evening. I read a book before sleeping. My best friend Anna gets up at 7 o'clock. "
                        "She plays computer games after school. She has dinner at 8 o'clock in the "
                        "evening.</i></p><p>Обрати внимание на окончания глаголов, когда я рассказываю "
                        "о своей подруге 😉</p>",
            }),

            # Wordwall «Выбери правильный вариант: gg1-unit-62» (обложка пустая) — СОСТАВ МОЙ
            mcq(CHAMPION + "Выбери правильный вариант ⭐", [
                ("My sister ___ to school by bus.", ["goes", "go"], "goes"),
                ("We ___ breakfast at 8 o'clock.", ["have", "has"], "have"),
                ("Tom ___ TV in the evening.", ["watches", "watch"], "watches"),
                ("I ___ my room on Saturdays.", ["tidy", "tidies"], "tidy"),
                ("Anna ___ English and Maths.", ["studies", "studys"], "studies"),
                ("They ___ to music after school.", ["listen", "listens"], "listen"),
            ]),

            # Wordwall «Заполни пропуски: gg1-unit-62» (обложка пустая) — СОСТАВ МОЙ
            ("gaps", {
                "title": "Заполни пропуски ⭐",
                "mode": "drag",
                "text": "My dad __gets__ up at 7 o'clock.\n"
                        "He __has__ a shower and __makes__ breakfast.\n"
                        "My brother __goes__ to school with me.\n"
                        "After school he __does__ his homework.\n"
                        "In the evening my mum __watches__ TV.",
                "gaps_expected": 6,
            }),

            bye(BYE, "well_done_star"),
        ],
    },

    "u6_hw3": {
        **U6,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня мы закрепим знания, полученные на уроке, и ты без "
                  "проблем сможешь использовать разные наречия, чтобы говорить о том, как часто "
                  "что-то происходит.</p>" + EXTRA, "hello_highfive"),

            ("text", {"html": REVIEW + pic(u("card_adverbs"), "Adverbs of frequency")
                              + pic(u("card_days"), "Days of the week")}),

            ("text", {"html": "<p>Ребята рассказывают, как они обычно проводят выходные. Посмотри на "
                              "картинку и попробуй угадать: <b>How often does Hammy play computer "
                              "games?</b></p>" + pic(u("hammy_weekend"), "Hammy", 240)
                              + "<p>Посмотри видео и проверь, угадал ли ты. Повторяй вопросы и "
                                "ответы за героями, чтобы хорошенько запомнить правила.</p>"}),

            ("video", {"title": "Max and Hammy: at the weekend", "url": "", "provider": "youtube"}),

            # в выгрузке «has breakfast home» — исправлено на «at home»
            ("gaps", {
                "title": "Посмотри на таблицу и на кружочки: сколько закрашено, так часто это бывает. "
                         "Впиши нужное слово",
                "mode": "drag",
                "image": u("adverbs_table"),
                "text": "1. Jack sometimes cycles to school. 🔴⚪⚪⚪ (пример)\n"
                        "2. Emma __always__ has breakfast at home. 🔴🔴🔴🔴\n"
                        "3. Pete __usually__ does his homework in his bedroom. 🔴🔴🔴⚪\n"
                        "4. I __sometimes__ play in the park. 🔴⚪⚪⚪\n"
                        "5. We __never__ watch TV in the morning. ⚪⚪⚪⚪\n"
                        "6. My parents __often__ go out with their friends. 🔴🔴⚪⚪",
                "gaps_expected": 5,
            }),

            order("I'm often busy on Saturdays.",
                  title="Расставь слова в правильном порядке. Подсказка — на карточке выше 👆"),
            order("Kit often helps me at home.", title="Расставь слова в правильном порядке"),
            order("Uncle Roberto sometimes visits me.", ["Uncle Roberto", "sometimes", "visits", "me."],
                  title="Расставь слова в правильном порядке"),
            order("I never cook dinner.", title="Расставь слова в правильном порядке"),
            order("Kit is always happy.", title="Расставь слова в правильном порядке"),
            order("Kit and I usually have fun.", ["Kit", "and I", "usually", "have", "fun."],
                  title="Расставь слова в правильном порядке"),

            ("sequence", {"title": "Ты уже на финишной прямой! Расставь дни недели в правильном "
                                   "порядке 👏", "items": [
                {"text": d} for d in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                                      "Saturday", "Sunday"]]}),

            ("task", {
                "title": "Как часто? ✍️",
                "needs_review": True,
                "html": "<p>Напиши 3 предложения о себе: как часто ты что-то делаешь?</p>"
                        "<p><i>Посмотри, это мои предложения: I usually get up at 9 o'clock. I sometimes "
                        "watch TV in the evening. I am never late for the train.</i></p>"
                        "<p>Удачи, у тебя всё получится!</p>",
            }),

            # Wordwall «Match up · Adverbs of frequency GG1 Un.6.3» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини наречие и то, как часто это бывает ⭐", "pairs": [
                {"left": "always", "right": "100% — всегда", "left_audio_tts": "always"},
                {"left": "usually", "right": "75% — обычно", "left_audio_tts": "usually"},
                {"left": "often", "right": "50% — часто", "left_audio_tts": "often"},
                {"left": "sometimes", "right": "25% — иногда", "left_audio_tts": "sometimes"},
                {"left": "never", "right": "0% — никогда", "left_audio_tts": "never"},
            ]}),

            # Wordwall «Unjumble · Gg1 6.3» — СОСТАВ МОЙ
            order("I always have breakfast.", title="Расставь слова в правильном порядке ⭐"),
            order("She usually goes to school by bus.", title="Расставь слова в правильном порядке ⭐"),
            order("He is never late.", title="Расставь слова в правильном порядке ⭐"),

            bye(BYE, "well_done_clap"),
        ],
    },

    "u6_hw4": {
        **U6,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня мы закрепим знания, полученные на уроке, и ты без "
                  "проблем сможешь определять время по часам и подсказывать время другим.</p>",
                  "hello_laptop"),

            ("text", {"html": REVIEW + pic(u("card_time"), "Telling the time")}),

            ("text", {"html": "<p>Внимательно посмотри видео и постарайся запомнить, как правильно "
                              "определять время на английском. Повторяй фразы за видео, чтобы "
                              "хорошенько запомнить.</p>"}),

            ("video", {"title": "Telling the time", "url": "", "provider": "youtube"}),

            # в выгрузке часов справа нет — циферблаты наши (tools/gg1_clocks.py)
            ("match", {"title": "Соедини предложения с часами", "pairs": [
                {"left": t, "right_image": clock(c), "left_audio_tts": t} for t, c in [
                    ("It's quarter to five.", "0445"),
                    ("It's six o'clock.", "0600"),
                    ("It's ten past nine.", "0910"),
                    ("It's quarter past one.", "0115"),
                    ("It's twenty to nine.", "0840"),
                    ("It's half past two.", "0230"),
                    ("It's five past five.", "0505"),
                    ("It's five to one.", "1255"),
                ]]}),

            ("gaps", {
                "title": "Расставь фразы в диалоги. Расписание телепрограмм поможет тебе!",
                "mode": "drag",
                "image": u("tv_schedule"),
                "text": "1. A: What time is Pet Time? B: It's at six o'clock. (пример)\n"
                        "2. A: What time is That's Magic? B: __It's at quarter past seven.__\n"
                        "3. A: __What time is Happy Days?__ B: It's at five past seven.\n"
                        "4. A: __What time is Super Girl?__ B: It's at twenty-five to seven.\n"
                        "5. A: What time is The Great Big Talent Show? B: __It's at ten to eight.__\n"
                        "6. A: OK. __What time is it__ now? B: It's five to six. Hurry up!",
                "gaps_expected": 5,
            }),

            ("sequence", {"title": "Расставь предложения так, чтобы получился складный диалог",
                          "items": [{"text": t} for t in [
                              "What time is it, Mandy?",
                              "It's half past five. Oh no!",
                              "What's wrong? Are you OK?",
                              "No, I'm not. I'm late for my music lesson.",
                              "Oh dear. What time is your music lesson?",
                              "It's at quarter to six. Bye!",
                          ]]}),

            # в выгрузке «впиши в пропуски», но ответы личные — проверяет учитель
            ("task", {
                "title": "Во сколько? ✍️",
                "needs_review": True,
                "html": "<p>Продолжи предложения о себе. Во сколько ты делаешь все эти дела? Пиши время "
                        "словами, например, <i>twenty to seven</i> или <i>six o'clock</i>.</p>"
                        "<ol><li>I get up at ______.</li><li>I have breakfast at ______.</li>"
                        "<li>I go to school at ______.</li><li>I do my homework at ______.</li>"
                        "<li>I go to bed at ______.</li></ol>",
            }),

            bye(BYE, "well_done_medal"),
        ],
    },

    "u6_hw5": {
        **U6,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Как ты помнишь, на уроке мы читали текст и выполняли "
                  "упражнения по нему. Сегодня ты тоже будешь читать текст и выполнять задания, "
                  "но уже самостоятельно!</p>" + EXTRA, "hello_rocket"),

            ("text", {"html": REVIEW + pic(u("card_months"), "Months of the year")}),

            # в выгрузке страница учебника с фото детей — у нас портреты Л6.4 и текст
            ("text", {"html":
                "<p><b>Внимательно прочитай текст, после тебя ждут упражнения.</b></p>"
                + pic(u("mike"), "Mike", 200)
                + "<p><i>Hi. I'm Mike. I'm ten and I'm American. I live in New York. My school is very "
                "big. I like sport. I'm not very good at Art but I love it. I have lunch in the "
                "classroom. I usually have pizza! After school I always hang out with my friends. We "
                "sometimes play basketball or we go to the park.</i></p>"
                + pic(u("dasha"), "Dasha", 200)
                + "<p><i>My name is Dasha and I'm nine. I go to a special school. It's a ballet school! "
                "After breakfast we have lessons. My favourite lessons are Maths and English. Then we "
                "have lunch. I often have pancakes! After lunch we always dance. I'm always busy.</i></p>"}),

            # в выгрузке элементы пустые — СОСТАВ МОЙ по тексту, картинки Л6.3
            ("sort", {"title": "Распредели картинки: что про Майка, а что про Дашу?", "groups": [
                {"name": "Mike", "items": [{"image": u(n)} for n in
                                           ["md_pizza", "md_basketball", "md_new_york"]]},
                {"name": "Dasha", "items": [{"image": u(n)} for n in
                                            ["md_ballet", "md_pancakes", "md_maths"]]},
            ]}),

            # в выгрузке п.6 отмечен true, по тексту — false (уроки после завтрака)
            ("truefalse", {"title": "Прочитай текст ещё раз: правда это (true) или ложь (false)? "
                                    "Находи доказательства в тексте", "statements": [
                {"text": "Mike likes Art.", "correct": True},
                {"text": "He eats pizza in the classroom.", "correct": True},
                {"text": "He never goes to the park after school.", "correct": False},
                {"text": "Dasha likes Maths.", "correct": True},
                {"text": "She has pancakes every day.", "correct": False},
                {"text": "She has lessons after lunch.", "correct": False},
            ]}),

            ("gaps", {
                "title": "Прочитай текст ещё раз и впиши в предложения 1–2 слова по смыслу",
                "mode": "type",
                "text": "1. Mike goes to a __big|very big__ school.\n"
                        "2. He plays basketball with his __friends__.\n"
                        "3. Dasha has __lessons__ after breakfast.\n"
                        "4. Dasha is always __busy__.",
                "gaps_expected": 4,
            }),

            ("sequence", {"title": "Дополнительное задание ⭐ Давай вспомним все месяцы! Расставь их "
                                   "в правильном порядке, начиная с January",
                          "image": u("seasons"),
                          "items": [{"text": m} for m in [
                              "January", "February", "March", "April", "May", "June", "July",
                              "August", "September", "October", "November", "December"]]}),

            ("speaking", {
                "title": "Мой год 🎤",
                "html": "<p>Нажми на микрофон и расскажи, что ты делаешь в разные месяцы года.</p>"
                        "<p><i>Пример: In January I go skiing. In March it's my birthday. In July I'm on "
                        "holiday with my family. In September I go to school again.</i></p>",
                "needs_review": True,
            }),

            bye(BYE, "well_done_jump"),
        ],
    },

    "u6_hw6": {
        **U6,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Как ты помнишь, на уроке мы слушали рассказы ребят о том, как "
                  "они проводят выходные. Сегодня ты тоже будешь слушать и выполнять задания, но уже "
                  "самостоятельно!</p>", "hello_headphones"),

            listening("Послушай рассказ Энди о его каникулах. Потом выполни два задания ниже."),

            ("gaps", {
                "title": "Заполни таблицу. В каждом пропуске — только ОДНО слово",
                "mode": "type",
                "text": "Country: __Italy__\n"
                        "Aunt's nationality: __British__\n"
                        "Aunt's job: __teacher|Teacher__\n"
                        "Favourite place: __beach|Beach__\n"
                        "Favourite game: __catch|Catch__",
                "gaps_expected": 5,
            }),

            mcq("Послушай рассказ Энди ещё раз и выбери правильный ответ. Сначала внимательно "
                "прочитай предложения", [
                    ("Andy ___ goes on holiday in August.", ["always", "usually"], "always"),
                    ("After breakfast they ___ go to the beach.", ["usually", "often"], "usually"),
                    ("They ___ have a picnic on the beach.", ["often", "always"], "often"),
                    ("They ___ go to bed after lunch.", ["often", "usually"], "often"),
                    ("He ___ gets up early.", ["always", "never"], "always"),
                ]),

            # в выгрузке страница учебника с фото девочки — у нас портрет Л6.4 и текст
            ("text", {"html":
                "<p><b>Прочитай небольшой текст о том, как Джен обычно проводит выходные. Подумай, "
                "похоже ли ваше времяпрепровождение?</b></p>"
                + pic(u("jen"), "Jen", 200)
                + "<p><b>My weekend</b></p><p><i>I usually get up at 8 o'clock on Saturdays. After "
                "breakfast I skateboard with my friends. I love my skateboard and I love Saturdays! "
                "Before dinner I watch TV or play computer games. I get up at 9 o'clock on Sundays. "
                "Before lunch I tidy my room and I do my homework. I always have lunch with my family! "
                "After lunch I often draw or listen to music.</i></p>"}),

            # в выгрузке правило шло после задания («прикреплено ниже») — поставили перед ним
            ("text", {"html": "<p><b>Правило: before (до) и after (после)</b></p>"
                              + pic(u("before_after"), "before, after")}),

            ("task", {
                "title": "Мои выходные ✍️",
                "needs_review": True,
                "html": pic(u("cat_sunglasses"), "Cat", 180)
                        + "<p>Напиши небольшой рассказ о себе по примеру рассказа Джен. Чтобы сделать "
                          "его интереснее, используй <b>after</b> (после) и <b>before</b> (до) — правило "
                          "выше. Котик желает тебе удачи! 😉</p>",
            }),

            bye(BYE, "well_done_smiley"),
        ],
    },

    "u6_hw7": {
        **U6,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня мы закрепим знания, полученные в этом месяце. На "
                  "следующем занятии тебя ждёт тест, и сегодня мы будем к нему готовиться вместе.</p>"
                  + EXTRA, "hello_book"),

            ("gaps", {
                "title": "Заполни пропуски недостающими по смыслу словами. Посмотри на пример под номером 0",
                "mode": "drag",
                "image": u("girl_routine"),
                "text": "0. In the morning I get up at 7 o'clock.\n"
                        "1. We __have__ lessons all day.\n"
                        "2. After school, I __hang__ out with friends.\n"
                        "3. We __play__ computer games on Saturdays.\n"
                        "4. Before bed, I __watch__ TV.\n"
                        "5. At night, I __go__ to bed at 9 o'clock.",
                "gaps_expected": 5,
            }),

            ("gaps", {
                "title": "Посмотри на слова и впиши пропущенное. Посмотри на пример под номером 0",
                "mode": "type",
                "text": "0. January — February — March\n"
                        "1. July — __August__ — September\n"
                        "2. Friday — __Saturday__ — Sunday\n"
                        "3. October — __November__ — December\n"
                        "4. March — __April__ — May\n"
                        "5. Tuesday — __Wednesday__ — Thursday",
                "gaps_expected": 5,
            }),

            mcq("Прочитай предложения и выбери правильный вариант. Пример: Tom gets up early.", [
                ("We ___ to a big school.", ["go", "gos", "goes"], "go"),
                ("Sally ___ chocolate ice cream.", ["likes", "like", "liks"], "likes",
                 u("obj_ice_cream_chocolate")),
                ("Harry ___ his room on Sundays.", ["tidies", "tidy", "tidys"], "tidies"),
                ("They ___ their homework in the living room.", ["do", "dos", "does"], "do"),
                ("I ___ lunch in the park.", ["have", "has", "haves"], "have"),
            ]),

            # в выгрузке клипарт с людьми — у нас предметы Л6.1–Л6.2
            order("I am always busy.", title="Расставь слова в правильном порядке",
                  image=u("obj_busy_planner")),
            order("We often play tennis.", title="Расставь слова в правильном порядке",
                  image=u("obj_tennis")),
            order("Mom never watches TV.", title="Расставь слова в правильном порядке",
                  image=day("watch TV")),
            order("I sometimes tidy my room.", title="Расставь слова в правильном порядке",
                  image=day("tidy my room")),
            order("Jess is usually late.", title="Расставь слова в правильном порядке",
                  image=u("obj_late_clock")),

            ("gaps", {
                "title": "Дополнительное задание ⭐ Прочитай диалоги и вставь пропущенные по смыслу слова",
                "mode": "type",
                "image": clock("1230"),
                "text": "1. A: What time is lunch? B: It's at half __past__ twelve.\n"
                        "2. A: What time __is__ it? B: It's ten __minutes__ to five.\n"
                        "3. A: What time is the film? B: It's __at__ six __o'clock|oclock__.",
                "gaps_expected": 5,
            }),

            ("speaking", {
                "title": "Моя неделя 🎤",
                "html": "<p>Нажми на микрофон и расскажи о своей типичной неделе.</p>"
                        "<p><i>Пример: On weekdays I always go to school. On Tuesday I usually have a "
                        "music lesson. At the weekend I often hang out with my friends. I never get up "
                        "early on Sunday.</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Match up · GG1 Unit 6.1» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини картинку и фразу ⭐", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in U6_DAY if en in ("get up", "have a shower", "have breakfast",
                                                  "go to school", "do my homework",
                                                  "hang out with my friends", "go to bed")
            ]}),

            # Wordwall «Quiz · GG1 (Unit 6.2 — Present Simple+)» — СОСТАВ МОЙ
            mcq("Выбери правильный вариант ⭐", [
                ("She ___ up at 7 o'clock.", ["gets", "get"], "gets"),
                ("My friends ___ football after school.", ["play", "plays"], "play"),
                ("Dad ___ the dishes after dinner.", ["washes", "washs"], "washes"),
                ("You ___ lunch at school.", ["have", "has"], "have"),
                ("My cat ___ a lot.", ["sleeps", "sleep"], "sleeps"),
                ("Ben ___ to music in his room.", ["listens", "listen"], "listens"),
            ]),

            # Wordwall «Find the match · gg1 6.3» — СОСТАВ МОЙ
            ("match", {"title": "Соедини наречие и перевод ⭐", "pairs": [
                {"left": en, "right": ru, "left_audio_tts": en} for en, ru in [
                    ("always", "всегда"), ("usually", "обычно"), ("often", "часто"),
                    ("sometimes", "иногда"), ("never", "никогда")]
            ]}),

            bye("<h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3>"
                "<p>Уверена, ты справишься с тестом на все сто! Удачи!</p>", "good_luck_clover"),
        ],
    },

    "u6_test": {
        **U6,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        "blocks": [
            # в выгрузке скрытые буквы не видны — прячем гласные, фразу пишем целиком
            ("exact_input", {"title": "Впиши фразу целиком, вставив недостающие буквы", "items": [
                {"prompt": f"{hide_vowels(en)} — {ru}", "accept": accept(en), "image": u(p)}
                for en, ru, p in U6_DAY if en in (
                    "do my homework", "tidy my room", "go to school", "have lessons",
                    "hang out with my friends", "listen to music", "have a shower",
                    "have breakfast", "have lunch", "have dinner")
            ]}),

            mcq("Прочитай предложение и выбери пропущенное слово", [
                ("He ___ up really early at 6 o'clock.", ["gets", "get"], "gets", u("boy_wakes_up")),
            ]),
            mcq("Прочитай диалог и выбери пропущенные слова", [
                ("A: I ___ lunch at home. And you?", ["have", "has"], "have", u("obj_school_canteen")),
                ("B: Me too. But my brother ___ at school all day…", ["is", "are"], "is"),
                ("B: …and he ___ lunch there.", ["has", "have", "haves"], "has"),
            ]),
            mcq("Прочитай предложение и выбери пропущенное слово", [
                ("My friend Alice and I ___ computer games after school.", ["play", "plays"], "play",
                 u("obj_computer_games")),
            ]),
            mcq("Посмотри на часы и выбери ответ", [
                ("A: What time is it? B: It is ___.",
                 ["quarter past 2", "quarter to 2", "half past 2"], "quarter past 2", clock("0215")),
            ]),
            # в выгрузке «half past eight» был и неверным в 1-м пропуске, и верным во 2-м —
            # в первом заменили на «half past seven»
            mcq("Прочитай диалог и выбери пропущенные слова", [
                ("A: What time do you get up? B: I get up at ___. And you?",
                 ["eight o'clock", "nine o'clock", "half past seven"], "eight o'clock", clock("0800")),
                ("A: I usually get up at ___.", ["half past eight", "eight past half"], "half past eight"),
            ]),

            order("He usually goes to the gym.", ["He", "usually", "goes", "to", "the gym."],
                  title="Расставь слова в правильном порядке", image=u("obj_gym")),
            order("She sometimes has dinner with us.", ["She", "sometimes", "has", "dinner", "with us."],
                  title="Расставь слова в правильном порядке", image=u("obj_family_dinner")),
            order("I get up at half past seven.", title="Расставь слова в правильном порядке",
                  image=clock("0730")),
            order("I have my birthday in September.", title="Расставь слова в правильном порядке",
                  image=u("birthday_cupcake")),
            order("What time is it now?", title="Расставь слова в правильном порядке",
                  image=u("pocket_watch")),

            # в выгрузке текст — картинкой
            ("text", {"html":
                "<h3>READING</h3><p>Прочитай дневник Джулии.</p>"
                "<p><b>My weekly schedule</b></p><p><i>On Monday, I always go to school early and have "
                "lessons until 3 pm. On Tuesday, I have a piano lesson after school. On Wednesday, I "
                "usually hang out with my friends in the park. On Thursday, I do my homework and watch "
                "TV. On Friday, I sometimes go to the cinema with my family. On Saturday, I always tidy "
                "my room in the morning. On Sunday, I never get up early — I love sleeping!</i></p>"}),

            ("match", {"title": "READING. Соедини каждый день недели с тем, что Джулия делает", "pairs": [
                {"left": "Monday", "right": "have lessons at school"},
                {"left": "Tuesday", "right": "have a piano lesson"},
                {"left": "Wednesday", "right": "hang out with friends in the park"},
                {"left": "Thursday", "right": "do homework and watch TV"},
                {"left": "Friday", "right": "go to the cinema with family"},
                {"left": "Saturday", "right": "tidy her room"},
                {"left": "Sunday", "right": "sleep late"},
            ]}),

            listening("LISTENING. Прослушай рассказ Алекса о его обычной субботе."),

            ("truefalse", {"title": "LISTENING. Правда или неправда?", "statements": [
                {"text": "Alex usually gets up at eight o'clock.", "correct": False},
                {"text": "He always has breakfast with his family.", "correct": True},
                {"text": "He does his homework on Sunday.", "correct": False},
                {"text": "He plays football with his friends in the park.", "correct": True},
                {"text": "They never go to the café.", "correct": False},
                {"text": "He has dinner at seven o'clock.", "correct": True},
                {"text": "He goes to bed at eleven.", "correct": False},
            ]}),

            ("speaking", {
                "title": "SPEAKING TASK. PART 1 🎤",
                "image": u("eric_day_comic"),
                "html": "<p>Посмотри на картинку и опиши, что делает Эрик и его семья.</p>"
                        "<p><i>Пример: Dad cooks breakfast at 7 o'clock.</i></p>"
                        "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>",
                "needs_review": True,
            }),

            ("speaking", {
                "title": "SPEAKING TASK. PART 2 🎤",
                "html": "<p>Ответь на вопросы:</p>"
                        "<ol><li>What do you do in the morning, afternoon and evening?</li>"
                        "<li>What does your mum / dad do in the morning, afternoon and evening?</li>"
                        "<li>What do you do at the weekend?</li></ol>"
                        "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>",
                "needs_review": True,
            }),
        ],
    },
}
