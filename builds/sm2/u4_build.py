# -*- coding: utf-8 -*-
"""SM2 · Unit 4 · Food — сборка восьми уроков."""
import os
from u4_lib import Lesson, WORDS, url, surl, img, simg, accept, scramble, distract, q_single

OUT = 'u4sql'
os.makedirs(OUT, exist_ok=True)
LESSONS = []

EN = [w for w, _, _ in WORDS]
YN = ['Yes, please.', 'No, thank you.']
ANY4 = ['Yes, there is.', 'Yes, there are.', "No, there isn't any.", "No, there aren't any."]


def q_multi(text, correct, options, image=None):
    """Вопрос с несколькими верными ответами."""
    d = {'q': text, 'type': 'multiple',
         'correct': sorted(options.index(c) for c in correct),
         'options': [{'text': x} for x in options]}
    if image:
        d['image'] = url(image)
    return d


# ─────────────────────────────────────────────────────────── ДЗ 1
l = Lesson('Homework 1', 'Food — новые слова', 0)

l.text(simg('hello_wave', 200) +
       '<h2>Привет!</h2>'
       '<p>Добро пожаловать в домашнее задание! Сегодня мы с тобой запомним новые слова. '
       'Будет вкусно, потому что мы будем учить названия продуктов! 😋</p>'
       '<p>После того, как завершишь все задания, внизу тебя ждёт дополнительная часть — '
       'её можно выполнить по желанию, НО если ты выполнишь, будешь нереально крут!</p>',
       'приветствие. В выгрузке была ссылка «вернись в кабинет и выбери Homework 1 (2)» — убрал, обе части в одном уроке')

l.text('<p>Вот все слова урока — рассмотри карточку, прежде чем начать.</p>' + img('card_market'),
       'карточка «Market» из выгрузки')

l.add('flashcards', {'cards': [{'text': w, 'translation': ru, 'image': url(p), 'audio_tts': w}
                               for w, ru, p in WORDS],
                     'title': 'Карточки: посмотри и запомни'},
      'механика «Карточки» из выгрузки')

l.add('flashcards', {'cards': [{'text': w, 'image': url(p), 'audio_tts': w} for w, ru, p in WORDS],
                     'title': 'Запомни: назови продукт по картинке'},
      'механика «Запомни» из выгрузки')

l.add('quiz', {'title': 'Послушай и выбери', 'questions': [
        q_single('Послушай и выбери, что ты услышал', w,
                 sorted([w] + distract(w, EN, 2, 'u4a' + w)), audio_tts=w)
        for w, _, _ in WORDS]},
      'механика «Послушай» из выгрузки')

l.add('match', {'title': 'Соедини картинку и слово', 'pairs': [
        {'left_image': url(p), 'right': w, 'right_audio_tts': w} for w, ru, p in WORDS]},
      'механика «Найди пару» из выгрузки')

l.add('exact_input', {'title': 'Скрэмбл: собери слово из букв', 'items': [
        {'prompt': f'{scramble(w, "u4" + w)}  ({ru})', 'accept': accept(w), 'audio_tts': w}
        for w, ru, p in WORDS]},
      'механика «Скрэмбл» из выгрузки')

l.add('exact_input', {'title': 'Напиши слово по-английски', 'items': [
        {'prompt': f'Напиши по-английски: {ru}', 'accept': accept(w), 'audio_tts': w}
        for w, ru, p in WORDS]},
      'механика «Заполни пропуски» из выгрузки — заменил на ввод слова целиком')

l.add('quiz', {'title': 'Проверь себя', 'questions': [
        q_single(f'Как по-английски «{ru}»?', w, sorted([w] + distract(w, EN, 2, 'u4b' + w)))
        for w, ru, p in WORDS]},
      'итоговый тест словаря')

# ── дополнительная часть
l.text('<h3>Дополнительная часть 🌟</h3>'
       '<p>Добро пожаловать в дополнительную часть домашнего задания!</p>'
       '<p>Здесь тебя ждут интересные упражнения. Их можно выполнить по желанию.</p>'
       '<p>НО если ты выполнишь их, то будешь большим молодцом!</p>')

l.add('speaking', {'title': 'Что вы покупаете? 🎤',
      'html': img('f_basket') +
              '<p>Нажми на микрофон и устно расскажи, какие продукты вы чаще всего покупаете.</p>'
              '<p>Но прежде чем записывать, послушай пример — я рассказала, что есть у меня в корзине.</p>'
              '<p>Удачи! У тебя всё получится!</p>',
      'sample_tts': 'In my basket there is some bread, some cheese and some milk. '
                    'There are three tomatoes and two lemons. There is a big watermelon, too!',
      'needs_review': True},
      'в выгрузке была фотография корзины — заменена рисунком f_basket')

l.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
       'для настоящих чемпионов!</p><p><b>Выбери правильный вариант:</b></p>')

l.add('quiz', {'title': 'a / an / some', 'questions': [
        q_single('Would you like ___ tomato?',   'a',    ['a', 'an', 'some'], image='f_tomato'),
        q_single('Would you like ___ egg?',      'an',   ['a', 'an', 'some'], image='f_egg'),
        q_single('Would you like ___ bread?',    'some', ['a', 'an', 'some'], image='f_bread'),
        q_single('Would you like ___ kiwi?',     'a',    ['a', 'an', 'some'], image='f_kiwi'),
        q_single('Would you like ___ grapes?',   'some', ['a', 'an', 'some'], image='f_grapes'),
      ]},
      'Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ, обложка в выгрузке пустая')

l.text('<p><b>Впиши слова:</b></p>')

l.add('exact_input', {'title': 'Посмотри на картинку и впиши слово', 'items': [
        {'image': url(p), 'prompt': 'Что на картинке?', 'accept': accept(w), 'audio_tts': w}
        for w, ru, p in WORDS[:6]]},
      'Wordwall «Впиши слова» — СОСТАВ МОЙ, обложка в выгрузке пустая')

l.text(simg('well_done_trophy', 200) +
       '<p>Вот и всё! Огромное спасибо за твой труд. Увидимся на занятии!</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 2
l = Lesson('Homework 2', 'Would you like…? и a / an / some', 1)

l.text(simg('hello_wave', 200) +
       '<h2>Привет!</h2>'
       '<p>В этом уроке тебя ждут несколько интересных заданий!</p>'
       '<p>Выполни все упражнения, если хочешь выучить тему на все 100!</p>'
       '<p>В конце тебя будет ждать дополнительное задание. Если ты его сделаешь, получишь звание '
       'ГРОССМЕЙСТЕРА английского 💪 (это очень крутое звание в шахматах ♟)</p>')

l.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_would'),
       'карточка «Would you like…?» из выгрузки')

l.text('<p>Мы начнём с видео. С ним ты научишься задавать вопрос «Не хочешь ли ты кофе?» '
       'или «Не хочешь ли ты сок?». Я оочень люблю сок и никогда от него не откажусь!</p>'
       '<p>Как думаешь, а герои видео откажутся от сока?</p>'
       '<p>Посмотри видео один раз, внимательно слушай, что говорит персонаж, и проверь себя — '
       'угадал ли ты? Затем посмотри видео снова и повторяй за персонажами.</p>')

l.add('video', {'title': 'Would you like some…?', 'url': ''},
      'НУЖНА ССЫЛКА НА ВИДЕО — в выгрузке медиафайла нет')

l.add('match', {'title': 'Соедини вопросы и подходящие ответы', 'pairs': [
        {'left': 'Would you like some coffee?', 'right': 'Yes, please.',
         'left_audio_tts': 'Would you like some coffee?', 'right_audio_tts': 'Yes, please.'},
        {'left': 'Would you like some lemonade?', 'right': 'No, thank you.',
         'left_audio_tts': 'Would you like some lemonade?', 'right_audio_tts': 'No, thank you.'}]},
      'в выгрузке инструкция «соедини вопросы и подходящие картинки», но картинок нет — '
      'собрал вопрос ↔ ответ')

l.text('<p>Посмотри на картинку — вспомни правило:</p>'
       '<p>Мы используем <b>a/an</b> с исчисляемыми существительными (которые мы можем посчитать) '
       'в единственном числе. С исчисляемыми существительными во множественном числе '
       'и неисчисляемыми существительными мы используем <b>some</b>.</p>' + img('rule_some'),
       'карточка-правило из выгрузки')

l.text('<p>А теперь потренируйся в использовании a/an/some — сыграй в игру ниже.</p>')

l.add('quiz', {'title': 'A / An / Some', 'questions': [
        q_single('There is ___ apple on the table.',      'an',   ['a', 'an', 'some']),
        q_single('There is ___ bottle on the table.',     'a',    ['a', 'an', 'some']),
        q_single('There is ___ cheese in the fridge.',    'some', ['a', 'an', 'some']),
        q_single('There are ___ apples in the fridge.',   'some', ['a', 'an', 'some']),
        q_single('Would you like ___ orange?',            'an',   ['a', 'an', 'some']),
        q_single('Would you like ___ potatoes?',          'some', ['a', 'an', 'some']),
      ]},
      'Wordwall — на обложке видно название «Quiz · SM2 Unit 4 - A/An/Some», по нему и собрал. СОСТАВ МОЙ')

l.text('<p>Отлично! Ты справился с половиной заданий. Ты — молодец.</p>'
       '<p>Внизу тебя ждут несколько вопросов, на которые нужно выбрать правильный ответ. '
       'Картинка поможет тебе понять, какой ответ нужно выбрать.</p>')

l.add('quiz', {'title': 'Выбери правильный ответ', 'questions': [
        {'q': 'Would you like a tomato?',      'type': 'single', 'correct': [0],
         'options': [{'text': YN[0]}, {'text': YN[1]}], 'image': surl('yes_thumb_up')},
        {'q': 'Would you like a lemon?',       'type': 'single', 'correct': [1],
         'options': [{'text': YN[0]}, {'text': YN[1]}], 'image': surl('no_thumb_down')},
        {'q': 'Would you like some potatoes?', 'type': 'single', 'correct': [1],
         'options': [{'text': YN[0]}, {'text': YN[1]}], 'image': surl('no_thumb_down')},
        {'q': 'Would you like some bread?',    'type': 'single', 'correct': [0],
         'options': [{'text': YN[0]}, {'text': YN[1]}], 'image': surl('yes_thumb_up')},
      ]},
      'в выгрузке к каждому вопросу фотография ребёнка с 👍 или 👎 — заменил общими картинками '
      'из media/shared. Ответы сверены с этими фотографиями')

l.text('<p>А теперь давай расставим слова в правильном порядке, чтобы получились предложения.</p>')

for words, sent in [
    (['Would', 'you', 'like', 'an', 'orange?'],      'Would you like an orange?'),
    (['Would', 'you', 'like', 'a', 'mango?'],        'Would you like a mango?'),
    (['Would', 'you', 'like', 'some', 'bread?'],     'Would you like some bread?'),
    (['Would', 'you', 'like', 'some', 'watermelons?'], 'Would you like some watermelons?'),
]:
    l.add('order', {'words': words, 'sentence': sent, 'audio_tts': sent})

l.add('task', {'title': 'Ответь о себе',
      'html': '<p>Ответь о себе на вопросы ниже. Варианты ответов — <b>Yes, please</b> / '
              '<b>No, thank you</b>.</p>'
              '<ol><li>Would you like some bread?</li><li>Would you like some cheese?</li>'
              '<li>Would you like a mango?</li><li>Would you like an apple?</li>'
              '<li>Would you like some oranges?</li></ol>',
      'needs_review': True})

l.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
       'для настоящих чемпионов!</p><p><b>Выбери правильный вариант:</b></p>')

l.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
        q_single('Would you like ___ watermelon?', 'a',    ['a', 'an', 'some']),
        q_single('Would you like ___ greens?',     'some', ['a', 'an', 'some']),
        q_single('Would you like ___ egg?',        'an',   ['a', 'an', 'some']),
      ]},
      'Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ, обложка в выгрузке пустая')

l.text('<p><b>Заполни пропуски:</b></p>')

l.add('gaps', {'title': 'Заполни пропуски: a / an / some', 'mode': 'drag',
      'text': '1. Would you like __a__ potato?\n'
              '2. Would you like __an__ apple?\n'
              '3. Would you like __some__ beans?\n'
              '4. Would you like __some__ water?'},
      'Wordwall «Заполни пропуски» — СОСТАВ МОЙ, обложка в выгрузке пустая')

l.text(simg('well_done_star', 200) + '<p>Отличная работа! Увидимся на уроке 👋</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 3
l = Lesson('Homework 3', 'Is / Are there any…?', 2)

l.text(simg('hello_rocket', 200) +
       '<h2>Добро пожаловать в домашнее задание!</h2>'
       '<p>Впереди тебя ждут несколько интересных видео и увлекательных упражнений, '
       'а также 1 дополнительное задание, которое можно выполнить по желанию.</p>'
       '<p>За каждое задание ты будешь получать ⭐⭐⭐⭐⭐</p>'
       '<p>Собери максимальное количество звёздочек и стань ЧЕМПИОНОМ.</p>')

l.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_there'),
       'карточка «Is / Are there any…?» из выгрузки')

l.text('<p>Давай посмотрим видео и узнаем, что у Penny есть дома. Но сначала попробуй угадать, '
       'какие продукты у неё есть.</p>'
       '<p>Посмотри видео один раз, внимательно слушай, что говорит персонаж, и проверь себя — '
       'угадал ли ты? Затем посмотри видео снова и повторяй за персонажами.</p>')

l.add('video', {'title': 'Что есть у Penny дома?', 'url': ''},
      'НУЖНА ССЫЛКА НА ВИДЕО — в выгрузке медиафайла нет')

l.add('match', {'title': 'Соедини вопросы с ответами', 'pairs': [
        {'left': 'Is there any cheese in the house?',  'right': "No, there isn't.",
         'left_audio_tts': 'Is there any cheese in the house?'},
        {'left': 'Are there any grapes in the house?', 'right': "No, there aren't.",
         'left_audio_tts': 'Are there any grapes in the house?'}]})

l.text('<p>Молодец!</p><p>Теперь время практики. Внизу ты найдёшь несколько вопросов, '
       'тебе нужно будет выбрать правильный ответ.</p>'
       '<p>Посмотри на картинку и отвечай по ней 👇</p>' + img('fridge_red'),
       'холодильник из выгрузки — по нему считаются ответы квиза ниже')

l.add('quiz', {'title': 'Посмотри на картинку и выбери правильный ответ', 'questions': [
        q_single('Are there any grapes in the fridge?', "No, there aren't any.",
                 ["No, there isn't any.", 'Yes, there is.', "No, there aren't any."]),
        q_single('Is there any chicken in the fridge?', 'Yes, there is.',
                 ['Yes, there is.', "No, there aren't any.", 'Yes, there are.']),
        q_single('Is there any bread in the fridge?', "No, there isn't any.",
                 ["No, there isn't any.", "No, there aren't any.", 'Yes, there are.']),
        q_single('Are there any eggs in the fridge?', 'Yes, there are.',
                 ["No, there isn't any.", 'Yes, there is.', 'Yes, there are.']),
      ]},
      'ответы сняты по отметкам в выгрузке и сверены с картинкой холодильника')

l.text('<p>Молодец! Ты справился с заданием. А теперь выбери правильный вариант для каждого пропуска.</p>')

l.add('gaps', {'title': 'Выбери правильный вариант', 'mode': 'drag',
      'text': "1. __Is__ there any cheese in the house? __No__, there __isn't__ any.\n"
              '2. Are there any __apples__ in the house? Yes, there __are__.\n'
              '3. __Is__ there __a__ banana in the house? __Yes__, there is.'})

l.text('<p>Посмотри на картинку ниже и письменно ответь на вопросы.</p>' + img('fridge_blue'))

l.add('task', {'title': 'Посмотри на картинку и ответь на вопросы',
      'html': '<ol><li>Is there any chicken in the fridge?</li>'
              '<li>Are there any grapes in the fridge?</li>'
              '<li>Are there any mangoes in the fridge?</li>'
              '<li>Are there any tomatoes in the fridge?</li>'
              '<li>Is there any cheese in the fridge?</li></ol>',
      'needs_review': True})

l.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
       'для настоящих чемпионов!</p><p><b>Расставь слова в правильном порядке:</b></p>')

for words, sent in [
    (['Is', 'there', 'any', 'bread', 'in', 'the fridge?'], 'Is there any bread in the fridge?'),
    (['Are', 'there', 'any', 'eggs', 'in', 'the box?'],    'Are there any eggs in the box?'),
    (['There', "aren't", 'any', 'lemons', 'in', 'the bag.'], "There aren't any lemons in the bag."),
]:
    l.add('order', {'words': words, 'sentence': sent, 'audio_tts': sent},
          'Wordwall «Unjumble · SM2 U4 (is/are +any)» — название видно на обложке. СОСТАВ МОЙ')

l.text('<p><b>Выбери правильный вариант:</b></p>')

l.add('quiz', {'title': 'Выбери правильный вариант', 'questions': [
        q_single('___ there any milk in the fridge?',  'Is',  ['Is', 'Are']),
        q_single('___ there any tomatoes in the box?', 'Are', ['Is', 'Are']),
        q_single('Is there any bread? — No, there ___ any.', "isn't", ["isn't", "aren't"]),
        q_single('Are there any kiwis? — No, there ___ any.', "aren't", ["isn't", "aren't"]),
      ]},
      'Wordwall «Выбери правильный вариант» — СОСТАВ МОЙ, обложка в выгрузке пустая')

l.text(simg('well_done_medal', 200) + '<p>Отлично! До встречи на уроке 👋</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 4
STORY = ("Flash: Here are two apples for everyone. "
         "Thunder: Look! I've got a bad apple. Misty: Me too. Whisper: So have I. "
         "Whisper: What can we do? Misty: I've got an idea. Come to the market with me. "
         "Man: Apples. Nice, sweet apples! "
         "Misty: The man has got a box with good apples and a box with bad apples. "
         "Flash and Thunder: We know what we can do. "
         "Flash: Eight apples, please. Man: Here you are. "
         "Flash: Look everybody! Whisper: Four bad apples! "
         "Thunder: A box of good apples and a box of bad apples. Woman: Well done, children!")

l = Lesson('Homework 4', 'История Bad Apples', 3)

l.text(simg('hello_book', 200) +
       '<h2>Добро пожаловать в домашнее задание!</h2>'
       '<p>Сегодня мы с тобой послушаем и прочитаем рассказ о наших супердрузьях!</p>'
       '<p>В дополнение к этому домашнему заданию идёт интерактивное видео — оно дополнительное '
       'и ты можешь сделать его по желанию, но ты будешь МЕГА крут, когда справишься с ним!</p>')

l.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_story'),
       'карточка «Ключевые фразы: Bad Apples» из выгрузки')

l.add('text', {'html': '<p>Твоё первое задание — послушать запись истории и выполнить тест под аудио.</p>'
                       '<p>В этот раз Misty, Thunder, Flash и Whisper отправляются на рынок за продуктами.</p>'
                       '<p>Прежде чем послушать аудио — посмотри на картинку. Почему ребята так смотрят '
                       'на фрукты? Что с ними не так? Попробуй угадать.</p>'
                       '<p>Прослушай аудио и узнай, угадал ли ты.</p>' + img('story_open'),
               'audio_tts': STORY},
      'НУЖНА АУДИОЗАПИСЬ ИСТОРИИ. Пока размечена под синтез — вся история одной строкой')

l.add('quiz', {'title': 'Прослушай историю ещё раз', 'questions': [
        q_single('Посчитай, сколько раз в истории встречается слово apples '
                 '(apple и название истории тоже считаются)', '11', ['5', '9', '11'],
                 image='f_apple')]},
      'ответ 11 — сверил по восьми кадрам плюс заголовок. '
      'В выгрузке здесь была фотография яблок — заменена рисунком f_apple')

l.text('<p>Молодец! А теперь внимательно прочитай историю и выполни упражнение, '
       'которое ты увидишь сразу после истории.</p>' + img('story_1') + img('story_2'),
       'кадры истории из выгрузки')

l.text('<p>Ты запомнил, кто что сказал?</p><p>Прочитай историю ещё раз и соедини фразы с героями.</p>'
       '<p>Удачи ❤</p>')

l.add('match', {'title': 'Соедини фразы с героями', 'pairs': [
        {'left': 'Come to the market with me.', 'right': 'Misty',
         'left_audio_tts': 'Come to the market with me.'},
        {'left': "I've got a bad apple.", 'right': 'Thunder',
         'left_audio_tts': "I've got a bad apple."},
        {'left': 'What can we do?', 'right': 'Whisper',
         'left_audio_tts': 'What can we do?'},
        {'left': 'Look everybody!', 'right': 'Flash',
         'left_audio_tts': 'Look everybody!'},
        {'left': 'Nice, sweet apples.', 'right': 'Man',
         'left_audio_tts': 'Nice, sweet apples.'}]})

l.text('<p>Прочитай историю ещё раз и выполни задание — расставь предложения в правильном порядке, '
       'как они идут в рассказе! У тебя всё получится!</p>')

l.add('sequence', {'title': 'Расставь предложения по порядку', 'items': [
        {'text': t, 'audio_tts': t} for t in [
            'Here are two apples for everyone.',
            "Look! I've got a bad apple.",
            "I've got an idea. Come to the market with me.",
            'Apples. Nice, sweet apples!',
            'The man has got a box with good apples and a box with bad apples.',
            'Look everybody! Four bad apples!',
            'Well done, children!']]})

l.text('<p>Вот он, рынок из нашей истории 👇</p>' + img('market'))

l.text(simg('well_done_clap', 200) +
       '<p>Ты справился! Вторая часть домашней работы — интерактивное видео — ждёт тебя '
       'в личном кабинете. Там нужно посмотреть видео и выполнить задания, которые '
       'уже находятся в самом видео. Она необязательная, но очень интересная 😀</p>',
       'вторая часть ДЗ 4 — интерактивное видео, содержимого в выгрузке нет')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 5
l = Lesson('Homework 5', 'Что в холодильнике: there is / there are', 4)

l.text(simg('hello_highfive', 200) +
       '<h2>Добро пожаловать в домашнее задание!</h2>'
       '<p>Тебя ждут интересные упражнения и 1 ДОПОЛНИТЕЛЬНОЕ задание, которое можно выполнить '
       'ПО ЖЕЛАНИЮ и получить дополнительные звёздочки.</p>'
       '<p>Чтобы стать ЧЕМПИОНОМ — необходимо собрать все звёздочки, которые ты будешь получать '
       'за выполнение каждого задания.</p>')

l.text('<p>Сейчас тебе нужно посмотреть видео и выполнить задание, которое находится под видео.</p>'
       '<p>Героиня видео покажет, какие продукты есть у неё в холодильнике. А что есть у тебя '
       'в холодильнике? Посмотри видео и сравни ваши холодильники.</p>')

l.add('video', {'title': "What's in my fridge?", 'url': ''},
      'НУЖНА ССЫЛКА НА ВИДЕО — в выгрузке медиафайла нет')

l.add('quiz', {'title': 'Посмотри видео ещё раз и выбери правильный ответ 🌟', 'questions': [
        q_single('Are there any eggs in the fridge?',    'Yes, there are.',       ANY4),
        q_single('Is there any cheese in the fridge?',   "No, there isn't any.",  ANY4),
        q_single('Are there any grapes in the fridge?',  'Yes, there are.',       ANY4),
        q_single('Are there any carrots in the fridge?', 'Yes, there are.',       ANY4),
        q_single('Are there any potatoes in the fridge?', "No, there aren't any.", ANY4),
      ]},
      'ответы сняты по отметкам в выгрузке. В первом вопросе в выгрузке был вариант '
      '«No, there isn\'t.» без any и «No, there aren\'t any..» с двумя точками — привёл к общему виду')

l.text('<p>Молодец, ты отлично справился! Скорее приступай к следующему заданию.</p>')

l.text('<p>Внимательно посмотри на картинку.</p>'
       '<p>Прочитай предложение и скажи, это правда (True) или неправда (False).</p>'
       '<p>За это задание ты сможешь получить 2 звёздочки 🌟🌟</p>' + img('fridge_photo'),
       'фото холодильника из выгрузки — по нему считаются утверждения ниже')

l.add('truefalse', {'title': 'Правда или неправда? Смотри на картинку выше', 'statements': [
        {'text': "There isn't any cheese in the fridge.", 'correct': False},
        {'text': 'There are some grapes in the fridge.',  'correct': True},
        {'text': 'There are some apples in the fridge.',  'correct': True},
        {'text': 'There is some bread in the fridge.',    'correct': False},
        {'text': "There aren't any eggs in the fridge.",  'correct': False}]},
      'ответы прописаны прямо в выгрузке и сошлись с картинкой')

l.text('<p>Ура, ты выполнил бо́льшую часть упражнений!</p>'
       '<p>Ниже ты найдёшь диалог. Но в нём чего-то не хватает 🤔 Посмотри, в тексте пропущены слова. '
       'Прочитай диалог и заполни пропуски.</p>'
       '<p>За это задание ты сможешь получить 3 звёздочки 🌟🌟🌟</p>' + img('kids_bubbles'))

l.add('gaps', {'title': 'Заполни пропуски', 'mode': 'drag',
      'text': 'Dad: Would you __like__ a sandwich, Sally?\n'
              'Sally: __Yes__, please.\n'
              'Dad: __Would__ you like __some__ cheese in your sandwich?\n'
              "Sally: __No__, thank you. I'd like a sausage. __Are__ there __any__ sausages in the fridge?\n"
              'Dad: Yes, there are. Would you like __an__ apple or __a__ banana, too?\n'
              "Sally: Yes, __please__. I'd like a banana."})

l.add('task', {'title': 'Нарисуй свой холодильник',
      'html': '<p>Нарисуй свой холодильник и письменно опиши, какие в нём есть продукты, а каких нет.</p>'
              '<p>Используй <b>there is a/some</b>, <b>there are some</b>, <b>there isn’t a/any</b>, '
              '<b>there aren’t any</b>…</p>'
              '<p><i>Например: There is a banana in my fridge. There is some cheese in my fridge. '
              'There are some tomatoes in my fridge. There isn’t any bread in my fridge. '
              'There aren’t any grapes in my fridge.</i></p>',
      'needs_review': True})

l.text(simg('well_done_smiley', 200) + '<p>Отличная работа! Увидимся на уроке 👋</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 6
l = Lesson('Homework 6', 'Веса и граммы', 5)

l.text(simg('hello_laptop', 200) +
       '<h2>Добро пожаловать в домашнее задание!</h2>'
       '<p>Сегодня тебя ждёт интересное видео, а также крутые задания!</p>'
       '<p>Ты будешь супер мега крутым, когда справишься с ними. Let’s go!</p>')

l.text('<p>Давай повторим всё, что выучили сегодня на уроке!</p>' + img('card_weights'),
       'карточка «Веса и граммы» из выгрузки')

l.text('<p>Я очень люблю готовить. И я подготовила для тебя видео-рецепт.</p>'
       '<p>Но прежде чем смотреть — угадай, что ребята приготовят на видео. '
       'Посмотри видео ниже и проверь — угадал ли ты?</p>')

l.add('video', {'title': 'Видео-рецепт', 'url': ''},
      'НУЖНА ССЫЛКА НА ВИДЕО — в выгрузке медиафайла нет')

l.text('<p>Чтобы блюдо получилось вкусным, нужно знать, какие ингредиенты добавлять и в каком '
       'количестве. В начале видео представлены все ингредиенты и их необходимое количество. '
       'Посмотри видео ещё раз и соедини продукты и их вес.</p>')

l.add('match', {'title': 'Соедини продукты и их вес', 'pairs': [
        {'left': 'Pineapple chunks',  'right': '500 g', 'left_audio_tts': 'pineapple chunks'},
        {'left': 'Mandarin oranges',  'right': '800 g', 'left_audio_tts': 'mandarin oranges'},
        {'left': 'Kiwi',              'right': '300 g', 'left_audio_tts': 'kiwi'},
        {'left': 'Banana',            'right': '700 g', 'left_audio_tts': 'banana'},
        {'left': 'Coconut',           'right': '100 g', 'left_audio_tts': 'coconut'},
        {'left': 'Lettuce',           'right': '350 g', 'left_audio_tts': 'lettuce'}]})

l.text('<p>Молодец! Ты справился с первым заданием.</p>'
       '<p>А теперь посмотри на картинки. Это же фрукты на весах! Помоги мне разобраться, '
       'сколько они весят — соедини вес продуктов с нужной картинкой.</p>'
       '<p>Но будь внимателен: одна цифра — лишняя.</p>')

l.add('hotspot', {'title': 'Соедини картинку с подходящей цифрой',
      'mode': 'label', 'image': url('scales'),
      'points': [
        {'x': 16, 'y': 34, 'text': '50 g'},
        {'x': 50, 'y': 34, 'text': '150 g'},
        {'x': 82, 'y': 34, 'text': '800 g'},
        {'x': 18, 'y': 81, 'text': '250 g'},
        {'x': 51, 'y': 81, 'text': '600 g'},
        {'x': 83, 'y': 81, 'text': '300 g'}],
      'extras': ['100 g']},
      'в выгрузке это блок «Диаграмма». Значения снял со стрелок на весах и сверил '
      'со списком в выгрузке — сошлись, лишний вариант 100 г')

l.text('<p>Ура, половина заданий позади!</p>'
       '<p>В следующем упражнении ты узнаешь, сколько весит 1 помидор, 1 киви. '
       'Как думаешь, что тяжелее? Давай приступим к заданию и поскорее узнаем!</p>'
       '<p>Внимательно изучи картинку и расставь фрукты по порядку, от самого лёгкого '
       'до самого тяжёлого.</p>' + img('weights_one'))

l.add('sequence', {'title': 'Расставь от самого лёгкого до самого тяжёлого', 'items': [
        {'text': t, 'audio_tts': t} for t in
        ['a grape', 'an egg', 'a kiwi', 'a tomato', 'a potato', 'a mango']]},
      'порядок сверен с весами на картинке: 5 г · 50 г · 75 г · 100 г · 150 г · 200 г')

l.text('<p>Ура! Это последнее задание на сегодня.</p>'
       '<p>С английским у тебя всё хорошо, поэтому пришло время потренировать математику.</p>'
       '<p>Посмотри на картинку. На ней указан вес 1 морковки, 1 лимона и 1 манго.</p>'
       + img('weights_key') +
       '<p>Ниже ты найдёшь примеры. Посчитай вес фруктов и письменно запиши.</p>'
       '<p><i>Например: 🥕 + 🍋 = 150 g</i></p>')

l.add('task', {'title': 'Посчитай вес фруктов', 'image': url('maths'),
      'html': '<p>Посмотри на картинку — на ней ты увидишь математические примеры. '
              'Посчитай вес фруктов и впиши правильные ответы.</p>'
              '<p>Помни: 1 carrot 🥕 = 50 g · 1 lemon 🍋 = 100 g · 1 mango 🥭 = 200 g</p>',
      'needs_review': True},
      'ответы: 1) 300 г  2) 350 г  3) 400 г  4) 750 г')

l.text(simg('well_done_jump', 200) + '<p>Отлично! До встречи на уроке 👋</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ДЗ 7
l = Lesson('Homework 7', 'Повторение перед тестом', 6)

l.text(simg('hello_rocket', 200) +
       '<h2>Привет!</h2>'
       '<p>Сегодня повторим всё-всё, что мы с тобой успели выучить за эту тему.</p>'
       '<p>В конце урока есть дополнительное задание — его можно выполнить по желанию, '
       'НО если ты сделаешь его, то будешь нереально крутым учеником!</p>')

l.text('<p>Сначала давай повторим с тобой продукты.</p>')

l.add('exact_input', {'title': 'Собери слово из букв', 'items': [
        {'prompt': f'{scramble(w, "u4h7" + w)}  ({ru})', 'accept': accept(w), 'audio_tts': w}
        for w, ru, p in WORDS]},
      'на этом месте была игра Wordwall «найди слово» — поиск слов в сетке букв мы не умеем, '
      'заменил скрэмблом по тем же словам. СОСТАВ МОЙ')

l.text('<p>Надеюсь, тебе понравилось!</p>'
       '<p>Теперь давай вспоминать, когда мы ставим <b>a / an / some</b>.</p>'
       '<p>Прочти диалоги ниже и впиши a/an/some.</p>')

l.add('gaps', {'title': 'Впиши a / an / some', 'mode': 'drag',
      'text': 'A: Would you like __a__ tomato?\nB: Yes, please.\n'
              'A: Would you like __some__ lemons?\nB: No, thank you.\n'
              'A: Would you like __an__ egg?\nB: Yes, please.\n'
              'A: Would you like __some__ grapes?\nB: No, thank you.\n'
              'A: Would you like __an__ orange?\nB: Yes, please.'})

l.text('<p>Посмотри на картинку и выбери правильный вариант ответа на вопросы.</p>' + img('stall'),
       'прилавок из выгрузки — по нему считаются ответы квиза ниже')

l.add('quiz', {'title': 'Ответь по картинке', 'questions': [
        q_single('Are there any grapes?',      'Yes, there are.',
                 ['Yes, there are.', "No, there aren't.", 'Yes, there is.', "No, there isn't."]),
        q_single('Are there any lemons?',      "No, there aren't.",
                 ['Yes, there are.', "No, there aren't.", 'Yes, there is.', "No, there isn't."]),
        q_single('Are there any watermelons?', "No, there aren't.",
                 ['Yes, there are.', "No, there aren't.", 'Yes, there is.', "No, there isn't."]),
        q_single('Is there any chicken?',      'Yes, there is.',
                 ['Yes, there are.', "No, there aren't.", 'Yes, there is.', "No, there isn't."]),
        q_single('Are there any eggs?',        'Yes, there are.',
                 ['Yes, there are.', "No, there aren't.", 'Yes, there is.', "No, there isn't."]),
        q_single('Is there any water?',        "No, there isn't.",
                 ['Yes, there are.', "No, there aren't.", 'Yes, there is.', "No, there isn't."]),
      ]},
      'ответы отмечены в выгрузке и сверены с картинкой прилавка')

l.text('<p>Давай представим, что мама попросила тебя сходить в магазин и купить продукты. '
       'Но вот беда — наш пакет выдерживает только 2000 грамм. К счастью, у нас есть картинка ниже. '
       'На ней указано, сколько весит каждый продукт.</p>' + img('weights_hw7'))

l.add('task', {'title': 'Собери пакет до 2000 г',
      'html': '<p>Внимательно посмотри на картинку выше и запиши как минимум 2 варианта, '
              'что можно купить в магазине, чтобы общий вес продуктов составлял не более 2000 г.</p>'
              '<p><i>Вот тебе пример: 2 potatoes, 2 lemons, 1 mango, 6 eggs, 1 kiwi.</i></p>',
      'needs_review': True},
      'в выгрузке в примере было «1 mangoes» — исправил на «1 mango»')

l.text('<p>Я подготовила несколько интересных картинок для тебя.</p>'
       '<p>Давай представим, что можно соединять несколько продуктов в один. Представь, '
       'сколько интересных продуктов могло бы получиться!</p>'
       '<p>Посмотри на картинки ниже и выбери, из каких 2 продуктов получился тот, '
       'что на картинке. Попробуй угадать!</p>')

l.add('quiz', {'title': 'Выбери два продукта, из которых получился этот', 'questions': [
        q_multi('Из чего получился этот фрукт?', ['apple', 'mandarin'],
                ['apple', 'kiwi', 'banana', 'mandarin'], image='hy_apple_mandarin'),
        q_multi('Из чего получился этот фрукт?', ['pineapple', 'banana'],
                ['orange', 'pineapple', 'banana', 'mango'], image='hy_pineapple_banana'),
        q_multi('Из чего получился этот продукт?', ['tomato', 'lemon'],
                ['potato', 'tomato', 'orange', 'lemon'], image='hy_tomato_lemon'),
        q_multi('Из чего получился этот фрукт?', ['strawberry', 'apple'],
                ['strawberry', 'kiwi', 'apple', 'orange'], image='hy_strawberry_apple'),
        q_multi('Из чего получился этот фрукт?', ['banana', 'orange'],
                ['banana', 'mango', 'orange', 'apple'], image='hy_banana_orange'),
        q_multi('Из чего получился этот фрукт?', ['orange', 'kiwi'],
                ['orange', 'banana', 'strawberry', 'kiwi'], image='hy_orange_kiwi'),
      ]},
      'шесть отдельных блоков «Тест» из выгрузки собраны в один квиз. '
      'В каждом по два верных варианта — сверил и по чекбоксам, и по самим картинкам')

l.text('<p>Включи свою фантазию на полную мощность и придумай гибриды — смесь разных фруктов '
       'или овощей. И попробуй придумать для них название.</p>'
       '<p>Например, это <b>grapetatoes</b> — grapes + potatoes 👇</p>' + img('hy_grape_potato') +
       '<p>С нетерпением жду нашего урока, чтобы скорее посмотреть на твои рисунки!</p>')

l.text('<p>Ты выполнил все задания из основной части! А это дополнительные задания — '
       'для настоящих чемпионов!</p><p><b>Впиши слова:</b></p>')

l.add('exact_input', {'title': 'Посмотри на картинку и впиши слово', 'items': [
        {'image': url(p), 'prompt': 'Что на картинке?', 'accept': accept(w), 'audio_tts': w}
        for w, ru, p in WORDS[5:]]},
      'Wordwall «Впиши слова» — СОСТАВ МОЙ, обложка в выгрузке пустая')

l.text('<p><b>Расставь слова в правильном порядке:</b></p>')

for words, sent in [
    (['Would', 'you', 'like', 'some', 'greens?'],        'Would you like some greens?'),
    (['Is', 'there', 'any', 'bread', 'in', 'the bag?'],  'Is there any bread in the bag?'),
    (['There', 'are', 'some', 'eggs', 'in', 'the fridge.'], 'There are some eggs in the fridge.'),
]:
    l.add('order', {'words': words, 'sentence': sent, 'audio_tts': sent},
          'Wordwall «Расставь слова в правильном порядке» — СОСТАВ МОЙ')

l.text('<p><b>Выбери верный вариант:</b></p>')

l.add('quiz', {'title': 'Выбери верный вариант', 'questions': [
        q_single('Would you like ___ watermelon?',          'a',    ['a', 'an', 'some']),
        q_single('___ there any beans in the box?',         'Are',  ['Is', 'Are']),
        q_single('Are there any kiwis? — Yes, there ___.',  'are',  ['is', 'are']),
        q_single('Is there any bread? — No, there ___ any.', "isn't", ["isn't", "aren't"]),
      ]},
      'Wordwall «Выбери верный вариант» — СОСТАВ МОЙ, обложка в выгрузке пустая')

l.text(simg('good_luck_clover', 200) + '<p>Ты готов к тесту на все 100% 💪 Удачи!</p>')

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── ТЕСТ
l = Lesson('Test', 'Super Minds 2 · Unit 4 · Test', 7, kind='test', threshold=90)

l.add('exact_input', {'title': 'Впиши буквы: напиши слово по-английски', 'items': [
        {'prompt': f'Напиши по-английски: {ru}', 'accept': accept(w), 'audio_tts': w}
        for w, ru, p in WORDS]})

l.add('match', {'title': 'Соедини слова с картинками', 'pairs': [
        {'left_image': url(p), 'right': w, 'right_audio_tts': w} for w, p in [
            ('watermelons', 'f_watermelon'), ('potatoes', 'f_potato'), ('grapes', 'f_grapes'),
            ('bread', 'f_bread'), ('lemons', 'f_lemon'), ('fish', 'f_fish')]]},
      'в выгрузке правая колонка пустая — подставил картинки')

l.add('quiz', {'title': 'Заполни пропуски — выбери подходящий вариант', 'questions': [
        q_single('A: ___ you like some cake?', 'Would', ['Would', 'Will', 'Do'], image='f_cake'),
        q_single('A: Would you like some cake? B: Yes, ___.', 'please', ['please', 'cake', 'thanks']),
        q_single('A: Would you ___ a mango?', 'like', ['like', 'love', 'want'], image='f_mango'),
        q_single('A: Would you like a mango? B: No, ___.', 'thank you',
                 ['thank you', "I don't want", 'please']),
        q_single('A: Are there any strawberries in the fridge? B: Yes, ___.', 'there are',
                 ['there are', 'there', 'there is'], image='f_strawberries'),
        q_single('A: ___ any cheese in the basket?', 'Is there',
                 ['Is there', 'Are there', 'There'], image='f_cheese'),
        q_single("A: Is there any cheese in the basket? B: No, ___ any.", "there isn't",
                 ["there isn't", 'there is', "there aren't"]),
        q_single("A: Let's make sandwiches for lunch! B: But ___ any bread.", "there isn't",
                 ["there isn't", "there aren't", 'there is'], image='f_bread'),
        q_single('A: ___ you like a slice of pizza? B: Of course!', 'Would', ['Would', 'Will', 'Do']),
      ]},
      'шесть блоков «Выбери правильный вариант» из выгрузки; предложения с двумя пропусками '
      'разбиты на два вопроса — итого девять')

for words, sent in [
    (['Are', 'there', 'any', 'bananas', 'in', 'the fridge?'], 'Are there any bananas in the fridge?'),
    (['Would', 'you', 'like', 'some', 'juice?'],              'Would you like some juice?'),
    (['There', "isn't", 'any', 'bread', 'in', 'the basket.'], "There isn't any bread in the basket."),
    (['Are', 'there', 'any', 'green', 'apples?'],             'Are there any green apples?'),
    (['Would', 'you', 'like', 'some', 'French fries?'],       'Would you like some French fries?'),
]:
    l.add('order', {'words': words, 'sentence': sent, 'audio_tts': sent},
          'Расставь слова в правильном порядке')

l.add('truefalse', {'title': 'READING · Прочитай текст и выбери Верно или Неверно', 'statements': [
        {'text': 'Mia is making a chocolate cake',   'correct': True},
        {'text': "They haven't got any flour",       'correct': False},
        {'text': 'There are some eggs',              'correct': True},
        {'text': 'There are some lemons',            'correct': False},
        {'text': "They've got some bread",           'correct': False},
        {'text': "Mia's mum offers some grapes",     'correct': True}]},
      'НУЖЕН САМ ТЕКСТ ДЛЯ ЧТЕНИЯ — в выгрузке есть только утверждения и ответы')

l.add('sort', {'title': 'LISTENING · Послушай запись и разложи продукты',
      'groups': [
        {'name': '✅ есть в магазине', 'items': [
            {'text': 'tomatoes', 'audio_tts': 'tomatoes'},
            {'text': 'butter',   'audio_tts': 'butter'},
            {'text': 'kiwis',    'audio_tts': 'kiwis'},
            {'text': 'sugar',    'audio_tts': 'sugar'},
            {'text': 'beans',    'audio_tts': 'beans'}]},
        {'name': '❌ нет в магазине', 'items': [
            {'text': 'mangoes',     'audio_tts': 'mangoes'},
            {'text': 'lemons',      'audio_tts': 'lemons'},
            {'text': 'watermelons', 'audio_tts': 'watermelons'}]}]},
      'в выгрузке это блок «Классификация». НУЖНА АУДИОЗАПИСЬ — без неё задание решается наугад')

l.add('task', {'title': 'SPEAKING TASK · Part 1', 'image': url('fridge_speaking'),
      'answer_kind': 'audio',
      'html': '<p>Посмотри на картинку и расскажи, что есть и чего нет в холодильнике. '
              'Используй <b>there is / there are</b> + <b>some / a / an / any</b>.</p>'
              '<p><i>For example: There is some milk in the fridge. There are three pears in the fridge. '
              'There isn’t any water in the fridge.</i></p>'
              '<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>',
      'needs_review': True})

l.add('task', {'title': 'SPEAKING TASK · Part 2', 'image': url('fridge_speaking'),
      'answer_kind': 'audio',
      'html': '<p>Посмотри на картинку и ответь на вопросы.</p>'
              '<ol><li>Is there any juice in the fridge?</li>'
              '<li>Are there any cupcakes in the fridge?</li>'
              '<li>Is there a fish in the fridge?</li>'
              '<li>Are there any carrots in the fridge?</li>'
              '<li>Would you like some cheese?</li>'
              '<li>Would you like a banana?</li></ol>'
              '<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>',
      'needs_review': True})

LESSONS.append(l)


# ─────────────────────────────────────────────────────────── запись
if __name__ == '__main__':
    for n, les in enumerate(LESSONS, 1):
        p = f'{OUT}/{n:02d}_{les.title.replace(" ", "_")}.sql'
        open(p, 'w', encoding='utf-8').write(les.sql())
        print(f'{p:34s} {len(les.blocks):2d} блоков')
