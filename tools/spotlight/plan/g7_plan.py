"""Spotlight 7: план колод и картинок. tsv/grade_7.tsv + plan/g7_topics.tsv → plan/g7_plan.tsv, plan/g7_reuse.tsv.
Картинки: reuse:<id> — слово тренажёра с тем же смыслом (сверено вручную по выборке words, image_url not null,
18.10.2026), new — рисовать, none — без картинки.
«Другие слова» модуля (темы с '@' в g7_topics) — одна на модуль (Анна, 17.10.2026): до 8 слов — одна колода
«Module N · другие слова» в папке модуля; больше — подпапка «Другие слова», колоды по темам; тема из 2–3 слов
вливается в самую большую с дописью «… и полезные слова». Колонка subfolder в плане — «Другие слова» или пусто."""
import csv, os, re, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
# 🟥 названия модулей — по памяти, сверить с учебником
MOD = {1: 'Lifestyles', 2: 'Tale time', 3: 'Profiles', 4: 'In the news', 5: 'What the future holds',
       6: 'Having fun', 7: 'In the spotlight', 8: 'Green issues', 9: 'Shopping time', 10: 'In good health'}
def sec_name(s):
    return re.sub(r'^(\d+d) – Culture Corner$', r'\1 Culture Corner', s)
# lower(term) → id; ключ (раздел, term) — для омонимов внутри класса
REUSE = {
 'guest': 2310, 'happy': 705, 'huge': 5629, 'interesting': 763, 'landscape': 3319, 'lonely': 2659, 'lovely': 1907,
 'miss': 6857, 'noisy': 5308, 'quiet': 766, 'relaxed': 3018, 'stressed': 5793, 'tired': 708, 'worried': 709, 'free': 5644,
 'burglar': 2844, 'danger': 5954, 'install': 3462, 'leaflet': 6147, 'protect': 1278, 'rob': 2850, 'steal': 2853,
 'run out of': 6694,
 'activity': 5422, 'choose': 3471, 'exhibition': 5989, 'museum': 745, 'popular': 1772, 'shop': 3173, 'surfing': 2822,
 'visit': 1796, 'hang out': 2900, 'do the gardening': 6680, 'go surfing': 1839, 'surf the net': 6655,
 'architecture': 7258, 'castle': 1933, 'century': 6998, 'classical': 5987, 'legend': 4437, 'mountain': 391, 'river': 342,
 'tourist': 1985, 'tower': 341, 'unique': 3819, 'view': 5179, 'volcano': 720, 'fall down': 3216, 'map': 337,
 'block of flats': 967, 'busy': 1960, 'cheap': 723, 'city centre': 6541, 'clean': 761, 'colourful': 2370,
 'crowded': 6920, 'currency': 6340, 'delicious': 961, 'dirty': 762, 'excellent': 6507, 'fantastic': 1771,
 'language': 5003, 'population': 3320,
 'amazing': 4621, 'appearance': 5310, 'author': 2672, 'biography': 3085, 'brilliant': 6811, 'character': 3043,
 'clever': 580, 'comedy': 1170, 'criminal': 1242, 'dangerous': 657, 'detective': 1243, 'drama': 6623,
 'emotional': 4048, 'famous': 5174, 'funny': 582, 'great': 5175, 'history': 307, 'humorous': 3816,
 'imagination': 6995, 'intelligent': 736, 'loyal': 3188, 'mysterious': 3699, 'myth': 3984, 'novel': 3088,
 'ordinary': 6140, 'poem': 5384, 'quiz': 5153, 'science fiction': 3040, 'strange': 4984, 'tidy': 856,
 'typical': 5239, 'unusual': 1773, 'writer': 3095, 'cape': 6985,
 'compass': 4366, 'discover': 4717, 'explore': 6862, 'hide': 5502, 'journey': 4626, 'nephew': 2243, 'plot': 3045,
 'confused': 3011, 'cosy': 2334, 'laugh': 5288, 'power cut': 2871, 'powerful': 3817, 'sigh': 4020, 'storm': 7227,
 'stormy': 7226, 'whisper': 4027, 'yawn': 3251,
 'champion': 2449, 'disappear': 3176, 'fight': 5549, 'gold': 1297, 'treasure': 4180, 'location': 6322, 'upset': 1350,
 'ankle': 2641, 'bottle': 1664, 'calm': 5783, 'marble': 5254, 'metal': 1299, 'novelist': 3129, 'poet': 3091,
 'warn': 3436,
 'afraid': 1913, 'boxing': 2813, 'chess': 490, 'collect': 7071, 'complain': 3431, 'creative': 2263, 'curious': 3440,
 'design': 1313, 'determined': 1258, 'drive': 3835, 'football': 88, 'go-kart': 233, 'ice-skating': 667, 'music': 310,
 'painting': 5343, ('3a Lead the way!', 'patient'): 854, 'sew': 3239, 'skateboarding': 670, 'sociable': 3192,
 'baby': 1434, 'bald': 1057, 'beard': 1058, 'child': 1437, 'curly': 2732, 'cute': 5401, 'dark': 569, 'elderly': 2734,
 'fair': 2735, 'fat': 1733, 'grey': 6271, 'long': 523, 'middle-aged': 2739, 'moustache': 1059, 'old': 525,
 'plump': 4518, 'pretty': 2252, 'red': 570, 'round': 2378, 'short': 1737, 'slim': 1739, 'spiky': 565,
 'straight': 566, 'tall': 1693, 'teenager': 6635, 'thin': 5328, 'ugly': 661, 'wavy': 567, 'young': 1741,
 'achieve': 3468, 'actor': 1195, 'admire': 3469, 'blink': 3243, 'brave': 3010, 'cope (with)': 3923,
 'politician': 3116, 'scientist': 3132, 'university': 1684, 'give away': 2926, 'give back': 2666,
 'crown jewels': 7262, 'palace': 1938, 'prisoner': 3862, 'tourist attraction': 5639, 'uniform': 4842,
 'look after': 1276, 'take care of': 4566, 'lawyer': 3114, 'office': 1963, 'vet': 782,
 'adult': 5399, 'chimney': 3882, 'cotton': 1295, 'fix': 591, 'health': 5474, 'mine': 6915, 'narrow': 6477,
 'poor': 6994, 'queen': 4922, 'tunnel': 7263,
 'advertisement': 2207, 'cartoon strip': 6146, 'chat show': 3033, 'documentary': 3036, 'interview': 2212,
 'magazine': 5710, 'mobile phone': 356, 'newspaper': 1644, 'porridge': 4651, 'recover': 3250, 'score': 1151,
 'television': 558, 'awful': 5148, 'excited': 1808, 'interested': 1917, 'sad': 706, 'surprised': 1920,
 'terrible': 6602, 'go off': 3585, 'member': 2472, 'pollution': 2870, 'proud (of)': 3017, 'proud': 3017,
 'come up with': 6874, 'attractive': 1769, 'beauty': 6081, 'celebrity': 3252, 'competition': 4056, 'offer': 6695,
 'news': 2511, 'reality show': 3039, 'soap opera': 3041, 'weather': 5717,
 'campus': 7016, 'dj': 3255, 'engineer': 1355, 'journalist': 1359, 'presenter': 3117, 'review': 2214,
 'practical': 4050,
 'creature': 6930, 'fuel': 3305, 'planet': 4380, 'traffic jam': 2875, 'look for': 995, 'look up': 3058,
 'button': 360, 'digital camera': 1647, 'headphones': 361, 'hungry': 1454, 'laptop': 354, 'press': 4292,
 'puppy': 1830, 'store': 5960, 'clean up': 6700, 'explanation': 3504, 'inspiration': 3836,
 'doll': 230, 'games console': 353, 'graph': 6668, 'pocket money': 6657, 'receive': 1930, 'develop': 3460,
 'train': 1153,
 'candyfloss': 5986, 'cartoon character': 5041, 'home-made': 7114, 'landmark': 5632, 'ride': 1508,
 'rollercoaster': 4733, 'theme park': 5998, 'tiny': 2338, 'come round': 2896,
 'book': 6050, 'video game': 2448, 'build a fire': 6645, 'go hiking': 92, 'go swimming': 1403,
 'sailing': 6110, 'get back': 2383, 'greeting': 5771,
 'active': 2262, 'driving licence': 6285, 'spaceship': 4669, 'spectacular': 3290, 'toffee apple': 6708,
 'find out': 994, 'ride a camel': 1146, 'diving': 2389, 'push': 6555, 'slip': 3771, 'surface': 3893, 'sign': 2914,
 'actress': 1196, 'athlete': 6764, 'beautiful': 732, 'comedian': 3123, 'expensive': 728, 'fast': 658,
 'film director': 1201, 'handsome': 2737, 'smart': 4402, 'successful': 3106, 'talented': 1263, 'wise': 5380,
 'adventure': 6767, 'animation': 1169, 'movie': 6650, 'romance': 6007, 'thriller': 6616, 'suggestion': 5646,
 'turn off': 910, 'turn on': 909,
 'acting': 6802, 'album': 5097, 'bright': 4088, 'cast': 3896, 'classical music': 1878, 'heavy metal': 1216,
 'jazz': 831, 'lyrics': 3260, 'pop': 832, 'rap': 833, ('7c In the charts!', 'rock'): 835, 'role': 3423,
 'singer': 780, 'soul': 1890, 'tune': 4657, 'voice': 5349,
 'footballer': 774, 'goalkeeper': 3126, 'professional': 3445, 'stadium': 749, 'team': 4426,
 'extract': 6777, 'feeling': 6099, 'horror film': 3037, 'introduce': 6943, 'scene': 3911, 'sound': 4522,
 'violin': 1232,
 'breathe': 3245, 'burn': 3246, 'cloud': 7233, 'distance': 6350, 'fog': 7231, 'gather': 3573, 'habitat': 3315,
 'lake': 715, 'land': 3356, 'pollute': 1277, 'snow': 1779, 'solar power': 3803, 'stream': 6151, 'make up': 6967,
 'join': 4493, 'ladder': 3888, 'recycle': 1279, 'rubbish': 2873,
 'camel': 4728, 'desert': 712, 'parrot': 19, 'penguin': 1270,
 'deer': 2995, 'garlic': 2695, 'geese': 4724, 'nest': 4217, 'remote': 4040, 'reserve': 4689, 'sheep': 1832,
 'wildlife': 2514,
 'bank account': 2923, 'cash': 2032, 'cost': 6042, 'credit card': 6051,
 'bacteria': 5950, 'carnivore': 4622, 'energy': 4439, 'grass': 1764, 'grasshopper': 5525, 'herbivore': 4625,
 'hunt': 1275, 'omnivore': 4627, 'provide': 7254,
 'bar': 4592, 'biscuit': 5821, 'box': 47, 'butter': 451, 'carton': 4596, 'cereal': 7106, 'chips': 5929,
 'chocolate': 452, 'cola': 2058, 'cream': 2043, 'cup': 322, 'curry': 2044, 'dairy products': 5942, 'egg': 453,
 'fish': 254, 'fruit': 435, 'grains': 7193, 'grilled': 2689, 'hamburger': 5921, 'honey': 1869, 'ice cream': 5873,
 'jar': 4601, 'juice': 1538, 'meat': 437, ('9a You are what you eat!', 'milk'): 456, 'olive oil': 4582,
 'packet': 5864, 'pasta': 440, 'peas': 257, 'pepper': 1670, 'pizza': 251, 'poultry': 7097, 'rice': 442,
 'salad': 317, 'salt': 1672, 'sandwich': 5912, 'snack': 4608, 'sweets': 1750, 'takeaway': 5936, 'tin': 4611,
 'toast': 1875, 'tomato': 4590, 'tuna': 447, 'vegetables': 319, 'yoghurt': 450, 'take away': 3082,
 'take back': 2931,
 'basketball': 84, 'camera': 684, 'cashier': 857, "chemist's": 873, 'cleaner': 1352, 'clothes shop': 874,
 'diary': 1743, 'first aid kit': 2399, "jeweller's": 5976, 'manager': 1950, 'ring': 1031, 'shop assistant': 779,
 'socks': 276, 'sports shop': 879, 'swimming trunks': 4749, 'swimsuit': 1165, 'toy shop': 6451,
 'bowl': 321, 'checked': 1042, 'cushion': 554, 'leather': 1298, 'oval': 4679, 'paper': 220, 'plain': 1044,
 'plastic': 1301, 'silver': 1302, 'square': 4171, 'striped': 1046, 'wallet': 1491, 'wood': 1303,
 'exchange': 3572, ('English in Use 9', 'match'): 5331, 'trainers': 484, 'bargain': 3651, 'share': 3374,
 'argue': 1331, 'daily': 5555, 'disagree': 3175, 'headache': 366, 'lose': 3966, 'mean': 3715, 'opinion': 2678,
 'rumour': 3750, 'stressful': 3105, 'unfair': 2762, 'valuable': 4053,
 'ambulance': 5582, 'hurt': 2989, 'wrap': 3077, 'exhausted': 1346, 'forehead': 2960, 'meal': 4559,
 'vitamin': 7187, 'hospital': 24, 'deal with': 3458, 'swallow': 3772,
 'cheerful': 2745, 'miserable': 2749, 'roast': 947, 'smooth': 2380, 'weak': 4405, 'grill': 3391,
}
# нашлось в тренажёре, но смысл другой — рисуем своё
MISMATCH = {
 ('1a A city mouse or a country mouse?', 'milk'): 'в тренажёре «молоко», у нас «доить»',
 'facilities': 'в тренажёре «удобства», у нас «оборудование»',
 'cry': 'в тренажёре «плакать», у нас «кричать»',
 ('2b A classic read', 'rock'): 'в тренажёре «рок», у нас «скала»',
 'notice': 'в тренажёре «объявление», у нас «замечать»',
 ('Across the Curriculum 2 – Literature', 'match'): 'в тренажёре «подходить», у нас «спичка»',
 'award': 'в тренажёре «присуждать», у нас «награда»',
 'jealous': 'в тренажёре «ревнивый», у нас «завистливый»',
 'brown': 'в тренажёре «коричневый», у нас «шатен»',
 'skinny': 'в тренажёре «обтягивающий», у нас «худой»',
 'chart': 'в тренажёре «диаграмма», у нас «хит-парад»',
 'hit': 'в тренажёре «ударять», у нас «хит»',
 'experience': 'в тренажёре «испытать», у нас «опыт»',
 'artist': 'в тренажёре «художник», у нас «исполнитель»',
 'fantasy': 'в тренажёре «фантазия», у нас «фэнтези»',
 'model': 'в тренажёре «модель» без пояснения, у нас «фотомодель»',
 'net': 'в тренажёре «интернет», у нас «сетка»',
 'leave': 'в тренажёре «уезжать», у нас «оставлять»',
 'plant': 'в тренажёре «растение», у нас «сажать»',
 'can': 'в тренажёре «мочь», у нас «консервная банка»',
 'frame': 'в тренажёре «каркас», у нас «рамка»',
 'take off': 'в тренажёре «взлетать», у нас «снимать»',
 'take out': 'в тренажёре «вынимать», у нас «приглашать с собой»',
 'move': 'в тренажёре «двигаться», у нас «переезжать»',
 'treat': 'в тренажёре «угощение», у нас «лечить»',
 'tablet': 'в тренажёре «планшет», у нас «таблетка»',
 'site': 'в тренажёре «сайт», у нас «место»',
 'primary': 'в тренажёре «начальный (о школе)», у нас «первичный»',
 'secondary': 'в тренажёре «средний (о школе)», у нас «вторичный»',
 'come out': 'в тренажёре «выходить (о фильме)», у нас «выходить, появляться»',
 'order': 'в тренажёре «заказ/приказывать», у нас «порядок»',
}
# одно слово — два смысла в одном классе: разные подписи на листах
HOMONYM = {('Across the Curriculum 2 – Literature', 'oil'): 'oil (a lock)', ('9a You are what you eat!', 'oil'): 'oil',
           ('3a Lead the way!', 'fit'): 'fit (healthy)', ('English in Use 9', 'fit'): 'fit (size)',
           ('2d – Culture Corner', 'trick'): 'trick (deceive)', ('6a The fun starts here!', 'trick'): 'trick (circus)',
           ('1c Hanging out', 'spot'): 'spot (place)', ('Across the Curriculum 7 – Music', 'spot'): 'spot (notice)',
           ('10d – Culture Corner', 'patient'): 'patient (hospital)',
           ('Across the Curriculum 4 – Media Studies', 'producer'): 'producer (radio)',
           ('Across the Curriculum 8 – Science', 'producer'): 'producer (food chain)',
           ('Across the Curriculum 4 – Media Studies', 'break down'): 'break down (machine)',
           ('Across the Curriculum 8 – Science', 'break down'): 'break down (rot)',
           ('1a A city mouse or a country mouse?', 'milk'): 'milk (a cow)', ('2b A classic read', 'rock'): 'rock (cliff)',
           ('Across the Curriculum 2 – Literature', 'match'): 'match (a light)'}
# без картинки: связки, отвлечённые слова и то, что детям не рисуем
NOPIC = {'eventually', 'according to', 'several', 'let alone', 'at first glance', 'include', 'come off it', 'have a point',
         'better safe than sorry', 'dusk to dawn', 'close at hand', 'against all odds', 'word soon gets around',
         'scratch my back and i\'ll scratch yours', 'he gets away with everything.', 'have it one\'s way',
         'break the chain', 'get the blame', 'cliché', 'specific', 'genuine', 'possible', 'logical', 'believable',
         'forgettable', 'basic', 'complete', 'obsession', 'psychology', 'enable', 'cause', 'exist', 'believe',
         'value', 'moral', 'duty', 'occasion', 'formal', 'incident', 'detail', 'copy', 'affect', 'choice', 'stuff',
         'designate', 'function', 'identify', 'fault', 'compound', 'organic', 'primary', 'secondary', 'tertiary',
         'conditions', 'event', 'order', 'excitement', 'enthusiasm', 'inform', 'opinion'}
# rum и gun рисуем (Анна, 18.10.2026): rum — пиратская бутылка без надписей, gun — старинный пистолет на сундуке
def nopic(term, pos):
    t = term.lower()
    if t in NOPIC: return True
    if t.rstrip('.') + '.' == t or t.endswith('!') or t.endswith('?') or '...' in t: return True  # реплики
    return False
def get(d, sec, t):
    return d.get((sec, t), d.get(t))
src = [r for r in csv.DictReader(open('tsv/grade_7.tsv'), delimiter='\t')
       if r['module'] not in ('People', 'Famous People/Characters', 'Places', 'Others')]
top = list(csv.DictReader(open('plan/g7_topics.tsv'), delimiter='\t'))
assert len(src) == len(top)
out, reuse_rows, bag = [], [], collections.defaultdict(list)
for r, t in zip(src, top):
    assert (r['module'], r['section'], r['term']) == (t['module'], t['section'], t['term'])
    sec, term = r['section'], r['term'].lower()
    n = int(r['module'].split()[1])
    folder = f"{r['module']}: {MOD[n]}"
    rid, mis = get(REUSE, sec, term), get(MISMATCH, sec, term)
    if rid:
        img, why = f'reuse:{rid}', 'совпал перевод'
    elif nopic(r['term'], r['pos']):
        img, why = 'none', 'связка / реплика / отвлечённое слово'
    elif mis:
        img, why = 'new', mis
    else:
        img, why = 'new', 'в тренажёре нет'
    cap = HOMONYM.get((sec, term), '')
    row = [folder, '', '', r['module'], sec_name(sec), r['term'], r['translation'], img, cap]
    if t['topic'].startswith('@'):
        bag[n].append((t['topic'][1:], row))
    else:
        row[2] = sec_name(sec) + (' · ' + t['topic'] if t['topic'] else '')
    out.append(row)
    reuse_rows.append([r['module'], sec_name(sec), r['term'], r['translation'],
                       img.split(':')[1] if img.startswith('reuse') else '', img.split(':')[0], why])
for n, items in bag.items():
    groups = collections.OrderedDict()
    for g, row in items: groups.setdefault(g, []).append(row)
    if len(items) <= 8:
        for g, rows in groups.items():
            for row in rows: row[2] = f'Module {n} · другие слова'
        continue
    big = max(groups, key=lambda g: len(groups[g]))
    names = {g: g for g in groups}
    small = [g for g in groups if g != big and len(groups[g]) <= 3]
    for g in small: names[g] = big
    if small: names = {g: (big.replace(' и ', ', ') + ' и полезные слова' if v == big else v) for g, v in names.items()}
    if len(set(names.values())) == 1:
        for rows in groups.values():
            for row in rows: row[2] = f'Module {n} · другие слова'
        continue
    for g, rows in groups.items():
        for row in rows: row[1], row[2] = 'Другие слова', f'Module {n} · другие слова · {names[g]}'
w = csv.writer(open('plan/g7_plan.tsv', 'w'), delimiter='\t', lineterminator='\n')
w.writerow(['folder', 'subfolder', 'deck', 'module', 'section', 'term', 'translation', 'image', 'caption']); w.writerows(out)
w = csv.writer(open('plan/g7_reuse.tsv', 'w'), delimiter='\t', lineterminator='\n')
w.writerow(['module', 'section', 'term', 'translation', 'reuse_id', 'image', 'reason']); w.writerows(reuse_rows)
keys = lambda d: {k if isinstance(k, str) else k[1] for k in d}
miss = (keys(REUSE) | keys(MISMATCH) | keys(HOMONYM)) - {r['term'].lower() for r in src}
assert not miss, miss
print('модуль | колод | слов | есть картинка | рисовать | без картинки')
tot = collections.Counter()
for m in dict.fromkeys(x[0] for x in out):
    xs = [x for x in out if x[0] == m]
    c = collections.Counter(x[7].split(':')[0] for x in xs)
    row = [len({x[2] for x in xs}), len(xs), c['reuse'], c['new'], c['none']]
    tot.update(dict(zip('dwrnz', row)))
    print(m, '|', ' | '.join(map(str, row)))
print('итого |', tot['d'], '|', tot['w'], '|', tot['r'], '|', tot['n'], '|', tot['z'])
