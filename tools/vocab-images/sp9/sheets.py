"""Spotlight 9: листы для генерации — слова плана «new» по 8 на лист (4×2, как Spotlight 8), подряд по
модулям и колодам; лист не переходит границу модуля. Описания — words.py (w1…w8).
Одно слово в двух колодах (veteran) рисуется один раз — картинка ляжет на обе."""
import csv, os
from words import WORDS, NOTE
PLAN = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../spotlight/plan/g9_plan.tsv')
PER = 8
_rows = list(csv.DictReader(open(PLAN), delimiter='\t'))
_deck, _mod = {}, {}
for r in _rows:
    _deck.setdefault(r['term'], r['deck']); _mod.setdefault(r['term'], r['module'])

def _topic(deck):
    head, _, tail = deck.partition(' · ')
    return tail or head

S, MOD_OF = [], []
_seen, _by = set(), {}
for w in WORDS:
    if w[0] in _seen: continue
    _seen.add(w[0]); _by.setdefault(_mod[w[0]], []).append(w)
for m, ws_all in _by.items():
    for k in range(0, len(ws_all), PER):
        ws = ws_all[k:k + PER]
        topics = list(dict.fromkeys(_topic(_deck[t]) for t, _, _ in ws))
        notes = list(dict.fromkeys(NOTE[c] for c, _, _ in ws if NOTE.get(c)))
        S.append((' / '.join(topics), ' '.join(notes), ws)); MOD_OF.append(m)
REPL, SKIP = {}, set()
DIGITS = []
