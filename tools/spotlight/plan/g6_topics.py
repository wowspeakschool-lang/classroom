"""Темы-подколоды Spotlight 6 (17.10.2026, правило «одна колода — одна тема»).
Раздел больше ~11 слов со смешанными темами делится; маленький однотемный — целиком.
Пишет plan/g6_topics.tsv (module, section, term, topic). Слова через |."""
import csv, os, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
rows = list(csv.DictReader(open('tsv/grade_6.tsv'), delimiter='\t'))
T = {
('Module 1', '1a Family Members'): {
 'семья': 'aunt|brother|child|children|cousin|dad|daughter|husband|mum|parents|sister|son|twins|uncle|wife|be married to smb.',
 'внешность': 'big|curly|fair|fat|grey|hair|height|long|short|slim|straight|wavy|weight|facial features',
 'возраст': "age|middle-aged|old|young|be in one's early sixties|be in late thirties|be in mid twenties"},
('Module 1', '1b Who are you?'): {
 'личные данные и документы': 'address|nationality|postcode|surname|credit card|date of birth|driving licence|expiry date|full name|home address|identity card|identification number|membership card|telephone number|join a club|register a library',
 'вещи': 'camera|computer|skateboard|watch|alarm clock'},
('Module 1', '1c My Country'): {
 'страны и национальности': 'Brazil|Brazilian|Britain|British|Chile|Chilean|German|Germany|Japan|Japanese|Poland|Polish|Russia|Russian|Spain|Spanish',
 'стороны света': 'compass|east|north|north-east|north-west|south|west',
 'природа и другие слова': 'desert|mountains|valley|location|exactly|include'},
('Module 1', '1d Culture Corner'): {
 'страны и города': 'Belfast|Cardiff|Edinburgh|England|Ireland|London|Scotland|Wales|the Union Jack|the United Kingdom',
 'другие слова': 'country|currency|map|population|as well as|British pound'},
('Module 2', '2a Happy Times'): {
 'месяцы': 'January|February|March|April|May|June|July|August|September|October|November|December',
 'дни недели': 'Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday',
 'порядковые числа': 'first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|twenty-first|thirtieth|thirty-second|fortieth|forty-fourth',
 'время': "at midnight|at midday|noon|o'clock|a quarter past|a quarter to|half past",
 'праздники': 'birthday|celebrate|event|graduation|invitation|occasion|take place|Halloween holiday|invite smb. to a party|trick or treat'},
('Module 2', '2b My place'): {
 'комнаты': 'bathroom|bedroom|kitchen|study|dining room|living room',
 'кухня и ванная': 'basin|bathtub|cooker|cupboard|fridge|sink',
 'мебель и вещи': 'armchair|bookcase|carpet|cushion|curtain|fireplace|mirror|painting|shelf|vase|wardrobe|coffee table|ceiling|floor|flower|newspaper',
 'фразы и другие слова': "expensive|do one's best|move house|give smb. a hand|Watch out!|Calm down!"},
('Module 2', '2c My neighbourhood'): {
 'места': "baker's|bank|café|chemist's|greengrocer's|library|newsagent's|supermarket|bus station|coffee shop|pet shop|post office|sports shop|toy shop|neighbourhood",
 'покупки': 'aspirin|stamp|vegetables|teddy bear'},
('Module 2', '2d Culture Corner'): {
 'улицы': 'avenue|boulevard|lane|place|road|street|pavement',
 'другие слова': 'narrow|power|store|fashionable clothes|outdoor café'},
('Module 3', '3a Road safety'): {
 'на дороге': 'traffic|traffic lights|traffic sign|traffic warden|zebra crossing|kerb|pedestrian|driver|bike lane|parking zone|flow of',
 'в машине и на велосипеде': 'tyre|brakes|back seat|seat belt|bicycle helmet|handgrip',
 'действия и правила': 'annoy|block|check|cross|enter|park|push|ride|use|lean out of the window|look both ways|on foot|clear|dangerous|safe'},
('Module 3', '3b On the move'): {
 'дорога и направления': 'plane|train|gallery|driving school|draw a map|go straight on|go towards|turn green|turn right/left',
 'другие слова': 'careful|excellent|perfect|remember|be careful'},
('Module 4', '4a Day in, Day out'): {
 'как часто': 'always|never|often|rarely|sometimes|usually|once a month|twice a week',
 'распорядок дня': 'brush my teeth|do my homework|get dressed|go out with friends|have a shower|listen to music|play sports|spend (spent)',
 'действия': 'catch (caught)|cook|cry|fix|kick|kiss|laugh|lose (lost)|teach (taught)|treat (well)',
 'другие слова': 'dormitory|dungeon|frog|greenhouse|habit|common room|hide and seek|magic tricks'},
('Module 4', '4b How about...?'): {
 'телепередачи и фильмы': 'comedy|drama|news|science fiction|sitcom|sports|talk show|thriller|music shows|reality shows|be on|star',
 'впечатления': 'awful|boring|delicious|disgusting|dull|enjoyable|exciting|fine|great|horrible|interesting|terrible|wonderful',
 'еда': 'chicken|fish|hamburger|pizza|spaghetti|eat out',
 'занятия и другие слова': 'dancing|skiing|windsurfing|pop concert|pop music|decide|teenager'},
('Module 5', '5a Festive time'): {
 'домашние дела': 'bake|do the dusting|do the gardening|do the shopping|do the washing up|make preparations|make a cake|make a phone call|make tea',
 'праздник и другие слова': 'dance|grapes|wish|as for|be busy|be excited|blow a horn|council workers|Good luck!|play the drums'},
('Module 5', "5b Let's celebrate"): {
 'праздники': "celebration|Thanksgiving|Guy Fawkes Day|May Day|St. Patrick's Day|Valentine's Day",
 'игры, костюмы и угощения': 'bobbing for apples|pin the tail on the donkey|perform tricks|throw streamers|toffee apple|pumpkin|costume|dress up|witch|wreath|guest',
 'действия и другие слова': 'be over|clean up|cool|exchange|gang|join in|offer|run out of|terrify'},
('Module 5', '5c Special days'): {
 'праздничные дела': 'decorate the house|exchange gifts|have a great time|have a meal|light lamps|make a speech|put in order|put up decorations|watch the fireworks|pray|display',
 'другие слова': 'activities|colourful|festive|finally|goddess|last|important|whole|wealth'},
('Module 5', '5d Culture Corner'): {
 'состязания': 'athlete|compete|competition|crowd|hill run|hammer throw|shot put|tossing the caber|tug of war|rope|pull over|take part in the game|tree trunk|marching band',
 'другие слова': 'advertisement|annual|available|before|upright|hold onto|popular|sell out|traditional|try|towards|take place'},
('Module 5', 'English in Use/Extensive Reading 5'): {
 'цветы': 'carnation|daisy|rose|sunflower|tulip|a/two dozen (roses/tulips/daisies)|send flowers|include a card|including delivery',
 'другие слова': 'adventure|belt|cravat|create|extract|lucky|quantity|strange|a fictional character|be offended|have in mind|I beg your pardon!|through a looking glass'},
('Module 6', '6a Free time'): {
 'увлечения': 'acting|novel|paint|photography|print|art museum|go cycling|go on trips|go windsurfing|join a club|present plays|PC (personal computer)|brochure|leaflet|learn|present',
 'фразы и описание': 'be good at|be fond of|be keen on|be mad about|be interested in|have fun|let the good times rock|at the weekend|brilliant|tiring'},
('Module 6', '6b Game on!'): {
 'игры': 'backgammon|billiards|chess|darts|dominoes|marbles|monopoly|scrabble|board game|jigsaw puzzle|points',
 'в игре': 'win (won)|lose (lost)|fair|agree|argue|suggest|prefer|enjoy|wait for smb.',
 'фразы и другие слова': "annoyance|arrangement|permanent|state|for a change|in the end|I bet|I don't care (about)"},
('Module 6', '6c Pastimes'): {
 'игра и остров': 'dice|pawn|square|snakes and ladders|island|parrot|coconut|corn|rice',
 'действия': 'explore|go down|go up|grow (grew)|hear (heard)|miss|sing (sang)|think (thought)',
 'другие слова': 'about|in|under|lonely|warm'},
('Module 6', '6d Culture Corner'): {
 'действия': 'cost (cost)|discover|design|invent|release|come up with|solve a crime',
 'другие слова': 'aim|at random|customer|property|weapon|as much as possible|be/become a great success|bonus points|letter tiles|the scene of crime'},
('Module 6', 'Use of English/Extensive Reading 6'): {
 'куклы и материалы': 'marionette|puppet|puppeteer|rubber|string|wooden|glove|glue|scissors|wrap|attach',
 'игры и наборы': 'chess board|dart set|hang gliding plane|roller skates|table tennis set',
 'другие слова': 'drawing|educate|look for|only|make us laugh|What about...?'},
('Module 7', '7a In the past'): {
 'описание города': 'busy|crowded|deserted|different|empty|modern|quiet|ruined|wealthy|ugly|ghost town|saloon|mine|horse',
 'когда и другие слова': 'ago|yesterday|last night|last week|even|be called'},
('Module 7', '7b Halloween Spirit'): {
 'чувства': 'bored|miserable|puzzled|scared|stressed|tired|worried',
 'действия': 'introduce|knock|rush|scream|shout',
 'другие слова': 'anyway|creature|fortnight|huge|naughty|owl|stairs|suddenly|treat|by the time'},
('Module 7', '7d Culture Corner'): {
 'супергерои': 'Batman|Spiderman|Superman|superhero|Zorro|cape|trunks|invisible|powerful|fire heat vision|fight criminals|gain strength|rescue|leap|bullet|rocket',
 'описание': 'able|helpless|just|shy|smart|unpopular',
 'другие слова': 'adopt|adult|fantasy|farmer|make up|American dream|in order to'},
('Module 7', 'Use of English/Extensive Reading 7'): {
 'старинные игрушки': 'build bricks|clay and wax|rocking horse|tool kit|handle|leather|item',
 'другие слова': 'century|common|familiar|imagination|poor|report|at the touch of|lost property office|run a home|the Victorian times|throughout the ages'},
('Module 8', "8a That's the rule"): {
 'жилище': 'accommodation|campus|cottage|hotel|palace|premise|school building|types of dwelling|university halls of residence|block of flats|outdoor area|kitchen appliances',
 'правила': "get permission|it's forbidden|it's (not) allowed|make noise|register overnight guests|remove food from|feed animals|barefoot|tidy",
 'другие слова': 'poster|squirrel|student'},
('Module 8', '8b Shall we?'): {
 'места': 'aquarium|gym|stadium|department store|fast food (restaurant)|sports centre|swimming pool',
 'описание людей': 'colleague|experienced|friendly|glamorous|intelligent|pretty',
 'фразы и другие слова': 'relax|serve|Are you joking?|Are you serious?|come on|have a snack|smoked salmon|What do you feel like doing?'},
('Module 8', 'Use of English/Extensive Reading 8'): {
 'в театре': 'performance|show|seat|row|book tickets|ticket counter|receptionist|questionnaire',
 'порядок и мусор': 'broken|damaged|graffiti|litter|messy|out of order|rubbish bins|swing',
 'другие слова': "collect|front|expire|look after|pay (paid)|you're on the right track"},
('Module 9', '9a Food & Drink'): {
 'продукты': 'biscuit|carrot|cereal|chocolate|honey|lamb|meat|onion|pepper|potato|poultry|sausage|tomato|vegetables|yoghurt|olive oil|toast',
 'блюда': "dessert|gravy|pudding|starter|takeaway|trifle|bacon and eggs|chilli con carne|fish and chips|main course|packed lunch|roast beef|shepherd's pie|spaghetti bolognaise",
 'вкус': 'bitter|dairy|home-made|hot|salty|sour|spicy|sweet|cuisine',
 'другие слова': 'either|pound|rush to work'},
('Module 9', '9b On the menu'): {
 'продукты и блюда': "bean|beef|celery|crisps|greens|melon|mushroom|pie|steak|pasta|spice|chef's salad|grilled chicken|milk shake|sirloin steak",
 'готовим': 'add|boil|dice|fry|mix|peel|pour|preheat|stir|taste',
 'другие слова': 'diet|waiter|be on a diet'},
('Module 9', "9c Let's cook!"): {
 'упаковка и меры': 'bowl|carton|jar|kilo|loaf|packet|portion|tablespoon (tbsp)|teaspoon (tsp)|degree',
 'выпечка': 'flour|muffin|raisin|baking powder|baking soda|melt|mixture|recipe',
 'другие слова': 'receipt|shopping list'},
('Module 10', '10a Holiday plans'): {
 'занятия на отдыхе': 'attend a performance|buy souvenirs|go on a boat cruise|go/do sightseeing|hire a car|holiday activities|post some letters|rent a boat|stay in a luxurious hotel|taste local food|travel abroad',
 'другие слова': 'caviar|collection|couple|exotic|flood|species|terrific|tomb|next month'},
('Module 10', "10b What's the weather like?"): {
 'погода': 'chilly|cloud|cloudy|fog|foggy|rainy|snowy|storm|stormy|sunny|wet|windy|boiling hot|freezing cold|get soaked',
 'одежда': 'jacket|raincoat|sandal|scarf|shirt|shorts|skirt|sweater|top|trainers|trousers|T-shirt',
 'другие слова': 'borrow|hang on|hurry|brand new|day off'},
('Module 10', '10d Culture Corner'): {
 'замок и праздник': 'bagpipes|band|castle|kilt|piper|musician|military|fire|chant|crown jewels|folk music|tunnel|treasure',
 'музеи детства и моря': 'childhood|tricycle|hot air balloon|multiplication table|sea life|underwater safari|transparent|object',
 'другие слова': 'accurate|admire|architecture|except|experience|lifetime|provide|tour|range from|remind smb. of smth.'},
('Module 10', 'English in Use/Extensive Reading 10'): {
 'в гостинице': 'check in/out|reservation|double room|en suite bathroom|per night|single room',
 'природа и другие слова': 'dunes|pebbles|volcano|stretch|grind|crash|ultimate'},
}
M = {}
for sec, topics in T.items():
    for topic, words in topics.items():
        for w in words.split('|'):
            assert (sec, w) not in M, (sec, w)
            M[(sec, w)] = topic
out, used = [], set()
for r in rows:
    sec = (r['module'], r['section'])
    if sec in T:
        topic = M.get((sec, r['term']))
        assert topic is not None, ('нет темы', sec, r['term'])
        used.add((sec, r['term']))
    else:
        topic = ''
    out.append((r['module'], r['section'], r['term'], topic))
extra = set(M) - used
assert not extra, ('лишние', extra)
with open('plan/g6_topics.tsv', 'w', newline='') as f:
    f.write('module\tsection\tterm\ttopic\n')
    for o in out: f.write('\t'.join(o) + '\n')
cnt = collections.Counter((r['module'], r['section']) for r in rows)
print(len(out), 'нераздел.:', [(s[1], n) for s, n in cnt.items() if s not in T and n > 11])
