"""Spotlight 7: листы для генерации — слова плана с отметкой «new» по 6 на лист (3×2), подряд по плану,
так что лист держится темы своей колоды. Описания — words.py. Порядковые числа («digits:1st» в плане)
рисует скрипт (symbols.py) — на листы не идут, лежат в DIGITS."""
import csv, os
from words import WORDS, NOTE
PLAN = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../spotlight/plan/g7_plan.tsv')
_rows = list(csv.DictReader(open(PLAN), delimiter='\t'))
_deck = {}
for r in _rows:
    _deck.setdefault(r['term'], r['deck'])

def _topic(deck):
    head, _, tail = deck.partition(' · ')
    return tail or head

S = []
for k in range(0, len(WORDS), 6):
    ws = WORDS[k:k + 6]
    topics = list(dict.fromkeys(_topic(_deck[t]) for t, _, _ in ws))
    notes = list(dict.fromkeys(NOTE[c] for _, c, _ in ws if NOTE.get(c)))
    S.append((' / '.join(topics), ' '.join(notes), ws))

# (term, подпись, 'ЦИФРЫ'), текст знака — в DIGIT_TEXT
DIGITS, DIGIT_TEXT = [], {}
for r in _rows:
    if r['image'].startswith('digits:'):
        DIGITS.append((r['term'], r['term'], 'ЦИФРЫ'))
        DIGIT_TEXT[r['term']] = r['image'].split(':', 1)[1]

# Листы замен (после проверки) — номера после основных. Списки — подписи, сцены — в промпте замены
# (docs/Тренажёр_Spotlight7_замены.md).
REPL = {97: ['beast', 'tan', 'guard', 'guide', 'shake hands', 'crayon', 'rich'],
        98: ['wrist', 'MP3 player', 'digital music player']}  # 98 — wrist без часов, плееры не как iPod (Анна 19.10.2026)  # 18.10.2026: сходство с Диснеем/Smokey Bear, голый торс, копьё, статуя без одежды, Crayola, Rolls-Royce
_w = {c: (t, c, d) for t, c, d in WORDS}  # по подписи: term бывает длиннее
for _n, _terms in sorted(REPL.items()):
    S.append(('замены', '', [_w[t] for t in _terms]))
