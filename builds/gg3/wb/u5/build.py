# -*- coding: utf-8 -*-
"""Go Getter 3, юнит 5 «Health matters» по рабочей тетради (стр. 42–48).

Ключи 5.7 — Answer key тетради (стр. 95); ключи аудирования 5.6 — по расшифровке
трека A13: Карен просится к Марии доделать проект по истории, папа не пускает —
завтра контрольная по математике; Карен говорила, что занималась, а на самом деле
играла в видеоигры; папа советует учиться усерднее, не играть, ложиться спать
(в итоге в десять), не заниматься после девяти, положить калькулятор в рюкзак и
делает ей гренки с сыром.

Задания тетради, завязанные на картинку, переписаны в текстовые (генератор
картинок исчерпан): 5.1 упр. 1 — подсказки перенесены в сам текст, 5.3 упр. 1 —
слово выбирается по описанию, 5.5 упр. 1 (порядок картинок) снято, 5.7 упр. 1 —
к каждому пункту дано словесное описание фотографии, ключ прежний.
"""
import io, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import (AUDIO, privet, poka, kartochki, kviz, pary, propuski, gruppy,
                    predlozheniya, vpisat, govorenie, pismo, tekst, sql_uroka)

UNIT = 'a2bbdc71-5c49-451a-88cd-b5b4cea4d17b'   # Unit 5 · Health matters
TEST = 'a941b58c-a7df-4877-aa62-41bbe488ea2c'
TRACK13 = AUDIO + 'GG%20L3%20WkBk%20A13.mp3'

# ─────────────────────── ДЗ 1 · 5.1 Vocabulary ───────────────────────
SLOVA = [
    ('a cold', 'простуда'), ('a cough', 'кашель'), ('a headache', 'головная боль'),
    ('a blocked nose', 'заложенный нос'), ('a runny nose', 'насморк'),
    ('a sore throat', 'больное горло'), ('a stomachache', 'боль в животе'),
    ('a temperature', 'температура'), ('earache', 'боль в ухе'), ('toothache', 'зубная боль'),
    ('the flu', 'грипп'), ('to sneeze', 'чихать'), ('I feel terrible', 'мне очень плохо'),
]

PLAKAT = ('<p><b>LOOK AFTER YOUR HEALTH</b></p>'
          '<p>Always brush your teeth after a meal. Clean teeth can stop toothache.</p>'
          '<p>Always put your hand in front of your mouth when you cough. And put it in front '
          'of your nose and mouth when you sneeze. Don’t give everyone your cold!</p>')

hw1 = [
    privet(0, 'Unit 5 · Health matters', 'Сегодня — здоровье: как сказать по-английски, что болит.'),
    kartochki('Повторяем слова урока. Нажми на карточку — услышишь слово и увидишь перевод', SLOVA),
    kviz('Прочитай плакат о здоровье и выбери правильное слово', [
        ('Always ___ your teeth after a meal.', ['brush', 'wash'], 0),
        ('Clean teeth can stop ___.', ['earache', 'toothache'], 1),
        ('Always put your hand in front of your mouth when you ___.', ['sneeze', 'cough'], 1),
        ('And put it in front of your nose and mouth when you ___.', ['sneeze', 'cough'], 0),
        ('Don’t give everyone your ___!', ['headache', 'cold'], 1),
    ]),
    propuski('Прочитай про семью Джо у врача и перетащи слова в пропуски',
             "This is Joe and his family. They all have health problems today and they are at "
             "the doctor's.\n"
             "Joe is very hot, so he has got __a temperature__.\n"
             "His mum is drinking tea because she has got __a sore throat__.\n"
             "His dad can't eat anything because his tooth hurts: he has got __toothache__.\n"
             "His grandma is holding her ear, so she has got __earache__.\n"
             "His sister, Penny, is holding her head because she has got __a headache__.\n"
             "And what about Rex, the dog? He is sneezing all the time: he has got "
             "__a runny nose__. The doctor looks surprised!", mode='drag'),
    propuski('Прочитай разговор Марка и Тины и перетащи слова в пропуски',
             "Mark: Hi Tina. I'm phoning you because I can't come to play the new computer game "
             "today. I feel __terrible__. I've got a sore __throat__ and I'm __coughing__ all "
             "the time.\n"
             "Tina: Oh dear. But it's OK, because I __feel__ bad too. I'm __hot__ because I've "
             "got a __temperature__.\n"
             "Mark: I'm going to __drink__ lots of tea with honey.\n"
             "Tina: Good idea. I'm going to __go__ to bed and sleep.\n"
             "Mark: Bye then. Sleep well.\n"
             "Tina: Thanks. Bye.", mode='drag'),
    vpisat('Прочитай предложение и напиши слово по-английски', [
        ("I'm sorry, but I can't come to the park. I've got a c… (простуда)",
         ['cold', 'a cold', 'Cold']),
        ("I can't smell anything because I've got a b… n… (заложенный нос)",
         ['blocked nose', 'a blocked nose', 'Blocked nose']),
        ("I ate too many pancakes and now I've got a s… (боль в животе)",
         ['stomachache', 'a stomachache', 'stomach ache', 'Stomachache']),
        ("I can't talk a lot today because I've got a c… (кашель)",
         ['cough', 'a cough', 'Cough']),
        ("My ear hurts. I've got e… (боль в ухе)", ['earache', 'an earache', 'Earache']),
        ("I'm very hot. I've got a t… (температура)",
         ['temperature', 'a temperature', 'Temperature']),
    ]),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи, что у тебя бывает часто, что иногда, а чего не бывает никогда: '
              '<i>I often have … I sometimes have … I never have …</i> Три-четыре предложения.</p>',
              'My little brother often has earache.'),
    poka(0, 'Готово! Теперь ты можешь объяснить врачу, что у тебя болит.'),
]

# ─────────────────────── ДЗ 2 · 5.2 Grammar: have to ───────────────────────
PISMO_EMMY = (
    '<p><b>Hi Poppy,</b></p>'
    "<p>I've got a sore throat and a runny nose, so Gran says I have to stay at home tomorrow. "
    "I'm happy because I don't have to go to school. But we have to finish our project. "
    "Don't worry, you don't have to come here. We can chat online – is 4 p.m. OK or do you have "
    "to go out then? I can't chat before that because Gran says she has to use the computer.</p>"
    '<p><b>Emma</b></p>'
)

hw2 = [
    privet(1, 'Unit 5 · have to', 'Сегодня — как сказать по-английски «придётся» и «можно не».'),
    kviz('Прочитай письмо Эммы и выбери правильную форму', [
        ('Gran says I ___ stay at home tomorrow.', ['have to', 'has to'], 0),
        ("I'm happy because I ___ go to school.", ["don't have to", "doesn't have to"], 0),
        ('But we ___ finish our project.', ['has to', 'have to'], 1),
        ("Don't worry, you ___ come here.", ["doesn't have to", "don't have to"], 1),
        ('Is 4 p.m. OK or ___ go out then?', ['you have to', 'do you have to'], 1),
        ('Gran says she ___ use the computer.', ['has to', 'have to'], 0),
    ], material=PISMO_EMMY),
    pary('Соедини вопрос с ответом', [
        ('Does Karen have to see the dentist?', 'Yes, she does. She has got toothache.'),
        ('Do we have to go to bed now?', "No, you don't. It isn't late."),
        ('Does Dad have to go to work?', "No, he doesn't. It's Sunday."),
        ('Do they have to do any homework today?', 'Yes, they do.'),
    ]),
    predlozheniya('Составь предложения с have to', [
        ('в субботу школы нет', "I don't have to go to school on Saturday."),
        ('мама и готовка', 'My mum has to cook every day.'),
        ('друг и автобус', 'My best friend has to get the bus home from school.'),
        ('дела по дому и головная боль', "I don't have to do chores when I've got a headache."),
    ]),
    propuski('Впиши have to в нужной форме с глаголом: brush · go · not go · not use · not wear · see',
             "Jane has got the flu. She __has to go__ to bed.\n"
             "It's Saturday. I __don't have to go__ to school. Hurray!\n"
             "Fred ate an ice cream. He __has to brush__ his teeth, but he can't find his "
             "toothbrush!\n"
             "Don't worry about wet hair. It's hot today! You __don't have to use__ the hairdryer "
             "before you go out.\n"
             "It's warm and sunny today. We __don't have to wear__ coats.\n"
             "George has got a stomachache. He __has to see__ a doctor. He can't play football today."),
    propuski('Прочитай разговор Поппи и Эммы и впиши have to в нужной форме',
             "Poppy: Emma, is that you? I can't hear you. You __have to speak__ (speak) louder.\n"
             "Emma: Yes, it's me. I've got a sore throat. That's why I didn't go to school. "
             "I think I __have to drink__ (drink) some more tea.\n"
             "Poppy: Oh dear. __Do__ you __have to see__ (see) a doctor?\n"
             "Emma: No, I __don't__. It's not really bad.\n"
             "Poppy: OK. I'm phoning because we __don't have to do__ (do) a French test on "
             "Wednesday. It's on Friday now. Our teacher told us at school today.\n"
             "Emma: That's good news. I __don't have to learn__ (learn) the new words on Tuesday. "
             "I can wait until Thursday.\n"
             "Poppy: I've got some more news. There's a new boy in our class. He's French.\n"
             "Emma: He's lucky! He __doesn't have to do__ (do) anything for the French test.\n"
             "Poppy: Ha ha! That's true. His French is perfect!"),
    pismo('WRITING ✍️ Напиши правдивые предложения о себе',
          '<p>Четыре предложения с <b>have to</b> или <b>don’t have to</b>: что тебе приходится '
          'делать дома и в школе, а что делать не нужно.</p>'
          '<p>Начни так: <i>On Monday I have to … At the weekend I don’t have to …</i></p>'),
    poka(1, 'Хорошая работа! have to и don’t have to больше не путаются.'),
]

# ─────────────────────── ДЗ 3 · 5.3 Grammar: should ───────────────────────
hw3 = [
    privet(2, 'Unit 5 · should', 'Сегодня — как дать совет и назвать мелкую травму.'),
    kviz('Прочитай и выбери подходящее слово', [
        ('Look at this big ___ on my leg. It’s from a football!', ['burn', 'bruise', 'bite'], 1),
        ("I've got a ___. Luckily, I write with my left hand!", ['cut', 'bite', 'broken arm'], 2),
        ("I've got a ___ on my hand. It's from a mosquito.", ['bite', 'bruise', 'burn'], 0),
        ("I've got a ___ on my finger. I wasn't careful when I was making salad.",
         ['bruise', 'cut', 'bite'], 1),
        ('This ___ on my hand is from hot soup.', ['broken arm', 'cut', 'burn'], 2),
    ]),
    pary('Соедини ситуацию с советом', [
        ('There are lots of mosquitoes.', 'You should use a net.'),
        ("It's raining.", 'You should take an umbrella.'),
        ('Dad has got a bad burn.', 'He should go to the doctor.'),
        ('Maria has a temperature.', 'She should go to bed.'),
        ('The weather is nice this weekend.', 'We should go camping.'),
        ('I played football and now I have a bruise.', 'You should be careful next time.'),
    ]),
    predlozheniya('Составь вопросы с should', [
        ('про книгу', 'Should I read this book?'),
        ('про Дэвида и футбол', 'Should David play football?'),
        ('про сон', 'Should we go to bed?'),
        ('про Пенни и пирожные', 'Should Penny have any cakes?'),
        ('про братьев', 'Should I phone my brothers?'),
    ]),
    propuski('Впиши should или shouldn’t с глаголом: go · have · phone · play · read',
             "You __should read__ this book. It's great.\n"
             "David has got a broken arm. He __shouldn't play__ football.\n"
             "It's 11.30 p.m. We __should go__ to bed.\n"
             "Penny has got a stomachache. She __shouldn't have__ any cakes.\n"
             "My brothers are late. I __should phone__ them and ask where they are."),
    propuski('Прочитай разговор доктора Кью и Милли и впиши should с глаголом',
             "Dr Q: I'm tired.\n"
             "Millie: You __should lie__ (lie) down.\n"
             "Dr Q: I have lots of work and there's a good film on TV. But I've got a headache too.\n"
             "Millie: You __should turn__ (turn) off your computer and you __shouldn't watch__ "
             "(watch) TV.\n"
             "Dr Q: OK.\n"
             "Millie: __Should I make__ (I / make) you some soup?\n"
             "Dr Q: No, thanks. I'm not hungry. But I've got a sore throat now. "
             "__Should I drink__ (I / drink) some tea with honey?\n"
             "Millie: Yes, you __should__. I can make it.\n"
             "Dr Q: Thank you, Millie."),
    govorenie('SPEAKING 🎤 Дай совет вслух и запиши ответ',
              '<p>Твой одноклассник весь день сидит за компьютером, и у него болит голова. '
              'Дай ему три совета: два с <b>should</b> и один с <b>shouldn’t</b>.</p>',
              "You shouldn't eat so many sweets."),
    poka(2, 'Отлично! Советовать по-английски ты уже умеешь.'),
]

# ─────────────────────── ДЗ 4 · 5.4 Communication ───────────────────────
hw4 = [
    privet(0, 'Unit 5 · Как спросить о самочувствии', 'Сегодня — как спросить, что случилось, и дать совет.'),
    kviz('Прочитай реплику и выбери ответ', [
        ("A: What's the matter?",
         ["Yes, you're right.", "I don't feel very well.", "Why don't you lie down?"], 1),
        ('A: I have a burn.',
         ['I feel terrible.', "What's the matter?", "Why don't you put some ice on it?"], 2),
        ("A: I've got a headache.",
         ["Why don't you take a painkiller?", "What's wrong?", 'I feel terrible.'], 0),
        ('A: I think you should see the dentist.',
         ["What's the matter?", "Yes, you're right.", "I've got a cut."], 1),
    ]),
    predlozheniya('Составь реплики разговора о здоровье', [
        ('вопрос о самочувствии', "What's the matter?"),
        ('ответ', 'I feel terrible.'),
        ('про порез', "I've got a cut."),
        ('совет про пластырь', "Why don't you put a plaster on it?"),
        ('про зубную боль', "I've got toothache."),
        ('совет про дантиста', 'I think you should see the dentist.'),
    ]),
    propuski('Прочитай разговор Грега с папой и впиши по одному слову',
             "Dad: What's the __matter__?\n"
             "Greg: I feel __terrible__, Dad. __I've__ got a headache.\n"
             "Dad: I think you __should__ take a painkiller.\n"
             "Greg: Yes, you're __right__.\n"
             "Dad: __Why__ don't you lie down too?\n"
             "Greg: Yes, that's a good __idea__."),
    propuski('Прочитай жалобу и впиши пропущенные слова в совет',
             "A: I've got a headache.\nB: I think you __should take__ a painkiller.\n"
             "A: I've got bad bruises on my legs.\nB: Why don't you __put__ some cream on them?\n"
             "A: I've got these mosquito bites.\nB: You should put __cream__ on them.\n"
             "A: I've got a burn on my hand.\nB: Why don't you put some __ice__ on it?\n"
             "A: I've got a sore throat.\nB: You should drink some __mint tea__."),
    pismo('WRITING ✍️ Напиши разговор с другом',
          '<p>Твой лучший друг чувствует себя ужасно. Напиши ваш разговор: спроси, что случилось, '
          'выслушай ответ, дай два совета и получи согласие.</p>'
          '<p>Используй слова: <b>idea · matter · right · should · terrible · well · why</b>.</p>'),
    govorenie('SPEAKING 🎤 Разыграй разговор и запиши ответ',
              '<p>Твоя сестра обожгла руку о горячий чайник. Спроси, что случилось, посочувствуй '
              'и дай ей совет.</p>',
              "What's the matter? You look terrible."),
    poka(3, 'Супер! Теперь ты знаешь, как поддержать и посоветовать.'),
]

# ─────────────────────── ДЗ 5 · 5.5 Reading ───────────────────────
BLOG5 = (
    '<h3>Bill’s blog · What should you do for a cold?</h3>'
    '<p><b>1 England.</b> What should you do when you have a cold? My mum usually makes me a cup '
    'of hot tea. But some parents have different ideas. I asked my e-pals from different countries '
    'what they have to do when they don’t feel well.</p>'
    '<p><b>2 Poland.</b> My friend Marek has to drink hot milk when he has a cold or a sore throat. '
    'His mum puts the milk with some butter in the microwave oven. When it’s hot, she adds an egg '
    '(not cooked!) and some honey. I don’t think it’s tasty, but he says it works.</p>'
    '<p><b>3 Japan.</b> Aiko doesn’t have a hot drink for a cold, but her dad makes her hot soup. '
    'It’s actually hot green onion soup. Aiko says you should have three bowls of this soup every '
    'day when you have a cold. She says it’s good for a blocked nose too.</p>'
    '<p><b>4 Canada.</b> My friend Charlie thinks socks are a good idea for a cold. He says you '
    'have to use old socks when you are ill! First, you have to put your feet in hot water, so they '
    'are warm. Then you put the socks in water, so they are wet. Next you put on the wet socks and '
    'wear some dry socks on top of them. Then go to bed!</p>'
)

hw5 = [
    privet(1, 'Unit 5 · Reading', 'Сегодня читаем блог Билла: что делают при простуде в разных странах.'),
    tekst(BLOG5),
    pary('Прочитай блог и соедини человека с тем, что он делает', [
        ("Bill's mum", 'makes tea for a cold.'),
        ('Marek has to', 'drink hot milk for a cold.'),
        ('Aiko', "doesn't have tea or milk for a cold."),
        ("Aiko's dad", 'makes hot soup for a cold.'),
        ('Charlie', 'wears wet socks for a cold.'),
    ], material=BLOG5),
    kviz('Прочитай блог и выбери правильный ответ', [
        ('Do all parents have the same ideas for a cold?',
         ['Yes, they do.', "No, they don't."], 1),
        ("How does Marek's mum make the milk hot?",
         ['She puts it in the fridge.', 'She puts it in the microwave oven.',
          'She puts it in the sun.'], 1),
        ("Does Aiko's dad make her something hot for a cold?",
         ["No, he doesn't. He makes her cold tea.", 'Yes, he does. He makes her hot soup.'], 1),
        ("What do you need for Charlie's idea?",
         ['green onions and honey', 'a net and a torch', 'old socks and hot water'], 2),
        ('How often should you have the soup, Aiko says?',
         ['three bowls every day', 'one bowl a week', 'two bowls on Sunday'], 0),
    ], material=BLOG5),
    propuski('Прочитай блог ещё раз и впиши по одному слову',
             "Bill asked his __e-pals__ for ideas.\n"
             "Marek's idea works for a cold or a sore __throat__.\n"
             "Bill thinks the milk drink isn't __tasty__.\n"
             "Aiko's soup has green __onions__ in it.\n"
             "Charlie wears __wet__ and dry socks in bed.", material=BLOG5),
    propuski('Прочитай про части тела и перетащи слова в пропуски',
             "Your __brain__ is a very important part of your body. You use it to think and it "
             "sends messages to all the other parts of your body. It tells your __heart__ to work, "
             "so the red __blood__ can go around your body. You also have lots of strong white "
             "__bones__ inside your body, so you can stand up. The __muscles__ hold them together "
             "and they make them move, so you can run and walk.", mode='drag'),
    pismo('WRITING ✍️ Напиши ответ Биллу',
          '<p>Какой из четырёх способов ты бы попробовал и почему? И что делают при простуде '
          'в твоей семье? Четыре-пять предложений.</p>'
          '<p>Начни так: <i>Hi Bill, I would like to try …</i></p>'),
    poka(4, 'Здорово! Блог прочитан, ответ Биллу написан.'),
]

# ─────────────────────── ДЗ 6 · 5.6 Listening and Writing ───────────────────────
STATYA = (
    '<h3>Get ready to go on a camping holiday</h3>'
    '<p><b>Do you want to go on a camping holiday this summer?</b></p>'
    '<p>It is often cold at night in a tent. You have to take warm clothes like a hoodie, not just '
    'T-shirts and shorts. Take boots too because it sometimes rains. Learn how to put up your tent '
    'before you go. It isn’t always easy. There are lots of mosquitoes in the countryside on summer '
    'nights. You should take a net. Then you don’t have to worry about bites. You should also take '
    'a torch. It is usually dark on campsites at night, so a torch is useful!</p>'
)

hw6 = [
    privet(2, 'Unit 5 · Listening and Writing', 'Сегодня слушаем разговор Карен с папой и пишем свою статью.'),
    ('gaps', {'title': 'LISTENING 🎧 Послушай разговор Карен с папой и впиши совет',
              'mode': 'type', 'audio': TRACK13,
              'text': "You __should study__ harder.\n"
                      "You __shouldn't play__ video games.\n"
                      "You should __go__ to bed early.\n"
                      "You should __put__ your calculator in your school bag.\n"
                      "You __have to eat__ when you study."}),
    ('quiz', {'title': 'LISTENING 🎧 Послушай разговор ещё раз и выбери: верно, неверно или не сказано',
              'audio': TRACK13,
              'questions': [
                  {'q': 'Karen has a Maths test tomorrow.', 'type': 'single', 'correct': [0],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': "Karen's mum is watching TV.", 'type': 'single', 'correct': [2],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': "Karen doesn't like Maths.", 'type': 'single', 'correct': [2],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': 'She was studying when her dad came home.', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': 'She has to go to bed at 9.30 p.m.', 'type': 'single', 'correct': [1],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
                  {'q': "Karen's dad made her some food.", 'type': 'single', 'correct': [0],
                   'options': [{'text': 'Верно'}, {'text': 'Неверно'}, {'text': 'Не сказано'}]},
              ]}),
    ('gaps', {'title': 'LISTENING 🎧 Карен рассказывает всё подруге. Впиши по одному слову',
              'mode': 'type', 'audio': TRACK13,
              'text': "Karen: Hi __Maria__. I'm sorry, but I can't come to your house and finish "
                      "the __history__ project.\n"
                      "Maria: Why not?\n"
                      "Karen: I have to study Maths. I'm not __ready__ for the test because I was "
                      "playing video __games__ when my dad came home.\n"
                      "Maria: Oh dear. Does your dad know?\n"
                      "Karen: Yes! Now I have to study all evening. But he says I shouldn't study "
                      "after __nine__ o'clock and then I should relax before I go to bed at "
                      "__ten__ o'clock.\n"
                      "Maria: OK. Sleep well! See you tomorrow!"}),
    tekst(STATYA),
    pary('Соедини вещь с тем, зачем её берут в поездку за город', [
        ('money', 'to buy a souvenir or a snack'),
        ('sandwiches', "you shouldn't be hungry when you walk a lot"),
        ('a camera', 'to take photos of birds, trees and your friends'),
        ('a hoodie', "you don't have to worry about mosquito bites"),
    ], material=STATYA),
    pismo('WRITING ✍️ Напиши статью о поездке за город',
          '<p>Напиши свою статью: как подготовиться к поездке за город. Шесть-семь предложений.</p>'
          '<p>Возьми за образец статью Беллы и слова из задания про вещи. Используй '
          '<b>have to</b>, <b>don’t have to</b>, <b>should</b>, <b>shouldn’t</b> и повелительные '
          'формы (<i>Take …, Learn …</i>).</p>'
          '<p>Начни так: <i>Do you want to go to the countryside this summer?</i></p>'),
    poka(5, 'Отлично! И послушали, и статью написали.'),
]

# ─────────────────────── ДЗ 7 · 5.7 Check yourself ───────────────────────
hw7 = [
    privet(0, 'Unit 5 · Check yourself!', 'Повторяем весь юнит перед тестом.'),
    kviz('Прочитай описание и выбери, что у человека болит', [
        ('Mum is in the garden and she is sneezing all the time. She has got …',
         ['a runny nose', 'a temperature', 'a sore throat'], 0),
        ('Aunt Jane is lying on the sofa and holding her stomach. She has got …',
         ['a mosquito bite', 'a blocked nose', 'a stomachache'], 2),
        ('Lara is in bed and the thermometer says 38.5°. She has got …',
         ['a temperature', 'a runny nose', 'a cough'], 0),
        ("Uncle Joe is holding his cheek and he can't eat anything. He has got …",
         ['toothache', 'a cold', 'a blocked nose'], 0),
        ('Gary is drinking tea with honey and he can hardly speak. He has got …',
         ['a cough', 'a sore throat', 'earache'], 1),
    ]),
    pary('Соедини начало и конец предложения', [
        ('Mum has to', 'go to the doctor.'),
        ("I don't", 'have to do my homework now.'),
        ('Does', 'Fred have to leave?'),
        ('Do you', 'have to learn these words?'),
        ('Stan and Archie', "don't have to study today."),
    ]),
    kviz('Прочитай разговор и выбери правильное слово', [
        ("A: I feel terrible. — B: What's ___ matter?", ['the', 'a'], 0),
        ("A: I've got a stomachache. — B: I think you ___ have some mint tea.",
         ['should', "shouldn't"], 0),
        ("A: Yes, you're ___.", ['idea', 'right'], 1),
        ('B: Why ___ you go to bed too?', ['should', "don't"], 1),
        ("A: OK. That's a good ___.", ['idea', 'right'], 0),
    ]),
    propuski('Прочитай разговор и впиши should в нужной форме',
             "A: You look tired. You __should lie down__ (lie down).\n"
             "B: I know. I feel terrible. __Should I see__ (I / see) the doctor?\n"
             "A: Don't be silly! Do you have a temperature?\n"
             "B: No, I don't.\n"
             "A: Then you __shouldn't go__ (not go) to the doctor. You're just tired. "
             "You __should sleep__ (sleep) in bed.\n"
             "B: OK. Can you phone Mark? He __shouldn't visit__ (not visit) me today.\n"
             "A: OK. __Should he call__ (he / call) you tomorrow?\n"
             "B: Yes. Thanks. You're a good friend."),
    vpisat('Прочитай предложение и напиши слово по-английски', [
        ('There are muscles and b… inside your arms and legs. (кости)', ['bones', 'Bones']),
        ('Your b… is in your head and you use it to think. (мозг)', ['brain', 'Brain']),
        ('Your h… makes your blood move round your body. (сердце)', ['heart', 'Heart']),
        ("Tom fell badly and he went to hospital. His leg is b… and he's got some bruises. (сломана)",
         ['broken', 'Broken']),
        ('Be careful in the kitchen. You can get a burn from hot food and a c… from a knife. (порез)',
         ['cut', 'a cut', 'Cut']),
    ]),
    govorenie('SPEAKING 🎤 Расскажи вслух и запиши ответ',
              '<p>Расскажи про день, когда ты болел: что у тебя болело, что тебе пришлось делать, '
              'какие советы тебе дали дома. Четыре-пять предложений.</p>',
              'Last winter my sister had the flu and she had to stay in bed for a week.'),
    poka(1, 'Юнит пройден! Можно браться за тест.'),
]

UROKI = [('Homework 1', hw1), ('Homework 2', hw2), ('Homework 3', hw3), ('Homework 4', hw4),
         ('Homework 5', hw5), ('Homework 6', hw6), ('Homework 7', hw7)]

if __name__ == '__main__':
    put = sys.argv[1] if len(sys.argv) > 1 else 'builds/gg3/wb/u5/u5.sql'
    out = ['-- Go Getter 3, юнит 5 «Health matters» по рабочей тетради: домашки 1–7 (черновики)',
           f"update classroom_lessons set sort_order = 10 where id = '{TEST}';"]
    for i, (nazv, bloki) in enumerate(UROKI):
        out.append(sql_uroka(UNIT, nazv, i, bloki))
    io.open(put, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(put, sum(len(b) for _, b in UROKI), 'блоков,', os.path.getsize(put) // 1024, 'КБ')
