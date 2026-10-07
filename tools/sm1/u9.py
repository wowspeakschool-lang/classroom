"""Super Minds 1 · Unit 9 · Holidays — Homework 1–7 и тест юнита.

Выгрузка ShkolaApp, разбор — docs/SM1_разбор_u9_final.md. Первый заход:
HW2, HW3, HW4, HW6 (2), тест. Догружено 07.10.2026: HW1 (1)+(2), HW5,
HW6 (1), HW7 — HW1 и HW6 собраны из обеих частей одним уроком.

Словарные тренажёры (HW1 (1), HW6 (1)) выгружены со свёрнутым списком слов:
видно только число слов (9 и 7) и названия заданий. Слова взяты из
материала юнита (9 занятий на море — как в тесте и HW7; 7 мест — как в
HW6 (2)), задания пересобраны штатными блоками — СОСТАВ МОЙ.

Не перенесено из выгрузки: картинка-реклама для родителей («3 бесплатных
урока», «Новогодний розыгрыш»), «робуксы» и «коллекция ракушек» за задания,
раскраска HW1 (2), декоративные картинки (речевой пузырь, Спанч Боб,
Скрудж, Микки Маус, сломанная зелёная дуга в HW4, стоковые фото-приветствия).

Картинки, которых в выгрузке нет (пейзажи HW6, занятия на пляже), — под
листы Л9.1, Л9.2, Л9.4, ЛТ9.1; check() на них ругается «нет файла».
Фото детей из HW5 заменены картинками тех же занятий без людей.
Остальное вырезано из PDF в media/sm1/u9/.
"""
from sm1_build import *

U = "u9"
UNIT = "Unit 9 · Holidays"


def c(name):
    return img(U, name)


def hello(image, title, *paras):
    return ("text", {"html":
        f'<p><img src="{shared(image)}" alt="" style="height:200px"></p>'
        f"<h2>{title}</h2>" + "".join(f"<p>{p}</p>" for p in paras)})


def bye(image, title, *paras):
    return ("text", {"html":
        f'<p><img src="{shared(image)}" alt="" style="height:180px"></p>'
        f"<h3>{title}</h3>" + "".join(f"<p>{p}</p>" for p in paras)})


def pic(name, alt="", width="100%"):
    return f'<p><img src="{c(name)}" alt="{alt}" style="max-width:{width}"></p>'


def q1(q, options, correct, image=None):
    d = {"q": q, "type": "single", "options": [{"text": o} for o in options], "correct": [correct]}
    if image:
        d["image"] = image
    return d


def order(sentence, words, image=None):
    d = {"words": words, "sentence": sentence, "audio_tts": sentence}
    if image:
        d["image"] = image
    return ("order", d)


# Места из HW6 — картинок в выгрузке нет, листы Л9.1 и Л9.2
PLACES = [
    ("mountains", "горы", "place_mountains"),
    ("countryside", "сельская местность", "place_countryside"),
    ("beach", "пляж", "place_beach"),
    ("city", "город", "place_city"),
    ("theme park", "парк развлечений", "place_theme_park"),
    ("campsite", "кемпинг", "place_campsite"),
    ("lake", "озеро", "place_lake"),
]

# Занятия на пляже — словарь теста (лист ЛТ9.1 под «соедини с картинками»)
ACTIVITIES = [
    ("catch a fish", "поймать рыбу"),
    ("paint a picture", "рисовать картину"),
    ("eat ice cream", "есть мороженое"),
    ("take a photo", "фотографировать"),
    ("listen to music", "слушать музыку"),
    ("look for shells", "искать ракушки"),
    ("read a book", "читать книгу"),
    ("make a sandcastle", "строить замок из песка"),
    ("play the guitar", "играть на гитаре"),
]

# Картинки занятий: шесть — лист ЛТ9.1, три (ice cream, book, guitar) — Л9.4
ACT_IMG = {
    "catch a fish": "act_catch_fish", "paint a picture": "act_paint_picture",
    "eat ice cream": "act_eat_ice_cream", "take a photo": "act_take_photo",
    "listen to music": "act_listen_music", "look for shells": "act_look_shells",
    "read a book": "act_read_book", "make a sandcastle": "act_make_sandcastle",
    "play the guitar": "act_play_guitar",
}
ACT_WORDS = [(en, ru, ACT_IMG[en]) for en, ru in ACTIVITIES]


def listen_quiz(words, title="Послушай и выбери, что прозвучало"):
    """«Послушай» тренажёра: звучит слово, выбрать из четырёх.
    Верный — на позиции i % 4: варианты при показе не перемешиваются."""
    n = len(words)
    qs = []
    for i, (en, ru, _) in enumerate(words):
        wrong = [words[(i + k) % n][0] for k in range(1, 4)]
        pos = i % 4
        opts = wrong[:pos] + [en] + wrong[pos:]
        qs.append({"q": title, "type": "single", "audio_tts": en,
                   "options": [{"text": o} for o in opts], "correct": [pos]})
    return {"questions": qs}


def en_to_ru_quiz(words):
    """«Найди определение»: английское слово → перевод."""
    n = len(words)
    qs = []
    for i, (en, ru, f) in enumerate(words):
        wrong = [words[(i + k) % n][1] for k in range(1, 4)]
        pos = (i + 2) % 4
        opts = wrong[:pos] + [ru] + wrong[pos:]
        qs.append({"q": f"Что значит <b>{en}</b>?", "type": "single", "audio_tts": en,
                   "image": c(f), "options": [{"text": o} for o in opts], "correct": [pos]})
    return {"questions": qs}


def scramble(word):
    """Буквы слова вразброс, детерминированно: чётные позиции с конца, потом нечётные."""
    s = word[1::2][::-1] + word[0::2]
    return s if s != word else word[::-1]


def masked(phrase):
    """Каждая вторая буква слова (кроме первой) — пропуск: c_t_h a f_s_."""
    return " ".join("".join(ch if i % 2 == 0 else "_" for i, ch in enumerate(w))
                    if len(w) > 1 else w for w in phrase.split())


def tf(q, image, true):
    """Верно / неверно по картинке; варианты всегда True, False — как в выгрузке."""
    return {"q": q, "type": "single", "image": image,
            "options": [{"text": "True ✅"}, {"text": "False ❌"}],
            "correct": [0 if true else 1]}


LESSONS = {
    # ------------------------------------------------------------------ HW1
    "u9_hw1": {
        "unit": U, "unit_title": UNIT, "unit_sort": 9,
        "lesson_title": "Homework 1", "lesson_sort": 0, "kind": "homework",
        # Часть (1) — словарный тренажёр на 9 слов (Remember, Listen, Match,
        # доп.: Unscramble, Fill in), список слов в выгрузке свёрнут — слова
        # из словаря юнита, задания наши (СОСТАВ МОЙ). Часть (2): фото
        # «Hello» на песке и реклама (бл. 1) не перенесены, приветствие
        # (бл. 2) — перемычка, раскраска (бл. 3) выброшена, бл. 4 — task,
        # бл. 5 — прощание.
        "blocks": [
            # 1 — Teacher's note части (1)
            hello("hello_wave", "Добро пожаловать в домашнее задание!",
                  "Я не знаю человека, который бы не любил море! 🌊",
                  "Сегодня мы с тобой выучим различные занятия, которыми можно заниматься "
                  "на море. В этом уроке тебя ждут задания на отработку новых слов! Выполни "
                  "все, если хочешь выучить тему на все 100!",
                  "После того как завершишь все задания, тебя ждёт дополнительное задание — "
                  "его можно выполнить по желанию, НО если ты выполнишь его, то будешь "
                  "нереально крут!"),

            # 2
            ("flashcards", {"title": "Запомни слова. Нажми на карточку, чтобы увидеть перевод",
                            "cards": [{"text": en, "translation": ru, "audio_tts": en, "image": c(f)}
                                      for en, ru, f in ACT_WORDS]}),

            # 3 — «Remember»
            ("quiz", quiz_ru_to_en(ACT_WORDS)),

            # 4 — «Listen»
            ("quiz", listen_quiz(ACT_WORDS)),

            # 5 — «Match»
            ("match", {"title": "Найди пару: соедини картинку и слова",
                       "pairs": [{"left_image": c(f), "right": en, "right_audio_tts": en}
                                 for en, ru, f in ACT_WORDS]}),

            # 6 — доп. «Unscramble»
            ("exact_input", {"items": [
                {"prompt": f"Собери слова из букв: {' '.join(scramble(w) for w in en.split())} ({ru})",
                 "accept": [en], "audio_tts": en}
                for en, ru, f in ACT_WORDS]}),

            # 7 — доп. «Fill in»
            ("exact_input", {"items": [
                {"prompt": f"Впиши пропущенные буквы: {masked(en)} ({ru})",
                 "accept": [en], "image": c(f), "audio_tts": en}
                for en, ru, f in ACT_WORDS]}),

            # 8 — перемычка: приветствие части (2)
            ("text", {"html":
                "<h3>Привет! 👋</h3>"
                "<p>Добро пожаловать во вторую, ДОПОЛНИТЕЛЬНУЮ часть домашнего задания.</p>"
                "<p>Выполни задание, чтобы хорошенько запомнить новые слова! "
                "Выполнив его, ты станешь МЕГА крутым учеником!</p>"}),

            # 9 — бл. 4 части (2)
            ("task", {
                "title": "Дополнительное задание ⭐ Мой отдых на море",
                "needs_review": True,
                "image": c("hw1_drawing_example"),
                "html":
                    "<p>Это ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ — для самых смелых!</p>"
                    "<p><b>Нарисуй свой отдых на море</b> и пришли рисунок сюда. А на уроке "
                    "устно расскажи учителю, чем ты больше всего любишь заниматься на каникулах.</p>"
                    "<p>Уверена, что твой рисунок будет очень красивым. Удачи 💗</p>",
            }),

            # 10
            bye("well_done_star", "Поздравляю! Ты завершил домашнее задание. Ты — МЕГА КРУТ! 🌟",
                "Жду тебя на уроке!"),
        ],
    },

    # ------------------------------------------------------------------ HW2
    "u9_hw2": {
        "unit": U, "unit_title": UNIT, "unit_sort": 9,
        "lesson_title": "Homework 2", "lesson_sort": 1, "kind": "homework",
        # Выгрузка: 12 блоков. Блок 2 (реклама) не перенесён, тексты 3 и 9
        # сведены с соседними заданиями, блоки-«диаграммы» 6 и 7 — в match
        # с кадрами, вырезанными из картинок задания.
        "blocks": [
            # 1
            hello("hello_wave", "Добро пожаловать в домашнее задание!",
                  "В этом уроке тебя ждут интересные упражнения и видео!",
                  "В конце урока есть дополнительное задание — его можно выполнить "
                  "по желанию! Его делают самые смелые и крутые ученики."),

            # 2
            ("text", {"html":
                "<p>Для начала посмотри видеоролик.</p>"
                "<p>В видео подружки решают, чем им заняться. Как думаешь, что предложит "
                "одна из подружек? <i>Listen to music? Look for shells? Paint a picture?</i></p>"
                "<p>Внимательно слушай, что говорят девочки в видео. Потом посмотри видео "
                "ещё раз и повторяй за подружками.</p>"
                + pic("hw2_friends_talk", "Подружки", "420px")}),

            # 3
            ("video", {"title": "Видео: чем займутся подружки?", "url": "", "provider": "file"}),

            # 4
            ("match", {
                "title": "Посмотри видео ещё раз и соедини левый столбик с правым, "
                         "чтобы получились правильные предложения!",
                "pairs": [
                    {"left": "Let’s eat ice cream.", "right": "Good idea!",
                     "right_audio_tts": "Good idea!"},
                    {"left": "Let’s listen to music.", "right": "Sorry, I don’t want to.",
                     "right_audio_tts": "Sorry, I don't want to."},
                    {"left": "Let’s paint a picture.", "right": "I’m not sure.",
                     "right_audio_tts": "I'm not sure."},
                ],
            }),

            # 5 — в выгрузке «Диаграмма»: 4 точки + 2 лишних варианта, но на
            # картинке шесть кадров и лишние подходят к кадрам e и f — соединяем все шесть
            ("match", {
                "title": "Внимательно посмотри на картинки. Соедини предложения с подходящей картинкой.",
                "pairs": [
                    {"left_image": c("hw2_lets_swim"), "right": "Let’s go swimming.",
                     "right_audio_tts": "Let's go swimming."},
                    {"left_image": c("hw2_lets_music"), "right": "Let’s listen to music.",
                     "right_audio_tts": "Let's listen to music."},
                    {"left_image": c("hw2_lets_photo"), "right": "Let’s take a photo.",
                     "right_audio_tts": "Let's take a photo."},
                    {"left_image": c("hw2_lets_paint"), "right": "Let’s paint a picture.",
                     "right_audio_tts": "Let's paint a picture."},
                    {"left_image": c("hw2_lets_park"), "right": "Let’s go to the park.",
                     "right_audio_tts": "Let's go to the park."},
                    {"left_image": c("hw2_lets_shells"), "right": "Let’s look for shells.",
                     "right_audio_tts": "Let's look for shells."},
                ],
            }),

            # 6
            ("match", {
                "title": "Посмотри! Здесь три смайлика. Соедини ответы с подходящим смайликом.",
                "pairs": [
                    {"left_image": c("smile_sorry"), "right": "Sorry, I don’t want to.",
                     "right_audio_tts": "Sorry, I don't want to."},
                    {"left_image": c("smile_not_sure"), "right": "I’m not sure.",
                     "right_audio_tts": "I'm not sure."},
                    {"left_image": c("smile_good_idea"), "right": "Good idea!",
                     "right_audio_tts": "Good idea!"},
                ],
            }),

            # 7
            ("gaps", {
                "title": "Заполни пропуски словами из таблички",
                "mode": "drag",
                "image": c("hw2_beach_umbrella"),
                "text":
                    "1. A: Let's __read__ a book.\nB: Good __idea__!\n"
                    "2. A: Let's __make__ a sandcastle.\nB: __Sorry__, I don't want to!\n"
                    "3. A: Let's __paint__ a picture.\nB: __Good__ idea!\n"
                    "4. A: Let's __catch__ a fish.\nB: I'm not __sure__.",
                "gaps_expected": 8,
            }),

            # 8 — в выгрузке к заданию приложено аудио (плеер пустой, 00:00)
            ("sequence", {
                "title": "Молодец! Осталось немного. Послушай аудио и расставь предложения "
                         "в правильном порядке, чтобы получился диалог.",
                "audio": "",
                "audio_tts": "Let's read a book. Sorry, I don't want to. Let's catch a fish. "
                             "I'm not sure. Let's paint a picture. Good idea!",
                "items": [
                    {"text": "– Let's read a book."},
                    {"text": "– Sorry, I don't want to."},
                    {"text": "– Let's catch a fish."},
                    {"text": "– I'm not sure."},
                    {"text": "– Let's paint a picture."},
                    {"text": "– Good idea!"},
                ],
            }),

            # 9
            ("task", {
                "title": "Дополнительное задание ⭐ Твой диалог",
                "needs_review": True,
                "html":
                    "<p>Здесь тебя ждёт ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ. Это задание для самых смелых учеников!</p>"
                    "<p>В предыдущем упражнении ты расставил предложения в правильном порядке, "
                    "и у тебя получился диалог. Используй его как пример. "
                    "<b>Составь и впиши свой диалог!</b></p>",
            }),

            # 10
            bye("well_done_star", "Поздравляю! Ты завершил домашнее задание, ты молодец! 🌟",
                "Увидимся на занятии!"),
        ],
    },

    # ------------------------------------------------------------------ HW3
    "u9_hw3": {
        "unit": U, "unit_title": UNIT, "unit_sort": 9,
        "lesson_title": "Homework 3", "lesson_sort": 2, "kind": "homework",
        # Выгрузка: 10 блоков. Не перенесены: блок 2 (реклама), картинка-реклама
        # в конце, «робуксы». Блоки 7 и 8 — «Открытый вопрос» → task.
        "blocks": [
            # 1
            hello("hello_book", "Добро пожаловать в домашнее задание!",
                  "Впереди тебя ждут видео и увлекательные упражнения, а также "
                  "одно дополнительное задание, которое можно выполнить по желанию."),

            # 2
            ("text", {"html":
                "<p>Давай начнём с видео. Но прежде чем смотреть, как думаешь, "
                "<b>где спрятался котик (cat)?</b></p>"
                "<p>Теперь посмотри видео один раз, внимательно слушай, что говорит персонаж, "
                "и проверь себя — угадал ли ты?</p>"
                "<p>Затем посмотри видео снова и повторяй за персонажами.</p>"
                + pic("hw3_cat", "Котик", "260px")}),

            # 3
            ("video", {"title": "Видео: где котик?", "url": "", "provider": "file"}),

            # 4
            ("match", {
                "title": "Посмотри видео ещё раз. Соедини вопросы и ответы.",
                "pairs": [
                    {"left": "Where are the candies?", "right": "They’re in the jar.",
                     "right_audio_tts": "They're in the jar."},
                    {"left": "Where’s the rabbit?", "right": "It’s in the hat.",
                     "right_audio_tts": "It's in the hat."},
                    {"left": "Where’s the cat?", "right": "It’s under the table.",
                     "right_audio_tts": "It's under the table."},
                    {"left": "Where are the books?", "right": "They’re in the bag.",
                     "right_audio_tts": "They're in the bag."},
                ],
            }),

            # 5
            ("text", {"html":
                "<p>А теперь посмотри на картинку и соедини вопросы с ответами в следующем задании.</p>"
                + pic("hw3_where_photos", "Книга, ракушки, гитара, рыбы", "560px")}),

            # 6
            ("match", {
                "title": "Соедини вопросы с ответами",
                "pairs": [
                    {"left": "Where are the shells?", "right": "They’re in the box.",
                     "right_audio_tts": "They're in the box."},
                    {"left": "Where’s the guitar?", "right": "It’s on the bed.",
                     "right_audio_tts": "It's on the bed."},
                    {"left": "Where are the fish?", "right": "They’re in the sea.",
                     "right_audio_tts": "They're in the sea."},
                    {"left": "Where’s the book?", "right": "It’s on the table.",
                     "right_audio_tts": "It's on the table."},
                ],
            }),

            # 7
            ("task", {
                "title": "Look and answer · Где что лежит?",
                "needs_review": True,
                "image": c("hw3_bags"),
                "html":
                    "<p>Ты — большой молодец! Посмотри на картинки и впиши ответы на вопросы. "
                    "Первый вопрос — пример, на него уже есть ответ.</p>"
                    "<ol>"
                    "<li>Where’s the blue book? — <i>It’s in the green bag.</i></li>"
                    "<li>Where’s the green lizard?</li>"
                    "<li>Where are the green books?</li>"
                    "<li>Where’s the black spider?</li>"
                    "<li>Where are the red books?</li>"
                    "<li>Where’s the yellow lizard?</li>"
                    "</ol>",
            }),

            # 8
            ("task", {
                "title": "Ask and answer · Где животные?",
                "needs_review": True,
                "image": c("hw3_house"),
                "html":
                    "<p>Посмотри на картинку и впиши вопросы про животных: "
                    "<b>crocodiles, cat, spider, snake</b>. Потом ответь на свои вопросы.</p>"
                    "<p>Пример:<br><i>Where’s the lizard?<br>It’s in the bedroom.</i></p>",
            }),

            # 9
            bye("well_done_clap", "Молодец! Ты справился с домашним заданием 👏",
                "Увидимся на занятии!"),
        ],
    },

    # ------------------------------------------------------------------ HW4
    "u9_hw4": {
        "unit": U, "unit_title": UNIT, "unit_sort": 9,
        "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework",
        # Выгрузка: 13 блоков. Блок 2 (реклама) и блок 6 (битая картинка —
        # зелёная дуга на чёрном) не перенесены; кадры истории (блоки 7, 8)
        # сведены в один текст. «Диаграмма» с 8 перепутанными кадрами (блок 9)
        # → sequence: кадры вырезаны, ученик ставит их по порядку.
        "blocks": [
            # 1
            hello("hello_rocket", "Добро пожаловать в домашнее задание!",
                  "Сегодня мы с тобой послушаем и прочитаем рассказ о наших супердрузьях!",
                  "А в конце тебя ждёт дополнительное задание — видео и задание к нему. "
                  "Оно выполняется по желанию, но ты будешь МЕГА крут, когда справишься с ним!"),

            # 2
            ("text", {"html":
                "<p>Твоё первое задание — послушать запись истории и выполнить задание под аудио.</p>"
                "<p>В этот раз Misty, Thunder, Flash и Whisper решили взобраться на вершину "
                "холма наперегонки. <b>Как думаешь, кто доберётся первым?</b></p>"
                "<p>Послушай аудио и узнай, угадал ли ты.</p>"
                + pic("hw4_flash_running", "Flash", "320px")}),

            # 3 — аудио истории
            ("video", {"title": "Аудио: история «The top of the hill»", "url": "", "provider": "file"}),

            # 4
            ("sequence", {
                "title": "Послушай историю ещё раз и расставь предложения в правильном порядке, "
                         "как они идут в рассказе!",
                "image": c("hw4_friends"),
                "items": [
                    {"text": "A race?"},
                    {"text": "See you at the top of the hill!"},
                    {"text": "I can walk up the hill, but I can't run!"},
                    {"text": "This is the end of the race."},
                    {"text": "Let's go together."},
                    {"text": "What a good idea!"},
                ],
            }),

            # 5
            ("text", {"html":
                "<h3>The top of the hill</h3>"
                "<p>Внимательно прочитай историю и выполни упражнение, которое ты увидишь "
                "сразу после неё.</p>"
                + pic("hw4_story_1", "История, кадры 1–4")
                + pic("hw4_story_2", "История, кадры 5–8")}),

            # 6
            ("sequence", {
                "title": "Смотри! История запуталась, и картинки стоят не по порядку 😱 "
                         "Расставь кадры так, как они идут в истории. Постарайся не подсматривать, "
                         "а в конце проверь себя по тексту.",
                "items": [{"image": c(f"hw4_frame_{n}")} for n in range(1, 9)],
            }),

            # 7
            ("text", {"html":
                "<p>Смотри, наша история ожила и превратилась в мультик! Давай посмотрим его!</p>"
                "<p>Это <b>ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ</b>! Его можно выполнить по желанию, "
                "но ты будешь МЕГА крут, когда справишься с ним!</p>"
                "<p>Посмотри видео и выполни упражнение под ним — вставь пропущенные слова "
                "в предложения.</p>"
                + pic("hw4_video_cover", "Unit 9 · The top of the hill", "420px")}),

            # 8
            ("video", {"title": "Мультфильм «The top of the hill»", "url": "", "provider": "file"}),

            # 9
            ("gaps", {
                "title": "Вставь пропущенные слова в предложения",
                "mode": "drag",
                "text":
                    "Let's __go__.\n"
                    "See you at the __top__ of the hill.\n"
                    "A race is not a __good__ idea.\n"
                    "I can __walk__ up the hill, but I can't __run__.\n"
                    "This is the end of the __race__.\n"
                    "Let's go __together__.\n"
                    "What a good __idea__!",
                "gaps_expected": 8,
            }),

            # 10
            bye("well_done_medal", "Поздравляю! Ты завершил домашнее задание ❤",
                "Ты замечательный ученик! Увидимся на занятии!"),
        ],
    },

    # ------------------------------------------------------------------ HW5
    "u9_hw5": {
        "unit": U, "unit_title": UNIT, "unit_sort": 9,
        "lesson_title": "Homework 5", "lesson_sort": 4, "kind": "homework",
        # Выгрузка: 21 блок. Не перенесены: бл. 1 (фото «hello» с ракушками),
        # бл. 2 (реклама), картинки-«ракушки в коллекцию» (бл. 9, 14, 17, 18)
        # и стоковое фото в прощании (бл. 21). Верно/неверно (бл. 4–8) — один
        # quiz; фото детей заменены картинками тех же занятий без людей
        # (ответы не меняются). «Расставь слова» (бл. 10–13) — четыре order.
        "blocks": [
            # 1 — бл. 3
            hello("hello_book", "Добро пожаловать в домашнее задание!",
                  "Тебя ждут интересные упражнения и 1 ДОПОЛНИТЕЛЬНОЕ задание, которое можно "
                  "выполнить ПО ЖЕЛАНИЮ. Но ты будешь МЕГА КРУТ, когда выполнишь его."),

            # 2 — бл. 4–8. Ответы по картинкам выгрузки: девочка ест мороженое;
            # девочка в наушниках (не читает); семья строит замок; мальчик ловит
            # рыбу (не фотографирует)
            ("quiz", {"title": "Внимательно посмотри на картинку. Прочитай предложение и скажи, "
                               "это правда (True) или неправда (False).", "questions": [
                tf("She is eating ice-cream.", c("hw5_girl_icecream"), True),
                tf("She is reading a book.", c("act_listen_music"), False),
                tf("They are making a sandcastle.", c("act_make_sandcastle"), True),
                tf("He is taking a photo.", c("act_catch_fish"), False),
            ]}),

            # 3–6 — бл. 10–13
            order("She is painting a picture.", ["She", "is", "painting", "a", "picture."],
                  c("act_paint_picture")),
            order("He is taking a photo.", ["He", "is", "taking", "a", "photo."], c("act_take_photo")),
            order("They are looking for shells.", ["They", "are", "looking", "for", "shells."],
                  c("act_look_shells")),
            order("She is reading a book.", ["She", "is", "reading", "a", "book."], c("act_read_book")),

            # 7 — бл. 15, аудио к заданию 8
            ("video", {"title": "Аудио: послушай и узнай, как зовут детей на пляже",
                       "url": "", "provider": "file"}),

            # 8 — бл. 16 «Диаграмма». Кто есть кто — по аудио, которого нет;
            # распределение имён угадано (мальчики Tom, Jim, Bob; девочки Sue, Mia) — в доработку
            ("hotspot", {
                "title": "Послушай аудио и подпиши детей на картинке их именами.",
                "mode": "label", "image": c("hw5_beach_kids"),
                "points": [
                    {"x": 19, "y": 44, "text": "Tom", "audio_tts": "Tom"},
                    {"x": 36, "y": 77, "text": "Jim", "audio_tts": "Jim"},
                    {"x": 50, "y": 64, "text": "Sue", "audio_tts": "Sue"},
                    {"x": 67, "y": 78, "text": "Mia", "audio_tts": "Mia"},
                    {"x": 87, "y": 55, "text": "Bob", "audio_tts": "Bob"},
                ], "extras": []}),

            # 9 — бл. 17–18
            ("text", {"html":
                "<p>Ты большой молодец! Ты выполнил основную часть домашнего задания, класс!</p>"
                "<p>Осталось одно ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ! Его можно выполнить по желанию.</p>"}),

            # 10 — бл. 19–20; в выгрузке к заданию аудио-образец (пустой плеер),
            # образец ниже наш
            ("speaking", {
                "title": "Дополнительное задание ⭐ Что делают на пляже? 🎤",
                "needs_review": True,
                "image": c("hw5_beach_scene"),
                "html":
                    "<p>Посмотри на картинку и запиши аудио, где ты описываешь, чем занимаются "
                    "дети и взрослые.</p>"
                    "<p>Послушай пример: <i>The girl is making a sandcastle.</i></p>"
                    "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>",
                "sample": "",
                "sample_tts": "The girl is making a sandcastle. The boy is swimming. "
                              "The woman is reading a book.",
            }),

            # 11 — бл. 21
            bye("well_done_clap", "Поздравляю! Ты завершил домашнее задание! 👏",
                "Горжусь тобой! Увидимся на занятии!"),
        ],
    },

    # ------------------------------------------------------------------ HW6
    "u9_hw6": {
        "unit": U, "unit_title": UNIT, "unit_sort": 9,
        "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework",
        # Часть (1) — словарный тренажёр на 7 слов (Cards, Remember, Find the
        # definition, Listen), список слов свёрнут: взяты 7 мест из части (2),
        # задания наши (СОСТАВ МОЙ). Приветствия у части (1) нет — наше;
        # приветствие части (2) — перемычка. Картинок к блокам 7–9 (бл. 2–4
        # части (2)) в PDF нет совсем: пейзажи — под листы Л9.1/Л9.2, а
        # «выбери имя по картинке» (дети в разных местах) без картинки не
        # решается — перестроено: имя дано, ученик вписывает место (СОСТАВ МОЙ).
        "blocks": [
            # 1 — наше
            hello("hello_highfive", "Добро пожаловать в домашнее задание!",
                  "Сегодня мы выучим, как по-английски называются места, куда можно поехать "
                  "на каникулы: горы, пляж, озеро, город…",
                  "Выполни все задания, если хочешь выучить тему на все 100!"),

            # 2 — «Cards»
            ("flashcards", {"title": "Запомни слова. Нажми на карточку, чтобы увидеть перевод",
                            "cards": [{"text": en, "translation": ru, "audio_tts": en, "image": c(f)}
                                      for en, ru, f in PLACES]}),

            # 3 — «Remember»
            ("quiz", quiz_ru_to_en(PLACES)),

            # 4 — «Find the definition»
            ("quiz", en_to_ru_quiz(PLACES)),

            # 5 — «Listen»
            ("quiz", listen_quiz(PLACES)),

            # 6 — перемычка: приветствие части (2)
            ("text", {"html":
                "<h3>Отлично! Переходим ко второй части 🙌</h3>"
                "<p>Уверена, что ты хорошо выучил новые слова и готов к следующему этапу!</p>"
                "<p>Тебя ждут увлекательные упражнения. А ещё тебя ждёт ДОПОЛНИТЕЛЬНОЕ задание, "
                "которое ты можешь выполнить по желанию, НО если ты его сделаешь, то будешь "
                "нереально крут!</p>"}),

            # 7
            ("match", {
                "title": "Посмотри на картинки и слова. Соедини пейзажи с их названиями:",
                "pairs": [{"left_image": c(f), "right": en, "right_audio_tts": en}
                          for en, ru, f in PLACES],
            }),

            # 8 — в выгрузке «Диаграмма», точки на картинке; картинки нет
            ("match", {
                "title": "А теперь давай вспомним, чем мы можем заняться в каждом из этих мест. "
                         "Соедини предложения с картинками.",
                "pairs": [
                    {"left_image": c("place_city"), "right": "We can go to shops here.",
                     "right_audio_tts": "We can go to shops here."},
                    {"left_image": c("place_mountains"), "right": "We can climb up here.",
                     "right_audio_tts": "We can climb up here."},
                    {"left_image": c("place_beach"), "right": "We can make a sandcastle here.",
                     "right_audio_tts": "We can make a sandcastle here."},
                    {"left_image": c("place_lake"), "right": "We can go on a boat here.",
                     "right_audio_tts": "We can go on a boat here."},
                    {"left_image": c("place_campsite"), "right": "We can sleep in a tent here.",
                     "right_audio_tts": "We can sleep in a tent here."},
                    {"left_image": c("place_theme_park"), "right": "We can ride on fun things here.",
                     "right_audio_tts": "We can ride on fun things here."},
                    {"left_image": c("place_countryside"), "right": "We can see lots of trees here.",
                     "right_audio_tts": "We can see lots of trees here."},
                ],
            }),

            # 9 — СОСТАВ МОЙ: в выгрузке «выбери имя по картинке», картинки нет
            ("gaps", {
                "title": "Прочитай рассказы ребят и перетащи в пропуск, где каждый из них сейчас.",
                "mode": "drag",
                "text":
                    "My name is Lucy. I’m at a __campsite__. I can sleep here.\n"
                    "My name is Mark. I’m in a __city__. I can take photos here.\n"
                    "My name is Jen. I’m in the __mountains__. I can go skiing here.\n"
                    "My name is Ben. I’m at the __beach__. I can go surfing here.\n"
                    "My name is Tim. I’m in the __countryside__. I can see birds here.",
                "gaps_expected": 5,
            }),

            # 10
            ("gaps", {
                "title": "Ты справился с большей частью задания, ты — большой МОЛОДЕЦ! "
                         "Прочитай о местах, которые я очень люблю, и заполни пропуски.",
                "mode": "drag",
                "text":
                    "I like the __mountains__. I can climb up and __go skiing__ here.\n"
                    "I like the __beach__. I can look for shells and __make a sandcastle__ here.\n"
                    "I like the __campsite__. I can sleep in a tent here.",
                "gaps_expected": 5,
            }),

            # 11
            ("task", {
                "title": "Дополнительное задание для ЧЕМПИОНОВ ⭐",
                "needs_review": True,
                "html":
                    "<p>Его можно выполнить по желанию. <b>Письменно расскажи мне о своих любимых "
                    "местах.</b> Используй мой рассказ из предыдущего упражнения как пример.</p>"
                    "<p><i>I like the … . I can … here.</i></p>",
            }),

            # 12
            bye("well_done_trophy", "Поздравляю! Ты завершил домашнее задание 🏆",
                "Ты замечательный ученик! Лови сердечко ❤ Увидимся на занятии!"),
        ],
    },

    # ------------------------------------------------------------------ HW7
    "u9_hw7": {
        "unit": U, "unit_title": UNIT, "unit_sort": 9,
        "lesson_title": "Homework 7", "lesson_sort": 6, "kind": "homework",
        # Выгрузка: 7 блоков, повторение перед тестом. Бл. 2 — «Найди пару»
        # на слух (9 озвученных кнопок ↔ 9 фраз; девятая карточка пропала на
        # стыке страниц PDF — это eat ice cream, единственное слово словаря,
        # которого нет в списке) → quiz «послушай и выбери». Картинки
        # приветствия и прощания (мальчик, Микки Маус) заменены общими.
        "blocks": [
            # 1
            hello("hello_rocket", "Привет! Как здорово, что ты открыл домашнее задание!",
                  "Сегодня мы повторяем всё перед тестом: лексику, грамматику и не только! "
                  "Ты справишься, я уверен!"),

            # 2 — бл. 2
            ("quiz", listen_quiz(ACT_WORDS, "Соедини фразы с картинкой: послушай и выбери, "
                                            "что прозвучало")),

            # 3 — бл. 3; верные отмечены в выгрузке
            ("quiz", {"title": "Посмотри на картинку. Правда или нет? Выбери True или False",
                      "questions": [
                tf("The boy is reading a book.", c("hw7_boy_guitar"), False),
                tf("The girl is listening to music.", c("hw7_girl_music"), True),
                tf("The boy is catching a fish.", c("hw7_boy_fishing"), True),
            ]}),

            # 4 — бл. 4
            ("gaps", {
                "title": "Заполни пропуски",
                "mode": "drag",
                "text":
                    "1. Let’s __listen__ to music. – Good __idea__!\n"
                    "2. Let’s paint a __picture__. – I’m not __sure__.\n"
                    "3. Let’s __eat__ ice cream. – __Good__ idea!\n"
                    "4. Let’s __catch__ a fish. – __Sorry__, I don’t want to.\n"
                    "5. __Let’s__ look for __shells__. – Good idea!",
                "gaps_expected": 10,
            }),

            # 5 — бл. 5
            ("quiz", {"title": "Выбери правильный ответ.", "questions": [
                q1("Where’s the shell?", ["They’re on the rocks.", "It’s on the rocks."], 1),
                q1("Where are the kites?", ["They aren’t in the box. They’re on the bed.",
                                            "It isn’t in the box. It’s on the bed."], 0),
                q1("Where’s my hat?", ["They aren’t in my bag. They’re on my head!",
                                       "It isn’t in my bag. It’s on my head!"], 1),
            ]}),

            # 6 — бл. 6
            ("speaking", {
                "title": "Где что? 🎤",
                "needs_review": True,
                "image": c("hw7_where_tiles"),
                "html":
                    "<p>Посмотри на картинки. Ответь на вопросы — нажми на микрофон и запиши "
                    "ответ голосом.</p>"
                    "<ol><li>Where is the apple?</li><li>Where are the frogs?</li>"
                    "<li>Where are the pencils?</li><li>Where is the frog?</li>"
                    "<li>Where are the apples?</li><li>Where is the pencil?</li></ol>",
            }),

            # 7 — бл. 7
            bye("well_done_trophy", "Ура! Ты справился! 🏆",
                "Ты отлично подготовился к тесту! Увидимся на уроке! 👋"),
        ],
    },

    # ------------------------------------------------------------------ TEST
    "u9_test": {
        "unit": U, "unit_title": UNIT, "unit_sort": 9,
        "lesson_title": "Unit 9 Test", "lesson_sort": 7, "kind": "test",
        # Выгрузка: 8 блоков; блок 3 (5 «выбери правильный вариант») собран
        # в один quiz, блок 4 (5 «составь предложение») — пять order.
        # В «выбери правильный вариант» верный — основной вариант, остальные
        # — «альтернативные» (сверено по PDF).
        "blocks": [
            # 1 — словарь юнита, в выгрузке «Заполни пропуски» по списку слов
            ("exact_input", {"items": [
                {"prompt": f"Напиши по-английски: {ru}", "accept": [en], "audio_tts": en}
                for en, ru in ACTIVITIES
            ]}),

            # 2 — картинок в выгрузке нет: лист ЛТ9.1
            ("match", {
                "title": "Соедини слова с картинками",
                "pairs": [
                    {"left_image": c("act_paint_picture"), "right": "paint a picture",
                     "right_audio_tts": "paint a picture"},
                    {"left_image": c("act_listen_music"), "right": "listen to music",
                     "right_audio_tts": "listen to music"},
                    {"left_image": c("act_catch_fish"), "right": "catch a fish",
                     "right_audio_tts": "catch a fish"},
                    {"left_image": c("act_take_photo"), "right": "take a photo",
                     "right_audio_tts": "take a photo"},
                    {"left_image": c("act_look_shells"), "right": "look for shells",
                     "right_audio_tts": "look for shells"},
                    {"left_image": c("act_make_sandcastle"), "right": "make a sandcastle",
                     "right_audio_tts": "make a sandcastle"},
                ],
            }),

            # 3
            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                q1("A: Let's listen to music!<br>B: ___ idea.", ["No", "Good", "Thanks"], 1,
                   c("test_listen_music")),
                q1("A: Let's paint a picture!<br>B: I'm not ___.", ["sure", "like it", "good idea"], 0,
                   c("test_palette")),
                q1("A: Where's the book?<br>B: ___ under the bed.", ["It", "They are", "It's"], 2,
                   c("test_book")),
                q1("A: Let's look for shells!<br>B: Sorry, I ___.",
                   ["don't", "want to", "don't want to"], 2, c("test_girl_bucket")),
                q1("A: Where are the birds?<br>B: ___ in the shower.", ["They", "They are", "They is"], 1,
                   c("test_birds")),
            ]}),

            # 4–8
            order("Where is the dog?", ["Where", "is", "the", "dog?"], c("test_dog")),
            order("Where are your pink shoes?", ["Where", "are", "your", "pink shoes?"],
                  c("test_pink_shoes")),
            order("The blue crocodiles are in the bathroom.",
                  ["The blue", "crocodiles", "are", "in", "the bathroom."], c("test_blue_crocodile")),
            order("Let's take a photo!", ["Let's", "take", "a", "photo!"], c("test_selfie")),
            # картинка в выгрузке — фото женщины с руками на голове, не берём
            order("They are on my head.", ["They", "are", "on", "my head."]),

            # 9 — аудио к заданию 10
            ("video", {"title": "Послушай аудио: Бен и его семья проводят выходной на пляже",
                       "url": "", "provider": "file"}),

            # 10 — верные сверены по PDF (у верного нет пустого чекбокса)
            ("quiz", {"title": "Послушай аудио и выбери правильные ответы на вопросы", "questions": [
                q1("What does Ben want to do?",
                   ["swim in the sea", "make a sandcastle", "paint a picture"], 1),
                q1("Where is the bucket?", ["in the bag", "on the chair", "under the towel"], 2),
                q1("Where are the shells?", ["in the bag", "under the towel", "on the chair"], 0),
                q1("What is Dad doing?",
                   ["eating ice cream", "listening to music", "catching a fish"], 2),
                q1("What is Grandma doing?",
                   ["taking a photo", "reading a book", "playing in the sand"], 0),
            ]}),

            # 11
            ("text", {"html":
                "<p>Прочитай открытку Эммы. Потом впиши в пропуски недостающие слова — "
                "<b>только ОДНО слово</b> в каждый пропуск.</p>"
                + pic("test_postcard", "Emma’s Postcard")}),

            # 12
            ("gaps", {
                "title": "Прочитай текст и впиши недостающее слово в пропуски. Только ОДНО слово.",
                "mode": "type",
                "text":
                    "1. Emma and Max __swim__ in the sea every morning.\n"
                    "2. Emma’s shells are in a box __on__ her table.\n"
                    "3. Mum is __under__ the umbrella.\n"
                    "4. Max is __painting__ a picture of the sea.\n"
                    "5. Tomorrow Emma wants to __read__ a book.",
                "gaps_expected": 5,
            }),

            # 13
            ("speaking", {
                "title": "SPEAKING TASK · Part 1 🎤",
                "needs_review": True,
                "image": c("test_beach_scene"),
                "html":
                    "<p>Посмотри на картинку и ответь на вопросы:</p>"
                    "<ol><li>Where are the shells?</li><li>Where is the sandcastle?</li>"
                    "<li>Where is the big boat?</li><li>Where is the bird?</li>"
                    "<li>Where is the snail?</li><li>Where are the fish?</li>"
                    "<li>Where is the kite?</li></ol>"
                    "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>",
            }),

            # 14
            ("speaking", {
                "title": "SPEAKING TASK · Part 2 🎤",
                "needs_review": True,
                "html":
                    "<p>Выбери свои любимые занятия (3–4) и предложи ими заняться.</p>"
                    "<p><i>For example:<br>Let’s fly a kite.<br>Let’s paint a picture.<br>"
                    "Let’s catch the fish.</i></p>"
                    "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>",
            }),
        ],
    },
}
