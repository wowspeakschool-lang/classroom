"""Go Getter 2 · Unit 1 · School — 7 домашек и тест.

Источник: docs/GG2_разбор_u1.md. Ключи «Не указано» в «верно/неверно»
Homework 5 и теста (утв. 6) заменены на «Неверно» — правка принята Анной
05.10.2026 (docs/GG2_доработать_руками.md, «Закрытые вопросы», п. 4).
Промо-баннер «Новогодний челлендж» выброшен во всех уроках.
"""
from gg2_build import img, shared, todo, video

U = "u1"
UNIT = {"unit": U, "unit_title": "Unit 1", "unit_sort": 1}

SUBJECTS = [  # (англ., перевод, картинка)
    ("Art", "изобразительное искусство", "subj_art"),
    ("Computer Studies", "информатика", "subj_computer"),
    ("English", "английский", "subj_english"),
    ("French", "французский", "subj_french"),
    ("Geography", "география", "subj_geography"),
    ("History", "история", "subj_history"),
    ("Maths", "математика", "subj_maths"),
    ("Music", "музыка", "subj_music"),
    ("P.E.", "физическое воспитание (физкультура)", "subj_pe"),
    ("Science", "естественные науки", "subj_science"),
]

THINGS = [
    ("calculator", "калькулятор", "calculator"),
    ("dictionary", "словарь", "dictionary"),
    ("laptop", "ноутбук", "laptop"),
    ("map", "карта", "map"),
    ("paints", "краски", "paints"),
    ("pencil case", "пенал", "pencil_case"),
    ("rubber", "ластик", "rubber"),
    ("ruler", "линейка", "ruler"),
    ("scissors", "ножницы", "scissors"),
    ("trainers", "кроссовки", "trainers"),
]

PLACES = [
    ("canteen", "столовая", "canteen"),
    ("classroom", "класс", "classroom"),
    ("computer room", "компьютерный зал", "computer_room"),
    ("gym", "спортивный зал", "gym"),
    ("hall", "коридор", "hall"),
    ("library", "библиотека", "library"),
    ("playground", "игровая площадка", "playground"),
    ("staff room", "учительская", "staff_room"),
]


def flashcards(words):
    return ("flashcards", {"cards": [
        {"text": en, "translation": ru, "image": img(U, f), "audio_tts": en} for en, ru, f in words]})


def match_pics(words, title="Соедини картинку со словом"):
    return ("match", {"title": title, "pairs": [
        {"left_image": img(U, f), "right": en, "right_audio_tts": en} for en, ru, f in words]})


def quiz_ru_to_en(words, per_question=4):
    """«Как по-английски…» — отвлекающие по кругу, варианты по алфавиту (позиция верного гуляет)."""
    qs, n = [], len(words)
    for i, (en, ru, _) in enumerate(words):
        wrong = [words[(i + k * 3) % n][0] for k in range(1, per_question)]
        options = sorted([en] + wrong, key=str.lower)
        qs.append({"q": f"Как по-английски «{ru}»?", "type": "single",
                   "options": [{"text": o} for o in options], "correct": [options.index(en)]})
    return ("quiz", {"title": "Выбери правильный перевод", "questions": qs})


def single(q, options, right, image=None):
    d = {"q": q, "type": "single", "options": [{"text": o} for o in options], "correct": [options.index(right)]}
    if image:
        d["image"] = image
    return d


def tf(q, right, image=None):
    return single(q, ["True", "False"], "True" if right else "False", image)


def order(parts, image=None):
    sentence = " ".join(parts)
    p = {"words": list(parts), "sentence": sentence, "audio_tts": sentence.replace("’", "'")}
    if image:
        p["image"] = image
    return ("order", p)


def pic(src, h=200):
    return f'<p><img src="{src}" alt="" style="height:{h}px"></p>'


def wide(src):
    return f'<p><img src="{src}" alt="" style="max-width:100%"></p>'


LESSONS = {
    # ------------------------------------------------------------------ HW1 (1)+(2)+(3)
    "u1_hw1": {**UNIT, "lesson_title": "Homework 1", "lesson_sort": 0, "kind": "homework", "blocks": [
        ("text", {"html": pic(shared("hello_wave")) +
            "<h2>Привет! 👋</h2><p>Сейчас мы с тобой выучим школьные предметы. Выполни все задания, "
            "чтобы выучить слова на 100%!</p><p>Также не забудь выучить школьные принадлежности и "
            "потренировать выученные слова на практике. У тебя всё получится! ❤️</p>"}),
        flashcards(SUBJECTS),
        match_pics(SUBJECTS, "Соедини картинку с названием предмета"),
        quiz_ru_to_en(SUBJECTS),

        ("text", {"html": pic(shared("hello_book")) +
            "<h3>Школьные принадлежности 🎒</h3><p>А теперь выучим школьные принадлежности. "
            "Посмотри карточки, послушай слова и выполни задания. Удачи! ❤️</p>"}),
        flashcards(THINGS),
        match_pics(THINGS, "Соедини картинку со словом"),
        ("exact_input", {"title": "Напиши слово по-английски", "items": [
            {"prompt": f"Напиши по-английски: {ru}", "image": img(U, f),
             "accept": [en, en.capitalize()], "audio_tts": en} for en, ru, f in THINGS]}),

        ("text", {"html": pic(shared("hello_rocket")) +
            "<h3>Дополнительная часть 🚀</h3><p>Добро пожаловать в ДОПОЛНИТЕЛЬНУЮ часть домашнего задания! "
            "Выполни все задания, чтобы хорошенько запомнить новые слова. Выполнив их, ты станешь "
            "МЕГА крутым учеником!</p><p>Твоё первое задание — вставить названия школьных предметов в пропуски. Удачи!</p>"}),
        ("gaps", {"title": "Перетащи названия предметов в пропуски", "mode": "drag",
                  "text": "1. I paint pictures of flowers in __Art__.\n"
                          "2. We learn to say Bonjour in __French__.\n"
                          "3. I learn about different countries in __Geography__.\n"
                          "4. In __Maths__ we can use a calculator for problems.\n"
                          "5. We do cool experiments in __Science__.\n"
                          "6. In __Music__ we sing lots of songs.\n"
                          "7. This book about the past is for __History__.\n"
                          "8. Today's grammar lesson for __English__ is “I can”.",
                  "gaps_expected": 8}),
        ("text", {"html": "<h3>Молодец! 👍</h3><p>А теперь прочитай, что рассказывает Karen, и отметь её "
                          "любимые школьные предметы.</p>"
                          "<blockquote><p>My name is Karen. I'm 11 years old. My favourite subjects are P.E. "
                          "and Computer Studies. I have P.E. on Monday and Wednesday and Computer Studies on "
                          "Friday.</p></blockquote>"}),
        ("quiz", {"title": "Отметь любимые предметы Karen", "questions": [
            {"q": "What are Karen's favourite subjects? Выбери ДВА варианта.", "type": "multiple",
             "options": [{"text": t} for t in ["Art", "Maths", "P.E.", "Science", "History", "Computer Studies"]],
             "correct": [2, 5]},
        ]}),
        ("task", {"title": "Дополнительное задание ⭐", "needs_review": True,
                  "html": "<p>А это ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ — для самых смелых! Прочитай ещё раз текст о Karen "
                          "и письменно перечисли свои любимые школьные предметы.</p>"
                          "<p><i>Например: My favourite subjects are English and Art.</i></p>"}),
        ("text", {"html": pic(shared("congrats_popper")) +
            "<h3>Поздравляю! 🎉</h3><p>Ты завершил домашнее задание. Ты — МЕГА КРУТ! Жду тебя на уроке!</p>"}),
    ]},

    # ------------------------------------------------------------------ HW2
    "u1_hw2": {**UNIT, "lesson_title": "Homework 2", "lesson_sort": 1, "kind": "homework", "blocks": [
        ("text", {"html": pic(shared("hello_wave")) +
            "<h2>Добро пожаловать в домашнее задание! 👋</h2><p>Сегодня мы с тобой научимся рассказывать "
            "о своём распорядке дня. Выполни все задания — и получишь звание чемпиона английского 💪</p>"}),
        ("text", {"html": "<p>Для начала посмотри видео. <b>What do Anna, Max and Hammy do after school?</b></p>" +
                          wide(img(U, "book_after_school"))}),
        video("Видео: Anna, Max and Hammy after school", "видео «After school» (Anna, Max, Hammy)"),
        ("quiz", {"title": "Выбери правильный вариант ответа для каждого пропуска", "questions": [
            single("We ___ sandwiches.", ["eat", "eats"], "eat"),
            single("Hammy ___ them too.", ["eat", "eats"], "eats"),
            single("We ___ up.", ["tidies", "tidy"], "tidy"),
            single("Hammy ___ up too.", ["tidies", "tidy"], "tidies"),
        ]}),
        ("sequence", {"title": "Посмотри видео ещё раз и расставь предложения в том порядке, как они идут в рассказе. У тебя получится!",
                      "items": [{"text": t} for t in [
                          "I go to Max's house.", "We do our homework.", "Hammy helps.",
                          "We have some drinks.", "We eat sandwiches.", "Hammy eats them too.",
                          "We tidy up.", "Hammy tidies up too."]]}),
        ("gaps", {"title": "Отлично! А теперь практика: перетащи нужный глагол в каждый пропуск", "mode": "drag",
                  "text": "1. My sister __likes__ going to the cinema.\n"
                          "2. Frank __goes__ to school with his sister.\n"
                          "3. My parents __like__ reading.\n"
                          "4. We __play__ basketball at school.\n"
                          "5. I __go__ to bed at 8 o'clock.\n"
                          "6. She __plays__ computer games on Sunday.",
                  "gaps_expected": 6}),
        ("text", {"html": pic(shared("well_done_clap")) +
            "<h3>Ура! 🎉</h3><p>Ты справился с домашней работой. Ты молодец! Увидимся на занятии! Bye!</p>"}),
    ]},

    # ------------------------------------------------------------------ HW3
    "u1_hw3": {**UNIT, "lesson_title": "Homework 3", "lesson_sort": 2, "kind": "homework", "blocks": [
        ("text", {"html": pic(shared("hello_wave")) +
            "<h2>Добро пожаловать в домашку! 👋</h2><p>В этом уроке тебя ждёт интересное видео и классные "
            "задания! В конце урока есть дополнительное задание — его можно выполнить по желанию, НО если "
            "выполнишь, то будешь нереально крут!</p>"}),
        ("text", {"html": "<p>Для начала посмотри видео. Попробуй угадать, кто из ребят любит играть в футбол: "
                          "Анна, Макс или Хэмми? А ты любишь играть в футбол в свободное время?</p>" +
                          pic(img(U, "book_football_question"), 260)}),
        video("Видео: Do you play football in your free time?",
              "видео «free time / football» (Anna, Max, Hammy)"),
        ("match", {"title": "Посмотри видео ещё раз и соедини вопросы и ответы", "pairs": [
            {"left": "Do you play football in your free time, Max?", "right": "No, I don't.",
             "right_audio_tts": "No, I don't."},
            {"left": "Does Anna play football in her free time?", "right": "No, she doesn't.",
             "right_audio_tts": "No, she doesn't."},
            {"left": "Do you play football in your free time, Hammy?", "right": "Yes, I do.",
             "right_audio_tts": "Yes, I do."},
        ]}),
        ("quiz", {"title": "Выбери только верные утверждения", "questions": [
            {"q": "Выбери только верные утверждения. Если нужно — посмотри видео ещё раз.", "type": "multiple",
             "image": img(U, "book_park"),
             "options": [{"text": "Max doesn't play football."}, {"text": "Anna doesn't like football."},
                         {"text": "Hammy doesn't play football."}],
             "correct": [0, 1]},
        ]}),
        ("text", {"html": "<h3>Замечательно! 👏</h3><p>Мы с тобой посмотрели видео, а теперь настало время "
                          "потрудиться! Посмотри на предложения ниже и выбери правильный вариант для каждого пропуска.</p>"}),
        ("quiz", {"title": "Выбери правильный вариант для каждого пропуска", "questions": [
            single("1. My sister ___ a hobby.", ["don't have", "doesn't have", "doesn't has"], "doesn't have"),
            single("2. They ___ my pictures.", ["don't likes", "doesn't like", "don't like"], "don't like"),
            single("3. David ___ karate.", ["doesn't do", "don't does", "doesn't does"], "doesn't do"),
            single("4. My parents ___ tennis.", ["don't plays", "doesn't play", "don't play"], "don't play"),
            single("5. She ___ French at school.", ["doesn't study", "don't study", "doesn't studies"], "doesn't study"),
            single("6. My grandfather ___ chess.", ["doesn't plays", "doesn't play", "don't play"], "doesn't play"),
        ]}),
        ("text", {"html": "<h3>Отличная работа! 💪</h3><p>Давай немного переведём дух и сыграем в игру. "
                          "Твоя задача — заполнить пропуски!</p>"}),
        todo(("gaps", {"title": "Do or does? Do or play? Перетащи слова в пропуски", "mode": "drag",
                       "text": "1. __Do__ you play tennis at the weekend?\n"
                               "2. __Does__ your brother do karate?\n"
                               "3. My sister __does__ ballet on Mondays.\n"
                               "4. We __play__ chess after school.\n"
                               "5. Max doesn't __play__ football in his free time.\n"
                               "6. I __do__ my homework in the evening.",
                       "gaps_expected": 6}),
             ("game", "СОСТАВ МОЙ: пересобрана игра Wordwall «Do or does? Do or play?» (cloze), "
                      "https://wordwall.net/resource/58864826/do-or-does-do-or-play — содержимого в выгрузке нет")),
        ("gaps", {"title": "Отлично! Давай теперь потренируемся составлять вопросы. Впиши Do или Does в пропуски",
                  "mode": "type", "image": img(U, "book_carla_rocco"),
                  "text": "1. __Does|does__ Carla paint pictures?\n"
                          "2. __Does|does__ Rocco paint pictures?\n"
                          "3. __Do|do__ Rocco and Carla like music?\n"
                          "4. __Do|do__ Rocco and Carla play football?\n"
                          "5. __Does|does__ Rocco play chess?\n"
                          "6. __Does|does__ Carla play chess?",
                  "gaps_expected": 6}),
        ("task", {"title": "Дополнительное задание ⭐", "needs_review": True,
                  "html": "<p>Ты справился с основной частью домашнего задания! Это задание — для самых больших "
                          "умников: оно дополнительное, но ты будешь мегакрутым учеником, если выполнишь его!</p>"
                          "<p>В таблице отмечено, чем любят и не любят заниматься Carla (кошка) и Rocco (енот). "
                          "Письменно ответь на вопросы из предыдущего упражнения "
                          "(например: <i>Yes, she does. / No, he doesn't.</i>).</p>" +
                          pic(img(U, "book_carla_rocco_table"), 220) +
                          "<ol><li>Does Carla paint pictures?</li><li>Does Rocco paint pictures?</li>"
                          "<li>Do Rocco and Carla like music?</li><li>Do Rocco and Carla play football?</li>"
                          "<li>Does Rocco play chess?</li><li>Does Carla play chess?</li></ol>"}),
        ("text", {"html": pic(shared("well_done_smiley")) +
            "<h3>Поздравляю! 🎉</h3><p>Ты завершил домашнее задание, ты замечательный ученик! "
            "Лови за это сердечко ❤️ Увидимся на занятии!</p>"}),
    ]},

    # ------------------------------------------------------------------ HW4
    "u1_hw4": {**UNIT, "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework", "blocks": [
        ("text", {"html": pic(shared("hello_wave")) +
            "<h2>Добро пожаловать в домашнее задание! 👋</h2><p>Сегодня мы с тобой научимся узнавать и "
            "рассказывать личную информацию. Let's start!</p>"}),
        ("text", {"html": "<p>Начнём с видеоинтервью. Но сначала представь, что ты стал журналистом. "
                          "У кого из знаменитостей ты бы хотел взять интервью? Посмотри видео ниже и выполни "
                          "задания к нему.</p>" + wide(img(U, "interview"))}),
        video("Видеоинтервью: Molly Greenberg", "видеоинтервью с Molly Greenberg (учитель из Нью-Йорка)"),
        ("match", {"title": "Посмотри видео и соедини вопросы с ответами", "pairs": [
            {"left": "What's your name?", "right": "My name is Molly.", "right_audio_tts": "My name is Molly."},
            {"left": "What's your last name?", "right": "My last name is Greenberg.",
             "right_audio_tts": "My last name is Greenberg."},
            {"left": "How do you spell it?", "right": "G-R-E-E-N-B-E-R-G.",
             "right_audio_tts": "G, R, E, E, N, B, E, R, G."},
            {"left": "Where are you from?", "right": "I'm from New York City.",
             "right_audio_tts": "I'm from New York City."},
            {"left": "What do you do?", "right": "I'm a teacher.", "right_audio_tts": "I'm a teacher."},
            {"left": "What's your phone number?", "right": "It's 2032548652.",
             "right_audio_tts": "It's 2 0 3 2 5 4 8 6 5 2."},
        ]}),
        ("gaps", {"title": "Прочитай диалог и перетащи слова в пропуски", "mode": "drag",
                  "image": img(U, "karen_chess_club"),
                  "text": "Karen: Good morning.\n"
                          "Mr Tims: Good morning.\n"
                          "Karen: I'd like to join the chess club, please.\n"
                          "Mr Tims: OK. What's your __name__?\n"
                          "Karen: My name is Karen Browne.\n"
                          "Mr Tims: How do you __spell__ that?\n"
                          "Karen: K-A-R-E-N B-R-O-W-N-E.\n"
                          "Mr Tims: Thanks. Where do you __live__?\n"
                          "Karen: 23 Green Street, Kingston.\n"
                          "Mr Tims: What's your __e-mail address__?\n"
                          "Karen: It's k.browne@mymail.com.\n"
                          "Mr Tims: And what's your phone number?\n"
                          "Karen: It's __08974942345__.\n"
                          "Mr Tims: Thanks.\n"
                          "Karen: What time does the club __start__?\n"
                          "Mr Tims: At 4 p.m.",
                  "gaps_expected": 6}),
        ("gaps", {"title": "Прочитай диалог ещё раз и впиши информацию о Карен", "mode": "type",
                  "text": "Name: __Karen Browne|karen browne__\n"
                          "Address: __23 Green Street, Kingston|23 Green Street Kingston|23 green street, kingston|23 green street kingston__\n"
                          "E-mail address: __k.browne@mymail.com|K.browne@mymail.com__\n"
                          "Phone number: __08974942345__",
                  "gaps_expected": 4}),
        ("quiz", {"title": "В вопросах чего-то не хватает. Выбери правильный вариант", "questions": [
            single("1. ___ your name?", ["What's", "Who's"], "What's"),
            single("2. ___ do you spell that?", ["Why", "How"], "How"),
            single("3. ___ do you live?", ["What's", "Where"], "Where"),
            single("4. ___ your e-mail address?", ["Where's", "What's"], "What's"),
            single("5. ___ your phone number?", ["What's", "Where's"], "What's"),
        ]}),
        ("task", {"title": "Расскажи о себе ✍️", "needs_review": True,
                  "html": "<p>Молодец! Осталось последнее задание. Письменно ответь о себе на вопросы:</p>"
                          "<ol><li>What's your name?</li><li>How do you spell that?</li><li>Where do you live?</li>"
                          "<li>What's your e-mail address?</li><li>What's your phone number?</li></ol>"
                          "<p><i>Можно придумать адрес и телефон — настоящие писать не обязательно.</i></p>"}),
        ("text", {"html": pic(shared("well_done_trophy")) +
            "<h3>Отлично! 🏆</h3><p>Ты справился со всеми заданиями — ты большой молодец. Держи за это кубок "
            "победителя. Жду тебя на занятии!</p>"}),
    ]},

    # ------------------------------------------------------------------ HW5 (1)+(2)
    "u1_hw5": {**UNIT, "lesson_title": "Homework 5", "lesson_sort": 4, "kind": "homework", "blocks": [
        ("text", {"html": pic(shared("hello_wave")) +
            "<h2>Привет! 👋</h2><p>В этом уроке мы выучим названия мест, которые можно встретить в школе. "
            "Выполни все задания, чтобы выучить слова! А потом попрактикуемся в чтении. У тебя всё получится. Удачи! ❤️</p>"}),
        flashcards(PLACES),
        match_pics(PLACES, "Соедини картинку с названием места"),
        ("match", {"title": "Соедини слово с его значением", "pairs": [
            {"left": "canteen", "right": "You have lunch there.", "right_audio_tts": "You have lunch there."},
            {"left": "computer room", "right": "This is a special classroom with laptops.",
             "right_audio_tts": "This is a special classroom with laptops."},
            {"left": "gym", "right": "This is a very large room for P.E.",
             "right_audio_tts": "This is a very large room for P.E."},
            {"left": "library", "right": "There are lots of books for extra study there.",
             "right_audio_tts": "There are lots of books for extra study there."},
            {"left": "staff room", "right": "Teachers relax and mark homework there.",
             "right_audio_tts": "Teachers relax and mark homework there."},
        ]}),
        ("text", {"html": "<h3>Время почитать 📖</h3><p>Посмотри, это Стив! Он подготовил интересный рассказ о "
                          "своей школе. Прежде чем читать, подумай: какие места в школе — твои самые любимые? "
                          "Где ты больше всего любишь проводить время?</p>" + pic(img(U, "steve"), 240) +
                          "<h3>My school</h3>"
                          "<p>How many students have P.E. every day for two hours? Not many? Well, I always have "
                          "P.E. from 2.30 to 4.30. I'm Steve and I want to tell you about my school.</p>"
                          "<p>My day starts early. I usually get to school at 8.00 but I'm sometimes late. Lessons "
                          "start at 8.30. My favourite subject is Geography because I like maps. I don't like Art "
                          "because I don't paint good pictures.</p>"
                          "<p>We have lunch at 12.00 and I often have chicken and chips. I never have fish and "
                          "chips. In the afternoon we have P.E. I love P.E.! We usually play football or do "
                          "karate. On Friday we play basketball. My favourite sport is football because I want "
                          "to play for a big team.</p>"
                          "<p>We finish school at 4.30. That's late for most schools. But I don't mind because I "
                          "play sport every day! My sport school is great!</p>"}),
        ("quiz", {"title": "Прочитай текст и выбери правильный ответ", "questions": [
            single("What school does Steve go to?", ["Art school", "Sports school", "Drama school"],
                   "Sports school", img(U, "sports_school")),
        ]}),
        ("quiz", {"title": "Прочитай текст о школе ещё раз. Это правда (True) или неправда (False)?", "questions": [
            tf("Steve always gets to school at 8.00.", False, img(U, "steve_late")),
            tf("Steve's favourite subject is Maths.", False, img(U, "steve_maths")),
            tf("Steve doesn't like Art.", True, img(U, "steve_art")),
            tf("Steve has lunch at 12.00.", True, img(U, "steve_lunch")),
            tf("Steve usually has fish and chips for lunch.", False, img(U, "fish_chips")),
            tf("Steve loves P.E.", True, img(U, "steve_pe")),
            tf("Steve plays basketball on Friday.", True, img(U, "steve_basketball")),
            tf("Steve's favourite sport is tennis.", False, img(U, "tennis_players")),
        ]}),
        ("task", {"title": "Последнее задание ✍️", "needs_review": True,
                  "html": "<p>Молодец! Прочитай текст ещё раз и письменно ответь на вопросы:</p>"
                          "<ol><li>Does Steve sometimes get to school late?</li><li>Why does he like Geography?</li>"
                          "<li>Does he paint good pictures?</li><li>What sports does he usually do?</li>"
                          "<li>What does he do on Friday?</li><li>Does he finish school before 4.00?</li></ol>"}),
        ("text", {"html": pic(shared("well_done_jump")) +
            "<h3>Ура! 🎉</h3><p>Ты справился с домашним заданием. Ты — мегакрут! Увидимся на занятии. Goodbye!</p>"}),
    ]},

    # ------------------------------------------------------------------ HW6
    "u1_hw6": {**UNIT, "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework", "blocks": [
        ("text", {"html": pic(shared("hello_headphones")) +
            "<h2>Добро пожаловать в домашнее задание! 👋</h2><p>Сегодня тебя ждут интересная аудиозапись и "
            "увлекательные упражнения. Let's go!</p>"}),
        ("text", {"html": "<p>Давай начнём с аудио. Это — Марк. Он расскажет нам о своих школьных предметах. "
                          "Но прежде чем слушать Марка, попробуй угадать: какой у него любимый школьный предмет?</p>" +
                          pic(img(U, "mark"), 240)}),
        todo(("video", {"title": "Послушай, как Марк рассказывает о своих предметах", "url": "", "provider": "file"}),
             ("audio", "аудио: Mark рассказывает о своих предметах и расписании (без него следующие задания не решаются)")),
        ("quiz", {"title": "Послушай аудио и заполни расписание Марка: выбери день недели для каждого предмета", "questions": [
            single("French: on ___", ["Monday", "Tuesday"], "Tuesday"),
            single("Science: on ___ (первый день)", ["Monday", "Tuesday"], "Monday"),
            single("Science: and on ___ (второй день)", ["Thursday", "Friday"], "Thursday"),
            single("History: on ___ (первый день)", ["Thursday", "Wednesday"], "Wednesday"),
            single("History: and on ___ (второй день)", ["Sunday", "Friday"], "Friday"),
            single("Football: on ___", ["Sunday", "Monday"], "Sunday"),
            single("Chess: on ___", ["Friday", "Saturday"], "Saturday"),
        ]}),
        ("quiz", {"title": "Послушай аудио ещё раз. Это правда (True) или неправда (False)?", "questions": [
            tf("Mark's favourite subject is French.", True, img(U, "subj_french")),
            tf("He likes History.", False, img(U, "history_lesson")),
            tf("Mark likes Science.", True, img(U, "mark_science")),
            tf("He plays football at school.", False, img(U, "kids_football")),
            tf("He always plays chess on Sunday.", False, img(U, "mark_chess")),
        ]}),
        ("text", {"html": "<h3>Молодец! 👏</h3><p>Ты справился с большей частью заданий. А какой твой любимый "
                          "день недели? Давай почитаем о Лили и её любимом дне.</p>"}),
        ("gaps", {"title": "Прочитай рассказ Лили и перетащи слова в пропуски", "mode": "drag",
                  "image": img(U, "lily_bus"),
                  "text": "Hi! My __name__ is Lily. My __favourite__ day is Tuesday. On Tuesday I get up __at__ 7.30. "
                          "I meet my friends at 8 __o'clock__ and we get the bus to school. We often talk about our "
                          "favourite computer __games__. __On__ Tuesday, we have Music, Computer Studies and "
                          "__English__. They are my favourite __subjects__! __In__ the morning, we have Music. We "
                          "sometimes sing and I usually play __the piano__. I have __pizza__ at lunchtime. Tuesday "
                          "is pizza day in the canteen! In the evening, after school, I always __do__ ballet.",
                  "gaps_expected": 12}),
        ("task", {"title": "Мой любимый день ✍️", "needs_review": True,
                  "html": "<p>Ура, это последнее задание! Напиши о своём любимом дне недели. Используй рассказ "
                          "Лили как пример. Удачи!</p>"
                          "<p><i>Например: My favourite day is … On … I get up at … We have …</i></p>"}),
        ("text", {"html": pic(shared("well_done_star")) +
            "<h3>Поздравляю! 🌟</h3><p>Ты завершил домашнее задание. Ты — супер ученик! Жду тебя на занятии!</p>"}),
    ]},

    # ------------------------------------------------------------------ HW7
    "u1_hw7": {**UNIT, "lesson_title": "Homework 7", "lesson_sort": 6, "kind": "homework", "blocks": [
        ("text", {"html": pic(shared("hello_highfive")) +
            "<h2>Привет! 👋</h2><p>Добро пожаловать в домашнее задание! В этом уроке тебя ждут несколько "
            "интересных упражнений, которые помогут закрепить полученные знания. Поехали!</p>"}),
        match_pics([s for s in SUBJECTS if s[0] != "French"],
                   "Давай сначала вспомним школьные предметы. Соедини название предмета с картинкой"),
        ("sort", {"title": "Молодец! Давай вспомним, с какими занятиями мы используем do, а с какими — play", "groups": [
            {"name": "do", "items": [{"text": "ballet"}, {"text": "karate"}, {"text": "pottery"}]},
            {"name": "play", "items": [{"text": "basketball"}, {"text": "chess"}, {"text": "football"}]},
        ]}),
        ("match", {"title": "Предложения и вопросы распались на две части и перемешались 😱 Найди вторую половинку для каждого", "pairs": [
            {"left": "Do you read", "right": "Harry Potter books in English?"},
            {"left": "In Maths we can use", "right": "a calculator for problems."},
            {"left": "We write games on laptops", "right": "in our Computer Studies lesson."},
            {"left": "Do you need a dictionary", "right": "for your French homework?"},
            {"left": "I like Geography because", "right": "I think maps are very interesting."},
            {"left": "His trainers are in his bag", "right": "because he has P.E. today."},
        ]}),
        ("quiz", {"title": "Выбери правильную форму глагола", "questions": [
            single("1. I ___ football at break time.", ["plays", "play", "plaies"], "play"),
            single("2. She ___ TV before dinner.", ["watchs", "watch", "watches"], "watches"),
            single("3. John ___ a new pencil.", ["doesn't have", "doesn't has", "don't have"], "doesn't have"),
            single("4. They ___ to school on Sunday.", ["doesn't go", "don't go"], "don't go"),
            single("5. We ___ pottery at school.", ["don't do", "doesn't do"], "don't do"),
            single("6. You ___ to music on the bus.", ["listenes", "listens", "listen"], "listen"),
        ]}),
        ("text", {"html": "<h3>Молодец! 💪</h3><p>Ты выполнил бóльшую часть заданий, осталось совсем немного. "
                          "Потренируйся составлять предложения.</p>"}),
        order(["I", "always", "do", "ballet", "on", "Monday."], img(U, "ballet_girl")),
        order(["He", "sometimes", "walks", "to", "school."], img(U, "walk_to_school")),
        order(["I", "never", "play", "football", "before", "school."], img(U, "football_morning")),
        order(["Do", "you", "have", "a", "sandwich", "for", "lunch?"], img(U, "lunch_box")),
        ("task", {"title": "Задание со звёздочкой ⭐", "needs_review": True,
                  "html": "<p>Это последнее задание, но оно «со звёздочкой». Вспомни вопросы, которые мы учили "
                          "несколько уроков назад. Обычно я задаю вопрос, а ты отвечаешь. А сейчас наоборот: "
                          "я напишу ответы, а ты составь и запиши к ним вопросы.</p>"
                          "<p><i>Например: ответ «I'm eleven». Вопрос к нему — «How old are you?»</i></p>"
                          "<ol><li>I'm Paul.</li><li>P-A-U-L.</li><li>22 North Street, Oldtown.</li>"
                          "<li>It's 02465 438967.</li><li>It's paulharris@mymail.com.</li></ol>"}),
        ("text", {"html": pic(shared("well_done_star")) +
            "<h3>Ты справился! 🌟</h3><p>Ты — большой молодец! За это держи звёздочку.</p>"}),
    ]},

    # ------------------------------------------------------------------ Test
    "u1_test": {**UNIT, "lesson_title": "Unit 1 Test", "lesson_sort": 7, "kind": "test", "blocks": [
        ("text", {"html": pic(shared("good_luck_clover"), 180) +
            "<h2>Тест Unit 1 📝</h2><p>Пора проверить, как ты запомнил школьные предметы, принадлежности и "
            "Present Simple. Чтобы пройти тест, нужно набрать 90 баллов. Читай задания внимательно. Удачи!</p>"}),
        ("exact_input", {"title": "Напиши слова по-английски", "items": [
            {"prompt": f"{i}. Напиши по-английски: {ru}", "image": img(U, f), "accept": [en, en.lower() if en[0].isupper() else en.capitalize()],
             "audio_tts": en}
            for i, (en, ru, f) in enumerate([
                ("calculator", "калькулятор", "calculator"), ("dictionary", "словарь", "dictionary"),
                ("scissors", "ножницы", "scissors"), ("Geography", "география", "subj_geography"),
                ("History", "история", "subj_history"), ("Science", "естественные науки", "subj_science")], 1)]}),
        ("quiz", {"title": "Выбери правильный вариант, чтобы предложение было грамматически верным", "questions": [
            single("1. Sarah ___ tennis on Saturdays.", ["always plays", "plays always", "always play"], "always plays"),
            single("2. Tom ___ Polish, but he speaks Russian.", ["don't speak", "doesn't speak", "doesn't speaks"],
                   "doesn't speak"),
            single("3. My sister ___ English and French at school.", ["studys", "study", "studies"], "studies"),
            single("4. — ___ judo or karate? — I do judo.", ["Are you do", "Do you do", "Does you do"], "Do you do"),
            single("5. We ___ in the canteen at half past twelve.",
                   ["have usually lunch", "has usually lunch", "usually have lunch"], "usually have lunch"),
        ]}),
        ("gaps", {"title": "Поставь глагол в скобках в правильную форму Present Simple", "mode": "type",
                  "text": "1. Mark __plays__ (play) basketball on Wednesdays.\n"
                          "2. My mum __teaches__ (teach) Geography at our school.\n"
                          "3. Anna __studies__ (study) Maths every evening.\n"
                          "4. We __don't go|don’t go|do not go__ (not go) to school on Sunday.\n"
                          "5. — Does Liam __do__ (do) karate? — Yes, he does.",
                  "gaps_expected": 5}),
        ("text", {"html": "<h3>Расставь части предложения в правильном порядке</h3>"
                          "<p>В следующих пяти заданиях собери предложения из частей.</p>"}),
        order(["We", "always", "play", "chess", "at the weekend."]),
        order(["My", "brother", "doesn't", "like", "Music", "at school."]),
        order(["Does", "Sarah", "ride", "her bike", "to school?"]),
        order(["Tom", "sometimes", "forgets", "his", "pencil case."]),
        order(["They", "never", "have", "P.E.", "on Friday morning."]),
        ("text", {"html": "<h3>READING</h3><p>Прочитай текст и реши, верны ли утверждения (True), неверны "
                          "(False) или об этом в тексте не сказано (Not stated).</p>"
                          "<h3>Daniel's School Week</h3>"
                          "<p>Hi! I'm Daniel and I'm twelve. I go to school in Bristol, in the UK. I've got six "
                          "lessons every day, but my favourite day is Wednesday because I have Art and P.E.!</p>"
                          "<p>I always take my pencil case, ruler and calculator to school. I sometimes forget my "
                          "dictionary, but my friend Liam usually helps me – he's a really helpful boy.</p>"
                          "<p>We have lunch in the canteen at half past twelve. The food is normally quite good. "
                          "After school, on Mondays and Thursdays, I do judo at the sports centre. I never play "
                          "computer games on weekdays because my mum doesn't let me. At the weekend I often play "
                          "chess with my dad. He usually wins!</p>"
                          "<p>My sister Emma loves Music. She plays the guitar and the piano.</p>"}),
        todo(("quiz", {"title": "True, False или Not stated?", "questions": [
            single("1. Daniel has six lessons every day.", ["True", "False", "Not stated"], "True"),
            single("2. Wednesday is his favourite day because of Art and P.E.", ["True", "False", "Not stated"], "True"),
            single("3. Daniel always remembers all his school things.", ["True", "False", "Not stated"], "False"),
            single("4. Daniel and Liam are in the same class.", ["True", "False", "Not stated"], "Not stated"),
            single("5. Daniel has lunch at half past twelve.", ["True", "False", "Not stated"], "True"),
            single("6. Daniel does judo three times a week.", ["True", "False", "Not stated"], "False"),
            single("7. Daniel can play computer games on Saturday.", ["True", "False", "Not stated"], "True"),
        ]}), ("check", "утв. 6 — ключ «False» вместо «Не указано» (правка принята); утв. 4 оставлено "
                       "«Not stated», утв. 7 «True» — как в выгрузке")),
        todo(("sequence", {"title": "Послушай рассказ Софии о её вторнике. Расставь события в том порядке, в котором она о них говорит",
                           "audio": "",
                           "items": [{"text": t} for t in [
                               "Sophia gets up at seven o’clock.", "Sophia's mum drives her to school.",
                               "Sophia has Computer Studies.", "Sophia goes to the canteen with Emma.",
                               "Sophia plays tennis with the school team.",
                               "Sophia goes to the library to do her homework.",
                               "Sophia has dinner with her family."]]}),
             ("audio", "аудио «Sophia's Tuesday» — вставить в поле аудио этого блока")),
        ("speaking", {"title": "SPEAKING I 🎤", "needs_review": True, "image": img(U, "scene_canteen"),
                      "html": "<p>Опиши картинку и ответь на вопросы-помощники. Нажми на микрофон и запиши ответ.</p>"
                              "<ol><li>Where are the students?</li><li>How many students can you see?</li>"
                              "<li>What food and drink can you see on the table?</li>"
                              "<li>Are the students friendly?</li>"
                              "<li>Where do you have lunch: at home, in the canteen or in the classroom?</li></ol>"}),
        ("speaking", {"title": "SPEAKING II 🎤", "needs_review": True,
                      "html": "<p>Ответь на вопросы полными предложениями. Нажми на микрофон и запиши ответ.</p>"
                              "<ol><li>What's your favourite subject at school?</li>"
                              "<li>Which subject don't you like? Why?</li>"
                              "<li>How many lessons do you have on Mondays?</li>"
                              "<li>What do you always have in your pencil case?</li>"
                              "<li>Do you have a laptop or a tablet for school?</li>"
                              "<li>How often do you do your homework – always, usually, sometimes or never?</li>"
                              "<li>What do you usually do on Friday evenings?</li></ol>"}),
        ("text", {"html": pic(shared("well_done_trophy"), 180) +
            "<h3>Тест завершён! 🎉</h3><p>Ты молодец! Unit 1 пройден — увидимся на занятии.</p>"}),
    ]},
}
