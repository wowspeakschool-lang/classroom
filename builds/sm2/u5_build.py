# -*- coding: utf-8 -*-
"""SM2 · Unit 5 · My room — сборка всех восьми уроков."""
import os
from u5_lib import (Lesson, WORDS, MATERIALS, url, surl, img, simg,
                    accept, scramble, distract, q_single, q_multi)

OUT = 'u5sql'
W = [w for w, _ in WORDS]

# ─────────────────────────────────────────────────────────── Homework 1 ──
h1 = Lesson('Homework 1', 'Моя комната — новые слова', 0)

h1.text(simg('hello_wave') + '<h2>Привет!</h2>'
        '<p>Добро пожаловать в домашнее задание! Здесь тебя ждут новые слова.</p>'
        '<p>После того, как ты всё сделаешь, тебя ждёт дополнительное задание — его можно '
        'выполнить по желанию, НО если ты выполнишь его, ты будешь просто супер учеником 💪</p>',
        'приветствие. В выгрузке урок разбит на две части (1) и (2) — свёл в один')

h1.text('<p>Вот все слова урока — рассмотри карточку, прежде чем начать.</p>' + img('card_room'),
        'карточка «Моя комната» из выгрузки')

h1.add('flashcards', {'cards': [
    {'text': w, 'translation': t, 'image': url('f_' + w), 'audio_tts': w}
    for w, t in WORDS]},
    'механика «Карточки» из выгрузки; картинки нарисовала методист')

h1.add('flashcards', {'title': 'Запомни слова', 'cards': [
    {'text': w, 'image': url('f_' + w), 'audio_tts': w} for w, _ in WORDS]},
    'механика «Запомни» из выгрузки')

h1.add('quiz', {'title': 'Послушай и выбери', 'questions': [
    q_single('Послушай и выбери, что ты услышал', w,
             sorted([w] + distract(w, W, 2, 'h1s' + w)), audio_tts=w)
    for w, _ in WORDS]},
    'механика «Послушай» из выгрузки')

h1.add('exact_input', {'title': 'Скрэмбл: собери слово из букв', 'items': [
    {'prompt': f'{scramble(w, "h1" + w)}  ({t})', 'accept': accept(w), 'audio_tts': w}
    for w, t in WORDS]},
    'механика «Скрэмбл» из выгрузки (в выгрузке 2 повторения)')

h1.add('exact_input', {'title': 'Напиши слово по-английски', 'items': [
    {'prompt': f'Напиши по-английски: {t}', 'accept': accept(w), 'audio_tts': w}
    for w, t in WORDS]},
    'механика «Заполни пропуски» из выгрузки — заменил вводом слова')

h1.add('quiz', {'title': 'Проверь себя', 'questions': [
    q_single(f'Как по-английски «{t}»?', w, sorted([w] + distract(w, W, 2, 'h1q' + w)))
    for w, t in WORDS]},
    'итоговый тест словаря')

h1.text('<h3>Дополнительная часть 🌟</h3>'
        '<p>Добро пожаловать в дополнительную часть домашнего задания, которую можно выполнить '
        'по желанию, НО если ты выполнишь её, то будешь нереально крут!</p>',
        'начало части (2) из выгрузки')

h1.add('task', {'title': 'Что есть в твоей комнате?',
                'html': img('room_boy') +
                        '<p>Для начала — напиши, какие предметы есть в твоей комнате. '
                        'Например, <i>armchair, bed</i>.</p>',
                'needs_review': True})

h1.add('speaking', {'title': 'Расскажи о своей комнате 🎤',
                    'html': '<p>Ура, это последнее задание!</p>'
                            '<p>Справа есть значок микрофона. Нажми на него и устно расскажи мне, '
                            'какого цвета предметы в твоей комнате.</p>'
                            '<p>А если ты очень любишь рисовать — можешь ещё и нарисовать картинку '
                            'комнаты, чтобы показать своему учителю на уроке.</p>',
                    'sample_tts': 'In my room there is a blue bed. There is a brown table and a '
                                  'green armchair. My rug is red and my lamp is yellow.',
                    'needs_review': True})

h1.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Соедини слово с картинкой:</b></p>')

h1.add('match', {'title': 'Соедини слово с картинкой', 'pairs': [
    {'left_image': url('f_' + w), 'right': w, 'right_audio_tts': w} for w, _ in WORDS]},
    'Wordwall «Найди пару · sm 2 unit 5 Vocabulary» — СОСТАВ МОЙ, '
    'содержимого игры в выгрузке нет')

h1.text('<p><b>Впиши слова:</b></p>')

h1.add('exact_input', {'title': 'Собери слово из букв', 'items': [
    {'prompt': f'{scramble(w, "h1w" + w)}  ({t})', 'accept': accept(w), 'audio_tts': w}
    for w, t in WORDS]},
    'Wordwall «Anagram · SM 2 unit 5 Vocabulary Anagram» — СОСТАВ МОЙ')

h1.text(simg('well_done_medal') +
        '<p>Поздравляю, вторая часть домашней работы выполнена!</p>'
        '<p>Ты очень старался и, наверное, немного подустал. Самое время отдохнуть.</p>'
        '<p>До встречи на уроке!</p>')

# ─────────────────────────────────────────────────────────── Homework 2 ──
h2 = Lesson('Homework 2', 'this / that / these / those', 1)

h2.text(simg('hello_highfive') + '<h2>Добро пожаловать в домашнее задание!</h2>'
        '<p>В этом уроке тебя ждёт интересное видео и классные упражнения!</p>'
        '<p>Ты будешь Мега Крутым учеником, когда всё выполнишь!</p>')

h2.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_this'),
        'карточка «Грамматика 1: This · That · These · Those» из выгрузки')

h2.text('<p>В этом видео Пенни побывает в комнате у своего друга. Прежде чем смотреть, '
        'как думаешь, Пенни понравилась комната?</p>'
        '<p>Теперь посмотри видео один раз, внимательно слушай, что говорит персонаж, '
        'и проверь себя — угадал ли ты?</p>'
        '<p>Затем посмотри видео снова и повторяй за персонажем.</p>')

h2.add('video', {'title': 'Комната друга Пенни', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО — в выгрузке медиафайла нет')

h2.add('gaps', {'title': 'Посмотри видео ещё раз и вставь пропущенные слова',
                'mode': 'drag', 'image': url('video_room'),
                'text': "I like your __bedroom__ and all the thing in here.\n"
                        "I like __this__ wardrobe. I like __that__ chair.\n"
                        "I like __these__ posters and __those__ lovely lamps.\n"
                        "I like it so much. I think I want to camp."},
       'текст и пропуски точно как в выгрузке')

h2.text('<p>Обрати внимание на правило, когда мы используем this / that / these / those:</p>'
        + img('rule_apples'))

h2.add('match', {'title': 'Еще раз внимательно посмотри на правило выше и соедини предложение с картинкой',
                 'pairs': [
                     {'left_image': url('ap_this'),  'right': 'I like this apple.',
                      'right_audio_tts': 'I like this apple.'},
                     {'left_image': url('ap_that'),  'right': 'I like that apple.',
                      'right_audio_tts': 'I like that apple.'},
                     {'left_image': url('ap_these'), 'right': 'I like these apples.',
                      'right_audio_tts': 'I like these apples.'},
                     {'left_image': url('ap_those'), 'right': 'I like those apples.',
                      'right_audio_tts': 'I like those apples.'}]},
       'в выгрузке правая колонка пустая — картинки вырезал из таблицы-правила выше, подписи обрезал')

h2.text('<p>Молодец!</p><p>Давай теперь потренируемся. Соедини предложения с картинками.</p>')

h2.add('hotspot', {'title': 'Соедини предложение с картинкой', 'mode': 'label',
                   'image': url('squirrels'),
                   'points': [
                       {'x': 22, 'y': 21, 'text': 'I like those rugs.'},
                       {'x': 78, 'y': 21, 'text': 'That wardrobe is nice.'},
                       {'x': 22, 'y': 80, 'text': 'This bed is fun!'},
                       {'x': 78, 'y': 80, 'text': 'I like these armchairs.'}]},
       'в выгрузке это «Диаграмма»; точки 1–4 стоят на картинках a–d, порядок подписей из выгрузки')

h2.text('<p>Ура, ты выполнил половину упражнений!</p>'
        '<p>Твоё следующее задание — расставить слова в правильном порядке, '
        'чтобы получились предложения.</p>')

for words, name in [('I like this wardrobe.',  'w_wardrobe'),
                    ('I like that chair.',     'w_chair'),
                    ('I like these posters.',  'w_posters'),
                    ('I like those lamps.',    'w_lamps')]:
    h2.add('order', {'words': words.split(' '), 'sentence': words,
                     'audio_tts': words, 'image': url(name)},
           'Составь предложение — картинка из выгрузки')

h2.text('<p>А теперь посмотри на картинку и выбери правильный вариант: '
        'this / that / these / those.</p>' + img('point_six'))

TTTT = ['this', 'that', 'these', 'those']
h2.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
    q_single('I like ___ sofa.',      'this',  TTTT),
    q_single('I like ___ table.',     'that',  TTTT),
    q_single('I like ___ chairs.',    'these', TTTT),
    q_single('I like ___ armchairs.', 'those', TTTT),
    q_single('I like ___ mirror.',    'this',  TTTT),
    q_single('I like ___ rug.',       'that',  TTTT)]},
    'ответы из выгрузки; сверил с картинкой выше — рука у предмета = this/these, '
    'рука вдали = that/those, всё сошлось')

h2.add('speaking', {'title': 'Что тебе нравится? 🎤',
                    'html': img('point_near_far') +
                            '<p>Посмотри на картинки и запиши голосом, какие предметы тебе нравятся, '
                            'а какие не нравятся. Используй this / that / these / those.</p>',
                    'sample_tts': 'I like this bed. I like these armchairs. '
                                  'I don’t like that wardrobe. I don’t like those chairs.',
                    'needs_review': True})

h2.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Выбери правильный вариант:</b></p>')

h2.add('quiz', {'title': 'This или That?', 'questions': [
    q_single('___ lamp here is mine.',        'This', ['This', 'That', 'These', 'Those']),
    q_single('___ wardrobe over there is big.', 'That', ['This', 'That', 'These', 'Those']),
    q_single('Look at ___ mirror here.',      'this', TTTT),
    q_single('Look at ___ poster over there.', 'that', TTTT)]},
    'Wordwall «Quiz · This that these those» — СОСТАВ МОЙ, содержимого игры в выгрузке нет')

h2.add('quiz', {'title': 'These или Those?', 'questions': [
    q_single('___ beds here are new.',       'These', ['This', 'That', 'These', 'Those']),
    q_single('___ rugs over there are red.', 'Those', ['This', 'That', 'These', 'Those']),
    q_single('I like ___ posters here.',     'these', TTTT),
    q_single('I like ___ lamps over there.', 'those', TTTT)]},
    'Wordwall «Quiz · This, that, these, those» — СОСТАВ МОЙ, содержимого игры в выгрузке нет')

h2.text(simg('well_done_smiley') +
        '<p>Поздравляю! Ты завершил домашнее задание, ты молодец!</p>'
        '<p>Увидимся на занятии!</p>')

# ─────────────────────────────────────────────────────────── Homework 3 ──
h3 = Lesson('Homework 3', 'Whose…? — It’s… / They’re…', 2)

h3.text(simg('hello_book') + '<h2>Добро пожаловать в домашку!</h2>'
        '<p>Впереди тебя ждут интересное видео и несколько увлекательных упражнений.</p>'
        '<p>За каждое задание ты будешь получать ⭐</p>'
        '<p>Собери максимальное количество звёздочек и стань ЧЕМПИОНОМ.</p>')

h3.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_whose'),
        'карточка «Грамматика 2: Whose…? / It’s… / They’re…» из выгрузки')

h3.text('<p>Давай начнём с видео!</p>'
        '<p>Как думаешь, в комнате Пенни все вещи лежат на своих местах? '
        'А в твоей комнате всегда порядок?</p>'
        '<p>Для начала посмотри видео один раз, внимательно слушай, что говорят персонажи.</p>'
        '<p>Затем посмотри видео ещё раз и повторяй за персонажами.</p>')

h3.add('video', {'title': 'В комнате у Пенни', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО — в выгрузке медиафайла нет')

h3.add('gaps', {'title': 'Посмотри видео ещё раз. Прочти текст и заполни пропуски. '
                         'За это задание ты получишь 1 ⭐',
                'mode': 'drag', 'image': url('video_room3'),
                'text': "__Whose__ shoes are __these__? __They are__ Penny’s shoes.\n"
                        "Whose hat is __this__? __It’s__ Penny’s hat."})

h3.add('gaps', {'title': 'Видео мы посмотрели, пришло время тренироваться. '
                         'Выбери правильный вариант для каждого пропуска. Ещё 1 ⭐',
                'mode': 'drag', 'image': url('video_room3'),
                'text': "1. __Whose__ cap __is__ this? It’s __Claire’s__.\n"
                        "2. Whose socks are __these__? __They are__ Bob’s.\n"
                        "3. Whose jeans __are these__? __They are__ Jane’s.\n"
                        "4. Whose skirt __is this__? __It’s__ Anna’s.\n"
                        "5. Whose computer __is this__? __It’s__ Ben’s."},
       'в выгрузке это «Выбери правильный вариант» — 11 пропусков, порядок ответов из выгрузки')

h3.add('gaps', {'title': 'Внимательно посмотри на картинку. С помощью линий выясни, кому '
                         'принадлежат вещи. Вставь пропущенные фразы. 2 ⭐⭐',
                'mode': 'drag', 'image': url('lines_whose'),
                'text': "1) Whose cap is this? __It’s Sam’s__.\n"
                        "2) Whose socks are these? __They’re Ben’s__.\n"
                        "3) Whose jumper is this? __It’s Anna’s__.\n"
                        "4) Whose trousers are these? __They’re Sam’s__.\n"
                        "5) Whose football boots are these? __They’re Anna’s__.\n"
                        "6) Whose bag is this? __It’s Ben’s__."},
       'в выгрузке опечатка «Whose beg is this?» — исправил на bag')

h3.text('<p>Посмотри на картинку ниже. На ней ты увидишь 2 комнаты. '
        'Какая комната тебе нравится больше?</p>'
        '<p>Под картинкой есть несколько вопросов. Письменно ответь на них.</p>'
        '<p>За это задание ты получишь 3 ⭐⭐⭐</p>')

h3.add('task', {'title': 'Внимательно посмотри на картинку и впиши ответы на вопросы',
                'image': url('two_rooms'),
                'html': '<ol><li>Whose purple socks are these?</li>'
                        '<li>Whose ball is this?</li>'
                        '<li>Whose plane is this?</li>'
                        '<li>Whose hat is this?</li>'
                        '<li>Whose black socks are these?</li>'
                        '<li>Whose white shoes are these?</li></ol>',
                'needs_review': True})

h3.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Выбери правильный вариант:</b></p>')

h3.add('quiz', {'title': 'Whose · this / that / these / those', 'questions': [
    q_single('___ cap is this?',                  'Whose', ['Whose', 'Who', 'Whom']),
    q_single('Whose socks are ___? (они рядом)',  'these', TTTT),
    q_single('___ is Ben’s bag. (вдали)',    'That',  ['This', 'That', 'These', 'Those']),
    q_single('Whose jumper is ___? (оно рядом)',  'this',  TTTT),
    q_single('Whose boots are ___? (они вдали)',  'those', TTTT),
    q_single('___ are my books. (они рядом)',     'These', ['This', 'That', 'These', 'Those'])]},
    'Wordwall «Quiz · Whose - this that these those?» — СОСТАВ МОЙ, содержимого игры в выгрузке нет')

h3.add('quiz', {'title': 'Выбери правильный ответ', 'questions': [
    q_single('Whose hat is this?',       'It’s Penny’s hat.',
             ['It’s Penny’s hat.', 'They’re Penny’s hat.', 'It’s Penny’s hats.']),
    q_single('Whose shoes are these?',   'They’re Sam’s shoes.',
             ['It’s Sam’s shoes.', 'They’re Sam’s shoes.', 'They’re Sam’s shoe.']),
    q_single('Whose cat is that?',       'It’s Anna’s cat.',
             ['It’s Anna’s cat.', 'They’re Anna’s cat.', 'It’s Anna’s cats.']),
    q_single('Whose trousers are those?', 'They’re Tom’s trousers.',
             ['It’s Tom’s trousers.', 'They’re Tom’s trousers.', 'They’re Tom’s trouser.'])]},
    'Wordwall «Quiz · SM2 unit 5 whose recognition» — СОСТАВ МОЙ, содержимого игры в выгрузке нет')

h3.text(simg('well_done_star') +
        '<p>Поздравляю! Ты завершил домашнее задание, ты молодец! '
        'За это держи ещё одну дополнительную ⭐</p>'
        '<p>До скорой встречи!</p>')

# ─────────────────────────────────────────────────────────── Homework 4 ──
h4 = Lesson('Homework 4', 'История Tidy Up!', 3)

h4.text(simg('hello_headphones') + '<h2>Привет!</h2>'
        '<p>Сегодня мы с тобой послушаем и прочитаем рассказ о наших супердрузьях!</p>'
        '<p>Ты будешь МЕГА крут, когда справишься со всеми заданиями!</p>')

h4.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_tidy'),
        'карточка «Tidy Up!» из выгрузки')

h4.text('<p>На этот раз наши друзья не смогут отправиться на поиски приключений, '
        'пока Флеш не уберёт в своей комнате.</p>'
        '<p>Но не расстраивайся. Флеш справилась со своей задачей буквально за 2 минуты. '
        'Но разве это возможно? Сколько времени ты обычно тратишь на уборку комнаты?</p>'
        '<p>Послушай аудио и узнай, как ей это удалось.</p>' + img('mess_room'))

h4.add('video', {'title': 'Аудио: история Tidy Up!',
                 'url': 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm2/u5/sm2_u5_hw4_b4.mp3', 'provider': 'file'},
       'медиафайл прислала методист')

LISTEN = ['sweater', 'jeans', 'skirt', 'shoes', 'books', 'bike', 'balls']
h4.add('quiz', {'title': 'Прослушай историю ещё раз', 'questions': [
    q_multi('Выбери только те вещи и предметы, название которых ты услышишь в аудио.',
            ['sweater', 'jeans', 'shoes', 'books', 'balls'], LISTEN)]},
    'ответы сняты по отметкам в выгрузке и сверены с текстом истории: '
    '«jeans, sweaters, caps, shoes and socks», «bag, books, balls and dolls»')

h4.text('<p>Внимательно прочитай историю и выполни упражнение, которое ты увидишь '
        'сразу после рассказа.</p>' + img('story_1') + img('story_2'),
        'комикс из выгрузки — это и есть текст для чтения')

TRUE5 = ['Flash is tidying up the kitchen.', 'Flash likes tidying up.',
         'Flash doesn’t like tidying up.', 'Flash has got an idea.',
         'Flash can go to the park.']
h4.add('quiz', {'title': 'Внимательно прочитай текст и выполни задание', 'questions': [
    q_multi('Выбери только те утверждения, которые верны.',
            ['Flash doesn’t like tidying up.', 'Flash has got an idea.'], TRUE5)]},
    'ответы сняты по отметкам в выгрузке')

h4.add('match', {'title': 'А сейчас попробуй вспомнить, кто что говорил в истории, '
                          'и соедини персонажей с их фразами!',
                 'pairs': [
                     {'left': 'Flash', 'right': 'I don’t like tidying up.',
                      'right_audio_tts': 'I don’t like tidying up.'},
                     {'left': 'Whisper', 'right': 'Can Flash come to the park?',
                      'right_audio_tts': 'Can Flash come to the park?'},
                     {'left': 'Flash’s mum', 'right': 'I don’t believe it!',
                      'right_audio_tts': 'I don’t believe it!'}]})

h4.add('sequence', {'title': 'А это — последнее задание. Расставь предложения в правильном '
                             'порядке, как они идут в рассказе!',
                    'items': [{'text': s, 'audio_tts': s} for s in [
                        'Hello, it’s Whisper. Can Flash come to the park?',
                        'Sorry Whisper, not now. She’s tidying up her room.',
                        'I don’t like tidying up. Ah, I’ve got an idea!',
                        'First the clothes – jeans, sweaters, caps, shoes and socks!',
                        'Now the school things and the toys!',
                        'Finished! Can I go to the park now?',
                        'Just a minute. Let me check first.',
                        'Wow! The room is really tidy now.',
                        'Oh, your T-shirt. Let’s put it in the wardrobe.',
                        'I don’t believe it!',
                        'Sorry, Mum. No park for me today.']]},
       'порядок из выгрузки, сверен с комиксом')

h4.text(simg('well_done_star') + '<p>Поздравляю!</p>'
        '<p>Ты завершил домашнее задание, ты молодец! ✨</p>')

# ─────────────────────────────────────────────────────────── Homework 5 ──
h5 = Lesson('Homework 5', 'Описываем свою комнату', 4)

h5.text(simg('hello_rocket') + '<h2>Привет!</h2>'
        '<p>Тебя ждут интересные упражнения и увлекательное видео, а также ДОПОЛНИТЕЛЬНОЕ '
        'задание, которое можно выполнить ПО ЖЕЛАНИЮ. Но ты будешь СУПЕР учеником, '
        'когда справишься с ним.</p>')

h5.text('<p>Посмотри! Ниже находится видео. Это описание комнаты Лили. '
        'Там есть много разных предметов. Как думаешь, что необычное есть у Лили?</p>'
        '<p>Посмотри видео и выполни задание под ним.</p>')

h5.add('video', {'title': 'Комната Лили', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО — в выгрузке медиафайла нет')

LILY = ['There is a mirror.', 'There is a wardrobe.', 'There is a dog.',
        'There is a bed.', 'There is a parrot.', 'There is a window.']
h5.add('quiz', {'title': 'Посмотри видео ещё раз', 'questions': [
    q_multi('Выбери только те предложения, которые описывают комнату Лили.',
            ['There is a mirror.', 'There is a dog.', 'There is a bed.',
             'There is a window.'], LILY)]},
    'ответы сняты по отметкам в выгрузке')

h5.text('<p>Молодец, ты справился с первым заданием!</p>'
        '<p>Посмотри, на картинке ниже нарисована семья. Каждый из членов семьи занят '
        'своим делом. Послушай аудио и выясни, кто чем занят.</p>')

h5.add('video', {'title': 'Аудио: кто чем занят',
                 'url': 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm2/u5/sm2_u5_hw5_b6.mp3', 'provider': 'file'},
       'медиафайл прислала методист')

h5.add('hotspot', {'title': 'Послушай аудио выше и соедини имена с персонажами на фото',
                   'mode': 'label', 'image': url('family'),
                   'points': [
                       {'x': 47, 'y': 14, 'text': 'Lucy'},
                       {'x': 83, 'y': 11, 'text': 'Dan'},
                       {'x': 46, 'y': 30, 'text': 'Tom'},
                       {'x': 82, 'y': 42, 'text': 'Sam'},
                       {'x': 76, 'y': 67, 'text': 'Grace'}]},
       'в выгрузке это «Диаграмма»; координаты точек 1–5 сняты из выгрузки, '
       'порядок имён — как в списке вариантов')

h5.text('<p>А в этом задании мы с тобой научимся описывать нашу комнату. '
        'Посмотри на картинку и вставь пропущенные слова.</p>')

h5.add('gaps', {'title': 'My room', 'mode': 'drag', 'image': url('room_my'),
                'text': "In my room, there’s a big orange and white __bed__. "
                        "There is a green __rug__ on the floor.\n"
                        "There are shoes and blue __jeans__ on it. "
                        "There is a table under the __window__.\n"
                        "There is a computer on the __table__. "
                        "There is a __poster__ on the wall.\n"
                        "There’s a brown __bookcase__ next to the table. "
                        "I think there are thirteen __books__ on it.\n"
                        "I love my __bedroom__!"})

h5.add('task', {'title': 'Опиши свою комнату',
                'image': url('room_photo'),
                'html': '<p>А это — последнее задание. Письменно опиши свою комнату. '
                        'Используй предыдущее упражнение как пример.</p>'
                        '<p>Мне уже не терпится побольше узнать о твоей комнате!</p>',
                'needs_review': True})

h5.text(simg('congrats_popper') +
        '<p>Поздравляю! Ты завершил домашнее задание и порадовал своего учителя. '
        'За это лови сердечко ❤</p><p>Жду тебя на занятии!</p>')

# ─────────────────────────────────────────────────────────── Homework 6 ──
h6 = Lesson('Homework 6', 'Из чего сделаны предметы', 5)

h6.text(simg('hello_laptop') + '<h2>Привет!</h2>'
        '<p>Сегодня мы узнаем, из каких материалов сделаны предметы, которые всюду нас '
        'окружают!</p>'
        '<p>Тебя ждут интересные увлекательные упражнения и видео. А ещё тебя ждёт '
        'ДОПОЛНИТЕЛЬНОЕ задание, которое ты можешь выполнить по желанию, НО если ты его '
        'сделаешь, то будешь нереально крут!</p>')

h6.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_materials'),
        'карточка «Словарь 2: Материалы» из выгрузки')

h6.add('match', {'title': 'Для начала давай вспомним наши материалы. Соедини название с картинкой',
                 'pairs': [{'left_image': url('mat_' + m), 'right': m, 'right_audio_tts': m}
                           for m, _ in MATERIALS]},
       'в выгрузке правая колонка пустая — картинки материалов нарисовала методист')

h6.text('<p>Посмотри видео о материалах и выполни задание под ним.</p>')

h6.add('video', {'title': 'Материалы', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО — в выгрузке медиафайла нет')

h6.add('match', {'title': 'Посмотри видео ещё раз. Соедини предмет с материалом, '
                          'из которого он изготовлен',
                 'pairs': [
                     {'left': 'table',   'left_audio_tts': 'table',   'right': 'wood'},
                     {'left': 'spoon',   'left_audio_tts': 'spoon',   'right': 'metal'},
                     {'left': 'toy car', 'left_audio_tts': 'toy car', 'right': 'plastic'},
                     {'left': 'T-shirt', 'left_audio_tts': 'T-shirt', 'right': 'fabric'},
                     {'left': 'mirror',  'left_audio_tts': 'mirror',  'right': 'glass'}]})

h6.add('sort', {'title': 'Отлично! А теперь распредели предметы в соответствии с материалами, '
                         'из которых они изготовлены. Если предмет сделан из нескольких '
                         'материалов, выбери тот, которого больше',
                'groups': [
                    {'name': 'glass',   'items': [{'text': x, 'audio_tts': x}
                                                  for x in ['a cup', 'a vase', 'a jar']]},
                    {'name': 'plastic', 'items': [{'text': x, 'audio_tts': x}
                                                  for x in ['a bottle', 'a bin', 'a glass']]},
                    {'name': 'wood',    'items': [{'text': x, 'audio_tts': x}
                                                  for x in ['a pencil', 'a chair', 'a table', 'a house']]},
                    {'name': 'metal',   'items': [{'text': x, 'audio_tts': x}
                                                  for x in ['a key', 'a spoon', 'a knife']]}]},
       'в выгрузке это «Классификация»')

h6.text('<p>Давай узнаем, из чего могут быть сделаны предметы, которые можно найти в комнате.</p>')

h6.add('hotspot', {'title': 'Соедини выражение с нужным предметом на картинке',
                   'mode': 'label', 'image': url('materials_five'),
                   'points': [
                       {'x': 22, 'y': 13, 'text': 'It’s made of fabric. '
                                                  'It’s got lots of different colours.'},
                       {'x': 78, 'y': 23, 'text': 'It’s made of wood.'},
                       {'x': 44, 'y': 43, 'text': 'It’s lovely – it’s made of wood and fabric.'},
                       {'x': 21, 'y': 78, 'text': 'It’s made of glass and wood.'},
                       {'x': 67, 'y': 78, 'text': 'It’s made of metal and plastic. '
                                                  'I use it every day!'}]},
       'в выгрузке это «Диаграмма»; точки 1–5 сняты из выгрузки: '
       'ковёр · полка · кресло · зеркало · ноутбук')

h6.text('<p>Посмотри на картинку! Это предметы из моей комнаты. '
        'Прочитай их описание и заполни пропуски.</p>')

h6.add('gaps', {'title': 'Заполни пропуски', 'mode': 'drag', 'image': url('my_things'),
                'text': "My table is made of glass and __wood__.\n"
                        "My chair is made of __plastic__.\n"
                        "My __lamp__ is made of metal.\n"
                        "My mirror is made of metal and __glass__.\n"
                        "My armchair is made of wood and __fabric__."})

h6.add('task', {'title': 'Из чего сделаны предметы в твоей комнате?',
                'image': url('room_real'),
                'html': '<p>Ура! Осталось всего 1 задание.</p>'
                        '<p>Напиши, из чего сделаны предметы в твоей комнате. Составь минимум '
                        '5 предложений. Используй предыдущее упражнение как пример.</p>',
                'needs_review': True})

h6.text(simg('well_done_clap') +
        '<p>Поздравляю! Ты завершил домашнее задание, ты замечательный ученик!</p>'
        '<p>За это лови звёздочку :)</p><p>Увидимся на занятии!</p>')

# ─────────────────────────────────────────────────────────── Homework 7 ──
h7 = Lesson('Homework 7', 'Повторение юнита', 6)

h7.text(simg('good_luck_clover') + '<h2>Добро пожаловать в домашнее задание!</h2>'
        '<p>В этом уроке тебя ждут несколько упражнений на повторение всего, '
        'что мы с тобой успели выучить за эту тему.</p>'
        '<p>В конце урока есть дополнительное задание — его можно выполнить по желанию, '
        'НО если ты сделаешь его, то будешь нереально крутым учеником!</p>')

h7.text('<p>Сначала давай повторим с тобой мебель и предметы, которые можно найти в комнате.</p>'
        '<p>Прочитай подсказку и впиши слово по-английски.</p>')

CLUES = [
    ('You sleep in it.',                  'bed'),
    ('You sit on it with your family.',   'sofa'),
    ('A big comfy chair.',                'armchair'),
    ('You look at yourself in it.',       'mirror'),
    ('It is on the floor.',               'rug'),
    ('You put your clothes in it.',       'wardrobe'),
    ('You do your homework at it.',       'table'),
    ('It gives you light.',               'lamp'),
    ('A big picture on the wall.',        'poster'),
]
h7.add('exact_input', {'title': 'Кроссворд: впиши слово по подсказке', 'items': [
    {'prompt': c, 'accept': accept(w), 'audio_tts': w} for c, w in CLUES]},
    'Wordwall «Crossword · SM 2 unit 5 Vocabulary» — СОСТАВ МОЙ, '
    'содержимого игры в выгрузке нет; кроссворда у нас нет, заменил вводом слова по подсказке')

h7.text('<p>В следующем задании мы вспомним, когда мы используем this, that, these, those. '
        'Выбери правильный вариант.</p>')

h7.add('quiz', {'title': 'This / that / these / those + одежда', 'questions': [
    q_single('Look at ___ cap here.',            'this',  TTTT),
    q_single('Look at ___ shoes over there.',    'those', TTTT),
    q_single('I like ___ jeans here.',           'these', TTTT),
    q_single('Whose skirt is ___ over there?',   'that',  TTTT),
    q_single('___ socks here are mine.',         'These', ['This', 'That', 'These', 'Those']),
    q_single('___ jumper over there is Ben’s.', 'That', ['This', 'That', 'These', 'Those'])]},
    'Wordwall «Quiz · This/that/these/those + clothes Unit 5» — СОСТАВ МОЙ, '
    'содержимого игры в выгрузке нет')

h7.add('match', {'title': 'Давай теперь вспомним, как задавать вопросы: соедини вопрос и ответ',
                 'pairs': [
                     {'left': 'Whose apple is this?', 'left_audio_tts': 'Whose apple is this?',
                      'right': 'It’s Anna’s apple.',
                      'right_audio_tts': 'It’s Anna’s apple.'},
                     {'left': 'Whose shoes are these?', 'left_audio_tts': 'Whose shoes are these?',
                      'right': 'They are Lily’s shoes.',
                      'right_audio_tts': 'They are Lily’s shoes.'}]})

h7.add('exact_input', {'title': 'Отлично! Теперь твоя очередь задавать вопросы. '
                                'Я напишу ответы, а ты напиши к ним вопросы',
                       'items': [
                           {'prompt': 'It’s Anna’s dog.',
                            'accept': ['Whose dog is this?', 'whose dog is this?'],
                            'audio_tts': 'Whose dog is this?'},
                           {'prompt': 'They are Ben’s posters.',
                            'accept': ['Whose posters are these?', 'whose posters are these?'],
                            'audio_tts': 'Whose posters are these?'},
                           {'prompt': 'It’s Bob’s phone.',
                            'accept': ['Whose phone is this?', 'whose phone is this?'],
                            'audio_tts': 'Whose phone is this?'},
                           {'prompt': 'It’s Kate’s cat.',
                            'accept': ['Whose cat is this?', 'whose cat is this?'],
                            'audio_tts': 'Whose cat is this?'},
                           {'prompt': 'It’s Lily’s skirt.',
                            'accept': ['Whose skirt is this?', 'whose skirt is this?'],
                            'audio_tts': 'Whose skirt is this?'},
                           {'prompt': 'They are Tom’s trousers.',
                            'accept': ['Whose trousers are these?', 'whose trousers are these?'],
                            'audio_tts': 'Whose trousers are these?'}]},
       'в выгрузке это «Впиши в пропуски»; ответы из выгрузки')

h7.text('<p>В следующем задании мы с тобой повторим материалы, из которых изготавливаются '
        'различные предметы. Посмотри на картинки ниже и выбери правильный вариант.</p>')

h7.add('quiz', {'title': 'Посмотри на картинку и выбери правильный вариант', 'questions': [
    q_single('This bed is…', 'This bed is made of metal and fabric.',
             ['This bed is made of wood.',
              'This bed is made of metal and fabric.',
              'This bed is made of fabric and glass.'], image='m_bed'),
    q_single('This mirror is…', 'This mirror is made of wood and glass.',
             ['This mirror is made of plastic.',
              'This mirror is made of wood and glass.',
              'This mirror is made of fabric.'], image='m_mirror'),
    q_single('This armchair is…', 'This armchair is made of fabric and wood.',
             ['This armchair is made of plastic and wood.',
              'This armchair is made of glass and wood.',
              'This armchair is made of fabric and wood.'], image='m_armchair'),
    q_single('This lamp is…', 'This lamp is made of plastic and metal.',
             ['This lamp is made of plastic and metal.',
              'This lamp is made of plastic and wood.',
              'This lamp is made of glass and metal.'], image='m_lamp')]},
    'четыре блока «Тест» из выгрузки, ответы сняты по отметкам и сверены с картинками')

h7.add('gaps', {'title': 'Посмотри! Это комната моей мечты. Прочти её описание и вставь '
                         'пропущенные слова',
                'mode': 'drag', 'image': url('dream_room'),
                'text': "This is my dream __bedroom__!\n"
                        "My bed is white. It’s made of __wood__.\n"
                        "There is a __pink__ chair. It’s made of __plastic__ and metal.\n"
                        "There is a white __lamp__ on my table. It’s made of plastic.\n"
                        "I want to live in this bedroom!"})

h7.add('task', {'title': 'Комната твоей мечты',
                'image': url('dream_room2'),
                'html': '<p>Ура, ты справился со всеми обязательными заданиями!</p>'
                        '<p>А это — последнее. Оно дополнительное. НО если ты сделаешь его, '
                        'то будешь нереально крутым учеником!</p>'
                        '<p>Нарисуй комнату своей мечты и письменно опиши её, используя '
                        'предыдущее упражнение как пример.</p>',
                'needs_review': True})

h7.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Впиши слова:</b></p>')

ANAG = ['wardrobe', 'armchair', 'mirror', 'poster', 'sofa', 'rug']
h7.add('exact_input', {'title': 'Собери слово из букв', 'items': [
    {'prompt': scramble(w, 'h7' + w), 'accept': accept(w), 'audio_tts': w} for w in ANAG]},
    'Wordwall «Anagram · SM2 U5 - furniture» — СОСТАВ МОЙ, содержимого игры в выгрузке нет')

h7.text('<p><b>Выбери правильный вариант:</b></p>')

h7.add('quiz', {'title': 'This / That / These / Those', 'questions': [
    q_single('___ bed here is very big.',          'This',  ['This', 'That', 'These', 'Those']),
    q_single('___ armchairs over there are new.',  'Those', ['This', 'That', 'These', 'Those']),
    q_single('Do you like ___ mirror here?',       'this',  TTTT),
    q_single('Whose posters are ___ over there?',  'those', TTTT),
    q_single('___ rugs here are beautiful.',       'These', ['This', 'That', 'These', 'Those']),
    q_single('Look at ___ wardrobe over there.',   'that',  TTTT)]},
    'Wordwall «Quiz · SM2 Unit 5 "This That These Those"» — СОСТАВ МОЙ, '
    'содержимого игры в выгрузке нет')

h7.text('<p><b>Расставь слова в правильном порядке:</b></p>')

for s in ['Whose bag is this?', 'Whose shoes are these?',
          'It’s Anna’s cat.', 'They are Tom’s books.']:
    h7.add('order', {'words': s.split(' '), 'sentence': s, 'audio_tts': s},
           'Wordwall «Unjumble · SM2 whose sentence builder» — СОСТАВ МОЙ, '
           'содержимого игры в выгрузке нет')

h7.text(simg('well_done_trophy') +
        '<p>Молодец, ты справился со всеми заданиями, ты супер ученик!</p>'
        '<p>Увидимся на занятии!</p>')

# ────────────────────────────────────────────────────────────────  Test ──
tt = Lesson('Test', 'Super Minds 2 · Unit 5 · Test', 7, kind='test', threshold=90)

tt.add('exact_input', {'title': 'Впиши буквы: напиши слово по-английски', 'items': [
    {'prompt': f'Напиши по-английски: {t}', 'accept': accept(w), 'audio_tts': w}
    for w, t in WORDS]})

tt.add('match', {'title': 'Соедини слова с картинками', 'pairs': [
    {'left_image': url('f_' + w), 'right': w.capitalize(), 'right_audio_tts': w}
    for w in ['rug', 'wardrobe', 'armchair', 'sofa', 'mirror']]},
    'в выгрузке правая колонка пустая — картинки нарисовала методист')

tt.add('gaps', {'title': 'Посмотри на картинку и заполни пропуски',
                'mode': 'drag', 'image': url('t_bedroom'),
                'text': "1. There is a big green __bed__.\n"
                        "2. There is a blue __rug__ next to my bed.\n"
                        "3. There isn’t a __mirror__.\n"
                        "4. There is a small green __lamp__ next to my bed on the left.\n"
                        "5. There is a yellow __wardrobe__ on the right of my bed."},
       'ответы из выгрузки, сверены с картинкой')

tt.add('quiz', {'title': 'Заполни пропуски — выбери подходящий вариант', 'questions': [
    q_single('A: Do you like ___ skateboard?', 'that', ['this', 'that'], image='t_skateboard'),
    q_single('A: Do you like that skateboard? B: No, I ___.', 'don’t', ['don’t', 'not']),
    q_single('A: I like ___ football. B: Me too.', 'this', ['this', 'that'], image='t_football'),
    q_single('A: Whose cakes are ___? B: They are Mary’s.', 'these', ['this', 'these']),
    q_single('A: Whose computer is ___? B: It is Bob’s.', 'that', ['this', 'that']),
    q_single('A: I like ___ kite. It is my brother’s.', 'this', ['this', 'that'])]},
    'пять блоков «Выбери правильный вариант» из выгрузки; предложение с двумя пропусками '
    'разбито на два вопроса — итого шесть')

for s, pic in [('Do you like these yellow chairs?', None),
               ('I don’t like those pictures.', 't_pictures'),
               ('Whose blue socks are these?', 't_socks'),
               ('That is Fred’s ball.', None),
               ('Look at this black book.', None)]:
    p = {'words': s.split(' '), 'sentence': s, 'audio_tts': s}
    if pic:
        p['image'] = url(pic)
    tt.add('order', p, 'Расставь слова в правильном порядке')

tt.add('gaps', {'title': 'READING · Прочитай текст. Посмотри на картинку. '
                         'Вставь подходящее слово в каждый пропуск',
                'mode': 'drag', 'image': url('t_reading'),
                'text': "Look at my bedroom! __That__ is my bed. It’s made of __wood__.\n"
                        "__Those__ are my books on the shelf – I’ve got lots!\n"
                        "__That__ armchair over there is really comfy. I love it!\n"
                        "And __these__ are my favourite shoes.\n"
                        "Whose cars are __these__? They’re my brother’s!"},
       'текст и ответы есть в выгрузке целиком; картинки к тексту в выгрузке не было — '
       'её нарисовала методист')

tt.add('match', {'title': 'LISTENING · Послушай запись. Чья это вещь? '
                          'Соедини предмет с владельцем',
                 'pairs': [
                     {'left': 'wardrobe', 'left_audio_tts': 'wardrobe', 'right': 'Dad'},
                     {'left': 'lamp',     'left_audio_tts': 'lamp',     'right': 'Grandma'},
                     {'left': 'rug',      'left_audio_tts': 'rug',      'right': 'Mum'},
                     {'left': 'mirror',   'left_audio_tts': 'mirror',   'right': 'Lily'},
                     {'left': 'sofa',     'left_audio_tts': 'sofa',     'right': 'Ben'}]},
       'НУЖНА АУДИОЗАПИСЬ — без неё задание решается наугад')

tt.add('task', {'title': 'SPEAKING TASK',
                'image': url('t_speaking'),
                'answer_kind': 'audio',
                'html': '<p>Посмотри на картинку и опиши отличия.</p>'
                        '<p><i>For example: There are 2 pictures. This bed is orange.</i></p>'
                        '<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>',
                'needs_review': True},
       'в выгрузке картинки не было — «найди отличия» нарисовала методист')

# ───────────────────────────────────────────────────────────────────────
LESSONS = [h1, h2, h3, h4, h5, h6, h7, tt]

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for i, ls in enumerate(LESSONS, 1):
        name = ls.title.replace(' ', '_')
        with open(f'{OUT}/{i:02d}_{name}.sql', 'w') as f:
            f.write(ls.sql())
        print(f'{i:02d} {ls.title:12} блоков: {len(ls.blocks)}')
