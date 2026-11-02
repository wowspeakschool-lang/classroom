"""Spotlight 8: листы для генерации — слова плана с отметкой «new» по 8 на лист (4×2, решение Анны
«чуть больше слов на картинку», 19.10.2026), подряд по плану, так что лист держится темы своей колоды.
Описания — words.py. Порядковые числа («digits:…» в плане) рисует скрипт (symbols.py) — на листы не идут."""
import csv, os
from words import WORDS, NOTE
PLAN = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../spotlight/plan/g8_plan.tsv')
PER = 8
_rows = list(csv.DictReader(open(PLAN), delimiter='\t'))
_deck = {}
for r in _rows:
    _deck.setdefault(r['term'], r['deck'])

def _topic(deck):
    head, _, tail = deck.partition(' · ')
    return tail or head

S = []
for k in range(0, len(WORDS), PER):
    ws = WORDS[k:k + PER]
    topics = list(dict.fromkeys(_topic(_deck[t]) for t, _, _ in ws))
    notes = list(dict.fromkeys(NOTE[c] for _, c, _ in ws if NOTE.get(c)))
    S.append((' / '.join(topics), ' '.join(notes), ws))

DIGITS, DIGIT_TEXT = [], {}
for r in _rows:
    if r['image'].startswith('digits:'):
        DIGITS.append((r['term'], r['term'], 'ЦИФРЫ'))
        DIGIT_TEXT[r['term']] = r['image'].split(':', 1)[1]

# Листы замен (после проверки) — номера после основных; списки — подписи.
REPL = {}
_w = {c: (t, c, d) for t, c, d in WORDS}
for _n, _terms in sorted(REPL.items()):
    S.append(('замены', '', [_w[t] for t in _terms]))
