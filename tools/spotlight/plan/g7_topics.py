"""Темы-подколоды Spotlight 7 (18.10.2026, правила Анны со Spotlight 4–6).
Раздел больше ~11 слов со смешанными темами делится; маленький однотемный — целиком (тема '').
Тема с '@' — слово уходит в «другие слова» модуля: '@фразовые глаголы', '@фразы', '@описание',
'@действия', '@предметы и понятия' (раскладка по колодам подпапки — в g7_plan.py).
Разделы People, Famous People/Characters, Places, Others — имена без перевода, в план не идут.
Пишет plan/g7_topics.tsv (module, section, term, topic). Слова через |."""
import csv, os, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
rows = list(csv.DictReader(open('tsv/grade_7.tsv'), delimiter='\t'))
SKIP = {'People', 'Famous People/Characters', 'Places', 'Others'}
PH, PV, DS, AC, OT = '@фразы', '@фразовые глаголы', '@описание', '@действия', '@предметы и понятия'
T = {
('Module 1', '1a A city mouse or a country mouse?'): {
 'деревня': 'barn|farmyard|feed|milk|landscape|isolated|hometown',
 'чувства': 'happy|homesick|lonely|relaxed|stressed|tired|worried|miss',
 'описание места': 'huge|interesting|lovely|noisy|quiet',
 'жизнь в городе': 'close at hand|constant noise & pollution|convenient public transport|crowded streets|heavy traffic|high cost of living|high quality lifestyle|high/low rate of unemployment|hustle and bustle|lead (un)healthy lifestyle|peace and quiet|facilities',
 DS: 'free', OT: 'guest', AC: 'swap'},
('Module 1', '1b Better safe than sorry'): {
 'безопасность дома': 'alarm system|door chain|peephole|install|protect|valuables|leaflet|identification (= ID)',
 'преступления': 'burglar|crime|danger|rob|shoplift|steal|stranger',
 'фразовые глаголы': 'hand over|run after|run into|run out of|switch on/off|turn on/off',
 'советы': "better safe than sorry|dusk to dawn|How about ... + ing|I think/don't think you should ...|Why don't you ...?|You should (not)"},
('Module 1', '1c Hanging out'): {
 'места и развлечения': 'activity|attraction|carousel|exhibition|museum|skating gear|spot|surfing',
 'чем заняться': 'chat|choose|shop|visit|hang out|chat with friends|do the gardening|go surfing|hang out at the shopping centre|have lunch outdoors|surf the Net',
 DS: 'crazy|popular', OT: 'outdoors|include'},
('Module 1', '1d – Culture Corner'): {
 'замки и легенды': 'castle|fortress|ghost|legend|raven|tower|medieval|spooky|century|architecture|masterpiece|classical|unique|tourist|view',
 'природа': 'extinct|mountain|river|volcano',
 PV: 'date back|fall down'},
('Module 1', 'English in Use 1'): {
 'транспорт': 'travel by boat|travel by bus|travel by car|travel by motorcycle|travel by plane|travel by ship|travel by taxi|travel by train|travel by tube|travel on foot',
 'на вокзале': "map|passenger|ticket seller|Next please!|Return to London, please.|Single or return?|That's £6.00.|You're welcome."},
('Module 1', 'Across the Curriculum 1 – Geography'): {
 'город': 'block of flats|capital city|city centre|metro network|trolley bus|nightlife|street party|horse racing|local food',
 'описание': 'busy|cheap|clean|colourful|crowded|delicious|dirty|excellent|fantastic',
 'страна': 'continent|currency|language|population'},
('Module 2', '2a Bookworms'): {
 'жанры и книги': 'adventure story|biography|comedy|drama|fairy tale|mystery|myth|novel|poem|science fiction|a suspense story|humorous story|history',
 'писатели и герои': 'author|writer|character|companion|criminal|detective|bookworm',
 'качества героев': 'appearance|brilliant|clever|faithful|intelligent|loyal|neat|tidy|funny|famous|well known|great|fictional',
 'описание': 'amazing|dangerous|emotional|extraordinary|humorous|mysterious|ordinary|strange|typical|underwater|unusual|several',
 'детектив': 'crime|investigation|magnifying glass|solve the mystery case|cape|event|obsession|order|psychology|excitement',
 AC: 'gossip|inspire', OT: 'imagination|quiz', PH: 'at first glance'},
('Module 2', '2b A classic read'): {'': 'adventure|bush|cave|compass|discover|explore|explorer|hide|huge|initials|journey|nephew|plot|raft|rock'},
('Module 2', '2c Vanished!'): {
 'звуки и действия': 'crawl|cry|gasp|laugh|sigh|snooze|snore|whisper|yawn|trip|chat|reply',
 'чувства и состояние': 'confused|cosy|relieved|sleepy|be fast asleep',
 'гроза': 'storm|stormy|a gust of wind|a flash of lightning|power cut|powerful',
 OT: 'velvet'},
('Module 2', '2d – Culture Corner'): {
 'сказочные герои': 'beast|elf|fairy|giant|king|saint|warrior|champion|storyteller',
 'сказка': 'folk tale|story|tradition|treasure|gold|crock|magical|incredible|noble|moral|value',
 'действия': 'disappear|entertain|fight|overcome|trick',
 OT: 'group|location|obstacle', DS: 'upset'},
('Module 2', 'English in Use 2'): {PH: "Oh my goodness!|You'll never guess what happened to me!"},
('Module 2', 'Across the Curriculum 2 – Literature'): {
 'привидение в замке': 'chain|clank|footstep|handcuffs|haunted|lubricant|oil|rusty|match|strike a match|marble|metal|bottle|dressing case|slippers|ankle|wrist',
 'люди': 'ambassador|dramatist|novelist|poet|local',
 DS: 'calm|foolish|old-fashioned', OT: 'incident', AC: 'notice|warn'},
('Module 3', '3a Lead the way!'): {
 'характер': 'artistic|athletic|creative|curious|daring|determined|imaginative|jealous|patient|sociable|afraid|fit|realistic',
 'увлечения': 'boxing|chess|fencing|football|go-kart|ice-skating|music|painting|pastel|skateboarding|songwriting|fashion|knit|sew|collect',
 'успех': 'award|career|drive|enthusiasm|empire|succeed|set up|be in charge of',
 AC: 'complain|design|staple', OT: 'copy|detail|speed', PV: 'piece together|try out', PH: 'pay attention to'},
('Module 3', "3b Who's who?"): {
 'волосы': 'bald|beard|blond(e)|brown|curly|dark|fair|grey|moustache|pigtail|red|shoulder-length|spiky|straight|wavy|long',
 'фигура и рост': 'fat|heavily built|plump|short|skinny|slim|tall|thin|well-built|of medium height',
 'возраст': 'baby|child|elderly|middle-aged|old|teenager|young|in his/her thirties|in his/her twenties',
 'лицо и внешность': 'cute|freckle|pretty|round|scar|tan|ugly'},
('Module 3', '3c Against all odds'): {
 'люди и достижения': 'actor|inventor|politician|scientist|achieve|admire|best seller|brave|ingenious|start a career|against all odds|university|universe|law',
 'болезнь': 'blink|communicate|computer system|cope (with)|diagnose|disease|enable|muscle|wheelchair|lose control',
 PV: 'give away|give back|give up', OT: 'eventually'},
('Module 3', '3d – Culture Corner'): {
 'Тауэр': 'Beefeater|Yeoman Warder|Crown Jewels|armed forces|bodyguard|guard|prisoner|palace|uniform|duty|formal|occasion',
 'туризм': 'guide|site|striking|tourist|tourist attraction',
 PV: 'look after', PH: 'take care of'},
('Module 3', 'English in Use 3'): {OT: 'lawyer|office|vet'},
('Module 3', 'Across the Curriculum 3 – History'): {
 'дети-рабочие': 'chimney|chimney sweep|coal|cotton|factory|mine|thread|truck|tunnel|wage|work long hours|conditions|master|orphan',
 'описание': 'cruel|narrow|poor|Victorian',
 OT: 'accident|adult|health|queen', AC: 'fix'},
('Module 4', '4a News stories'): {
 'СМИ': 'advertisement|cartoon strip|chat show|documentary|e-mail|horoscope|interview|international news|local news|magazine|mobile phone|music|national news|newspaper|television|TV guide|weather report',
 'из новостей': 'nursery rhyme|panic|porridge|recover|safety|score|scorpion|break a record'},
('Module 4', '4b Did you hear about ...?'): {
 '': 'amazing|awful|excited|interested|marvellous|sad|scary|shocked|surprised|terrible|unbelievable|worried',
 PV: 'go off|go on|go with'},
('Module 4', 'Across the Curriculum 4 – Media Studies'): {
 '': 'campus|chart|hit|DJ|engineer|equipment|experience|journalist|inform|practical|presenter|producer|radio station|review',
 PV: 'break down'},
('Module 5', '5a Predictions'): {
 'будущее': 'glass dome|mini-submarine|online school|robotic housemaid|underwater city|planet|fuel|petrol|traffic jam|housework|creature',
 'фразовые глаголы с look': 'look after|look for|look forward to|look up',
 AC: 'believe|cause|exist'},
('Module 5', '5b Gadget madness'): {
 'гаджеты': 'button|digital camera|e-book device|file|headphones|laptop|MP3 music player|robot pet|text message|computerise|press|store|take a picture of',
 'согласие и несогласие': "come off it|Definitely.|have a point|You're (dead) right.",
 OT: 'affection|puppy', DS: 'hungry', PV: 'clean up'},
('Module 5', '5d – Culture Corner'): {
 'техника': 'digital music player (MP3)|games console|hi-fi system|high-tech|radio|tape recorder|doll',
 'опрос и деньги': 'afford|gold mine|graph|increase|innovation|percentage|pocket money|receive|survey'},
('Module 5', 'English in Use 5'): {PH: "connect to the Internet|click on 'send'|select an email address"},
('Module 6', '6a The fun starts here!'): {
 'парк развлечений': 'big wheel|candyfloss|cartoon character|circus|clown|fun fair|pirate ship|rollercoaster|theme park|trapeze artist|trick|perform|ride|landmark|mansion',
 'фразовые глаголы с come': 'come across|come back|come out|come round',
 'чем заняться': 'go on a rocket journey|go on a water ride|go souvenir shopping|shake hands with|take a stroll|explore',
 DS: 'home-made|tiny'},
('Module 6', '6d – Culture Corner'): {
 'описание': 'active|balanced|believable|forgettable|logical|possible|responsible|spectacular|unforgettable',
 'развлечения': 'attraction|sights|spaceship|toffee apple|fly a plane|go on a safari trek|ride a camel|take a ride on a rollercoaster|driving licence|bone|brick|fossil',
 PV: 'find out'},
('Module 6', 'English in Use 6'): {PH: "reserve a place|I'm afraid there aren't any places left in photography.|Looking forward to seeing you in July.|You need to send a deposit."},
('Module 7', '7a Walk of fame'): {
 'профессии': 'actor|actress|athlete|comedian|figure skater|film director|model|opera singer|performer',
 'описание': 'attractive|beautiful|expensive|fast|funny|handsome|intelligent|noisy|proud|rich|smart|successful|talented|wise',
 OT: 'career'},
('Module 7', '7b DVD frenzy!'): {
 'фильмы': 'adventure|animation|comedy|fantasy|film review|movie|romance|science fiction|thriller|creepy|stunning',
 'фразовые глаголы с turn': 'turn in|turn into|turn off|turn on',
 'нравится — не нравится': "How about ...?|I don't mind.|I don't really like ...|I hate / can't stand ...|I love/like/enjoy ...|I (quite) like ... but I prefer ...|I'm not a big fan of ...|That's a great idea.|suggestion",
 PH: 'according to'},
('Module 7', '7c In the charts!'): {
 'музыка': 'album|artist|catchy|classical music|funk|genre|heavy metal|jazz|lyrics|music chart|musical instrument|pop|rap|rock|singer|songwriter|soul|tune|voice',
 'кино': 'acting|cast|plot|rating|role|script|sound effects|special effects',
 DS: 'bright|genuine'},
('Module 7', 'English in Use 7'): {PH: "Enjoy the movie!|Here are your tickets and your change.|Is that for the 7pm or the 10pm showing?|I'm afraid it's sold out.|Is there a discount for students?"},
('Module 7', 'Across the Curriculum 7 – Music'): {
 'музыка в кино': 'accordion|violin|xylophone|melody|sound|background|extract|scene|horror film|cliché',
 'настроение и звук': 'feeling|mood|sharp|silent|specific',
 AC: 'accompany|introduce|spot'},
('Module 8', '8a Save the Earth'): {
 'загрязнение': 'acid rain|air pollution|factory waste|soil pollution|toxic fumes|water pollution|pollute|poison|harm|harmful|emit|burn|kill|wipe out',
 'природа и погода': 'atmosphere|cloud|fog|lake|oxygen|sleet|snow|stream|habitat|plant species',
 'энергия': 'power station|solar power|industry|heat|government|reduce',
 PV: 'make out|make up|make up with', AC: 'breathe|gather|land', OT: 'distance'},
('Module 8', '8b Eco-helpers'): {
 'инструменты': 'gardening gloves|hammer|ladder|nail|net|rake|spade|watering can|plastic bag',
 'экология': 'collect|ecology|join|leave|plant|recycle|rubbish',
 'предложить помощь': "Can I give you a hand ...?|No thanks, I'm fine.|No, I can manage, thanks.|No, it's OK, but thanks anyway!"},
('Module 8', '8d – Culture Corner'): {
 'животные и птицы': 'deer|fieldmice|flock|geese|golden eagle|puffin|seabird|sheep|swan|nest',
 'природа': 'bluebell|cave|cliff|garlic|marsh|nature trail|reserve|wildlife|rare|remote',
 OT: 'donation'},
('Module 8', 'English in Use 8'): {'деньги': 'bank account|cash|cheque|cost|credit card|direct debit'},
('Module 8', 'Across the Curriculum 8 – Science'): {
 '': 'carnivore|herbivore|omnivore|consumer|producer|decomposer|food chain|primary|secondary|tertiary|energy|sunlight|extinction|hunt|bacteria|fungi|compound|organic|grass|grasshopper|hawk',
 AC: 'provide', PV: 'break down'},
('Module 9', '9a You are what you eat!'): {
 'упаковка': 'bar|bottle|box|can|carton|cup|jar|packet|tin|family-sized',
 'напитки и молочное': 'beverages|coffee|cola|fizzy drink|juice|milk|cream|butter|yoghurt|dairy products|ice cream',
 'мясо и рыба': 'chicken burger|chicken leg|fish|lamb chop|meat|poultry|tuna|egg|hamburger',
 'хлеб, крупы, орехи': 'brown rice|cereal|grains|pasta|rice|white bread|wholemeal bread|toast|biscuit|seeds|nuts|peas',
 'овощи, фрукты, приправы': 'fruit|vegetables|lettuce|tomato|herbs|spices|pepper|salt|mayonnaise|oil|olive oil|honey|white sugar',
 'еда и блюда': 'chips|crisp|chocolate|sweets|snack|takeaway|pizza|salad|sandwich|curry|grilled|health food|junk food',
 'фразовые глаголы с take': 'take away|take back|take off|take out'},
('Module 9', '9b Can I help you?'): {
 'магазины': "chemist's|clothes shop|electronics|jeweller's|optician's|sports shop|stationery shop|toy shop",
 'профессии': 'cashier|cleaner|manager|security guard|shop assistant',
 'покупки': 'basketball|camera|crayon|diary|first aid kit|hooded sweater|phonecard|ring|socks|sunscreen|swimming trunks|swimsuit'},
('Module 9', '9c Gifts for everyone!'): {
 'материалы': 'cotton|leather|metal|paper|plastic|silver|velvet|wood|woollen',
 'узор и форма': 'checked|oval|polka dot|plain|rectangular|round|square|striped',
 'подарки': 'bowl|case|cushion|frame|wallet'},
('Module 10', '10a Stress free'): {
 'отношения': 'argue|co-operate|disagree|gossip|mate|sibling|snob|mean|opinion|rumour|hurtful|unfair|fall out with somebody|spread rumours|get the blame',
 'выражения': "break the chain|have it one's way|He gets away with everything.|scratch my back and I'll scratch yours|throw a party|have an appointment|sit exams",
 'стресс и повседневность': 'ache|headache|stressful|harmless|daily|weekly planner|valuable|lose|move|allow|separate',
 PV: 'fall apart|fall behind with sth|sit around'},
('Module 10', '10b Accident-prone'): {
 'травмы': "ambulance|ankle|bang one's head|break one's leg|chip one's tooth|cut one's finger|hurt|hurt one's back|sprain one's wrist|twist one's ankle|wrap",
 'участие': "Are you all right?|What's the matter?|What's up?|Is something wrong?|It's nothing serious.|It's going to be all right.|Let me help you.|You don't look well."},
('Module 10', '10c Doctor, doctor!'): {
 'болезни': 'have a headache|have a sore throat|have a stomachache|have a toothache|have an earache|have high fever|have sore eyes|forehead|exhausted',
 'лечение': 'advice|drop|fluid|meal|vitamin|get some rest|lie down|take a painkiller',
 PV: 'turn out'},
('Module 10', '10d – Culture Corner'): {
 '': 'assistance|basic|complete|emergency|health care|hospital|isolation|landing|mile|non-profit charity|operate|patient|risk|treat',
 PV: 'deal with|set up', PH: 'let alone'},
('Module 10', 'English in Use 10'): {DS: 'dizzy', AC: 'swallow', PV: 'come down with', PH: "Bless you. Here's a tissue."},
('Module 10', 'Across the Curriculum 10 – Literature'): {
 'Робинзон Крузо': 'ash|capsule|grill|gun|herbal remedy|roast|rum|shipwrecked|sickness|supper|syrup|tablet',
 'описание': 'cheerful|lively|miserable|smooth|weak',
 OT: 'author|fiction|journalist'},
}
M = {}
for sec, topics in T.items():
    for topic, words in topics.items():
        for w in words.split('|'):
            assert (sec, w) not in M, (sec, w)
            M[(sec, w)] = topic
out, used = [], set()
for r in rows:
    if r['module'] in SKIP: continue
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
with open('plan/g7_topics.tsv', 'w', newline='') as f:
    f.write('module\tsection\tterm\ttopic\n')
    for o in out: f.write('\t'.join(o) + '\n')
cnt = collections.Counter((r['module'], r['section']) for r in rows if r['module'] not in SKIP)
print(len(out), 'нераздел. >11:', [(s[1], n) for s, n in cnt.items() if s not in T and n > 11])
