# -*- coding: utf-8 -*-
"""Go Getter 3, юнит 2 «Shopping» по рабочей тетради (стр. 14–20) — семь домашек.

Разделы: 2.1 Vocabulary · 2.2 Grammar · 2.3 Grammar · 2.4 Communication ·
2.5 Reading · 2.6 Listening and Writing · 2.7 Check yourself.
Ключи 2.7 — по Answer key тетради (стр. 95), ключи аудирования 2.6 — по
расшифровке трека A5 (faster-whisper): наушники £30, фонарик £9,
телефон £200, фотоаппарат £70.
"""
import io, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import (AUDIO, privet, poka, kartochki, kviz, pary, propuski, gruppy,
                    predlozheniya, vpisat, govorenie, pismo, tekst, sql_uroka)

UNIT = 'f342c5ca-ce88-40dc-b97a-79032ef7a76f'   # Unit 2 · Shopping
TEST = 'ad6fefbc-b1f5-4acd-a6f7-d79cd15e6c88'

# ─────────────────────── ДЗ 1 · 2.1 Vocabulary ───────────────────────
SLOVA = [
    ('cashier', 'кассир'), ('shopping list', 'список покупок'),
    ('shopping trolley', 'тележка для покупок'), ('shopping basket', 'корзина для покупок'),
    ('shopping bag', 'сумка для покупок'), ('special offer', 'акция, скидка'),
    ('card', 'банковская карта'), ('cash', 'наличные'), ('change', 'сдача'),
    ('price', 'цена'), ('receipt', 'чек'), ('queue', 'очередь'),
]

hw1 = [
    privet(0, 'Unit 2 · Shopping', 'Сегодня — поход в магазин: как назвать всё по-английски и как заплатить.'),
    kartochki('Повторяем слова урока. Нажми на карточку — услышишь слово и увидишь перевод', SLOVA),
    pary('Соедини слово с объяснением', [
        ('cashier', 'the person who takes your money in a shop'),
        ('shopping list', 'the paper with the things you need to buy'),
        ('shopping trolley', 'you push it around the supermarket'),
        ('shopping basket', 'you carry it in your hand'),
        ('change', 'the money you get back after you pay'),
        ('receipt', 'the paper that shows how much you paid'),
        ('queue', 'the line of people waiting to pay'),
        ('special offer', 'a lower price for a short time'),
    ]),
    kviz('Прочитай предложение и выбери правильное слово', [
        ('My dad ___ the shopping home in a big shopping bag.', ['carries', 'checks'], 0),
        ('Would you like to pay in ___?', ['cash', 'card'], 0),
        ('When I pay for the shopping, I make sure I get the correct ___.', ['price', 'change'], 1),
        ('Check how much everything costs after you shop on the ___.', ['price', 'receipt'], 1),
        ("Let's stand in this ___. It's short.", ['change', 'queue'], 1),
        ('I always get a shopping ___ because it’s easier when you buy a lot of things.',
         ['trolley', 'bag'], 0),
    ]),
    propuski('Прочитай разговор в магазине и перетащи слова в пропуски',
             "Paul: Have you got the shopping list, Katy?\n"
             "Katy: Yes. Here you are. Can I put these biscuits in the shopping __trolley__, please? "
             "They're a __special__ offer.\n"
             "Mum: How much are they?\n"
             "Paul: Let's check the __price__. They're 70p for six. Is that cheap?\n"
             "Mum: Yes. I think we've got everything. Let's pay __for__ the shopping there. "
             "The __queue__ is short.", mode='drag'),
    gruppy('Распредели слова по группам', [
        ('💳 этим платят', ['card', 'cash']),
        ('🛒 сюда кладут покупки', ['bag', 'basket', 'trolley']),
        ('🧾 здесь смотрят цену', ['receipt', 'special offer']),
    ]),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи, как ты ходишь в магазин: что берёшь с собой, чем платишь, '
              'во что кладёшь покупки.</p>',
              'I always write a shopping list.'),
    poka(0, 'Отлично! Теперь ты знаешь, как всё назвать в магазине.'),
]

# ─────────────────────── ДЗ 2 · 2.2 Grammar ───────────────────────
hw2 = [
    privet(1, 'Unit 2 · Сравнение', 'Сегодня сравниваем: кто быстрее, что интереснее и что самое-самое.'),
    propuski('Впиши сравнительную форму прилагательного из скобок',
             "Cats are __smaller__ (small) than elephants.\n"
             "Mary's schoolbag is __bigger__ (big) than my schoolbag. It takes more books.\n"
             "Dad says chess is __more interesting__ (interesting) than video games, but I think it's boring.\n"
             "Chores are __worse__ (bad) than homework. I don't like them.\n"
             "This test is __easier__ (easy) than the last test. I know all the answers."),
    predlozheniya('Составь предложения в превосходной степени', [
        ('Mark / intelligent student / in my class', 'Mark is the most intelligent student in my class.'),
        ('Ice Age 5 / good film / at the cinema this week', 'Ice Age 5 is the best film at the cinema this week.'),
        ('Basketball / exciting sport / I know', 'Basketball is the most exciting sport I know.'),
        ('My friend Jack / funny boy / in our school', 'My friend Jack is the funniest boy in our school.'),
    ]),
    kviz('Прочитай, что Джордж говорит на своём дне рождения, и выбери правильную форму',
         [('This is the ___ party in my life.', ['nicer', 'nicest'], 1),
          ('The jokes and games are ___ than last year.', ['funniest', 'funnier'], 1),
          ('It is the most ___ cake in the world.', ['biggest', 'amazing'], 1),
          ('She always answers the ___ difficult questions!', ['more', 'most'], 1),
          ('Mum, thanks for everything. You are the ___.', ['better', 'best'], 1)],
         material='<p><b>George:</b> «Guys, thanks for the presents. This is the <sup>1</sup>… party in my life. '
                  'The jokes and games are <sup>2</sup>… than last year – well done, Harry! And the cake is great, '
                  'Poppy. It is the most <sup>3</sup>… cake in the world. As usual Emma is the winner of all the games. '
                  'She always answers the <sup>4</sup>… difficult questions! And Mum, thanks for everything. '
                  'You are the <sup>5</sup>….»</p>'),
    propuski('Прочитай разговор Поппи и Эммы и впиши сравнительную или превосходную форму',
             "Poppy: Hi, Emma. Can you help me with my French homework? You're __better__ (good) than me. "
             "I can't do Exercise 4. It's __more difficult__ (difficult) than the other exercises. "
             "It's __longer__ (long) than the other exercises too. It's got thirty questions! "
             "It's __the most boring__ (boring) exercise in this book!\n"
             "Emma: Don't worry. Let's see. That's funny ...\n"
             "Poppy: What?\n"
             "Emma: Well, I don't know these words! You are looking at page 59. Our homework is on page 29.\n"
             "Poppy: Good! I'm not __the worst__ (bad) student in our French class!"),
    pismo('WRITING ✍️ Напиши правдивые предложения о себе',
          '<p>Напиши пять предложений про себя — в сравнительной или превосходной степени. '
          'Выбери одно прилагательное из пары.</p>'
          '<ol><li>I / runner / than my best friend — <b>fast / slow</b></li>'
          '<li>Monday / day / in my week — <b>good / bad</b></li>'
          '<li>video games / than books — <b>interesting / boring</b></li>'
          '<li>my mum / than me — <b>tall / short</b></li>'
          '<li>my street / than my school’s street — <b>quiet / noisy</b></li></ol>'),
    poka(1, 'Молодец! Сравнивать теперь получается и в словах, и в предложениях.'),
]

# ─────────────────────── ДЗ 3 · 2.3 Grammar ───────────────────────
hw3 = [
    privet(2, 'Unit 2 · Магазины и too / enough',
           'Сегодня — названия магазинов и как сказать «слишком» и «достаточно».'),
    kartochki('Повторяем названия магазинов. Нажми на карточку — услышишь слово и увидишь перевод', [
        ("baker's", 'булочная'), ('bookshop', 'книжный магазин'), ("chemist's", 'аптека'),
        ('clothes shop', 'магазин одежды'), ('department store', 'универмаг'),
        ("greengrocer's", 'овощной магазин'), ("newsagent's", 'газетный киоск'),
        ('shoe shop', 'обувной магазин'), ('sports shop', 'спортивный магазин'),
    ]),
    kviz('Прочитай и выбери, в каком магазине это купят', [
        ('Where can you buy bread and cakes?', ["a baker's", 'a bookshop', "a chemist's"], 0),
        ('Where can you buy apples and potatoes?', ['a shoe shop', "a greengrocer's", 'a sports shop'], 1),
        ('Where can you buy medicine?', ["a chemist's", "a newsagent's", 'a clothes shop'], 0),
        ('Where can you buy a magazine?', ['a bookshop', "a newsagent's", 'a department store'], 1),
        ('Where can you buy trainers and a football?', ["a baker's", 'a sports shop', "a chemist's"], 1),
        ('Where can you buy clothes, food and toys in one building?',
         ['a department store', 'a shoe shop', 'a bookshop'], 0),
    ]),
    propuski('Впиши too или enough и прилагательное из рамки: big · clean · expensive · old · small',
             "You can't wear Dad's T-shirt. It's __too big__.\n"
             "I haven't got lots of money, so I can't buy these trainers. They are __too expensive__.\n"
             "These glasses aren't __clean enough__. You need to wash them again.\n"
             "Tina isn't __old enough__ to see this film. It's for 15-year-olds and she is twelve.\n"
             "Oh no! This pizza is __too small__. It has six pieces and there are twenty people here."),
    pary('Соедини начало и конец предложения', [
        ('These black shoes are as', 'nice as those brown shoes.'),
        ("The apples aren't", 'as expensive as the oranges.'),
        ("Honey shampoo isn't as cheap", 'as lemon shampoo.'),
        ('Is your school bag as heavy', 'as my bag?'),
    ]),
    predlozheniya('Составь предложения из слов', [
        ('слишком дорогой', 'This shampoo is too expensive for me.'),
        ('достаточно сладкие', 'These oranges are sweet enough for me.'),
        ('недостаточно интересная', "This book isn't interesting enough for me."),
        ('не слишком тяжёлые', "The shopping bags aren't too heavy for her."),
    ]),
    propuski('Прочитай разговор в магазине и впиши too, enough или as',
             "Rob: What's on the list?\n"
             "Millie: Four small apples. Are these green apples small __enough__?\n"
             "Rob: No. They're __too__ big. What about those red apples?\n"
             "Millie: They aren't __as__ big as the green apples. Let's buy four red apples.\n"
             "Rob: OK. What's next on the list?\n"
             "Millie: Six lemon or chocolate cupcakes. I think lemon cupcakes aren't __as__ tasty as chocolate cupcakes.\n"
             "Rob: I think chocolate cupcakes are __too__ sweet!\n"
             "Millie: I think lemon cupcakes aren't sweet __enough__!\n"
             "Rob: Let's get three lemon cupcakes and three chocolate cupcakes.\n"
             "Millie: Good idea!"),
    poka(2, 'Супер — теперь ты можешь сказать, что слишком дорого, а чего не хватает.'),
]

# ─────────────────────── ДЗ 4 · 2.4 Communication ───────────────────────
hw4 = [
    privet(0, 'Unit 2 · В магазине одежды', 'Сегодня — разговор с продавцом: размер, цвет, примерочная.'),
    pary('Соедини начало и конец фразы', [
        ('Can I', 'help you?'),
        ("No, thanks. I'm", 'just looking.'),
        ('Do you', 'have this in a small?'),
        ('Sorry,', "we don't."),
        ('Can I try', 'it on?'),
        ('Yes, of course. The changing rooms', 'are over there.'),
    ]),
    kviz('Прочитай реплику продавца или покупателя и выбери ответ', [
        ('A: Good morning. Can I help you?',
         ["Thanks, but I don't want it.", 'Yes, we can.', "No, thanks. I'm just looking."], 2),
        ('A: Excuse me, this top is too small.',
         ["They're a size 10.", 'What size are you?', "No, they're big."], 1),
        ('A: Do you have this top in a different colour?',
         ['What colour are you looking for?', "It's a size 10.", 'Would you like a smaller top?'], 0),
        ('A: What size is that coat?', ["It's expensive.", "I think it's purple.", 'Medium.'], 2),
    ]),
    propuski('Прочитай разговор Теда с продавцом и впиши пропущенное слово',
             "Assistant: Can I help you?\n"
             "Ted: Yes, __please__. I'm looking for a T-shirt.\n"
             "Assistant: What __size__ are you?\n"
             "Ted: I'm a small, I think. Do you __have__ this T-shirt in black?\n"
             "Assistant: Yes, we __do__.\n"
             "Ted: Cool. Can I __try__ it on?\n"
             "Assistant: Yes, of course. The changing __rooms__ are over there."),
    propuski('Прочитай два разговора в магазине и впиши пропущенные слова',
             "1\n"
             "Assistant: Can I help you?\n"
             "Peter: Yes, please. I'm __looking for__ orange trainers.\n"
             "Assistant: What __size__ are you?\n"
             "Peter: Thirty-nine. Do you __have them__ in green?\n"
             "Assistant: Sorry, we __don't__.\n"
             "2\n"
             "Tracy: Excuse me. Do you __have__ this grey hoodie in a small?\n"
             "Assistant: Yes, we __do__.\n"
             "Tracy: Great. Can I __try it__ on?\n"
             "Assistant: Yes, __of course__. The changing __rooms__ are over there.\n"
             "Tracy: Thank you."),
    govorenie('SPEAKING 🎤 Разыграй разговор в магазине и запиши ответ',
              '<p>Ты хочешь купить зелёную куртку. Ты носишь размер 8, а на куртке размер 10. '
              'Поговори с продавцом: поздоровайся, скажи, что ищешь, спроси про свой размер '
              'и про примерочную.</p>',
              'Excuse me. Do you have this jacket in a size eight?'),
    poka(3, 'Отлично! Теперь в магазине одежды ты не растеряешься.'),
]

# ─────────────────────── ДЗ 5 · 2.5 Reading ───────────────────────
BLOG = (
    '<h3>Cereal Cafés <span style="color:#888">by Vicky</span></h3>'
    "<p><b>What's the most amazing breakfast food in the world? For me, it's cereal! "
    "It's tastier than eggs and it's more interesting than bread.</b></p>"
    "<p>Now you can have breakfast at a cereal café! It's called ‘Rainbow’ and it is in Oxford in the UK. "
    "It has 123 different cereals and thirty different types of milk! Inside, the café looks like a bedroom "
    "because there are chairs and beds to sit on. You can enjoy British and American cereals. "
    "Kids usually drink hot chocolate, but their parents prefer tea or coffee. Its opening hours are 8 a.m. "
    "to 8 p.m., so you can have breakfast all day. You can also book kids' parties here!</p>"
    "<p>There's also a cereal café, ‘Fantastico’, inside a big department store in Boston in the USA. "
    "This café has twenty-two different cereals. OK, that isn't as amazing as the cereal café in Oxford. "
    "But there is a surprise – they serve cereal with ice cream. It isn't breakfast – it's dessert! "
    "I'd like chocolate cereal with vanilla milk, please!</p>"
    "<p><i>Your comments: Which café would you like to visit? What would you like to try? Write to me.</i></p>"
)

hw5 = [
    privet(1, 'Unit 2 · Reading', 'Сегодня читаем блог Вики про кафе, где на завтрак — хлопья.'),
    tekst(BLOG),
    kviz('Прочитай блог ещё раз и выбери правильный ответ', [
        ('When can you go to a cereal café in Oxford?',
         ['all day', 'only in the morning', 'only in the afternoon'], 0),
        ('The ___ UK cereal café is in Oxford.', ['‘Rainbow’', '‘Fantastico’'], 0),
        ('There are ___ different types of milk at the café in Oxford.', ['123', '30'], 1),
        ('The cereal café in Oxford is like a ___.', ['bedroom', 'kitchen'], 0),
        ("It's open ___ hours a day.", ['eleven', 'twelve'], 1),
        ('The cereal café in Boston is in a ___.', ['shop', 'restaurant'], 0),
        ('They serve ice cream in the café in ___.', ['Boston', 'Oxford'], 0),
    ], material=BLOG),
    propuski('Прочитай блог ещё раз и впиши по одному слову в каждый пропуск',
             "Cereal is tastier than __eggs__.\n"
             "Bread isn't as __interesting__ as cereal.\n"
             "You can __drink__ hot chocolate, tea or coffee in the café.\n"
             "People organise kids' __parties__ at the cereal café.\n"
             "There are __twenty-two__ types of cereals at the café in Boston.\n"
             "Vicky wants __vanilla__ milk on her cereal.", material=BLOG),
    kviz('Прочитай блог ещё раз и выбери ответ', [
        ("What is Vicky's favourite breakfast food?", ['cereal', 'eggs'], 0),
        ('Which menu is from the cereal café in Oxford?', ['a menu with 30 cereals', 'a menu with 123 cereals'], 1),
        ('What do kids usually drink at the cereal café in Oxford?', ['tea', 'hot chocolate'], 1),
        ("What's the surprise at the café in Boston?", ['ice cream', 'a birthday cake'], 0),
        ('What would Vicky like?', ['chocolate cereal with vanilla milk', 'ice cream in a cone'], 0),
    ], material=BLOG),
    pismo('WRITING ✍️ Ответь на вопросы Вики',
          '<p>Напиши два предложения: в какое кафе ты бы сходил и что бы попробовал.</p>'
          '<p>Начни так: <i>I would like to visit the cereal café in … I would like to try …</i></p>'),
    poka(4, 'Здорово! Текст прочитан, а завтрак теперь звучит вкусно.'),
]

# ─────────────────────── ДЗ 6 · 2.6 Listening and Writing ───────────────────────
TRACK5 = AUDIO + 'GG%20L3%20WkBk%20A5.mp3'

FUTBOLKI = ('<p><b>Три футболки в магазине:</b></p>'
            '<ul><li>синяя — £22</li><li>зелёная — £18</li>'
            '<li>розовая с надписью HELLO SUN — £10</li></ul>')

hw6 = [
    privet(2, 'Unit 2 · Listening and Writing', 'Сегодня слушаем, что хотят купить ребята, и пишем письмо другу.'),
    ('match', {'title': 'LISTENING 🎧 Послушай запись и соедини предмет с ценой',
               'audio': TRACK5, 'skill': 'listening',
               'pairs': [{'left': 'headphones', 'right': '£30'},
                         {'left': 'a torch', 'right': '£9'},
                         {'left': 'a mobile phone', 'right': '£200'},
                         {'left': 'a camera', 'right': '£70'}]}),
    ('match', {'title': 'LISTENING 🎧 Послушай запись ещё раз и соедини, кому что нравится',
               'audio': TRACK5, 'skill': 'listening',
               'pairs': [{'left': 'Martha likes', 'right': 'the headphones.'},
                         {'left': 'Andy likes', 'right': 'the blue torch.'},
                         {'left': 'Sally likes', 'right': 'the mobile phone.'},
                         {'left': 'Fred likes', 'right': 'the camera.'}]}),
    ('quiz', {'title': 'LISTENING 🎧 Послушай запись ещё раз и выбери: верно, неверно или не сказано',
              'audio': TRACK5, 'skill': 'listening',
              'questions': [
                  {'q': 'Martha wants a new mobile phone.', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': "Martha's favourite colour is red.", 'type': 'single', 'correct': [2],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': 'Andy has lots of money.', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': 'Andy wants a torch for camping.', 'type': 'single', 'correct': [0],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': "Sally's old phone has a camera.", 'type': 'single', 'correct': [2],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': 'Sally likes the most expensive thing in the shop.', 'type': 'single', 'correct': [0],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': 'Fred has a blue camera.', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': 'Fred can buy a camera with money from his grandparents.', 'type': 'single', 'correct': [0],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
              ]}),
    propuski('Прочитай письмо Терри и впиши слова: finally · first · more · opinion',
             "Hi Tony,\n"
             "There are different backpacks at the department store in the city centre. "
             "There are three special offers. The ‘Whizz’ backpack isn't too bad, but I don't think "
             "it's the best choice. It isn't big enough. The ‘Super’ backpack is bigger than the ‘Whizz’, "
             "but in my __opinion__ the ‘Power’ backpack is the best. __First__ of all, it's big enough "
             "for books and a tablet. What's __more__, it has a key. __Finally__, it's the cheapest backpack.\n"
             "Bye for now,\nTerry", mode='drag'),
    propuski('Посмотри на цены трёх футболок и впиши пропущенное слово',
             "The __blue__ T-shirt is the most expensive.\n"
             "The __green__ T-shirt is bigger than the blue T-shirt and the pink T-shirt.\n"
             "The __pink__ T-shirt has words on it.\n"
             "The __pink__ T-shirt is the cheapest.", material=FUTBOLKI),
    pismo('WRITING ✍️ Напиши другу письмо о том, какая футболка лучше',
          FUTBOLKI +
          '<p>Напиши Юле письмо: какая футболка, по-твоему, лучше и почему. '
          'Используй <b>in my opinion</b>, <b>first of all</b>, <b>what’s more</b>, <b>finally</b>.</p>'
          '<p>Начни так: <i>Hi Julia, There are different T-shirts in the department store in the city centre. …</i></p>'),
    poka(5, 'Отлично! Ты услышал цены и написал настоящее письмо с доводами.'),
]

# ─────────────────────── ДЗ 7 · 2.7 Check yourself ───────────────────────
hw7 = [
    privet(0, 'Unit 2 · Check yourself!', 'Повторяем весь юнит перед тестом.'),
    vpisat('Напиши слово по-английски', [
        ('корзина для покупок (b…)', ['basket', 'Basket', 'shopping basket']),
        ('сдача (c…)', ['change', 'Change']),
        ('тележка для покупок (t…)', ['trolley', 'Trolley', 'shopping trolley']),
        ('наличные (c…)', ['cash', 'Cash']),
        ('чек (r…)', ['receipt', 'Receipt']),
    ]),
    kviz('Прочитай предложение и выбери правильное слово', [
        ("I'd like to pay ___ card.", ['by', 'in'], 0),
        ("Let's get some bread at the ___.", ['bookshop', "baker's"], 1),
        ("Dad doesn't want to stand in the ___.", ['offer', 'queue'], 1),
        ("They've got new trainers at the ___.", ['sports shop', "chemist's"], 0),
        ('This ___ has good fruit.', ["newsagent's", "greengrocer's"], 1),
    ]),
    pary('Соедини начало и конец предложения', [
        ('Dad is taller', 'than Mum.'),
        ('Oranges are sweeter', 'than apples.'),
        ('This T-shirt is the', 'cheapest T-shirt in the shop.'),
        ('French is more', 'difficult than English.'),
        ('Dave is the most', 'intelligent student in the class.'),
        ('We are', 'the happiest kids in the world!'),
    ]),
    propuski('Прочитай разговор и впиши too, enough, as или not',
             "A: My laptop is __too__ slow to play video games. I need a new one.\n"
             "B: Look at this laptop. I think it's fast __enough__ for games.\n"
             "A: It isn't __as__ small as that one, but I like it.\n"
             "B: The size is a problem. Can you put it in your bag? I think it's __too__ big.\n"
             "A: Yes, you're right. But it is __not__ as expensive as that laptop. I can buy a new bag.\n"
             "B: That's true. Look. This laptop bag is as cheap __as__ a schoolbag! It's a special offer."),
    pary('Собери разговор в магазине: соедини реплику с ответом', [
        ('Can I', 'help you?'),
        ("Yes, please. I'm", 'looking for a jacket.'),
        ('What size', 'are you?'),
        ("I'm a medium. Do", 'you have this jacket in blue?'),
        ('Can I', 'try it on?'),
        ('Yes, of course. The changing', 'rooms are over there.'),
    ]),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи про свой любимый магазин: как он называется по-английски, '
              'что там покупают и почему он тебе нравится. Скажи три-четыре предложения.</p>',
              'My favourite shop is the bookshop near my house.'),
    poka(1, 'Юнит пройден! Теперь можно браться за тест.'),
]

UROKI = [('Homework 1', hw1), ('Homework 2', hw2), ('Homework 3', hw3), ('Homework 4', hw4),
         ('Homework 5', hw5), ('Homework 6', hw6), ('Homework 7', hw7)]

if __name__ == '__main__':
    put = sys.argv[1] if len(sys.argv) > 1 else 'builds/gg3/wb/u2/u2.sql'
    out = ['-- Go Getter 3, юнит 2 «Shopping» по рабочей тетради: домашки 1–7 (черновики)',
           f"update classroom_lessons set sort_order = 10 where id = '{TEST}';"]
    for i, (nazv, bloki) in enumerate(UROKI):
        out.append(sql_uroka(UNIT, nazv, i, bloki))
    io.open(put, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(put, sum(len(b) for _, b in UROKI), 'блоков,', os.path.getsize(put) // 1024, 'КБ')
