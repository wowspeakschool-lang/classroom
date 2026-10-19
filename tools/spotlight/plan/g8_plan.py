"""Spotlight 8: план колод и картинок. tsv/grade_8.tsv + plan/g8_topics.tsv → plan/g8_plan.tsv, plan/g8_reuse.tsv.
Картинки: reuse:<id> — слово тренажёра с тем же смыслом (g8_match.py: общий корень перевода; спорные
совпадения разобраны вручную в SAME/MISMATCH ниже, 19.10.2026), new — рисовать, none — без картинки.
«Другие слова» модуля (темы с '@') — как в Spotlight 6–7: до 8 слов — одна колода «Module N · другие слова»;
больше — подпапка «Другие слова», колоды по темам; тема из 2–3 слов вливается в самую большую
с дописью «… и полезные слова»."""
import csv, os, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
from g8_match import match, roots  # noqa: E402  (plan/ в sys.path, скрипт запускается из plan/)
# названия модулей — из содержания учебника (gtext/Spotlight_8_SB-страницы.txt)
MOD = {1: 'Socialising', 2: 'Food & Shopping', 3: 'Great Minds', 4: 'Be Yourself', 5: 'Global Issues',
       6: 'Culture Exchanges', 7: 'Education', 8: 'Pastimes'}
# темы разделов из содержания учебника
SEC = {'Culture Corner 1': 'Culture Corner 1 – Socialising in the UK',
       'Across the Curriculum: PSHE': 'Across the Curriculum 1 – PSHE: Dealing with conflict',
       'Culture Corner 2': 'Culture Corner 2 – Charity begins at home',
       'Going Green 2': 'Going Green 2 – Paper bag vs plastic bag',
       'Culture Corner 3': 'Culture Corner 3 – English banknotes',
       'Across the Curriculum: History': 'Across the Curriculum 3 – History',
       'Culture Corner 4': 'Culture Corner 4 – Traditional costumes in the UK',
       'Going Green 4': 'Going Green 4 – Eco-clothes',
       'Culture Corner 5': 'Culture Corner 5 – Highland cows',
       'Across the Curriculum: Science': 'Across the Curriculum 5 – Science: Tornadoes & Hail',
       'Culture Corner 6': 'Culture Corner 6 – The Thames',
       'Going Green 6': 'Going Green 6 – Monuments in danger',
       'Culture Corner 7': 'Culture Corner 7 – Trinity College Dublin',
       'Across the Curriculum: ICT': 'Across the Curriculum 7 – ICT: Using a computer network',
       'Culture Corner 8': 'Culture Corner 8 – Mascots',
       'Going Green 8': 'Going Green 8 – Project A.W.A.R.E.'}
def base(s):
    return s.replace(' Phrasals & Phrases', '').replace(' Phrasal verbs', '').replace(' Phrases', '')
def sec_name(s):
    return SEC.get(base(s), base(s))
# g8_match считает «не совпало», но смысл тот же — берём картинку (раздел, слово)
SAME = {('1a', 'furious'), ('1b', 'neighbourhood'), ('1d', 'humorous'), ('1d', 'sensible'),
        ('1d Phrasals & Phrases', 'run into'), ('1e', 'anniversary'), ('Culture Corner 1', 'hug'),
        ('2a', 'encourage'), ('2a', 'grilled'), ('2a', 'train station'), ('2a Phrasals & Phrases', 'date back'),
        ('2a Phrasals & Phrases', 'packed lunch'), ('2c', 'jewellery'), ('2d', 'chop'), ('Going Green 4', 'chop'),
        ('2d', 'fold'), ('2d', 'reasonable'), ('2e Phrasals & Phrases', 'break down'), ('2f', 'increase'),
        ('Culture Corner 2', 'donate'), ('3a', 'nearby'), ('3a', 'reach'), ('5a', 'reach'), ('5c', 'reach'),
        ('3a', 'flight'), ('3c', 'spot'), ('3d', 'graduate'), ('3e', 'cover'), ('3f Phrasals & Phrases', 'pass out'),
        ('Across the Curriculum: History', 'storm'), ('4b Phrasals & Phrases', 'hang on'), ('4c', 'borrow'),
        ('4d', 'needle'), ('4d', 'scary'), ('4d', 'scream'), ('5a', 'scream'), ('4e', 'nasty'), ('4f', 'afford'),
        ('Going Green 4 Phrasals & Phrases', 'environmentally friendly'), ('5e', 'reduce'), ('5f', 'staff'),
        ('Across the Curriculum: Science', 'freeze'), ('6c', 'report'), ('6d Phrasals & Phrases', 'get off'),
        ('6e', 'accommodation'), ('6f', 'hire'), ('7a', 'connect'), ('7a', 'download'),
        ('7a Phrasals & Phrases', 'chat online'), ('7c', 'cheat'), ('7f', 'mean'), ('Culture Corner 7', 'precious'),
        ('8a', 'bizarre'), ('8b', 'rugby'), ('8c', 'reservation'), ('8c', 'boil'), ('8d', 'amazed'), ('8d', 'pitch')}
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
src = [r for r in csv.DictReader(open('tsv/grade_8.tsv'), delimiter='\t') if r['term'].strip()]
top = list(csv.DictReader(open('plan/g8_topics.tsv'), delimiter='\t'))
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
    k, best = match(term, r['translation'])
    if k == 'mismatch' and (sec, term.lower()) in SAME: k = 'reuse'
    if k == 'reuse':
        img, why = f'reuse:{best[0]}', f'совпал смысл: {best[1]}'
    elif nopic(term, r['pos']):
        img, why = 'none', 'связка / реплика / отвлечённое слово'
    elif k == 'mismatch':
        img, why = 'new', f'в тренажёре другой смысл: {best[1]}'
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
w = csv.writer(open('plan/g8_plan.tsv', 'w'), delimiter='\t', lineterminator='\n')
w.writerow(['folder', 'subfolder', 'deck', 'module', 'section', 'term', 'translation', 'image', 'caption']); w.writerows(out)
w = csv.writer(open('plan/g8_reuse.tsv', 'w'), delimiter='\t', lineterminator='\n')
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
