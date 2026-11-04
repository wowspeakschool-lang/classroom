# -*- coding: utf-8 -*-
"""Серии «Составь предложение» / «Собери слово» → одно задание с items (решение методиста 04.11.2026).

series_raw.json — подряд идущие блоки order (от двух) из базы, выгрузка 04.11.2026.
Выход: plan.json, spisok.md → «Серии «Составь предложение» — проверить.docx», apply.sql.
Первый блок серии остаётся (его id), в нём title + items (+ skill/material первого блока),
остальные блоки серии удаляются, нумерация урока смыкается.
"""
import json, re, collections, hashlib
J = json.load(open('series_raw.json'))
LES = json.load(open('../podvodki/lessons.json'))
NAMES = {'sm0': 'Super Minds Starter', 'sm1': 'Super Minds 1', 'sm2': 'Super Minds 2', 'sm3': 'Super Minds 3',
         'gg1': 'Go Getter 1', 'gg2': 'Go Getter 2', 'gg3': 'Go Getter 3'}
PLURAL = [('Составь предложение', 'Составь предложения'), ('Собери предложение', 'Собери предложения'),
          ('Собери слово из частей', 'Собери слова'), ('Собери слово', 'Собери слова'), ('Составь слово', 'Составь слова'),
          ('Составь правильное предложение', 'Составь правильные предложения'), ('Составь вопрос', 'Составь вопросы')]
def plural(t):
    for a, b in PLURAL:
        if t.startswith(a): return b + t[len(a):]
    return t
def letters(w): return bool(w) and all(len(x) <= 1 for x in w)

P = []
for s in J:
    bl = s['b']; ts = [(b['t'] or '').strip() for b in bl]
    nonempty = [t for t in ts if t]
    word = all(letters(b['w'] or []) for b in bl)
    pat = [re.match(r'^(.+?):\s*(.+)$', t) for t in ts]
    prompts = [None] * len(bl)
    if nonempty and len(set(nonempty)) == 1:
        title = plural(nonempty[0]); kind = 'один заголовок'
    elif all(pat):
        # «Собери слово: ручка» — подпись у каждого пункта, общий заголовок из начала
        heads = collections.Counter(plural(m.group(1).strip()) for m in pat)
        title = heads.most_common(1)[0][0]
        if word and '🔤' not in title: title += ' 🔤'
        prompts = [m.group(2).strip() for m in pat]; kind = 'подпись у каждого слова'
    elif nonempty and all(re.match(r'^(Составь предложени|Расставь слова)', t) for t in nonempty):
        # одна и та же инструкция разными словами — подписи не нужны
        title = plural(collections.Counter(nonempty).most_common(1)[0][0].rstrip('.')); kind = 'один заголовок'
    else:
        top = collections.Counter(nonempty).most_common(1)[0][0] if nonempty else ('Собери слова' if word else 'Составь предложения')
        title = plural(top.rstrip('.'))
        prompts = [t if (t and t != top) else None for t in ts]; kind = 'разные заголовки'
    # ручные правки трёх серий с разными по смыслу заголовками
    key = (s['c'], s['u'], s['l'])
    if key == ('gg2', 2, 'Homework 6'):
        title, prompts = 'Собери предложения', ['со словом because', 'со словом so']
    elif key == ('sm1', 6, 'Homework 3'):
        title, prompts = 'Слова перепутаны! Составь вопросы', [None] * len(bl)
    elif key == ('sm1', 6, 'Homework 7'):
        title, prompts = 'Слова перепутаны! Составь предложения и вопрос', [None] * len(bl)
    items = []
    for b, pr in zip(bl, prompts):
        it = {'words': b['w'] or [], 'sentence': b['s'] or ''}
        if pr or b['pr']: it['prompt'] = pr or b['pr']
        if b['i']: it['image'] = b['i']
        if b['a']: it['audio'] = b['a']
        if b['at'] is not None: it['audio_tts'] = b['at']
        items.append(it)
    P.append({'c': s['c'], 'u': s['u'], 'l': s['l'], 'lid': s['lid'], 'no': s['no'], 'n': len(bl), 'kind': kind,
              'keep': bl[0]['id'], 'del': [b['id'] for b in bl[1:]], 'old': ts, 'title': title, 'items': items, 'word': word})
json.dump(P, open('plan.json', 'w'), ensure_ascii=False, indent=1)

C = collections.Counter('3+' if x['n'] >= 3 else '2' for x in P)
L = ['# Серии «Составь предложение» и «Собери слово» — в одно задание: проверить', '',
     f"Серий: **{len(P)}** (по три и больше — {C['3+']}, по два — {C['2']}), блоков в них **{sum(x['n'] for x in P)}**. "
     f"После правки станет **{len(P)}** заданий — уйдёт {sum(x['n'] for x in P) - len(P)} одинаковых экранов.", '',
     '- От трёх пунктов ученик листает их по одному («Предложение 2 из 3» / «Слово 2 из 3»), два — стоят подряд на одном экране.',
     '- Заголовок — общий; если у блоков были разные подписи («Собери слово: ручка»), подпись остаётся у каждого пункта («ручка»).',
     '- Картинка и звук — у каждого пункта свои, как были.',
     '- Балл за задание — доля верно собранных предложений (слов): каждое засчитывается, только если собрано целиком.',
     '', 'Название урока — ссылка на превью (урок как есть сейчас, до правки). Номера блоков — как в редакторе, до правки.',
     'Где не нравится — напишите «курс, юнит, урок, блок → как надо».', '']
for c in NAMES:
    xs = [x for x in P if x['c'] == c]
    if not xs: continue
    L += ['---', '', f'## {NAMES[c]}', '', '| урок | блоки | было | станет |', '|---|---|---|---|']
    for x in xs:
        url = 'https://app.wowteach.ru/?run=' + x['lid'] + '&preview=1'
        old = collections.Counter(t or '(без заголовка)' for t in x['old'])
        was = '; '.join(f"«{t}»" + (f" ×{k}" if k > 1 else '') for t, k in old.items())
        pr = [it.get('prompt') for it in x['items']]
        st = f"«{x['title']}», {x['n']} {('слова' if x['n'] < 5 else 'слов') if x['word'] else ('предложения' if x['n'] < 5 else 'предложений')}"
        if any(pr): st += '<br>подписи: ' + ', '.join(p or '—' for p in pr)
        L.append(f"| [Unit {x['u']} · {x['l']}]({url}) | {x['no']}–{x['no'] + x['n'] - 1} | {was.replace('|', '/')[:200]} | {st.replace('|', '/')} |")
    L.append('')
open('spisok.md', 'w').write('\n'.join(L) + '\n')

pj = json.dumps([{'k': x['keep'], 'd': x['del'], 't': x['title'], 'i': x['items']} for x in P], ensure_ascii=False)
assert '$plan$' not in pj
SQL = open('apply_tpl.sql').read().replace('@@PLAN@@', pj)
open('apply.sql', 'w').write(SQL)
print(C, len(P), 'apply.sql', len(SQL.encode()), hashlib.md5(SQL.encode()).hexdigest())
