# -*- coding: utf-8 -*-
"""SM2 · Unit 9 · Summer holidays — восемь уроков + отдельный юнит Final Test."""
import os
import u_lib as L
from u_lib import (Lesson, url, simg, img, accept, scramble, distract,
                   q_single, q_multi)

L.setup('Unit 9 · Summer holidays', 9, 'sm2/u9')
OUT = 'u9sql'

WORDS = [('visit cousins', 'навестить двоюродных братьев и сестёр'),
         ('go hiking', 'отправиться на долгую прогулку'),
         ('keep a scrapbook', 'вести альбом'),
         ('help in the garden', 'помогать в саду'),
         ('build a tree house', 'построить дом на дереве'),
         ('read a comic', 'читать комикс'),
         ('learn to swim', 'научиться плавать'),
         ('go camping', 'пойти в поход'),
         ('take riding lessons', 'взять уроки верховой езды')]
W = [w for w, _ in WORDS]
PIC = {'visit cousins': 'y_cousins', 'go hiking': 'y_hiking',
       'keep a scrapbook': 'y_scrapbook', 'help in the garden': 'y_garden',
       'build a tree house': 'y_treehouse', 'read a comic': 'y_comic',
       'learn to swim': 'y_swim', 'go camping': 'y_camping',
       'take riding lessons': 'y_riding'}

VIDEO = ('Ссылка на видео', 'блок «Видео/аудио» пустой',
         'в выгрузке медиафайла нет — платформа его не отдаёт')
AUDIO = ('Ссылка на аудио', 'блок «Видео/аудио» пустой',
         'в выгрузке медиафайла нет — платформа его не отдаёт')

# ═══════════════════════════════════════════════════════════ Homework 1 ══
h1 = Lesson('Homework 1', 'Летние каникулы — новые слова', 0)

h1.text(simg('hello_wave') + '<h2>Привет!</h2>'
        '<p>Сегодня мы с тобой научимся говорить о том, что можно делать на каникулах! '
        'В конце урока ты найдёшь тест — чтобы успешно его пройти, нужно набрать '
        '90 баллов. Ты справишься 💪 Вперёд!</p>'
        '<p>(Во второй обязательной части домашнего задания ты найдёшь ещё много новых '
        'полезных слов. Не забудь туда заглянуть.)</p>',
        'приветствие; в выгрузке урок разбит на части (1) и (2) — свёл в один')

h1.add('flashcards', {'cards': [
    {'text': w, 'translation': t, 'image': url(PIC[w]), 'audio_tts': w}
    for w, t in WORDS]},
    'механика «Карточки» из выгрузки; картинки нарисовала методист')

h1.add('flashcards', {'title': 'Запомни слова', 'cards': [
    {'text': w, 'image': url(PIC[w]), 'audio_tts': w} for w, _ in WORDS]},
    'механика «Запомни» из выгрузки')

h1.add('quiz', {'title': 'Найди определение', 'questions': [
    q_single(f'{w} — это…', t, sorted([t] + distract(t, [x for _, x in WORDS], 2, 'h1d' + w)))
    for w, t in WORDS]},
    'механика «Найди определение» из выгрузки')

h1.add('quiz', {'title': 'Послушай и выбери', 'questions': [
    q_single('Послушай и выбери, что ты услышал', w,
             sorted([w] + distract(w, W, 2, 'h1s' + w)), audio_tts=w)
    for w, _ in WORDS]},
    'механика «Послушай» из выгрузки')

h1.add('exact_input', {'title': 'Скрэмбл: собери фразу из букв', 'items': [
    {'prompt': f'{scramble(w, "h1" + w)}  ({t})', 'accept': accept(w), 'audio_tts': w}
    for w, t in WORDS]},
    'механика «Скрэмбл» из выгрузки')

h1.add('exact_input', {'title': 'Напиши по-английски', 'items': [
    {'prompt': f'Напиши по-английски: {t}', 'accept': accept(w), 'audio_tts': w}
    for w, t in WORDS]},
    'механика «Заполни пропуски» из выгрузки — заменил вводом фразы целиком')

h1.text('<h3>Дополнительная часть 🌟</h3>'
        '<p>Добро пожаловать в дополнительную часть домашнего задания!</p>',
        'начало части (2) из выгрузки')

h1.add('gaps', {'title': 'Прочитай предложение и вставь подходящее слово', 'mode': 'drag',
                'text': "1. I like to read a __comic__ on the sofa.\n"
                        "2. We __go__ hiking in the mountains every summer.\n"
                        "3. I want to __learn__ to swim in the pool.\n"
                        "4. My brother wants to build a __tree__ house.\n"
                        "5. We go __camping__ in a tent near the forest.\n"
                        "6. She takes __riding__ lessons every Saturday.\n"
                        "7. I help in the __garden__ and water the flowers.\n"
                        "8. We visit our __cousins__ at the weekend.\n"
                        "9. She keeps a __scrapbook__ with photos and stickers."})

h1.add('speaking', {'title': 'Запиши голосовое сообщение! (5–6 предложений) 🎤',
                    'html': '<p>Расскажи, что ты любишь делать, а что — нет. '
                            'Используй подсказки:</p>'
                            '<p><i>I like to ___. I don’t like to ___.</i></p>'
                            '<p>Пример: <i>I like to go camping. '
                            'I don’t like to help in the garden.</i></p>',
                    'sample_tts': "I like to go camping. I like to read a comic. "
                                  "I don't like to help in the garden.",
                    'needs_review': True})

h1.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Выбери правильный вариант:</b></p>')

h1.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
    q_single('I’d like to ___ a tree house.', 'build', ['build', 'go', 'keep']),
    q_single('I’d like to ___ camping.', 'go', ['build', 'go', 'keep']),
    q_single('I’d like to ___ a scrapbook.', 'keep', ['build', 'go', 'keep']),
    q_single('I’d like to ___ riding lessons.', 'take', ['take', 'go', 'build']),
    q_single('I’d like to ___ a comic.', 'read', ['read', 'go', 'take']),
    q_single('I’d like to ___ to swim.', 'learn', ['learn', 'go', 'keep'])]},
    'Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ, содержимого игры в выгрузке нет')

h1.text('<p><b>Впиши фразы:</b></p>')

h1.add('exact_input', {'title': 'Смотри на картинку и впиши фразу', 'items': [
    {'prompt': f'{i + 1}.', 'image': url(PIC[w]), 'accept': accept(w), 'audio_tts': w}
    for i, (w, _) in enumerate(WORDS)]},
    'Wordwall «Впиши фразы» — СОСТАВ МОЙ')

h1.text(simg('well_done_medal') + '<p>Поздравляю, домашняя работа выполнена! '
        'До встречи на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 2 ══
h2 = Lesson('Homework 2', 'Can I…? Can we…? — просим разрешения', 1)

h2.text(simg('hello_highfive') + '<h2>Привет-привет, мастер английского языка 😉</h2>'
        '<p>Сегодня тебя ждёт новая домашняя работа. Ты точно с ней справишься, '
        'можешь быть уверен :) Let’s go 😃</p>')

h2.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_can'),
        'карточка «Грамматика: Can I / Can we…?» из выгрузки')

h2.text('<p>Внизу тебя ждёт видео 👇</p>'
        '<ol><li>Посмотри первую часть видео — как думаешь, с кем разговаривает Пенни?</li>'
        '<li>Посмотри вторую часть видео (с субтитрами) и повторяй фразы за персонажами.</li>'
        '</ol>')

h2.add('video', {'title': 'Видео с Пенни', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h2.add('sequence', {'title': 'Отлично! Давай вспомним, в каком порядке Пенни задавала '
                             'вопросы? Посмотри видео ещё раз и расставь вопросы '
                             'в правильном порядке! ;)',
                    'items': [
                        {'text': 'Can I build a tree house?', 'image': url('pen_tree'),
                         'audio_tts': 'Can I build a tree house?'},
                        {'text': 'Can I take riding lessons?', 'image': url('pen_ride'),
                         'audio_tts': 'Can I take riding lessons?'},
                        {'text': 'Can we go fishing?', 'image': url('pen_fish'),
                         'audio_tts': 'Can we go fishing?'}]},
       'в выгрузке это «Порядок предложений»; кадры из видео добавил к предложениям')

h2.add('match', {'title': 'А теперь давай перейдём к практике. Соедини начало и конец '
                          'предложения, чтобы получились вопросы! Удачи 😉',
                 'pairs': [
                     {'left': 'Can I help you in the…', 'right': 'garden?',
                      'right_audio_tts': 'Can I help you in the garden?'},
                     {'left': 'Can I visit my cousin at the…', 'right': 'weekend?',
                      'right_audio_tts': 'Can I visit my cousin at the weekend?'},
                     {'left': 'Can I go horse riding tomorrow…', 'right': 'afternoon?',
                      'right_audio_tts': 'Can I go horse riding tomorrow afternoon?'},
                     {'left': 'Can we have pizza for…', 'right': 'dinner?',
                      'right_audio_tts': 'Can we have pizza for dinner?'},
                     {'left': 'Can we take my football to the…', 'right': 'park?',
                      'right_audio_tts': 'Can we take my football to the park?'},
                     {'left': 'Can we go camping in the…', 'right': 'summer?',
                      'right_audio_tts': 'Can we go camping in the summer?'}]},
       'в выгрузке пары записаны целыми предложениями — разделил на начало и конец')

h2.add('gaps', {'title': 'Ты отлично справляешься! Смотри, все слова перемешались '
                         'и не могут найти свои предложения — давай поможем им? '
                         'Расставь слова в предложения по смыслу 🥳',
                'mode': 'drag',
                'text': "1. Can we __have__ a party this weekend?\n"
                        "2. Can I __build__ a tree house tomorrow afternoon?\n"
                        "3. Can I go __horse__ riding tomorrow morning?\n"
                        "4. Can we __visit__ Grandpa tomorrow morning?\n"
                        "5. __Can__ we have pizza for dinner on Friday?\n"
                        "6. Can we go __swimming__ tomorrow evening?"})

h2.text('<p>Осталось чуть-чуть! Слова в предложениях перемешались, давай расставим их '
        'в правильном порядке, чтобы получились предложения. Вперёд! 😍</p>')

for words, pic in [('Can/we/visit/our/cousins/?', 'y_cousins'),
                   ('Can/I/take/swimming/lessons/?', 'k_swim'),
                   ('Can/I/keep/a/scrapbook/?', 'y_scrapbook'),
                   ('Can/I/read/a/book/?', 'k_read')]:
    ws = words.split('/')
    h2.add('order', {'words': ws, 'sentence': ' '.join(ws), 'audio_tts': ' '.join(ws),
                     'image': url(pic)},
           'в выгрузке это «Составь предложение»')

h2.add('task', {'title': 'Уррра! У нас осталось последнее задание 🎉',
                'html': '<p>Оно дополнительное, но только самые крутые ученики с ним '
                        'справятся! Посмотри на картинку и составь три вопросительных '
                        'предложения.</p>' + img('k_dreams') +
                        '<p>Например: <i>Can we go camping?</i></p>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h2.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Расставь слова в правильном порядке:</b></p>')

for words in ['Can/I/go/camping/?', 'Can/we/build/a/tree/house/?',
              'Can/I/take/riding/lessons/?', 'Can/we/go/fishing/?']:
    ws = words.split('/')
    h2.add('order', {'words': ws, 'sentence': ' '.join(ws), 'audio_tts': ' '.join(ws)},
           'Wordwall «Unjumble · SM2 Unit 9 Can I (permission)» — СОСТАВ МОЙ')

h2.text(simg('well_done_star') + '<p>Молодец! Увидимся на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 3 ══
h3 = Lesson('Homework 3', 'Вопросительные слова и ответы на них', 2)

h3.text(simg('hello_book') + '<h2>Привет!</h2>'
        '<p>Давай повторим вопросы, которые мы изучили, и ответы на них.</p>')

h3.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>'
        + img('card_qwords') + img('card_sodo'),
        'карточки «Вопросительные слова» и «So do I!» из выгрузки')

h3.add('quiz', {'title': 'Прочитай вопрос и выбери правильный ответ', 'questions': [
    q_single('Does your brother like tennis?', 'Yes, he does.',
             ['Yes, he does.', 'Yes, he is.', 'No, he does.']),
    q_single('How old is Lucy?', 'She’s seven.',
             ['It’s eight.', 'November.', 'She’s seven.']),
    q_single('Have you got a skateboard?', 'No, I haven’t.',
             ['Yes, I am.', 'No, I haven’t.', 'Yes, I can.']),
    q_single('When do you get up?', 'At seven o’clock.',
             ['At seven o’clock.', 'Yes, I do.', 'On the sofa.']),
    q_single('Whose sock is this?', 'It’s Lily’s.',
             ['It’s purple.', 'It’s Lily’s.', 'They are Lily’s.']),
    q_single('Where is the playground?', 'Between the school and the shops.',
             ['Between the school and the shops.', 'Yes, it’s great.',
              'Behind the wardrobe.']),
    q_single('Would you like a kiwi?', 'No, thank you.',
             ['Yes, I do.', 'Yes, I can.', 'No, thank you.']),
    q_single('Are there any mangoes in the fridge?', 'Yes, there are.',
             ['Yes, there is.', 'No, there are.', 'Yes, there are.'])]},
    'в выгрузке это восемь блоков «Тест» — свёл в один; ответы отмечены в выгрузке')

h3.add('speaking', {'title': 'Представь, что ты берёшь интервью 🎤',
                    'html': '<p>Задай 5–6 вопросов на любую тему. Используй вопросы '
                            'из теста выше как пример.</p>',
                    'sample_tts': 'How old are you? Where do you live? '
                                  'Have you got a bike? What sport do you like doing?',
                    'needs_review': True})

h3.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Соедини вопрос с ответом:</b></p>')

h3.add('match', {'title': 'Соедини вопрос с ответом', 'pairs': [
    {'left': 'How many cousins have you got?', 'right': 'Four.', 'right_audio_tts': 'Four.'},
    {'left': 'Can I go camping?', 'right': 'Yes, of course you can.',
     'right_audio_tts': 'Yes, of course you can.'},
    {'left': 'Does he like camping?', 'right': 'Yes, he does.',
     'right_audio_tts': 'Yes, he does.'},
    {'left': 'Whose comic is this?', 'right': 'It’s Ben’s.',
     'right_audio_tts': 'It’s Ben’s.'},
    {'left': 'Are there any animals here?', 'right': 'Yes, there are.',
     'right_audio_tts': 'Yes, there are.'},
    {'left': 'Has she got a scrapbook?', 'right': 'No, she hasn’t.',
     'right_audio_tts': 'No, she hasn’t.'}]},
    'Wordwall «Match up · SM2 Unit 9 Homework 7 (1)» — СОСТАВ МОЙ')

h3.text('<p><b>Расставь слова в правильном порядке:</b></p>')

for words in ['How/many/cousins/have/you/got/?', 'Whose/scrapbook/is/this/?',
              'Does/your/brother/like/camping/?', 'Has/your/town/got/a/park/?']:
    ws = words.split('/')
    h3.add('order', {'words': ws, 'sentence': ' '.join(ws), 'audio_tts': ' '.join(ws)},
           'Wordwall «Unjumble · SM2 Unit 9 Grammar» — СОСТАВ МОЙ')

h3.text(simg('well_done_clap') + '<p>Отличная работа! До встречи на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 4 ══
h4 = Lesson('Homework 4', 'История «Super friends on holiday»', 3)

h4.text(simg('hello_rocket') + '<h2>Добро пожаловать в домашнее задание!</h2>'
        '<p>Сегодня мы с тобой вспомним текст, который читали на уроке, а также выполним '
        'по нему задания!</p>'
        '<p>Для начала давай прочитаем и послушаем текст ещё раз, чтобы вспомнить, чем '
        'Super friends собираются заниматься на каникулах!</p>')

h4.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_idlike'),
        'карточка «I’d like to…» из выгрузки')

h4.text('<p>Читай и слушай:</p>' + img('story_hol1') + img('story_hol2'),
        'комикс из выгрузки, кадры 1–4 и 5–6')

h4.add('video', {'title': 'Аудио к истории',
                 'url': '@@MEDIA@@sm2/u9/sm2_u9_hw4_b4.mp3', 'provider': 'file'},
       'медиафайл прислала методист')

h4.add('quiz', {'title': 'Отлично! Проверим, как внимательно ты читал?', 'questions': [
    q_single("Who is Whisper's teacher?", 'dolphin', ['shark', 'dolphin', 'fish'])]},
    'ответ отмечен в выгрузке')

h4.add('truefalse', {'title': 'Отлично! А теперь следующее задание: выбери вариант — '
                              'true (верно) или false (неверно) для каждого предложения. '
                              'Не торопись! 😁',
                     'statements': [
                         {'text': 'Thunder would like to build a tree house.',
                          'answer': True},
                         {'text': 'Whisper would like to take riding lessons.',
                          'answer': False},
                         {'text': 'Misty would like to visit her grandparents.',
                          'answer': False},
                         {'text': 'Flash would like to help in the garden.', 'answer': True},
                         {'text': 'Children are happy when they have got a picnic.',
                          'answer': True}]},
       'ответы отмечены в выгрузке')

h4.add('task', {'title': 'А теперь задание посложнее!',
                'html': '<p>Мы с тобой узнали, чем хотят заниматься ребята на каникулах. '
                        'А как насчёт тебя?</p>'
                        '<p><b>What would you like to do on summer holidays?</b></p>'
                        + img('beach_kids') +
                        '<p>Пример ответа: <i>I would like to ride a bike with my sister '
                        'and keep a scrapbook with photos.</i></p>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h4.text(simg('well_done_trophy') + '<p>Ты справился! До встречи на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 5 ══
h5 = Lesson('Homework 5', 'Проект «Мои идеальные каникулы»', 4)

h5.text(simg('hello_laptop') + '<h2>Привет!</h2>'
        '<p>Вот и новая домашняя работа. Ты большой молодец, что решил её сделать. '
        'Время пролетит незаметно. Let’s go!</p>')

h5.add('task', {'title': 'Внимательно посмотри на картинку и расшифруй летние активности '
                         'с помощью кода',
                'html': '<p>Не забудь их вписать. Я уверена, у тебя получится!</p>'
                        + img('code_sheet'),
                'needs_review': True},
       'в выгрузке это «Открытый вопрос» с картинкой-шифровкой')

h5.add('task', {'title': 'Макс и Эми подготовили проект «Мои идеальные каникулы»',
                'html': '<p>Посмотри на картинку и письменно ответь на вопросы:</p>'
                        + img('proj1') +
                        '<ol><li>Where are the boy and the girl?</li>'
                        '<li>What is the boy wearing on his head?</li>'
                        '<li>What are they building?</li></ol>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h5.add('task', {'title': 'Посмотри на картинку и письменно ответь на вопросы',
                'html': img('proj2') +
                        '<ol><li>Where are they now?</li>'
                        '<li>What has the girl got in her hand?</li></ol>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h5.add('task', {'title': 'И ещё картинка — ответь на вопросы',
                'html': img('proj3') +
                        '<ol><li>Where are they now?</li>'
                        '<li>How many sandwiches are there?</li></ol>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h5.add('speaking', {'title': 'Теперь твоя очередь рассказывать 🎤',
                    'html': '<p>Расскажи о своих идеальных каникулах. Как бы ты хотел '
                            'их провести? Куда бы хотел сходить? Чем бы хотел заняться? '
                            'Самое время помечтать.</p>'
                            + img('hol_collage') +
                            '<p>Нажми на значок микрофона и расскажи о своих идеальных '
                            'каникулах.</p>',
                    'sample_tts': "I'd like to go camping with my family. I'd like to swim "
                                  "in the lake and go fishing. I'd like to take riding "
                                  "lessons too.",
                    'needs_review': True})

h5.text(simg('well_done_smiley') + '<p>Молодец! Увидимся на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 6 ══
h6 = Lesson('Homework 6', 'Природа и забота об окружающей среде', 5)

h6.text(simg('hello_headphones') + '<h2>Привет, самый лучший ученик!</h2>'
        '<p>Готов приступать к домашнему заданию? Давай поскорее начинать :)</p>')

h6.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_env'),
        'карточка «Environment on Holiday» из выгрузки')

h6.add('match', {'title': 'Для начала соедини картинки с их названием',
                 'pairs': [
                     {'left_image': url('n_bins'), 'right': 'recycling bins',
                      'right_audio_tts': 'recycling bins'},
                     {'left_image': url('n_nature'), 'right': 'natural environment',
                      'right_audio_tts': 'natural environment'},
                     {'left_image': url('n_recycle'), 'right': 'recycle',
                      'right_audio_tts': 'recycle'},
                     {'left_image': url('n_rubbish'), 'right': 'rubbish',
                      'right_audio_tts': 'rubbish'},
                     {'left_image': url('n_path'), 'right': 'path',
                      'right_audio_tts': 'path'}]},
       'в выгрузке правая колонка пустая — картинки нарисовала методист')

ENV = ['recycle your rubbish', 'walk on the plants and flowers', 'play with the animals',
       'leave your rubbish on the ground', 'walk on the path',
       'learn about the animals in their environment']

h6.add('quiz', {'title': 'Выбери только те действия, которые помогают окружающей среде',
                'questions': [q_multi(
                    'Что помогает окружающей среде?',
                    ['recycle your rubbish', 'walk on the path',
                     'learn about the animals in their environment'], ENV)]},
       'ответы отмечены в выгрузке')

h6.add('quiz', {'title': 'Выбери только те действия, которые вредят окружающей среде',
                'questions': [q_multi(
                    'Что вредит окружающей среде?',
                    ['walk on the plants and flowers', 'play with the animals',
                     'leave your rubbish on the ground'], ENV)]},
       'ответы отмечены в выгрузке')

h6.add('task', {'title': 'Посмотри на картинку и впиши активности',
                'html': '<p>Впиши, чем можно заниматься на пляже (beach), в горах '
                        '(mountains), на озере (lake).</p>' + img('act_box') +
                        '<p>Например:</p>'
                        '<p>beach: <i>look for shells</i> · mountains: <i>go climbing</i> · '
                        'lake: <i>go fishing</i></p>'
                        '<p>(Можно использовать одну активность для нескольких групп.)</p>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос» с рамочкой активностей')

h6.text(simg('well_done_jump') + '<p>Замечательно! До встречи на уроке 🌿</p>')

# ═══════════════════════════════════════════════════════════ Homework 7 ══
h7 = Lesson('Homework 7', 'Повторяем весь юнит', 6)

h7.text(simg('hello_wave') + '<h2>Привет!</h2>'
        '<p>Сегодня мы повторяем всё перед тестом — лексику, грамматику и не только! '
        'Ты справишься, я уверен!</p>')

h7.add('match', {'title': 'Соедини слово с картинкой', 'pairs': [
    {'left_image': url(PIC[w]), 'right': w, 'right_audio_tts': w} for w, _ in WORDS]},
    'механика «Найди определение» из выгрузки; картинки нарисовала методист')

h7.add('gaps', {'title': 'Заполни пропуски', 'mode': 'drag',
                'text': "Can __I__ build a tree __house__?\n"
                        "Yes, of course __you__ can.\n"
                        "Can I __take__ riding lessons?\n"
                        "Yes, of __course__ you can.\n"
                        "Can __we__ go fishing?\n"
                        "__Yes__, of course we can."})

for pic in ['q_comic', 'q_cousins', 'q_treehouse']:
    h7.add('task', {'title': 'Посмотри на картинку и запиши вопросы с «Can I / Can we…?»',
                    'html': img(pic) +
                            '<p>Используй вопросы из предыдущего задания как пример.</p>',
                    'needs_review': True},
           'в выгрузке это «Открытый вопрос» с картинкой')

h7.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
    q_single('1. ___ animals live in the forest?', 'How many',
             ['How many', 'Does', 'Are']),
    q_single('2. ___ your town got a park?', 'Has', ['Has', 'Can', 'Does']),
    q_single('3. ___ your brother like camping?', 'Does', ['Does', 'Has', 'Can']),
    q_single('4. ___ scrapbook is this?', 'Whose', ['Whose', 'How many', 'Can'])]},
    'в выгрузке это «Выбери правильный вариант»')

h7.add('speaking', {'title': 'Твой друг из другой страны спрашивает про твои летние '
                             'каникулы 🎤',
                    'html': '<p>Расскажи ему! (5–6 предложений)</p>'
                            '<p>Пример: <i>I’d like to go camping! '
                            'I’d like to help in the garden!</i></p>',
                    'sample_tts': "I'd like to go camping. I'd like to help in the garden. "
                                  "I'd like to visit my cousins and read a comic.",
                    'needs_review': True})

h7.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Выбери правильный вариант:</b></p>')

h7.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
    q_single('Can I go camping? — Yes, of course you ___.', 'can', ['can', 'are', 'do']),
    q_single('___ we visit our cousins?', 'Can', ['Can', 'Does', 'Has']),
    q_single('___ many comics have you got?', 'How', ['How', 'Whose', 'What']),
    q_single('___ tree house is this?', 'Whose', ['Whose', 'How', 'Does']),
    q_single('___ your sister like hiking?', 'Does', ['Does', 'Has', 'Can'])]},
    'Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ')

h7.text('<p><b>Соедини вопрос с ответом:</b></p>')

h7.add('match', {'title': 'Соедини вопрос с ответом', 'pairs': [
    {'left': 'Can I go swimming?', 'right': 'Yes, of course you can.',
     'right_audio_tts': 'Yes, of course you can.'},
    {'left': 'How many cousins have you got?', 'right': 'I’ve got three.',
     'right_audio_tts': 'I’ve got three.'},
    {'left': 'Whose comic is this?', 'right': 'It’s mine.', 'right_audio_tts': 'It’s mine.'},
    {'left': 'Does your brother like camping?', 'right': 'No, he doesn’t.',
     'right_audio_tts': 'No, he doesn’t.'},
    {'left': 'Has your town got a park?', 'right': 'Yes, it has.',
     'right_audio_tts': 'Yes, it has.'}]},
    'Wordwall «Соедини вопрос с ответом» — СОСТАВ МОЙ')

h7.text(simg('congrats_popper') +
        '<p>Девятый юнит позади! Ты большой молодец 🎉</p><p>До встречи на уроке!</p>')

# ════════════════════════════════════════════════════════════════ Test ══
t = Lesson('Unit 9 Test', 'Итоговый тест по юниту', 7, kind='test', threshold=90)

t.text('<h2>Super Minds 2 · Unit 9 Test</h2>'
       '<p>Проверим, как ты усвоил юнит. Будь внимателен — у теста высокий проходной балл.</p>')

TMASK = [('visit cousins', 'v _ s i t  c o u s _ n s'),
         ('go hiking', 'g o  h _ k i n g'),
         ('keep a scrapbook', 'k e _ p  a  s c r a p b o _ k'),
         ('help in the garden', 'h e l _  i n  t h e  g a r d _ n'),
         ('build a tree house', 'b u _ l d  a  t r e e  h o u s _'),
         ('read a comic', 'r e _ d  a  c o m _ c'),
         ('learn to swim', 'l e a r _  t o  s w _ m'),
         ('go camping', 'g o  c a m p _ n g'),
         ('take riding lessons', 't a k _  r i d i n g  l e s s o n _')]

t.add('exact_input', {'title': 'Впиши буквы', 'items': [
    {'prompt': f'{m} — напиши фразу целиком ({tr})', 'accept': accept(w), 'audio_tts': w}
    for (w, m), (_, tr) in zip(TMASK, WORDS)]},
    'в выгрузке это «Заполни пропуски» по словарю юнита (9 фраз)')

t.add('match', {'title': 'Соедини вопрос с ответом', 'pairs': [
    {'left': 'Where are my pencils?', 'right': 'They are under the desk.',
     'right_audio_tts': 'They are under the desk.'},
    {'left': 'Would you like an apple?', 'right': 'Yes, please.',
     'right_audio_tts': 'Yes, please.'},
    {'left': 'Is there any juice in the bottle?', 'right': 'Yes, there is.',
     'right_audio_tts': 'Yes, there is.'},
    {'left': 'Can you swim?', 'right': 'Yes, I can.', 'right_audio_tts': 'Yes, I can.'},
    {'left': 'Whose t-shirt is pink?', 'right': "It's Emily's.",
     'right_audio_tts': "It's Emily's."}]})

t.add('quiz', {'title': 'Заполни пропуски — выбери подходящий вариант', 'questions': [
    q_single('Can I ___ grandma in the evening?', 'visit', ['visit', 'go'],
             image='tt_grandma'),
    q_single('A: Can I go horse ___? B: Yes, you can.', 'riding',
             ['riding', 'ride', 'running'], image='tt_riding'),
    q_single('A: Can I ___ a tree house tomorrow? B: No, you can’t.', 'build',
             ['build', 'climb', 'go'], image='tt_treehouse'),
    q_single('A: Can I ___ a bike? B: Of course!', 'ride', ['ride', 'go', 'riding'],
             image='tt_bike'),
    q_single('A: Can I ___ swimming?', 'go', ['go', 'ride', 'do'])]},
    'в выгрузке это пять блоков «Выбери правильный вариант» — свёл в один тест')

for words in ['Can/I/help/in/the/garden?', 'What/would/you/like/to/do?',
              "I'd/like/to/build/a/tree/house.", 'Would/you/like/to/read/a/comic?',
              "I'd/like/to/play/computer/games."]:
    ws = words.split('/')
    t.add('order', {'words': ws, 'sentence': ' '.join(ws), 'audio_tts': ' '.join(ws)},
          'в выгрузке это «Составь предложение»')

READING = (
    '<h3>READING</h3>'
    '<p>Hi! I’m Jake. The summer holidays start next week and I’m very excited!</p>'
    '<p>I’d like to go camping near a river with my dad. We’ve got a big green tent.</p>'
    '<p>I can build a tree house — my grandpa helps me. Our tree house is in the garden, '
    'in an old apple tree.</p>'
    '<p>I can’t swim, so I’d like to learn to swim this summer. My sister Emma can swim '
    'very well.</p>'
    '<p>Emma and I would like to keep a scrapbook with photos of our holiday.</p>'
    '<p>I’d like to take riding lessons too, but they are on Saturdays and I play football '
    'on Saturdays. Maybe next year!</p>')

t.text(READING,
       'ТЕКСТ МОЙ: в выгрузке у блока READING остались только утверждения, самого текста нет',
       todo=('Прочитать текст для READING', 'блок «Материал» с текстом про Jake',
             'в выгрузке текста нет — написала его я, под все шесть утверждений'))

t.add('truefalse', {'title': 'Прочитай текст. Прочитай предложения и выбери '
                             '«Верно» или «Неверно»',
                    'statements': [
                        {'text': 'Jake would like to go camping near a river.',
                         'answer': True},
                        {'text': "Jake can't build a tree house.", 'answer': False},
                        {'text': 'Jake would like to learn to swim.', 'answer': True},
                        {'text': "Emma is Jake's friend.", 'answer': False},
                        {'text': 'Jake and Emma would like to keep a scrapbook.',
                         'answer': True},
                        {'text': 'Jake can take riding lessons this summer.',
                         'answer': False}]},
       'ответы отмечены в выгрузке')

t.add('speaking', {'title': 'SPEAKING TASK 🎤',
                   'html': '<p>Что бы ты хотел сделать на каникулах? Спланируй каникулы '
                           'и расскажи о них (5–7 предложений).</p>'
                           '<p>For example: <i>I’d like to build a tree house.</i></p>'
                           '<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>',
                   'sample_tts': "I'd like to build a tree house. I'd like to go camping "
                                 "with my family and learn to swim.",
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
