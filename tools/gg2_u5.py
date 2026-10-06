"""Go Getter 2 · Unit 5 · My town — шесть домашек и тест.

Источник — docs/GG2_разбор_u5.md. Номера блоков в комментариях — как в выгрузке.
Кадры учебника — media/gg2/u5/book_*.webp, карточки — листы 36–42.
Апострофы в английском — прямые ('), в пропусках принимаются оба (' и ’):
сервер сравнивает ответы без учёта регистра, но апострофы не сводит.
"""
from gg2_build import img, shared, todo, video

U = "u5"
UNIT = {"unit": U, "unit_title": "Unit 5 · My town", "unit_sort": 5}


def hello(pic, title, *paras):
    return ("text", {"html": f'<p><img src="{shared(pic)}" alt="" style="height:200px"></p>'
                             f"<h2>{title}</h2>" + "".join(f"<p>{p}</p>" for p in paras)})


def bye(pic, title, *paras):
    return ("text", {"html": f'<p><img src="{shared(pic)}" alt="" style="height:180px"></p>'
                             f"<h3>{title}</h3>" + "".join(f"<p>{p}</p>" for p in paras)})


def book(name, alt=""):
    return f'<p><img src="{img(U, "book_" + name)}" alt="{alt}" style="max-width:100%"></p>'


def alt(ans):
    """Пропуск с обоими апострофами: wasn't → wasn't|wasn’t."""
    if "'" in ans:
        return f"{ans}|{ans.replace(chr(39), '’')}"
    return ans


def sentence_alts(s):
    """Короткий ответ целиком: с запятой и без, с точкой и без, оба апострофа."""
    base = s.rstrip(".")
    forms = []
    for b in (base, base.replace(",", "")):
        for f in (b, b + "."):
            for g in (f, f.replace("'", "’")):
                if g not in forms:
                    forms.append(g)
    return "|".join(forms)


def q(text, options, right):
    """Вопрос квиза: варианты в заданном порядке, right — верный вариант (строкой)."""
    return {"q": text, "type": "single", "options": [{"text": o} for o in options],
            "correct": [options.index(right)]}


# ---------- словарь юнита ----------

PLACES = [  # (слово, перевод, картинка)
    ("bank", "банк", "bank"),
    ("café", "кафе", "cafe"),
    ("cinema", "кинотеатр", "cinema"),
    ("hotel", "отель", "hotel"),
    ("hospital", "больница", "hospital"),
    ("library", "библиотека", "library"),
    ("park", "парк", "park"),
    ("museum", "музей", "museum"),
    ("restaurant", "ресторан", "restaurant"),
    ("supermarket", "супермаркет", "supermarket"),
    ("shop", "магазин", "clothes_shop"),
    ("stadium", "стадион", "stadium"),
    ("theatre", "театр", "theatre"),
]


def tts(word):
    return "cafe" if word == "café" else word


def quiz_ru_to_en(words):
    """«Как по-английски …?» — по три варианта, верный на разных местах."""
    en = [w for w, _, _ in words]
    qs = []
    for i, (w, ru, _) in enumerate(words):
        others = [en[(i + 3) % len(en)], en[(i + 7) % len(en)]]
        pos = i % 3
        opts = others[:pos] + [w] + others[pos:]
        qs.append(q(f"Как по-английски «{ru}»?", opts, w))
    return {"title": "Выбери правильное слово", "questions": qs}


# ---------- Homework 1 ----------

HW1 = [
    # (1) словарный тренажёр
    hello("hello_wave", "Привет! 👋",
          "Сегодня тебя ждёт изучение новых слов. Ты повторишь названия разных мест, "
          "куда можно пойти в городе. Давай начинать 😉",
          "Не забудь: после слов тебя ждёт ещё одна часть домашнего задания — с упражнениями!"),
    ("flashcards", {"cards": [
        {"text": w, "translation": ru, "audio_tts": tts(w), "image": img(U, f)} for w, ru, f in PLACES]}),
    ("match", {"title": "Соедини картинку со словом", "pairs": [
        {"left_image": img(U, f), "right": w, "right_audio_tts": tts(w)} for w, ru, f in PLACES[:7]]}),
    ("match", {"title": "И ещё шесть мест — соедини картинку со словом", "pairs": [
        {"left_image": img(U, f), "right": w, "right_audio_tts": tts(w)} for w, ru, f in PLACES[7:]]}),
    ("quiz", quiz_ru_to_en(PLACES)),

    # (2) задания
    hello("hello_highfive", "Привет-привет, самый старательный ученик!",
          "В этой части домашнего задания мы закрепим всё, что выучили. Для этого нужно "
          "сделать несколько упражнений. Время пролетит незаметно. Вперёд 😄"),
    # 2 Диаграмма — точки на номерах домиков 1–6
    ("hotspot", {
        "title": "Внимательно посмотри на картинку и соедини названия мест с правильными домиками. Удачи!",
        "mode": "label",
        "image": img(U, "book_street"),
        "points": [
            {"x": 4.7, "y": 18.7, "text": "restaurant", "audio_tts": "restaurant"},
            {"x": 26.1, "y": 18.7, "text": "cinema", "audio_tts": "cinema"},
            {"x": 42.0, "y": 18.7, "text": "supermarket", "audio_tts": "supermarket"},
            {"x": 57.8, "y": 18.7, "text": "hotel", "audio_tts": "hotel"},
            {"x": 73.3, "y": 18.7, "text": "café", "audio_tts": "cafe"},
            {"x": 87.8, "y": 18.7, "text": "hospital", "audio_tts": "hospital"},
        ],
        "extras": [],
    }),
    # 3 Выбери правильный вариант
    ("quiz", {"title": "Ты великолепно справился! Прочитай предложения и выбери правильный вариант по смыслу",
              "questions": [
        q("I want to get some eggs and flour from the ___.", ["café", "supermarket"], "supermarket"),
        q("Let's go to the ___ to get some money.", ["bank", "cinema"], "bank"),
        q("This is a nice ___. I love the clothes they sell.", ["library", "shop"], "shop"),
        q("Who wants to see an Egyptian mummy at the ___?", ["museum", "hotel"], "museum"),
        q("There's a football match on Saturday at the ___.", ["theatre", "stadium"], "stadium"),
        q("Can we have a picnic in the ___, please, Mum?", ["park", "hospital"], "park"),
    ]}),
    # 4 Диаграмма → match кадр ↔ предлог
    ("match", {"title": "Супер! А теперь вспомним предлоги места. Где собачка? Соедини картинку с предлогом",
               "pairs": [
        {"left_image": img(U, "book_dog_1"), "right": "between", "right_audio_tts": "between"},
        {"left_image": img(U, "book_dog_2"), "right": "next to", "right_audio_tts": "next to"},
        {"left_image": img(U, "book_dog_3"), "right": "opposite", "right_audio_tts": "opposite"},
        {"left_image": img(U, "book_dog_4"), "right": "in front of", "right_audio_tts": "in front of"},
        {"left_image": img(U, "book_dog_5"), "right": "behind", "right_audio_tts": "behind"},
    ]}),
    # 5 Заполни пропуски по карте
    ("gaps", {
        "title": "Ты просто супер! Внимательно посмотри на карту и заполни пропуски подходящими словами",
        "mode": "drag",
        "image": img(U, "book_map_north_south"),
        "text": "A: Where's the café? I'd like a cup of coffee.\n"
                "B: It's __next to__ my favourite clothes shop in North Street. But I haven't got any money, "
                "so let's go to the bank first. It's __between__ the library and the Italian restaurant.\n"
                "A: I know, it's near the hotel in South Street. There is a lovely garden __in front of__ "
                "the hotel and there is a park __behind__ it.\n"
                "B: Yes. The supermarket is __opposite__ the café, so we can get some food for a picnic ...\n"
                "A: ... and have lunch in the park. Good idea!",
        "gaps_expected": 5,
    }),
    # 6 дополнительное
    ("task", {
        "title": "Дополнительное задание — для самых крутых учеников! ⭐",
        "needs_review": True,
        "html": "<p>Посмотри внимательно на карту и опиши её. Напиши 2–3 предложения.</p>"
                "<p><i>Например: The swimming pool is behind the restaurant.</i></p>"
                + book("town_map", "Карта города"),
    }),
    bye("well_done_star", "Bye-bye! 👋", "Ты отлично поработал. До встречи на уроке!"),
]


# ---------- Homework 2 ----------

HW2 = [
    hello("hello_wave", "Добро пожаловать в домашнее задание!",
          "Сегодня мы закрепим знания, полученные на уроке. В конце тебя будет ждать дополнительное "
          "упражнение — для самых смелых и самых сильных учеников 💪"),
    # (1)·1
    video("Посмотри видео с урока и выполни задания ниже",
          "видео с урока: Лукас опоздал в кино, его ждут Elena, Tom и Amy"),
    # (1)·2
    ("gaps", {
        "title": "Заполни пропуски в диалоге",
        "mode": "drag",
        "text": "Elena: Where's Lucas? The film starts in five __minutes__.\n"
                "Tom: He was OK this __morning__.\n"
                "Lucas: Sorry I'm __late__. There weren't any buses.\n"
                "Amy: Never __mind__, Lucas. Let's go for a pizza now.",
        "gaps_expected": 4,
    }),
    # (1)·3
    todo(("truefalse", {"title": "Отметь, верны ли эти утверждения", "statements": [
        {"text": "Lucas was at school yesterday.", "correct": True},
        {"text": "Lucas came on time to the cinema.", "correct": False},
        {"text": "Lucas had a new bike.", "correct": False},
        {"text": "Lucas's phone was out of battery.", "correct": True},
        {"text": "They didn't go to the pizzeria.", "correct": True},
    ]}), ("check", "ключ утверждения 5 «They didn't go to the pizzeria» = Верно (как в выгрузке), "
                   "но в диалоге Amy: «Let's go for a pizza now» — сверить с видео")),
    # (1)·4
    ("task", {
        "title": "Ответь на вопросы",
        "needs_review": True,
        "html": "<ol><li>Why were Lucas's friends worried?</li><li>Why was Lucas late?</li>"
                "<li>Where did they want to go after the cinema?</li></ol>",
    }),
    # (2)·2
    ("text", {"html": "<h3>Вторая часть: видео про школьную поездку</h3>"
                      "<p>Макс и Хэмми рассказывают Анне о школьной поездке... Посмотри на картинку "
                      "и попробуй угадать, чем они занимались.</p>"
                      + book("hammy_boat", "Хэмми в лодке")}),
    # (2)·3
    video("Посмотри видео и проверь, угадал ли ты. Повторяй реплики за ребятами, чтобы хорошенько "
          "запомнить правила",
          "видео Max & Hammy: школьная поездка, парусные лодки (It was really hot! / I was completely wet!)"),
    # (2)·4
    ("sort", {"title": "Посмотри видео ещё раз и распредели реплики: кто какие фразы сказал?",
              "groups": [
        {"name": "Max", "items": [{"text": "It was really hot!"}, {"text": "The sailing boats were fun!"}]},
        {"name": "Hammy", "items": [{"text": "The sailing boats weren't fun."}, {"text": "And it wasn't hot."},
                                    {"text": "It was cold!"}, {"text": "I was completely wet!"}]},
    ]}),
    # (2)·5
    ("quiz", {"title": "Потренируем грамматику: выбери правильный вариант", "questions": [
        q("I ___ at the shops.", ["was", "were"], "was"),
        q("Mum and Dad ___ at work.", ["was", "were"], "were"),
        q("We ___ at school.", ["were", "was"], "were"),
        q("Sam ___ at home.", ["weren't", "wasn't"], "wasn't"),
        q("My grandparents ___ at the theatre.", ["weren't", "wasn't"], "weren't"),
        q("Anna ___ at school yesterday.", ["were", "was"], "was"),
        q("There ___ some people at the bank.", ["was", "were"], "were"),
        q("These shoes ___ expensive.", ["wasn't", "weren't"], "weren't"),
    ]}),
    # (2)·6
    ("gaps", {
        "title": "Задание посложнее: впиши was, wasn't, were или weren't",
        "mode": "type",
        "text": "Lucas: Tell me about the film. I was late. I __" + alt("wasn't") + "__ there, remember?\n"
                "Tom: I remember! Amy and Elena __were__ worried about you.\n"
                "Lucas: I know. Sorry!\n"
                "Tom: Well, it __was__ a really good film. I'm sad you __" + alt("weren't") + "__ there. "
                "The popcorn __was__ great, too.\n"
                "Lucas: Oh no! I love popcorn.",
        "gaps_expected": 5,
    }),
    # (2)·7 — табличка LOOK! текстом
    ("text", {"html": "<h3>Как говорить о времени в прошлом</h3>"
                      "<p>Посмотри на табличку — она поможет тебе в следующем задании.</p>"
                      "<p><b>LOOK!</b><br>yesterday<br><b>last</b> night / week / month / year<br>"
                      "<b>last</b> Monday / May<br><b>in</b> 2014</p>"}),
    ("gaps", {
        "title": "Today is the 8th of February and it's Tuesday. Расставь слова к их эквивалентам",
        "mode": "drag",
        "text": "1. 7 February = __yesterday__\n"
                "2. 7 February at 8 p.m. = __last night__\n"
                "3. 8 January = __last month__\n"
                "4. 8 December = __last year__\n"
                "5. 5 February = __last Saturday__",
        "gaps_expected": 5,
    }),
    # (2)·8
    ("task", {
        "title": "Дополнительное задание — для самых смелых! ⭐",
        "needs_review": True,
        "html": "<p>Ура, ты выполнил все основные задания! Составь и запиши несколько предложений о том, "
                "где ты был или не был на прошлой неделе.</p>"
                "<p><i>Например: I was at the cinema last Monday. I wasn't at school last Sunday.</i></p>"
                "<p>Удачи, ты обязательно справишься!</p>",
    }),
    bye("well_done_clap", "Bye! 👋", "Ты отлично справился. До встречи на уроке!"),
]


# ---------- Homework 3 ----------

HW3 = [
    hello("hello_book", "Огромный привет!",
          "В этой домашней работе мы повторим всё, что ты прошёл на уроке с учителем. Это поможет "
          "тебе не только всё запомнить, но и использовать :) Давай начинать 😉"),
    # 2 + 3
    video("Давай начнём с видео. Посмотри его, а потом сделай задание ниже",
          "видео с вопросами Were you in the garden / park / kitchen?"),
    # 4
    todo(("match", {"title": "Посмотри видео ещё раз и соедини вопросы с ответами, как в видео",
                    "pairs": [
        {"left": "Were you in the garden?", "left_image": img(U, "garden"),
         "right": "No, I wasn't. I was with my friends.", "right_audio_tts": "No, I wasn't. I was with my friends."},
        {"left": "Were you in the park?", "left_image": img(U, "park_small"),
         "right": "No, we weren't.", "right_audio_tts": "No, we weren't."},
        {"left": "Were you in the kitchen?", "left_image": img(U, "kitchen"),
         "right": "Yes, we were!", "right_audio_tts": "Yes, we were!"},
    ]}), ("check", "по грамматике пары park и kitchen взаимозаменяемы (оба ответа на «we») — "
                   "ключ держится только на видео, сверить")),
    # 5
    ("quiz", {"title": "Время серьёзной практики! Прочитай и выбери правильный ответ", "questions": [
        q("A: Were you at the bank?<br>B: Yes, I ___.", ["was", "wasn't"], "was"),
        q("A: Was Andy sad?<br>B: No, he ___.", ["were", "wasn't"], "wasn't"),
        q("A: Was it cold yesterday?<br>B: No, it ___.", ["wasn't", "weren't"], "wasn't"),
        q("A: Were your friends at your house?<br>B: Yes, ___.", ["we were", "they were"], "they were"),
        q("A: Was Anna there?<br>B: Yes, ___.", ["she was", "he was"], "she was"),
        q("A: Were you late to work?<br>B: No, we ___.", ["wasn't", "weren't"], "weren't"),
    ]}),
    # 6
    ("gaps", {
        "title": "Впиши в вопросы was или were, а потом дополни ответы: ✓ — ответ «да», ✗ — ответ «нет». "
                 "Первый пункт — пример",
        "mode": "type",
        "text": "1. Were you at home last night? ✓ Yes, I was.\n"
                "2. __Was__ Oliver happy yesterday? ✗ __No__, __" + alt("he wasn't") + "__.\n"
                "3. __Were__ you and Ted at the cinema together? ✓ __Yes__, __we were__.\n"
                "4. __Were__ all your friends at your party? ✗ __No__, __" + alt("they weren't") + "__.\n"
                "5. __Was__ I the fastest in the race? ✓ __Yes__, __you were__.\n"
                "6. __Was__ Katy at school last Friday? ✓ __Yes__, __she was__.",
        "gaps_expected": 15,
    }),
    # 7
    ("task", {
        "title": "Составь вопросы и ответы по примеру",
        "needs_review": True,
        "html": "<p>Ты уже на финишной прямой! Посмотри на пункт 1 — это пример: мы задали вопрос и дали "
                "ответ (отрицательный, потому что стоит крестик). Напиши так же вопросы и ответы к пунктам 2–5.</p>"
                "<ol><li>Carla / angry yesterday ✗ — <i>Was Carla angry yesterday? No, she wasn't.</i></li>"
                "<li>the muffins / in the fridge / yesterday ✓</li>"
                "<li>the muffins / good yesterday ✓</li>"
                "<li>the muffins / next to the eggs yesterday ✗</li>"
                "<li>the muffins / next to the pizzas ✓</li></ol>",
    }),
    # 8
    ("task", {
        "title": "Дополнительное задание — для чемпионов! ⭐",
        "needs_review": True,
        "html": "<p>За него ты получишь дополнительный балл! ;) Напиши 2 предложения о том, где ты был, "
                "и 2 предложения о том, где ты не был на выходных.</p>"
                "<p><i>Например: I was at the cinema on Saturday. I wasn't at the supermarket.</i></p>",
    }),
    bye("well_done_smiley", "Bye! 👋", "Отличная работа! До встречи на уроке!"),
]


# ---------- Homework 4 ----------

HW4 = [
    hello("hello_rocket", "Привет!",
          "Здесь тебя ждёт новая домашняя работа. Сегодня мы будем вспоминать, как правильно указывать "
          "дорогу, разговаривать и делать разные упражнения. У тебя всё получится, как и всегда 😃 "
          "Давай приступим :)"),
    # 2 + 3 — карточка Directions текстом
    ("text", {"html": "<h3>Communication: Directions</h3>"
                      "<p>Узнаёшь табличку? Внимательно изучи её, а затем выполни упражнения.</p>"
                      "<p><b>Asking for directions</b><br>Excuse me. Where's <i>North Street</i>?<br>"
                      "I'm looking for <i>a library</i>.<br>How can I get to <i>the Science Museum</i>?<br>"
                      "Is it far?</p>"
                      "<p><b>Giving directions</b><br>It's in/on <i>Green Street</i>.<br>Go straight on.<br>"
                      "Go past <i>the cinema</i>.<br>Turn left. / Turn right.<br>"
                      "It's on the left. / It's on the right.</p>"}),
    # 4
    ("text", {"html": "<h3>Excuse me. Where's the hospital?</h3>"
                      "<p>Внимательно посмотри на карту: красная стрелка — это начало пути. "
                      "В следующем задании заполни пропуски, удачи! ;)</p>"
                      + book("map_hospital", "Карта: путь к больнице")}),
    ("gaps", {
        "title": "Заполни пропуски по карте",
        "mode": "drag",
        "text": "1. __Go__ straight on.\n"
                "2. Then __turn__ right.\n"
                "3. Go __past__ the bank.\n"
                "4. Turn __left__.\n"
                "5. Go __straight__ on and then turn right.\n"
                "6. The hospital is __on__ the right.\n"
                "7. It's __opposite__ the museum.",
        "gaps_expected": 7,
    }),
    # 5
    ("gaps", {
        "title": "Задание посложнее — но в табличку можно подглядывать ;) Прочитай диалог и впиши "
                 "недостающие слова",
        "mode": "type",
        "text": "A: __Excuse__ me. I'm __looking__ for the History Museum. Is it __far__?\n"
                "B: No, it's not far. It's __in|on__ Brown Street. Go __past__ the bank. "
                "Then __turn__ right — that's Brown Street.\n"
                "A: OK.\n"
                "B: Go __straight__ __on__. The museum is __on__ the left, opposite the park.\n"
                "A: Thank you.",
        "gaps_expected": 9,
    }),
    # 6
    ("text", {"html": "<h3>Карта: River Street и Smith Street</h3>"
                      "<p>Посмотри на карту. Красная точка — это ты. В следующем задании заполни пропуски "
                      "в диалогах, вписывай слова внимательно!</p>"
                      + book("map_river", "Карта River Street и Smith Street")}),
    ("gaps", {
        "title": "Впиши слова в диалоги по карте (красная точка — это ты)",
        "mode": "type",
        "text": "1. A: Excuse me. Where's the cinema?\n"
                "B: It's in __River__ Street. __Go__ past the supermarket. Turn __right__ at the __café|cafe__. "
                "Then go straight on. The cinema is on the __right__, opposite the __restaurant__.\n\n"
                "2. A: Excuse me. How can I get to the park?\n"
                "B: It's not far. Go __straight__ on. Go past the __supermarket__, café and the __bank__. "
                "They are all on the right. The park is next to the bank, __on__ the right.\n\n"
                "3. A: Excuse me. I'm looking for the shoe shop.\n"
                "B: It's in River Street. Go __straight__ __on__. Then __turn__ __left__. "
                "The shoe shop is on the left.",
        "gaps_expected": 14,
    }),
    # 7
    ("task", {
        "title": "Дополнительное задание — для самых стойких и терпеливых! ⭐",
        "needs_review": True,
        "html": "<p>Представь, что ты помогаешь кому-то найти дорогу. Напиши диалог, используя примеры выше "
                "и карту из предыдущего задания. У тебя получится!</p>" + book("map_river", "Карта"),
    }),
    bye("well_done_trophy", "Bye-bye! 🚌", "Ты отлично справился. До встречи на уроке!"),
]


# ---------- Homework 5 ----------

LONDON = (
    "<h3>An amazing city</h3>"
    "<p>London is a very big city today. It was very big in 1965 too. My grandpa was a boy in London then.</p>"
    "<p>In 1965 London was an exciting place for fashion and music. The fashion industry was new then and "
    "there were a lot of small clothes shops. Pop music was also new, and bands like The Beatles were very "
    "popular. There were a lot of small cafés. The theatres were busy, and the museums were full of people.</p>"
    "<p>Today some things about London are different. Now there are more big shops and shopping centres. "
    "There are many large cafés. The theatres have more music shows today like <i>Mamma Mia</i>. "
    "The museums are full today too. But there are more things to do today. For example, you can have a "
    "ride on the London Eye. It was new in 2000.</p>"
)

HW5 = [
    hello("hello_laptop", "Привет, самый старательный и классный ученик!",
          "Сегодня тебе предстоит много читать :) Но ты точно справишься, ведь для тебя нет ничего "
          "невозможного 😎 Давай начнём?"),
    # 2
    ("text", {"html": "<p>Для начала давай прочитаем текст.</p>" + book("london", "London Eye") + LONDON}),
    # 3
    ("quiz", {"title": "Прекрасно! Прочитай предложения и выбери правильный вариант", "questions": [
        q("London is a very ___ place.", ["big", "small"], "big"),
        q("In 1965 there were a lot of ___ shops in London.", ["big", "small"], "small"),
        q("Pop music was ___ then.", ["new", "old"], "new"),
        q("The museums ___ full in 1965.", ["weren't", "were"], "were"),
        q("Today London has got more ___.", ["theatres", "shopping centres"], "shopping centres"),
        q("The London Eye is a ___.", ["ride", "museum"], "ride"),
    ]}),
    # 4
    ("gaps", {
        "title": "Ещё раз прочитай текст и ответь на вопросы коротким ответом. Первый — пример",
        "mode": "type",
        "text": "1. Was the writer's grandpa a boy in 1965? Yes, he was.\n"
                "2. Was pop music new in London in 1965? __" + sentence_alts("Yes, it was") + "__\n"
                "3. Were the theatres busy in 1965? __" + sentence_alts("Yes, they were") + "__\n"
                "4. Were there large cafés like Starbucks in the past? __"
                + sentence_alts("No, there weren't") + "__\n"
                "5. Are there more music shows today? __" + sentence_alts("Yes, there are") + "__",
        "gaps_expected": 4,
    }),
    # 5 — места в городе: целые слова по картинкам
    ("text", {"html": "<h3>Места в городе</h3><p>Ты просто супер! Повторим места в городе. Посмотри на "
                      "картинку, прочитай предложение и впиши пропущенное слово целиком — первая буква "
                      "подскажет. Первое предложение — на два слова.</p>"}),
    ("exact_input", {"items": [
        {"image": img(U, "sports_centre"), "prompt": "1. Let's play basketball at the s______ c______.",
         "accept": ["sports centre", "sports center"], "audio_tts": "sports centre"},
        {"image": img(U, "film_studio"), "prompt": "2. They're making a film at the film s______.",
         "accept": ["studio", "film studio"], "audio_tts": "film studio"},
        {"image": img(U, "theme_park"), "prompt": "3. The rides at this theme p______ are exciting.",
         "accept": ["park", "theme park"], "audio_tts": "theme park"},
        {"image": img(U, "shopping_centre"), "prompt": "4. Do you want to buy some clothes at the s______ centre?",
         "accept": ["shopping", "shopping centre", "shopping center"], "audio_tts": "shopping centre"},
        {"image": img(U, "police_station"), "prompt": "5. You can look for your lost bag at the police s______.",
         "accept": ["station", "police station"], "audio_tts": "police station"},
        {"image": img(U, "post_office"), "prompt": "6. I'm going to the post o______ to post a letter.",
         "accept": ["office", "post office"], "audio_tts": "post office"},
        {"image": img(U, "train_station"), "prompt": "7. Let's buy our tickets to London at the t______ station.",
         "accept": ["train", "train station"], "audio_tts": "train station"},
        {"image": img(U, "swimming_pool"), "prompt": "8. I like the s______ pool, but I like the sea more!",
         "accept": ["swimming", "swimming pool"], "audio_tts": "swimming pool"},
    ]}),
    # 6 — подсказка по годам в выгрузке не прогрузилась, даём её текстом (на других годах)
    ("gaps", {
        "title": "Ты уже на финишной прямой! Впиши год цифрами. Подсказка: 1800 — eighteen hundred, "
                 "1999 — nineteen ninety-nine, 2008 — two thousand and eight, 2010 — twenty ten",
        "mode": "type",
        "text": "1. nineteen hundred — __1900__\n"
                "2. nineteen fifteen — __1915__\n"
                "3. nineteen fifty — __1950__\n"
                "4. nineteen sixty-five — __1965__\n"
                "5. two thousand — __2000__\n"
                "6. twenty fifteen — __2015__",
        "gaps_expected": 6,
    }),
    bye("congrats_popper", "Ура, всё готово! 🎉", "Ты много читал и отлично справился. До встречи на уроке!"),
]


# ---------- Homework 6 ----------

ADJ = [  # (слово, перевод, картинка или None)
    ("busy", "оживлённый, людный", "busy_street"),
    ("quiet", "тихий", "quiet_street"),
    ("small", "маленький", "small_house"),
    ("big", "большой", "big_house"),
    ("interesting", "интересный", "interesting_museum"),
    ("boring", "скучный", None),
    ("old", "старый", "old_stadium"),
    ("new", "новый", "new_stadium"),
    ("clean", "чистый", "clean_cinema"),
    ("dirty", "грязный", "dirty_cinema"),
]

HW6 = [
    hello("hello_headphones", "Добро пожаловать в домашнее задание!",
          "Сегодня мы послушаем, как Джимми разговаривает с мамой, повторим прилагательные "
          "и поговорим о городе в прошлом и сейчас."),
    # 2
    todo(("task", {
        "title": "Послушай аудио и впиши названия мест в городе, о которых Джимми говорит с мамой",
        "needs_review": True,
        "audio": "",
        "html": "<p>Напиши названия мест, которые ты услышал, по-английски.</p>",
    }), ("audio", "аудио: Джимми с мамой смотрят старые фото (library, bank, supermarket, train station)")),
    # 3
    ("quiz", {"title": "Послушай аудио ещё раз и выбери правильный ответ", "questions": [
        q("Is Jimmy looking at new photos?", ["Yes", "No"], "No"),
        q("Was the library in Green Street?", ["Yes", "No"], "Yes"),
        q("Is there a library in Green Street now?", ["Yes", "No"], "No"),
        q("Was the bank next to the library?", ["Yes", "No"], "Yes"),
        q("Is there a supermarket next to the bank today?", ["Yes", "No"], "Yes"),
        q("Is Jimmy's mum behind the train station in the next photo?", ["Yes", "No"], "No"),
        q("Does Jimmy think his mum's hat was nice?", ["Yes", "No"], "No"),
    ]}),
    # 4 — сначала карточки прилагательных (листы 38–39), потом пропуски
    ("flashcards", {"cards": [
        dict({"text": w, "translation": ru, "audio_tts": w}, **({"image": img(U, f)} if f else {}))
        for w, ru, f in ADJ]}),
    ("gaps", {
        "title": "Прочитай предложения и заполни пропуски подходящими прилагательными",
        "mode": "drag",
        "text": "1. There are lots of people in the village. It's very __busy__. But it's usually __quiet__ "
                "on Sundays.\n"
                "2. This __small__ house has one bedroom, but that __big__ house has five.\n"
                "3. I usually think museums are __interesting__, but this one is __boring__. "
                "There's nothing good to see.\n"
                "4. The __old__ stadium wasn't great. But the __new__ stadium is amazing!\n"
                "5. The cinema was __clean__ before the film, but after the film it was __dirty__ because "
                "there was popcorn on the floor.",
        "gaps_expected": 10,
    }),
    # 5 — вместо обрезанного кадра учебника — наши «тогда / сейчас» (лист 40)
    ("task", {
        "title": "Город в прошлом и сейчас",
        "needs_review": True,
        "html": "<p>Посмотри на картинки города и расскажи, что там было и чего не было в прошлом, "
                "и что есть сейчас.</p>"
                f'<p><b>In the past</b><br><img src="{img(U, "town_past")}" alt="Город в прошлом" '
                'style="max-width:100%;width:400px"></p>'
                f'<p><b>Now</b><br><img src="{img(U, "town_now")}" alt="Город сейчас" '
                'style="max-width:100%;width:400px"></p>'
                "<p>Используй шаблон:<br><i>There was … . There were … . There wasn't … . "
                "There weren't … . There is … . There are … .</i></p>",
    }),
    # 6 — шаблон My town текстом
    ("task", {
        "title": "Дополнительное задание — по желанию ⭐",
        "needs_review": True,
        "html": "<p>Напиши о своём городе в прошлом и сейчас. Используй шаблон:</p>"
                "<p><i><b>My town</b><br>Hi, my name is Alice and I live in Overtown. It's a small town.<br>"
                "In the past … .<br>Today … .</i></p>",
    }),
    bye("well_done_medal", "Bye! 👋", "Ты отлично поработал. До встречи на уроке!"),
]


# ---------- Unit 5 Test ----------

TEST_WORDS = [("cinema", "кинотеатр"), ("library", "библиотека"), ("museum", "музей"),
              ("restaurant", "ресторан"), ("stadium", "стадион"), ("theatre", "театр")]


def order(*words):
    s = " ".join(words)
    return ("order", {"words": list(words), "sentence": s, "audio_tts": s})


GRANDFATHER = (
    "<h3>READING · My Grandfather's Town</h3>"
    "<p>My name's Olivia and I love my town, Brighton. But my grandfather always says it was very different "
    "sixty years ago. Last Sunday we went for a walk and he told me about old Brighton.</p>"
    "<p>\"In 1965 there wasn't a shopping centre here,\" he said. \"Now there are lots of modern shops, but "
    "then there was just a small market on Saturdays. And the cinema was much smaller — there was only one "
    "screen!\"</p>"
    "<p>We walked past the train station. \"When I was a teenager, the station was old and dirty,\" he said. "
    "\"Now it's modern and clean — that's much better!\"</p>"
    "<p>Then we went to the park. \"This park was always my favourite place. My friends and I were here every "
    "weekend. There weren't any phones or computers, so we played football and rode our bikes for hours!\"</p>"
)

TFN = ["True", "False", "Not stated"]

TEST = [
    # 1
    ("exact_input", {"items": [
        {"image": img(U, w), "prompt": f"Напиши по-английски: {ru}",
         "accept": [w] + (["theater"] if w == "theatre" else []), "audio_tts": w}
        for w, ru in TEST_WORDS]}),
    # 2
    ("quiz", {"title": "Выбери правильный вариант, чтобы предложение было грамматически верным", "questions": [
        q("Yesterday I ___ at the swimming pool with my friends.", ["were", "was", "am"], "was"),
        q("My parents ___ at home last weekend.", ["weren't", "wasn't", "didn't"], "weren't"),
        q("___ you at the cinema last night?", ["Was", "Did", "Were"], "Were"),
        q("The shopping centre ___ very busy on Saturday.", ["is", "were", "was"], "was"),
        q("___ you two days ago?", ["Where was", "Where were", "Where you were"], "Where were"),
    ]}),
    # 3
    ("gaps", {
        "title": "Впиши was, wasn't, were или weren't",
        "mode": "type",
        "text": "1. The museum __was__ closed on Monday, so we went to the park.\n"
                "2. We __" + alt("weren't") + "__ at school last Tuesday because it was a holiday.\n"
                "3. — __Was__ the restaurant good? — Yes, it was amazing!\n"
                "4. My grandparents __were__ young in 1970.\n"
                "5. There __" + alt("wasn't") + "__ a sports centre in our town 1000 years ago.",
        "gaps_expected": 5,
    }),
    # 4 — пять «составь предложение»
    order("There", "was", "a", "small", "café", "opposite", "the", "library."),
    order("My", "brother", "wasn't", "at", "the", "stadium", "yesterday."),
    order("Where", "were", "you", "last", "Saturday", "evening?"),
    order("The", "hotel", "was", "between", "the", "bank", "and", "the", "post office."),
    order("Were", "your", "friends", "at", "the", "shopping centre", "last", "week?"),
    # 5
    ("text", {"html": GRANDFATHER}),
    ("quiz", {"title": "Прочитай текст выше. Выбери True (верно), False (неверно) или Not stated (в тексте не сказано)",
              "questions": [
        q("Olivia is from Brighton.", TFN, "True"),
        q("Olivia's grandfather thinks the town is the same as before.", TFN, "False"),
        q("There was a big shopping centre in Brighton in 1965.", TFN, "False"),
        q("The old cinema had only one screen.", TFN, "True"),
        q("Olivia's grandfather worked at the train station.", TFN, "Not stated"),
        q("He thinks the train station is better now.", TFN, "True"),
        q("Children played outside more in the past.", TFN, "True"),
    ]}),
    # 6
    todo(("sequence", {
        "title": "Послушай, как Лиам объясняет туристу дорогу до его отеля. Расставь места в том порядке, "
                 "в котором турист пройдёт мимо них",
        "audio": "",
        "items": [{"text": "the supermarket"}, {"text": "the post office"}, {"text": "the park"},
                  {"text": "the museum"}, {"text": "the café"}, {"text": "the Royal Hotel"}],
    }), ("audio", "аудио: Лиам объясняет туристу дорогу до Royal Hotel")),
    # 7
    ("speaking", {
        "title": "SPEAKING I 🎤",
        "needs_review": True,
        "image": img(U, "scene_street"),
        "html": "<p>Опиши картинку и ответь на вопросы. Запиши ответ (до 5 минут), нажав на кнопку микрофона.</p>"
                "<ol><li>What can you see in the picture?</li><li>Is this a big city or a small town?</li>"
                "<li>Is the street clean or dirty?</li><li>Is the place busy or quiet?</li>"
                "<li>Is it a modern or an old part of the city?</li><li>What buildings can you see?</li></ol>",
    }),
    # 8
    ("speaking", {
        "title": "SPEAKING II 🎤",
        "needs_review": True,
        "html": "<p>Ответь на вопросы полными предложениями. Запиши ответ (до 5 минут), нажав на кнопку микрофона.</p>"
                "<ol><li>Where do you live — in a big city, a small town or a village?</li>"
                "<li>Is your town clean and quiet, or busy and dirty?</li>"
                "<li>Is there a museum or a theatre in your town?</li>"
                "<li>What's your favourite place?</li>"
                "<li>Where's the nearest supermarket (opposite your house, behind the park, etc.)?</li>"
                "<li>Is there a swimming pool or a sports centre near your home?</li>"
                "<li>Where were you yesterday evening?</li>"
                "<li>Where were you last Saturday at three o'clock?</li>"
                "<li>Was the weather good or bad last weekend?</li></ol>",
    }),
]


LESSONS = {
    "u5_hw1": {**UNIT, "lesson_title": "Homework 1", "lesson_sort": 0, "kind": "homework", "blocks": HW1},
    "u5_hw2": {**UNIT, "lesson_title": "Homework 2", "lesson_sort": 1, "kind": "homework", "blocks": HW2},
    "u5_hw3": {**UNIT, "lesson_title": "Homework 3", "lesson_sort": 2, "kind": "homework", "blocks": HW3},
    "u5_hw4": {**UNIT, "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework", "blocks": HW4},
    "u5_hw5": {**UNIT, "lesson_title": "Homework 5", "lesson_sort": 4, "kind": "homework", "blocks": HW5},
    "u5_hw6": {**UNIT, "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework", "blocks": HW6},
    "u5_test": {**UNIT, "lesson_title": "Unit 5 Test", "lesson_sort": 6, "kind": "test", "blocks": TEST},
}
