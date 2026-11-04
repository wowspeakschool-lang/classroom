# -*- coding: utf-8 -*-
"""Подводки отдельным блоком перед заданием → внутрь задания (решение Анны 04.11.2026, «38 да»).

plan_agents.json — разбор по курсам (text_id, action merge|material|keep, targets, new_title…).
dups.txt         — текстовые блоки, чей текст и картинки уже целиком лежат в material
                   следующего задания (сверено запросом 04.11.2026): их просто убираем.
Выход: plan.json (итоговый), spisok.md → «Подводки в задания — проверить.docx», apply.sql.
"""
import json, re, subprocess, collections, hashlib
A = json.load(open('plan_agents.json'))
D = set(open('dups.txt').read().split())
LOST = dict(l.split(' ',1) for l in open('lost_pics.txt').read().strip().split('\n'))
NAMES = {'sm0': 'Super Minds Starter', 'sm1': 'Super Minds 1', 'sm2': 'Super Minds 2', 'sm3': 'Super Minds 3',
         'gg1': 'Go Getter 1', 'gg2': 'Go Getter 2', 'gg3': 'Go Getter 3',
         'wow-dragon-1': 'Wow Dragon 1', 'wow-dragon-2': 'Wow Dragon 2'}
ORDER = list(NAMES)
for x in A:
    if x['text_id'] in D and x['action'] == 'keep':
        x['action'] = 'dup'; x['targets'] = []
def lkey(x):
    m = re.search(r'\d+', x['lesson']); t = x['lesson']
    return (ORDER.index(x['course']), x['unit'], 1 if 'Test' in t else 0, int(m.group()) if m and 'Homework' in t else 0, x['text_no'])
A.sort(key=lkey)
json.dump(A, open('plan.json', 'w'), ensure_ascii=False, indent=1)
C = collections.Counter(x['action'] for x in A)

def esc(s): return (s or '').replace('|', '/').replace('\n', ' ').strip()
L = ['# Подводки — внутрь задания: проверить', '',
     f"Всего текстовых блоков перед заданием: **{len(A)}**. Убираем отдельным экраном: **{C['merge'] + C['material'] + C['dup']}**, "
     f"остаётся как есть: **{C['keep']}**.", '',
     '- **В заголовок** (' + str(C['merge']) + ') — подводка была инструкцией или похвалой: блок убираем, задание получает понятный заголовок.',
     '- **В материал** (' + str(C['material']) + ') — текст или картинка, по которым отвечают: переходит в «Материал задания» (на компьютере слева, на телефоне — кнопка «📖 Показать текст»).',
     '- **Дубль** (' + str(C['dup']) + ') — этот текст уже лежит в «Материале задания» следующего задания: отдельный экран просто убираем.',
     '- **Оставляем** (' + str(C['keep']) + ') — разделители серий, «Давай повторим…», карточки-правила, блоки со звуком, прописи, комиксы.', '',
     'Подсказки-правила («Помни: после love глагол с -ing», «Пример: He ___ (play) → is playing») не переносим — решение от 04.11.2026.',
     'Номера блоков — как в редакторе, до правки; после неё номера ниже сдвинутся.', '',
     'Где не нравится — напишите «курс, юнит, урок, блок → как надо».', '']
for c in ORDER:
    xs = [x for x in A if x['course'] == c and x['action'] != 'keep']
    ks = [x for x in A if x['course'] == c and x['action'] == 'keep']
    if not xs and not ks: continue
    L += ['---', '', f'## {NAMES[c]}', '']
    if xs:
        L += ['| юнит · урок | блок | было | станет |', '|---|---|---|---|']
        for x in xs:
            if x['action'] == 'dup':
                st = 'убираем — этот текст уже есть в «Материале» задания ' + str(x['text_no'] + 1)
            else:
                parts = []
                for t in x['targets']:
                    s = f"задание {t['no']}: «{esc(t.get('new_title') or t.get('old_title'))}»"
                    if (t.get('new_title') or '') and t.get('new_title') != t.get('old_title') and t.get('old_title'):
                        s += f" (было «{esc(t['old_title'])}»)"
                    parts.append(s)
                pre = '**в материал** ' if x['action'] == 'material' else '**в заголовок** '
                st = pre + '<br>'.join(parts)
                if x['text_id'] in LOST: st += f"<br>🟥 уходит картинка: {LOST[x['text_id']].strip()}"
            L.append(f"| Unit {x['unit']} · {x['lesson']} | {x['text_no']} | {esc(x['was'])[:180]} | {st} |")
        L.append('')
    if ks:
        L += ['**Оставляем как есть:**', '']
        for x in ks:
            L.append(f"- Unit {x['unit']} · {x['lesson']}, блок {x['text_no']} — {esc(x['reason'])[:160]}")
        L.append('')
open('spisok.md', 'w').write('\n'.join(L) + '\n')
print(C, sum(len(x['targets']) for x in A if x['action'] in ('merge', 'material')))

# ── apply.sql: план компактно, правка — одним DO-блоком ──
P = []
for x in A:
    if x['action'] == 'keep': continue
    e = {'t': x['text_id'], 'a': x['action'], 's': bool(x.get('strip_first_p'))}
    if x.get('material_html'): e['mh'] = x['material_html']
    if x.get('material_from_ids'): e['mf'] = x['material_from_ids']
    e['g'] = [{'id': t['id'], 'nt': (t.get('new_title') or '').strip()} for t in x['targets']]
    P.append(e)
pj = json.dumps(P, ensure_ascii=False)
assert '$plan$' not in pj
SQL = open('apply_tpl.sql').read().replace('@@PLAN@@', pj)
open('apply.sql', 'w').write(SQL)
print('apply.sql', len(SQL.encode()), hashlib.md5(SQL.encode()).hexdigest())
