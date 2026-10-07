"""Super Minds 1 · Unit 6 · My house — уроки из выгрузки ShkolaApp.

HW1 собран из двух частей: «Homework 1 (1)» (словарный тренажёр, в папке юнита)
и «Homework 1 (2)» (догружена 07.10.2026 в корень SM1). HW3, HW5, HW6 — тоже
из догрузки. Есть HW1–HW7 и тест.
Разбор по блокам — docs/SM1_разбор_u6_t3.md.

Картинки комнат (room_*.webp, house_outside) — лист Л6.1, ещё не сгенерирован.
test_books_bedroom и test_park_empty — лист ЛТ6.1 (замена фото с ребёнком
и фото фирменного карта). hw3_rats, hw3_cars, hw3_go_kart — лист Л6.3
(в выгрузке крысы в руках человека, машинки из мультфильма и фирменная модель).
Остальное вырезано из PDF.
"""
from sm1_build import *  # noqa: F401,F403  img, shared

U = "u6"
UNIT_TITLE = "Unit 6 · My house"

ROOMS = [  # (en, ru, файл)
    ("bathroom", "ванная", "room_bathroom"),
    ("bedroom", "спальня", "room_bedroom"),
    ("living room", "гостиная", "room_living_room"),
    ("hall", "коридор", "room_hall"),
    ("dining room", "столовая", "room_dining_room"),
    ("kitchen", "кухня", "room_kitchen"),
    ("stairs", "лестница", "room_stairs"),
    ("cellar", "подвал", "room_cellar"),
]


def rotate_quiz(items, q_text, per_question=4, with_image=False, option_audio=False):
    """Квиз «выбери слово»: верный вариант гуляет по позициям 0..3.

    Варианты при показе не перемешиваются, поэтому позицию верного задаём сами:
    у i-го вопроса верный стоит на месте i % per_question.
    """
    qs = []
    n = len(items)
    for i, (en, ru, f) in enumerate(items):
        wrong = [items[(i + k) % n][0] for k in range(1, per_question)]
        pos = i % per_question
        options = wrong[:pos] + [en] + wrong[pos:]
        q = {"q": q_text, "type": "single", "correct": [pos],
             "options": [({"text": o, "audio_tts": o} if option_audio else {"text": o}) for o in options]}
        if with_image:
            q["image"] = img(U, f)
        else:
            q["audio_tts"] = en
        qs.append(q)
    return {"questions": qs}


def scramble(en, ru, f):
    letters = [c for c in en if c != " "]
    return ("order", {
        "title": f"Собери слово: {ru}" + (" (два слова)" if " " in en else ""),
        "image": img(U, f),
        "words": letters,
        "sentence": " ".join(letters),
        "audio_tts": en,
    })


def hello(name, html):
    return ("text", {"html": f'<p><img src="{shared(name)}" alt="" style="height:200px"></p>' + html})


def bye(name, html):
    return ("text", {"html": f'<p><img src="{shared(name)}" alt="" style="height:180px"></p>' + html})


def base(key, title, sort, kind="homework"):
    return {"unit": U, "unit_title": UNIT_TITLE, "unit_sort": 6,
            "lesson_title": title, "lesson_sort": sort, "kind": kind}


LESSONS = {}

# ---------------------------------------------------------------- Homework 1
# Две части. «(1)» — словарный тренажёр (vocabulary-drilling): 8 слов + задания
# «Запомни», «Послушай», «Найди пару», «Скрэмбл» и тест. «(2)» (догружена) —
# карточка Rooms in the House, запись голосом «назови комнаты своего дома» и
# доп. задание из двух игр («Соедини картинки со словами», «Впиши слова»),
# содержимое игр в выгрузку не попало — СОСТАВ МОЙ. Порядок по содержимому:
# приветствие (1) обещает доп. задание, (2) — «вторая часть домашнего задания».
# Прощание (1) и приветствие (2) сведены в перемычку 15.
# Блок 2 «(2)» — реклама для родителей, не перенесена.
LESSONS["u6_hw1"] = dict(base("u6_hw1", "Homework 1", 0), blocks=[
    hello("hello_wave",
          "<h2>Привет! 👋</h2>"
          "<p>Сейчас мы с тобой выучим все слова, которые разобрали на уроке: комнаты в доме. "
          "Выполни все задания, чтобы выучить слова на 100%!</p>"
          "<p>В конце первой части тебя ждёт тест. А потом — вторая часть и ДОПОЛНИТЕЛЬНОЕ задание. "
          "Его можно выполнить по желанию, но если ты его сделаешь — ты будешь МЕГА КРУТЫМ! "
          "У тебя всё получится. Удачи! ❤</p>"
          f'<p><img src="{img(U, "house_outside")}" alt="" style="max-width:100%;max-height:260px"></p>'),

    ("flashcards", {"title": "Запомни слова. Нажми на карточку, чтобы увидеть перевод", "cards": [
        {"text": en, "translation": ru, "audio_tts": en, "image": img(U, f)} for en, ru, f in ROOMS]}),

    ("quiz", rotate_quiz(ROOMS, "Послушай слово и выбери его.")),

    ("match", {"title": "Найди пару: слово и перевод", "pairs": [
        {"left": en, "right": ru, "left_audio_tts": en} for en, ru, f in ROOMS]}),

    *[scramble(en, ru, f) for en, ru, f in ROOMS],

    ("quiz", rotate_quiz(ROOMS, "Посмотри на картинку и выбери слово.", with_image=True, option_audio=True)),

    ("exact_input", {"items": [
        {"image": img(U, f), "prompt": f"Напиши по-английски: {ru}",
         "accept": [en, en.capitalize()], "audio_tts": en} for en, ru, f in ROOMS]}),

    # 15 — перемычка: прощание (1) + приветствие (2)
    ("text", {"html":
        f'<p><img src="{shared("hello_rocket")}" alt="" style="height:180px"></p>'
        "<h3>Ты выучил все комнаты! 🎉</h3>"
        "<p>Добро пожаловать во вторую часть домашнего задания. "
        "Выполни все задания, чтобы хорошенько запомнить новые слова!</p>"
        "<p>Выполнив это задание, ты станешь МЕГА крутым учеником!</p>"}),

    ("text", {"html":
        "<h3>Давай повторим всё, что выучили с тобой на уроке:</h3>"
        f'<p><img src="{img(U, "card_rooms_vocab")}" alt="Vocabulary — Rooms in the House" style="max-width:100%"></p>'}),

    ("speaking", {"title": "Какие комнаты есть в твоём доме? 🎤",
                  "html": "<p>Запиши аудио, где ты называешь все комнаты, которые есть в твоём доме.</p>"
                          "<p>Послушай пример ответа, а потом нажми на микрофон.</p>"
                          "<p><i>Например: a kitchen, a bathroom, a living room, two bedrooms, a hall.</i></p>",
                  "sample": "",
                  "sample_tts": "In my house there is a kitchen, a bathroom, a living room, two bedrooms and a hall.",
                  "needs_review": True}),

    # Игра «Соедини картинки со словами» — содержимого в выгрузке нет. СОСТАВ МОЙ: комнаты Л6.1.
    ("match", {"title": "⭐ Ты выполнил все задания из основной части! А это дополнительное задание — "
                        "для настоящих чемпионов! Соедини картинки со словами:",
               "pairs": [{"left_image": img(U, f), "right": en, "right_audio_tts": en}
                         for en, ru, f in ROOMS]}),

    # Игра «Впиши слова» — содержимого нет. СОСТАВ МОЙ: комната по картинке, без перевода.
    ("exact_input", {"items": [{"image": img(U, f), "prompt": "⭐ Впиши слово: что это за комната?",
                                "accept": [en, en.capitalize(), f"a {en}", f"the {en}"]}
                               for en, ru, f in ROOMS]}),

    bye("well_done_trophy",
        "<h3>Поздравляю! Ты завершил домашнее задание. Ты — МЕГА КРУТ! 🎉</h3><p>Жду тебя на уроке!</p>"),
])

# ---------------------------------------------------------------- Homework 2
LESSONS["u6_hw2"] = dict(base("u6_hw2", "Homework 2", 1), blocks=[
    hello("hello_book",
          "<h2>Добро пожаловать в домашнее задание!</h2>"
          "<p>В этом уроке тебя ждут интересные упражнения и видео!</p>"
          "<p>В конце урока есть два дополнительных задания — их можно выполнить по желанию! "
          "Их выполняют самые смелые и крутые ученики.</p>"),

    ("text", {"html":
        "<h3>Давай повторим всё, что выучили с тобой на уроке:</h3>"
        f'<p><img src="{img(U, "grammar_there_is_are")}" alt="There’s … / There are …" style="max-width:100%"></p>'}),

    ("video", {"title": "Для начала посмотри видео. В видео девочка описывает свою любимую комнату. "
                        "Как думаешь, какая её любимая комната? Внимательно слушай, что говорит персонаж. "
                        "Посмотри видео ещё раз и повторяй за персонажами.",
               "url": "", "provider": "file"}),

    ("match", {"title": "Посмотри видео ещё раз и соедини левый столбик с правым, "
                        "чтобы получились правильные предложения!",
               "pairs": [
                   {"left": "There is", "right": "one bed.", "right_audio_tts": "There is one bed."},
                   {"left": "There are", "right": "two pillows.", "right_audio_tts": "There are two pillows."},
               ]}),

    ("hotspot", {
        "title": "Давай теперь попрактикуемся! Соедини предложения с картинками. Вперёд! У тебя всё получится ❤",
        "mode": "label",
        "image": img(U, "food_numbered"),
        "points": [
            {"x": 13, "y": 48, "text": "There are 3 bananas.", "audio_tts": "There are three bananas."},
            {"x": 37, "y": 19, "text": "There is a sandwich.", "audio_tts": "There is a sandwich."},
            {"x": 64, "y": 24, "text": "There is a doll.", "audio_tts": "There is a doll."},
            {"x": 84, "y": 46, "text": "There are four apples.", "audio_tts": "There are four apples."},
            {"x": 37, "y": 70, "text": "There are three sausages.", "audio_tts": "There are three sausages."},
            {"x": 62, "y": 75, "text": "There is a dog.", "audio_tts": "There is a dog."},
        ]}),

    ("text", {"html":
        "<h3>Отлично, ты справился с первой частью домашнего задания!</h3>"
        "<p>Настало время следующего задания — внимательно посмотри на картинку. "
        "Под картинкой есть предложения: скажи, правда это (True) или неправда (False). "
        "Ты можешь всегда смотреть на картинку, чтобы проверить себя.</p>"
        f'<p><img src="{img(U, "cats_house")}" alt="" style="max-width:100%"></p>'}),

    ("truefalse", {"title": "Посмотри на картинку и выбери True, если предложение верно, False — если не верно.",
                   "statements": [
                       {"text": "There are two bedrooms in the house.", "correct": True},
                       {"text": "There are three rooms in the house.", "correct": False},
                       {"text": "There are two cats in the kitchen.", "correct": False},
                       {"text": "There are three dogs in the bedroom.", "correct": False},
                       {"text": "There are four cats in the kitchen.", "correct": True},
                   ]}),

    ("text", {"html":
        "<p>Смотри, это рисунок моего домика. Как тебе? Нравится?</p>"
        "<p>Обязательно нарисуй свой дом и покажи мне рисунок на уроке.</p>"
        f'<p><img src="{img(U, "my_house_drawing")}" alt="" style="max-width:100%"></p>'}),

    ("speaking", {"title": "Расскажи про свой дом 🎤",
                  "html": "<p>Посмотри на рисунок, который ты нарисовал. Запиши голосом, какие комнаты ты нарисовал. "
                          "Не забудь использовать <b>there is / there are</b> (послушай пример ответа).</p>"
                          "<p><i>Например: There is a kitchen. There are two bedrooms. There is a bathroom.</i></p>",
                  "sample": "",
                  "sample_tts": "There is a kitchen. There are two bedrooms. There is a bathroom.",
                  "needs_review": True}),

    # Wordwall «Соедини картинки с описанием» — обложка пустая, содержимого нет.
    # СОСТАВ МОЙ: те же предметы, что в «Диаграмме», вырезаны из её картинки.
    ("match", {"title": "⭐ Дополнительное задание для настоящих чемпионов! Соедини картинки с описанием",
               "pairs": [
                   {"left_image": img(U, "food_apples"), "right": "There are four apples.",
                    "right_audio_tts": "There are four apples."},
                   {"left_image": img(U, "food_dog"), "right": "There is a dog.",
                    "right_audio_tts": "There is a dog."},
                   {"left_image": img(U, "food_bananas"), "right": "There are three bananas.",
                    "right_audio_tts": "There are three bananas."},
                   {"left_image": img(U, "food_doll"), "right": "There is a doll.",
                    "right_audio_tts": "There is a doll."},
                   {"left_image": img(U, "food_sausages"), "right": "There are three sausages.",
                    "right_audio_tts": "There are three sausages."},
                   {"left_image": img(U, "food_sandwich"), "right": "There is a sandwich.",
                    "right_audio_tts": "There is a sandwich."},
               ]}),

    # Wordwall «Выбери правильный вариант» — обложка пустая. СОСТАВ МОЙ.
    ("quiz", {"questions": [
        {"q": "___ a bed in the bedroom.", "type": "single",
         "options": [{"text": "There is"}, {"text": "There are"}], "correct": [0]},
        {"q": "___ two pillows on the bed.", "type": "single",
         "options": [{"text": "There is"}, {"text": "There are"}], "correct": [1]},
        {"q": "___ four cats in the kitchen.", "type": "single",
         "options": [{"text": "There is"}, {"text": "There are"}], "correct": [1]},
        {"q": "___ a dog in the hall.", "type": "single",
         "options": [{"text": "There is"}, {"text": "There are"}], "correct": [0]},
        {"q": "___ three bananas on the table.", "type": "single",
         "options": [{"text": "There is"}, {"text": "There are"}], "correct": [1]},
        {"q": "___ a sandwich on the plate.", "type": "single",
         "options": [{"text": "There is"}, {"text": "There are"}], "correct": [0]},
    ]}),

    bye("well_done_star",
        "<h3>Поздравляю! Ты завершил домашнее задание, ты молодец! 🌟</h3><p>Увидимся на занятии!</p>"),
])

# ---------------------------------------------------------------- Homework 3
# «SM1 Unit 6 Homework 3» (догружена). Видео про животных — файла нет.
# Ответы бл. 5 по картинкам: львов три (не пять), мяч большой (не small),
# дракон один, собак четыре. В бл. 6–8 картинки крыс (в руках человека),
# машинок из мультфильма и фирменной модели болида заменены листом Л6.3.
# Бл. 10–11 — две пустые игры «Выбери правильный вариант» — СОСТАВ МОЙ.
# Бл. 12 — реклама розыгрыша, не перенесена.
YN = ["Yes, there is.", "No, there isn't.", "Yes, there are.", "No, there aren't."]


def yn_q(q, correct, image=None, order=(0, 1, 2, 3), intro=""):
    opts = [YN[i] for i in order]
    d = {"q": intro + q, "type": "single", "audio_tts": q,
         "options": [{"text": o} for o in opts], "correct": [opts.index(correct)]}
    if image:
        d["image"] = img(U, image)
    return d


def pick(q, options, correct, image=None):
    d = {"q": q, "type": "single", "options": [{"text": o} for o in options],
         "correct": [options.index(correct)]}
    if image:
        d["image"] = img(U, image)
    return d


LESSONS["u6_hw3"] = dict(base("u6_hw3", "Homework 3", 2), blocks=[
    hello("hello_laptop",
          "<h2>Добро пожаловать в домашнее задание!</h2>"
          "<p>Впереди тебя ждут несколько интересных видео и увлекательных упражнений.</p>"
          "<p>За каждое задание ты будешь получать ⭐ Собери максимальное количество звёздочек "
          "и стань ЧЕМПИОНОМ!</p>"),

    ("text", {"html":
        "<h3>Давай повторим всё, что выучили с тобой на уроке:</h3>"
        f'<p><img src="{img(U, "card_grammar_is_there")}" alt="Is there…? / Are there…?" style="max-width:100%"></p>'}),

    ("video", {"title": "Ура! Мы с тобой посмотрим интересное видео. В этом видео ты увидишь много животных. "
                        "Попробуй угадать, какие животные встретятся тебе в видео? "
                        "Для начала посмотри видео один раз, внимательно слушай, что говорят персонажи. "
                        "Потом посмотри видео ещё раз и повторяй за персонажами.",
               "url": "", "provider": "file"}),

    ("quiz", {"questions": [
        yn_q("Are there five lions?", "No, there aren't.", "hw3_lions", (0, 3, 1, 2),
             intro="Посмотри видео ещё раз и на картинку. Выбери ответ на вопрос. "),
        yn_q("Is there a small ball?", "No, there isn't.", "hw3_ball", (1, 0, 2, 3)),
        yn_q("Is there a dragon?", "Yes, there is.", "hw3_dragon", (1, 3, 0, 2)),
        yn_q("Are there four dogs?", "Yes, there are.", "hw3_dogs", (3, 1, 0, 2)),
    ]}),

    ("quiz", {"questions": [
        pick("Ты посмотрел видео, и сейчас нужно выполнить ещё одно задание. Выбери правильный вариант: "
             "___ there any pears?", ["Are", "Is"], "Are", "test_pears"),
        pick("___ there any rats?", ["Is", "Are"], "Are", "hw3_rats"),
        pick("How many cars ___ there?", ["is", "are"], "are", "hw3_cars"),
        pick("___ there a plane?", ["Is", "Are"], "Is", "test_plane"),
        pick("___ there a go-kart?", ["Are", "Is"], "Is", "hw3_go_kart"),
        pick("How many cakes ___ there?", ["is", "are"], "are", "hw3_cake"),
    ]}),

    ("task", {"title": "Посмотри на картинку и впиши ответы на вопросы ✏️",
              "image": img(U, "hw3_house_rooms"),
              "needs_review": True,
              "html": "<p>Внимательно посмотри на картинку. Впиши ответы на вопросы 1–8. "
                      "Первые три вопроса — примеры, на них уже есть ответы.</p>"
                      "<p><i>How many bedrooms are there? — There are two bedrooms.<br>"
                      "Are there two living rooms? — No, there aren't.<br>"
                      "Is there a bathroom? — Yes, there is.</i></p>"
                      "<ol><li>How many rooms are there?</li><li>Are there two bedrooms?</li>"
                      "<li>Is there a hall?</li><li>Is there a living room?</li><li>Are there 3 rooms?</li>"
                      "<li>Are there 4 bedrooms?</li><li>Is there a dining room?</li><li>Is there a kitchen?</li></ol>"}),

    # Бл. 10 — игра «Выбери правильный вариант», содержимого нет. СОСТАВ МОЙ.
    ("quiz", {"questions": [
        pick("⭐ Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих "
             "чемпионов! Выбери правильный вариант: ___ there a kitchen in the house?", ["Is", "Are"], "Is"),
        pick("___ there any chairs in the dining room?", ["Is", "Are"], "Are"),
        pick("___ there a sofa in the living room?", ["Are", "Is"], "Is"),
        pick("How many bedrooms ___ there?", ["are", "is"], "are"),
        pick("___ there any lizards in the bathroom?", ["Is", "Are"], "Are"),
        pick("___ there a cellar in the house?", ["Are", "Is"], "Is"),
    ]}),

    # Бл. 11 — вторая пустая игра «Выбери правильный вариант». СОСТАВ МОЙ: по картинке дома.
    ("quiz", {"questions": [
        yn_q("Is there a sofa in the living room?", "Yes, there is.", "hw3_house_rooms",
             intro="⭐ Посмотри на картинку дома и выбери правильный ответ. "),
        yn_q("Is there a fridge in the kitchen?", "Yes, there is.", "hw3_house_rooms", (1, 0, 3, 2)),
        yn_q("Are there any cats in the house?", "No, there aren't.", "hw3_house_rooms", (2, 3, 0, 1)),
        yn_q("Is there a car in the kitchen?", "No, there isn't.", "hw3_house_rooms", (3, 2, 1, 0)),
        yn_q("Are there any lamps in the living room?", "Yes, there are.", "hw3_house_rooms", (1, 0, 3, 2)),
    ]}),

    bye("well_done_jump",
        "<h3>Ура, ты справился со всеми заданиями, ты — супер ученик! 💜</h3><p>Увидимся на занятии!</p>"),
])

# ---------------------------------------------------------------- Homework 4
STORY_ORDER = [
    "There's the old house.",
    "Wait for me here.",
    "The stairs to the cellar.",
    "It's cold here.",
    "Yuck! Big spiders!",
    "Wow! Big rats!",
    "There's no problem, you can come in.",
    "Misty, where are you?",
    "Here I am.",
]

LESSONS["u6_hw4"] = dict(base("u6_hw4", "Homework 4", 3), blocks=[
    hello("hello_headphones",
          "<h2>Привет!</h2>"
          "<p>Сегодня мы с тобой послушаем и прочитаем рассказ. А в конце тебя ждёт дополнительное задание, "
          "которое выполняется по желанию. Но ты будешь МЕГА крут, когда справишься с ним!</p>"),

    ("text", {"html":
        "<h3>Давай повторим всё, что выучили с тобой на уроке:</h3>"
        f'<p><img src="{img(U, "story_key_phrases")}" alt="Story — At the House" style="max-width:100%"></p>'}),

    ("text", {"html":
        f'<p><img src="{img(U, "haunted_house")}" alt="" style="height:200px"></p>'
        "<p>Наши супер друзья — Misty, Thunder, Flash и Whisper — отправляются в жуткий дом. "
        "Как думаешь, встретят ли ребята в этом доме привидений?</p>"}),

    ("video", {"title": "Для начала прослушай аудио и выполни задание.", "url": "", "provider": "file"}),

    ("quiz", {"questions": [
        {"q": "Прослушай историю ещё раз. Какие слова из перечисленных упоминаются в истории? "
              "Выбери все верные.", "type": "multiple",
         "options": [{"text": "house"}, {"text": "stairs"}, {"text": "kitchen"},
                     {"text": "cellar"}, {"text": "bedroom"}],
         "correct": [0, 1, 3]},
    ]}),

    ("text", {"html":
        "<p>Внимательно прочитай историю и выполни упражнения.</p>"
        f'<p><img src="{img(U, "story_old_house")}" alt="Story" style="max-width:100%"></p>'}),

    # Номера кадров на картинке закрашены: в выгрузке они стояли прямо на
    # кадрах и выдавали ответ. Точки — в центрах кадров.
    ("hotspot", {
        "title": "Смотри! История запуталась, и картинки стоят не в правильном порядке 😱 "
                 "Соедини картинку и номер: первую картинку истории — с «Picture 1», вторую — с «Picture 2», "
                 "и так по порядку. Постарайся не подсматривать, а в конце можешь проверить себя по тексту.",
        "mode": "label",
        "image": img(U, "story_old_house_shuffled"),
        "points": [
            {"x": 25, "y": 36, "text": "Picture 1"},
            {"x": 75, "y": 87, "text": "Picture 2"},
            {"x": 25, "y": 87, "text": "Picture 3"},
            {"x": 25, "y": 12, "text": "Picture 4"},
            {"x": 75, "y": 12, "text": "Picture 5"},
            {"x": 75, "y": 36, "text": "Picture 6"},
            {"x": 25, "y": 61, "text": "Picture 7"},
            {"x": 75, "y": 61, "text": "Picture 8"},
        ]}),

    ("match", {"title": "Ты запомнил, кто что сказал? Прочитай историю ещё раз и соедини фразы с героями. Удачи ❤",
               "pairs": [
                   {"left": "Go in? No way!", "right": "Flash", "left_audio_tts": "Go in? No way!"},
                   {"left": "It's cold here.", "right": "Misty", "left_audio_tts": "It's cold here."},
                   {"left": "Misty, where are you?", "right": "Whisper", "left_audio_tts": "Misty, where are you?"},
                   {"left": "Careful, Misty.", "right": "Thunder", "left_audio_tts": "Careful, Misty."},
               ]}),

    ("video", {"title": "⭐ ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ. Смотри, наша история ожила и превратилась в мультик! "
                        "Давай посмотрим его и выполним упражнение!",
               "url": "", "provider": "file"}),

    ("sequence", {"title": "Посмотри видео ещё раз. Расставь предложения из видео в правильном порядке:",
                  "items": [{"text": s, "audio_tts": s} for s in STORY_ORDER]}),

    bye("well_done_clap",
        "<h3>Поздравляю!</h3><p>Ты завершил домашнее задание, ты замечательный ученик! ✨</p>"
        "<p>Жду тебя на занятии!</p>"),
])

# ---------------------------------------------------------------- Homework 5
# «SM1 Unit 6 Homework 5» (догружена). Бл. 2 — реклама, не перенесена.
# Бл. 6 «Отметь, какие комнаты показывал герой видео» (a hall, a bedroom,
# a bathroom, a garage, a toilet, a kitchen, a garden, a living room):
# ключа в выгрузке нет (все чекбоксы пустые), видео нет — в урок НЕ положен,
# строка в доработке. Бл. 13–14 — три пустые игры — СОСТАВ МОЙ.
HOUSE_TEXT = ("I live in a nice house. There are 4 rooms. There is a bedroom, a bathroom, "
              "a living room and a kitchen. There isn't a cellar. There isn't a hall. I like my house!")


def order_s(sentence, words, image):
    return ("order", {"title": "Расставь слова в правильном порядке.", "image": img(U, image),
                      "words": words, "sentence": sentence, "audio_tts": sentence})


LESSONS["u6_hw5"] = dict(base("u6_hw5", "Homework 5", 4), blocks=[
    hello("hello_highfive",
          "<h2>Добро пожаловать в домашнее задание!</h2>"
          "<p>Тебя ждут интересные упражнения и увлекательное видео, а также ДОПОЛНИТЕЛЬНОЕ задание, "
          "которое можно выполнить ПО ЖЕЛАНИЮ и получить дополнительные кристаллы 💎</p>"
          "<p>Чтобы стать ЧЕМПИОНОМ — собери все кристаллы, которые ты будешь получать "
          "за выполнение каждого задания.</p>"),

    ("video", {"title": "Сейчас тебе нужно будет посмотреть видео. Герой видео проведёт небольшую экскурсию "
                        "по своему дому. Попробуй угадать, какие комнаты есть у него в доме 🏡",
               "url": "", "provider": "file"}),

    ("text", {"html":
        "<p>Внимательно посмотри на картинку. Под картинкой есть предложения: прочитай их и скажи, "
        "правда это (True) или неправда (False). За задания под картинкой ты можешь заработать 2 💎💎</p>"
        f'<p><img src="{img(U, "hw5_house_attic")}" alt="" style="max-width:100%"></p>'}),

    ("truefalse", {"title": "Посмотри на картинку и выбери True, если предложение верно, False — если не верно.",
                   "statements": [
                       {"text": "There are three rooms in the house.", "correct": False},
                       {"text": "There is a living room.", "correct": True},
                       {"text": "There is a kitchen.", "correct": True},
                       {"text": "There isn't a bathroom.", "correct": False},
                       {"text": "There is a cellar.", "correct": False},
                   ]}),

    ("text", {"html":
        f'<p><img src="{shared("good_luck_clover")}" alt="" style="height:160px"></p>'
        "<p>А в следующем упражнении мы с тобой потренируемся составлять предложения.</p>"
        "<p>Расставь слова в правильном порядке, чтобы получилось предложение. "
        "Тебя ждут 5 таких предложений. Составь их и получи 2 💎💎</p>"}),

    order_s("There are two bedrooms in the house.", ["There", "are", "two", "bedrooms", "in", "the house."],
            "hw5_bedroom"),
    order_s("There isn't a living room.", ["There", "isn't", "a", "living", "room."], "hw5_living_room"),
    order_s("There aren't five bedrooms.", ["There", "aren't", "five", "bedrooms."], "hw5_floorplan"),
    order_s("There is a kitchen.", ["There", "is", "a", "kitchen."], "hw5_kitchen"),
    order_s("How many rooms are there in the house?",
            ["How", "many", "rooms", "are", "there", "in", "the house?"], "hw5_house"),

    ("speaking", {"title": "Прочитай вслух 🎤",
                  "html": "<p>Следующее упражнение оценивается в целых 3 💎💎💎</p>"
                          "<p>Посмотри ещё раз на картинку домика и прочитай его описание. "
                          "Прочитай текст вслух. Запиши себя на диктофон.</p>"
                          "<p><i>I live in a nice house.<br>There are 4 rooms. There is a bedroom, a bathroom, "
                          "a living room and a kitchen. There isn't a cellar. There isn't a hall.<br>"
                          "I like my house!</i></p>",
                  "image": img(U, "hw5_house_attic"),
                  "sample": "", "sample_tts": HOUSE_TEXT,
                  "needs_review": True}),

    ("task", {"title": "Опиши свой дом ✏️",
              "needs_review": True,
              "html": "<p>Здесь тебя ждёт ещё одно задание. За него ты получишь 4 💎💎💎💎</p>"
                      "<p>Опиши свой дом, используя <b>there is / there are / there isn't / there aren't</b>. "
                      "Используй предыдущее упражнение как пример.</p>"
                      "<p>Напиши 5–7 предложений.</p>"
                      "<p>(По желанию можешь нарисовать рисунок своего дома и показать учителю на уроке. "
                      "За рисунок я подарю тебе дополнительный 💎)</p>"}),

    # Бл. 13 — игра «Впиши слова», содержимого нет. СОСТАВ МОЙ: комнаты по картинке и переводу.
    ("exact_input", {"items": [
        {"image": img(U, f), "prompt": f"⭐ Дополнительное задание. Впиши слово: {ru}",
         "accept": [en, en.capitalize(), f"a {en}"]}
        for en, ru, f in ROOMS if en in ("bedroom", "bathroom", "living room", "kitchen", "hall", "cellar")]}),

    # Бл. 14 — две игры «Выбери правильный вариант», содержимого нет. СОСТАВ МОЙ: по картинке домика.
    ("quiz", {"questions": [
        {"q": "⭐ Посмотри на картинку домика и выбери правильный вариант: ___ a bedroom.", "type": "single",
         "image": img(U, "hw5_house_attic"),
         "options": [{"text": "There is"}, {"text": "There are"}, {"text": "There isn't"}], "correct": [0]},
        {"q": "___ a hall.", "type": "single",
         "options": [{"text": "There is"}, {"text": "There isn't"}, {"text": "There aren't"}], "correct": [1]},
        {"q": "___ four rooms.", "type": "single",
         "options": [{"text": "There is"}, {"text": "There isn't"}, {"text": "There are"}], "correct": [2]},
        {"q": "___ any spiders in the kitchen.", "type": "single",
         "options": [{"text": "There aren't"}, {"text": "There isn't"}, {"text": "There is"}], "correct": [0]},
        {"q": "___ a cellar.", "type": "single",
         "options": [{"text": "There are"}, {"text": "There aren't"}, {"text": "There isn't"}], "correct": [2]},
        {"q": "How many rooms are there?", "type": "single",
         "options": [{"text": "There is four rooms."}, {"text": "There are four rooms."},
                     {"text": "There aren't four rooms."}], "correct": [1]},
    ]}),

    bye("well_done_star",
        "<h3>Поздравляю! Ты завершил домашнее задание! Молодец! 💎</h3>"
        "<p>За прохождение домашнего задания держи ещё 1 дополнительный 💎</p><p>Жду тебя на занятии!</p>"),
])

# ---------------------------------------------------------------- Homework 6
# «SM1 Unit 6 Homework 6» (догружена). Тема — виды домов (CLIL Geography).
# Бл. 2 — реклама, не перенесена. Бл. 6 «выбери виды домов, которые звучали в
# видео» (castle, hut, cave house, tree house, igloo, caravan, yurt, boat house):
# ключа нет, видео нет — в урок НЕ положен, строка в доработке.
# Бл. 9 — выпадающие списки: варианты в выгрузку не попали — СОСТАВ ВАРИАНТОВ МОЙ.
HOMES = [  # (en, файл)
    ("tree house", "home_tree"),
    ("house boat", "home_boat"),
    ("yurt", "home_yurt"),
    ("cave house", "home_cave"),
]

LESSONS["u6_hw6"] = dict(base("u6_hw6", "Homework 6", 5), blocks=[
    hello("hello_wave",
          "<h2>Привет!</h2>"
          "<p>Сегодня мы узнаем о разных домах. Тебя ждут интересные увлекательные упражнения и видео.</p>"),

    ("text", {"html":
        "<h3>Давай повторим всё, что выучили с тобой на уроке:</h3>"
        f'<p><img src="{img(U, "card_types_of_homes")}" alt="Types of Homes" style="max-width:100%"></p>'}),

    ("video", {"title": "Посмотри видео и выполни задание под ним. В этом видео Сэм путешествует по всему миру "
                        "и узнаёт о различных видах домов. А где живёшь ты?",
               "url": "", "provider": "file"}),

    ("match", {"title": "А теперь давай вспомним названия домиков, которые мы выучили на уроке. "
                        "Соедини название с картинкой.",
               "pairs": [{"left_image": img(U, f), "right": f"It's a {en}.", "right_audio_tts": f"It's a {en}."}
                         for en, f in HOMES]}),

    ("gaps", {"title": "Молодец, ты справился с большей частью заданий! А теперь прочитай текст и заполни пропуски.",
              "mode": "drag", "image": img(U, "homes_many"),
              "text": "1) My house is in water. I live in a __house boat__.\n"
                      "2) My house is in a tree. I live in a __tree house__.\n"
                      "3) My house is round. I live in a __yurt__.\n"
                      "4) My house is in a cave. I live in a __cave house__.",
              "gaps_expected": 4}),

    # Бл. 9 — выпадающие списки, вариантов в выгрузке нет. Варианты мои, ответ — по фото:
    # пещерный дом, в кадре спальня и ванна, кухни нет.
    ("quiz", {"questions": [
        {"q": "Посмотри! Я очень хочу побывать в этом доме. Прочитай его описание и выбери правильный вариант "
              "для каждого пропуска.<br>Look! It's a ___.", "type": "single", "image": img(U, "cave_house_room"),
         "options": [{"text": "tree house"}, {"text": "cave house"}, {"text": "house boat"}, {"text": "yurt"}],
         "correct": [1]},
        {"q": "There are ___ rooms.", "type": "single", "image": img(U, "cave_house_room"),
         "options": [{"text": "two"}, {"text": "five"}, {"text": "ten"}], "correct": [0]},
        {"q": "It has got a ___ and a bathroom.", "type": "single", "image": img(U, "cave_house_room"),
         "options": [{"text": "kitchen"}, {"text": "garden"}, {"text": "bedroom"}], "correct": [2]},
        {"q": "It hasn't got a ___.", "type": "single", "image": img(U, "cave_house_room"),
         "options": [{"text": "bedroom"}, {"text": "kitchen"}, {"text": "bathroom"}], "correct": [1]},
    ]}),

    ("speaking", {"title": "Мой домик мечты 🎤",
                  "html": "<p>Ура! Осталось всего 1 задание.</p>"
                          "<p>Выбери один из домиков, которые мы сегодня выучили. Может быть тот, который тебе "
                          "больше всего понравился, в котором ты бы хотел жить или просто побывать. "
                          "Нарисуй его, нажми на микрофон и опиши. Используй предыдущее задание как пример.</p>"
                          "<p><i>Look! It's a tree house. There are two rooms. It has got a bedroom and a bathroom. "
                          "It hasn't got a kitchen. I like it!</i></p>",
                  "image": img(U, "homes_four"),
                  "sample": "",
                  "sample_tts": "Look! It's a tree house. There are two rooms. It has got a bedroom and a bathroom. "
                                "It hasn't got a kitchen. I like it!",
                  "needs_review": True}),

    bye("well_done_smiley",
        "<h3>Поздравляю! Ты завершил домашнее задание, ты замечательный ученик!</h3>"
        "<p>За это лови звёздочку ⭐</p><p>Увидимся на занятии!</p>"),
])

# ---------------------------------------------------------------- Homework 7
THERE = "There’s|There's|There is"
THERE_ARE = "There are"

LESSONS["u6_hw7"] = dict(base("u6_hw7", "Homework 7", 6), blocks=[
    hello("hello_rocket",
          "<h2>Привет, исследователь старого дома!</h2>"
          "<p>Это последняя домашка перед тестом! Повтори все комнаты, "
          "<b>There’s / There are</b> и вопросы <b>Is there / Are there</b>.</p>"),

    ("quiz", {"questions": [
        {"q": "Посмотри на картинку и выбери правильное слово.", "type": "single",
         "image": img(U, "room_cellar_hw7"),
         "options": [{"text": "bedroom"}, {"text": "bathroom"}, {"text": "kitchen"}, {"text": "cellar"}],
         "correct": [3]},
        {"q": "Посмотри на картинку и выбери правильное слово.", "type": "single",
         "image": img(U, "room_hall_hw7"),
         "options": [{"text": "hall"}, {"text": "dining room"}, {"text": "bathroom"}, {"text": "living room"}],
         "correct": [0]},
        {"q": "Посмотри на картинку и выбери правильное слово.", "type": "single",
         "image": img(U, "room_stairs_hw7"),
         "options": [{"text": "kitchen"}, {"text": "stairs"}, {"text": "bedroom"}, {"text": "hall"}],
         "correct": [1]},
        {"q": "Посмотри на картинку и выбери правильное слово.", "type": "single",
         "image": img(U, "room_dining_hw7"),
         "options": [{"text": "cellar"}, {"text": "kitchen"}, {"text": "dining room"}, {"text": "living room"}],
         "correct": [2]},
    ]}),

    ("gaps", {"title": "Впиши There’s или There are.", "mode": "type",
              "text": f"1. __{THERE}__ a spider in the cellar.\n"
                      f"2. __{THERE_ARE}__ three fish in the hall.\n"
                      f"3. __{THERE}__ a monster in the bedroom.\n"
                      f"4. __{THERE_ARE}__ two cats in the living room.\n"
                      f"5. __{THERE_ARE}__ four mice in the dining room.\n"
                      f"6. __{THERE}__ a bat in the bathroom.",
              "gaps_expected": 6}),

    ("quiz", {"questions": [
        {"q": "Is there a bath in the kitchen?", "type": "single", "audio_tts": "Is there a bath in the kitchen?",
         "options": [{"text": "Yes, there is."}, {"text": "No, there isn’t."}, {"text": "Yes, there are."}],
         "correct": [1]},
        {"q": "Is there a bed in the bedroom?", "type": "single", "audio_tts": "Is there a bed in the bedroom?",
         "options": [{"text": "No, there isn’t."}, {"text": "Yes, there are."}, {"text": "Yes, there is."}],
         "correct": [2]},
        {"q": "Is there a fridge in the bathroom?", "type": "single",
         "audio_tts": "Is there a fridge in the bathroom?",
         "options": [{"text": "No, there isn’t."}, {"text": "Yes, there is."}, {"text": "Yes, there are."}],
         "correct": [0]},
    ]}),

    ("order", {"title": "Слова перепутаны! Составь правильное предложение.",
               "words": ["Is", "there", "a cat", "in", "the kitchen?"],
               "sentence": "Is there a cat in the kitchen?",
               "audio_tts": "Is there a cat in the kitchen?"}),
    ("order", {"title": "Составь правильное предложение.",
               "words": ["There", "are", "three", "cats", "in", "the hall."],
               "sentence": "There are three cats in the hall.",
               "audio_tts": "There are three cats in the hall."}),
    ("order", {"title": "Составь правильное предложение.",
               "words": ["Are", "there", "any", "spiders", "in", "the bathroom?"],
               "sentence": "Are there any spiders in the bathroom?",
               "audio_tts": "Are there any spiders in the bathroom?"}),

    ("speaking", {"title": "Расскажи, что ты видишь 🎤",
                  "html": "<p>Посмотри на картинку. Нажми на микрофон и расскажи, что ты видишь (5–7 предложений).</p>"
                          "<p><i>Пример: There is a house. There are 5 rooms. There is a bedroom. "
                          "There is a bed in the bedroom.</i></p>",
                  "image": img(U, "house_rooms"),
                  "sample_tts": "There is a house. There are five rooms. There is a bedroom. There is a bed in the bedroom.",
                  "needs_review": True}),

    # Wordwall «SM1 U6 matching» (Match up) — содержимого нет. СОСТАВ МОЙ: комнаты Л6.1.
    ("match", {"title": "⭐ Дополнительное задание для настоящих чемпионов! Соедини картинку со словом",
               "pairs": [{"left_image": img(U, f), "right": en, "right_audio_tts": en}
                         for en, ru, f in ROOMS]}),

    # Wordwall «SM1 U6 there is / there are» (Quiz) — содержимого нет. СОСТАВ МОЙ.
    ("quiz", {"questions": [
        {"q": "___ a monster in the cellar.", "type": "single",
         "options": [{"text": "There’s"}, {"text": "There are"}], "correct": [0]},
        {"q": "___ two beds in the bedroom.", "type": "single",
         "options": [{"text": "There’s"}, {"text": "There are"}], "correct": [1]},
        {"q": "___ there a sofa in the living room? — Yes, there is.", "type": "single",
         "options": [{"text": "Are"}, {"text": "Is"}], "correct": [1]},
        {"q": "___ there any spiders in the hall? — No, there aren’t.", "type": "single",
         "options": [{"text": "Are"}, {"text": "Is"}], "correct": [0]},
        {"q": "Is there a bath in the bathroom?", "type": "single",
         "options": [{"text": "Yes, there is."}, {"text": "Yes, there are."}], "correct": [0]},
        {"q": "Are there any chairs in the dining room?", "type": "single",
         "options": [{"text": "Yes, there is."}, {"text": "Yes, there are."}], "correct": [1]},
    ]}),

    bye("well_done_medal",
        "<h3>Ты повторил все комнаты, There’s / There are и вопросы.</h3>"
        "<p>Молодец! Ты готов к тесту! 🏆</p>"),
])

# ---------------------------------------------------------------- Unit 6 Test
LESSONS["u6_test"] = dict(base("u6_test", "Unit 6 Test", 7, kind="test"), blocks=[
    # Блок 1 выгрузки — словарный тест «Заполни пропуски» по 8 словам юнита.
    ("exact_input", {"items": [
        {"prompt": f"Напиши по-английски: {ru}", "accept": [en, en.capitalize()]} for en, ru, f in ROOMS]}),

    # Блок 2 «Соедини слова с картинками»: в выгрузке справа пусто, картинок нет —
    # ставим карточки комнат Л6.1.
    ("match", {"title": "Соедини слова с картинками",
               "pairs": [{"left_image": img(U, f), "right": en}
                         for en, ru, f in ROOMS if en in
                         ("bedroom", "living room", "kitchen", "dining room", "bathroom", "hall")]}),

    # Блок 3 «Выбери правильный вариант» (выпадающие списки) — у нас квиз,
    # варианты на два пропуска даём парой.
    ("quiz", {"questions": [
        {"q": "A: ___ there any pears in the fridge?<br>B: Yes, there ___.", "type": "single",
         "image": img(U, "test_pears"),
         "options": [{"text": "Is … is"}, {"text": "Are … are"}, {"text": "Is … isn't"}, {"text": "Are … aren't"}],
         "correct": [1]},
        {"q": "There ___ a lizard in the bedroom.", "type": "single",
         "image": img(U, "test_lizard"),
         "options": [{"text": "is"}, {"text": "are"}, {"text": "got"}],
         "correct": [0]},
        {"q": "A: How many planes ___?<br>B: There ___ one plane.", "type": "single",
         "image": img(U, "test_plane"),
         "options": [{"text": "is there … are"}, {"text": "have got … is"}, {"text": "are there … is"},
                     {"text": "are there … are"}],
         "correct": [2]},
        {"q": "A: ___ there a crocodile in the picture?<br>B: No, there ___.", "type": "single",
         "image": img(U, "test_crocodile"),
         "options": [{"text": "Has … hasn't"}, {"text": "Are … aren't"}, {"text": "Is … aren't"},
                     {"text": "Is … isn't"}],
         "correct": [3]},
        {"q": "A: ___ there any bikes?<br>B: No, there ___.", "type": "single",
         "image": img(U, "test_bikes"),
         "options": [{"text": "Are … aren't"}, {"text": "Is … isn't"}, {"text": "Do … haven't"},
                     {"text": "Are … isn't"}],
         "correct": [0]},
    ]}),

    ("order", {"title": "Расставь слова в правильном порядке.", "image": img(U, "test_frog_piano"),
               "words": ["There", "is", "a", "frog", "on", "the piano."],
               "sentence": "There is a frog on the piano."}),
    ("order", {"title": "Расставь слова в правильном порядке.", "image": img(U, "test_dogs"),
               "words": ["How", "many", "dogs", "are", "there?"],
               "sentence": "How many dogs are there?"}),
    ("order", {"title": "Расставь слова в правильном порядке.", "image": img(U, "test_kitten_kitchen"),
               "words": ["Is", "there", "a", "cat", "in", "the kitchen?"],
               "sentence": "Is there a cat in the kitchen?"}),
    ("order", {"title": "Расставь слова в правильном порядке.", "image": img(U, "test_park_empty"),
               "words": ["There", "aren't", "any", "go-karts", "in the park."],
               "sentence": "There aren't any go-karts in the park."}),
    # В выгрузке «Are there any book in the bedroom?» — опечатка, исправлено на books.
    ("order", {"title": "Расставь слова в правильном порядке.", "image": img(U, "test_books_bedroom"),
               "words": ["Are", "there", "any", "books", "in the bedroom?"],
               "sentence": "Are there any books in the bedroom?"}),

    # Блок 5: в выгрузке есть лишнее слово «are» в банке — у gaps банка
    # лишних слов нет, поэтому оно не переносится.
    ("gaps", {"title": "Прочитай текст и перетащи слова в пропуски.", "mode": "drag",
              "text": "This is Ben's house. It is old and very big. There are six rooms!\n"
                      "Ben's favourite room is the __kitchen__. He loves food! There's a big table and there "
                      "are five chairs. There's a fridge and a cat! The cat is under the table.\n"
                      "Upstairs, there's Ben's __bedroom__. There's a bed, a desk, and two lamps. "
                      "There are lots of books on the desk. Ben reads every night!\n"
                      "There are __three__ bathrooms — one upstairs and two downstairs. "
                      "That's a lot of bathrooms!\n"
                      "Outside, there's a beautiful __garden__. There are four trees, lots of flowers, "
                      "and a little pond with fish!\n"
                      "But there __isn't__ a living room. That's OK — Ben and his family sit in the kitchen together!",
              "gaps_expected": 5}),

    # Блок 6 — аудио диалога Тома и Сары: у «Верно / неверно» нет поля
    # для звука, поэтому аудио отдельным блоком перед утверждениями.
    ("video", {"title": "Послушай диалог Тома и Сары: Том пришёл к Саре в гости.", "url": "", "provider": "file"}),
    ("truefalse", {"title": "Прочитай предложения и отметь — True (верно) или False (неверно).",
                   "statements": [
                       {"text": "The kitchen is big.", "correct": False},
                       {"text": "There are four chairs in the kitchen.", "correct": True},
                       {"text": "There's a television in the living room.", "correct": False},
                       {"text": "There are books in the bedroom.", "correct": True},
                       {"text": "There is a garden.", "correct": True},
                   ]}),

    ("speaking", {"title": "SPEAKING TASK 🎤",
                  "html": "<p>Посмотри на картинку. Опиши, кого ты видишь (используй <b>there is / there are</b>).</p>"
                          "<p><i>For example: There are two boys. There is one dog. There is a frog on the bag.</i></p>"
                          "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>",
                  "image": img(U, "test_fishing_scene"),
                  "needs_review": True}),
])
