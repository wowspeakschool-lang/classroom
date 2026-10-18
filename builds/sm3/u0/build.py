# -*- coding: utf-8 -*-
"""SM3 · Unit 0 — сборка уроков в SQL и JSON.

    python3.13 builds/sm3/u0/build.py

Пока собран тест юнита. Домашки 1–4 добавляются в этот же файл.
Юнита 0 в базе нет — SQL заводит его сам: «Unit 0 · Meet The Explorers»,
sort_order 0, перед Unit 1 · School.

Звук везде размечен audio_tts — синтезирует методист кнопкой «Озвучить пачкой».
Картинка одна: семейное дерево, вырезано из учебника (media/sm3/u0).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
M = '@@MEDIA@@sm3/u0/'


def t(html):
    return 'text', {'html': html}


def tts(text):
    return {'audio': '', 'audio_tts': text}


def quiz(title, questions):
    return 'quiz', {'title': title, 'questions': questions, 'needs_review': False}


def q(qtext, options, correct, audio=None):
    o = {'q': qtext, 'type': 'single', 'correct': [correct],
         'options': [{'text': x} for x in options]}
    if audio:
        o.update(tts(audio))
    return o


def order(words, sentence):
    return 'order', {'words': words, 'sentence': sentence, **tts(sentence)}


def speaking(title, html):
    return 'speaking', {'title': title, 'html': html, 'needs_review': True}


TEST = [
    t('<p>Сегодня у нас с тобой тест по нулевому юниту. Проверим числа, '
      'be good at, семью и историю про The Explorers. Уверена, ты справишься!</p>'),

    quiz('Послушай и выбери число.', [
        q('', ['24', '42', '14'], 0, 'twenty-four'),
        q('', ['93', '39', '49'], 1, 'thirty-nine'),
        q('', ['52', '25', '15'], 0, 'fifty-two'),
        q('', ['67', '76', '70'], 1, 'seventy-six'),
        q('', ['10', '90', '100'], 2, 'one hundred'),
    ]),

    quiz('Прочитай диалог и выбери пропущенное слово.', [
        q('A: Where’s your bedroom?<br>B: It’s ___. My room is on the second floor.',
          ['upstairs', 'downstairs', 'in the cellar'], 0),
        q('A: Where’s the kitchen?<br>B: It’s ___, next to the front door.',
          ['upstairs', 'downstairs', 'in the cellar'], 1),
        q('A: It’s dark here and there are a lot of old boxes. Where are you?<br>B: I’m ___.',
          ['upstairs', 'downstairs', 'in the cellar'], 2),
    ]),

    quiz('Выбери правильный вариант.', [
        q('She’s good at ___ the guitar.', ['playing', 'play', 'plays'], 0),
        q('I’m not good at ___ lies.', ['telling', 'tell', 'to tell'], 0),
        q('___ you good at swimming?', ['Are', 'Do', 'Is'], 0),
        q('Ben and Lucy ___ good at climbing trees.', ['are', 'is', 'do'], 0),
        q('Lucy isn’t good ___ painting.', ['at', 'in', 'on'], 0),
    ]),

    order(['I’m', 'good at', 'riding', 'a bike.'], 'I’m good at riding a bike.'),
    order(['She', 'isn’t', 'good at', 'playing', 'football.'],
          'She isn’t good at playing football.'),
    order(['Nick', 'is', 'Julia’s', 'grandson.'], 'Nick is Julia’s grandson.'),
    order(['Paula and Zoe', 'are', 'Nick’s', 'cousins.'],
          'Paula and Zoe are Nick’s cousins.'),

    quiz('Выбери правильный вариант.', [
        q('Tom is Simon___ father.', ['’s', 's', 's’'], 0),
        q('She’s Greg___ sister.', ['’s', 's', 's’'], 0),
        q('Nick’s dog is big. Who has got the dog?', ['Nick', 'the dog', 'Nick’s friend'], 0),
        q('Jack is Nick’s grandfather. So Nick is Jack’s ___.',
          ['grandson', 'son', 'uncle'], 0),
    ]),

    t('<p><b>Посмотри на семейное дерево и впиши слово.</b></p>'
      f'<p style="text-align:center"><img src="{M}family_tree.webp" alt=""></p>'),

    ('exact_input', {'items': [
        {'prompt': '1. Julia is Penny’s ___.', 'accept': ['grandmother', 'Grandmother']},
        {'prompt': '2. Claire is Julia’s ___.', 'accept': ['daughter', 'Daughter']},
        {'prompt': '3. Oliver is Nick’s ___.', 'accept': ['uncle', 'Uncle']},
        {'prompt': '4. Paula is Zoe’s ___.', 'accept': ['sister', 'Sister']},
    ], 'needs_review': False}),

    ('truefalse', {'title': 'История «The old book» — верно или неверно?',
                   'statements': [
                       {'text': 'Ben and Lucy are in a castle.', 'correct': True},
                       {'text': 'Ben and Lucy find an old book.', 'correct': True},
                       {'text': 'Horax and Zelda help Ben and Lucy.', 'correct': False},
                       {'text': 'Zelda ties Lucy up.', 'correct': True},
                       {'text': 'Buster helps The Explorers to get the book back.',
                        'correct': True},
                       {'text': 'Horax and Zelda have got the book at the end.',
                        'correct': False},
                   ]}),

    quiz('Выбери слово, в котором такой же гласный звук.', [
        q('<b>cat</b>', ['hat', 'cake', 'car'], 0),
        q('<b>pet</b>', ['ten', 'tree', 'me'], 0),
        q('<b>big</b>', ['fish', 'bike', 'five'], 0),
        q('<b>cup</b>', ['run', 'cube', 'blue'], 0),
    ]),

    speaking('SPEAKING TASK 🎤',
             '<p>Расскажи про себя и свою семью, 5–7 предложений. Нажми на микрофон '
             'и запиши ответ.</p>'
             '<p><i>For example:<br>I’m good at swimming, but I’m not good at '
             'painting.<br>This is my mum’s sister. She’s my aunt.<br>Her son is my '
             'cousin.</i></p>'),

    t('<p>Ты справился! 🌟 Это был тест за весь нулевой юнит: числа, комнаты, '
      'be good at, семья и история про The Explorers.</p>'),
]


def gaps(title, text, mode='type'):
    return 'gaps', {'title': title, 'text': text, 'mode': mode}


def exact(title, items):
    return 'exact_input', {'title': title, 'items': items, 'needs_review': False}


def qimg(qtext, images, correct, audio=None):
    o = {'q': qtext, 'type': 'single', 'correct': [correct],
         'options': [{'image': M + i + '.webp'} for i in images]}
    if audio:
        o.update(tts(audio))
    return o


def pic(name, alt=''):
    return f'<p style="text-align:center"><img src="{M}{name}.webp" alt="{alt}"></p>'


# ══════════════════════════════════════════════════════════════════════════
# ДЗ 1 — Lesson 1: upstairs / downstairs / cellar, числа 21–100
# ══════════════════════════════════════════════════════════════════════════
HW1 = [
    t('<p>Привет! 👋 В этой домашке повторим числа от 21 до 100 и новые слова: '
      '<b>upstairs</b>, <b>downstairs</b>, <b>cellar</b>.</p>'),

    quiz('Посмотри на картинку и выбери правильный вариант.', [
        {'q': 'Where is the cat?', 'type': 'single', 'correct': [0],
         'image': M + 'house_upstairs.webp',
         'options': [{'text': 'Upstairs.'}, {'text': 'Downstairs.'},
                     {'text': 'In the cellar.'}]},
        {'q': 'Where is the cat?', 'type': 'single', 'correct': [1],
         'image': M + 'house_downstairs.webp',
         'options': [{'text': 'Upstairs.'}, {'text': 'Downstairs.'},
                     {'text': 'In the cellar.'}]},
        {'q': 'Where is the cat?', 'type': 'single', 'correct': [2],
         'image': M + 'house_cellar.webp',
         'options': [{'text': 'Upstairs.'}, {'text': 'Downstairs.'},
                     {'text': 'In the cellar.'}]},
    ]),

    quiz('Послушай и выбери число.', [
        q('', ['34', '43', '14'], 0, 'thirty-four'),
        q('', ['17', '70', '77'], 1, 'seventy'),
        q('', ['58', '85', '55'], 0, 'fifty-eight'),
        q('', ['61', '16', '66'], 0, 'sixty-one'),
        q('', ['99', '79', '19'], 0, 'ninety-nine'),
    ]),

    exact('Прочитай число словами и впиши его цифрами.', [
        {'prompt': '1. forty-two', 'accept': ['42']},
        {'prompt': '2. sixty-three', 'accept': ['63']},
        {'prompt': '3. eighty-seven', 'accept': ['87']},
        {'prompt': '4. one hundred', 'accept': ['100']},
    ]),

    gaps('Вставь пропущенные слова: upstairs · downstairs · cellar.',
         'My bedroom is __upstairs__.\n'
         'The kitchen is __downstairs__, next to the front door.\n'
         'The old boxes are in the __cellar__.'),

    order(['My', 'bedroom', 'is', 'upstairs.'], 'My bedroom is upstairs.'),
    order(['The', 'cellar', 'is', 'under', 'the house.'],
          'The cellar is under the house.'),

    speaking('SPEAKING TASK 🎤',
             '<p>Расскажи про свой дом или квартиру, 4–5 предложений. Нажми на '
             'микрофон и запиши ответ.</p>'
             '<p><i>For example:<br>My bedroom is upstairs.<br>The kitchen is '
             'downstairs.<br>We haven’t got a cellar.</i></p>'),

    t('<p>Молодец! 🌟 Теперь ты знаешь, где upstairs, где downstairs и что такое '
      'cellar, и считаешь до ста.</p>'),
]

# ══════════════════════════════════════════════════════════════════════════
# ДЗ 2 — Lesson 2: be good at + Ving
# ══════════════════════════════════════════════════════════════════════════
HW2 = [
    t('<p>Привет! 👋 В этой домашке тренируем <b>be good at + Ving</b> — '
      'рассказываем, что получается хорошо, а что не очень.</p>'),

    quiz('Посмотри на картинку и выбери правильный вариант.', [
        {'q': 'What is she good at?', 'type': 'single', 'correct': [0],
         'image': M + 'act_dancing.webp',
         'options': [{'text': 'dancing'}, {'text': 'painting'}, {'text': 'swimming'}]},
        {'q': 'What is he good at?', 'type': 'single', 'correct': [1],
         'image': M + 'act_painting.webp',
         'options': [{'text': 'climbing'}, {'text': 'painting'}, {'text': 'riding a bike'}]},
        {'q': 'What is she good at?', 'type': 'single', 'correct': [2],
         'image': M + 'act_swimming.webp',
         'options': [{'text': 'dancing'}, {'text': 'playing football'}, {'text': 'swimming'}]},
        {'q': 'What is he good at?', 'type': 'single', 'correct': [1],
         'image': M + 'act_football.webp',
         'options': [{'text': 'swimming'}, {'text': 'playing football'}, {'text': 'painting'}]},
        {'q': 'What is she good at?', 'type': 'single', 'correct': [0],
         'image': M + 'act_riding.webp',
         'options': [{'text': 'riding a bike'}, {'text': 'climbing trees'}, {'text': 'dancing'}]},
        {'q': 'What is he good at?', 'type': 'single', 'correct': [2],
         'image': M + 'act_climbing.webp',
         'options': [{'text': 'swimming'}, {'text': 'painting'}, {'text': 'climbing trees'}]},
    ]),

    quiz('Выбери правильный вариант.', [
        q('I’m good at ___ pictures.', ['painting', 'paint', 'paints'], 0),
        q('He isn’t good at ___ football.', ['playing', 'play', 'played'], 0),
        q('___ she good at dancing?', ['Is', 'Does', 'Do'], 0),
        q('We ___ good at climbing trees.', ['are', 'is', 'am'], 0),
        q('They aren’t good ___ swimming.', ['at', 'in', 'to'], 0),
    ]),

    exact('Поставь глагол в правильную форму.', [
        {'prompt': '1. I’m good at ___ (ride) a bike.', 'accept': ['riding', 'Riding']},
        {'prompt': '2. She’s not good at ___ (tell) lies.', 'accept': ['telling', 'Telling']},
        {'prompt': '3. Are you good at ___ (dance)?', 'accept': ['dancing', 'Dancing']},
        {'prompt': '4. He’s good at ___ (climb) trees.', 'accept': ['climbing', 'Climbing']},
    ]),

    order(['I’m', 'good at', 'playing', 'the guitar.'], 'I’m good at playing the guitar.'),
    order(['Lucy', 'isn’t', 'good at', 'painting.'], 'Lucy isn’t good at painting.'),
    order(['Are', 'you', 'good at', 'doing', 'puzzles?'], 'Are you good at doing puzzles?'),

    speaking('SPEAKING TASK 🎤',
             '<p>Расскажи, что у тебя получается хорошо, а что не очень — '
             '4–6 предложений. Нажми на микрофон и запиши ответ.</p>'
             '<p><i>For example:<br>I’m good at swimming and riding a bike.<br>'
             'I’m not good at painting.<br>My friend is good at playing football.</i></p>'),

    t('<p>Отлично! 🌟 Теперь ты умеешь рассказать, в чём ты хорош, и спросить '
      'об этом друга.</p>'),
]

HEAD = """\
-- {title}
-- Собрано скриптом builds/sm3/u0/build.py. Не заливать, пока не назовут,
-- куда переехала платформа. Проверка:
--   python3.13 tools/val.py builds/sm3/u0 sm3/u0

do $$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm3';
  if v_course is null then raise exception 'курс sm3 не найден'; end if;

  select id into v_unit from classroom_units where course_id = v_course and sort_order = 0;
  if v_unit is null then
    insert into classroom_units (course_id, title, sort_order)
    values (v_course, 'Unit 0 · Meet The Explorers', 0)
    returning id into v_unit;
  end if;

  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and sort_order = {lesson_sort};
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, kind, sort_order, pass_threshold, is_published)
    values (v_unit, '{lesson_title}', '{kind}', {lesson_sort}, {threshold}, false)
    returning id into v_lesson;
  else
    update classroom_lessons
       set title = '{lesson_title}', kind = '{kind}', pass_threshold = {threshold}
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
"""

TAIL = """  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  raise notice '{lesson_title}: % блоков', {n};
end $$;
"""


def emit(name, blocks, title, lesson_title, kind, lesson_sort, threshold):
    rows = []
    for i, (typ, payload) in enumerate(blocks):
        raw = json.dumps(payload, ensure_ascii=False)
        assert '$blk$' not in raw
        rows.append(f"    (v_lesson, '{typ}', replace($blk${raw}$blk$, "
                    f"'@@MEDIA@@', v_media)::jsonb, {i})")
    sql = (HEAD.format(title=title, lesson_title=lesson_title, kind=kind,
                       lesson_sort=lesson_sort, threshold=threshold)
           + ',\n'.join(rows) + '\n'
           + TAIL.format(lesson_title=lesson_title, n=len(blocks)))
    open(f'{HERE}/{name}.sql', 'w').write(sql)
    open(f'{HERE}/{name}.json', 'w').write(json.dumps({
        'course': 'sm3', 'unit': 'Unit 0 · Meet The Explorers', 'unit_sort_order': 0,
        'lesson': lesson_title, 'kind': kind, 'lesson_sort_order': lesson_sort,
        'pass_threshold': threshold, 'is_published': False,
        'media_base': 'https://classroom.wowteach.ru/media/',
        'blocks': [{'sort_order': i, 'type': ty, 'payload': p}
                   for i, (ty, p) in enumerate(blocks)],
    }, ensure_ascii=False, indent=1))
    print(f'{name}: {len(blocks)} блоков → {name}.sql, {name}.json')


emit('u0_hw1', HW1, 'SM3 · Unit 0 · Homework 1 — к уроку Lesson 1',
     'Homework 1', 'homework', 0, 60)
emit('u0_hw2', HW2, 'SM3 · Unit 0 · Homework 2 — к уроку Lesson 2',
     'Homework 2', 'homework', 1, 60)
emit('u0_test', TEST, 'SM3 · Unit 0 · Test — к уроку Lesson 5 «Revision + Test»',
     'Test', 'test', 5, 90)
