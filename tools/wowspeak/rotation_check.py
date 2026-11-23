#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка чередования: насколько часто у тем совпадают наборы заданий.

Аня, 23.11.2026: «если делать чередования, то по-разному, чтобы меньше было
през где задания идут одинаково. Например, игра 1, лидин 1, мини-задание 1,
вопросы к видео 1, и потом в третьей презе те же самые».

Старая формула брала лид-ин, видео и мини по одному модулю 5 - тройка
возвращалась ровно каждые пять тем. Здесь это меряется, а не обещается.
"""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_theme import plan, LEGACY_UNTIL

LO, HI = LEGACY_UNTIL + 1, LEGACY_UNTIL + 88
STAGE = ('mood', 'lead', 'video', 'mini')
# (что меряем, как достать, какой разрыв между повторами считаем приемлемым)
RULES = [
    ('набор разминка+лид-ин+видео+мини', lambda p: tuple(p[k] for k in STAGE), 999),
    ('тройка лид-ин+видео+мини',         lambda p: (p['lead'], p['video'], p['mini']), 10),
    ('пара лид-ин+видео',                lambda p: (p['lead'], p['video']), 5),
    ('пара лид-ин+мини',                 lambda p: (p['lead'], p['mini']), 5),
    ('пара игр Beginners',               lambda p: p['beg'], 8),
    ('тройка игр Advanced',              lambda p: p['adv'], 6),
]

def main():
    rows = [(r, plan(r)) for r in range(LO, HI + 1)]
    bad = 0
    print(f'темы {LO}-{HI} ({len(rows)} шт.)\n')
    for name, key, need in RULES:
        last, gaps = {}, []
        for r, p in rows:
            k = key(p)
            if k in last: gaps.append(r - last[k])
            last[k] = r
        got = min(gaps) if gaps else 999
        ok = got >= need
        bad += not ok
        word = 'не повторяется ни разу' if got == 999 else f'повтор через {got} тем'
        print(f'  [{"ок" if ok else "ПЛОХО"}] {name:<36} {word}, нужно не чаще чем через {need}')

    worst = 0
    for i in range(1, len(rows)):
        for j in range(max(0, i - 4), i):
            a, b = rows[i][1], rows[j][1]
            worst = max(worst, sum(a[k] == b[k] for k in STAGE))
    ok = worst <= 1
    bad += not ok
    print(f'\n  [{"ок" if ok else "ПЛОХО"}] с любой из 4 предыдущих тем совпадает {worst} позиция из 4, нужно не больше 1')

    print('\nкак часто используется каждый вариант:')
    for k in STAGE:
        c = Counter(p[k] for _, p in rows)
        lo, hi = min(c.values()), max(c.values())
        ok = hi <= lo * 1.6
        bad += not ok
        print(f'  [{"ок" if ok else "ПЛОХО"}] {k:<6} ' +
              ', '.join(f'{n} ×{v}' for n, v in c.most_common()))

    print('\nвсё в порядке' if not bad else f'\nнарушений: {bad}')
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main())
