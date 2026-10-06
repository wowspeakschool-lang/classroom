"""Go Getter 2 · Unit 8 · Celebrations — домашки 1–6 и тест юнита.

Источник содержания — docs/GG2_разбор_u8.md. Подтверждённые правки (Анна, 05.10.2026):
HW2 (1)·12 ключ «going» (не «going to»), HW2 (1)·8 «her homework».
"""
from gg2_build import img, shared, todo, video

U = "u8"
UNIT = {"unit": U, "unit_title": "Unit 8", "unit_sort": 8}


def hello(name, title, *paras):
    body = "".join(f"<p>{p}</p>" for p in paras)
    return ("text", {"html": f'<p><img src="{shared(name)}" alt="" style="height:200px"></p><h2>{title}</h2>{body}'})


def bye(name, title, *paras):
    body = "".join(f"<p>{p}</p>" for p in paras)
    return ("text", {"html": f'<p><img src="{shared(name)}" alt="" style="height:180px"></p><h3>{title}</h3>{body}'})


def text(*paras, h=None, image=None):
    out = f"<h3>{h}</h3>" if h else ""
    out += "".join(f"<p>{p}</p>" for p in paras)
    if image:
        out += f'<p><img src="{image}" alt="" style="max-width:100%"></p>'
    return ("text", {"html": out})


def q(question, options, correct, image=None):
    d = {"q": question, "type": "single", "options": [{"text": o} for o in options], "correct": [correct]}
    if image:
        d["image"] = image
    return d


def order(sentence_words, image=None):
    s = " ".join(sentence_words)
    d = {"words": list(sentence_words), "sentence": s, "audio_tts": s}
    if image:
        d["image"] = image
    return ("order", d)


def gaps(title, mode, body, n, image=None):
    d = {"title": title, "mode": mode, "text": body, "gaps_expected": n}
    if image:
        d["image"] = image
    return ("gaps", d)


# ---------- словарь ----------

EVENTS = [  # (англ, рус, картинка)
    ("barbecue", "барбекю", "barbecue"),
    ("birthday party", "праздник в честь дня рождения", "birthday_party"),
    ("concert", "концерт", "concert"),
    ("dance show", "танцевальное шоу", "dance_show"),
    ("football match", "футбольный матч", "football_match"),
    ("fancy dress party", "костюмированная вечеринка", "fancy_dress"),
    ("picnic", "пикник", "picnic"),
    ("play", "пьеса", "play"),
    ("sleepover", "ночёвка", "sleepover"),
    ("talent competition", "конкурс талантов", "talent_competition"),
]

ACTIONS = [
    ("cook food", "готовить пищу", "cook_food"),
    ("get presents", "получать подарки", "get_presents"),
    ('sing "Happy Birthday"', "спеть «С днём рождения»", "sing_birthday"),
    ("sleep on the floor", "спать на полу", "sleep_floor"),
    ("take part in a competition", "принять участие в конкурсе", "competition"),
    ("wear a costume", "носить костюм", "wear_costume"),
]

ORDINALS = [
    ("the first", "первый"), ("the second", "второй"), ("the third", "третий"),
    ("the fourth", "четвёртый"), ("the fifth", "пятый"), ("the sixth", "шестой"),
    ("the seventh", "седьмой"), ("the eighth", "восьмой"), ("the ninth", "девятый"),
    ("the tenth", "десятый"), ("the eleventh", "одиннадцатый"), ("the twelfth", "двенадцатый"),
    ("the thirteenth", "тринадцатый"), ("the twentieth", "двадцатый"), ("the thirtieth", "тридцатый"),
    ("the twenty-first", "двадцать первый"), ("the forty-second", "сорок второй"),
    ("the first of September", "первое сентября"), ("the second of April", "второе апреля"),
    ("the thirty-first of December", "тридцать первое декабря"),
]


def flashcards(words):
    return ("flashcards", {"cards": [
        {"text": en, "translation": ru, "image": img(U, f), "audio_tts": en.replace('"', "")}
        for en, ru, f in words]})


def match_pics(words, title):
    return ("match", {"title": title, "pairs": [
        {"left_image": img(U, f), "right": en, "right_audio_tts": en.replace('"', "")}
        for en, ru, f in words]})


def match_text(pairs, title):
    return ("match", {"title": title, "pairs": [
        {"left": l, "right": r, "right_audio_tts": r} for l, r in pairs]})


LESSONS = {
    # ------------------------------------------------------------------ HW1
    "u8_hw1": {**UNIT, "lesson_title": "Homework 1", "lesson_sort": 0, "kind": "homework", "blocks": [
        # часть (1) — словарный тренажёр
        hello("hello_wave", "Привет! 👋",
              "Надеюсь, ты любишь вечеринки! Сегодня мы изучим слова, которые ты сможешь использовать "
              "на мероприятиях 😋",
              "Выполни все задания, чтобы выучить слова на 100%!"),
        flashcards(EVENTS),
        match_pics(EVENTS, "Соедини картинки со словами"),
        ("exact_input", {"items": [
            {"prompt": f"Напиши по-английски: {ru}", "accept": [en], "audio_tts": en}
            for en, ru, f in EVENTS]}),
        # часть (2) — словарный тренажёр
        text("Что ты любишь делать на вечеринках? Выучи ещё шесть фраз — и выполни задания, "
             "чтобы запомнить их на 100%!", h="Что делают на празднике 🎉"),
        flashcards(ACTIONS),
        match_pics(ACTIONS, "Соедини картинки с фразами"),
        ("quiz", {"title": "Как это по-английски?", "questions": [
            q("Как по-английски «готовить пищу»?", ["get presents", "cook food", "wear a costume"], 1),
            q("Как по-английски «получать подарки»?", ["get presents", "sleep on the floor", "cook food"], 0),
            q("Как по-английски «спеть «С днём рождения»»?",
              ["take part in a competition", "get presents", 'sing "Happy Birthday"'], 2),
            q("Как по-английски «спать на полу»?", ["wear a costume", "sleep on the floor", "cook food"], 1),
            q("Как по-английски «принять участие в конкурсе»?",
              ["take part in a competition", 'sing "Happy Birthday"', "sleep on the floor"], 0),
            q("Как по-английски «носить костюм»?", ["cook food", "get presents", "wear a costume"], 2),
        ]}),
        # часть (3)
        hello("hello_highfive", "Привет ещё раз! 🙌",
              "Добро пожаловать в третью ДОПОЛНИТЕЛЬНУЮ часть домашнего задания. Выполни все задания, "
              "чтобы хорошенько запомнить новые слова!",
              "Выполнив эти задания, ты станешь БОЛЬШИМ МОЛОДЦОМ!"),
        ("quiz", {"title": "Выбери подходящее по смыслу слово", "questions": [
            q("Dad's cooking meat on the ___.", ["party", "barbecue"], 1, img(U, "barbecue")),
            q("We're having a ___ at Tracy's house tonight!", ["sleepover", "lunch"], 0, img(U, "sleepover_girls")),
            q("We're enjoying a great ___! I'm 12 today!", ["birthday party", "concert"], 0,
              img(U, "birthday_party")),
            q("Maria is doing ballet in the ___.", ["football match", "dance show"], 1, img(U, "dance_show")),
        ]}),
        text("Молодец! А теперь прочти текст об Анне! Узнай, чем занимается её семья и у кого какие хобби."),
        gaps("Прочитай текст ещё раз и впиши пропущенные слова", "type",
             "Hi, I'm Anna. The people in my family do interesting things. My grandad loves sport so he "
             "usually sees a football __match__ at the weekend at the stadium. Mum likes the theatre so she "
             "often sees a __play__. I like wearing costumes so I always have a fancy __dress__ party on my "
             "birthday. My older brother James is a good singer. He loves music and often goes to a "
             "__concert__ to hear his favourite band. My uncle, Paul, is also a good singer. He wants to be "
             "famous, so he is in a __talent competition__ at the moment. I hope he wins! Dad loves being "
             "outdoors. So he often takes us to the park for a __picnic__. He makes all the sandwiches!",
             6, image=img(U, "anna")),
        ("task", {"title": "Дополнительное задание — для самых смелых! 💪", "needs_review": True,
                  "html": "<p>Прочти ещё раз текст об Анне в предыдущем упражнении и письменно перечисли: "
                          "какие увлечения у твоей семьи.</p>"
                          "<p><i>Например: My mum often sees a play. My brother loves football matches.</i></p>"}),
        bye("well_done_star", "Поздравляю! 🎉",
            "Ты завершил домашнее задание. Ты — БОЛЬШОЙ МОЛОДЕЦ! Жду тебя на уроке!"),
    ]},

    # ------------------------------------------------------------------ HW2
    "u8_hw2": {**UNIT, "lesson_title": "Homework 2", "lesson_sort": 1, "kind": "homework", "blocks": [
        hello("hello_wave", "Добро пожаловать! 👋",
              "Сегодня мы с тобой научимся рассказывать о своих планах на будущее.",
              "В конце тебя будет ждать дополнительное задание. Если ты его сделаешь, получишь звание "
              "чемпиона английского 💪"),
        text("Для начала посмотри видео. Что собирается делать Hammy на каникулах?",
             image=img(U, "book_hammy_holiday")),
        video("Посмотри видео: что собирается делать Hammy на каникулах?",
              "мультфильм Hammy о планах на каникулы (be going to), из выгрузки не выгрузился"),
        ("quiz", {"title": "Посмотри видео ещё раз и выбери правильный вариант для каждого пропуска",
                  "questions": [
            q("What ___ you going to do on holidays?", ["is", "are"], 1),
            q("I ___ swim in the sea.", ["am going to", "is going to"], 0),
            q("I ___ to eat lots of food.", ["likes", "am going"], 1),
            q("My dad ___ drive to France.", ["is going to", "am going to"], 0),
        ]}),
        text("Отлично, ты посмотрел видео и выполнил задание, а теперь переходим к практике!",
             "Расставь слова в правильном порядке, чтобы получилось предложение."),
        order(["We", "are", "not", "going", "to", "see", "our", "grandmother", "this", "summer."],
              img(U, "grandma_cottage")),
        order(["Are", "you", "going", "to", "come", "to", "my", "party", "tomorrow?"], img(U, "birthday_party")),
        order(["I", "am", "going", "to", "go", "to", "Japan", "to", "see", "sakura."], img(U, "sakura")),
        order(["She", "is", "going", "to", "do", "her", "homework", "in the evening."], img(U, "homework_girl")),
        text("Молодец! Ты справился с большей частью заданий. Давай ещё немного потренируемся!",
             "Посмотри на картинки и выбери правильный вариант ответа!"),
        ("quiz", {"title": "Выбери правильный вариант ответа", "questions": [
            q("We ___ going to paint our bedroom tomorrow.", ["aren't", "isn't", "am not"], 0,
              img(U, "paint_bedroom")),
            q("I ___ going to go on holiday next week.", ["is", "are", "am"], 2, img(U, "beach_holiday")),
            q("She is ___ to the cinema tonight.", ["going to", "going", "go to"], 1, img(U, "cinema_tonight")),
            q("He's going to ___ the book.", ["reading", "read"], 1, img(U, "boy_reading")),
        ]}),
        match_text([
            ("I'm going to buy tickets to the", "cinema tomorrow."),
            ("Are you going to come to my birthday", "party next week?"),
            ("My favourite singer is going to", "sing at the concert this Friday."),
            ("I am going to wear a vampire costume", "for a fancy dress party this Saturday."),
            ("My best friend Kate is going to come to my house", "for a sleepover this weekend."),
            ("They are going to take part in a", "dance show at school next month."),
        ], "Ты большой молодец! Осталось ещё пару заданий! Внимательно прочитай слова и найди продолжения "
           "предложений."),
        ("task", {"title": "Дополнительное задание — для самых смелых! 💪", "needs_review": True,
                  "html": "<p>Мне очень интересно, что ты и твоя семья планируете делать на каникулах. "
                          "Письменно напиши 3 предложения о себе и 3 предложения о членах семьи.</p>"
                          "<p><i>Например: I am going to swim in the sea. My grandma is going to play golf.</i></p>"}),
        bye("well_done_trophy", "Ура! 🎉",
            "Ты справился с домашней работой. Ты — большой молодец! Увидимся на занятии!"),
        # часть (2) — словарный тренажёр: порядковые числительные и даты
        text("Выучи порядковые числительные и даты — они пригодятся, чтобы рассказать, когда у тебя "
             "праздник. Послушай каждую карточку и повтори вслух.", h="Бонус: числа и даты 📅"),
        ("flashcards", {"cards": [{"text": en, "translation": ru, "audio_tts": en} for en, ru in ORDINALS]}),
        match_text([
            ("1st", "the first"), ("2nd", "the second"), ("3rd", "the third"), ("5th", "the fifth"),
            ("8th", "the eighth"), ("12th", "the twelfth"), ("20th", "the twentieth"),
            ("21st", "the twenty-first"), ("30th", "the thirtieth"), ("42nd", "the forty-second"),
        ], "Соедини числа с их названиями"),
        ("quiz", {"title": "Выбери, как сказать дату по-английски", "questions": [
            q("1 сентября", ["the first of September", "the one of September", "the first September of"], 0),
            q("2 апреля", ["the two of April", "the second April", "the second of April"], 2),
            q("31 декабря", ["the thirty-one of December", "the thirty-first of December",
                             "the thirtieth of December"], 1),
        ]}),
    ]},

    # ------------------------------------------------------------------ HW3
    "u8_hw3": {**UNIT, "lesson_title": "Homework 3", "lesson_sort": 2, "kind": "homework", "blocks": [
        hello("hello_rocket", "Привет! 👋",
              "В этом уроке тебя ждёт интересное видео и классные задания!",
              "В конце урока есть дополнительное задание — его можно выполнить по желанию, НО если выполнишь, "
              "то будешь нереально крут!"),
        text("Для начала посмотри видео! Как думаешь, почему Hammy так недоволен?",
             image=img(U, "book_hammy_angry")),
        video("Посмотри видео: почему Hammy так недоволен?",
              "эпизод Hammy с вопросами Is he asleep? / Can Hammy swim? / Does he like biscuits? и т.п., "
              "из выгрузки не выгрузился"),
        match_text([
            ("Is he asleep?", "Yes, he is."),
            ("Can Hammy swim?", "Yes, he can."),
            ("Does he like biscuits?", "No, he doesn't."),
            ("Did he exercise this morning?", "No, he didn't."),
            ("Do you love your pet?", "Yes, we do!"),
        ], "Посмотри видео ещё раз и соедини вопросы и ответы."),
        text("Замечательно! Мы с тобой посмотрели видео, а теперь перейдём к практике!",
             "Посмотри на предложения ниже. Расставь слова в правильном порядке."),
        order(["Are", "you", "wearing", "my", "clothes?"], img(U, "armful_clothes")),
        order(["What", "did", "you", "have", "for", "breakfast?"]),
        order(["Do", "you", "want", "tickets", "for", "a", "concert?"], img(U, "concert_tickets")),
        order(["Have", "you", "got", "a boyfriend?"], img(U, "flowers")),
        order(["Where", "does", "she", "buy", "her", "clothes?"], img(U, "shop_window")),
        match_text([
            ("What did you have for breakfast?", "I had sausages and eggs."),
            ("Where were you last week?", "I was in New York. I played two concerts there."),
            ("Do you live in a big house?", "Yes, I do. It's got seven bedrooms."),
            ("Can you play the guitar?", "No, I can't. But I can sing and rap."),
            ("Does your mom like rap music?", "No, she doesn't. She hates it!"),
            ("Are you in an ice hotel?", "Yes, I am. It's very nice."),
        ], "Отлично! Ты хорошо справляешься! Сопоставь вопросы и ответы."),
        text("Отлично! А теперь давай поговорим немного о музыке! Какая музыка тебе нравится? "
             "Какие виды музыки ты знаешь?",
             "Посмотри на картинки в упражнении и выбери правильный вариант!", h="Types of music 🎵"),
        todo(("quiz", {"title": "Какая это музыка?", "questions": [
            q("What type of music is it?", ["pop", "rock", "jazz"], 1, img(U, "rock")),
            q("What type of music is it?", ["pop", "country", "classical"], 0, img(U, "pop")),
            q("What type of music is it?", ["rap", "rock", "classical"], 2, img(U, "classical")),
            q("What type of music is it?", ["rap", "jazz", "country"], 0, img(U, "rap")),
            q("What type of music is it?", ["classical", "jazz", "pop"], 1, img(U, "jazz")),
            q("What type of music is it?", ["rock", "rap", "country"], 2, img(U, "country")),
        ]}), ("game", "СОСТАВ МОЙ: пересобрана игра Wordwall «Go getter 2 Unit 8.3 types of music» "
                      "(quiz, картинка → тип музыки: rock, pop, classical, rap, jazz, country)")),
        ("task", {"title": "Дополнительное задание — для самых больших умников! 🧠", "needs_review": True,
                  "html": "<p>Отлично, ты справился с основной частью домашнего задания! Это задание "
                          "дополнительное, но ты будешь мегакрутым учеником, если выполнишь его!</p>"
                          "<p>Придумай 3 вопроса для своих одноклассников! Не забудь задать их на уроке!</p>"}),
        bye("congrats_popper", "Поздравляю! 🎉",
            "Ты завершил домашнее задание, ты замечательный ученик! Увидимся на занятии!"),
    ]},

    # ------------------------------------------------------------------ HW4
    "u8_hw4": {**UNIT, "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework", "blocks": [
        hello("hello_book", "Привет! 👋",
              "Готов выполнять домашнее задание? В этом уроке тебя ждёт интересное видео и классные задания!",
              "В конце урока есть дополнительное задание — его можно выполнить по желанию, НО если выполнишь, "
              "то будешь нереально крут!"),
        text("Давай начнём с просмотра видео! Куда собираются пойти ребята?"),
        video("Посмотри видео: куда собираются пойти ребята?",
              "диалог-приглашение (Are you busy next Thursday? … Let's meet outside the Arena), "
              "из выгрузки не выгрузился"),
        match_text([
            ("Are you busy next Thursday?", "No. Why?"),
            ("Would you like to come?", "That sounds great! I'd love to come."),
            ("What time does it start?", "At half past six."),
            ("Where shall we meet?", "Let's meet outside the Arena at six o'clock."),
        ], "Посмотри видео выше и соедини вопросы с ответами."),
        gaps("Прочитай диалог и впиши пропущенные слова", "type",
             "Maria: Hi Alison. Are you __busy__ next Tuesday?\n"
             "Alison: No. Why?\n"
             "Maria: I've got four tickets for a dance show. __Would you__ and your mum like to come?\n"
             "Alison: __I'd love|I'd like|I would love|I would like|I’d love|I’d like__ to come. "
             "Let's text my mum and ask. What time does it start?\n"
             "Maria: At half past seven. It's at the Old Theatre near the underground.\n"
             "Alison: Great, Mum texted me and said yes. Where __shall we__ meet?\n"
             "Maria: __Let's meet|Let’s meet|Let us meet__ outside the underground station at seven o'clock.\n"
             "Alison: Great. See you then.", 5),
        text("Давай ещё немного потренируемся! Соедини первую часть предложения со второй!"),
        match_text([
            ("Are you", "busy next Tuesday?"),
            ("I've got tickets", "for a football match."),
            ("Would you", "like to come?"),
            ("That sounds", "great."),
            ("I'd", "love to come."),
            ("What time", "does it start?"),
            ("Where shall", "we meet?"),
            ("Let's meet at five", "o'clock at my house."),
        ], "Посмотри внимательно на предложения! Попробуй соединить их!"),
        text("Ты такой молодец! Давай ещё немного потренируемся! Расставь слова в предложениях "
             "в правильном порядке!"),
        order(["Are", "you", "busy", "next", "Thursday?"]),
        order(["Would", "you", "like", "to", "come?"]),
        order(["Where", "shall", "we", "meet?"]),
        order(["I'd", "love", "to", "come."]),
        order(["What", "time", "does", "it", "start?"]),
        text("Молодец! Осталось ДОПОЛНИТЕЛЬНОЕ задание. Оно необязательное, но если ты его сделаешь, "
             "получишь дополнительный балл на уроке! У тебя обязательно получится! Так держать!"),
        ("task", {"title": "Дополнительное задание: напиши свой диалог ✍️", "needs_review": True,
                  "html": "<p>Посмотри внимательно на билеты и изучи информацию на них! Выбери один из "
                          "билетов и напиши свой диалог-приглашение. Для примера ты можешь использовать "
                          "диалог из предыдущих заданий!</p>"
                          f'<p><img src="{img(U, "book_tickets")}" alt="Tickets" style="max-width:100%"></p>'}),
        bye("well_done_trophy", "Отлично! 🏆",
            "Ты справился со всеми заданиями. Ты — большой молодец. Держи за это кубок победителя. "
            "Жду тебя на занятии!"),
    ]},

    # ------------------------------------------------------------------ HW5
    "u8_hw5": {**UNIT, "lesson_title": "Homework 5", "lesson_sort": 4, "kind": "homework", "blocks": [
        hello("hello_headphones", "Hello! 👋",
              "Сегодня мы с тобой попрактикуемся в чтении и сделаем много интересных упражнений!",
              "Не забудь про дополнительное задание! Оно тебе понравится! Готов начать?"),
        text("Для начала внимательно прочитай текст ниже!", h="Running for fun! 🏃",
             image=img(U, "book_running_poster")),
        ("match", {"title": "Прочитай текст ещё раз и соедини картинки с названиями!", "pairs": [
            {"left_image": img(U, "fun_races"), "right": "Fun Races!", "right_audio_tts": "Fun Races"},
            {"left_image": img(U, "winter_run"), "right": "Winter Run!", "right_audio_tts": "Winter Run"},
            {"left_image": img(U, "costume_run"), "right": "Costume Run!", "right_audio_tts": "Costume Run"},
        ]}),
        text("Молодец! Прочитай вопросы по тексту и выбери правильный ответ: <b>yes</b> или <b>no</b>."),
        ("quiz", {"title": "Yes or no?", "questions": [
            q("Can families run in all the events?", ["yes", "no"], 1),
            q("Is there a hot meal for the runners in the Winter Run?", ["yes", "no"], 0),
            q("Can children over 12 run in the Fun Races?", ["yes", "no"], 1),
            q("Are there three races in the Winter Run?", ["yes", "no"], 1),
            q("Are there three races in the Costume Run?", ["yes", "no"], 0),
            q("Is there a picnic at the Tree Park event?", ["yes", "no"], 0),
        ]}),
        text("Давай ещё немного потренируемся! Как хорошо ты прочитал текст? Ответь на вопросы ниже!"),
        ("quiz", {"title": "Ответь на вопросы по тексту", "questions": [
            q("Which event is in a forest?", ["Winter Run!", "Fun Races!", "Costume Run!"], 0),
            q("Which event is in a park?", ["Winter Run!", "Fun Races!", "Costume Run!"], 2),
            q("Who can run in the Costume Run?", ["families", "children aged 7–12", "children in costumes"], 2),
            q("What can you do in the afternoon at New Park School?",
              ["play basketball", "have some soup", "have a picnic"], 0),
            q("What do you wear in the basketball game after the Fun Races?", ["a costume", "gloves", "a hat"], 1),
            q("What food do you need for the Fun Races event?", ["a soup", "an egg", "an apple"], 1),
        ]}),
        ("task", {"title": "Дополнительное задание — для настоящих чемпионов! 🏅", "needs_review": True,
                  "html": "<p>Ответь на вопросы:</p><ol>"
                          "<li>What is your favourite running event in the text?</li>"
                          "<li>Do you like running?</li><li>Can you run 50 metres?</li>"
                          "<li>Can you run two kilometres?</li>"
                          "<li>Do you think running is better in winter or summer?</li></ol>"
                          "<p>Не забудь прочитать свои ответы учителю на уроке!</p>"}),
        bye("well_done_jump", "Ура! 🎉",
            "Ты справился с домашним заданием! Ты — мегакрут! Увидимся на занятии. Goodbye!"),
    ]},

    # ------------------------------------------------------------------ HW6
    "u8_hw6": {**UNIT, "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework", "blocks": [
        # часть (1)
        hello("hello_headphones", "Hello! 👋",
              "Сегодня мы с тобой попрактикуемся в чтении и аудировании! Тебя ждёт много интересных заданий! "
              "Готов начать?"),
        video("Послушай аудиозапись: как ребята собираются провести дни рождения? Чей праздник тебе "
              "понравился больше всего?",
              "аудио: ребята (Tina, Harry, Robert, Kelly, David) рассказывают, как проведут дни рождения; "
              "из выгрузки не выгрузилось"),
        match_text([
            ("Tina", "see a dance show"),
            ("Harry", "go to the cinema"),
            ("Robert", "birthday party at home"),
            ("Kelly", "go bowling"),
            ("David", "eat at a restaurant"),
        ], "Послушай аудиозапись ещё раз и соедини имена ребят с событиями!"),
        gaps("Послушай аудиозапись ещё раз и расставь слова по смыслу", "drag",
             "1. Tina has a ticket for her __sister__.\n"
             "2. Harry is going to go out with his __brother__.\n"
             "3. Robert's __mum__ is making a cake.\n"
             "4. Kelly and her __uncle__ love the same activity.\n"
             "5. David is going to go out with his __dad__.", 5),
        todo(text("SUPER! Ты справился с аудированием! У меня для тебя есть приглашение на вечеринку, "
                  "но оно незаполненное! Прочитай его в следующем задании и вставь пропущенные слова.",
                  image=img(U, "invitation")),
             ("check", "картинка приглашения из выгрузки не попала (блок был пустой); вопрос «What is the "
                       "name of the party?» убран — без картинки на него нет ответа. Если исходник найдётся — "
                       "вставить сюда")),
        todo(gaps("Прочитай приглашение и вставь пропущенные слова по смыслу", "drag",
                  "PARTY INVITATION\n"
                  "On: Tuesday, 3rd __August__, at 4:30 __p.m.__\n"
                  "__At__: Fun Times Sport Centre\n"
                  "We're going to go swimming and then eat pancakes.\n"
                  "__Please__ bring towels for the swimming.\n"
                  "Your parents can __collect__ you from Patty's Pancakes at 9 o'clock.\n"
                  "Please __reply__ to 678954321.", 6),
             ("check", "в исходнике «Please reply to ___ or 678954321» — перед «or» было пусто (имя/почта "
                       "потеряны), оставлено «Please reply to 678954321»")),
        ("quiz", {"title": "Прочитай приглашение ещё раз и ответь на вопросы", "questions": [
            q("What day is the party going to happen?", ["Wednesday", "Tuesday", "Friday"], 1),
            q("Where is the party going to happen?",
              ["At Fun Times Sport Centre", "At Swimming pool", "At School"], 0),
            q("What are they going to do first?", ["play football", "play basketball", "go swimming"], 2),
            q("What do they need to bring?", ["boots", "towels", "hats"], 1),
            q("What are they going to eat?", ["salads", "fruits", "pancakes"], 2),
            q("What time is the party going to finish?", ["at 9 o'clock", "at 6 o'clock", "at 10 o'clock"], 0),
        ]}),
        text("Ты большой молодец! У меня для тебя есть дополнительное задание! Оно необязательное, но если "
             "ты его выполнишь, ты будешь МЕГА КРУТ!"),
        ("task", {"title": "Дополнительное задание: твоё приглашение 💌", "needs_review": True,
                  "html": "<p>Подумай, куда бы ты хотел пригласить друзей! Напиши своё приглашение! "
                          "Используй вопросы из предыдущего задания — они помогут тебе составить "
                          "приглашение.</p><p>Не забудь показать своё приглашение учителю на уроке!</p>"}),
        bye("well_done_clap", "Ура! 🎉",
            "Ты справился с первой частью домашнего задания! Ты — мегакрут! А теперь — повторение перед тестом."),
        # часть (2)
        hello("hello_laptop", "Hello! 👋",
              "Сегодня мы будем повторять изученный материал, чтобы ты смог хорошо подготовиться к тесту :) "
              "Давай начнём!"),
        match_pics(EVENTS, "Посмотри на картинки и соедини их с названиями!"),
        text("Отлично! Давай ещё потренируемся! Соедини цифры и их названия ниже!"),
        match_text([
            ("24th", "twenty-fourth"), ("1st", "first"), ("2nd", "second"),
            ("3rd", "third"), ("7th", "seventh"), ("6th", "sixth"),
        ], "Соедини цифры и их названия"),
        text("Ты отлично справляешься! А теперь давай повторим грамматику! Внимательно посмотри на слова "
             "и расставь их в правильном порядке!"),
        order(["I", "am", "going", "to", "visit", "my", "grandpa", "on", "Monday."]),
        order(["We", "are", "going", "to", "have", "a", "party", "on", "Saturday."]),
        order(["He", "is", "going", "to", "travel", "by", "plane."]),
        order(["They", "are", "not", "going", "to", "play", "football", "next", "week."]),
        text("МОЛОДЕЦ! А сейчас мы с тобой вспомним вопросы! Внимательно прочитай слова и расставь их "
             "по порядку!"),
        todo(order(["Is", "he", "asleep?"]),
             ("game", "СОСТАВ МОЙ: пересобрана игра Wordwall «Go Getter (2) 8.3 Yes/No questions» (unjumble) — "
                      "пять блоков order подряд из вопросов Homework 3: Is he asleep? Can Hammy swim? "
                      "Does he like biscuits? Did he exercise this morning? Do you love your pet?")),
        order(["Can", "Hammy", "swim?"]),
        order(["Does", "he", "like", "biscuits?"]),
        order(["Did", "he", "exercise", "this", "morning?"]),
        order(["Do", "you", "love", "your", "pet?"]),
        bye("well_done_star", "Hooray! 🌟",
            "Домашняя работа выполнена на отлично, всё благодаря твоим стараниям. Теперь ты готов к тесту "
            "на 100%! Увидимся на занятии!"),
    ]},

    # ------------------------------------------------------------------ TEST
    "u8_test": {**UNIT, "lesson_title": "Unit 8 Test", "lesson_sort": 6, "kind": "test", "blocks": [
        ("exact_input", {"items": [
            {"prompt": f"Напиши по-английски: {ru}", "accept": [en], "audio_tts": en}
            for en, ru in [("barbecue", "барбекю"), ("dance show", "танцевальное шоу"),
                           ("fancy dress party", "костюмированная вечеринка"), ("picnic", "пикник"),
                           ("sleepover", "ночёвка"), ("talent competition", "конкурс талантов")]]}),
        todo(("quiz", {"title": "Выбери правильный вариант, чтобы предложение было грамматически верным",
                       "questions": [
            q("We ___ to have a barbecue on Saturday.", ["going to have", "are going", "going"], 1),
            q("My sister ___ to the concert with us.",
              ["not going to come", "doesn't going to come", "isn't going to come"], 2),
            q("___ invite Tom to your party?", ["Do you going to", "You are going to", "Are you going to"], 2),
            q("___ going to wear to the fancy dress party?", ["What is Anna", "What does Anna", "What Anna is"], 0),
            q("___ last weekend?", ["Where you went", "Where did you go", "Where did you went"], 1),
        ]}), ("check", "вопрос 2: в исходнике «My sister ___ to come to the concert» с ключом «isn't going to» — "
                       "получалось «isn't going to to come». Переписано «My sister ___ to the concert with us», "
                       "ключ «isn't going to come» (неверные из исходника: not going to come, doesn't going to come)")),
        gaps("Поставь глагол в скобках в правильную форму с be going to", "type",
             "1. On the twenty-first of June, we __are going to celebrate|'re going to celebrate|’re going to celebrate__ "
             "(celebrate) my dad's birthday.\n"
             "2. They __aren't going to watch|are not going to watch|aren’t going to watch|'re not going to watch__ "
             "(not watch) the football match — they hate football.\n"
             "3. __Is__ Liam __going to play__ (play) at the talent competition?\n"
             "4. I __am going to have|'m going to have|’m going to have__ (have) a sleepover with my best friend "
             "on Friday.\n"
             "5. What __are you going to do__ (do) on the thirty-first of December?", 6),
        text("Расставь части предложения в правильном порядке."),
        order(["We", "are", "going", "to have", "a picnic", "in the park."]),
        order(["Are", "you", "going", "to wear", "a costume", "to the fancy", "dress party?"]),
        order(["My", "birthday", "is", "on", "the twelfth", "of May."]),
        order(["They", "aren't", "going", "to listen", "to classical", "music", "tonight."]),
        order(["What", "time", "are", "we", "going", "to meet", "on Sunday?"]),
        ("text", {"html":
            "<h3>READING 📖</h3><p>Прочитай приглашение Маркуса и сообщения. Потом перетащи слова в пропуски "
            "в предложениях.</p>"
            "<h4>Markus's Invitation</h4>"
            "<p><b>Please come to my 13th birthday party!</b><br>"
            "<b>When:</b> Saturday, the seventh of June, at 4 p.m.<br>"
            "<b>Where:</b> 25 Park Road<br>"
            "<b>Theme:</b> Fancy dress – favourite singer or band!<br>"
            "<b>RSVP</b> by Wednesday.</p>"
            "<h4>Messages between Markus and his friends</h4>"
            "<p><b>Anna:</b> Hi Markus! Thanks for the invitation! I'm going to come, of course! I'm going to "
            "wear a Taylor Swift costume – I'm her biggest fan!<br>"
            "<b>Markus:</b> Cool! Can't wait!<br>"
            "<b>Tom:</b> Sorry mate, I can't come. My family is going to Spain on the seventh of June. We're going "
            "to be there for two weeks. I'll bring you a present when I'm back!<br>"
            "<b>Markus:</b> No problem! Have a great holiday!<br>"
            "<b>Lily:</b> Hi! I'd love to come, but I don't have a costume! Can I just wear normal clothes?<br>"
            "<b>Markus:</b> Of course! It's not a problem. Are you going to bring your sister?<br>"
            "<b>Lily:</b> Yes! She loves rap music, so she's going to come as a famous rapper!</p>"}),
        gaps("Перетащи слова в пропуски", "drag",
             "1. The party is on the __seventh__ of June.\n"
             "2. Anna is going to come as __Taylor Swift__.\n"
             "3. Tom __isn't going to__ come to the party.\n"
             "4. Tom and his family are going on holiday for __two weeks__.\n"
             "5. Lily isn't going to wear a __costume__.\n"
             "6. Lily's sister loves __rap__ music.", 6),
        video("LISTENING 🎧 Послушай разговор Софи и Бена о субботе.",
              "аудио теста: разговор Софи и Бена о субботе (конкурс талантов, встреча в кафе); "
              "из выгрузки не выгрузилось"),
        ("sequence", {"title": "Расставь реплики Бена в том порядке, в котором он их говорит", "items": [
            {"text": "Hi Sophie! Yes, I am. Why?"},
            {"text": "A talent competition? Sounds fun! What time does it start?"},
            {"text": "OK, great. Where shall we meet?"},
            {"text": "Good idea! I love that café. What are you going to wear?"},
            {"text": "Cool. Is anyone else coming?"},
            {"text": "Amazing! See you on Saturday at half past five at the café!"},
        ]}),
        ("speaking", {"title": "SPEAKING I 🎤", "needs_review": True, "image": img(U, "scene_birthday"),
                      "html": "<p>Опиши картинку и ответь на вопросы. Запиши ответ, нажав на кнопку "
                              "микрофона (до 5 минут).</p><ol>"
                              "<li>What event is this?</li><li>How many people are there?</li>"
                              "<li>What are they wearing?</li><li>What food and drinks can you see?</li>"
                              "<li>What are they going to do next — open the presents, eat the cake or dance?</li>"
                              "</ol>"}),
        ("speaking", {"title": "SPEAKING II 🎤", "needs_review": True,
                      "html": "<p>Ответь на вопросы полными предложениями. Запиши ответ, нажав на кнопку "
                              "микрофона (до 5 минут).</p><ol>"
                              "<li>When is your birthday?</li>"
                              "<li>How are you going to celebrate your next birthday?</li>"
                              "<li>What's your favourite type of music?</li>"
                              "<li>What are you going to do next weekend?</li>"
                              "<li>Are you going to study English this evening?</li>"
                              "<li>What did you do last weekend?</li>"
                              "<li>Do you like sleepovers? Who do you usually have sleepovers with?</li>"
                              "<li>What's the best birthday present you ever got?</li></ol>"}),
    ]},
}
