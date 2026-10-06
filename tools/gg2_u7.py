"""Go Getter 2 · Unit 7 · Travel — 6 домашек и тест. Источник: docs/GG2_разбор_u7.md."""
from gg2_build import img, shared, todo, video

U = "u7"
UNIT = {"unit": U, "unit_title": "Unit 7 · Travel", "unit_sort": 7}


def hello(pic, title, *paras):
    body = "".join(f"<p>{p}</p>" for p in paras)
    return ("text", {"html": f'<p><img src="{shared(pic)}" alt="" style="height:200px"></p><h2>{title}</h2>{body}'})


def txt(*paras, image=None, h=None):
    html = (f"<h3>{h}</h3>" if h else "") + "".join(f"<p>{p}</p>" for p in paras)
    if image:
        html += f'<p><img src="{image}" alt="" style="max-width:100%"></p>'
    return ("text", {"html": html})


def q(question, options, correct, image=None):
    d = {"q": question, "type": "single", "options": [{"text": o} for o in options], "correct": [correct]}
    if image:
        d["image"] = image
    return d


def quiz(*questions, title=None):
    p = {"questions": list(questions)}
    if title:
        p["title"] = title
    return ("quiz", p)


def order(sentence, image=None, words=None, title=None):
    p = {"words": words or sentence.split(" "), "sentence": sentence, "audio_tts": sentence}
    if image:
        p["image"] = image
    if title:
        p["title"] = title
    return ("order", p)


def match(title, pairs, images=False):
    out = []
    for left, right in pairs:
        pr = {"left_image": left} if images else {"left": left}
        pr.update({"right": right, "right_audio_tts": right})
        out.append(pr)
    return ("match", {"title": title, "pairs": out})


def cards(items):
    return ("flashcards", {"cards": [{"text": t, "translation": tr, "image": im, "audio_tts": t}
                                     for t, tr, im in items]})


def exact(items, title="Напиши слово по-английски"):
    return ("exact_input", {"title": title, "items": [
        {"prompt": f"Напиши по-английски: {ru}", "accept": acc, "audio_tts": acc[0]} for ru, acc in items]})


def task(title, html):
    return ("task", {"title": title, "html": html, "needs_review": True})


def speaking(title, html, image=None):
    p = {"title": title, "html": html, "needs_review": True}
    if image:
        p["image"] = image
    return ("speaking", p)


def audio(title, what):
    return todo(("video", {"title": title, "url": "", "provider": "file"}), ("audio", what))


TRANSPORT = [
    ("car", "автомобиль"), ("boat", "лодка"), ("bike", "велосипед"), ("bus", "автобус"),
    ("motorbike", "мотоцикл"), ("plane", "самолёт"), ("taxi", "такси"), ("train", "поезд"),
    ("tram", "трамвай"), ("underground", "метро"),
]
VERBS = [
    ("arrive", "прибыть", "arrive"),
    ("get on", "сесть, войти (в автобус, поезд)", "get_on"),
    ("get off", "выйти (из автобуса, поезда)", "get_off"),
    ("leave", "уезжать, отправляться", "leave"),
    ("take", "сесть на (транспорт), поехать на", "take_bus"),
]

# ------------------------------------------------------------------ Homework 1
HW1 = [
    hello("hello_wave", "Привет! 👋",
          "Сейчас мы с тобой выучим разные виды транспорта, а потом — глаголы, которые с ним говорят.",
          "Выполни все задания, чтобы выучить слова на 100%!"),
    cards([(w, ru, img(U, w)) for w, ru in TRANSPORT]),
    match("Соедини картинку со словом", [(img(U, w), w) for w, _ in TRANSPORT], images=True),
    exact([("автомобиль", ["car", "a car"]), ("лодка", ["boat", "a boat"]),
           ("велосипед", ["bike", "a bike", "bicycle"]), ("автобус", ["bus", "a bus"]),
           ("мотоцикл", ["motorbike", "a motorbike"]), ("самолёт", ["plane", "a plane"]),
           ("такси", ["taxi", "a taxi"]), ("поезд", ["train", "a train"]),
           ("трамвай", ["tram", "a tram"]), ("метро", ["underground", "the underground"])]),
    txt("Отлично! А теперь выучим глаголы, которые нужны в дороге. "
        "Например: <i>take a bus</i> — поехать на автобусе, <i>get off the train</i> — выйти из поезда.",
        h="Глаголы в дороге 🚉"),
    cards([(w, ru, img(U, f)) for w, ru, f in VERBS]),
    match("Соедини картинку с глаголом", [(img(U, f), w) for w, _, f in VERBS], images=True),
    exact([("прибыть", ["arrive"]), ("сесть, войти (в автобус)", ["get on"]),
           ("выйти (из поезда)", ["get off"]), ("уезжать, отправляться", ["leave"]),
           ("сесть на (транспорт), поехать на", ["take"])]),
    hello("hello_rocket", "Дополнительная часть 🚀",
          "Добро пожаловать в ДОПОЛНИТЕЛЬНУЮ часть домашнего задания! Выполни все задания, чтобы хорошенько "
          "запомнить новые слова. Выполнив их, ты станешь МЕГАКЛАССНЫМ учеником!"),
    quiz(
        q("It is very long and it has lots of wheels. It runs on streets.", ["bus", "tram", "car"], 1),
        q("You can go to an island on this over water.", ["boat", "car", "bike"], 0),
        q("It flies in the air.", ["car", "motorbike", "plane"], 2),
        q("It has four wheels. Many families have got one.", ["bus", "car", "motorbike"], 1),
        q("Children have got these and they can ride them in the park.", ["boat", "plane", "bike"], 2),
        title="Прочитай описание и выбери подходящий транспорт"),
    ("gaps", {"title": "Прочитай историю про Энзо. Как он добирается до школы? Перетащи слова в пропуски",
              "mode": "drag", "image": img(U, "enzo"),
              "text": "14-year-old Enzo Paci lives in Queens in New York City and he travels two hours to a school "
                      "in the Bronx. It's a very good school. Enzo __takes__ a bus and two trains, and the last ten "
                      "minutes of his journey is __on__ foot. At 6.30 a.m. he goes to the train station __by__ bus. "
                      "The train __leaves__ at 7 a.m. and arrives in Manhattan at 8 a.m. Then, at 8.30 a.m. Enzo "
                      "__gets on__ another train to his school! It's one of the longest school journeys in the world!",
              "gaps_expected": 5}),
    speaking("Как ты добираешься до школы? 🎤",
             "<p>ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ — для самых смелых! Прочитай ещё раз историю Энзо и расскажи, "
             "как ты добираешься до школы.</p><p><i>Например: I go to school by bus. The bus leaves at 7.30 a.m.</i></p>"),
    hello("well_done_star", "Супер! ⭐⭐⭐⭐⭐", "Вся домашняя работа выполнена. Ты просто крут! Увидимся на уроке :)"),
]

# ------------------------------------------------------------------ Homework 2
HW2 = [
    hello("hello_wave", "Добро пожаловать! 👋",
          "Сегодня тебя ждёт много интересных упражнений! В конце — дополнительное задание. "
          "Если ты его сделаешь, получишь дополнительную звёздочку! ⭐"),
    txt("Для начала посмотри видео! Как думаешь, что на этот раз случилось с хомячком?",
        image=img(U, "book_hammy_rain")),
    video("Посмотри видео: что случилось с Хэмми и друзьями? 🌧️",
          "видео учебника: Хэмми и друзья не попали в кино — автобус не пришёл, пошёл дождь"),
    quiz(q("The bus ___.", ["come", "came"], 1),
         q("We ___ umbrellas.", ["had", "has"], 0),
         q("We ___ to the cinema.", ["goes", "went"], 1),
         title="Посмотри видео и выбери правильный вариант"),
    ("sequence", {"title": "Посмотри видео ещё раз и расставь предложения в том порядке, как они идут в рассказе",
                  "items": [{"text": t} for t in [
                      "How was the cinema last night?", "It is a long story.", "The bus didn't come.",
                      "It started to rain.", "We wanted to take a taxi.", "We didn't go to the cinema.",
                      "We came home."]]}),
    txt("Отлично, ты посмотрел видео и выполнил задание! А теперь практика: расставь слова в правильном порядке."),
    order("Tim ate pizza at the pizzeria.", img(U, "tim_pizza")),
    order("Dad drank coffee in the kitchen.", img(U, "dad_coffee")),
    order("Tina wore a hat.", img(U, "tina_hat")),
    order("Mum and Stan went to the supermarket.", img(U, "mum_stan_shop")),
    txt("Молодец! Ты справился с большей частью заданий. Давай ещё немного потренируемся! "
        "Сделай из утвердительных предложений отрицательные."),
    quiz(q("Elena and Amy stayed at home. → Elena and Amy ___ at home.", ["didn't stay", "stayed"], 0),
         q("The first night Elena slept well. → The first night Elena ___ well.", ["sleepy", "didn't sleep"], 1),
         q("The spider went inside Elena's sleeping bag. → The spider ___ inside Elena's sleeping bag.",
           ["didn't go", "gone"], 0),
         q("That evening they ate at a restaurant. → That evening they ___ at a restaurant.",
           ["eat", "didn't eat"], 1),
         title="Выбери отрицательную форму"),
    txt("А здесь — дополнительное задание для самых смелых! Посмотри, что Эми и Елена взяли с собой в путешествие.",
        image=img(U, "scene_suitcase")),
    match("Соедини названия предметов с картинками", [
        (img(U, "guidebook"), "guidebook"), (img(U, "sun_hat"), "hat"), (img(U, "suitcase"), "suitcase"),
        (img(U, "socks"), "socks"), (img("u3", "camera"), "camera"), (img(U, "passport"), "passport"),
        (img(U, "sunglasses"), "sunglasses")], images=True),
    task("Что вы берёте в путешествие? ✍️",
         "<p>Мне очень интересно, что ты и твоя семья берёте с собой в путешествия! Напиши небольшой текст о том, "
         "какие вещи вы брали с собой, когда ездили отдыхать.</p><p><i>Например: I took a tent, a camera …</i></p>"
         "<p>Не забудь прочитать свой текст учителю на уроке!</p>"),
    hello("congrats_popper", "Поздравляю! 🎉",
          "Ты завершил домашнее задание, ты замечательный ученик! Увидимся на занятии!"),
]

# ------------------------------------------------------------------ Homework 3
HW3 = [
    hello("hello_wave", "Добро пожаловать! 👋",
          "В этом уроке тебя ждёт интересное видео и классные упражнения! В конце есть дополнительное задание — "
          "его можно выполнить по желанию, НО если выполнишь, будешь нереально крут!"),
    txt("Готов начать? Посмотри видео! Куда отправились Анна, Макс и Хэмми на этот раз?",
        image=img(U, "book_hammy_explorer")),
    video("Посмотри видео: куда отправились Анна, Макс и Хэмми? 🧭",
          "видео учебника: Anna, Max и Hammy на каникулах, обезьяна с фотоаппаратом"),
    match("Посмотри видео ещё раз и соедини вопросы и ответы", [
        ("Did you have a good holiday?", "Yes, I did."),
        ("Did you stay in the hotel?", "No, I didn't."),
        ("Did the monkey take any photos?", "Yes, it did.")]),
    txt("Отлично! А теперь настало время потрудиться: расставь слова в вопросах в правильном порядке."),
    order("Did they go on holiday last weekend?"),
    order("Did the boy sleep in a tent?"),
    order("Did your grandparents go shopping yesterday?"),
    order("Did your granny buy a new camera?"),
    quiz(q("Did Big Al go to Italy last week?", ["Yes, he did.", "No, he doesn't."], 0),
         q("Did he stay in the hotel?", ["Yes, I do.", "No, he didn't."], 1),
         q("Did Al and Sofia eat at a restaurant?", ["No, she didn't.", "Yes, they did."], 1),
         q("Did Al buy a T-shirt?", ["Yes, he did.", "No, she didn't."], 0),
         q("Did Al like Sofia?", ["No, they didn't.", "Yes, he did."], 1),
         title="Ты хорошо справляешься! Прочитай вопросы про Big Al и выбери правильный ответ"),
    txt("Смотри, сколько ты уже сделал! А теперь давай обсудим, что можно делать на каникулах :)"),
    quiz(q("Что здесь делают?", ["take photos", "eat at a restaurant", "play computer games"], 1, img(U, "restaurant")),
         q("Что здесь делают?", ["take photos", "visit a museum", "make friends"], 0, img(U, "take_photos")),
         q("Что здесь делают?", ["stay in a hotel", "eat pizza", "visit a museum"], 2, img(U, "museum")),
         q("Что здесь делают?", ["buy a souvenir", "stay in a hotel", "go sightseeing"], 1, img(U, "hotel")),
         q("Что здесь делают?", ["play the piano", "go sightseeing", "buy a souvenir"], 2, img(U, "souvenir")),
         title="Посмотри на картинку и выбери правильный вариант"),
    txt("Молодец! Запомнил выражения? А теперь соедини первую часть выражения со второй!"),
    match("Соедини части выражений", [
        ("buy", "a souvenir"), ("visit", "a museum"), ("make", "friends"), ("eat", "at a restaurant"),
        ("stay", "in a hotel"), ("take", "photos"), ("go", "sightseeing")]),
    task("Мои каникулы ✍️",
         "<p>Дополнительное задание для самых больших умников! Вспомни: куда ты ездил отдыхать в последний раз? "
         "Напиши небольшой текст о том, чем ты занимался в путешествии, и прочитай его на занятии.</p>"
         "<p><i>Например: I went sightseeing with my family. We took a lot of photos …</i></p>"),
    hello("well_done_trophy", "Поздравляю! 🏆",
          "Ты завершил домашнее задание, ты замечательный ученик! Не забудь показать свой текст на занятии — "
          "и получишь дополнительную звёздочку от учителя! 🌟 Увидимся!"),
]

# ------------------------------------------------------------------ Homework 4
HW4 = [
    hello("hello_wave", "Привет! 👋",
          "Готов выполнять домашнее задание? Тебя ждёт интересное видео! В конце есть дополнительное "
          "упражнение — его можно выполнить по желанию, НО если выполнишь, будешь нереально крут!"),
    txt("Сегодня мы отправимся в путешествие! Но сначала представь, что тебе нужно купить билет на поезд. "
        "Как спросить по-английски, сколько стоит билет? Посмотри видео и выполни задания к нему."),
    video("Посмотри видео: покупаем билет на поезд 🎫",
          "видео: покупка билета на поезд в Калифорнию (How much is it? Which platform?)"),
    match("Соедини вопросы с ответами", [
        ("How can I help you?", "I would like to buy a train ticket to California."),
        ("How much is it?", "It costs 40 dollars."),
        ("Which platform is the train on?", "Platform Number 2."),
        ("When does it leave?", "It leaves at 6:30 pm.")]),
    todo(("gaps", {"title": "Прочитай диалог и перетащи реплики продавщицы в пропуски",
                   "mode": "drag",
                   "text": "Boy: I'd like two tickets to York, please.\nWoman: __Here you are.__\n"
                           "Boy: How much is it?\nWoman: __It is ten pounds, please.__\n"
                           "Boy: What time does the train leave?\nWoman: __At 10:30 a.m.__\n"
                           "Boy: What time does it arrive?\nWoman: __At 11:45 a.m.__",
                   "gaps_expected": 4}),
         ("check", "время прибытия исправлено: в оригинале «At 10 a.m.» (раньше отправления 10:30 a.m.), "
                   "поставлено «At 11:45 a.m.»; вписывание фраз заменено перетаскиванием")),
    ("text", {"html": "<h3>LOOK! Prices 💷</h3><p>Молодец! Теперь узнаем, как по-английски говорят о деньгах. "
                      "Внимательно посмотри правило!</p><p>£10.50 = <b>ten pounds fifty</b><br>"
                      "£7.25 = <b>seven pounds twenty-five</b><br>£0.50 = <b>fifty pence</b></p>"}),
    match("А теперь соедини цифры со словами", [
        ("£2.50", "two pounds fifty"), ("£0.75", "seventy-five pence"), ("£30.40", "thirty pounds forty"),
        ("£22.60", "twenty-two pounds sixty"), ("£0.30", "thirty pence")]),
    ("text", {"html": "<h3>Билет до Оксфорда 🚆</h3><p>Так держать! А теперь чтение. Внимательно прочитай диалог.</p>"
                      "<p><b>A:</b> What time does the next train from London to Oxford leave?<br>"
                      "<b>B:</b> At quarter past one.<br><b>A:</b> I'd like one ticket, please.<br>"
                      "<b>B:</b> Here you are.<br><b>A:</b> How much is it?<br>"
                      "<b>B:</b> It's twelve pounds fifty, please.<br><b>A:</b> What time does it arrive in Oxford?<br>"
                      "<b>B:</b> At half past three.</p>"}),
    ("gaps", {"title": "Прочитай диалог ещё раз и заполни билет (время пиши цифрами, например 2:45)",
              "mode": "type", "image": img(U, "book_ticket"),
              "text": "From: London\nTo: __Oxford__\nPrice: £__12.50|12,50|12.5__\n"
                      "Leave: __1:15|01:15|13:15|1.15__\nArrive: __3:30|03:30|15:30|3.30__",
              "gaps_expected": 4}),
    txt("Молодец! Осталось последнее задание. Подумай: в какую страну ты хотел бы сейчас уехать? "
        "Напиши данные своего билета, как в предыдущем упражнении.",
        "<i>Например: Train ticket: From: Russia To: London Price: £50 Leave: 2:50 Arrive: 8:30</i>"),
    task("Мой билет ✍️", "<p>Посмотри на пример ещё раз и напиши данные своего билета: "
                         "From, To, Price, Leave, Arrive.</p>"),
    hello("well_done_trophy", "Отлично! 🏆", "Ты справился со всеми заданиями. Ты — большой молодец! Жду тебя на занятии!"),
]

# ------------------------------------------------------------------ Homework 5
TFN = ["True", "False", "Not stated"]
HW5 = [
    hello("hello_wave", "Привет-привет! 👋",
          "Очень здорово, что ты снова решил сделать домашнюю работу. Сегодня мы будем много читать, "
          "но тебе понравится 😎 Ну что, начинаем!"),
    txt("Любишь ли ты путешествовать? Какие города и страны ты уже посетил? Сегодня мы прочитаем историю про "
        "Эдмунда Хиллари. Он часто путешествовал из-за своей работы. Как думаешь, куда он отправился на этот раз?"),
    ("text", {"html": "<h3>Edmund Hillary 🏔️</h3>"
              f'<p><img src="{img(U, "everest")}" alt="" style="max-width:100%"></p>'
              "<p>In 1953, the <b>explorer</b> Edmund Hillary travelled to the Himalayan Mountains with two climbing "
              "teams. He was on an <b>expedition</b> to climb the tallest mountain in the world – Mount Everest. "
              "The mountain was very <b>dangerous</b>. There was snow and ice, and it was very <b>cold</b>.</p>"
              "<p>There were two teams for the climb to the top. The first team <b>tried</b>, but they didn't get "
              "there. Edmund Hillary and his guide Tenzing Norgay were the second <b>team</b>. They started to climb "
              "the mountain. Their backpacks were <b>heavy</b> – 14 kg! They had a <b>tent</b>, food and a camera "
              "with them.</p><p>On 29th May, Edmund Hillary and Tenzing Norgay <b>arrived</b> at the top of Mount "
              "Everest. Edmund <b>got</b> there first. Edmund took photos of Tenzing and the <b>tall</b> mountain, "
              "but he didn't want Tenzing to <b>take</b> a photo of him. So there isn't a photo of Edmund Hillary "
              "on the top of the world!</p>"}),
    quiz(q("How many people got to the top of Mount Everest on 29th May?",
           ["four people", "two people", "eight people", "ten people"], 1),
         title="Прочитай текст и ответь на вопрос"),
    txt("Молодец! Прочитай текст об экспедиции ещё раз.",
        "Для каждого предложения выбери: правда (<b>True</b>), неправда (<b>False</b>) или "
        "<b>Not stated</b> — если по тексту этого определить нельзя."),
    quiz(q("The expedition was in the Himalayan Mountains.", TFN, 0),
         q("The weather wasn't cold.", TFN, 1),
         q("There were three men on the first team.", TFN, 2),
         q("The first team didn't get to the top.", TFN, 0),
         q("Edmund Hillary got to the top before Tenzing Norgay.", TFN, 0),
         q("They were very tired.", TFN, 2),
         q("Tenzing didn't want Edmund to take his photo.", TFN, 1),
         q("There isn't a photo of Edmund on the top of Mount Everest.", TFN, 0),
         title="True, False или Not stated?"),
    task("Ответь на вопросы ✍️",
         "<p>Молодец! Осталось последнее задание. Прочитай текст ещё раз и письменно ответь на вопросы:</p><ol>"
         "<li>When did this expedition happen?</li><li>What was the name of the mountain?</li>"
         "<li>How many teams were there?</li><li>How heavy were the backpacks?</li>"
         "<li>Who arrived at the top first?</li><li>Why isn't there a photo of Edmund at the top?</li></ol>"),
    hello("well_done_trophy", "Ура! 🏆", "Ты справился с домашним заданием! Ты — мегакрутой ученик. "
                                         "Увидимся на занятии. Goodbye!"),
]

# ------------------------------------------------------------------ Homework 6 (1) + (2)
HW6 = [
    hello("hello_wave", "Добро пожаловать! 👋",
          "Сегодня мы послушаем интересную аудиозапись, напишем открытку и вспомним транспорт и прошедшее время. Поехали!"),
    txt("А начнём мы с аудио. Это — Пенни. Послушай её разговор с Дэвидом и выполни задания.",
        image=img(U, "penny_skateboard")),
    audio("Послушай разговор Пенни и Дэвида 🎧", "аудио учебника: Penny рассказывает David про свой отпуск"),
    quiz(q("Did Penny have a nice holiday?",
           ["No, I didn't. It was horrible!", "Yes, I did. It was amazing!", "Yes, I do. It was fun!"], 1),
         title="Послушай аудио и выбери правильный ответ"),
    todo(match("Послушай аудио ещё раз и соедини вопросы с ответами", [
        ("Where did Penny stay?", "She stayed at a hotel."),
        ("What did she do every day?", "She went swimming every day."),
        ("What did she take the photos with?", "She took a lot of photos with her mobile phone."),
        ("What did she download her photos to?", "She downloaded photos to her tablet."),
        ("What was the weather like?", "It was sunny!")]),
         ("check", "в оригинале «Jenny» — заменено на Penny; ответ про погоду «Yes! It was sunny!» → «It was sunny!»")),
    todo(match("Вспомни слова из аудио! Соедини картинки с названиями", [
        (img("u3", "tablet"), "tablet"), (img("u3", "camera"), "camera"), (img(U, "hotel"), "hotel"),
        (img("u3", "mobile_phone"), "mobile phone")], images=True),
         ("check", "в оригинале 5 слов, «photo» убрано — отдельной карточки «фотография» нет, а с camera она путается")),
    txt("Отлично! Теперь напишем открытку. Для начала прочитай открытку Терри для Джоша и заполни пропуски."),
    ("gaps", {"title": "Перетащи фразы в пропуски", "mode": "drag",
              "text": "__Hi__ Josh!\n__We're having a lovely time in__ London. It's cloudy here, but it isn't cold. "
                      "We're staying in a nice hotel. __There are lots of__ museums and cafés, but the hotel isn't "
                      "near the big shops. __Yesterday we went to__ the Science Museum and I bought some souvenirs. "
                      "For dinner we had cheeseburgers and chips and it was great! Today we are at the river. "
                      "There's a boat here that goes to Tower Bridge. It leaves in 20 minutes! I hope it's fun!\n"
                      "__Lots of love__,\nTerry",
              "gaps_expected": 5}),
    task("Открытка другу ✍️",
         "<p>Напиши открытку своему другу! О чём ты хотел бы ему рассказать? Постарайся ответить в тексте "
         "на вопросы:</p><ol><li>Where are you?</li><li>Where are you staying?</li><li>What's the weather like?</li>"
         "<li>What did you do/eat/drink yesterday?</li><li>What are you doing today?</li></ol>"),
    txt("Молодец! Первая часть позади. Во второй части закрепим транспорт и прошедшее время. Let's go! 😎",
        h="Вторая часть"),
    match("Давай вспомним виды транспорта. Соедини картинку со словом", [
        (img(U, w), w) for w in ["car", "bike", "lorry", "train", "bus", "plane", "boat"]], images=True),
    todo(match("Какие слова мы говорим с транспортом? Соедини глагол с маленьким словом", [
        ("arrive ___ the station", "at"), ("get ___ the bus (выйти)", "off"),
        ("get ___ the train (сесть)", "on"), ("go to school ___ bus", "by")]),
         ("check", "СОСТАВ МОЙ: в оригинале только 2 пары (arrive — at, get — off), добавлены get on и by bus")),
    txt("Молодец! Следующее задание — выбери, какие слова пропущены."),
    quiz(q("Be careful when you get ___.", ["on foot", "on the boat"], 1, img(U, "boat")),
         q("I go to school ___.", ["by car", "by bus"], 0, img(U, "car")),
         q("Dad always ___ of us on holiday.", ["takes a taxi", "takes pictures"], 1, img(U, "dad_photos")),
         q("Terry always goes to work ___.", ["by bike", "by car"], 0, img(U, "bike")),
         q("The boy ___ at this stop.", ["get on the boat", "gets off the bus"], 1, img(U, "kids_off_bus")),
         title="Посмотри на картинку и выбери правильный вариант"),
    ("gaps", {"title": "Вспомним прошедшее время! Напиши подходящие вопросы и ответы. "
                       "Образец: A: Did you stay in a hotel in London? B: Yes, I did.",
              "mode": "type",
              "text": "1) A: __Did he leave|did he leave__ (he / leave) at 9 a.m.? B: Yes, he did.\n"
                      "2) A: __Did your dad cook|did your dad cook__ (your dad / cook) dinner last night? "
                      "B: No, he didn't.\n"
                      "3) A: Did your mum have coffee for breakfast? B: __Yes, she did.|Yes, she did|yes, she did__\n"
                      "4) A: Did he go to school yesterday? B: __Yes, he did.|Yes, he did|yes, he did__\n"
                      "5) A: Did they arrive at 3 p.m.? B: __No, they didn't.|No, they didn't|no, they didn't|"
                      "No, they did not.__",
              "gaps_expected": 5}),
    txt("Молодец! Следующее задание — расставь слова в правильном порядке."),
    todo(order("Did you go to school by bus?"),
         ("game", "СОСТАВ МОЙ: пересобрана игра Wordwall «Unjumble — Past Simple negative & interrogative forms» "
                  "— 5 блоков order подряд")),
    order("I didn't take a taxi."),
    order("Did they arrive at the station on time?"),
    order("We didn't get off the train."),
    order("Where did she buy the ticket?"),
    task("Моя дорога в школу ✍️",
         "<p>Дополнительное задание для самых смелых! Расскажи, как ты добираешься до школы. "
         "Постарайся ответить на вопросы:</p><ul><li>What time do you leave home?</li>"
         "<li>What transport do you use?</li><li>How long does it take?</li>"
         "<li>Do you like your journey to school? Why/Why not?</li></ul>"
         "<p>Не забудь прочитать свой рассказ учителю!</p>"),
    hello("well_done_star", "Ты супер ученик! ⭐", "Ты справился с домашним заданием — держи звёздочку! До встречи на занятии!"),
]

# ------------------------------------------------------------------ Test
TEST = [
    exact([("прибыть", ["arrive"]), ("лодка", ["boat", "a boat"]), ("мотоцикл", ["motorbike", "a motorbike"]),
           ("самолёт", ["plane", "a plane"]), ("поезд", ["train", "a train"]),
           ("метро", ["underground", "the underground"])], title="VOCABULARY. Напиши слова по-английски"),
    todo(quiz(q("We ___ the bus yesterday — we walked.", ["didn't took", "didn't take", "wasn't take"], 1),
         q("___ the museum last weekend?", ["Did you visit", "Did you visited", "Were you visit"], 0),
         q("My parents ___ in a hotel — they stayed with friends.", ["weren't stay", "didn't stayed", "didn't stay"], 2),
         q("Where ___ on holiday last summer?", ["Tom did go", "did Tom go", "did Tom went"], 1),
         q("— ___ you buy any souvenirs? — Yes, I did.", ["Were", "Do", "Did"], 2),
         q("— Did you ___ any souvenirs? — Yes, I did.", ["buy", "buyed", "bought"], 0),
         title="GRAMMAR. Выбери вариант, чтобы предложение было грамматически верным"),
         ("check", "пятое предложение разбито на два вопроса (Did / buy); подсказки «(Were / buyed) "
                   "(Did / bought)» из текста убраны, повтор «did» среди вариантов заменён на «Do»")),
    ("gaps", {"title": "Поставь глагол в скобках в правильную форму", "mode": "type",
                   "text": "1) We __didn't go|did not go__ (not go) sightseeing because the weather was bad.\n"
                           "2) __Did|did__ you __eat__ (eat) at a Spanish restaurant in Madrid?\n"
                           "3) My sister __didn't make|did not make__ (not make) any new friends on the trip.\n"
                           "4) Where __did__ they __stay__ (stay) in Paris?\n"
                           "5) I __didn't take|did not take__ (not take) my camera, so I haven't got any photos.",
                   "gaps_expected": 7}),
    order("Why did you take a taxi to the airport?",
          words=["Why", "did", "you", "take", "a taxi", "to", "the airport?"],
          title="Расставь части предложения в правильном порядке"),
    order("We didn't get off the bus at the right stop.",
          words=["We", "didn't", "get off", "the bus", "at", "the right stop."]),
    order("Did your family go to the beach last summer?",
          words=["Did", "your family", "go", "to", "the beach", "last summer?"]),
    order("When did the train arrive in London?",
          words=["When", "did", "the train", "arrive", "in", "London?"]),
    order("I didn't pack my sleeping bag, so I was cold.",
          words=["I", "didn't", "pack", "my sleeping bag,", "so", "I", "was cold."]),
    ("text", {"html": "<h3>READING. My Trip to Rome 🇮🇹</h3><p>Прочитай рассказ Эммы о её поездке в Рим.</p>"
              "<p>Last April, my family and I went to Rome for a week. It was an amazing trip! We flew from London "
              "to Rome on Sunday morning. The plane was very fast – only two and a half hours. From the airport, we "
              "took a taxi to our hotel because there was a lot of luggage.</p><p>On Monday, we visited the "
              "Colosseum. It was incredible, but very busy with tourists. My dad took hundreds of photos. After "
              "that, we ate pizza at a small restaurant near the hotel – the best pizza I've ever had!</p><p>On "
              "Wednesday, we went sightseeing all day and made friends with an American family. Their daughter "
              "Lily was twelve, like me. We chat online now. On our last day, I bought a small souvenir – a tiny "
              "model of the Colosseum. I didn't want to leave Rome!</p>"}),
    match("Соедини вопросы с правильными ответами", [
        ("How long did Emma's family stay in Rome?", "for one week"),
        ("How did they travel from London to Rome?", "by plane"),
        ("Why did they take a taxi to the hotel?", "because they had a lot of luggage"),
        ("What did they do on Monday?", "They visited the Colosseum."),
        ("What did Emma's dad do at the Colosseum?", "He took hundreds of photos."),
        ("Where did they have pizza?", "at a small restaurant near the hotel"),
        ("How did Emma feel at the end of the trip?", "She didn't want to leave.")]),
    audio("LISTENING. Послушай разговор в кассе на железнодорожной станции 🎧",
          "аудио теста: разговор в кассе вокзала (билет до Эдинбурга, return, обратно в воскресенье вечером, "
          "поезд 11:30, £85, платформа 6)"),
    todo(quiz(q("Where is the customer going?", ["London", "Edinburgh", "Glasgow", "Manchester"], 1),
              q("What kind of ticket does she want?", ["single", "return", "family", "student"], 1),
              q("When is the customer coming back?",
                ["Saturday morning", "Saturday evening", "Sunday evening", "Monday morning"], 2),
              q("What time does the next train leave?", ["11:00", "11:15", "11:30", "11:45"], 2),
              q("How much is the ticket?", ["£55", "£75", "£85", "£95"], 2),
              q("Which platform does the train leave from?", ["platform 4", "platform 5", "platform 6", "platform 16"], 2),
              title="Послушай аудио и выбери правильный ответ на каждый вопрос"),
         ("check", "ключи LISTENING взяты из выгрузки, по аудио не сверены (аудио нет)")),
    speaking("SPEAKING I 🎤",
             "<p>Опиши картинку и ответь на вопросы. Запиши ответ, нажав на кнопку микрофона.</p><ol>"
             "<li>Where are the people?</li><li>How many people are there?</li><li>What are they wearing?</li>"
             "<li>What can you see?</li><li>Are they going to travel by plane or by train?</li></ol>",
             image=img(U, "scene_airport")),
    speaking("SPEAKING II 🎤",
             "<p>Ответь на вопросы полными предложениями. Запиши ответ, нажав на кнопку микрофона.</p><ol>"
             "<li>Did you go on holiday last summer? Where did you go?</li>"
             "<li>How did you travel — by car, by train, by plane or by bus?</li>"
             "<li>What did you take with you in your suitcase?</li><li>Did you take a lot of photos?</li>"
             "<li>Did you visit any museums?</li><li>Did you buy any souvenirs? What did you buy?</li>"
             "<li>What was the best thing about the trip?</li></ol>"),
]

LESSONS = {
    "u7_hw1": {**UNIT, "lesson_title": "Homework 1", "lesson_sort": 0, "kind": "homework", "blocks": HW1},
    "u7_hw2": {**UNIT, "lesson_title": "Homework 2", "lesson_sort": 1, "kind": "homework", "blocks": HW2},
    "u7_hw3": {**UNIT, "lesson_title": "Homework 3", "lesson_sort": 2, "kind": "homework", "blocks": HW3},
    "u7_hw4": {**UNIT, "lesson_title": "Homework 4", "lesson_sort": 3, "kind": "homework", "blocks": HW4},
    "u7_hw5": {**UNIT, "lesson_title": "Homework 5", "lesson_sort": 4, "kind": "homework", "blocks": HW5},
    "u7_hw6": {**UNIT, "lesson_title": "Homework 6", "lesson_sort": 5, "kind": "homework", "blocks": HW6},
    "u7_test": {**UNIT, "lesson_title": "Unit 7 Test", "lesson_sort": 6, "kind": "test", "blocks": TEST},
}
