"""Spotlight 5: названия юнитов в колодах, география в «Другие разделы», порядок колод.
Перезаписывает plan/g5_plan.tsv из tsv + g5_topics.tsv + g5_reuse*.tsv."""
import csv, os, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
T = {'1a': 'School!', '1b': 'First day!', '1c': 'My favourite subjects', '1d': 'Schools in England',
 '2a': "I'm from…", '2b': 'My things!', '2c': 'My collection', '2d': 'Souvenirs from Great Britain',
 '3a': 'At home', '3b': 'Move in!', '3c': 'My bedroom', '3d': 'A typical English house',
 '4a': 'My family!', '4b': 'Who is who?', '4c': 'Famous people', '4d': 'American TV families',
 '5a': 'Amazing creatures', '5b': 'At the zoo', '5c': 'My pet', '5d': 'Furry friends',
 '6a': 'Wakey, wakey!', '6b': 'At work', '6c': 'Weekends', '6d': 'Main sights',
 '7a': 'Year after year', '7b': 'Dress right', '7c': "It's fun!", '7d': 'Climate: Alaska',
 '8a': 'Festivals and celebrations', '8b': 'Master Chef', '8c': "It's my birthday!", '8d': 'Thanksgiving',
 '9a': 'Shopping time', '9b': "Let's go…", '9c': "Don't miss it!", '9d': 'Window shopping',
 '10a': 'Travel and leisure', '10b': "Let's have fun!", '10c': 'Just a note…', '10d': 'Hello from…'}
MOD = {1: 'School days', 2: "That's me!", 3: 'My home, my castle', 4: 'Family ties', 5: 'World animals',
       6: 'Round the clock', 7: 'In all weathers', 8: 'Special days', 9: 'Modern living', 10: 'Holidays'}
def sec_name(s):
    code = s.split(' ')[0]
    if code in T:
        return f'{code} Culture Corner: {T[code]}' if 'Culture' in s else f'{code} {T[code]}'
    return s
GEO_CITY = set('Agra Ballater Barranquilla Belfast Canberra Cork Dublin Edinburgh Glasgow London|New York City|Oban Ottawa Springfield|St Andrews|Stirling|Washington DC|Wellington York'.replace('|', '\n').replace(' ', '\n').split('\n')) - {''}
GEO_CITY |= {'New York City', 'St Andrews', 'Washington DC'}
GEO_CITY -= {'New', 'York', 'City', 'St', 'Andrews', 'Washington', 'DC'}; GEO_CITY.add('York')
GEO_PLACE = {'Aleutian Islands', 'Bering Sea', 'Forth', 'Kiska Island', 'Kodiak Island', 'Loch Ness', 'Mallorca',
  'Mount Kilimanjaro', 'Nunivak Island', 'Pacific Ocean', 'Pribilof Islands', 'the River Nile', 'the River Stirling',
  'St George Island', 'St Lawrence Island', 'St Matthew Island', 'St Paul Island', 'the Thames', 'the Himalayas',
  'Valley of the Kings', 'Dona Lola', 'Surrey', 'Southwest Alaska', 'Northern India'}
GEO_PART = {'Africa', 'America', 'Antarctica', 'Asia', 'Australia', 'Europe', 'North America', 'South America', 'South Asia'}
GEO_REUSE = {'Australia': 372, 'London': 4318, 'Brazil': 373, 'Canada': 4794, 'China': 375, 'Egypt': 376, 'England': 4796,
  'France': 4798, 'Germany': 4799, 'Greece': 4800, 'India': 377, 'Ireland': 4801, 'Italy': 1424, 'Japan': 4803, 'Mexico': 378,
  'New Zealand': 4805, 'Russia': 1428, 'Scotland': 4808, 'Spain': 379, 'Turkey': 380}
# без картинки: узнать на рисунке нельзя
GEO_NOPIC = {'Aleutian Islands', 'Kiska Island', 'Kodiak Island', 'Nunivak Island', 'Pribilof Islands', 'St George Island',
  'St Lawrence Island', 'St Matthew Island', 'St Paul Island', 'the River Stirling', 'Forth', 'Dona Lola', 'Surrey',
  'Southwest Alaska', 'Northern India', 'Ballater', 'Oban', 'Barranquilla', 'Springfield', 'Agra', 'Cork', 'Stirling', 'South Asia'}
src = list(csv.DictReader(open('tsv/grade_5.tsv'), delimiter='\t'))
rows = [r for r in src if r['module'] not in ('Geographical Names', 'Personal Names', 'Other Proper Names')]
top = list(csv.DictReader(open('plan/g5_topics.tsv'), delimiter='\t'))
reu = {}
for f in ('plan/g5_reuse.tsv', 'plan/g5_reuse2.tsv'):
    for r in csv.DictReader(open(f), delimiter='\t'):
        if r['reuse_id']: reu[(r['module'], r['section'], r['term'])] = r['reuse_id']
out = []
for r, t in zip(rows, top):
    assert (r['module'], r['section'], r['term']) == (t['module'], t['section'], t['term'])
    folder = 'Starter Unit' if r['module'] == 'Starter Unit' else r['module'] + ': ' + MOD[int(r['module'].split()[1])]
    deck = sec_name(r['section'] or r['module']) + (' · ' + t['topic'] if t['topic'] else '')
    rid = reu.get((r['module'], r['section'], r['term']))
    out.append([folder, deck, r['module'], r['section'], r['term'], r['translation'], f'reuse:{rid}' if rid else 'new'])
for r in src:
    if r['module'] != 'Geographical Names': continue
    t = r['term']
    kind = ('города' if t in GEO_CITY else 'острова, реки, горы' if t in GEO_PLACE
            else 'части света' if t in GEO_PART else 'страны A–I' if t.lstrip('(the ').upper()[:1] <= 'I' else 'страны J–W')
    out.append(['Другие разделы', 'Geographical Names · ' + kind, r['module'], '', t, r['translation'],
                'none' if t in GEO_NOPIC else f'reuse:{GEO_REUSE[t]}' if t in GEO_REUSE else 'new'])
# порядок: папки в порядке появления; колоды — по разделу, внутри раздела темы в порядке g5_topics.py
order = {}
for i, x in enumerate(out): order.setdefault((x[0], x[1]), i)
out.sort(key=lambda x: order[(x[0], x[1])])
w = csv.writer(open('plan/g5_plan.tsv', 'w'), delimiter='\t', lineterminator='\n')
w.writerow(['folder', 'deck', 'module', 'section', 'term', 'translation', 'image']); w.writerows(out)
c = collections.Counter(x[6].split(':')[0] for x in out); print(len(out), dict(c))
d = collections.Counter((x[0], x[1]) for x in out); print('decks', len(d))
for k in [k for k in d if k[0] == 'Другие разделы']: print(k, d[k])
print([k[1] for k in d if k[0].startswith('Module 1:')])
