# -*- coding: utf-8 -*-
"""Собирает планы агентов (plan_*.json) в одну миграцию и отчёт «было → стало»."""
import json, glob, io, os, sys

SRC = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/gg1_order'
plany = []
for f in sorted(glob.glob(os.path.join(SRC, 'plan_*.json'))):
    plany.extend(json.load(open(f)))

oshibki = []
for x in plany:
    if sorted(x['stalo']) != sorted(x['bylo']):
        oshibki.append((x['urok'], 'stalo не перестановка bylo'))
    if x['stalo'][0] != x['bylo'][0]:
        oshibki.append((x['urok'], 'первым стоит не приветствие'))
    if x['stalo'][-1] != x['bylo'][-1]:
        oshibki.append((x['urok'], 'последним стоит не прощание'))
if oshibki:
    for o in oshibki: print('ОШИБКА', o)
    raise SystemExit('план не прошёл проверку')

menyaem = [x for x in plany if x['stalo'] != x['bylo']]
data = [{'lesson_id': x['lesson_id'], 'stalo': x['stalo']} for x in menyaem]

sql = io.StringIO()
sql.write('-- Go Getter 1: порядок заданий по лесенке сложности (решение Анны 20.11.2026)\n')
sql.write('create table if not exists classroom_backup_gg1_poryadok_20261120 as\n'
          'select b.* from classroom_blocks b\n'
          ' join classroom_lessons l on l.id = b.lesson_id\n'
          ' join classroom_units u on u.id = l.unit_id\n'
          ' join classroom_courses c on c.id = u.course_id\n'
          " where c.slug = 'gg1' and l.kind = 'homework';\n\n")
sql.write('do $$\ndeclare plan jsonb := $plan$' + json.dumps(data, ensure_ascii=False) + '$plan$::jsonb;\n'
          '        r jsonb; v_lesson uuid; i int; staryj int;\nbegin\n'
          '  for r in select * from jsonb_array_elements(plan) loop\n'
          "    v_lesson := (r->>'lesson_id')::uuid;\n"
          '    update classroom_blocks set sort_order = -1 - sort_order where lesson_id = v_lesson;\n'
          '    i := 0;\n'
          "    for staryj in select (x #>> '{}')::int from jsonb_array_elements(r->'stalo') x loop\n"
          '      update classroom_blocks set sort_order = i\n'
          '       where lesson_id = v_lesson and sort_order = -1 - (staryj - 1);\n'
          '      i := i + 1;\n'
          '    end loop;\n'
          '  end loop;\n'
          'end $$;\n')
io.open('/home/user/classroom/builds/gg1_poryadok/poryadok.sql', 'w', encoding='utf-8').write(sql.getvalue())

otchet = io.StringIO()
otchet.write('# Go Getter 1 — новый порядок заданий в домашках (20.11.2026)\n\n')
otchet.write(f'Разобрано домашек: {len(plany)}. Порядок изменён в {len(menyaem)}.\n\n')
for x in sorted(plany, key=lambda y: (y['unit'], y['urok'])):
    if x['stalo'] == x['bylo']:
        continue
    otchet.write(f"## Юнит {x['unit']} · {x['urok']}\n\n")
    otchet.write(f"Посмотреть: https://app.wowteach.ru/?run={x['lesson_id']}&preview=1\n\n")
    otchet.write(f"было: {' · '.join(map(str, x['bylo']))}\n\n")
    otchet.write(f"стало: {' · '.join(map(str, x['stalo']))}\n\n")
    otchet.write(f"{x['pochemu']}\n\n")
io.open('/home/user/classroom/builds/gg1_poryadok/otchet.md', 'w', encoding='utf-8').write(otchet.getvalue())
print('домашек:', len(plany), '· меняется:', len(menyaem), '· байт SQL:', len(sql.getvalue()))
