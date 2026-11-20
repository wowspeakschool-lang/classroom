# -*- coding: utf-8 -*-
"""Go Getter 3, юнит 1 по рабочей тетради — сборка домашек в SQL."""
import json, io

MEDIA = 'https://classroom.wowteach.ru/media/'
GOLOS = 'en_GB-alba'
UNIT = '96161506-701b-4074-9115-ee113b71a739'   # Unit 1 · Life at home


def tts(t):
    return {'text': t if t.endswith('.') or t.endswith('?') or t.endswith('!') else t + '.', 'voice': GOLOS}


def privet(kartinka, zagolovok, text):
    return ('text', {'html': f'<p><img src="{MEDIA}shared/gg/{kartinka}" alt="" style="height:200px"></p>'
                             f'<h2>{zagolovok}</h2><p>{text}</p>'})


def poka(kartinka, text):
    return ('text', {'html': f'<p><img src="{MEDIA}shared/gg/{kartinka}" alt="" style="height:200px"></p><p>{text}</p>'})


# ─────────────────────────────── ДЗ 1 · 1.1 Vocabulary ───────────────────────
SLOVA = [
    ('make the bed', 'застилать кровать'), ('load the dishwasher', 'загружать посудомойку'),
    ('empty the dishwasher', 'разгружать посудомойку'), ('wash the dishes', 'мыть посуду'),
    ('vacuum the living room', 'пылесосить гостиную'), ('take out the rubbish', 'выносить мусор'),
    ('water the plants', 'поливать растения'), ('feed my pet', 'кормить питомца'),
    ('set the table', 'накрывать на стол'), ('clear the table', 'убирать со стола'),
    ('iron my T-shirt', 'гладить футболку'), ('put away my clothes', 'убирать одежду'),
    ('load the washing machine', 'загружать стиральную машину'), ('tidy my room', 'убирать комнату'),
    ('cook lunch', 'готовить обед'),
]

hw1 = [
    privet('hello_teen_wave.webp', 'Unit 1 · Life at home',
           'Сегодня — дела по дому: как они называются по-английски и как про них рассказать.'),
    ('flashcards', {'title': 'Повторяем слова урока. Нажми на карточку — услышишь слово и увидишь перевод',
                    'cards': [{'text': w, 'translation': p, 'audio': '', 'audio_tts': tts(w)} for w, p in SLOVA]}),
    ('quiz', {'title': 'Посмотри на картинку и выбери правильный вариант', 'questions': [
        {'q': '', 'image': MEDIA + 'gg3/u1/chore_dishwasher.webp', 'type': 'single', 'correct': [1],
         'options': [{'text': 'wash the dishes'}, {'text': 'empty the dishwasher'}, {'text': 'water the plants'}]},
        {'q': '', 'image': MEDIA + 'gg3/u1/chore_vacuum.webp', 'type': 'single', 'correct': [2],
         'options': [{'text': 'make the bed'}, {'text': 'take out the rubbish'}, {'text': 'vacuum the living room'}]},
        {'q': '', 'image': MEDIA + 'gg3/u1/chore_feed_pet.webp', 'type': 'single', 'correct': [0],
         'options': [{'text': 'feed my pet'}, {'text': 'water the plants'}, {'text': 'clear the table'}]},
        {'q': '', 'image': MEDIA + 'gg3/u1/chore_set_table.webp', 'type': 'single', 'correct': [1],
         'options': [{'text': 'cook lunch'}, {'text': 'set the table'}, {'text': 'iron my T-shirt'}]},
    ]}),
    ('match', {'title': 'Соедини начало и конец предложения', 'pairs': [
        {'left': 'Can you iron', 'right': 'my T-shirt, please?'},
        {'left': 'Anna always puts', 'right': 'away her clothes.'},
        {'left': 'Dad often clears the', 'right': 'table after dinner.'},
        {'left': 'We make our', 'right': 'beds before we go to school.'},
        {'left': 'Please take', 'right': 'out the rubbish.'},
        {'left': 'Grandpa waters', 'right': 'our plants on hot days.'},
        {'left': 'Tina usually loads', 'right': 'the washing machine.'},
        {'left': 'Mum cooks', 'right': 'lunch at the weekend.'},
    ]}),
    ('sort', {'title': 'Распредели глаголы: что с чем делают', 'groups': [
        {'name': 'the dishwasher', 'items': [{'text': 'load'}, {'text': 'empty'}]},
        {'name': 'my room', 'items': [{'text': 'vacuum'}, {'text': 'tidy'}]},
        {'name': 'my clothes', 'items': [{'text': 'iron'}, {'text': 'put away'}]},
        {'name': 'the table', 'items': [{'text': 'set'}, {'text': 'clear'}]}]}),
    ('gaps', {'title': 'Прочитай блог Кэти и перетащи слова в пропуски', 'mode': 'drag', 'text':
        "Hi! Today I want to tell you about my new friend, Charlie.\n"
        "Charlie helps his parents every day. He makes his bed after he gets up. "
        "Before breakfast he empties the __dishwasher__ and puts the plates and glasses in the kitchen cupboard.\n"
        "When it's hot, he waters the __plants__ in the garden. Then he goes to school.\n"
        "He gets home from school at two o'clock and he feeds the __cat__ because it's her lunch time.\n"
        "His favourite chore is cooking __dinner__ with his dad because it's fun."}),
    ('speaking', {'title': 'Расскажи о своих делах по дому 🎤', 'needs_review': True, 'html':
        '<p>Назови три дела, которые ты делаешь дома, и скажи, какое тебе нравится больше всего.</p>'
        '<p><i>Например: I take out the rubbish every evening. I like cooking with my mum.</i></p>'}),
    poka('bye_star.webp', 'Отлично! Теперь ты можешь рассказать, кто что делает дома.'),
]

# ─────────────────────────────── ДЗ 2 · 1.2 Grammar ──────────────────────────
VF = [{'text': 'Верно'}, {'text': 'Неверно'}]

hw2 = [
    privet('hello_laptop.webp', 'Unit 1 · Life at home',
           'Грамматика: Present Continuous — что происходит прямо сейчас — и глаголы, которые в нём не используются.'),
    ('quiz', {'title': 'Посмотри на картинку и выбери: верно или неверно', 'questions': [
        {'q': 'Peter is listening to music.', 'image': MEDIA + 'gg3/u1/fam_bed.webp', 'type': 'single',
         'correct': [1], 'options': VF},
        {'q': 'Dad is washing the dishes.', 'image': MEDIA + 'gg3/u1/fam_dishes.webp', 'type': 'single',
         'correct': [0], 'options': VF},
        {'q': "Peter's brothers are feeding the cat.", 'image': MEDIA + 'gg3/u1/fam_cat.webp', 'type': 'single',
         'correct': [0], 'options': VF},
        {'q': "Peter's sister is doing her homework.", 'image': MEDIA + 'gg3/u1/fam_phone.webp', 'type': 'single',
         'correct': [1], 'options': VF},
    ]}),
    ('order', {'title': 'Расставь слова по порядку — получится вопрос мамы', 'items': [
        {'words': 'Is your sister vacuuming her room?'.split(), 'sentence': 'Is your sister vacuuming her room?'},
        {'words': 'Are your brothers sleeping?'.split(), 'sentence': 'Are your brothers sleeping?'},
        {'words': 'Is Dad making breakfast?'.split(), 'sentence': 'Is Dad making breakfast?'},
        {'words': 'Are you making your bed, Peter?'.split(), 'sentence': 'Are you making your bed, Peter?'},
    ]}),
    ('quiz', {'title': 'Выбери правильный вариант', 'questions': [
        {'q': 'The dog ___ food. He’s hungry.', 'type': 'single', 'correct': [1],
         'options': [{'text': 'is needing'}, {'text': 'needs'}]},
        {'q': 'I ___ the answers.', 'type': 'single', 'correct': [0],
         'options': [{'text': "don't know"}, {'text': 'am not knowing'}]},
        {'q': '___ watching films on TV?', 'type': 'single', 'correct': [1],
         'options': [{'text': 'Are you liking'}, {'text': 'Do you like'}]},
        {'q': 'Where’s Dad? He ___ lunch.', 'type': 'single', 'correct': [0],
         'options': [{'text': 'is cooking'}, {'text': 'cooks'}]},
        {'q': 'Mum ___ the beds. Let’s help her.', 'type': 'single', 'correct': [1],
         'options': [{'text': 'makes'}, {'text': 'is making'}]},
        {'q': '___ his new phone?', 'type': 'single', 'correct': [1],
         'options': [{'text': 'Is Dave loving'}, {'text': 'Does Dave love'}]},
    ]}),
    ('gaps', {'title': 'Прочитай разговор и выбери правильную форму глагола', 'mode': 'choice', 'text':
        "Emma: Hi, Harry. What are you doing?\n"
        "Harry: I __am setting__ the table for dinner. Why __are you asking__?\n"
        "Emma: I __need__ some help with tidying my room. I __don't like__ doing it on my own. Please!\n"
        "Harry: I've got my own chores, thanks!\n"
        "Emma: What about George? __Is he doing__ any work now? Can he help me?\n"
        "Harry: George __hates__ chores too! He __doesn't like__ tidying or vacuuming.",
        'choices': [['set', 'am set'], ['do you ask', 'you are asking'], ['am needing', 'needs'],
                    ['am not liking', 'doesn’t like'], ['Does he doing', 'Is he do'],
                    ['is hating', 'hate'], ["isn't liking", "don't like"]]}),
    ('task', {'title': 'Допиши разговор с другом ✍️', 'needs_review': True, 'html':
        '<p>Представь, что сейчас субботнее утро. Ты звонишь другу. Допиши разговор — по одному предложению в каждой строке.</p>'
        '<p><b>You:</b> Hi! What are you doing?<br>'
        '<b>Your friend:</b> I … (tidy / my bedroom).<br>'
        '<b>You:</b> Poor you! I … (hate) tidying my room.<br>'
        '<b>Your friend:</b> And what about you?<br>'
        '<b>You:</b> Well, I … (vacuum / my room) …<br>'
        '<b>Your friend:</b> I … (not like) vacuuming. It’s boring!</p>'
        '<p><i>Например: I’m washing the dishes. I don’t like doing the dishes.</i></p>'}),
    poka('bye_thumb.webp', 'Готово! Теперь ты знаешь, какие глаголы не ставят в Present Continuous.'),
]

UROKI = [('Homework 1', 0, hw1), ('Homework 2', 1, hw2)]

out = io.StringIO()
out.write('-- Go Getter 3, юнит 1 по рабочей тетради: домашки 1–2 (черновики)\n')
out.write("update classroom_lessons set sort_order = 10 where id = '87f1ce1e-8300-43d2-82b0-594ff8099a0f';\n")
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

io.open('builds/gg3/wb/u1/u1_hw1_hw2.sql', 'w', encoding='utf-8').write(out.getvalue())
print('блоков:', sum(len(b) for _, _, b in UROKI), '· байт:', len(out.getvalue()))
