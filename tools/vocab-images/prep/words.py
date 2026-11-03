"""Prepare: пробелы в картинках (Анна, 02.11.2026: «ок»). Слова без картинки в непредметных колодах
грамматики (Linking words, Irregular verbs, наречия, Expressions with at/in, Number expressions…)
не рисуем. WORDS: (term ровно как в базе, подпись на листе, что нарисовать, колода)."""
DOC = 'Экраны, бумаги и документы — вместо букв волнистые линии; никаких настоящих слов, вывесок и табличек.'
MONEY = 'На деньгах нет лиц и портретов — только цветы, здания и цифры номинала.'
HEAD = 'У каждого человека одна голова и обычная анатомия.'
BRAND = 'Все вещи и персонажи придуманные: без логотипов, марок, известных героев и талисманов.'
DIG = 'Цифры рисовать только там, где сказано.'

W = [
 # Prepare 2 · City tourism / Geography / Weather / Phrasal verbs
 ('cycle tour', 'cycle tour', 'Группа туристов в шлемах едет на велосипедах за гидом мимо старинных домов', 'City tourism'),
 ('walking tour', 'walking tour', 'Гид с поднятым флажком ведёт пешую группу туристов по старой улице', 'City tourism'),
 ('deep', 'deep', 'Глубокое озеро в разрезе: дно далеко внизу, водолаз опускается вглубь', 'Geography'),
 ('icy', 'icy', 'Обледеневшая дорожка, мальчик в шапке осторожно идёт, на ветках сосульки', 'Weather'),
 ('pick up', 'pick up', 'Мальчик наклонился и поднимает с пола упавшую варежку', 'Phrasal verbs'),
 # Prepare 2 · Online actions
 ('buy clothes', 'buy clothes', 'Девочка на планшете выбирает футболку, кладёт её в значок-корзину', 'Online actions'),
 ('chat to friends', 'chat to friends', 'Девочка переписывается с друзьями в телефоне, на экране облачка со смайликами', 'Online actions'),
 ('digital', 'digital', 'Цифровые устройства в ряд: цифровой фотоаппарат, планшет и электронная книга с экранами', 'Online actions'),
 ('download music', 'download music', 'На экране ноутбука стрелка вниз, из неё в наушники летят ноты', 'Online actions'),
 ('download videos', 'download videos', 'На экране планшета стрелка вниз и значок видео с треугольником «плей»', 'Online actions'),
 ('machine', 'machine', 'Большое умное устройство с кнопками, экранчиком и лампочками на столе', 'Online actions'),
 ('memory', 'memory', 'Карта памяти и флешка крупно рядом с ноутбуком', 'Online actions'),
 ('software', 'software', 'Экран компьютера с окнами программ и цветными значками', 'Online actions'),
 ('virus', 'virus', 'Мультяшный зелёный жучок-вирус на экране ноутбука, красный тревожный треугольник', 'Online actions'),
 ('visit websites', 'visit websites', 'Мальчик листает на ноутбуке страницы сайтов с картинками и полосками вместо текста', 'Online actions'),
 ('watch videos', 'watch videos', 'Двое детей на диване смотрят видео на планшете и смеются', 'Online actions'),
 # Prepare 3 · Big numbers
 ('thousand', 'thousand', 'Число 1000 из ярких объёмных цифр', 'Big numbers'),
 ('billion', 'billion', 'Число 1 000 000 000 из ярких объёмных цифр в одну строку', 'Big numbers'),
 # Prepare 4 · Noun and verb pairs / Say, speak, talk, tell
 ('cost (noun)', 'cost (noun)', 'Ценник с монетками висит на новом велосипеде', 'Noun and verb pairs'),
 ('cost (verb)', 'cost (verb)', 'Мальчик смотрит на игрушечную машинку в витрине и считает монеты на ладони — хватит ли', 'Noun and verb pairs'),
 ('pay (noun)', 'pay (noun)', 'Работник получает конверт с зарплатой от начальницы', 'Noun and verb pairs'),
 ('pay (verb)', 'pay (verb)', 'Девочка платит кассиру монетами за яблоки', 'Noun and verb pairs'),
 ('charge (noun)', 'charge (noun)', 'Окошко кассы у входа в музей, посетитель протягивает монеты за вход', 'Noun and verb pairs'),
 ('charge (verb)', 'charge (verb)', 'Продавец берёт с покупателя монетку за бумажный пакет', 'Noun and verb pairs'),
 ('speak a language', 'speak a language', 'Девочка разговаривает с иностранным гостем, над ними облачка с флажками разных стран без надписей', 'Say / speak / talk / tell'),
 # Prepare 5 · Word families
 ('achievement', 'achievement', 'Девочка на вершине горы поднимает флаг', 'Word families'),
 ('entertainer', 'entertainer', 'Весёлый артист жонглирует на детском празднике', 'Word families'),
 ('entertaining', 'entertaining', 'Дети хохочут на кукольном спектакле', 'Word families'),
 ('entertainment', 'entertainment', 'Парк развлечений: карусель, колесо обозрения, огни', 'Word families'),
 ('record (noun)', 'record (noun)', 'Виниловая пластинка рядом с проигрывателем', 'Word families'),
 ('record (verb)', 'record (verb)', 'Девочка поёт в микрофон, на телефоне горит красная кнопка записи', 'Word families'),
 ('musical', 'musical', 'Музыкальная семья: каждый играет на своём инструменте', 'Word families'),
 ('perform', 'perform', 'Мальчик выступает на сцене с гитарой, зрители аплодируют', 'Word families'),
 # Prepare 6 · Word families / Personal qualities / Formal verbs / Permission
 ('difference', 'difference', 'Две почти одинаковые картинки с домиком, отличие обведено красным кружком', 'Word families (noun ↔ adjective)'),
 ('generosity', 'generosity', 'Мальчик отдаёт свой зонт промокшей девочке', 'Word families (noun ↔ adjective)'),
 ('happiness', 'happiness', 'Семья смеётся, обнявшись на пикнике', 'Word families (noun ↔ adjective)'),
 ('importance', 'importance', 'В календаре один день обведён ярким красным кругом со звездой', 'Word families (noun ↔ adjective)'),
 ('organisation', 'organisation', 'Аккуратный стол: всё разложено по коробкам и стопкам', 'Word families (noun ↔ adjective)'),
 ('patience', 'patience', 'Рыбак спокойно сидит с удочкой и ждёт клёва', 'Word families (noun ↔ adjective)'),
 ('qualification', 'qualification', 'Выпускница получает диплом с печатью и лентой', 'Word families (noun ↔ adjective)'),
 ('qualified', 'qualified', 'Опытный электрик в каске уверенно чинит щиток, на стене его диплом', 'Word families (noun ↔ adjective)'),
 ('fit', 'fit', 'Подтянутая девушка в спортивной форме бодро бежит по парку', 'Word families (noun ↔ adjective)'),
 ('sense', 'sense', 'Собака-ищейка принюхивается к следу на тропинке', 'Personal qualities'),
 ('spirit', 'spirit', 'Команда в одинаковой форме обнимается и кричит перед игрой, все горят задором', 'Personal qualities'),
 ('influence', 'influence', 'Младшая сестра повторяет за старшей её причёску и позу', 'Formal verbs'),
 ('be allowed to', 'be allowed to', 'Мама кивает, и мальчик радостно бежит гулять на площадку', 'Permission and obligation'),
 ('let (sb do sth)', 'let', 'Папа даёт дочке самой порулить игрушечным катером в пруду', 'Permission and obligation'),
 ('make (sb do sth)', 'make', 'Мама строго показывает на тарелку, мальчик нехотя ест брокколи', 'Permission and obligation'),
 # Prepare 7
 ('decade', 'decade', 'Лента времени: десять кружков-лет, один и тот же мальчик растёт от малыша до подростка', 'History and society'),
 ('personality', 'personality', 'Три разных ребёнка: весёлый, задумчивый и шумный, у каждого своё облачко-символ', 'Personality and qualities'),
 ('nature', 'nature', 'Добрый по натуре мальчик кормит бездомного котёнка', 'Word families (noun forms)'),
 ('version', 'version', 'Два рисунка одного и того же замка: простой и раскрашенный новый вариант, стрелка', 'Media and culture'),
 ('belief', 'belief', 'Девочка с закрытыми глазами, рука на сердце, над ней звезда — верит в мечту', 'Word families (noun forms)'),
 ('make the most of (sth)', 'make the most of', 'Семья на пляже в последний солнечный день: купаются, строят замок, едят мороженое', 'Idiomatic expressions'),
 ('for hours/weeks on end', 'for hours on end', 'Мальчик весь день собирает огромный пазл, за окном уже луна', 'Time expressions'),
 ('in no time', 'in no time', 'Девочка мгновенно собрала пазл, рядом песочные часы с почти полной верхней колбой', 'Time expressions'),
]
NOTE = {'buy clothes': DOC, 'chat to friends': DOC, 'download music': DOC, 'download videos': DOC,
        'software': DOC, 'virus': DOC, 'visit websites': DOC, 'machine': BRAND, 'memory': BRAND,
        'thousand': DIG, 'billion': DIG, 'cost (noun)': MONEY,
        'cost (verb)': MONEY, 'pay (noun)': MONEY, 'pay (verb)': MONEY, 'charge (noun)': MONEY,
        'charge (verb)': MONEY, 'speak a language': DOC, 'record (verb)': DOC, 'difference': HEAD,
        'importance': DOC, 'qualification': DOC, 'qualified': DOC, 'decade': HEAD, 'personality': HEAD,
        'version': DOC}
S = [W[k:k + 8] for k in range(0, len(W), 8)]
