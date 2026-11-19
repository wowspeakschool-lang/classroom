"""Вводный урок 13+ (escape room) — всё содержание: чек-лист, комнаты, предметы, задания, план.
Структура согласована с Анной 04.11.2026 (builds/mvu_13plus/predmety.md).
build.py превращает это в lessons/mvu_13plus/index.html и план (Word/PDF).

Типы заданий (поле kind):
  choice — пункты по одному: вопрос (+картинка) и варианты; первый вариант верный (перемешивается в уроке)
  tf     — «верно / неверно»; у неверного fix — как правильно (показывается после ответа)
  match  — слово ↔ картинка (или слово ↔ определение)
  sort   — разложить по группам
  order  — собрать предложение
  listen — голосовое сообщение + вопросы choice
  hotspot— точки на картинке, к каждой выбрать слово
  oral   — картинка и вопросы учителя, ответ устно, балл ставит учитель (qs: вопрос, темы, ожидаемое)
  fix    — в предложении ошибка: нажать на неверное слово (bad — номер слова), сказать правильно (fix)
Каждый пункт помечен темой чек-листа (t), по ней балл попадает в чек-лист.
"""

# ── чек-лист: копия «Assessment chart» без изменений, только с id ──────────────────────────
CHECKLIST = [
    {'part': 1, 'title': 'ЧАСТЬ 1. Уровень А1.1 – А1.2', 'blocks': [
        ('PR 1 Unit 0-4', ['Families', 'Countries', 'School objects', 'To be', 'Have got', 'There is']),
        ('PR 1 Unit 5-9', ['Sports', 'Body parts', 'Food and drinks', 'Present Simple', 'Can/Can’t', 'Some, any, lots of']),
        ('PR 1 Unit 10-14', ['Jobs', 'Transport', 'Entertainment', 'Present Simple vs Present Continuous', 'Adverbs of frequency', 'Let’s…']),
        ('PR 1 Unit 15-20', ['Weather', 'Pets and farm animals', 'Clothes', 'Need, want', 'Comparatives', 'Past Simple']),
    ]},
    {'part': 2, 'title': 'ЧАСТЬ 2. Уровень А2.1 – В1.1', 'blocks': [
        ('PR 2 Unit 0-9', ['Clothes', 'Holidays', 'Emotions', 'Past Simple irregulars and Regulars', 'Present Simple vs Present Continuous', 'Quantifiers (some, any, a lot of)']),
        ('PR 3 Unit 0-9', ['Household and furniture', 'Ways of travelling', 'Adjectives to describe objects', 'Past continuous vs Past Simple', 'Future with will, may, might', 'Modals of obligation (must, have to)']),
        ('PR 4 Unit 0-9', ['Describing people', 'Crime and criminals', 'Money and shopping', 'Present Perfect vs Past Simple', 'Past Continuous', 'Be going to vs Present Continuous for future']),
        ('PR 2 Unit 10-20', ['Health and Illnesses', 'Geographical features', 'Travelling activities', 'Going to', 'Past Continuous', 'Have to/Don’t have to']),
        ('PR 3 Unit 10-20', ['Relationships', 'Free time activities: books and films', 'Body parts', 'Present Perfect', '1st Conditional', 'Present Simple and Past Simple Passive']),
        ('PR 4 Unit 10-20', ['Food and drink adjectives', 'Collocations with look, see, watch', 'Computer phrases', 'Reported speech', '2nd Conditional', 'Relative clauses']),
    ]},
    {'part': 3, 'title': 'ЧАСТЬ 3. Уровень В1.2 – В2.2', 'blocks': [
        ('PR 5 Unit 0-9', ['Sport phrases', 'Health verbs', 'Music', 'Ing forms', 'Used to', 'Modals of obligation and advice']),
        ('PR 6 Unit 0-9', ['Education', 'Phrasal verbs for relationships', 'Natural disasters', 'Modals of ability and possibility', 'Passive: complex forms', 'Question forms (complex)']),
        ('PR 7 Unit 0-9', ['Online, films and media', 'Abstract nouns', 'History', 'Future Continuous and perfect', 'Narrative tenses', 'Present and past habits']),
        ('PR 5 Unit 10-20', ['Social media', 'Verbs of communication', 'Hopes and dreams', 'Past Perfect', 'Reporting verbs', 'Causative have']),
        ('PR 6 Unit 10-20', ['Personal qualities', 'Crime and criminals', 'Reporting verbs', 'Reported questions and requests', 'Modals of deduction in the past', '3d conditional']),
        ('PR 7 Unit 10-20', ['Idioms', 'Advertising', 'Global issues', 'Modals in the past', '3d and mixed Conditionals', 'Determiners']),
    ]},
]


def tid(part, block, n):
    """id темы: p<часть>b<блок>t<номер>, всё с 1."""
    return f'p{part}b{block}t{n}'


def find(part, name, block=None):
    """id темы по названию (в части 2 Past Continuous встречается дважды — тогда блок обязателен)."""
    hits = []
    for bi, (_, topics) in enumerate(CHECKLIST[part - 1]['blocks'], 1):
        for ti, t in enumerate(topics, 1):
            if t == name and (block is None or block == bi):
                hits.append(tid(part, bi, ti))
    assert len(hits) == 1, (part, name, hits)
    return hits[0]


def T(part, *names):
    return [find(part, n) if not isinstance(n, tuple) else find(part, n[0], n[1]) for n in names]



M = 'https://classroom.wowteach.ru/media/mvu_13plus/'

# ── комнаты ────────────────────────────────────────────────────────────────────────────────
# Предмет: id, img (картинка на экране «назови»), x/y/h — где стоит в комнате (в % сцены, если у комнаты
# нет вырезок), name — что ученик должен назвать, name_t — тема (пусто — без балла), ask — вопрос учителя,
# tasks — задания, you — вопросы «And you?».
# Задание: kind, title (по-русски — для учителя, в план), en (короткая инструкция на экране), items.
# Состав — по правке Анны 13.11.2026 («Урок 13+ после сокращения — правка Анны 13.11.docx») и решениям 13–19.11.

WHAT = "What's this?"
WHATP = "What are these?"

P1 = [
    dict(id='family_photo', img='family_photo', x=84, y=50, h=12, wall=0, name='a family photo', ask=WHAT, name_t=[],
         tasks=[dict(kind='choice', title='Посмотри на семейное дерево Тома и выбери верный вариант', en='Look at the family tree and choose.',
                     image='family_tree', items=[
             dict(q='Bob is Emma’s ___ .', o=['uncle', 'father', 'grandfather'], t=T(1, 'Families')),
             dict(q='Mark and Kate ___ Tom’s parents.', o=['are', 'is', 'am'], t=T(1, 'To be')),
         ])],
         you=[('Tell me about your family.', T(1, 'Families', 'To be'))]),
    dict(id='schoolbag', img='schoolbag', x=30.7, y=88, h=19, wall=0, name='a schoolbag (a backpack)', ask=WHAT,
         name_t=T(1, 'School objects'),
         tasks=[dict(kind='choice', title='Это рюкзак Тома. Посмотри, что в нём лежит, и выбери верный вариант', en='Look and choose.',
                     image='schoolbag_open', items=[
             dict(q='There ___ two pens.', o=['are', 'is', 'am'], t=T(1, 'There is')),
             dict(q='Tom ___ got a pencil case.', o=['has', 'have', 'is'], t=T(1, 'Have got')),
         ])],
         you=[('What have you got in your school bag?', T(1, 'School objects', 'Have got'))]),
    dict(id='passport', img='passport', x=41, y=68, h=5, wall=0, name='a passport', ask=WHAT, name_t=[],
         tasks=[dict(kind='choice', title='Это паспорт друга Тома. Посмотри на флаг и выбери верный вариант', en='Look at the flag and choose.', items=[
             dict(flag='de', q='Hans is from Germany. He’s ___ .', o=['German', 'Germany', 'Germanish'], t=T(1, 'Countries')),
         ])],
         you=[('Where are you from? Which country would you like to visit?', T(1, 'Countries'))]),
    dict(id='fruit_bowl', img='fruit_bowl', x=50, y=68.3, h=9, wall=0, name='fruit (a bowl of fruit)', ask=WHAT,
         name_t=T(1, 'Food and drinks'),
         tasks=[dict(kind='choice', title='Фрукты есть в вазе, а что в холодильнике у Тома? Выбери слово', en='Look and choose.',
                     image='fridge_open', items=[
             dict(q='There is ___ milk in the fridge.', o=['some', 'any', 'a'], t=T(1, 'Some, any, lots of')),
             dict(q='There aren’t ___ apples in the fridge.', o=['any', 'some', 'a'], t=T(1, 'Some, any, lots of')),
         ])],
         you=[('What do you usually have for breakfast?', T(1, 'Food and drinks'))]),
    dict(id='football', img='football', x=21, y=96.6, h=11, wall=0, name='a football (a ball)', ask=WHAT,
         name_t=T(1, 'Sports'),
         tasks=[
             dict(kind='hotspot', title='Это Том, он играет в футбол. Что показывает стрелка? Выбери слово', en='Look and choose one word.', image='athlete',
                  words=['head', 'arm', 'hand', 'knee', 'foot', 'leg'], items=[
                      dict(x=33, y=71, a='knee', t=T(1, 'Body parts')),
                      dict(x=48, y=6, a='head', t=T(1, 'Body parts')),
                  ]),
             dict(kind='choice', title='Том очень любит спорт. Посмотри на картинку и выбери верный вариант', en='Look and choose.', items=[
                 dict(img='sport_bike', q='___ Tom ride a bike to school? — Yes, he does.', o=['Does', 'Do', 'Is'], t=T(1, 'Present Simple')),
                 dict(img='sport_tennis', q='Tom can play tennis, but he ___ play basketball.', o=['can’t', 'can', 'don’t can'], t=T(1, 'Can/Can’t')),
             ])],
         you=[]),
    dict(id='bus', img='bus', x=93.5, y=50, h=6, wall=0, name='a bus', ask=WHAT,
         name_t=T(1, 'Transport'),
         tasks=[dict(kind='oral', title='Вид из окна. Спросите ученика, кого он видит и чем люди заняты; ответов на экране нет', image='street',
                     en='Look out of the window!', qs=[
             ('Who can you see? What do they do?', T(1, 'Jobs'), 'a police officer, a doctor, a chef…'),
             ('What is she doing?', T(1, 'Present Simple vs Present Continuous'), 'She is riding a bike.'),
             ('What’s on the bridge?', T(1, 'Transport'), 'a train'),
         ])],
         you=[]),
    dict(id='cinema_tickets', img='cinema_tickets', x=59.6, y=68, h=5, wall=0, name='cinema tickets', ask=WHATP,
         name_t=T(1, 'Entertainment'),
         tasks=[
             dict(kind='order', title='Том и его друзья любят кино. Собери предложение', en='Put the words in order.', items=[
                 dict(s='I always go to the cinema on Fridays.', t=T(1, 'Adverbs of frequency')),
             ]),
             dict(kind='choice', title='У Тома два билета в кино. Выбери верный вариант', en='Choose the right answer.', items=[
                 dict(q='Let’s ___ to the cinema tonight!', o=['go', 'going', 'to go'], t=T(1, 'Let’s…')),
             ])],
         you=[('How often do you go to the cinema? What are your favourite places in your city?', T(1, 'Adverbs of frequency', 'Entertainment'))]),
    dict(id='umbrella', img='umbrella', x=82, y=93, h=16, wall=0, name='an umbrella', ask=WHAT, name_t=[],
         tasks=[
             dict(kind='sort', title='Завтра едем на море: солнечно и жарко. Что берём, а что оставляем? Ученик раскладывает и называет каждую вещь вслух',
                  en='What do you take? Sort and name.', image='w_sunny', groups=['Take ✅', 'Don’t take ❌'], items=[
                      dict(w='shorts', img='cl_shorts', g=0, t=T(1, 'Clothes')),
                      dict(w='a T-shirt', img='cl_tshirt', g=0, t=T(1, 'Clothes')),
                      dict(w='a jacket', img='cl_jacket', g=1, t=T(1, 'Clothes')),
                      dict(w='a scarf', img='cl_scarf', g=1, t=T(1, 'Clothes')),
                  ]),
             dict(kind='choice', title='Выбери слово', en='Choose the right word.', items=[
                 dict(q='Tom ___ to the beach every summer.', o=['goes', 'go', 'gos'], t=T(1, 'Present Simple')),
             ])],
         you=[('What’s the weather like today? What do you need for a trip to the mountains?', T(1, 'Weather', 'Need, want', 'Clothes'))]),
    dict(id='cat', img='cat', x=66.3, y=96.6, h=17, wall=0, name='a cat', ask=WHAT,
         name_t=T(1, 'Pets and farm animals'),
         tasks=[
             dict(kind='choice', title='Это кошка Тома. Посмотри на животных и выбери верный вариант', en='Look and choose.', items=[
                 dict(img2=['an_horse', 'an_cat'], q='A horse is ___ than a cat.', o=['bigger', 'big', 'biggest'], t=T(1, 'Comparatives')),
                 dict(img2=['an_tiger', 'an_cat'], q='A tiger is ___ than a cat.', o=['more dangerous', 'dangerouser', 'most dangerous'], t=T(1, 'Comparatives')),
                 dict(img2=['an_cow', 'an_pig', 'an_chicken'], q='Which animal gives us milk?', o=['a cow', 'a pig', 'a chicken'], t=T(1, 'Pets and farm animals')),
             ]),
             dict(kind='listen', title='Голосовое сообщение про ферму. Послушай и ответь на вопросы', en='Listen and choose.', audio='p1_voicemail_v2',
                  text=('Yesterday Tom went to his grandparents’ farm. In the morning he fed the chickens and the sheep. '
                        'Then he rode a horse! He didn’t see the pigs, because they were asleep. '
                        'In the evening they had a big dinner and watched a film. It was a great day!'),
                  items=[
                      dict(q='What did Tom ride?', o=['a horse', 'a bike', 'a bus'], t=T(1, 'Past Simple')),
                      dict(q='Did he see the pigs?', o=['No, he didn’t.', 'Yes, he did.', 'No, he don’t.'], t=T(1, 'Past Simple')),
                      dict(q='What did they do in the evening?', o=['They watched a film.', 'They played football.', 'They went to bed.'], t=T(1, 'Past Simple')),
                  ])],
         you=[('What did you do last weekend?', T(1, 'Past Simple'))]),
]

P2 = [
    dict(id='wardrobe', img='wardrobe', x=89.3, y=77.8, h=40, wall=0, name='a wardrobe (a big wooden wardrobe)', ask=WHAT,
         name_t=T(2, 'Household and furniture'),
         tasks=[
             dict(kind='sort', title='Спальня или кухня? Ученик раскладывает картинки и называет каждую вещь', en='Sort and name.',
                  groups=['Bedroom 🛏', 'Kitchen 🍳'], items=[
                      dict(w='a bed', img='fu_bed', g=0, t=T(2, 'Household and furniture')),
                      dict(w='a chest of drawers', img='fu_drawers', g=0, t=T(2, 'Household and furniture')),
                      dict(w='a fridge', img='fu_fridge', g=1, t=T(2, 'Household and furniture')),
                      dict(w='a cooker', img='fu_cooker', g=1, t=T(2, 'Household and furniture')),
                  ]),
             dict(kind='choice', title='Загляни в шкаф и выбери верный вариант', en='Choose the right word.', items=[
                 dict(q='There aren’t ___ clothes in the wardrobe.', o=['many', 'much', 'a'], t=T(2, 'Quantifiers (some, any, a lot of)')),
                 dict(q='My sister keeps ___ shoes in this wardrobe — more than fifty pairs!', o=['a lot of', 'much', 'any'], t=T(2, 'Quantifiers (some, any, a lot of)')),
             ])],
         you=[('Describe your room.', T(2, 'Adjectives to describe objects'))]),
    dict(id='suitcase', img='suitcase', x=48.5, y=98, h=14, wall=0, name='a suitcase', ask=WHAT,
         name_t=T(2, 'Holidays'),
         tasks=[dict(kind='choice', title='Это чемодан Mia — она вернулась из отпуска. Выбери верный вариант', en='Look and choose.', items=[
             dict(img='hol_castle', q='At the castle Mia was ___ .', o=['excited', 'bored', 'angry'], t=T(2, 'Emotions')),
             dict(q='Mia usually ___ to the beach on holiday, but today she ___ a castle.', o=['goes … is visiting', 'is going … visits', 'goes … visits'], t=T(2, 'Present Simple vs Present Continuous')),
         ])],
         you=[('Tell me about your best trip. Where did you go? How did you feel?', T(2, 'Holidays', 'Past Simple irregulars and Regulars', 'Emotions'))]),
    dict(id='map', img='map', x=32.2, y=27.8, h=13, wall=1, name='a map', ask=WHAT,
         name_t=T(2, 'Geographical features'),
         tasks=[
             dict(kind='match', title='Что есть на карте? Соедини слова с картинками', en='Match the words and the pictures.', items=[
                 dict(w='a river', img='geo_river', t=T(2, 'Geographical features')),
                 dict(w='an island', img='geo_island', t=T(2, 'Geographical features')),
                 dict(w='go sightseeing', img='tr_sightseeing', t=T(2, 'Travelling activities')),
                 dict(w='go camping', img='tr_camping', t=T(2, 'Travelling activities')),
             ]),
             dict(kind='choice', title='Это карта путешествий. Выбери верный вариант', en='Choose the right answer.', items=[
                 dict(img='tr_ferry', q='We crossed the sea ___ .', o=['by ferry', 'on foot', 'by bike'], t=T(2, 'Ways of travelling')),
                 dict(img='geo_mountains', q='Next summer we ___ climb these mountains. We’ve already bought the tickets.', o=['are going to', 'might', 'will can'], t=T(2, 'Going to')),
                 dict(q='I’m not sure, but I ___ go to Italy next year.', o=['might', 'am going to', 'must'], t=T(2, 'Future with will, may, might')),
             ])],
         you=[('What are you going to do this summer?', T(2, 'Going to'))]),
    dict(id='first_aid_kit', img='first_aid_kit', x=9.3, y=67.8, h=9, wall=0, name='a first-aid kit', ask=WHAT,
         name_t=T(2, 'Health and Illnesses'),
         tasks=[dict(kind='choice', title='Разговор у врача. Выбери верный вариант', en='Choose the right answer.', items=[
             dict(q='— What’s the matter? — I’ve got a ___ . I ate too much.', o=['stomachache', 'stomach', 'hurt'], t=T(2, 'Health and Illnesses')),
             dict(q='You’ve got a high temperature. You ___ stay in bed today — don’t go out!', o=['must', 'mustn’t', 'don’t have to'], t=T(2, 'Modals of obligation (must, have to)')),
             dict(q='It’s Saturday tomorrow — you ___ go to school.', o=['don’t have to', 'have to', 'mustn’t to'], t=T(2, 'Have to/Don’t have to')),
         ])],
         you=[]),
    dict(id='novel', img='novel', x=31.5, y=71, h=5.5, wall=0, name='a book (a novel)', ask=WHAT,
         name_t=T(2, 'Free time activities: books and films'),
         tasks=[dict(kind='choice', title='Это отзыв о книге. Выбери верный вариант', en='Choose the right answer.', items=[
             dict(q='This book ___ by a 15-year-old girl in 2010.', o=['was written', 'wrote', 'is writing'], t=T(2, 'Present Simple and Past Simple Passive')),
             dict(q='I love it! I ___ it three times.', o=['have read', 'am reading', 'reads'], t=T(2, 'Present Perfect')),
             dict(q='Kate and Sam are best friends, but then they ___ in love.', o=['fall', 'get', 'make'], t=T(2, 'Relationships')),
             dict(q='If you like adventures, you ___ love it.', o=['will', 'would', 'are'], t=T(2, '1st Conditional')),
         ])],
         you=[]),
    dict(id='wanted_poster', img='wanted_poster', x=50, y=55.6, h=13, wall=1, name='a poster (a wanted poster)', ask=WHAT,
         name_t=T(2, 'Crime and criminals'),
         tasks=[dict(kind='choice', title='Что было в музее той ночью? Выбери верный вариант', en='Choose the right answer.', items=[
             dict(q='The thief ___ the painting when the alarm ___ .', o=['was taking … rang', 'took … was ringing', 'was taking … was ringing'],
                  t=T(2, 'Past continuous vs Past Simple', ('Past Continuous', 3), ('Past Continuous', 4))),
         ])],
         you=[('Describe someone in your family. What does he or she look like?', T(2, 'Describing people'))]),
    dict(id='wallet', img='wallet', x=22.5, y=60.5, h=5, wall=0, name='a wallet', ask=WHAT,
         name_t=T(2, 'Money and shopping'),
         tasks=[dict(kind='choice', title='Покупки. Выбери верный вариант', en='Choose the right answer.', items=[
             dict(q='I ___ any new clothes for two years.', o=['haven’t bought', 'didn’t buy', 'don’t buy'], t=T(2, 'Present Perfect vs Past Simple')),
             dict(q='I ___ my friends at the shopping centre at 5 tomorrow — it’s all arranged.', o=['am meeting', 'meet', 'met'], t=T(2, 'Be going to vs Present Continuous for future')),
         ])],
         you=[]),
    dict(id='laptop', img='laptop', x=18.1, y=69.4, h=11, wall=0, name='a laptop', ask=WHAT,
         name_t=T(2, 'Computer phrases'),
         tasks=[dict(kind='fix', title='Переписка в чате: в каждом предложении ошибка. Ученик нажимает на неверное слово и говорит правильно вслух',
                     en='Find the mistake and correct it.', items=[
             dict(s='Tom said that he is tired.', bad=4, fix='was', t=T(2, 'Reported speech')),
             dict(s='The boy which lives next door is my friend.', bad=2, fix='who', t=T(2, 'Relative clauses')),
         ])],
         you=[('What do you usually do on your phone?', T(2, 'Computer phrases'))]),
    dict(id='binoculars', img='binoculars', x=28.5, y=62, h=6, wall=0, name='binoculars', ask=WHATP, name_t=[],
         tasks=[
             dict(kind='match', title='Посмотри в бинокль на кафе напротив. Какая там еда на вкус? Соедини слово с блюдом', en='Match the words and the pictures.', items=[
                 dict(w='spicy', img='food_spicy', t=T(2, 'Food and drink adjectives')),
                 dict(w='sour', img='food_sour', t=T(2, 'Food and drink adjectives')),
                 dict(w='sweet', img='food_sweet', t=T(2, 'Food and drink adjectives')),
                 dict(w='salty', img='food_salty', t=T(2, 'Food and drink adjectives')),
             ]),
             dict(kind='choice', title='Что можно делать с биноклем? Выбери верный вариант', en='Choose the right word.', items=[
                 dict(q='___ at that bird! It’s huge!', o=['Look', 'See', 'Watch'], t=T(2, 'Collocations with look, see, watch')),
                 dict(q='If I had better binoculars, I ___ see the birds on that island.', o=['would', 'will', 'am'], t=T(2, '2nd Conditional')),
             ])],
         you=[]),
]

P3 = [
    dict(id='trophy', img='trophy', x=7, y=57.8, h=11, wall=0, name='a trophy', ask=WHAT,
         name_t=T(3, 'Sport phrases'),
         tasks=[dict(kind='choice', title='Этот кубок выиграла наша команда! Выбери более подходящий вариант', en='Choose the best answer.', items=[
             dict(q='Would you like to ___ our tennis club?', o=['join', 'enter', 'win'], t=T(3, 'Sport phrases')),
             dict(q='___ is my favourite sport — I won this trophy last year.', o=['Swimming', 'Swim', 'To swimming'], t=T(3, 'Ing forms')),
             dict(q='I’m really good at ___ penalties.', o=['scoring', 'score', 'to score'], t=T(3, 'Ing forms')),
             dict(q='Nick ___ like snowboarding, but now he loves it.', o=['didn’t use to', 'doesn’t used to', 'not used to'], t=T(3, 'Used to')),
         ])],
         you=[]),
    dict(id='stethoscope', img='stethoscope', x=89.3, y=57.8, h=9, wall=0, name='a stethoscope', ask=WHAT, name_t=[],
         tasks=[dict(kind='choice', title='Ты на приёме у врача. Выбери верный вариант', en='Choose the best answer.', items=[
             dict(q='I fell down the stairs and ___ my ankle.', o=['sprained', 'coughed', 'sneezed'], t=T(3, 'Health verbs')),
             dict(q='You ___ go to bed earlier. You look really tired.', o=['should', 'must to', 'have'], t=T(3, 'Modals of obligation and advice')),
         ])],
         you=[('What should people do to stay healthy? What do you do?', T(3, 'Modals of obligation and advice', 'Health verbs'))]),
    dict(id='microphone', img='microphone', x=14.4, y=58.3, h=10, wall=0, name='a microphone', ask=WHAT, name_t=[],
         tasks=[],
         you=[('What kind of music do you listen to? Have you ever been to a concert?', T(3, 'Music'))]),
    dict(id='smartphone', img='smartphone', x=21.1, y=59.4, h=8, wall=0, name='a smartphone', ask=WHAT,
         name_t=T(3, 'Social media'),
         tasks=[dict(kind='choice', title='Anna выложила в сеть фото заката. Выбери верный вариант', en='Choose the right answer.', items=[
             dict(q='When Emma saw the photo, Jess ___ a comment under it.', o=['had already left', 'has already left', 'already leaves'], t=T(3, 'Past Perfect')),
             dict(q='“Let’s record a video together!” → Anna ___ recording a video together.', o=['suggested', 'told', 'agreed'], t=T(3, ('Reporting verbs', 4))),
             dict(q='Jess ___ Emma that Anna could be a great photographer.', o=['told', 'said', 'spoke'], t=T(3, 'Verbs of communication')),
             dict(q='Anna’s phone screen was broken, so ___ yesterday.', o=['she had it repaired', 'she had repaired it', 'she have it repair'], t=T(3, 'Causative have')),
         ])],
         you=[]),
    dict(id='graduation_cap', img='graduation_cap', x=96, y=58.5, h=6, wall=0, name='a graduation cap', ask=WHAT,
         name_t=T(3, 'Education'),
         tasks=[dict(kind='choice', title='Школа и университет. Выбери верный вариант', en='Choose the right answer.', items=[
             dict(q='Do you know where the exam room ___ ?', o=['is', 'is it', 'does'], t=T(3, 'Question forms (complex)')),
             dict(q='Our school is believed ___ more than 200 years ago.', o=['to have been built', 'to build', 'building'], t=T(3, 'Passive: complex forms')),
             dict(q='I get ___ really well with my classmates.', o=['on', 'up', 'off'], t=T(3, 'Phrasal verbs for relationships')),
         ])],
         you=[('Do you know what you would like to study in the future? Why?', T(3, 'Education', 'Question forms (complex)'))]),
    dict(id='seismograph', img='seismograph', x=81.1, y=57.8, h=9, wall=0, name='a seismograph', ask=WHAT,
         name_t=T(3, 'Natural disasters'),
         tasks=[
             dict(kind='match', title='Сейсмограф следит за природой. Соедини слова с картинками', en='Match the words and the pictures.', items=[
                 dict(w='a volcanic eruption', img='dis_volcano', t=T(3, 'Natural disasters')),
                 dict(w='a flood', img='dis_flood', t=T(3, 'Natural disasters')),
                 dict(w='an earthquake', img='dis_earthquake', t=T(3, 'Natural disasters')),
             ]),
             dict(kind='choice', title='Выбери верный вариант', en='Choose the right answer.', items=[
                 dict(q='When the volcano erupted, most people ___ escape in time.', o=['were able to', 'could to', 'can'], t=T(3, 'Modals of ability and possibility')),
             ])],
         you=[('What could you do to stay safe in an earthquake?', T(3, 'Modals of ability and possibility'))]),
    dict(id='magnifying_glass', img='magnifying_glass', x=27.8, y=63.3, h=8, wall=0, name='a magnifying glass', ask=WHAT,
         name_t=T(3, ('Crime and criminals', 5)),
         tasks=[dict(kind='choice', title='Ты детектив. Посмотри на место кражи и выбери верный вариант', en='Look and choose.', image='crime_scene', items=[
             dict(q='The broken glass is inside the room. The thief ___ through the window.', o=['must have come', 'can’t have come', 'must come'], t=T(3, 'Modals of deduction in the past')),
             dict(q='“Where were you last night?” → The detective asked me where I ___ the night before.', o=['had been', 'have been', 'was being'], t=T(3, 'Reported questions and requests')),
             dict(q='“I didn’t take the money!” → The suspect ___ taking the money.', o=['denied', 'admitted', 'suggested'], t=T(3, ('Reporting verbs', 5))),
             dict(q='If the window had been locked, the thief ___ in.', o=['wouldn’t have got', 'won’t get', 'didn’t get'], t=T(3, '3d conditional')),
             dict(q='The owner always tells the truth. She is very ___ .', o=['honest', 'selfish', 'lazy'], t=T(3, 'Personal qualities')),
             dict(q='A person who breaks into a house and steals things is a ___ .', o=['burglar', 'witness', 'judge'], t=T(3, ('Crime and criminals', 5))),
         ])],
         you=[]),
    dict(id='scroll', img='scroll', x=8.5, y=96.7, h=13, wall=0, name='a scroll', ask=WHAT,
         name_t=T(3, 'History'),
         tasks=[dict(kind='choice', title='История свитка. Выбери верный вариант', en='Choose the right answer.', items=[
             dict(q='An old man ___ along the beach when he found an ancient scroll.', o=['was walking', 'walked', 'has walked'], t=T(3, 'Narrative tenses')),
             dict(q='The people in the scroll fought for ___ .', o=['freedom', 'free', 'freely'], t=T(3, 'Abstract nouns')),
             dict(q='When I was little, my grandfather ___ tell me stories about our ancestors.', o=['would', 'will', 'was'], t=T(3, 'Present and past habits')),
         ])],
         you=[('What did your grandparents use to do when they were young?', T(3, 'Present and past habits'))]),
    dict(id='time_capsule', img='time_capsule', x=32.2, y=95.6, h=9, wall=0, name='a time capsule', ask=WHAT,
         name_t=T(3, 'Hopes and dreams'),
         tasks=[dict(kind='choice', title='Загляни в будущее и выбери верный вариант', en='Look and choose.', items=[
             dict(img='fut_travel', q='This time next week Mia ___ to London.', o=['will be flying', 'will have flown', 'flies'], t=T(3, 'Future Continuous and perfect')),
             dict(img='fut_graduation', q='By the end of the year they ___ from university.', o=['will have graduated', 'will be graduate', 'graduated'], t=T(3, 'Future Continuous and perfect')),
         ])],
         you=[]),
    dict(id='billboard', img='billboard', x=70.7, y=96.7, h=17, wall=0, name='a billboard', ask=WHAT,
         name_t=T(3, 'Advertising'),
         tasks=[
             dict(kind='match', title='Это слоганы с рекламных щитов. Собери половинки предложений', en='Match the halves.', halves=True, items=[
                 dict(w='This new phone is great, but it costs', d='an arm and a leg.', t=T(3, 'Idioms')),
                 dict(w='Our new board game will help you break', d='the ice at any party!', t=T(3, 'Idioms')),
                 dict(w='The company could have chosen', d='a better slogan for this advert.', t=T(3, 'Modals in the past')),
                 dict(w='If I hadn’t seen that advert,', d='I wouldn’t be wearing these trainers now.', t=T(3, '3d and mixed Conditionals')),
             ]),
             dict(kind='choice', title='Про рекламу. Выбери слово (— значит без артикля)', en='Choose the right word.', items=[
                 dict(q='This is ___ best advert of the year!', o=['the', 'a', '—'], t=T(3, 'Determiners')),
                 dict(q='It’s ___ advert for a new electric car.', o=['an', 'a', 'the'], t=T(3, 'Determiners')),
                 dict(q='This advert asks us to stop ___ — the air in our city is dirty.', o=['pollution', 'poverty', 'honesty'], t=T(3, 'Global issues')),
                 dict(q='You can ___ the new series online — no need to download it.', o=['stream', 'print', 'post'], t=T(3, 'Online, films and media')),
             ])],
         you=[('Have you ever bought something because of an advert? If you hadn’t seen it, would you have bought it?', T(3, '3d and mixed Conditionals'))]),
]

PARTS = [
    dict(n=1, room='room1_living', room_name='🛋 The Living Room', digits=4, objects=P1,
         intro=('Ты заперт в квест-комнате WowSpeak! Дверь закрыта на кодовый замок. '
                'В комнате спрятаны кусочки старой записки с кодом. Найди их — нажимай на предметы!'),
         intro_en='You are locked in the WowSpeak Escape Room! Find the pieces of the secret note to open the door.'),
    dict(n=2, room='room2_study', room_name='📚 The Secret Study', digits=2, objects=P2,
         intro=('Смотри — стена сдвинулась! За ней тайный кабинет. Здесь спрятана ещё одна записка.'),
         intro_en='Look — the wall is moving! There is a secret study behind it.'),
    dict(n=3, room='room3_lab', room_name='🧪 The Secret Lab', digits=2, objects=P3,
         intro=('В кабинете нашёлся люк на чердак. Там — тайная лаборатория и последняя записка.'),
         intro_en='There is a secret door to the attic. Welcome to the secret lab!'),
]

FLAGS = {'it': 'Italy', 'jp': 'Japan', 'fr': 'France', 'de': 'Germany', 'es': 'Spain'}

FAMILY = [  # портреты семьи для схемы family_tree: (картинка, имя, кто)
    ('fam_grandfather', 'George', 'grandfather'), ('fam_grandmother', 'Rose', 'grandmother'),
    ('fam_uncle', 'Bob', 'uncle'), ('fam_father', 'Mark', 'father'), ('fam_mother', 'Kate', 'mother'),
    ('fam_aunt', 'Lily', 'aunt'), ('fam_boy', 'Tom', 'Tom, 14'), ('fam_girl', 'Emma', 'Emma, 10'),
]

# одинаковые темы в разных частях/блоках получают балл друг от друга (решение Анны 13.11)
def topic_names():
    return {tid(p['part'], bi, ti): t for p in CHECKLIST for bi, (_, ts) in enumerate(p['blocks'], 1) for ti, t in enumerate(ts, 1)}
