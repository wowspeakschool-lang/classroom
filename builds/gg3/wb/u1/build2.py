# -*- coding: utf-8 -*-
"""Go Getter 3, юнит 1 по рабочей тетради — домашки 3–7 (разделы 1.3–1.7)."""
import json, io

MEDIA = 'https://classroom.wowteach.ru/media/'
BUCKET = 'https://api.wowteach.ru/storage/v1/object/public/classroom-media/gg3%20wb/'
UNIT = '96161506-701b-4074-9115-ee113b71a739'   # Unit 1 · Life at home
A2 = BUCKET + 'GG%20L3%20WkBk%20A2.mp3'
A3 = BUCKET + 'GG%20L3%20WkBk%20A3.mp3'
VF = [{'text': 'Верно'}, {'text': 'Неверно'}]


def privet(kartinka, zagolovok, text):
    return ('text', {'html': f'<p><img src="{MEDIA}shared/gg/{kartinka}" alt="" style="height:200px"></p>'
                             f'<h2>{zagolovok}</h2><p>{text}</p>'})


def poka(kartinka, text):
    return ('text', {'html': f'<p><img src="{MEDIA}shared/gg/{kartinka}" alt="" style="height:200px"></p><p>{text}</p>'})


def q(text, options, correct, image=None):
    d = {'q': text, 'type': 'single', 'correct': [correct],
         'options': [{'text': o} for o in options]}
    if image:
        d['image'] = MEDIA + image
    return d


# ───────────────────────── ДЗ 3 · 1.3 Present Simple и Present Continuous ────
PREDL = [
    "She's dancing right now.", "I'm working at home.", 'Dad often drinks tea.',
    'They play chess at the weekend.', "We're doing our English homework now.",
    'He gets up early every day.',
]

hw3 = [
    privet('hello_books.webp', 'Unit 1 · Life at home',
           'Present Simple и Present Continuous: что происходит обычно, а что прямо сейчас.'),
    ('sort', {'title': 'Распредели выражения времени', 'groups': [
        {'name': 'Сейчас', 'items': [{'text': 'right now'}, {'text': 'at the moment'}, {'text': 'today'}]},
        {'name': 'Регулярно', 'items': [{'text': 'always'}, {'text': 'often'}, {'text': 'on Mondays'},
                                        {'text': 'at the weekend'}, {'text': 'every week'}, {'text': 'sometimes'}]},
    ]}),
    ('order', {'title': 'Расставь слова по порядку', 'items': [
        {'words': s.split(), 'sentence': s} for s in PREDL]}),
    ('quiz', {'title': 'Прочитай предложение и выбери, когда это происходит', 'questions': [
        q(PREDL[0], ['Сейчас', 'Регулярно'], 0),
        q(PREDL[1], ['Сейчас', 'Регулярно'], 0),
        q(PREDL[2], ['Сейчас', 'Регулярно'], 1),
        q(PREDL[3], ['Сейчас', 'Регулярно'], 1),
        q(PREDL[4], ['Сейчас', 'Регулярно'], 0),
        q(PREDL[5], ['Сейчас', 'Регулярно'], 1),
    ]}),
    ('match', {'title': 'Соедини начало и конец предложения', 'pairs': [
        {'left': 'What are', 'right': 'you doing?'},
        {'left': 'Mum never', 'right': 'gets up late.'},
        {'left': 'My teacher is', 'right': 'telling us a story.'},
        {'left': 'We always', 'right': 'meet on Fridays.'},
        {'left': 'Are they', 'right': 'playing basketball?'},
        {'left': "I'm not going", 'right': 'to school.'},
    ]}),
    ('quiz', {'title': 'Выбери правильную форму глагола', 'questions': [
        q('Doctor Q ___ in his lab all day, every day.', ['works', 'is working'], 0),
        q('He usually ___ at eight o’clock in the morning.', ['is starting', 'starts'], 1),
        q('But today Doctor Q ___ his time outside the garage.', ['spends', 'is spending'], 1),
        q('Right now Pi and Doctor Q ___!', ['skateboard', 'are skateboarding'], 1),
        q('Millie is surprised because Doctor Q never ___.', ['skateboards', 'is skateboarding'], 0),
        q('Doctor Q isn’t all right. He ___ to bed now.', ['goes', 'is going'], 1),
    ]}),
    ('gaps', {'title': 'Прочитай блог Фреда и выбери правильную форму глагола', 'mode': 'choice', 'text':
        "This is George. He often __goes__ to the park. He usually __hangs out__ with his friends, "
        "Peter and Jess. They usually __ride__ their bikes.\n"
        "But today George __isn't riding__ his bike. He __is skateboarding__ with Peter and Jess at a skatepark.\n"
        "— Hi, George! __Are you having__ fun?\n"
        "— Yes! I __am learning__ some new jumps. It isn't easy!",
        'choices': [['is going', 'go'], ['is hanging out', 'hang out'], ['are riding', 'rides'],
                    ["doesn't ride", "isn't ride"], ['skateboards', 'skateboard'],
                    ['Do you have', 'Are you have'], ['learn', 'is learning']]}),
    ('task', {'title': 'Ответь за Джорджа ✍️', 'needs_review': True, 'html':
        '<p>Джордж из блога отвечает на вопросы. Напиши его ответы — по предложению на каждый вопрос.</p>'
        '<p>1 Where do you usually hang out with your friends?<br>'
        '2 What do you do there?<br>'
        '3 Where are you meeting Peter and Jess today?<br>'
        '4 What are you doing now?<br>'
        '5 Are you having fun?</p>'
        '<p><i>Например: I usually hang out at the sports centre.</i></p>'}),
    poka('bye_medal.webp', 'Дальше — как попросить о помощи и предложить свою.'),
]

# ───────────────────────── ДЗ 4 · 1.4 Communication ──────────────────────────
hw4 = [
    privet('hello_highfive.webp', 'Unit 1 · Life at home',
           'Как попросить о помощи, как предложить её и что ответить.'),
    ('text', {'audio': A2, 'html':
        '<h3>Asking for help</h3><p>Can you help me <i>with the sofa</i>, please?<br>'
        'Can you move <i>the coffee table</i>, please?</p>'
        '<h3>Reacting</h3><p>No problem. / Yes, of course.<br>I’m sorry, I can’t. I’m busy right now.</p>'
        '<h3>Offering help</h3><p>Can I help you <i>with the lamp</i>?<br>'
        'Do you need any help <i>with the lamp</i>?</p>'
        '<h3>Reacting</h3><p>Yes, please. / No, that’s fine, thank you.</p>'
        '<p>Послушай запись и повтори фразы вслух.</p>'}),
    ('gaps', {'title': 'Прочитай разговор и перетащи слова в пропуски', 'mode': 'drag', 'text':
        "Mum: Can you __help__ me with the living room, please?\n"
        "Bob: Yes, __of course__, Mum.\n"
        "Mum: __Can__ you clear the table, Dan?\n"
        "Dan: __No__ problem, Mum.\n"
        "Bob: Do you __need__ any help with the bedrooms?\n"
        "Mum: Yes, __please__. We can make the beds next.\n"
        "Dan: Can I help you __with__ the car? I like washing the car!\n"
        "Mum: No, that's __fine__, thank you. The car is clean."}),
    ('quiz', {'title': 'Выбери подходящий ответ', 'questions': [
        q('Мама просит: «Can you help me with the table, please?» Ты согласен.',
          ['Yes, please.', 'Yes, of course.', 'No, that’s fine, thank you.'], 1),
        q('Сестра предлагает: «Can I help you with your homework?» Помощь нужна.',
          ['Yes, please.', 'No problem.', 'I’m sorry, I can’t.'], 0),
        q('Друг просит помочь, но ты сейчас занят.',
          ['No, that’s fine, thank you.', 'Yes, please.', 'I’m sorry, I can’t. I’m busy right now.'], 2),
        q('Бабушка предлагает помощь, но она не нужна.',
          ['No problem.', 'No, that’s fine, thank you.', 'Yes, of course.'], 1),
    ]}),
    ('order', {'title': 'Расставь слова по порядку', 'items': [
        {'words': 'Do you need any help with the shopping?'.split(),
         'sentence': 'Do you need any help with the shopping?', 'prompt': 'вопрос'},
        {'words': "No, that's fine, thank you.".split(),
         'sentence': "No, that's fine, thank you.", 'prompt': 'ответ'},
        {'words': 'Can you help me with the washing, please?'.split(),
         'sentence': 'Can you help me with the washing, please?', 'prompt': 'вопрос'},
        {'words': "I'm sorry, I can't. I'm busy right now.".split(),
         'sentence': "I'm sorry, I can't. I'm busy right now.", 'prompt': 'ответ'},
    ]}),
    ('gaps', {'title': 'Впиши по одному слову', 'mode': 'type', 'text':
        "__Do__ you need any help with the sofa?\n"
        "Can you move the table, __please__?\n"
        "Can __you__ help me with the dishes?"}),
    ('speaking', {'title': 'Разыграй разговор 🎤', 'needs_review': True, 'html':
        '<p>Дома генеральная уборка. Попроси кого-то о помощи, а потом предложи свою. '
        'Скажи четыре реплики: просьба — ответ — предложение помощи — ответ.</p>'
        '<p><i>Например: Can you help me with the window, please?</i></p>'}),
    poka('bye_trophy.webp', 'Дальше — текст о характере.'),
]

# ───────────────────────── ДЗ 5 · 1.5 Reading ────────────────────────────────
TEST_HTML = (
    '<h3>Do my personality quiz!</h3>'
    '<p><b>1 Your friend wants to see a cartoon at the cinema on Monday. You …</b><br>'
    'A go and have fun.<br>B do your homework first and then go.<br>'
    'C don’t go because you don’t like cartoons.</p>'
    '<p><b>2 Your mum asks you to tidy your room. You …</b><br>'
    'A tidy it and listen to music.<br>B don’t tidy it. It’s always tidy!<br>'
    'C don’t tidy it. You like it messy.</p>'
    '<p><b>3 You are at a café. Your friends are late. You …</b><br>'
    'A wait and play games on your phone.<br>B send them lots of texts.<br>'
    'C don’t wait and ask for a lemonade.</p>'
    '<p><b>4 You want to listen to music. You …</b><br>'
    'A play it on speakers and dance around the room.<br>'
    'B listen on headphones in your bedroom.<br>'
    'C listen in the kitchen and tell your family to listen too.</p>'
    '<p><b>Mostly A</b> — You are easy-going and patient. Sometimes you are loud.<br>'
    '<b>Mostly B</b> — You are organised and tidy. You are usually easy-going.<br>'
    '<b>Mostly C</b> — You are bossy and a bit messy. You like having fun.</p>')

hw5 = [
    privet('hello_girl_wave.webp', 'Unit 1 · Life at home',
           'Читаем тест о характере и разбираем слова, которыми описывают людей.'),
    ('text', {'html': TEST_HTML}),
    ('gaps', {'title': 'Перетащи слова в пропуски', 'mode': 'drag', 'text':
        "John is __bossy__. He tells everybody what to do.\n"
        "The kids make a lot of noise. They are __loud__.\n"
        "I'm __messy__. There are clothes on the floor and books on the bed.\n"
        "The teacher is __patient__. He waits for all the students to finish.\n"
        "Dad is __organised__. He uploads his photos to his tablet every day.\n"
        "Susan is __quiet__. She never makes a noise.\n"
        "Aunt Jane is an __easy-going__ person. She doesn't tell us what to do or when to do it.\n"
        "The twins always put away their clothes and toys. They're __tidy__ children."}),
    ('quiz', {'title': 'Выбери лучший заголовок для теста', 'material': TEST_HTML, 'questions': [
        q('', ['What do you like?', 'What are you like?', 'What are you doing?'], 1)]}),
    ('quiz', {'title': 'Прочитай тест ещё раз. Верно или неверно?', 'material': TEST_HTML, 'questions': [
        q('The quiz tells you about your personality.', ['Верно', 'Неверно'], 0),
        q('Question 1 is about seeing a film.', ['Верно', 'Неверно'], 0),
        q('Question 2 is about chores.', ['Верно', 'Неверно'], 0),
        q('Question 3 is about shopping.', ['Верно', 'Неверно'], 1),
        q('In question 1, one answer is about a drink.', ['Верно', 'Неверно'], 1),
        q('In question 2, one answer is about homework.', ['Верно', 'Неверно'], 1),
        q('In question 3, two answers are about phones.', ['Верно', 'Неверно'], 0),
        q('There are four results.', ['Верно', 'Неверно'], 1),
    ]}),
    ('quiz', {'title': 'Прочитай комментарии и выбери правильный вариант', 'questions': [
        q('Dave: I ___ your quiz! It’s great! I am mostly C and yes, I am bossy!', ['love', 'hate'], 0),
        q('Charlie: I ___ with your quiz! It isn’t right. I am mostly A. But I’m not loud! I’m quiet!',
          ['agree', 'don’t agree'], 1),
        q('Anita: I ___ with everything! I am mostly B and it’s true, I am tidy and easy-going.',
          ['agree', 'don’t agree'], 0),
    ]}),
    ('task', {'title': 'Пройди тест и напиши свой комментарий ✍️', 'needs_review': True, 'material': TEST_HTML,
              'html':
        '<p>Выбери ответы A, B или C и посмотри результат. Напиши три предложения: '
        'согласен ты с тестом или нет, какая у тебя буква и какой ты на самом деле.</p>'
        '<p><i>Например: I don’t agree with the quiz. It isn’t right.</i></p>'}),
    poka('bye_popper.webp', 'Дальше — задание на слух и письмо.'),
]

# ───────────────────────── ДЗ 6 · 1.6 Listening and Writing ──────────────────
DELA = [('vacuum the floor', 'vacuum_room.webp'), ('empty the dishwasher', 'empty_dishwasher.webp'),
        ('feed the dog', 'feed_dog.webp'), ('take out the rubbish', 'take_rubbish.webp'),
        ('set the table', 'set_table.webp'), ('make my bed', 'make_bed.webp')]

hw6 = [
    privet('hello_laptop.webp', 'Unit 1 · Life at home',
           'Слушаем, кто какие дела делает по дому, и пишем о знакомом человеке.'),
    ('quiz', {'title': 'Посмотри на картинку и выбери подпись', 'questions': [
        q('', ['vacuum the floor', 'water the plants', 'iron my T-shirt'], 0, 'gg3/u1/vacuum_room.webp'),
        q('', ['clear the table', 'empty the dishwasher', 'cook lunch'], 1, 'gg3/u1/empty_dishwasher.webp'),
        q('', ['feed the dog', 'tidy my room', 'wash the dishes'], 0, 'gg3/u1/feed_dog.webp'),
        q('', ['make my bed', 'put away my clothes', 'take out the rubbish'], 2, 'gg3/u1/take_rubbish.webp'),
        q('', ['load the washing machine', 'set the table', 'water the plants'], 1, 'gg3/u1/set_table.webp'),
        q('', ['iron my T-shirt', 'wash the dishes', 'make my bed'], 2, 'gg3/u1/make_bed.webp'),
    ]}),
    ('match', {'title': 'Послушай запись и соедини имя с делом по дому', 'audio': A3, 'pairs': [
        {'left': 'Fred', 'right': 'vacuum the floor'},
        {'left': 'Gary', 'right': 'feed the dog'},
        {'left': 'Arthur', 'right': 'take out the rubbish'},
        {'left': 'Nelly', 'right': 'set the table'},
        {'left': 'Walter', 'right': 'empty the dishwasher'},
        {'left': 'Mary', 'right': 'make my bed'},
    ]}),
    ('quiz', {'title': 'Послушай запись ещё раз и выбери правильный вариант', 'audio': A3, 'questions': [
        q('Fred tidies his room on …', ['Fridays', 'Saturdays', 'Sundays'], 1),
        q('Gary ___ looks after his sister at the weekend.', ['sometimes', 'never', 'always'], 0),
        q('Arthur helps at home after …', ['breakfast', 'lunch', 'dinner'], 2),
        q('Nelly …', ['loads the dishwasher', 'hasn’t got a dishwasher', 'doesn’t like the dishwasher'], 1),
        q('Walter ___ chores.', ['likes', 'hates', 'doesn’t do'], 1),
        q('Mary does lots of chores …', ['every day', 'at the weekend', 'on Mondays'], 0),
    ]}),
    ('gaps', {'title': 'Прочитай текст и выбери подходящее слово', 'mode': 'choice', 'text':
        "Ellen is my neighbour. In her family, the children and parents don't do a lot of things together "
        "on weekdays. They never have breakfast as a family __because__ her mum and dad leave for work early. "
        "The family don't have lunch together, __but__ they always eat dinner at home.\n"
        "On Saturdays, Ellen does her chores. She tidies her bedroom __and__ she loads the washing machine. "
        "Amy, her sister, often helps her. Then they watch TV __and__ hang out with their friends. "
        "On Sundays, Ellen, Amy and their parents often go to the park. They don't have a car, __so__ they take a bus.",
        'choices': [['but'], ['so'], ['so'], ['because'], ['because']]}),
    ('task', {'title': 'Напиши о человеке, которого хорошо знаешь ✍️', 'needs_review': True, 'html':
        '<p>Выбери человека — друга, соседа, родственника — и напиши о нём 5–6 предложений. '
        'Ответь по порядку:</p>'
        '<p>1 что он делает в будни;<br>2 какие дела по дому он делает в выходные;<br>'
        '3 что вы делаете вместе в выходные.</p>'
        '<p>Свяжи предложения словами <b>and</b>, <b>but</b>, <b>because</b>, <b>so</b>.</p>'
        '<p><i>Например: Andy is my cousin. He gets up at seven, so he always has breakfast at home.</i></p>'}),
    poka('bye_star.webp', 'Остался последний шаг — проверь себя.'),
]

# ───────────────────────── ДЗ 7 · 1.7 Check yourself ─────────────────────────
hw7 = [
    privet('hello_girl_wave.webp', 'Unit 1 · Проверь себя',
           'Повторяем весь юнит: слова о характере, дела по дому, два времени и просьбы о помощи.'),
    ('gaps', {'title': 'Прочитай текст о семье Боба и перетащи слова в пропуски', 'mode': 'drag', 'text':
        "Dad is cool, but he's bossy. He tells everybody what to do. But my sister never listens to him "
        "and she never tidies her room. She's very __messy__.\n"
        "Grandpa is lots of fun. He doesn't mind what we watch on TV or what we play. He's very __easy-going__.\n"
        "My grandma likes planning everything because she's __organised__. She plans the best holidays and trips.\n"
        "I have a baby brother. He's not in the photo. He cries a lot and he makes a lot of noise. He's very __loud__!\n"
        "Luckily, Mum is __patient__ and she doesn't get angry."}),
    ('quiz', {'title': 'Записка мамы: выбери правильное слово', 'questions': [
        q('___ your beds.', ['Set', 'Make'], 1),
        q('___ your T-shirts.', ['Iron', 'Vacuum'], 0),
        q('Water the ___ in the garden.', ['dogs', 'plants'], 1),
        q('___ out the rubbish.', ['Hang', 'Take'], 1),
        q('___ the floor in the living room.', ['Load', 'Vacuum'], 1),
    ]}),
    ('quiz', {'title': 'Выбери правильную форму глагола', 'questions': [
        q('I usually ___ a snack in the morning.', ['have', 'am having'], 0),
        q('He ___ his friend right now.', ['texts', 'is texting'], 1),
        q('She ___ this film!', ['loves', 'is loving'], 0),
        q('What ___ at the moment?', ['do you do', 'are you doing'], 1),
        q('Grandpa often ___ tennis at the weekend.', ['plays', 'is playing'], 0),
    ]}),
    ('gaps', {'title': 'Прочитай телефонный разговор и выбери правильную форму', 'mode': 'choice', 'text':
        "Andy: Are you doing your chores?\n"
        "Beth: No, __I'm not__. __I'm playing__ a new video game.\n"
        "Andy: Oh. Is Fred there?\n"
        "Beth: Yes. Do you want to speak to him?\n"
        "Andy: Yes, please.\n"
        "Beth: Just a minute. __He's tidying__ his room. Fred! It's Andy on the phone.\n"
        "Fred: Hi, Andy.\n"
        "Andy: Hi. I'm with Bob and __we're watching__ TV, but it's boring. Do you want to go to the park with us?\n"
        "Fred: Sure. __I'm not doing__ anything important right now. Let's meet in five minutes.",
        'choices': [["I don't", 'I amn’t'], ['I play', 'I playing'], ['He tidies', 'He tidy'],
                    ['we watch', 'we watching'], ["I don't do", "I'm not do"]]}),
    ('gaps', {'title': 'Впиши по одному слову в каждый пропуск', 'mode': 'drag', 'text':
        "A: Do you need __any__ help with the sofa?\n"
        "B: Yes, __please__.\n"
        "A: Can you help __me__ with the chair, please?\n"
        "B: Yes, of __course__.\n"
        "A: Can I help you with the lamp?\n"
        "B: No, that's __fine__, thank you."}),
    ('speaking', {'title': 'Расскажи о делах по дому 🎤', 'needs_review': True, 'html':
        '<p>Расскажи, кто что делает у вас дома и что делаешь прямо сейчас ты. '
        'Скажи 4–5 предложений и используй оба времени.</p>'
        '<p><i>Например: My brother usually waters the plants. Right now he is doing his homework.</i></p>'}),
    poka('bye_certificate.webp', 'Юнит 1 пройден. Дальше — тест юнита.'),
]

UROKI = [('Homework 3', 2, hw3), ('Homework 4', 3, hw4), ('Homework 5', 4, hw5),
         ('Homework 6', 5, hw6), ('Homework 7', 6, hw7)]

out = io.StringIO()
out.write('-- Go Getter 3, юнит 1 по рабочей тетради: домашки 3–7 (черновики)\n')
for title, so, bloki in UROKI:
    out.write(f"""
do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '{UNIT}' and title = '{title}';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('{UNIT}', '{title}', {so}, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = {so}, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
""")
    for i, (typ, payload) in enumerate(bloki):
        js = json.dumps(payload, ensure_ascii=False)
        out.write(f"  insert into classroom_blocks (lesson_id, type, payload, sort_order)\n"
                  f"  values (v_lesson, '{typ}', $blk${js}$blk$::jsonb, {i});\n")
    out.write('end $$;\n')

io.open('/home/user/classroom/builds/gg3/wb/u1/u1_hw3_hw7.sql', 'w', encoding='utf-8').write(out.getvalue())
print('уроков:', len(UROKI), '· блоков:', sum(len(b) for _, _, b in UROKI), '· байт:', len(out.getvalue()))
