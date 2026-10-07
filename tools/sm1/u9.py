"""Super Minds 1 · Unit 9 · Holidays — HW2, HW3, HW4, HW6 и тест юнита.

Выгрузка ShkolaApp, разбор — docs/SM1_разбор_u9_final.md. Homework 1, 5, 7 в
выгрузке нет, номера уроков не сдвигаем (lesson_sort = K - 1). У Homework 6
есть только часть (2); часть (1) — словарный тренажёр — не выгрузилась.

Не перенесено из выгрузки: картинка-реклама для родителей («3 бесплатных
урока», «Новогодний розыгрыш»), «робуксы» за задания, декоративные картинки
(речевой пузырь, Спанч Боб, Скрудж, сломанная зелёная дуга в HW4).

Картинки, которых в выгрузке нет (пейзажи HW6, занятия на пляже в тесте), —
под будущие листы Л9.1, Л9.2, ЛТ9.1; check() на них ругается «нет файла».
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


LESSONS = {
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

    # ------------------------------------------------------------------ HW6
    "u9_hw6": {
        "unit": U, "unit_title": UNIT, "unit_sort": 9,
        "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework",
        # В выгрузке только часть (2), часть (1) (словарный тренажёр) не
        # выгрузилась. Картинок к блокам 2, 3 и 4 в PDF нет совсем: пейзажи
        # — под листы Л9.1/Л9.2, а «выбери имя по картинке» (дети в разных
        # местах) без картинки не решается — перестроено: имя дано, ученик
        # вписывает место (СОСТАВ МОЙ, в доработку).
        "blocks": [
            # 1
            hello("hello_highfive", "Добро пожаловать в домашнее задание!",
                  "Уверена, что ты хорошо выучил новые слова и готов к следующему этапу!",
                  "Сегодня тебя ждут увлекательные упражнения. А ещё тебя ждёт ДОПОЛНИТЕЛЬНОЕ "
                  "задание, которое ты можешь выполнить по желанию, НО если ты его сделаешь, "
                  "то будешь нереально крут!"),

            # 2
            ("match", {
                "title": "Посмотри на картинки и слова. Соедини пейзажи с их названиями:",
                "pairs": [{"left_image": c(f), "right": en, "right_audio_tts": en}
                          for en, ru, f in PLACES],
            }),

            # 3 — в выгрузке «Диаграмма», точки на картинке; картинки нет
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

            # 4 — СОСТАВ МОЙ: в выгрузке «выбери имя по картинке», картинки нет
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

            # 5
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

            # 6
            ("task", {
                "title": "Дополнительное задание для ЧЕМПИОНОВ ⭐",
                "needs_review": True,
                "html":
                    "<p>Его можно выполнить по желанию. <b>Письменно расскажи мне о своих любимых "
                    "местах.</b> Используй мой рассказ из предыдущего упражнения как пример.</p>"
                    "<p><i>I like the … . I can … here.</i></p>",
            }),

            # 7
            bye("well_done_trophy", "Поздравляю! Ты завершил домашнее задание 🏆",
                "Ты замечательный ученик! Лови сердечко ❤ Увидимся на занятии!"),
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
