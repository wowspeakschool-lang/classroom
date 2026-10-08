"""Темы-подколоды Spotlight 5: большой раздел (>18 слов) делится на темы по смыслу.
Пишет plan/g5_topics.tsv (module, section, term, topic). Слова через |."""
import csv, os, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
rows = list(csv.DictReader(open('tsv/grade_5.tsv'), delimiter='\t'))
SKIP = {'Geographical Names', 'Personal Names', 'Other Proper Names'}
T = {
('Starter Unit', ''): {
 'фразы': "Hello!|Hi!|What's your name?|My name's ...|How are you?|I'm fine, thanks.|Nice to meet you.|Goodbye! Bye!|Where are you from?|please",
 'цвета': 'black|blue|brown|colour|green|grey|pink|purple|red|white|yellow|rainbow',
 'школьные принадлежности': 'blackboard|book|crayon|desk|eraser|glue|ink|notebook|paper clips|pen|pencil|pencil case|ruler|schoolbag|sharpener|chair',
 'в школе и счёт': 'alphabet|pupil|school|uniform|question|reading rules|right|wrong|number|count|equals|minus|plus|date|name',
 'животные и природа': 'ant|bird|cat|fox|nest|snake|zebra|flower|grass|tree|sky|sun',
 'еда': 'apple|cake|cup|egg|garlic|jam|lemon|melon|orange',
 'действия': 'climb|draw|eat|finish|know|look|run|say|sing|sleep|speak|spell|start|walk|write|have got',
 'места и люди': 'café|gym|house|market|museum|park|shop|zoo|doctor|vet|friend|girl|queen|I',
 'игрушки и одежда': 'ball|cap|doll|game|hat|jeans|kite|robot|train|yacht',
 'другие слова': 'box|flag|glass|hand|music|nose|now|song|window'},
('Module 1', '1a'): {
 'школьные предметы': 'art|English|geography|history|information technology (IT)|mathematics (maths)|physical education (PE)|science|subject|favourite|timetable|break|class',
 'в школе': 'atlas|dictionary|notepad|school objects|student|teacher|textbook',
 'дни недели': 'days of the week|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday'},
('Module 1', '1b'): {
 'числа': 'eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty',
 'другие слова и фразы': "best|same|grade|new|strange|then|together|Excuse me, ...|How do you spell it?|How old are you?|Let's go!"},
('Module 2', '2a'): {
 'страны и национальности': 'American|Australian|British|Canadian|English|French|Italian|Japanese|nationality|New Zealander|Russian|people|live|speak English|next door',
 'описание и действия': 'cartoon character|powers|spider|evil|fast|strong|special|amazing|brilliant|quiet|bite|can|stop|wall|watch|find out|aunt|who'},
('Module 2', '2b'): {
 'личные вещи': 'basketball|bicycle (bike)|digital camera|guitar|handbag|helmet|knife|lamp|personal things|present|skateboard|teddy bear|thing|toy|watch|gloves|scarf|tie|trainers|Happy birthday!',
 'необычное множественное число': 'child (pl: children)|fly|foot (pl: feet)|man (pl: men)|mouse (pl: mice)|tooth (pl: teeth)|woman (pl: women)'},
('Module 2', '2c'): {
 'числа': 'thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred',
 'коллекции и описание': 'album|coin|collection|picture|stamp|age|feel|happy|nice|great|easy|be proud of|but|because'},
('Module 3', '3a'): {
 'комнаты': 'bathroom|bedroom|dining room|hall|kitchen|living room|reception room|garage|swimming pool|lift',
 'дом и этажи': 'flat|floor|ground floor|home|roof|step|tower|villa|block of flats|live high up|first|second|third',
 'описание': 'beautiful|famous|great|own|unusual|true|false|view|keep fit',
 'объявление о продаже': 'advert|architect|article|letter|number (of)|pay|price|for sale'},
('Module 3', '3b'): {
 'мебель': 'armchair|bed|bookcase|book shelves|carpet|coffee table|furniture|mirror|painting|sofa|table|wardrobe|window|television (TV)',
 'кухня, ванная и фразы': "appliance|bath|cooker|fridge|sink|toilet|washbasin|How many?|Really?|Sounds great!|What's your new flat like?|heads or tails"},
('Module 4', '4a'): {
 'семья': 'baby|boy|brother|dad|family|family members|father|grandfather|grandma|grandmother|grandpa|grandparents|mother|mum|sister',
 'характер': 'caring|clever|cool|friendly|funny|kind|naughty|noisy|sweet',
 'действия и хобби': 'burn|dance|give|laugh|make|play|see|tell|visit|piano|violin|hobby|cookie|food|diary|pilot|secret|weekend|yet|every summer'},
('Module 4', '4b'): {
 'внешность': 'appearance|build|ear|eye|facial features|fair|fat|hair|height|long|lovely|moustache|mouth|nose|plump|short|tall|thin|description',
 'другие слова': 'classmate|come|match|party|talk|whose|with|over there'},
('Module 4', 'Across the Curriculum 4: Literature'): {
 'животные': 'bee|lamb|mule|owl|ox (pl: oxen)|peacock|snail',
 'описание': 'busy|gentle|playful|slow|stubborn|wise|as ... as',
 'стихи и литература': 'granny|literature|poem|rhyming words|simile|title|send an email'},
('Module 5', '5a'): {
 'животные': 'animal|camel|cobra|creature|crocodile|deer (pl: deer)|elephant|leopard|lion|rhino|tiger|horn|trunk|stripe',
 'действия': 'bite|carry|cry|hide|hunt|relax|sleep|swim|use|wash',
 'описание и природа': 'amazing|dangerous|female|heavy|permanent|habit|metre|mud|grass|plant'},
('Module 5', '5b'): {
 'части тела животных': 'beak|feather|fur|leg|mane|neck|paw|tail|trunk|tusk|wing|parts of the body',
 'животные': 'bear|fish|giraffe|monkey|otter|peacock|penguin|cute|wild|thick|adult',
 'другие слова': 'address|anyway|find|hear|highlighted|opening times|reason|sound|ticket|fruit'},
('Module 5', '5c'): {
 'домашние животные': 'budgie|cow|dog|duck|farm animals|goat|goldfish|goose (pl: geese)|guinea pig|hen|pet|rabbit|sheep (pl: sheep)|tortoise',
 'другие слова': 'activity|bright|else|golden|guy|list|notify|take|all day long|take sb for walks|talk online'},
('Module 5', '5d - Culture Corner'): {
 'коала и природа': 'koala|eucalyptus|leaf (pl: leaves)|mammal|marsupial|zoologist|characteristic|fact file|liquid',
 'описание': 'cute|furry|little|round|sharp|soft',
 'другие слова': "complete|get|mean|need|never|during the day|they don't make good pets"},
('Module 5', 'Across the Curriculum 5: Science'): {
 'насекомые': 'ant|antenna (plural: antennae)|bee|beetle|butterfly|dragonfly|fly|grasshopper|insect|ladybird|mosquito|wasp|buzz around|honey',
 'природа и отходы': 'field|forest|ground|life|rubbish|unwanted|waste|dead',
 'другие слова': 'call|detective|expect|important|keep|million|present'},
('Module 6', '6a'): {
 'распорядок дня': 'daily routine|get up|wake up|at home|do homework|do the/go shopping|have/eat dinner|have/eat lunch|get dressed|go to bed|go to school|work on computer',
 'время': "clock|at ... o'clock|at midnight/at night|at noon|half past seven|Have you got the time, please?|quarter past seven|quarter to seven|What's the time, please?|for a while",
 'как часто': 'always|often|sometimes|usually|daily|after|before|late',
 'спорт и герои': 'acrobatics|action hero|archaeologist|fight|go jogging|practise kick boxing'},
('Module 6', '6b'): {
 'профессии': 'baker|doctor|mechanic|nurse|painter|postman|taxi driver|waiter|waitress|job|Mr|Ms|Mrs|What does your dad do?',
 'места в городе': "ambulance|baker's|bakery|café|hospital|a street scene|across the road|by the fire",
 'действия': 'drive|paint|serve|wait|repair|act out a dialogue|catch the bus home|deliver letters|do a crossword|say goodbye to ...'},
('Module 6', 'Across the Curriculum 6: Science'): {
 'солнце и стороны света': 'compass|east|north|south|west|sky|shadow|sundial|sunny day|early|move around',
 'предметы и действия': 'centimetre|hole|lid|stone|straw|tape|top|mobile phone|mark|put|point|place|side|use',
 'другие слова': 'be ready|correct|different|nearby|need|perfect|until|do the same'},
('Module 7', '7a'): {
 'времена года и месяцы': 'autumn|spring|summer|winter|season|month|year|January|February|March|April|May|June|July|August|September|October|November|December',
 'погода': "snow|weather|weather forecast|It's (very) hot.|It's cold.|It's freezing.|It's raining (heavily).|It's snowing.|It's warm.|The sun is shining.|What's the weather like in ...?",
 'фразы': "How are you doing?|It doesn't suit me.|It's fabulous!|It's awful!|It's terrible!|That's not my kind of place.|You're lucky.|be fed up with sth|at the moment",
 'занятия и другие слова': 'balcony|chat log|computer screen|go swimming|image|magazine|mind|proverb|statement|pick flowers|rake leaves'},
('Module 7', '7b'): {
 'одежда': 'blouse|boots|clothes|coat|dress|high heels|jumper|raincoat|shirt|shoes|shorts|skirt|socks|suit|trainers|trousers|bag',
 'как сидит одежда': "light|loose|tight|put on|wear|How do I look in this?|How does this look on me?|I'm not sure it suits you.",
 'другие слова': 'airport|couple|get on|habit|hang up|joke|telephone conversation|go on foot'},
('Module 8', '8a'): {
 'еда и урожай': 'biscuit|banana|carrot|cranberry sauce|dessert|dish|pumpkin pie|rice|sweet potato|turkey|wheat|crop|harvest|fresh|cookery competition',
 'праздники': 'celebrate|celebration|costume|dress up|festive|festival|holiday|moon|street parade|light bonfires|set off fireworks|exchange gifts|last',
 'другие слова': 'both|choose|complete|cut|dictionary entry|different varieties|farmer|radio show'},
('Module 8', '8b'): {
 'еда': 'bread|burger|butter|cereal|cheese|chicken|chocolate|ice cream|meat|olive oil|pasta|pizza|sausage|sugar|cake',
 'фрукты и овощи': 'cabbage|cherry|garlic|grapes|onion|pineapple|strawberry|tomato',
 'упаковка и посуда': 'bottle|bowl|box|carton|container|cupboard|glass|jar|packet',
 'напитки и другие слова': 'milk|lemonade|orange juice|everything|master chef|meal|shopping list|tonight'},
('Module 8', '8c'): {
 'еда': 'crisps|noodles|sandwich|soup|treat|Chinese|stick',
 'праздник и фразы': "balloon|bring|envelope|full of|good luck|magazine entry|mean|money|paper|unlucky|I'd love to ...|I don't think so.|Would you like ...?"},
('Module 8', 'Across the Curriculum 8: PSHE'): {
 'безопасность на кухне': 'bacteria|chop|clean|danger|knife|sharp|surface|touch|keep clean|keep away|keep out|store|prepare|carefully',
 'продукты и другие слова': "dairy products|fruit & vegetables|yoghurt|back|first|forget|PSHE (Personal Social & Health Education)|the list of dos and don'ts|for example"},
('Module 9', '9a'): {
 'магазины': "baker's|bakery|chemist's|florist's|greengrocer's|jeweller's|newsagent's|record shop|shoe shop|shop|shopping centre/mall|fast food restaurant",
 'покупки и другие слова': 'aspirin|mean|mention|sell|tulip|look for|pair of shoes'},
('Module 9', '9c'): {
 'кино': 'action film|adventure film|animated|comedy|horror film|romance|hero|leading star|main character|plot|review|heading',
 'другие слова': 'adult|become|face|miss|recommend|recommendation|save|It is (well) worth seeing.'},
('Module 10', '10a'): {
 'виды отдыха и транспорт': 'activity holiday|camp|cruise|extreme sports|mountaineering|rock climbing|safari|sightseeing tour|trekking|motorbike|coach|ship',
 'путешествие': 'advert|apartment|book|credit card|fill in|free brochure|full board|hotel|price|travel agent|abroad|holiday|travel',
 'места и описание': 'ancient culture|beauty|countryside|historic|magic|magnificent|sand',
 'действия': 'advise|discover|experience|join (in)|learn (about)|leisure|rest|spend'},
('Module 10', '10b'): {
 'виды отдыха': 'canoeing|fishing|hiking|jet skiing|sailing|scuba diving|sunbathing|white water rafting|windsurfing',
 'чувства и описание': 'bored|boring|enjoyable|excited|exciting|feeling|relaxed|relaxing|tiring|tired|difficult|hard|hungry',
 'другие слова': "airport|business|decide|mind|Don't worry!|pass the exam"},
}
M = {}
for sec, topics in T.items():
    for topic, words in topics.items():
        for w in words.split('|'):
            assert (sec, w) not in M, (sec, w)
            M[(sec, w)] = topic
out, used = [], set()
cnt = collections.Counter((r['module'], r['section']) for r in rows)
for r in rows:
    if r['module'] in SKIP: continue
    sec = (r['module'], r['section'])
    if cnt[sec] <= 18:
        assert sec not in T, sec
        topic = ''
    else:
        topic = M.get((sec, r['term']))
        assert topic is not None, ('нет темы', sec, r['term'])
        used.add((sec, r['term']))
    out.append((r['module'], r['section'], r['term'], topic))
extra = set(M) - used
assert not extra, ('лишние', extra)
missing = {s for s in cnt if cnt[s] > 18 and s[0] not in SKIP} - set(T)
assert not missing, missing
with open('plan/g5_topics.tsv', 'w', newline='') as f:
    f.write('module\tsection\tterm\ttopic\n')
    for o in out: f.write('\t'.join(o) + '\n')
print(len(out))
