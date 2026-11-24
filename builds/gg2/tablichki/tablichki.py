# -*- coding: utf-8 -*-
"""Таблички с правилами для Go Getter 2 (по боксам учебника, см. istochniki.md).
Сначала превью, заливка — только после «да» Анны."""
import json, pathlib

BLUE, GREEN, ORANGE, VIOLET = '#2F6FB8', '#2E9E6B', '#E8732A', '#6B4CC4'
DARK = {BLUE: '#1F4E7A', GREEN: '#1B6B49', ORANGE: '#B4530F', VIOLET: '#5B2FBF'}
BG = {BLUE: '#F2F7FC', GREEN: '#F1FAF5', ORANGE: '#FFF8EF', VIOLET: '#F5F2FF'}
TD = 'padding:4px 8px;border-bottom:1px solid #F0ECE6;vertical-align:top'
RU = TD + ';color:#6B7280'

def card(colour, head, body):
    return ('<div style="max-width:680px;border:1px solid #E6E0D8;border-radius:14px;'
            'overflow:hidden;font-size:15px;line-height:1.35">'
            f'<div style="background:{colour};color:#fff;padding:7px 12px;font-weight:700">{head}</div>'
            f'<div style="padding:10px 12px;background:#fff">{body}</div></div>')

def p(t, m='0 0 8px'):
    return f'<p style="margin:{m}">{t}</p>'

def pairs(rows, colour):
    out = ''.join(f'<tr><td style="{TD}"><b style="color:{DARK[colour]}">{a}</b></td>'
                  f'<td style="{RU}">{b}</td></tr>' for a, b in rows)
    return f'<table style="width:100%;border-collapse:collapse">{out}</table>'

def grid(colour, heads, rows):
    h = ''.join(f'<th style="text-align:left;padding:4px 8px;color:{DARK[colour]}">{x}</th>' for x in heads)
    r = ''.join('<tr>' + ''.join(f'<td style="{TD}">{c}</td>' for c in row) + '</tr>' for row in rows)
    return (f'<table style="width:100%;border-collapse:collapse;background:{BG[colour]}">'
            f'<tr>{h}</tr>{r}</table>')

def note(colour, t):
    bg = {BLUE: '#F2F7FC', GREEN: '#F1FAF5', ORANGE: '#FFF8EF', VIOLET: '#F5F2FF'}[colour]
    return (f'<p style="margin:10px 0 0;padding:8px 10px;background:{bg};'
            f'border-left:4px solid {colour};border-radius:8px">{t}</p>')

def warn(t):
    return ('<p style="margin:10px 0 0;padding:8px 10px;background:#FDF0F4;'
            'border-left:4px solid #D94A77;border-radius:8px">⚠️ ' + t + '</p>')

def pod(t):  # подводка «давай вспомним»
    return p('<b>Давай вспомним правило с урока.</b> ' + t)

C = {}   # key -> (куда, html)

# ─────────── Юнит 1 ───────────
C['u1_hw2'] = ('Юнит 1 · ДЗ 2 — новый блок 2', card(BLUE,
 'Unit 1 · Present Simple — то, что бывает обычно',
 pod('Present Simple — про то, что происходит <b>регулярно</b>: каждый день, по понедельникам, всегда.') +
 grid(BLUE, ['Кто', 'Глагол', 'Пример'], [
   ['I / You / We / They', '<b>listen</b>', '<b>I listen to music.</b> <span style="color:#6B7280">Я слушаю музыку.</span>'],
   ['He / She / It', '<b>listen<u>s</u></b>', '<b>He listens to music.</b> <span style="color:#6B7280">Он слушает музыку.</span>']]) +
 p('<b>Как добавляется -s у he / she / it</b>', '10px 0 4px') +
 pairs([('love → love<u>s</u> · eat → eat<u>s</u> · play → play<u>s</u>', 'обычно просто -s'),
        ('do → do<u>es</u> · go → go<u>es</u> · wash → wash<u>es</u>', 'после o, s, sh, ch — <b>-es</b>'),
        ('stud<u>y</u> → stud<u>ies</u> · fly → fl<u>ies</u>', 'после согласной <b>y → ies</b>')], BLUE) +
 p('<b>Как часто?</b> always → usually → often → sometimes → never', '10px 0 4px') +
 pairs([('I <u>never</u> listen to music.', 'перед обычным глаголом'),
        ('We <u>sometimes</u> watch TV.', 'перед обычным глаголом'),
        ('He <u>is</u> often late for school.', 'после <b>be</b>: is / am / are'),
        ('I <u>am</u> always happy.', 'после <b>be</b>')], BLUE)))

C['u1_hw3'] = ('Юнит 1 · ДЗ 3 — новый блок 2', card(GREEN,
 'Unit 1 · Present Simple — отрицание и вопрос',
 pod('В отрицании и вопросе помогают <b>do</b> и <b>does</b>, а сам глагол стоит в начальной форме.') +
 grid(GREEN, ['Кто', 'Отрицание', 'Вопрос'], [
   ['I / You / We / They', "<b>don't</b> paint", '<b>Do</b> you paint?'],
   ['He / She / It', "<b>doesn't</b> paint", '<b>Does</b> he paint?']]) +
 p('<b>Короткие ответы</b>', '10px 0 4px') +
 pairs([("Do you paint? — Yes, I <b>do</b>. / No, I <b>don't</b>.", 'Да. / Нет.'),
        ("Does she paint? — Yes, she <b>does</b>. / No, she <b>doesn't</b>.", 'Да. / Нет.'),
        ('Where <b>do</b> you paint? · How often <b>does</b> she paint?', 'с вопросительным словом')], GREEN) +
 note(GREEN, "don't = do not · doesn't = does not") +
 warn("После does глагол без -s: <b>Does he paints?</b> ✗ → <b>Does he paint?</b> ✓")))

C['u1_hw4'] = ('Юнит 1 · ДЗ 4 — новый блок 2', card(ORANGE,
 'Unit 1 · Как спросить про человека',
 p('Фразы урока. Послушай запись и повтори вслух.') +
 pairs([("What's your name?", 'Как тебя зовут?'),
        ('How do you spell that?', 'Как это пишется?'),
        ('Where do you live?', 'Где ты живёшь?'),
        ("What's your email address?", 'Какой у тебя адрес почты?'),
        ("What's your phone number?", 'Какой у тебя номер телефона?')], ORANGE) +
 note(ORANGE, 'Адрес почты вслух: <b>@</b> — «at», <b>.com</b> — «dot com». '
               'В номере <b>0</b> — «oh» или «zero», <b>33</b> — «double three».')))

C['u1_hw6'] = ('Юнит 1 · ДЗ 6 — новый блок перед заданием «Выбери at, in или on»', card(VIOLET,
 'Unit 1 · at, in или on — предлоги времени',
 pod('Какой предлог поставить, зависит от того, насколько точное время мы называем.') +
 grid(VIOLET, ['Предлог', 'Когда', 'Пример'], [
   ['<b>at</b>', 'точное время, ночь, выходные', '<b>at 7.30 · at night · at the weekend</b>'],
   ['<b>in</b>', 'часть дня, месяц, год', '<b>in the morning · in May · in 2026</b>'],
   ['<b>on</b>', 'день недели и дата', '<b>on Monday · on 3 June</b>']]) +
 warn('Исключение: <b>at night</b>, но <b>in the evening</b>.')))

# ─────────── Юнит 2 ───────────
C['u2_hw2'] = ('Юнит 2 · ДЗ 2 — вместо текста «Новое правило 💪» (блок 5)', card(BLUE,
 'Unit 2 · Что можно посчитать, а что нельзя · some / any',
 pod('Одни продукты можно посчитать поштучно, другие — нет. От этого зависит, как мы о них говорим.') +
 grid(BLUE, ['Считаем поштучно', 'Посчитать нельзя'], [
   ['<b>an egg, a strawberry, two lemons</b><br><span style="color:#6B7280">яйцо, клубника, два лимона</span>',
    '<b>sugar, milk, flour</b><br><span style="color:#6B7280">сахар, молоко, мука</span>'],
   ['There <b>are</b> some sausages.', 'There <b>is</b> some milk.'],
   ["There <b>aren't any</b> sausages.", "There <b>isn't any</b> milk."],
   ['<b>Are</b> there <b>any</b> sausages?<br>Yes, there are. / No, there aren’t.',
    '<b>Is</b> there <b>any</b> milk?<br>Yes, there is. / No, there isn’t.']]) +
 note(BLUE, '<b>some</b> — в утверждении, <b>any</b> — в вопросе и отрицании.')))

C['u2_hw3'] = ('Юнит 2 · ДЗ 3 — новый блок 2', card(GREEN,
 'Unit 2 · How much …? How many …? a lot of',
 pod('«Сколько?» по-английски спрашивают двумя разными способами.') +
 grid(GREEN, ['Можно посчитать', 'Посчитать нельзя'], [
   ['<b>How many</b> apples are there?<br><span style="color:#6B7280">Сколько яблок?</span>',
    '<b>How much</b> water is there?<br><span style="color:#6B7280">Сколько воды?</span>'],
   ['There are <b>a lot of</b> apples.<br>There are <b>six</b> apples.',
    'There is <b>a lot of</b> water.<br>There are <b>four bottles of</b> water.']]) +
 note(GREEN, 'Неисчисляемое считают ёмкостями: <b>a bottle of water, a bar of chocolate, '
              'a packet of biscuits</b>.')))

C['u2_hw4'] = ('Юнит 2 · ДЗ 4 — вместо текста «В кафе ☕» (блок 7)', card(ORANGE,
 'Unit 2 · Как заказать еду в кафе',
 p('Фразы урока. Послушай запись и повтори вслух.') +
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;font-weight:700;margin:0 0 6px">🧑‍🍳 Официант</div>' +
 pairs([('What would you like?', 'Что бы вы хотели?'),
        ('Would you like anything to drink?', 'Будете что-нибудь пить?'),
        ('Anything else?', 'Что-нибудь ещё?')], ORANGE) +
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;font-weight:700;margin:12px 0 6px">🙋 Гость</div>' +
 pairs([('Can I have <i>a vegetarian pizza</i>, please?', 'Можно мне вегетарианскую пиццу?'),
        ("I'd like <i>a lemonade</i>, please.", 'Я бы хотел лимонад.')], ORANGE) +
 note(ORANGE, 'Курсивом — то, что меняется: подставь любое блюдо из меню.')))

# ─────────── Юнит 3 ───────────
C['u3_hw2'] = ('Юнит 3 · ДЗ 2 — вместо текста «Правило: как прибавлять -ing» (блок 6)', card(BLUE,
 'Unit 3 · Present Continuous — что происходит сейчас',
 pod('Present Continuous — действие идёт <b>прямо сейчас</b>: <b>am / is / are</b> + глагол + <b>-ing</b>.') +
 grid(BLUE, ['Кто', 'Утверждение', 'Отрицание'], [
   ['I', "<b>I'm</b> talking.", "<b>I'm not</b> talking."],
   ['He / She / It', "<b>He's</b> talking.", "<b>He isn't</b> talking."],
   ['You / We / They', "<b>They're</b> talking.", "<b>They aren't</b> talking."]]) +
 p('<b>Как прибавляется -ing</b>', '10px 0 4px') +
 pairs([('look → look<u>ing</u>', 'обычно просто -ing'),
        ('tak<u>e</u> → tak<u>ing</u>', 'немая <b>e</b> в конце пропадает'),
        ('si<u>t</u> → si<u>tt</u>ing', 'короткое слово — согласная удваивается')], BLUE) +
 note(BLUE, "'m = am · 're = are · 's = is · isn't = is not · aren't = are not")))

C['u3_hw3'] = ('Юнит 3 · ДЗ 3 — вместо текста «Вопросы и краткие ответы» (блок 4)', card(GREEN,
 'Unit 3 · Present Continuous — вопрос и краткий ответ',
 pod('В вопросе <b>am / is / are</b> уходит вперёд, перед того, кто действует.') +
 grid(GREEN, ['Вопрос', 'Да', 'Нет'], [
   ['<b>Am I</b> coming?', 'Yes, I am.', "No, I'm not."],
   ['<b>Is he / she / it</b> coming?', 'Yes, he is.', "No, he isn't."],
   ['<b>Are you / we / they</b> coming?', 'Yes, we are.', "No, we aren't."]]) +
 p('<b>С вопросительным словом</b>', '10px 0 4px') +
 pairs([('<b>What</b> are you doing?', 'Что ты делаешь?'),
        ("<b>Where</b>'s it going?", 'Куда это едет?'),
        ('<b>Why</b> are they running?', 'Почему они бегут?')], GREEN)))

C['u3_hw4'] = ('Юнит 3 · ДЗ 4 — новый блок перед заданиями про телефон', card(ORANGE,
 'Unit 3 · Разговор по телефону',
 p('Фразы урока. Послушай запись и повтори вслух.') +
 pairs([("Hello, it's <i>Elena</i> here.", 'Здравствуйте, это Елена.'),
        ('Can I speak to <i>Amy</i>, please?', 'Можно Эми?'),
        ('Just one moment. / Just a minute. / Hang on.', 'Минутку. / Подожди.'),
        ("It's <i>Elena</i> for you.", 'Это тебя, Елена.'),
        ("I'm afraid he's / she's out.", 'Боюсь, его / её нет дома.'),
        ('Bye. / See you soon. / See you later.', 'Пока. / До скорого.')], ORANGE)))

# ─────────── Юнит 4 ───────────
C['u4_hw2'] = ('Юнит 4 · ДЗ 2 — вместо текста с правилом (блок 10)', card(BLUE,
 'Unit 4 · Сравниваем: comparative',
 pod('Чтобы сказать «выше», «интереснее», к прилагательному добавляют <b>-er</b> или ставят перед ним <b>more</b>.') +
 grid(BLUE, ['Какое слово', 'Как меняется', 'Пример'], [
   ['короткое', '+ <b>-er</b>', 'cold → cold<b>er</b> · nice → nic<b>er</b>'],
   ['короткое на согласную', 'согласная удваивается', 'big → bi<b>gger</b>'],
   ['короткое на -y', '<b>y → ier</b>', 'easy → eas<b>ier</b>'],
   ['длинное', '<b>more</b> + слово', 'exciting → <b>more</b> exciting'],
   ['особые', 'надо запомнить', 'good → <b>better</b> · bad → <b>worse</b>']]) +
 pairs([('That wall is <b>lower</b>.', 'Та стена ниже.'),
        ('Kayaking is <b>more exciting than</b> cycling.', 'Каякинг интереснее, чем велосипед.')], BLUE) +
 note(BLUE, 'Сравниваем с чем-то — ставим <b>than</b>: <i>bigger than</i>, <i>more exciting than</i>.')))

C['u4_hw3'] = ('Юнит 4 · ДЗ 3 — новый блок 2', card(GREEN,
 'Unit 4 · Короткие и длинные прилагательные',
 pod('В этой домашке ты раскладываешь слова по тому, как у них получается сравнительная форма.') +
 grid(GREEN, ['Группа', 'Правило', 'Примеры'], [
   ['короткие', '+ <b>-er</b>', 'cheap → cheaper · high → higher · low → lower'],
   ['на -y', '<b>-ier</b>', 'easy → easier · funny → funnier'],
   ['длинные (2+ слога)', '<b>more</b> +', 'boring → more boring · dangerous → more dangerous'],
   ['особые', 'запомнить', 'good → better · bad → worse']]) +
 note(GREEN, 'Слова урока: boring, cheap, dangerous, difficult, easy, exciting, expensive, high, low, safe.')))

C['u4_hw5'] = ('Юнит 4 · ДЗ 5 — новый блок 2', card(ORANGE,
 'Unit 4 · Как спросить и сказать своё мнение',
 p('Фразы урока. Послушай запись и повтори вслух.') +
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;font-weight:700;margin:0 0 6px">❓ Спрашиваем</div>' +
 pairs([("What's your favourite <i>film</i>?", 'Какой твой любимый фильм?'),
        ('What about you?', 'А ты?'),
        ('What do you think of <i>cartoons</i>?', 'Что ты думаешь о мультфильмах?')], ORANGE) +
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;font-weight:700;margin:12px 0 6px">💬 Отвечаем</div>' +
 pairs([('My favourite film is <i>Action Team</i>.', 'Мой любимый фильм — «Action Team».'),
        ('I think <i>Electro Max</i> is more exciting.', 'По-моему, «Electro Max» интереснее.'),
        ('In my opinion, they are a bit silly.', 'По-моему, они глуповаты.'),
        ("You're right. They are silly.", 'Ты прав. Они глупые.')], ORANGE)))

C['u4_hw6'] = ('Юнит 4 · ДЗ 6 — новый блок 2', card(VIOLET,
 'Unit 4 · Самый-самый: superlative',
 pod('Когда кто-то лучше всех, добавляем <b>the … -est</b> или <b>the most</b>.') +
 grid(VIOLET, ['Какое слово', 'Сравнительная', 'Превосходная'], [
   ['tall (короткое)', 'taller', '<b>the tallest</b>'],
   ['big', 'bigger', '<b>the biggest</b>'],
   ['funny (на -y)', 'funnier', '<b>the funniest</b>'],
   ['dangerous (длинное)', 'more dangerous', '<b>the most dangerous</b>'],
   ['good / bad', 'better / worse', '<b>the best</b> / <b>the worst</b>']]) +
 pairs([("He's <b>the funniest</b>.", 'Он самый смешной.'),
        ("They're <b>the most dangerous</b> animals in the world.", 'Это самые опасные животные в мире.')], VIOLET) +
 warn('Перед превосходной формой почти всегда стоит <b>the</b>.')))

# ─────────── Юнит 5 ───────────
C['u5_hw2'] = ('Юнит 5 · ДЗ 2 — новый блок 2', card(BLUE,
 'Unit 5 · was и were — «был, была, были»',
 pod('Это прошедшее время глагола <b>be</b>. Другого глагола в таком предложении нет.') +
 grid(BLUE, ['Кто', 'Утверждение', 'Отрицание'], [
   ['I / He / She / It', '<b>was</b> at the cinema', "<b>wasn't</b> at the park"],
   ['You / We / They', '<b>were</b> at the cinema', "<b>weren't</b> at the park"]]) +
 p('<b>There was / There were</b>', '10px 0 4px') +
 pairs([('There <b>was</b> a problem.', 'Была проблема.'),
        ("There <b>wasn't</b> a problem.", 'Проблемы не было.'),
        ('There <b>were</b> some buses.', 'Было несколько автобусов.'),
        ("There <b>weren't</b> any buses.", 'Автобусов не было.')], BLUE) +
 note(BLUE, "wasn't = was not · weren't = were not")))

C['u5_hw3'] = ('Юнит 5 · ДЗ 3 — вместо текста «Как говорить о времени в прошлом» (блок 2)', card(GREEN,
 'Unit 5 · Вопросы с was / were и слова о прошлом',
 pod('В вопросе <b>was</b> и <b>were</b> уходят вперёд.') +
 grid(GREEN, ['Вопрос', 'Да', 'Нет'], [
   ['<b>Was</b> I / he / she / it at the park?', 'Yes, he was.', "No, he wasn't."],
   ['<b>Were</b> you / we / they at the park?', 'Yes, they were.', "No, they weren't."],
   ['<b>Was</b> there a pizza in the fridge?', 'Yes, there was.', "No, there wasn't."],
   ['<b>Were</b> there any muffins?', 'Yes, there were.', "No, there weren't."]]) +
 p('<b>Когда это было</b>', '10px 0 4px') +
 pairs([('yesterday', 'вчера'),
        ('last night / last week / last month / last year', 'вчера вечером, на прошлой неделе, в прошлом месяце, в прошлом году'),
        ('last Monday / last May', 'в прошлый понедельник, в мае'),
        ('in 2014', 'в 2014 году')], GREEN) +
 note(GREEN, 'С вопросительным словом: <b>Where were</b> you last night? · <b>When was</b> Rocco at the park?')))

C['u5_hw5'] = ('Юнит 5 · ДЗ 5 — вместо текста «Communication: Directions» (блок 2)', card(ORANGE,
 'Unit 5 · Как спросить и объяснить дорогу',
 p('Фразы урока. Послушай запись и повтори вслух.') +
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;font-weight:700;margin:0 0 6px">❓ Спрашиваем дорогу</div>' +
 pairs([("Excuse me. Where's <i>North Street</i>?", 'Извините, где Норт-стрит?'),
        ("I'm looking for <i>a library</i>.", 'Я ищу библиотеку.'),
        ('How can I get to <i>the Science Museum</i>?', 'Как добраться до музея науки?'),
        ('Is it far?', 'Это далеко?')], ORANGE) +
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;font-weight:700;margin:12px 0 6px">➡️ Объясняем дорогу</div>' +
 pairs([("It's in / on <i>Green Street</i>.", 'Это на Грин-стрит.'),
        ('Go straight on.', 'Иди прямо.'),
        ('Go past <i>the cinema</i>.', 'Пройди мимо кинотеатра.'),
        ('Turn left. / Turn right.', 'Поверни налево. / направо.'),
        ("It's on the left. / It's on the right.", 'Это слева. / справа.')], ORANGE)))

# ─────────── Юнит 6 ───────────
C['u6_hw2'] = ('Юнит 6 · ДЗ 2 — новый блок 2', card(BLUE,
 'Unit 6 · Past Simple — правильные глаголы',
 pod('Чтобы рассказать о том, что уже случилось, к глаголу добавляют <b>-ed</b>. Форма одна для всех.') +
 grid(BLUE, ['Кто', 'Глагол', 'Пример'], [
   ['I / You / He / She / We / They', '<b>played</b>',
    '<b>I played football.</b> <span style="color:#6B7280">Я играл в футбол.</span>']]) +
 p('<b>Как добавляется -ed</b>', '10px 0 4px') +
 pairs([('cook → cook<u>ed</u>', 'обычно просто -ed'),
        ('arriv<u>e</u> → arriv<u>ed</u>', 'если слово кончается на -e, добавляем только -d'),
        ('tid<u>y</u> → tid<u>ied</u>', 'после согласной <b>y → ied</b>'),
        ('sto<u>p</u> → sto<u>pped</u>', 'короткое слово — согласная удваивается')], BLUE)))

C['u6_hw3'] = ('Юнит 6 · ДЗ 3 — вместо текста «Маркеры прошедшего времени» (блок 3)', card(GREEN,
 'Unit 6 · Слова-подсказки прошедшего времени',
 pod('Эти слова сразу говорят: действие уже закончилось.') +
 grid(GREEN, ['Сколько времени прошло', 'Пример'], [
   ['<b>ago</b> — «назад»', 'two days <b>ago</b> · an hour <b>ago</b> · a week <b>ago</b>'],
   ['', 'a month <b>ago</b> · a year <b>ago</b> · ten minutes <b>ago</b>'],
   ['<b>last</b> — «прошлый»', '<b>last</b> night · <b>last</b> week · <b>last</b> Monday'],
   ['просто время', '<b>yesterday</b> · <b>in 2014</b>']]) +
 pairs([('Her babysitter was ill two days <b>ago</b>.', 'Её няня болела два дня назад.')], GREEN) +
 note(GREEN, '<b>ago</b> ставится <u>после</u> промежутка времени: <i>a week ago</i>, а не <i>ago a week</i>.')))

C['u6_hw4'] = ('Юнит 6 · ДЗ 4 — вместо текста «Неправильные глаголы» (блок 2)', card(VIOLET,
 'Unit 6 · Неправильные глаголы',
 pod('У этих глаголов в прошедшем времени <b>нет -ed</b> — форму надо запомнить.') +
 grid(VIOLET, ['Сейчас', 'В прошлом', 'Перевод'], [
   ['come', '<b>came</b>', 'приходить'],
   ['drink', '<b>drank</b>', 'пить'],
   ['eat', '<b>ate</b>', 'есть'],
   ['feel', '<b>felt</b>', 'чувствовать'],
   ['go', '<b>went</b>', 'идти, ехать'],
   ['have', '<b>had</b>', 'иметь'],
   ['make', '<b>made</b>', 'делать'],
   ['meet', '<b>met</b>', 'встречать'],
   ['take', '<b>took</b>', 'брать']]) +
 pairs([('I <b>drank</b> a coke.', 'Я выпил колу.')], VIOLET)))

C['u6_hw5'] = ('Юнит 6 · ДЗ 5 — вместо текста «Asking for and giving permission» (блок 2)', card(ORANGE,
 'Unit 6 · Как попросить разрешения',
 p('Фразы урока. Послушай запись и повтори вслух.') +
 pairs([('Can I borrow <i>a pen</i>, please?', 'Можно одолжить ручку?'),
        ('Yes, you can. / Sure, no problem.', 'Да, конечно. / Без проблем.'),
        ("No, sorry, you can't.", 'Нет, извини, нельзя.'),
        ('Is it OK if I use <i>your mobile</i>?', 'Ничего, если я возьму твой телефон?'),
        ("No, sorry, it isn't OK.", 'Нет, извини, нельзя.'),
        ("Oh, all right. / Yes, that's fine.", 'Ну ладно. / Да, нормально.')], ORANGE) +
 note(ORANGE, '<b>Please</b> можно поставить и в начало, и в конец: '
               '<i>Please can I go to the party?</i> · <i>Can I go to the party, please?</i>')))

# ─────────── Юнит 7 ───────────
C['u7_hw2'] = ('Юнит 7 · ДЗ 2 — новый блок 2', card(BLUE,
 'Unit 7 · Past Simple — отрицание',
 pod('В отрицании помогает <b>didn’t</b>, а сам глагол возвращается в начальную форму.') +
 grid(BLUE, ['Какой глагол', 'Было', 'Отрицание'], [
   ['правильный', 'I stayed at home.', "I <b>didn't stay</b> at home."],
   ['неправильный', 'I slept well.', "I <b>didn't sleep</b> well."]]) +
 note(BLUE, "didn't = did not. Форма одна для всех: I / you / he / she / we / they <b>didn't</b> …") +
 warn("После didn't глагол без -ed: <b>I didn't stayed</b> ✗ → <b>I didn't stay</b> ✓")))

C['u7_hw5'] = ('Юнит 7 · ДЗ 5 — новый блок 2', card(ORANGE,
 'Unit 7 · Как купить билет',
 p('Фразы урока. Послушай запись и повтори вслух.') +
 pairs([("I'd like a ticket to <i>London</i>, please.", 'Мне билет до Лондона, пожалуйста.'),
        ('Here you are.', 'Вот, пожалуйста.'),
        ('How much is it?', 'Сколько стоит?'),
        ("It's <i>ten pounds twenty</i>, please.", 'Десять фунтов двадцать.'),
        ('What time does the train leave?', 'Во сколько отходит поезд?'),
        ('What time does it arrive?', 'Во сколько он приезжает?'),
        ('At <i>seven thirty</i>. / At <i>eight</i>.', 'В половине восьмого. / В восемь.')], ORANGE) +
 note(ORANGE, 'Цена вслух: <b>£10.50</b> — ten pounds fifty · <b>£7.25</b> — seven pounds '
               'twenty-five · <b>£0.50</b> — fifty pence.')))

# ─────────── Юнит 8 ───────────
C['u8_hw2'] = ('Юнит 8 · ДЗ 2 — новый блок 2', card(BLUE,
 'Unit 8 · be going to — планы на будущее',
 pod('Так говорят о том, что <b>собираются</b> сделать: <b>am / is / are</b> + <b>going to</b> + глагол.') +
 grid(BLUE, ['Кто', 'Утверждение', 'Отрицание'], [
   ['I', "<b>I'm going to</b> play.", "<b>I'm not going to</b> play."],
   ['He / She / It', "<b>He's going to</b> play.", "<b>He isn't going to</b> play."],
   ['You / We / They', "<b>They're going to</b> play.", "<b>They aren't going to</b> play."]]) +
 p('<b>Вопрос и краткий ответ</b>', '10px 0 4px') +
 pairs([('<b>Am I going to</b> play? — Yes, I am. / No, I’m not.', 'Я буду играть?'),
        ('<b>Is he going to</b> play? — Yes, he is. / No, he isn’t.', 'Он будет играть?'),
        ('<b>Are they going to</b> play? — Yes, they are. / No, they aren’t.', 'Они будут играть?')], BLUE)))

C['u8_hw3'] = ('Юнит 8 · ДЗ 3 — вместо текста «Сначала вспомним прошлое 🕰» (блок 2)', card(GREEN,
 'Unit 8 · Вопрос в любом времени',
 pod('Вопрос строится одинаково: вперёд выходит помощник — <b>be</b>, <b>have</b>, <b>can</b>, '
     '<b>do</b> или <b>did</b>.') +
 grid(GREEN, ['Утверждение', 'Вопрос'], [
   ['You <b>are</b> excited.', '<b>Are</b> you excited?'],
   ['You <b>are</b> wearing my clothes.', '<b>Are</b> you wearing my clothes?'],
   ['You <b>were</b> a good student.', '<b>Were</b> you a good student?'],
   ["You'<b>ve got</b> a girlfriend.", '<b>Have</b> you got a girlfriend?'],
   ['You <b>can</b> rap.', '<b>Can</b> you rap?'],
   ['You <b>want</b> tickets.', '<b>Do</b> you want tickets?'],
   ['She <b>sings</b>.', '<b>Does</b> she sing?'],
   ['You <b>went</b> to Paris.', '<b>Did</b> you go to Paris?']]) +
 pairs([('<b>Where do</b> you buy your clothes?', 'Где ты покупаешь одежду?'),
        ('<b>What did</b> you have for breakfast?', 'Что ты ел на завтрак?')], GREEN) +
 warn('После <b>do / does / did</b> глагол в начальной форме: <b>Did you went?</b> ✗ → '
      '<b>Did you go?</b> ✓')))

C['u8_hw5'] = ('Юнит 8 · ДЗ 5 — новый блок 2', card(ORANGE,
 'Unit 8 · Как договориться о встрече',
 p('Фразы урока. Послушай запись и повтори вслух.') +
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;font-weight:700;margin:0 0 6px">📨 Приглашаем</div>' +
 pairs([('Are you busy <i>next Thursday</i>?', 'Ты занят в следующий четверг?'),
        ("I've got tickets for <i>a basketball match</i>.", 'У меня есть билеты на баскетбол.'),
        ('Would you like to come?', 'Хочешь пойти?'),
        ("Let's meet outside <i>the Arena</i> / at <i>six o'clock</i>.", 'Давай встретимся у «Арены» / в шесть.')], ORANGE) +
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;font-weight:700;margin:12px 0 6px">👍 Отвечаем</div>' +
 pairs([("That sounds great. I'd love to come.", 'Звучит здорово. С радостью приду.'),
        ('What time does it start?', 'Во сколько начало?'),
        ('Where shall we meet?', 'Где встретимся?')], ORANGE)))

out = pathlib.Path('builds/gg2/tablichki')
out.mkdir(parents=True, exist_ok=True)
(out / 'tablichki.json').write_text(
    json.dumps({k: {'kuda': v[0], 'html': v[1]} for k, v in C.items()}, ensure_ascii=False, indent=1),
    encoding='utf-8')

PREV = ('<!doctype html><meta charset="utf-8"><title>Таблички GG2</title>'
        '<body style="font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;'
        'background:#FAF8F5;padding:24px;max-width:760px;margin:0 auto">'
        '<h1 style="font-size:20px">Таблички с правилами — Go Getter 2</h1>'
        '<p style="color:#6B7280;font-size:14px">Всего ' + str(len(C)) + '. Как это увидит ученик. '
        'Серой строкой — куда встаёт. Заливаю только после «да».</p>')
for k, (kuda, html) in C.items():
    PREV += (f'<h2 style="font-size:14px;color:#B4530F;margin:26px 0 8px">{kuda}</h2>' + html)
PREV += '</body>'
(out / 'preview.html').write_text(PREV, encoding='utf-8')
print(len(C), 'табличек,', sum(len(v[1]) for v in C.values()) // 1024, 'КБ')
