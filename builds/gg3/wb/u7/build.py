# -*- coding: utf-8 -*-
"""Go Getter 3, юнит 7 «Where I live» по рабочей тетради (стр. 60–66).

Ключи 7.7 — Answer key тетради (стр. 95); ключи аудирования 7.6 — по расшифровке
трека A18: Чарли живёт в многоквартирном доме; дядя — в маленькой квартире и
держит велосипед в подвале (лифт туда не идёт), Чарли и Амин живут на втором
этаже дверь в дверь, бабушка с дедушкой Амина — на первом (ground floor), Мэри
с семьёй — в большой квартире на последнем этаже; в воскресенье у них праздник
ко Дню матери.

Задания, которые в тетради держатся на картинке (7.1 Ex3 — фото квартиры,
7.3 Ex1 — подписать мебель на фото, 7.5 Ex2 — подписать фото домов,
7.6 Ex1 — подписать этажи на рисунке, 7.7 Ex1 — картинки про Сандру),
переписаны в текстовые: описание вместо картинки. Своих картинок не добавляем.
"""
import io, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import (AUDIO, privet, poka, kartochki, kviz, pary, propuski, gruppy,
                    predlozheniya, vpisat, govorenie, pismo, tekst, posledovatelnost, sql_uroka)

UNIT = 'cf15bae3-9e38-4b55-bf3d-a263b994126e'   # Unit 7 · Where I live
TEST = 'd72b1e55-b713-4966-9f8d-4fc505021d7a'
TRACK18 = AUDIO + 'GG%20L3%20WkBk%20A18.mp3'

# ─────────────────────── ДЗ 1 · 7.1 Vocabulary ───────────────────────
SLOVA = [
    ('city', 'большой город'), ('town', 'город, городок'), ('village', 'деревня'),
    ('the country', 'сельская местность'), ('island', 'остров'),
    ('a cottage', 'домик в деревне'), ('a detached house', 'отдельно стоящий дом'),
    ('a semi-detached house', 'дом на две семьи'),
    ('a terraced house', 'дом в сплошном ряду домов'),
    ('a block of flats', 'многоквартирный дом'), ('a flat', 'квартира'),
    ('an attic', 'чердак, мансарда'), ('a balcony', 'балкон'),
    ('a lift', 'лифт'), ('stairs', 'лестница'),
]

hw1 = [
    privet(0, 'Unit 7 · Where I live',
           'Сегодня — где люди живут: город и деревня, дома и квартиры.'),
    kartochki('Повторяем слова урока. Нажми на карточку — услышишь слово и увидишь перевод', SLOVA),
    propuski('Прочитай блог Лии про Великобританию и перетащи слова в пропуски',
             "Most British people live on a big __island__. There is sea all around Britain.\n"
             "Glasgow is the biggest __city__ in Scotland, but it's not as big as London.\n"
             "There are lots of farms in the __country__ in England. It's a very green place.\n"
             "Bibury is a very old English __village__. It's a lovely place to visit.\n"
             "Criccieth is a small __town__ by the sea in North Wales. It's very pretty.",
             mode='drag'),
    pary('Соедини описание с типом дома', [
        ('This house looks like the houses on its left and right; their walls touch.',
         'a terraced house'),
        ("It's a house; its walls don't touch other houses.", 'a detached house'),
        ("It's a big building with lots of homes in it.", 'a block of flats'),
        ("It's a small house in a village.", 'a cottage'),
        ("It's a house; one wall touches another house that looks the same.",
         'a semi-detached house'),
    ]),
    kviz('Прочитай разговор ребят про их дома и выбери правильное слово', [
        ('A: What ___ does Jeff live on?', ['floor', 'attic'], 0),
        ("B: The 5th, but there's a ___. We don't need to walk up there.", ['lift', 'stairs'], 0),
        ('A: Has his flat got a ___? B: Yes, so after school we can sit outside and look at the lake.',
         ['basement', 'balcony'], 1),
        ("C: Is this Kelly's house? D: Yes. Her bedroom is in the ___ at the top.",
         ['attic', 'lift'], 0),
        ('C: She has a lot of ___ to walk up and down!', ['balconies', 'stairs'], 1),
        ('D: And there is a gym in a room in the ___ under the house!', ['basement', 'floor'], 0),
        ("B: My mum's parents live ___ an island. I go there in the summer.", ['on', 'in'], 0),
        ('B: They live ___ a city.', ['on', 'in'], 1),
    ]),
    gruppy('Распредели слова по группам', [
        ('🏙 где люди живут', ['city', 'town', 'village', 'the country', 'island']),
        ('🏠 типы домов', ['cottage', 'detached house', 'semi-detached house',
                           'terraced house', 'flat']),
        ('🪜 части дома', ['3rd floor', 'attic', 'balcony', 'lift', 'stairs']),
    ]),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи, где ты живёшь: город это или деревня, какой у тебя дом или квартира, '
              'на каком этаже. Три-четыре предложения.</p>',
              'My cousin lives in a small cottage in a quiet village.'),
    poka(0, 'Готово! Теперь ты можешь рассказать про любой дом по-английски.'),
]

# ─────────────────── ДЗ 2 · 7.2 Present Continuous for future ───────────────────
SEJCHAS = 'сейчас, прямо в этот момент'
BUDUSHEE = 'договорённость на будущее'

hw2 = [
    privet(1, 'Unit 7 · Present Continuous для будущего',
           'Сегодня — как по-английски говорят о планах, о которых уже договорились.'),
    kviz('Прочитай предложение и реши: это происходит сейчас или это договорённость на будущее', [
        ("I'm coming to your house right now.", [SEJCHAS, BUDUSHEE], 0),
        ("I'm coming to your house this evening.", [SEJCHAS, BUDUSHEE], 1),
        ('Diana and I are going to the shops now.', [SEJCHAS, BUDUSHEE], 0),
        ('Diana and I are going shopping at 6 p.m.', [SEJCHAS, BUDUSHEE], 1),
        ("Mum's driving us home after school.", [SEJCHAS, BUDUSHEE], 1),
        ("Mum's driving us home. We aren't on the bus.", [SEJCHAS, BUDUSHEE], 0),
        ("She's going to the cinema with her friends tonight.", [SEJCHAS, BUDUSHEE], 1),
        ('Look! Bob and Dan are going home. Bye!', [SEJCHAS, BUDUSHEE], 0),
    ]),
    kviz('Выбери правильную форму', [
        ('Joe and I ___ making fish and chips tonight.', ['are', 'is', 'am'], 0),
        ('Jeff and his brothers ___ going on the school trip tomorrow.',
         ['am not', "aren't", "isn't"], 1),
        ("We aren't ___ house. We decided to stay in our old house.",
         ['move', 'moved', 'moving'], 2),
        ('___ meeting you here at five?', ['Is she', "She isn't", "She's"], 0),
        ('When ___ going on holiday?', ['you are', 'are you', "you're"], 1),
    ]),
    pary('Соедини начало и конец предложения', [
        ("Next week Dad's", 'getting a new car.'),
        ('My grandparents are visiting us', 'this weekend.'),
        ('When are', 'you changing school?'),
        ('Are we playing tennis', 'today or tomorrow?'),
        ('Mum is picking', 'me up in a minute.'),
    ]),
    predlozheniya('Сегодня воскресенье. Посмотри на ежедневник Поппи и составь предложения', [
        ('понедельник: go shopping with Mum',
         'Tomorrow Poppy is going shopping with Mum.'),
        ('вторник: meet George and Emma after school',
         'On Tuesday Poppy, Emma and George are meeting after school.'),
        ('среда: go to the chess club at 4 p.m.',
         'On Wednesday at 4 p.m. she is going to the chess club.'),
        ('четверг: do homework all evening',
         'On Thursday she is doing homework all evening.'),
        ('пятница: free! do nothing!',
         'At the end of the week she is doing nothing.'),
    ]),
    propuski('Впиши пропущенное слово: ✔ — утвердительное предложение, ✘ — отрицательное',
             "what you / eat for dinner tonight\n"
             "What __are__ you __eating__ for dinner tonight?\n"
             "✘ burgers: We __aren't__ eating burgers.\n"
             "✔ pizza: We __are__ eating pizza.\n"
             "when they / meet Jane this afternoon\n"
             "When __are__ they __meeting__ Jane this afternoon?\n"
             "✘ six o'clock: They __aren't__ meeting her at six o'clock.\n"
             "✔ five o'clock: They __are__ meeting her at five o'clock."),
    pismo('WRITING ✍️ Напиши правдивые предложения о себе',
          '<p>Используй Present Continuous для договорённостей. Там, где стоит ✔, предложение '
          'утвердительное, где ✘ — отрицательное.</p>'
          '<ol><li>Tomorrow I … ✔</li><li>Next week my parents … ✘</li>'
          '<li>Tonight my parents and I … ✔</li><li>At the weekend I … ✘</li></ol>'),
    poka(1, 'Отлично! Планы на неделю теперь можно описать по-английски.'),
]

# ─────────────────────── ДЗ 3 · 7.3 must, mustn't, can ───────────────────────
hw3 = [
    privet(2, "Unit 7 · must, mustn't, can",
           'Сегодня — правила: что нужно делать, чего нельзя и что можно.'),
    pary('Соедини предмет в доме с его описанием', [
        ('a bookcase', 'You keep your books on it.'),
        ('a cupboard', 'You keep cups and plates in it, behind doors.'),
        ('a drawer', 'You pull it out of a desk to get your things.'),
        ('a mirror', 'You look at your face in it.'),
        ('a sink', 'You wash the plates in it.'),
        ('a tap', 'You turn it on and water comes out.'),
    ]),
    propuski("Впиши в школьные правила must или mustn't",
             "You __must__ arrive five minutes before the first lesson.\n"
             "You __mustn't__ run in the classrooms.\n"
             "You __must__ be quiet during a test.\n"
             "You __mustn't__ give your homework to the teacher late.\n"
             "You __mustn't__ fall asleep in class!\n"
             "You __must__ put your hand up to ask a question!"),
    kviz("Выбери can, must или mustn't", [
        ("You've finished your chores, so you ___ watch TV now.", ['can', 'must', "mustn't"], 0),
        ('Turn off the tap. We ___ save water.', ['can', 'must', "mustn't"], 1),
        ('___ I borrow a book from your bookcase, please?', ['Can', 'Must', "Mustn't"], 0),
        ('The sink is dirty. I ___ clean it.', ['can', 'must', "mustn't"], 1),
        ('You ___ tidy your drawer. It is very messy.', ['can', 'must', "mustn't"], 1),
        ('Be careful with that mirror. You ___ break it.', ['can', 'must', "mustn't"], 2),
    ]),
    propuski('Прочитай указания доктора Кью и впиши по одному слову в каждый пропуск',
             "Dr Q: OK everyone, listen carefully. Today we __must__ get ready for Millie's "
             "surprise party. Here are my instructions. Pi, you __mustn't__ eat the nuts because "
             "they are for the party tonight. Rob, you __can__ choose the music - any songs you "
             "like. Remember, we __mustn't__ tell Millie about the party. It __must__ be a surprise.\n"
             "Pi: Ha, ha, ha ...\n"
             "Dr Q: What's the matter? Why are you laughing? You __mustn't__ laugh at me. It's rude!\n"
             "Rob: Turn around. Millie is standing behind you ... and listening carefully too!"),
    pismo('WRITING ✍️ Напиши семейные правила про компьютер',
          '<p>Напиши пять правил. Первые три — по подсказкам, ещё два придумай сам.</p>'
          '<ol><li><b>must</b> — you / use the computer after ___ p.m.</li>'
          "<li><b>mustn't</b> — you / chat online with your friends for ___ hour(s)</li>"
          '<li><b>can</b> — parents / know your password</li>'
          '<li>своё правило</li><li>ещё одно своё правило</li></ol>'),
    poka(2, 'Хорошо! Правила по-английски теперь не проблема.'),
]

# ─────────────────────── ДЗ 4 · 7.4 Communication ───────────────────────
hw4 = [
    privet(0, 'Unit 7 · Приглашения',
           'Сегодня — как позвать друга, как согласиться и как вежливо отказаться.'),
    pary('Соедини начало и конец фразы', [
        ('Are you', 'free next weekend?'),
        ('Do you', 'want to come to my house?'),
        ('That', 'sounds great.'),
        ("Yes, I'd love", 'to.'),
        ("I'm", "sorry, I can't come."),
        ('Sorry,', 'maybe next time.'),
    ]),
    kviz('Прочитай реплику и выбери подходящий ответ', [
        ('A: Would you like to hang out tomorrow? B: ___',
         ["I'm sorry, you can't come.", "Yes, I'd love to.", 'Thanks.'], 1),
        ("A: I'm going shopping. Can you come? B: ___",
         ["I mustn't come.", "Sorry, I don't come.", "I'm sorry, I can't come. I'm busy."], 2),
        ('A: Do you want to go to the zoo on Saturday? B: ___',
         ['Sorry, maybe next time.', 'I love spiders.', 'Thank you.'], 0),
        ("B: I'd love to! Какой была реплика A?",
         ['Do you like going to the cinema?', 'Do you want to come to the cinema?',
          'Do you often go to the cinema?'], 1),
    ]),
    propuski('Прочитай разговор Фрэн и Стэна и впиши пропущенные слова',
             "Fran: Hello, Stan. It's Fran. I've got two cinema tickets. Would you like to go?\n"
             "Stan: I'd __love__ __to__. What time?\n"
             "Fran: Eight o'clock.\n"
             "Stan: Do __you__ __want__ __to__ go to the cinema in my car?\n"
             "Fran: That __sounds__ __great__! Thank you. See you later!"),
    posledovatelnost('Расставь реплики разговора по порядку', [
        'Vicky: Hello, Micky. Are you free this afternoon?',
        "Vicky: I've got a new football. Would you like to play in the park?",
        "Micky: I'd love to. What time?",
        "Vicky: At five o'clock.",
        'Micky: Can we meet at the park now?',
        'Vicky: Great! See you at five.',
    ]),
    pismo('WRITING ✍️ Напиши разговор-приглашение',
          '<p>Вики звонит Мики: у неё новый мяч, и она зовёт его играть в футбол в парке '
          'в пять часов. Мики соглашается.</p>'
          '<p>Напиши их разговор из шести-восьми реплик. Слова-помощники: '
          "<b>a new ball, great, football, o'clock, park</b>. "
          'Образцом возьми разговор Фрэн и Стэна из задания выше.</p>'),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Позови друга куда-нибудь на выходных: скажи, куда и во сколько. '
              'Потом откажись от его приглашения и объясни почему. Четыре-пять предложений.</p>',
              'Are you free on Saturday? Would you like to come to the swimming pool with me?'),
    poka(3, 'Отлично! Теперь ты знаешь, как приглашать и как отвечать на приглашение.'),
]

# ─────────────────────── ДЗ 5 · 7.5 Reading ───────────────────────
BLOG = (
    '<h3>Green and clean neighbourhood blog <span style="color:#888">by Trevor</span></h3>'
    '<p>My friends live in different parts of the UK. Check out their posts on my '
    'neighbourhood blog.</p>'
    '<p><b>Hugh</b><br>I live in a small cottage in a quiet village. There are lots of flowers '
    'in our garden. When we peel vegetables and fruit, we keep the skins. After some time, the '
    'skins go brown and we can use them in the garden! They are good for the plants - they make '
    'them grow healthier and stronger.</p>'
    '<p><b>Carly</b><br>I live on the 4th floor of a block of flats. When we moved here, there '
    'was only a dirty car park next to the building. One day the families here decided to grow '
    'grass and trees behind the building. Now we also regularly clean up the car park to keep '
    'the neighbourhood nice and green.</p>'
    "<p><b>Zach</b><br>I live in a city. I'd like to live in a big detached house like "
    'Trevor, but they are too expensive! My street has terraced houses and our houses are all '
    'different colours! Last year everyone in my street decided to paint their houses because '
    'we wanted to live in a nicer and cleaner neighbourhood. There is a white house, a '
    '‘coffee cream’ house, a red and white house and my house!</p>'
)

hw5 = [
    privet(1, 'Unit 7 · Reading',
           'Сегодня читаем блог Тревора о том, где живут его друзья.'),
    kviz('Выбери пропущенное слово', [
        ('How can I find ___ what a word means?', ['out', 'up', 'for'], 0),
        ("Let's check ___ the film times on the cinema website.", ['up', 'out', 'for'], 1),
        ('We must clean ___ after the party. The house is messy.', ['up', 'out', 'for'], 0),
        ('I can help you look ___ your car keys.', ['for', 'up', 'out'], 0),
        ("I usually wake ___ at seven o'clock in the morning.", ['up', 'out', 'for'], 0),
    ]),
    tekst(BLOG),
    pary('Прочитай блог и соедини человека с его домом', [
        ('Hugh', 'a small cottage in a quiet village'),
        ('Carly', 'a flat on the 4th floor of a block of flats'),
        ('Zach', 'a terraced house in a city street'),
        ('Trevor', 'a big detached house'),
    ], material=BLOG),
    kviz('Прочитай блог ещё раз и выбери правильный ответ', [
        ('Who lives in a village?', ['Hugh', 'Carly', 'Zach'], 0),
        ('Who would like to live in a detached house?', ['Hugh', 'Carly', 'Zach'], 2),
        ("What was next to Carly's block of flats when she moved there?",
         ['a dirty car park', 'a green park', 'a small school'], 0),
        ('Who lives in a street with different colour houses?', ['Hugh', 'Carly', 'Zach'], 2),
        ('What does Hugh use in his garden to make the plants healthier?',
         ['the skins of vegetables and fruit', 'water from the river', 'flowers from the shop'], 0),
        ("Why did the people in Carly's building grow grass and trees?",
         ['to keep the neighbourhood nice and green', 'to sell the flowers',
          'because the car park was too small'], 0),
    ], material=BLOG),
    pismo('WRITING ✍️ Ответь на вопросы о себе',
          '<p>Ответь письменно, по два-три предложения на каждый вопрос.</p>'
          '<ol><li>What type of house do you live in?</li>'
          '<li>Is your neighbourhood nice? Why?</li>'
          '<li>What can you do to make your neighbourhood nicer?</li></ol>'),
    poka(4, 'Здорово! Блог прочитан, про свой район рассказано.'),
]

# ─────────────────── ДЗ 6 · 7.6 Listening and Writing ───────────────────
hw6 = [
    privet(2, 'Unit 7 · Listening and Writing',
           'Сегодня слушаем рассказ Чарли про его дом и пишем приглашение.'),
    pary('Соедини часть дома с её описанием', [
        ('a balcony', 'You can stand outside here and look at the garden.'),
        ('the basement', 'This room is under the house, below the ground.'),
        ('the ground floor', 'This floor is at the same level as the garden.'),
        ('the 1st floor', 'In Britain this is the floor above the ground floor.'),
        ('the 2nd floor', 'This floor is above the 1st floor.'),
        ('the stairs', 'You walk up and down these when there is no lift.'),
    ]),
    ('quiz', {'title': 'LISTENING 🎧 Послушай рассказ Чарли и выбери, кто где живёт',
              'audio': TRACK18, 'skill': 'listening',
              'questions': [
                  {'q': "Charlie's uncle lives ...", 'type': 'single', 'correct': [0],
                   'options': [{'text': 'in a small flat'}, {'text': 'on the top floor'},
                               {'text': 'next door to each other'},
                               {'text': 'on the ground floor'}]},
                  {'q': 'Charlie and Amin live ...', 'type': 'single', 'correct': [2],
                   'options': [{'text': 'in a small flat'}, {'text': 'on the top floor'},
                               {'text': 'next door to each other'},
                               {'text': 'on the ground floor'}]},
                  {'q': "Amin's grandparents live ...", 'type': 'single', 'correct': [3],
                   'options': [{'text': 'in a small flat'}, {'text': 'on the top floor'},
                               {'text': 'next door to each other'},
                               {'text': 'on the ground floor'}]},
                  {'q': 'Mary lives ...', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'in a small flat'}, {'text': 'on the top floor'},
                               {'text': 'next door to each other'},
                               {'text': 'on the ground floor'}]},
                  {'q': 'Where does the uncle keep his bike?', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'on his balcony'}, {'text': 'in the basement'},
                               {'text': 'in the garden'}]},
              ]}),
    ('gaps', {'title': 'LISTENING 🎧 Послушай рассказ ещё раз и впиши по одному слову',
              'audio': TRACK18, 'mode': 'type',
              'text': "Charlie's uncle's flat is small but __cool__.\n"
                      "The __lift__ doesn't go down to the basement.\n"
                      "Amin is Charlie's best __friend__.\n"
                      "The __doors__ of Charlie and Amin's flats are always open.\n"
                      "Amin's grandma makes them __pancakes__ when they clean up for her.\n"
                      "They're having a Mother's Day party on __Sunday__."}),
    vpisat('В приглашении Салли восемь ошибок. Прочитай строку и напиши слово правильно', [
        ('Woud you like to have lunch at my house with my family?', ['Would', 'would']),
        ('We having a picnic in the garden.', ["We're", 'We are', "we're"]),
        ('Its a great way to meet old and new neighbours.', ["It's", "it's"]),
        ('Lots of my friends from the neihbourhood are coming.',
         ['neighbourhood', 'Neighbourhood']),
        ("Can you come at about eleven oclock?", ["o'clock", "O'clock"]),
        ('Dad says we can play table tenis in the garage.', ['tennis', 'Tennis']),
    ]),
    pismo('WRITING ✍️ Напиши другу письмо-приглашение',
          '<p>Сначала выбери, о чём будешь писать:</p>'
          '<ul><li><b>Day:</b> Friday / Saturday / Sunday</li>'
          '<li><b>Activity 1:</b> the cinema / shopping / football</li>'
          "<li><b>Time:</b> eleven o'clock / 2 p.m. / five o'clock</li>"
          '<li><b>Activity 2:</b> a picnic / computer games / burgers</li>'
          '<li><b>Useful verbs:</b> do / get / go / hang out / like / make / meet / play / want</li></ul>'
          '<p>Теперь напиши письмо на 60–80 слов. Начни так: <i>Hi Marek, What are you '
          'doing next ...?</i> Перечитай письмо и проверь орфографию и знаки препинания.</p>'),
    poka(5, 'Отлично! И рассказ послушали, и приглашение написали.'),
]

# ─────────────────────── ДЗ 7 · 7.7 Check yourself ───────────────────────
hw7 = [
    privet(0, 'Unit 7 · Check yourself!', 'Повторяем весь юнит перед тестом.'),
    ('gaps', {'title': 'Прочитай рассказ про Сандру и выбери правильное слово',
              'mode': 'choice',
              'text': "Sandra lives in a __cottage__. It's in a pretty __village__ in the country. "
                      "Every day she wakes up and she looks in the __mirror__ in the bathroom and "
                      "she brushes her teeth. Then she goes to the kitchen and she gets a mug from "
                      "the __cupboard__, so she can make tea. She likes sitting on the __stairs__ "
                      "to drink her morning tea because her cat sits there. She is a tidy girl, so "
                      "she always __cleans up__ after her tea.",
              'choices': [['detached house'], ['city'], ['tap'], ['sink'], ['basement'],
                          ['finds out']]}),
    pary('Соедини начало и конец предложения', [
        ('David lives in a block', 'of flats.'),
        ('My flat is on the ground', 'floor.'),
        ('Grandpa lives in a terraced', 'house.'),
        ('Life in the city is', 'often noisy.'),
        ("I'd like to live on", 'an island.'),
        ('You can use the lift to', 'go to the 2nd floor.'),
    ]),
    propuski('Впиши глагол в Present Continuous — речь о договорённостях на будущее',
             "We __are moving__ (move) to a new house next week.\n"
             "Dave __is meeting__ (meet) us at seven o'clock at my house.\n"
             "Hurry up! We __are leaving__ (leave) in five minutes!\n"
             "__What is Fred doing__ (what / Fred do) tomorrow?\n"
             "__Are you watching__ (you / watch) anything good on TV tonight?\n"
             "Mandy __isn't running__ (not run) in the race on Saturday. She's sick."),
    kviz("Выбери can, must или mustn't", [
        ('We ___ hurry up. The train is leaving in a moment.', ['can', 'must', "mustn't"], 1),
        ('You ___ watch TV after you do your homework.', ['can', 'must', "mustn't"], 0),
        ("Stop! You ___ cross the road here. It's not safe.", ['can', 'must', "mustn't"], 2),
        ('Your bedroom is messy. You ___ tidy it this weekend.', ['can', 'must', "mustn't"], 1),
        ("It's raining. We ___ take an umbrella.", ['can', 'must', "mustn't"], 1),
        ("We ___ play football in the garden. Dad says it's OK.", ['can', 'must', "mustn't"], 0),
    ]),
    kviz('Прочитай разговоры и выбери правильный вариант', [
        ('A: ___ like to come to my house on Sunday?', ['Would you', 'You would'], 0),
        ('B: ___ to. Can I come with Jiggs, my dog?', ['I love', "I'd love"], 1),
        ('A: ___ you want to see the match with me this afternoon?', ['Do', 'Would'], 0),
        ("B: ___ sorry I can't see it. I'm busy this afternoon.", ['I', "I'm"], 1),
        ('A: Are you free tomorrow? Would you ___ to go to the country?', ['like', 'want'], 0),
        ('B: Sorry. Maybe ___ time.', ['next', 'this'], 0),
    ]),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Позови друга в гости на выходных: скажи, где ты живёшь, какой у тебя дом '
              'и что вы будете делать. Четыре-пять предложений.</p>',
              'I live in a flat on the third floor of a block of flats.'),
    poka(1, 'Юнит пройден! Можно браться за тест.'),
]

UROKI = [('Homework 1', hw1), ('Homework 2', hw2), ('Homework 3', hw3), ('Homework 4', hw4),
         ('Homework 5', hw5), ('Homework 6', hw6), ('Homework 7', hw7)]

if __name__ == '__main__':
    put = sys.argv[1] if len(sys.argv) > 1 else 'builds/gg3/wb/u7/u7.sql'
    out = ['-- Go Getter 3, юнит 7 «Where I live» по рабочей тетради: домашки 1–7 (черновики)',
           f"update classroom_lessons set sort_order = 10 where id = '{TEST}';"]
    for i, (nazv, bloki) in enumerate(UROKI):
        out.append(sql_uroka(UNIT, nazv, i, bloki))
    io.open(put, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(put, sum(len(b) for _, b in UROKI), 'блоков,', os.path.getsize(put) // 1024, 'КБ')
