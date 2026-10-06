#!/usr/bin/env python3
"""Go Getter 1 · Unit 8 · Sport and health — уроки (разбор: docs/GG1_разбор/u8.md).

Виды спорта и do / go / play, love / like / hate + -ing, объектные местоимения,
вопросительные слова, погода и времена года, здоровый образ жизни. Картинки
спорта, погоды, сезонов и ЗОЖ — сгенерированные (media/gg1/u8/sport_*, weather_*,
season_*, life_*); карточки методиста, сцены учебника (Даг с автографом, Мэнди
по телефону, четыре дерева, таблицы) — кадры из выгрузки. Фото детей не берём:
тексты учебника переписаны HTML. Прощание в выгрузке — Микки (©), приветствие
в HW1 — пингвин из мультфильма: заменены картинками media/shared.
"""
from gg1_lib import *  # noqa: F401,F403

U = "u8"
U8 = {"unit": U, "unit_title": "Unit 8 · Sport and health", "unit_sort": 8}


def u(name):
    return img(U, name)


U8_SPORTS = vocab([
    ("badminton", "бадминтон", "sport_badminton"),
    ("basketball", "баскетбол", "sport_basketball"),
    ("cycling", "велосипедный спорт", "sport_cycling"),
    ("hockey", "хоккей", "sport_hockey"),
    ("ice-skating", "катание на коньках", "sport_ice_skating"),
    ("roller skating", "катание на роликовых коньках", "sport_roller_skating"),
    ("sailing", "парусный спорт", "sport_sailing"),
    ("skateboarding", "скейтбординг", "sport_skateboarding"),
    ("skiing", "катание на лыжах", "sport_skiing"),
    ("swimming", "плавание", "sport_swimming"),
    ("table tennis", "настольный теннис", "sport_table_tennis"),
    ("taekwondo", "тхэквондо", "sport_taekwondo"),
    ("tennis", "теннис", "sport_tennis"),
    ("volleyball", "волейбол", "sport_volleyball"),
    ("windsurfing", "виндсерфинг", "sport_windsurfing"),
])

CHAMPION = ("Ты выполнил все задания из основной части! А это дополнительное задание — "
            "для настоящих чемпионов! ")
REVIEW = "<p>Давай повторим всё, что выучили сегодня на уроке.</p>"
BYE = "<h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"
HELLO_HW = ("Добро пожаловать на домашнее задание! Сегодня мы с тобой закрепим знания, "
            "полученные на уроке")
EXTRA = ("В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых "
         "сильных учеников 💪")


def sport(en):
    return u(next(p for e, r, p in U8_SPORTS if e == en))


def spellings(*sentences):
    """Варианты ответа для exact_input: с точкой и без, полные и краткие формы."""
    out = []
    for s in sentences:
        forms = {s}
        for short, full in [("doesn't", "does not"), ("don't", "do not")]:
            forms |= {f.replace(short, full) for f in forms}
        for f in sorted(forms, key=lambda x: (x != s, x)):
            for g in (f, f.rstrip(".?!")):
                if g not in out:
                    out.append(g)
    return out


LESSONS = {
    # Homework 1 (1) — словарный тренажёр «виды спорта», (2) — задания. Один урок.
    "u8_hw1": {
        **U8,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня тебя ждёт изучение новых слов. Ты повторишь "
                  "названия разных видов спорта. Давай начинать 😉</p>"),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": u(p)}
                for en, ru, p in U8_SPORTS
            ]}),

            ("match", {"title": "Соедини картинку и слово", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in U8_SPORTS[:8]
            ]}),

            ("match", {"title": "И ещё: соедини картинку и слово", "pairs": [
                {"left_image": u(p), "right": en, "right_audio_tts": en}
                for en, ru, p in U8_SPORTS[8:]
            ]}),

            ("quiz", quiz_ru_to_en(U8_SPORTS[:8])),

            ("exact_input", {"title": "Посмотри на картинку и напиши слово по-английски", "items": [
                {"prompt": ru, "accept": list(dict.fromkeys([en, en.capitalize()])), "image": u(p),
                 "audio_tts": en}
                for en, ru, p in U8_SPORTS[8:]
            ]}),

            ("text", {"html": "<h3>🌟 Привет, дружок! Рада снова видеть тебя на нашем домашнем "
                              "задании!</h3><p>Сегодня мы будем говорить о спорте — это очень "
                              "интересная тема. Настройся и приступай! 💪</p>"
                              + REVIEW + pic(u("card_sports"), "Unit 8 Спорт")}),

            # в выгрузке — шесть отдельных тестов с фото предметов; у нас картинки Л8
            mcq("Посмотри на картинки. Выбери правильное слово", [
                ("What sport is it?", ["cycling", "taekwondo"], "cycling", sport("cycling")),
                ("What sport is it?", ["hockey", "badminton"], "hockey", sport("hockey")),
                ("What sport is it?", ["sailing", "windsurfing"], "windsurfing", sport("windsurfing")),
                ("What sport is it?", ["basketball", "volleyball"], "volleyball", sport("volleyball")),
                ("What sport is it?", ["tennis", "table tennis"], "table tennis", sport("table tennis")),
                ("What sport is it?", ["ice-skating", "roller skating"], "ice-skating",
                 sport("ice-skating")),
            ]),

            # в выгрузке — страница учебника со сценами с детьми; у нас картинки предметов
            ("exact_input", {"title": "Посмотри на картинки и подпиши виды спорта. "
                                      "Используй слова из первого задания", "items": [
                {"prompt": f"{n}.", "accept": acc, "image": sport(en), "audio_tts": en}
                for n, en, acc in [
                    (1, "badminton", ["badminton", "Badminton"]),
                    (2, "basketball", ["basketball", "Basketball"]),
                    (3, "taekwondo", ["taekwondo", "Taekwondo"]),
                    (4, "sailing", ["sailing", "Sailing"]),
                    (5, "roller skating", ["roller skating", "Roller skating", "roller-skating",
                                           "rollerskating"]),
                    (6, "tennis", ["tennis", "Tennis"]),
                ]
            ]}),

            choose("Выбери правильное слово: go, do или play", [
                (f"___ {w}", ["go", "do", "play"], ok) for w, ok in [
                    ("ice-skating", "go"), ("cycling", "go"), ("taekwondo", "do"),
                    ("tennis", "play"), ("football", "play"), ("swimming", "go"),
                    ("sailing", "go"), ("volleyball", "play"), ("skiing", "go"),
                    ("badminton", "play"),
                ]
            ]),

            ("match", {"title": "Соедини половинки предложений", "pairs": [
                {"left": "I sometimes play", "right": "badminton with my dad or my brother."},
                {"left": "George does", "right": "taekwondo every Monday after school."},
                {"left": "Do you go", "right": "skiing with your family?"},
                {"left": "My brother plays", "right": "hockey with his friends."},
                {"left": "Sandra never goes", "right": "ice-skating because she can't ice-skate."},
                {"left": "Do you often play", "right": "basketball at school?"},
            ]}),

            ("speaking", {
                "title": "Мой спорт 🎤",
                "html": "<p>Нажми на микрофон и расскажи, какими видами спорта ты занимаешься, "
                        "а какими — нет. Используй глаголы do, go, play.</p>"
                        "<p><i>Пример: I play tennis and I go swimming, but I don't do "
                        "taekwondo.</i></p>",
                "needs_review": True,
            }),

            # Wordwall (обложка пустая, тип и название неизвестны) «Соедини:» — СОСТАВ МОЙ
            ("match", {"title": CHAMPION + "Соедини слова с картинками ⭐", "pairs": [
                {"left": phrase, "left_audio_tts": phrase, "right_image": sport(en)}
                for phrase, en in [
                    ("go skiing", "skiing"), ("play hockey", "hockey"),
                    ("go skateboarding", "skateboarding"), ("do taekwondo", "taekwondo"),
                    ("play basketball", "basketball"), ("go swimming", "swimming"),
                ]
            ]}),

            # Wordwall (обложка пустая) «Перетащи активности к подходящим глаголам:» —
            # СОСТАВ МОЙ, группы по карточке методиста
            ("sort", {"title": "Перетащи активности к подходящим глаголам ⭐", "groups": [
                {"name": "DO", "items": [{"text": t} for t in ["taekwondo", "exercise"]]},
                {"name": "GO", "items": [{"text": t} for t in
                                         ["swimming", "cycling", "skiing", "sailing",
                                          "skateboarding", "ice-skating", "roller skating",
                                          "windsurfing"]]},
                {"name": "PLAY", "items": [{"text": t} for t in
                                           ["basketball", "football", "hockey", "volleyball",
                                            "tennis", "badminton", "table tennis"]]},
            ]}),

            bye("<h3>🎊 Ура-ура! Ты выполнил все задания и узнал много новых слов о спорте. "
                "Ты просто чемпион! 🏆</h3><p>Жду тебя на нашем следующем уроке!</p>",
                "well_done_trophy"),
        ],
    },

    "u8_hw2": {
        **U8,
        "lesson_title": "Homework 2",
        "lesson_sort": 1,
        "kind": "homework",
        "blocks": [
            hello(f"<h2>Hello! 👋</h2><p>{HELLO_HW}, и ты без проблем сможешь говорить о том, что "
                  f"тебе нравится или не нравится. {EXTRA}</p>", "hello_book"),

            ("text", {"html": REVIEW + pic(u("card_like_ing"), "love / like / hate + -ing")
                              + pic(u("card_object_pronouns"), "Объектные местоимения")}),

            # в выгрузке «Медиафайл» пустой — видео вставит методист
            ("video", {"title": "Макс и Хэмми рассказывают, как они сходили в поход! Повторяй "
                                "вопросы и ответы за героями, чтобы хорошенько запомнить правила.",
                       "url": "", "provider": "youtube"}),

            # в выгрузке после каждого предложения «Who?» — вопрос к видео без поля
            # для ответа; у нас убран
            ("gaps", {
                "title": "Мы посмотрели видео и немного размялись, теперь пришло время практики! "
                         "Впиши правильную форму слова",
                "mode": "type",
                "text": "1. This person loves (play) __playing__ the guitar.\n"
                        "2. This person likes (make) __making__ cupcakes.\n"
                        "3. This person hates (get up) __getting up__ early and (cook) "
                        "__cooking__.\n"
                        "4. This person likes (skateboard) __skateboarding__ and (climb) "
                        "__climbing__.",
                "gaps_expected": 6,
            }),

            order("Lisa loves playing the guitar.",
                  title="Отлично, двигаемся дальше! Теперь давай расставим слова в правильном "
                        "порядке, чтобы получились предложения"),
            order("What does Monica like doing?",
                  title="Расставь слова в правильном порядке, чтобы получилось предложение"),
            order("Janet doesn't like getting up early.",
                  ["Janet", "doesn't like", "getting", "up", "early."],
                  title="Расставь слова в правильном порядке, чтобы получилось предложение"),
            order("Mark loves watching funny films.",
                  title="Расставь слова в правильном порядке, чтобы получилось предложение"),
            order("Wendy likes sailing and windsurfing.",
                  title="Расставь слова в правильном порядке, чтобы получилось предложение"),
            # в выгрузке опечатка «taekwando»
            order("Does Tim like doing taekwondo?",
                  title="Расставь слова в правильном порядке, чтобы получилось предложение"),

            # в выгрузке смайлики непоследовательны (у Ann 😫😫 = doesn't like, у кошки
            # 😫 = hates) — выровнено: 😊😊 love, 😊 like, 😫 don't like, 😫😫 hate
            ("gaps", {
                "title": "Внимательно посмотри на смайлики — о чём они говорят? Вставь слова по "
                         "смыслу так, чтобы они грамматически подходили в предложения. "
                         "😊😊 — love, 😊 — like, 😫 — don't like, 😫😫 — hate",
                "mode": "drag",
                "text": "1. We 😫😫 __hate__ rock climbing.\n"
                        "2. My parents 😊 __like__ skiing.\n"
                        "3. Ann 😫 __doesn't like__ playing football.\n"
                        "4. My grandad 😊😊 __loves__ cooking.\n"
                        "5. My friends 😫 __don't like__ getting up early.\n"
                        "6. I 😊😊 __love__ cycling.\n"
                        "7. Mark 😊 __likes__ playing basketball.\n"
                        "8. My cat 😫😫 __hates__ getting wet.",
                "gaps_expected": 8,
            }),

            # в выгрузке — таблица учебника, повторяет карточку методиста
            ("gaps", {
                "title": "Мы уже на финишной прямой! Внимательно посмотри на правило и заполни "
                         "пропуски в предложениях",
                "mode": "type",
                "image": u("card_object_pronouns"),
                "text": "1. Emma is nice. I like __her__.\n"
                        "2. Skating is fun. I love __it__.\n"
                        "3. You are great at football. I like watching __you__.\n"
                        "4. Amy and Tom are my best friends. I like __them__.\n"
                        "5. Tom is my baby brother. I love __him__.\n"
                        "6. We're good at dancing. Watch __us__.",
                "gaps_expected": 6,
            }),

            ("task", {
                "title": "Что мне нравится ✍️",
                "needs_review": True,
                "html": "<p>Напиши 3 предложения о себе и 3 предложения о своём члене семьи, друге "
                        "или даже учителе! Что тебе нравится, что тебе не нравится и что ты "
                        "ненавидишь? И то же самое о другом человеке.</p>"
                        "<p>Посмотри, это мои предложения:</p>"
                        "<p><i>I like playing basketball. I don't like cleaning. I hate watching "
                        "football. She likes playing tennis. She doesn't like cooking. She hates "
                        "watching cartoons.</i></p>"
                        "<p>Обрати внимание на окончания глаголов, когда я рассказываю о своей "
                        "подруге 😉</p>",
            }),

            # Wordwall «Unjumble · like/love/don't like/hate …ing (gg1-u8)» — СОСТАВ МОЙ
            order("I love playing football.",
                  title=CHAMPION + "Расставь слова в правильном порядке ⭐"),
            order("She doesn't like cooking.", ["She", "doesn't like", "cooking."],
                  title="Расставь слова в правильном порядке ⭐"),
            order("My brother hates getting up early.",
                  title="Расставь слова в правильном порядке ⭐"),
            order("Do you like swimming?", title="Расставь слова в правильном порядке ⭐"),

            # Wordwall «Quiz · GG1 unit 8.2» — СОСТАВ МОЙ
            mcq("Выбери правильный вариант ⭐", [
                ("I love ___ volleyball.", ["play", "playing", "plays"], "playing"),
                ("My sister ___ cooking.", ["like", "likes", "liking"], "likes"),
                ("We don't like ___ TV.", ["watching", "watch", "watches"], "watching"),
                ("Ben is my friend. I like ___.", ["he", "his", "him"], "him"),
                ("Where are my keys? I can't see ___.", ["they", "them", "their"], "them"),
                ("Can you help ___, please?", ["I", "my", "me"], "me"),
            ]),

            bye(BYE, "well_done_star"),
        ],
    },

    "u8_hw3": {
        **U8,
        "lesson_title": "Homework 3",
        "lesson_sort": 2,
        "kind": "homework",
        "blocks": [
            hello(f"<h2>Hello! 👋</h2><p>{HELLO_HW}. Мы будем не только задавать мнооого вопросов, "
                  f"но и отвечать на них. {EXTRA}</p>", "hello_highfive"),

            ("text", {"html": REVIEW + pic(u("card_question_words"), "Вопросительные слова")}),

            # в выгрузке «Медиафайл» пустой — видео вставит методист
            ("video", {"title": "Хэмми расспрашивает Анну о её лучшей подруге… Как думаешь, откуда "
                                "она? Посмотри видео и проверь себя! Повторяй вопросы и ответы за "
                                "героями, чтобы хорошенько запомнить правила.",
                       "url": "", "provider": "youtube"}),

            # в выгрузке четыре пары, у двух ответы взаимозаменяемы («I don't know...» на
            # How old is she? и «I'm not sure...» на Is she a student?) — оставлены три
            ("match", {"title": "Внимательно посмотри видео ещё раз и соедини вопросы и ответы",
                       "pairs": [
                           {"left": "Who is this girl?", "right": "This is Kimmy."},
                           {"left": "Where does she live?", "right": "In Hong Kong."},
                           {"left": "Is she a student?", "right": "I'm not sure..."},
                       ]}),

            mcq("Нам дали прочитать интервью с одним из друзей Хэмми… Но все вопросы и ответы "
                "перепутались! Найди правильный ответ на каждый вопрос", [
                    ("When is the football game?", ["It's on Saturday.", "It's great."],
                     "It's on Saturday."),
                    ("Where is my mobile phone?", ["It's on the table.", "It's from China."],
                     "It's on the table."),
                    ("Whose bike is in front of the house?",
                     ["It's my mum's bike.", "The bike is green."], "It's my mum's bike."),
                    ("How many friends have you got?", ["Five.", "Five years old."], "Five."),
                    ("What is in your bag?", ["There's a notebook.", "It's next to the desk."],
                     "There's a notebook."),
                    ("Who is your English teacher?", ["It's Mr Evans.", "Mr Evans is here."],
                     "It's Mr Evans."),
                ]),

            mcq("Посмотри на картинку (мы уже видели её на уроке) и выбери правильное "
                "вопросительное слово. Ответы после вопросов тебе помогут!", [
                    ("A: ___ is Dug? B: He's in a shopping centre.", ["Where", "When"], "Where",
                     u("dug_autograph")),
                    ("A: ___ is the woman? B: She's Irina Peters.", ["Who", "Whose"], "Who"),
                    ("A: ___ is her sport? B: It's tennis.", ["What", "Who"], "What"),
                    ("A: ___ does Dug want? B: He wants her autograph.", ["What", "Why"], "What"),
                    ("A: ___ mobile phones can you see? B: Two.", ["How many", "When"],
                     "How many"),
                ]),

            ("gaps", {
                "title": "А вот это задание уже посложнее… Догадайся сам, какое слово пропущено!",
                "mode": "type",
                "text": "1. A: __What__ is your name? B: Marco.\n"
                        "2. A: __Where__ are you from? B: I'm from Italy, but I live in London now.\n"
                        "3. A: __How many__ friends have you got in London? B: A lot! Six or seven.\n"
                        "4. A: __Who__ is your best friend? B: Jacob. He's my classmate. We want to "
                        "go to a party today.\n"
                        "5. A: __Whose__ party is it? B: It's my sister's party! It's her birthday!\n"
                        "6. A: __When|What time__ is the party? B: It's at five o'clock.",
                "gaps_expected": 6,
            }),

            # в выгрузке пропуски с подсказками name / number… — ответы свободные
            ("task", {
                "title": "Интервью со звездой ⭐",
                "needs_review": True,
                "html": "<p>А это задание — для самых крутых чемпионов! Представь, что у тебя "
                        "берут интервью 😉 Ответь на вопросы и почувствуй себя звездой!</p>"
                        "<ol><li>What is your name? <i>(name)</i></li>"
                        "<li>How old are you? <i>(number)</i></li>"
                        "<li>Where are you from? <i>(country)</i></li>"
                        "<li>How many friends have you got? <i>(number)</i></li>"
                        "<li>What is your hobby? <i>(hobby)</i></li>"
                        "<li>What is your favourite school subject? <i>(subject)</i></li>"
                        "<li>Who is your best friend? <i>(name)</i></li></ol>",
            }),

            ("speaking", {
                "title": "Вопросы другу 🎤",
                "html": "<p>Задай 4 вопроса другу о его жизни (имя, возраст, спорт, день рождения) "
                        "и ответь на них. Нажми на микрофон.</p>"
                        "<p><i>Пример: What's your favourite sport? Where do you live? When is your "
                        "birthday? How many brothers and sisters have you got?</i></p>",
                "needs_review": True,
            }),

            # Wordwall «Find the match · Question words GG1 8.3» — СОСТАВ МОЙ
            mcq(CHAMPION + "Выбери подходящее вопросительное слово ⭐", [
                ("___ is your birthday? — In May.", ["When", "Where", "Who", "Whose"], "When"),
                ("___ do you live? — In Moscow.", ["Where", "When", "What", "Whose"], "Where"),
                ("___ is your hero? — My dad.", ["Who", "Whose", "Where", "When"], "Who"),
                ("___ sport do you like? — Tennis.", ["What", "Who", "Whose", "Where"], "What"),
                ("___ bike is this? — It's Tom's.", ["Whose", "Who", "What", "When"], "Whose"),
                ("___ sisters have you got? — Two.", ["How many", "What", "Who", "When"],
                 "How many"),
            ]),

            # Wordwall «Match up · gg1 8.3» — СОСТАВ МОЙ
            ("match", {"title": "Соедини вопрос с ответом ⭐", "pairs": [
                {"left": "Where do you live?", "right": "In London."},
                {"left": "Who is your best friend?", "right": "It's Jacob."},
                {"left": "What sport do you like?", "right": "I like volleyball."},
                {"left": "When is your birthday?", "right": "It's in June."},
                {"left": "How many sisters have you got?", "right": "I've got one sister."},
                {"left": "Whose bag is this?", "right": "It's my brother's bag."},
            ]}),

            bye(BYE, "well_done_clap"),
        ],
    },

    "u8_hw4": {
        **U8,
        "lesson_title": "Homework 4",
        "lesson_sort": 3,
        "kind": "homework",
        "blocks": [
            hello(f"<h2>Hello! 👋</h2><p>{HELLO_HW}, и ты без проблем сможешь говорить о погоде. "
                  f"{EXTRA}</p>", "hello_laptop"),

            ("text", {"html": REVIEW + pic(u("card_weather"), "Weather")}),

            # в выгрузке «Медиафайл» пустой — видео вставит методист; постер с чужим
            # логотипом над ним не берём
            ("video", {"title": "Внимательно посмотри видео и постарайся запомнить, как правильно "
                                "говорить о погоде на английском. Повторяй фразы за видео!",
                       "url": "", "provider": "youtube"}),

            ("match", {"title": "Сопоставь страны и прогнозы погоды из видео", "pairs": [
                {"left": c, "right_image": u(f"weather_{w}")}
                for c, w in [("Russia", "cold"), ("Mexico", "warm"), ("Japan", "cloudy"),
                             ("Australia", "hot"), ("France", "rainy"), ("England", "foggy")]
            ]}),

            ("sequence", {
                "title": "Расставь предложения в правильном порядке так, чтобы получился "
                         "складный диалог",
                "image": u("mandy_phone"),
                "items": [{"text": t} for t in [
                    "Hi, Mandy. Is the weather nice in Scotland?",
                    "No, it isn't. It's rainy and cold!",
                    "Oh dear. That's horrible.",
                    "Yes, it's really horrible. What's the weather like in France?",
                    "It's cold and snowy here.",
                    "Well, I hope it's snowy in Scotland too!",
                ]],
            }),

            ("match", {"title": "Соедини предложения по смыслу: какие занятия и действия подойдут "
                                "к какой погоде", "pairs": [
                {"left": "It's hot.", "right": "Let's go swimming."},
                {"left": "It's very cold.", "right": "Let's go skiing."},
                {"left": "It's windy.", "right": "Let's go sailing."},
                {"left": "It's rainy and wet.", "right": "Wear a coat."},
                {"left": "It's snowy.", "right": "Wear your boots."},
                {"left": "It's warm.", "right": "Wear a T-shirt."},
            ]}),

            # фото деревьев из учебника, людей нет; точки — на кронах
            ("hotspot", {
                "title": "Давай-ка вспомним времена года! Подпиши каждое деревце",
                "mode": "label",
                "image": u("four_trees"),
                "points": [
                    {"x": 22.0, "y": 22.0, "text": "spring"},
                    {"x": 76.0, "y": 22.0, "text": "summer"},
                    {"x": 22.0, "y": 70.0, "text": "autumn"},
                    {"x": 76.0, "y": 70.0, "text": "winter"},
                ],
                "extras": [],
            }),

            ("gaps", {
                "title": "И последнее задание на сегодня! Прочитай диалог и расставь слова по "
                         "смыслу. Ты справишься!",
                "mode": "drag",
                "text": "A: Hi, __what__'s the weather __like__ in New York today?\n"
                        "B: It's windy and __rainy__. I've got an umbrella!\n"
                        "A: I hate getting __wet__!\n"
                        "B: Me too! I __hope__ it's sunny and __warm__ tomorrow.",
                "gaps_expected": 6,
            }),

            ("speaking", {
                "title": "Погода 🎤",
                "html": "<p>Нажми на микрофон и расскажи о погоде сегодня и о погоде в твоё "
                        "любимое время года.</p>"
                        "<p><i>Пример: Today it's warm and sunny. My favourite season is summer. "
                        "In summer it's hot and sunny. I love it! In winter it's cold and "
                        "snowy.</i></p>",
                "needs_review": True,
            }),

            bye(BYE, "well_done_smiley"),
        ],
    },

    "u8_hw5": {
        **U8,
        "lesson_title": "Homework 5",
        "lesson_sort": 4,
        "kind": "homework",
        "blocks": [
            hello(f"<h2>Hello! 👋</h2><p>{HELLO_HW}. Как ты помнишь, на уроке мы читали текст и "
                  "выполняли упражнения по нему. Сегодня ты тоже будешь читать текст и выполнять "
                  f"задания, но уже самостоятельно!</p>", "hello_rocket"),

            ("text", {"html": REVIEW + pic(u("card_healthy"), "Healthy Lifestyle")}),

            # в выгрузке текст — страница учебника с фото детей; у нас текстом
            # («gets up and half past six» → «at half past six»)
            ("text", {"html":
                "<p><b>Начнём с текста. Внимательно его прочитай — после него тебя ждут "
                "упражнения.</b></p>"
                "<p><i>Sam is twelve. He's very sporty. He likes getting up early but he goes to bed "
                "very late. He goes swimming before school. After school he plays football. At the "
                "weekend he goes cycling with his friends. Sam's sister Tammy is ten. She doesn't "
                "like sport and she never does exercise. She likes reading and cooking. She goes to "
                "bed at nine, and she gets up at half past six.</i></p>"
                "<p><i>Sam loves cakes and chocolate and he often eats pizza and chips, but Tammy "
                "doesn't usually eat them. He doesn't like fruit and he hates vegetables – but Tammy "
                "loves them. Tammy likes chocolate but she doesn't eat it a lot. Sam usually drinks "
                "cola, but Tammy doesn't like it. She drinks fruit juice or water.</i></p>"}),

            # в выгрузке у Sam отмечено «sometimes», а по тексту он плавает каждое утро,
            # после школы играет в футбол, по выходным катается — исправлено на often
            mcq("Найди в тексте главное: выбери правильный вариант для Сэма и Тэмми", [
                ("Sam ___ does exercise.", ["often", "sometimes"], "often"),
                ("Tammy ___ does exercise.", ["never", "usually"], "never"),
                ("Does Sam eat healthy food?", ["yes", "no"], "no"),
                ("Does Tammy eat healthy food?", ["yes", "no"], "yes"),
            ]),

            # в выгрузке ответы пустые («.» во всех пропусках) — ответы по тексту, ТЕКСТ МОЙ
            ("gaps", {
                "title": "Прочитай текст ещё раз и ответь на вопросы: впиши пропущенные слова",
                "mode": "type",
                "text": "1. What exercise does Sam do in the morning? — He goes __swimming__.\n"
                        "2. When does Tammy do exercise? — She __never__ does exercise.\n"
                        "3. What does Tammy like doing? — She likes __reading__ and __cooking__.\n"
                        "4. What does Sam like eating? — He loves __cakes__ and __chocolate__.\n"
                        "5. Does Tammy like fruit and vegetables? — __Yes|yes__, she does. "
                        "She __loves__ them.\n"
                        "6. What does Sam usually drink? — He usually drinks __cola__.",
                "gaps_expected": 9,
            }),

            ("match", {"title": "Составь пары так, чтобы получились фразы о здоровом образе жизни",
                       "pairs": [
                           {"left": "eat", "right": "fruit and vegetables"},
                           {"left": "drink", "right": "a lot of water"},
                           {"left": "do", "right": "exercise"},
                           {"left": "brush", "right": "your teeth"},
                           {"left": "have", "right": "friends"},
                           {"left": "go", "right": "to bed early"},
                       ]}),

            # в выгрузке — клипарт с человечками; у нас сердце из фруктов и гантелей
            ("task", {
                "title": "Мой образ жизни ✍️",
                "needs_review": True,
                "html": pic(u("life_healthy_heart"), "Healthy lifestyle", 200)
                        + "<p>Давай напишем небольшой рассказ о твоём образе жизни! Что ты делаешь, "
                          "чтобы быть здоровым, а что не делаешь?</p>"
                          "<p><i>Например: I always brush my teeth in the morning. I often drink "
                          "water.</i></p>",
            }),

            bye(BYE, "well_done_medal"),
        ],
    },

    "u8_hw6": {
        **U8,
        "lesson_title": "Homework 6",
        "lesson_sort": 5,
        "kind": "homework",
        "blocks": [
            hello(f"<h2>Hello! 👋</h2><p>{HELLO_HW}. Как ты помнишь, мы слушали рассказы ребят о "
                  "том, какой образ жизни они ведут. Сегодня ты тоже будешь слушать и выполнять "
                  "задания, но уже самостоятельно!</p>", "hello_headphones"),

            # в выгрузке картинок нет — наши (Л8)
            ("match", {"title": "Первое задание — очень лёгкое! Соедини картинки со словами 😉",
                       "pairs": [
                           {"left_image": u("life_fruit_vegetables"), "right": "food",
                            "right_audio_tts": "food"},
                           {"left_image": u("life_sleep"), "right": "sleep",
                            "right_audio_tts": "sleep"},
                           {"left_image": u("life_do_exercise"), "right": "exercise",
                            "right_audio_tts": "exercise"},
                       ]}),

            listening("Пришло время серьёзной работы! Послушай, как Том отвечает на вопросы "
                      "о своём образе жизни."),

            ("match", {"title": "Соедини номера вопросов из аудио с темами", "pairs": [
                {"left": "Question 1", "right": "Food"},
                {"left": "Question 2", "right": "Exercise"},
                {"left": "Question 3", "right": "Sleep"},
            ]}),

            # аудио в выгрузке пустое — строка в доработать
            ("gaps", {
                "title": "Послушай Тома ещё раз и впиши в предложения недостающие слова",
                "mode": "type",
                "audio": "",
                "text": "Question 1: Tom's favourite food is __chips__. He eats a lot of __fruit__ "
                        "and vegetables. He drinks a lot of __water__.\n"
                        "Question 2: He likes __cycling__. He always __walks__ to school. He "
                        "sometimes goes __swimming__.\n"
                        "Question 3: He goes to bed at __9.30|9:30|half past nine|half past 9__. "
                        "He goes to sleep at __ten o'clock|10 o'clock|10.00|10:00|ten|10__.",
                "gaps_expected": 8,
            }),

            # в выгрузке ошибки выделены красным; в пропусках разметки нет — ошибка в
            # квадратных скобках. «eats sandwich» и «and but» не были помечены как ошибки —
            # исправлены в самом тексте
            ("gaps", {
                "title": "Побудь в роли учителя! В квадратных скобках — ошибки. Впиши в окошко "
                         "правильное слово или поменяй порядок слов. Первое исправление уже "
                         "сделано: Andy [like] likes pizza",
                "mode": "type",
                "text": "Andy [like] likes pizza but he [don't] __doesn't__ eat it very often. "
                        "He [has always] __always has__ lunch at school. He often eats "
                        "sandwiches.\n"
                        "He likes [read] __reading__ but he doesn't [likes] __like__ sport very "
                        "much. His favourite sport [are] __is__ swimming. He has swimming lessons "
                        "on Fridays.\n"
                        "Andy goes to bed [in] __at__ nine because he likes [sleep] __sleeping__. "
                        "He doesn't get up early.",
                "gaps_expected": 7,
            }),

            ("task", {
                "title": "Рассказ о Мэй ✍️",
                "needs_review": True,
                "html": "<p>Напиши небольшой рассказ о Мэй по примеру рассказа Энди, который ты "
                        "прочитал(а) выше! Воспользуйся табличкой — там есть вся нужная тебе "
                        "информация о Мэй. Не забудь разделить рассказ на три абзаца: еда, спорт, "
                        "подъём и отход ко сну!</p>"
                        + pic(u("may_table"), "May"),
            }),

            bye(BYE, "well_done_jump"),
        ],
    },

    "u8_hw7": {
        **U8,
        "lesson_title": "Homework 7",
        "lesson_sort": 6,
        "kind": "homework",
        "blocks": [
            hello("<h2>Hello! 👋</h2><p>Сегодня мы закрепим знания, полученные в этом месяце. На "
                  "следующем занятии тебя ждёт тест, и сегодня мы будем к нему готовиться "
                  f"вместе. {EXTRA}</p>", "hello_book"),

            mcq("В первом задании тебе нужно проявить смекалку! Посмотри на слова и выбери "
                "одно лишнее", [
                    ("table tennis / taekwondo / tennis / badminton",
                     ["table tennis", "taekwondo", "tennis", "badminton"], "taekwondo"),
                    ("sailing / windsurfing / swimming / ice-skating",
                     ["sailing", "windsurfing", "swimming", "ice-skating"], "ice-skating"),
                    ("spring / January / winter / summer",
                     ["spring", "January", "winter", "summer"], "January"),
                    ("hot / warm / autumn / sunny", ["hot", "warm", "autumn", "sunny"], "autumn"),
                    ("snowy / cold / windy / early", ["snowy", "cold", "windy", "early"], "early"),
                ]),

            ("gaps", {
                "title": "Повторим вопросительные слова и местоимения! Воспользуйся табличками, "
                         "чтобы заполнить пропуски",
                "mode": "type",
                "image": u("tables_question_pronouns"),
                "text": "1. A: __Where__ are you? Are you at school?\n"
                        "2. A: __How__ many cookies are there? B: Six.\n"
                        "3. Your parents are nice. I like __them__.\n"
                        "4. Where's Emma? I can't see __her__.\n"
                        "5. Look at that picture! Do you like __it__?",
                "gaps_expected": 5,
            }),

            # в выгрузке «Открытый вопрос» — у каждого предложения один правильный ответ
            ("exact_input", {
                "title": "Все предложения рассыпались, слова потеряли окончания, а вспомогательные "
                         "глаголы сбежали! Напиши предложения правильно. Образец: Jack / hate / "
                         "play / tennis → Jack hates playing tennis. Обрати внимание на "
                         "окончание -ing — как думаешь, почему?",
                "items": [
                    {"prompt": p, "accept": spellings(s)} for p, s in [
                        ("my sister / not like / roller skate",
                         "My sister doesn't like roller skating."),
                        ("you / like / swim?", "Do you like swimming?"),
                        ("I / love / sing", "I love singing."),
                        ("we / not like / get up / early", "We don't like getting up early."),
                        ("your friends / like / eat / pizza?", "Do your friends like eating pizza?"),
                    ]
                ]}),

            # в выгрузке рассказ Лукаса — страница учебника с фото; у нас текстом
            ("task", {
                "title": "Мой образ жизни ✍️",
                "needs_review": True,
                "html": "<p>Давай вспомним Лукаса и как он рассказывал о себе. Напиши такой же "
                        "небольшой текст, только уже О СЕБЕ!</p>"
                        "<p><b>My lifestyle!</b></p>"
                        "<p><i><b>Sleep.</b> I go to bed at half past nine on school days and I get "
                        "up at eight o'clock. I love sleeping!</i></p>"
                        "<p><i><b>Food.</b> My favourite food is pizza. Mum and Dad don't like "
                        "pizza. Yes, really! They like fruit and vegetables. I drink a lot of "
                        "water.</i></p>"
                        "<p><i><b>Sports and friends.</b> I'm not very sporty but I like watching "
                        "football on TV. I love music and I play the guitar every day after school "
                        "from 5 to 6. I often hang out with Jen, Alex and Lian too!</i></p>",
            }),

            # Wordwall «Anagram · gg1 8.1» — СОСТАВ МОЙ
            ("exact_input", {"title": CHAMPION + "Собери слово из букв ⭐", "items": [
                {"prompt": anagram(en), "accept": [en, en.capitalize()], "image": sport(en),
                 "audio_tts": en}
                for en in ["hockey", "tennis", "skiing", "sailing", "cycling", "volleyball"]
            ]}),

            # Wordwall «Complete the sentence · GG1 8.2 Grammar» — СОСТАВ МОЙ
            ("gaps", {
                "title": "Заполни пропуски ⭐",
                "mode": "drag",
                "text": "1. My dad loves __cooking__ pizza.\n"
                        "2. We don't like __getting__ up early.\n"
                        "3. Does your sister __like__ swimming?\n"
                        "4. Tom __hates__ cleaning his room.\n"
                        "5. Kate is my friend. I like __her__ a lot.\n"
                        "6. These are my cats. I love __them__!",
                "gaps_expected": 6,
            }),

            # Wordwall «Complete the sentence · Go Getter 1 Unit 8.3» — СОСТАВ МОЙ
            ("gaps", {
                "title": "Выбери правильное вопросительное слово ⭐",
                "mode": "drag",
                "text": "1. __Where__ do you live? — In Paris.\n"
                        "2. __Who__ is your sports hero? — Irina Peters.\n"
                        "3. __When__ is the game? — It's on Tuesday.\n"
                        "4. __Whose__ phone is it? — It's Irina's phone.\n"
                        "5. __What__ have you got there? — Her autograph!\n"
                        "6. __How many__ photos have you got? — Eighty.",
                "gaps_expected": 6,
            }),

            bye("<h3>У тебя отлично получилось! 🎉</h3><p>Уверена, ты справишься с тестом "
                "на все сто! Удачи!</p>", "good_luck_clover"),
        ],
    },

    # картинок в PDF теста нет вовсе (лениво подгружались) — свои там, где они помогают
    "u8_test": {
        **U8,
        "lesson_title": "Test",
        "lesson_sort": 7,
        "kind": "test",
        "blocks": [
            ("exact_input", {"title": "Посмотри на картинку и впиши слово по-английски", "items": [
                {"prompt": ru, "accept": list(dict.fromkeys([en, en.capitalize()])),
                 "image": u(p)}
                for en, ru, p in U8_SPORTS
                if en in ["badminton", "basketball", "cycling", "hockey", "ice-skating", "sailing",
                          "skateboarding", "taekwondo", "volleyball", "windsurfing"]
            ]}),

            mcq("Прочитай предложение и выбери пропущенное слово", [
                ("He likes ___ football after school.", ["play", "playing", "plays"], "playing",
                 u("sport_football")),
            ]),
            mcq("Прочитай предложение и выбери пропущенные слова", [
                ("___ is a good friend. I like her.", ["She", "Her"], "She"),
                ("She is a good friend. I like ___.", ["his", "she", "her"], "her"),
            ]),
            mcq("Прочитай предложение и выбери пропущенные слова", [
                ("My sister ___ eating, but she doesn't like cooking.", ["like", "likes"], "likes"),
                ("My sister likes ___, but she doesn't like cooking.", ["eat", "eats", "eating"],
                 "eating"),
                ("My sister likes eating, but she ___ like cooking.", ["don't", "doesn't"],
                 "doesn't"),
                ("My sister likes eating, but she doesn't like ___.", ["cooks", "cook", "cooking"],
                 "cooking"),
            ]),
            mcq("Прочитай диалог и выбери пропущенные слова", [
                ("A: ___ she like playing the piano?", ["Do", "Does"], "Does"),
                ("A: Does she like ___ the piano?", ["play", "plays", "playing"], "playing"),
                ("B: No, she ___. She likes playing the guitar instead.",
                 ["does", "do", "don't", "doesn't"], "doesn't"),
                ("B: No, she doesn't. She likes ___ the guitar instead.",
                 ["play", "plays", "playing"], "playing"),
            ]),
            mcq("Прочитай диалог и выбери пропущенные слова", [
                ("A: What ___ your brother like doing?", ["do", "does"], "does"),
                ("A: What does your brother ___ doing?", ["likes", "liking", "like"], "like"),
                ("A: What does your brother like ___?", ["do", "does", "doing"], "doing"),
                ("B: He ___ listening to music.", ["like", "liking", "likes"], "likes"),
                ("B: He likes ___ to music.", ["listens", "listen", "listening"], "listening"),
            ]),

            # в выгрузке у первого предложения нет точки — добавлена
            order("He doesn't like playing computer games.",
                  title="Расставь слова в правильном порядке"),
            order("What do you like doing?", title="Расставь слова в правильном порядке"),
            order("What is your favourite sport?", title="Расставь слова в правильном порядке",
                  image=sport("tennis")),
            order("What is the weather like today?",
                  ["What", "is", "the weather", "like", "today?"],
                  title="Расставь слова в правильном порядке", image=u("weather_sunny")),
            order("It is good to brush your teeth.",
                  ["It is", "good", "to brush", "your", "teeth."],
                  title="Расставь слова в правильном порядке", image=u("life_brush_teeth")),

            # текста Сары в выгрузке нет — написан под утверждения, ТЕКСТ МОЙ
            ("text", {"html":
                "<h3>READING</h3><p>Прочитай рассказ Сары о своём образе жизни.</p>"
                "<p><i>Hi! I'm Sara and I love sports! In summer I go swimming every day, and in "
                "winter I go ice-skating with my brother. I go to bed at half past nine and I get "
                "up at seven o'clock. I drink two litres of water a day. I eat a lot of fruit — "
                "apples and bananas are my favourite. I brush my teeth two times a day, in the "
                "morning and in the evening. I've got a lot of friends, and we often play "
                "volleyball in the park at the weekend.</i></p>"}),

            ("truefalse", {"title": "READING. Правда или неправда?", "statements": [
                {"text": "Sara doesn't like sports.", "correct": False},
                {"text": "She goes swimming in summer.", "correct": True},
                {"text": "She loves ice-skating in autumn.", "correct": False},
                {"text": "She goes to bed at ten o'clock.", "correct": False},
                {"text": "She drinks two litres of water a day.", "correct": True},
                {"text": "Sara eats a lot of fruit.", "correct": True},
                {"text": "She brushes her teeth one time a day.", "correct": False},
                {"text": "Sara has only a few friends.", "correct": False},
            ]}),

            # аудио в выгрузке пустое — строка в доработать
            ("gaps", {
                "title": "LISTENING. Прослушай прогноз погоды на эту неделю и перетащи нужное "
                         "слово в каждый пропуск",
                "mode": "drag",
                "audio": "",
                "text": "1. On __Sunday__, it's very hot all day.\n"
                        "2. In the afternoon, it's __rainy__.\n"
                        "3. On __Monday__, it's cloudy – there are no blue __skies__.\n"
                        "4. On Saturday morning, it's __sunny__ and __warm__.\n"
                        "5. On Tuesday, it's very __windy__.",
                "gaps_expected": 7,
            }),

            # картинка задания потеряна (видимо, люди со смайликами) — таблица, СОСТАВ МОЙ
            ("speaking", {
                "title": "SPEAKING TASK PART 1 🎤",
                "html": "<p>Посмотри на таблицу. Расскажи, кто что любит или не любит делать. "
                        "Затем расскажи, что любишь / не любишь делать ты. Запиши свой ответ, "
                        "нажав на кнопку микрофона 🙌</p>"
                        "<table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\">"
                        "<tr><th></th><th>😊 likes</th><th>😫 doesn't like</th></tr>"
                        "<tr><td><b>Mary</b></td><td>swimming</td><td>climbing</td></tr>"
                        "<tr><td><b>Tom</b></td><td>playing football</td><td>cooking</td></tr>"
                        "<tr><td><b>Lucy</b></td><td>reading</td><td>getting up early</td></tr>"
                        "<tr><td><b>Ben</b></td><td>cycling</td><td>playing tennis</td></tr>"
                        "</table>"
                        "<p><i>Пример: Mary likes swimming, but she doesn't like climbing. As for "
                        "me, I like…, I don't like…</i></p>",
                "needs_review": True,
            }),

            ("speaking", {
                "title": "SPEAKING TASK PART 2 🎤",
                "html": "<p>Расскажи, что ты делаешь, чтобы вести здоровый образ жизни. Запиши свой "
                        "ответ, нажав на кнопку микрофона 🙌</p>"
                        "<p><i>Пример: I do sport. I don't eat sweets.</i></p>",
                "needs_review": True,
            }),
        ],
    },
}
