"""План колод Spotlight 4: слово → папка/колода, картинка (готовая id / новая / без картинки).
Пишет plan/g4_plan.tsv. Готовые картинки — words.id из тренажёра, сверены по переводу."""
import csv, collections, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
rows = list(csv.DictReader(open('tsv/grade_4.tsv'), delimiter='\t'))

# колоды-темы: (папка, колода) → слова; что не названо — по разделу ниже
D = {
 ('Module 1', 'Unit 1 · Мои вещи'): 'camera CD glove guitar hairbrush key|mobile phone|roller blades|watch',
 ('Module 1', 'Unit 1 · Какой он?'): "friendly kind slim sporty vet|What does he look like?|What's he like?",
 ('Module 1', 'Unit 2 · Друзья и хобби'): 'best friend|both crew dive glue|play the violin|plump quite skate ski sound|stick together|surf',
 ('Module 2', 'Unit 3–4 · Профессии'): "baker greengrocer mechanic nurse postman waiter doctor firefighter|police officer|taxi driver|zoo keeper",
 ('Module 2', 'Unit 3 · Места в городе'): "baker's|greengrocer's|garage hospital|post office|station",
 ('Module 2', 'Unit 3 · Дела и как часто'): 'always never sometimes usually bake carry clean curtain fix|go shopping|play sports|serve sick injection|wake (up)|wash the dishes',
 ('Module 2', 'Unit 4 · Спорт и свободное время'): 'badminton baseball hockey volleyball|free time|sports centre|whistle',
 ('Module 2', 'Unit 4 · Другие слова'): 'meal parcel polite postcard surprise|take care of|wait week',
 ('Module 3', 'Unit 5–6 · Фрукты и овощи'): 'coconut lemon mango pineapple tomato beans pepper cherry onion',
 ('Module 3', 'Unit 5–6 · Продукты'): 'butter flour|olive oil|salt sugar beef lamb yogurt cookie dairy',
 ('Module 3', 'Unit 6 · Упаковка и количество'): 'bar bottle carton jar kilo loaf packet tin basket',
 ('Module 3', 'Unit 5–6 · Блюда и на кухне'): 'barbecue|French fries|paella sushi snack treat tasty taste easy|make sure|pass put world',
 ('Module 4', 'Unit 7–8 · Животные'): 'giraffe seal cuckoo|elephant seal|panda carnivore herbivore omnivore zoo plant',
 ('Module 4', 'Unit 7–8 · Путешествие и другие слова'): 'journey passport suitcase ticket|a whale of a time|amazing rubbish|cookery book|lazy lunchtime',
 ('Module 8', 'Unit 15–16 · Отдых и погода'): 'go camping|go to the lake|go to the mountains|go to the seaside|cloudy rainy Coliseum',
 ('Module 8', 'Unit 16 · Вещи в поездку'): 'boots flippers|sleeping bag|sunglasses|swimming trunks|swimsuit tent',
 ('Справочник', 'Страны'): 'Australia Canada China England France Germany Greece Ireland Italy Japan Mexico|New Zealand|Poland Portugal Russia Scotland Spain Turkey Florida',
 ('Справочник', 'Города и национальности'): 'Athens London Madrid Moscow Paris Rome Italian Japanese Russian',
}
SEC = {  # раздел целиком → (папка, колода)
 'Starter Unit': ('', 'Starter Unit'),
 'Module 5': ('Module 5–7', 'Module 5 · Чувства и вчера'),
 'Module 6': ('Module 5–7', 'Module 6 · Сказки'),
 'Module 7': ('Module 5–7', 'Module 7 · Лучшие времена'),
 'Goldilocks and the Three Bears': ('Чтение', 'Goldilocks and the Three Bears'),
 'Arthur & Rascal': ('Чтение', 'Arthur & Rascal'),
 'Months': ('Справочник', 'Месяцы'), 'Numbers': ('Справочник', 'Числа'),
 'Useful English': ('Справочник', 'Полезные фразы'),
}
def culture(m, s):
    n = int(s.split('.')[0]) if s[:1].isdigit() else 9
    if m.startswith('Cultural'): return ('Culture Corner', 'Cultural Sections 1–4' if n <= 4 else 'Cultural Sections 5–8 и Special Days')
    if m.startswith('Spotlight on Russia'): return ('Spotlight on Russia', 'Spotlight on Russia 1–4' if n <= 4 else 'Spotlight on Russia 5–8')
    if m.startswith('Special'): return ('Culture Corner', 'Cultural Sections 5–8 и Special Days')

# готовая картинка: id слова тренажёра; сверено по переводу
REUSE = {
 'amazing':1768,'angry':703,'april':624,'august':628,'australia':372,'badminton':81,'bake':940,"baker's":871,
 'balloon':210,'barbecue':2411,'baseball':85,'beans':37,'best friend':2467,'boots':504,'bored':704,'bottle':1664,
 'brilliant':1802,'busy':1960,'butter':451,'camera':684,'celebrate':4235,'character':3043,'cheap':723,'china':375,
 'church':1936,'coconut':12,'competition':4056,'dancer':2457,'december':632,'delicious':961,'diary':1743,
 'dinosaur':4112,'discover':1314,'dive':589,'doctor':364,'dream':4329,'easy':726,'february':622,
 'firefighter':1357,'fix':591,'flour':454,'friendly':581,'funfair':335,'garage':538,'giraffe':640,'glue':4275,
 'go camping':99,'go shopping':1706,'golden':4250,"greengrocer's":876,'guitar':58,'hiking':2390,'hockey':89,
 'hospital':24,'hug':4304,'hungry':1454,'italian':1425,'italy':1424,'january':621,'july':627,'june':626,
 'kind':737,'kitten':1828,'lazy':1065,'lemon':455,'london':4318,'loud':1800,'lunchtime':3347,'mango':1872,
 'march':623,'may':625,'mechanic':1951,'mexico':378,'mistake':2633,'mobile phone':356,'november':631,
 'nurse':367,'october':630,'panda':1269,'passport':1980,'pepper':1670,'performance':3421,'plant':556,
 'police officer':778,'polite':1068,'post office':753,'postcard':4360,'pot':953,'programme':2190,'put':4151,
 'quite':2260,'remember':1507,'remind':3435,'river':342,'rubbish':2873,'russia':1428,'russian':1429,
 'salt':1672,'save':1280,'saxophone':1230,'scared':707,'scientist':3132,'seal':347,'september':629,
 'serve':3171,'share':3374,'shy':1072,'sick':2097,'sixty':1554,'skate':1511,'sleeping bag':808,'slim':1739,
 'soft':1309,'spain':379,'sports centre':755,'sporty':585,'station':1682,'sugar':458,'suitcase':809,
 'sunglasses':810,'swimsuit':1165,'taste':3395,'tasty':2949,'tent':811,'thief':1247,'ticket':1983,
 'tired':708,'travel':1795,'trumpet':1231,'turkey':380,'vet':782,'volleyball':86,'waiter':1662,
 'wash the dishes':789,'watch':282,'whistle':4028,'wolf':3003,'young':1741,
}
# совпало слово, но не смысл → рисуем заново
MISMATCH = {'clean': 'в тренажёре «чистый», у нас «убирать»', 'fair': '«светлый» ≠ «честный»',
            'ride': '«кататься» ≠ «аттракцион»', 'wood': '«дерево (материал)» ≠ «лес»'}
# без картинки: отвлечённое, фразы, числа — картинка не объясняет слово
NOPIC = set('''activity|back together|feel|hope|join|same|both|quite|stick together|always|never|sometimes|usually
|free time|surprise|take care of|wait|week|make sure|treat|easy|a whale of a time|amazing|check|in a hurry|luck|mine
|never mind|on my way|return|worry|for a while|is called|project|almost|at least|simple|fun-loving|resolution
|last a long time|millionaire|adopt|donate|raise|soon|discover|it is worth it|rest|young|brilliant|pull down|remember|remind
|eighty|ninety|seventy|sixty|hundred|first|second|third|sound|horrid|naughty|share|serve|polite|kind|save
|what does he look like?|what's he like?|bon voyage!|congratulations!|excuse me, where's ...?|happy new year!
|it's your turn|nice to meet you.|see you later.|thank you. — you're welcome.|pass|put|dream|busy|hate|cheap|delicious'''
  .replace('\n', '').split('|'))

lk = {}
RAW = {r['term'] for r in rows}
# фразы, где пробел внутри, распознаём жадно
def split(s):
    out, cur = [], s.replace('|', ' | ').split()
    i = 0
    while i < len(cur):
        if cur[i] == '|': i += 1; continue
        for j in range(len(cur), i, -1):
            ph = ' '.join(cur[i:j])
            if ph in RAW: out.append(ph); i = j; break
        else: raise SystemExit('нет слова: ' + cur[i])
    return out
for k, ws in D.items():
    for w in split(ws): lk[w] = k

out, miss = [], []
for r in rows:
    m, s, t = r['module'], r['section'], r['term']
    k = lk.get(t)
    if k and k[0] != m and k[0] != 'Справочник': k = None  # pass, lamb — в двух разделах
    k = k or culture(m, s) or SEC.get(m)
    if not k: miss.append((m, s, t)); continue
    lt = t.lower()
    img = ('mismatch' if lt in MISMATCH else f'reuse:{REUSE[lt]}' if lt in REUSE else
           'none' if lt in NOPIC else 'new')
    if lt in REUSE and lt in NOPIC: img = f'reuse:{REUSE[lt]}'
    out.append([k[0], k[1], m, s, t, r['translation'], img])
if miss: print('НЕ РАЗЛОЖЕНО:', *miss, sep='\n'); raise SystemExit(1)
w = csv.writer(open('plan/g4_plan.tsv', 'w'), delimiter='\t', lineterminator='\n')
w.writerow(['folder', 'deck', 'module', 'section', 'term', 'translation', 'image']); w.writerows(out)
c = collections.Counter(x[6].split(':')[0] for x in out)
print(len(out), dict(c))
by = collections.OrderedDict()
for x in out: by.setdefault((x[0], x[1]), []).append(x)
for (f, d), g in by.items():
    cc = collections.Counter(x[6].split(':')[0] for x in g)
    print(f'{f:20} {d:42} {len(g):3}  есть {cc["reuse"]:2} новых {cc["new"]+cc["mismatch"]:2} без {cc["none"]:2}')
