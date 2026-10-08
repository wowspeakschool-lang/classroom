# -*- coding: utf-8 -*-
"""SM2 · Unit 7 · Transport — сборка всех восьми уроков."""
import os
import u_lib as L
from u_lib import (Lesson, url, simg, img, accept, scramble, distract,
                   q_single, q_multi)

L.setup('Unit 7 · Transport', 7, 'sm2/u7')
OUT = 'u7sql'

WORDS = [('helicopter', 'вертолёт'), ('ship', 'корабль'), ('lorry', 'грузовик'),
         ('boat', 'лодка'), ('scooter', 'самокат'), ('skateboard', 'скейтборд'),
         ('motorbike', 'мотоцикл'), ('taxi', 'такси'), ('bus', 'автобус')]
W = [w for w, _ in WORDS]

VIDEO = ('Ссылка на видео', 'блок «Видео/аудио» пустой',
         'в выгрузке медиафайла нет — платформа его не отдаёт')
AUDIO = ('Ссылка на аудио', 'блок «Видео/аудио» пустой',
         'в выгрузке медиафайла нет — платформа его не отдаёт')

# ═══════════════════════════════════════════════════════════ Homework 1 ══
h1 = Lesson('Homework 1', 'Транспорт — новые слова', 0)

h1.text(simg('hello_wave') + '<h2>Привет!</h2>'
        '<p>Сейчас мы с тобой выучим все слова, которые разобрали на уроке. '
        'Выполни все задания, чтобы выучить слова на 100%! В конце урока тебя ждёт тест — '
        'чтобы его пройти, нужно набрать 90 баллов.</p>'
        '<p>Как только ты выполнишь это задание, тебя ждёт ещё одно ДОПОЛНИТЕЛЬНОЕ. '
        'Его можно выполнить по желанию. Но если ты его сделаешь — ты будешь МЕГА КРУТЫМ! '
        'У тебя всё получится. Успехов! ❤</p>',
        'приветствие; в выгрузке урок разбит на части (1) и (2) — свёл в один')

h1.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_transport'),
        'карточка «Vocabulary · Transport Words» из выгрузки')

h1.add('flashcards', {'title': 'Запомни слова', 'cards': [
    {'text': w, 'translation': t, 'image': url('t_' + w), 'audio_tts': w}
    for w, t in WORDS]},
    'механика «Запомни» из выгрузки; картинки нарисовала методист')

h1.add('quiz', {'title': 'Послушай и выбери', 'questions': [
    q_single('Послушай и выбери, что ты услышал', w,
             sorted([w] + distract(w, W, 2, 'h1s' + w)), audio_tts=w)
    for w, _ in WORDS]},
    'механика «Послушай» из выгрузки')

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
        '<p>Привет! Это дополнительная часть твоего домашнего задания. Ты большой молодец, '
        'что решил её сделать. Давай скорее приступать!</p>',
        'начало части (2) из выгрузки')

h1.text('<p>Начнём с кроссворда. Смотри на картинки и вписывай слова. '
        'У тебя наверняка получится сделать всё быстро и правильно 😁</p>')

h1.add('exact_input', {'title': 'Кроссворд: смотри на картинку и впиши слово', 'items': [
    {'prompt': f'{i + 1}.', 'image': url('t_' + w), 'accept': accept(w), 'audio_tts': w}
    for i, (w, _) in enumerate(WORDS)]},
    'в выгрузке это внешний кроссворд «Transport» — пересобрал вводом слов, СОСТАВ МОЙ')

h1.add('sort', {'title': 'Этот непростой кроссворд оказался для тебя очень лёгким. '
                         'А давай теперь посмотрим на это задание? '
                         'Распредели транспорт по столбикам :)',
                'groups': [
                    {'name': 'water transport 💦', 'items': [{'text': x, 'audio_tts': x}
                                                            for x in ['a ship', 'a boat']]},
                    {'name': 'land transport 🛣', 'items': [
                        {'text': x, 'audio_tts': x}
                        for x in ['a bus', 'a car', 'a taxi', 'a scooter']]},
                    {'name': 'air transport ☁', 'items': [
                        {'text': x, 'audio_tts': x} for x in ['a plane', 'a helicopter']]}]},
       'в выгрузке это «Классификация», состав столбиков из выгрузки')

h1.add('task', {'title': 'Время для творчества!',
                'html': '<p>Нарисуй свой транспорт, можно даже несколько. Приложи фото '
                        'рисунка сюда, в Мой Класс, или принеси рисунок на урок 😉</p>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h1.add('speaking', {'title': 'Последнее задание на сегодня 🎤',
                    'html': '<p>Посмотри на свой классный рисунок и опиши его. '
                            'Можешь послушать пример перед тем, как записать свой ответ.</p>',
                    'sample_tts': "This is my transport. It's a big red bus. "
                                  "It goes on land. I'd like to drive it!",
                    'needs_review': True})

h1.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Соедини картинки со словами:</b></p>')

h1.add('match', {'title': 'Соедини картинку со словом', 'pairs': [
    {'left_image': url('t_' + w), 'right': w, 'right_audio_tts': w} for w, _ in WORDS]},
    'Wordwall «Соедини картинки со словами» — СОСТАВ МОЙ, содержимого игры в выгрузке нет')

h1.text('<p><b>Впиши слова:</b></p>')

h1.add('exact_input', {'title': 'Собери слово из букв', 'items': [
    {'prompt': f'{scramble(w, "h1w" + w)}  ({t})', 'accept': accept(w), 'audio_tts': w}
    for w, t in WORDS]},
    'Wordwall «Впиши слова» — СОСТАВ МОЙ')

h1.text(simg('well_done_medal') + '<p>Поздравляю, домашняя работа выполнена! '
        'До встречи на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 2 ══
h2 = Lesson('Homework 2', 'I’d like to… — о чём мечтают люди', 1)

h2.text(simg('hello_highfive') + '<h2>Привет!</h2>'
        '<p>Ну что, готов к новому домашнему заданию? Наверняка готов :) Давай начинать!</p>')

h2.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_would'),
        'карточка «Grammar 1 · I’d like to…» из выгрузки')

h2.text('<p>Начнём с видео! Посмотри его и сделай задание ниже. Будь внимателен 😉</p>')

h2.add('video', {'title': 'Видео к уроку', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h2.add('gaps', {'title': 'Ура! Видео посмотрели, давай теперь проверим, как хорошо мы '
                         'запомнили правило с урока. Заполни пропуски нужными словами',
                'mode': 'drag',
                'text': "1. I __would__ like to answer that question.\n"
                        "2. I would __like__ to become a doctor.\n"
                        "3. I would like to __see__ you more often.\n"
                        "4. I would like __to__ thank you."})

h2.add('hotspot', {'title': 'Отличная работа! Правило запомнили. А теперь посмотри '
                            'на картинку ниже. Люди мечтают о разных вещах. '
                            'Соедини мысль с человеком, которому она подходит',
                   'mode': 'label', 'image': url('dreams'),
                   'points': [
                       {'x': 22, 'y': 68, 'text': "I'd like to fly to Canada and see a bear."},
                       {'x': 48, 'y': 70, 'text': "I'd like to go sailing on a big boat."},
                       {'x': 85, 'y': 20, 'text': "I'd like to drive a lorry."}]},
       'в выгрузке это «Диаграмма» с тремя точками',
       todo=('Проверить, куда встали точки', 'блок «Точки на картинке» с тремя мечтами',
             'координаты точек я расставил сам — в выгрузке они не сохраняются'))

h2.add('gaps', {'title': 'И с этим заданием ты справился! А что насчёт этого? '
                         'Выбери правильный вариант ответа. Будь внимателен, '
                         'здесь есть ловушки 😁',
                'mode': 'drag',
                'text': "1. I'd like to __go__ to the jungle by bus.\n"
                        "2. I'd __like to__ eat a pizza.\n"
                        "3. I __'d like__ to see an elephant.\n"
                        "4. I'd like to __fly to__ Africa.\n"
                        "5. I'd like __to sail__ around the world.\n"
                        "6. I'd like to __drive__ a bus."},
       'в выгрузке это «Выбери правильный вариант»')

h2.add('match', {'title': 'Помнишь, недавно мы говорили про транспорт? Ты наверняка '
                          'запомнил все слова на 💯 процентов. Давай проверим? '
                          'Соедини картинку с подходящей фразой',
                 'pairs': [
                     {'left_image': url('t_train'), 'right': "I'd like to drive a train.",
                      'right_audio_tts': "I'd like to drive a train."},
                     {'left_image': url('t_helicopter'), 'right': "I'd like to fly a helicopter.",
                      'right_audio_tts': "I'd like to fly a helicopter."},
                     {'left_image': url('t_motorbike'), 'right': "I'd like to ride a motorbike.",
                      'right_audio_tts': "I'd like to ride a motorbike."},
                     {'left_image': url('t_boat'), 'right': "I'd like to sail a boat.",
                      'right_audio_tts': "I'd like to sail a boat."},
                     {'left_image': url('t_scooter'), 'right': "I'd like to ride a scooter.",
                      'right_audio_tts': "I'd like to ride a scooter."},
                     {'left_image': url('t_lorry'), 'right': "I'd like to drive a lorry.",
                      'right_audio_tts': "I'd like to drive a lorry."}]},
       'в выгрузке правая колонка пустая — картинки нарисовала методист')

h2.add('task', {'title': 'Теперь твоя очередь мечтать 🗯',
                'html': '<p>Придумай, куда бы ты хотел отправиться (страна, город, место) '
                        'и какой транспорт ты для этого бы использовал. '
                        'Напиши два предложения о своей мечте.</p>'
                        '<p>Пример: <i>I’d like to visit France. '
                        'I’d like to go to France by plane.</i></p>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h2.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Выбери правильный вариант:</b></p>')

h2.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
    q_single("I'd like ___ a helicopter.", 'to fly', ['to fly', 'to drive', 'to sail']),
    q_single("I'd like ___ a boat.", 'to sail', ['to sail', 'to ride', 'to fly']),
    q_single("I'd like ___ a motorbike.", 'to ride', ['to ride', 'to sail', 'to fly']),
    q_single("I'd like ___ a lorry.", 'to drive', ['to drive', 'to sail', 'to fly']),
    q_single('I ___ like to go to Japan.', 'would', ['would', 'will', 'want'])]},
    'Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ')

h2.text('<p><b>Расставь слова в правильном порядке:</b></p>')

for words in ["I'd/like/to/fly/a/plane.", "I'd/like/to/sail/a/ship.",
              "I'd/like/to/ride/a/scooter.", "I'd/like/to/drive/a/taxi."]:
    ws = words.split('/')
    h2.add('order', {'words': ws, 'sentence': ' '.join(ws), 'audio_tts': ' '.join(ws)},
           'Wordwall «Расставь слова в правильном порядке» — СОСТАВ МОЙ')

h2.text(simg('well_done_star') + '<p>Молодец! Увидимся на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 3 ══
h3 = Lesson('Homework 3', 'Present Continuous: что ты делаешь сейчас', 2)

h3.text(simg('hello_book') + '<h2>Привет!</h2>'
        '<p>Сегодня тебя ждёт новая домашняя работа. Давай приступать!</p>')

h3.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_cont'),
        'карточка «Grammar 2 · Present Continuous Q&A» из выгрузки')

h3.text('<p>Начнём с видео! Посмотри и найди ответ на вопрос: <i>Who is sleeping?</i></p>')

h3.add('video', {'title': 'Видео: Who is sleeping?', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h3.add('quiz', {'title': 'Давай выберем правильный ответ на вопрос выше', 'questions': [
    q_single('Who is sleeping?', 'a girl with yellow hair',
             ['a girl with brown hair', 'a girl with yellow hair',
              'a boy with brown hair', 'a boy with yellow hair'])]},
    'ответ отмечен в выгрузке')

h3.add('match', {'title': 'Супер! А теперь давай проверим, насколько внимательно ты смотрел '
                          'видео. Соедини слова с человеком, который их произнёс',
                 'pairs': [
                     {'left_image': url('k_asking'), 'right': 'What are you doing?',
                      'right_audio_tts': 'What are you doing?'},
                     {'left_image': url('k_drawing'), 'right': "I'm drawing.",
                      'right_audio_tts': "I'm drawing."},
                     {'left_image': url('k_jumping'), 'right': "I'm jumping.",
                      'right_audio_tts': "I'm jumping."},
                     {'left_image': url('k_sleeping'), 'right': 'She is sleeping.',
                      'right_audio_tts': 'She is sleeping.'}]},
       'в выгрузке правая колонка пустая — картинки нарисовала методист')

h3.add('gaps', {'title': 'Посмотри на картинку ниже. Ребята играют в пантомиму. '
                         'Прочитай их диалог и заполни пропуски недостающими словами',
                'mode': 'drag', 'image': url('mime'),
                'text': "Boy: What __are__ you doing? Are __you__ driving a car?\n"
                        "Girl: No, I'm __not__.\n"
                        "Boy: Are you __driving__ a big lorry?\n"
                        "Girl: Yes, I __am__!"})

h3.text('<p>С каждым заданием у тебя получается всё лучше и лучше! Посмотри на картинку '
        'и впиши слова в нужной форме :)</p>'
        '<p>Пример: <i>She is dancing (dance)</i> или <i>She’s dancing.</i></p>')

for pic, verb, ans, alt in [
        ('ac_basketball', 'play',  'is playing',  "'s playing"),
        ('ac_reading',    'read',  'is reading',  "'s reading"),
        ('ac_bike',       'ride',  'is riding',   "'s riding"),
        ('ac_sleeping',   'sleep', 'is sleeping', "'s sleeping"),
        ('ac_singing',    'sing',  'is singing',  "'s singing"),
        ('ac_flying',     'fly',   'is flying',   "'s flying"),
        ('ac_eating',     'eat',   'is eating',   "'s eating"),
        ('ac_jumping',    'jump',  'is jumping',  "'s jumping")]:
    tail = {'play': 'basketball.', 'read': 'a book.', 'ride': 'a bike.',
            'sleep': 'in the bed.', 'sing': 'a song.', 'fly': 'in the sky.',
            'eat': 'lunch.', 'jump': '.'}[verb]
    subj = {'sleep': 'She', 'sing': 'She', 'fly': 'It'}.get(verb, 'He')
    h3.add('exact_input', {'image': url(pic), 'items': [
        {'prompt': f'{subj} ___ ({verb}) {tail}'.replace(' .', '.'),
         'accept': [ans, alt], 'audio_tts': f'{subj} {ans} {tail}'.replace(' .', '.')}]},
        'в выгрузке это «Впиши в пропуски», альтернативный ответ — краткая форма')

h3.text('<p>Как здорово у тебя получается! Самое время перейти к вопросам 😁 '
        'Составь предложения так, чтобы англичане точно поняли, что ты хочешь у них '
        'спросить.</p>')

for words in ['What/are/you/doing/?', 'Are/you/playing/football/?',
              'Is/she/riding/a/scooter/?', 'What/is/she/doing/?',
              'Are/you/eating/an ice cream/?', 'Is/he/playing/computer games/?']:
    ws = words.split('/')
    h3.add('order', {'words': ws, 'sentence': ' '.join(ws), 'audio_tts': ' '.join(ws)},
           'в выгрузке это «Составь предложение»')

h3.add('match', {'title': 'А теперь давай попробуем найти ответы на эти вопросы. Заодно '
                          'проверим, насколько классные мы сыщики 🕵️',
                 'pairs': [
                     {'left': 'What are you doing?', 'right': "I'm dancing.",
                      'right_audio_tts': "I'm dancing."},
                     {'left': 'Are you playing football?', 'right': "No, I'm not.",
                      'right_audio_tts': "No, I'm not."},
                     {'left': 'Is she riding a scooter?', 'right': 'Yes, she is.',
                      'right_audio_tts': 'Yes, she is.'},
                     {'left': 'What is she doing?', 'right': "She's sailing a boat.",
                      'right_audio_tts': "She's sailing a boat."},
                     {'left': 'Is he playing computer games?', 'right': 'Yes, he is.',
                      'right_audio_tts': 'Yes, he is.'}]})

h3.add('speaking', {'title': 'Теперь твоя очередь! 🎤',
                    'html': '<p>Ответь на вопросы ниже устно (не забывай, что вопросы про то, '
                            'что ты делаешь сейчас :)</p>'
                            '<ol><li>Are you riding a bike?</li>'
                            '<li>Is your friend walking?</li>'
                            '<li>Are you learning English?</li>'
                            '<li>Are you sitting?</li>'
                            '<li>What are you doing?</li></ol>',
                    'sample_tts': "No, I'm not riding a bike. I'm learning English. "
                                  "Yes, I'm sitting.",
                    'needs_review': True})

h3.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Выбери правильный вариант:</b></p>')

h3.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
    q_single('What ___ you doing?', 'are', ['am', 'is', 'are']),
    q_single('She ___ riding a bike.', 'is', ['am', 'is', 'are']),
    q_single('Are you sailing a boat? — Yes, ___.', 'I am', ['I am', 'I is', 'I are']),
    q_single('He is ___ a taxi.', 'driving', ['drive', 'driving', 'drives']),
    q_single('They ___ playing football.', 'are', ['am', 'is', 'are'])]},
    'Wordwall «Find the match · SM2 Transport» и «Quiz · Present Continuous SM2 Unit 7» — '
    'СОСТАВ МОЙ, содержимого игр в выгрузке нет')

h3.text('<p><b>И ещё раз — выбери правильный вариант:</b></p>')

h3.add('quiz', {'title': 'Ещё немного практики', 'questions': [
    q_single('Is she sleeping? — No, ___.', "she isn't", ["she isn't", "she aren't", "she not"]),
    q_single('What ___ he doing?', 'is', ['am', 'is', 'are']),
    q_single('I ___ reading a book.', 'am', ['am', 'is', 'are']),
    q_single('Are they jumping? — Yes, ___.', 'they are', ['they are', 'they is', 'they am'])]},
    'второй Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ')

h3.text(simg('well_done_clap') + '<p>Отличная работа! До встречи на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 4 ══
h4 = Lesson('Homework 4', 'История «The Bus Trip»', 3)

h4.text(simg('hello_rocket') + '<h2>Привет-привет, самый лучший ученик!</h2>'
        '<p>Сегодня будем вспоминать видео, которое ты смотрел на уроке.</p>'
        '<p>К этой домашней работе есть ещё дополнительное задание. Его выполнять '
        'необязательно, но если ты захочешь его сделать, будет очень здорово!</p>'
        '<p>Ну что, готов начинать?</p>')

h4.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_bustrip'),
        'карточка «The Bus Trip» из выгрузки')

h4.text('<p>Давай послушаем аудио и найдём ответ на вопрос: '
        '<i>Where would children like to go?</i></p>')

h4.add('video', {'title': 'Аудио к истории',
                 'url': 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm2/u7/sm2_u7_hw4_b4.mp3', 'provider': 'file'},
       'медиафайл прислала методист')

h4.text('<p>Прочитай историю:</p>' + img('story_bus'),
        'комикс «The Bus Trip» из выгрузки')

h4.add('quiz', {'title': 'Барабанная дробь 🥁', 'questions': [
    q_single('Where would children like to go?', 'to the beach',
             ['to the airport', 'to the beach', 'to school', 'to the playground'])]},
    'ответ отмечен в выгрузке')

h4.add('match', {'title': 'Супер! Давай теперь попробуем вспомнить, кто и что говорил? '
                          'Соедини фразу с человеком, который её произнёс',
                 'pairs': [
                     {'left': 'No problem.', 'right': 'Whisper', 'right_audio_tts': 'Whisper'},
                     {'left': 'I think I can help.', 'right': 'Thunder',
                      'right_audio_tts': 'Thunder'},
                     {'left': "Now it's my turn to help you.", 'right': 'The driver',
                      'right_audio_tts': 'The driver'}]},
       'в выгрузке правая колонка пустая — подставил имена героев из комикса')

h4.add('truefalse', {'title': 'Проверим, насколько внимательно мы прочитали историю? '
                              'Определи, верно или неверно утверждение',
                     'statements': [
                         {'text': 'The children are excited.', 'correct': True},
                         {'text': 'There are lots of lizards on the road.', 'correct': False},
                         {'text': "They've got a problem with a plane.", 'correct': False},
                         {'text': 'The driver can help.', 'correct': True},
                         {'text': "They're going to the restaurant.", 'correct': False}]},
       'ответы отмечены в выгрузке; там опечатка «They’ve got problem» — исправил')

h4.add('speaking', {'title': 'А теперь мы с тобой отправляемся в театральный кружок! 🎭',
                    'html': '<p>Представь, что ты Thunder. Расскажи историю от его лица.</p>'
                            '<p>Чтобы было понятнее, как это можно сделать, сначала послушай '
                            'историю от Уиспера.</p>',
                    'sample_tts': "A day at the beach! I'm excited. Oh no, the bus isn't "
                                  "moving. There are lots of sheep on the road. "
                                  "I think I can help!",
                    'needs_review': True})

h4.text('<h3>Вторая часть — интерактивное видео 🌟</h3>'
        '<p>Посмотри мультфильм и выполни задания, которые появятся прямо в видео.</p>')

h4.text(simg('well_done_trophy') + '<p>Ты справился! До встречи на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 5 ══
h5 = Lesson('Homework 5', 'История Мэри про путешествия', 4)

h5.text(simg('hello_laptop') + '<h2>Привет!</h2>'
        '<p>Вот и новая домашняя работа. Ты большой молодец, что решил её сделать. '
        'Время пролетит незаметно. Let’s go!</p>')

h5.text('<p>А теперь тебя ждёт текст! Прочитай историю Мэри про её путешествие.</p>'
        + img('mary_text'),
        'текст из выгрузки')

h5.add('speaking', {'title': 'Прочитай текст вслух 🎤',
                    'html': '<p>Нажми на микрофончик и запиши, как ты читаешь этот текст 😁</p>'
                            + img('mary_text'),
                    'sample_tts': "Hi. My name's Mary. I like travelling. My family and "
                                  "friends live in different countries.",
                    'needs_review': True})

h5.add('match', {'title': 'А теперь давай вспомним, как путешествует Мэри? '
                          'Соедини картинку с названием транспорта',
                 'pairs': [
                     {'left_image': url('t_plane'), 'right': 'Jessica — by plane',
                      'right_audio_tts': 'Jessica by plane'},
                     {'left_image': url('t_train'), 'right': 'Boris — by train',
                      'right_audio_tts': 'Boris by train'},
                     {'left_image': url('t_bike'), 'right': 'Cousin Sara — riding her bike',
                      'right_audio_tts': 'Cousin Sara riding her bike'},
                     {'left_image': url('t_car'), 'right': 'Italy — by car',
                      'right_audio_tts': 'Italy by car'}]},
       'в выгрузке правая колонка пустая — картинки нарисовала методист')

h5.add('task', {'title': 'Теперь твоя очередь!',
                'html': '<p>Расскажи, каким транспортом любишь пользоваться ты :)</p>'
                        '<p>Чтобы было немножко легче, пока будешь писать, отвечай '
                        'на эти вопросы:</p>'
                        '<ul><li>What is your favourite transport?</li>'
                        '<li>Where do you go by this transport?</li>'
                        '<li>Where does your friend live?</li>'
                        '<li>What transport do you use to visit your friend?</li></ul>'
                        '<p>У тебя должно получиться 4–5 предложений.</p>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h5.text(simg('well_done_smiley') + '<p>Молодец! Увидимся на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 6 ══
h6 = Lesson('Homework 6', 'Где ездит транспорт: on land / on water / in the air', 5)

h6.text(simg('hello_headphones') + '<h2>Добро пожаловать в домашнее задание!</h2>'
        '<p>Тебя ждут интересные видео и увлекательные упражнения.</p>'
        '<p>А ещё тебя ждёт ДОПОЛНИТЕЛЬНОЕ задание, которое ты можешь выполнить '
        'по желанию, НО если ты его сделаешь, то будешь нереально крут!</p>')

h6.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_where'),
        'карточка «Where Does Transport Go?» из выгрузки')

h6.add('match', {'title': 'Посмотри на картинки — это различные виды транспорта, которые '
                          'ты уже знаешь! Сопоставь картинки с типами транспорта ;)',
                 'pairs': [
                     {'left_image': url('w_land'), 'right': 'on land',
                      'right_audio_tts': 'on land'},
                     {'left_image': url('w_water'), 'right': 'on water',
                      'right_audio_tts': 'on water'},
                     {'left_image': url('w_air'), 'right': 'in the air',
                      'right_audio_tts': 'in the air'}]},
       'в выгрузке правая колонка пустая — картинки нарисовала методист')

h6.add('sort', {'title': 'А теперь распредели по категориям! Как думаешь, частями каких '
                         'видов транспорта являются эти вещи?',
                'groups': [
                    {'name': 'on water', 'items': [{'text': x, 'audio_tts': x}
                                                   for x in ['a sail', 'an anchor']]},
                    {'name': 'on land', 'items': [{'text': x, 'audio_tts': x}
                                                  for x in ['a wheel', 'a road']]},
                    {'name': 'in the air', 'items': [{'text': x, 'audio_tts': x}
                                                     for x in ['a wing', 'a propeller']]}]},
       'в выгрузке это «Классификация», но элементы пустые — СОСТАВ МОЙ',
       todo=('Посмотреть состав задания', 'блок «Классификация» с тремя столбиками',
             'в выгрузке столбики пустые — я подобрал по две детали на каждый вид транспорта'))

h6.add('match', {'title': 'А теперь давай попробуем соединить разные принадлежности '
                          'и предметы инвентаря и транспорт, для которого они нужны. Вперёд!',
                 'pairs': [
                     {'left_image': url('p_motorbike'), 'right': 'I ride a motorbike.',
                      'right_audio_tts': 'I ride a motorbike.'},
                     {'left_image': url('p_taxi'), 'right': 'I drive a taxi.',
                      'right_audio_tts': 'I drive a taxi.'},
                     {'left_image': url('p_canoe'), 'right': "I've got a canoe.",
                      'right_audio_tts': "I've got a canoe."},
                     {'left_image': url('p_skateboard'), 'right': "I've got a skateboard.",
                      'right_audio_tts': "I've got a skateboard."},
                     {'left_image': url('p_helicopter'), 'right': 'I fly a helicopter.',
                      'right_audio_tts': 'I fly a helicopter.'},
                     {'left_image': url('p_sailboat'), 'right': 'I sail a boat.',
                      'right_audio_tts': 'I sail a boat.'}]},
       'в выгрузке правая колонка пустая — картинки нарисовала методист')

h6.add('task', {'title': 'Попробуй нарисовать группы транспорта — on land, in the air, '
                         'on water!',
                'html': '<p>Ниже прикреплён пример такого рисунка. Можешь нарисовать одну '
                        'группу, две или даже все три — как тебе хочется!</p>'
                        + img('draw_example') +
                        '<p>Я буду рада полюбоваться твоим рисунком на уроке!</p>'
                        '<p>Если хочется, можешь нарисовать какой-нибудь необычный транспорт '
                        '(например, водный автобус)! Удачи!</p>',
                'needs_review': True})

h6.text(simg('well_done_jump') + '<p>Замечательно! До встречи на уроке 🎨</p>')

# ═══════════════════════════════════════════════════════════ Homework 7 ══
h7 = Lesson('Homework 7', 'Повторяем весь юнит', 6)

h7.text(simg('hello_wave') + '<h2>Привет!</h2>'
        '<p>Сегодня в домашнем задании тебя ждут задания на повторение. Ты отлично '
        'занимался, поэтому наверняка всё сделаешь на 💯 Давай начинать!</p>')

REV = ['ship', 'bike', 'bus', 'motorbike', 'helicopter', 'taxi',
       'lorry', 'scooter', 'boat', 'submarine', 'rocket']

h7.add('match', {'title': 'Начнём с простого? С этим заданием ты справишься быстро! '
                          'Соедини название транспорта с его картинкой',
                 'pairs': [{'left_image': url('t_' + w), 'right': w, 'right_audio_tts': w}
                           for w in REV]},
       'в выгрузке левая колонка пустая — картинки нарисовала методист')

h7.text('<p>Переходим к видео! Ответь на вопросы: <i>What is he doing? What is she doing?</i></p>'
        '<p>Предложения зачитывай полностью 😄 Пример: <i>They are watching.</i></p>')

h7.add('video', {'title': 'Видео к вопросам', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h7.text('<p>Вау! Как здорово ты справился с предыдущим заданием! А что насчёт этого? '
        'Прочитай вопрос, посмотри на картинку и впиши свой ответ :)</p>'
        '<p>Пример: <i>What would you like to do? — I’d like to fly a plane.</i></p>')

for pic, ans in [('d_plane', "I'd like to fly a plane."),
                 ('d_boat', "I'd like to sail a boat."),
                 ('d_jump', "I'd like to jump."),
                 ('d_dance', "I'd like to dance."),
                 ('d_train', "I'd like to go by train.")]:
    h7.add('exact_input', {'image': url(pic), 'items': [
        {'prompt': 'What would you like to do?', 'accept': [ans], 'audio_tts': ans}]},
        'в выгрузке это «Впиши в пропуски» с картинкой')

h7.add('gaps', {'title': 'А теперь мы превращаемся в составителей таблиц! Определи, '
                         'в каких местах транспорт обычно находится, а в каких — нет. '
                         'Если находится — пиши yes, если нет — no',
                'mode': 'drag',
                'text': "Пример: a plane — in the air: yes, on water: no, on land: yes\n"
                        "1. a helicopter — in the air: __yes__, on water: __no__, "
                        "on land: __yes__\n"
                        "2. a boat — in the air: __no__, on water: __yes__, on land: __yes__\n"
                        "3. a motorbike — in the air: __no__, on water: __no__, "
                        "on land: __yes__\n"
                        "4. a bus — in the air: __no__, on water: __no__, on land: __yes__\n"
                        "5. a lorry — in the air: __no__, on water: __no__, on land: __yes__"},
       'в выгрузке это таблица «Впиши в пропуски» с ответами yes/no')

h7.add('task', {'title': 'Последнее задание на сегодня',
                'html': '<p>Расскажи в трёх-четырёх предложениях о своей мечте.</p>'
                        '<p>Вот пример: <i>I’d like to become an astronaut. I like space '
                        'and stars. I can jump and run well. I’ve got good health.</i></p>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h7.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Найди слова:</b></p>')

h7.add('exact_input', {'title': 'Собери слово из букв', 'items': [
    {'prompt': f'{scramble(w, "h7" + w)}', 'accept': accept(w), 'audio_tts': w}
    for w in REV]},
    'Wordwall «Найди слова» — СОСТАВ МОЙ, содержимого игры в выгрузке нет')

h7.text('<p><b>Выбери правильный вариант:</b></p>')

h7.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
    q_single('A helicopter goes ___.', 'in the air', ['in the air', 'on water', 'on land']),
    q_single('A ship goes ___.', 'on water', ['in the air', 'on water', 'on land']),
    q_single('A lorry goes ___.', 'on land', ['in the air', 'on water', 'on land']),
    q_single('You ___ a bike.', 'ride', ['ride', 'sail', 'fly']),
    q_single('You ___ a boat.', 'sail', ['ride', 'sail', 'fly'])]},
    'Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ')

h7.text('<p><b>И ещё раз — выбери правильный вариант:</b></p>')

h7.add('quiz', {'title': 'Ещё немного практики', 'questions': [
    q_single('What ___ she doing?', 'is', ['am', 'is', 'are']),
    q_single("I'd like ___ a taxi.", 'to drive', ['to drive', 'to sail', 'to fly']),
    q_single('Are you riding a scooter? — No, ___.', "I'm not", ["I'm not", "I not", "I am"]),
    q_single('They ___ waiting for a bus.', 'are', ['am', 'is', 'are'])]},
    'второй Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ')

h7.text(simg('congrats_popper') +
        '<p>Какая потрясающая у тебя мечта! Если стараться и поставить цель, '
        'то всё получится!</p>')

# ════════════════════════════════════════════════════════════════ Test ══
t = Lesson('Unit 7 Test', 'Итоговый тест по юниту', 7, kind='test', threshold=90)

t.text('<h2>Super Minds 2 · Unit 7 Test</h2>'
       '<p>Проверим, как ты усвоил юнит. Будь внимателен — у теста высокий проходной балл.</p>')

TMASK = [('helicopter', 'h _ l i c o p t _ r'), ('ship', 's h _ p'), ('lorry', 'l _ r r y'),
         ('boat', 'b _ a t'), ('scooter', 's c _ o t _ r'), ('skateboard', 's k _ t e b o _ r d'),
         ('motorbike', 'm _ t o r b i k _'), ('taxi', 't _ x i'), ('bus', 'b _ s')]

t.add('exact_input', {'title': 'Впиши буквы', 'items': [
    {'prompt': f'{m} — напиши слово целиком ({tr})', 'accept': accept(w), 'audio_tts': w}
    for (w, m), (_, tr) in zip(TMASK, WORDS)]},
    'в выгрузке это «Заполни пропуски» по словарю юнита (9 слов)')

t.add('match', {'title': 'Соедини картинку со словом', 'pairs': [
    {'left_image': url('t_' + w.lower()), 'right': w, 'right_audio_tts': w}
    for w in ['Lorry', 'Boat', 'Motorbike', 'Helicopter', 'Scooter']]},
    'в выгрузке левая колонка пустая — картинки нарисовала методист')

t.add('gaps', {'title': 'Прочитай и заполни пропуски', 'mode': 'drag',
               'text': "1. I'd like to sail a __boat__.\n"
                       "2. I'd like to ride a __bike__.\n"
                       "3. I'd like to drive a __car__.\n"
                       "4. It is a big car — it's a __lorry__.\n"
                       "5. It is a car that drives other people — it's a __taxi__."})

t.add('quiz', {'title': 'Заполни пропуски — выбери подходящий вариант', 'questions': [
    q_single('A: Are you ___ a skateboard?', 'riding', ['riding', 'ride', 'driving'],
             image='tt_skate'),
    q_single('B: No, I ___ not.', 'am', ['am', 'is', 'are']),
    q_single('A: I ___ playing football.', 'am', ['am', 'is', 'are'], image='tt_football'),
    q_single("A: I'd like to ___ a helicopter.", 'fly', ['fly', 'ride'], image='tt_heli'),
    q_single('A: What ___ you doing?', 'are', ['are', 'is'], image='tt_bike'),
    q_single('A: What are you ___?', 'doing', ['doing', 'do']),
    q_single('B: I ___ riding a bike.', 'am', ['am', 'is']),
    q_single('B: I am ___ a bike.', 'riding', ['riding', 'ride', 'drive']),
    q_single('He ___ not flying a kite.', 'is', ['is', 'am'], image='tt_kite')]},
    'в выгрузке это пять блоков «Выбери правильный вариант» — свёл в один тест')

for words, pic in [('What/are/you/doing/now?', None),
                   ('I/am/flying/a/plane/now.', 'tt_plane'),
                   ('Are/you/reading/a/book/now?', 'tt_book'),
                   ("I'd/like/to/go/by/car.", None),
                   ('I/am/waiting/for/a/bus.', None)]:
    ws = words.split('/')
    p = {'words': ws, 'sentence': ' '.join(ws), 'audio_tts': ' '.join(ws)}
    if pic:
        p['image'] = url(pic)
    t.add('order', p, 'в выгрузке это «Составь предложение»')

READING = (
    '<h3>READING</h3>'
    '<p>My name is Leo. I love transport! My favourite transport is the helicopter — '
    'I’d like to fly it one day.</p>'
    '<p>My mum has got a red scooter. She rides it to work every morning.</p>'
    '<p>My uncle is a sailor. He sails a big ship on water. It is very, very big!</p>'
    '<p>There is a lorry near our house. It is huge, and I’d like to drive it.</p>'
    '<p>My sister has got a new skateboard. She wants to go to school by skateboard, '
    'but mum says «No!».</p>')

t.text(READING,
       'ТЕКСТ МОЙ: в выгрузке у блока READING остались только пары, самого текста нет',
       todo=('Прочитать текст для READING', 'блок «Материал» с текстом про Leo',
             'в выгрузке текста нет — написала его я, под все пять пар'))

t.add('match', {'title': 'Прочитай текст. Найди каждый вид транспорта и соедини его '
                         'с правильным описанием',
                'pairs': [
                    {'left': 'helicopter', 'left_audio_tts': 'helicopter',
                     'right': 'Leo would like to fly it'},
                    {'left': 'scooter', 'left_audio_tts': 'scooter',
                     'right': 'his mum rides it to work'},
                    {'left': 'ship', 'left_audio_tts': 'ship',
                     'right': 'his uncle sails it on water'},
                    {'left': 'lorry', 'left_audio_tts': 'lorry',
                     'right': "he'd like to drive it"},
                    {'left': 'skateboard', 'left_audio_tts': 'skateboard',
                     'right': 'his sister wants to go to school by it'}]})

t.text('<h3>LISTENING</h3><p>Послушай запись и выбери правильный ответ.</p>')

t.add('video', {'title': 'Аудио к заданию LISTENING',
                'url': 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm2/u7/sm2_u7_test_b14.mp3', 'provider': 'file'},
      'аудио прислала методист')

t.add('quiz', {'title': 'Послушай запись. Выбери правильный ответ', 'questions': [
    q_single('What is Tom doing?', "He's riding a motorbike.",
             ["He's flying a plane.", "He's riding a motorbike.", "He's driving a taxi."]),
    q_single('How would Lucy like to go to Paris?', 'by plane', ['by boat', 'by bus', 'by plane']),
    q_single('Where does the helicopter go?', 'in the air',
             ['on land', 'on water', 'in the air']),
    q_single('Is Anna sailing a boat?', 'Yes, she is!',
             ['Yes, she is!', "No, she's riding a scooter.", "No, she's flying a plane."]),
    q_single('What would Ben like to drive?', 'a taxi', ['a bus', 'a lorry', 'a taxi'])]},
    'ответы отмечены в выгрузке')

t.add('speaking', {'title': 'SPEAKING TASK · Part 1 🎤',
                   'html': '<p>Посмотри на картинки и расскажи, на каком транспорте '
                           'ты бы хотел покататься.</p>'
                           + ''.join(f'<img src="{url("t_" + w)}" alt="" '
                                     f'style="height:120px;margin:4px">'
                                     for w in ['helicopter', 'ship', 'lorry', 'boat',
                                               'scooter', 'skateboard', 'motorbike',
                                               'taxi', 'bus']) +
                           '<p>For example: <i>I would like to ride a scooter. '
                           'I would like to fly a plane.</i></p>'
                           '<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>',
                   'sample_tts': 'I would like to ride a scooter. '
                                 'I would like to fly a helicopter.',
                   'needs_review': True},
      'картинки в выгрузке не было — собрал из картинок словаря юнита')

t.add('speaking', {'title': 'SPEAKING TASK · Part 2 🎤',
                   'html': '<p>Посмотри на картинку и опиши, кто чем занимается.</p>'
                           + img('street_scene') +
                           '<p>For example: <i>The boy is riding a bike. '
                           'The woman is driving a car.</i></p>',
                   'sample_tts': 'The boy is riding a bike. The woman is driving a car. '
                                 'The children are waiting for a bus.',
                   'needs_review': True},
      'картинки в выгрузке не было — нарисовала методист')

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
