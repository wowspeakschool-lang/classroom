"""Проверка листов Spotlight 6 по плану: каждое «new» — ровно один раз, подписи и имена файлов уникальны."""
import csv, sys
sys.path.insert(0, '..')
from lib import fname
from sheets import S, DIGITS, PLAN, REPL
S = S[:len(S) - len(REPL)]  # листы замен повторяют слова — проверяем только основные
rows = list(csv.DictReader(open(PLAN), delimiter='\t'))
new = list(dict.fromkeys(r['term'] for r in rows if r['image'] == 'new'))
got = [t for _, _, ws in S for t, _, _ in ws]
caps = [c for _, _, ws in S for _, c, _ in ws] + [c for _, c, _ in DIGITS]
err = []
if sorted(got) != sorted(new):
    err.append(f'нет: {sorted(set(new) - set(got))}; лишние: {sorted(set(got) - set(new))}; дубли: {sorted({t for t in got if got.count(t) > 1})}')
if got != new: print('порядок отличается от плана (допустимо)')
for c in caps:
    if caps.count(c) > 1 or [fname(x).lower() for x in caps].count(fname(c).lower()) > 1: err.append('подпись ' + c)
for n, (_, _, ws) in enumerate(S, 1):
    if len(ws) != 6: print('лист', n, 'картинок', len(ws))
    for _, c, d in ws:
        if len(c.split()) > 5: err.append('длинная подпись ' + c)
        if len(d) > 140: print('длинное описание', c, len(d))
print(len(S), 'листов,', len(got), 'слов,', len(DIGITS), 'цифр')
print('\n'.join(sorted(set(err))) or 'ok')
