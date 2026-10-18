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


emit('u0_test', TEST, 'SM3 · Unit 0 · Test — к уроку Lesson 5 «Revision + Test»',
     'Test', 'test', 5, 90)
