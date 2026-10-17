"""Spotlight 6: план колод и картинок. tsv/grade_6.tsv + plan/g6_topics.tsv → plan/g6_plan.tsv, plan/g6_reuse.tsv.
Картинки: reuse:<id> — слово тренажёра с тем же смыслом (сверено вручную по выборке words, image_url not null),
new — рисовать, digits:<x> — цифрами скриптом, none — без картинки."""
import csv, os, re, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
# 🟥 названия модулей — по памяти, сверить с учебником
MOD = {1: "Who's who?", 2: 'Here we are!', 3: 'Getting around', 4: 'Day after day', 5: 'Feasts',
       6: 'Leisure activities', 7: 'Now and then', 8: 'Rules and regulations', 9: 'Food and refreshments', 10: 'Holiday time'}
# названия Culture Corner — из содержания учебника (Spotlight 6 SB, Table of Contents)
CC = {'1d': 'The United Kingdom', '2d': 'Famous streets', '3d': 'Getting around London', '4d': 'Teenage life in Britain',
      '5d': 'The Highland games', '6d': 'Board games', '7d': 'Superman', '8d': 'Building Big',
      '9d': 'Places to eat in the UK', '10d': 'The Edinburgh Experience'}
def sec_name(s):
    s = s.replace('Use of English/', 'English in Use/')
    k = s.split(' ')[0]
    if s == f'{k} Culture Corner' and k in CC: s += ': ' + CC[k]
    return s
# lower(term) → id; ключ с разделом — для омонимов внутри класса
REUSE = {
 'age': 2273, 'aunt': 303, 'big': 520, 'brother': 422, 'child': 1437, 'children': 1438, 'cousin': 426, 'curly': 2732,
 'daughter': 299, 'dad': 414, 'fat': 1733, 'hair': 63, 'height': 5319, 'husband': 1442, 'long': 523, 'middle-aged': 2739,
 'mum': 412, 'old': 525, 'parents': 294, 'short': 526, 'sister': 423, 'slim': 1739, 'son': 298, 'straight': 2741,
 'uncle': 302, 'wavy': 567, 'wife': 1448, 'young': 1741, 'facial features': 5315,
 'address': 2272, 'camera': 684, 'computer': 685, 'nationality': 5063, 'skateboard': 76, 'surname': 2279, 'watch': 282,
 'credit card': 6051, 'full name': 5339, 'join a club': 3199,
 'brazil': 373, 'brazilian': 1421, 'british': 5056, 'chile': 374, 'compass': 4366, 'desert': 712, 'east': 4370,
 'exactly': 5627, 'germany': 4799, 'japan': 4803, 'japanese': 5061, 'north': 4367, 'poland': 4792, 'russia': 1428,
 'russian': 1429, 'south': 4368, 'spain': 379, 'spanish': 1431, 'valley': 2287, 'west': 4369,
 'belfast': 6169, 'country': 5001, 'edinburgh': 6173, 'england': 4796, 'ireland': 4801, 'london': 4318, 'map': 337,
 'population': 3320, 'scotland': 4808, 'wales': 6238, 'the union jack': 5133, 'solar system': 4381,
 'january': 621, 'february': 622, 'march': 623, 'april': 624, 'may': 625, 'june': 626, 'july': 627, 'august': 628,
 'september': 629, 'october': 630, 'november': 631, 'december': 632, 'monday': 614, 'tuesday': 615, 'wednesday': 616,
 'thursday': 617, 'friday': 618, 'saturday': 619, 'sunday': 620, 'celebrate': 4235, "o'clock": 1550,
 'armchair': 52, 'bathroom': 1459, 'bedroom': 260, 'bookcase': 268, 'carpet': 553, 'ceiling': 1935, 'cooker': 5196,
 'cupboard': 5861, 'cushion': 554, 'curtain': 4531, 'expensive': 728, 'fireplace': 5232, 'flower': 100, 'fridge': 549,
 'kitchen': 264, 'mirror': 51, 'newspaper': 1644, 'painting': 269, 'shelf': 2680, 'sink': 990, 'wardrobe': 5218,
 'coffee table': 5211, 'dining room': 263, 'living room': 261, 'move house': 2724,
 'aspirin': 5964, "baker's": 4528, 'bank': 332, 'café': 26, "chemist's": 873, "greengrocer's": 876, 'library': 336,
 "newsagent's": 877, 'stamp': 5108, 'supermarket': 340, 'vegetables': 319, 'bus station': 333, 'post office': 753,
 'sports shop': 879, 'teddy bear': 5082, 'street': 30, 'choose': 3471, 'heating': 2416,
 'check': 4635, 'cross': 1924, 'dangerous': 657, 'ride': 595, 'safe': 731, 'traffic': 2513, 'use': 5507, 'on foot': 2309,
 'careful': 2743, 'gallery': 3087, 'perfect': 1909, 'plane': 228, 'remember': 1507, 'train': 232,
 'bring (brought)': 5897, 'fan': 2185, 'fast': 658, 'hobby': 5287, 'jogging': 2819, 'team': 4426, 'be born': 1185,
 'forget (forgot)': 5944, 'get around': 3631, 'journey': 4626, 'luggage': 2312, 'tourist': 1985, 'underground': 1703,
 'warn': 3436,
 'always': 4525, 'catch (caught)': 1590, 'cook': 324, 'cry': 5501, 'frog': 59, 'habit': 5479, 'kiss': 1010, 'laugh': 5288,
 ('4a', 'lose (lost)'): 3966, ('6b', 'lose (lost)'): 1150, 'never': 4540, 'often': 5557, 'sometimes': 4547,
 'spend (spent)': 6079, 'usually': 4549, 'do my homework': 601, 'get dressed': 2, 'go out with friends': 1704,
 'have a shower': 606, 'listen to music': 393, 'play sports': 4542,
 'awful': 5148, 'boring': 521, 'chicken': 255, 'comedy': 1170, 'dancing': 1599, 'decide': 5786, 'delicious': 961,
 'disgusting': 962, 'enjoyable': 3692, 'exciting': 727, 'fine': 1904, 'fish': 254, 'great': 1688, 'hamburger': 5921,
 'horrible': 1906, 'interesting': 763, 'news': 2511, 'pizza': 251, 'science fiction': 3040, 'skiing': 671,
 'terrible': 1911, 'windsurfing': 677, 'wonderful': 1774, 'eat out': 3582,
 'camp': 6061, 'climb/go climbing': 1923, 'meet (met)': 1593, 'put on (a dress)': 5763, 'set off': 2921,
 'disagree': 3175, 'teenage': 2742, 'mobile phone': 356, 'semi-detached house': 971, 'soap opera': 3041,
 'hope': 4492, 'worry': 4828, 'feel better': 1611,
 'bake': 4526, 'dance': 4144, 'grapes': 44, 'do the shopping': 325, 'make a cake': 2706, 'play the drums': 2002,
 'celebration': 5844, 'clean up': 993, 'cool': 522, 'costume': 5845, 'dress up': 5846, 'exchange': 3572, 'guest': 2310,
 'join in': 3480, 'colourful': 2370, 'festive': 5847, 'last': 5850, 'important': 1689, 'exchange gifts': 5855,
 'have a great time': 2624, 'advertisement': 2207, 'before': 5554, 'compete': 1149, 'competition': 4056,
 'popular': 1772, 'rope': 4345, 'traditional': 3291, 'belt': 1019, 'create': 3231, 'strange': 4984, 'tulip': 5968,
 'brilliant': 1802, 'brochure': 3139, 'leaflet': 6147, 'learn': 4145, 'novel': 3088, 'paint': 1316,
 'photography': 2601, 'present': 4328, 'tiring': 3030, 'go cycling': 884, 'have fun': 2626,
 'agree': 5643, 'argue': 1331, 'arrangement': 3558, 'chess': 490, 'enjoy': 5770, ('6b', 'fair'): 4637,
 ('1a', 'fair'): 2735, 'permanent': 5483, 'suggest': 3429, 'win (won)': 1154, 'board game': 2435,
 'coconut': 12, 'corn': 5918, ('6c', 'dice'): 4249, 'go up': 5815, 'hear (heard)': 5393, 'in': 4206, 'island': 714,
 'lonely': 2659, 'parrot': 19, 'rice': 442, 'sing (sang)': 597, 'square': 4171, 'think (thought)': 1595,
 'under': 4204, 'warm': 1783,
 'customer': 5136, 'cost (cost)': 6042, 'discover': 4717, 'design': 1313, 'invent': 1315,
 'attach': 4397, 'glove': 4499, 'glue': 4275, 'look for': 995, 'scissors': 483, 'wooden': 2382, 'wrap': 3077,
 'busy': 760, 'crowded': 4323, 'different': 5251, 'modern': 764, 'quiet': 766, 'wealthy': 3662, 'ugly': 661,
 'yesterday': 4694,
 'anyway': 5390, 'bored': 704, 'creature': 3311, 'huge': 5629, 'knock': 4642, 'miserable': 2749, 'naughty': 4646,
 'owl': 5371, 'rush': 4018, 'scared': 707, 'shout': 1333, 'stairs': 265, 'stressed': 5793, 'tired': 708,
 ('7b', 'treat'): 5915, 'worried': 709,
 'biography': 3085, 'cartoon': 2183, 'die': 1925, 'garage': 538, 'receive': 1930, 'studio': 2203,
 'adopt': 4692, 'adult': 5399, 'farmer': 773, 'invisible': 2761, 'powerful': 3817, 'shy': 1072, 'smart': 4402,
 'item': 6043, 'leather': 1298,
 'cottage': 969, 'hotel': 6056, 'palace': 1938, 'poster': 50, 'student': 4969, 'tidy': 856, 'block of flats': 967,
 'friendly': 581, 'gym': 4916, 'intelligent': 736, 'pretty': 5364, 'relax': 5504, 'serve': 4545, 'stadium': 749,
 'department store': 875, 'fast food (restaurant)': 5982, 'sports centre': 755, 'swimming pool': 33,
 'comfortable': 2332, 'own': 5176, 'rent': 6142,
 'amazing': 5036, 'complete': 5456, 'ground': 5541, 'historic': 3287, 'metre': 5481, 'visitor': 2317,
 'broken': 2968, 'graffiti': 2868, 'look after': 1276, 'pay (paid)': 5159, 'performance': 4740,
 'receptionist': 3130, 'seat': 6027, 'show': 5357, 'swing': 4247,
 'biscuit': 5821, 'bitter': 2938, 'carrot': 5822, 'cereal': 5869, 'chocolate': 452, 'dairy': 4599, 'dessert': 4672,
 'honey': 1869, ('9a', 'lamb'): 4603, 'meat': 437, 'onion': 4605, 'pepper': 1670, 'salty': 963, 'sausage': 252,
 'sour': 964, 'spicy': 965, 'sweet': 966, 'takeaway': 5936, 'toast': 1875, 'tomato': 4590, 'yoghurt': 450,
 'olive oil': 4582,
 'beef': 4594, 'crisps': 5910, 'greens': 38, 'melon': 2696, 'mushroom': 2053, 'steak': 256, 'waiter': 1662,
 'add': 939, 'boil': 942, 'fry': 944, 'mix': 945, 'peel': 946, 'pour': 3072, 'stir': 3075, 'taste': 4610,
 'pasta': 5876,
 'bowl': 321, 'carton': 4596, 'flour': 454, 'jar': 4601, 'kilo': 4602, 'loaf': 4604, 'packet': 5864,
 'receipt': 2036, 'shopping list': 860, 'protect': 1278,
 'collection': 5101, 'couple': 5737, 'flood': 1284, 'go/do sightseeing': 815,
 'cloudy': 4754, 'jacket': 271, 'rainy': 4751, 'raincoat': 386, 'scarf': 1033, 'shirt': 512, 'shorts': 274,
 'skirt': 273, 'sunny': 4240, 'sweater': 272, 'top': 516, 'trainers': 484, 'trousers': 519, 't-shirt': 277,
 'windy': 4241, 'brand new': 2770,
 'admire': 3469, 'castle': 1933, 'experience': 6074, 'musician': 1659, 'tour': 3360, 'transparent': 1311,
 'treasure': 4180, 'check in/out': 3629, 'volcano': 720,
}
# нашлось в тренажёре, но смысл другой — рисуем своё
MISMATCH = {
 'grey': 'в тренажёре «серый», у нас «седой»',
 'place': 'в тренажёре «место», у нас «площадь»',
 'power': 'в тренажёре «энергия», у нас «власть, сила»',
 'store': 'в тренажёре «хранить», у нас «магазин»',
 'block': 'в тренажёре «заблокировать», у нас «загораживать»',
 'park': 'в тренажёре «парк», у нас «парковать(ся)»',
 'room': 'в тренажёре «комната», у нас «место, пространство»',
 'fix': 'в тренажёре «чинить», у нас «устанавливать»',
 'treat (well)': 'в тренажёре «угощение», у нас «обращаться (хорошо)»',
 'drama': 'в тренажёре «театральный кружок», у нас «драма»',
 'star': 'в тренажёре «звезда», у нас «сниматься в главной роли»',
 'display': 'в тренажёре «дисплей», у нас «показ»',
 'miss': 'в тренажёре «пропускать», у нас «скучать»',
 'aim': 'в тренажёре «стремиться», у нас «цель»',
 'release': 'в тренажёре «освобождать», у нас «выпускать (в свет)»',
 'rubber': 'в тренажёре «ластик», у нас «резина»',
 'mine': 'в тренажёре «мой», у нас «рудник, шахта»',
 'live on': 'в тренажёре «жить на (доход)», у нас «продолжать жить»',
 'make up': 'в тренажёре «мириться», у нас «выдумывать»',
 'handle': 'в тренажёре «справляться», у нас «ручка»',
 'step': 'в тренажёре «ступенька», у нас «шаг»',
 'messy': 'в тренажёре «неряшливый» (о человеке), у нас «запачканный, грязный»',
 'hot': 'в тренажёре «жаркий/жарко», у нас «горячий»',
 'pound': 'в тренажёре «фунт» без пояснения и «фунт стерлингов», у нас фунт веса',
 'degree': 'в тренажёре «учёная степень», у нас «градус»',
 'band': 'в тренажёре «группа (музыкальная)», у нас «оркестр»',
 ('8d', 'floor'): 'в тренажёре «пол», у нас «этаж»',
 ('9b', 'dice'): 'в тренажёре «кубик», у нас «нарезать кубиками»',
 ('2b', 'floor'): None,  # пол — новый? нет: см. REUSE ниже
}
REUSE[('2b', 'floor')] = 537
del MISMATCH[('2b', 'floor')]
# без картинки: связки и отвлечённые слова, которые на рисунке не узнать
NOPIC = {'about', 'ago', 'anyway', 'as for', 'as well as', 'as much as possible', 'by the time', 'either', 'even',
         'except', 'in order to', 'only', 'the rest of', 'finally', 'definitely', 'in total', 'in the end', 'whole',
         'just', 'towards', 'i bet', 'what about...?', "what's up?", 'i beg your pardon!', 'at random', 'include',
         'have in mind', 'premise', 'depending on the occasion', 'requiring services', 'range from', 'flow of',
         'available', 'familiar', 'common', 'total', 'ultimate', 'object', 'occasion', 'event', 'item'}
def digits(term):
    m = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5, 'sixth': 6, 'seventh': 7, 'eighth': 8,
         'ninth': 9, 'tenth': 10, 'eleventh': 11, 'twelfth': 12, 'thirteenth': 13, 'fourteenth': 14, 'fifteenth': 15,
         'sixteenth': 16, 'seventeenth': 17, 'eighteenth': 18, 'nineteenth': 19, 'twentieth': 20, 'twenty-first': 21,
         'thirtieth': 30, 'thirty-second': 32, 'fortieth': 40, 'forty-fourth': 44}
    n = m[term]
    suf = 'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f'{n}{suf}'
def get(d, code, t):
    return d.get((code, t), d.get(t))
src = list(csv.DictReader(open('tsv/grade_6.tsv'), delimiter='\t'))
top = list(csv.DictReader(open('plan/g6_topics.tsv'), delimiter='\t'))
out, reuse_rows = [], []
for r, t in zip(src, top):
    assert (r['module'], r['section'], r['term']) == (t['module'], t['section'], t['term'])
    code, term = r['section'].split(' ')[0], r['term'].lower()
    folder = r['module'] + ': ' + MOD[int(r['module'].split()[1])]
    deck = sec_name(r['section']) + (' · ' + t['topic'] if t['topic'] else '')
    rid, mis = get(REUSE, code, term), get(MISMATCH, code, term)
    if t['topic'] == 'порядковые числа':
        img, why = 'digits:' + digits(term), 'порядковое число — цифрами'
    elif rid:
        img, why = f'reuse:{rid}', 'совпал перевод'
    elif mis:
        img, why = 'new', mis
    elif term in NOPIC:
        img, why = 'none', 'связка / отвлечённое слово'
    else:
        img, why = 'new', 'в тренажёре нет'
    out.append([folder, deck, r['module'], sec_name(r['section']), r['term'], r['translation'], img])
    reuse_rows.append([r['module'], sec_name(r['section']), r['term'], r['translation'],
                       img.split(':')[1] if img.startswith('reuse') else '', img.split(':')[0], why])
# крошечные «другие слова» (2–3 слова) влиты в соседнюю тему раздела (решение 17.10.2026)
MERGE = {
    "8a That's the rule · другие слова": "8a That's the rule · правила и другие слова",
    "8a That's the rule · правила": "8a That's the rule · правила и другие слова",
    '9a Food & Drink · другие слова': '9a Food & Drink · продукты и другие слова',
    '9a Food & Drink · продукты': '9a Food & Drink · продукты и другие слова',
    '9b On the menu · другие слова': '9b On the menu · блюда, продукты и другие слова',
    '9b On the menu · продукты и блюда': '9b On the menu · блюда, продукты и другие слова',
    "9c Let's cook! · другие слова": "9c Let's cook! · упаковка, меры и покупки",
    "9c Let's cook! · упаковка и меры": "9c Let's cook! · упаковка, меры и покупки",
}
assert all(any(x[1] == k for x in out) for k in MERGE), [k for k in MERGE if not any(x[1] == k for x in out)]
for x in out: x[1] = MERGE.get(x[1], x[1])
w = csv.writer(open('plan/g6_plan.tsv', 'w'), delimiter='\t', lineterminator='\n')
w.writerow(['folder', 'deck', 'module', 'section', 'term', 'translation', 'image']); w.writerows(out)
w = csv.writer(open('plan/g6_reuse.tsv', 'w'), delimiter='\t', lineterminator='\n')
w.writerow(['module', 'section', 'term', 'translation', 'reuse_id', 'image', 'reason']); w.writerows(reuse_rows)
# сводка по модулям
used = {k if isinstance(k, str) else k[1] for k in REUSE} | {k if isinstance(k, str) else k[1] for k in MISMATCH}
miss = used - {r['term'].lower() for r in src}
assert not miss, miss
print('модуль | колод | слов | есть картинка | рисовать | цифрами | без картинки')
tot = collections.Counter()
for m in dict.fromkeys(x[0] for x in out):
    xs = [x for x in out if x[0] == m]
    c = collections.Counter(x[6].split(':')[0] for x in xs)
    row = [len({x[1] for x in xs}), len(xs), c['reuse'], c['new'], c['digits'], c['none']]
    tot.update(dict(zip('dwrnzx', row)))
    print(m, '|', ' | '.join(map(str, row)))
print('итого |', ' | '.join(str(tot[k]) for k in 'dwrnzx'))
