# -*- coding: utf-8 -*-
"""Go Getter 3, юнит 4 «Useful things» по рабочей тетради (стр. 32–38).

Ключи 4.7 — Answer key тетради (стр. 95); ключи аудирования 4.6 — по расшифровке
трека A10: история 1 — торт и собака на день рождения брата, история 2 — лыжный
отпуск с папой, снег и два лишних дня в отеле.
"""
import io, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import (AUDIO, privet, poka, kartochki, kviz, pary, propuski, gruppy,
                    predlozheniya, vpisat, govorenie, pismo, tekst, sql_uroka)

UNIT = '1c0998df-b88e-42e9-ba65-5962093f45cd'   # Unit 4 · Useful things
TEST = '2763c9bf-4b1a-4bff-830c-6f5da5c98e2d'
TRACK10 = AUDIO + 'GG%20L3%20WkBk%20A10.mp3'

# ─────────────────────── ДЗ 1 · 4.1 Vocabulary ───────────────────────
SLOVA = [
    ('smart TV', 'умный телевизор'), ('remote control', 'пульт'),
    ('games console', 'игровая приставка'), ('DVD player', 'DVD-плеер'),
    ('microwave oven', 'микроволновка'), ('electric toothbrush', 'электрическая зубная щётка'),
    ('hairdryer', 'фен'), ('blender', 'блендер'), ('toaster', 'тостер'),
    ('USB stick', 'флешка'), ('touch screen', 'сенсорный экран'),
    ('portable charger', 'внешний аккумулятор'), ('battery', 'батарея'),
    ('app', 'приложение'), ('ringtone', 'рингтон'),
]

hw1 = [
    privet(0, 'Unit 4 · Useful things', 'Сегодня — техника дома: как всё это называется по-английски.'),
    kartochki('Повторяем слова урока. Нажми на карточку — услышишь слово и увидишь перевод', SLOVA),
    vpisat('Прочитай подсказку и напиши слово по-английски', [
        ('You can watch films and surf the Internet on it (sm… TV)', ['smart TV', 'Smart TV', 'smart tv']),
        ('The photos from the party are on this (U… s…)', ['USB stick', 'usb stick', 'a USB stick']),
        ("Let's put a film in it to watch (D… p…)", ['DVD player', 'dvd player', 'a DVD player']),
        ("The toast is in it. Be careful, it's hot! (t…)", ['toaster', 'Toaster', 'a toaster']),
        ("Let's make strawberry milkshakes in it (b…)", ['blender', 'Blender', 'a blender']),
        ("My hair is wet and it isn't working (h…)", ['hairdryer', 'Hairdryer', 'a hairdryer', 'hair dryer']),
    ]),
    kviz('Прочитай разговор Пэм и папы за завтраком и выбери правильное слово', [
        ('Dad: Can you put the bread in the ___, please?', ['toaster', 'blender'], 0),
        ('Pam: Sure. Do you want me to turn it ___ now?', ['off', 'on'], 1),
        ('Dad: No, I can do it in a minute. But you can ___.', ['unplug it', 'plug it in'], 1),
        ('Dad: Put some milk in the ___.', ['remote control', 'microwave oven'], 1),
        ("Dad: There's a problem with the toaster! It didn't turn ___ and the bread is black now.",
         ['on', 'off'], 1),
    ]),
    gruppy('Распредели технику по комнатам', [
        ('🍳 кухня', ['blender', 'toaster', 'microwave oven']),
        ('🛁 ванная', ['hairdryer', 'electric toothbrush']),
        ('🛋 гостиная', ['DVD player', 'games console', 'smart TV', 'remote control']),
    ]),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи, какой техникой дома ты пользуешься чаще всего и для чего. '
              'Три-четыре предложения.</p>',
              'I use the microwave oven every morning.'),
    poka(0, 'Отлично! Теперь вся домашняя техника — по-английски.'),
]

# ─────────────────────── ДЗ 2 · 4.2 Past Continuous ───────────────────────
hw2 = [
    privet(1, 'Unit 4 · Past Continuous', 'Сегодня — что происходило в какой-то момент в прошлом.'),
    propuski('Посмотри на время и впиши глагол в Past Continuous',
             "At 3 p.m. yesterday Mark and Dan __weren't watching__ TV. "
             "They __were playing__ video games.\n"
             "At 10 a.m. last Sunday my sister __wasn't listening__ to music. "
             "She __was helping__ me with my homework.\n"
             "At 6.30 p.m. yesterday Aunt Jane __wasn't reading__ a book. "
             "She __was cooking__ dinner."),
    pary('Соедини вопрос с ответом', [
        ('Were you shopping at 1 p.m., Sarah?', 'Yes, I was.'),
        ('Were the crew filming in the park yesterday?', 'Yes, they were.'),
        ('Was Dad watching a DVD at eight o’clock?', "No, he wasn't. He was reading."),
        ('Was Mum drinking tea at four o’clock?', 'Yes, she was.'),
        ('Were you two sitting here a minute ago?', "No, we weren't. We were over there."),
        ('Was I talking to your grandma?', "No, you weren't. It was my aunt."),
    ]),
    predlozheniya('Составь вопросы в Past Continuous', [
        ('Адрианна снимала видео?', 'Was Adrianna filming a new video in the park?'),
        ('Гарри играл в теннис?', 'Was Harry playing tennis?'),
        ('Эмма занималась дома?', 'Was Emma studying at home?'),
        ('Поппи с мамой искали фен?', 'Were Poppy and her mum looking for a hairdryer?'),
    ]),
    propuski('Впиши короткий ответ: ✔ — да, ✘ — нет',
             "Were Poppy and Harry hanging out in the park? ✘ No, __they weren't__.\n"
             "Was Adrianna filming a new video in the park? ✔ Yes, __she was__.\n"
             "Was Harry playing tennis? ✔ Yes, __he was__.\n"
             "Was Emma studying at home? ✘ No, __she wasn't__.\n"
             "Were Poppy and her mum looking for a hairdryer? ✔ Yes, __they were__."),
    pismo('WRITING ✍️ Напиши вопросы и ответь на них о себе',
          '<p>Составь вопросы в Past Continuous и ответь правдиво.</p>'
          '<ol><li>you / take photos / yesterday / 10 a.m.?</li>'
          '<li>your friend / chat online to you / last Saturday / 8 p.m.?</li>'
          '<li>you and your classmates / have an English lesson / on Monday / 10 a.m.?</li>'
          '<li>What / you / do / yesterday / 6 a.m.?</li></ol>'),
    poka(1, 'Молодец! Past Continuous теперь понятен.'),
]

# ─────────────────────── ДЗ 3 · 4.3 Past Continuous и Past Simple ───────────────────────
hw3 = [
    privet(2, 'Unit 4 · when и наречия', 'Сегодня — что происходило, когда что-то случилось, и как это происходило.'),
    kviz('Прочитай историю про доктора Кью и выбери правильную форму', [
        ('Doctor Q ___ in his lab one day when Pi flew in.', ['was working', 'worked'], 0),
        ('Doctor Q was working in his lab one day when Pi ___ in.', ['was flying', 'flew'], 1),
        ("'Doctor Q, I ___ in the garden when I found this strange box.'", ['was hopping', 'hopped'], 0),
        ("'I was hopping in the garden when I ___ this strange box.'", ['was finding', 'found'], 1),
        ("'Thank you, Pi. I ___ for that box when you came in.'", ['was looking', 'looked'], 0),
        ("'I was looking for that box when you ___ in.'", ['were coming', 'came'], 1),
    ]),
    predlozheniya('Составь предложения с when', [
        ('читал книгу, когда пришли родители', 'I was reading a book when my parents came home.'),
        ('готовил на кухне, когда мы открыли дверь', 'Dad was cooking in the kitchen when we opened the front door.'),
        ('играл в игру, когда пришли близнецы', 'I was playing a game when the twins arrived.'),
    ]),
    propuski('Прочитай разговор Энн с мамой и впиши глагол в нужной форме',
             "Ann: Mum, this morning I __was using__ (use) the blender when it __stopped__ (stop) working.\n"
             "Mum: That's strange. It worked yesterday.\n"
             "Ann: Olga was here. We __put__ (put) strawberries into the blender when Dad __came__ (come) in. "
             "The blender __was mixing__ (mix) the strawberries and yogurt when suddenly it __turned off__ (turn off).\n"
             "Mum: Hmm. Did you ask Dad to fix it?\n"
             "Ann: Yes, and he says we need a new blender."),
    pary('Соедини предложение с продолжением', [
        ('Wendy is good at English.', 'She speaks it well.'),
        ("I don't know a lot of French.", 'I speak it badly.'),
        ('Dave is good at Maths.', 'He does his homework easily.'),
        ('Dogs like running.', 'They can go fast.'),
        ('Grandpa is old.', 'He walks slowly.'),
        ('The baby is sleeping.', 'Please talk quietly.'),
    ]),
    propuski('Впиши глагол и наречие: carefully · happily · loudly · politely · fast',
             "We __were talking__ __loudly__ (talk) when our teacher came in.\n"
             "Dad __was running__ __fast__ (run) when I saw him in the park.\n"
             "The dog was playing __happily__ in the garden when it __started__ (start) to rain.\n"
             "I __was doing__ the exercise __carefully__ (do) when the teacher came to my desk.\n"
             "I was answering the nurse __politely__ when the doctor __came__ (come) in."),
    poka(2, 'Супер! Теперь понятно, что шло, а что вдруг случилось.'),
]

# ─────────────────────── ДЗ 4 · 4.4 Communication ───────────────────────
hw4 = [
    privet(0, 'Unit 4 · Сочувствие', 'Сегодня — как поддержать друга, когда у него неприятность.'),
    pary('Соедини начало и конец фразы', [
        ('You', 'look upset.'),
        ('You look', 'worried.'),
        ("What's", 'wrong?'),
        ('What', 'happened?'),
        ("I'm so sorry", 'to hear that.'),
        ("That's a", 'shame.'),
    ]),
    kviz('Прочитай реплику и выбери ответ', [
        ('A: What happened to your arm?',
         ['I was ice skating when I fell over.', 'No, not really.', 'I went ice skating.'], 0),
        ("B: No, I can't. — Какой была реплика A?",
         ['Can I help?', 'You look upset.', "That's terrible. Can you write?"], 2),
        ("B: Yes, please. I'd like some help. — Какой была реплика A?",
         ["I'm so sorry. Can I help?", "I'm so sorry to hear that.", "What's wrong?"], 0),
    ]),
    propuski('Прочитай разговор Зака и Вики и впиши пропущенное слово',
             "Zach: You look upset. What's __wrong__?\n"
             "Vicky: I __was__ doing my homework __when__ I dropped my calculator. Now it doesn't work.\n"
             "Zach: That's a __shame__. Can I __help__?\n"
             "Vicky: __No__, not really. I can't do my Maths without a calculator.\n"
             "Zach: Why don't __you__ ask your brother for help? He's good at Maths.\n"
             "Vicky: That's a good idea. Thanks."),
    predlozheniya('Составь фразы поддержки', [
        ('ты выглядишь расстроенным', 'You look worried.'),
        ('что случилось?', "What's happened?"),
        ('звонил маме, когда телефон сломался', 'I was calling Mum when my phone broke.'),
        ('какой ужас', "That's terrible."),
    ]),
    govorenie('SPEAKING 🎤 Разыграй разговор и запиши ответ',
              '<p>Твой друг промок под дождём, и его собака тоже. Поддержи его: заметь, что он расстроен, '
              'спроси, что случилось, посочувствуй и предложи помощь.</p>',
              'You look upset. What happened?'),
    poka(3, 'Отлично! Теперь ты знаешь, что сказать другу в трудный момент.'),
]

# ─────────────────────── ДЗ 5 · 4.5 Reading ───────────────────────
RASSKAZ = (
    '<h3>Read my dad’s story! <span style="color:#888">by Josh</span></h3>'
    "<p>‘In 1990 I was a young boy. It was an autumn day in town. I was walking down the High Street with "
    "my mum when I stopped because I wanted to look in a shop window. I was feeling very excited because "
    "I saw something very special in the shop.</p>"
    "<p>That special thing was a new games console. But it wasn't just a normal games console. It was the "
    "first portable games console.</p>"
    "<p>That day was my birthday. I had some money to spend and I was looking for a present to buy when "
    "I saw that games console.</p>"
    "<p>I bought it and I was really happy. The games console had four buttons on it, it took headphones "
    "and it also had a battery pack that you plugged in. There weren't a lot of games at first – in fact, "
    "I had only two. I loved computer games, so I played a lot!’</p>"
    "<p>And now my dad has a fantastic job! He is a game tester! He plays games before they sell them in "
    "the shops. Amazing! So, he still loves computer games and he plays a lot.</p>"
)

hw5 = [
    privet(1, 'Unit 4 · Reading', 'Сегодня читаем рассказ Джоша про первую игровую приставку его папы.'),
    tekst(RASSKAZ),
    kviz('Прочитай рассказ и выбери правильный ответ', [
        ('What year was it?', ['It was 1990.', 'It was 1999.', 'It was 2009.'], 0),
        ('Where was the young boy walking?',
         ['in the park', 'down the High Street', 'in a shopping centre'], 1),
        ('Why did he stop?',
         ['because he was tired', 'because he wanted to look in a shop window',
          'because his mum called him'], 1),
        ('What day was it?', ['his birthday', 'Christmas Day', 'the first day of school'], 0),
        ('Were there a lot of games for the console?',
         ["No, there weren't. He had only two.", 'Yes, there were a lot.'], 0),
    ], material=RASSKAZ),
    kviz('Эти предложения про рассказ неверные. Выбери, как правильно', [
        ('It was winter.', ['It was autumn.', 'It was summer.'], 0),
        ('The boy was excited about an old games console in the shop.',
         ['He was excited about a new games console.', 'He was excited about a new phone.'], 0),
        ('The games console had five buttons.',
         ['It had four buttons.', 'It had two buttons.'], 0),
        ("Josh's dad had three games.",
         ['He had only two games.', 'He had ten games.'], 0),
    ], material=RASSKAZ),
    propuski('Прочитай разговор Ребекки с дедушкой и перетащи слова в пропуски',
             "Grandad: I want to buy a smartphone.\n"
             "Rebecca: Do you know anything about them, Grandad?\n"
             "Grandad: Yes, I do. I know they have __touch screens__, not buttons, and that you can "
             "download __apps__.\n"
             "Rebecca: Yes, that's right. You can also choose different __ringtones__ for different people.\n"
             "Grandad: Can I get those from the Internet?\n"
             "Rebecca: Yes. Now look at my phone. It has a very good __battery__. It lasts for ten hours.\n"
             "Grandad: That's good. Do I need to buy a __portable charger__ too?\n"
             "Rebecca: No. It comes with the phone.\nGrandad: Thanks, Rebecca.", mode='drag'),
    pismo('WRITING ✍️ Напиши про свой любимый гаджет',
          '<p>Четыре-пять предложений: что это, когда он у тебя появился, что ты с ним делаешь '
          'и почему он тебе нравится.</p>'),
    poka(4, 'Здорово! История прочитана, свой гаджет описан.'),
]

# ─────────────────────── ДЗ 6 · 4.6 Listening and Writing ───────────────────────
ISTORIYA = (
    "<p><b>Something cool happened at school … by Tina Smith</b></p>"
    "<p>Last Monday I <b>was</b> sitting in the classroom at my desk. My best friend, Tom, … talking loudly "
    "and his brother, Fred, was laughing. We … waiting for our teacher, but she was late. Finally, she came "
    "in the classroom with a hamster in a box. It was her pet hamster. Tom and Fred were quiet. We … looking "
    "into the box when the hamster came out of its little house. It was brown and it had a pink nose. "
    "I think it felt a bit scared at first. But five minutes later it … eating a carrot and it was happy. "
    "The hamster's name was Chuck. Our teacher told us a lot about hamsters in the lesson. It was very "
    "interesting. We liked the lesson a lot.</p>"
)

hw6 = [
    privet(2, 'Unit 4 · Listening and Writing', 'Сегодня слушаем две смешные истории и пишем свою.'),
    vpisat('Напиши название чувства по-английски', [
        ('заинтересованный (i…)', ['interested', 'Interested']),
        ('счастливый (h…)', ['happy', 'Happy']),
        ('грустный (s…)', ['sad', 'Sad']),
        ('уставший (t…)', ['tired', 'Tired']),
        ('испуганный (s…)', ['scared', 'Scared']),
        ('встревоженный (w…)', ['worried', 'Worried']),
    ]),
    ('quiz', {'title': 'LISTENING 🎧 Послушай две истории и выбери правильный ответ',
              'audio': TRACK10, 'skill': 'listening',
              'questions': [
                  {'q': 'Story 1 is about …', 'type': 'single', 'correct': [2],
                   'options': [{'text': 'an angry brother'}, {'text': 'a school ski trip'},
                               {'text': 'birthday food'}, {'text': 'an interesting holiday'}]},
                  {'q': 'Story 2 is about …', 'type': 'single', 'correct': [3],
                   'options': [{'text': 'an angry brother'}, {'text': 'a school ski trip'},
                               {'text': 'birthday food'}, {'text': 'an interesting holiday'}]},
                  {'q': 'Why did the cake go wrong in Story 1?', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'the oven was broken'},
                               {'text': 'the dog ate the cake mix'},
                               {'text': 'there wasn’t any sugar'}]},
                  {'q': 'Why did they stay two extra days in Story 2?', 'type': 'single', 'correct': [0],
                   'options': [{'text': 'the road was closed because of the snow'},
                               {'text': 'the hotel was very cheap'},
                               {'text': 'Dad was ill'}]},
              ]}),
    propuski('LISTENING 🎧 Послушай истории ещё раз и впиши по одному слову',
             "Story 1\n"
             "It was my __brother's__ birthday. I was making a __cake__. "
             "__Twenty__ minutes later I was watching TV. "
             "The __dog__ was eating the cake mix when I walked in. Mum ordered __pizza__.\n"
             "Story 2\n"
             "__Dad__ and I were staying in a hotel in the mountains. We were on a __skiing__ holiday. "
             "On __Saturday__ there was snow everywhere. We looked for the __road__, but we couldn't see it. "
             "We stayed for __two__ extra days."),
    propuski('Прочитай историю Тины и впиши глагол в нужной форме',
             "Last Monday I __was__ sitting in the classroom at my desk. My best friend, Tom, __was__ "
             "talking loudly and his brother, Fred, was laughing. We __were__ waiting for our teacher, "
             "but she was late. Finally, she came in the classroom with a hamster in a box. It was her pet "
             "hamster. Tom and Fred were quiet. We __were__ looking into the box when the hamster came out "
             "of its little house. It was brown and it had a pink nose. I think it felt a bit scared at "
             "first. But five minutes later it __was__ eating a carrot and it was happy."),
    pismo('WRITING ✍️ Напиши историю про урок с собакой учителя',
          '<p>Представь: учитель принёс в класс свою собаку. Напиши историю из пяти-шести предложений.</p>'
          '<p>Сначала задай обстановку (Past Continuous), потом расскажи, что случилось (Past Simple '
          'или Past Continuous с <b>when</b>), в конце — чем всё закончилось и что ты почувствовал.</p>'
          '<p>Слова-помощники: big, dark, ears, friendly, jump, (not) interested, legs, long, quickly, run, '
          '(not) scared, walk.</p><p>Начни так: <i>Last Friday …</i></p>'),
    poka(5, 'Отлично! И послушали, и свою историю написали.'),
]

# ─────────────────────── ДЗ 7 · 4.7 Check yourself ───────────────────────
hw7 = [
    privet(0, 'Unit 4 · Check yourself!', 'Повторяем весь юнит перед тестом.'),
    propuski('Прочитай короткие разговоры и впиши название техники',
             "A: I'd like some hot milk.\nB: Put a mug of milk in the __microwave oven__.\n"
             "A: My hair is wet.\nB: You need a __hairdryer__.\n"
             "A: Let's watch TV.\nB: OK. Where's the __remote control__?\n"
             "A: Can I make a smoothie?\nB: Yes. You have to plug in the __blender__ first.\n"
             "A: I bought a new film.\nB: Cool, let's watch it! Put it in the __DVD player__.\n"
             "A: Your teeth are very white.\nB: Thanks. I've got a new __electric toothbrush__."),
    kviz('Выбери правильный вариант', [
        ("There's a good film on tonight. Let's watch it on my ___.",
         ['smart TV', 'toaster', 'portable charger'], 0),
        ("Grandpa's old mobile phone doesn't have a ___.",
         ['games console', 'ringtone', 'touch screen'], 2),
        ("You must speak ___. Grandma can't hear very well.", ['quietly', 'loudly', 'badly'], 1),
        ("'Why doesn't your TV work?' 'Because you didn't ___.'",
         ['plug it in', 'turn it off', 'unplug it'], 0),
        ('I walked to school ___, so I was late.', ['easily', 'fast', 'slowly'], 2),
    ]),
    propuski('Впиши глагол в Past Continuous: do · listen · play · not tidy · watch',
             "A: Where's Fred? He __was doing__ his homework an hour ago.\n"
             "B: His friends __were playing__ football in the park an hour ago and he wanted to play too.\n"
             "A: Sally and Tina __weren't tidying__ their room at six o'clock because they weren't at home. "
             "Where were they?\n"
             "B: Don't worry. They did it at five o'clock. I think they __were watching__ TV at Jane's house.\n"
             "A: I phoned you at ten, but you didn't answer. __Were you listening__ to your music?\n"
             "B: Yes, __I was__! I didn't hear the phone."),
    propuski('Прочитай историю про пса Рекса и впиши глагол в нужной форме',
             "I __was walking__ (walk) home when I __saw__ (see) Uncle George in his car. "
             "He __was turning__ (turn) right when a tired hungry dog __ran__ (run) into the road. "
             "Luckily, Uncle George __was driving__ (drive) slowly when the dog __went__ (go) in front of "
             "his car and he stopped. Now Rex lives with Uncle George! Uncle George loves Rex and Rex "
             "loves Uncle George."),
    kviz('Прочитай разговор и выбери правильный вариант', [
        ('A: You ___ upset.', ['worried', 'look'], 1),
        ("A: What's ___?", ['wrong', 'happened'], 0),
        ('B: I was shopping ___ I lost my phone.', ['where', 'when'], 1),
        ("A: That's ___! Can I help?", ['shame', 'terrible'], 1),
        ("A: That's terrible! Can ___ help?", ['I', 'you'], 0),
        ("A: I'm ___ to hear that. I hope you find it.", ['so sorry', 'so worry'], 0),
    ]),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи про случай, когда техника подвела: что ты делал, что случилось и чем всё '
              'закончилось. Три-четыре предложения в прошедшем времени.</p>',
              'Last week I was watching a film when the TV stopped working.'),
    poka(1, 'Юнит пройден! Можно браться за тест.'),
]

UROKI = [('Homework 1', hw1), ('Homework 2', hw2), ('Homework 3', hw3), ('Homework 4', hw4),
         ('Homework 5', hw5), ('Homework 6', hw6), ('Homework 7', hw7)]

if __name__ == '__main__':
    put = sys.argv[1] if len(sys.argv) > 1 else 'builds/gg3/wb/u4/u4.sql'
    out = ['-- Go Getter 3, юнит 4 «Useful things» по рабочей тетради: домашки 1–7 (черновики)',
           f"update classroom_lessons set sort_order = 10 where id = '{TEST}';"]
    for i, (nazv, bloki) in enumerate(UROKI):
        out.append(sql_uroka(UNIT, nazv, i, bloki))
    io.open(put, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(put, sum(len(b) for _, b in UROKI), 'блоков,', os.path.getsize(put) // 1024, 'КБ')
