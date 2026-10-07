"""Super Minds 1 · Unit 5 · My week — HW4, HW5, HW6, HW7 и тест юнита.

Выгрузка ShkolaApp, разбор — docs/SM1_разбор_u5_t1_t2.md. Homework 1–3 уже в
базе (на base64, не трогаем; догруженный в корень SM1 «Unit 5 Homework 1» не
собираем). Homework 5 — из догрузки 07.10.2026 (lesson_sort = K - 1).

Картинки занятий (act_*) — листы Л5.1 и ЛТ5.1: в HW6 и в тесте у «соедини
картинку с фразой» картинок в выгрузке нет совсем, а в «Составь предложение»
теста три картинки — фото детей, их не берём. Кадры мультфильма «We're lost!»
(story_*), карточки методиста (card_*) и клипарт теста (t_*) вырезаны из PDF.
Реклама для родителей («3 бесплатных урока») не перенесена нигде.
"""
from sm1_build import *

U = "u5"
UNIT = "Unit 5 · My week"


def c(name):
    return img(U, name)


def pic(name, width=None):
    style = f"max-width:{width}px;width:100%" if width else "max-width:100%"
    return f'<p><img src="{c(name)}" alt="" style="{style}"></p>'


def single(q, options, correct, image=None):
    d = {"q": q, "type": "single", "options": [{"text": o} for o in options], "correct": [correct]}
    if image:
        d["image"] = image
    return d


def order(sentence, words, image=None, title="Расставь слова в правильном порядке"):
    d = {"title": title, "words": words, "sentence": sentence, "audio_tts": sentence}
    if image:
        d["image"] = image
    return ("order", d)


DAYS = [
    ("Monday", "понедельник"),
    ("Tuesday", "вторник"),
    ("Wednesday", "среда"),
    ("Thursday", "четверг"),
    ("Friday", "пятница"),
    ("Saturday", "суббота"),
    ("Sunday", "воскресенье"),
]

# go + -ing (HW6). Порядок — как в «Найди пару» выгрузки.
GO_SPORTS = [
    ("go swimming", "заниматься плаванием", "act_go_swimming"),
    ("go climbing", "заниматься скалолазанием", "act_go_climbing"),
    ("go running", "заниматься бегом", "act_go_running"),
    ("go sledging", "кататься на санках", "act_go_sledging"),
    ("go surfing", "заниматься серфингом", "act_go_surfing"),
    ("go skiing", "кататься на лыжах", "act_go_skiing"),
]

STORY_LOST = (
    "<p><b>1.</b> <b>Misty:</b> Where’s the lake? <b>Flash:</b> I don’t know. "
    "<b>Thunder:</b> We’re lost!<br>"
    "<b>2.</b> <b>Whisper:</b> I’ve got an idea. <b>Flash:</b> What?<br>"
    "<b>3.</b> <b>Whisper:</b> Wait and see. <b>Thunder:</b> This isn’t much fun.<br>"
    "<b>4.</b> <b>Whisper:</b> Rabbit, we’re lost. Where’s the lake? <b>Rabbit:</b> Come with me.<br>"
    "<b>5.</b> <b>Whisper:</b> Thank you very much. <b>Thunder:</b> Here you are, Rabbit.<br>"
    "<b>6.</b> <b>Rabbit:</b> Yippee! <b>Whisper:</b> Watch out!<br>"
    "<b>7.</b> <b>Whisper:</b> Are you OK, Rabbit?<br>"
    "<b>8.</b> <b>Rabbit:</b> Now, I’m lost! <b>Whisper:</b> Now, he’s lost!</p>"
)


LESSONS = {
    # ------------------------------------------------------------------ HW4
    "u5_hw4": {
        "unit": U, "unit_title": UNIT, "unit_sort": 5,
        "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework",
        # «Homework 4 (1)» — 12 блоков, «(2)» — интерактивное видео на Rutube
        # («SM2ed Animated story video L1 U5», 1:44) с 7 вопросами по таймкодам.
        # Прощание (1) и приветствие (2) сведены в перемычку 9. Вопросы
        # интерактивного видео в выгрузку не попали — ставим само видео.
        # Блок 1 выгрузки «(1)» — реклама для родителей, не перенесена.
        "blocks": [
            # 1
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>Добро пожаловать в домашнюю работу!</h2>"
                "<p>Здесь тебя ждут задания по истории, которую мы обсуждали на уроке. "
                "Будет очень-очень интересно.</p>"
                "<p>В конце тебя ждёт вторая часть — интерактивное видео. Делать его "
                "необязательно, но если у тебя получится его выполнить, ты будешь супер крут 😀</p>"}),

            # 2
            ("text", {"html":
                "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
                + pic("card_lost_phrases") + pic("card_phonics_u")}),

            # 3
            ("text", {"html":
                "<p>Прежде чем мы послушаем и прочитаем текст, попробуй вспомнить — "
                "<b>куда шли ребята:</b> <i>lake</i> (озеро), <i>forest</i> (лес), "
                "<i>river</i> (речка)?</p>"
                "<p>Прочитай и прослушай текст — правильно ли ты угадал?</p>"
                + pic("story_lost_forest", 567)}),

            # 4 — аудио истории (в выгрузке «Медиафайл» без файла)
            ("video", {"title": "Послушай историю «We’re lost!» 🎧", "url": "", "provider": "file"}),

            # 5
            ("text", {"html": pic("story_lost_comic", 630) + STORY_LOST}),

            # 6
            ("quiz", {"questions": [{
                "q": "Отлично! А теперь прочитай, послушай и выбери предложения, которые "
                     "произнёс зайчик 🐰",
                "type": "multiple",
                "options": [{"text": t, "audio_tts": t} for t in [
                    "Now, he’s lost.", "Yippee!", "Here you are.",
                    "Come with me.", "Now, I’m lost.", "Wait and see."]],
                "correct": [1, 3, 4],
            }]}),

            # 7 — «Выбери правильный вариант», три предложения с кадрами
            ("quiz", {"title": "Давай вспомним то, что говорили ребята в этой истории. "
                               "Выбери правильный ответ.",
                      "questions": [
                          single("Where’s the ___?", ["frog", "lake"], 1, c("story_lost_flash")),
                          single("Wait and ___.", ["see", "swim"], 0, c("story_lost_whisper")),
                          single("Are you OK, ___?", ["Misty", "rabbit"], 1, c("story_lost_rabbit")),
                      ]}),

            # 8
            ("match", {
                "title": "Класс! Все задания выполнены просто отлично. Давай сделаем ещё одно? "
                         "Соедини вопросы с ответами. Похожие фразы встречались тебе в тексте — "
                         "можешь заглянуть туда, чтобы понять, что они означают.",
                "pairs": [
                    {"left": "Where’s my bag?", "right": "I don’t know.",
                     "right_audio_tts": "I don't know."},
                    {"left": "Are you OK?", "right": "Yes, I am.",
                     "right_audio_tts": "Yes, I am."},
                    {"left": "Where’s my classroom?", "right": "Come with me.",
                     "right_audio_tts": "Come with me."},
                ]}),

            # 9 — перемычка: прощание (1) + приветствие (2)
            ("text", {"html":
                f'<p><img src="{shared("hello_rocket")}" alt="" style="height:180px"></p>'
                "<h3>Ну вот и всё! Первая часть домашней работы выполнена 🎉</h3>"
                "<p>А это значит, что ты невероятный молодец.</p>"
                "<p>Дальше — дополнительная часть: интерактивное видео с вопросами. Делать её "
                "не обязательно, но она очень-очень интересная. Давай посмотрим видео и сделаем "
                "все упражнения 👍</p>"}),

            # 10 — интерактивное видео из «(2)»
            ("video", {"title": "Дополнительное задание: мультфильм «We’re lost!»",
                       "url": "", "provider": "file"}),

            # 11
            ("text", {"html":
                f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                "<h3>Домашнее задание сделано!</h3>"
                "<p>Ты отлично потрудился. Увидимся на уроке!</p>"}),
        ],
    },

    # ------------------------------------------------------------------ HW5
    "u5_hw5": {
        "unit": U, "unit_title": UNIT, "unit_sort": 5,
        "lesson_title": "Homework 5", "lesson_sort": 4, "kind": "homework",
        # «SM1 Unit 5 Homework 5» — догружена 07.10.2026 в корень SM1.
        # Блок 3 выгрузки: клипарт с детьми-спортсменами — украшение, не взят.
        # Блок 5 LISTENING (James, Emma, Charles, Hannah — по три картинки на
        # выбор): аудио нет, ключа нет (все кружки пустые), две картинки из
        # двенадцати не выгрузились — в урок НЕ положен, строка в доработке.
        # Блок 8 — две пустые игры («Впиши слова», «Составь предложения») — СОСТАВ МОЙ.
        # Блок 10 — реклама розыгрыша, не перенесена.
        "blocks": [
            # 1
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>Привет!</h2>"
                "<p>Это новая домашняя работа. Сегодня тебя ждут много не совсем простых, но "
                "очень-очень интересных заданий! Ты познакомишься с новыми персонажами, а с одним "
                "даже пообщаешься 😉</p><p>Ну что, предлагаю начинать!</p>"}),

            # 2
            ("sort", {
                "title": "Начнём с интересного задания! Распредели слова по группам, чтобы получились "
                         "выражения. Например: play the piano или go swimming.",
                "groups": [
                    {"name": "PLAY", "items": [{"text": t, "audio_tts": "play " + t} for t in
                                               ["hide-and-seek", "with friends", "with toys", "computer games"]]},
                    {"name": "WATCH", "items": [{"text": "TV", "audio_tts": "watch TV"}]},
                    {"name": "GO", "items": [{"text": "swimming", "audio_tts": "go swimming"}]},
                    {"name": "RIDE", "items": [{"text": t, "audio_tts": "ride " + t} for t in
                                               ["my horse", "my bike", "my pony"]]},
                ]}),

            # 3
            ("match", {
                "title": "Ты прекрасно справился с предыдущим заданием! А вот и следующее — соедини одну "
                         "часть предложения со второй. Думаю, у тебя получится 😉",
                "pairs": [
                    {"left": "On Saturdays I play the", "right": "piano",
                     "right_audio_tts": "On Saturdays I play the piano."},
                    {"left": "On Sundays I watch", "right": "TV",
                     "right_audio_tts": "On Sundays I watch TV."},
                    {"left": "On Mondays I play with", "right": "friends",
                     "right_audio_tts": "On Mondays I play with friends."},
                    {"left": "On Thursdays I go", "right": "swimming",
                     "right_audio_tts": "On Thursdays I go swimming."},
                    {"left": "On Tuesdays I ride", "right": "my bike",
                     "right_audio_tts": "On Tuesdays I ride my bike."},
                    {"left": "On Wednesdays I play", "right": "computer games",
                     "right_audio_tts": "On Wednesdays I play computer games."},
                ]}),

            # 4 — письмо Милы (блок 6 выгрузки)
            ("text", {"html":
                "<p>Мы с тобой сейчас познакомимся с Милой и узнаем, как проходит её неделя.</p>"
                "<p>Она тебе написала письмо, давай прочитаем его!</p>"
                + pic("hw5_mila_letter", 660)}),

            # 5
            ("task", {
                "title": "Ответное письмо Миле ✉️",
                "needs_review": True,
                "html": "<p>А теперь давай напишем ответное письмо Миле.</p>"
                        "<p>Ты можешь написать его в окошке здесь. А если тебе неудобно печатать текст, "
                        "можешь написать его от руки и прислать фото.</p>"
                        "<p>Начни, пожалуйста, письмо с таких слов: <i>Hello, Mila! My name is … "
                        "This is my week!</i></p>"}),

            # 6 — игра «Впиши слова», содержимого нет. СОСТАВ МОЙ.
            ("exact_input", {"items": [
                {"prompt": "⭐ Ты выполнил все задания из основной части! А это дополнительное задание — "
                           "для настоящих чемпионов! Впиши по-английски: смотреть телевизор",
                 "accept": ["watch TV", "watch tv", "Watch TV"]},
                {"prompt": "кататься на велосипеде", "accept": ["ride a bike", "ride my bike", "Ride a bike"]},
                {"prompt": "играть на пианино", "accept": ["play the piano", "Play the piano"]},
                {"prompt": "играть в прятки", "accept": ["play hide-and-seek", "play hide and seek",
                                                         "Play hide-and-seek"]},
                {"prompt": "заниматься плаванием", "accept": ["go swimming", "Go swimming"]},
                {"prompt": "играть в компьютерные игры", "accept": ["play computer games",
                                                                    "Play computer games"]},
            ]}),

            # 7–9 — игра «Составь предложения», содержимого нет. СОСТАВ МОЙ: фразы из письма Милы.
            order("On Mondays I watch TV for two hours.",
                  ["On", "Mondays", "I", "watch", "TV", "for", "two", "hours."],
                  title="⭐ Составь предложение из письма Милы"),
            order("I play tennis for one hour.",
                  ["I", "play", "tennis", "for", "one", "hour."],
                  title="⭐ Составь предложение из письма Милы"),
            order("On Saturdays and Sundays I do nothing!",
                  ["On", "Saturdays", "and", "Sundays", "I", "do", "nothing!"],
                  title="⭐ Составь предложение из письма Милы"),

            # 10
            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>Ого! Вот это здорово!</h3>"
                "<p>Как много заданий ты сделал сегодня. Ты потрудился на славу.</p>"
                "<p>Ты самый-самый лучший ученик на свете. Молодец ⭐</p>"}),
        ],
    },

    # ------------------------------------------------------------------ HW6
    "u5_hw6": {
        "unit": U, "unit_title": UNIT, "unit_sort": 5,
        "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework",
        # Имена файлов врут: основная часть лежит в «Homework 6 (2)» (8 блоков,
        # приветствие говорит о «второй, дополнительной части»), а «Homework 6
        # (1)», внутри озаглавленная «(2)», — игра Matching Columns на те же
        # 6 занятий. Поэтому порядок: файл (2) → перемычка 7 → файл (1).
        # Блок 1 выгрузки — реклама для родителей, не перенесена.
        # «Найди пару» (блок 3): картинок в выгрузке нет — лист Л5.1.
        # «Классификация» (блок 4): пейзажей пляжа и гор в выгрузке нет,
        # у блока sort картинок групп нет — названия с эмодзи.
        "blocks": [
            # 1
            ("text", {"html":
                f'<p><img src="{shared("hello_highfive")}" alt="" style="height:200px"></p>'
                "<h2>Добро пожаловать в домашнюю работу!</h2>"
                "<p>Здесь мы с тобой повторим тему, которую ты уже прошёл на уроке. "
                "Как всегда, тебя ждут классные задания 😄</p>"
                "<p>В конце есть вторая, дополнительная часть. Её не обязательно делать, но "
                "если у тебя получится её выполнить, то ты будешь мега крут!</p>"}),

            # 2
            ("text", {"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p>"
                              + pic("card_go_activities")}),

            # 3
            ("match", {
                "title": "Для начала давай соединим картинку с фразой. Вспомним спортивные занятия!",
                "pairs": [{"left_image": c(f), "right": en, "right_audio_tts": en}
                          for en, ru, f in GO_SPORTS]}),

            # 4
            ("sort", {
                "title": "Смотри, какие красивые места! Давай выберем, какими видами спорта где "
                         "можно заниматься. Разложи фразы: Beach — пляж, Mountains — горы.",
                "groups": [
                    {"name": "Beach 🏖️", "items": [
                        {"text": "go running", "audio_tts": "go running"},
                        {"text": "go surfing", "audio_tts": "go surfing"},
                        {"text": "go swimming", "audio_tts": "go swimming"},
                    ]},
                    {"name": "Mountains 🏔️", "items": [
                        {"text": "go climbing", "audio_tts": "go climbing"},
                        {"text": "go skiing", "audio_tts": "go skiing"},
                        {"text": "go sledging", "audio_tts": "go sledging"},
                    ]},
                ]}),

            # 5 — «Диаграмма»: шесть фото мест, точки по центрам кадров
            ("hotspot", {
                "title": "А вот ещё несколько мест, где мы можем заниматься спортом. "
                         "Давай соединим предложения с местами 😀",
                "mode": "label",
                "image": c("sport_places"),
                "points": [
                    {"x": 15.3, "y": 36, "text": "We ride a horse there.",
                     "audio_tts": "We ride a horse there."},
                    {"x": 50.0, "y": 36, "text": "We play football here.",
                     "audio_tts": "We play football here."},
                    {"x": 84.7, "y": 36, "text": "We go fishing here.",
                     "audio_tts": "We go fishing here."},
                    {"x": 15.3, "y": 89, "text": "We go running here.",
                     "audio_tts": "We go running here."},
                    {"x": 50.0, "y": 89, "text": "We go climbing here.",
                     "audio_tts": "We go climbing here."},
                    {"x": 84.7, "y": 89, "text": "We play tennis here.",
                     "audio_tts": "We play tennis here."},
                ]}),

            # 6
            ("speaking", {
                "title": "Моё идеальное место для спорта 🎤",
                "html": "<p>Ты большой-большой молодец! Самое время пофантазировать!</p>"
                        "<p>Придумай своё идеальное место для занятий спортом, нарисуй его. "
                        "Затем нажми на микрофон и опиши его.</p>"
                        "<p><b>Пример:</b> <i>It’s big and green. I can go climbing and go "
                        "running there.</i></p>",
                "sample_tts": "It's big and green. I can go climbing and go running there.",
                "needs_review": True,
            }),

            # 7 — перемычка: прощание основной части + вход в дополнительную
            ("text", {"html":
                f'<p><img src="{shared("hello_rocket")}" alt="" style="height:180px"></p>'
                "<h3>Вау! Отличная работа!</h3>"
                "<p>Не забудь показать свой рисунок учителю. Он очень-очень хочет его увидеть.</p>"
                "<p>А теперь — дополнительная часть. Соедини английские фразы с переводом!</p>"}),

            # 8 — «Homework 6 (1)»: Activity Matching Columns Game
            ("match", {
                "title": "Соедини фразу с переводом",
                "pairs": [{"left": en, "right": ru, "left_audio_tts": en}
                          for en, ru, f in GO_SPORTS]}),

            # 9
            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>Ты справился со всем домашним заданием!</h3>"
                "<p>Увидимся на уроке 🥰</p>"}),
        ],
    },

    # ------------------------------------------------------------------ HW7
    "u5_hw7": {
        "unit": U, "unit_title": UNIT, "unit_sort": 5,
        "lesson_title": "Homework 7", "lesson_sort": 6, "kind": "homework",
        # 10 блоков выгрузки. «Найди слово» (поиск слов, дни недели) собран
        # как match «день — перевод». Два Wordwall — Anagram «SM1 Unit 5 Days
        # of the week» и Complete the sentence «SM1-5» — пересобраны блоками
        # exact_input и gaps: СОСТАВ МОЙ. В вопросе 2 блока 5 опечатка
        # выгрузки «at the on Mondays» исправлена на «on Mondays».
        "blocks": [
            # 1
            ("text", {"html":
                f'<p><img src="{shared("hello_book")}" alt="" style="height:200px"></p>'
                "<h2>Привет! Как здорово, что ты решил сделать домашнее задание!</h2>"
                "<p>Это повторение перед тестом — давай вспомним всё!</p>"}),

            # 2 — «Найди слово»
            ("match", {
                "title": "Вспомни дни недели: соедини слово с переводом",
                "pairs": [{"left": en, "right": ru, "left_audio_tts": en} for en, ru in DAYS]}),

            # 3
            ("sort", {
                "title": "Раздели занятия на 2 группы: PLAY или GO",
                "groups": [
                    {"name": "PLAY", "items": [{"text": t, "audio_tts": t} for t in
                                               ["football", "tennis", "board games"]]},
                    {"name": "GO", "items": [{"text": t, "audio_tts": t} for t in
                                             ["swimming", "skiing", "surfing", "climbing", "running"]]},
                ]}),

            # 4
            ("gaps", {
                "title": "Впиши нужный день недели",
                "mode": "type",
                "text": "1. I play football on __Monday__. (понедельник)\n"
                        "2. I go swimming on __Wednesday__. (среда)\n"
                        "3. I ride my bike on __Friday__. (пятница)\n"
                        "4. I watch TV on __Saturday__. (суббота)\n"
                        "5. I play tennis on __Thursday__. (четверг)",
                "gaps_expected": 5,
            }),

            # 5
            ("quiz", {"title": "Прочитай вопрос и выбери ответ. Смайлик поможет тебе догадаться, "
                               "да или нет.",
                      "questions": [
                          single("Do you play football at the weekend? 😊",
                                 ["Yes, I do.", "Yes, I am.", "Yes, I like."], 0),
                          single("Do you ride your bike on Mondays? 😊",
                                 ["No, I not.", "Yes, I doing.", "Yes, I do."], 2),
                          single("Do you watch TV at the weekend? 😞",
                                 ["Yes, I don’t.", "No, I don’t.", "No, I do."], 1),
                      ]}),

            # 6, 7
            order("I play football on Mondays.", ["I", "play", "football", "on", "Mondays."]),
            order("Do you play tennis at the weekend?",
                  ["Do", "you", "play", "tennis", "at", "the weekend?"]),

            # 8
            ("speaking", {
                "title": "Расскажи про свою неделю 🎤",
                "html": "<p>Запиши рассказ о своей неделе — минимум 5 предложений! "
                        "Нажми на микрофон и расскажи про свою неделю.</p>"
                        "<p><b>Пример:</b> <i>I play football on Mondays. I go swimming on "
                        "Wednesdays.</i></p>",
                "sample_tts": "I play football on Mondays. I go swimming on Wednesdays.",
                "needs_review": True,
            }),

            # 9
            ("text", {"html":
                "<h3>Ты выполнил все задания из основной части!</h3>"
                "<p>А это дополнительное задание — для настоящих чемпионов! 🏆</p>"}),

            # 10 — Wordwall Anagram «SM1 Unit 5 Days of the week», СОСТАВ МОЙ
            ("exact_input", {"items": [
                {"prompt": "Составь слово из букв: " + p, "accept": [en], "audio_tts": en}
                for p, en in [
                    ("d · a · y · M · o · n", "Monday"),
                    ("s · d · u · e · y · T · a", "Tuesday"),
                    ("n · e · s · W · d · a · y · d · e", "Wednesday"),
                    ("r · s · h · u · d · a · y · T", "Thursday"),
                    ("i · d · r · F · y · a", "Friday"),
                    ("t · u · r · a · S · d · a · y", "Saturday"),
                    ("n · u · d · S · y · a", "Sunday"),
                ]]}),

            # 11 — Wordwall Complete the sentence «SM1-5», СОСТАВ МОЙ
            ("gaps", {
                "title": "Перетащи слова в пропуски",
                "mode": "drag",
                "text": "Hi! I’m Sue. On __Mondays__ I go __swimming__. "
                        "On Tuesdays I __play__ football. "
                        "On Wednesdays I __ride__ my bike. "
                        "On Saturdays I __watch__ TV. "
                        "Do you play the piano at the __weekend__?",
                "gaps_expected": 6,
            }),

            # 12
            ("text", {"html":
                f'<p><img src="{shared("well_done_medal")}" alt="" style="height:180px"></p>'
                "<h3>Молодец! Ты готов к тесту!</h3><p>До встречи на уроке.</p>"}),
        ],
    },

    # ------------------------------------------------------------------ тест
    "u5_test": {
        "unit": U, "unit_title": UNIT, "unit_sort": 5,
        "lesson_title": "Unit 5 Test", "lesson_sort": 7, "kind": "test",
        # 7 блоков выгрузки → 12: «Составь предложение» с пятью предложениями
        # разложен на пять order (4–8), «Выбери правильный вариант» — один
        # quiz из пяти вопросов, LISTENING — аудио отдельным блоком 10 перед
        # классификацией. «Соедини слова с картинками» (2): картинок в
        # выгрузке нет — лист ЛТ5.1. В order 6–8 в выгрузке фото детей —
        # заменены картинками листов Л5.1 / ЛТ5.1.
        "blocks": [
            # 1 — «Впиши буквы»
            ("exact_input", {"items": [
                {"prompt": f"Напиши по-английски: {ru}", "accept": [en], "audio_tts": en}
                for en, ru in DAYS]}),

            # 2
            ("match", {
                "title": "Соедини слова с картинками",
                "pairs": [{"left_image": c(f), "right": en, "right_audio_tts": en} for en, f in [
                    ("ride a pony", "act_ride_pony"),
                    ("go swimming", "act_go_swimming"),
                    ("watch TV", "act_watch_tv"),
                    ("play football", "act_play_football"),
                    ("play computer games", "act_computer_games"),
                    ("ride a bike", "act_ride_bike"),
                ]]}),

            # 3
            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                single("A: Do you play computer games at the weekend?<br>B: ___",
                       ["Yes, I don’t.", "Yes, I do.", "No, I do."], 1, c("t_computer_games")),
                single("A: Do you play the piano every day?<br>B: ___",
                       ["No, I don’t.", "No, I do.", "Yes, I don’t."], 0, c("t_piano")),
                single("A: Do you play football on Sundays?<br>B: ___",
                       ["Yes, I do. I go swimming.", "Yes, I don’t.", "No, I don’t. I go swimming."],
                       2, c("t_football")),
                single("A: Do you watch TV at the weekend?<br>B: ___",
                       ["No, I do.", "Yes, I do.", "Yes, I don’t."], 1, c("t_watch_tv")),
                single("A: Do you do your homework every day?<br>B: ___",
                       ["Yes, I do.", "No, I do."], 0, c("t_homework")),
            ]}),

            # 4–8
            order("Do you watch TV at the weekend?",
                  ["Do", "you", "watch", "TV", "at the weekend?"], c("t_order_watch_tv")),
            order("Do you play the piano on Mondays?",
                  ["Do", "you", "play", "the piano", "on", "Mondays?"], c("t_order_piano")),
            order("Do you go swimming on Wednesdays?",
                  ["Do", "you", "go", "swimming", "on", "Wednesdays?"], c("act_go_swimming")),
            order("Do you play hide-and-seek on Saturdays?",
                  ["Do", "you", "play", "hide-and-seek", "on", "Saturdays?"], c("act_hide_and_seek")),
            order("Do you ride a pony every Friday?",
                  ["Do", "you", "ride", "a pony", "every Friday?"], c("act_ride_pony")),

            # 9 — READING
            ("match", {
                "title": "READING. Прочитай текст. Соедини день недели с действием. "
                         "«Hi! I’m Sam. Here is my week! On Mondays I don’t play football – "
                         "I go swimming. On Tuesdays I play computer games. On Thursdays I don’t "
                         "watch TV – I play hide-and-seek with my friends. On Saturdays I sing. "
                         "On Sundays I play ball with my dad.»",
                "pairs": [{"left": d, "right": a, "right_audio_tts": a} for d, a in [
                    ("Monday", "go swimming"),
                    ("Tuesday", "play computer games"),
                    ("Thursday", "play hide-and-seek"),
                    ("Saturday", "sing"),
                    ("Sunday", "play ball"),
                ]]}),

            # 10 — LISTENING, аудио
            ("video", {"title": "LISTENING. Послушай запись 🎧", "url": "", "provider": "file"}),

            # 11
            ("sort", {
                "title": "Перетащи дни недели и занятия в колонку нужного ребёнка",
                "groups": [
                    {"name": "Tom", "items": [{"text": t} for t in
                                              ["Sunday", "Saturday", "play football", "watch TV"]]},
                    {"name": "Lucy", "items": [{"text": t} for t in
                                               ["Monday", "go swimming", "sing"]]},
                    {"name": "Ben", "items": [{"text": t} for t in
                                              ["Wednesday", "play hide-and-seek", "play computer games"]]},
                ]}),

            # 12
            ("speaking", {
                "title": "SPEAKING TASK 🎤",
                "html": "<p>Ответь на вопросы:</p><ol>"
                        "<li>What do you do on Mondays?</li>"
                        "<li>What do you do on Tuesdays?</li>"
                        "<li>What do you do on Wednesdays?</li>"
                        "<li>What do you do on Fridays?</li>"
                        "<li>What do you do on Saturdays?</li>"
                        "<li>What do you do on Sundays?</li>"
                        "<li>Do you like swimming?</li>"
                        "<li>Do you like playing computer games?</li>"
                        "<li>Do you like playing football?</li>"
                        "<li>Do you like doing your homework?</li>"
                        "<li>What do you like to do in your free time?</li>"
                        "<li>What do you like to do with your friends?</li>"
                        "</ol><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>",
                "needs_review": True,
            }),
        ],
    },
}
