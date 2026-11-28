# -*- coding: utf-8 -*-
"""Go Getter 3, юнит 6 «Cooking and eating» по рабочей тетради (стр. 50–56).

Ключи 6.7 — Answer key тетради (стр. 95); ключи аудирования 6.6 — по расшифровке
трека A15: подростковый телеповар готовит зимний куриный суп (одна курица, три
картофелины, одна луковица, два литра воды, варить тридцать минут, кости вынуть,
воду оставить, в конце — блендер).
"""
import io, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import (AUDIO, privet, poka, kartochki, kviz, pary, propuski, gruppy,
                    predlozheniya, vpisat, govorenie, pismo, tekst, sql_uroka)

UNIT = 'a4f27767-6f35-491b-8def-f7efd9caacee'   # Unit 6 · Cooking and eating
TEST = 'e6eeecd4-070f-4818-9cfb-cdc837c7361c'
TRACK15 = AUDIO + 'GG%20L3%20WkBk%20A15.mp3'


def so_zvukom(blok, url):
    """Прикрепляет запись к самому заданию (правило «запись — в задании»)."""
    blok[1]['audio'] = url
    blok[1]['skill'] = 'listening'
    return blok


# ─────────────────────── ДЗ 1 · 6.1 Vocabulary ───────────────────────
SLOVA = [
    ('peel', 'чистить от кожуры'), ('chop', 'нарезать кубиками'),
    ('slice', 'нарезать ломтиками'), ('add', 'добавлять'),
    ('mix', 'смешивать'), ('beat', 'взбивать'),
    ('bake', 'печь в духовке'), ('boil', 'варить в воде'),
    ('fry', 'жарить на масле'), ('roast', 'запекать мясо в духовке'),
    ('a pot', 'кастрюля'), ('a frying pan', 'сковорода'),
    ('a cake tin', 'форма для выпечки'), ('a bowl', 'миска'),
]

hw1 = [
    privet(0, 'Unit 6 · Cooking and eating',
           'Сегодня — кухня: что с едой делают и чем это делают.'),
    kartochki('Повторяем слова урока. Нажми на карточку — услышишь слово и увидишь перевод', SLOVA),
    pary('Соедини глагол с его значением', [
        ('chop', 'cut food into small pieces'),
        ('boil', 'cook food in water'),
        ('fry', 'cook food in butter or oil'),
        ('roast', 'cook meat in the oven'),
        ('beat', 'mix eggs fast with a fork'),
        ('peel', 'cut off the skin of an apple'),
    ]),
    propuski('Прочитай рецепт яблочно-морковного пирога и перетащи слова в пропуски',
             "Today I'm making an apple carrot cake. Look, it's easy! "
             "First, peel the apples and the carrots.\n"
             "Then __chop__ the apples and the carrots.\n"
             "Next __add__ sugar, two eggs and flour to the butter.\n"
             "The apples and carrots are in the bowl now. It's time to __mix__ everything with a spoon.\n"
             "__Bake__ the cake in the oven for 45 minutes.\n"
             "Here is my apple carrot cake. __Slice__ it and give everyone some cake!",
             mode='drag'),
    propuski('Впиши глагол: bake · beat · boil · fry · roast',
             "You can mix strawberries and yoghurt for a nice snack.\n"
             "Some people always __roast__ chicken and potatoes in the oven on Sundays.\n"
             "You can __fry__ eggs in butter for a hot breakfast.\n"
             "You can eat carrots in salad or __boil__ them in water for a hot meal.\n"
             "It's fun to learn with Mum how to __bake__ biscuits in the oven.\n"
             "You have to __beat__ eggs first to make an omelette."),
    kviz('Прочитай рецепт пасты с курицей и выбери правильное слово', [
        ('First slice or chop the chicken and put it in a ___.', ['bowl', 'pot'], 0),
        ('Choose the pasta you like and boil it in water in a big ___.', ['pot', 'frying pan'], 0),
        ('Then fry the chicken in some butter in a ___.', ['cake tin', 'frying pan'], 1),
        ('Add some cheese and cream to the chicken and ___ them all together.',
         ['mix', 'peel'], 0),
        ('Put the pasta in a ___ and the chicken on top. Enjoy!', ['bowl', 'cake tin'], 0),
    ]),
    vpisat('Прочитай, что делают с продуктом, и напиши глагол по-английски', [
        ('onions and carrots — режут кубиками (ch…)', ['chop', 'Chop', 'to chop']),
        ('eggs and rice — варят в воде (b…)', ['boil', 'Boil', 'to boil']),
        ('cheese and bread — режут ломтиками (s…)', ['slice', 'Slice', 'to slice']),
        ('fish and pancakes — жарят на масле (f…)', ['fry', 'Fry', 'to fry']),
        ('cake and biscuits — пекут в духовке (b…)', ['bake', 'Bake', 'to bake']),
    ]),
    poka(0, 'Готово! Теперь кухня тебе по-английски понятна.'),
]

# ─────────────────────── ДЗ 2 · 6.2 Present Perfect ───────────────────────
hw2 = [
    privet(1, 'Unit 6 · Present Perfect', 'Сегодня — что уже сделано, а что ещё нет.'),
    pary('Соедини глагол с его третьей формой (Past Participle)', [
        ('eat', 'eaten'), ('chop', 'chopped'), ('drink', 'drunk'),
        ('buy', 'bought'), ('make', 'made'), ('bring', 'brought'),
    ]),
    gruppy('Распредели посуду по назначению', [
        ('🥤 из этого пьют', ['a cup', 'a mug', 'a glass']),
        ('🍴 этим едят', ['a fork', 'a knife', 'a spoon']),
        ('🍽 на это кладут еду', ['a plate', 'a bowl']),
    ]),
    propuski('Прочитай разговор Эммы с бабушкой и перетащи отрицательную форму в пропуск',
             "Emma: I want to make a chocolate cake, but the chef hasn't put any nice recipes "
             "on my favourite cooking blog.\n"
             "Gran: There's a good chocolate cake recipe in my cookbook. But, oh dear. "
             "Harry __hasn't bought__ any chocolate!\n"
             "Emma: Hmm. I __haven't looked__ at your cookbook. Is there a lemon cake recipe in it?\n"
             "Gran: Let's look. Yes, there's a recipe on page 12. We __haven't made__ it yet, "
             "but it looks nice. Let's try it.\n"
             "Emma: OK. We need two lemons, three eggs, some flour, butter and sugar.\n"
             "Ten minutes later …\n"
             "Emma: OK. The cake is in the oven.\n"
             "Gran: Oh dear! We __haven't added__ the lemon juice!\n"
             "Emma: Don't worry! Let's put some jam on the cake.",
             mode='drag'),
    predlozheniya('Составь предложения про сегодняшний день в Present Perfect', [
        ('мама приготовила пиццу', 'Mum has made pizza.'),
        ('я не убрал свою комнату', "I haven't tidied my room."),
        ('папа поставил кружки не в тот шкаф', 'Dad has put the mugs in the wrong cupboard.'),
        ('мы съели весь торт', 'We have eaten all the cake.'),
    ]),
    propuski('Впиши глагол в Present Perfect: полная форма has/have + третья форма',
             "I have finished (finish) my soup. Can I have some more, please?\n"
             "This is Fred's plate. He __has eaten__ (eat) all his food.\n"
             "Oh, there isn't any water in the cat's bowl. It __has drunk__ (drink) it all.\n"
             "We __have chopped__ (chop) all the vegetables, Mum. Now what do we do?\n"
             "You __have boiled__ (boil) the water, so now you can add the pasta.\n"
             "Look, everyone! I __have brought__ (bring) a dessert. It's chocolate ice cream!"),
    pismo('WRITING ✍️ Напиши, что ты уже сделал сегодня',
          '<p>Напиши три предложения в Present Perfect — правдиво про себя.</p>'
          '<ol><li>do my homework → I …</li>'
          '<li>write a text on my phone → I …</li>'
          '<li>send me an email → My friend …</li></ol>'
          '<p>Если что-то ещё не сделано, пиши отрицание: <b>I haven\'t …</b></p>'),
    poka(1, 'Present Perfect разобран: has/have и третья форма глагола.'),
]

# ─────────────────────── ДЗ 3 · 6.3 Вопросы, ever и never ───────────────────────
hw3 = [
    privet(2, 'Unit 6 · Вопросы в Present Perfect',
           'Сегодня — как спросить «ты когда-нибудь…?» и как коротко ответить.'),
    kviz('Прочитай разговор Энди и Беллы и выбери короткий ответ', [
        ('Andy: Have you ever made popcorn? — Bella: Yes, ___.', ['I have', 'it has'], 0),
        ('Andy: Have your friends ever eaten your dishes? — Bella: Yes, ___.',
         ['you have', 'they have'], 1),
        ('Andy: Have you ever tried banana cookies? — Bella: No, ___.',
         ["you haven't", "I haven't"], 1),
        ('Andy: Has your pet ever eaten chicken ice cream? — Bella: No, ___.',
         ["it hasn't", "they haven't"], 0),
        ('Andy: Have you ever won a cooking competition? — Bella: Yes, ___.',
         ["I haven't", 'I have'], 1),
    ]),
    predlozheniya('Составь вопросы для Дэйва из списка дел к ужину', [
        ('ты купил напитки?', 'Have you bought the drinks?'),
        ('Джон помыл овощи?', 'Has John washed the vegetables?'),
        ('мы купили достаточно пасты?', 'Have we bought enough pasta?'),
        ('твои тёти привезли десерт?', 'Have your aunts brought the dessert?'),
    ]),
    propuski('Впиши слова, чтобы получился вопрос и короткий ответ (bake · use · watch)',
             "Has Doctor Q made pancakes for everyone? Yes, he has. ✔\n"
             "__Have__ Millie and Rob __baked__ a cake? Yes, they __have__. ✔\n"
             "__Has__ Millie __used__ all the sugar? No, she __hasn't__. ✘\n"
             "__Have__ Pi and Doctor Q __watched__ their show on TV? No, they __haven't__. ✘"),
    propuski('Прочитай разговоры и впиши по одному слову в каждый пропуск',
             "A: Have you ever baked biscuits?\n"
             "B: No, I haven't. I've __never__ baked anything!\n"
             "A: Has Dave __ever__ won a football competition?\n"
             "B: Yes, I think he __has__. He's the best footballer in the school.\n"
             "A: Have __you__ ever eaten at that restaurant?\n"
             "B: __No__, I haven't. Is the food nice there?\n"
             "A: __Has__ your mum ever tried Chinese food?\n"
             "B: No, she hasn't. She __has__ never eaten at a Chinese restaurant."),
    pismo('WRITING ✍️ Напиши вопросы и правдивые короткие ответы',
          '<p>Прочитай предложение и составь к нему вопрос с <b>ever</b>, '
          'а потом ответь правдиво про себя.</p>'
          '<ol><li>I\'ve never won a competition. → Have you ever …?</li>'
          '<li>My best friend has cooked at my house. → Has your best friend ever …?</li>'
          '<li>I\'ve never drunk fresh lemonade. → Have you ever …?</li></ol>'),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи, что ты когда-нибудь готовил или пробовал, а чего не пробовал никогда. '
              'Три-четыре предложения с <b>ever</b> и <b>never</b>.</p>',
              "I have never eaten a samosa."),
    poka(2, 'Теперь ты умеешь спрашивать про опыт и коротко отвечать.'),
]

# ─────────────────────── ДЗ 4 · 6.4 Communication ───────────────────────
TEKSTY = (
    '<p><b>Beth:</b> I like picnics at the park. People usually have sandwiches at picnics, '
    "but I don't like them. I prefer pizza! I don't mind what I drink. I like cola or water. "
    'My best friend, Jess, likes playing badminton at picnics. I prefer volleyball.</p>'
    '<p><b>John:</b> I like picnics at the park or on the beach. My good friend, Matt, says '
    'lemonade is the best picnic drink, but I prefer cola. I like sandwiches. And my favourite '
    'sport at picnics? Yes, I like playing football at picnics, but I prefer volleyball.</p>'
)

hw4 = [
    privet(0, 'Unit 6 · Что ты предпочитаешь',
           'Сегодня — как спросить о предпочтениях и как ответить на такой вопрос.'),
    pary('Соедини начало и конец фразы', [
        ('Would you like chips', 'or rice?'),
        ('Would you like to', 'play football or video games?'),
        ('Would you', 'like tea or coffee?'),
        ("I'd", 'like tea.'),
        ("I'd prefer", 'chips.'),
        ("I don't", 'mind.'),
    ]),
    kviz('Прочитай, что рассказали Бет и Джон, и выбери правильный ответ', [
        ('Where does Beth like having picnics?',
         ['at the park', 'on the beach', 'at home'], 0),
        ('What food does Beth prefer at picnics?',
         ['sandwiches', 'pizza', 'fish and chips'], 1),
        ('What does Beth say about drinks?',
         ["She doesn't mind.", 'She prefers lemonade.', 'She only drinks water.'], 0),
        ('Which sport does Beth prefer?', ['badminton', 'volleyball', 'football'], 1),
        ('What does John prefer to drink?', ['lemonade', 'cola', 'water'], 1),
        ('Which sport does John prefer?', ['football', 'volleyball', 'badminton'], 1),
    ], material=TEKSTY),
    predlozheniya('Составь фразы про предпочтения', [
        ('спроси, что он хочет: чай или кофе', 'Would you like tea or coffee?'),
        ('скажи, что предпочитаешь пиццу', "I'd prefer pizza."),
        ('скажи, что тебе всё равно', "I don't mind."),
        ('спроси, хочет ли он пойти на пляж', 'Would you like to go to the beach?'),
    ]),
    propuski('Прочитай разговор Джона и Бет и впиши по одному слову в каждый пропуск',
             "John: Would you like to have a picnic at the park or on the __beach__?\n"
             "Beth: __I'd__ like to have a picnic at the __park__.\n"
             "John: OK. __Would__ you __like__ sandwiches or pizza at the picnic?\n"
             "Beth: I'd prefer __pizza__.\n"
             "John: Cool. What about drinks? Would you like cola or water?\n"
             "Beth: I don't __mind__. You __choose__. Would you like to play football or "
             "volleyball at the picnic?\n"
             "John: I'd like to play __volleyball__.\n"
             "Beth: Me too."),
    pismo('WRITING ✍️ Запиши разговор в кафе',
          '<p>Вы с мамой в кафе и хотите что-нибудь сладкое: капкейк или шоколадное мороженое. '
          'Запиши разговор из четырёх реплик.</p>'
          '<p>Мама спрашивает про выбор, ты отвечаешь, что предпочитаешь, мама спрашивает про '
          'напиток, ты говоришь, что тебе всё равно.</p>'),
    govorenie('SPEAKING 🎤 Разыграй разговор и запиши ответ',
              '<p>Вы с другом на отдыхе и выбираете, чем заняться: покататься на каяке по озеру '
              'или поплавать в озере. Спроси друга о его выборе, скажи, что предпочитаешь ты, '
              'и почему.</p>',
              "Would you like to go for a bike ride or go to the beach?"),
    poka(3, 'Отлично! Теперь ты умеешь выбирать и спрашивать о выборе.'),
]

# ─────────────────────── ДЗ 5 · 6.5 Reading ───────────────────────
RASSKAZ = (
    '<h3>Pies from around the world <span style="color:#888">by Sasha</span></h3>'
    '<p>People make pies all around the world. Here are my favourite pies.</p>'
    "<p><b>1</b> I'm English and I like our traditional apple pie. It's a sweet pie and it's a "
    'popular dessert.</p>'
    '<p><b>2</b> Another sweet pie is pumpkin pie from America. Pumpkins are vegetables, but they '
    'add sugar to this pie, so it is sweet. I usually have apple pie and pumpkin pie with sour '
    'cream, but you can have ice cream as well.</p>'
    "<p><b>3</b> Not all pies are sweet. My best friend's mum is from Ukraine and she makes a "
    'delicious Ukrainian fish pie. She mixes fish, boiled eggs and rice and puts them in the pie.</p>'
    '<p><b>4</b> Another pie is quiche. This is an open pie from France and it has fish or meat in '
    "it with eggs, cheese and vegetables. You can eat hot or cold quiche, so it's great for picnics.</p>"
    "<p><b>5</b> In Greece they make little pies for snacks. The best pies are the little cheese "
    "pies – I've eaten them for breakfast there.</p>"
    '<p><b>6</b> The last pie on my list is an Indian spicy pie – a samosa. It has vegetables and '
    'sometimes meat in it. My brother has never tried them. He thinks samosas are disgusting '
    "because he doesn't like spicy food, but I love them!</p>"
)

hw5 = [
    privet(1, 'Unit 6 · Reading', 'Сегодня читаем блог Саши про пироги разных стран.'),
    tekst(RASSKAZ),
    pary('Соедини пирог со страной, откуда он', [
        ('apple pie', 'England'),
        ('pumpkin pie', 'America'),
        ('fish pie', 'Ukraine'),
        ('quiche', 'France'),
        ('little cheese pies', 'Greece'),
        ('samosas', 'India'),
    ]),
    kviz('Прочитай блог ещё раз и реши: верно, неверно или в тексте этого нет', [
        ('Sasha is from America.', ['Верно', 'Неверно', 'В тексте этого нет'], 1),
        ("Apple pies aren't popular desserts.", ['Верно', 'Неверно', 'В тексте этого нет'], 1),
        ('Pumpkin pie has sugar in it.', ['Верно', 'Неверно', 'В тексте этого нет'], 0),
        ("Sasha's best friend makes fish pies.", ['Верно', 'Неверно', 'В тексте этого нет'], 1),
        ('In Greece, Sasha has had a pie for breakfast.',
         ['Верно', 'Неверно', 'В тексте этого нет'], 0),
        ("Sasha's brother has never eaten spicy food.",
         ['Верно', 'Неверно', 'В тексте этого нет'], 2),
    ], material=RASSKAZ),
    propuski('Впиши слово: delicious · disgusting · salty · sour · spicy',
             "Chocolate ice cream is sweet because it has lots of sugar in it.\n"
             "I love fish pie. It's __delicious__!\n"
             "Dad adds chilli to chicken, so it is __spicy__.\n"
             "Don't try the pumpkin ice cream – it's __disgusting__! Yuk!\n"
             "Is it really apple pie? I think it's lemon pie – it's very __sour__.\n"
             "__Salty__ popcorn is my favourite snack."),
    govorenie('SPEAKING 🎤 Ответь вслух и запиши ответ',
              '<p>Ответь на вопросы по блогу Саши:</p>'
              '<ol><li>Which pie would you like to try? Why?</li>'
              '<li>What is your favourite pie? Where is it from?</li>'
              '<li>Do you prefer fish or meat pies? Why?</li>'
              '<li>Have you ever eaten quiche?</li></ol>',
              "My favourite pie is a cherry pie and it is from my grandma's kitchen."),
    poka(4, 'Блог прочитан — и про пироги мира ты теперь знаешь.'),
]

# ─────────────────────── ДЗ 6 · 6.6 Listening and Writing ───────────────────────
hw6 = [
    privet(2, 'Unit 6 · Listening and Writing',
           'Сегодня слушаем рецепт от телеповара и пишем свой.'),
    kviz('Прочитай описание блюда и выбери, как оно называется', [
        ('Fish with chips and green peas on a plate.',
         ['Chicken soup', 'Fish and chips', 'Chicken pie and chips'], 1),
        ('Chicken, potatoes, onion and water — everything goes in the blender.',
         ['Chicken soup', 'Fish and chips', 'Chicken pie and chips'], 0),
        ('A hot pie with chicken inside and chips next to it.',
         ['Chicken soup', 'Fish and chips', 'Chicken pie and chips'], 2),
    ]),
    ('quiz', {'title': 'LISTENING 🎧 Послушай рецепт телеповара и выбери правильный ответ',
              'audio': TRACK15, 'skill': 'listening',
              'questions': [
                  {'q': 'Which meal is the chef preparing?', 'type': 'single', 'correct': [0],
                   'options': [{'text': 'chicken soup'}, {'text': 'fish and chips'},
                               {'text': 'chicken pie and chips'}]},
                  {'q': 'How many potatoes do you need?', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'two'}, {'text': 'three'}, {'text': 'four'}]},
                  {'q': 'How much water do you need?', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'one litre'}, {'text': 'two litres'},
                               {'text': 'three litres'}]},
                  {'q': 'How long do you boil the chicken?', 'type': 'single', 'correct': [2],
                   'options': [{'text': 'fifteen minutes'}, {'text': 'twenty minutes'},
                               {'text': 'thirty minutes'}]},
                  {'q': 'What do you do when the chicken is ready?', 'type': 'single',
                   'correct': [0],
                   'options': [{'text': 'You take the bones out of the meat.'},
                               {'text': 'You throw the water away.'},
                               {'text': 'You put the chicken in the oven.'}]},
                  {'q': 'What do you use at the end?', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'a frying pan'}, {'text': 'a blender'},
                               {'text': 'a cake tin'}]},
              ]}),
    so_zvukom(propuski('LISTENING 🎧 Послушай рецепт ещё раз и перетащи слова в пропуски',
                       "Ingredients:\n"
                       "one chicken\n"
                       "__three__ potatoes\n"
                       "one __onion__\n"
                       "__two__ litres of water\n"
                       "salt and pepper\n"
                       "some __oil__\n"
                       "Instructions:\n"
                       "Cut the chicken in pieces.\n"
                       "Boil the chicken for thirty minutes.\n"
                       "Take the bones out of the __meat__.\n"
                       "Keep the __water__.\n"
                       "Peel and chop the vegetables.\n"
                       "Fry the onion in oil.\n"
                       "Add the vegetables to the chicken and water.\n"
                       "Cook for __thirty__ minutes and then blend in the blender.\n"
                       "Add some salt and pepper.", mode='drag'), TRACK15),
    kviz('Прочитай рецепт французских тостов из блога бабушки и выбери правильный вариант. '
         'В рецептах пишут командами: Slice the bread.', [
        ('Two slices of bread, one egg, one cup of milk, some honey. Как называется этот список?',
         ['Ingredients', 'Instructions'], 0),
        ('You ___ need: a frying pan, a fork, a spoon.', ['also', 'never'], 0),
        ('Slice the bread. Break the egg into a bowl. Как называется этот список?',
         ['Ingredients', 'Instructions'], 1),
        ('___ the bread.', ['Slice', 'You slice'], 0),
        ('___ the egg into a bowl.', ['Break', 'Broke'], 0),
        ('___ the milk and mix.', ['It adds', 'Add'], 1),
        ('___ the toast on a plate and put a spoonful of honey on the toast.',
         ['You put', 'Put'], 1),
    ]),
    pismo('WRITING ✍️ Напиши свой рецепт перекуса с хлебом',
          '<p>Сначала составь заметки: продукты (<i>some bread, …</i>), что ещё нужно '
          '(<i>a knife, …</i>) и что делать (<i>slice the bread, …</i>).</p>'
          '<p>Потом напиши рецепт по образцу французских тостов: список продуктов, '
          'список нужных вещей и инструкции командами (Beat the eggs and sugar.).</p>'
          '<p>Начни так: <i>Ingredients: …</i></p>'),
    poka(5, 'И рецепт на слух понят, и свой записан.'),
]

# ─────────────────────── ДЗ 7 · 6.7 Check yourself ───────────────────────
hw7 = [
    privet(0, 'Unit 6 · Check yourself!', 'Повторяем весь юнит перед тестом.'),
    kviz('Прочитай рецепт традиционного английского воскресного обеда и выбери правильное слово', [
        ('First peel the potatoes. Then ___ the chicken and the potatoes in the oven for two hours.',
         ['bake', 'roast'], 1),
        ('___ the carrots.', ['Slice', 'Fry'], 0),
        ('Always use a sharp ___. Be careful.', ['cup', 'knife'], 1),
        ('___ the vegetables for fifteen minutes.', ['Boil', 'Mix'], 0),
        ('Add salt and pepper and your ___ meal is ready! Yum yum!',
         ['awful', 'delicious'], 1),
    ]),
    pary('Соедини вопрос с ответом', [
        ('Have you ever made pizza?', 'Yes, I have! I love Italian food.'),
        ('Have your parents ever won anything?', "No, they haven't."),
        ('Has Fred bought a new phone?', "No. He hasn't got enough money."),
        ("Have you tried Grandma's apple pie?", "Yes, we have. It's very good."),
        ('Have you and Jack finished your meal?', "No, Dad. We're still eating."),
    ]),
    kviz('Прочитай разговоры и выбери правильный вариант', [
        ('A: ___ like a hot drink?', ['Would you', 'You would'], 0),
        ('B: ___ something cold, please.', ['I like', "I'd like"], 1),
        ('A: Would you like to watch TV ___ a DVD?', ['or', 'and'], 0),
        ("B: I'd ___ watch TV.", ['prefer to', 'prefer'], 0),
        ('A: Would you like to go to the park or ___ to the beach?', ['go', 'going'], 0),
        ("B: I don't ___.", ['choose', 'mind'], 1),
    ]),
    propuski('Прочитай разговор мамы и Дэна и впиши пропущенное слово',
             "Mum: Can you set the table, please? We need knives and forks for everyone.\n"
             "Dan: OK. What about __spoons__ for soup?\n"
             "Mum: Yes, and we also need __bowls__ to put the soup in and plates for the fish pie.\n"
             "Dan: Fish pie? Oh! I love fish pie. But please don't make it __spicy__, Mum. "
             "I don't like chilli.\n"
             "Mum: There isn't any chilli in the pie! And there's something __sweet__ for dessert.\n"
             "Dan: Great! What are we drinking? Do we need big or small __glasses__?\n"
             "Mum: Big please. I've bought some lemonade."),
    propuski('Впиши глагол в Present Perfect',
             "We have made (make) popcorn for everyone!\n"
             "Dad __has bought__ (buy) some yummy bananas!\n"
             "My friends __haven't brought__ (not bring) a cake for my birthday – "
             "it's a big pizza! It smells great.\n"
             "__Has Doug tried__ (Doug / try) a fish pie?\n"
             "I __have chopped__ (chop) the tomatoes for the salad.\n"
             "__Have you watched__ (you / watch) this cooking competition on TV? "
             "Let's watch it. It's great!"),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи про блюдо, которое ты уже готовил сам: что это было, что ты делал '
              'с продуктами и каким оно получилось на вкус. Четыре-пять предложений.</p>',
              'I have cooked pancakes with my dad and they were delicious.'),
    poka(1, 'Юнит пройден! Можно браться за тест.'),
]

UROKI = [('Homework 1', hw1), ('Homework 2', hw2), ('Homework 3', hw3), ('Homework 4', hw4),
         ('Homework 5', hw5), ('Homework 6', hw6), ('Homework 7', hw7)]

if __name__ == '__main__':
    put = sys.argv[1] if len(sys.argv) > 1 else 'builds/gg3/wb/u6/u6.sql'
    out = ['-- Go Getter 3, юнит 6 «Cooking and eating» по рабочей тетради: домашки 1–7 (черновики)',
           f"update classroom_lessons set sort_order = 10 where id = '{TEST}';"]
    for i, (nazv, bloki) in enumerate(UROKI):
        out.append(sql_uroka(UNIT, nazv, i, bloki))
    io.open(put, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(put, sum(len(b) for _, b in UROKI), 'блоков,', os.path.getsize(put) // 1024, 'КБ')
