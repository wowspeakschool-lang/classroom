"""GG2 · Unit 2 · Food — 7 домашек и тест. Источник: docs/GG2_разбор_u2.md.

Части (1)/(2) одной домашки — один урок, блоки подряд. Баннер «Новогодний
челлендж» выброшен везде. Фото реальных людей заменены нарисованными
героями листа «Герои Unit 2» (max, anya_pancakes, …). «Выбери правильный
вариант» с вариантами внутри пропусков — quiz, по вопросу на пропуск;
варианты не перемешиваются при показе, поэтому место верного разведено руками.
"""
import random

from gg2_build import img, shared, todo, video

U = "u2"
UNIT = {"unit": U, "unit_title": "Unit 2 · Food", "unit_sort": 2}


def hello(name, title, body):
    return ("text", {"html": f'<p><img src="{shared(name)}" alt="" style="height:200px"></p>'
                             f"<h2>{title}</h2>{body}"})


def bye(name, title, body):
    return ("text", {"html": f'<p><img src="{shared(name)}" alt="" style="height:180px"></p>'
                             f"<h3>{title}</h3>{body}"})


def pic(name, alt=""):
    return f'<p><img src="{img(U, name)}" alt="{alt}" style="max-width:100%;max-height:320px"></p>'


def q(text, options, correct):
    """Вопрос с одним верным: correct — индекс верного варианта."""
    return {"q": text, "type": "single", "options": [{"text": o} for o in options], "correct": [correct]}


def flashcards(words):
    return ("flashcards", {"cards": [
        {"text": en, "translation": ru, "audio_tts": en, "image": img(U, f)} for en, ru, f in words]})


def match_pics(words, title="Соедини картинку со словом"):
    return ("match", {"title": title, "pairs": [
        {"left_image": img(U, f), "right": en, "right_audio_tts": en} for en, ru, f in words]})


def quiz_ru_to_en(words, per_question=4):
    """«Как по-английски»: отвлекающие — соседи по списку с обеих сторон, варианты перемешаны
    с постоянным зерном (сборка повторяема), чтобы верный не стоял всегда на одном месте."""
    qs, n = [], len(words)
    step = 3 if n > 3 * per_question else 1
    for i, (en, ru, _) in enumerate(words):
        wrong = [words[(i + k * step) % n][0] for k in (-1, 1, 2)[:per_question - 1]]
        options = [en] + wrong
        random.Random(f"{en}|{n}").shuffle(options)
        qs.append({"q": f"Как по-английски «{ru}»?", "type": "single",
                   "options": [{"text": o} for o in options], "correct": [options.index(en)]})
    return ("quiz", {"questions": qs})


def accept(en):
    out = []
    for v in (en, en.lower(), en[0].upper() + en[1:]):
        if v not in out:
            out.append(v)
    return out


FOOD_1 = [
    ("apple", "яблоко", "apple"), ("biscuits", "печенье", "biscuits"), ("bread", "хлеб", "bread"),
    ("cereal", "хлопья", "cereal"), ("cheese", "сыр", "cheese"), ("chicken", "курица", "chicken"),
    ("chips", "картошка фри", "chips"), ("fish", "рыба", "fish"),
    ("fruit", "фрукты", "fruit"), ("ham", "ветчина", "ham"), ("meat", "мясо", "meat"),
    ("orange juice", "апельсиновый сок", "orange_juice"), ("pancakes", "блины", "pancakes"),
    ("pasta", "макароны", "pasta"), ("potato", "картофель", "potato"), ("rice", "рис", "rice"),
    ("salad", "салат", "salad"), ("sandwich", "сэндвич", "sandwich"), ("sausage", "сосиска", "sausage"),
    ("tomato", "помидор", "tomato"), ("tuna", "тунец", "tuna"), ("vegetables", "овощи", "vegetables"),
    ("water", "вода", "water"), ("yoghurt", "йогурт", "yoghurt"),
]

FOOD_2 = [
    ("butter", "сливочное масло", "butter"), ("chocolate", "шоколад", "chocolate"), ("egg", "яйцо", "egg"),
    ("flour", "мука", "flour"), ("lemon", "лимон", "lemon"), ("milk", "молоко", "milk"),
    ("strawberry", "клубника", "strawberry"), ("sugar", "сахар", "sugar"),
]

CONTAINERS = [
    ("a bar of chocolate", "плитка шоколада", "bar_of_chocolate"),
    ("a bottle of water", "бутылка воды", "bottle_of_water"),
    ("a can of cola", "банка колы", "can_of_cola"),
    ("a carton of juice", "пачка сока", "carton_of_juice"),
    ("a jar of jam", "баночка варенья", "jar_of_jam"),
    ("a packet of biscuits", "пачка печенья", "packet_of_biscuits"),
]


LESSONS = {
    # ------------------------------------------------------------------ HW1
    "u2_hw1": {**UNIT, "lesson_title": "Homework 1", "lesson_sort": 0, "kind": "homework", "blocks": [
        hello("hello_wave", "Привет! 👋",
              "<p>Надеюсь, ты перекусил перед домашним заданием, так как сегодня нас с тобой ждут "
              "вкусняшки 😋</p><p>Выполни все задания, чтобы выучить слова на 100%! В конце первой "
              "части тебя ждёт небольшой тест.</p>"),
        todo(flashcards(FOOD_1),
             ("check", "chips переведено «картошка фри» (в выгрузке «чипсы»): в британском chips — "
                       "картофель фри, и картинка, и fish and chips в HW5 про него")),
        match_pics(FOOD_1[:8]),
        match_pics(FOOD_1[8:16]),
        match_pics(FOOD_1[16:]),
        quiz_ru_to_en(FOOD_1),
        hello("hello_rocket", "Дополнительная часть 🚀",
              "<p>Добро пожаловать во вторую, ДОПОЛНИТЕЛЬНУЮ часть домашки. Выполни все упражнения, "
              "чтобы хорошенько запомнить новые слова! Выполнив эти задания, ты станешь МЕГА крутым "
              "учеником!</p>"),
        ("gaps", {
            "title": "Прочти предложения и перетащи в пропуски слова, подходящие по смыслу. Ты справишься!",
            "mode": "drag",
            "text": "1. I usually have __cereal__ for breakfast. I like corn flakes best.\n"
                    "2. Have we got any bread? I want to make a ham __sandwich__.\n"
                    "3. I like __tuna__. It's my favourite fish.\n"
                    "4. Can I have a chocolate __biscuit__ with my tea?\n"
                    "5. __Apples__ are good for you. They're my favourite fruit.\n"
                    "6. Let's have __pasta__ for dinner. I hope you like spaghetti.",
            "gaps_expected": 6}),
        ("text", {"html": "<h3>Это Макс</h3>"
                          "<p>Смотри — это Макс. Он расскажет нам о своём питании. Прочти его рассказ и "
                          "выбери подходящий вариант для каждого пропуска.</p>" + pic("max", "Max")}),
        ("quiz", {"questions": [
            q("Hi! I have ___ at 7 a.m.", ["dinner", "breakfast"], 1),
            q("I love fruit, so I always have ___ at school.", ["an apple", "sausages"], 0),
            q("For lunch I have pasta and ___. This is my favourite fish!", ["chicken", "tuna"], 1),
            q("I have ___ at 7 p.m.", ["dinner", "breakfast"], 0),
            q("Mum often cooks chicken because it's dad's favourite ___.", ["fish", "meat"], 1),
        ]}),
        ("sort", {"title": "Вспомни рассказ Макса. Что Макс ест на завтрак, обед и ужин?",
                  "groups": [
                      {"name": "breakfast", "items": [{"text": "an apple"}]},
                      {"name": "lunch", "items": [{"text": "pasta"}, {"text": "tuna"}]},
                      {"name": "dinner", "items": [{"text": "chicken"}]},
                  ]}),
        ("task", {"title": "Что ты ешь на завтрак, обед и ужин?", "needs_review": True,
                  "html": "<p>Молодец! Ты справился! А это — твоё последнее задание. Письменно перечисли, "
                          "что ты ешь на завтрак, обед и ужин. Можешь использовать рассказ Макса как "
                          "пример.</p><p><i>For example: I have breakfast at 8 a.m. I have cereal and "
                          "milk…</i></p>" + pic("three_meals", "breakfast, lunch, dinner")}),
        bye("well_done_star", "Ура, ты выполнил все задания!",
            "<p>Ты — супер ученик! За это держи звёздочку. До встречи на занятии!</p>"),
    ]},

    # ------------------------------------------------------------------ HW2
    "u2_hw2": {**UNIT, "lesson_title": "Homework 2", "lesson_sort": 1, "kind": "homework", "blocks": [
        hello("hello_book", "Привет! 👋",
              "<p>В этом уроке мы выучим ещё несколько названий продуктов. Выполни все задания, чтобы "
              "выучить слова! У тебя всё получится. Удачи! ❤️</p>"),
        flashcards(FOOD_2),
        match_pics(FOOD_2),
        ("exact_input", {"items": [
            {"image": img(U, f), "prompt": "Посмотри на картинку и напиши слово", "accept": accept(en),
             "audio_tts": en} for en, ru, f in FOOD_2]}),
        hello("hello_wave", "Вторая часть 💪",
              "<p>Добро пожаловать во вторую часть домашнего задания! Сегодня мы с тобой закрепим "
              "знания, полученные на уроке, и ты без проблем сможешь различать исчисляемые и "
              "неисчисляемые существительные. В конце тебя будет ждать дополнительное упражнение — для "
              "самых смелых и самых сильных учеников 💪</p>"),
        ("text", {"html": "<p>И начнём мы с тобой с видео! Анна, Макс и Хэмми решили весело провести время "
                          "вместе. Посмотри на картинку и попробуй угадать, чем же они будут заниматься. "
                          "Посмотри видео и проверь, угадал ли ты. Повторяй вопросы и ответы за ребятами, "
                          "чтобы хорошенько запомнить правила.</p>"
                          f'<p><img src="{img(U, "book_bake_perfect")}" alt="Hammy" '
                          'style="max-width:100%;max-height:320px"></p>'}),
        video("Посмотри видео: что готовят Анна, Макс и Хэмми? 🥞",
              "видео: Анна, Макс и Хэмми пекут блины (Is there any…? / Are there any…?)"),
        ("match", {"title": "Посмотри видео ещё раз и соедини вопросы и ответы", "pairs": [
            {"left": "Are there any eggs?", "right": "Yes, there are.", "right_audio_tts": "Yes, there are."},
            {"left": "Is there any cream?", "right": "There's some milk.",
             "right_audio_tts": "There's some milk."},
            {"left": "Are there any bananas?", "right": "No, there aren't. But there are some strawberries.",
             "right_audio_tts": "No, there aren't. But there are some strawberries."},
            {"left": "Is there any flour?", "right": "Yes, there is.", "right_audio_tts": "Yes, there is."},
        ]}),
        ("sort", {"title": "Рассортируй продукты: исчисляемые (их можно посчитать) — в колонку countable, "
                           "неисчисляемые (их посчитать нельзя) — в колонку uncountable",
                  "groups": [
                      {"name": "countable", "items": [{"text": w} for w in
                                                      ["egg", "apple", "banana", "sausage", "lemon",
                                                       "strawberry"]]},
                      {"name": "uncountable", "items": [{"text": w} for w in
                                                        ["butter", "milk", "water", "sugar", "flour",
                                                         "chocolate"]]},
                  ]}),
        ("text", {"html": "<h3>Блинчики Ани 🥞</h3>"
                          "<p>Молодец! Ты справился с заданием. Посмотри — это Аня. Она обожает готовить и "
                          "есть блинчики. Они у неё оооочень вкусные. Аня поделилась с нами своим рецептом. "
                          "Как думаешь, в чём же её секрет? Прочти рецепт и выбери правильный вариант для "
                          "каждого пропуска.</p>" + pic("anya_pancakes", "Anya") +
                          "<p><i>My pancake recipe has (1) ___, (2) ___, (3) ___ and (4) ___. For the "
                          "topping I like (5) ___ and (6) ___.</i></p>"}),
        ("quiz", {"questions": [
            q("(1) My pancake recipe has ___, …", ["a flour", "flour", "an flour"], 1),
            q("(2) …, ___, …", ["an egg", "egg", "a egg"], 0),
            q("(3) … ___ and …", ["a milk", "an milk", "milk"], 2),
            q("(4) … and ___.", ["butter", "a butter", "an butter"], 0),
            q("(5) For the topping I like ___ and …", ["banana", "an banana", "a banana"], 2),
            q("(6) … and ___.", ["a cream", "cream", "an cream"], 1),
        ]}),
        ("quiz", {"questions": [
            q("А теперь потренируемся составлять вопросы. ___ there ___ sugar?",
              ["Are … any", "Is … any", "Is … some", "a … an"], 1),
            q("___ there ___ apples?", ["Are … any", "Is … any", "Are … some", "Are … a"], 0),
            q("___ there ___ butter?", ["Are … any", "Is … some", "Is … a", "Is … any"], 3),
            q("___ there ___ bananas?", ["Is … any", "Are … some", "Are … any", "Are … a"], 2),
            q("___ there ___ flour?", ["Is … some", "Is … any", "Are … any", "Is … a"], 1),
        ]}),
        ("text", {"html": "<h3>Список покупок 📝</h3>"
                          "<p>Ты справился с большей частью заданий! Посмотри! Том и Мэтт собираются в "
                          "магазин. Но сначала им нужно составить список продуктов. Прочти диалог ниже и "
                          "заполни пропуски. А ты составляешь список продуктов перед походом в магазин?</p>"
                          + pic("tom_matt_list", "Tom and Matt") +
                          "<p><b>Shopping list:</b> 1 litre milk · 6 eggs · butter · flour · chocolate · "
                          "4 bananas</p>"}),
        ("gaps", {"title": "Перетащи слова в пропуски", "mode": "drag",
                  "text": "Tom: What's on the shopping list? Does mum want __any__ chocolate?\n"
                          "Matt: Yes! There are __some__ bananas too.\n"
                          "Tom: And __are__ there any eggs on the list?\n"
                          "Matt: Yes, __there__ are.\n"
                          "Tom: What about __an__ orange?\n"
                          "Matt: No. There __aren't__ any oranges. Look! There __is__ some butter on the "
                          "list. It's a list for pancakes!",
                  "gaps_expected": 7}),
        ("task", {"title": "Дополнительное задание: диалог о списке продуктов", "needs_review": True,
                  "html": "<p>Ура, ты выполнил все основные задания! А это — последнее, дополнительное, для "
                          "самых смелых! Составь и запиши диалог о списке продуктов. Можешь взять диалог из "
                          "предыдущего упражнения в качестве примера. Удачи, ты обязательно справишься!</p>"
                          "<p><i>Shopping list: apples, carrots, chicken, cheese, curry sauce, doughnuts</i></p>"}),
        bye("well_done_clap", "Ура! Ты справился с домашней работой!",
            "<p>Ты молодец! Увидимся на занятии!</p>"),
    ]},

    # ------------------------------------------------------------------ HW3
    # В выгрузке только словарный тренажёр — так и переносим (Анна).
    "u2_hw3": {**UNIT, "lesson_title": "Homework 3", "lesson_sort": 2, "kind": "homework", "blocks": [
        hello("hello_highfive", "Привет! 👋",
              "<p>В этом уроке мы научимся считать неисчисляемые продукты. Как это возможно? Давай "
              "начнём урок и узнаешь!</p><p>Выполни все задания, чтобы выучить слова! У тебя всё "
              "получится. Удачи! ❤️</p>"),
        flashcards(CONTAINERS),
        match_pics(CONTAINERS, "Соедини картинку с выражением"),
        ("gaps", {"title": "Перетащи слова в пропуски", "mode": "drag",
                  "text": "1. a __bar__ of chocolate\n2. a __bottle__ of water\n3. a __can__ of cola\n"
                          "4. a __carton__ of juice\n5. a __jar__ of jam\n6. a __packet__ of biscuits",
                  "gaps_expected": 6}),
        quiz_ru_to_en(CONTAINERS),
        bye("well_done_trophy", "Отлично!",
            "<p>Теперь ты умеешь считать даже то, что посчитать нельзя! Увидимся на занятии!</p>"),
    ]},

    # ------------------------------------------------------------------ HW4
    "u2_hw4": {**UNIT, "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework", "blocks": [
        hello("hello_highfive", "Привет! 👋",
              "<p>Рада снова видеть тебя в домашнем задании! Благодаря сегодняшним упражнениям ты сможешь "
              "смело ходить в кафе или ресторан и заказывать себе еду! 😱 Let's start!</p>"),
        ("task", {"title": "Где лучше поужинать?", "needs_review": True,
                  "html": "<p>Прежде чем приступить к первому заданию, подумай, где лучше поужинать: дома "
                          "или в кафе/ресторане. Что бы ты выбрал?</p><p>Впиши <b>restaurant/cafe</b>, если "
                          "предпочитаешь есть в кафе или ресторане, или впиши <b>home</b>, если считаешь, "
                          "что лучшее место, где можно поесть, — это твой дом.</p>"}),
        todo(("text", {
            "html": "<h3>В кафе ☕</h3>"
                    "<p>Давай вспомним все фразы, которые пригодятся нам в кафе. Смотри, это диалог между "
                    "официантом и гостем. Давай его разыграем. Я буду официантом, а ты — моим почётным "
                    "гостем. Включи запись, и ты услышишь слова официанта. Попробуй дополнить мой "
                    "«монолог» ответами гостя. Я буду делать паузы, но если не будешь успевать — можешь "
                    "поставить аудио на паузу, а затем включить. У нас получится отличный диалог.</p>"
                    + pic("cafe_waiter", "café") +
                    "<p><b>Waitress:</b> What would you like?<br><b>Guest:</b> I'd like a ham sandwich, "
                    "please.<br><b>Waitress:</b> Anything else?<br><b>Guest:</b> Yes. Can I have some "
                    "chips, please?<br><b>Waitress:</b> Would you like anything to drink?<br><b>Guest:</b> "
                    "Can I have a lemonade, please?<br><b>Waitress:</b> Great, thanks.</p>",
            "audio": "",
            "audio_tts": "What would you like? ... Anything else? ... Would you like anything to drink? "
                         "... Great, thanks."}),
             ("audio", "аудио: реплики официанта с паузами для ролевой игры — пусто; стоит audio_tts "
                       "реплик официанта без длинных пауз, при желании заменить записью")),
        ("speaking", {"title": "Твоя очередь 🎤", "needs_review": True,
                      "html": "<p>Молодец! Ещё раз посмотри на диалог выше. Теперь твоя очередь записывать! "
                              "Нажми на микрофон и запиши свои реплики. Твои слова выделены жёлтым.</p>"
                              "<p>Waitress: What would you like?<br>Guest: <mark>I'd like a ham sandwich, "
                              "please.</mark><br>Waitress: Anything else?<br>Guest: <mark>Yes. Can I have "
                              "some chips, please?</mark><br>Waitress: Would you like anything to drink?"
                              "<br>Guest: <mark>Can I have a lemonade, please?</mark><br>Waitress: Great, "
                              "thanks.</p>"}),
        ("sequence", {"title": "Расставь реплики в правильном порядке, чтобы получился наш диалог",
                      "items": [{"text": t} for t in [
                          "What would you like?", "I'd like a ham sandwich, please.", "Anything else?",
                          "Yes. Can I have some chips, please?", "Would you like anything to drink?",
                          "Can I have a lemonade, please?", "Great, thanks."]]}),
        ("task", {"title": "Дополнительное задание: свой диалог в кафе", "needs_review": True,
                  "html": "<p>Ура! Ты справился со всеми обязательными упражнениями. Осталось последнее — "
                          "дополнительное. Твоя задача — составить и записать диалог. Используй диалог из "
                          "предыдущих упражнений как пример.</p>"}),
        bye("well_done_trophy", "Good job!",
            "<p>Отлично, ты справился со всеми заданиями. Ты — большой молодец. Жду тебя на занятии!</p>"),
    ]},

    # ------------------------------------------------------------------ HW5
    "u2_hw5": {**UNIT, "lesson_title": "Homework 5", "lesson_sort": 4, "kind": "homework", "blocks": [
        hello("hello_book", "Привет! 👋",
              "<p>Добро пожаловать в домашнее задание! Сегодня мы с тобой потренируем навык чтения. "
              "Поехали!</p>"),
        ("text", {"html": "<h3>Susie's favourite meals</h3>"
                          "<p>Это Сьюзи. Она из Великобритании, и она подготовила нам интересный рассказ о "
                          "своих любимых блюдах. Как думаешь, о скольких блюдах она нам расскажет? 1? 3? 5? "
                          "Давай прочитаем и узнаем.</p>" + pic("susie", "Susie") +
                          "<p><b>English breakfast</b><br>This is a hot breakfast. My mum cooks it for me at "
                          "the weekend. You can have different things for this breakfast, but I like some "
                          "sausages, two eggs and a tomato.</p>"
                          "<p><b>Fish and chips</b><br>People usually order this meal from a restaurant. But "
                          "my dad makes the best fish and chips in the world! There's always some fish in the "
                          "fridge at my house because he cooks fish and chips for the whole family every "
                          "Friday.</p>"
                          "<p><b>Chicken and rice</b><br>Is there any chicken on the menu at my house? No, "
                          "there isn't. But there is some chicken and some rice at my aunt's house. She "
                          "cooks this meal for me when I visit her. There's always a lot of food so she "
                          "gives me some to take home!</p>"}),
        ("match", {"title": "Внимательно прочитай текст и соедини блюдо с картинкой", "pairs": [
            {"left_image": img(U, "english_breakfast"), "right": "English breakfast",
             "right_audio_tts": "English breakfast"},
            {"left_image": img(U, "fish_and_chips"), "right": "Fish and chips",
             "right_audio_tts": "Fish and chips"},
            {"left_image": img(U, "chicken_rice"), "right": "Chicken and rice",
             "right_audio_tts": "Chicken and rice"},
        ]}),
        ("quiz", {"questions": [
            q("Is Susie from England?", ["Yes, she is.", "No, she isn't."], 0),
            q("Is an English breakfast cold?", ["Yes, it is.", "No, it isn't."], 1),
            q("Does Susie like sausages?", ["Yes, she does.", "No, she doesn't."], 0),
            q("Does Susie order fish and chips from a restaurant?", ["Yes, she does.", "No, she doesn't."], 1),
            q("Does Susie's mum cook fish and chips?", ["No, she doesn't.", "Yes, she does."], 0),
            q("Is there any chicken and rice at her aunt's house?", ["No, there isn't.", "Yes, there is."], 1),
        ]}),
        ("sort", {"title": "Перетащи утверждения к подходящему блюду. Если не помнишь — подсмотри в тексте",
                  "groups": [
                      {"name": "English breakfast", "items": [
                          {"text": "There are some eggs in this meal."},
                          {"text": "Susie's mum cooks it at the weekend."}]},
                      {"name": "Fish and chips", "items": [
                          {"text": "There isn't any meat in this meal."},
                          {"text": "A lot of people order this meal."},
                          {"text": "Susie's dad cooks it every week."}]},
                      {"name": "Chicken and rice", "items": [
                          {"text": "Susie's aunt cooks it for Susie."}]},
                  ]}),
        ("task", {"title": "Ответь на вопросы о себе", "needs_review": True,
                  "html": "<p>Ура, это последнее задание на сегодня! Письменно ответь на вопросы о себе:</p>"
                          "<ol><li>What's your favourite meal?</li><li>Who cooks it?</li>"
                          "<li>How often do you go to restaurants?</li>"
                          "<li>What do you usually have for breakfast?</li></ol>"}),
        bye("well_done_star", "Ура, ты справился с домашним заданием!",
            "<p>Ты — большой молодец и супер ученик! Увидимся на занятии. Bye!</p>"),
    ]},

    # ------------------------------------------------------------------ HW6
    "u2_hw6": {**UNIT, "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework", "blocks": [
        hello("hello_headphones", "Привет! 👋",
              "<p>Добро пожаловать в домашнее задание! Сегодня мы прослушаем интересную аудиозапись и "
              "напишем электронное письмо (e-mail). Поехали!</p>"),
        todo(("text", {"html": "<h3>А начнём мы с аудио 🎧</h3>"
                               "<p>Это Пенни. Прослушай её диалог с папой и выполни задания под аудио.</p>"
                               + pic("penny_breakfast", "Penny and her dad"),
                       "audio": ""}),
             ("audio", "аудио: диалог Пенни с папой о завтраке — пусто (без него задания про Пенни решаются "
                       "только по памяти)")),
        ("quiz", {"questions": [{
            "q": "Прослушай аудио и выбери, что Пенни будет на завтрак. Верных ответов несколько.",
            "type": "multiple",
            "options": [{"text": t} for t in ["an egg", "some bread and ham", "some orange juice",
                                              "a glass of milk", "some sugar", "some cereal"]],
            "correct": [0, 1, 3]}]}),
        ("quiz", {"questions": [
            q("Прослушай аудио ещё раз. Penny has P.E. ___.", ["after lunch", "in the morning"], 1),
            q("She ___ for breakfast.", ["doesn't want any cereal", "wants some cereal"], 0),
            q("She wants a ___ sandwich.", ["cheese", "ham"], 1),
            q("She can have a glass of ___.", ["juice", "water", "milk"], 2),
            q("She would like to have ___.", ["an egg", "two eggs"], 0),
        ]}),
        ("sequence", {"title": "Вспомни диалог и расставь реплики в правильном порядке (не подглядывая)",
                      "items": [{"text": t} for t in [
                          "Good morning, Penny.", "What would you like for breakfast?",
                          "How about some cereal?", "I don't want any cereal.", "How about a sandwich?",
                          "Yes, please.", "Would you like anything to drink?",
                          "Is there any orange juice in the fridge?", "Ok. Milk is fine.",
                          "Can I have an egg too, please, dad?", "Yes, I can make one for you."]]}),
        ("text", {"html": "<h3>Письмо Стива ✉️</h3>"
                          "<p>Отлично! Ты справился с первой частью заданий. Я обещала тебе, что мы напишем "
                          "электронное письмо сегодня. Для начала прочти письмо Стива и выбери слово для "
                          "каждого пропуска: <b>because</b> или <b>so</b>.</p>"
                          "<p><b>From:</b> Steve<br><b>Subject:</b> What would you like to eat?</p>"
                          "<p>Hi! I'm very happy (1) ___ you are coming to stay at my house this weekend. "
                          "Mum wants to do the shopping (2) ___ she wants to know what food you like. For "
                          "breakfast I usually have milk and cereal (3) ___ it is quick and easy. I also "
                          "drink apple juice (4) ___ it is my favourite. What would you like? We can go to "
                          "the beach on Saturday (5) ___ let's take a picnic lunch. What would you like for "
                          "lunch? I love chicken and chips. Can we have that for dinner? Do you like chicken "
                          "and chips too?</p><p>Bye for now!<br>Steve</p>"}),
        ("quiz", {"questions": [
            q("(1) I'm very happy ___ you are coming to stay at my house this weekend.", ["so", "because"], 1),
            q("(2) Mum wants to do the shopping ___ she wants to know what food you like.",
              ["so", "because"], 0),
            q("(3) For breakfast I usually have milk and cereal ___ it is quick and easy.",
              ["because", "so"], 0),
            q("(4) I also drink apple juice ___ it is my favourite.", ["so", "because"], 1),
            q("(5) We can go to the beach on Saturday ___ let's take a picnic lunch.", ["because", "so"], 1),
        ]}),
        ("task", {"title": "Ответь на письмо Стива", "needs_review": True,
                  "html": "<p>Ура! Ты справился почти со всеми заданиями. Это — последнее! Письменно ответь "
                          "на письмо Стива: расскажи ему, что ты любишь на завтрак, обед и ужин. С началом "
                          "письма я тебе помогу:</p>"
                          "<p><i>From: Your name<br>Subject: My favourite food.<br>Hi, Steve!<br>"
                          "I'm very happy, too.<br>For breakfast …</i></p>"}),
        bye("well_done_star", "Молодец!",
            "<p>Ты сделал всё-всё домашнее задание. Увидимся на занятии ⭐</p>"),
    ]},

    # ------------------------------------------------------------------ HW7
    "u2_hw7": {**UNIT, "lesson_title": "Homework 7", "lesson_sort": 6, "kind": "homework", "blocks": [
        hello("hello_wave", "Привет! 👋",
              "<p>Рада, что ты заглянул в домашку! Сегодня мы с тобой выполним несколько полезных "
              "упражнений, которые помогут тебе закрепить полученные знания. В конце урока тебя также "
              "ждёт дополнительное задание — его можно выполнить по желанию. Но ты станешь МЕГА крутым "
              "учеником, когда справишься с ним. 😎 Let's go!</p>"),
        match_pics([w for w in FOOD_1 + FOOD_2 if w[0] in
                    ("biscuits", "butter", "pancakes", "yoghurt", "ham", "cereal", "flour", "milk",
                     "strawberry")],
                   "Давай сначала вспомним продукты. Соедини картинку с названием"),
        ("match", {"title": "Как посчитать неисчисляемое? С помощью ёмкостей! Соедини две части, чтобы "
                            "получилась фраза", "pairs": [
            {"left": a, "right": b, "right_audio_tts": f"{a} {b}"} for a, b in [
                ("a bar", "of chocolate"), ("a jar", "of jam"), ("a can", "of cola"),
                ("a bottle", "of water"), ("a carton", "of juice"), ("a packet", "of biscuits")]]}),
        todo(("gaps", {"title": "A / an / some / any: перетащи слова в пропуски", "mode": "drag",
                       "text": "1. There is __an__ orange on the table.\n"
                               "2. I've got __a__ sandwich for lunch.\n"
                               "3. There are __some__ eggs in the fridge.\n"
                               "4. We haven't got __any__ bread.\n"
                               "5. Mum wants __some__ milk for the pancakes.\n"
                               "6. There isn't __any__ cheese in the fridge.\n"
                               "7. Can I have __an__ apple, please?\n"
                               "8. There's __a__ lemon in the bag.",
                       "gaps_expected": 8}),
             ("game", "СОСТАВ МОЙ: пересобрана игра Wordwall «Complete the sentence: A/an-some-any» "
                      "(https://wordwall.net/resource/762927/a-an-some-any) — 8 предложений на a/an/some/any")),
        ("gaps", {"title": "Прочти диалог между Кейт и продавцом и перетащи подходящие слова в пропуски",
                  "mode": "drag", "image": img(U, "hot_dog_cart"),
                  "text": "Waiter: What __would__ you like?\n"
                          "Kate: __I'd like__ a hot dog, please.\n"
                          "Waiter: Would you __like__ anything to drink?\n"
                          "Kate: Can I have a __lemonade__, please?\n"
                          "Waiter: __Anything__ else?\n"
                          "Kate: __Yes__. Can I have a small __salad__, please?\n"
                          "Waiter: Great, __thanks__.",
                  "gaps_expected": 8}),
        ("gaps", {"title": "Прочитай диалоги и впиши в пропуски How much или How many", "mode": "type",
                  "text": "1. A: __How much|how much__ milk is there in the fridge? B: There isn't any milk!\n"
                          "2. A: __How much|how much__ chocolate do you put in the cake? B: Just one bar.\n"
                          "3. A: I'd like a salad, please. B: __How many|how many__ tomatoes would you like "
                          "in your salad?\n"
                          "4. A: Matt usually eats a lot of chips. B: __How many|how many__ potatoes do we "
                          "need then?\n"
                          "5. A: Can you buy some cream, please? B: Yes. __How much|how much__ cream do you "
                          "want?\n"
                          "6. A: __How much|how much__ water do you drink every day? B: I don't know!",
                  "gaps_expected": 6}),
        ("gaps", {"title": "Я обожаю тосты на завтрак. Прочитай рецепт моих любимых тостов и заполни пропуски",
                  "mode": "drag", "image": img(U, "toast"),
                  "text": "What's toast? It's hot __bread__. You need a __toaster__ to cook the bread. "
                          "I like French toast. What's French toast? Well, you dip your bread in an __egg__. "
                          "Then you cook it in __butter__ in a frying pan. Then put some __sugar__ on it and "
                          "it's ready.",
                  "gaps_expected": 5}),
        ("task", {"title": "Дополнительное задание: рецепт любимого завтрака", "needs_review": True,
                  "html": "<p>А это последнее задание, оно дополнительное, для самых смелых учеников. "
                          "Напиши рецепт своего любимого завтрака. Можешь использовать рецепт тостов из "
                          "предыдущего задания как пример.</p>"}),
        bye("well_done_star", "Ты справился с домашним заданием!",
            "<p>Ты — супер ученик! За это держи звёздочку. До встречи на занятии!</p>"),
    ]},

    # ------------------------------------------------------------------ Test
    "u2_test": {**UNIT, "lesson_title": "Unit 2 Test", "lesson_sort": 7, "kind": "test", "blocks": [
        ("exact_input", {"items": [
            {"prompt": f"Напиши по-английски: {ru}", "accept": accept(en), "audio_tts": en}
            for en, ru in [("biscuits", "печенье"), ("cereal", "хлопья"), ("ham", "ветчина"),
                           ("sausage", "сосиска"), ("water", "вода"), ("yoghurt", "йогурт")]]}),
        ("quiz", {"questions": [
            q("Выбери правильный вариант. There ___ apples on the table.",
              ["is some", "are some", "are any"], 1),
            q("We haven't got ___ bread for breakfast.", ["some", "a", "any"], 2),
            q("How ___ milk do you drink every day?", ["much", "many", "a lot"], 0),
            q("I'd like ___ egg and a sandwich, please.", ["a", "an", "some"], 1),
            q("How ___ sausages are there in the packet?", ["much", "many"], 1),
        ]}),
        ("gaps", {"title": "Вставь нужное слово", "mode": "drag",
                  "text": "1. There are __some__ tomatoes in the salad.\n"
                          "2. There isn't __any__ sugar in my tea, thanks.\n"
                          "3. Can I have __an__ apple, please?\n"
                          "4. How __much__ chocolate do you eat in a week?\n"
                          "5. How __many__ eggs do we need for the pancakes?",
                  "gaps_expected": 5}),
        ("text", {"html": "<h3>Расставь части предложения в правильном порядке</h3>"
                          "<p>Ниже пять предложений — собери каждое.</p>"}),
        ("order", {"words": ["There", "are", "some", "sausages", "in", "the fridge."],
                   "sentence": "There are some sausages in the fridge.",
                   "audio_tts": "There are some sausages in the fridge."}),
        ("order", {"words": ["How", "much", "cheese", "do", "you", "want?"],
                   "sentence": "How much cheese do you want?", "audio_tts": "How much cheese do you want?"}),
        ("order", {"words": ["We", "haven't", "got", "any", "orange juice", "today."],
                   "sentence": "We haven't got any orange juice today.",
                   "audio_tts": "We haven't got any orange juice today."}),
        ("order", {"words": ["I'd", "like", "a", "bottle", "of", "water,", "please."],
                   "sentence": "I'd like a bottle of water, please.",
                   "audio_tts": "I'd like a bottle of water, please."}),
        ("order", {"words": ["How", "many", "strawberries", "are", "there", "in", "the", "jar?"],
                   "sentence": "How many strawberries are there in the jar?",
                   "audio_tts": "How many strawberries are there in the jar?"}),
        ("text", {"html": "<h3>READING</h3>"
                          "<p>Прочитай тексты трёх подростков об их завтраке.</p>"
                          "<p><b>Three Breakfasts Around the World</b></p>"
                          "<p><b>Carlos, 13, from Spain:</b> \"In Spain we don't usually have a big "
                          "breakfast. I just have toast with butter and a glass of orange juice. On Sundays "
                          "my dad makes hot chocolate – it's amazing!\"</p>"
                          "<p><b>Yuki, 12, from Japan:</b> \"My breakfast is very different from breakfasts "
                          "in Europe. I usually have rice, fish and a green vegetable called natto. I drink "
                          "green tea, not orange juice.\"</p>"
                          "<p><b>Olivia, 13, from the UK:</b> \"On weekdays I have cereal with milk because "
                          "we don't have much time in the morning. But on Saturdays my mum makes a big "
                          "English breakfast with eggs, sausages, tomatoes and beans. It's my favourite meal "
                          "of the week!\"</p>"}),
        ("sort", {"title": "Соедини каждого человека с фактами о нём. Каждый факт подходит только к одному "
                           "человеку",
                  "groups": [
                      {"name": "Carlos", "items": [{"text": "drinks hot chocolate on Sundays"},
                                                   {"text": "has toast with butter"}]},
                      {"name": "Yuki", "items": [{"text": "eats fish for breakfast"},
                                                 {"text": "doesn't drink orange juice"},
                                                 {"text": "drinks green tea"}]},
                      {"name": "Olivia", "items": [{"text": "has cereal on weekdays"},
                                                   {"text": "is often in a hurry in the morning"}]},
                  ]}),
        todo(("text", {"html": "<h3>LISTENING 🎧</h3>"
                               "<p>Послушай рассказ Мии о покупках в супермаркете. Затем отметь, какие "
                               "предложения верные (True), а какие — неверные (False).</p>",
                       "audio": ""}),
             ("audio", "аудио LISTENING: рассказ Мии о покупках в супермаркете — пусто; без него "
                       "следующий блок (верно/неверно) нерешаем")),
        ("truefalse", {"title": "True or False?", "statements": [
            {"text": "Mia is shopping with her dad.", "correct": False},
            {"text": "Her brother eats bread every morning.", "correct": True},
            {"text": "They need eggs for pancakes.", "correct": True},
            {"text": "Mia's dad wants to cook pasta with vegetables.", "correct": False},
            {"text": "They need orange juice for Sunday breakfast.", "correct": True},
        ]}),
        ("speaking", {"title": "SPEAKING I 🎤", "needs_review": True,
                      "image": img(U, "scene_breakfast"),
                      "html": "<p>Опиши картинку и ответь на вопросы.</p><ol>"
                              "<li>How many people are there in the picture?</li><li>Where are they?</li>"
                              "<li>What time of day is it — breakfast, lunch or dinner?</li>"
                              "<li>What food can you see on the table?</li><li>What drinks are there?</li>"
                              "<li>Is there any cheese?</li></ol>"}),
        ("speaking", {"title": "SPEAKING II 🎤", "needs_review": True,
                      "html": "<p>Ответь на вопросы полными предложениями.</p><ol>"
                              "<li>What do you usually have for breakfast?</li><li>What's your favourite food?</li>"
                              "<li>What food don't you like?</li>"
                              "<li>How much water do you drink every day?</li>"
                              "<li>How many eggs do you eat in a week?</li>"
                              "<li>Can you cook? What can you make?</li></ol>"}),
    ]},
}
