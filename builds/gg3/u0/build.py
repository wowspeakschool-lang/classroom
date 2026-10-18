# -*- coding: utf-8 -*-
"""GG3 · Unit 0 «Get started!» — тест юнита.

    python3.13 builds/gg3/u0/build.py

В GG3 в базе только тесты, домашек и планов нет — собираем один тест.
Структура как в тесте Unit 1 того же курса: match, грамматика выбором,
«составь предложение», вписывание и говорение.

Материал юнита (SB pp. 4–9):
  0.1 Present Simple, adverbs of frequency; places in town; means of transport
  0.2 jobs; question words
  0.3 be going to; school subjects; places in a school
  0.4 adjectives; adjectives with prepositions
  0.5 countable/uncountable, some/any, how much/many; food and drink; containers

Юнита 0 в базе нет — SQL заводит его сам, sort_order 0, перед Unit 1.
Весь звук размечен audio_tts: синтезирует методист «Озвучить пачкой».
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))


def tts(text):
    return {'audio': '', 'audio_tts': text}


def t(html):
    return 'text', {'html': html}


def quiz(title, questions):
    return 'quiz', {'title': title, 'questions': questions, 'needs_review': False}


def q(qtext, options, correct):
    return {'q': qtext, 'type': 'single', 'correct': [correct],
            'options': [{'text': x} for x in options]}


def order(words, sentence):
    return 'order', {'words': words, 'sentence': sentence, **tts(sentence)}


READING = [
    t('<p><b>READING.</b> Прочитай текст и ответь, верно или неверно.</p>'
      '<p>The Nichols family live in London. Peter is George and Harry’s dad. '
      'He is a doctor and he works at Park Hill General Hospital. He usually '
      'starts work at eight o’clock and he travels to work by motorbike. '
      'Angela, their mum, is a teacher. She often takes the bus to school. '
      'Harry is thirteen. He is good at tennis and he is interested in art. '
      'George doesn’t like sport, but he is excited about his new computer. '
      'At the weekend the family always go to the park.</p>'),

    ('truefalse', {'title': 'True or false?', 'statements': [
        {'text': 'Peter works at a hospital.', 'correct': True},
        {'text': 'Peter travels to work by bus.', 'correct': False},
        {'text': 'Angela is a doctor.', 'correct': False},
        {'text': 'Harry is interested in art.', 'correct': True},
        {'text': 'The family never go to the park.', 'correct': False},
    ]}),
]

# Текст аудирования методист начитывает своим голосом — синтезом не озвучиваем,
# поэтому audio_tts здесь нет и «Озвучить пачкой» этот блок не тронет.
NARRATION = (
    'This is Emma. Emma is thirteen years old. She lives with her mum and her '
    'gran Bertie. Emma usually goes to school by bike, but when it rains her mum '
    'drives her. Emma is good at dancing and she has got dance classes twice a '
    'week. This year she is going to study Geography more. Emma is scared of '
    'spiders. Her favourite food is pancakes: her gran always makes pancakes for '
    'breakfast on Sunday.')

LISTENING = [
    ('text', {'html': '<p><b>LISTENING 🎧</b> Послушай рассказ про Эмму. '
                      'Текста не будет — слушай и отвечай на вопросы ниже. '
                      'Можно послушать два раза.</p>',
              'audio': ''}),

    quiz('Послушай ещё раз и выбери правильный ответ.', [
        q('How old is Emma?', ['thirteen', 'nine', 'thirty'], 0),
        q('How does Emma usually go to school?', ['by bike', 'by car', 'by bus'], 0),
        q('How often has she got dance classes?',
          ['twice a week', 'every day', 'at the weekend'], 0),
        q('What is she going to study more this year?',
          ['Geography', 'Maths', 'Art'], 0),
        q('What is Emma scared of?', ['spiders', 'dogs', 'the dark'], 0),
    ]),
]

DICTATION = ('exact_input', {
    'title': 'DICTATION ✍️ Послушай предложение и запиши его целиком.',
    'needs_review': False,
    'items': [
        {**tts('Harry usually plays tennis on Thursdays.'),
         'prompt': '1.', 'accept': ['Harry usually plays tennis on Thursdays.',
                                    'Harry usually plays tennis on Thursdays']},
        {**tts('My dad travels to work by motorbike.'),
         'prompt': '2.', 'accept': ['My dad travels to work by motorbike.',
                                    'My dad travels to work by motorbike']},
        {**tts('There isn’t any milk in the fridge.'),
         'prompt': '3.', 'accept': ['There isn’t any milk in the fridge.',
                                    'There isn’t any milk in the fridge',
                                    "There isn't any milk in the fridge.",
                                    "There isn't any milk in the fridge"]},
        {**tts('We are going to visit a museum.'),
         'prompt': '4.', 'accept': ['We are going to visit a museum.',
                                    'We are going to visit a museum']},
    ]})


TEST = [
    t('<p>Сегодня у нас с тобой тест по нулевому юниту Get started! Проверим '
      'Present Simple, be going to, вопросы, еду и всё, что мы повторяли. '
      'Уверена, ты справишься!</p>'),

    ('match', {'title': 'Match the place with what you can do there.',
               'pairs': [
                   {'left': 'You can see paintings here.', 'right': 'museum',
                    **{'right_audio': '', 'right_audio_tts': 'museum'}},
                   {'left': 'You can watch a film here.', 'right': 'cinema',
                    **{'right_audio': '', 'right_audio_tts': 'cinema'}},
                   {'left': 'You can stay here on holiday.', 'right': 'hotel',
                    **{'right_audio': '', 'right_audio_tts': 'hotel'}},
                   {'left': 'You can watch a football match here.', 'right': 'stadium',
                    **{'right_audio': '', 'right_audio_tts': 'stadium'}},
                   {'left': 'You can have dinner here.', 'right': 'restaurant',
                    **{'right_audio': '', 'right_audio_tts': 'restaurant'}},
                   {'left': 'A doctor works here.', 'right': 'hospital',
                    **{'right_audio': '', 'right_audio_tts': 'hospital'}},
               ], 'needs_review': False}),

    quiz('Means of transport and places — choose the right word.', [
        q('Harry goes to school ___ bike.', ['by', 'on', 'with'], 0),
        q('It goes under the ground. It’s the ___.',
          ['underground', 'tram', 'boat'], 0),
        q('Emma and Gran travel to France ___ plane.', ['by', 'in', 'at'], 0),
        q('George and his dad go to the ___ to watch the football.',
          ['stadium', 'museum', 'bank'], 0),
        q('You can take money out at the ___.', ['bank', 'park', 'theatre'], 0),
    ]),

    quiz('Present Simple and adverbs of frequency — choose the right option.', [
        q('George ___ karate on Tuesdays.', ['does', 'do', 'doing'], 0),
        q('Emma ___ have dance classes on Mondays.',
          ['doesn’t', 'don’t', 'isn’t'], 0),
        q('___ Harry play tennis on Thursdays?', ['Does', 'Do', 'Is'], 0),
        q('I ___ late for school.', ['am never', 'never am', 'never'], 0),
        q('She ___ to school by bike.',
          ['always goes', 'goes always', 'always go'], 0),
    ]),

    quiz('Question words — complete the questions about Harry’s dad.', [
        q('___ does your dad do?', ['What', 'Who', 'When'], 0),
        q('___ does he work?', ['Where', 'How', 'What'], 0),
        q('___ does he start work?', ['When', 'Where', 'Who'], 0),
        q('___ does he travel to work?', ['How', 'What', 'When'], 0),
    ]),

    quiz('Jobs — who is it?', [
        q('This person looks after animals when they are ill.',
          ['a vet', 'a farmer', 'a nurse'], 0),
        q('This person cooks in a restaurant.',
          ['a chef', 'a waiter', 'a shop assistant'], 0),
        q('This person helps people in hospital and works with a doctor.',
          ['a nurse', 'a teacher', 'a pilot'], 0),
        q('This person flies a plane.', ['a pilot', 'a bus driver', 'a builder'], 0),
    ]),

    quiz('be going to — choose the right option.', [
        q('I ___ study Geography more this year.',
          ['am going to', 'going to', 'am going'], 0),
        q('My parents ___ buy me a laptop.',
          ['are going to', 'is going to', 'going to'], 0),
        q('___ you going to have lunch at school?', ['Are', 'Do', 'Is'], 0),
        q('He ___ going to get up late again.', ['isn’t', 'aren’t', 'doesn’t'], 0),
    ]),

    quiz('Adjectives with prepositions — choose the right word.', [
        q('I’m bad ___ cooking.', ['at', 'in', 'of'], 0),
        q('She’s interested ___ science.', ['in', 'at', 'about'], 0),
        q('He’s scared ___ spiders.', ['of', 'at', 'for'], 0),
        q('They’re excited ___ the new game.', ['about', 'of', 'in'], 0),
    ]),

    quiz('Food and drink — some, any, how much, how many.', [
        q('There ___ some apples in the kitchen.', ['are', 'is', 'be'], 0),
        q('There isn’t ___ sugar in my tea.', ['any', 'some', 'a'], 0),
        q('___ milk is there?', ['How much', 'How many', 'How long'], 0),
        q('___ eggs are there?', ['How many', 'How much', 'How often'], 0),
        q('Have we got ___ bread?', ['any', 'many', 'a'], 0),
    ]),

    order(['She', 'doesn’t go', 'to the gym', 'on Mondays.'],
          'She doesn’t go to the gym on Mondays.'),
    order(['How often', 'do you', 'travel', 'by train?'],
          'How often do you travel by train?'),
    order(['I’m', 'going to', 'study', 'English', 'this year.'],
          'I’m going to study English this year.'),
    order(['There', 'isn’t', 'any juice', 'in the fridge.'],
          'There isn’t any juice in the fridge.'),

    ('exact_input', {'title': 'Containers — write the missing word.',
                     'items': [
                         {'prompt': '1. a ___ of chocolate', 'accept': ['bar', 'Bar']},
                         {'prompt': '2. a ___ of water', 'accept': ['bottle', 'Bottle']},
                         {'prompt': '3. a ___ of tuna', 'accept': ['can', 'Can']},
                         {'prompt': '4. a ___ of milk', 'accept': ['carton', 'Carton']},
                         {'prompt': '5. a ___ of flour', 'accept': ['packet', 'Packet']},
                     ], 'needs_review': False}),

    *READING,
    *LISTENING,
    DICTATION,

    ('speaking', {'title': 'SPEAKING TASK 🎤', 'needs_review': True,
                  'html': '<p>Ответь на вопросы, 6–8 предложений. Нажми на микрофон '
                          'и запиши ответ.</p>'
                          '<ol><li>What do you usually do at the weekend?</li>'
                          '<li>How do you travel to school?</li>'
                          '<li>What are you good at? What are you scared of?</li>'
                          '<li>What are you going to do this year?</li>'
                          '<li>What is there in your fridge at home?</li></ol>'}),

    t('<p>Ты справился! 🌟 Это был тест за весь нулевой юнит: город и транспорт, '
      'профессии, школа, характер и еда.</p>'),
]

HEAD = """\
-- {title}
-- Собрано скриптом builds/gg3/u0/build.py. Не заливать, пока не назовут,
-- куда переехала платформа. Проверка:
--   python3.13 tools/val.py builds/gg3/u0 gg3/u0

do $$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'gg3';
  if v_course is null then raise exception 'курс gg3 не найден'; end if;

  select id into v_unit from classroom_units where course_id = v_course and sort_order = 0;
  if v_unit is null then
    insert into classroom_units (course_id, title, sort_order)
    values (v_course, 'Unit 0', 0)
    returning id into v_unit;
  end if;

  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and sort_order = 0;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, kind, sort_order, pass_threshold, is_published)
    values (v_unit, 'Unit 0 Test', 'test', 0, 90, false)
    returning id into v_lesson;
  else
    update classroom_lessons
       set title = 'Unit 0 Test', kind = 'test', pass_threshold = 90
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
"""

TAIL = """  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  raise notice 'GG3 Unit 0 Test: % блоков', {n};
end $$;
"""

rows = []
for i, (typ, payload) in enumerate(TEST):
    raw = json.dumps(payload, ensure_ascii=False)
    assert '$blk$' not in raw
    rows.append(f"    (v_lesson, '{typ}', replace($blk${raw}$blk$, "
                f"'@@MEDIA@@', v_media)::jsonb, {i})")
open(f'{HERE}/u0_test.sql', 'w').write(
    HEAD.format(title='GG3 · Unit 0 «Get started!» · Test') + ',\n'.join(rows) + '\n'
    + TAIL.format(n=len(TEST)))
open(f'{HERE}/u0_test.json', 'w').write(json.dumps({
    'course': 'gg3', 'unit': 'Unit 0', 'unit_sort_order': 0,
    'lesson': 'Unit 0 Test', 'kind': 'test', 'lesson_sort_order': 0,
    'pass_threshold': 90, 'is_published': False,
    'blocks': [{'sort_order': i, 'type': ty, 'payload': p}
               for i, (ty, p) in enumerate(TEST)],
}, ensure_ascii=False, indent=1))
print(f'GG3 Unit 0 Test: {len(TEST)} блоков → u0_test.sql, u0_test.json')
