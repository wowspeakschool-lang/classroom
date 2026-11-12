# Урок 13+ после сокращения — попредметно, для Анны (12.11.2026).
# Сборка: python3 builds/mvu_13plus/sokrashchenie.py → builds/mvu_13plus/Урок 13+ после сокращения.docx
# Правило: каждая тема чек-листа — 1–2 раза. Назвать предмет даёт балл, только если слово само из темы
# (мяч → Sports, но паспорт ≠ Countries). Сортировка и «соедини пары» — одно задание: по теме считается раз.
import os, tempfile
from PIL import Image
from docx import Document
from docx.shared import Pt, Cm, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
MEDIA = os.path.join(HERE, '..', '..', 'media', 'mvu_13plus')
OUT = os.path.join(HERE, 'Урок 13+ после сокращения.docx')

# Элемент предмета:
#   ('name', вопрос, ответ, тема|None)
#   ('task', заголовок, инструкция на экране, [картинки], [пункты], примечание)
#      пункт: (текст, [варианты; верный — первый], тема)  или (текст, None, тема) — устно / без вариантов
#   ('audio', текст записи)
#   ('you', вопрос, [темы])
R = []

def room(title, code, objs): R.append((title, code, objs))

room('Часть 1 · Гостиная (уровень A1.1–A1.2)', '4 цифры', [
 ('Семейная фотография', [
  ('name', "What's this?", 'a family photo', None),
  ('task', 'Задание 1. Семья Тома', 'Look and choose.', ['СХЕМА'],
   [('Bob is Emma’s ___ .', ['uncle', 'father', 'grandfather'], 'Families'),
    ('Mark and Kate ___ Tom’s parents.', ['are', 'is', 'am'], 'To be')],
   'Картинка — новое семейное дерево схемой: George ═ Rose → их сыновья Mark и Bob; Mark ═ Kate → Tom и Emma; Bob ═ Lily. Под портретами только имена.'),
  ('you', 'Tell me about your family.', ['Families', 'To be'])]),
 ('Рюкзак', [
  ('name', "What's this?", 'a schoolbag (a backpack)', 'School objects'),
  ('task', 'Задание 1. Что в рюкзаке у Тома', 'Look and choose.', ['schoolbag_open'],
   [('There ___ two pens.', ['are', 'is', 'am'], 'There is'),
    ('There ___ a calculator.', ['isn’t', 'aren’t', 'is'], 'There is'),
    ('Tom ___ got a pencil case.', ['has', 'have', 'is'], 'Have got')], ''),
  ('you', 'What have you got in your school bag?', ['School objects', 'Have got'])]),
 ('Паспорт', [
  ('name', "What's this?", 'a passport', None),
  ('task', 'Задание 1. Паспорт друга Тома', 'Look at the flag and choose.', [],
   [('🇩🇪 Hans is from Germany. He’s ___ .', ['German', 'Germany', 'Germanish'], 'Countries')], ''),
  ('you', 'Where are you from? Which country would you like to visit?', ['Countries'])]),
 ('Ваза с фруктами', [
  ('name', "What's this?", 'fruit (a bowl of fruit)', 'Food and drinks'),
  ('task', 'Задание 1. Что в холодильнике у Тома', 'Look and choose.', ['fridge_open'],
   [('There is ___ milk in the fridge.', ['some', 'any', 'a'], 'Some, any, lots of'),
    ('There aren’t ___ apples in the fridge.', ['any', 'some', 'a'], 'Some, any, lots of')],
   'Было «верно / неверно» на 6 пунктов — ответ был виден по картинке без грамматики.'),
  ('you', 'What do you usually have for breakfast?', ['Food and drinks'])]),
 ('Футбольный мяч', [
  ('name', "What's this?", 'a football (a ball)', 'Sports'),
  ('task', 'Задание 1. Том играет в футбол', 'Look and choose one word.', ['athlete'],
   [('стрелка на колено', ['knee', 'foot', 'leg', 'arm'], 'Body parts'),
    ('стрелка на ступню', ['foot', 'knee', 'leg', 'arm'], 'Body parts')], 'Было пять стрелок, стало две.'),
  ('task', 'Задание 2. Какой спорт любит Том', 'Look and choose.', ['sport_bike', 'sport_tennis'],
   [    ('___ Tom ride a bike to school? — Yes, he does.', ['Does', 'Do', 'Is'], 'Present Simple'),
    ('Tom can play tennis, but he ___ play basketball.', ['can’t', 'can', 'don’t can'], 'Can/Can’t')],
   'Теннисную ракетку перерезать (замечание 13).'),
  ('you', 'What sports can you do?', ['Sports', 'Can/Can’t'])]),
 ('Игрушечный автобус', [
  ('name', "What's this?", 'a bus', 'Transport'),
  ('task', 'Задание 1. Вид из окна — устно', 'Who can you see? What do they do?', ['street'],
   [('Ученик называет людей и профессии: a police officer, a doctor, a chef…', None, 'Jobs (учитель ставит балл)')],
   'Вариантов нет — учитель спрашивает и отмечает, сколько профессий назвал ученик.'),
  ('task', 'Задание 2. Та же картинка', 'Look and choose.', [],
   [('Look! He ___ a sandwich now.', ['is eating', 'eats', 'eat'], 'Present Simple vs Present Continuous'),
    ('What’s on the bridge?', ['a train', 'a taxi', 'a bus'], 'Transport')], ''),
  ('you', 'What are you doing now?', ['Present Simple vs Present Continuous'])]),
 ('Билеты в кино', [
  ('name', "What are these?", 'cinema tickets', 'Entertainment'),
  ('task', 'Задание 1. Собери предложение', 'Put the words in order.', [],
   [('I always go to the cinema on Fridays.', None, 'Adverbs of frequency')], ''),
  ('task', 'Задание 2. Выбери ответ', 'Choose the right answer.', [],
   [('Let’s ___ to the cinema tonight!', ['go', 'going', 'to go'], 'Let’s…')], ''),
  ('you', 'How often do you go to the cinema? What are your favourite places in your city?', ['Adverbs of frequency', 'Entertainment'])]),
 ('Зонтик', [
  ('name', "What's this?", 'an umbrella', None),
  ('task', 'Задание 1. Какая погода — устно', 'What’s the weather like?', ['w_snowy'],
   [('Ученик отвечает сам: It’s snowy. / It’s cold.', None, 'Weather (учитель ставит балл)')],
   'Вариантов нет. Облако со снегом перерезать (замечание 13).'),
  ('task', 'Задание 2. Едем на море: солнечно и жарко', 'What do you take? Sort.',
   ['cl_shorts', 'cl_scarf'],
   [('Take ✅: shorts, a T-shirt · Don’t take ❌: a jacket, a scarf', None, 'Clothes')],
   'Четыре картинки без подписей. Ученик раскладывает и называет каждую вещь вслух (в плане). Футболку и куртку нарисовать (промпт в чате).'),
  ('task', 'Задание 3. Выбери слово', 'Choose the right word.', [],
   [('Tom ___ to the beach every summer.', ['goes', 'go', 'gos'], 'Present Simple')], ''),
  ('you', 'What’s the weather like today? What do you need for a trip to the mountains?', ['Weather', 'Need, want', 'Clothes'])]),
 ('Кошка', [
  ('name', "What's this?", 'a cat', 'Pets and farm animals'),
  ('task', 'Задание 1. Животные', 'Look and choose.', ['an_horse', 'an_cat', 'an_cow', 'an_pig', 'an_chicken'],
   [('(лошадь и кошка) A horse is ___ than a cat.', ['bigger', 'big', 'biggest'], 'Comparatives'),
    ('(тигр и кошка) A tiger is ___ than a cat.', ['more dangerous', 'dangerouser', 'most dangerous'], 'Comparatives'),
    ('(корова, свинья, курица) Which animal gives us milk?', ['a cow', 'a pig', 'a chicken'], 'Pets and farm animals')],
   'Вёрстку переделать: картинки животных крупно (замечание 20). Тигра нарисовать (промпт в чате).'),
  ('task', 'Задание 2. Голосовое сообщение', 'Listen and choose.', [],
   [('What did Tom ride?', ['a horse', 'a bike', 'a bus'], 'Past Simple'),
    ('Did he see the pigs?', ['No, he didn’t.', 'Yes, he did.', 'No, he don’t.'], 'Past Simple'),
    ('What did they do in the evening?', ['They watched a film.', 'They played football.', 'They went to bed.'], 'Past Simple')],
   'Все три вопроса сразу на одном экране.'),
  ('audio', 'This is Tom. Yesterday he went to his grandparents’ farm. In the morning he fed the chickens and the sheep. '
            'Then he rode a horse! He didn’t see the pigs, because they were asleep. In the evening they had a big dinner '
            'and watched a film. It was a great day!'),
  ('you', 'What did you do last weekend?', ['Past Simple'])]),
])

room('Часть 2 · Тайный кабинет (уровень A2.1–B1.1)', '2 цифры', [
 ('Шкаф', [
  ('name', "What's this? Describe it.", 'a big wooden wardrobe', 'Household and furniture, Adjectives to describe objects'),
  ('task', 'Задание 1. Спальня или кухня', 'Sort the pictures. Name them.', [],
   [('Bedroom: a bed, a chest of drawers · Kitchen: a fridge, a cooker', None, 'Household and furniture')],
   'Четыре картинки без подписей: ученик раскладывает и называет каждую вещь. Одежду здесь не проверяем — она была в части 1. Картинки нарисовать (промпт в чате).'),
  ('task', 'Задание 2. Загляни в шкаф', 'Choose the right word.', [],
   [('There aren’t ___ clothes in the wardrobe.', ['many', 'much', 'a'], 'Quantifiers'),
    ('My sister keeps ___ shoes in this wardrobe — more than fifty pairs!', ['a lot of', 'much', 'any'], 'Quantifiers')], ''),
  ('you', 'Describe your room.', ['Adjectives to describe objects'])]),
 ('Чемодан', [
  ('name', "What's this?", 'a suitcase', 'Holidays'),
  ('task', 'Задание 1. Как себя чувствовала Mia', 'Look. How did Mia feel?', ['hol_castle'],
   [('At the castle she was ___ .', ['excited', 'bored', 'angry'], 'Emotions')], ''),
  ('task', 'Задание 2. Рассказ Mia: найди ошибку', 'Right or wrong? Correct the mistakes.', [],
   [('Last summer we goed to Spain. → went', ['✘ False', '✔ True'], 'Past Simple'),
    ('Look at this photo! Here I take a photo of the castle. → I’m taking', ['✘ False', '✔ True'], 'Present Simple vs Present Continuous')], ''),
  ('you', 'Tell me about your best trip. Where did you go? How did you feel?', ['Holidays', 'Past Simple', 'Emotions'])]),
 ('Карта', [
  ('name', "What's this?", 'a map', 'Geographical features'),
  ('task', 'Задание 1. Соедини слова с картинками', 'Match the words and the pictures.', ['geo_river', 'geo_island', 'tr_sightseeing', 'tr_camping'],
   [('a river · an island · go sightseeing · go camping', None, 'Geographical features, Travelling activities')], ''),
  ('task', 'Задание 2. Путешествие', 'Choose the right answer.', ['tr_ferry', 'geo_mountains'],
   [('We crossed the sea ___ .', ['by ferry', 'on foot', 'by bike'], 'Ways of travelling'),
    ('Next summer we ___ climb these mountains. We’ve already bought the tickets.', ['are going to', 'might', 'will can'], 'Going to'),
    ('I’m not sure, but I ___ go to Italy next year.', ['might', 'am going to', 'must'], 'Future with will, may, might')], ''),
  ('you', 'What are you going to do this summer? Where would you like to travel?', ['Going to', 'Travelling activities'])]),
 ('Аптечка', [
  ('name', "What's this?", 'a first-aid kit', 'Health and Illnesses'),
  ('task', 'Задание 1. У врача', 'Choose the right answer.', [],
   [('— What’s the matter? — I’ve got a ___ . I ate too much.', ['stomachache', 'stomach', 'hurt'], 'Health and Illnesses'),
    ('I fell off my bike and now my ___ hurts. I can’t walk.', ['ankle', 'elbow', 'chin'], 'Body parts'),
    ('You ___ stay in bed for two days.', ['must', 'mustn’t', 'don’t have to'], 'Must, have to'),
    ('It’s Saturday tomorrow — you ___ go to school.', ['don’t have to', 'have to', 'mustn’t to'], 'Have to / don’t have to')], ''),
  ('you', 'What do you have to do at home? What must students do at your school?', ['Have to / don’t have to', 'Must, have to'])]),
 ('Книга', [
  ('name', "What's this?", 'a book (a novel)', 'Free time activities: books and films'),
  ('task', 'Задание 1. Отзыв о книге', 'Choose the right answer.', [],
   [('This book ___ by a 15-year-old girl in 2010.', ['was written', 'wrote', 'is writing'], 'Passive'),
    ('I love it! I ___ it three times.', ['have read', 'am reading', 'reads'], 'Present Perfect'),
    ('Kate and Sam are best friends, but then they ___ in love.', ['fall', 'get', 'make'], 'Relationships'),
    ('If you like adventures, you ___ love it.', ['will', 'would', 'are'], '1st Conditional')], ''),
  ('you', 'What’s the best book or film you’ve ever read or seen?', ['Present Perfect', 'Free time activities'])]),
 ('Плакат «Разыскивается»', [
  ('name', "What's this?", 'a poster (a wanted poster)', 'Crime and criminals'),
  ('task', 'Задание 1. Голосовое сообщение: найди вора', 'Listen and find the thief.', ['suspect_1', 'suspect_2', 'suspect_3', 'suspect_4'],
   [('Who is the thief? (четыре портрета)', None, 'Describing people'),
    ('What did the thief steal?', ['a painting', 'some money', 'a phone'], 'Crime and criminals'),
    ('What was he doing when the police arrived?', ['He was running to his car.', 'He runs to his car.', 'He is running to his car.'], 'Past Continuous')],
   'Все три вопроса сразу на одном экране.'),
  ('audio', 'Last night somebody broke into the museum and stole a famous painting. A witness saw the thief. He was tall, '
            'with curly dark hair and a beard, and he was wearing glasses and a black leather jacket. When the police arrived, '
            'he was running to his car.'),
  ('task', 'Задание 2. Что было в музее', 'Choose the right answer.', [],
   [('The thief ___ the painting when the alarm ___ .', ['was taking … rang', 'took … was ringing', 'was taking … was ringing'], 'Past Continuous vs Past Simple')],
   'Один вопрос с двумя пропусками.'),
  ('you', 'Describe someone in your family. What does he or she look like?', ['Describing people'])]),
 ('Кошелёк', [
  ('name', "What's this?", 'a wallet', 'Money and shopping'),
  ('task', 'Задание 1. Покупки', 'Choose the right answer.', [],
   [('I ___ any new clothes for two years.', ['haven’t bought', 'didn’t buy', 'don’t buy'], 'Present Perfect vs Past Simple'),
    ('I ___ my friends at the shopping centre at 5 tomorrow — it’s all arranged.', ['am meeting', 'meet', 'met'], 'Going to vs Present Continuous for future')], ''),
  ('you', 'What are you doing this weekend? What did you buy last time you went shopping?', ['Going to vs Present Continuous', 'Money and shopping'])]),
 ('Ноутбук', [
  ('name', "What's this?", 'a laptop', 'Computer phrases'),
  ('task', 'Задание 1. Переписка в чате: найди и исправь ошибку', 'Find the mistake and correct it.', [],
   [('Tom said that he is tired. → ошибка is, верно: was', None, 'Reported speech'),
    ('The boy which lives next door is my friend. → ошибка which, верно: who', None, 'Relative clauses')],
   'В каждом предложении есть ошибка. Ученик нажимает на неверное слово (балл ставится сам) и говорит правильный вариант вслух.'),
  ('you', 'What do you usually do on your computer or phone?', ['Computer phrases'])]),
 ('Бинокль', [
  ('name', "What are these?", 'binoculars', None),
  ('task', 'Задание 1. Еда в кафе напротив', 'Match the words and the pictures.', ['food_spicy', 'food_sour', 'food_sweet', 'food_salty'],
   [('spicy · sour · sweet · salty', None, 'Food and drink adjectives')], ''),
  ('task', 'Задание 2. Выбери слово', 'Choose the right word.', [],
   [('___ at that bird! It’s huge!', ['Look', 'See', 'Watch'], 'Look, see, watch'),
    ('If I had better binoculars, I ___ see the birds on that island.', ['would', 'will', 'am'], '2nd Conditional')], ''),
  ('you', 'If you had binoculars, what would you like to watch?', ['2nd Conditional', 'Look, see, watch'])]),
])

room('Часть 3 · Тайная лаборатория (уровень B1.2–B2.2)', '2 цифры', [
 ('Кубок', [
  ('name', "What's this? What is it for?", 'a trophy', 'Sport phrases'),
  ('task', 'Задание 1. Наша команда', 'Choose the best answer.', [],
   [('Would you like to ___ our tennis club?', ['join', 'enter', 'win'], 'Sport phrases'),
    ('___ is my favourite sport — I won this trophy last year.', ['Swimming', 'Swim', 'To swimming'], 'Ing forms'),
    ('I’m really good at ___ penalties.', ['scoring', 'score', 'to score'], 'Ing forms'),
    ('Nick ___ like snowboarding, but now he loves it.', ['didn’t use to', 'doesn’t used to', 'not used to'], 'Used to')], ''),
  ('you', 'What did you use to do when you were a child that you don’t do now?', ['Used to'])]),
 ('Стетоскоп', [
  ('name', "What's this? What is it for?", 'a stethoscope', None),
  ('task', 'Задание 1. У врача', 'Choose the best answer.', [],
   [('I fell down the stairs and ___ my ankle.', ['sprained', 'coughed', 'sneezed'], 'Health verbs'),
    ('You ___ go to bed earlier. You look really tired.', ['should', 'must to', 'have'], 'Modals of obligation and advice')], ''),
  ('you', 'What should people do to stay healthy? What do you do?', ['Modals of obligation and advice', 'Health verbs'])]),
 ('Микрофон', [
  ('name', "What's this? What is it for?", 'a microphone', None),
  ('task', 'Задание 1. Слова про музыку', 'Match the words and the definitions.', [],
   [('lyrics — the words of a song · a band — a group of musicians who play together · an album — a collection of songs released together', None, 'Music')], ''),
  ('you', 'What kind of music do you listen to? Have you ever been to a concert?', ['Music'])]),
 ('Смартфон', [
  ('name', "What's this? What is it for?", 'a smartphone', 'Social media'),
  ('task', 'Задание 1. Голосовое сообщение', 'Listen and choose.', [],
   [('What had Anna done before she suggested recording a video?', ['She had posted a photo online.', 'She had recorded a video.', 'She had met Jess at school.'], 'Past Perfect'),
    ('What did Anna suggest?', ['recording a video together', 'going to the cinema', 'taking more photos'], 'Reporting verbs'),
    ('Jess ___ Emma that Anna could be a great photographer.', ['told', 'said', 'spoke'], 'Verbs of communication')],
   'Все три вопроса сразу на одном экране.'),
  ('audio', 'Emma and Jess are best friends. Yesterday Emma saw a photo that Anna had posted online. Anna had taken it at sunset, '
            'and it was amazing. Jess had already seen it and had left a comment under it. She told Emma that Anna could be a great '
            'photographer. When Anna read the comments, she laughed and suggested recording a video together. Jess agreed, and they '
            'decided to meet on Sunday, because Jess doesn’t like putting things off.'),
  ('task', 'Задание 2. Телефон Анны', 'Choose the right answer.', [],
   [('Anna’s phone screen was broken, so ___ yesterday.', ['she had it repaired', 'she had repaired it', 'she have it repair'], 'Causative have')], ''),
  ('you', 'Have you ever had something repaired or done for you?', ['Causative have'])]),
 ('Шапочка выпускника', [
  ('name', "What's this? What is it for?", 'a graduation cap', 'Education'),
  ('task', 'Задание 1. Школа и университет', 'Choose the right answer.', [],
   [('Do you know where the exam room ___ ?', ['is', 'is it', 'does'], 'Question forms (complex)'),
    ('Our school is believed ___ more than 200 years ago.', ['to have been built', 'to build', 'building'], 'Passive: complex forms'),
    ('I get ___ really well with my classmates.', ['on', 'up', 'off'], 'Phrasal verbs for relationships')], ''),
  ('you', 'Do you know what you would like to study in the future? Why?', ['Education', 'Question forms (complex)'])]),
 ('Сейсмограф', [
  ('name', "What's this? What is it for?", 'a seismograph', 'Natural disasters'),
  ('task', 'Задание 1. Соедини слова с картинками', 'Match the words and the pictures.', ['dis_volcano', 'dis_flood', 'dis_earthquake'],
   [('a volcanic eruption · a flood · an earthquake', None, 'Natural disasters')], ''),
  ('task', 'Задание 2. Выбери ответ', 'Choose the right answer.', [],
   [('When the volcano erupted, most people ___ escape in time.', ['were able to', 'could to', 'can'], 'Modals of ability and possibility')], ''),
  ('you', 'What could you do to stay safe in an earthquake?', ['Modals of ability and possibility'])]),
 ('Лупа', [
  ('name', "What's this? What is it for?", 'a magnifying glass', 'Crime and criminals'),
  ('task', 'Задание 1. Место кражи', 'Look and choose.', ['crime_scene'],
   [('The broken glass is inside the room. The thief ___ through the window.', ['must have come', 'can’t have come', 'must come'], 'Modals of deduction in the past'),
    ('“Where were you last night?” → The detective asked me where I ___ the night before.', ['had been', 'have been', 'was being'], 'Reported questions'),
    ('“I didn’t take the money!” → The suspect ___ taking the money.', ['denied', 'admitted', 'suggested'], 'Reporting verbs'),
    ('If the window had been locked, the thief ___ in.', ['wouldn’t have got', 'won’t get', 'didn’t get'], '3rd conditional'),
    ('The owner always tells the truth. She is very ___ .', ['honest', 'selfish', 'lazy'], 'Personal qualities'),
    ('A person who breaks into a house and steals things is a ___ .', ['burglar', 'witness', 'judge'], 'Crime and criminals')], ''),
  ('you', 'What would you have done if you had been the detective?', ['3rd conditional'])]),
 ('Свиток', [
  ('name', "What's this? What is it for?", 'a scroll', 'History'),
  ('task', 'Задание 1. Разложи слова', 'Sort the words.', [],
   [('History: ancestor, century · Abstract nouns: freedom, honesty', None, 'History, Abstract nouns')], ''),
  ('task', 'Задание 2. История свитка', 'Choose the right answer.', [],
   [('An old man ___ along the beach when he found an ancient scroll.', ['was walking', 'walked', 'has walked'], 'Narrative tenses'),
    ('When I was little, my grandfather ___ tell me stories about our ancestors.', ['would', 'will', 'was'], 'Present and past habits')], ''),
  ('you', 'What did your grandparents use to do when they were young?', ['Present and past habits'])]),
 ('Капсула времени', [
  ('name', "What's this? What is it for?", 'a time capsule', 'Hopes and dreams'),
  ('task', 'Задание 1. Будущее', 'Look and choose.', ['fut_travel', 'fut_graduation'],
   [('This time next week Mia ___ to London.', ['will be flying', 'will have flown', 'flies'], 'Future Continuous'),
    ('By the end of the year they ___ from university.', ['will have graduated', 'will be graduate', 'graduated'], 'Future Perfect')], ''),
  ('you', 'What do you hope to achieve by the end of this year?', ['Hopes and dreams'])]),
 ('Рекламный щит', [
  ('name', "What's this? What is it for?", 'a billboard', 'Advertising'),
  ('task', 'Задание 1. Разложи слова', 'Sort the words.', [],
   [('Advertising: a slogan, a brand · Global issues: pollution, poverty · Online & media: a podcast, to stream', None, 'Advertising, Global issues, Online and media')], ''),
  ('task', 'Задание 2. Слоганы: собери половинки', 'Match the halves.', [],
   [('This new phone is great, but it costs … an arm and a leg.', None, 'Idioms'),
    ('Our new board game will help you break … the ice at any party!', None, 'Idioms'),
    ('The company could have chosen … a better slogan for this advert.', None, 'Modals in the past'),
    ('If I hadn’t seen that advert, … I wouldn’t be wearing these trainers now.', None, '3rd and mixed conditionals')], ''),
  ('task', 'Задание 3. Артикли', 'Choose a, an, the or —.', [],
   [('This is ___ best advert of the year!', ['the', 'a', '—'], 'Determiners'),
    ('It’s ___ advert for a new electric car.', ['an', 'a', 'the'], 'Determiners')], ''),
  ('you', 'Have you ever bought something because of an advert? If you hadn’t seen it, would you have bought it?', ['3rd and mixed conditionals'])]),
])

GREY = RGBColor(0x80, 0x80, 0x80)
GREEN = RGBColor(0x1F, 0x7A, 0x3A)
tmp = tempfile.mkdtemp()

def pic(name, w):
    src = os.path.join(MEDIA, name + '.webp')
    if not os.path.exists(src): return None
    p = os.path.join(tmp, name + '.png')
    if not os.path.exists(p):
        im = Image.open(src).convert('RGBA'); bg = Image.new('RGB', im.size, 'white'); bg.paste(im, mask=im.split()[3]); bg.save(p)
    return p

def run(par, text, bold=False, color=None, italic=False, size=None):
    r = par.add_run(text); r.bold = bold; r.italic = italic
    if color: r.font.color.rgb = color
    if size: r.font.size = Pt(size)
    return r

d = Document()
st = d.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(11)
for s in d.sections: s.left_margin = s.right_margin = Cm(2); s.top_margin = s.bottom_margin = Cm(1.6)
d.add_heading('Вводный урок 13+ после сокращения', 0)
p = d.add_paragraph(); run(p, 'Как читать. ', bold=True)
run(p, 'Каждая тема чек-листа проверяется 1–2 раза. «Назвать предмет» даёт балл, только если слово само из темы '
       '(мяч → Sports; паспорт к теме Countries не относится — её проверяют флаг и вопрос). Сортировка и «соедини пары» — '
       'одно задание: по теме считается раз. Верный вариант — ')
run(p, 'зелёный', bold=True, color=GREEN); run(p, ', на экране варианты перемешаны. Справа серым — тема чек-листа. '
       'На экране ученика — только короткая инструкция по-английски; русский заголовок задания — для учителя, он в плане.')
p = d.add_paragraph(); run(p, 'Начало урока: ', bold=True)
run(p, 'Welcome to WowSpeak School! → знакомство, три вопроса по одной карточке (What’s your name? How old are you? '
       'What do you like doing in your free time?) → учитель рассказывает историю квеста → комната 1.')

for title, code, objs in R:
    d.add_heading(title, 1)
    for k, (oname, els) in enumerate(objs, 1):
        d.add_heading(f'{k}. {oname}', 2)
        for e in els:
            if e[0] == 'name':
                p = d.add_paragraph(); run(p, 'Назвать: ', bold=True); run(p, e[1] + ' → '); run(p, e[2], bold=True, color=GREEN)
                run(p, '   ' + (e[3] or 'без балла'), color=GREY, size=9)
            elif e[0] == 'task':
                _, h, en, imgs, items, note = e
                p = d.add_paragraph(); run(p, h, bold=True); run(p, '   на экране: ', color=GREY, size=9); run(p, en, italic=True)
                if imgs == ['СХЕМА']:
                    p = d.add_paragraph(); run(p, '[картинка: семейное дерево — соберу из портретов, покажу превью]', italic=True, color=GREY)
                elif imgs:
                    p = d.add_paragraph(); w = Cm(16 / max(len(imgs), 2.5)) if len(imgs) > 1 else Cm(8)
                    for im in imgs:
                        f = pic(im, w)
                        if f: p.add_run().add_picture(f, width=w); p.add_run(' ')
                for n, (q, opts, t) in enumerate(items, 1):
                    p = d.add_paragraph(style='List Number' if False else None); p.paragraph_format.left_indent = Cm(0.8)
                    run(p, f'{n}) {q}')
                    if opts:
                        run(p, '  — '); run(p, opts[0], bold=True, color=GREEN)
                        if len(opts) > 1: run(p, ' / ' + ' / '.join(opts[1:]))
                    run(p, '   ' + t, color=GREY, size=9)
                if note:
                    p = d.add_paragraph(); p.paragraph_format.left_indent = Cm(0.8); run(p, note, italic=True, color=GREY, size=9)
            elif e[0] == 'audio':
                p = d.add_paragraph(); p.paragraph_format.left_indent = Cm(0.8); run(p, 'Текст записи: ', bold=True); run(p, e[1], italic=True)
            elif e[0] == 'you':
                p = d.add_paragraph(); run(p, 'And you? ', bold=True); run(p, e[1]); run(p, '   ' + ', '.join(e[2]), color=GREY, size=9)
        p = d.add_paragraph(); run(p, '→ кусочек записки', color=GREY, size=9)
    p = d.add_paragraph(); run(p, f'Записка собрана → код ({code}). ', bold=True)
    run(p, 'Экран с кодом: «Open the lock» — закончить урок, «Keep looking» — следующая часть.' if 'Часть 3' not in title
        else 'Ученик читает код вслух → дверь открыта, финал.')

d.save(OUT)
print(OUT)
