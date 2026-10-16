# -*- coding: utf-8 -*-
"""SM2 · Unit 6 · Faces — сборка всех восьми уроков."""
import os
import u_lib as L
from u_lib import (Lesson, url, surl, img, simg, accept, scramble, distract,
                   q_single, q_multi)

L.setup('Unit 6 · Faces', 6, 'sm2/u6')
OUT = 'u6sql'

FACE = [('eyes', 'глаза'), ('face', 'лицо'), ('glasses', 'очки'), ('hair', 'волосы'),
        ('cheeks', 'щёки'), ('ears', 'уши'), ('nose', 'нос'), ('tears', 'слёзы'),
        ('chin', 'подбородок'), ('mouth', 'рот')]
FW = [w for w, _ in FACE]

FEEL = [('happy', 'счастливый'), ('sad', 'грустный'), ('tired', 'уставший'),
        ('angry', 'злой'), ('excited', 'радостный'), ('scared', 'испуганный')]
EW = [w for w, _ in FEEL]

VIDEO = ('Ссылка на видео', 'блок «Видео/аудио» пустой',
         'в выгрузке медиафайла нет — платформа его не отдаёт')
AUDIO = ('Ссылка на аудио', 'блок «Видео/аудио» пустой',
         'в выгрузке медиафайла нет — платформа его не отдаёт')

# ═══════════════════════════════════════════════════════════ Homework 1 ══
h1 = Lesson('Homework 1', 'Части лица — новые слова', 0)

h1.text(simg('hello_wave') + '<h2>Привет-привет!</h2>'
        '<p>Сегодня тебя ждёт небольшое домашнее задание. Давай вспомним слова, '
        'которые ты учил на уроке? 😉 Можешь приступать — let’s go!</p>'
        '<p>Выполни все задания, если хочешь выучить тему на все 100! После того, как '
        'завершишь их, тебя ждёт дополнительное задание — его можно выполнить по желанию, '
        'НО если ты его выполнишь, то будешь нереально крут!</p>',
        'приветствие; в выгрузке урок разбит на части (1) и (2) — свёл в один')

h1.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_face'),
        'карточка «Vocabulary — Face» из выгрузки')

h1.add('flashcards', {'cards': [
    {'text': w, 'translation': t, 'image': url('f_' + w), 'audio_tts': w}
    for w, t in FACE]},
    'механика «Карточки» из выгрузки; картинки нарисовала методист')

h1.add('flashcards', {'title': 'Запомни слова', 'cards': [
    {'text': w, 'image': url('f_' + w), 'audio_tts': w} for w, _ in FACE]},
    'механика «Запомни» из выгрузки')

h1.add('quiz', {'title': 'Найди слово', 'questions': [
    q_single(f'Как по-английски «{t}»?', w, sorted([w] + distract(w, FW, 2, 'h1f' + w)),
             image='f_' + w)
    for w, t in FACE]},
    'механика «Найди слово» из выгрузки')

h1.add('quiz', {'title': 'Послушай и выбери', 'questions': [
    q_single('Послушай и выбери, что ты услышал', w,
             sorted([w] + distract(w, FW, 2, 'h1s' + w)), audio_tts=w)
    for w, _ in FACE]},
    'механика «Послушай» из выгрузки')

h1.add('match', {'title': 'Найди пару: слово и перевод', 'pairs': [
    {'left': w, 'left_audio_tts': w, 'right': t} for w, t in FACE]},
    'механика «Найди пару» из выгрузки')

h1.add('exact_input', {'title': 'Скрэмбл: собери слово из букв', 'items': [
    {'prompt': f'{scramble(w, "h1" + w)}  ({t})', 'accept': accept(w), 'audio_tts': w}
    for w, t in FACE]},
    'механика «Скрэмбл» из выгрузки')

h1.add('exact_input', {'title': 'Напиши слово по-английски', 'items': [
    {'prompt': f'Напиши по-английски: {t}', 'accept': accept(w), 'audio_tts': w}
    for w, t in FACE]},
    'механика «Заполни пропуски» из выгрузки — заменил вводом слова целиком')

h1.text('<h3>Дополнительная часть 🌟</h3>'
        '<p>Как здорово, что ты решил заглянуть в дополнительную часть домашнего задания. '
        'Она небольшая, но полезная и интересная. У тебя всё получится! '
        'Давай скорее начинать 😃</p>',
        'начало части (2) из выгрузки')

h1.add('hotspot', {'title': 'Роберт забыл, как называются части лица по-английски 😲 '
                            'Помоги ему — соедини названия с нужными частями лица',
                   'mode': 'label', 'image': url('face_boy'),
                   'points': [
                       {'x': 50, 'y': 18, 'text': 'hair'},
                       {'x': 36, 'y': 57, 'text': 'eyes'},
                       {'x': 15, 'y': 63, 'text': 'ears'},
                       {'x': 28, 'y': 73, 'text': 'cheeks'},
                       {'x': 50, 'y': 69, 'text': 'nose'},
                       {'x': 50, 'y': 77, 'text': 'mouth'},
                       {'x': 50, 'y': 89, 'text': 'chin'},
                       {'x': 73, 'y': 80, 'text': 'face'}]},
       'в выгрузке это «Диаграмма» — 8 точек-слов на картинке мальчика',
       todo=('Проверить, куда встали точки', 'блок «Точки на картинке» с лицом мальчика',
             'координаты точек я расставил сам — в выгрузке они не сохраняются'))

MASK = [('face', 'f _ c _'), ('nose', 'n _ s _'), ('tears', 't _ a r s'),
        ('chin', 'c _ i n'), ('eyes', '_ y e s'), ('ears', 'e a _ s'),
        ('cheeks', 'c _ e e _ s')]

h1.add('exact_input', {'title': 'Ну вот, теперь Роберт потерял буквы. Впиши пропущенные '
                                'буквы в слова — Роберт без тебя не справится :)',
                       'items': [{'prompt': f'{m} — напиши слово целиком',
                                  'accept': accept(w), 'audio_tts': w}
                                 for w, m in MASK]},
       'в выгрузке это «Впиши в пропуски» с отдельными буквами — заменил вводом слова целиком')

h1.add('speaking', {'title': 'Какие части лица у тебя есть? 🎤',
                    'html': '<p>Нажми на микрофон и расскажи. '
                            'Например: <i>I have a chin. I have 2 eyes.</i></p>',
                    'sample_tts': 'I have a face. I have two eyes and two ears. '
                                  'I have a nose, a mouth and a chin.',
                    'needs_review': True})

h1.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Соедини картинку со словом:</b></p>')

h1.add('match', {'title': 'Соедини картинку со словом', 'pairs': [
    {'left_image': url('f_' + w), 'right': w, 'right_audio_tts': w} for w, _ in FACE]},
    'Wordwall «Match up · SM 2 unit 6 vocabulary» — СОСТАВ МОЙ, содержимого игры в выгрузке нет')

h1.text('<p><b>Впиши слова:</b></p>')

h1.add('exact_input', {'title': 'Собери слово из букв', 'items': [
    {'prompt': f'{scramble(w, "h1w" + w)}  ({t})', 'accept': accept(w), 'audio_tts': w}
    for w, t in FACE]},
    'Wordwall «Hangman · Face (SM2 Unit 6)» — СОСТАВ МОЙ')

h1.text(simg('well_done_medal') +
        '<p>Поздравляю, домашняя работа выполнена!</p>'
        '<p>Ты очень старался и, наверное, немного подустал. Самое время отдохнуть.</p>'
        '<p>До встречи на уроке!</p>')

# ═══════════════════════════════════════════════════════════ Homework 2 ══
h2 = Lesson('Homework 2', 'Чувства: am / is / are + прилагательное', 1)

h2.text(simg('hello_highfive') + '<h2>Привет-привет!</h2>'
        '<p>Ну что, готов к новой домашней работе? Тогда давай приступать! '
        'У тебя всё получится 😃</p>'
        '<p>В этом уроке тебя ждут упражнения на отработку новых слов. '
        'Выполни все, если хочешь выучить тему на все 100!</p>')

h2.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_feel'),
        'карточка «Grammar 1 — Am / Is / Are + Adjective» из выгрузки')

h2.add('flashcards', {'cards': [
    {'text': w, 'translation': t, 'image': url('e_' + w), 'audio_tts': w}
    for w, t in FEEL]},
    'механика «Карточки» из выгрузки; картинки нарисовала методист')

h2.add('flashcards', {'title': 'Запомни слова', 'cards': [
    {'text': w, 'image': url('e_' + w), 'audio_tts': w} for w, _ in FEEL]},
    'механика «Запомни» из выгрузки')

h2.add('quiz', {'title': 'Найди слово', 'questions': [
    q_single(f'Как по-английски «{t}»?', w, sorted([w] + distract(w, EW, 2, 'h2f' + w)),
             image='e_' + w)
    for w, t in FEEL]},
    'механика «Найди слово» из выгрузки')

h2.add('quiz', {'title': 'Найди определение', 'questions': [
    q_single(f'{w} — это…', t, sorted([t] + distract(t, [x for _, x in FEEL], 2, 'h2d' + w)))
    for w, t in FEEL]},
    'механика «Найди определение» из выгрузки')

h2.add('quiz', {'title': 'Послушай и выбери', 'questions': [
    q_single('Послушай и выбери, что ты услышал', w,
             sorted([w] + distract(w, EW, 2, 'h2s' + w)), audio_tts=w)
    for w, _ in FEEL]},
    'механика «Послушай» из выгрузки')

h2.add('match', {'title': 'Найди пару: слово и перевод', 'pairs': [
    {'left': w, 'left_audio_tts': w, 'right': t} for w, t in FEEL]},
    'механика «Найди пару» из выгрузки')

h2.add('video', {'title': 'Давай посмотрим видео! Оно маленькое, но твоя задача — '
                          'запомнить, какое настроение у ребят', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h2.text('<p>Давай проверим, насколько внимательно ты посмотрел видео 😊 '
        'Заполни пропуски нужными словами.</p>')

h2.add('gaps', {'title': 'Впиши пропущенные слова', 'mode': 'drag',
                'image': url('th_angry'),
                'text': "Girl: __Are__ you angry?\n"
                        "Boy: Yes, I __am__. __Are__ you happy?"},
       'текст и пропуски точно как в выгрузке')

h2.add('gaps', {'title': 'И ещё раз', 'mode': 'drag', 'image': url('th_scared'),
                'text': "Girl: No, I __'m not__. I __'m__ scared."},
       'в выгрузке к пропускам указаны альтернативы «am not» и «am»')

h2.text('<p>Ты отлично справился с этим заданием! Тебя ждёт ещё одно видео.</p>'
        '<p>Но задача усложняется — теперь тебя ждёт не только один мальчик и девочка, '
        'а много-много людей. Так что будь внимателен :)</p>')

h2.add('video', {'title': 'Второе видео', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h2.text('<p>Смотри на картинки и вписывай пропущенные слова. Если вдруг запутался, '
        'можешь заглянуть обратно в видео. Честно-честно никому не расскажу 🤫</p>')

for sent, pic in [("I __am__ Tom.", 'v_tom'),
                  ("She __is__ a girl.", 'v_girl'),
                  ("He __is__ a boy.", 'v_boy'),
                  ("They __are__ friends.", 'v_friends'),
                  ("You __are__ beautiful.", 'v_you'),
                  ("We __are__ friends.", 'v_we')]:
    h2.add('gaps', {'mode': 'drag', 'image': url(pic), 'text': sent},
           'кадр из видео и пропуск — как в выгрузке')

h2.add('sort', {'title': 'Ой, смотри! Все слова разбежались. Давай вернём их обратно '
                         'в нужные колонки: какие слова употребляются с am, какие с is, '
                         'а какие с are',
                'groups': [
                    {'name': 'am',  'items': [{'text': 'I', 'audio_tts': 'I'}]},
                    {'name': 'is',  'items': [{'text': x, 'audio_tts': x}
                                              for x in ['she', 'he', 'it']]},
                    {'name': 'are', 'items': [{'text': x, 'audio_tts': x}
                                              for x in ['we', 'they', 'you']]}]},
       'в выгрузке это «Классификация»')

h2.add('match', {'title': 'Теперь посмотри на картинки и соедини их с нужными фразами. '
                          'Обращай внимание и на настроение на картинке, и на людей',
                 'pairs': [
                     {'left_image': url('ph_she'),  'right': 'She is excited',
                      'right_audio_tts': 'She is excited'},
                     {'left_image': url('ph_it'),   'right': 'It is sad',
                      'right_audio_tts': 'It is sad'},
                     {'left_image': url('ph_he'),   'right': 'He is tired',
                      'right_audio_tts': 'He is tired'},
                     {'left_image': url('ph_they'), 'right': 'They are happy',
                      'right_audio_tts': 'They are happy'},
                     {'left_image': url('ph_i'),    'right': "I'm scared",
                      'right_audio_tts': "I'm scared"},
                     {'left_image': url('ph_you'),  'right': 'You are angry',
                      'right_audio_tts': 'You are angry'}]},
       'в выгрузке правая колонка «Введите слово» пустая — картинок к фразам нет, '
       'нарисованы отдельно')

h2.add('gaps', {'title': 'Ура! Последнее задание. Прочитай и вставь пропущенные слова. Вперёд!',
                'mode': 'drag',
                'text': "1. Are you angry? No, I __'m__ not. It's a busy week. I'm __tired__.\n"
                        "2. Are you __scared__? Yes, there's a big dog. Help!\n"
                        "3. __Are__ you __happy__? Yes, I am. It's the weekend!\n"
                        "4. Are you sad? No, I'm not. I'm __angry__. There isn't any cake.\n"
                        "5. Are you __excited__? Yes, I am. It's my party today!\n"
                        "6. Are you tired? No, I'm not. I'm __sad__. "
                        "I can't play football today."},
       'в выгрузке опечатка «It’s a bust week» — исправил на busy')

h2.add('speaking', {'title': 'Какое сейчас настроение у тебя и у членов твоей семьи? 🎤',
                    'html': '<p>Нажми на микрофон и расскажи.</p>'
                            '<p>Пример: <i>I am happy. My mum is scared. '
                            'My brother is angry.</i></p>',
                    'sample_tts': 'I am happy. My mum is tired. My brother is excited.',
                    'needs_review': True})

h2.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Выбери правильный вариант:</b></p>')

h2.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
    q_single('I ___ happy.', 'am', ['am', 'is', 'are']),
    q_single('She ___ sad.', 'is', ['am', 'is', 'are']),
    q_single('They ___ tired.', 'are', ['am', 'is', 'are']),
    q_single('___ you scared?', 'Are', ['Am', 'Is', 'Are']),
    q_single('He ___ excited.', 'is', ['am', 'is', 'are']),
    q_single('We ___ angry.', 'are', ['am', 'is', 'are'])]},
    'Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ, содержимого игры в выгрузке нет')

h2.text('<p><b>И ещё раз — выбери правильный вариант:</b></p>')

h2.add('quiz', {'title': 'Ответь на вопрос', 'questions': [
    q_single('Are you happy? — Yes, ___.', 'I am', ['I am', 'I is', 'I are']),
    q_single('Is he tired? — No, ___.', "he isn't", ["he isn't", "he aren't", "he amn't"]),
    q_single('Are they excited? — Yes, ___.', 'they are', ['they are', 'they is', 'they am']),
    q_single('Is she scared? — Yes, ___.', 'she is', ['she is', 'she are', 'she am'])]},
    'второй Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ')

h2.text(simg('well_done_star') +
        '<p>Какой ты молодец! Это было непростое домашнее задание, но ты справился '
        'с ним просто отлично.</p><p>Увидимся на уроке!</p>')

# ═══════════════════════════════════════════════════════════ Homework 3 ══
h3 = Lesson('Homework 3', 'Our / Their + месяцы и дни рождения', 2)

h3.text(simg('hello_book') + '<h2>Привет!</h2>'
        '<p>Как твои дела? Здорово, что ты решил сделать домашнюю работу. '
        'Сегодня нас ждут видео и задания. Давай скорее начинать :)</p>')

h3.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_birthday'),
        'карточка «Grammar 2 — Our / Their + Birthdays» из выгрузки')

h3.text('<p>Начнём с видео! Смотри и подпевай :) Заодно вспомним месяцы, '
        'которые ты проходил на уроке.</p>')

h3.add('video', {'title': 'Песня про месяцы', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

h3.add('order', {'title': 'Как здорово ты поёшь 👍 Теперь тебя ждёт очень непростая '
                          'задача — поставь месяцы по порядку',
                 'words': MONTHS, 'sentence': ' '.join(MONTHS),
                 'image': url('months_cal')},
       'в выгрузке это «Составь предложение» из 12 месяцев')

h3.add('gaps', {'title': 'Вааау! Ты справился с предыдущим заданием, значит, с этим точно '
                         'всё получится. Впиши пропущенные месяцы :)',
                'mode': 'drag',
                'text': "1. My birthday is in __March__.\n"
                        "2. Our birthdays are in __December__.\n"
                        "3. My cat is four. Its birthday is in __July__.\n"
                        "4. My dog is ten. Its birthday is in __April__.\n"
                        "5. Their birthdays are in __February__.\n"
                        "6. His birthday is in __May__."},
       'в выгрузке пропущены отдельные буквы — заменил пропуском на всё слово; '
       'там же опечатки «It birthday» и «Their birthday are» — исправил')

h3.text('<p>Тебя ждёт новое видео! Готовь микрофон (можно представить, что ручка — '
        'это микрофон :)) и будем подпевать!</p>')

h3.add('video', {'title': 'Вторая песня', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h3.text('<p>В этой домашней работе очень много сердечек :) Посмотри на картинки '
        'и расскажи, чьё же сердце, заполнив пропуски нужными словами.</p>')

for sent, pic in [("It's __my__ heart.", 'h_my'),
                  ("It's __your__ heart.", 'h_your'),
                  ("It's __his__ heart.", 'h_his'),
                  ("It's __her__ heart.", 'h_her'),
                  ("It's __our__ house.", 'h_our'),
                  ("It's __their__ house.", 'h_their')]:
    h3.add('gaps', {'mode': 'drag', 'image': url(pic), 'text': sent},
           'картинка и пропуск — как в выгрузке')

POSS = ['My', 'Your', 'His', 'Her', 'Our', 'Their']
h3.add('quiz', {'title': 'Класс! Немножко попели — теперь можно покликать. '
                         'Выбери правильный вариант ответа',
                'questions': [
    q_single("It's Lucy and Ann's birthday today. ___ birthday is in June.", 'Their', POSS),
    q_single("It's Ben's party today. He's nine. ___ birthday is in August.", 'His', POSS),
    q_single('My sister is fifteen today. ___ birthday is in May.', 'Her', POSS),
    q_single("I've got a present for my dad. ___ birthday is in October.", 'His', POSS),
    q_single('We are eight today! ___ birthday is in December.', 'Our', POSS),
    q_single("I'm ten today. ___ birthday is in January.", 'My', POSS)]},
    'в выгрузке это «Выбери правильный вариант»',
    todo=('Посмотреть вопросы 3 и 4', 'блок «Тест», вопросы «My sister…» и «my dad…»',
          'в выгрузке у них отмечены ответы «She» и «Her» — поставил Her и His'))

h3.add('task', {'title': 'Отличная работа! Последнее задание',
                'html': '<p>Мальчик по имени Майк написал тебе сообщение и рассказал '
                        'о своём любимом месяце и о своём дне рождения. А ещё о своём друге. '
                        'Прочитай его и напиши похожее сообщение, только про себя 😁</p>'
                        '<blockquote><p>Hi! My name is Mike. My favourite month is June. '
                        'My birthday is in April.</p><p>I’ve got a friend. His name is Jacob. '
                        'His favourite month is September. His birthday is in February.</p>'
                        '<p>What about you and your friend?</p></blockquote>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h3.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Расставь в правильном порядке:</b></p>')

h3.add('sequence', {'title': 'Расставь месяцы по порядку',
                    'items': [{'text': m, 'audio_tts': m} for m in MONTHS]},
       'Wordwall «Rank order · Months» — СОСТАВ МОЙ')

h3.text('<p><b>Выбери правильный вариант:</b></p>')

h3.add('quiz', {'title': 'Our или Their?', 'questions': [
    q_single('We are brothers. ___ birthdays are in May.', 'Our', ['Our', 'Their']),
    q_single('Tom and Ben are twins. ___ birthdays are in June.', 'Their', ['Our', 'Their']),
    q_single('My sister and I are eight. ___ birthdays are in July.', 'Our', ['Our', 'Their']),
    q_single('Look at Lucy and Ann! ___ mum is a teacher.', 'Their', ['Our', 'Their']),
    q_single('We’ve got a dog. ___ dog is small.', 'Our', ['Our', 'Their']),
    q_single('The boys are here. ___ bags are big.', 'Their', ['Our', 'Their'])]},
    'Wordwall «Quiz · our their sm2» — СОСТАВ МОЙ')

h3.text(simg('well_done_clap') + '<p>Ты справился! Увидимся на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 4 ══
h4 = Lesson('Homework 4', 'История «Thunder’s Birthday»', 3)

h4.text(simg('hello_rocket') + '<h2>Добро пожаловать в домашнюю работу!</h2>'
        '<p>Здесь тебя ждут задания по истории, которую мы обсуждали на уроке. '
        'Будет очень-очень интересно.</p>'
        '<p>В личном кабинете тебя будет ждать вторая часть домашней работы — '
        'интерактивное видео. Делать его необязательно, но если у тебя получится '
        'его выполнить, ты будешь супер крут 😀</p>')

h4.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_story'),
        'карточка «Key phrases — Thunder’s Birthday» из выгрузки')

h4.add('quiz', {'title': 'Прежде чем мы послушаем и прочитаем текст, попробуй вспомнить — '
                         'кто из ребят выиграл медаль. Who is the winner?',
                'questions': [q_single(
                    'Who is the winner?', 'No one',
                    ['Whisper', 'Thunder', 'Misty', 'Flash', 'Everyone', 'No one'],
                    image='story_scene')]},
       'ответ «No one» — как отмечено в выгрузке')

h4.text('<p>Прочитай и прослушай текст. Правильно ли ты угадал?</p>'
        + img('story_1') + img('story_2'),
        'комикс из выгрузки, кадры 1–6 и 7–8')

h4.add('video', {'title': 'Аудио к истории',
                 'url': 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm2/u6/sm2_u6_hw4_b5.mp3', 'provider': 'file'},
       'медиафайл прислала методист')

h4.add('gaps', {'title': 'Отлично! Мы прочитали историю и немного вспомнили, о чём читали '
                         'раньше 😃 Давай прочитаем предложения ниже и выберем правильный '
                         'вариант :) Можешь подглядывать в историю при необходимости',
                'mode': 'drag',
                'text': "1. Pull, pull, pull, you can __win__ this tug of war.\n"
                        "2. __Great__. I want to be with Flash, __please__.\n"
                        "3. No __medal__ for us.\n"
                        "4. Let’s __play__ Pin the tail on the donkey.\n"
                        "5. You aren’t wearing your blindfold. That’s not __fair__!"},
       'в выгрузке это «Выбери правильный вариант»; неверные варианты — '
       'lose/fly, No./Fine., thank you/maybe, cup/winning, dance/jump, good/excellent')

h4.add('match', {'title': 'Супер-пупер! Половина домашнего задания почти позади, '
                          'осталось немножко 👇 Соедини вопросы с ответами',
                 'pairs': [
                     {'left': 'What is the first game?', 'right': 'The tug of war!',
                      'right_audio_tts': 'The tug of war!'},
                     {'left': 'Who wants to be with Flash?', 'right': 'Whisper.',
                      'right_audio_tts': 'Whisper.'},
                     {'left': 'Who plays Pin the tail on the donkey?', 'right': 'Misty.',
                      'right_audio_tts': 'Misty.'},
                     {'left': 'What is Misty wearing?', 'right': "She's wearing a blindfold.",
                      'right_audio_tts': "She's wearing a blindfold."}]})

h4.text('<p>Ну вот и всё! Первая часть домашней работы выполнена. '
        'А это значит, что ты невероятный молодец.</p>')

h4.text('<h3>Вторая часть — интерактивное видео 🌟</h3>'
        '<p>Посмотри мультфильм про день рождения Тандера и выполни задания, '
        'которые появятся прямо в видео.</p>' + img('story_party'),
        'начало части (2) из выгрузки')

h4.text(simg('well_done_trophy') + '<p>Ты справился! До встречи на уроке 👋</p>')

# ═══════════════════════════════════════════════════════════ Homework 5 ══
h5 = Lesson('Homework 5', 'Приглашение на день рождения', 4)

h5.text(simg('congrats_popper') + '<h2>🎉 Привет! Сегодня у нас вечеринка!</h2>'
        '<p>Готов? Начинаем!</p>')

h5.add('speaking', {'title': 'Запиши голосовое сообщение! 🎤',
                    'html': '<p>Расскажи о своём лучшем друге или подруге. '
                            'Используй подсказки:</p>'
                            '<p><i>My best friend is ___.<br>'
                            'He / She has got ___ hair and ___ eyes.<br>'
                            'He / She is ___ years old.<br>'
                            'He / She likes ___.</i></p>',
                    'sample_tts': 'My best friend is Anna. She has got long hair and '
                                  'brown eyes. She is eight years old. She likes music.',
                    'needs_review': True})

h5.add('gaps', {'title': 'Прочитай письма и впиши подходящие слова из рамочки',
                'mode': 'drag',
                'text': "1. Please come to my birthday party on Sunday. It starts at two "
                        "o'clock. The party is next to the lake in the __park__. "
                        "Can you bring your new __football__?\n"
                        "2. Please come to my __birthday__ party on Saturday. It's in the "
                        "village hall. You can bring your __sister__. The party starts at "
                        "three o'clock in the __afternoon__.\n"
                        "3. Please come to my birthday party on Saturday 6th __May__. "
                        "The party is in our garden, at my house — __38__ Franklin Road. "
                        "It starts at __eleven__ o'clock in the morning."},
       'слова из рамочки: park, football, birthday, sister, afternoon, May, 38, eleven')

h5.add('task', {'title': 'Напиши своё письмо-приглашение на день рождения!',
                'html': '<p>Используй пример:</p>'
                        '<blockquote><p>Dear Kate,</p>'
                        '<p>Please come to my birthday party on Saturday. It starts at '
                        '5 o’clock. The party is at the cafe. You can bring drinks.</p>'
                        '<p>See you there!</p></blockquote>',
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h5.text(simg('well_done_smiley') + '<p>Молодец! Увидимся на вечеринке 🎈</p>')

# ═══════════════════════════════════════════════════════════ Homework 6 ══
h6 = Lesson('Homework 6', 'Портреты', 5)

h6.text(simg('hello_laptop') + '<h2>Hello-hello!</h2>'
        '<p>Сегодня поговорим о разных портретах и вспомним то, что ты проходил '
        'на уроке. Let’s go!</p>')

h6.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_portrait'),
        'карточка «Vocabulary 2 — Portraits» из выгрузки')

h6.add('match', {'title': 'Давай вспомним, какие виды портретов есть? '
                          'Соедини название с картинкой!',
                 'pairs': [
                     {'left_image': url('a_collage'),  'right': 'paper collage',
                      'right_audio_tts': 'paper collage'},
                     {'left_image': url('a_drawing'),  'right': 'drawing',
                      'right_audio_tts': 'drawing'},
                     {'left_image': url('a_painting'), 'right': 'painting',
                      'right_audio_tts': 'painting'},
                     {'left_image': url('a_photo'),    'right': 'photo',
                      'right_audio_tts': 'photo'}]},
       'в выгрузке правая колонка пустая — картинки нарисовала методист')

h6.add('hotspot', {'title': 'Супер! Виды портретов вспомнили. Давай посмотрим на картинку '
                            'и соединим нужный рисунок с описанием :) Будь внимателен, '
                            'чтобы не запутаться 😀',
                   'mode': 'label', 'image': url('portraits4'),
                   'points': [
                       {'x': 25, 'y': 25,
                        'text': "I've got a self-portrait. That's a picture of myself! "
                                "It's a painting."},
                       {'x': 75, 'y': 25,
                        'text': "I'm taking a picture of an angry boy. This angry boy is me!"},
                       {'x': 25, 'y': 75,
                        'text': "I'm making a paper collage. It's of my brother and my sister."},
                       {'x': 75, 'y': 75,
                        'text': "I'm drawing with my friends! We love trees and animals."}]},
       'в выгрузке это «Диаграмма»; точки 1–4 стоят на четвертях картинки, '
       'подписи в порядке из выгрузки')

h6.add('embed', {'title': 'Начинаем самое интересное! Собери портрет из кусочков пазла :)',
                 'html': '<p>Пока будешь собирать, подумай, кто же может быть изображён '
                         'на этом портрете ❓</p>',
                 'url': ''},
       'в выгрузке это внешний пазл — ссылки нет',
       todo=('Ссылка на пазл', 'блок «Тренажёр» без ссылки',
             'в выгрузке пазл вставлен со стороннего сайта, адрес не сохранился'))

h6.add('speaking', {'title': 'Самое время описать нашего героя на портрете 🎤',
                    'html': '<p>Смотри, какой он симпатяга. Расскажи немножко про него. '
                            'Может, придумаешь, откуда он? А, возможно, с ним приключилась '
                            'какая-то смешная история?</p>'
                            '<p>Расскажи всё, что хочешь, об этом персонаже!</p>',
                    'sample_tts': 'This is a cat. He has got big green eyes and grey hair. '
                                  'He is happy today. His birthday is in March.',
                    'needs_review': True})

h6.text('<p>Посмотри видео о том, как рисовать автопортреты. Запомни, какие животные '
        'встретятся тебе в видео :)</p>')

h6.add('video', {'title': 'Как нарисовать автопортрет', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h6.add('quiz', {'title': 'Что было в видео?', 'questions': [
    q_multi('What animals do you see in the video?', ['birds', 'a pig', 'a dog'],
            ['birds', 'hippos', 'pigs', 'a pig', 'a dog', 'a rhino'])]},
    'в выгрузке отмечены три варианта: birds, a pig, a dog')

STEPS = [('draw1', 'Start with a circle.'),
         ('draw2', 'Add a chin.'),
         ('draw3', 'Draw one line across the middle.'),
         ('draw4', 'Draw eyes on the line across the middle.'),
         ('draw5', 'Draw a nose between the eyes and the chin.'),
         ('draw6', 'Draw a mouth in the middle.'),
         ('draw7', 'Add some hair!')]

h6.add('match', {'title': 'Перед тем как нарисовать свой портрет, давай повторим все-все '
                          'шаги! Соедини картинку с нужной инструкцией :)',
                 'pairs': [{'left_image': url(p), 'right': s, 'right_audio_tts': s}
                           for p, s in STEPS]},
       'в выгрузке правая колонка пустая; шаг 3 там слит с шагом 4 — разделил',
       todo=('Посмотреть подписи к шагам 3 и 4', 'блок «Найди пару» с семью картинками',
             'в выгрузке шаг 3 записан как «Draw eyes… Then draw one line…» — '
             'похоже на склейку двух шагов, разделил их'))

h6.text(simg('well_done_jump') + '<p>Ты нарисовал целый портрет! До встречи на уроке 🎨</p>')

# ═══════════════════════════════════════════════════════════ Homework 7 ══
h7 = Lesson('Homework 7', 'Повторяем весь юнит', 6)

h7.text(simg('hello_headphones') + '<h2>Привет!</h2>'
        '<p>Ну что, готов вспомнить всё, что прошёл в шестом юните? '
        'Ты наверняка всё-всё помнишь :) Давай начинать 😄</p>')

h7.add('match', {'title': 'Давай начнём с частей лица. Соедини названия с картинками :)',
                 'pairs': [{'left_image': url('f_' + w), 'right': w, 'right_audio_tts': w}
                           for w, _ in FACE]})

h7.text('<p>Как ты здорово справился с предыдущим заданием! Части лица ты помнишь, '
        'а что насчёт следующей викторины?</p>')

h7.add('video', {'title': 'Видео к викторине', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h7.text('<p>С каждым заданием у тебя получается всё лучше и лучше! Посмотри на картинки '
        'и ответь на вопросы 😀 Не забудь правильно формулировать ответы.</p>')

for sent, pic in [("Are they in the forest? __Yes, they are.__", 'q_forest'),
                  ("Is she tall? __No, she isn't.__", 'q_tall'),
                  ("Is it a rhino? __No, it isn't.__", 'q_rhino'),
                  ("Are we family? __Yes, we are.__", 'q_family')]:
    h7.add('gaps', {'mode': 'drag', 'image': url(pic), 'text': sent},
           'картинка и пропуск — как в выгрузке')

h7.add('gaps', {'title': 'Перед тем как мы посмотрим следующее видео, сделаем супер '
                         'быстрое задание — выбери правильный вариант ответа 📄',
                'mode': 'drag',
                'text': "1. Faces can be happy or __sad__.\n"
                        "2. They can have green eyes or __brown eyes__.\n"
                        "3. They can have long or __short__ hair.\n"
                        "4. They can be in photos, paper collages, paintings "
                        "or __drawings__."},
       'в выгрузке это «Выбери правильный вариант»')

h7.text('<p>Урра! Смотрим новое видео. Обязательно запоминай эмоции, которые встретятся '
        'у героев этого мультика :) Let’s go!</p>')

h7.add('video', {'title': 'Мультик про эмоции', 'url': ''},
       'НУЖНА ССЫЛКА НА ВИДЕО', todo=VIDEO)

h7.add('hotspot', {'title': 'А теперь попробуй соединить эмоции с элементами :)',
                   'mode': 'label', 'image': url('emotions5'),
                   'points': [
                       {'x': 16, 'y': 25, 'text': 'sad'},
                       {'x': 50, 'y': 25, 'text': 'happy'},
                       {'x': 84, 'y': 25, 'text': 'angry'},
                       {'x': 16, 'y': 75, 'text': 'scared'},
                       {'x': 50, 'y': 75, 'text': 'excited'}]},
       'в выгрузке это «Диаграмма»; точки 1–5 стоят на кадрах, подписи из выгрузки')

h7.add('task', {'title': 'Супер! А теперь давай подытожим',
                'html': '<p>Напиши о каждом элементе развёрнутое предложение.</p>'
                        '<p>Смотри пример: <i>The cloud is scared.</i></p>'
                        '<p>Теперь твоя очередь!</p>' + img('emotions5'),
                'needs_review': True},
       'в выгрузке это «Открытый вопрос»')

h7.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
        'для настоящих чемпионов!</p><p><b>Выбери правильный вариант:</b></p>')

h7.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
    q_single('___ she got brown hair?', 'Has', ['Has', 'Have', 'Is']),
    q_single('He ___ got big ears.', 'has', ['has', 'have', 'is']),
    q_single('Are they happy? — Yes, ___.', 'they are', ['they are', 'they is', 'they am']),
    q_single('___ birthday is in May. (Tom and Ben)', 'Their', ['Their', 'Our', 'His']),
    q_single('I ___ excited today.', 'am', ['am', 'is', 'are'])]},
    'Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ, обложка игры в выгрузке пустая')

h7.text('<p><b>Впиши слова:</b></p>')

h7.add('exact_input', {'title': 'Собери слово из букв', 'items': [
    {'prompt': f'{scramble(w, "h7" + w)}  ({t})', 'accept': accept(w), 'audio_tts': w}
    for w, t in FACE + FEEL]},
    'Wordwall «Впиши слова» — СОСТАВ МОЙ, обложка игры в выгрузке пустая')

h7.text('<p><b>Соедини слова с картинкой:</b></p>')

h7.add('match', {'title': 'Соедини слово с картинкой', 'pairs': [
    {'left_image': url('e_' + w), 'right': w, 'right_audio_tts': w} for w, _ in FEEL]},
    'Wordwall «Соедини слова с картинкой» — СОСТАВ МОЙ, обложка игры в выгрузке пустая')

h7.text(simg('congrats_popper') +
        '<p>Шестой юнит позади! Ты большой молодец 🎉</p><p>До встречи на уроке!</p>')

# ════════════════════════════════════════════════════════════════ Test ══
t = Lesson('Unit 6 Test', 'Итоговый тест по юниту', 7, kind='test', threshold=90)

t.text('<h2>Super Minds 2 · Unit 6 Test</h2>'
       '<p>Проверим, как ты усвоил юнит. Будь внимателен — у теста высокий проходной балл.</p>')

TMASK = [('eyes', 'e _ e s'), ('face', 'f a _ e'), ('glasses', 'g l _ s s _ s'),
         ('hair', 'h _ i r'), ('cheeks', 'c h _ e k s'), ('ears', 'e _ r s'),
         ('nose', 'n o _ e'), ('tears', 't e _ r s'), ('chin', 'c h _ n'),
         ('mouth', 'm o _ t h')]

t.add('exact_input', {'title': 'Впиши буквы', 'items': [
    {'prompt': f'{m} — напиши слово целиком', 'accept': accept(w), 'audio_tts': w}
    for w, m in TMASK]},
    'в выгрузке это «Заполни пропуски» по словарю юнита (10 слов)')

t.add('gaps', {'title': 'Посмотри на картинку и заполни пропуски', 'mode': 'drag',
               'image': url('monster'),
               'text': "1. He has got black __glasses__.\n"
                       "2. He has got two blue __eyes__.\n"
                       "3. He has got orange __hair__ and two purple __ears__.\n"
                       "4. There are 4 teeth in his __mouth__."})

t.add('quiz', {'title': 'Заполни пропуски — выбери подходящий вариант', 'questions': [
    q_single('She ___ got blue eyes and orange hair.', 'has', ['has', 'have'],
             image='girl_hair'),
    q_single('A: ___ you happy?', 'Are', ['Are', 'Is']),
    q_single('B: Yes, I ___.', 'am', ['am', 'is']),
    q_single('We are twins and ___ birthdays are in May.', 'our', ['our', 'their']),
    q_single('A: ___ she got brown hair?', 'Has', ['Has', 'Have']),
    q_single('A: Has she ___ brown hair?', 'got', ['got', 'get']),
    q_single("B: No, she ___.", "hasn't", ["hasn't", "haven't"]),
    q_single("Bob's birthday is ___ February.", 'in', ['in', 'on'])]},
    'в выгрузке это пять блоков «Выбери правильный вариант» — свёл в один тест')

for words in ['She/has/got/brown/hair.',
              'Has/he/got/brown/eyes?',
              'He/is/wearing/black/glasses.',
              'Are/you/tired/today?',
              'Their/birthday/is/in/May.']:
    ws = words.split('/')
    t.add('order', {'words': ws, 'sentence': ' '.join(ws), 'audio_tts': ' '.join(ws)},
          'в выгрузке это «Составь предложение»')

READING = (
    '<h3>READING</h3>'
    '<p>Today is sports day at school. Jake is excited! He has got a new T-shirt '
    'and new trainers.</p>'
    '<p>His friend Sam isn’t happy. He’s scared. He doesn’t like the tug of war — '
    'it’s too hard!</p>'
    '<p>«Don’t worry», says Jake. «The three-legged race is first. I’m not scared '
    'of it. It’s fun!»</p>'
    '<p>Lily is excited too. Her birthday is in October, but today she has got '
    'a present from her mum — a red cap.</p>'
    '<p>Mrs Brown is their teacher. She is happy. «What a lovely day!» she says. '
    '«Good luck, everyone!»</p>')

t.text(READING,
       'ТЕКСТ МОЙ: в выгрузке у блока READING остались только вопросы, самого текста нет',
       todo=('Прочитать текст для READING', 'блок «Материал» с текстом про sports day',
             'в выгрузке текста нет — написала его я, под все пять вопросов'))

t.add('quiz', {'title': 'Прочитай текст. Выбери правильный ответ', 'questions': [
    q_single('How does Jake feel today?', 'excited', ['scared', 'sad', 'excited']),
    q_single('Why is Sam scared?', "He doesn't like tug of war.",
             ["He doesn't like medals.", "He doesn't like tug of war.",
              "He doesn't like running."]),
    q_single("When is Lily's birthday?", 'in October', ['in June', 'in October', 'in November']),
    q_single('How does Mrs Brown feel?', 'happy', ['tired', 'angry', 'happy']),
    q_single('Is Jake scared of the three-legged race?', "No, he isn't.",
             ['Yes, he is.', "No, he isn't."])]},
    'вопросы и ответы — как отмечено в выгрузке')

t.text('<h3>LISTENING</h3><p>Послушай запись. Прочитай предложения и выбери '
       '«Верно» или «Неверно».</p>')

t.add('video', {'title': 'Аудио к заданию LISTENING',
                'url': 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm2/u6/sm2_u6_test_b13.mp3', 'provider': 'file'},
      'аудио прислала методист')

t.add('truefalse', {'title': 'Верно или неверно?', 'statements': [
    {'text': 'Clown 1 has got big ears and a small nose.', 'correct': False},
    {'text': 'Clown 1 is happy.', 'correct': True},
    {'text': 'Clown 2 has got long hair and glasses.', 'correct': True},
    {'text': "Clown 2's birthday is in March.", 'correct': False},
    {'text': 'Clown 3 is angry.', 'correct': False},
    {'text': 'Clown 3 has got a medal.', 'correct': True}]},
    'ответы — как отмечено в выгрузке')

t.add('speaking', {'title': 'SPEAKING TASK 🎤',
                   'html': '<p>Посмотри на картинку, выбери двух ребят и опиши их.</p>'
                           + img('kids_group') +
                           '<p>Например: <i>She has got black eyes. She is wearing glasses. '
                           'She is happy.</i></p>'
                           '<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>',
                   'sample_tts': 'She has got long hair and brown eyes. She is happy. '
                                 'He has got short hair. He is wearing a blue jumper.',
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
