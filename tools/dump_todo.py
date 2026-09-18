# -*- coding: utf-8 -*-
"""Данные для файла «доработать руками»: python3 tools/dump_todo.py u6_build doc/u6.json

Считывает сборку юнита (модуль со списком LESSONS) и выгружает в JSON то,
что попадёт в docx: строки «нужно от вас», пересобранные игры («СОСТАВ МОЙ»)
и исправленные опечатки. Номера блоков — как в редакторе, с 1.
"""
import importlib, json, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.getcwd())

import lib as L
from lib import TYPE_RU

mod = importlib.import_module(sys.argv[1])
out = {'unit': L.UNIT, 'course': L.COURSE, 'lessons': []}

for les in mod.LESSONS:
    rows, made, typos = [], [], []
    for i, (t, p, c, todo) in enumerate(les.blocks):
        n = i + 1
        if todo:
            need, look, why = todo
            rows.append([str(n), TYPE_RU.get(t, t), look, need, why])
        if 'СОСТАВ МОЙ' in c:
            made.append([str(n), TYPE_RU.get(t, t),
                         (p.get('title') or p.get('text') or '')[:110], c])
        if 'опечат' in c:
            typos.append([str(n), TYPE_RU.get(t, t), c])
    out['lessons'].append({
        'title': les.title, 'summary': les.summary, 'kind': les.kind,
        'blocks': len(les.blocks), 'todo': rows, 'made': made, 'typos': typos,
        'tts': sum(1 for _, p, _, _ in les.blocks
                   if '_tts' in json.dumps(p, ensure_ascii=False)),
    })

json.dump(out, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
print(sys.argv[2], sum(len(l['todo']) for l in out['lessons']), 'строк «нужно от вас»')
