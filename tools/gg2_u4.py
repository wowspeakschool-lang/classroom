"""Go Getter 2 · Unit 4 · Our world — 7 домашек и тест.

Источник: docs/GG2_разбор_u4.md (Homework 7 (1) — по PDF, присланному методистом).
Части «(1)» и «(2)» одной домашки — один урок, блоки подряд.

Что сделано не один в один с выгрузкой:
* «Выбери правильный вариант» (варианты внутри пропусков) — quiz, по вопросу на пропуск.
* У quiz и order заголовок в прохождении не показывается, поэтому инструкция
  к ним стоит отдельным text-блоком перед ними.
* Фото детей заменены карточками листа 34 (plato, jake_michael, dan_laptop,
  kayak_river, boat_lake), фото пейзажей HW7 (1) — карточками листов 28–29.
* HW6 №9: еда Ленни и Зака в ключе выгрузки перепутана — исправлено по тексту
  (Lenny — hamburgers, Zach — pizza), подтверждено Анной.
"""
from gg2_build import img, shared, todo, video

U = "u4"
UNIT = {"unit": U, "unit_title": "Unit 4 · Our world", "unit_sort": 4}


def book(name):
    return img(U, f"book_{name}")


def im(src, h=260):
    return f'<p><img src="{src}" alt="" style="max-width:100%;max-height:{h}px;border-radius:12px"></p>'


def hello(name, title, text):
    return ("text", {"html": f'<p><img src="{shared(name)}" alt="" style="height:200px"></p>'
                             f"<h2>{title}</h2>{text}"})


def bye(name, title, text):
    return ("text", {"html": f'<p><img src="{shared(name)}" alt="" style="height:180px"></p>'
                             f"<h3>{title}</h3>{text}"})


def q1(q, options, correct, **extra):
    d = {"q": q, "type": "single", "options": [{"text": o} for o in options], "correct": [correct]}
    d.update(extra)
    return d


def vocab_blocks(words, match_title):
    """flashcards → match картинка↔слово → quiz «как по-английски»."""
    blocks = [
        ("flashcards", {"cards": [{"text": en, "translation": ru, "audio_tts": en, "image": img(U, f)}
                                  for en, ru, f in words]}),
        ("match", {"title": match_title,
                   "pairs": [{"left_image": img(U, f), "right": en, "right_audio_tts": en}
                             for en, ru, f in words]}),
    ]
    n = len(words)
    qs = []
    for i, (en, ru, f) in enumerate(words):
        others = [words[(i + k) % n][0] for k in (3, 5, 7) if (i + k) % n != i]
        others = list(dict.fromkeys(o for o in others if o != en))[:2]
        pos = i % 3
        opts = others[:pos] + [en] + others[pos:]
        qs.append(q1(f"Как по-английски «{ru}»?", opts, pos))
    blocks.append(("quiz", {"questions": qs}))
    return blocks


PLACES = [
    ("beach", "пляж", "beach"), ("city", "крупный город", "city"), ("desert", "пустыня", "desert"),
    ("forest", "лес", "forest"), ("island", "остров", "island"), ("lake", "озеро", "lake"),
    ("mountain", "гора", "mountain"), ("river", "река", "river"), ("sea", "море", "sea"),
    ("town", "городок", "town"), ("volcano", "вулкан", "volcano"), ("waterfall", "водопад", "waterfall"),
]
ADJ_HW2 = [
    ("boring", "скучный", "boring"), ("cheap", "дешёвый", "cheap"), ("dangerous", "опасный", "dangerous"),
    ("difficult", "сложный", "difficult"), ("easy", "лёгкий", "easy"), ("exciting", "увлекательный", "exciting"),
    ("expensive", "дорогой", "expensive"), ("high", "высокий", "high"), ("low", "низкий", "low"),
    ("safe", "безопасный", "safe"),
]
ADJ_HW3 = [
    ("beautiful", "красивый", "beautiful"), ("fast", "быстрый", "fast"), ("friendly", "дружелюбный", "friendly"),
    ("funny", "смешной", "funny"), ("intelligent", "умный", "intelligent"), ("kind", "добрый", "kind"),
    ("strong", "сильный", "strong"),
]


def order(words, image=None):
    s = " ".join(words)
    d = {"words": words, "sentence": s, "audio_tts": s.replace("’", "'")}
    if image:
        d["image"] = image
    return ("order", d)


def tx(html):
    return ("text", {"html": html})


LESSONS = {
    # ------------------------------------------------------------------ HW1
    "u4_hw1": {**UNIT, "lesson_title": "Homework 1", "lesson_sort": 0, "kind": "homework", "blocks": [
        hello("hello_wave", "Привет! 👋",
              "<p>Сегодня тебя ждёт изучение новых слов. Ты повторишь названия разных мест, "
              "которые есть на нашей планете. Давай начинать 😉</p>"),
        *vocab_blocks(PLACES, "Соедини картинку с названием места"),
        hello("hello_highfive", "Привет-привет, самый старательный ученик!",
              "<p>В этой части домашнего задания мы закрепим всё, что выучили. Для этого нужно сделать "
              "несколько упражнений. Время пролетит незаметно. Вперёд 😄</p>"),
        ("hotspot", {
            "title": "Помнишь, в прошлом юните ты с учителем изучал различные технологии? Эту картинку "
                     "нарисовала нейросеть! Поставь название каждого места к нужной точке.",
            "mode": "label",
            "image": book("places_ai"),
            "points": [
                {"x": 47, "y": 27, "text": "waterfall", "audio_tts": "waterfall"},
                {"x": 60, "y": 8, "text": "forest", "audio_tts": "forest"},
                {"x": 30, "y": 44, "text": "lake", "audio_tts": "lake"},
                {"x": 73, "y": 54, "text": "mountain", "audio_tts": "mountain"},
                {"x": 59, "y": 73, "text": "city", "audio_tts": "city"},
                {"x": 66, "y": 90, "text": "beach", "audio_tts": "beach"},
                {"x": 18, "y": 82, "text": "sea", "audio_tts": "sea"},
            ]}),
        ("match", {"title": "Молодец! А теперь соедини название места с его описанием.", "pairs": [
            {"left": "desert", "right": "There aren’t any plants because it’s too hot.",
             "right_audio_tts": "There aren't any plants because it's too hot."},
            {"left": "town", "right": "People live in this small place.",
             "right_audio_tts": "People live in this small place."},
            {"left": "beach", "right": "There is sand next to the sea.",
             "right_audio_tts": "There is sand next to the sea."},
            {"left": "forest", "right": "There are a lot of trees.",
             "right_audio_tts": "There are a lot of trees."},
            {"left": "volcano", "right": "This is a mountain but it hasn’t got a top.",
             "right_audio_tts": "This is a mountain but it hasn't got a top."},
            {"left": "city", "right": "People live in this big place.",
             "right_audio_tts": "People live in this big place."},
        ]}),
        tx("<p>Ты великолепно справился! Посмотри на картинку. Это Платон. Давай узнаем о нём больше. "
           "Прочитай текст и выбери правильный вариант для каждого пропуска.</p>"
           + im(img(U, "plato"))),
        ("quiz", {"questions": [
            q1("I live in Greece. There are ___ with lots of trees …", ["forests", "deserts"], 0),
            q1("… and there are lots of ___ in the sea.", ["waterfalls", "islands"], 1),
            q1("I live in a small ___.", ["town", "beach"], 0),
            q1("In the holidays, I sometimes stay with my uncle in the big ___.", ["river", "city"], 1),
            q1("In winter, we always go skiing in the ___.", ["lake", "mountains"], 1),
            q1("In summer, we go to an island. I like swimming in the ___.", ["sea", "volcano"], 0),
        ]}),
        ("task", {"title": "Необязательное задание: мои места для отдыха", "needs_review": True, "html":
            "<p>Главная часть домашней работы позади, и ты просто супер постарался! Это задание "
            "необязательное. Перерисуй табличку себе на листочек или в тетрадь и заполни её своими "
            "идеями. Можешь написать ответы и здесь. Обязательно поделись тем, что написал, с учителем на уроке.</p>"
            "<table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\">"
            "<tr><th>Holiday places</th><th>Winter or summer?</th><th>Activities you can do there?</th>"
            "<th>How often do you go there?</th></tr>"
            "<tr><td>sea or lake</td><td></td><td></td><td></td></tr>"
            "<tr><td>forest</td><td></td><td></td><td></td></tr>"
            "<tr><td>mountain</td><td></td><td></td><td></td></tr>"
            "<tr><td>town or city</td><td></td><td></td><td></td></tr></table>"}),
        bye("well_done_star", "Классная работа!",
            "<p>Поздравляю — домашняя работа выполнена очень здорово. До встречи на занятии 🖐</p>"),
    ]},

    # ------------------------------------------------------------------ HW2
    "u4_hw2": {**UNIT, "lesson_title": "Homework 2", "lesson_sort": 1, "kind": "homework", "blocks": [
        hello("hello_rocket", "Привет-привет!",
              "<p>Давай вспомним слова, которые ты изучал на уроке. Благодаря этому заданию ты точно "
              "их запомнишь. Вперёд 🏃‍♂️</p>"),
        *vocab_blocks(ADJ_HW2, "Соедини картинку со словом"),
        tx("<h3>Сравниваем! 🤹</h3><p>Настало время для новой домашней работы. Сегодня тебя ждёт одно "
           "интересное правило, которое ты прошёл на уроке, и несколько заданий, которые помогут его усвоить.</p>"
           "<p>Начнём с видео: 1. Посмотри его. 2. Выбери персонажа, который понравился тебе больше всех, "
           "включи видео ещё раз и повторяй за своим героем :)</p>"),
        video("Посмотри видео и повторяй за своим героем", "видео с урока: герои сравнивают себя "
              "(жонглирование, трюки), в конце правило comparative"),
        todo(("match", {"title": "Соедини предложения с героем, который их произносил.", "pairs": [
            {"left": "Герой 1", "right": "You’re faster than me at juggling.",
             "right_audio_tts": "You're faster than me at juggling."},
            {"left": "Герой 2", "right": "Yes, but I’m more surprising than you!",
             "right_audio_tts": "Yes, but I'm more surprising than you!"},
            {"left": "Герой 3", "right": "I’m better than you at tricks.",
             "right_audio_tts": "I'm better than you at tricks."},
        ]}), ("check", "левая часть пар в выгрузке пустая (были картинки героев видео): заменить «Герой 1–3» "
                       "картинками героев и проверить пары по видео")),
        ("match", {"title": "Посмотри на правило. Соедини обычное слово с его сравнительной формой.", "pairs": [
            {"left": "big", "right": "bigger", "right_audio_tts": "bigger"},
            {"left": "high", "right": "higher", "right_audio_tts": "higher"},
            {"left": "exciting", "right": "more exciting", "right_audio_tts": "more exciting"},
            {"left": "dangerous", "right": "more dangerous", "right_audio_tts": "more dangerous"},
            {"left": "good", "right": "better", "right_audio_tts": "better"},
            {"left": "bad", "right": "worse", "right_audio_tts": "worse"},
            {"left": "low", "right": "lower", "right_audio_tts": "lower"},
            {"left": "boring", "right": "more boring", "right_audio_tts": "more boring"},
            {"left": "expensive", "right": "more expensive", "right_audio_tts": "more expensive"},
        ]}),
        tx("<p>Правило-подсказка:</p>" + im(book("comparative_rule"), 360)),
        tx("<p>Великолепно! Следующее задание кажется простым, но будь внимателен. "
           "Расставь слова по порядку, чтобы получились предложения.</p>"),
        order(["I’m", "taller", "than", "my", "friend."]),
        order(["Kayaking", "is", "more", "exciting", "than", "cycling."], img(U, "kayaking")),
        order(["Hamburgers", "are", "better", "than", "hot", "dogs."]),
        order(["Walking", "is", "slower", "than", "running."], img(U, "slow")),
        order(["Winter", "weather", "is", "worse", "than", "summer", "weather."]),
        order(["Geography", "books", "are", "more", "interesting", "than", "Maths", "books."]),
        ("gaps", {"title": "Прочитай разговор Джейка и Майкла и впиши правильную форму слова из скобок.",
                  "mode": "type", "image": img(U, "jake_michael"),
                  "text": "Jake: Let’s go swimming in the lake. The water today is __hotter__ (hot) than yesterday.\n"
                          "Michael: No. Let’s go kayaking. It’s __more exciting__ (exciting) than swimming.\n"
                          "Jake: OK. Let’s get a kayak for two. Two people are __faster__ (fast) than one person.\n"
                          "Michael: OK. And my arms are __longer__ (long) than your arms so I can help you.\n"
                          "Jake: What? That’s not true! My arms aren’t __shorter__ (short) than yours!\n"
                          "Michael: Yes, they are. And I’m a __better__ (good) swimmer than you.\n"
                          "Jake: No, you aren’t. You are a __worse__ (bad) swimmer.",
                  "gaps_expected": 7}),
        ("task", {"title": "Сравни мальчиков", "needs_review": True, "html":
            "<p>Задания становятся всё сложнее! Посмотри на картинку и сравни мальчиков. "
            "Составь четыре предложения.</p>" + im(book("five_boys"), 300) +
            "<p><i>Пример: Tom is shorter than John.</i></p>"
            "<p>Можешь использовать слова: young, old, happy, sad, tall, short, big "
            "(не забудь поставить их в правильную форму).</p>"}),
        ("gaps", {"title": "Какое слово пропущено? Подсказка — первая буква уже дана 😄", "mode": "type",
                  "text": "1. The water in this bottle is c__older__ than the Arctic!\n"
                          "2. Sailing is m__ore__ dangerous than cycling.\n"
                          "3. I’m shorter t__han__ my brother.\n"
                          "4. This bad painting is w__orse__ than that good painting.\n"
                          "5. I can’t do my homework. It’s more d__ifficult__ than the lesson.\n"
                          "6. He’s a better runner t__han__ you.",
                  "gaps_expected": 6}),
        todo(("quiz", {"questions": [
            {**q1("Необязательное задание. Помоги лягушке добраться до берега: выбери слово, которое "
                  "подходит картинке 🐸", ["safe", "dangerous", "boring"], 1), "image": img(U, "dangerous")},
            {**q1("Какое слово подходит картинке?", ["expensive", "cheap"], 0), "image": img(U, "expensive")},
            {**q1("Какое слово подходит картинке?", ["difficult", "easy", "low"], 1), "image": img(U, "easy")},
            {**q1("Какое слово подходит картинке?", ["low", "high"], 1), "image": img(U, "high")},
            {**q1("Какое слово подходит картинке?", ["boring", "exciting", "safe"], 1), "image": img(U, "exciting")},
            {**q1("Какое слово подходит картинке?", ["cheap", "difficult"], 1), "image": img(U, "difficult")},
            {**q1("Какое слово подходит картинке?", ["safe", "dangerous"], 0), "image": img(U, "safe")},
            {**q1("Какое слово подходит картинке?", ["high", "expensive", "low"], 2), "image": img(U, "low")},
        ]}), ("game", "СОСТАВ МОЙ: игры «лягушка» в выгрузке нет (ни ссылки, ни обложки) — пересобрана "
                      "quiz «картинка → прилагательное» по словам HW2")),
        bye("well_done_trophy", "Ура! Домашняя работа выполнена.",
            "<p>Наверное, пора отдохнуть :) Увидимся на занятии 😃</p>"),
    ]},

    # ------------------------------------------------------------------ HW3
    "u4_hw3": {**UNIT, "lesson_title": "Homework 3", "lesson_sort": 2, "kind": "homework", "blocks": [
        hello("hello_book", "Привет-привет!",
              "<p>В первой части домашнего задания мы выучим слова, которые пригодятся для описания "
              "людей или даже животных :) Let’s go 🎉</p>"),
        *vocab_blocks(ADJ_HW3, "Соедини картинку со словом"),
        tx("<h3>Огромный привет!</h3><p>В этой части мы повторим всё, что ты прошёл на уроке с учителем. "
           "Это поможет тебе не только всё запомнить, но и использовать :)</p>"
           "<p>Давай начнём с видео. Посмотри его, а потом сделай задание ниже.</p>"),
        video("Посмотри видео", "видео с урока: superlatives (cat — small, elephant — big, tree — beautiful)"),
        tx("<p>Правило-подсказка:</p>" + im(book("superlative_rule"), 380)),
        ("sort", {"title": "Распредели предложения из видео по колонкам. Можешь подсматривать в правило.",
                  "groups": [
                      {"name": "Adjective", "items": [{"text": "This cat is small."},
                                                      {"text": "This elephant is big."},
                                                      {"text": "This tree is beautiful."}]},
                      {"name": "Comparative (-er / more)", "items": [{"text": "This cat is smaller."},
                                                                     {"text": "This elephant is bigger."},
                                                                     {"text": "This tree is more beautiful."}]},
                      {"name": "Superlative (-est / most)", "items": [{"text": "This cat is the smallest."},
                                                                      {"text": "This elephant is the biggest."},
                                                                      {"text": "This tree is the most beautiful."}]},
                  ]}),
        ("gaps", {"title": "Посмотри на картинку с животными и подбери правильное слово к каждому.",
                  "mode": "drag", "image": book("giraffe_hippo_elephant"),
                  "text": "1. The giraffe is __the tallest__.\n2. The hippo is __the smallest__.\n"
                          "3. The elephant is __the funniest__.",
                  "gaps_expected": 3}),
        ("gaps", {"title": "Впиши правильную форму слова из скобок.", "mode": "type",
                  "image": book("lion_dog_monkey"),
                  "text": "1. The lion is __the most dangerous__ (dangerous).\n"
                          "2. The dog is __the friendliest|the most friendly__ (friendly).\n"
                          "3. The monkey is __the most intelligent__ (intelligent).",
                  "gaps_expected": 3}),
        tx("<p>Наши знакомые — Карла, Рокко и Большой Эл — нарисовали картины! Слева картина Рокко, "
           "посередине — Большого Эла, справа — Карлы. Посмотри на них, а потом прочитай предложения "
           "и выбери правильный вариант.</p>" + im(img(U, "three_paintings"), 300)),
        todo(("quiz", {"questions": [
            q1("Rocco’s painting is ___ Big Al’s painting …", ["the biggest", "bigger than"], 1),
            q1("… but Carla’s painting is ___ of all.", ["the biggest", "bigger"], 0),
            q1("Big Al’s picture and Carla’s picture are ___ Rocco’s picture.", ["better than", "the best"], 0),
            q1("His painting isn’t good! I think it is ___.", ["worse than", "the worst"], 1),
            q1("I think Big Al is ___ artist of all.", ["funnier than", "the funniest"], 1),
            q1("His picture is ___ than Carla’s picture.", ["more interesting", "the most interesting"], 0),
        ]}), ("check", "картинки трёх картин в выгрузке не было — поставлена сгенерированная three_paintings "
                       "(лист 35): проверить, что подходит к предложениям")),
        ("gaps", {"title": "Так держать! Посмотри на этого тигра. Ого! Пока он на нас не смотрит, "
                           "впиши нужные слова в пропуски.",
                  "mode": "type", "image": img(U, "tiger"),
                  "text": "Tigers are bigger __than__ pet cats. They are also __more__ dangerous than pet cats. "
                          "They eat meat. They are faster __than__ many animals so they can catch them. "
                          "I think tigers are __the__ __most__ beautiful cats in the world. "
                          "They’ve got __the__ nicest colours __of__ all the cats. They’ve also got the best faces.",
                  "gaps_expected": 7}),
        ("task", {"title": "Напиши свои предложения о животных", "needs_review": True, "html":
            "<p>Фух, успели — тигр так и не оглянулся :) А теперь непростое задание. Напиши свои "
            "предложения о животных. Используй слова ниже и свои идеи.</p>"
            "<p><i>Пример: nicer than — Giraffes are nicer than monkeys.</i></p>"
            "<ol><li>smaller than</li><li>more intelligent than</li><li>the funniest</li>"
            "<li>the most beautiful</li></ol>"}),
        tx("<p>Великолепно! Какие классные предложения у тебя получились 👍</p>"
           "<p><b>Это задание необязательное</b>, но если ты его выполнишь, будешь по-настоящему крут. "
           "Помнишь картины Карлы, Рокко и Большого Эла? Нарисуй три картины, будто их нарисовали три "
           "разных персонажа.</p>"),
        todo(("speaking", {"title": "Сравни картины 🎤", "needs_review": True, "html":
            "<p>А теперь сравни свои картины между собой. Можешь взять за образец предложения про картины "
            "Карлы, Рокко и Большого Эла. Нажми на микрофон и расскажи.</p>"}),
             ("audio", "аудио-образец ответа (в выгрузке пустой)")),
        bye("well_done_clap", "Спасибо тебе огромное!",
            "<p>Ты сегодня здорово потрудился. Твой учитель тобой гордится, и ты тоже можешь собой "
            "гордиться. До встречи на занятии ⭐</p>"),
    ]},

    # ------------------------------------------------------------------ HW4
    "u4_hw4": {**UNIT, "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework", "blocks": [
        hello("hello_headphones", "Привет-привет! Как твои дела?",
              "<p>В этом домашнем задании мы будем говорить про фильмы 🎥 Ну что, поехали :)</p>"
              + im(img(U, "cinema"), 220)),
        tx("<p>Давай сначала посмотрим видео, где ребята рассказывают про свои любимые фильмы. "
           "Если кажется, что они говорят слишком быстро, нажми на шестерёнку в видео и уменьши скорость 😉</p>"),
        video("Посмотри видео: ребята рассказывают о любимых фильмах", "видео: ребята рассказывают о любимых фильмах"),
        todo(("sequence", {"title": "Вспомни разговор ребят из видео и расставь реплики по порядку.", "items": [
            {"text": "What’s your favourite film?"},
            {"text": "My favourite film is ‘Puss in Boots’."},
            {"text": "What about you?"},
            {"text": "My favourite film is ‘The Angry Birds Movie 2’."},
            {"text": "And what about you?"},
            {"text": "My favourite film is ‘Shrek’."},
        ]}), ("check", "СОСТАВ МОЙ: в выгрузке match «вопрос ↔ фильм» с неоднозначными парами (на любой вопрос "
                       "подходит любой ответ) — сделан sequence в порядке пар выгрузки; сверить порядок фильмов "
                       "с видео. «family film» исправлено на «favourite film»")),
        todo(("speaking", {"title": "Мой любимый фильм 🎤", "needs_review": True, "html":
            "<p>Расскажи про свой любимый мультик или фильм. Нажми на микрофон и запиши ответ.</p>"
            "<p><i>For example: My favourite film is … I think it is funnier than …</i></p>"}),
             ("audio", "аудио-образец рассказа о любимом фильме (в выгрузке пустой)")),
        tx("<p>Супер! Какой интересный рассказ! А сейчас давай расставим слова по порядку. "
           "Можешь подсматривать в подсказку :)</p>" + im(book("opinions"), 300)),
        order(["What’s", "your", "favourite", "subject?"]),
        order(["In", "my", "opinion,", "it’s", "a", "bit", "silly."]),
        order(["What", "about", "you,", "Kim?"]),
        order(["I", "think", "that", "cartoons", "are", "more", "exciting."]),
        order(["What", "do", "you", "think", "of", "adventure stories?"]),
        ("gaps", {"title": "Билли и Патти разговаривают о любимых книгах. Прочитай разговор и впиши "
                           "потерявшиеся слова.",
                  "mode": "type", "image": book("billy_patty"),
                  "text": "Patty: What’s your __favourite|favorite__ book, Billy?\n"
                          "Billy: __My__ favourite book is Harry Potter and the Philosopher’s Stone.\n"
                          "Patty: What do you think __of__ adventure stories?\n"
                          "Billy: I __think__ adventure stories are great. __What__ about you, Patty?\n"
                          "Patty: In my __opinion__, funny stories are better than adventure stories.\n"
                          "Billy: Well, Harry Potter books are adventure stories and they are funny too.\n"
                          "Patty: You’re __right__.",
                  "gaps_expected": 7}),
        tx("<p>Молодец! А теперь представь, что кто-то разговаривает о фильмах с тобой. "
           "Выбери самый подходящий ответ на каждую реплику.</p>"),
        ("quiz", {"questions": [
            q1("What do you think of cartoons?", ["I think they’re funny.", "That’s true."], 0),
            q1("What about you?", ["I often watch a film.", "I prefer Transformers."], 1),
            q1("In my opinion, Frozen is a great film.", ["I think so.", "You’re right."], 1),
            q1("I think action films are better than cartoons.",
               ["My favourite cartoon is Frozen.", "In my opinion, cartoons are better."], 1),
            q1("Do you like cartoons or action films?",
               ["Cartoons. I think they are funnier than action films.", "I don’t like watching cartoons."], 0),
        ]}),
        tx("<p>Великолепно 👍 Давай прочитаем рассказы Тины и Гари об их любимых фильмах.</p>"
           "<p><b>Tina:</b> I like cartoons. I don’t like action films. My favourite film is <i>Minions</i>. "
           "I think it is funnier than an action film.</p>"
           "<p><b>Gary:</b> I don’t like cartoons. I like action films. My favourite film is <i>Transformers</i>. "
           "I think it is more exciting than a cartoon.</p>"),
        todo(("gaps", {"title": "Заполни табличку информацией из текстов.", "mode": "type",
                       "text": "Tina. Cartoons or action films? __cartoons__ · Favourite film: __Minions__ · "
                               "Why? It is __funnier__ than an action film.\n"
                               "Gary. Cartoons or action films? __action films__ · Favourite film: __Transformers__ · "
                               "Why? It is __more exciting__ than a cartoon.",
                       "gaps_expected": 6}),
             ("check", "столбец «Why?» в выгрузке пустой — добавлены пропуски funnier / more exciting из текстов")),
        bye("well_done_smiley", "Bye-bye! 👋", "<p>Отличная работа! До встречи на занятии.</p>"),
    ]},

    # ------------------------------------------------------------------ HW5
    "u4_hw5": {**UNIT, "lesson_title": "Homework 5", "lesson_sort": 4, "kind": "homework", "blocks": [
        hello("hello_wave", "Привет, самый старательный и классный ученик!",
              "<p>Сегодня тебе предстоит много читать :) Но ты точно справишься, ведь для тебя нет "
              "ничего невозможного 😎 Давай начнём?</p>"),
        tx("<p>Сначала прочитаем текст о рекордах, которые установили ученики одной школы, а потом "
           "сделаем по нему несколько заданий.</p>" + im(book("school_records"), 340) +
           "<h3>Friday 24th May: School Records Competition</h3>"
           "<p>What do you think of world records? In my opinion, they are fun and interesting. Well, we have "
           "a School Records Competition every year. It is the funniest day of the year! Everyone can join the fun!</p>"
           "<p><b>These are some records to beat:</b></p><ul>"
           "<li><b>Thomas Baker:</b> He’s the fastest runner. 100m in 14.4 seconds!</li>"
           "<li><b>Katie Lancer:</b> She’s the most intelligent student. 19/20 questions correct in 5 minutes.</li>"
           "<li><b>Mrs Price</b> (our Maths teacher!): Her pizza is the longest of all: 80 centimetres long!</li>"
           "<li><b>Daniella</b> (Mr Nunn’s pet cat!): She’s the most beautiful pet of all. "
           "Bring your photos, not your pets!</li></ul>"
           "<p>Are you faster, taller, more intelligent or maybe funnier than your classmates? Then come to the "
           "School Records Competition and be the best!</p>"
           "<p>Check out the after school clubs website for all the records you can try. There are a lot of them!</p>"
           "<p>Contact me: Gordon Butler for forms.</p>"),
        todo(("quiz", {"questions": [
            q1("О чём текст, который ты прочитал? What is the text about?",
               ["a sports club", "a school competition", "a pet show", "a pizza restaurant"], 1),
        ]}), ("check", "СОСТАВ МОЙ: в выгрузке все 4 варианта — пустые плейсхолдеры; варианты придуманы, "
                       "верный — a school competition")),
        ("gaps", {"title": "Прочитай текст ещё раз. Найди правильный ответ на каждый вопрос.", "mode": "drag",
                  "text": "1. Who is the fastest runner? __Thomas Baker__\n"
                          "2. Who has the competition forms? __Gordon Butler__\n"
                          "3. Who is the cleverest person? __Katie Lancer__\n"
                          "4. Who has the most beautiful pet? __Mr Nunn__\n"
                          "5. Who can make the longest pizza? __Mrs Price__",
                  "gaps_expected": 5}),
        ("task", {"title": "Ответь на вопросы по тексту", "needs_review": True, "html":
            "<p>Прочитай текст ещё раз (если нужно) и ответь на вопросы.</p>"
            "<p><i>Образец: What’s the name of the competition? — School Records Competition.</i></p>"
            "<ol><li>When is the competition?</li><li>What does Gordon think of world records?</li>"
            "<li>Who can join the fun?</li><li>Where can you find all the records?</li>"
            "<li>How many records are there to try?</li></ol>"}),
        tx("<p>Ещё одно очень интересное задание. Посмотри на подсказку, а потом соедини начало "
           "предложения с его концом.</p>" + im(book("look_sizes"), 200)),
        ("match", {"title": "Соедини начало предложения с его концом.", "pairs": [
            {"left": "My parents", "right": "are 42 years old.", "right_audio_tts": "are 42 years old."},
            {"left": "The Eiffel Tower", "right": "is 324 metres high.", "right_audio_tts": "is 324 metres high."},
            {"left": "My baby sister", "right": "is 12 months old.", "right_audio_tts": "is 12 months old."},
            {"left": "My dad", "right": "is 1 metre 80 centimetres tall.",
             "right_audio_tts": "is 1 metre 80 centimetres tall."},
            {"left": "This ruler", "right": "is 30 centimetres long.", "right_audio_tts": "is 30 centimetres long."},
        ]}),
        tx("<p>А вот и последнее задание. <b>Оно необязательное</b>, но будет очень здорово, если ты его "
           "сделаешь :) Мы будем измерять всё, что нас окружает. Сначала нарисуй двух знакомых тебе людей, "
           "одно здание (можно достопримечательность) и один предмет.</p>"),
        todo(("speaking", {"title": "Расскажи о своих рисунках 🎤", "needs_review": True, "html":
            "<p>А теперь расскажи о каждом рисунке: какого он размера или сколько лет человеку.</p>"
            "<p><i>For example: My mum is 38 years old. The Eiffel Tower is 324 metres high.</i></p>"}),
             ("audio", "аудио-образец рассказа о размерах и возрасте (в выгрузке пустой)")),
        bye("congrats_popper", "Bye-bye! 👋", "<p>Ты отлично поработал. Увидимся на занятии!</p>"),
    ]},

    # ------------------------------------------------------------------ HW6
    "u4_hw6": {**UNIT, "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework", "blocks": [
        hello("hello_highfive", "Огромный привет!",
              "<p>Как твоё настроение? Как погода? Самое время сделать новое домашнее задание. Сегодня ты "
              "будешь много слушать и кое-что напишешь. Давай начнём 😉</p>"),
        todo(("text", {"html": "<p>Для начала послушай аудио. Во время прослушивания представляй друзей, "
                               "которых описывают ребята.</p>", "audio": ""}),
             ("audio", "аудио: ребята описывают своих друзей (Lenny и Zach, Bella и Fiona, Fred и Dave, "
                       "Diana и Mary)")),
        ("match", {"title": "Послушай аудио ещё раз и соедини друзей.", "pairs": [
            {"left": "Lenny", "right": "Zach", "right_audio_tts": "Zach"},
            {"left": "Bella", "right": "Fiona", "right_audio_tts": "Fiona"},
            {"left": "Fred", "right": "Dave", "right_audio_tts": "Dave"},
            {"left": "Diana", "right": "Mary", "right_audio_tts": "Mary"},
        ]}),
        ("gaps", {"title": "Прочитай предложения и вставь пропущенные слова. Если трудно — послушай аудио ещё раз.",
                  "mode": "drag",
                  "text": "1. Zach is __older__ than Lenny.\n2. Lenny thinks that Zach is __funny__.\n"
                          "3. Fiona is __smaller__ than Bella.\n4. Fiona is the most __beautiful__ animal.\n"
                          "5. Dave is the __fastest__ runner in the family.\n"
                          "6. Dave is the __best__ friend in the world.\n"
                          "7. Mary is the most __intelligent__ girl in the class.\n"
                          "8. Diana thinks that Mary is a __good__ teacher.",
                  "gaps_expected": 8}),
        tx("<p>Следующее задание — посмотри видео и узнай, что такое абзац (paragraph).</p>"),
        video("Посмотри видео: что такое абзац (paragraph)", "видео «что такое абзац (paragraph)»"),
        ("quiz", {"questions": [
            q1("What is a paragraph?", ["It’s a book about school.", "It’s a big text.",
                                        "It’s a group of sentences."], 2),
        ]}),
        ("sequence", {"title": "Прочитай текст Ленни о его лучшем друге Заке и расставь абзацы по порядку.",
                      "image": img(U, "zak_lenny"), "items": [
            {"text": "My best friend is called Zach. He’s a lot of fun. We spend a lot of time together. "
                     "In some ways we are similar, but in other ways we are different."},
            {"text": "We both like cycling. We go cycling in the mountains. We both like playing football, "
                     "but Zach is faster than I am! We also like playing basketball."},
            {"text": "But we are also different. I am 12, but Zach is 15. Zach likes pizza, but I like hamburgers. "
                     "Zach is a worse Maths student, but he’s a better Art student. He’s a great friend."},
        ]}),
        # Ключ выгрузки исправлен по тексту (подтверждено Анной): Lenny — hamburgers, Zach — pizza.
        ("gaps", {"title": "Отличная работа 👍 Впиши пропущенные слова в табличку о Ленни и Заке.",
                  "mode": "type",
                  "text": "SIMILAR: We both like cycling, __playing football|football|playing basketball|basketball__ "
                          "and __playing basketball|basketball|playing football|football__.\n"
                          "DIFFERENT:\n"
                          "Age — Lenny: __12|twelve__ · Zach: __15|fifteen__\n"
                          "Food — Lenny: __hamburgers|hamburger__ · Zach: __pizza__\n"
                          "Good at — Lenny: __Maths|maths|Math|math__ · Zach: __Art|art__",
                  "gaps_expected": 8}),
        ("task", {"title": "Опиши Ленни от лица Зака", "needs_review": True, "html":
            "<p>Великолепно! Сейчас тебя ждёт непростое, но очень интересное задание. Напиши описание Ленни "
            "от лица Зака. Используй то, что ты уже знаешь о Ленни.</p>"
            "<p><i>Можешь начать так: My best friend is called …</i></p>"}),
        tx("<p>Вот это да! Какой отличный рассказ у тебя получился.</p><p><b>Это задание дополнительное</b>, "
           "но если ты его сделаешь, будет очень круто! Нарисуй Зака и Ленни такими, какими ты их "
           "представляешь. Не забудь показать рисунок учителю :)</p>"),
        bye("well_done_jump", "Bye-bye! 👋", "<p>Ты отлично поработал. До встречи на занятии!</p>"),
    ]},

    # ------------------------------------------------------------------ HW7
    "u4_hw7": {**UNIT, "lesson_title": "Homework 7", "lesson_sort": 6, "kind": "homework", "blocks": [
        hello("hello_rocket", "Hello, dear student!",
              "<p>Представляешь, ты уже заканчиваешь четвёртый юнит! В этой домашней работе тебя ждёт "
              "повторение того, что ты прошёл. Ты наверняка всё отлично помнишь. Let’s go 🚀</p>"),
        tx("<p>Посмотри на картинку и выбери, что на ней изображено.</p>"),
        ("quiz", {"questions": [
            {**q1("What is it?", ["sea", "river", "beach"], 0), "image": img(U, "sea")},
            {**q1("What is it?", ["city", "forest", "grass"], 1), "image": img(U, "forest")},
            {**q1("What is it?", ["island", "volcano", "mountain"], 1), "image": img(U, "volcano")},
            {**q1("What is it?", ["waterfall", "river", "desert"], 2), "image": img(U, "desert")},
            {**q1("What is it?", ["town", "mountain", "forest"], 1), "image": img(U, "mountain")},
            {**q1("What is it?", ["lake", "beach", "volcano"], 0), "image": img(U, "lake")},
        ]}),
        ("gaps", {"title": "Отлично! Теперь поработаем со словами. Прочитай предложения и вставь нужные слова.",
                  "mode": "drag",
                  "text": "1. Geography trips aren’t boring. They’re __exciting__.\n"
                          "2. Be careful. That dog isn’t __friendly__.\n"
                          "3. I can’t do my homework. It’s __difficult__.\n"
                          "4. He is a __fast__ runner.\n"
                          "5. I can’t buy this watch because it’s very __expensive__.\n"
                          "6. My bike isn’t dangerous. It’s __safe__.",
                  "gaps_expected": 6}),
        ("gaps", {"title": "Прочитай предложения и впиши нужную форму слова из скобок.", "mode": "type",
                  "text": "1. My feet are __bigger than__ (big) your feet!\n"
                          "2. This test is __easier than__ (easy) the last test.\n"
                          "3. I think it’s __more difficult than__ (difficult) the last test!\n"
                          "4. My brother is __better than__ (good) me at Maths!\n"
                          "5. This car is __more expensive than__ (expensive) that one.\n"
                          "6. Today is __hotter than__ (hot) yesterday.",
                  "gaps_expected": 6}),
        tx("<p>В этом задании ты точно мастер! Составь из слов предложения.</p>"),
        order(["This", "is", "the", "highest", "mountain", "in", "my", "country."], book("mountain_cartoon")),
        order(["This", "pizza", "is", "the", "cheapest", "meal."], book("pizza")),
        order(["This", "is", "the", "best", "holiday", "of", "all."], img(U, "beach")),
        order(["This", "is", "the", "worst", "ice", "cream."], book("icecream")),
        order(["My", "sister", "is", "the", "most", "beautiful", "person", "in", "my", "family."]),
        order(["You", "are", "the", "most", "intelligent", "student", "in", "my", "class."], img(U, "intelligent")),
        tx("<p>Супер! Давай прочитаем разговор Лукаса и Эми (это герои видео, которое ты смотришь с учителем "
           "на уроке). Выбери правильный вариант для каждого пропуска :)</p>"),
        ("quiz", {"questions": [
            q1("Lucas: ___ your favourite film?", ["What", "What’s"], 1),
            q1("Amy: My ___ Frozen.", ["favourite film is", "favourite is"], 0),
            q1("Amy: What ___ you?", ["do", "about"], 1),
            q1("Lucas: I like Shrek. What do you ___ of going to the cinema?", ["think", "thinking"], 0),
            q1("Amy: ___ my opinion, it’s great.", ["On", "In"], 1),
            q1("Lucas: You’re ___. Going to the cinema is great.", ["right", "true"], 0),
        ]}),
        tx("<p>Первая часть домашнего задания позади! Дальше тебя ждут интересные задания о спорте "
           "и отдыхе на природе. А ты любишь спорт? ⚽ 🚴 ⚾</p><p>Посмотри на картинки и выбери правильный вариант.</p>"),
        ("quiz", {"questions": [
            {**q1("I like big ___.", ["islands", "cities", "mountains"], 1), "image": img(U, "city")},
            {**q1("I like activities on the ___.", ["river", "sea", "beach"], 0), "image": img(U, "kayak_river")},
            {**q1("We always ride bikes in the ___.", ["city", "volcano", "forest"], 2), "image": img(U, "bike_forest")},
            {**q1("I love activities on the ___.", ["town", "lake", "desert"], 1), "image": img(U, "boat_lake")},
        ]}),
        ("gaps", {"title": "Прочитай текст про каникулы в городе и вставь пропущенные буквы — по одной в каждый пропуск.",
                  "mode": "type", "image": book("city_park"),
                  "text": "I like city holidays. Cities are not b__o__r__i__ng at all. They are exc__i__t__i__ng places. "
                          "They are sometimes exp__e__ns__i__v__e__, so you need money. But you can find ch__e____a__p "
                          "places to eat burgers and pizzas. In many cities there are b__e____a____u__t__i__f__u__l parks. "
                          "Some cities are d__a__ng__e__r__o____u__s because there are lots of f__a__st cars. But most "
                          "cities have got buses, so it is __e____a__sy to get to places. People are usually "
                          "fr__i____e__ndly and k__i__nd to tourists.",
                  "gaps_expected": 24}),
        ("match", {"title": "Соедини название вида спорта с картинкой.", "pairs": [
            {"left_image": img(U, "kayaking"), "right": "kayaking", "right_audio_tts": "kayaking"},
            {"left_image": img(U, "climbing"), "right": "climbing", "right_audio_tts": "climbing"},
            {"left_image": img(U, "parachute"), "right": "jumping with a parachute",
             "right_audio_tts": "jumping with a parachute"},
            {"left_image": img(U, "sailing"), "right": "sailing", "right_audio_tts": "sailing"},
            {"left_image": img(U, "fishing"), "right": "fishing", "right_audio_tts": "fishing"},
        ]}),
        ("task", {"title": "Необязательное задание: мой любимый спорт", "needs_review": True, "html":
            "<p>Оно необязательное, но будет очень здорово, если ты его сделаешь. Нарисуй картинку со своим "
            "любимым видом спорта. Покажи её учителю на уроке и расскажи о ней. Можешь написать здесь, "
            "что ты нарисовал.</p>"}),
        # --- часть (2)
        tx(f'<p><img src="{shared("hello_laptop")}" alt="" style="height:180px"></p>'
           "<h3>Привет! Это вторая часть домашней работы :)</h3><p>И она последняя в этом юните. Здесь ты "
           "узнаешь кое-что об интересных технологиях и прочитаешь объявления. Прочитай три очень "
           "познавательные истории о технологиях, а потом сделаем по ним задания 😊</p>"),
        tx(im(book("kitchen_robot"), 240) +
           "<p>Micky Bailey’s parents have got a … robot! They’re very excited about it. It’s a kitchen robot and "
           "it makes dinner for Micky’s family every day. It’s very good at cooking! Micky’s mum and dad are really "
           "happy. Now they don’t need to cook dinner so now they’ve got more time. All they need to do is go shopping!</p>"),
        tx(im(book("dog_attila"), 240) +
           "<p>David Smith’s new puppy, Attila, is friendly and intelligent. David is worried about Attila because "
           "he sometimes gets lost. Like all dogs in the UK, Attila has got a microchip so the police know his name "
           "and address. The microchip isn’t new technology but it’s David’s favourite!</p>"),
        tx(im(img(U, "dan_laptop"), 240) +
           "<p>Suzie Highton’s brother Dan can’t see very well. He can’t see text in books. The most important "
           "technology in Suzie’s house is a computer program. Dan can download books onto his computer. The text "
           "is big so he can see it and the computer reads it aloud too.</p>"),
        ("gaps", {"title": "Ты огромный молодец! Впиши одно или два слова в каждый пропуск. Пример: Micky’s "
                           "parents are very excited about their new robot.",
                  "mode": "type",
                  "text": "1. The robot is __good at__ cooking.\n"
                          "2. Attila is David’s __dog|puppy__.\n"
                          "3. David is __worried about__ Attila because he sometimes gets lost.\n"
                          "4. David’s favourite technology is Attila’s __microchip__.\n"
                          "5. Suzie Highton’s brother can’t __see__ very well.\n"
                          "6. Dan can see text on his computer because it’s __big__.",
                  "gaps_expected": 6}),
        ("gaps", {"title": "Посмотри на картинку и допиши предложения.", "mode": "type",
                  "image": book("river_scene"),
                  "text": "1. The boy with the tablet feels __scared__.\n"
                          "2. The dog is playing __in the river|in the water__.\n"
                          "3. The blue boat is bigger __than the red boat|than the red one__.\n"
                          "4. The yellow boat is __the biggest|the biggest boat|the biggest one__.",
                  "gaps_expected": 4}),
        ("task", {"title": "Ответь на вопросы по картинке", "needs_review": True, "html":
            "<p>Задание усложняется! Теперь нужно не просто дописать слова, а ответить на вопросы по той же "
            "картинке. Ты точно-точно справишься 💪</p>" + im(book("river_scene"), 300) +
            "<ol><li>What is the girl doing?</li><li>What’s the girl wearing?</li>"
            "<li>What’s the woman wearing?</li></ol>"}),
        tx("<p>Первая часть этой домашней работы позади. Теперь осталось совсем немножко!</p>"),
        ("task", {"title": "Прочитай объявления и ответь на вопросы", "needs_review": True, "html":
            im(book("game_ads"), 300) +
            "<p><i>Даты выхода игр (на картинке мелко): Shark City — August 2017, Volcano Disaster! — March 2015, "
            "Desert Adventure — September 2017.</i></p>"
            "<ol><li>What’s the shark doing?</li><li>What’s the girl doing?</li>"
            "<li>Which game is the most expensive?</li>"
            "<li>Is Desert Adventure more difficult than Volcano Disaster?</li>"
            "<li>Which is the newest game?</li></ol>"}),
        todo(("gaps", {"title": "Послушай разговор Софи и папы и вставь пропущенные слова. "
                                "Пример: Sophie is doing her Geography homework.",
                       "mode": "drag", "audio": "",
                       "text": "1. Studying: mountains, lakes and __waterfalls__\n"
                               "2. Ben Nevis, Scotland: the __highest__ __mountain__ in the UK\n"
                               "3. Windermere: __17__ kilometres long\n"
                               "4. Volcanoes: sometimes __very__ __dangerous__",
                       "gaps_expected": 6}),
             ("audio", "аудио: разговор Софи и папы о домашке по географии (Ben Nevis, Windermere, вулканы)")),
        tx("<p>И-и-и — последнее задание на сегодня! Прочитай диалоги и выбери самый подходящий ответ.</p>"),
        ("quiz", {"questions": [
            q1("Ben: Are you busy? May: …", ["No, I’m doing my homework.", "Yes, it’s busy.",
                                              "Yes, I’m downloading music."], 2),
            q1("Ben: Let’s go to the cinema! May: …", ["OK. Tickets are cheap today.", "You’re right, it’s boring.",
                                                        "OK. It’s on TV."], 0),
            q1("Ben: What do you think of Star Trek? May: …", ["I’m worried about it.", "I think it’s amazing!",
                                                               "Well done!"], 1),
            q1("Ben: What time is the film? May: …", ["We can walk.", "It’s at 5 p.m.", "Yes, it is."], 1),
            q1("Ben: Let’s meet at my house. May: …", ["I like your house.", "What’s my address?",
                                                        "OK, see you later."], 2),
        ]}),
        bye("well_done_trophy", "Великолепная работа!",
            "<p>Поздравляю тебя с окончанием большой-пребольшой темы! Ты отлично потрудился и узнал много нового "
            "о технологиях, научился сравнивать предметы и интересоваться мнением других. Твой учитель очень-очень "
            "гордится тобой! Увидимся на занятии 😎</p>"),
    ]},

    # ------------------------------------------------------------------ Test
    "u4_test": {**UNIT, "lesson_title": "Unit 4 Test", "lesson_sort": 7, "kind": "test", "blocks": [
        ("exact_input", {"items": [
            {"image": img(U, f), "prompt": f"Напиши по-английски: {ru}", "accept": [en, en.capitalize()],
             "audio_tts": en}
            for en, ru, f in [("beach", "пляж", "beach"), ("desert", "пустыня", "desert"),
                              ("island", "остров", "island"), ("mountain", "гора", "mountain"),
                              ("volcano", "вулкан", "volcano"), ("waterfall", "водопад", "waterfall")]
        ]}),
        tx("<p>Выбери правильный вариант, чтобы предложение было грамматически верным.</p>"),
        ("quiz", {"questions": [
            q1("The Nile is ___ the Thames.", ["longer than", "more long than", "longer that"], 0),
            q1("Mount Everest is ___ mountain in the world.", ["highest", "the highest", "the most high"], 1),
            q1("This film is ___ than the book.", ["excitinger than", "more exciting that", "more exciting"], 2),
            q1("My brother is ___ person in our family.", ["the funnyest", "the funniest", "most funny"], 1),
            q1("Russian is ___ than English for tourists.", ["more difficult", "difficulter than",
                                                             "more difficult that"], 0),
        ]}),
        ("gaps", {"title": "Поставь прилагательное в скобках в правильную форму (comparative / superlative).",
                  "mode": "type",
                  "text": "1. The Sahara is __the biggest__ (big) desert in the world.\n"
                          "2. A train is __cheaper__ (cheap) than a plane.\n"
                          "3. This is __the most beautiful__ (beautiful) beach I know!\n"
                          "4. My new bike is __better__ (good) than my old one.\n"
                          "5. Today the weather is __worse__ (bad) than yesterday.",
                  "gaps_expected": 5}),
        tx("<p>Расставь части предложения в правильном порядке.</p>"),
        order(["Italy", "is", "smaller", "than", "Spain."]),
        order(["The", "Amazon", "is", "the", "longest", "river", "in", "South America."]),
        order(["Climbing", "mountains", "is", "more", "dangerous", "than", "swimming."]),
        order(["What", "is", "the", "most", "interesting", "city", "in", "your", "country?"]),
        order(["My", "sister", "is", "kinder", "than", "my", "brother."]),
        tx("<h3>READING</h3><p>Прочитай текст, потом перетащи слова и числа в пропуски в предложениях.</p>"
           "<h3>Three Amazing Places</h3>"
           "<p>The world has thousands of beautiful places. Here are three of them.</p>"
           "<p>The Sahara is the biggest hot desert in the world. It’s in North Africa and it’s bigger than many "
           "countries – about 9 million square kilometres! It’s a very dangerous place because it’s so hot and dry. "
           "But it’s also beautiful and famous.</p>"
           "<p>Lake Baikal is in Russia. It isn’t the biggest lake in the world, but it’s the deepest – 1,642 metres "
           "deep! It’s also the oldest lake on Earth. In winter the water freezes and people sometimes walk on the ice.</p>"
           "<p>Angel Falls in Venezuela is the highest waterfall in the world. It’s 979 metres high. The forest around "
           "it is dangerous and difficult for tourists, so it’s not as popular as Niagara Falls.</p>"),
        ("gaps", {"title": "Перетащи слова и числа в пропуски.", "mode": "drag",
                  "text": "1. The Sahara is the __biggest__ hot desert in the world.\n"
                          "2. The Sahara is in __North Africa__.\n"
                          "3. Lake Baikal is the __deepest__ lake on Earth.\n"
                          "4. Lake Baikal is __1,642__ metres deep.\n"
                          "5. Angel Falls is __979__ metres high.\n"
                          "6. Angel Falls is in __Venezuela__.\n"
                          "7. Niagara Falls is __more popular__ than Angel Falls for tourists.",
                  "gaps_expected": 7}),
        todo(("quiz", {"questions": [
            q1("<b>LISTENING.</b> Послушай интервью с туристом и выбери правильный ответ на каждый вопрос.<br>"
               "1. What is Marco’s job?", ["tour guide", "travel blogger", "photographer", "teacher"], 1, audio=""),
            q1("What does Marco think about New Zealand?",
               ["It’s the biggest country he knows.", "It’s the most beautiful country he knows.",
                "It’s the most expensive country he knows.", "It’s the most dangerous country he knows."], 1),
            q1("According to Marco, people in New Zealand are … than in other countries.",
               ["funnier", "cleverer", "friendlier", "richer"], 2),
            q1("Where did Marco go last year?", ["New Zealand", "Brazil", "Iceland", "Italy"], 2),
            q1("What was the weather like in Iceland?",
               ["hotter than he expected", "colder than he expected", "the same as he expected",
                "the worst weather of his life"], 1),
            q1("Why is the Amazon forest dangerous?",
               ["The mountains are very high.", "There are dangerous animals.", "It’s too cold there.",
                "People aren’t friendly."], 1),
        ]}), ("audio", "аудио LISTENING: интервью с туристом Марко (вставить в вопрос 1)")),
        ("speaking", {"title": "SPEAKING I 🎤", "needs_review": True, "image": book("mountain_lake"), "html":
            "<p>Опиши картинку и ответь на вопросы. Нажми на микрофон и запиши ответ.</p>"
            "<ol><li>What can you see in the picture?</li><li>Are the mountains high or low?</li>"
            "<li>Is the lake big or small?</li><li>Is this place beautiful?</li>"
            "<li>Is it a dangerous place or a safe place?</li><li>What’s the most beautiful thing in the picture?</li></ol>"}),
        ("speaking", {"title": "SPEAKING II 🎤", "needs_review": True, "html":
            "<p>Ответь на вопросы полными предложениями. Нажми на микрофон и запиши ответ.</p>"
            "<ol><li>What’s the biggest city in your country?</li><li>What’s the longest river in your country?</li>"
            "<li>Are mountains more beautiful than the sea?</li>"
            "<li>What’s the most interesting place in your town or city?</li>"
            "<li>Who is the funniest person in your family?</li>"
            "<li>What’s more exciting: football or computer games?</li>"
            "<li>What’s more difficult: Maths or English?</li>"
            "<li>What’s the most dangerous animal you know?</li></ol>"}),
    ]},
}
