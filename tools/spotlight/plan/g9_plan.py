"""Spotlight 9: план колод и картинок. tsv/grade_9.tsv + plan/g9_topics.tsv → plan/g9_plan.tsv, plan/g9_reuse.tsv.
Картинки: reuse:<id> — слово тренажёра с тем же смыслом (g8_match.py: общий корень перевода; спорные
совпадения разобраны вручную в SAME/MISMATCH ниже, 19.10.2026), new — рисовать, none — без картинки.
«Другие слова» модуля (темы с '@') — как в Spotlight 6–7: до 8 слов — одна колода «Module N · другие слова»;
больше — подпапка «Другие слова», колоды по темам; тема из 2–3 слов вливается в самую большую
с дописью «… и полезные слова»."""
import csv, os, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
from g8_match import roots  # noqa: E402
# совпадения с тренажёром посчитаны в базе (тот же общий корень перевода, что в g8_match):
# g9_reuse_rows.txt — номера строк grade_9.tsv (с 1), md5 сверен с базой 04.11.2026
REUSE = set(map(int, open('plan/g9_reuse_rows.txt').read().strip().split(',')))
def match(term, tr): raise RuntimeError('не используется')
# названия модулей — из содержания учебника (gtext/Spotlight_8_SB-страницы.txt)
# названия модулей и разделов — из содержания учебника (Spotlight_9_SB, стр. iii–vi), сверено 05.11.2026
MOD = {1: 'Celebrations', 2: 'Life & Living', 3: 'See it to believe it', 4: 'Technology', 5: 'Art & Literature',
       6: 'Town & Community', 7: 'Staying safe', 8: 'Challenges'}
SEC = {'Culture Corner 1': 'Culture Corner 1 – Pow-Wow. The Gathering of Nations',
       'PSHE': 'Across the Curriculum 1 – PSHE: Remembrance Day',
       'Culture Corner 2': 'Culture Corner 2 – 10 Downing Street',
       'Going Green 2': 'Going Green 2 – In Danger',
       'Culture Corner 3': 'Culture Corner 3 – The Most Haunted Castle in Britain',
       'Across the Curriculum 3': 'Across the Curriculum 3 – History: Painting Styles',
       'Culture Corner 4': 'Culture Corner 4 – The Gadget Show on five',
       'Going Green 4': 'Going Green 4 – E-waste… Why so much junk?',
       'Culture Corner 5': 'Culture Corner 5 – William Shakespeare',
       'Literature: Across the Curriculum': 'Across the Curriculum 5 – Literature: The Merchant of Venice',
       'Culture Corner 6': 'Culture Corner 6 – Welcome to Sydney, Australia',
       'Going Green 6': 'Going Green 6 – Green Transport',
       'Culture Corner 7': "Culture Corner 7 – BEWARE! The USA's Dangerous Wild Animals",
       'Across the Curriculum': 'Across the Curriculum 7 – PSHE: Protect yourself',
       'Culture Corner 8': 'Culture Corner 8 – Helen Keller',
       'Going Green 8': 'Going Green 8 – The Challenge of Antarctica'}
def base(s):
    return s.replace(' Phrasals & Phrases', '').replace(' Phrasal verbs', '').replace(' Phrases', '')
def sec_name(s):
    return SEC.get(base(s), base(s))
# g8_match считает «не совпало», но смысл тот же — берём картинку (раздел, слово)
# в базе слово то же, перевод другой, но смысл совпал — берём картинку (номера строк grade_9.tsv), разобрано 04.11.2026
SAME = {36,77,132,146,154,182,204,215,236,243,247,254,255,265,352,397,413,419,423,433,475,508,514,516,526,542,553,559,566,627,649,668,672,673,729,761,777,805,839,857,858,861,887,944,972,982,993,1013,1049,1100,1108,1110,1141,1142,1174,1197,1202,1215,1227,1246,1262,1273,1278,1280,1314,1338,1368,1375,1424,1447,1454,1489,1497,1521,1527,1535,1554,1622,1624,1633,1676,1691,1699,1702,1708,1717,1733,1743,1764,1790,1791,1793,1812,1816,1817,1829,1840,1880,1929,1938,1939,1976,1984,2000,2020,2074,2104,2191,2192,2200,2202}
# без картинки: отвлечённые слова и связки (части речи adv/conj/prep — тоже)
NOPIC = {'purpose', 'reason', 'benefit', 'opportunity', 'quality', 'contents', 'task', 'likely', 'indeed', 'rather',
         'pretty', 'attitude', 'disbelief', 'enthusiasm', 'view', 'argument', 'duration', 'emphasis', 'intention',
         'definitely', 'concern', 'consequence', 'condition', 'issue', 'point', 'fact', 'detail', 'aspect', 'case',
         'event', 'occasion', 'opinion', 'viewpoint', 'statement', 'sense', 'mind', 'state', 'stuff', 'item',
         'element', 'factor', 'option', 'alternative', 'outcome', 'result', 'process', 'procedure', 'sequence',
         'theory', 'phenomenon', 'reality', 'existence', 'being', 'source', 'origin', 'level', 'degree', 'term',
         'abbreviation', 'derivative', 'predicate', 'prefix', 'suffix', 'linker', 'linkers', 'syllable', 'gist',
         'rubric', 'paraphrase', 'restate', 'general truth', 'deduction', 'equivalent', 'relevant', 'irrelevant',
         'specific', 'genuine', 'possible', 'probable', 'improbable', 'logical', 'basic', 'complete', 'absolute',
         'actual', 'exact', 'certain', 'obvious', 'apparently', 'eventually', 'immediately', 'nowadays', 'normally',
         'occasionally', 'regularly', 'probably', 'hopefully', 'luckily', 'somehow', 'therefore', 'consequently',
         'furthermore', 'moreover', 'besides', 'although', 'either', 'but', 'once', 'twice', 'still', 'so far',
         'whole', 'least', 'plenty', 'various', 'variety', 'similar', 'similarity', 'contrast', 'enable',
         'entitle', 'involve', 'include', 'exist', 'seem', 'suppose', 'regard', 'refer', 'relate', 'represent',
         'require', 'indicate', 'justify', 'conclude', 'conclusion', 'summary', 'sum up'}
def nopic(term, pos):
    t = term.lower().strip()
    if t in NOPIC: return True
    if (pos or '').strip().lower() in ('adv', 'conj', 'prep', 'pos', 'adj/adv'): return True
    if t.endswith(('?', '!', '.')) or '...' in t: return True  # реплики
    return False
src = []
for i, r in enumerate(csv.DictReader(open('tsv/grade_9.tsv'), delimiter='\t'), 1):
    if r['term'].strip(): r['_i'] = i; src.append(r)
top = list(csv.DictReader(open('plan/g9_topics.tsv'), delimiter='\t'))
assert len(src) == len(top)
# омонимы: одно слово с разными переводами в разных разделах класса, обе — рисовать
by_term = collections.defaultdict(list)
for r in src: by_term[r['term'].lower().strip()].append(r)
out, reuse_rows, bag = [], [], collections.defaultdict(list)
for r, t in zip(src, top):
    assert (r['module'], r['section'], r['term']) == (t['module'], t['section'], t['term'])
    sec, term = r['section'], r['term'].strip()
    n = int(r['module'].split()[1])
    folder = f"{r['module']}: {MOD[n]}"
    k = 'reuse' if r['_i'] in REUSE or r['_i'] in SAME else None
    if k == 'reuse':
        img, why = f"reuse:{r['_i']}", 'совпал смысл (картинка — из базы по номеру строки)'
    elif nopic(term, r['pos']):
        img, why = 'none', 'связка / реплика / отвлечённое слово'
    else:
        img, why = 'new', 'в тренажёре нет'
    same = by_term[term.lower()]
    cap = ''
    # омоним — только если у переводов нет общего корня (иначе это одно слово, одна картинка)
    others = [x for x in same if x is not r]
    if img == 'new' and others and any(not (roots(x['translation']) & roots(r['translation'])) for x in others):
        cap = f"{term} ({r['translation'].split(',')[0].split(';')[0].strip()})"
    row = [folder, '', '', r['module'], sec_name(sec), term, r['translation'], img, cap]
    if t['topic'].startswith('@'):
        bag[n].append((t['topic'][1:], row))
    else:
        row[2] = sec_name(sec) + (' · ' + t['topic'] if t['topic'] else '')
    out.append(row)
    reuse_rows.append([r['module'], sec_name(sec), term, r['translation'],
                       img.split(':')[1] if img.startswith('reuse') else '', img.split(':')[0], why])
for n, items in bag.items():
    groups = collections.OrderedDict()
    for g, row in items: groups.setdefault(g, []).append(row)
    if len(items) <= 8:
        for rows in groups.values():
            for row in rows: row[2] = f'Module {n} · другие слова'
        continue
    big = max(groups, key=lambda g: len(groups[g]))
    names = {g: g for g in groups}
    small = [g for g in groups if g != big and len(groups[g]) <= 3]
    for g in small: names[g] = big
    if small: names = {g: (big + ' и полезные слова' if v == big and 'полезные' not in big else v) for g, v in names.items()}
    if len(set(names.values())) == 1:
        for rows in groups.values():
            for row in rows: row[2] = f'Module {n} · другие слова'
        continue
    for g, rows in groups.items():
        for row in rows: row[1], row[2] = 'Другие слова', f'Module {n} · другие слова · {names[g]}'
w = csv.writer(open('plan/g9_plan.tsv', 'w'), delimiter='\t', lineterminator='\n')
w.writerow(['folder', 'subfolder', 'deck', 'module', 'section', 'term', 'translation', 'image', 'caption']); w.writerows(out)
w = csv.writer(open('plan/g9_reuse.tsv', 'w'), delimiter='\t', lineterminator='\n')
w.writerow(['module', 'section', 'term', 'translation', 'reuse_id', 'image', 'reason']); w.writerows(reuse_rows)
print('модуль | колод | слов | есть картинка | рисовать | без картинки')
tot = collections.Counter()
for m in dict.fromkeys(x[0] for x in out):
    xs = [x for x in out if x[0] == m]
    c = collections.Counter(x[7].split(':')[0] for x in xs)
    row = [len({x[2] for x in xs}), len(xs), c['reuse'], c['new'], c['none']]
    tot.update(dict(zip('dwrnz', row)))
    print(m, '|', ' | '.join(map(str, row)))
print('итого |', tot['d'], '|', tot['w'], '|', tot['r'], '|', tot['n'], '|', tot['z'])
print('подписи-омонимы:', sorted({x[8] for x in out if x[8]}))
