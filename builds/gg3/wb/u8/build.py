# -*- coding: utf-8 -*-
"""Go Getter 3, юнит 8 «A happy life» по рабочей тетради (стр. 68–74).

Ключи 8.7 — Answer key тетради (стр. 95); ключи аудирования 8.6 — по расшифровке
трека A20: Фрэнк и Зена спорят о будущем — электронные книги вместо бумажных,
жара и снег у белых медведей, электромобили, сады и площадки у домов,
трёхдневная рабочая неделя.

Задания тетради, державшиеся на фотографиях (8.1 упр. 2 про семью Гэри,
8.2 упр. 2 с картинками предсказаний, 8.4 упр. 3 с фотографиями), переписаны
в текстовые: сами предложения дают весь нужный контекст.
"""
import io, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import (AUDIO, privet, poka, kartochki, kviz, pary, propuski, gruppy,
                    predlozheniya, vpisat, govorenie, pismo, tekst, sql_uroka)

UNIT = '028f1e92-6608-40c6-befc-4395319ab6ea'   # Unit 8 · A happy life
TEST = 'e77318f0-9a9f-4c41-a86a-b7df375ec266'
TRACK20 = AUDIO + 'GG%20L3%20WkBk%20A20.mp3'

# ─────────────────────── ДЗ 1 · 8.1 Vocabulary ───────────────────────
SLOVA = [
    ('be rich', 'быть богатым'), ('be famous', 'быть знаменитым'),
    ('be a doctor', 'быть врачом'), ('be an astronaut', 'быть космонавтом'),
    ('have my own business', 'иметь своё дело'),
    ('have an interesting job', 'иметь интересную работу'),
    ('have a big family', 'иметь большую семью'),
    ('have good health', 'быть здоровым'),
    ('learn a foreign language', 'выучить иностранный язык'),
    ('learn to drive', 'научиться водить машину'),
    ('live abroad', 'жить за границей'), ('live on my own', 'жить самостоятельно'),
    ('ambition', 'мечта, цель в жизни'),
]

hw1 = [
    privet(0, 'Unit 8 · A happy life',
           'Сегодня — о планах на жизнь: кем быть, что иметь, чему научиться и где жить.'),
    kartochki('Повторяем слова урока. Нажми на карточку — услышишь слово и увидишь перевод', SLOVA),
    pary('Соедини начало и конец предложения — получатся мечты Гэри', [
        ('I want to be', 'rich.'),
        ("I'd like to have my", 'own business.'),
        ("I don't want to live on", 'my own.'),
        ('I want to learn to', "drive when I'm 18."),
        ("I'd love to have", 'a big family.'),
    ]),
    gruppy('Распредели мечты по глаголам', [
        ('be …', ['rich', 'famous', 'a doctor']),
        ('have …', ['my own business', 'an interesting job', 'a big family']),
        ('learn …', ['a foreign language', 'to drive']),
        ('live …', ['abroad', 'on my own']),
    ]),
    propuski('Прочитай про семью Гэри и перетащи слова в пропуски',
             "When Gary's mum, Karen, was seventeen, she wanted to be __famous__ "
             "and sing in a band.\n"
             "When his dad, Steve, was at school, he wanted to leave England one day and to live "
             "__abroad__. He went to the USA.\n"
             "His little brother, Kenny, would like to be a __doctor__. He practises on his toys.\n"
             "Gary's sister, Tracy, wants to have an __interesting job__. "
             "She'd love to be an astronaut.\n"
             "Finally, his cousin, Nadia, would like to learn a __foreign language__, "
             "but she can't decide which to choose.", mode='drag'),
    propuski('Прочитай историю про клоуна Фреда и впиши по одному слову',
             "When Funny Fred left school, he wanted to __be__ a clown and to have his __own__ "
             "business. He decided to leave the UK and to live __abroad__ – he moved to the USA. "
             "What did he do there? He went to circus school to __learn__ about acrobatics and "
             "magic tricks. He also learned to play __the__ drums. When he finished school, "
             "he learned two __foreign__ languages – French and Italian. Then he opened his own "
             "circus schools in the UK, France and Italy. Now he has a big business. "
             "Funny Fred often visits children's hospitals too. He wears his clown clothes "
             "because he wants the children to __have__ fun and get better quickly!"),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи о своих планах на будущее: кем ты хочешь стать, что хотел бы иметь, '
              'чему научиться и где жить. Четыре-пять предложений.</p>',
              'I want to learn to drive.'),
    poka(0, 'Готово. Теперь ты можешь рассказать о своих планах по-английски.'),
]

# ─────────────────────── ДЗ 2 · 8.2 will для предсказаний ───────────────────────
hw2 = [
    privet(1, 'Unit 8 · will — предсказания',
           'Сегодня — как говорить о будущем: will и won’t.'),
    pary('Соедини факт с предсказанием', [
        ('I love music.', "I'll be a famous musician one day."),
        ('We are mad about bikes.', "We'll ride around Europe one day."),
        ('Maggie likes the city.', "She'll live in her own flat in the centre one day."),
        ('Bob and Sam can cook very well.', "They'll open a restaurant one day."),
    ]),
    kviz('Прочитай предсказания Эммы и выбери правильную форму', [
        ("I love going abroad, so when I'm older, I ___ travel a lot.", ["'ll", "won't"], 0),
        ('I only speak English and a bit of German, so I think I ___ learn another foreign language.',
         ['will', "won't"], 0),
        ('My dream is to visit the Amazon rainforest. My cousin George says he hopes that he ___ '
         'go there with me.', ['will', "won't"], 0),
        ("But I don't like spiders, so maybe I ___ go to the Amazon!", ['will', "won't"], 1),
        ('I actually think George ___ travel with me …', ['will', "won't"], 1),
        ('… because he ___ prefer to play computer games every day with Harry!',
         ['will', "won't"], 0),
    ]),
    predlozheniya('Составь предсказания о будущем этих ребят', [
        ('Мария отлично играет в футбол', 'Maria will play football for England.'),
        ('Таня учит французский и любит объяснять', 'Tanya will be a French teacher.'),
        ('Гэри возится с собаками и кошками', 'Gary will be a vet.'),
        ('Дениз мечтает о домике за городом', 'Denise will buy a cottage.'),
        ('Марку скоро восемнадцать', 'Mark will learn to drive a car.'),
    ]),
    predlozheniya('Составь вопросы о будущем', [
        ('Дональд поедет в Китай?', 'Will Donald visit China?'),
        ('Грег и Тони выиграют много денег?', 'Will Greg and Tony win lots of money?'),
        ('я стану прекрасным певцом?', 'Will I be an amazing singer?'),
        ('мы все будем счастливы?', 'Will we all be happy?'),
    ]),
    propuski('Впиши короткий ответ: ✔ — да, ✘ — нет',
             "Will Susan be famous? ✔ Yes, __she will__.\n"
             "Will Donald visit China? ✘ No, __he won't__.\n"
             "Will Greg and Tony win lots of money? ✘ No, __they won't__.\n"
             "Will I be an amazing singer? ✔ Yes, __you will__.\n"
             "Will we all be happy? ✔ Yes, __we will__."),
    pismo('WRITING ✍️ Напиши о своём будущем',
          '<p>Составь из слов два вопроса и ответь на них правдиво.</p>'
          '<ol><li>be / will / What / you / ?</li><li>live / will / you / Where / ?</li></ol>'
          '<p>Потом добавь ещё три своих предсказания с <b>will</b> и <b>won’t</b>.</p>'),
    poka(1, 'Будущее время разобрано: will — будет, won’t — не будет.'),
]

# ─────────────────────── ДЗ 3 · 8.3 Вопросы и вопросительные слова ───────────────────────
hw3 = [
    privet(2, 'Unit 8 · Вопросы и вопросительные слова',
           'Сегодня — как спросить про что угодно: What, Where, When, Who, Why, How often.'),
    pary('Соедини начало и конец предложения — получится история про доктора Кью', [
        ('Doctor Q invited his', 'mum to stay.'),
        ('Doctor Q called her', 'on the phone.'),
        ('Mrs Q visited him', 'two days later.'),
        ("Mrs Q didn't want to shake", 'hands.'),
        ('Mrs Q gave everyone', 'a hug.'),
        ("Pi didn't", 'kiss her.'),
    ]),
    propuski('Прочитай разговор миссис Кью с сыном и перетащи слова в пропуски',
             "Mrs Q: __How often__ do you exercise, Cornelius?\n"
             "Dr Q: Not very often, Mum.\n"
             "Mrs Q: __What__ time did you get up?\n"
             "Dr Q: At 5.30, Mum!\n"
             "Mrs Q: __Why__ are you tired?\n"
             "Dr Q: Because we went for a long run in the morning!\n"
             "Mrs Q: __Where__ are we going after lunch?\n"
             "Dr Q: To my lab!\n"
             "Mrs Q: __Who__ are you calling?\n"
             "Dr Q: I'm calling Dr Spark. He's my friend. He's visiting me today.\n"
             "Mrs Q: __When__ is he visiting?\n"
             "Dr Q: At four o'clock.", mode='drag'),
    kviz('Прочитай ответ и выбери вопрос, который к нему подходит', [
        ('B: EMILY invited us to stay.',
         ['Who invited us to stay?', 'Who did we invite to stay?'], 0),
        ('B: Poppy visited GEORGE yesterday.',
         ['Who visited Poppy yesterday?', 'Who did Poppy visit yesterday?'], 1),
        ('B: FRED saw them at the park.',
         ['Who saw them at the park?', 'Who did they see at the park?'], 0),
        ('B: Grandma kissed SOPHIE.',
         ['Who kissed Grandma?', 'Who did Grandma kiss?'], 1),
    ]),
    predlozheniya('Составь вопрос к ответу', [
        ('B: I want to play football.', 'What do you want to do?'),
        ("B: I'm calling my grandma.", 'Who are you calling?'),
        ('B: They arrived two hours ago.', 'When did they arrive?'),
        ("B: I'll live in Berlin.", 'Where will you live?'),
    ]),
    propuski('Прочитай разговор Кейт и Сьюзи и впиши по одному слову',
             "Kate: This is great ice cream. Who __brought__ it?\n"
             "Susie: My aunt brought it. She's staying here for the weekend.\n"
             "Kate: How __often__ __does__ she visit you?\n"
             "Susie: Every holiday. She's a teacher.\n"
             "Kate: __What__ does she __teach__?\n"
             "Susie: She teaches Music. I'm going to stay at her house in the summer.\n"
             "Kate: __Where__ does __she__ live?\n"
             "Susie: In Scotland. You should come to visit too! __When__ __are__ you going on "
             "holiday with your parents? We can visit her before your holiday.\n"
             "Kate: We're going in August, so I'm free in July.\n"
             "Aunt: Hi there, Susie. __Who__ __did__ you invite to stay at my house?\n"
             "Susie: Oh, hi, Aunt Maria. This is Kate. I invited her, she's my best friend."),
    govorenie('SPEAKING 🎤 Задай вопросы и запиши ответ',
              '<p>Представь, что в класс пришёл новый ученик. Задай ему пять вопросов с разными '
              'словами: What, Where, When, Who, How often.</p>',
              'How often do you play computer games?'),
    poka(2, 'Вопросы разобраны: и обычные, и те, где спрашивают про подлежащее.'),
]

# ─────────────────────── ДЗ 4 · 8.4 Communication ───────────────────────
hw4 = [
    privet(0, 'Unit 8 · Согласие и несогласие',
           'Сегодня — как сказать по-английски «я согласен» и «я так не думаю».'),
    gruppy('Распредели фразы на согласие и несогласие', [
        ('✅ согласие', ['I agree with you.', "You're right.", "That's true.",
                        "That's what I think too."]),
        ('❌ несогласие', ['I disagree with you.', "You're wrong.", "That's not true.",
                          "I don't think so."]),
    ]),
    kviz('Прочитай реплику и выбери подходящий ответ', [
        ('A: Everybody likes summer holidays.',
         ["That's true. It's a brilliant idea.", 'I agree. She likes them.',
          "You're right. They're fun."], 2),
        ('A: History is boring.',
         ["No, that isn't right. We have Maths now.",
          "I disagree with you. I think it's interesting.",
          "I don't think so. He's clever."], 1),
        ('A: The violin is a difficult instrument to play.',
         ["That's true. The piano is easier.", "That isn't true. It's difficult.",
          "That's what I think. It's amazing."], 0),
    ]),
    propuski('Прочитай разговор Ника с папой и перетащи слова в пропуски',
             "Dad: OK, the carpet is clean now. Good job, Nick. Are you tired?\n"
             "Nick: No, I'm not tired, I'm bored. Chores are boring!\n"
             "Dad: I agree __with__ you. Let's go shopping. All kids like shopping.\n"
             "Nick: That's not __true__. I hate shopping. Shopping is boring too.\n"
             "Dad: I __don't__ agree with you. It was fun at the tech shop last week.\n"
             "Nick: You're __right__. That's an amazing shop.\n"
             "Dad: That's __what__ I think too.\n"
             "Nick: Let's go by bus. It's quicker than the tram.\n"
             "Dad: I don't think __so__. The bus is really slow!\n"
             "Nick: OK. I'll be ready in five minutes.", mode='drag'),
    propuski('Впиши по одному слову в ответы',
             "A: Everybody loves pizza.\n"
             "B: I __agree__! I often have pizza because it's tasty.\n"
             "A: Everybody hates tests.\n"
             "B: __You're__ __right__. I don't like them because they're sometimes difficult.\n"
             "A: Girls don't want to be pilots.\n"
             "B: I disagree __with__ __you__. Girls want to be pilots because it's an exciting job.\n"
             "A: Kids don't like climbing.\n"
             "B: __That's__ not __true__. They love climbing because it's fun."),
    pismo('WRITING ✍️ Напиши своё мнение',
          '<p>Напиши, согласен ты или нет с каждым утверждением, и объясни почему — '
          'с союзом <b>because</b>.</p>'
          '<ol><li>Everybody loves pizza.</li><li>Everybody hates tests.</li>'
          "<li>Girls don't want to be pilots.</li><li>Kids don't like climbing.</li></ol>"),
    govorenie('SPEAKING 🎤 Ответь вслух и запиши ответ',
              '<p>Друг говорит тебе четыре фразы. Согласись с двумя и не согласись с двумя, '
              'каждый раз объясняя почему.</p>'
              '<ol><li>School starts too early.</li><li>Winter is better than summer.</li>'
              '<li>Homework is useful.</li><li>Films are better than books.</li></ol>',
              "I don't think so."),
    poka(3, 'Спорить по-английски вежливо — тоже навык.'),
]

# ─────────────────────── ДЗ 5 · 8.5 Reading ───────────────────────
RASSKAZ = (
    '<h3>A short story competition! <span style="color:#888">by Paula Maple, Class B</span></h3>'
    "<p>Fay was a polite girl. She waited her turn, she asked for permission to do things and "
    "she was never late.</p>"
    "<p>One summer, Fay's cousin, Julie, was visiting her. Julie lived abroad and this was her "
    "first trip to England in five years.</p>"
    "<p>On the first day of the visit, Fay got up at eight o'clock. She waited for Julie to get up. "
    "They wanted to meet their grandparents for lunch at one o'clock. But Julie got up at "
    "12.45 p.m. They were late for lunch.</p>"
    "<p>'Sorry,' Fay said to her grandma. 'Julie got up late.'</p>"
    "<p>'Maybe she's tired from the trip,' said Grandma.</p>"
    "<p>At home, Julie took Fay's MP3 player. She didn't ask for permission. She didn't wait her "
    "turn when they were playing computer games. And then she didn't come to dinner on time.</p>"
    "<p>'Listen Julie. I want to …' Fay started to say.</p>"
    "<p>'Be quiet. I'm watching TV,' said Julie.</p>"
    "<p>'Listen Julie!' said Fay. 'In my house we are polite, we aren't late, we don't interrupt, "
    "we don't take people's things and we wait our turn. In my family we have good manners!'</p>"
    "<p>Julie was very surprised. For the rest of the visit, Julie was very polite.</p>"
)

hw5 = [
    privet(1, 'Unit 8 · Reading',
           'Сегодня читаем рассказ-победитель школьного конкурса — про вежливость.'),
    tekst(RASSKAZ),
    propuski('Перетащи слова в пропуски: interrupt · late · permission · polite · time · turn',
             "I hope Larry arrives on __time__. The train will be here soon.\n"
             "Don't __interrupt__ when your mum is speaking.\n"
             "Please don't be __late__ for the film. It starts at 7 p.m.\n"
             "'I want to play now.' 'You have to wait your __turn__!'\n"
             "You must ask for __permission__ to leave the classroom.\n"
             "It's important for shop assistants to be __polite__ and helpful.", mode='drag'),
    kviz('Прочитай объявление о конкурсе и выбери правильное слово', [
        ('___ you think good manners are important?', ['Do', 'Are'], 0),
        ('___ you got great imagination?', ['Have', 'Do'], 0),
        ('___ you good at writing?', ['Do', 'Are'], 1),
        ('___ you draw pictures?', ['Can', 'Are'], 0),
    ]),
    kviz('Прочитай рассказ и выбери правильный ответ', [
        ('Какой заголовок подходит рассказу лучше всего?',
         ['Late for lunch', 'Good family', 'Cousin problems'], 2),
        ('Where did Julie live?', ['abroad', 'in England', 'in the same town as Fay'], 0),
        ('What time did Fay get up on the first day?',
         ["at eight o'clock", 'at 12.45 p.m.', "at one o'clock"], 0),
        ('What did Julie take from Fay?',
         ['her MP3 player', 'her computer game', 'her phone'], 0),
        ('Why did Julie tell Fay to be quiet?',
         ['Because she was watching TV.', 'Because she was sleeping.',
          'Because she was having dinner.'], 0),
        ("What does Fay's family have?",
         ['good manners', 'a big house', 'lots of money'], 0),
    ], material=RASSKAZ),
    propuski('Прочитай рассказ ещё раз и впиши по одному слову',
             "Fay was a __polite__ girl.\n"
             "She __waited__ her turn.\n"
             "She asked for __permission__ to do things.\n"
             "She was never __late__.\n"
             "Julie and Fay were late for __lunch__ with their grandparents.\n"
             "Julie __didn't__ wait her turn when they were playing video games.\n"
             "Julie didn't arrive on time for __dinner__.\n"
             "After Fay spoke to her, Julie was __polite__ for the rest of the visit.",
             material=RASSKAZ),
    pismo('WRITING ✍️ Напиши свой короткий рассказ на конкурс',
          '<p>Тема конкурса — почему быть вежливым это хорошая мысль. Напиши рассказ из '
          'шести-восьми предложений в прошедшем времени.</p>'
          '<p>Слова-помощники: polite, interrupt, wait your turn, ask for permission, late, '
          'good manners.</p>'),
    poka(4, 'Рассказ прочитан, свой написан.'),
]

# ─────────────────────── ДЗ 6 · 8.6 Listening and Writing ───────────────────────
ESSE = (
    '<h3>Houses in the future <span style="color:#888">by Tony Watson</span></h3>'
    "<p>I'm sure houses in fifty years from now will be different. Some people think we will all "
    "live in blocks of flats in cities, but I don't think this will happen. I think lots of people "
    "will move to the country. Maybe there will be faster trains from the villages that people "
    "will take to go to work in the cities. Houses will be detached or semi-detached. I hope more "
    "people will grow fruit and vegetables in their gardens to help nature. I think people will go "
    "hiking and ride their bikes more to spend time close to nature.</p>"
)

hw6 = [
    privet(2, 'Unit 8 · Listening and Writing',
           'Сегодня слушаем спор о будущем и пишем своё сочинение.'),
    predlozheniya('Составь предсказания о будущем мира', [
        ('все будут читать электронные книги', 'We will all read e-books.'),
        ('погода станет жарче', 'The weather will be hotter.'),
        ('машины станут чище для природы', 'Cars will be cleaner for the environment.'),
        ('выходные будут с четверга по воскресенье',
         'The weekend will be from Thursday to Sunday.'),
    ]),
    ('quiz', {'title': 'LISTENING 🎧 Послушай разговор Фрэнка и Зены и выбери правильный ответ',
              'audio': TRACK20, 'skill': 'listening',
              'questions': [
                  {'q': '___ books will be on tablets.', 'type': 'single', 'correct': [0],
                   'options': [{'text': 'School'}, {'text': 'All'}]},
                  {'q': 'Animals will have problems because of the ___.',
                   'type': 'single', 'correct': [0],
                   'options': [{'text': 'weather'}, {'text': 'people'}]},
                  {'q': 'There will be ___ snow where the polar bears live.',
                   'type': 'single', 'correct': [1],
                   'options': [{'text': 'more'}, {'text': 'no'}]},
                  {'q': 'Cars ___ work with electricity.', 'type': 'single', 'correct': [1],
                   'options': [{'text': "won't"}, {'text': 'will'}]},
                  {'q': 'There will be more ___ for kids.', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'gardens'}, {'text': 'playgrounds'}]},
                  {'q': "We'll work ___ days a week.", 'type': 'single', 'correct': [1],
                   'options': [{'text': 'four'}, {'text': 'three'}]},
              ]}),
    ('gaps', {'title': 'LISTENING 🎧 Послушай разговор ещё раз и впиши по одному слову',
              'audio': TRACK20, 'skill': 'listening', 'mode': 'type',
              'text': "We won't have books anymore. We will all read __e-books__. "
                      "Our school books will be on __tablets__.\n"
                      "I think the weather will be __hotter__ and there won't be any __snow__ "
                      "where the polar bears live.\n"
                      "I think the environment will be __cleaner__ because most cars will work "
                      "with __electricity__.\n"
                      "There will be nice __gardens__ next to the flats and more playgrounds "
                      "for kids.\n"
                      "I think we will work __three__ days a week. "
                      "The weekend will be from __Thursday__ to Sunday."}),
    kviz('Прочитай сочинение Тони о домах будущего и выбери правильный вариант', [
        ("I'm ___ houses in fifty years from now will be different.", ['sure', 'think'], 0),
        ('Some people think we will all live in blocks of flats in cities, '
         'but I ___ think this will happen.', ["don't", "won't"], 0),
        ('I ___ lots of people will move to the country.', ['sure', 'think'], 1),
        ('___ there will be faster trains from the villages.', ['Maybe', 'Hope'], 0),
        ('I ___ more people will grow fruit and vegetables in their gardens to help nature.',
         ['will', 'hope'], 1),
    ], material=ESSE),
    pismo('WRITING ✍️ Напиши сочинение «Школа через пятьдесят лет»',
          '<p>Начни так: <i>I think schools in fifty years from now …</i> — и напиши '
          'восемь-десять предложений.</p>'
          '<p>Сначала выбери, о чём будешь писать:</p>'
          '<ul><li><b>School items:</b> tablets / books / computers / e-books</li>'
          '<li><b>Where:</b> home / school building / online lessons</li>'
          '<li><b>Students:</b> lots of students / not a lot of students / teachers</li>'
          '<li><b>What:</b> more subjects / not a lot of subjects / exams / no exams</li>'
          '<li><b>How often:</b> every week / every day / at weekends / three days a week</li>'
          '<li><b>Classroom:</b> small or big / computer studies rooms / gym / playground / '
          'library</li>'
          '<li><b>School trips:</b> abroad / the country / city</li>'
          '<li><b>School lunches:</b> meals / sandwiches / free / expensive</li></ul>'
          '<p>Используй фразы предсказаний: <b>I think …</b>, <b>I don’t think …</b>, '
          '<b>I’m sure …</b>, <b>I hope …</b>, <b>Maybe …</b></p>'),
    poka(5, 'И послушали, и сочинение о будущем написали.'),
]

# ─────────────────────── ДЗ 7 · 8.7 Check yourself ───────────────────────
hw7 = [
    privet(0, 'Unit 8 · Check yourself!', 'Повторяем весь юнит перед тестом.'),
    kviz('Выбери правильное слово', [
        ('One day I want to ___ rich.', ['be', 'have'], 0),
        ('Will you ___ a foreign language next year at school?', ['learn', 'live'], 0),
        ('Would you like to live ___ your own?', ['on', 'in'], 0),
        ('I want to ___ an interesting job.', ['be', 'have'], 1),
        ('When Dad was a student he ___ abroad.', ['had', 'lived'], 1),
        ('Mum wanted to be ___ when she was younger.', ['famous', 'doctor'], 0),
    ]),
    vpisat('Посмотри на подсказку и напиши пропущенное слово по-английски', [
        ('Who did you ___ to the party? (пригласить)', ['invite', 'Invite']),
        ('Come here and give me a ___! (объятие)', ['hug', 'a hug', 'Hug']),
        ('Grandma likes to ___ all her grandchildren. (целовать)', ['kiss', 'Kiss']),
        ("I'll ___ you on the phone later. (позвонить)", ['call', 'Call']),
        ('Your brother is playing on the computer now, you need to wait your ___. (очередь)',
         ['turn', 'Turn']),
        ("When you want to use Dad's tablet, ask him ___. (разрешение)",
         ['permission', 'for permission', 'Permission']),
    ]),
    predlozheniya('Составь предложения о будущем: ✔ — утверждение, ✘ — отрицание, ❓ — вопрос', [
        ('✔ я стану ветеринаром', "I'll be a vet one day."),
        ('✘ Аманда не будет летать самолётом', "Amanda won't travel by plane."),
        ('❓ Джон научится водить в восемнадцать?', 'Will John learn to drive when he is eighteen?'),
        ('❓ что Фред будет делать после школы?', 'What will Fred do after school?'),
        ('✔ Мэри однажды разбогатеет', 'Mary will be rich one day.'),
        ('✘ у Тины не будет большой семьи', "Tina won't have a big family."),
    ]),
    propuski('Прочитай ответы и перетащи вопросительные слова в пропуски',
             "A: __What__ is your favourite hobby?\nB: My favourite hobby is chess.\n"
             "A: __Which__ did you eat in the UK?\nB: I ate fish and chips in the UK.\n"
             "A: __Where__ are you going to fly for your next holiday?\n"
             "B: We're going to fly to France for our next holiday.\n"
             "A: __Who__ made this cake?\nB: Mum made this cake.\n"
             "A: __How often__ do you exercise?\nB: I exercise three days a week.\n"
             "A: __When__ is the film on TV?\nB: The film is on TV in five minutes.", mode='drag'),
    kviz('Прочитай короткие разговоры и выбери правильный ответ', [
        ('A: This cake is disgusting!  B: I ___. I don’t like it.',
         ['agree', "don't agree"], 0),
        ('A: I think John will be late.  B: You’re ___. He’s opening the door now!',
         ['right', 'wrong'], 1),
        ('A: Cars are very bad for cities.  B: ___ Bikes are much better.',
         ["That's what I think too.", "No, that's not true."], 0),
        ('A: This Maths homework will be boring.  B: ___ I enjoy Maths.',
         ['I agree.', "I don't think so."], 1),
        ('A: I think Venice is a beautiful city.  B: ___ I love it there.',
         ['I agree.', 'I disagree.'], 0),
        ('A: This watch costs $500!  B: ___ Look! It’s $50!',
         ["No, that isn't right!", "That's right!"], 0),
    ]),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи, каким ты видишь себя через десять лет: где будешь жить, что будешь '
              'делать, чему научишься. Пять-шесть предложений с <b>will</b>.</p>',
              'I think I will live in a big city.'),
    poka(1, 'Юнит пройден. Можно браться за тест.'),
]

UROKI = [('Homework 1', hw1), ('Homework 2', hw2), ('Homework 3', hw3), ('Homework 4', hw4),
         ('Homework 5', hw5), ('Homework 6', hw6), ('Homework 7', hw7)]

if __name__ == '__main__':
    put = sys.argv[1] if len(sys.argv) > 1 else 'builds/gg3/wb/u8/u8.sql'
    out = ['-- Go Getter 3, юнит 8 «A happy life» по рабочей тетради: домашки 1–7 (черновики)',
           f"update classroom_lessons set sort_order = 10 where id = '{TEST}';"]
    for i, (nazv, bloki) in enumerate(UROKI):
        out.append(sql_uroka(UNIT, nazv, i, bloki))
    io.open(put, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(put, sum(len(b) for _, b in UROKI), 'блоков,', os.path.getsize(put) // 1024, 'КБ')
