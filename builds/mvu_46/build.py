"""Сборка вводного урока 4–6 (Wow Dragon) → lessons/mvu_46/index.html + план в lessons/mvu_46/plans/.
python3 builds/mvu_46/build.py            — урок и html плана
python3 builds/mvu_46/build.py --docs     — ещё Word (LibreOffice) и PDF (Playwright)
"""
import json, os, re, sys, html, base64, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(REPO, 'lessons', 'mvu_46'); os.makedirs(OUT + '/plans', exist_ok=True)
SITE = 'https://classroom.wowteach.ru/lessons/mvu_46/plans/'
MEDIA = 'https://classroom.wowteach.ru/media/mvu_46/'
e = html.escape

# ── чек-лист Анны (Wow Dragon assessment chart), без строки «Базовые навыки чтения» (решение 24.11, «50») ──
CHECKLIST = [
    ('Wow Dragon 1 · Module 1', [('toys', 'Toys'), ('can', 'Can + Actions'), ('food', 'Food')]),
    ('Wow Dragon 1 · Module 2', [('school', 'School things'), ('clothes', 'Clothes'), ('have', 'Have / don’t have')]),
    ('Wow Dragon 1 · Module 3', [('rooms', 'Rooms + furniture'), ('prep', 'Prepositions of place (on / in / under / next to)'), ('habitats', 'Habitats')]),
    ('Wow Dragon 2 · Module 1', [('family', 'Family'), ('they', 'They are / aren’t'), ('pcont', 'Present Continuous')]),
    ('Wow Dragon 2 · Module 2', [('city', 'City places'), ('this', 'Demonstrative pronouns (this / that / these / those)'), ('travel', 'Travelling')]),
    ('Wow Dragon 2 · Module 3', [('planets', 'Planets'), ('tobe', 'To be (present)'), ('psimple', 'Present Simple (he / she / it + s)')]),
]
TOPIC_RU = {'toys': 'игрушки', 'can': 'can и действия', 'food': 'еда', 'school': 'школьные принадлежности', 'clothes': 'одежда',
            'have': 'have / don’t have', 'rooms': 'комнаты и мебель', 'prep': 'предлоги места (on, in, under, next to)',
            'habitats': 'где живут животные', 'family': 'семья', 'they': 'they are / they aren’t', 'pcont': 'Present Continuous (что делает сейчас)',
            'city': 'места в городе', 'this': 'this / that / these / those', 'travel': 'путешествия', 'planets': 'планеты',
            'tobe': 'глагол to be', 'psimple': 'Present Simple (he / she / it + s)'}
PASS = 4   # модуль пройден, если 4 из 6 и больше (решение Анны 27.11.2026, «56 да»)

# ── экраны: название для преподавателя, вопросы и ожидаемые ответы, темы ──
SCREEN_RU = {'hello': 'Привет', 'dragon': 'Дракоша', 'map': 'Карта', 'room': 'Дом: собираем рюкзак', 'teddy': 'Дом: где мишка?',
             'missing': 'Дом: что пропало?', 'key_red': 'Красный ключ', 'forest': 'Лес', 'bushes': 'Лес: кто в кустах?',
             'riddle': 'Лес: загадка и дерево', 'key_blue': 'Голубой ключ', 'park': 'Парк', 'says': 'Парк: Дракоша говорит',
             'feed': 'Парк: покорми бабушку', 'key_green': 'Зелёный ключ', 'launch': 'Космос: отсчёт', 'space': 'Космос: планеты',
             'key_yellow': 'Жёлтый ключ', 'jungle': 'Джунгли: сундук', 'bye': 'Финал'}
P = lambda q, a='', *t: dict(q=q, a=a, topics=list(t))
PROMPTS = {
    'hello': [P('Hi! What’s your name? How are you?', 'I’m Masha. / I’m fine.')],
    'dragon': [P('Look! Is he happy or sad? (нажмите на Дракошу — станет грустным) Are you happy?', 'He’s happy. / He’s sad. / I’m happy.', 'tobe'),
               P('What is it? (свиток справа)', 'It’s a map.')],
    'map': [P('What is it? Is it a house or a park? Where do you live — in a house or a flat? Is there a park near your house?', 'It’s a house. / It’s a park. / I live in a flat.', 'city')],
    'room': [P('What room is it? Is it a bathroom or a bedroom? What is it? (bed, wardrobe, desk, chair)', 'It’s a bedroom. / It’s a bed.', 'rooms'),
             P('What is it? Is it a car or a plane? (игрушки)', 'It’s a car. / It’s a teddy bear.', 'toys'),
             P('What is it? (pencil, book, ruler)', 'It’s a pencil.', 'school'),
             P('What is it? (T-shirt, hat, socks, sneakers)', 'It’s a hat. / They’re socks.', 'clothes'),
             P('What do you have in your bag? Let’s say: I have a car! Do you have a robot at home?', 'I have a car. / No, I don’t have a robot.', 'have')],
    'teddy': [P('Where’s the teddy? Is it on the bed or under the bed? (нажмите на мишку — он перепрыгнет)', 'It’s {teddy}.', 'prep')],
    'missing': [P('Close your eyes! … What’s missing?', 'The {missing}!', 'toys')],
    'key_red': [P('It’s a key! What colour is the key? (нажмите на ключ — он улетит в связку)', 'It’s red.')],
    'forest': [P('Look! What is it: jungle or forest?', 'It’s a forest.'),
               P('What is it? Is it a cat? Where does it live? (в лесу, на дереве, в пруду)', 'It’s a fox. / It lives in the forest.', 'habitats'),
               P('What are they? Are they cats? (пары: утята, лягушки, котята, зайчики)', 'They are ducks. / No, they aren’t.', 'they'),
               P('Where is the owl? Where is the squirrel?', 'It’s in the tree. / It’s on the tree.', 'prep'),
               P('What’s this? (котята — близко) What’s that? (медведь — далеко)', 'These are kittens. / That’s a bear.', 'this')],
    'bushes': [P('Who’s behind the bush? (нажмите на куст — зверь выглянет)', 'It’s a fox!')],
    'riddle': [P('I’m small. I’m blue. I can fly. Who am I?', 'A butterfly!', 'can'),
               P('Let’s be trees! Hands up, shake! (нажмите на дерево три раза — ключ упадёт)', '—')],
    'key_blue': [P('What colour is the key?', 'It’s blue.')],
    'park': [P('Who’s this? Is it Granny? Who’s in your family?', 'It’s Granny. / This is my mum.', 'family'),
             P('What is it? Is it a bird? Can it fly? Can it swim? What can you do?', 'Yes, it can. / I can run.', 'can'),
             P('What is he doing? What is she doing?', 'He’s running. / She’s eating ice cream.', 'pcont')],
    'says': [P('Dragon says: {says}! (ребёнок делает движение и говорит: I can {says}) — нажмите на Дракошу, будет следующее', 'I can {says}!', 'can')],
    'feed': [P('Listen and feed Granny! (Next — послушать, ребёнок показывает еду; Next ещё раз — дать верную)', 'Баллы ставит игра.'),
             P('What do you like?', 'I like pizza.', 'food'),
             P('What does Granny like? What does your mum like?', 'She likes fish. / My mum likes cake.', 'psimple')],
    'key_green': [P('What colour is the key?', 'It’s green.')],
    'launch': [P('Let’s count! Ten, nine, eight… (нажимайте на число, на нуле ракета улетит)', 'ten, nine, eight… one!')],
    'space': [P('Look! What is it? (планеты)', 'It’s a planet. / It’s the Earth. / It’s the Moon.', 'planets'),
              P('How many stars? Let’s count.', '{stars} stars'),
              P('Is it hot or cold? (красная и ледяная планеты, в иллюминаторе)', 'It’s hot. / It’s cold.', 'tobe'),
              P('What is it? (открытка на красной планете, ракета на Луне)', 'It’s a postcard. / It’s a rocket.', 'travel'),
              P('Where do you go on holiday? How do you travel?', 'By plane. / By car.', 'travel')],
    'key_yellow': [P('Hooray! We have all the keys! Where did we find them?', 'In the house, in the park, in the forest, in space.')],
    'jungle': [P('Which key? What colour is it? (ребёнок называет цвет — нажмите на этот ключ)', 'The red key!'),
               P('What is it?', 'It’s a book!')],
    'bye': [P('Did you like it? What did you like? (по-русски: что понравилось, что нет, чего не хватило)', '—')],
}
NOTE = {'feed': 'Еду урок считает сам: верно с первого раза — балл, иначе — нет. Кнопка 🔊 повторяет фразу.',
        'map': 'Порядок: дом → парк → лес → космос → джунгли. Светится следующее место, пройденные — с галочкой. Next ведёт туда сам.',
        'space': 'Слабым: посчитать звёзды или планеты и нажать «⏭ Skip» — ключ выдастся сразу.',
        'jungle': 'Если ключей меньше четырёх, сундук не откроется — вернитесь на карту.'}
ALL = {t for _, ts in CHECKLIST for t, _ in ts}
used = {t for ps in PROMPTS.values() for p in ps for t in p['topics']} | {'food'}
if ALL - used: sys.exit('!! темы без вопроса: ' + str(ALL - used))

# ── картинки: всё, что упомянуто в шаблоне, должно лежать в media/mvu_46 ──
tpl = open(os.path.join(HERE, 'template.html')).read()
names = set(re.findall(r"'((?:bg|obj|hero)/[a-z0-9_]+)'", tpl))
names |= {'obj/' + f for f in ['pizza', 'broccoli', 'icecream', 'fish', 'cake', 'apple', 'banana', 'carrot']}
names |= {'obj/key_' + c for c in ['red', 'blue', 'green', 'yellow']} | {'obj/porthole_' + k for k in ['red', 'ice', 'moon', 'earth']} | {'obj/bush' + str(i) for i in (1, 2, 3)}
names = {n for n in names if not n.endswith('_') and n not in ('obj/bush', 'obj/kid_swingset', 'obj/teddy_box')}
missing = sorted(n for n in names if not os.path.exists(os.path.join(REPO, 'media', 'mvu_46', n + '.webp')))
if missing: sys.exit('!! нет картинок: ' + str(missing))

# ── звук «I like …»: синтез голосом en_US-amy (Piper), внутри страницы — 8 фраз по 12 КБ ──
AUD = os.path.join(HERE, 'audio')
audio = {f[:-4]: 'data:audio/mpeg;base64,' + base64.b64encode(open(os.path.join(AUD, f), 'rb').read()).decode() for f in sorted(os.listdir(AUD)) if f.endswith('.mp3')}

# ── план урока ──
rows = []
def row(step, do, tl, ru, exp):
    rows.append(f'<tr><td class="st">{step}</td><td>{do}</td><td class="tl">{tl}<br><span class="ru">{ru}</span></td><td class="sa">{exp}</td></tr>')
def part(t): rows.append(f'<tr class="part"><td colspan="4">{t}</td></tr>')
N = '<b>Next:</b> '
row('1. Привет', 'Представьтесь, спросите имя. Скажите, что это игра и оценок нет; если ребёнок чего-то не знает, можно сказать «I don’t know». Узнайте, с чего он занимается: телефон, планшет, компьютер.',
    'Hi! My name is … Today we have an adventure! What’s your name?', 'Привет! Меня зовут … Сегодня у нас урок-приключение! Как тебя зовут?', 'I’m Masha.')
row('2. Дракоша', 'Познакомьте с Дракошей, не забывайте TPR: показывайте «happy» и «sad» лицом. ' + N + 'Дракоша грустит → снова радуется → карта в руке подпрыгивает → дальше.',
    'Look! This is Wow Dragon. Is he happy or sad? Are you happy?', 'Это Волшебный Дракоша. Он весёлый или грустный? А ты?', 'He’s happy. I’m happy.')
row('3. История', 'Расскажите историю. Для сильных — спросите, что у Дракоши в руках.',
    'Dragons guard treasure. Repeat: treasure! Dragon found an old treasure map. Let’s find four keys and open the treasure chest!',
    'Драконы охраняют сокровища. Повтори: treasure! Дракоша нашёл старую карту сокровищ. Найдём четыре ключа и откроем сундук!', 'It’s a map. Treasure!')
part('🗺 КАРТА — порядок мест: дом → парк → лес → космос → джунгли')
row('Карта', 'Дракоша стоит в углу карты. Следующее место светится — туда и идём. Пройденные места отмечены галочкой и ключом. ' + N + 'Дракоша идёт в светящееся место. Кнопка «🗺 Map» внизу слева в любой момент возвращает на карту.',
    'Look! What is it? Is it a house or a park? Where do you live? Let’s go!', 'Что это? Дом или парк? А ты где живёшь? Пойдём!', 'It’s a house. / It’s a park.')
part('🏠 1. ДОМ — красный ключ')
row('Собираем рюкзак', 'Предметы светятся. Ребёнок называет предмет — он улетает в рюкзак Дракоши. Спрашивайте и про комнату, и про то, что в рюкзаке. ' + N + 'следующий предмет летит в рюкзак.',
    'What room is it? What is it? Is it a car or a plane? What do you have in your bag? Let’s say: I have a car!',
    'Что это за комната? Что это? Машинка или самолёт? Что у тебя в рюкзаке? Скажи: I have a car!', 'It’s a bedroom. It’s a car. I have a ball.')
row('Где мишка?', 'Мишка сидит в разных местах: на кровати, под кроватью, под столом, в коробке, рядом со стулом, на стуле. ' + N + 'мишка перепрыгивает на новое место.',
    'Where’s the teddy? Is it on the bed or under the bed?', 'Где мишка? На кровати или под кроватью?', 'It’s on the bed. It’s under the table.')
row('Что пропало?', 'Пять вещей из рюкзака. ' + N + 'закрыть глаза — одна вещь пропадает; ещё Next — показать ответ. Два раунда.',
    'Close your eyes! … Open! What’s missing?', 'Закрой глазки! … Открой! Чего не хватает?', 'The ball!')
row('Ключ', N + 'ключ улетает в связку вверху; ещё Next — на карту.', 'You did it! It’s a key! What colour is the key?', 'Молодец! Это ключ! Какого он цвета?', 'It’s red.')
part('🌸 2. ПАРК — зелёный ключ')
row('Парк', 'Бабушка Дракоши на лавочке, вокруг дети, по небу летит птица. ' + N + 'герои по очереди подпрыгивают — спрашивайте про каждого.',
    'Who’s this? Is it Granny? What is it? Is it a bird? Can it fly? Can it swim? What can you do? What is he doing?',
    'Кто это? Бабушка? Что это? Птица? Она умеет летать? А плавать? Что умеешь ты? Что он делает?', 'It’s Granny. It can fly. I can run. He’s running.')
row('Дракоша говорит', 'Игра на движение: вы говорите команду, ребёнок выполняет и говорит «I can jump!». ' + N + 'следующее движение (прыгать, плавать, летать, бегать, танцевать, хлопать).',
    'Dragon says: jump! Can you jump?', 'Дракоша говорит: прыгай! Ты умеешь прыгать?', 'I can jump!')
row('Покорми бабушку', 'Бабушка голодная и плачет. Четыре раунда: бабушка говорит, что любит, ребёнок показывает еду. Верно — еда летит на тарелку и бабушка её ест; неверно — бабушка морщится. Баллы за еду игра ставит сама. '
    + N + 'послушать фразу; ребёнок показывает; ещё Next — бабушка получает верную еду. Кнопка «⏭ Skip» внизу слева — сразу к ключу.',
    'Granny is hungry! Listen! What does Granny like? What do you like? What does your mum like?',
    'Бабушка голодная! Послушай! Что любит бабушка? А ты что любишь? А что любит мама?', 'She likes fish. I like pizza. My mum likes cake.')
row('Ключ', N + 'ключ в связку; ещё Next — на карту.', 'Thank you! Here is a key! What colour is the key?', 'Спасибо! Вот ключ! Какого он цвета?', 'It’s green.')
part('🌳 3. ЛЕС — голубой ключ')
row('Лес', 'Звери поодиночке и парами. Спрашивайте, кто это, где живёт и где сидит. Медведь вдали — для «that», котята впереди — для «these». ' + N + 'звери по очереди подпрыгивают.',
    'What is it: jungle or forest? What is it? Is it a cat? What are they? Are they cats? Where is the owl? What’s this? What’s that?',
    'Это джунгли или лес? Что это? Это кошка? Кто это (их двое)? Это кошки? Где сова? Что это (близко)? А что там (далеко)?', 'It’s a fox. They are ducks. It’s in the tree. That’s a bear.')
row('Кто в кустах?', 'Пусть ребёнок угадает, кто прячется. ' + N + 'из-за следующего куста выглядывает зверь.', 'Who’s behind the bush? Is it a fox?', 'Кто прячется в кустах? Лиса?', 'It’s a fox! It’s a rabbit!')
row('Загадка и дерево', 'Ключ висит на ветке, Дракоше не достать. Загадка с TPR: small — показать маленькое, blue — синее, fly — помахать руками. Ребёнок выбирает ответ — ключ опускается, но всё ещё высоко. «Станем деревьями»: руки вверх и трясём. '
    + N + 'верный ответ (бабочка), потом три встряски — ключ падает. «⏭ Skip» — сразу к ключу.',
    'I’m small. I’m blue. I can fly. Who am I? It’s too high! Let’s be trees! Hands up! Shake, shake, shake!',
    'Я маленькая, синяя, умею летать. Кто я? Высоко! Давай станем деревьями: руки вверх и трясём!', 'A butterfly!')
row('Ключ', N + 'ключ в связку; ещё Next — на карту.', 'Hooray! Another key! What colour is the key?', 'Ура, ещё один ключ! Какого цвета?', 'It’s blue.')
part('🚀 4. КОСМОС — жёлтый ключ')
row('Отсчёт', 'Космос проходят все. Считайте вместе от 10 до 1. ' + N + 'минус один; на нуле ракета улетает.',
    'Let’s count! Ten, nine, eight… one! Blast off!', 'Считаем вместе! Десять, девять… один! Полетели!', 'ten, nine… one!')
row('Планеты', 'Слабым — посчитать звёзды или планеты и нажать маленькую кнопку «⏭ Skip» внизу слева: жёлтый ключ выдаётся сразу. Сильным — ещё и иллюминаторы: на красной планете открытка, на ледяной — ничего, на Луне — ракета, на Земле — жёлтый ключ. '
    + N + 'открыть следующую планету / закрыть иллюминатор; после Земли — ключ.',
    'Look! What is it? How many stars? Let’s count! Is it hot or cold? What is it? Where do you go on holiday? How do you travel?',
    'Что это? Сколько звёзд? Считаем! Тут жарко или холодно? Что это? Куда ты ездишь отдыхать? На чём?', 'It’s a planet. Seven stars! It’s cold. It’s a postcard. By plane.')
row('Все ключи', 'Вспомните, где нашли каждый ключ. ' + N + 'ключ в связку; ещё Next — на карту.', 'Hooray! We have all the keys! Where did we find them?', 'Ура! Все ключи у нас! Где мы их нашли?', 'In the house, in the park…')
part('🌴 5. ДЖУНГЛИ — сундук')
row('Сундук', 'Ребёнок называет цвет — ключ этого цвета летит в свою скважину. Когда вставлены все четыре, сундук открывается, в нём волшебная книга. ' + N + 'следующий ключ в скважину; потом — финал.',
    'Look! A treasure chest! What’s in it? Gold? Which key? What colour? What is it?',
    'Смотри, сундук с сокровищами! Что там? Золото? Какой ключ? Какого цвета? Что это?', 'The red key! It’s a book!')
row('🎉 Финал', 'Это книга английского — наше сокровище, с Дракошей будем учиться дальше. Спросите по-русски, что понравилось и что нет, чего не хватило. Обязательно позовите родителя. Отчёт — в окне ✅ внизу.',
    'Well done! It’s a magic English book! Did you like it? Bye-bye!', 'Молодец! Это волшебная книга английского! Тебе понравилось? Пока!', '—')
MUST = [
    ('Окна', 'Вверху урока две кнопки: ✅ открывает чек-лист, 📋 — этот план. Оба открываются отдельными окнами: держите их у себя, ученику показывайте только экран урока (демонстрация экрана со звуком). В чек-листе сразу впишите имя, пол и возраст — они попадут в отчёт.'),
    ('Как идёт урок', 'Дракоша нашёл карту сокровищ. Идём по местам строго по порядку: дом → парк → лес → космос → джунгли. На карте светится то место, куда идти сейчас. В каждом месте ребёнок отвечает на вопросы и играет, а в конце получает ключ. Ключи собираются в связку вверху слева, четыре ключа открывают сундук в джунглях.'),
    ('Кнопка Next', 'Ведите урок кнопкой Next — она делает следующий шаг в сцене: Дракоша грустит и радуется, предмет летит в рюкзак, мишка перепрыгивает, ключ улетает в связку, открывается планета. Так ничего не пропустится. Нажимать на сами предметы тоже можно. В плане ниже у каждого шага написано, что делает Next.'),
    ('Кнопка Skip', 'Маленькая кнопка «⏭ Skip» внизу слева есть там, где ключ выдаётся только после задания: бабушка в парке, загадка в лесу, отсчёт и планеты в космосе. Если ребёнку трудно, нажмите её — ключ выдастся сразу, урок пойдёт дальше.'),
    ('Слабый ученик', 'Если ребёнок совсем ничего не знает, не мучаем: проходим ту же историю в обучающем формате — вместо вопросов цвета, числа, названия мест. Переключиться можно в любой момент. Сокровище находим всегда; в космосе слабые считают звёзды или планеты, дальше — «⏭ Skip».'),
    ('Баллы', 'Устные ответы оцениваете вы: вверху чек-листа есть рамка «Сейчас на экране» — в ней вопрос, ожидаемый ответ и кнопки 0 / 1 / 2. Еду в игре «Покорми бабушку» урок считает сам. Любой балл можно поменять прямо в таблице — ваш заменит посчитанный.'),
    ('Метки 🔎', 'У каждой темы в чек-листе стоит метка 🔎 с местом, где её проверяют. Нажатие сразу открывает это место в уроке — удобно, если какую-то тему пропустили.'),
    ('Отчёт', 'Отчёт — внизу окна ✅: что ребёнок знает уверенно, с чем знаком, чего пока не знает и какой модуль ему рекомендуется (модуль пройден при 4 из 6 баллов и больше). Отчёт можно править прямо в окне, потом нажмите «Скопировать отчёт». Обязательно позовите родителя.'),
    ('Если ребёнок не понимает английский', 'Историю и инструкции можно говорить по-русски — русский вариант стоит в колонке «Teacher’s language» под английским.'),
]
PLAN_INNER = (
    '<h1 style="color:#4f2a9a;margin:4px 0 10px">🐉 План урока: Wow Dragon — Treasure Quest (вводный урок 4–6)</h1>'
    f'<p class="dl"><a href="{SITE}mvu_46_plan.docx" download>⬇ Скачать план (Word)</a><a class="pdf" href="{SITE}mvu_46_plan.pdf" download>⬇ Скачать план (PDF)</a></p>'
    '<div class="must"><h2>❗ Как работать с уроком — прочитайте обязательно</h2>' + ''.join(f'<p><b>{h}.</b> {x}</p>' for h, x in MUST) + '</div>'
    '<table class="plan"><tr><th>Шаг</th><th>Что делать</th><th>Teacher’s language</th><th>Ожидаемые ответы</th></tr>' + ''.join(rows) + '</table>'
)
PLAN_STYLE = ('.must{background:#fff0ee;border:3px solid #d32f2f;border-radius:12px;padding:8px 18px 6px;margin:10px 0 16px}.must h2{margin:4px 0 8px;color:#c62828;font-size:18px}.must p{margin:6px 0;line-height:1.45}.ru{color:#555;font-style:normal}'
              'table.plan td.st{font-weight:700;white-space:nowrap}table.plan td.tl{color:#5a2d9a;font-style:italic;width:28%}'
              'table.plan td.sa{color:#1f5fa8;width:18%}table.plan tr.part td{background:#4f2a9a;color:#ffe07a;font-weight:700}')
PLAN_HEAD = ("body{font-family:'Segoe UI',Arial,sans-serif;background:#f4effb;color:#2a1a3a;padding:18px 22px;max-width:1200px;margin:0 auto;font-size:14px}"
             'table{border-collapse:collapse;width:100%;background:#fff}th,td{border:1px solid #d8cbee;padding:5px 8px;vertical-align:top}th{background:#7b4bd6;color:#fff;text-align:left}'
             '.dl a{display:inline-block;margin:0 8px 10px 0;padding:8px 16px;border-radius:10px;background:#7b4bd6;color:#fff;font-weight:700;text-decoration:none}.dl a.pdf{background:#e8631a}')

EAT = [f for f in ['pizza', 'broccoli', 'icecream', 'fish', 'cake', 'apple', 'banana', 'carrot'] if os.path.exists(os.path.join(REPO, 'media', 'mvu_46', 'hero', 'granny_eat_' + f + '.webp'))]
names |= {'hero/granny_eat_' + f for f in EAT}
BIRD = 'obj/bird_fly' if os.path.exists(os.path.join(REPO, 'media', 'mvu_46', 'obj', 'bird_fly.webp')) else 'obj/bird'
names.add(BIRD)
SWING = os.path.exists(os.path.join(REPO, 'media', 'mvu_46', 'obj', 'kid_swingset.webp'))
if SWING: names.add('obj/kid_swingset')
TBOX = os.path.exists(os.path.join(REPO, 'media', 'mvu_46', 'obj', 'teddy_box.webp'))
if TBOX: names.add('obj/teddy_box')
D = dict(media=MEDIA, audio=audio, eat=EAT, bird=BIRD, swingset=SWING, teddybox=TBOX, pass_=PASS,
         checklist=[dict(title=t, topics=[[i, n] for i, n in ts]) for t, ts in CHECKLIST],
         topic_ru=TOPIC_RU, prompts=PROMPTS, screen_ru=SCREEN_RU, note=NOTE, preload=sorted(names))
D['pass'] = D.pop('pass_')
D['mw_html'] = open(os.path.join(HERE, 'manager.html')).read()
D['plan_html'] = ('<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><title>План урока — Wow Dragon 4–6</title><style>'
                  + PLAN_HEAD + PLAN_STYLE + '</style></head><body>' + PLAN_INNER + '</body></html>')
page = tpl.replace('/*DATA*/null', json.dumps(D, ensure_ascii=False).replace('</', '<\\/'))
open(os.path.join(OUT, 'index.html'), 'w').write(page)
print('index.html', len(page) // 1024, 'KB,', len(names), 'картинок,', len(audio), 'фраз')

plan_html = ('<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><title>План урока — Wow Dragon 4–6</title><style>'
             'body{font-family:Arial,sans-serif;color:#2a1a3a;font-size:11pt}table{border-collapse:collapse;width:100%}'
             'th,td{border:1px solid #bfb3d6;padding:4px 6px;vertical-align:top}th{background:#7b4bd6;color:#fff}' + PLAN_STYLE + '</style></head><body>'
             + re.sub(r'<p class="dl">.*?</p>', '', PLAN_INNER) + '</body></html>')
open(os.path.join(OUT, 'plans', 'mvu_46_plan.html'), 'w').write(plan_html)
if '--docs' in sys.argv:
    d = os.path.join(OUT, 'plans')
    subprocess.run(['soffice', '--headless', '--convert-to', 'docx:MS Word 2007 XML', '--outdir', d, os.path.join(d, 'mvu_46_plan.html')], check=True, capture_output=True)
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();"
          f"await p.goto('file://{d}/mvu_46_plan.html');await p.pdf({{path:'{d}/mvu_46_plan.pdf',format:'A4',landscape:true,printBackground:true,"
          "margin:{top:'10mm',bottom:'10mm',left:'10mm',right:'10mm'}});await b.close();})();")
    subprocess.run(['node', '-e', js], check=True)
    print(sorted(os.listdir(d)))
