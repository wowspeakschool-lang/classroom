# -*- coding: utf-8 -*-
"""SM0 · Unit 0 — сборка восстановленной ДЗ 1 и теста юнита.

    python3.13 builds/sm0/u0/build.py

Кладёт рядом четыре файла:
    u0_hw1.sql / u0_hw1.json   — Homework 1 (была потеряна, собрана по плану Lesson 1)
    u0_test.sql / u0_test.json — тест юнита (Lesson 6 «Revision + Test»)

SQL пишется в том же виде, что сборки SM2, — его проверяет tools/val.py:
    python3.13 tools/val.py builds/sm0/u0 sm0/legacy

Звук переиспользуется из домашек 2–5 того же юнита: это записи голосом
методиста (файлы *_rec_*.webm в хранилище), поэтому в тесте ребёнок слышит
тот же голос, что в домашках. Новый звук нужен только там, где помечено
AUDIO_NEEDED и audio_tts.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
AUD = 'https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/'
M = '@@MEDIA@@sm0/legacy/'          # подставляется v_media при заливке

# ── звук из домашек юнита 0 ───────────────────────────────────────────────
A = {
    'k':        AUD + '1788808327805_rec_1788808327805.webm',   # ДЗ 5 б3
    'r':        AUD + '1788808314749_rec_1788808314748.webm',   # ДЗ 5 б3
    'e_p':      AUD + '1788806756568_rec_1788806756568.webm',   # ДЗ 4 б3 (два звука)
    'd_a':      AUD + '1788806780166_rec_1788806780166.webm',   # ДЗ 4 б3
    'word_n':   AUD + '1788806302367_rec_1788806302367.webm',   # ДЗ 3 б3
    'word_i':   AUD + '1788806324376_rec_1788806324376.webm',
    'word_p':   AUD + '1788806337276_rec_1788806337276.webm',
    'snd_t':    AUD + '1788459694262_rec_1788459694261.webm',   # ДЗ 2 б3
    'snd_p':    AUD + '1788459890618_rec_1788459890618.webm',
    'sat':      AUD + '1788806353766_rec_1788806353766.webm',   # ДЗ 3 б5
    'kit':      AUD + '1788808132346_rec_1788808132346.webm',   # ДЗ 5 б6
    'col1':     AUD + '1788808191679_rec_1788808191679.webm',   # ДЗ 5 б12
    'col2':     AUD + '1788808198640_rec_1788808198639.webm',
    'col3':     AUD + '1788808205132_rec_1788808205132.webm',
    'col4':     AUD + '1788808211949_rec_1788808211949.webm',
    'col5':     AUD + '1788808218715_rec_1788808218715.webm',
    'num1':     AUD + '1788806448522_rec_1788806448522.webm',   # ДЗ 3 б9
    'num2':     AUD + '1788806458771_rec_1788806458771.webm',
    'num6':     AUD + '1788806475433_rec_1788806475433.webm',
    'num7':     AUD + '1788806485334_rec_1788806485334.webm',
    'num5':     AUD + '1788806494048_rec_1788806494047.webm',
}

# ── картинки (все уже лежат в media/sm0/legacy) ───────────────────────────
IMG = {
    'red': M + '8b38abac4dbc.webp', 'green': M + '481214562a38.webp',
    'blue': M + '34b8efecd4b2.webp', 'orange': M + 'ce01e4bbf55f.webp',
    'pink': M + 'f40c937be9f8.webp', 'yellow': M + 'fccf971c0287.webp',
    'ten_a': M + '627e87247d6d.webp', 'ten_b': M + 'b1483e6028be.webp',
    'ten_c': M + '5390b2ec3d05.webp',
    'colour_count': M + '143c8106fe9d.webp',                    # сцена из ДЗ 5 б14
}


def t(html):
    return 'text', {'html': html}


def q(title, questions):
    p = {'questions': questions, 'needs_review': False}
    if title:
        p['title'] = title
    return 'quiz', p


def single(audio, options, correct, qtext=''):
    o = {'q': qtext, 'type': 'single', 'correct': [correct], 'options': options}
    if audio:
        o['audio'] = audio
    return o


def multi(audio, options, correct, qtext=''):
    return {'q': qtext, 'type': 'multiple', 'audio': audio,
            'correct': correct, 'options': options}


def txt(*words):
    return [{'text': w} for w in words]


def img(*keys):
    return [{'image': IMG[k]} for k in keys]


def tts(text):
    return {'audio': '', 'audio_tts': text}


def order(audio, letters, word):
    p = {'words': list(letters), 'sentence': word}
    if audio:
        p['audio'] = audio
    else:
        p['audio'] = ''
        p['audio_tts'] = word
    return 'order', p


def speaking(title, html):
    return 'speaking', {'title': title, 'html': html, 'needs_review': True}


# ══════════════════════════════════════════════════════════════════════════
# ДЗ 1 юнита 0 — по плану «Unit 0 · Say Hello! — Lesson 1 (Hello)»
# Лексика: Hello! · What's your name? — I'm… · фоника s /s/, a /æ/ · чтение as/sa
# ══════════════════════════════════════════════════════════════════════════
HW1 = [
    t('<p>Привет! 👋 Сегодня повторим, как знакомиться по-английски, '
      'и выучим буквы <b>S</b> и <b>A</b>.</p>'),

    # AUDIO_NEEDED: звук /s/ и /æ/ — записывает методист (имя буквы не годится)
    q('Послушай звук и выбери букву.', [
        {'q': '', 'type': 'single', 'audio': '', 'correct': [0], 'options': txt('s', 'a')},
        {'q': '', 'type': 'single', 'audio': '', 'correct': [1], 'options': txt('s', 'a')},
    ]),

    q('Это большая буква. Выбери её маленькую пару.', [
        {'q': '<b>S</b>', 'type': 'single', 'correct': [0], 'options': txt('s', 'a', 't')},
        {'q': '<b>A</b>', 'type': 'single', 'correct': [1], 'options': txt('s', 'a', 'p')},
    ]),

    q('Послушай вопрос и выбери ответ.', [
        dict(q='', type='single', correct=[0], **tts("What's your name?"),
             options=[{'text': "I'm Misty.", **tts("I'm Misty.")},
                      {'text': 'How are you?', **tts('How are you?')},
                      {'text': 'Hello, hello!', **tts('Hello, hello!')}]),
        dict(q='', type='single', correct=[1], **tts('How are you?'),
             options=[{'text': "I'm Misty.", **tts("I'm Misty.")},
                      {'text': "I'm happy!", **tts("I'm happy!")},
                      {'text': "What's your name?", **tts("What's your name?")}]),
    ]),

    order('', 'as', 'as'),
    order('', 'sa', 'sa'),

    speaking('Нажми на микрофон и прочитай слоги вслух 🎤',
             '<p><b>as &nbsp;·&nbsp; sa &nbsp;·&nbsp; AS &nbsp;·&nbsp; SA</b></p>'),
    speaking('Поздоровайся и назови своё имя 🎤',
             '<p>Нажми на микрофон и скажи: <b>Hello! I’m …</b></p>'),

    t('<p>Молодец! 🌟 Ты познакомился по-английски и сам прочитал '
      'первые слоги — <b>as</b> и <b>sa</b>.</p>'),
]

# ══════════════════════════════════════════════════════════════════════════
# Тест юнита 0 — к уроку Lesson 6 «Revision + Test»
# ══════════════════════════════════════════════════════════════════════════
TEST = [
    t('<p>Сегодня у нас с тобой тест. Проверим, как хорошо ты знаешь буквы, '
      'цвета и числа и умеешь читать слова. Уверена, ты справишься!</p>'),

    ('match', {'title': 'Соедини большую и маленькую букву.',
               'pairs': [{'left': 'S', 'right': 's'}, {'left': 'A', 'right': 'a'},
                         {'left': 'E', 'right': 'e'}, {'left': 'D', 'right': 'd'},
                         {'left': 'R', 'right': 'r'}, {'left': 'K', 'right': 'k'}],
               'needs_review': False}),

    q('Послушай звук и выбери букву.', [
        single(A['r'], txt('r', 'k', 'd'), 0),
        single(A['k'], txt('r', 'k', 'd'), 1),
        multi(A['e_p'], txt('e', 'd', 'p'), [0, 2]),
        multi(A['d_a'], txt('d', 'p', 'a'), [0, 2]),
    ]),

    q('Послушай слово. С какой буквы оно начинается?', [
        single(A['word_n'], txt('n', 'i', 'p'), 0),
        single(A['word_i'], txt('n', 'i', 'p'), 1),
        single(A['word_p'], txt('n', 'i', 'p'), 2),
    ]),

    q('Послушай звук и выбери слово, в котором есть эта буква.', [
        single(A['snd_t'], txt('tap', 'as'), 0),
        single(A['snd_p'], txt('pat', 'sat'), 0),
    ]),

    q('Послушай вопрос и выбери ответ.', [
        dict(q='', type='single', correct=[0], **tts("What's your name?"),
             options=[{'text': "I'm Misty.", **tts("I'm Misty.")},
                      {'text': 'How are you?', **tts('How are you?')},
                      {'text': 'Hello, hello!', **tts('Hello, hello!')}]),
        dict(q='', type='single', correct=[1], **tts('How are you?'),
             options=[{'text': "I'm Misty.", **tts("I'm Misty.")},
                      {'text': "I'm happy!", **tts("I'm happy!")},
                      {'text': "What's your name?", **tts("What's your name?")}]),
    ]),

    order(A['sat'], 'sat', 'sat'),
    order(A['kit'], 'kit', 'kit'),

    q('Послушай цвет и выбери его.', [
        single(A['col1'], img('red', 'green', 'blue'), 0),
        single(A['col2'], img('yellow', 'pink', 'blue'), 1),
        single(A['col3'], img('green', 'red', 'orange'), 2),
        single(A['col4'], img('green', 'orange', 'pink'), 0),
        single(A['col5'], img('blue', 'yellow', 'red'), 0),
    ]),

    q('Слушай и выбирай числа.', [
        single(A['num1'], txt('1', '4', '7'), 0),
        single(A['num2'], txt('2', '5', '8'), 0),
        single(A['num6'], txt('3', '6', '9'), 1),
        single(A['num7'], txt('4', '7', '10'), 1),
        single(A['num5'], txt('5', '8', '1'), 0),
    ]),

    q('Прочитай слово и выбери картинку.', [
        {'q': '<b>RED</b>', 'type': 'single', 'correct': [0],
         'options': img('red', 'blue', 'yellow')},
        {'q': '<b>pink</b>', 'type': 'single', 'correct': [1],
         'options': img('green', 'pink', 'orange')},
        {'q': '<b>TEN</b>', 'type': 'single', 'correct': [2],
         'options': img('ten_a', 'ten_b', 'ten_c')},
    ]),

    speaking('Нажми на микрофон и прочитай слова вслух 🎤',
             '<p><b>SAT &nbsp;·&nbsp; pin &nbsp;·&nbsp; TEN &nbsp;·&nbsp; den '
             '&nbsp;·&nbsp; rat &nbsp;·&nbsp; KIT</b></p>'),
    speaking('Нажми на микрофон и назови, сколько предметов каждого цвета ты видишь 🎤',
             f'<p style="text-align:center"><img src="{IMG["colour_count"]}" alt=""></p>'),

    t('<p>Ты справился! 🌟 Это был тест за весь Unit 0 — буквы, цвета, числа '
      'и первые слова, которые ты читаешь сам.</p>'),
]

HEAD = """\
-- {title}
-- Собрано скриптом builds/sm0/u0/build.py. Не заливать, пока не назовут,
-- куда переехала платформа: is_published остаётся false в любом случае.
-- Проверка: python3.13 tools/val.py builds/sm0/u0 sm0/legacy

do $$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm0';
  if v_course is null then raise exception 'курс sm0 не найден'; end if;

  select id into v_unit from classroom_units where course_id = v_course and sort_order = 0;
  if v_unit is null then raise exception 'юнит 0 курса sm0 не найден'; end if;

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
        assert '$blk$' not in raw, 'в payload попал разделитель $blk$'
        rows.append(f"    (v_lesson, '{typ}', replace($blk${raw}$blk$, "
                    f"'@@MEDIA@@', v_media)::jsonb, {i})")
    sql = (HEAD.format(title=title, lesson_title=lesson_title, kind=kind,
                       lesson_sort=lesson_sort, threshold=threshold)
           + ',\n'.join(rows) + '\n'
           + TAIL.format(lesson_title=lesson_title, n=len(blocks)))
    open(f'{HERE}/{name}.sql', 'w').write(sql)
    open(f'{HERE}/{name}.json', 'w').write(json.dumps({
        'course': 'sm0', 'unit_sort_order': 0, 'lesson': lesson_title, 'kind': kind,
        'lesson_sort_order': lesson_sort, 'pass_threshold': threshold,
        'is_published': False,
        'media_base': 'https://classroom.wowteach.ru/media/',
        'blocks': [{'sort_order': i, 'type': typ, 'payload': p}
                   for i, (typ, p) in enumerate(blocks)],
    }, ensure_ascii=False, indent=1))
    print(f'{name}: {len(blocks)} блоков → {name}.sql, {name}.json')


emit('u0_hw1', HW1,
     'SM0 · Unit 0 · Homework 1 — восстановлена по плану Lesson 1 (Hello)',
     'Homework 1', 'homework', 0, 60)
emit('u0_test', TEST,
     'SM0 · Unit 0 · Test — к уроку Lesson 6 «Revision + Test»',
     'Test', 'test', 6, 90)
