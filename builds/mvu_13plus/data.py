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
# Предмет: id, img, x/y/h — где стоит в комнате (в % от ширины/высоты сцены, h — высота в % высоты),
# name — что ученик должен назвать, name_t — тема лексики, ask — что спрашивает менеджер,
# tasks — задания, you — вопросы «And you?» (каждый со своей темой).

P1 = [
    dict(id='family_photo', img='family_photo', x=84, y=50, h=12, wall=0, name='a family photo', ask="What's this?",
         name_t=T(1, 'Families'),
         tasks=[dict(kind='family', title='Посмотри на семью Тома и выбери верный вариант', items=[
             dict(q='Emma is Tom’s ___ .', o=['sister', 'brother', 'aunt'], t=T(1, 'Families')),
             dict(q='Rose is Tom’s ___ .', o=['grandmother', 'mother', 'aunt'], t=T(1, 'Families')),
             dict(q='Bob is Emma’s ___ .', o=['uncle', 'father', 'grandfather'], t=T(1, 'Families')),
             dict(q='Tom ___ fourteen.', o=['is', 'are', 'am'], t=T(1, 'To be')),
             dict(q='Mark and Kate ___ Tom’s parents.', o=['are', 'is', 'am'], t=T(1, 'To be')),
         ])],
         you=[('Tell me about your family. How many people are there in your family?', T(1, 'Families', 'To be'))]),
    dict(id='schoolbag', img='schoolbag', x=30.7, y=88, h=19, wall=0, name='a schoolbag (a backpack)', ask="What's this?",
         name_t=T(1, 'School objects'),
         tasks=[dict(kind='choice', title='Это рюкзак Тома. Посмотри, что в нём лежит, и выбери верный вариант', image='schoolbag_open', items=[
             dict(q='There ___ two pens.', o=['are', 'is', 'am'], t=T(1, 'There is')),
             dict(q='There ___ a calculator.', o=['isn’t', 'aren’t', 'is'], t=T(1, 'There is')),
             dict(q='Tom has got a ___ and a notebook.', o=['ruler', 'rubber', 'calculator'], t=T(1, 'School objects')),
             dict(q='___ Tom got a book? — No, he hasn’t.', o=['Has', 'Have', 'Is'], t=T(1, 'Have got')),
             dict(q='Tom ___ got a pencil case.', o=['has', 'have', 'is'], t=T(1, 'Have got')),
         ])],
         you=[('What have you got in your school bag?', T(1, 'Have got', 'School objects'))]),
    dict(id='passport', img='passport', x=41, y=68, h=5, wall=0, name='a passport', ask="What's this?",
         name_t=T(1, 'Countries'),
         tasks=[dict(kind='choice', title='Это паспорта друзей Тома. Посмотри на флаг и выбери верный вариант', items=[
             dict(flag='it', q='Where is Marco from? He’s from ___ .', o=['Italy', 'Spain', 'France'], t=T(1, 'Countries')),
             dict(flag='jp', q='Where is Yuki from? She’s from ___ .', o=['Japan', 'China', 'Germany'], t=T(1, 'Countries')),
             dict(flag='fr', q='Claire is from France. She’s ___ .', o=['French', 'France', 'Frenchy'], t=T(1, 'Countries')),
             dict(flag='de', q='Hans is from Germany. He’s ___ .', o=['German', 'Germany', 'Germanish'], t=T(1, 'Countries')),
             dict(flag='es', q='Where ___ Lucia and Pablo from? — They’re from Spain.', o=['are', 'is', 'am'], t=T(1, 'To be')),
         ])],
         you=[('Where are you from? Which country would you like to visit?', T(1, 'Countries', 'To be'))]),
    dict(id='fruit_bowl', img='fruit_bowl', x=50, y=68.3, h=9, wall=0, name='fruit (a bowl of fruit)', ask="What's this?",
         name_t=T(1, 'Food and drinks'),
         tasks=[dict(kind='tf', title='Фрукты есть в вазе, а что есть в холодильнике у Тома? Верно или неверно?', image='fridge_open', items=[
             dict(q='There is some milk in the fridge.', a=True, t=T(1, 'Some, any, lots of')),
             dict(q='There are lots of eggs in the fridge.', a=True, t=T(1, 'Some, any, lots of')),
             dict(q='There isn’t any cheese in the fridge.', a=False, fix='There is some cheese in the fridge.', t=T(1, 'Some, any, lots of')),
             dict(q='There are three tomatoes in the fridge.', a=True, t=T(1, 'Food and drinks')),
             dict(q='There is some juice in the fridge.', a=False, fix='There isn’t any juice in the fridge.', t=T(1, 'Some, any, lots of')),
             dict(q='There are some apples in the fridge.', a=False, fix='There aren’t any apples in the fridge — they are in the bowl.', t=T(1, 'Food and drinks')),
         ])],
         you=[('What do you usually have for breakfast?', T(1, 'Food and drinks', 'Present Simple'))]),
    dict(id='football', img='football', x=21, y=96.6, h=11, wall=0, name='a football (a ball)', ask="What's this?",
         name_t=T(1, 'Sports'),
         tasks=[
             dict(kind='hotspot', title='Это Том, он играет в футбол. Что показывает стрелка? Выбери слово', image='athlete',
                  words=['head', 'arm', 'hand', 'knee', 'foot', 'leg'], items=[
                      dict(x=48, y=6, a='head', t=T(1, 'Body parts')),
                      dict(x=10, y=36, a='arm', t=T(1, 'Body parts')),
                      dict(x=10, y=56, a='hand', t=T(1, 'Body parts')),
                      dict(x=33, y=71, a='knee', t=T(1, 'Body parts')),
                      dict(x=80, y=94, a='foot', t=T(1, 'Body parts')),
                  ]),
             dict(kind='choice', title='Том очень любит спорт. Посмотри на картинку и выбери верный вариант', items=[
                 dict(img='athlete', q='Tom ___ football with his friends after school.', o=['plays', 'play', 'playing'], t=T(1, 'Present Simple')),
                 dict(img='sport_swim', q='Can Tom swim? — Yes, he ___ .', o=['can', 'can’t', 'is'], t=T(1, 'Can/Can’t')),
                 dict(img='sport_tennis', q='Tom ___ tennis every Saturday.', o=['plays', 'play', 'playing'], t=T(1, 'Present Simple')),
                 dict(img='sport_bike', q='___ Tom ride a bike to school? — Yes, he does.', o=['Does', 'Do', 'Is'], t=T(1, 'Present Simple')),
                 dict(img='sport_tennis', q='Tom can play tennis, but he ___ play basketball. He doesn’t know how.', o=['can’t', 'can', 'don’t can'], t=T(1, 'Can/Can’t')),
             ])],
         you=[('What sports can you do? How often do you do sport?', T(1, 'Sports', 'Can/Can’t', 'Present Simple'))]),
    dict(id='bus', img='bus', x=93.5, y=50, h=6, wall=0, name='a bus', ask="What's this?",
         name_t=T(1, 'Transport'),
         tasks=[dict(kind='choice', title='Посмотри в окно и выбери верный вариант', image='street', items=[
             dict(q='The man on the bench is a ___ .', o=['bus driver', 'doctor', 'chef'], t=T(1, 'Jobs')),
             dict(q='Look! He ___ a sandwich now.', o=['is eating', 'eats', 'eat'], t=T(1, 'Present Simple vs Present Continuous')),
             dict(q='He usually ___ the bus.', o=['drives', 'is driving', 'drive'], t=T(1, 'Present Simple vs Present Continuous')),
             dict(q='The woman on the bike is a ___ . She usually works in a hospital.', o=['doctor', 'chef', 'teacher'], t=T(1, 'Jobs')),
             dict(q='What’s on the bridge?', o=['a train', 'a taxi', 'a bus'], t=T(1, 'Transport')),
         ])],
         you=[('What are you doing now? What do your parents do?', T(1, 'Present Simple vs Present Continuous', 'Jobs'))]),
    dict(id='cinema_tickets', img='cinema_tickets', x=59.6, y=68, h=5, wall=0, name='cinema tickets', ask="What are these?",
         name_t=T(1, 'Entertainment'),
         tasks=[
             dict(kind='order', title='Том и его друзья любят кино. Собери предложения', items=[
                 dict(s='I always go to the cinema on Fridays.', t=T(1, 'Adverbs of frequency')),
                 dict(s='We often watch films at the weekend.', t=T(1, 'Adverbs of frequency')),
             ]),
             dict(kind='choice', title='У Тома два билета в кино. Выбери верный вариант', items=[
                 dict(q='— Let’s go to the cinema tonight! — ___', o=['Good idea! What film?', 'Yes, I am.', 'I go.'], t=T(1, 'Let’s…')),
                 dict(q='Let’s ___ a film at home.', o=['watch', 'watching', 'to watch'], t=T(1, 'Let’s…')),
                 dict(q='Where can you watch a new film on a big screen?', o=['at the cinema', 'at the library', 'at the hospital'], t=T(1, 'Entertainment')),
             ])],
         you=[('How often do you go to the cinema? What do you like doing at the weekend?', T(1, 'Adverbs of frequency', 'Entertainment'))]),
    dict(id='umbrella', img='umbrella', x=82, y=93, h=16, wall=0, name='an umbrella', ask="What's this?",
         name_t=T(1, 'Weather'),
         tasks=[
             dict(kind='choice', title='Какая погода? Выбери верный вариант', items=[
                 dict(img='w_snowy', q='What’s the weather like?', o=['It’s snowy.', 'It’s sunny.', 'It’s windy.'], t=T(1, 'Weather')),
                 dict(img='w_windy', q='What’s the weather like?', o=['It’s windy.', 'It’s rainy.', 'It’s hot.'], t=T(1, 'Weather')),
             ]),
             dict(kind='sort', title='Завтра едем на море: солнечно и жарко ☀️ Что берём, а что оставляем?', image='w_sunny',
                  groups=['Take ✅', 'Don’t take ❌'], items=[
                      dict(w='shorts', img='cl_shorts', g=0, t=T(1, 'Clothes')),
                      dict(w='a swimsuit', img='cl_swimsuit', g=0, t=T(1, 'Clothes')),
                      dict(w='sandals', img='cl_sandals', g=0, t=T(1, 'Clothes')),
                      dict(w='sunglasses', img='cl_sunglasses', g=0, t=T(1, 'Clothes')),
                      dict(w='a coat', img='cl_coat', g=1, t=T(1, 'Clothes')),
                      dict(w='a scarf', img='cl_scarf', g=1, t=T(1, 'Clothes')),
                      dict(w='gloves', img='cl_gloves', g=1, t=T(1, 'Clothes')),
                      dict(w='a woolly hat', img='cl_hat', g=1, t=T(1, 'Clothes')),
                  ]),
             dict(kind='choice', title='Зачем Тому зонтик? Выбери верный вариант', items=[
                 dict(q='It’s raining. I ___ an umbrella.', o=['need', 'needs', 'am need'], t=T(1, 'Need, want')),
                 dict(q='It’s sunny today. I ___ to go to the beach!', o=['want', 'wants', 'wanting'], t=T(1, 'Need, want')),
             ])],
         you=[('What’s the weather like today? What do you need for a trip to the mountains?', T(1, 'Weather', 'Need, want', 'Clothes'))]),
    dict(id='cat', img='cat', x=66.3, y=96.6, h=17, wall=0, name='a cat', ask="What's this?",
         name_t=T(1, 'Pets and farm animals'),
         tasks=[
             dict(kind='choice', title='Это кошка Тома, а летом он ездит на ферму к бабушке. Посмотри на животных и выбери верный вариант', items=[
                 dict(img2=['an_horse', 'an_cat'], q='A horse is ___ than a cat.', o=['bigger', 'big', 'biggest'], t=T(1, 'Comparatives')),
                 dict(img2=['an_cat', 'an_dog'], q='Tom’s cat is ___ than his dog.', o=['smaller', 'small', 'more small'], t=T(1, 'Comparatives')),
                 dict(img2=['an_cow', 'an_pig', 'an_chicken'], q='Which animal gives us milk?', o=['a cow', 'a pig', 'a chicken'], t=T(1, 'Pets and farm animals')),
             ]),
             dict(kind='listen', title='Голосовое сообщение про ферму, где живут животные. Послушай и ответь на вопросы', audio='p1_voicemail',
                  text=('Hi, it’s me, the Quest Master! Yesterday I visited my grandparents’ farm. '
                        'In the morning I fed the chickens and the sheep. Then I rode a horse! '
                        'I didn’t see the pigs, because they were asleep. '
                        'In the evening we had a big dinner and watched a film. It was a great day!'),
                  items=[
                      dict(q='Where did the Quest Master go yesterday?', o=['to a farm', 'to the cinema', 'to school'], t=T(1, 'Past Simple')),
                      dict(q='What did he ride?', o=['a horse', 'a bike', 'a bus'], t=T(1, 'Past Simple')),
                      dict(q='Did he see the pigs?', o=['No, he didn’t.', 'Yes, he did.', 'No, he don’t.'], t=T(1, 'Past Simple')),
                      dict(q='What did they do in the evening?', o=['They watched a film.', 'They played football.', 'They went to bed.'], t=T(1, 'Past Simple')),
                  ])],
         you=[('What did you do last weekend? Have you got a pet?', T(1, 'Past Simple', 'Pets and farm animals'))]),
]

P2 = [
    dict(id='wardrobe', img='wardrobe', x=89.3, y=77.8, h=40, wall=0, name='a wardrobe — + 2 adjectives (a big wooden wardrobe)', ask="What's this? Describe it.",
         name_t=T(2, 'Household and furniture', 'Adjectives to describe objects'),
         tasks=[
             dict(kind='sort', title='Что в шкафу, что рядом и какой он? Разложи слова по группам', groups=['Clothes', 'Furniture', 'Describing objects'], items=[
                 dict(w='a hoodie', g=0, t=T(2, 'Clothes')), dict(w='trainers', g=0, t=T(2, 'Clothes')),
                 dict(w='a jacket', g=0, t=T(2, 'Clothes')), dict(w='jeans', g=0, t=T(2, 'Clothes')),
                 dict(w='a sofa', g=1, t=T(2, 'Household and furniture')), dict(w='a shelf', g=1, t=T(2, 'Household and furniture')),
                 dict(w='an armchair', g=1, t=T(2, 'Household and furniture')), dict(w='a chest of drawers', g=1, t=T(2, 'Household and furniture')),
                 dict(w='wooden', g=2, t=T(2, 'Adjectives to describe objects')), dict(w='plastic', g=2, t=T(2, 'Adjectives to describe objects')),
                 dict(w='huge', g=2, t=T(2, 'Adjectives to describe objects')), dict(w='round', g=2, t=T(2, 'Adjectives to describe objects')),
             ]),
             dict(kind='choice', title='Загляни в шкаф и выбери верный вариант', items=[
                 dict(q='There aren’t ___ clothes in the wardrobe.', o=['many', 'much', 'a'], t=T(2, 'Quantifiers (some, any, a lot of)')),
                 dict(q='There isn’t ___ space in the wardrobe. It’s full!', o=['much', 'many', 'a few'], t=T(2, 'Quantifiers (some, any, a lot of)')),
                 dict(q='My sister keeps ___ shoes in this wardrobe — more than fifty pairs!', o=['a lot of', 'much', 'any'], t=T(2, 'Quantifiers (some, any, a lot of)')),
             ])],
         you=[('Describe your room. What furniture is there?', T(2, 'Household and furniture', 'Adjectives to describe objects'))]),
    dict(id='suitcase', img='suitcase', x=48.5, y=98, h=14, wall=0, name='a suitcase', ask="What's this? Describe it.",
         name_t=T(2, 'Holidays'),
         tasks=[
             dict(kind='choice', title='Это чемодан Mia — она вернулась из отпуска. Как она себя чувствовала?', items=[
                 dict(img='hol_airport', q='At the airport Mia was ___ .', o=['bored', 'excited', 'relaxed'], t=T(2, 'Emotions')),
                 dict(img='hol_castle', q='At the castle she was ___ .', o=['excited', 'bored', 'angry'], t=T(2, 'Emotions')),
                 dict(img='hol_beach', q='On the beach she felt ___ .', o=['relaxed', 'scared', 'bored'], t=T(2, 'Emotions')),
             ]),
             dict(kind='tf', title='Это рассказ Mia об отпуске. Верно построено предложение? Если нет — исправь вслух', items=[
                 dict(q='Last summer we goed to Spain.', a=False, fix='Last summer we went to Spain.', t=T(2, 'Past Simple irregulars and Regulars')),
                 dict(q='Our flight was late, so we waited for three hours.', a=True, t=T(2, 'Past Simple irregulars and Regulars')),
                 dict(q='Look at this photo! Here I take a photo of the castle.', a=False, fix='Here I’m taking a photo of the castle.', t=T(2, 'Present Simple vs Present Continuous')),
                 dict(q='We usually go on holiday in August.', a=True, t=T(2, 'Present Simple vs Present Continuous')),
                 dict(q='We booked a hotel and went sightseeing every day.', a=True, t=T(2, 'Holidays')),
             ])],
         you=[('Tell me about your best trip. Where did you go? How did you feel?', T(2, 'Holidays', 'Past Simple irregulars and Regulars', 'Emotions'))]),
    dict(id='map', img='map', x=32.2, y=27.8, h=13, wall=1, name='a map', ask="What's this? Describe it.",
         name_t=T(2, 'Geographical features'),
         tasks=[
             dict(kind='match', title='Что есть на карте? Соедини слова с картинками', items=[
                 dict(w='a river', img='geo_river', t=T(2, 'Geographical features')),
                 dict(w='a desert', img='geo_desert', t=T(2, 'Geographical features')),
                 dict(w='a waterfall', img='geo_waterfall', t=T(2, 'Geographical features')),
                 dict(w='an island', img='geo_island', t=T(2, 'Geographical features')),
                 dict(w='go sightseeing', img='tr_sightseeing', t=T(2, 'Travelling activities')),
                 dict(w='go camping', img='tr_camping', t=T(2, 'Travelling activities')),
             ]),
             dict(kind='choice', title='Это карта путешествий. Выбери верный вариант', items=[
                 dict(img='tr_ferry', q='We crossed the sea ___ .', o=['by ferry', 'on foot', 'by bike'], t=T(2, 'Ways of travelling')),
                 dict(img='geo_mountains', q='Next summer we ___ climb these mountains. We’ve already bought the tickets.', o=['are going to', 'might', 'will can'], t=T(2, 'Going to')),
                 dict(q='I’m not sure, but I ___ go to Italy next year.', o=['might', 'am going to', 'must'], t=T(2, 'Future with will, may, might')),
                 dict(q='Look at the map! I think we ___ need two days to get to the island.', o=['will', 'are', 'did'], t=T(2, 'Future with will, may, might')),
             ])],
         you=[('What are you going to do this summer? Where would you like to travel?', T(2, 'Going to', 'Travelling activities'))]),
    dict(id='first_aid_kit', img='first_aid_kit', x=9.3, y=67.8, h=9, wall=0, name='a first-aid kit', ask="What's this? Describe it.",
         name_t=T(2, 'Health and Illnesses'),
         tasks=[dict(kind='choice', title='Разговор у врача. Выбери верный вариант', items=[
             dict(q='— What’s the matter? — I’ve got a ___ . I ate too much.', o=['stomachache', 'stomach', 'hurt'], t=T(2, 'Health and Illnesses')),
             dict(q='I fell off my bike and now my ___ hurts. I can’t walk.', o=['ankle', 'elbow', 'chin'], t=T(2, 'Body parts')),
             dict(q='You ___ stay in bed for two days.', o=['must', 'mustn’t', 'don’t have to'], t=T(2, 'Modals of obligation (must, have to)')),
             dict(q='It’s Saturday tomorrow — you ___ go to school.', o=['don’t have to', 'have to', 'mustn’t to'], t=T(2, 'Have to/Don’t have to')),
             dict(q='Do you ___ take this medicine every day?', o=['have to', 'must to', 'has to'], t=T(2, 'Have to/Don’t have to')),
         ])],
         you=[('What do you have to do at home? What must students do at your school?', T(2, 'Have to/Don’t have to', 'Modals of obligation (must, have to)'))]),
    dict(id='novel', img='novel', x=31.5, y=71, h=5.5, wall=0, name='a book (a novel)', ask="What's this? Describe it.",
         name_t=T(2, 'Free time activities: books and films'),
         tasks=[dict(kind='choice', title='Это отзыв о книге. Выбери верный вариант', items=[
             dict(q='This book ___ by a 15-year-old girl.', o=['was written', 'wrote', 'is writing'], t=T(2, 'Present Simple and Past Simple Passive')),
             dict(q='I love it! I ___ it three times.', o=['have read', 'am reading', 'reads'], t=T(2, 'Present Perfect')),
             dict(q='Kate and Sam are best friends, but then they ___ in love.', o=['fall', 'get', 'make'], t=T(2, 'Relationships')),
             dict(q='If you like adventures, you ___ love it.', o=['will', 'would', 'are'], t=T(2, '1st Conditional')),
             dict(q='A story about the future, robots and space is ___ .', o=['science fiction', 'a comedy', 'a documentary'], t=T(2, 'Free time activities: books and films')),
         ])],
         you=[('What’s the best book or film you’ve ever read or seen? Why do you like it?', T(2, 'Present Perfect', 'Free time activities: books and films'))]),
    dict(id='wanted_poster', img='wanted_poster', x=50, y=55.6, h=13, wall=1, name='a poster (a wanted poster)', ask="What's this? Describe it.",
         name_t=T(2, 'Crime and criminals'),
         tasks=[dict(kind='listen', title='Голосовое сообщение! Послушай и найди вора', audio='p2_voicemail', suspects=True,
                     text=('Hello, it’s the Quest Master again. Last night somebody broke into the museum and stole a famous painting. '
                           'A witness saw the thief. He was tall, with curly dark hair and a beard, and he was wearing glasses '
                           'and a black leather jacket. When the police arrived, he was running to his car.'),
                     items=[
                         dict(q='Who is the thief?', suspect=True, t=T(2, 'Describing people')),
                         dict(q='What did the thief steal?', o=['a painting', 'some money', 'a phone'], t=T(2, 'Crime and criminals')),
                         dict(q='What was he doing when the police arrived?', o=['He was running to his car.', 'He runs to his car.', 'He is running to his car.'], t=T(2, ('Past Continuous', 3))),
                         dict(q='A person who saw the crime is a ___ .', o=['witness', 'thief', 'judge'], t=T(2, 'Crime and criminals')),
                     ]),
                dict(kind='choice', title='Что было в музее той ночью? Выбери верный вариант', items=[
                    dict(q='The thief ___ the painting when the alarm rang.', o=['was taking', 'took', 'is taking'], t=T(2, 'Past continuous vs Past Simple')),
                    dict(q='At midnight the guard ___ in his chair.', o=['was sleeping', 'sleeps', 'is sleeping'], t=T(2, ('Past Continuous', 4))),
                ])],
         you=[('Describe someone in your family. What does he or she look like?', T(2, 'Describing people'))]),
    dict(id='wallet', img='wallet', x=22.5, y=60.5, h=5, wall=0, name='a wallet', ask="What's this? Describe it.",
         name_t=T(2, 'Money and shopping'),
         tasks=[dict(kind='choice', title='Что купили на эти деньги? Выбери верный вариант', items=[
             dict(q='Look! I’ve just ___ these trainers. They were in the sale!', o=['bought', 'buy', 'buying'], t=T(2, 'Present Perfect vs Past Simple')),
             dict(q='I ___ a new phone last week.', o=['bought', 'have bought', 'buy'], t=T(2, 'Present Perfect vs Past Simple')),
             dict(q='I ___ my friends at the shopping centre at 5 tomorrow — it’s all arranged.', o=['am meeting', 'meet', 'met'], t=T(2, 'Be going to vs Present Continuous for future')),
             dict(q='When something is cheaper than usual, it’s on ___ .', o=['sale', 'sell', 'price'], t=T(2, 'Money and shopping')),
             dict(q='You pay at the ___ .', o=['checkout', 'menu', 'pocket'], t=T(2, 'Money and shopping')),
         ])],
         you=[('What are you doing this weekend? What did you buy last time you went shopping?', T(2, 'Be going to vs Present Continuous for future', 'Money and shopping'))]),
    dict(id='laptop', img='laptop', x=18.1, y=69.4, h=11, wall=0, name='a laptop', ask="What's this? Describe it.",
         name_t=T(2, 'Computer phrases'),
         tasks=[
             dict(kind='choice', title='Включаем ноутбук. Выбери верный вариант', items=[
                 dict(q='First, ___ in with your password.', o=['log', 'click', 'type'], t=T(2, 'Computer phrases')),
                 dict(q='___ on the link to open the page.', o=['Click', 'Log', 'Download'], t=T(2, 'Computer phrases')),
             ]),
             dict(kind='tf', title='Это переписка в чате. Верно построено предложение? Если нет — исправь вслух', items=[
                 dict(q='Tom said that he is tired.', a=False, fix='Tom said that he was tired.', t=T(2, 'Reported speech')),
                 dict(q='She told me she had downloaded the game.', a=True, t=T(2, 'Reported speech')),
                 dict(q='The boy which lives next door is my friend.', a=False, fix='The boy who lives next door is my friend.', t=T(2, 'Relative clauses')),
                 dict(q='This is the app that I told you about.', a=True, t=T(2, 'Relative clauses')),
             ])],
         you=[('What do you usually do on your computer or phone?', T(2, 'Computer phrases'))]),
    dict(id='binoculars', img='binoculars', x=28.5, y=62, h=6, wall=0, name='binoculars', ask="What are these? Describe them.",
         name_t=T(2, 'Collocations with look, see, watch'),
         tasks=[
             dict(kind='match', title='Посмотри в бинокль на кафе напротив. Какая там еда на вкус? Соедини слово с блюдом', items=[
                 dict(w='spicy', img='food_spicy', t=T(2, 'Food and drink adjectives')),
                 dict(w='crunchy', img='food_crunchy', t=T(2, 'Food and drink adjectives')),
                 dict(w='sour', img='food_sour', t=T(2, 'Food and drink adjectives')),
                 dict(w='sweet', img='food_sweet', t=T(2, 'Food and drink adjectives')),
                 dict(w='bitter', img='food_bitter', t=T(2, 'Food and drink adjectives')),
                 dict(w='salty', img='food_salty', t=T(2, 'Food and drink adjectives')),
             ]),
             dict(kind='choice', title='Что можно делать с биноклем? Выбери верный вариант', items=[
                 dict(q='___ at that bird! It’s huge!', o=['Look', 'See', 'Watch'], t=T(2, 'Collocations with look, see, watch')),
                 dict(q='Can you ___ the castle from here?', o=['see', 'look', 'watch'], t=T(2, 'Collocations with look, see, watch')),
                 dict(q='We sat on the hill to ___ the sunset through the binoculars.', o=['watch', 'look', 'see at'], t=T(2, 'Collocations with look, see, watch')),
                 dict(q='If I had better binoculars, I ___ see the birds on that island.', o=['would', 'will', 'am'], t=T(2, '2nd Conditional')),
             ])],
         you=[('If you had binoculars, what would you like to watch?', T(2, '2nd Conditional', 'Collocations with look, see, watch'))]),
]

P3 = [
    dict(id='trophy', img='trophy', x=7, y=57.8, h=11, wall=0, name='a trophy — and what it is for', ask="What's this? What is it for?",
         name_t=T(3, 'Sport phrases'),
         tasks=[dict(kind='choice', title='Этот кубок выиграла наша команда! Выбери более подходящий вариант', items=[
             dict(q='Would you like to ___ our tennis club? 🎾', o=['join', 'enter', 'win'], t=T(3, 'Sport phrases')),
             dict(q='Have you ever ___ a goal in a real match? ⚽', o=['scored', 'won', 'given'], t=T(3, 'Sport phrases')),
             dict(q='___ is my favourite sport — I won this trophy last year. 🏊', o=['Swimming', 'Swim', 'To swimming'], t=T(3, 'Ing forms')),
             dict(q='I’m really good at ___ penalties. ⚽', o=['scoring', 'score', 'to score'], t=T(3, 'Ing forms')),
             dict(q='Nick ___ like snowboarding, but now he loves it. 🏂', o=['didn’t use to', 'doesn’t used to', 'not used to'], t=T(3, 'Used to')),
         ])],
         you=[('What did you use to do when you were a child that you don’t do now?', T(3, 'Used to'))]),
    dict(id='stethoscope', img='stethoscope', x=89.3, y=57.8, h=9, wall=0, name='a stethoscope — and what it is for', ask="What's this? What is it for?",
         name_t=T(3, 'Health verbs'),
         tasks=[dict(kind='choice', title='Ты на приёме у врача. Выбери верный вариант', items=[
             dict(q='If your nose starts to ___ , you should put your head forward. 👃', o=['bleed', 'ache', 'burn'], t=T(3, 'Health verbs')),
             dict(q='I fell down the stairs and ___ my ankle.', o=['sprained', 'coughed', 'sneezed'], t=T(3, 'Health verbs')),
             dict(q='You ___ go to bed earlier. You look really tired.', o=['should', 'must to', 'have'], t=T(3, 'Modals of obligation and advice')),
             dict(q='Stop! You ___ drink this water — it’s dirty! 🚱', o=['mustn’t', 'don’t have to', 'needn’t'], t=T(3, 'Modals of obligation and advice')),
         ])],
         you=[('What should people do to stay healthy? What do you do?', T(3, 'Modals of obligation and advice', 'Health verbs'))]),
    dict(id='microphone', img='microphone', x=14.4, y=58.3, h=10, wall=0, name='a microphone — and what it is for', ask="What's this? What is it for?",
         name_t=T(3, 'Music'),
         tasks=[dict(kind='match', title='Это микрофон с концерта. Соедини слова про музыку с определениями', defs=True, items=[
             dict(w='lyrics', d='the words of a song', t=T(3, 'Music')),
             dict(w='a sound technician', d='a person who controls the sound at a concert', t=T(3, 'Music')),
             dict(w='a concert hall', d='a big building where people listen to live music', t=T(3, 'Music')),
             dict(w='a band', d='a group of musicians who play together', t=T(3, 'Music')),
             dict(w='an album', d='a collection of songs released together', t=T(3, 'Music')),
         ])],
         you=[('What kind of music do you listen to? Have you ever been to a concert?', T(3, 'Music'))]),
    dict(id='smartphone', img='smartphone', x=21.1, y=59.4, h=8, wall=0, name='a smartphone — and what it is for', ask="What's this? What is it for?",
         name_t=T(3, 'Social media'),
         tasks=[
             dict(kind='listen', title='Голосовое сообщение! Послушай историю и ответь на вопросы', audio='p3_voicemail',
                  text=('Emma and Jess are best friends. Yesterday Emma saw a photo that Anna had posted online. '
                        'Anna had taken it at sunset, and it was amazing. Jess had already seen it and had left a comment under it. '
                        'She told Emma that Anna could be a great photographer. When Anna read the comments, she laughed '
                        'and suggested recording a video together. Jess agreed, and they decided to meet on Sunday, '
                        'because Jess doesn’t like putting things off.'),
                  items=[
                      dict(q='What had Anna done before she suggested recording a video?', o=['She had posted a photo online.', 'She had recorded a video.', 'She had met Jess at school.'], t=T(3, 'Past Perfect')),
                      dict(q='What had Jess done under the photo?', o=['She had left a comment.', 'She had deleted it.', 'She had taken another photo.'], t=T(3, 'Social media')),
                      dict(q='What did Anna suggest?', o=['recording a video together', 'going to the cinema', 'taking more photos'], t=T(3, ('Reporting verbs', 4))),
                      dict(q='Jess ___ Emma that Anna could be a great photographer.', o=['told', 'said', 'spoke'], t=T(3, 'Verbs of communication')),
                  ]),
             dict(kind='choice', title='Ещё немного про телефон Анны. Выбери верный вариант', items=[
                 dict(q='Anna’s phone screen was broken, so ___ yesterday.', o=['she had it repaired', 'she had repaired it', 'she have it repair'], t=T(3, 'Causative have')),
                 dict(q='Anna hopes ___ a famous photographer one day.', o=['to become', 'becoming', 'become'], t=T(3, 'Hopes and dreams')),
             ])],
         you=[('Have you ever had something repaired or done for you? What do you hope to achieve this year?', T(3, 'Causative have', 'Hopes and dreams'))]),
    dict(id='graduation_cap', img='graduation_cap', x=96, y=58.5, h=6, wall=0, name='a graduation cap — and what it is for', ask="What's this? What is it for?",
         name_t=T(3, 'Education'),
         tasks=[dict(kind='choice', title='Это шапка выпускника. Выбери верный вариант', items=[
             dict(q='She ___ from university last year and now she works as a lawyer.', o=['graduated', 'passed', 'failed'], t=T(3, 'Education')),
             dict(q='Do you know where the exam room ___ ?', o=['is', 'is it', 'does'], t=T(3, 'Question forms (complex)')),
             dict(q='Could you tell me what time the lesson ___ ?', o=['starts', 'does start', 'start'], t=T(3, 'Question forms (complex)')),
             dict(q='Our school is believed ___ more than 200 years ago.', o=['to have been built', 'to build', 'building'], t=T(3, 'Passive: complex forms')),
             dict(q='I get ___ really well with my classmates.', o=['on', 'up', 'off'], t=T(3, 'Phrasal verbs for relationships')),
             dict(q='We fell ___ last week, but now we’re friends again.', o=['out', 'down', 'off'], t=T(3, 'Phrasal verbs for relationships')),
         ])],
         you=[('Do you know what you would like to study in the future? Why?', T(3, 'Education', 'Question forms (complex)'))]),
    dict(id='seismograph', img='seismograph', x=81.1, y=57.8, h=9, wall=0, name='a seismograph — and what it is for', ask="What's this? What is it for?",
         name_t=T(3, 'Natural disasters'),
         tasks=[
             dict(kind='match', title='Сейсмограф следит за природой. Соедини слова с картинками', items=[
                 dict(w='a volcanic eruption', img='dis_volcano', t=T(3, 'Natural disasters')),
                 dict(w='a flood', img='dis_flood', t=T(3, 'Natural disasters')),
                 dict(w='an earthquake', img='dis_earthquake', t=T(3, 'Natural disasters')),
                 dict(w='a wildfire', img='dis_wildfire', t=T(3, 'Natural disasters')),
                 dict(w='a hurricane', img='dis_hurricane', t=T(3, 'Natural disasters')),
                 dict(w='a tsunami', img='dis_tsunami', t=T(3, 'Natural disasters')),
             ]),
             dict(kind='choice', title='Сейсмограф записал землетрясение. Выбери верный вариант', items=[
                 dict(img='dis_earthquake', q='During the earthquake the old building ___ .', o=['collapsed', 'erupted', 'flooded'], t=T(3, 'Natural disasters')),
                 dict(q='Nobody ___ predict exactly when an earthquake will happen.', o=['can', 'may to', 'is able'], t=T(3, 'Modals of ability and possibility')),
                 dict(q='When the volcano erupted, most people ___ escape in time.', o=['were able to', 'could to', 'can'], t=T(3, 'Modals of ability and possibility')),
             ])],
         you=[('What could you do to stay safe in an earthquake?', T(3, 'Modals of ability and possibility'))]),
    dict(id='magnifying_glass', img='magnifying_glass', x=27.8, y=63.3, h=8, wall=0, name='a magnifying glass — and what it is for', ask="What's this? What is it for?",
         name_t=T(3, ('Crime and criminals', 5)),
         tasks=[dict(kind='choice', title='Ты детектив 🕵️ Посмотри на место кражи и выбери верный вариант', image='crime_scene', items=[
             dict(q='The broken glass is inside the room. The thief ___ through the window.', o=['must have come', 'can’t have come', 'must come'], t=T(3, 'Modals of deduction in the past')),
             dict(q='The door is locked with a chain. The thief ___ through the door.', o=['can’t have come', 'must have come', 'mustn’t come'], t=T(3, 'Modals of deduction in the past')),
             dict(q='The dog didn’t bark. The thief ___ the dog.', o=['must have known', 'can’t have known', 'must know'], t=T(3, 'Modals of deduction in the past')),
             dict(q='“Where were you last night?” → The detective asked me where I ___ the night before.', o=['had been', 'have been', 'was being'], t=T(3, 'Reported questions and requests')),
             dict(q='“I didn’t take the money!” → The suspect ___ taking the money.', o=['denied', 'admitted', 'suggested'], t=T(3, ('Reporting verbs', 5))),
             dict(q='If the window had been locked, the thief ___ in.', o=['wouldn’t have got', 'won’t get', 'didn’t get'], t=T(3, '3d conditional')),
             dict(q='The owner always tells the truth. She is very ___ .', o=['honest', 'selfish', 'lazy'], t=T(3, 'Personal qualities')),
             dict(q='A person who breaks into a house and steals things is a ___ .', o=['burglar', 'witness', 'judge'], t=T(3, ('Crime and criminals', 5))),
         ])],
         you=[('What would you have done if you had been the detective?', T(3, '3d conditional'))]),
    dict(id='scroll', img='scroll', x=8.5, y=96.7, h=13, wall=0, name='a scroll — and what it is for', ask="What's this? What is it for?",
         name_t=T(3, 'History'),
         tasks=[
             dict(kind='sort', title='Это древний свиток. Распредели слова из него по темам', groups=['History 🏛', 'Abstract nouns 💭'], items=[
                 dict(w='ancestor', g=0, t=T(3, 'History')), dict(w='century', g=0, t=T(3, 'History')),
                 dict(w='myth', g=0, t=T(3, 'History')), dict(w='inhabitants', g=0, t=T(3, 'History')),
                 dict(w='freedom', g=1, t=T(3, 'Abstract nouns')), dict(w='honesty', g=1, t=T(3, 'Abstract nouns')),
                 dict(w='happiness', g=1, t=T(3, 'Abstract nouns')), dict(w='knowledge', g=1, t=T(3, 'Abstract nouns')),
             ]),
             dict(kind='choice', title='История свитка. Выбери верный вариант', items=[
                 dict(q='An old man ___ along the beach when he found an ancient scroll.', o=['was walking', 'walked', 'has walked'], t=T(3, 'Narrative tenses')),
                 dict(q='Someone ___ it there many years before.', o=['had hidden', 'has hidden', 'hides'], t=T(3, 'Narrative tenses')),
                 dict(q='When I was little, my grandfather ___ tell me stories about our ancestors.', o=['would', 'will', 'was'], t=T(3, 'Present and past habits')),
                 dict(q='My grandmother ___ telling us this old legend — we know it by heart!', o=['is always', 'always is', 'was always being'], t=T(3, 'Present and past habits')),
             ])],
         you=[('What did your grandparents use to do when they were young?', T(3, 'Present and past habits'))]),
    dict(id='time_capsule', img='time_capsule', x=32.2, y=95.6, h=9, wall=0, name='a time capsule — and what it is for', ask="What's this? What is it for?",
         name_t=T(3, 'Hopes and dreams'),
         tasks=[dict(kind='choice', title='Загляни в будущее и выбери верный вариант', items=[
             dict(img='fut_travel', q='This time next week Mia ___ to London.', o=['will be flying', 'will have flown', 'flies'], t=T(3, 'Future Continuous and perfect')),
             dict(img='fut_graduation', q='By the end of the year they ___ from university.', o=['will have graduated', 'will be graduate', 'graduated'], t=T(3, 'Future Continuous and perfect')),
             dict(img='fut_doctor', q='By the time he is 30, Leo ___ as a doctor for five years.', o=['will have worked', 'will work', 'is working'], t=T(3, 'Future Continuous and perfect')),
             dict(img='fut_band', q='In four years this band ___ at the biggest stadiums.', o=['will be playing', 'will have play', 'is played'], t=T(3, 'Future Continuous and perfect')),
         ])],
         you=[('What will you have achieved by the end of this year?', T(3, 'Future Continuous and perfect', 'Hopes and dreams'))]),
    dict(id='billboard', img='billboard', x=70.7, y=96.7, h=17, wall=0, name='a billboard — and what it is for', ask="What's this? What is it for?",
         name_t=T(3, 'Advertising'),
         tasks=[
             dict(kind='sort', title='Что бывает на рекламных щитах? Распредели слова по темам', groups=['Advertising', 'Global issues', 'Online & media'], items=[
                 dict(w='a slogan', g=0, t=T(3, 'Advertising')), dict(w='a brand', g=0, t=T(3, 'Advertising')), dict(w='a commercial', g=0, t=T(3, 'Advertising')),
                 dict(w='pollution', g=1, t=T(3, 'Global issues')), dict(w='poverty', g=1, t=T(3, 'Global issues')), dict(w='climate change', g=1, t=T(3, 'Global issues')),
                 dict(w='to subscribe', g=2, t=T(3, 'Online, films and media')), dict(w='a podcast', g=2, t=T(3, 'Online, films and media')), dict(w='to stream', g=2, t=T(3, 'Online, films and media')),
             ]),
             dict(kind='match', title='Это слоганы с рекламных щитов. Собери половинки предложений', halves=True, items=[
                 dict(w='This new phone is great, but it costs', d='an arm and a leg.', t=T(3, 'Idioms')),
                 dict(w='Our new board game will help you break', d='the ice at any party!', t=T(3, 'Idioms')),
                 dict(w='The company could have chosen', d='a better slogan for this advert.', t=T(3, 'Modals in the past')),
                 dict(w='If I hadn’t seen that advert,', d='I wouldn’t be wearing these trainers now.', t=T(3, '3d and mixed Conditionals')),
             ]),
             dict(kind='choice', title='Про рекламу. Выбери артикль (— значит без артикля)', items=[
                 dict(q='This is ___ best advert of the year!', o=['the', 'a', '—'], t=T(3, 'Determiners')),
                 dict(q='It’s ___ advert for a new electric car.', o=['an', 'a', 'the'], t=T(3, 'Determiners')),
                 dict(q='___ people don’t always trust adverts on social media.', o=['—', 'The', 'A'], t=T(3, 'Determiners')),
             ])],
         you=[('Have you ever bought something because of an advert? If you hadn’t seen that advert, would you have bought it?', T(3, '3d and mixed Conditionals', 'Advertising'))]),
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

FAMILY = [  # семейное дерево задания family_photo: (картинка, имя, кто)
    ('fam_grandfather', 'George', 'grandfather'), ('fam_grandmother', 'Rose', 'grandmother'),
    ('fam_uncle', 'Bob', 'uncle'), ('fam_father', 'Mark', 'father'), ('fam_mother', 'Kate', 'mother'),
    ('fam_aunt', 'Lily', 'aunt'), ('fam_boy', 'Tom', 'Tom, 14'), ('fam_girl', 'Emma', 'Emma, 10'),
]


# короткая инструкция на английском — на экране; русский title — для учителя (в план)
EN = {
"family_photo#0": "Look and choose.",
"schoolbag#0": "Look and choose.",
"passport#0": "Look at the flag and choose.",
"fruit_bowl#0": "Look. True or false?",
"football#0": "Look and choose one word.",
"football#1": "Look and choose.",
"bus#0": "Look and choose.",
"cinema_tickets#0": "Put the words in order.",
"cinema_tickets#1": "Choose the right answer.",
"umbrella#0": "Look and choose.",
"umbrella#1": "What do you take? Sort.",
"umbrella#2": "Choose the right word.",
"cat#0": "Look and choose.",
"cat#1": "Listen and choose.",
"wardrobe#0": "Sort the words.",
"wardrobe#1": "Choose the right word.",
"suitcase#0": "Look. How did Mia feel?",
"suitcase#1": "Right or wrong? Correct the mistakes.",
"map#0": "Match the words and the pictures.",
"map#1": "Choose the right answer.",
"first_aid_kit#0": "Choose the right answer.",
"novel#0": "Choose the right answer.",
"wanted_poster#0": "Listen and find the thief.",
"wanted_poster#1": "Choose the right answer.",
"wallet#0": "Choose the right answer.",
"laptop#0": "Choose the right word.",
"laptop#1": "Right or wrong? Correct the mistakes.",
"binoculars#0": "Match the words and the pictures.",
"binoculars#1": "Choose the right word.",
"trophy#0": "Choose the best answer.",
"stethoscope#0": "Choose the best answer.",
"microphone#0": "Match the words and the definitions.",
"smartphone#0": "Listen and choose.",
"smartphone#1": "Choose the right answer.",
"graduation_cap#0": "Choose the right answer.",
"seismograph#0": "Match the words and the pictures.",
"seismograph#1": "Choose the right answer.",
"magnifying_glass#0": "Look and choose.",
"scroll#0": "Sort the words.",
"scroll#1": "Choose the right answer.",
"time_capsule#0": "Look and choose.",
"billboard#0": "Sort the words.",
"billboard#1": "Match the halves.",
"billboard#2": "Choose a, an, the or — ."
}
for _P in (P1, P2, P3):
    for _o in _P:
        for _i, _t in enumerate(_o['tasks']):
            _t['en'] = EN[f"{_o['id']}#{_i}"]
