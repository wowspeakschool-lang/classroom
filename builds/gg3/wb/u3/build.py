# -*- coding: utf-8 -*-
"""Go Getter 3, юнит 3 «Going on holiday» по рабочей тетради (стр. 24–30).

Ключи 3.7 — Answer key тетради (стр. 95); ключи аудирования 3.6 — по расшифровке
трека A8: Анна — пляж и плавание, Стив — горы и хайкинг, Джейн — скучный город,
Боб — кемпинг у озера.
"""
import io, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import (AUDIO, privet, poka, kartochki, kviz, pary, propuski, gruppy,
                    predlozheniya, vpisat, govorenie, pismo, tekst, posledovatelnost, sql_uroka)

UNIT = '30796c5f-452a-448f-b057-ba8daa32201b'   # Unit 3 · Going on holiday
TEST = '58db3616-b9e6-4113-8f1a-d87ab4f7bff4'
TRACK8 = AUDIO + 'GG%20L3%20WkBk%20A8.mp3'

# ─────────────────────── ДЗ 1 · 3.1 Vocabulary ───────────────────────
SLOVA = [
    ('go to the beach', 'ходить на пляж'), ('go cycling', 'кататься на велосипеде'),
    ('go snorkelling', 'нырять с маской'), ('go hiking', 'ходить в поход'),
    ('go camping', 'жить в палатке'), ('go on a boat trip', 'кататься на лодке'),
    ('go on a day trip', 'ездить на экскурсию на день'),
    ('go on a guided tour', 'ходить на экскурсию с гидом'),
    ('explore the area', 'исследовать местность'), ('try the local food', 'пробовать местную еду'),
    ('go sightseeing', 'осматривать достопримечательности'), ('get bored', 'скучать'),
]

hw1 = [
    privet(0, 'Unit 3 · Going on holiday', 'Сегодня — отдых и путешествия: чем заняться и как об этом рассказать.'),
    kartochki('Повторяем слова урока. Нажми на карточку — услышишь слово и увидишь перевод', SLOVA),
    pary('Соедини начало и конец совета для отпуска', [
        ('A good idea is to go on a day', 'boat trip on a lake and take photos of birds.'),
        ('Maybe you can go on a guided', 'tour of a museum.'),
        ("It's a good idea to explore the", 'city in the evening and see the lights.'),
        ("Why don't you go on", 'a trip to the beach?'),
        ("It's nice to explore the area", 'near your hotel.'),
        ("Don't forget to try", 'the local food because it is often delicious.'),
    ]),
    propuski('Прочитай блог Мирны про Хорватию и впиши пропущенные слова',
             "We have beautiful forests. You can go __hiking__ and you can go __cycling__ there. "
             "They are both great ways to explore the __area__.\n"
             "It's a good idea to go on a day __trip__ to Dubrovnik and to explore the __city__.\n"
             "When you are there, try the __local__ food. Croatian food is delicious. "
             "You can go on a __guided__ tour of the city and I think it is also a good idea to go on "
             "a __boat__ trip because the blue sea is wonderful."),
    gruppy('Распредели слова по глаголам', [
        ('go …', ['cycling', 'camping', 'hiking', 'snorkelling']),
        ('go on …', ['a boat trip', 'a guided tour']),
        ('go to …', ['the beach']),
        ('try …', ['the local food']),
        ('explore …', ['the area']),
    ]),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи, какой отдых тебе нравится: куда ты любишь ездить и чем там занимаешься. '
              'Скажи три-четыре предложения.</p>',
              'I like going camping with my family.'),
    poka(0, 'Отлично! Теперь ты можешь рассказать про любой отдых.'),
]

# ─────────────────────── ДЗ 2 · 3.2 Past Simple ───────────────────────
hw2 = [
    privet(1, 'Unit 3 · Past Simple', 'Сегодня — прошедшее время: что было и чего не было.'),
    kviz('Прочитай предложение и выбери правильную форму', [
        ('My friend Tony ___ on an island last week. His photos are amazing.', ['was', 'were'], 0),
        ('My sisters ___ in the hotel room an hour ago. Where are they now?', ['was', 'were'], 1),
        ("We ___ happy in the tent because it rained all the time.", ["wasn't", "weren't"], 1),
        ("The museum ___ interesting, so we explored the city.", ["wasn't", "weren't"], 0),
        ('I ___ in Paris last summer. I had a great time!', ['was', 'were'], 0),
        ("Our passports ___ in Mum's handbag. She forgot them!", ["wasn't", "weren't"], 1),
    ]),
    gruppy('Распредели глаголы в прошедшем времени: правильные или неправильные', [
        ('правильные (-ed)', ['locked', 'loved', 'played', 'tried', 'wanted']),
        ('неправильные', ['drank', 'ate', 'got up', 'went', 'knew']),
    ]),
    propuski('Впиши глагол в Past Simple',
             "Today I am on holiday, but yesterday I __was__ (am) at home.\n"
             "I'd like to try a different pizza. I __tried__ (try) the 'quattro stagioni' last time.\n"
             "I don't want to read Gulliver's Travels because I __read__ (read) it last year.\n"
             "Dave usually sleeps for eight hours, but last night he only __slept__ (sleep) for seven hours.\n"
             "Don't stay at that hotel. We __stayed__ (stay) there last summer and it was dirty.\n"
             "Jim often goes to the beach. He __went__ (go) there yesterday, last Monday and last Saturday!"),
    propuski('Прочитай дневник Поппи и впиши глагол в нужной форме',
             "Dear Diary,\n"
             "Harry is back from his holidays, so we __went__ (go) on a trip to London. "
             "It __was__ (be) fun! I loved it. But Emma __wasn't__ (not be) there! She was ill at home. "
             "We __explored__ (explore) the area near the River Thames and we __ate__ (eat) at a nice "
             "restaurant there. I __tried__ (try) fish pie for the first time. It was tasty, but Harry "
             "__didn't like__ (not like) it – he said it was horrible! Then we __went__ (go) on a boat trip "
             "on the river – we __were__ (be) really excited, but Harry's grandma __didn't want__ (not want) "
             "to go on the boat trip because she's scared of the water. But in the end, she came with us and "
             "she __had__ (have) fun.\nPoppy"),
    pismo('WRITING ✍️ Напиши пять правдивых предложений о себе',
          '<p>Закончи предложения своими словами, в прошедшем времени.</p>'
          '<ol><li>I … to the beach last … . It was a great day.</li>'
          '<li>My friends and I … snorkelling three … ago.</li>'
          '<li>We … the local … . But today I want a sandwich.</li>'
          '<li>I … go hiking last … because it rained.</li>'
          '<li>We … our cousins in Paris last … .</li></ol>'),
    poka(1, 'Молодец! Прошедшее время теперь слушается.'),
]

# ─────────────────────── ДЗ 3 · 3.3 Вопросы в Past Simple ───────────────────────
hw3 = [
    privet(2, 'Unit 3 · Вопросы о прошлом', 'Сегодня — как спросить про прошлые выходные и коротко ответить.'),
    pary('Соедини вопрос с коротким ответом', [
        ('Did you go to the park, Ann?', 'Yes, I did.'),
        ('Did your little sister go cycling?', "No, she didn't."),
        ('Was the weather good?', 'Yes, it was.'),
        ('Did you and your brothers have a picnic?', 'Yes, we did.'),
        ('Were your grandparents with you?', "No, they weren't."),
        ('What was in your sandwich?', 'Cheese and tomato.'),
    ]),
    predlozheniya('Составь вопросы, которые Энн задаёт Тому', [
        ('сестра пошла с тобой?', 'Did your sister go with you?'),
        ('вы ели попкорн?', 'Did you and your sister eat some popcorn?'),
        ('фильм был смешной?', 'Was the film funny?'),
        ('шёл ли дождь?', 'Did it rain?'),
        ('папа отвёз тебя домой?', 'Did your dad drive you home?'),
    ]),
    propuski('Прочитай разговор доктора Кью и Пи и впиши пропущенные слова',
             "Dr Q: __Did__ you and Millie play chess?\n"
             "Pi: Yes, __I did__. I won three games and Millie won two.\n"
             "Dr Q: Did you tidy the lab?\n"
             "Pi: __We didn't__. Sorry!\n"
             "Dr Q: __What__ did you watch on TV?\n"
             "Pi: We watched a film. It was very funny.\n"
             "Dr Q: __Was__ the weather good?\n"
             "Pi: Yes, __it was__. It was great.\n"
             "Dr Q: __Did__ you cook?\n"
             "Pi: Yes, __we did__. We were hungry.\n"
             "Dr Q: __What__ did you eat?\n"
             "Pi: We __ate__ pizza."),
    pismo('WRITING ✍️ Ответь на вопросы анкеты про свой последний отпуск',
          '<p>Ответь полными предложениями.</p>'
          '<ol><li>Did you go sightseeing on your last holiday?</li>'
          '<li>Where did you go?</li><li>Did it rain then?</li>'
          '<li>Was it cold in the morning or in the evening?</li>'
          '<li>Were your parents with you?</li><li>Did you all go to the beach?</li>'
          '<li>What did you do on the first day of your last holiday?</li>'
          '<li>Did you go hiking?</li></ol>'),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи про свои прошлые выходные: куда ходил, что делал, какая была погода. '
              'Три-четыре предложения в прошедшем времени.</p>',
              'Last Saturday I went to my grandparents.'),
    poka(2, 'Супер! Теперь ты умеешь и спрашивать, и отвечать о прошлом.'),
]

# ─────────────────────── ДЗ 4 · 3.4 Communication ───────────────────────
hw4 = [
    privet(0, 'Unit 3 · Просьбы', 'Сегодня — как вежливо попросить и как ответить на просьбу.'),
    predlozheniya('Составь вежливые просьбы и ответы', [
        ('просьба про фонарик', 'Can you bring me my torch, please?'),
        ('ответ на неё', 'Yes, no problem.'),
        ('просьба про карту', 'Can I have the map?'),
        ('вежливый отказ', "Sorry, I'm using it right now."),
        ('просьба про расписание', 'Could you give me the train timetable?'),
        ('согласие', 'Yes, of course.'),
    ]),
    posledovatelnost('Расставь реплики по порядку — получится разговор сына с папой', [
        'Can I have the camera, Dad?',
        "Sorry, you can't. I'm taking some photos now.",
        'OK Dad. So Dad, can I borrow your smartphone? I want to take a photo.',
        'Yes, no problem. Here you are.',
        'Thank you, Dad. Could you stand there, please? I’d like you to be in the photo.',
        'Yes, of course. Is here OK?',
        "Yes, it's fine. Smile!",
    ]),
    kviz('Прочитай просьбу и выбери ответ', [
        ('A: Could you bring me the menu?',
         ["Sorry, you can't.", 'Oh, never mind.', 'Yes, of course.'], 2),
        ('A: Can you lend me some money, please?',
         ['Yes, you can.', 'Yes, no problem.', "Sorry, you can't."], 1),
        ("B: Sorry, not now. I'm looking at it. — Какой была просьба?",
         ['Could you buy me a map?', 'Can I have the map now, please?', 'Can you see the map?'], 1),
    ]),
    propuski('Впиши пропущенные слова в вежливые просьбы',
             "A: Can I __borrow your torch__, please?\nB: __Yes, of__ course.\n"
             "A: Could __you give me__ the key to the garage?\nB: __Yes, no__ problem.\n"
             "A: Can __I wear your sunglasses__, please?\nB: Sorry, __you can't__. I'm wearing them right now.\n"
             "A: Could __you lend me your phone__?\nB: Not __now, sorry__. I'm using it."),
    govorenie('SPEAKING 🎤 Разыграй две просьбы и запиши ответ',
              '<p>Попроси у мамы фотоаппарат, а у брата — планшет. На одну просьбу придумай согласие, '
              'на другую — вежливый отказ.</p>',
              "Could you lend me your tablet, please?"),
    poka(3, 'Отлично! Просить и отказывать вежливо — тоже навык.'),
]

# ─────────────────────── ДЗ 5 · 3.5 Reading ───────────────────────
BLOG3 = (
    '<h3>My holidays in Scotland <span style="color:#888">by Tommy</span></h3>'
    "<p><b>A</b> My mum and I don't stay at home in the holidays. We love sports, so last year we went to "
    "Scotland. Scotland has lots of mountains and wild countryside, so it is great for outdoor activities. "
    "The place we stayed at is a holiday village called Glencoe Mountain. We went there in the summer and "
    "in the winter.</p>"
    "<p><b>B</b> We drove to Glencoe Mountain in August. There is a campsite there and we put up our tent "
    "together at 10 p.m. It wasn't dark because it gets dark late in Scotland in the summer. We went cycling "
    "on our mountain bikes for the first two days. We got tired, but the views were amazing. Then we went "
    "hiking and we saw some wild rabbits and a fox.</p>"
    "<p><b>C</b> We went to Glencoe Mountain again in December. On the first day, we travelled by coach and "
    "the coach got lost on the way! But our holiday was great. It was sunny all the time, so we didn't get "
    "cold. My mum and I went skiing every day. Glencoe Mountain is my favourite place for a holiday. "
    "There is so much to do. You never get bored.</p>"
)

hw5 = [
    privet(1, 'Unit 3 · Reading', 'Сегодня читаем блог Томми про отдых в Шотландии.'),
    tekst(BLOG3),
    kviz('Прочитай блог и подбери заголовок к каждому абзацу', [
        ('Абзац A', ['Summer fun', 'Two holidays in one year', 'Bad weather', 'A winter holiday'], 1),
        ('Абзац B', ['Summer fun', 'Two holidays in one year', 'Bad weather', 'A winter holiday'], 0),
        ('Абзац C', ['Summer fun', 'Two holidays in one year', 'Bad weather', 'A winter holiday'], 3),
    ], material=BLOG3),
    propuski('Прочитай блог ещё раз и впиши по одному слову',
             "Tommy went on holiday with his __mum__.\n"
             "In August it wasn't __dark__ at 10 p.m.\n"
             "__Cycling__ was their first activity.\n"
             "They saw some rabbits and a fox when they went __hiking__.\n"
             "Tommy and his mum didn't __travel__ by car for the winter holiday.\n"
             "Tommy and his mum went __skiing__ in December.\n"
             "Glencoe Mountain is Tommy's __favourite__ place to go on holiday.", material=BLOG3),
    kviz('Выбери правильное слово после get', [
        ('In winter it gets ___ in my town at 10 p.m.', ['bored', 'dark'], 1),
        ('It gets ___ in winter in my town.', ['tired', 'cold'], 1),
        ('People sometimes get ___ when they go hiking.', ['lost', 'dark'], 0),
        ('Last night I got ___ at 9 p.m., so I went to bed early.', ['tired', 'cold'], 0),
        ('I never get ___ when I go sightseeing.', ['bored', 'dark'], 0),
    ]),
    pismo('WRITING ✍️ Напиши про своё любимое место для отдыха',
          '<p>Четыре-пять предложений: где это, когда ты там был, что вы делали и почему тебе там нравится.</p>'),
    poka(4, 'Здорово! Шотландия прочитана, а своё место описано.'),
]

# ─────────────────────── ДЗ 6 · 3.6 Listening and Writing ───────────────────────
hw6 = [
    privet(2, 'Unit 3 · Listening and Writing', 'Сегодня слушаем рассказы об отпуске и пишем письмо дяде.'),
    gruppy('Распредели слова по группам', [
        ('🏖 пляж', ['beach', 'swimming', 'snorkelling']),
        ('⛺ горы', ['camping', 'hiking', 'mountains']),
        ('🏙 город', ['city', 'museums', 'restaurants']),
    ]),
    ('quiz', {'title': 'LISTENING 🎧 Послушай запись и выбери правильный ответ',
              'audio': TRACK8, 'skill': 'listening',
              'questions': [
                  {'q': 'Where did Anna go on holiday?', 'type': 'single', 'correct': [0],
                   'options': [{'text': 'to the beach'}, {'text': 'to the mountains'},
                               {'text': 'to a campsite'}]},
                  {'q': 'What did Steve do on holiday?', 'type': 'single', 'correct': [2],
                   'options': [{'text': 'he went snorkelling'}, {'text': 'he went cycling'},
                               {'text': 'he went hiking'}]},
                  {'q': 'Why didn’t Jane like her holiday?', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'the weather was bad'}, {'text': 'the city wasn’t interesting'},
                               {'text': 'the hotel was dirty'}]},
                  {'q': 'Where did Bob stay?', 'type': 'single', 'correct': [0],
                   'options': [{'text': 'at a campsite next to a lake'}, {'text': 'in a hotel in the city'},
                               {'text': 'at his grandparents’ house'}]},
              ]}),
    propuski('LISTENING 🎧 Послушай запись ещё раз и впиши по одному слову',
             "Anna: She took __photos__ on her holiday. She went __swimming__ every day.\n"
             "Steve: He went to the __mountains__. He went __hiking__.\n"
             "Jane: She didn't __like__ her holiday. The __city__ wasn't interesting.\n"
             "Bob: He stayed at a __campsite__ next to a lake. He loves __camping__."),
    propuski('Прочитай письмо Ребекки и перетащи слова в пропуски',
             "Dear Uncle Paul,\n"
             "I hope you're __well__. We're having a great time on the island. I wish __you__ were here! "
             "There are lots of __things__ to do here. Last Sunday we went snorkelling with Aunt Jess. "
             "We swam for an hour. I saw lots of pretty fish and an octopus. Dan saw a starfish and "
             "Aunt Jess saw a crab. Yesterday we __went__ cycling in the countryside. It was windy, but "
             "I had a jacket, so I didn't __get__ cold. I need to help Aunt Jess with the cooking now, "
             "so I can't write any __more__. __See__ you soon!\nLots of __love__,\nRebecca", mode='drag'),
    pismo('WRITING ✍️ Напиши письмо дяде от имени Дэна',
          '<p>Используй заметки о двух днях отдыха:</p>'
          '<p><b>Понедельник:</b> ресторан с тётей Джесс; попробовали местную еду; Ребекка — курица, '
          'Дэн — рыба с картошкой, тётя Джесс — рис с овощами.<br>'
          '<b>Вторник:</b> поход в горы; Ребекка устала, Дэн — нормально, тётя Джесс очень довольна.</p>'
          '<p>Начни так: <i>Dear Uncle Paul, I hope …</i></p>'),
    poka(5, 'Отлично! И послушали, и написали настоящее письмо.'),
]

# ─────────────────────── ДЗ 7 · 3.7 Check yourself ───────────────────────
hw7 = [
    privet(0, 'Unit 3 · Check yourself!', 'Повторяем весь юнит перед тестом.'),
    kviz('Прочитай про выходные Джо и Роба и выбери правильное слово', [
        ('Last Saturday Joe and Rob went ___ in the morning.', ['cycling', 'hiking'], 0),
        ('They got on their bikes and they went ___.', ['camping', 'to the beach'], 1),
        ('They swam and then they got ___.', ['lost', 'cold'], 1),
        ('In the afternoon they explored the ___.', ['area', 'city'], 0),
        ('They were hungry, so they decided to ___.', ['go snorkelling', 'try the local food'], 1),
        ("They went home at eight o'clock because it got ___.", ['dark', 'tired'], 0),
    ]),
    propuski('Прочитай объявление про поездку в Лондон и перетащи слова в пропуски',
             "Why don't you __go on__ a day trip to London and visit the Tower of London!\n"
             "How to get there: You can go on a boat __trip__ on the River Thames. "
             "Or you can go __cycling__ on your bike along the river paths.\n"
             "What to do there: We have great __guided__ tours for kids and families. "
             "You can also __explore__ the Tower on your own. Find out interesting facts about the kings "
             "and queens of England. You won't get __bored__!", mode='drag'),
    propuski('Впиши глагол в Past Simple',
             "My neighbours, the Greens, spent their last summer holidays on an island. "
             "They __arrived__ (arrive) at the airport early, but the plane was late. "
             "Mr Green __left__ (leave) the guidebook at home. "
             "Mrs Green __didn't like__ (not like) the hotel. "
             "The weather __was__ (be) windy. "
             "Their son __got__ (get) lost on the beach. "
             "They __didn't take__ (not take) any photos. That holiday wasn't their favourite."),
    propuski('Прочитай разговор Марко и Джейн и впиши пропущенное слово',
             "Marco: How __was__ your month in Italy? __Did__ you try Italian food?\n"
             "Jayne: Yes, I __did__. It was tasty.\n"
             "Marco: __Were__ the museums interesting?\n"
             "Jayne: Yes, they were. I went sightseeing a lot.\n"
             "Marco: Was the weather good?\n"
             "Jayne: No, it __wasn't__. The first week it rained.\n"
             "Marco: Oh no. Did you stay in the hotel?\n"
             "Jayne: No, I __didn't__. I went out. I had an umbrella, so I was OK."),
    kviz('Прочитай разговор в ресторане и выбери правильный вариант', [
        ('A: ___ bring me the menu, please?', ['Can you', 'You can'], 0),
        ('B: Yes, ___.', ['of course', 'not now'], 0),
        ('A: And could ___ also bring me some water?', ['I', 'you'], 1),
        ('B: ___, no problem.', ['No', 'Yes'], 1),
        ('A: ___ have the fish, please?', ['Can I', 'Can you'], 0),
        ("B: ___ There isn't any fish today.", ['Not now, sorry.', "Sorry, you can't."], 1),
    ]),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи о поездке, которая тебе запомнилась: куда вы поехали, что делали, '
              'какая была погода и что понравилось больше всего.</p>',
              'Last summer we went to the mountains.'),
    poka(1, 'Юнит пройден! Можно браться за тест.'),
]

UROKI = [('Homework 1', hw1), ('Homework 2', hw2), ('Homework 3', hw3), ('Homework 4', hw4),
         ('Homework 5', hw5), ('Homework 6', hw6), ('Homework 7', hw7)]

if __name__ == '__main__':
    put = sys.argv[1] if len(sys.argv) > 1 else 'builds/gg3/wb/u3/u3.sql'
    out = ['-- Go Getter 3, юнит 3 «Going on holiday» по рабочей тетради: домашки 1–7 (черновики)',
           f"update classroom_lessons set sort_order = 10 where id = '{TEST}';"]
    for i, (nazv, bloki) in enumerate(UROKI):
        out.append(sql_uroka(UNIT, nazv, i, bloki))
    io.open(put, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(put, sum(len(b) for _, b in UROKI), 'блоков,', os.path.getsize(put) // 1024, 'КБ')
