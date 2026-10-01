# -*- coding: utf-8 -*-
"""SM2 · Unit 3 · My town — сборка всех восьми уроков."""
import os
from u3_lib import (Lesson, WORDS, WORDS6, url, surl, img, simg,
                    accept, scramble, distract, q_single)

OUT = 'u3sql'
os.makedirs(OUT, exist_ok=True)
LESSONS = []

EN = [w for w, _, _ in WORDS]
PREPS = ['in front of', 'behind', 'next to', 'between']


# ─────────────────────────────────────────────────────────── ДЗ 1
l = Lesson('Homework 1', 'Places in town — новые слова', 0)

l.text(simg('hello_wave', 200) +
       '<h2>Привет!</h2>'
       '<p>Добро пожаловать в домашнее задание! Здесь тебя ждут новые слова — места в городе.</p>'
       '<p>Когда всё сделаешь, внизу тебя ждёт дополнительная часть. Её можно выполнить по желанию, '
       'но если выполнишь — будет просто супер 💪</p>',
       'приветствие. В выгрузке была ссылка «вернись в кабинет и выбери Homework 1 (2)» — убрал, обе части в одном уроке')

l.text('<p>Вот все слова урока — рассмотри карточку, прежде чем начать.</p>' + img('card_places'),
       'карточка «Places in Town» из выгрузки')

l.add('flashcards', {'cards': [
        {'text': w, 'translation': ru, 'image': url(p), 'audio_tts': w}
        for w, ru, p in WORDS],
      'title': 'Карточки: посмотри и запомни'})

l.add('flashcards', {'cards': [
        {'text': w, 'image': url(p), 'audio_tts': w} for w, ru, p in WORDS],
      'title': 'Запомни: назови место по картинке'},
      'механика «Запомни» из выгрузки')

l.add('quiz', {'title': 'Послушай и выбери', 'questions': [
        q_single('Послушай и выбери, что ты услышал', w,
                 sorted([w] + distract(w, EN, 2, 'l1a' + w)), audio_tts=w)
        for w, _, _ in WORDS]},
      'механика «Послушай» из выгрузки')

l.add('match', {'title': 'Соедини картинку и слово', 'pairs': [
        {'left_image': url(p), 'right': w, 'right_audio_tts': w} for w, ru, p in WORDS]},
      'механика «Найди пару» из выгрузки')

l.add('exact_input', {'title': 'Скрэмбл: собери слово из букв', 'items': [
        {'prompt': f'{scramble(w, "l1" + w)}  ({ru})', 'accept': accept(w), 'audio_tts': w}
        for w, ru, p in WORDS]},
      'механика «Скрэмбл» из выгрузки')

l.add('exact_input', {'title': 'Напиши слово по-английски', 'items': [
        {'prompt': f'Напиши по-английски: {ru}', 'accept': accept(w), 'audio_tts': w}
        for w, ru, p in WORDS]},
      'механика «Заполни пропуски» из выгрузки — заменил на ввод слова целиком')

l.add('quiz', {'title': 'Проверь себя', 'questions': [
        q_single(f'Как по-английски «{ru}»?', w,
                 sorted([w] + distract(w, EN, 2, 'l1b' + w)))
        for w, ru, p in WORDS]},
      'итоговый тест словаря')

# ── дополнительная часть (бывший Homework 1 (2))
l.text('<h3>Дополнительная часть 🌟</h3>'
       '<p>Привет! Это дополнительная часть домашней работы. Здесь тебя ждут очень интересные задания.</p>'
       '<p>Её можно выполнить по желанию. Но если ты всё-таки её сделаешь, будет просто отлично 👍</p>')

l.add('task', {'title': 'Погуляй по городу 🏙',
      'image': url('town_a'),
      'html': '<p>Посмотри на город и назови вслух всё, что видишь: '
              '<i>It’s a hospital. It’s a beautiful house.</i></p>'
              '<p>Придумай этому городу название и напиши его в поле ниже.</p>',
      'needs_review': True},
      'ЗАМЕНА Embed с 3D-моделью города — картинка + то же задание')

l.add('task', {'title': 'И ещё один город 🏙',
      'image': url('town_b'),
      'html': '<p>Теперь этот город. Назови вслух всё, что видишь, и придумай ему название.</p>'
              '<p>Напиши название в поле ниже.</p>',
      'needs_review': True},
      'ЗАМЕНА второго Embed с 3D-моделью города')

l.add('speaking', {'title': 'Расскажи о своих городах 🎤',
      'html': '<p>Расскажи о том, как ты назвал эти города, и о том, что ты там видел.</p>'
              '<p>Перед этим прослушай пример.</p>',
      'sample_tts': 'My town is called Sunny City. It has got a hospital, a park and a big cinema.',
      'needs_review': True})

l.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
       'для настоящих чемпионов!</p><p><b>Выбери подходящее слово:</b></p>')

l.add('quiz', {'title': 'Выбери подходящее слово', 'questions': [
        q_single('Что на картинке?', w, sorted([w] + distract(w, EN, 2, 'l1c' + w)), image=p)
        for w, ru, p in WORDS[:6]]},
      'Wordwall «Выбери подходящее слово» — СОСТАВ МОЙ, содержимого в выгрузке нет')

l.text('<p><b>Впиши слова:</b></p>')

l.add('exact_input', {'title': 'Посмотри на картинку и впиши слово', 'items': [
        {'image': url(p), 'prompt': 'Что на картинке?', 'accept': accept(w), 'audio_tts': w}
        for w, ru, p in WORDS[6:] + WORDS[:2]]},
      'Wordwall «Впиши слова» — СОСТАВ МОЙ, содержимого в выгрузке нет')

l.text(simg('well_done_trophy', 200) +
       '<p>Вот и всё, вторая часть домашней работы выполнена. Огромное спасибо за твой труд!</p>'
       '<p>Сейчас самое время отдохнуть. Ты можешь отправиться на прогулку и узнать, какие здания есть '
       'в твоём городе. Не забудь рассказать о них своему учителю.</p><p>Увидимся на занятии!</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 2
l = Lesson('Homework 2', 'Has your town got…? — вопрос и короткий ответ', 1)

l.text(simg('hello_headphones', 200) +
       '<h2>Привет-привет!</h2>'
       '<p>Сегодня тебя ждёт новая и интересная домашняя работа. Ты огромный молодец, что решил её сделать.</p>'
       '<p>Предлагаю начать. Поехали :)</p>')

l.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_grammar1'),
       'карточка «Grammar 1 — Has your town got…?» из выгрузки')

l.text('<p>Сегодня мы начнём с видео-песни :)</p>'
       '<p>Сначала внимательно посмотри её и попробуй ответить на вопрос: '
       '<b>Has the penguin’s town got a swimming pool?</b></p>'
       '<p>А затем представь, что ты один из этих симпатичных пингвинят, включи видео ещё раз '
       'и повторяй за пингвином, который тебе понравился 🐧</p>')

l.add('video', {'title': 'Песня: Has your town got…?', 'url': ''},
      'НУЖНА ССЫЛКА НА ВИДЕО — в выгрузке медиафайла нет')

l.add('match', {'title': 'Соедини картинки с предложениями', 'pairs': [
        {'left_image': url('p_cinema'),        'right': 'Has your town got a cinema?',
         'right_audio_tts': 'Has your town got a cinema?'},
        {'left_image': surl('no_thumb_down'),  'right': "No, it hasn't.",
         'right_audio_tts': "No, it hasn't."},
        {'left_image': url('p_swimming_pool'), 'right': 'Has your town got a swimming pool?',
         'right_audio_tts': 'Has your town got a swimming pool?'},
        {'left_image': surl('yes_thumb_up'),   'right': 'Yes, it has.',
         'right_audio_tts': 'Yes, it has.'}]},
      'в выгрузке левая колонка пустая — картинки подобрал по смыслу')

l.text('<p>Следующее задание — все слова в предложениях запутались. Наши пингвины просят тебя помочь им.</p>'
       '<p>Расставь, пожалуйста, слова в правильном порядке. Не забывай: в вопросах порядок слов всегда '
       'меняется и <b>has</b> убегает вперёд :)</p>')

for words, sent, pic in [
    (['Has', 'your', 'town', 'got', 'a', 'hospital', '?'],      'Has your town got a hospital ?',      'p_hospital'),
    (['Has', 'your', 'town', 'got', 'a', 'park', '?'],          'Has your town got a park ?',          'p_park'),
    (['Has', 'your', 'town', 'got', 'a', 'train station', '?'], 'Has your town got a train station ?', 'p_train_station'),
]:
    l.add('order', {'words': words, 'sentence': sent, 'image': url(pic),
                    'audio_tts': sent.replace(' ?', '?')})

l.add('order', {'words': ['Yes', ',', 'it', 'has'], 'sentence': 'Yes , it has',
                'image': surl('yes_thumb_up'), 'audio_tts': 'Yes, it has.'})
l.add('order', {'words': ['No', ',', 'it', "hasn't"], 'sentence': "No , it hasn't",
                'image': surl('no_thumb_down'), 'audio_tts': "No, it hasn't."})

l.text('<p>Посмотри внимательно на картинку города.</p>'
       '<p>После того как изучишь эту карту, ответь на вопросы ниже 👇</p>' + img('map_town_quiz'),
       'карта города из выгрузки — по ней отвечают на квиз ниже')

YN = ['Yes, it has.', "No, it hasn't."]
l.add('quiz', {'title': 'Has this town got…?', 'questions': [
        q_single('Has this town got a cafe?',          YN[0], YN),
        q_single('Has this town got a school?',        YN[0], YN),
        q_single('Has this town got a train station?', YN[1], YN),
        q_single('Has this town got a cinema?',        YN[0], YN),
        q_single('Has this town got a swimming pool?', YN[1], YN),
    ]},
      'ответы сверены с картой: вокзала и бассейна на карте нет')

l.text('<p>Класс! Ты отлично справился с предыдущими заданиями.</p>'
       '<p>Нарисуй, пожалуйста, карту своего города и подпиши названия мест. '
       'Обязательно покажи рисунок учителю на уроке.</p>')

l.add('speaking', {'title': 'Расскажи о своём городе 🎤',
      'html': '<p>А теперь возьми свой рисунок, посмотри на него и ответь на вопросы:</p>'
              '<ol><li>Has your city got a cinema?</li>'
              '<li>Has your city got a school?</li>'
              '<li>Has your city got a hospital?</li>'
              '<li>Has your city got a train station?</li>'
              '<li>Has your city got a playground?</li>'
              '<li>Has your city got a shop?</li>'
              '<li>Has your city got a swimming pool?</li></ol>'
              '<p>Перед тем, как ответить на вопросы, прослушай запись с примером.</p>',
      'sample_tts': 'Has your city got a cinema? Yes, it has. Has your city got a swimming pool? No, it hasn’t.',
      'needs_review': True},
      'в выгрузке в вопросе 6 опечатка «Has your city FOR a shop?» — исправил на got')

l.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
       'для настоящих чемпионов!</p><p><b>Выбери правильный вариант:</b></p>')

l.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
        q_single('___ your town got a park?',          'Has',    ['Has', 'Have', 'Is']),
        q_single('Our town ___ got a big hospital.',   'has',    ['has', 'have', 'is']),
        q_single('Has your town got a cinema? — Yes, it ___.',  'has',    ['has', 'have', 'is']),
        q_single('Has your town got a zoo? — No, it ___.',      "hasn't", ["hasn't", "haven't", "isn't"]),
    ]},
      'Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ, содержимого в выгрузке нет')

l.text('<p><b>Расставь слова в правильном порядке:</b></p>')

for words, sent in [
    (['Has', 'your', 'town', 'got', 'a', 'cinema', '?'], 'Has your town got a cinema ?'),
    (['Our', 'town', 'has', 'got', 'a', 'big', 'park', '.'], 'Our town has got a big park .'),
    (['My', 'town', "hasn't", 'got', 'a', 'zoo', '.'], "My town hasn't got a zoo ."),
]:
    l.add('order', {'words': words, 'sentence': sent,
                    'audio_tts': sent.replace(' ?', '?').replace(' .', '.')},
          'Wordwall «Расставь слова в правильном порядке» — СОСТАВ МОЙ')

l.text(simg('well_done_star', 200) + '<p>Отличная работа! Увидимся на уроке 👋</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 3
l = Lesson('Homework 3', 'Prepositions of place: in front of · behind · next to · between', 2)

l.text(simg('hello_rocket', 200) +
       '<h2>Огромный привет самому классному ученику!</h2>'
       '<p>Это новая домашняя работа, а значит мы узнаем сегодня что-то полезное и сделаем много '
       'всего интересного.</p>'
       '<p>У такого старательного и потрясающего ученика как ты всё-всё получится 👍</p>',
       'в выгрузке «потрясающегося» — исправил на «потрясающего»')

l.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_grammar2'),
       'карточка «Grammar 2 — Prepositions of Place» из выгрузки')

l.text('<p>Сегодня тебя снова ждут уже знакомые тебе пингвинята :)</p>'
       '<ol><li>Посмотри видео про них.</li>'
       '<li>Включи видео ещё раз и спой песню вместе с этими пингвинами 🎤</li></ol>')

l.add('video', {'title': 'Песня про пингвинов', 'url': ''},
      'НУЖНА ССЫЛКА НА ВИДЕО — в выгрузке медиафайла нет')

l.add('quiz', {'title': 'Где рыбка? Посмотри на картинку и выбери подходящий вариант',
      'questions': [
        q_single('The fish is ___ the rock.', 'behind',      PREPS, image='fish_behind'),
        q_single('The fish is ___ the rock.', 'in front of', PREPS, image='fish_in_front_of'),
        q_single('The fish is ___ the rock.', 'next to',     PREPS, image='fish_next_to'),
        q_single('The fish is ___ the tree and the rock.', 'between', PREPS, image='fish_between'),
      ]},
      'четыре блока «Выбери правильный вариант» из выгрузки собраны в один квиз с картинками')

l.add('match', {'title': 'Соедини картинку с подходящим словом', 'pairs': [
        {'left_image': url('fish_in_front_of'), 'right': 'in front of', 'right_audio_tts': 'in front of'},
        {'left_image': url('fish_behind'),      'right': 'behind',      'right_audio_tts': 'behind'},
        {'left_image': url('fish_next_to'),     'right': 'next to',     'right_audio_tts': 'next to'},
        {'left_image': url('fish_between'),     'right': 'between',     'right_audio_tts': 'between'}]},
      'в выгрузке левая колонка пустая — подставил картинки с рыбкой и камнем из этого же урока')

l.add('speaking', {'title': 'Расскажи про рыбку 🎤',
      'html': '<p>А теперь давай расскажем нашим пингвинам про рыбку поподробнее. '
              'Составь четыре предложения, используя картинки выше.</p>'
              '<p>Перед тем как записывать аудио, прослушай пример.</p>',
      'sample_tts': 'The fish is behind the rock. The fish is in front of the rock.',
      'needs_review': True},
      'в выгрузке задание про «мячик и коробку», но картинок с мячиком в выгрузке нет — '
      'переписал под картинки с рыбкой, которые в уроке есть')

l.text('<p>Какой ты молодец! А сейчас отправимся в небольшой городок.</p>'
       '<p>Внимательно посмотри на картинку и напиши пропущенное слово '
       '(behind, in front of, next to, between).</p>' + img('map_colour'),
       'в выгрузке «behind. in front of» — поставил запятую')

l.add('gaps', {'title': 'Впиши в пропуски', 'mode': 'drag',
      'text': '1. The Coco cafe is __next to__ the hospital.\n'
              '2. The park is __in front of__ the car park.\n'
              '3. The swimming pool is __behind__ the cafe Blue.\n'
              '4. The cinema is __between__ the school and the zoo.'})

l.add('speaking', {'title': 'Составь три предложения по карте 🎤',
      'html': '<p>Теперь составь три предложения, опираясь на карту выше.</p>'
              '<p>Можешь прослушать пример перед тем, как приступить к заданию.</p>',
      'sample_tts': 'The zoo is next to the cinema. The park is in front of the car park.',
      'needs_review': True})

l.text('<p>Отлично. Ты просто чудесно потрудился. Осталось последнее задание для супер чемпионов. '
       'Твой учитель уверен, ты с ним справишься 💪</p>'
       '<p>Вставь пропущенные слова в нужные пропуски. Не забывай подглядывать на картинку, '
       'чтобы правильно выполнить упражнение.</p>' + img('map_bw'))

l.add('gaps', {'title': 'Заполни пропуски', 'mode': 'drag',
      'text': "1. The town __hasn't__ got a bus stop.\n"
              '2. The toy shop is __next to__ the cafe.\n'
              '3. The train station is __between__ the hospital and the cinema.\n'
              '4. The town __has__ got a swimming pool.\n'
              '5. The road is __behind__ the swimming pool.\n'
              "6. Has the town __got__ a playground? __No__, it hasn't."})

l.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
       'для настоящих чемпионов!</p><p><b>Выбери Верно (True) или Неверно (False):</b></p>')

l.add('truefalse', {'title': 'Верно или неверно? Смотри на цветную карту выше',
      'statements': [
        {'text': 'The Coco cafe is next to the hospital.',        'correct': True},
        {'text': 'The park is behind the car park.',              'correct': False},
        {'text': 'The swimming pool is behind the cafe Blue.',    'correct': True},
        {'text': 'The cinema is between the school and the zoo.', 'correct': True},
        {'text': 'The zoo is in front of the stadium.',           'correct': False},
      ]},
      'Wordwall True/False — СОСТАВ МОЙ, содержимого в выгрузке нет')

l.text('<p><b>Выбери правильный вариант:</b></p>')

l.add('quiz', {'title': 'Выбери правильный предлог', 'questions': [
        q_single('The ball is ___ the box.', 'in front of', PREPS, image='b_in_front_of'),
        q_single('The ball is ___ the box.', 'next to',     PREPS, image='b_next_to'),
        q_single('The ball is ___ the two boxes.', 'between', PREPS, image='b_between'),
        q_single('The dog is ___ the house.', 'behind',     PREPS, image='t_dog_behind'),
      ]},
      'Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ, содержимого в выгрузке нет')

l.text(simg('well_done_medal', 200) + '<p>Просто великолепно! Задание выполнено на ура :)</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 4
STORY = ("Thunder: Look. The train is leaving the station. Misty: But there's a tree on the track! "
         "Whisper: Run, Flash! Run and stop the train! Flash: OK. "
         "Flash: Stop! Stop the train! Driver: Wow. She's fast! "
         "Flash: It's no good. Hmm. Let's try something else. "
         "Driver: She's next to my train again. What does she want? Driver: S-T-O-P. "
         "Flash: Stop! Driver: Thanks, kids! Flash: No problem.")

l = Lesson('Homework 4', 'История The Tree on the Track', 3)

l.text(simg('hello_book', 200) +
       '<h2>Добро пожаловать в домашнюю работу!</h2>'
       '<p>Здесь тебя ждут задания по истории, которую мы обсуждали на уроке. '
       'Будет очень-очень интересно.</p>'
       '<p>В личном кабинете тебя будет ждать вторая часть домашней работы — интерактивное видео. '
       'Делать его необязательно, но если у тебя получится его выполнить, ты будешь супер крут 😀</p>')

l.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_story'),
       'карточка «Story Phrases» из выгрузки')

l.text('<p>Прежде чем мы послушаем и прочитаем текст, попробуй вспомнить — что на железной дороге '
       'написала Флэш: <b>STOP</b>, <b>THANK YOU</b> или <b>PLEASE</b>?</p>'
       '<p>Прочитай и прослушай текст, правильно ли ты угадал?</p>' + img('story_open'))

l.add('text', {'html': img('story_1') + img('story_2'), 'audio_tts': STORY},
      'кадры истории из выгрузки; озвучка всей истории — по кнопке «Озвучить пачкой»')

l.text('<p>Отлично! Мы прочитали историю и немного вспомнили о чём читали раньше 😃</p>'
       '<p>Давай прочитаем предложения ниже и выберем правильный вариант :) '
       'Можешь подглядывать в историю при необходимости.</p>')

l.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
        q_single("But there's a tree ___ the track!", 'on', ['on', 'under', 'in front of']),
        q_single("She's ___ my train again.", 'next to', ['next to', 'behind', 'in front of']),
        q_single('Run, Flash! Run and ___ the train!', 'stop', ['stop', 'walk', 'jump']),
        q_single('___, kids!', 'Thanks', ['Thanks', 'Please', 'Hold on']),
      ]},
      'ответ во втором вопросе — next to, как отмечено в выгрузке')

l.text('<p>Супер-дупер! Половина домашнего задания почти позади, осталось немножко 👇</p>'
       '<p>Соедини вопросы с ответами.</p>')

l.add('match', {'title': 'Соедини вопросы с ответами', 'pairs': [
        {'left': 'What is there on the track?',      'right': 'A big tree.',
         'left_audio_tts': 'What is there on the track?'},
        {'left': 'Who runs to stop the train?',      'right': 'Flash.',
         'left_audio_tts': 'Who runs to stop the train?'},
        {'left': 'What does the train driver think?', 'right': 'The girl is fast.',
         'left_audio_tts': 'What does the train driver think?'},
        {'left': 'What idea has Flash got?',          'right': "She writes 'Stop'.",
         'left_audio_tts': 'What idea has Flash got?'},
        {'left': 'Does the driver stop the train?',   'right': 'Yes, he does.',
         'left_audio_tts': 'Does the driver stop the train?'},
        {'left': "Who says 'Thanks'?",                'right': 'The train driver.',
         'left_audio_tts': "Who says 'Thanks'?"}]})

l.text('<p>А сейчас у меня для тебя супер задание! Расставь предложения по порядку. '
       'Вспомни, как всё происходило в истории.</p>')

l.add('sequence', {'title': 'Расставь предложения по порядку', 'items': [
        {'text': t, 'audio_tts': t} for t in [
            'The Super Friends are on a hill.',
            'They see a tree on the train track.',
            'Flash runs down the hill.',
            "Flash says 'Stop the train!'.",
            'The driver does not understand.',
            "Flash writes 'Stop'.",
            'The driver stops the train.',
            "He says 'Thanks'."]]})

l.text(simg('well_done_clap', 200) +
       '<p>Ты справился! Вторая часть домашней работы — интерактивное видео — ждёт тебя '
       'в личном кабинете. Она необязательная, но очень интересная 😀</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 5
l = Lesson('Homework 5', 'Моё любимое место — аудирование и письмо', 4)

l.text(simg('hello_highfive', 200) +
       '<h2>Привет!</h2>'
       '<p>Это новая домашняя работа. А это значит, что сегодня ты узнаешь и сделаешь много полезного 😉</p>'
       '<p>Ну что, предлагаю начинать!</p>')

l.add('match', {'title': 'Listen to the audio and match', 'pairs': [
        {'left': 'Sarah', 'right': 'the park',          'right_audio_tts': 'the park'},
        {'left': 'Oscar', 'right': 'the swimming pool', 'right_audio_tts': 'the swimming pool'},
        {'left': 'Cheryl', 'right': 'the cafe',         'right_audio_tts': 'the cafe'}]},
      'НУЖНА АУДИОЗАПИСЬ И ПРОВЕРКА ПАР. В выгрузке три одинаковых блока «Найди пару» '
      'с пустой правой колонкой и без аудио — собрал один блок, места подставил СВОИ')

l.add('text', {'html': img('grace_girl', 260) +
       '<p style="font-size:18px"><i>“I go to my favourite shop with my mum on Saturdays. '
       'I read a book there every week!”</i></p><p><b>— Grace</b></p>',
       'audio_tts': 'I go to my favourite shop with my mum on Saturdays. I read a book there every week!'},
      'в выгрузке фото реального ребёнка — заменил на рисунок в стиле программы, '
      'текст перенёс в блок, чтобы его можно было озвучить')

l.add('task', {'title': 'Read and write',
      'html': '<p>Прочитай, что говорит Grace, и закончи предложение:</p>'
              '<p><b>Grace’s favourite place is the … .</b></p>',
      'needs_review': True})

l.add('task', {'title': 'Опиши своё любимое место',
      'html': '<p>Теперь опиши своё любимое место — используй текст с картинки как пример.</p>',
      'needs_review': True})

l.text(simg('well_done_smiley', 200) +
       '<p>Ого! Вот это здорово. Как много заданий ты сделал сегодня. Ты потрудился на славу.</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 6
l = Lesson('Homework 6', 'More places in town: market · car park · monument · sports centre · museum', 5)

l.text(simg('hello_laptop', 200) +
       '<h2>Привет-привет!</h2>'
       '<p>Давай повторим всё, что мы с тобой выучили на уроке!</p>')

l.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_more_places'),
       'карточка «More Places in Town» из выгрузки')

l.add('match', {'title': 'Соедини название мест с картинками', 'pairs': [
        {'left_image': url(p), 'right': w, 'right_audio_tts': w} for w, ru, p in WORDS6]},
      'в выгрузке правая колонка пустая — подставил сгенерированные картинки')

l.add('match', {'title': 'Где ты можешь увидеть эти предметы? Соедини их с местами.', 'pairs': [
        {'left': 'a red car',          'right': 'car park',      'right_audio_tts': 'car park'},
        {'left': 'a dinosaur skeleton', 'right': 'museum',       'right_audio_tts': 'museum'},
        {'left': 'apples and carrots', 'right': 'market',        'right_audio_tts': 'market'},
        {'left': 'a football',         'right': 'sports centre', 'right_audio_tts': 'sports centre'}]},
      'в выгрузке левая колонка пустая — подставил предметы словами')

l.add('task', {'title': 'Посмотри на карту и запиши места',
      'image': url('map_grid'),
      'html': '<p>Посмотри на карту и запиши следующие места:</p>'
              '<p>2A · 4B · 3C · 1A</p>'
              '<p><i>Пример: 1C — hospital</i></p>',
      'needs_review': True},
      'ответы по карте: 2A — market, 4B — sports centre, 3C — car park, 1A — train station')

l.text(simg('well_done_jump', 200) + '<p>Отлично! До встречи на уроке 👋</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 7
l = Lesson('Homework 7', 'Повторение перед тестом', 6)

l.text(simg('hello_rocket', 200) +
       '<h2>Привет, супер-ученик!</h2>'
       '<p>Как здорово, что ты открыл домашнее задание!</p>'
       '<p>Сегодня мы повторяем всё и готовимся к тесту. Выполни задания и будешь готов на все 100%</p>')

l.add('match', {'title': 'Найди определение: соедини слово и перевод', 'pairs': [
        {'left': w, 'right': ru, 'left_audio_tts': w} for w, ru, p in WORDS]},
      'механика «Найди определение» из выгрузки')

l.text('<p>✨ Отлично! Ты знаешь столько мест! Продолжай! 💪</p>'
       '<p>Вставь: <b>has / hasn’t / Has / Yes / No</b>.</p>',
       'в выгрузке инструкция «Вставь: has / has / hasn\'t / no / yes» — пять слов на девять пропусков; '
       'переписал списком без повторов')

l.add('gaps', {'title': 'Впиши в пропуски', 'mode': 'drag',
      'text': '1. __Has__ your town got a hospital? — Yes, it __has__.\n'
              "2. __Has__ your town got a zoo? — No, it __hasn't__.\n"
              "3. My town __has__ got a swimming pool. It's amazing!\n"
              "4. __Has__ the street got a market? — __No__, it hasn't.\n"
              '5. __Has__ your town got a supermarket? — __Yes__, it has.'})

l.text('<p>Посмотри на картинку и выбери правильный предлог!</p>' + img('town_hw7'))

l.add('quiz', {'title': 'Выбери правильный предлог', 'questions': [
        q_single('The café is ___ the hospital and the cinema.', 'between', PREPS),
        q_single('The car is ___ the café.',    'in front of', PREPS),
        q_single('The park is ___ the school.', 'behind',      PREPS),
        q_single('The cafe is ___ the hospital.', 'next to',   PREPS),
      ]},
      'в выгрузке первый и четвёртый вопросы одинаковые («The café is ___ the hospital»), '
      'но отмечены разные ответы — between и next to. По картинке верно next to, '
      'поэтому в первый вопрос дописал «and the cinema», чтобы between стало верным')

l.add('speaking', {'title': 'Расскажи о своём городе Мечты 🎤',
      'html': '<p>Нажми на микрофон и расскажи о своём городе Мечты.</p>'
              '<p><i>Пример: My town is called Star City! Has my town got a cinema? Yes, it has! '
              'It’s next to the park. The hospital is behind the school. '
              'The swimming pool is between the café and the playground!</i></p>',
      'sample_tts': 'My town is called Star City! Has my town got a cinema? Yes, it has! '
                    'It is next to the park. The hospital is behind the school. '
                    'The swimming pool is between the cafe and the playground!',
      'needs_review': True})

l.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
       'для настоящих чемпионов!</p><p><b>Впиши слово:</b></p>')

l.add('exact_input', {'title': 'Посмотри на картинку и впиши слово', 'items': [
        {'image': url(p), 'prompt': 'Что на картинке?', 'accept': accept(w), 'audio_tts': w}
        for w, ru, p in WORDS6]},
      'Wordwall «Впиши слово» — СОСТАВ МОЙ, содержимого в выгрузке нет')

l.text('<p><b>Выбери правильный вариант:</b></p>')

l.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
        q_single('___ your town got a museum?',        'Has',     ['Has', 'Have', 'Is']),
        q_single('Our town ___ got a sports centre.',  'has',     ['has', 'have', 'is']),
        q_single('Has the street got a market? — Yes, it ___.',  'has',    ['has', 'have', 'is']),
        q_single('Has your town got a monument? — No, it ___.',  "hasn't", ["hasn't", "haven't", "isn't"]),
        q_single('My town ___ got a car park. We always walk.',  "hasn't", ["hasn't", 'has', 'have']),
      ]},
      'Wordwall Quiz · SM2 U3 (has got) — СОСТАВ МОЙ, содержимого в выгрузке нет')

l.text('<p><b>Перетащи картинку к подходящему предлогу:</b></p>')

l.add('match', {'title': 'Соедини картинку и предлог', 'pairs': [
        {'left_image': url('b_in_front_of'), 'right': 'in front of', 'right_audio_tts': 'in front of'},
        {'left_image': url('b_next_to'),     'right': 'next to',     'right_audio_tts': 'next to'},
        {'left_image': url('b_between'),     'right': 'between',     'right_audio_tts': 'between'},
        {'left_image': url('t_dog_behind'),  'right': 'behind',      'right_audio_tts': 'behind'}]},
      'Wordwall Group sort · SM2 U3 (prepositions of place) — СОСТАВ МОЙ, содержимого в выгрузке нет')

l.text(simg('good_luck_clover', 200) + '<p>Ты готов к тесту на все 100% 💪 Удачи!</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ТЕСТ
l = Lesson('Test', 'Super Minds 2 · Unit 3 · Test', 7, kind='test', threshold=90)

l.add('exact_input', {'title': 'Впиши буквы: напиши слово по-английски', 'items': [
        {'prompt': f'Напиши по-английски: {ru}', 'accept': accept(w), 'audio_tts': w}
        for w, ru, p in WORDS]})

l.add('match', {'title': 'Соедини слова с картинками', 'pairs': [
        {'left_image': url(p), 'right': w, 'right_audio_tts': w} for w, p in [
            ('hospital', 'p_hospital'), ('shop', 'p_shop'), ('café', 'p_cafe'),
            ('train station', 'p_train_station'), ('park', 'p_park'), ('street', 'p_street')]]},
      'в выгрузке правая колонка пустая — подставил картинки')

l.add('quiz', {'title': 'Заполни пропуски — выбери подходящий вариант', 'questions': [
        q_single('Our town ___ a swimming pool.', 'has got', ['has got', 'have got', 'got'],
                 image='p_swimming_pool'),
        q_single('Our town has got a swimming ___.', 'pool', ['pool', 'place', 'hole']),
        q_single('___ your town got a playground?', 'Has', ['Has', 'Have', 'have'],
                 image='p_playground'),
        q_single('Has your town ___ a playground?', 'got', ['got', 'gotten', 'get']),
        q_single('The toy shop is ___ the house.', 'in front of', ['in front of', 'behind', 'next to'],
                 image='t_toy_shop'),
        q_single('Our town ___ a bus stop.', 'has got', ['has got', 'have got', 'got'],
                 image='p_bus_stop'),
        q_single('The dog is ___ the house.', 'behind', ['behind', 'in front of', 'between'],
                 image='t_dog_behind'),
        q_single('The cat is ___ the house and the toy shop.', 'between',
                 ['between', 'behind', 'in front of'], image='t_cat_between'),
      ]},
      'шесть блоков «Выбери правильный вариант» из выгрузки; предложения с двумя пропусками '
      'разбиты на два вопроса — итого восемь')

for words, sent, pic in [
    (['Has', 'your', 'town', 'got', 'a cafe?'], 'Has your town got a cafe?', 'p_cafe'),
    (['The hospital', 'is', 'in', 'front', 'of', 'the train', 'station.'],
     'The hospital is in front of the train station.', 'p_hospital'),
    (['Our town', 'has', 'got', 'a', 'sweet shop.'], 'Our town has got a sweet shop.', 'p_sweet_shop'),
    (['The park', 'is', 'next', 'to', 'the school.'], 'The park is next to the school.', 'p_school'),
    (['The cinema', 'is', 'behind', 'the swimming', 'pool.'],
     'The cinema is behind the swimming pool.', 'p_cinema'),
]:
    l.add('order', {'words': words, 'sentence': sent, 'image': url(pic), 'audio_tts': sent},
          'Расставь слова в правильном порядке')

l.add('gaps', {'title': 'READING · Прочитай текст, посмотри на карту и вставь нужное слово',
      'mode': 'drag', 'image': url('map_greenville'),
      'text': "Welcome to Greenville! It's a great town. The cinema is __between__ the café and the shop. "
              'The park is __next to__ the school. The school is __behind__ the train station. '
              'The bus stop is __in front of__ the train station. The hospital is __next to__ '
              'the sports centre. Has Greenville got a swimming pool? Yes, it has! '
              'The swimming pool is __between__ the car parks.'})

l.add('match', {'title': 'LISTENING · Послушай запись. Соедини место в городе с правильным описанием.',
      'pairs': [
        {'left': 'train station', 'right': 'next to the bus stop',
         'left_audio_tts': 'train station'},
        {'left': 'playground',    'right': 'behind the hospital',
         'left_audio_tts': 'playground'},
        {'left': 'market',        'right': 'in front of the park',
         'left_audio_tts': 'market'},
        {'left': 'cinema',        'right': 'between the café and the museum',
         'left_audio_tts': 'cinema'},
        {'left': 'car park',      'right': 'next to the sports centre',
         'left_audio_tts': 'car park'}]},
      'НУЖНА АУДИОЗАПИСЬ к заданию LISTENING — в выгрузке её нет')

l.add('task', {'title': 'SPEAKING TASK · Посмотри на картинку и ответь на вопросы',
      'image': url('town_test'), 'answer_kind': 'audio',
      'html': '<ol><li>Where is the school?</li><li>Where is the café?</li>'
              '<li>Where is the hospital?</li><li>Has this town got a cinema?</li>'
              '<li>Has this town got a bus stop?</li><li>Has this town got a school?</li></ol>'
              '<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>',
      'needs_review': True})

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── запись
if __name__ == '__main__':
    for n, les in enumerate(LESSONS, 1):
        p = f'{OUT}/{n:02d}_{les.title.replace(" ", "_")}.sql'
        open(p, 'w', encoding='utf-8').write(les.sql())
        print(f'{p:34s} {len(les.blocks):2d} блоков')
