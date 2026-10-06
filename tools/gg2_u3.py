"""Go Getter 2 · Unit 3 · Technology — 7 домашек и тест.

Источник: docs/GG2_разбор_u3.md. Промо-баннер «Новогодний челлендж» выброшен
во всех уроках. Части (1)/(2)/(3) Homework 1 и (1)/(2) Homework 5 — один урок.
Homework 6, блоки 4–5: варианты восстановлены — Гарри: tablet, Лили: phone
(подтверждено Анной, «Закрытые вопросы», п. 4).
Кадры учебника с нарисованными людьми берём как есть (там же, п. 5).
"""
from gg2_build import img, shared, todo, video

U = "u3"
UNIT = {"unit": U, "unit_title": "Unit 3 · Technology", "unit_sort": 3}

GADGETS = [  # (англ., перевод, картинка)
    ("mobile phone", "мобильный телефон", "mobile_phone"),
    ("computer", "компьютер", "computer"),
    ("laptop", "ноутбук", "laptop"),
    ("camera", "камера", "camera"),
    ("tablet", "планшет", "tablet"),
    ("TV", "телевизор", "tv"),
    ("headphones", "наушники", "headphones"),
    ("keyboard", "клавиатура", "keyboard"),
    ("mouse", "мышь", "mouse"),
    ("printer", "принтер", "printer"),
    ("screen", "экран", "screen"),
    ("speakers", "колонки", "speakers"),
]

ACTIONS = [
    ("chat online", "общаться онлайн", "chat_online"),
    ("download a song", "скачать песню", "download_song"),
    ("send an email", "отправить электронное письмо", "send_email"),
    ("surf the Internet", "сидеть в интернете", "surf_internet"),
    ("take a selfie/photo", "сделать селфи/фото", "take_selfie"),
    ("talk on the phone", "говорить по телефону", "talk_phone"),
    ("text a friend", "написать другу", "text_friend"),
]


def hello(name, html):
    return ("text", {"html": f'<p><img src="{shared(name)}" alt="" style="height:200px"></p>' + html})


def bye(name, html):
    return ("text", {"html": f'<p><img src="{shared(name)}" alt="" style="height:200px"></p>' + html})


def pic(name, alt="", h=260):
    return f'<p><img src="{img(U, name)}" alt="{alt}" style="max-width:100%;max-height:{h}px"></p>'


def flashcards(words, title):
    return ("flashcards", {"title": title, "cards": [
        {"text": en, "translation": ru, "image": img(U, f), "audio_tts": en.replace("/photo", "")}
        for en, ru, f in words]})


def match_pics(words, title="Соедини картинку со словом"):
    return ("match", {"title": title, "pairs": [
        {"left_image": img(U, f), "right": en, "right_audio_tts": en.replace("/photo", "")}
        for en, ru, f in words]})


def quiz_ru_to_en(words, per_question=4):
    """Отвлекающие — по кругу от самого слова, варианты по алфавиту."""
    qs, n = [], len(words)
    for i, (en, ru, _) in enumerate(words):
        wrong = [words[(i + k) % n][0] for k in range(1, per_question)]
        options = sorted([en] + wrong, key=str.lower)
        qs.append({"q": f"Как по-английски «{ru}»?", "type": "single",
                   "options": [{"text": o} for o in options], "correct": [options.index(en)]})
    return ("quiz", {"questions": qs})


def quiz(*items):
    """quiz(("вопрос", ["вариант", ...], индекс_верного), ...)."""
    return ("quiz", {"questions": [
        {"q": q, "type": "single", "options": [{"text": o} for o in opts], "correct": [c]}
        for q, opts, c in items]})


def order(sentence, image=None):
    p = {"words": sentence.split(" "), "sentence": sentence, "audio_tts": sentence}
    if image:
        p["image"] = img(U, image)
    return ("order", p)


def order_parts(parts, image=None):
    sentence = " ".join(parts)
    p = {"words": list(parts), "sentence": sentence, "audio_tts": sentence}
    if image:
        p["image"] = img(U, image)
    return ("order", p)


def gaps(title, text, n, mode="drag", **extra):
    return ("gaps", {"title": title, "mode": mode, "text": text, "gaps_expected": n, **extra})


def task(title, html):
    return ("task", {"title": title, "needs_review": True, "html": html})


def speaking(title, html, image=None, **extra):
    p = {"title": title, "needs_review": True, "html": html, **extra}
    if image:
        p["image"] = img(U, image)
    return ("speaking", p)


TF = ["True", "False", "Not stated"]

LESSONS = {
    # ------------------------------------------------------------------ HW1
    "u3_hw1": {**UNIT, "lesson_title": "Homework 1", "lesson_sort": 0, "kind": "homework", "blocks": [
        hello("hello_laptop",
              "<h2>Привет! 👋</h2>"
              "<p>Сегодня мы с тобой выучим названия разных электронных устройств. Наверняка многими "
              "из них ты пользуешься каждый день :)</p>"
              "<p>Сначала карточки, потом упражнения и небольшой тест в конце. Ты справишься 💪 Вперёд!</p>"
              "<p>Во второй части домашнего задания ты найдёшь ещё много новых полезных слов. "
              "Не забудь туда заглянуть.</p>"),
        flashcards(GADGETS, "Гаджеты: посмотри, послушай и запомни"),
        match_pics(GADGETS[:6], "Соедини картинку со словом (1)"),
        match_pics(GADGETS[6:], "Соедини картинку со словом (2)"),
        quiz_ru_to_en(GADGETS),

        ("text", {"html": "<h3>Часть 2: что мы делаем с гаджетами</h3>"
                          "<p>Привет-привет! В этой части домашнего задания мы постараемся запомнить выражения, "
                          "которые связаны с интернетом и гаджетами. Они лёгкие и при этом очень полезные!</p>"}),
        flashcards(ACTIONS, "Действия с гаджетами: посмотри, послушай и запомни"),
        match_pics(ACTIONS, "Соедини картинку с выражением"),
        ("exact_input", {"items": [
            {"image": img(U, f), "prompt": f"Напиши по-английски: {ru}",
             "accept": ([en, "take a selfie", "take a photo"] if "/" in en
                        else [en] + (["surf the internet"] if en == "surf the Internet" else [])),
             "audio_tts": en.replace("/photo", "")}
            for en, ru, f in ACTIONS]}),

        hello("hello_highfive",
              "<h3>Часть 3: упражнения</h3>"
              "<p>Огромный привет прекрасному ученику! Здесь тебя ждёт несколько упражнений. Они нужны, "
              "чтобы наверняка запомнить всё-всё, что ты недавно выучил. Давай начинать 😉</p>"),
        gaps("Прочитай историю про Джека и его гаджеты. Вставь пропущенные слова",
             "Jack is a little boy who loves technology. He has a mobile phone, a laptop, and a tablet. "
             "He uses them every day to watch videos and play games. He also has __headphones__, so he can "
             "listen to music without disturbing anyone. Jack's favourite device is his __laptop__. He loves "
             "playing games on it and watching videos on the big __screen__. He has a __camera__, too, so he "
             "can take pictures of himself and his friends. When he needs to type something, he uses a "
             "__keyboard__. He also has a __mouse__ to help him move things around on the __screen__. Jack's "
             "mom has a __printer__, so he can print out pictures and documents when he needs to. Jack likes "
             "to connect his devices to __speakers__, so he can listen to music or watch videos with better "
             "sound. He even knows how to connect his __laptop__ to the __TV__! Jack is very smart and knows "
             "a lot about technology.", 11, image=img(U, "jack")),
        ("match", {"title": "Отлично! Давай теперь соберём фразы — соедини слова так, чтобы получились нужные выражения",
                   "pairs": [{"left": l, "right": r, "right_audio_tts": f"{l} {r}"} for l, r in [
                       ("surf", "the Internet"), ("text", "a friend"), ("chat", "online"),
                       ("talk on", "the phone"), ("download", "a song"), ("send", "an email")]]}),
        gaps("Молодец! Осталось последнее задание 💪 Прочитай диалог и вставь пропущенные слова",
             "A: Let's take a __selfie__. Ready? Smile!\n"
             "B: Cool! I really like your new __mobile__ phone. What else do you use it for?\n"
             "A: Mostly I __text__ my friends, __download__ songs and __surf the__ Internet.\n"
             "B: Can we use it to __chat__ online to Terry?\n"
             "A: Let's check!", 6, image=img(U, "take_selfie")),
        bye("well_done_star", "<h2>Супер! ⭐⭐⭐</h2><p>Вся домашняя работа выполнена. Ты просто крут! "
                              "Увидимся на уроке :)</p>"),
    ]},

    # ------------------------------------------------------------------ HW2
    "u3_hw2": {**UNIT, "lesson_title": "Homework 2", "lesson_sort": 1, "kind": "homework", "blocks": [
        hello("hello_rocket",
              "<h2>Привет-привет, мастер английского языка 😉</h2>"
              "<p>Сегодня тебя ждёт новая домашняя работа. Ты точно с ней справишься, можешь быть уверен :) "
              "Let's go 😃</p>"),
        ("text", {"html": "<p>Внизу тебя ждёт видео 👇</p><ol><li>Посмотри его.</li>"
                          "<li>Включи видео ещё раз и найди не обычного человека, а супергероя. Как только его "
                          "увидишь, попробуй ответить на вопросы: <i>What is he doing? What is he wearing?</i></li></ol>"}),
        video("Посмотри видео и найди супергероя: What is he doing? What is he wearing?",
              "видео на Present Continuous, в нём есть супергерой"),
        todo(("match", {"title": "А теперь давай вспомним, кто что делает. Соедини картинку с предложением",
                        "pairs": [{"left_image": img(U, f), "right": r, "right_audio_tts": r} for f, r in [
                            ("cat_sitting", "It is sitting."), ("fox_running", "She is running."),
                            ("animals_eating", "They are eating."), ("animals_reading", "We are reading.")]]}),
             ("check", "в выгрузке левые картинки (персонажи видео) пустые — поставлены наши зверята: "
                       "кот сидит, лисичка бежит, зверята едят, зверята читают")),
        quiz(("Mum ___ working today.", ["am", "is", "are"], 1),
             ("They ___ chatting online at the moment.", ["are", "am", "is"], 0),
             ("He ___ taking a photo of a famous person.", ["am", "are", "is"], 2),
             ("We ___ watching a film on TV.", ["am", "is", "are"], 2),
             ("I ___ wearing my tracksuit because we have P.E.", ["am", "is", "are"], 0),
             ("You ___ wearing a nice T-shirt. Is it new?", ["is", "are", "am"], 1)),
        gaps("Знакомься! Это Сара. Прочитай про её обычный день и гаджеты, которыми она пользуется. Вставь пропущенные слова",
             "It's a typical day for Sarah. She wakes up and checks her phone. She sees that her friends are "
             "__sending__ emails to each other, so she decides to text them too. She quickly gets dressed and "
             "heads out to meet her friend, Emma. Emma is __wearing__ a new smartwatch that can do lots of "
             "things. They walk to school together, listening to music on their phones. When they arrive at "
             "school, the bell rings and they go to class. In class, the teacher is __talking__ about new "
             "technologies. Sarah is __watching__ TV on her tablet under the desk, but she still hears what "
             "the teacher is __saying__. After class, Sarah and Emma take selfies together with their phones. "
             "Later, Sarah's phone rings — it's her mom. Sarah says goodbye to Emma and goes home. At home, "
             "Sarah's little brother is __playing__ video games on his computer. After dinner, Sarah watches "
             "a movie on her laptop before going to bed. It was a good day, full of new technologies.",
             6, image=img(U, "sarah")),
        order("We are dancing now.", "bunny_dancing"),
        order("He is not jumping.", "dog_not_jumping"),
        order("They are crying.", "kittens_crying"),
        order("His mother and I are walking today.", "bear_panda_walking"),
        order("Sarah and her friend are not cleaning Sarah's room.", "pandas_not_cleaning"),
        task("Что вы делаете сейчас?",
             "<p>Молодец! Предыдущее задание выполнено на ура! А теперь напиши, что делаешь сейчас ты, твоя "
             "семья и твои друзья (пять предложений). Даже если не знаешь, пофантазируй :)</p>"
             "<p><i>Например: I am playing computer games. My friend Jess is dancing. "
             "My brother and sister are going to school.</i></p>"),
        ("text", {"html": "<h3>Правило: как прибавлять -ing</h3>"
                          "<p>Класс! Самое время немножко отдохнуть и почитать одно интересное правило. "
                          "Оказывается, когда мы прибавляем ING к слову, иногда происходит что-то необычное:</p>"
                          "<ul><li>look + ing = look<b>ING</b></li>"
                          "<li>tak<s>e</s> + ing = tak<b>ING</b> — буква <b>e</b> на конце исчезает</li>"
                          "<li>sit + <b>t</b> + ing = sit<b>TING</b> — если в слове короткая гласная, а после "
                          "неё согласная, последнюю букву удваиваем</li></ul>"}),
        ("sort", {"title": "Распредели слова по колонкам (используй правило выше)", "groups": [
            {"name": "look → looking", "items": [{"text": t} for t in ["ask → asking", "surf → surfing", "wait → waiting"]]},
            {"name": "take → taking", "items": [{"text": t} for t in ["dance → dancing", "have → having", "write → writing"]]},
            {"name": "sit → sitting", "items": [{"text": t} for t in ["chat → chatting", "run → running", "stop → stopping"]]},
        ]}),
        task("Опиши картинку",
             "<p>Уррра! Осталось последнее задание 🎉 Посмотри на картинку и составь три положительных и три "
             "отрицательных предложения.</p><p><i>Например: The boy and the girl are jumping. "
             "The animals are not flying.</i></p>" + pic("scene_pool", "У бассейна", 420)),
        todo(("text", {"audio": "",
                       "html": "<p>👏👏👏👏 Это аплодисменты за твои труды! Ты мега крут!</p>"
                               "<p>Для тебя есть ещё дополнительное задание. Оно выполняется по желанию. Если ты "
                               "устал, можешь отложить его. Но если есть силы, вперёд! Сначала послушай пример.</p>"}),
             ("audio", "пример описания картинки (Present Continuous) к следующему заданию")),
        speaking("Опиши картинку 🎤",
                 "<p>Опиши то, что видишь на картинке. Можешь прослушать пример выше и продолжить своё описание. "
                 "Не забудь использовать Present Continuous.</p>", "selfie_teens"),
        bye("well_done_trophy", "<h2>Поздравляю 😉</h2><p>Ты прекрасно выполнил домашнюю работу и можешь "
                                "гордиться собой. До встречи!</p>"),
    ]},

    # ------------------------------------------------------------------ HW3
    "u3_hw3": {**UNIT, "lesson_title": "Homework 3", "lesson_sort": 2, "kind": "homework", "blocks": [
        hello("hello_book",
              "<h2>Привет! 👋</h2><p>Добро пожаловать в новую домашнюю работу :) Здесь тебя как всегда ждут "
              "интересные и даже иногда непростые задания. Но у тебя всё-всё получится. Вперёд 🎉</p>"),
        ("text", {"html": "<p>Внизу тебя ждёт видео. Посмотри его. Когда увидишь вопросы, отвечай на них вслух: "
                          "либо <i>Yes</i>, либо <i>No</i>.</p>"}),
        video("Посмотри видео и отвечай на вопросы вслух: Yes или No",
              "видео с вопросами в Present Continuous (ответы Yes/No)"),
        ("text", {"html": "<h3>Вопросы и краткие ответы</h3><p>Посмотри правило и изучи его. Оно пригодится "
                          "для следующих заданий.</p>" + pic("book_short_answers", "Am I coming? Yes, I am.", 360)}),
        gaps("На картинке — кошка Карла и пёс Большой Эл. Прочитай их диалог и впиши пропущенные слова",
             "Carla: Hi Rocco. Are you playing with Big Al?\n"
             "Rocco: No, I'm not. __Are__ you playing with Big Al?\n"
             "Carla: No, I'm not! Where __is__ he? What __is__ Big Al doing?\n"
             "Rocco: I don't know. __Is__ he answering the phone?\n"
             "Carla: No, he isn't!\n"
             "Big Al: Hi Carla. What __are__ you doing? __Are__ we playing a game?\n"
             "Carla: No, Big Al. I'm looking for you. I'm worried.",
             6, mode="type", image=img(U, "book_carla_big_al")),
        order("Are you texting a friend now?"),
        order("Are you sending an email now?"),
        order("Is your friend texting you now?"),
        order("Is Jessica doing her homework now?"),
        order("What are you wearing now?"),
        ("quiz", {"questions": [
            {"q": "Супер-пупер! Прочитай вопрос и выбери правильный ответ. Are you sending an email? Yes, I ___.",
             "type": "single", "options": [{"text": "is"}, {"text": "am"}, {"text": "are"}], "correct": [1]},
            {"q": "Is he doing his homework? Yes, he ___.", "type": "single",
             "options": [{"text": "is"}, {"text": "am"}, {"text": "are"}], "correct": [0]},
            {"q": "Is she listening to music? No, she ___.", "type": "single",
             "options": [{"text": "am not"}, {"text": "aren't"}, {"text": "isn't"}], "correct": [2]},
            {"q": "Are you having lunch? Yes, we ___.", "type": "single",
             "options": [{"text": "am"}, {"text": "are"}, {"text": "is"}], "correct": [1]},
            {"q": "Are they wearing hats? No, they ___.", "type": "single",
             "options": [{"text": "aren't"}, {"text": "am not"}, {"text": "isn't"}], "correct": [0]},
            {"q": "Am I dreaming? No, you ___.", "type": "single",
             "options": [{"text": "am not"}, {"text": "isn't"}, {"text": "aren't"}], "correct": [2]},
        ]}),
        ("text", {"html": "<p>Смотри, сколько всего ты уже сделал! Первая часть домашней работы позади. "
                          "А сейчас мы с тобой поговорим об эмоциях 😜</p>"}),
        ("match", {"title": "Соедини названия эмоций с картинками", "pairs": [
            {"left_image": img(U, w), "right": w, "right_audio_tts": w}
            for w in ["worried", "angry", "happy", "tired", "scared", "sad", "bored"]]}),
        task("Опиши картинку · 1",
             "<p>Молодец! А теперь посмотри на картинки и опиши их. Расскажи про эмоции героев.</p>"
             "<p><i>Например: They are happy.</i></p>" + pic("cat_tired", "", 240)),
        task("Опиши картинку · 2", "<p>Какие эмоции у героя? Напиши предложение.</p>" + pic("angry_bird", "", 240)),
        task("Опиши картинку · 3", "<p>Какие эмоции у героя? Напиши предложение.</p>" + pic("scared", "", 240)),
        task("Опиши картинку · 4", "<p>Какие эмоции у героев? Напиши предложение.</p>" + pic("bored_students", "", 240)),
        task("Опиши картинку · 5", "<p>Какие эмоции у героини? Напиши предложение.</p>" + pic("worried_woman", "", 240)),
        ("text", {"html": "<p>Уррра!! Домашняя работа сделана. Для тебя есть ещё дополнительное задание. "
                          "Ты можешь его не делать, но оно супер интересное. Нужно помочь лягушке 🐸 добраться до "
                          "берега, отвечая на вопросы.</p>"}),
        todo(("quiz", {"questions": [
            {"q": "🐸 Попробуй, тебе понравится! ___ you watching TV? — Yes, I am.", "type": "single",
             "options": [{"text": "Is"}, {"text": "Are"}, {"text": "Am"}], "correct": [1]},
            {"q": "🐸 Is your dad cooking dinner? — No, he ___.", "type": "single",
             "options": [{"text": "isn't"}, {"text": "aren't"}, {"text": "doesn't"}], "correct": [0]},
            {"q": "🐸 What ___ they doing? — They're playing football.", "type": "single",
             "options": [{"text": "is"}, {"text": "do"}, {"text": "are"}], "correct": [2]},
            {"q": "🐸 ___ I talking too loudly? — No, you aren't.", "type": "single",
             "options": [{"text": "Am"}, {"text": "Is"}, {"text": "Are"}], "correct": [0]},
            {"q": "🐸 Are your friends chatting online? — Yes, they ___.", "type": "single",
             "options": [{"text": "is"}, {"text": "are"}, {"text": "do"}], "correct": [1]},
            {"q": "🐸 Where ___ Anna going? — To the park.", "type": "single",
             "options": [{"text": "are"}, {"text": "does"}, {"text": "is"}], "correct": [2]},
            {"q": "🐸 Is the cat sleeping? — Yes, it ___.", "type": "single",
             "options": [{"text": "is"}, {"text": "does"}, {"text": "are"}], "correct": [0]},
            {"q": "🐸 Why ___ you running? — Because I'm late!", "type": "single",
             "options": [{"text": "is"}, {"text": "are"}, {"text": "do"}], "correct": [1]},
        ]}), ("game", "СОСТАВ МОЙ: пересобрана игра Educaplay «Froggy Jumps» (вопросы и краткие ответы "
                      "Present Continuous) — в выгрузке содержимого нет")),
        bye("well_done_clap", "<h2>Ты заслуживаешь большой-большой похвалы!</h2><p>Вся твоя домашняя работа "
                              "сделана. Самое время немножко отдохнуть. Увидимся на занятии 😉</p>"),
    ]},

    # ------------------------------------------------------------------ HW4
    "u3_hw4": {**UNIT, "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework", "blocks": [
        hello("hello_headphones",
              "<h2>Привет! 👋</h2><p>Здесь тебя ждёт новая домашняя работа. Сегодня мы будем смотреть видео, "
              "разговаривать и делать разные упражнения. У тебя всё получится, как и всегда 😃 "
              "Давай приступим :)</p>"),
        ("text", {"html": "<p>Начнём с видео!</p><ol><li>Сначала посмотри его и найди ответ на вопросы: "
                          "<i>Where is Samantha? Where is Tony?</i></li>"
                          "<li>После этого выбери персонажа, который понравился тебе больше — Тони или "
                          "Саманту. Включи видео ещё раз и повторяй за своим героем.</li></ol>"}),
        video("Посмотри видео: Where is Samantha? Where is Tony?",
              "видео: телефонный разговор Тони и Саманты"),
        ("match", {"title": "Вот это круто! Теперь давай соединим вопросы с ответами. Если нужно что-то "
                            "вспомнить — посмотри видео ещё раз",
                   "pairs": [{"left": l, "right": r, "right_audio_tts": r} for l, r in [
                       ("What are you doing, Tony?", "I'm reading my newspaper."),
                       ("How about you, Samantha?", "I'm shopping at the grocery store."),
                       ("What is Poppy doing?", "She's practising violin in her room."),
                       ("What is Philipp doing?", "He's playing with Fluffy."),
                       ("What is Junior doing?", "He's watching TV and singing.")]]}),
        ("text", {"html": "<p>А теперь давай попробуем сыграть ситуацию, похожую на ту, что мы уже изучили. "
                          "Представь, что ты Елена или Миша. Включи запись и в паузах зачитывай свои реплики "
                          "(они выделены). Давай попробуем!</p>"}),
        todo(("text", {"audio": "", "html":
                       "<p><b>Elena/Misha: Hello?</b><br>"
                       "Amy's Dad: Hi, it's Amy's dad. How are you doing?<br>"
                       "<b>Elena/Misha: Oh, hi! I'm good, thanks.</b><br>"
                       "Amy's Dad: Good to hear. Amy's just upstairs. Amy, it's for you!<br>"
                       "<b>Elena/Misha: Thank you!</b><br>"
                       "Amy: Hi! It's great to hear from you!<br>"
                       "<b>Elena/Misha: Hi Amy! What are you doing?</b><br>"
                       "Amy: I'm watching TV. What about you?<br>"
                       "<b>Elena/Misha: I'm reading a book. I'm bored… Do you want to go to the park?</b><br>"
                       "Amy: Sounds great! See you in fifteen minutes.<br>"
                       "<b>Elena/Misha: See you soon!</b></p>"}),
             ("audio", "реплики Amy и Amy's Dad с паузами для ролевой игры")),
        ("sequence", {"title": "Супер! Расставь диалог между Нилом, миссис Грин и Викки в правильном порядке",
                      "image": img(U, "phone_call"), "items": [{"text": t} for t in [
                          "Hello Mrs Green. It's Neil here. Can I speak to Vicky?",
                          "Yes, Neil. Hang on. Vicky, it's for you!",
                          "Hi Vicky. What are you doing?",
                          "I'm watching TV. What about you, Neil?",
                          "Nothing. Do you want to go swimming at five, Vicky?",
                          "Yes. Great idea. See you soon.",
                          "Bye! See you later."]]}),
        gaps("Вау! На картинке Джанет и миссис Ди, мама Билли. Прочитай их диалог и впиши пропущенные слова",
             "Janet: Hello. It's Janet __here__. Can I __speak__ to Billy, please?\n"
             "Mrs Dee: __Hello|Hi__ Janet. __Just__ a minute. Billy, it's __for__ you.",
             5, mode="type", image=img(U, "book_janet_mrs_dee")),
        gaps("Молодец! С Джанет начал разговаривать Билли. Дочитай разговор и впиши пропущенные слова",
             "Janet: Hi Billy. __What__ are you doing at the moment?\n"
             "Billy: Nothing. What __about__ you?\n"
             "Janet: __I'm|I’m|I am__ bored. Do you want to go to the cinema?\n"
             "Billy: Great __idea__! See you in ten minutes.\n"
             "Janet: Bye. See you __later__.",
             5, mode="type", image=img(U, "book_billy_janet")),
        task("Напиши телефонный разговор",
             "<p>А это дополнительное задание для самых стойких и терпеливых! Представь, что ты, твоя мама и "
             "твой друг разговариваете по телефону. Напиши диалог, используя примеры выше. У тебя получится!</p>"),
        bye("congrats_popper", "<h2>Уррррааа! 🌟</h2><p>Домашняя работа выполнена на отлично, всё благодаря "
                               "твоим стараниям. Увидимся на занятии!</p>"),
    ]},

    # ------------------------------------------------------------------ HW5
    "u3_hw5": {**UNIT, "lesson_title": "Homework 5", "lesson_sort": 4, "kind": "homework", "blocks": [
        hello("hello_highfive",
              "<h2>Привет-привет! 👋</h2><p>Очень здорово, что ты снова решил сделать домашнюю работу. "
              "Сегодня мы будем много читать, но тебе понравится 😎 Ну что, начинаем!</p>"),
        ("text", {"html": "<p>Прочитай интервью. Потом запиши себя на аудио (внизу есть кнопочка). Не забудь "
                          "менять голоса, чтобы было понятно, кто Дэйв, а кто Тэд.</p>"
                          + pic("inventor", "", 260) +
                          "<h3>TECH TED</h3>"
                          "<p><i>Tech Ted is interviewing Dave Fernandez. Dave is a young technology blogger and "
                          "student at North Street Secondary School.</i></p>"
                          "<p><b>Tech Ted:</b> Hi Dave. I can see some photos on the screen. What are you doing in this photo?<br>"
                          "<b>Dave:</b> Hi Ted. In this photo I'm talking to some parents from my school.<br>"
                          "<b>Tech Ted:</b> What are you talking about?<br>"
                          "<b>Dave:</b> I'm asking the parents for help. We need computers for my school.<br>"
                          "<b>Tech Ted:</b> What's wrong with computers at your school?<br>"
                          "<b>Dave:</b> A lot of our computers are old and slow. My friend Hunter knows a lot about "
                          "computers and sometimes he can fix them. But when they stop working, we can't do "
                          "Computer Studies lessons.<br>"
                          "<b>Tech Ted:</b> How can the parents help?<br>"
                          "<b>Dave:</b> Well, their families can give their old computers to my school. You know, "
                          "computers or tablets they don't use. But ones that work of course.<br>"
                          "<b>Tech Ted:</b> Do parents help?<br>"
                          "<b>Dave:</b> Yes! We have four computers and two tablets already. It's amazing.<br>"
                          "<b>Tech Ted:</b> That's brilliant. Good luck with your Computer Studies lessons!<br>"
                          "<b>Dave:</b> Thanks!</p>"}),
        speaking("Прочитай интервью вслух 🎤", "<p>Запиши своё чтение, нажав на кнопку здесь.</p>"),
        task("Who is Dave?", "<p>А теперь давай ответим на вопрос: <b>Who is Dave?</b> Напиши ответ своими "
                             "словами.</p>"),
        todo(("truefalse", {"title": "Прочитай интервью ещё раз. Затем прочитай предложения и выбери: верно "
                                     "это или неверно",
                            "statements": [
                                {"text": "There are some photos on Dave's screen.", "correct": True},
                                {"text": "He is talking to friends in the photo.", "correct": False},
                                {"text": "He is asking people for help in the photo.", "correct": True},
                                {"text": "Dave can do Computer Studies at school.", "correct": False},
                                {"text": "He wants new computers for his school.", "correct": False},
                                {"text": "They have got some computers and tablets.", "correct": True}]}),
             ("check", "утверждение 5 «He wants new computers for his school» — по выгрузке «неверно» (просят "
                       "старые компьютеры родителей), но в тексте «We need computers for my school»; ключ спорный")),
        task("Ответь на вопросы",
             "<p>Великолепно!!! А теперь давай ответим на вопросы письменно.</p>"
             "<ol><li>Who is Tech Ted interviewing?</li><li>Who is Dave talking to in the photo?</li>"
             "<li>What does his school need?</li><li>What can families do to help?</li></ol>"),
        gaps("Закончи предложения, вставив нужные слова в пропуски",
             "1. He's worried __about__ the Computer Studies lessons.\n"
             "2. He's interested __in__ technology.\n"
             "3. She's good __at__ playing computer games.\n"
             "4. Are you __scared__ of aliens?\n"
             "5. I'm really excited __about__ my new tablet!\n"
             "6. Grandpa is bad __at__ using my mobile.", 6),
        ("text", {"html": "<p>Ты большой-большой молодец!!! Самый старательный ученик на свете 👍</p>"
                          "<h3>Часть 2: дневник Пенни</h3>"
                          "<p>Это дополнительная часть домашнего задания. Сегодня мы будем читать дневник одной "
                          "девочки — Пенни. Прочитай текст и запомни, в каких местах Пенни успела побывать :) "
                          "А затем сделай задания по тексту.</p>"}),
        ("text", {"html": "<h3>Penny's holiday diary</h3>"
                          "<p><b>23rd July</b><br>It's day number one of our holiday. We usually go to Spain in the "
                          "summer. We love it there but this year we're in Corsica, in France. It's a beautiful island!</p>"
                          "<p><b>27th July</b><br>There are white beaches and you can go swimming, windsurfing and "
                          "sailing. But today I'm swimming in a lake! There are a lot of lakes and rivers here. The "
                          "longest river is the Golo – it's 90 kilometres long. I want to swim in the lake again but "
                          "Mum says the sea is better. She doesn't like cold water and the water in the lake is cold!</p>"
                          "<p><b>1st August</b><br>It's a beautiful day. We're walking in the mountains. You can go "
                          "mountain biking too. I want to go rock climbing but Dad says it's too dangerous.</p>"
                          "<p><b>3rd August</b><br>Today we're in Ajaccio. Ajaccio is next to the sea and it's the "
                          "coolest town on the island. I love the shops here. It's lunch time now and we're sitting "
                          "under an umbrella and eating sausages and cheese. Yum!</p>"
                          + pic("book_penny_diary", "Penny's diary", 420)}),
        task("Ответь на вопросы по дневнику",
             "<p>Фух, вот это дневник! Давай проверим, насколько хорошо ты запомнил то, что рассказала Пенни. "
             "Ответь на вопросы полными предложениями. Можешь подглядывать в текст 😃</p>"
             "<ol><li>Where does Penny usually go on holiday?</li><li>What water sports can you do in Corsica?</li>"
             "<li>How long is the Golo river?</li><li>Why doesn't Penny's mum like swimming in the lake?</li>"
             "<li>What does Penny's dad think about rock climbing?</li>"
             "<li>It's 3rd August. What are Penny and her family eating?</li></ol>"),
        task("Мой дневник на каникулах",
             "<p>Прекрасная работа 👍 А теперь представь, что ты ведёшь дневник на каникулах. Запиши свои "
             "любимые дни и чем ты занимался. Используй дневник Пенни как пример.</p>"),
        bye("well_done_smiley", "<h2>Ура! 😃</h2><p>Домашняя работа выполнена, ты отлично постарался. "
                                "Увидимся на занятии!</p>"),
    ]},

    # ------------------------------------------------------------------ HW6
    "u3_hw6": {**UNIT, "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework", "blocks": [
        hello("hello_laptop",
              "<h2>Привет, самый лучший ученик! 👋</h2><p>Как твои дела? Сегодня нас ждёт много классных заданий. "
              "Let's go 😉</p>"),
        todo(("text", {"audio": "", "html": "<p>Сначала мы с тобой познакомимся с Гарри и Лили. Послушай их "
                                            "разговор и ниже выбери любимый гаджет каждого из ребят.</p>"}),
             ("audio", "разговор Гарри и Лили о гаджетах (им же пользуются блоки 3–6)")),
        ("quiz", {"questions": [{"q": "Harry: какой его любимый гаджет?", "type": "single",
                                 "image": img(U, "harry"),
                                 "options": [{"text": "phone"}, {"text": "tablet"}], "correct": [1]}]}),
        ("quiz", {"questions": [{"q": "Lily: какой её любимый гаджет?", "type": "single",
                                 "image": img(U, "lily"),
                                 "options": [{"text": "phone"}, {"text": "tablet"}], "correct": [0]}]}),
        todo(gaps("Послушай разговор Лили и Гарри ещё раз. Дополни предложения пропущенными словами",
                  "1. Harry watches __films__ on TV and on his tablet.\n"
                  "2. Harry likes __downloading__ videos.\n"
                  "3. Lily chats __online__ a lot with her friends.\n"
                  "4. Lily also likes __surfing__ the Internet.\n"
                  "5. Lily takes her __phone__ everywhere. She can put it in her __jeans__ or __jacket__.",
                  7, mode="type", audio=""),
             ("audio", "тот же разговор Гарри и Лили, что в блоке 2")),
        ("sort", {"title": "Проверим, насколько хорошо ты запомнил разговор Гарри и Лили :) Распредели их фразы "
                           "в нужный столбик", "groups": [
            {"name": "Harry", "items": [{"text": t} for t in [
                "I've got a TV. I've also got a tablet.", "I download my videos to my tablet."]]},
            {"name": "Lily", "items": [{"text": t} for t in [
                "I've got a mobile phone and I've got a laptop too.", "I also like surfing the Internet.",
                "I can also put it in my jacket."]]},
        ]}),
        gaps("Молодец! Половина домашки уже позади. Вспомни правило с урока и вставь нужные слова в пропуски",
             "1. Too usually comes __at the end__ of a sentence.\n"
             "2. Also usually comes __before__ the verb.\n\n"
             "I listen to music on my CDs. I listen to music on my phone too.\n"
             "I use the computer to do my homework. I also use it to talk to my grandparents.", 2),
        gaps("Уррра! А теперь давай всё закрепим. Впиши в пропуски also или too",
             "My name is Lily. I love technology. I've got a laptop. I've __also__ got a mobile phone. I chat "
             "online to my friends on my phone. I surf the Internet on my phone __too__. I play games on my "
             "laptop and I do my homework on my laptop __too__. My friend Harry __also__ likes technology. "
             "He's got a TV and a tablet __too__. He downloads videos to his tablet.", 5, mode="type"),
        task("Мои гаджеты",
             "<p>Вау! Как отлично ты всё сделал. А теперь расскажи, какие гаджеты есть у тебя. Перепиши текст и "
             "заполни пропуски своими идеями.</p>"
             "<p><i>My technology items: ___ and ___.<br>I use item 1 to ___.<br>I use item 2 to ___.<br>"
             "My friend's technology items: ___ and ___.<br>My friend uses ___ to ___.</i></p>"),
        todo(speaking("Мой любимый гаджет 🎤",
                      "<p>А это задание необязательное, но если ты его сделаешь, то будешь мега крут 💪 Запиши свой "
                      "рассказ про любимое электронное устройство и любимое электронное устройство твоего друга. "
                      "Можешь послушать пример перед тем, как записывать своё аудио.</p>", sample=""),
             ("audio", "пример рассказа о любимых гаджетах")),
        bye("well_done_medal", "<h2>Спасибо тебе огромное за твой труд!</h2><p>Всё сделано просто великолепно! "
                               "До встречи на уроке 😄</p>"),
    ]},

    # ------------------------------------------------------------------ HW7
    "u3_hw7": {**UNIT, "lesson_title": "Homework 7", "lesson_sort": 6, "kind": "homework", "blocks": [
        hello("hello_wave",
              "<h2>Привет! 👋</h2><p>Вот и подходит к концу наш юнит. Самое время повторить всё, что ты прошёл за "
              "это время. Давай начнём. Всё-всё получится 😎</p>"),
        quiz(("Выбери правильный ответ. Is there any paper in the ___?", ["speakers", "printer"], 1),
             ("Turn on the ___ so I can see you.", ["camera", "headphones"], 0),
             ("Let's watch a film on the ___.", ["keyboard", "TV"], 1),
             ("I ___ Computer Studies. I always get 20/20 in the test.", ["am good at", "worry about"], 0),
             ("Are you ___ this film? Don't watch it then!", ["bad at", "scared of"], 1),
             ("I like your ___. The screen is very clear.", ["tablet", "mouse"], 0)),
        ("exact_input", {"items": [
            {"image": img(U, f), "prompt": p, "accept": a, "audio_tts": s}
            for f, p, a, s in [
                ("book_dad_phone", "1. Dad's talking on the ___ with his brother.", ["phone"],
                 "Dad's talking on the phone with his brother."),
                ("book_text_hi", "2. How often do you ___ your friend?", ["text"],
                 "How often do you text your friend?"),
                ("book_boy_selfie", "3. Let's ___ a selfie.", ["take"], "Let's take a selfie."),
                ("book_pets_site", "4. I sometimes ___ the Internet in the evening.", ["surf"],
                 "I sometimes surf the Internet in the evening."),
                ("book_video_chat", "5. We often chat ___ because we've got cameras on our computers.",
                 ["online"], "We often chat online because we've got cameras on our computers."),
                ("book_download_song", "6. I ___ songs to my phone.", ["download"],
                 "I download songs to my phone.")]]}),
        order("I am listening to my favourite song."),
        order("He is sending an email."),
        order("She is not doing her homework."),
        order("We are wearing black trousers."),
        order("They are not having lunch."),
        order("I am running really fast."),
        ("text", {"html": "<p>Самое время посмотреть видео. Ответь на вопросы: <i>Where is Sally? Where is Hana? "
                          "What are they doing?</i></p>"}),
        video("Посмотри видео: Where is Sally? Where is Hana? What are they doing?",
              "видео: Хана звонит Салли, они навещают заболевшую Кейт"),
        todo(gaps("Посмотри видео ещё раз и заполни диалог",
                  "Hana: Hello? Hello. __Can I speak__ to Sally, please?\n"
                  "Sally: Speaking.\n"
                  "Hana: Hi. This is Hana.\n"
                  "Sally: Hi, __Hana|Hannah__. What's up?\n"
                  "Hana: Kate is __sick|ill__.\n"
                  "Sally: That's __too bad__.\n"
                  "Hana: Um, __how about__ going to see her?\n"
                  "Sally: That's a __good idea__. What time shall we meet?\n"
                  "Hana: How about __at two__?\n"
                  "Sally: Sounds good. Let's meet at the __bus stop__.\n"
                  "Hana: Okay. __See you__ then.\n"
                  "Sally: __How are you__?\n"
                  "Kate: I'm okay now. I __can go__ to school on Monday.\n"
                  "Hana: Good!\n"
                  "Sally: Kate, here's an __apple pie__. I made it for you.\n"
                  "Kate: __Thanks|Thank you__. I like apple pie.", 13, mode="type"),
             ("check", "имя в выгрузке то Hana, то Hannah — в тексте везде Hana, в пропуске принимаются оба "
                       "написания; к «sick» добавлен вариант «ill», к «Thanks» — «Thank you». Сверить с видео")),
        bye("congrats_popper",
            "<h2>Молодец! Очень-очень отличная работа 👍</h2><p>Представляешь, ты прошёл целый юнит. Теперь ты "
            "знаешь всё про технологии, можешь говорить про действия, которые происходят сейчас, и разговаривать "
            "по телефону. Увидимся на занятии 😄</p>"),
    ]},

    # ------------------------------------------------------------------ TEST
    "u3_test": {**UNIT, "lesson_title": "Unit 3 Test", "lesson_sort": 7, "kind": "test", "blocks": [
        ("exact_input", {"items": [
            {"prompt": f"Напиши по-английски: {ru}", "accept": acc, "audio_tts": acc[0]}
            for ru, acc in [
                ("общаться онлайн", ["chat online"]),
                ("скачать песню", ["download a song"]),
                ("сидеть в интернете", ["surf the Internet"]),
                ("планшет", ["tablet", "a tablet"]),
                ("наушники", ["headphones"]),
                ("клавиатура", ["keyboard", "a keyboard"])]]}),
        todo(quiz(("Выбери правильный вариант. Look! Tom ___ a selfie with his new phone.",
                   ["takes", "is taking", "is take"], 1),
                  ("We ___ TV right now — we're surfing the Internet.",
                   ["aren't watching", "don't watch", "not watching"], 0),
                  ("— ___ your sister chatting online? — Yes, she is.", ["Does", "Are", "Is"], 2),
                  ("I ___ an email to my grandma at the moment.", ["write", "am writeing", "am writing"], 2),
                  ("What ___ now?", ["you do", "are you doing", "you are"], 1)),
             ("check", "вопрос 5: неверные варианты в выгрузке «What you do / What you are» — лишнее What "
                       "убрано (стоит перед пропуском)")),
        gaps("Поставь глагол в скобках в правильную форму Present Continuous",
             "1. My brother __is downloading__ (download) a new song right now.\n"
             "2. We __are sitting__ (sit) in the kitchen and having lunch.\n"
             "3. They __aren't listening|aren’t listening|are not listening__ (not listen) to music — they're studying.\n"
             "4. — What __is__ Anna __writing__ (write)? — A text message to her friend.\n"
             "5. I __am not using__ (not use) my laptop now, you can take it.",
             6, mode="type"),
        order("What are your friends doing today?"),
        order("I'm not scared of spiders, I'm scared of snakes."),
        order_parts(["Is", "Sophie", "sending", "an email", "to", "her", "teacher?"]),
        order_parts(["They", "aren't", "playing", "computer games", "at the moment."]),
        order_parts(["My", "dad", "is", "talking", "on", "the phone", "now."]),
        ("text", {"html": "<h3>READING</h3><p>Прочитай текст и ответь на вопросы ниже.</p>"
                          "<h3>A Family Video Call</h3>" + pic("video_call", "", 240) +
                          "<p>It's Sunday evening at the Wilson family's house in Manchester. Everyone is at home, "
                          "but they aren't sitting together — they're all using technology!</p>"
                          "<p>In the living room, Mum is having a video call with Grandma. Grandma lives in "
                          "Scotland and they talk every Sunday. Mum is showing her some new photos on the screen.</p>"
                          "<p>Dad is in the kitchen. He's wearing his big headphones and listening to a podcast "
                          "about football. He often does this when he cooks dinner.</p>"
                          "<p>Upstairs, twelve-year-old Lucy is in her bedroom. She's chatting online with her best "
                          "friend Mia about their school project. They're both worried about their History test on "
                          "Monday.</p>"
                          "<p>Lucy's brother Jake is fourteen. He's not very interested in school today — he's "
                          "playing a computer game with his friends and laughing loudly!</p>"}),
        quiz(("Where are the Wilsons today?",
              ["At Grandma's house", "In a café", "At home", "At school"], 2),
             ("Why is Mum showing Grandma photos?",
              ["Grandma is in their house", "They are having a video call", "Grandma is taking selfies",
               "Mum is sending an email"], 1),
             ("What is Dad doing?",
              ["Watching football on TV", "Cooking and listening to a podcast", "Talking on the phone",
               "Eating dinner"], 1),
             ("Why is Lucy talking to Mia?",
              ["Mia is in their kitchen", "They're worried about a test", "They're playing a game together",
               "Mia is her sister"], 1),
             ("Jake is…",
              ["doing his homework", "studying with Lucy", "having fun with his friends online",
               "helping his dad in the kitchen"], 2)),
        todo(("text", {"audio": "", "html": "<h3>LISTENING</h3><p>Послушай разговор по телефону между Эммой и её "
                                            "мамой. Потом выбери для каждого предложения: True (верно), False "
                                            "(неверно) или Not stated (не сказано).</p>"}),
             ("audio", "LISTENING: Эмма звонит маме (от подруги Лили)")),
        quiz(("Emma is calling her mum from home.", TF, 1),
             ("Lily and Emma are doing a school project together.", TF, 0),
             ("Lily's brother is helping them with the computer.", TF, 0),
             ("Lily's brother is fifteen years old.", TF, 2),
             ("Lily's mum is at home.", TF, 1),
             ("Lily's dad is cooking dinner.", TF, 0),
             ("Emma is going home tonight.", TF, 1)),
        speaking("SPEAKING I 🎤",
                 "<p>Посмотри на картинку и ответь на вопросы.</p><ol><li>How many people can you see?</li>"
                 "<li>Where are they?</li><li>What is each person doing right now?</li>"
                 "<li>What gadgets can you see in the picture?</li><li>Who is using headphones?</li></ol>",
                 "scene_gadgets_breakfast"),
        speaking("SPEAKING II 🎤",
                 "<p>Ответь на вопросы полными предложениями.</p><ol><li>What are you doing right now?</li>"
                 "<li>What gadgets have you got?</li><li>What's your favourite gadget?</li>"
                 "<li>Do you usually chat online with your friends or talk on the phone?</li>"
                 "<li>What music are you listening to these days?</li><li>Are you good at computer games?</li>"
                 "<li>What are you scared of?</li><li>Are your parents good at technology?</li></ol>"),
    ]},
}
