"""Super Minds 1 · Unit 8 — домашки 1–7 и тест юнита.

Разбор выгрузки и список того, что нужно от методиста, — docs/SM1_разбор_u8.md.
Номера блоков в комментариях — как в редакторе (sort_order + 1).

Блок «Картинка» с рекламой для родителей («Информация для родителей! Мы
дарим 3 бесплатных урока…»), который стоит вторым в каждой домашке
выгрузки, не переносим — это не задание.
"""
from sm1_build import *  # noqa: F401,F403

U = "u8"
UNIT_TITLE = "Unit 8 · My body"


def I(name):
    return img(U, name)


def pic(name, alt="", width="100%"):
    return f'<p><img src="{I(name)}" alt="{alt}" style="max-width:{width}"></p>'


def hello(text, image="hello_wave"):
    return ("text", {"html":
        f'<p><img src="{shared(image)}" alt="" style="height:200px"></p>' + text})


def bye(text, image="well_done_star"):
    return ("text", {"html":
        f'<p><img src="{shared(image)}" alt="" style="height:180px"></p>' + text})


def listen_quiz(words, title="Послушай слово и выбери его"):
    """«Послушай» тренажёра: звучит слово, выбрать его из четырёх.

    Верный вариант ставим на позицию i % 4 — варианты при показе не
    перемешиваются, иначе ребёнок отвечает по месту.
    """
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
                   "image": I(f), "options": [{"text": o} for o in opts], "correct": [pos]})
    return {"questions": qs}


def yn(q, image, yes_text, no_text, yes, yes_first):
    """Вопрос с двумя ответами; yes_first разводит позицию верного."""
    opts = [yes_text, no_text] if yes_first else [no_text, yes_text]
    right = yes_text if yes else no_text
    d = {"q": q, "type": "single", "options": [{"text": o} for o in opts],
         "correct": [opts.index(right)]}
    if image:
        d["image"] = I(image)
    return d


def order(sentence, image=None, chunks=None):
    words = chunks or sentence.split()
    d = {"words": words, "sentence": sentence, "audio_tts": sentence}
    if image:
        d["image"] = I(image)
    return ("order", d)


# Слова юнита. Картинки body_* — будущий лист Л8.1 (плюшевый мишка, у
# которого подсвечена нужная часть тела): людей мы не генерируем.
BODY = [
    ("head", "голова", "body_head"),
    ("fingers", "пальцы рук", "body_fingers"),
    ("hand", "кисть руки", "body_hand"),
    ("knee", "колено", "body_knee"),
    ("leg", "нога", "body_leg"),
    ("toes", "пальцы ног", "body_toes"),
    ("foot", "ступня", "body_foot"),
    ("arms", "руки (от плеча)", "body_arms"),
]

# HW6 (1): в выгрузке у слов вместо перевода заглушка «Определение» —
# переводы с карточки методиста «Vocabulary 2 — Movements» из HW6 (2).
# Картинки — лист Л8.2.
MOVES = [
    ("forwards", "вперёд", "move_forwards"),
    ("backwards", "назад", "move_backwards"),
    ("stretch", "тянуться", "move_stretch"),
    ("sideways", "вбок", "move_sideways"),
    ("step", "шаг", "move_step"),
    ("jump", "прыжок", "move_jump"),
]

# Картинки «умею / не умею» из листа-клипарта HW3 (вырезаны из PDF).
ABILITIES = [
    ("I can't swim.", "ab_cant_swim"),
    ("I can stand on one leg.", "ab_stand_one_leg"),
    ("I can't ride a bike.", "ab_cant_ride_bike"),
    ("I can play football.", "ab_play_football"),
    ("I can skip.", "ab_skip"),
    ("I can't play the piano.", "ab_cant_piano"),
]


def base(n, title, sort, kind="homework"):
    return {"unit": U, "unit_title": UNIT_TITLE, "unit_sort": 8,
            "lesson_title": title, "lesson_sort": sort, "kind": kind}


LESSONS = {}

# ---------------------------------------------------------------- HW1
# Две части одним уроком. (1) — словарный тренажёр на 8 слов («Карточки»,
# «Запомни», «Послушай», «Найди пару»), блоки 1–5. (2) — «дополнительная
# часть» (догружена 07.10.2026), блоки 7–10: карточка Vocabulary — The Body,
# «Нарисуй монстра и расскажи», две игры. Прощание (1) и приветствие (2)
# сведены в перемычку — блок 6.
# Обе игры (2) в выгрузке пустые — открытое окно без содержимого, обложки нет:
# «Соедини слово с картинкой» и «Впиши слова». Собраны по словам урока —
# СОСТАВ МОЙ.
LESSONS["u8_hw1"] = {**base(1, "Homework 1", 0), "blocks": [
    hello("<h2>Добро пожаловать в домашнее задание! 👋</h2>"
          "<p>В этом уроке тебя ждёт много классных упражнений — мы выучим, как "
          "по-английски называются части тела.</p>"
          f'<p><img src="{I("body_teddy")}" alt="" style="max-width:260px"></p>'
          "<p>Выполни все задания, если хочешь выучить тему на все 100!</p>"),
    ("flashcards", {"title": "Запомни слова", "cards": [
        {"text": en, "translation": ru, "audio_tts": en, "image": I(f)} for en, ru, f in BODY]}),
    ("quiz", quiz_ru_to_en(BODY)),
    ("quiz", listen_quiz(BODY)),
    ("match", {"title": "Найди пару: соедини картинку и слово", "pairs": [
        {"left_image": I(f), "right": en, "right_audio_tts": en} for en, ru, f in BODY]}),
    ("text", {"html": f'<p><img src="{shared("hello_wave")}" alt="" style="height:180px"></p>'
              "<h3>Основная часть позади — ты большой молодец! 🎉</h3>"
              "<p>Добро пожаловать в дополнительную часть домашнего задания! Эти задания "
              "можно выполнить по желанию, НО если ты выполнишь их, то будешь нереально "
              "крут!</p>"}),                                                          # 6
    ("text", {"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
              + pic("vocab_body", "Vocabulary — The Body")}),
    ("speaking", {"title": "Мой монстр 🎤",
                  "html": "<p>Нарисуй своего монстра и расскажи, какие у него части тела! "
                          "Я уверена, у тебя получится очень красиво!</p>"
                          "<p><b>Пример:</b> <i>2 legs, 4 arms, 10 teeth.</i></p>",
                  "image": I("monster_draw"), "sample": "",
                  "sample_tts": "2 legs, 4 arms, 10 teeth.", "needs_review": True}),  # 8
    # 9–10. Игры (2), в выгрузке пустые — СОСТАВ МОЙ.
    ("exact_input", {"items": [
        {"prompt": ("Задание для настоящих чемпионов! 🏆 Впиши слова! " if i == 0 else "") + f"Напиши по-английски: {ru}",
         "accept": [en, en.capitalize()], "audio_tts": en}
        for i, (en, ru, f) in enumerate(BODY)]}),                                    # 9
    bye("<h3>Поздравляю! Ты завершил домашнее задание, ты замечательный ученик! 🌟</h3>"
        "<p>За это лови звёздочку :)</p><p>Увидимся на занятии!</p>"),
]}

# ---------------------------------------------------------------- HW2
# Задание «Найди пару» после видео (соедини картинку и предложение: I can
# swim, I can't walk, I can climb trees, I can't fly, I can ski, I can't
# stop) в выгрузке без картинок — левый столбец пустой, «Введите слово».
# Блок не переносим, он в «доработать руками».
LESSONS["u8_hw2"] = {**base(2, "Homework 2", 1), "blocks": [
    hello("<h2>Привет! 👋</h2>"
          "<p>В этом уроке тебя ждут несколько интересных заданий! Выполни все "
          "упражнения, если хочешь выучить тему на все 100!</p>"
          "<p>В конце тебя будет ждать дополнительное задание. Если ты его сделаешь, "
          "то получишь дополнительную ⭐ от учителя!</p>"),
    ("text", {"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
              + pic("grammar_can_cant", "I can / I can't")}),
    ("text", {"html": "<p>Для начала давай посмотрим видео! Как думаешь, каких животных ты "
              "увидишь там?</p><p>Посмотри видео один раз, внимательно слушай и проверь — "
              "угадал ли ты?</p><p>Затем посмотри видео снова и повторяй за животными.</p>"}),
    ("video", {"title": "Видео: что умеют животные?", "url": "", "provider": "file"}),   # 4
    ("hotspot", {
        "title": "Отлично! У меня для тебя есть ещё одно задание! Посмотри внимательно "
                 "на картинку. Соедини предложения с подходящей картинкой!",
        "mode": "label", "image": I("sb_can_cant_kids"),
        "points": [
            {"x": 67, "y": 12, "text": "I can stand on one leg.", "audio_tts": "I can stand on one leg."},
            {"x": 37, "y": 14, "text": "I can't stand on one leg.", "audio_tts": "I can't stand on one leg."},
            {"x": 45, "y": 42, "text": "I can't skip.", "audio_tts": "I can't skip."},
            {"x": 28, "y": 65, "text": "I can skip.", "audio_tts": "I can skip."},
            {"x": 45, "y": 72, "text": "I can't touch my toes.", "audio_tts": "I can't touch my toes."},
            {"x": 77, "y": 89, "text": "I can touch my toes.", "audio_tts": "I can touch my toes."},
        ], "extras": []}),
    # 6. В выгрузке у каждого предложения своя картинка, но в PDF дошла
    # только обрезанная первая — ставим клипарт из HW3 и одну новую (ski).
    ("quiz", {"questions": [
        {"q": "Отлично! Это ещё не всё! Посмотри внимательно на картинку и выбери "
              "правильный вариант.", "type": "single", "image": I("ab_cant_swim"),
         "options": [{"text": "I can swim."}, {"text": "I can't swim."}], "correct": [1]},
        {"q": "Посмотри на картинку и выбери правильный вариант.", "type": "single",
         "image": I("ab_stand_one_leg"),
         "options": [{"text": "I can stand on one leg."}, {"text": "I can't stand on one leg."}],
         "correct": [0]},
        {"q": "Посмотри на картинку и выбери правильный вариант.", "type": "single",
         "image": I("she_cant_skip"),
         "options": [{"text": "I can skip."}, {"text": "I can't skip."}], "correct": [1]},
        {"q": "Посмотри на картинку и выбери правильный вариант.", "type": "single",
         "image": I("ab_can_ski"),
         "options": [{"text": "I can't ski."}, {"text": "I can ski."}], "correct": [1]},
    ]}),
    ("speaking", {"title": "Познакомься с Бобом 🎤",
                  "html": "<p>Давай познакомимся с новым героем! Это — Боб. Он расскажет тебе, "
                          "что он умеет делать! Послушай запись и узнай, что умеет Боб.</p>"
                          "<p>А теперь настала твоя очередь! Расскажи, что ты умеешь делать, "
                          "и запиши свой ответ на платформе!</p>",
                  "sample": "", "needs_review": True}),                                 # 7
    # 8–9. Игры Wordwall, обложки в выгрузке пустые — СОСТАВ МОЙ.
    ("match", {"title": "Ты выполнил все задания из основной части! А это дополнительное "
                        "задание — для настоящих чемпионов! Соедини описание с картинкой.",
               "pairs": [{"left_image": I(f), "right": s, "right_audio_tts": s} for s, f in ABILITIES]}),
    ("quiz", {"questions": [
        {"q": "A fish ___ swim.", "type": "single",
         "options": [{"text": "can"}, {"text": "can't"}], "correct": [0]},
        {"q": "A dog ___ fly.", "type": "single",
         "options": [{"text": "can"}, {"text": "can't"}], "correct": [1]},
        {"q": "A bird ___ fly.", "type": "single",
         "options": [{"text": "can't"}, {"text": "can"}], "correct": [1]},
        {"q": "A fish ___ walk.", "type": "single",
         "options": [{"text": "can't"}, {"text": "can"}], "correct": [0]},
        {"q": "A monkey ___ climb trees.", "type": "single",
         "options": [{"text": "can"}, {"text": "can't"}], "correct": [0]},
    ]}),
    bye("<h3>Ура! Ты справился с домашней работой. Вот твой приз — звезда победителя! ⭐</h3>"
        "<p>Увидимся на занятии!</p>"),
]}

# ---------------------------------------------------------------- HW3
LESSONS["u8_hw3"] = {**base(3, "Homework 3", 2), "blocks": [
    hello("<h2>Добро пожаловать в домашнее задание! 👋</h2>"
          "<p>В этом уроке тебя ждут интерактивные видео и много интересных упражнений!</p>"
          "<p>В конце урока есть дополнительные задания — их можно выполнить по желанию, "
          "но если ты их сделаешь, то получишь дополнительный балл от учителя! ⭐</p>"),
    ("text", {"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
              + pic("grammar_can_you", "Can you …?")}),
    ("text", {"html": "<p>Ура! Мы посмотрим видео! Как думаешь, с какими персонажами ты "
              "познакомишься?</p><p>Для начала посмотри видео один раз, внимательно слушай, "
              "что говорят персонажи.</p><p>Посмотри видео ещё раз и повторяй за персонажами.</p>"}),
    ("video", {"title": "Видео: Can you …?", "url": "", "provider": "file"}),            # 4
    ("match", {"title": "Посмотри видео ещё раз и соедини вопросы и ответы",
               "pairs": [
                   {"left": "Can you swim?", "right": "Yes, I can.", "right_audio_tts": "Yes, I can."},
                   {"left": "Can you fly?", "right": "No, I can't.", "right_audio_tts": "No, I can't."},
               ]}),
    ("hotspot", {
        "title": "У тебя есть ещё одно практическое задание! Внимательно посмотри на картинку. "
                 "Соедини предложения с подходящей картинкой.",
        "mode": "label", "image": I("abilities_sheet"),
        "points": [
            {"x": 16, "y": 25, "text": "I can't swim.", "audio_tts": "I can't swim."},
            {"x": 48, "y": 25, "text": "I can stand on one leg.", "audio_tts": "I can stand on one leg."},
            {"x": 78, "y": 30, "text": "I can't ride a bike.", "audio_tts": "I can't ride a bike."},
            {"x": 14, "y": 75, "text": "I can play football.", "audio_tts": "I can play football."},
            {"x": 37, "y": 75, "text": "I can skip.", "audio_tts": "I can skip."},
            {"x": 75, "y": 78, "text": "I can't play the piano.", "audio_tts": "I can't play the piano."},
        ], "extras": []}),
    ("gaps", {"title": "Молодец! Внимательно прочитай предложения. Посмотри на смайлик перед "
                       "предложением и выбери can или can't",
              "mode": "drag",
              "text": "✗ I __can't__ swim.\n"
                      "✓ He __can__ ride a horse.\n"
                      "✓ She __can__ play tennis.\n"
                      "✗ He __can't__ play the piano.\n"
                      "✓ She __can__ ride a bike.\n"
                      "✓ She __can__ do ballet.",
              "gaps_expected": 6}),
    ("speaking", {"title": "Мой монстрик 🎤",
                  "html": "<p>Посмотри, это мой монстрик! Послушай, что он умеет делать!</p>"
                          "<p>Нарисуй своего монстрика, раскрась и расскажи: что он умеет делать?</p>"
                          "<p><b>Пример:</b> It can jump. It can fly!</p>",
                  "image": I("monster"), "sample": "", "needs_review": True}),              # 8
    # 9–12. Игры Wordwall, обложки пустые — СОСТАВ МОЙ.
    ("quiz", {"questions": [
        {"q": "Ты выполнил все задания из основной части! А это дополнительное задание — "
              "для настоящих чемпионов!<br>Can a fish swim?", "type": "single",
         "options": [{"text": "Yes, it can."}, {"text": "No, it can't."}], "correct": [0]},
        {"q": "Can a dog fly?", "type": "single",
         "options": [{"text": "Yes, it can."}, {"text": "No, it can't."}], "correct": [1]},
        {"q": "Can a bird fly?", "type": "single",
         "options": [{"text": "No, it can't."}, {"text": "Yes, it can."}], "correct": [1]},
        {"q": "Can a penguin fly?", "type": "single",
         "options": [{"text": "No, it can't."}, {"text": "Yes, it can."}], "correct": [0]},
        {"q": "Can a monkey climb trees?", "type": "single",
         "options": [{"text": "Yes, it can."}, {"text": "No, it can't."}], "correct": [0]},
    ]}),
    order("Can you swim?"),
    order("Can you ride a bike?"),
    order("No, I can't play the piano."),
    bye("<h3>Поздравляю! Ты завершил домашнее задание, ты молодец!</h3>"
        "<p>Лови звёздочку! ⭐ Увидимся на занятии!</p>"),
]}

# ---------------------------------------------------------------- HW4
# «Homework 4 (1)» + «(2)» одним уроком. Прощание первой части и
# приветствие второй сведены в перемычку — блок 8. Часть (2) — интерактивное
# видео (2:11) с шестью вопросами по таймкодам; текста вопросов в выгрузке нет.
STORY_PICS = [  # точка на перемешанной картинке → какой это кадр истории
    (62, 75, 1), (12, 25, 2), (37, 25, 3), (12, 75, 4),
    (37, 75, 5), (87, 25, 6), (62, 25, 7), (87, 75, 8),
]
LESSONS["u8_hw4"] = {**base(4, "Homework 4", 3), "blocks": [
    hello("<h2>Привет! 👋</h2>"
          "<p>Добро пожаловать в домашнее задание! Нас сегодня ждёт много интересных "
          "упражнений!</p><p>В конце тебя ждёт интерактивное видео — оно дополнительное, "
          "но ты будешь большой молодец, если справишься с ним!</p>"),
    ("text", {"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
              + pic("story_key_phrases", "The Problem — key phrases")}),
    ("text", {"html": "<p>Сегодня Misty, Flash, Thunder и Whisper подготовили для тебя историю!</p>"
              "<p>Как думаешь, что с ними случилось на этот раз? Послушай историю, прочитай "
              "текст и выполни задания!</p>"}),
    ("video", {"title": "Послушай историю «The Problem»", "url": "", "provider": "file"}),  # 4
    ("text", {"html": "<h3>The Problem</h3>" + pic("story_robot_1_6", "Кадры 1–6")
              + pic("story_robot_7_8", "Кадры 7–8")}),
    ("hotspot", {
        "title": "Картинки перемешались! Давай поможем героям восстановить порядок истории! "
                 "Подпиши каждую картинку: первая картинка истории — «Picture 1», вторая — "
                 "«Picture 2», и так по порядку. Постарайся не подсматривать, а в конце "
                 "проверь себя по тексту.",
        "mode": "label", "image": I("story_robot_shuffled"),
        "points": [{"x": x, "y": y, "text": f"Picture {n}"}
                   for x, y, n in sorted(STORY_PICS, key=lambda t: t[2])],
        "extras": []}),
    ("match", {"title": "Молодец! Вспомни, кто что говорил в истории, и соедини фразу с героем. "
                        "Если нужно, перечитай текст ещё раз!",
               "pairs": [
                   {"left": "Here's the head.", "right": "Whisper", "right_audio_tts": "Whisper"},
                   {"left": "No problem.", "right": "Flash", "right_audio_tts": "Flash"},
                   {"left": "It can't speak.", "right": "Thunder", "right_audio_tts": "Thunder"},
                   {"left": "Robot, can you speak now?", "right": "Misty", "right_audio_tts": "Misty"},
               ]}),
    ("text", {"html": f'<p><img src="{shared("hello_rocket")}" alt="" style="height:180px"></p>'
              "<h3>Поздравляю! Основная часть позади, ты большой молодец! ✨</h3>"
              "<p>А теперь дополнительное задание — интерактивное видео. Внимательно посмотри "
              "видео и выполни все задания в нём. Удачи!</p>"}),
    ("video", {"title": "Интерактивное видео", "url": "", "provider": "file"}),           # 9
    bye("<h3>Ты завершил домашнее задание, ты большой молодец! 🌟</h3>"
        "<p>До встречи на уроке!</p>"),
]}

# ---------------------------------------------------------------- HW5
LESSONS["u8_hw5"] = {**base(5, "Homework 5", 4), "blocks": [
    hello("<h2>Добро пожаловать в домашнее задание! 👋</h2>"
          "<p>Сегодня тебя ждут много интересных историй и задания к ним! Внимательно читай "
          "инструкцию к каждому заданию!</p><p>В конце тебя ждёт дополнительное задание! Его "
          "делать необязательно, но если ты его выполнишь, то будешь супер мега крутым "
          "учеником!</p><p>Let's go!</p>"),
    ("text", {"html": "<p>Начнём с практики!</p><p>Внимательно посмотри на картинку. Прочитай "
              "вопрос и ответь: <b>Yes, he/she/it can</b> или <b>No, he/she/it can't</b>!</p>"}),
    ("quiz", {"questions": [
        yn("Can she skip?", "she_cant_skip", "Yes, she can.", "No, she can't.", False, True),
        yn("Can he touch his toes?", "he_touch_toes", "Yes, he can.", "No, he can't.", True, False),
        yn("Can she dance?", "ab_cat_dance", "Yes, she can.", "No, she can't.", True, True),
        yn("Can he ride his bike?", "ab_bear_cant_ride_bike", "Yes, he can.", "No, he can't.", False, False),
        yn("Can this dog swim?", "ab_dog_swim", "Yes, it can.", "No, it can't.", True, False),
    ]}),
    ("text", {"html": "<p>Ура! Ты справился с первым заданием! А теперь перейдём к следующему…</p>"
              "<p>Посмотри внимательно на картинку и расставь слова в правильном порядке.</p>"}),
    order("He can stand on one leg.", "ab_stand_one_leg"),                                 # 5
    order("He can swim.", "ab_dog_swim"),
    order("She can't ride a horse.", "she_cant_ride_horse"),
    order("He can't play tennis.", "he_cant_play_tennis"),
    ("text", {"html": "<p>Ты такой молодец! Ты выполнил уже два задания. А сейчас тебя ждут "
              "интересные истории.</p><p>Ребята подготовили для тебя рассказ о своих питомцах. "
              "Как думаешь, какие у них домашние животные? Прочитай текст вслух и проверь себя.</p>"
              + pic("pet_forum", "Pet forum")}),
    ("truefalse", {"title": "Отлично! Тебе понравились истории? Прочитай текст ещё раз и ответь: "
                            "верно или неверно?",
                   "statements": [
                       {"text": "Patch can swim.", "correct": True},
                       {"text": "Jazzy is a horse.", "correct": True},
                       {"text": "Jazzy can't skip.", "correct": False},
                   ]}),
    ("speaking", {"title": "Мой питомец 🎤",
                  "html": "<p>Послушай, как я описала своего домашнего животного! Тебе понравился "
                          "мой дружок?</p><p>Настала твоя очередь! Нарисуй своего питомца, опиши "
                          "его и покажи рисунок на уроке.</p><p><b>Пример:</b> I have got a dog. "
                          "His name is Tabby. He can swim and he can play football.</p>",
                  "sample": "", "needs_review": True}),                                 # 11
    # 12–13. Игры Wordwall, обложки пустые — СОСТАВ МОЙ, по тексту форума.
    ("gaps", {"title": "Ты выполнил все задания из основной части! А это дополнительное задание — "
                       "для настоящих чемпионов! Впиши слова can или can't.",
              "mode": "type",
              "text": "Bob is a cat. He __can__ run and jump and he __can__ sing!\n"
                      "Harry's cat __can't__ sing.\n"
                      "Patch is a dog. He __can__ swim and he __can__ play football.\n"
                      "Jazzy is a horse. She __can't__ sing. She __can__ skip.",
              "gaps_expected": 7}),
    ("match", {"title": "Соедини описание с именем питомца",
               "pairs": [
                   {"left": "He's black with one white foot. He can sing!", "right": "Bob",
                    "right_audio_tts": "Bob"},
                   {"left": "He can swim and he can play football.", "right": "Patch",
                    "right_audio_tts": "Patch"},
                   {"left": "She's a big black horse. She can skip.", "right": "Jazzy",
                    "right_audio_tts": "Jazzy"},
               ]}),
    bye("<h3>Поздравляю! Ты завершил домашнее задание! Молодец!</h3>"
        "<p>За прохождение домашнего задания держи ещё одну дополнительную ⭐. "
        "Жду тебя на занятии!</p>"),
]}

# ---------------------------------------------------------------- HW6
# Две части одним уроком. (1) — словарный тренажёр на шесть слов движения
# (forwards, backwards, stretch, sideways, step, jump; задания «Послушай»,
# «Найди пару», «Скрэмбл» ×2, «Введи слова» ×2), блоки 1–6. В (1) у слов
# вместо перевода заглушка «Определение»; переводы взяты с карточки методиста
# «Vocabulary 2 — Movements» из (2): step — шаг, jump — прыжок.
# (2) догружена 07.10.2026, блоки 8–10: карточка, «Соедини описание с
# картинкой», запись голоса. Прощание (1) и приветствие (2) — перемычка, блок 7.
# В «Соедини» у (2) шесть фото детей — фото не берём, картинки с
# животными — лист Л8.5 (move_*_pic).
SCRAMBLE = {"forwards": "w a r d s o f r", "backwards": "s k b a w r d a c",
            "stretch": "t c h e r s t", "sideways": "y s w a s i d e",
            "step": "p e t s", "jump": "m u p j"}
MOVE_SENTENCES = [
    ("He stretches forwards.", "move_he_stretches_forwards"),
    ("She jumps forwards.", "move_she_jumps_forwards"),
    ("She stretches sideways.", "move_she_stretches_sideways"),
    ("She jumps backwards.", "move_she_jumps_backwards"),
    ("He runs sideways.", "move_he_runs_sideways"),
    ("She steps forwards.", "move_she_steps_forwards"),
]
LESSONS["u8_hw6"] = {**base(6, "Homework 6", 5), "blocks": [
    hello("<h2>Добро пожаловать в домашнее задание! 👋</h2>"
          "<p>Сегодня мы выучим слова-движения: вперёд, назад, вбок, шаг, тянуться и "
          "прыжок. Вставай — будем двигаться вместе!</p>"),
    ("flashcards", {"title": "Запомни слова", "cards": [
        {"text": en, "translation": ru, "audio_tts": en, "image": I(f)} for en, ru, f in MOVES]}),
    ("quiz", listen_quiz(MOVES)),
    ("match", {"title": "Найди пару: соедини картинку и слово", "pairs": [
        {"left_image": I(f), "right": en, "right_audio_tts": en} for en, ru, f in MOVES]}),
    ("exact_input", {"items": [
        {"prompt": f"Собери слово из букв: {SCRAMBLE[en]} ({ru})", "accept": [en, en.capitalize()],
         "audio_tts": en} for en, ru, f in MOVES]}),
    ("exact_input", {"items": [
        {"prompt": f"Напиши по-английски: {ru}", "accept": [en, en.capitalize()],
         "image": I(f), "audio_tts": en} for en, ru, f in MOVES]}),
    ("text", {"html": f'<p><img src="{shared("hello_highfive")}" alt="" style="height:180px"></p>'
              "<h3>Отличная работа! Слова выучены 🎉</h3>"
              "<p>Давай продолжим — впереди ещё несколько заданий!</p>"}),          # 7
    ("text", {"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
              + pic("vocab_moves", "Vocabulary 2 — Movements")}),
    ("match", {"title": "Соедини описание с картинкой", "pairs": [
        {"left_image": I(f), "right": t, "right_audio_tts": t} for t, f in MOVE_SENTENCES]}),
    ("speaking", {"title": "Что ты умеешь делать? 🎤",
                  "html": "<p>Нажми на микрофон и расскажи, что ты умеешь делать. Используй "
                          "движения из предыдущего задания.</p>"
                          "<p><b>Пример:</b> <i>I can jump backwards.</i></p>",
                  "sample": "", "sample_tts": "I can jump backwards.",
                  "needs_review": True}),                                             # 10
    bye("<h3>Отличная работа! 🎉</h3><p>Увидимся на занятии! :)</p>"),
]}

# ---------------------------------------------------------------- HW7
LESSONS["u8_hw7"] = {**base(7, "Homework 7", 6), "blocks": [
    hello("<h2>Привет, изобретатель! 👋</h2>"
          "<p>Это последняя домашка перед тестом! Повтори все части тела, I can / I can't и "
          "вопросы Can you…?</p>" + pic("inventors_robot", "", "320px")),
    ("quiz", en_to_ru_quiz(BODY)),                                                          # 2
    ("gaps", {"title": "Посмотри на картинку. Впиши can или can't.",
              "mode": "type", "image": I("animals_can_cant"),
              "text": "1. A penguin __can't__ fly.\n2. A fish __can__ swim.\n"
                      "3. A fish __can't__ walk.\n4. A duck __can__ fly.\n"
                      "5. A duck __can__ swim.\n6. A penguin __can__ walk.",
              "gaps_expected": 6}),
    ("quiz", {"questions": [
        yn("Прочитай вопрос и посмотри на картинку. Выбери правильный ответ.<br>Can he play tennis?",
           "boy_tennis_cook", "Yes, he can.", "No, he can't.", True, True),
        yn("Can he cook?", "boy_tennis_cook", "Yes, he can.", "No, he can't.", False, True),
        yn("Can she dance?", "girl_dance_fly", "Yes, she can.", "No, she can't.", True, False),
        yn("Can she fly?", "girl_dance_fly", "Yes, she can.", "No, she can't.", False, False),
    ]}),
    ("speaking", {"title": "Что ты умеешь? 🎤",
                  "html": "<p>Нажми на микрофон и расскажи, что ты умеешь и не умеешь делать.</p>"
                          "<p><b>Пример:</b> <i>I can swim. I can ride a bike. I can't play "
                          "the piano.</i></p>",
                  "sample_tts": "I can swim. I can ride a bike. I can't play the piano.",
                  "needs_review": True}),
    # 6–9. Игры Wordwall «Super Minds 1 Unit 8 Voc spelling» (Spell the word)
    # и «Unit 8 Can / Can't» (Unjumble) — пересобраны штатными блоками, СОСТАВ МОЙ.
    ("exact_input", {"items": [
        {"prompt": "Ты выполнил все задания из основной части! А это дополнительное задание — "
                   "для настоящих чемпионов! Впиши слово." if i == 0 else "Впиши слово.",
         "image": I(f), "accept": [en, en.capitalize()], "audio_tts": en}
        for i, (en, ru, f) in enumerate(BODY)]}),
    order("I can touch my toes."),
    order("Can you ride a bike?"),
    order("She can't play the piano."),
    bye("<h3>Молодец! Ты готов к тесту! 💪</h3>", "yes_thumb_up"),
]}

# ---------------------------------------------------------------- Test
GAP_LETTERS = [("head", "h _ _ d"), ("fingers", "f _ n g _ r s"), ("hand", "h _ n _"),
               ("knee", "k n _ _"), ("leg", "l _ g"), ("toes", "t _ _ s"),
               ("foot", "f _ _ t"), ("arms", "a _ m s")]
LETTER = (
    "<h3>A Letter from Jake</h3>"
    "<p>Dear Grandma,</p>"
    "<p>Today I am very happy! I have got a new robot! His name is Beep. He is very funny!</p>"
    "<p>Beep has got a big head and small hands. He has got two long arms and two short legs. "
    "He has got eight fingers but he hasn't got toes!</p>"
    "<p>Beep can dance very well! He can jump and he can run fast. But he can't swim — he "
    "doesn't like water. Can he fly? No, he can't! But he can sing funny songs.</p>"
    "<p>My friend Lily is here today. “Can you play football?” she asks Beep. “Yes, I can!” "
    "says Beep. But he can't kick the ball with his feet — they are too small! We all laugh.</p>"
    "<p>I love my robot! Can you come and see him? He can say “Hello” to you!</p>"
    "<p>Love, Jake</p>")

LESSONS["u8_test"] = {**base(8, "Unit 8 Test", 7, "test"), "blocks": [
    ("exact_input", {"items": [
        {"prompt": f"Впиши недостающие буквы — напиши слово целиком: {mask}",
         "image": I(next(f for e, r, f in BODY if e == en)),
         "accept": [en, en.capitalize()], "audio_tts": en} for en, mask in GAP_LETTERS]}),  # 1
    ("match", {"title": "Соедини слова с картинками", "pairs": [
        {"left_image": I(f), "right": w, "right_audio_tts": w} for w, f in [
            ("hand", "body_hand"), ("foot", "body_foot"), ("toes", "body_toes"),
            ("head", "body_head"), ("fingers", "body_fingers"), ("arm", "body_arms")]]}),
    ("quiz", {"questions": [
        {"q": "Заполни пропуск — выбери подходящий вариант:<br>He ___ play the piano.",
         "type": "single", "image": I("t_he_piano"),
         "options": [{"text": "can"}, {"text": "can't"}], "correct": [1]},
        {"q": "He ___ play tennis.", "type": "single", "image": I("t_he_tennis"),
         "options": [{"text": "can't"}, {"text": "can"}], "correct": [0]},
        {"q": "He ___ swim.", "type": "single", "image": I("t_he_swim"),
         "options": [{"text": "can"}, {"text": "can't"}], "correct": [0]},
        {"q": "She ___ dance.", "type": "single", "image": I("t_she_dance"),
         "options": [{"text": "can't"}, {"text": "can"}], "correct": [1]},
        {"q": "She ___ ride a pony.", "type": "single", "image": I("t_she_pony"),
         "options": [{"text": "can't"}, {"text": "can"}], "correct": [0]},
        {"q": "She ___ ride a bike.", "type": "single", "image": I("t_she_bike"),
         "options": [{"text": "can"}, {"text": "can't"}], "correct": [0]},
    ]}),
    order("Can you stand on one leg?", "t_stand_one_leg",
          ["Can", "you", "stand", "on", "one leg?"]),                                       # 4
    order("My dog can play football.", "t_dog_football", ["My dog", "can", "play", "football."]),
    order("I can't touch my toes.", "t_touch_toes", ["I", "can't", "touch", "my toes."]),
    order("Can your cat play the guitar?", "t_cat_guitar", ["Can", "your cat", "play", "the guitar?"]),
    order("Can your sister fly a kite?", "kite_sky", ["Can", "your", "sister", "fly", "a kite?"]),
    ("text", {"html": "<p>Прочитай текст и выбери правильный вариант ответа к каждому вопросу "
              "после текста.</p>" + pic("t_letter_jake", "A Letter from Jake") + LETTER}),     # 9
    ("quiz", {"questions": [
        {"q": "How many fingers has Beep got?", "type": "single",
         "options": [{"text": "ten"}, {"text": "eight"}, {"text": "six"}], "correct": [1]},
        {"q": "What can Beep do?", "type": "single",
         "options": [{"text": "He can swim."}, {"text": "He can fly."}, {"text": "He can dance."}],
         "correct": [2]},
        {"q": "Can Beep play football?", "type": "single",
         "options": [{"text": "No, he can't."}, {"text": "Yes, he can."},
                     {"text": "He doesn't want to."}], "correct": [1]},
        {"q": "Why can't Beep kick the ball?", "type": "single",
         "options": [{"text": "His feet are too small."}, {"text": "His arms are too long."},
                     {"text": "His legs are too short."}], "correct": [0]},
        {"q": "What does Jake want Grandma to do?", "type": "single",
         "options": [{"text": "Buy a robot."}, {"text": "Play football."},
                     {"text": "Come and see Beep."}], "correct": [2]},
    ]}),
    ("video", {"title": "Послушай разговор Лили и Тома о новом роботе", "url": "",
               "provider": "file"}),                                                        # 11
    ("gaps", {"title": "Впиши только ОДНО недостающее слово в пропуски",
              "mode": "type",
              "text": "1. The robot's name is __Bloop__.\n"
                      "2. He's got a __big__ head.\n"
                      "3. He's got __four|4__ arms.\n"
                      "4. He __can't|cant|can not|cannot__ swim.\n"
                      "5. He can __jump__ very high.",
              "gaps_expected": 5}),
    ("speaking", {"title": "SPEAKING TASK 🎤",
                  "html": "<p>Посмотри на картинку и ответь на вопросы:</p>"
                          "<ol><li>Can the girl run?</li><li>Can the boy ride a bike?</li>"
                          "<li>Can the children play football?</li><li>Can the dog fly?</li>"
                          "<li>Can the baby walk?</li></ol>"
                          "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>",
                  "image": I("t_town_scene"), "needs_review": True}),
]}
