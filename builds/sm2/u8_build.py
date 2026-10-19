# -*- coding: utf-8 -*-
"""SM2 · Unit 8 · Sports — сборка всех восьми уроков."""
import os
import u_lib as L
from u_lib import (Lesson, url, simg, img, accept, scramble, distract,
                   q_single, q_multi)

L.setup('Unit 8 · Sports', 8, 'sm2/u8')
OUT = 'u8sql'

WORDS = [('badminton', 'бадминтон'), ('table tennis', 'настольный теннис'),
         ('tennis', 'теннис'), ('baseball', 'бейсбол'), ('basketball', 'баскетбол'),
         ('volleyball', 'волейбол'), ('swimming', 'плавание'), ('football', 'футбол'),
         ('athletics', 'лёгкая атлетика'), ('hockey', 'хоккей')]
W = [w for w, _ in WORDS]
PIC = {'badminton': 's_badminton', 'table tennis': 's_tabletennis', 'tennis': 's_tennis',
       'baseball': 's_baseball', 'basketball': 's_basketball', 'volleyball': 's_volleyball',
       'swimming': 's_swimming', 'football': 's_football', 'athletics': 's_athletics',
       'hockey': 's_hockey'}

VIDEO = ('Ссылка на видео', 'блок «Видео/аудио» пустой',
         'в выгрузке медиафайла нет — платформа его не отдаёт')
AUDIO = ('Ссылка на аудио', 'блок «Видео/аудио» пустой',
         'в выгрузке медиафайла нет — платформа его не отдаёт')

# ═══════════════════════════════════════════════════════════ Homework 1 ══
h1 = Lesson('Homework 1', 'Виды спорта — новые слова', 0)

h1.text(simg('hello_wave') + '<h2>Привет!</h2>'
        '<p>Сегодня повторим слова, которые были на уроке :) Поговорим о спорте! '
        'Давай начинать 😁</p>',
        'приветствие; в выгрузке урок разбит на части (1) и (2) — свёл в один')

h1.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_sports'),
        'карточка «Vocabulary: Sports» из выгрузки')

h1.add('flashcards', {'cards': [
    {'text': w, 'translation': t, 'image': url(PIC[w]), 'audio_tts': w}
    for w, t in WORDS]},
    'механика «Карточки» из выгрузки; картинки нарисовала методист')

h1.add('quiz', {'title': 'Проверь себя', 'questions': [
    q_single(f'Как по-английски «{t}»?', w, sorted([w] + distract(w, W, 2, 'h1q' + w)),
             image=PIC[w])
    for w, t in WORDS]},
    'механика «Квиз» из выгрузки')

h1.add('match', {'title': 'Найди пару: слово и перевод', 'pairs': [
    {'left': w, 'left_audio_tts': w, 'right': t} for w, t in WORDS]},
    'механика «Найди пару» из выгрузки')

h1.add('exact_input', {'title': 'Скрэмбл: собери слово из букв', 'items': [
    {'prompt': f'{scramble(w, "h1" + w)}  ({t})', 'accept': accept(w), 'audio_tts': w}
    for w, t in WORDS]},
    'механика «Скрэмбл» из выгрузки')

h1.add('exact_input', {'title': 'Напиши слово по-английски', 'items': [
    {'prompt': f'Напиши по-английски: {t}', 'accept': accept(w), 'audio_tts': w}
    for w, t in WORDS]},
    'механика «Заполни пропуски» из выгрузки — заменил вводом слова целиком')

h1.text('<h3>Дополнительная часть 🌟</h3>'
        '<p>Привет! Время домашней работы :) Готов? Давай начинать!</p>',
        'начало части (2) из выгрузки')

h1.add('match', {'title': 'Для начала давай начнём с пар! Перед тобой виды спорта '
                          'и инструменты, которые в них могут пригодиться. Соедини их',
                 'pairs': [
                     {'left_image': url('s_basketball'), 'right': 'a basketball hoop',
                      'right_audio_tts': 'a basketball hoop'},
                     {'left_image': url('s_swimming'), 'right': 'goggles',
                      'right_audio_tts': 'goggles'},
                     {'left_image': url('s_baseball'), 'right': 'a baseball bat',
                      'right_audio_tts': 'a baseball bat'},
                     {'left_image': url('s_football'), 'right': 'a football',
                      'right_audio_tts': 'a football'},
                     {'left_image': url('s_tabletennis'), 'right': 'a small bat',
                      'right_audio_tts': 'a small bat'},
                     {'left_image': url('s_volleyball'), 'right': 'a net',
                      'right_audio_tts': 'a net'},
                     {'left_image': url('s_badminton'), 'right': 'a shuttlecock',
                      'right_audio_tts': 'a shuttlecock'},
                     {'left_image': url('s_athletics'), 'right': 'trainers',
                      'right_audio_tts': 'trainers'},
                     {'left_image': url('s_hockey'), 'right': 'a hockey stick',
                      'right_audio_tts': 'a hockey stick'}]},
       'в выгрузке правая колонка пустая — названия инвентаря подобрал сам, СОСТАВ МОЙ',
       todo=('Посмотреть названия инвентаря', 'блок «Найди пару» с девятью видами спорта',
             'в выгрузке правая колонка пустая — я подобрал по одному предмету на вид спорта'))

h1.text('<p>Теперь давай перейдём к видео! Посмотри его и ответь на вопросы ниже.</p>')

h1.add('video', {'title': 'Видео: ребята о любимом спорте', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h1.add('truefalse', {'title': 'Определи — верно утверждение или нет. Если понадобится, '
                              'можешь заглянуть обратно в видео и вспомнить ответ 😊',
                     'statements': [
                         {'text': "The first girl's name is Olivia.", 'correct': True},
                         {'text': "Noah's favourite sport is baseball.", 'correct': False},
                         {'text': "Scarlett doesn't like water.", 'correct': False},
                         {'text': 'Thomas likes catching the ball.', 'correct': True},
                         {'text': 'Lucas likes basketball and volleyball.', 'correct': False}]},
       'ответы отмечены в выгрузке; там опечатка «Thomas like catching» — исправил')

h1.add('sequence', {'title': 'Послушай ещё разок Оливию. Расставь то, что она сказала, '
                             'по порядку',
                    'items': [{'text': s, 'audio_tts': s} for s in [
                        'My favourite sport is soccer.',
                        'Because lots of my friends play it.',
                        "And I'm very good at it.",
                        'And pretty much everyone in my family used to play it.',
                        'And I got all my friends around my team.',
                        "And it's really fun for me!"]]},
       'в выгрузке это «Порядок предложений»')

h1.add('speaking', {'title': 'Теперь твоя очередь! 🎤',
                    'html': '<p>Расскажи о своём любимом виде спорта. Если хочешь, '
                            'можешь ответить на эти вопросы:</p>'
                            '<ul><li>What is your favourite sport?</li>'
                            '<li>Why do you like this sport?</li>'
                            '<li>What do you do in this sport? (Do you jump, run, swim?)</li>'
                            '</ul>',
                    'sample_tts': 'My favourite sport is football. I like it because '
                                  'I play it with my friends. I run and I jump.',
                    'needs_review': True})

h1.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Соедини картинки со словами:</b></p>')

h1.add('match', {'title': 'Соедини картинку со словом', 'pairs': [
    {'left_image': url(PIC[w]), 'right': w, 'right_audio_tts': w} for w, _ in WORDS]},
    'Wordwall «Соедини картинки со словами» — СОСТАВ МОЙ, содержимого игры в выгрузке нет')

h1.text('<p><b>Впиши слова:</b></p>')

h1.add('exact_input', {'title': 'Собери слово из букв', 'items': [
    {'prompt': f'{scramble(w, "h1w" + w)}  ({t})', 'accept': accept(w), 'audio_tts': w}
    for w, t in WORDS]},
    'Wordwall «Впиши слова» — СОСТАВ МОЙ')

h1.text(simg('well_done_medal') +
        '<p>Отличная работа! Спасибо тебе за твои старания :))</p>'
        '<p>Самое время немножко отдохнуть! Хорошего тебе дня!</p>')

# ═══════════════════════════════════════════════════════════ Homework 2 ══
h2 = Lesson('Homework 2', 'Verb + ing: Swimming is fun', 1)

h2.text(simg('hello_highfive') + '<h2>Привет!</h2>'
        '<p>Как твои дела? Надеюсь, всё отлично! Давай начинать домашнюю работу?</p>')

h2.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_activity'),
        'карточка «Grammar 1: [Activity]’s [adjective]» из выгрузки')

h2.text('<p>Посмотри маленькое видео и обрати внимание на слова и на их окончание :)</p>')

h2.add('video', {'title': 'Видео про окончание -ing',
                 'url': 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm2/u8/sm2_u8_hw2_b4.mp4', 'provider': 'file'},
       'видео прислала методист')

h2.add('match', {'title': 'Видео посмотрели! Теперь давай соединим картинку с названием '
                          'спорта или развлечения. Ты точно справишься! Вперёд!',
                 'pairs': [{'left_image': url('v_' + a), 'right': a, 'right_audio_tts': a}
                           for a in ['flying', 'listening', 'watching', 'making',
                                     'riding', 'reading', 'playing', 'painting']]},
       'в выгрузке правая колонка пустая — картинки нарисовала методист')

h2.add('gaps', {'title': 'Отличная работа! Самое время полностью составить правило. '
                         'Справимся? Вспомни то, что ты прошёл на уроке, и заполни '
                         'пропуски нужными словами',
                'mode': 'drag',
                'text': "Use verb + __ing__ to make sentences to describe __activities__.\n"
                        "__Flying__ a kite's difficult.\n"
                        "__Riding__ is great."})

h2.add('quiz', {'title': 'Ты большой молодец! Правило составил на ура! Самое время '
                         'практиковаться. Выбери правильный вариант ответа 😄',
                'questions': [
    q_single('___ a kite is difficult.', 'Flying', ['Flying', 'Fly']),
    q_single('___ computer games is boring.', 'Playing', ['Playing', 'Play']),
    q_single('___ cakes is fun.', 'Making', ['Making', 'Makes']),
    q_single('___ a horse is easy.', 'Riding', ['Riding', 'Ride']),
    q_single('___ a book is great.', 'Reading', ['Reading', 'Reads']),
    q_single('___ pictures is fun.', 'Painting', ['Painting', 'Paint'])]},
    'в выгрузке это «Выбери правильный вариант»')

h2.text('<p>Отличная работа!! Задания становятся всё сложнее и сложнее 😁 Впиши в пропуски '
        'нужное слово. Чтобы узнать, что это за слово, смотри на картинку.</p>'
        '<p>Пример: <i>Playing baseball is boring.</i></p>' + img('a_baseball'))

for pic, ans, tail in [('a_dancing', 'Dancing', 'is great.'),
                       ('a_swimming', 'Swimming', 'is fun.'),
                       ('a_tennis', 'Playing tennis', 'is difficult.'),
                       ('a_football', 'Playing football', 'is fun.'),
                       ('a_hockey', 'Playing hockey', 'is boring.')]:
    h2.add('exact_input', {'image': url(pic), 'items': [
        {'prompt': f'___ {tail}', 'accept': [ans], 'audio_tts': f'{ans} {tail}'}]},
        'в выгрузке это «Впиши в пропуски» с картинкой')

h2.add('speaking', {'title': 'Предпоследнее задание 🎤',
                    'html': '<p>Посмотри на пропущенные слова и запиши свой ответ, '
                            'прочитав предложение полностью :)</p>'
                            + img('a_dancing') + img('a_swimming') + img('a_tennis'),
                    'sample_tts': 'Dancing is great. Swimming is fun. '
                                  'Playing tennis is difficult.',
                    'needs_review': True})

h2.add('task', {'title': 'Супер! Самое интересное — ответь письменно на вопросы ниже',
                'html': '<ol><li>Is playing basketball difficult?</li>'
                        '<li>Is dancing easy?</li><li>Is reading fun?</li>'
                        '<li>Is playing computer games great?</li>'
                        '<li>Is playing hockey fun?</li></ol>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h2.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Соедини картинки с фразами:</b></p>')

h2.add('match', {'title': 'Соедини картинку с фразой', 'pairs': [
    {'left_image': url('a_dancing'), 'right': 'Dancing is great.',
     'right_audio_tts': 'Dancing is great.'},
    {'left_image': url('a_swimming'), 'right': 'Swimming is fun.',
     'right_audio_tts': 'Swimming is fun.'},
    {'left_image': url('a_tennis'), 'right': 'Playing tennis is difficult.',
     'right_audio_tts': 'Playing tennis is difficult.'},
    {'left_image': url('a_football'), 'right': 'Playing football is fun.',
     'right_audio_tts': 'Playing football is fun.'},
    {'left_image': url('a_hockey'), 'right': 'Playing hockey is boring.',
     'right_audio_tts': 'Playing hockey is boring.'}]},
    'Wordwall «Соедини картинки с фразами» — СОСТАВ МОЙ')

h2.text('<p><b>Выбери правильный вариант:</b></p>')

h2.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
    q_single('___ TV is boring.', 'Watching', ['Watching', 'Watch', 'Watches']),
    q_single('___ to music is great.', 'Listening', ['Listening', 'Listen', 'Listens']),
    q_single('___ a bike is easy.', 'Riding', ['Riding', 'Ride', 'Rides']),
    q_single('___ pictures is fun.', 'Painting', ['Painting', 'Paint', 'Paints'])]},
    'второй Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ')

h2.text(simg('well_done_star') + '<p>Молодец! Увидимся на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 3 ══
h3 = Lesson('Homework 3', 'I like / I don’t like + verb-ing', 2)

h3.text(simg('hello_book') + '<h2>Привет-привет, самый лучший ученик!</h2>'
        '<p>Готов к новому домашнему заданию? Давай начинать 😁</p>')

h3.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_like'),
        'карточка «Grammar 2: I like / I don’t like + [verb]ing» из выгрузки')

h3.text('<p>Давай начнём с видео! Посмотри его и найди ответ на вопрос: '
        '<i>What sports game do children like?</i></p>')

h3.add('video', {'title': 'Видео к уроку', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h3.add('quiz', {'title': 'Давай ответим на вопрос :)', 'questions': [
    q_single('What sports game do children like?', 'soccer',
             ['volleyball', 'swimming', 'soccer', 'baseball'])]},
    'ответ отмечен в выгрузке')

h3.add('match', {'title': 'Самое время соединять! Соедини вопрос и ответ :)',
                 'pairs': [
                     {'left': 'What sport do you like doing?',
                      'right': 'I like playing football.',
                      'right_audio_tts': 'I like playing football.'},
                     {'left': 'I like playing soccer.', 'right': 'Me too!',
                      'right_audio_tts': 'Me too!'},
                     {'left': 'I like swimming.',
                      'right': "I don't. I don't like swimming.",
                      'right_audio_tts': "I don't. I don't like swimming."}]})

h3.add('hotspot', {'title': 'Ты молодец! Посмотри на картинку ниже, прочитай диалоги '
                            'и соедини их с нужным фото 😉',
                   'mode': 'label', 'image': url('dialogs4'),
                   'points': [
                       {'x': 25, 'y': 25, 'text': 'I like running. — So do I.'},
                       {'x': 75, 'y': 25, 'text': "I like playing table tennis. — I don't."},
                       {'x': 25, 'y': 75, 'text': 'I like swimming. — So do I.'},
                       {'x': 75, 'y': 75, 'text': "I like playing football. — I don't."}]},
       'в выгрузке это «Диаграмма» с четырьмя точками',
       todo=('Проверить, куда встали точки', 'блок «Точки на картинке» с четырьмя диалогами',
             'координаты точек я расставил сам — в выгрузке они не сохраняются'))

h3.add('gaps', {'title': 'Вау! Как ты здорово решаешь задания. Огромный молодец! '
                         'А сейчас прочитай текст ниже и выбери правильный вариант ответа',
                'mode': 'drag', 'image': url('i_bike'),
                'text': "Matt: What sport do you like __doing__?\n"
                        "Jane: I like playing hockey.\n"
                        "Matt: I __don't__. I like dancing — I think dancing is great. "
                        "Do you like any other sports?\n"
                        "Jane: Yes, I like __riding__ my bike on a sunny day.\n"
                        "Matt: So __do I__. I __like__ going to the lake on my bike "
                        "and swimming.\n"
                        "Jane: Me __too__!"},
       'в выгрузке это «Выбери правильный вариант»')

h3.text('<p>Иии — последнее задание на сегодня! Посмотри на фото и дополни пропуски '
        'своими идеями :) На фото образец.</p>' + img('ex_tennis'))

h3.add('exact_input', {'image': url('i_ballet'), 'items': [
    {'prompt': '✅ ___ .', 'accept': ['I like dancing'], 'audio_tts': 'I like dancing'},
    {'prompt': '❎ ___ .', 'accept': ["I don't"], 'audio_tts': "I don't"}]},
    'в выгрузке это «Впиши в пропуски» с картинкой')

h3.add('exact_input', {'image': url('i_bike'), 'items': [
    {'prompt': '✅ I like ___ .', 'accept': ['riding a bike'],
     'audio_tts': 'I like riding a bike'},
    {'prompt': '❎ Me ___ .', 'accept': ['too'], 'audio_tts': 'Me too'}]},
    'в выгрузке это «Впиши в пропуски» с картинкой')

h3.add('exact_input', {'image': url('i_swim'), 'items': [
    {'prompt': 'What sport ___ ?', 'accept': ['do you like doing', 'do you like'],
     'audio_tts': 'What sport do you like doing?'},
    {'prompt': '___ .', 'accept': ['I like swimming'], 'audio_tts': 'I like swimming'}]},
    'в выгрузке это «Впиши в пропуски» с картинкой')

h3.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Расставь слова в правильном порядке:</b></p>')

for words in ['I/like/playing/football.', "I/don't/like/swimming.",
              'What/sport/do/you/like/doing?', 'I/like/riding/my/bike.']:
    ws = words.split('/')
    h3.add('order', {'words': ws, 'sentence': ' '.join(ws), 'audio_tts': ' '.join(ws)},
           'Wordwall «Unjumble · I like doing» — СОСТАВ МОЙ')

h3.text('<p><b>Заполни пропуски:</b></p>')

h3.add('gaps', {'title': 'Заполни пропуски', 'mode': 'drag',
                'text': "1. I like __playing__ tennis.\n"
                        "2. I don't like __watching__ TV.\n"
                        "3. What sport do you like __doing__?\n"
                        "4. I like swimming. — So __do__ I!\n"
                        "5. I like hockey. — I __don't__."},
       'Wordwall «Complete the sentence · SM2 Unit 8» — СОСТАВ МОЙ')

h3.text(simg('well_done_clap') + '<p>Отличная работа! До встречи на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 4 ══
h4 = Lesson('Homework 4', 'История «The Football Club»', 3)

h4.text(simg('hello_rocket') + '<h2>Привет! Как дела?</h2>'
        '<p>Сегодня тебя ждёт интересное домашнее задание. Будем вспоминать историю, '
        'которую прошли сегодня на уроке.</p>'
        '<p>К этому домашнему заданию ты найдёшь дополнительную часть. Она необязательна, '
        'но если ты её выполнишь, будет здорово. Тебя там ждёт видео!</p>'
        '<p>Давай начинать?</p>')

h4.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_club'),
        'карточка «The Football Club» из выгрузки')

h4.text('<p>Прослушай историю и найди ответ на вопрос: <i>Who is the winner?</i></p>'
        '<p>Во время прослушивания следи за текстом по картинке ниже :)</p>'
        + img('story_club'),
        'комикс «The Football Club» из выгрузки')

h4.add('video', {'title': 'Аудио к истории',
                 'url': 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm2/u8/sm2_u8_hw4_b4.mp3', 'provider': 'file'},
       'медиафайл прислала методист')

h4.add('quiz', {'title': 'Итак, давай ответим на вопрос', 'questions': [
    q_single('Who is the winner?', 'a yellow team',
             ['a green team', 'a yellow team', 'boys', 'girls'])]},
    'ответ отмечен в выгрузке')

h4.add('truefalse', {'title': 'Проверим, насколько хорошо мы поняли историю? '
                              'Начнём с простого — выбери, верно или неверно утверждение :)',
                     'statements': [
                         {'text': 'Flash wants to play football.', 'correct': True},
                         {'text': 'At first, the boy wants Flash in his team.',
                          'correct': False},
                         {'text': 'Flash wants to join the table tennis club.',
                          'correct': False},
                         {'text': 'Misty scores a goal.', 'correct': True},
                         {'text': 'The green team wins the football game.', 'correct': False},
                         {'text': 'At the end, the boy wants Flash in his team.',
                          'correct': True}]},
       'ответы отмечены в выгрузке')

h4.add('hotspot', {'title': 'Отличная работа! Теперь посмотри на картинку и соедини '
                            'слова ребят с нужным фото',
                   'mode': 'label', 'image': url('quotes6'),
                   'points': [
                       {'x': 17, 'y': 25, 'text': "I don't like playing table tennis."},
                       {'x': 50, 'y': 25, 'text': 'Would you like to join our team?'},
                       {'x': 83, 'y': 25, 'text': 'Good job, Flash!'},
                       {'x': 17, 'y': 75, 'text': 'Well done, Misty!'},
                       {'x': 50, 'y': 75, 'text': 'Hooray!'},
                       {'x': 83, 'y': 75, 'text': "It's going to be very easy."}]},
       'в выгрузке это «Диаграмма» с шестью точками',
       todo=('Проверить, куда встали точки', 'блок «Точки на картинке» с шестью репликами',
             'координаты точек я расставил сам — в выгрузке они не сохраняются'))

h4.add('match', {'title': 'Самое непростое! Соедини вопросы с возможными ответами :) '
                          'Ты справишься!',
                 'pairs': [
                     {'left': 'Can I join your football team?', 'right': 'Yes, you can!',
                      'right_audio_tts': 'Yes, you can!'},
                     {'left': 'Do you like table tennis?', 'right': "No, I don't. It's boring.",
                      'right_audio_tts': "No, I don't. It's boring."},
                     {'left': "Let's start a football team.", 'right': 'OK!',
                      'right_audio_tts': 'OK!'},
                     {'left': 'Do you want to play a game?',
                      'right': "No, we don't. We don't like games.",
                      'right_audio_tts': "No, we don't. We don't like games."},
                     {'left': 'Would you like to be in my team?', 'right': 'No, thank you.',
                      'right_audio_tts': 'No, thank you.'}]},
       'в выгрузке опечатка «Let’s start football team» — добавил артикль')

h4.text('<h3>Вторая часть — интерактивное видео 🌟</h3>'
        '<p>Посмотри мультфильм и выполни задания, которые появятся прямо в видео.</p>')

h4.text(simg('well_done_trophy') + '<p>Ты справился! До встречи на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 5 ══
h5 = Lesson('Homework 5', 'Спортивная мечта Мэдди', 4)

h5.text(simg('hello_laptop') + '<h2>Привет, чемпион!</h2>'
        '<p>Ты большой молодец, что решил сделать домашнюю работу. Спасибо тебе за это '
        'большое! У тебя всё получится. Давай начинать :)</p>')

h5.text('<p>Начнём с очень интересного задания. Посмотри на картинку внимательно '
        'и ответь на вопрос: <i>Is there a ship?</i></p>' + img('park_scene'),
        'картинка-сцена из выгрузки')

h5.add('quiz', {'title': 'Картинку рассмотрели, теперь самое время ответить на вопрос',
                'questions': [q_single(
                    'Is there a camera?',
                    'Yes, there is. The boy in the red and white T-shirt has got a camera.',
                    ['Yes, there is. The girl in the blue dress has got a camera.',
                     'Yes, there is. The boy in the red and white T-shirt has got a camera.',
                     "No, there isn't a camera.",
                     "No, there isn't a camera. There's a smartphone."],
                    image='park_scene')]},
    'ответ отмечен в выгрузке')

h5.add('truefalse', {'title': 'Снова вернёмся к картинке — определи, верны ли предложения '
                              'ниже или нет. Будь внимателен, чтобы не попасть в ловушку 😉',
                     'image': url('park_scene'),
                     'statements': [
                         {'text': "There's a boy with a camera.", 'correct': True},
                         {'text': 'Two girls are playing tennis.', 'correct': False},
                         {'text': 'The man next to the cinema is painting a picture.',
                          'correct': False},
                         {'text': 'Some people are swimming.', 'correct': True},
                         {'text': 'Two people are playing tennis on the grass.',
                          'correct': True},
                         {'text': 'The boy with an ice cream has got trousers.',
                          'correct': False}]},
       'ответы отмечены в выгрузке; там опечатка «The boys with an ice cream has got» — '
       'исправил на «The boy … has got»')

h5.text('<p>Послушай рассказ Мэдди о её спортивной мечте (Мэдди, кстати, на картинке '
        'ниже :). Как ты думаешь: <i>What is Maddie’s favourite sport?</i></p>'
        + img('maddie'))

h5.add('video', {'title': 'Аудио: рассказ Мэдди',
                 'url': 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm2/u8/sm2_u8_hw5_b6.mp3', 'provider': 'file'},
       'аудио прислала методист')

h5.add('task', {'title': 'Внимание, вопросы о Мэдди!',
                'html': '<p>Ты наверняка ответишь на все-все-все. '
                        'Напиши ответы на вопросы ниже:</p>'
                        '<ol><li>What club does Maddie want to join?</li>'
                        '<li>When is the club?</li><li>Where is the club?</li>'
                        '<li>Who is this club for?</li></ol>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h5.add('speaking', {'title': 'Последнее задание! 🎤',
                    'html': '<p>Посмотри на картинки и опиши каждую :)</p>'
                            + img('sports6'),
                    'sample_tts': 'They are doing athletics. He is playing baseball. '
                                  'They are playing basketball. They are playing hockey. '
                                  'She is playing badminton.',
                    'needs_review': True})

h5.text(simg('well_done_smiley') + '<p>Молодец! Увидимся на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 6 ══
h6 = Lesson('Homework 6', 'Инвентарь и места для спорта', 5)

h6.text(simg('hello_headphones') + '<h2>Привет!</h2>'
        '<p>Как твои дела? Надеюсь, всё отлично! Давай начинать делать новую '
        'домашнюю работу :)</p>')

h6.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_equip'),
        'карточка «Vocabulary: Equipment & Places» из выгрузки')

h6.add('match', {'title': 'Давай вспомним предметы, которые могут нам пригодиться, когда '
                          'мы занимаемся разными видами спорта? Соедини предмет с его '
                          'названием',
                 'pairs': [{'left_image': url('g_' + g), 'right': g, 'right_audio_tts': g}
                           for g in ['helmet', 'net', 'snowboard', 'racket', 'bat',
                                     'goggles']]},
       'в выгрузке правая колонка пустая — картинки нарисовала методист')

h6.add('quiz', {'title': 'Отличная работа! Самое время усложнять задания. Прочитай '
                         'предложения и выбери наиболее подходящий вариант',
                'questions': [
    q_single('1. She wears a ___ when she rides her bike.', 'helmet',
             ['helmet', 'net', 'racket']),
    q_single('2. The fisherman can catch a lot of fish with his ___.', 'net',
             ['net', 'bat', 'helmet']),
    q_single('3. He goes ___ every single winter.', 'snowboarding',
             ['snowboarding', 'racket', 'goggles']),
    q_single('4. This badminton player always forgets his ___ at home.', 'racket',
             ['racket', 'bat', 'net']),
    q_single('5. Do you have a ___ to play table tennis?', 'bat',
             ['bat', 'racket', 'helmet']),
    q_single('6. She wears ___ to protect her eyes from the salt water in the pool.',
             'goggles', ['goggles', 'snowboarding', 'net'])]},
    'в выгрузке это «Выбери правильный вариант»')

h6.add('hotspot', {'title': 'Следующее задание — вспомним места, где занимаются спортом. '
                            'Смотри, какие красивые фотки! Соедини название места '
                            'с его картинкой',
                   'mode': 'label', 'image': url('places3'),
                   'points': [
                       {'x': 17, 'y': 50, 'text': 'track'},
                       {'x': 50, 'y': 50, 'text': 'court'},
                       {'x': 83, 'y': 50, 'text': 'pitch'}]},
       'в выгрузке это «Диаграмма» с тремя точками',
       todo=('Проверить, куда встали точки', 'блок «Точки на картинке» с тремя фото',
             'координаты точек я расставил сам — в выгрузке они не сохраняются'))

h6.add('sort', {'title': 'Супер! А теперь распредели виды спорта по местам, где ими '
                         'можно заниматься. У тебя получится 😉',
                'groups': [
                    {'name': 'court', 'items': [{'text': x, 'audio_tts': x} for x in
                                                ['basketball', 'tennis', 'badminton',
                                                 'volleyball']]},
                    {'name': 'track', 'items': [{'text': x, 'audio_tts': x} for x in
                                                ['running', 'cycling']]},
                    {'name': 'pitch', 'items': [{'text': x, 'audio_tts': x} for x in
                                                ['football', 'baseball']]}]},
       'в выгрузке это «Классификация», состав столбиков из выгрузки')

h6.add('truefalse', {'title': 'Отличная работа! А теперь давай попробуем поиграть '
                              'в следователей :) Определи, правдиво ли предложение ниже',
                     'statements': [
                         {'text': "When I play table tennis I've got my goggles and "
                                  "I'm going to the court.", 'correct': False},
                         {'text': "When I go skiing, I've got my goggles and my helmet, "
                                  "and I'm going to the mountains.", 'correct': True},
                         {'text': "When I go surfing, I've got my board and I'm going "
                                  "to the beach.", 'correct': True},
                         {'text': 'When I do athletics, I wear my shorts and a T-shirt, '
                                  "and I'm going to the court.", 'correct': False},
                         {'text': 'When I play volleyball, I take my helmet and go '
                                  'to the pitch.', 'correct': False}]},
       'ответы отмечены в выгрузке')

h6.add('task', {'title': 'Вот это ты здорово справился с заданием! Молодец :)',
                'html': '<p>А теперь исправь предложения, которые оказались '
                        'неправильными. Вот пример:</p>'
                        '<p>❌ When I go swimming, I wear my sunglasses and go to the pitch.<br>'
                        '✅ When I go swimming, I wear my goggles and go to the swimming pool.</p>'
                        '<p>Неправильное предложение можешь не переписывать 😉</p>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h6.text(simg('well_done_jump') + '<p>Замечательно! До встречи на уроке 🏅</p>')

# ═══════════════════════════════════════════════════════════ Homework 7 ══
h7 = Lesson('Homework 7', 'Повторяем весь юнит', 6)

h7.text(simg('hello_wave') + '<h2>Привет-привет, самый лучший ученик!</h2>'
        '<p>Представляешь, сегодня мы будем с тобой повторять восьмой юнит? '
        'Ты уже его весь прошёл, и ты невероятный молодец! Давай приступать?</p>')

h7.add('video', {'title': 'Видео: угадай спорт за кубиками', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h7.add('speaking', {'title': 'Начнём с видео! 🎤',
                    'html': '<p>Включи его и попробуй отгадать, что за спорт прячется '
                            'за кубиками. В промежутках называй этот спорт по образцу:</p>'
                            '<p><i>It’s basketball. It’s running.</i> И так далее :)</p>',
                    'sample_tts': "It's basketball. It's running. It's swimming.",
                    'needs_review': True})

h7.add('sort', {'title': 'Ты огромный молодец! Отличная работа :) Готов распределить '
                         'слова по столбикам: транспорт и спорт? Давай попробуем!',
                'groups': [
                    {'name': 'Transport 🚌', 'items': [{'text': x, 'audio_tts': x} for x in
                                                      ['a boat', 'a scooter', 'a ship',
                                                       'a lorry', 'a helicopter']]},
                    {'name': 'Sport 🏸', 'items': [{'text': x, 'audio_tts': x} for x in
                                                  ['athletics', 'cycling', 'running',
                                                   'badminton', 'hockey']]}]},
       'в выгрузке это «Классификация», состав столбиков из выгрузки')

h7.add('match', {'title': 'Отличная работа! А теперь определи предметы, которые связаны '
                          'между собой, и соедини их :)',
                 'pairs': [
                     {'left': 'ball', 'left_audio_tts': 'ball', 'right': 'pitch'},
                     {'left': 'helmet', 'left_audio_tts': 'helmet', 'right': 'track'},
                     {'left': 'net', 'left_audio_tts': 'net', 'right': 'court'}]})

h7.add('task', {'title': 'Супер! Даже эту простую загадку ты разгадал',
                'html': '<p>А теперь расскажи, зачем нам нужны предметы из предыдущего '
                        'упражнения. Составь три предложения по образцу:</p>'
                        '<p><i>When I play badminton, I use a racket and go to the '
                        'court.</i></p>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h7.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Впиши слова:</b></p>')

h7.add('exact_input', {'title': 'Собери слово из букв', 'items': [
    {'prompt': f'{scramble(w, "h7" + w)}  ({t})', 'accept': accept(w), 'audio_tts': w}
    for w, t in WORDS]},
    'Wordwall «Spell the word · Copy of SM 2 Unit 8 Vocabulary» — СОСТАВ МОЙ')

h7.text('<p><b>Выбери правильный вариант:</b></p>')

h7.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
    q_single('I like ___ football.', 'playing', ['playing', 'play', 'plays']),
    q_single('___ is fun.', 'Swimming', ['Swimming', 'Swim', 'Swims']),
    q_single('I like swimming. — So ___ I!', 'do', ['do', 'am', 'like']),
    q_single('You play tennis on a ___.', 'court', ['court', 'track', 'pitch']),
    q_single('You play football on a ___.', 'pitch', ['court', 'track', 'pitch']),
    q_single('You need ___ to swim.', 'goggles', ['goggles', 'a racket', 'a helmet'])]},
    'Wordwall «Gameshow quiz · SM2 Unit 8 grammar» — СОСТАВ МОЙ')

h7.text(simg('congrats_popper') +
        '<p>Восьмой юнит позади! Ты большой молодец 🎉</p><p>До встречи на уроке!</p>')

# ════════════════════════════════════════════════════════════════ Test ══
t = Lesson('Unit 8 Test', 'Итоговый тест по юниту', 7, kind='test', threshold=90)

t.text('<h2>Super Minds 2 · Unit 8 Test</h2>'
       '<p>Проверим, как ты усвоил юнит. Будь внимателен — у теста высокий проходной балл.</p>')

TMASK = [('badminton', 'b _ d m i n t _ n'), ('table tennis', 't _ b l e  t e n n _ s'),
         ('tennis', 't _ n n i s'), ('baseball', 'b _ s e b a l l'),
         ('basketball', 'b a s k _ t b a l l'), ('volleyball', 'v _ l l e y b a l l'),
         ('swimming', 's w _ m m i n g'), ('football', 'f _ o t b a l l'),
         ('athletics', 'a t h l _ t i c s'), ('hockey', 'h _ c k e y')]

t.add('exact_input', {'title': 'Впиши буквы', 'items': [
    {'prompt': f'{m} — напиши слово целиком ({tr})', 'accept': accept(w), 'audio_tts': w}
    for (w, m), (_, tr) in zip(TMASK, WORDS)]},
    'в выгрузке это «Заполни пропуски» по словарю юнита (10 слов)')

t.add('match', {'title': 'Соедини слова с картинками', 'pairs': [
    {'left_image': url(PIC[w.lower()]), 'right': w, 'right_audio_tts': w}
    for w in ['Badminton', 'Baseball', 'Basketball', 'Football', 'Hockey']]},
    'в выгрузке правая колонка пустая — картинки нарисовала методист')

t.add('gaps', {'title': 'Прочитай предложения и заполни пропуски', 'mode': 'drag',
               'text': "1. You need special clothes and water to do this sport — "
                       "__swimming__.\n"
                       "2. You play it with rackets — __tennis__.\n"
                       "3. You play it with rackets and you need a special table — "
                       "__table tennis__.\n"
                       "4. You do this sport alone — __athletics__.\n"
                       "5. You need skates and ice to do this sport — __hockey__."},
      'в выгрузке опечатки «rockets» и «a special desk» — исправил на rackets и table')

t.add('quiz', {'title': 'Заполни пропуски — выбери подходящий вариант', 'questions': [
    q_single('A: What ___ you think about football?', 'do', ['do', 'does']),
    q_single('A: What do you ___ about football?', 'think', ['think', 'thinking']),
    q_single('B: I think ___ football is boring.', 'playing', ['playing', 'play', 'doing']),
    q_single('A: What music do you like ___ to?', 'listening', ['listening', 'listen']),
    q_single('B: I ___ listening to pop music.', 'like', ['like', 'liking', 'playing']),
    q_single('A: Do you like ___ tennis?', 'playing', ['playing', 'play', 'doing']),
    q_single('B: No, I don’t. But I like ___ it on TV.', 'watching', ['watching', 'watch']),
    q_single('A: I like ___ a bike.', 'riding', ['riding', 'ride', 'rode']),
    q_single('B: ___ do I!', 'So', ['So', 'Mee', 'But']),
    q_single('___ basketball is interesting.', 'Playing', ['Playing', 'Play', 'Doing', 'Do'])]},
    'в выгрузке это пять блоков «Выбери правильный вариант» — свёл в один тест')

for words in ['Dancing/is/a/good/hobby.', 'Playing/hockey/is/dangerous.',
              'What/do/you/think/about/football?', 'What/sport/do/you/like/doing?',
              'I/like/playing/computer/games.']:
    ws = words.split('/')
    t.add('order', {'words': ws, 'sentence': ' '.join(ws), 'audio_tts': ' '.join(ws)},
          'в выгрузке это «Составь предложение»')

READING = (
    '<h3>READING</h3>'
    '<p>Hello! My name is Zoe. I love sport, but not all sports!</p>'
    '<p>My favourite sport is swimming. I go to the swimming pool every Saturday. '
    'I like playing tennis too, and I like running on the track with my friends.</p>'
    '<p>At school we play basketball. It’s great — I like playing basketball very much. '
    'And in the winter I go skiing with my dad. Skiing is fantastic!</p>'
    '<p>But I don’t like playing football. It’s boring for me. '
    'And I don’t like hockey — I think hockey is dangerous.</p>')

t.text(READING,
       'ТЕКСТ МОЙ: в выгрузке у блока READING остались только пустые столбики, '
       'самого текста нет',
       todo=('Прочитать текст для READING', 'блок «Материал» с текстом про Zoe',
             'в выгрузке нет ни текста, ни состава столбиков — написала их я'))

t.add('sort', {'title': 'Прочитай текст. Перетащи каждый вид спорта в нужный столбик',
               'groups': [
                   {'name': '✅ Zoe likes', 'items': [{'text': x, 'audio_tts': x} for x in
                                                     ['swimming', 'tennis', 'running',
                                                      'basketball', 'skiing']]},
                   {'name': "❌ Zoe doesn't like", 'items': [{'text': x, 'audio_tts': x}
                                                            for x in ['football', 'hockey']]}]},
      'в выгрузке столбики пустые — заполнил по тексту, который написала я')

t.text('<h3>LISTENING</h3><p>Послушай запись. Прочитай предложения и выбери '
       '«Верно» или «Неверно».</p>')

t.add('video', {'title': 'Аудио к заданию LISTENING',
                'url': 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm2/u8/sm2_u8_test_b14.mp3', 'provider': 'file'},
      'аудио прислала методист')

t.add('truefalse', {'title': 'Верно или неверно?', 'statements': [
    {'text': 'Sam likes playing volleyball.', 'correct': True},
    {'text': 'Playing tennis is boring for Sam.', 'correct': False},
    {'text': "Lisa doesn't like swimming.", 'correct': False},
    {'text': 'Lisa likes athletics.', 'correct': True},
    {'text': 'Sam and Lisa both like football.', 'correct': True},
    {'text': "Lisa thinks hockey's dangerous.", 'correct': True}]},
    'ответы отмечены в выгрузке')

t.add('speaking', {'title': 'SPEAKING TASK 🎤',
                   'html': '<p>Ответь на вопросы:</p>'
                           '<ol><li>What is your favourite transport and why?</li>'
                           '<li>Do you think reading a book is boring?</li>'
                           '<li>How old are you?</li>'
                           '<li>Can you fly a kite in the street?</li>'
                           '<li>Can you play tennis at home?</li>'
                           '<li>What is your favourite sport and why?</li>'
                           '<li>Do you go to bed at 10 o’clock?</li>'
                           '<li>What is your favourite day and why?</li>'
                           '<li>Is playing badminton difficult?</li>'
                           '<li>Do you like hockey? Why?</li></ol>'
                           '<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>',
                   'sample_tts': 'My favourite transport is the bus. I think reading '
                                 'a book is great. I am eight years old.',
                   'needs_review': True})

t.text(simg('good_luck_clover') + '<p>Тест пройден! Отличная работа 👏</p>')

# ═════════════════════════════════════════════════════════════════════════
LESSONS = [h1, h2, h3, h4, h5, h6, h7, t]

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for i, les in enumerate(LESSONS):
        fn = f'{OUT}/{i:02d}_{les.title.lower().replace(" ", "_")}.sql'
        open(fn, 'w').write(les.sql())
        print(f'{fn}: {len(les.blocks)} блоков')
    print('всего блоков:', sum(len(l.blocks) for l in LESSONS))
