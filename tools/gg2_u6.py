"""Go Getter 2 · Unit 6 · Jobs — шесть домашек и тест.

Источник — docs/GG2_разбор_u6.md. Части (1)/(2) у HW1, HW2 и HW6 склеены в один
урок: приветствие второй части стало коротким текстом-переходом.
"""
import random

from gg2_build import img, shared, todo, video

U = "u6"
UNIT = {"unit": U, "unit_title": "Unit 6 · Jobs", "unit_sort": 6}

JOBS = [
    ("artist", "художник", "artist"),
    ("builder", "строитель", "builder"),
    ("bus driver", "водитель автобуса", "bus_driver"),
    ("chef", "повар", "chef"),
    ("doctor", "врач", "doctor"),
    ("farmer", "фермер", "farmer"),
    ("footballer", "футболист", "footballer"),
    ("nurse", "медсестра", "nurse"),
    ("office worker", "офисный работник", "office_worker"),
    ("pilot", "пилот", "pilot"),
    ("police officer", "полицейский", "police_officer"),
    ("shop assistant", "продавец", "shop_assistant"),
    ("singer", "певица", "singer"),
    ("teacher", "учитель", "teacher"),
    ("vet", "ветеринар", "vet"),
]
JOB_FILE = {en: f for en, ru, f in JOBS}


def hello(pic, title, *paras):
    return ("text", {"html": f'<p><img src="{shared(pic)}" alt="" style="height:200px"></p>'
                             f"<h2>{title}</h2>" + "".join(f"<p>{p}</p>" for p in paras)})


def bye(pic, title, *paras):
    return ("text", {"html": f'<p><img src="{shared(pic)}" alt="" style="height:180px"></p>'
                             f"<h3>{title}</h3>" + "".join(f"<p>{p}</p>" for p in paras)})


def audio(title, todo_text):
    """Пустой медиаблок под аудио — файла в выгрузке нет."""
    return todo(("video", {"title": title, "url": "", "provider": "file"}), ("audio", todo_text))


def order(sentence, words=None):
    words = words or sentence.split(" ")
    return ("order", {"words": words, "sentence": sentence, "audio_tts": sentence})


def q1(question, options, correct):
    return {"q": question, "type": "single", "options": [{"text": o} for o in options], "correct": [correct]}


def quiz_ru_to_en(items, seed):
    rnd = random.Random(seed)
    words = [en for en, ru, f in items]
    out = []
    for en, ru, f in items:
        wrong = rnd.sample([w for w in words if w != en], 3)
        opts = wrong[:]
        opts.insert(rnd.randrange(4), en)
        out.append(q1(f"Как по-английски «{ru}»?", opts, opts.index(en)))
    return {"title": "Выбери правильный перевод", "questions": out}


LESSONS = {
    # ------------------------------------------------------------ Homework 1
    "u6_hw1": {**UNIT, "lesson_title": "Homework 1", "lesson_sort": 0, "kind": "homework", "blocks": [
        hello("hello_wave", "Привет! 👋",
              "Сейчас мы с тобой выучим различные профессии. Выполни все задания, чтобы выучить "
              "слова на 100%!",
              "Сначала посмотри карточки и послушай, как звучит каждое слово."),
        ("flashcards", {"cards": [
            {"text": en, "translation": ru, "audio_tts": en, "image": img(U, f)} for en, ru, f in JOBS]}),
        ("quiz", quiz_ru_to_en(JOBS, seed=61)),
        ("exact_input", {"title": "Напиши слово по-английски", "items": [
            {"prompt": f"Напиши по-английски: {ru}", "accept": [en, en.capitalize()], "audio_tts": en,
             "image": img(U, JOB_FILE[en])}
            for en, ru in [("doctor", "врач"), ("chef", "повар"), ("bus driver", "водитель автобуса")]]}),
        ("text", {"html": f'<p><img src="{shared("hello_rocket")}" alt="" style="height:180px"></p>'
                          "<h3>А теперь — задания! 💪</h3>"
                          "<p>Сейчас мы закрепим знания, полученные на уроке. "
                          "У тебя всё обязательно получится!</p>"}),
        ("match", {"title": "Итак, первое задание! Посмотри внимательно на картинки и соедини названия "
                            "профессий с подходящими картинками. Удачи!",
                   "pairs": [{"left_image": img(U, JOB_FILE[en]), "right": en, "right_audio_tts": en}
                             for en in ["shop assistant", "builder", "bus driver", "office worker", "chef",
                                        "police officer", "vet", "artist", "singer", "farmer"]]}),
        ("quiz", {"title": "Прочитай предложения и выбери правильный вариант ответа по смыслу",
                  "questions": [
                      q1("I sing in a band. I'm a…", ["singer", "office worker"], 0),
                      q1("I sit at a desk and work on a computer. I'm an…", ["bus driver", "office worker"], 1),
                      q1("I build houses and flats. I'm a…", ["pilot", "builder"], 1),
                      q1("I drive around town and take people to different places. I'm a…",
                         ["bus driver", "footballer"], 0),
                      q1("I fly planes and take people to other countries. I'm a…", ["artist", "pilot"], 1),
                      q1("I play a popular sport and I score goals. I'm a…", ["footballer", "farmer"], 0),
                  ]}),
        ("gaps", {"title": "Внимательно прочитай текст и заполни пропуски подходящими словами. "
                           "Слово chef уже вписано — это пример.",
                  "mode": "drag",
                  "text": "Hi, I'm Mark and this is my family. You can see me with my dad on the left. "
                          "Dad loves cooking but he isn't a chef. He works at the hospital, but he isn't "
                          "a doctor. He's a __nurse__. Mum works at my sister's school. She's a French "
                          "__teacher__. My grandpa and grandma work too. Grandma is a great __artist__ and "
                          "she paints beautiful pictures. She sells them in a shop. Grandpa works in her "
                          "shop – he's her __shop assistant__. I like animals and when I grow up I want to "
                          "be a __vet__ so I can look after people's pets.",
                  "gaps_expected": 5}),
        ("task", {"title": "Дополнительное задание — для самых крутых учеников! ⭐",
                  "needs_review": True,
                  "html": "<p>Заполни табличку про себя и расскажи, кем ты хочешь стать и почему.</p>"
                          "<p><b>What do you want to be? Why?</b></p>"
                          "<ul><li>jobs I like: ___, ___</li>"
                          "<li>jobs I don't like: ___, ___</li>"
                          "<li>jobs I like a lot: ___, ___</li>"
                          "<li>I want to be ___ because ___.</li></ul>"
                          "<p><i>For example: I want to be a vet because I like animals.</i></p>"}),
        bye("well_done_clap", "Классная работа! 🖐",
            "Я тебя поздравляю — домашняя работа выполнена очень здорово. До встречи на занятии!"),
    ]},

    # ------------------------------------------------------------ Homework 2
    "u6_hw2": {**UNIT, "lesson_title": "Homework 2", "lesson_sort": 1, "kind": "homework", "blocks": [
        hello("hello_book", "Огромный привет! 😉",
              "В этой домашней работе мы повторим всё то, что ты прошёл на уроке с учителем. "
              "Это поможет тебе не только всё запомнить, но и использовать :))",
              "К этому домашнему заданию есть дополнение! Оно необязательное, но если ты его "
              "выполнишь, учитель даст тебе дополнительную ⭐ Давай начинать!"),
        video("Давай начнём с видео. Посмотри его, а потом сделай задания ниже.",
              "видео: семья хотела стать поп-звёздами (mum played the drums, dad danced, they tried hard)"),
        ("match", {"title": "Супер! Посмотри видео ещё раз и соедини глаголы по парам",
                   "pairs": [{"left": a, "right": b, "right_audio_tts": b}
                             for a, b in [("play", "played"), ("dance", "danced"), ("try", "tried")]]}),
        ("text", {"html": "<h3>Молодец! 👍</h3><p>Посмотри видео ещё раз и расставь слова в предложениях "
                          "по смыслу.</p>"}),
        order("My mum played the drums."),
        order("My dad danced."),
        order("They wanted to be pop stars.", ["They", "wanted", "to", "be", "pop stars."]),
        order("They tried hard."),
        ("gaps", {"title": "Перейдём к практике! Расставь пропущенные слова в предложения по смыслу",
                  "mode": "drag",
                  "text": "1. My aunt __phoned__ me last Saturday on my mobile.\n"
                          "2. She __invited__ me to Harry's birthday party.\n"
                          "3. I __stopped__ on the way at the toy shop for a present.\n"
                          "4. Harry and his friends __listened__ to music.\n"
                          "5. I __helped__ my aunt with the food.\n"
                          "6. Harry __liked__ his party!",
                  "gaps_expected": 6}),
        ("task", {"title": "Задание для чемпионов! За него ты получишь дополнительный балл ;)",
                  "needs_review": True,
                  "html": "<p>Напиши 4 предложения о себе, используя Past Simple.</p>"
                          "<p><i>For example:<br>I played computer games on Monday.<br>"
                          "I danced at school on Thursday.</i></p>"}),
        ("text", {"html": f'<p><img src="{shared("well_done_star")}" alt="" style="height:180px"></p>'
                          "<h3>Ты МЕГАКРУТ! ⭐</h3>"
                          "<p>Основная часть готова — ты так здорово потрудился!</p>"
                          "<p>Дальше — <b>дополнительная часть</b>. Она необязательная, но если ты её "
                          "сделаешь, получишь дополнительную ⭐ Давай начинать 😉</p>"}),
        ("text", {"html": "<h3>Маркеры прошедшего времени</h3>"
                          "<p>Внимательно изучи табличку: эти слова подсказывают, что действие было "
                          "в прошлом — значит, нужен Past Simple.</p>"
                          "<p><b>Past Simple:</b></p>"
                          "<ul><li><b>last week</b> — на прошлой неделе</li>"
                          "<li><b>2 days ago</b> — 2 дня назад</li>"
                          "<li><b>in 1999</b> — в 1999 году</li>"
                          "<li><b>yesterday</b> — вчера</li></ul>"}),
        ("gaps", {"title": "Посмотри на картинку: сейчас 04:00, май, вторник. Сколько времени прошло? "
                           "Заполни пропуски. Первый ответ подсказан на картинке.",
                  "mode": "drag",
                  "image": img(U, "book_time_now"),
                  "text": "1. 03:00 — __an hour ago__\n"
                          "2. 03:50 — __10 minutes ago__\n"
                          "3. March — __2 months ago__\n"
                          "4. Saturday — __3 days ago__",
                  "gaps_expected": 4}),
        todo(("match", {"title": "Здорово! Ты так хорошо справляешься! Посмотри на маркеры Past Simple "
                                 "и соедини их с переводом",
                        "pairs": [{"left": en, "right": ru} for en, ru in [
                            ("yesterday", "вчера"), ("last week", "на прошлой неделе"),
                            ("last year", "в прошлом году"), ("last Saturday", "в прошлую субботу"),
                            ("two days ago", "два дня назад"), ("an hour ago", "час назад"),
                            ("in 1999", "в 1999 году"), ("this morning", "сегодня утром")]]}),
             ("game", "СОСТАВ МОЙ: пересобрана игра Wordwall «Match up — Past simple time markers» "
                      "(маркер ↔ перевод, 8 пар)")),
        bye("well_done_trophy", "Hurray! 🌟",
            "Домашняя работа выполнена на отлично — всё благодаря твоим стараниям. Увидимся на занятии!"),
    ]},

    # ------------------------------------------------------------ Homework 3
    "u6_hw3": {**UNIT, "lesson_title": "Homework 3", "lesson_sort": 2, "kind": "homework", "blocks": [
        hello("hello_rocket", "Огромный привет! 😉",
              "В этой домашней работе мы повторим всё то, что ты прошёл на уроке с учителем. "
              "Это поможет тебе не только всё запомнить, но и использовать :)) Давай начинать!"),
        ("text", {"html": "<h3>Неправильные глаголы</h3>"
                          "<p>Давай повторим неправильные глаголы! Помни: у них совсем другая форма "
                          "в прошедшем времени.</p>"
                          "<ul><li>come – <b>came</b></li><li>drink – <b>drank</b></li>"
                          "<li>eat – <b>ate</b></li><li>feel – <b>felt</b></li>"
                          "<li>go – <b>went</b></li><li>have – <b>had</b></li>"
                          "<li>make – <b>made</b></li><li>meet – <b>met</b></li>"
                          "<li>take – <b>took</b></li></ul>"}),
        video("Посмотри видео, а потом сделай задание ниже.",
              "видео: Hammy в школе (went to school, drank, ate my Maths book, cookery class, chocolate cakes)"),
        ("sequence", {"title": "Посмотри видео ещё раз и расставь предложения по порядку",
                      "items": [{"text": t} for t in [
                          "Yesterday I went to school.", "Hammy came too.", "Hammy drank something!",
                          "Hammy ate my Maths book!", "Later we had a cookery class.",
                          "We made chocolate cakes."]]}),
        ("gaps", {"title": "Здорово! Давай ещё немного потренируемся! Впиши глагол в прошедшем времени",
                  "mode": "type",
                  "text": "1. We __had__ (have) lunch at 2 o'clock yesterday.\n"
                          "2. I __made__ (make) a pizza last Sunday.\n"
                          "3. We __went__ (go) to the cinema last month.\n"
                          "4. You __took__ (take) a photo of me two minutes ago.\n"
                          "5. They __drank__ (drink) tea after the meal yesterday evening.\n"
                          "6. I __ate__ (eat) a sandwich for lunch an hour ago.\n"
                          "7. We first __met__ (meet) three years ago.\n"
                          "8. Everyone __came__ (come) to my party last Sunday.",
                  "gaps_expected": 8}),
        ("match", {"title": "Молодец! Ещё одно задание: соедини неправильные глаголы по парам",
                   "pairs": [{"left": a, "right": b, "right_audio_tts": b} for a, b in [
                       ("have", "had"), ("make", "made"), ("feel", "felt"), ("take", "took"),
                       ("come", "came"), ("drink", "drank"), ("meet", "met"), ("go", "went"),
                       ("eat", "ate")]]}),
        ("task", {"title": "Задание для чемпионов! За него ты получишь дополнительный балл ;)",
                  "needs_review": True,
                  "html": "<p>Напиши 5 предложений о том, что ты делал на выходных.</p>"
                          "<p><i>For example: I walked with my dog on Saturday.</i></p>"}),
        bye("well_done_star", "Спасибо тебе огромное! ⭐",
            "Ты так сегодня здорово потрудился. Твой учитель тобой гордится, и ты тоже можешь собой "
            "гордиться. До встречи на занятии!"),
    ]},

    # ------------------------------------------------------------ Homework 4
    "u6_hw4": {**UNIT, "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework", "blocks": [
        hello("hello_highfive", "Привет, самый старательный и классный ученик! 😎",
              "Сегодня мы будем вспоминать слова, которые ты учил на занятии. Давай начнём?"),
        ("text", {"html": "<h3>Asking for and giving permission</h3>"
                          "<p>Начнём с небольшой таблички — узнаёшь? Так просят разрешения и отвечают "
                          "на просьбу.</p>"
                          "<p><b>Can I borrow a pen, please?</b><br>"
                          "Yes, you can. / No, sorry, you can't. / Sure, no problem.</p>"
                          "<p><b>Is it OK if I use your mobile?</b><br>"
                          "No, sorry, it isn't OK. / Oh, all right. / Yes, that's fine.</p>"}),
        ("text", {"html": "<p>Итак, приступим к упражнению! Подглядывай в табличку и расставь слова "
                          "в правильном порядке.</p>"}),
        order("Can I borrow a pen, please?"),
        order("Yes, you can."),
        order("Is it OK if I use your mobile?"),
        order("No, sorry, it isn't OK."),
        order("Sure, no problem."),
        ("gaps", {"title": "Следующее задание немного посложнее… Можно подглядывать в табличку ;) "
                           "Прочитай диалоги и заполни пропуски",
                  "mode": "drag",
                  "text": "Dialogue 1\n"
                          "Elena: We've got a Maths test today. Have you got your calculator this time?\n"
                          "Tom: Oh no, I forgot it. __Is it OK if I use yours__?\n"
                          "Elena: __No, it isn't.__ I need it for the test!\n"
                          "Tom: OK, I understand. I hope the test is easy!\n\n"
                          "Dialogue 2\n"
                          "Jess: Hi Tom. Do you want to go to the cinema?\n"
                          "Matt: Sure, but I have to ask my mum first. __Can I borrow your mobile, please?__ "
                          "I don't have my phone with me.\n"
                          "Jess: __Yes, you can__. Here you are.\n"
                          "Matt: Thanks. Oh, hi mum. __Please can I go to the cinema?__\n"
                          "Mum: __Sure, no problem.__",
                  "gaps_expected": 6}),
        ("task", {"title": "Напиши 2 вежливые просьбы",
                  "needs_review": True,
                  "html": "<p>Ты отлично справляешься! Осталось одно задание из основной части. Напиши "
                          "каждую просьбу двумя способами. Не забудь <b>please</b> — будь вежливым!</p>"
                          "<p><i>Пример. You want to go to the cinema.<br>"
                          "a) Please can I go to the cinema?<br>b) Can I go to the cinema, please?</i></p>"
                          "<ol><li>You want to use your dad's laptop.<br>a) …<br>b) …</li>"
                          "<li>You want to borrow a friend's mobile.<br>a) …<br>b) …</li></ol>"}),
        ("task", {"title": "Дополнительное задание — для самых стойких и терпеливых! ⭐",
                  "needs_review": True,
                  "html": "<p>Внимательно посмотри на записку. Пол и Лео хотят пойти в бассейн и "
                          "спрашивают разрешения у папы Лео. Напиши их диалог: как они просят и как "
                          "папа отвечает. У тебя получится!</p>"
                          f'<p><img src="{img(U, "book_permission_note")}" alt="Who: Paul and Leo. '
                          "Where: go to the swimming pool. Ask Leo's dad for permission. Permission: No. "
                          'Why: homework" style="max-width:100%"></p>'}),
        bye("well_done_medal", "Hurray! 🌟",
            "Домашняя работа выполнена на отлично — всё благодаря твоим стараниям. Увидимся на занятии!"),
    ]},

    # ------------------------------------------------------------ Homework 5
    "u6_hw5": {**UNIT, "lesson_title": "Homework 5", "lesson_sort": 4, "kind": "homework", "blocks": [
        hello("hello_laptop", "Привет! 😎",
              "Сегодня тебе предстоит много читать :) Но ты точно справишься, ведь для тебя нет ничего "
              "невозможного. Давай начнём?"),
        ("text", {"html": "<h3>Для начала давай прочитаем текст</h3>"
                          "<p><i>Do you think that a child's life was different in the past? "
                          "I asked my dad and grandpa.</i></p>"
                          "<p><b>Dad:</b> When I was a boy I helped my mum with jobs in the house every "
                          "weekend. She gave me 50p when I washed the car or I tidied the living room. It "
                          "wasn't a lot of money, but I did many jobs! When I had the money, I bought an "
                          "expensive football. It was really cool and all my friends liked it.</p>"
                          "<p><b>Grandpa:</b> My family was poor, so there wasn't any pocket money! But I "
                          "wanted some money, so I got a Saturday job at a restaurant. I washed the dishes "
                          "and the floor, and I put the plates on the tables. I made a lot of money and "
                          "when I was sixteen I bought a bicycle. I went everywhere on that bike!</p>"}),
        ("quiz", {"title": "Прочитай статью ещё раз и выбери подходящее для неё название",
                  "questions": [q1("What is the best title for the article?",
                                   ["The house jobs my dad did", "How Grandpa bought a bike",
                                    "When Dad and Grandpa were children"], 2)]}),
        ("truefalse", {"title": "Прочитай текст ещё раз: True (правда) или False (неправда)? "
                                "Читай внимательно и не торопись",
                       "statements": [
                           {"text": "Dad helped his mum every Saturday and Sunday.", "correct": True},
                           {"text": "Dad's mum gave him a lot of money.", "correct": False},
                           {"text": "Dad tidied the living room.", "correct": True},
                           {"text": "Dad's friends liked his football.", "correct": True},
                           {"text": "Grandpa worked every Sunday.", "correct": False},
                           {"text": "Grandpa bought a bike when he was 16.", "correct": True},
                       ]}),
        ("task", {"title": "Опиши картинку в прошедшем времени",
                  "needs_review": True,
                  "html": "<p>Ты уже на финишной прямой! Посмотри внимательно на картинку и опиши, что "
                          "делали люди разных профессий. Напиши не меньше 5 предложений. "
                          "Не забудь про Past Simple!</p>"
                          "<p><i>For example: An artist emptied the bin.</i></p>"
                          f'<p><img src="{img(U, "book_jobs_chores")}" alt="" style="max-width:100%"></p>'}),
        bye("well_done_smiley", "Ура! 🎉",
            "Ты справился с домашним заданием просто прекрасно. Самое время немножко отдохнуть. "
            "Увидимся на занятии :)"),
    ]},

    # ------------------------------------------------------------ Homework 6
    "u6_hw6": {**UNIT, "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework", "blocks": [
        hello("hello_headphones", "Привет! 😃",
              "Сегодня мы будем тренироваться в аудировании и даже напишем небольшой рассказ. "
              "У тебя всё получится, как и всегда. Давай приступим :)"),
        audio("Послушай рассказ Ника о его дне, а потом сделай задания ниже 🎧",
              "аудио: рассказ Ника о весёлом дне (дядя Ted, Gary; парк, футбол, ресторан, кино)"),
        ("quiz", {"title": "Послушай аудио и выбери правильный вариант ответа",
                  "questions": [
                      q1("Nick's ___ visited.", ["uncle", "grandfather"], 0),
                      q1("They played ___.", ["basketball", "football"], 1),
                      q1("They had lunch at ___.", ["a restaurant", "home"], 0),
                      q1("They went to the ___.", ["theatre", "cinema"], 1),
                  ]}),
        ("gaps", {"title": "Послушай аудио ещё раз и впиши пропущенные слова",
                  "mode": "type",
                  "text": "1. Nick had a fun day last __Saturday|saturday__.\n"
                          "2. First, Nick went to the __park__.\n"
                          "3. He scored __three|3__ goals.\n"
                          "4. Nick ate __two|2__ cheeseburgers.\n"
                          "5. Nick and Ted drank __lemonade__.\n"
                          "6. The __film|movie__ was really exciting.\n"
                          "7. Gary and Ted went home at __seven|7__ o'clock.",
                  "gaps_expected": 7}),
        ("gaps", {"title": "Прочитай рассказ Элены о её выходных и впиши глаголы в прошедшем времени. "
                           "Смотри пример: go → went",
                  "mode": "type",
                  "text": "Last Sunday I went to the beach with my friends. First, we went (go) to the beach "
                          "and we went swimming. But the sea __was__ (be) cold, so we __got__ (get) out "
                          "quickly! Then we played (play) beach volleyball. Amy and I were (be) Team A and "
                          "the boys were Team B. It was a lot of fun. Amy and I were the winners! After "
                          "that, we __had__ (have) a picnic on the sand. We __ate__ (eat) sandwiches and "
                          "__drank__ (drink) coke. Mum came and took us home in her car. We arrived home "
                          "at 4 o'clock. It was a great day out!",
                  "gaps_expected": 5}),
        ("task", {"title": "Напиши свой рассказ",
                  "needs_review": True,
                  "html": "<p>Супер, ты отлично справляешься! Теперь напиши небольшой рассказ о своих "
                          "прошлых выходных или о каком-то памятном и интересном для тебя дне ;)</p>"
                          "<p>Воспользуйся примером текста Элены и словами <b>First, Then, After that</b>. "
                          "Рассказ должен быть в прошедшем времени — проверяй, в какой форме ты пишешь "
                          "глаголы.</p>"
                          "<p><i><b>First</b>, we visited Madame Tussaud's.<br>"
                          "<b>Then</b>, we went to the London Aquarium.<br>"
                          "<b>After that</b>, we went to a Mexican restaurant.</i></p>"}),
        ("text", {"html": f'<p><img src="{shared("well_done_jump")}" alt="" style="height:180px"></p>'
                          "<h3>Классная работа! 🖐</h3>"
                          "<p>Первая часть готова. Теперь повторим изученный материал, чтобы ты смог "
                          "хорошо подготовиться к тесту. Для тебя нет ничего невозможного 😎</p>"}),
        ("match", {"title": "Давай сначала вспомним названия профессий. Соедини название с картинкой",
                   "pairs": [{"left": en, "right_image": img(U, JOB_FILE[en])}
                             for en in ["nurse", "builder", "police officer", "doctor", "farmer", "vet",
                                        "teacher", "chef"]]}),
        todo(("gaps", {"title": "Молодец! А сейчас вспомним прошедшее время. Прочитай диалог и вставь "
                                "подходящие слова",
                       "mode": "drag",
                       "text": "A: Where __did__ you go last weekend?\n"
                               "B: I __went__ to the zoo.\n"
                               "A: What did you __see__?\n"
                               "B: We __saw__ lions and monkeys.\n"
                               "A: __Did__ you have lunch there?\n"
                               "B: Yes, we __had__ pizza.",
                       "gaps_expected": 6}),
             ("game", "СОСТАВ МОЙ: пересобрана игра Wordwall «Complete the sentence — Past simple grammar» "
                      "(диалог: did, went, see, saw, Did, had)")),
        ("gaps", {"title": "Ты отлично справляешься! Прочитай предложения и заполни пропуски",
                  "mode": "drag",
                  "text": "1. I __had__ lunch at 2 p.m. yesterday.\n"
                          "2. I __met__ Ted at the cinema an hour ago.\n"
                          "3. Yesterday Mum __drank__ tea after dinner.\n"
                          "4. We __bought__ some cakes at the supermarket.\n"
                          "5. Jim __took__ lots of photos on holiday last year.\n"
                          "6. Dad __gave__ me a watch for my last birthday.",
                  "gaps_expected": 6}),
        ("gaps", {"title": "Следующее задание немного посложнее… Но ты обязательно справишься! "
                           "Прочитай диалог и заполни пропуски",
                  "mode": "drag",
                  "text": "Pam: Please __can__ I borrow your laptop, dad?\n"
                          "Dad: No, __sorry__, you can't. I'm using it. Why do you need it?\n"
                          "Pam: I'm planning a project for school and I want to look at the Internet.\n"
                          "Dad: Is it OK __if__ I look at your notes?\n"
                          "Pam: Yes, that's __fine__. Here.\n"
                          "Dad: They're good.\n"
                          "Pam: Come on, dad. Can I use your laptop, __please__? Just for an hour.\n"
                          "Dad: Oh, __all right__.",
                  "gaps_expected": 6}),
        bye("congrats_popper", "Hurray! 🌟",
            "Домашняя работа выполнена на отлично — всё благодаря твоим стараниям. Теперь ты готов "
            "к тесту на 100%! Увидимся на занятии."),
    ]},

    # ------------------------------------------------------------ Test
    "u6_test": {**UNIT, "lesson_title": "Unit 6 Test", "lesson_sort": 6, "kind": "test", "blocks": [
        ("exact_input", {"title": "Напиши слово по-английски", "items": [
            {"prompt": f"Напиши по-английски: {ru}", "accept": [en, en.capitalize()], "audio_tts": en}
            for en, ru in [("builder", "строитель"), ("nurse", "медсестра"), ("pilot", "пилот"),
                           ("police officer", "полицейский"), ("shop assistant", "продавец"),
                           ("teacher", "учитель")]]}),
        ("quiz", {"title": "Выбери правильный вариант, чтобы предложение было грамматически верным",
                  "questions": [
                      q1("Yesterday my dad ___ the car after work.", ["washd", "washed", "washes"], 1),
                      q1("We ___ to a new restaurant last Saturday.", ["went", "goed", "wented"], 0),
                      q1("My sister ___ her room two hours ago.", ["tidyed", "tidy", "tidied"], 2),
                      q1("I ___ a new dictionary for school last week.", ["buyed", "bought", "boughted"], 1),
                      q1("The doctor ___ me some medicine this morning.", ["gived", "give", "gave"], 2),
                  ]}),
        ("gaps", {"title": "Поставь глагол в скобках в правильную форму Past Simple",
                  "mode": "type",
                  "text": "1. Last summer my family __stayed__ (stay) in a small hotel in Italy.\n"
                          "2. The chef __made__ (make) an amazing pizza for dinner.\n"
                          "3. I __stopped__ (stop) playing computer games at ten o'clock.\n"
                          "4. We __had__ (have) a Maths test on Monday.\n"
                          "5. My brother __took__ (take) the dog for a walk an hour ago.",
                  "gaps_expected": 5}),
        order("My mum cooked dinner for us yesterday."),
        order("We didn't go to school last Friday."),
        order("First, I made my bed, then I tidied my room."),
        order("The police officer helped a lost tourist two days ago.",
              ["The", "police officer", "helped", "a", "lost", "tourist", "two", "days", "ago."]),
        order("My dad drank a cup of coffee and went to work."),
        ("text", {"html": "<h3>READING</h3><p>Прочитай текст и ответь на вопросы ниже.</p>"
                          "<h4>A Day in My Mum's Life</h4>"
                          "<p>My mum is a vet. She loves her job, but it's never easy. Yesterday was a "
                          "really busy day for her, so I want to tell you about it.</p>"
                          "<p>First, she got up at six o'clock and made breakfast for me and my brother. "
                          "Then she walked the dog and went to work. She arrived at the animal hospital at "
                          "half past seven.</p>"
                          "<p>In the morning, a man came in with his old cat. The cat was very ill, and Mum "
                          "felt sad. But she gave the cat some medicine and the cat got better!</p>"
                          "<p>After lunch, a little girl brought a small bird with a broken wing. Mum helped "
                          "the bird for two hours.</p>"
                          "<p>She came home at eight o'clock. She was tired, but she said, \"I love my "
                          "job.\" Then she took the dog for another walk!</p>"}),
        ("quiz", {"title": "READING. Выбери правильный ответ на каждый вопрос",
                  "questions": [
                      q1("What's the writer's mum's job?", ["doctor", "nurse", "vet", "farmer"], 2),
                      q1("What did Mum do first yesterday?",
                         ["walked the dog", "made breakfast", "went to work", "tidied the kitchen"], 1),
                      q1("Where does the writer's mum work?",
                         ["in a hospital for people", "in an animal hospital", "at home", "in a school"], 1),
                      q1("Why was Mum sad in the morning?",
                         ["The man wasn't friendly.", "The cat was very ill.", "She was tired.",
                          "The cat didn't like her."], 1),
                      q1("How long did Mum help the little bird?",
                         ["half an hour", "one hour", "two hours", "all afternoon"], 2),
                      q1("After work, Mum…",
                         ["was happy and energetic", "was tired but happy with her job",
                          "didn't want to do anything", "was angry"], 1),
                  ]}),
        audio("LISTENING. Послушай, как четыре человека рассказывают о том, что они делали вчера 🎧",
              "аудио LISTENING теста: четыре человека рассказывают, что делали вчера (Speaker 1–4)"),
        ("sort", {"title": "LISTENING. Соедини каждого человека с двумя фактами о том, что он делал",
                  "groups": [
                      {"name": "Speaker 1", "items": [{"text": "is a builder"}, {"text": "watched TV after work"}]},
                      {"name": "Speaker 2", "items": [{"text": "bought food at the supermarket"},
                                                      {"text": "read a book in the evening"}]},
                      {"name": "Speaker 3", "items": [{"text": "made food for fifty people"},
                                                      {"text": "ordered a sandwich for dinner"}]},
                      {"name": "Speaker 4", "items": [{"text": "walked the dog in the evening"},
                                                      {"text": "is a nurse"}]},
                  ]}),
        ("speaking", {"title": "SPEAKING I 🎤",
                      "needs_review": True,
                      "image": img(U, "scene_cleaning"),
                      "html": "<p>Опиши картинку и ответь на вопросы. Запиши ответ, нажав на кнопку "
                              "микрофона.</p>"
                              "<ol><li>How many people are there in the picture?</li>"
                              "<li>Where are they?</li><li>What is each person doing?</li>"
                              "<li>Are the children helping their parents?</li></ol>"}),
        ("speaking", {"title": "SPEAKING II 🎤",
                      "needs_review": True,
                      "html": "<p>Ответь на вопросы. Запиши ответ, нажав на кнопку микрофона.</p>"
                              "<ol><li>What do you want to be in the future: a doctor, a teacher, an artist "
                              "or something else?</li>"
                              "<li>What's the most interesting job in your opinion?</li>"
                              "<li>Is being a chef difficult?</li><li>Where does a vet work?</li>"
                              "<li>Where did you go last weekend?</li>"
                              "<li>What time did you get up today?</li>"
                              "<li>Did you tidy your room yesterday?</li>"
                              "<li>Did you walk the dog this week?</li></ol>"}),
    ]},
}
