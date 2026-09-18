# -*- coding: utf-8 -*-
"""Проверка payload до заливки — обязательный шаг.

    python3 tools/val.py u6sql sm2/u6

Первый аргумент — папка с файлами SQL, второй — папка картинок внутри media/.
Печатает ошибки и их число; заливать можно только при «ОШИБОК: 0».
"""
import re, json, glob, os, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQ, MDIR = sys.argv[1], sys.argv[2]


def names(path):
    return set(os.path.splitext(f)[0] for f in os.listdir(path)) if os.path.isdir(path) else set()


MEDIA = names(f'{ROOT}/media/{MDIR}')
SHARED = names(f'{ROOT}/media/shared')
RX = r"\(v_lesson, '(\w+)', replace\(\$blk\$(.*?)\$blk\$, '@@MEDIA@@', v_media\)::jsonb, (\d+)\)"
bad = 0

for fn in sorted(glob.glob(f'{SQ}/*.sql')):
    s = open(fn).read()
    print('=' * 70); print(fn)
    blocks = re.findall(RX, s, re.S)
    for t, raw, so in blocks:
        so = int(so)
        try:
            p = json.loads(raw)
        except Exception as e:
            print(f'  !! JSON {t}#{so}: {e}'); bad += 1; continue
        if t == 'quiz':
            for qi, q in enumerate(p['questions']):
                opts = [o['text'] for o in q['options']]
                if len(set(opts)) != len(opts):
                    print(f'  !! дубль вариантов {so}/q{qi}: {opts}'); bad += 1
                for c in q['correct']:
                    if not (0 <= c < len(opts)):
                        print(f'  !! correct вне диапазона {so}/q{qi}'); bad += 1
                if q['type'] == 'single' and len(q['correct']) != 1:
                    print(f'  !! single с {len(q["correct"])} ответами {so}/q{qi}'); bad += 1
                if q['type'] == 'multiple' and len(q['correct']) < 2:
                    print(f'  !! multiple с одним ответом {so}/q{qi}'); bad += 1
                if not q['correct']:
                    print(f'  !! нет верного ответа {so}/q{qi}'); bad += 1
        elif t == 'match':
            r = [x['right'] for x in p['pairs']]
            if len(set(r)) != len(r):
                d = [k for k, v in collections.Counter(r).items() if v > 1]
                print(f'  !! дубль правых значений {so}: {d}'); bad += 1
            lf = [x.get('left') or x.get('left_image') for x in p['pairs']]
            if len(set(lf)) != len(lf):
                print(f'  !! дубль левых значений {so}'); bad += 1
            for x in p['pairs']:
                if not (x.get('left') or x.get('left_image')):
                    print(f'  !! пустая левая часть {so}'); bad += 1
        elif t == 'gaps':
            g = re.findall(r'__(.+?)__', p['text'])
            if not g:
                print(f'  !! нет пропусков {so}'); bad += 1
            for w in g:
                if '__' in w or not w.strip():
                    print(f'  !! кривой пропуск {so}: {w!r}'); bad += 1
        elif t == 'exact_input':
            for it in p['items']:
                if not it.get('accept'):
                    print(f'  !! нет accept {so}'); bad += 1
        elif t == 'order':
            if ' '.join(p['words']) != p['sentence']:
                print(f"  !! порядок не сходится {so}"); bad += 1
        elif t == 'truefalse':
            if not p.get('statements'):
                print(f'  !! нет утверждений {so}'); bad += 1
        elif t == 'hotspot':
            for pt in p.get('points', []):
                if not (0 <= pt.get('x', -1) <= 100 and 0 <= pt.get('y', -1) <= 100):
                    print(f'  !! точка вне картинки {so}'); bad += 1
            lbl = [pt.get('text') for pt in p.get('points', [])]
            if len(set(lbl)) != len(lbl):
                print(f'  !! дубль подписей hotspot {so}'); bad += 1
        elif t == 'sort':
            if len(p['groups']) < 2:
                print(f'  !! меньше двух групп {so}'); bad += 1
        elif t == 'sequence':
            if len(p.get('items', [])) < 2:
                print(f'  !! sequence с одним элементом {so}'); bad += 1
        elif t == 'speaking':
            if not p.get('html'):
                print(f'  !! пустой speaking {so}'); bad += 1
    for m in re.findall(r'@@MEDIA@@' + MDIR + r'/([A-Za-z0-9_]+)\.webp', s):
        if m not in MEDIA:
            print(f'  !! нет файла {MDIR}/{m}.webp'); bad += 1
    for m in re.findall(r'@@MEDIA@@shared/([A-Za-z0-9_]+)\.webp', s):
        if m not in SHARED:
            print(f'  !! нет файла shared/{m}.webp'); bad += 1
    types = collections.Counter(t for t, _, _ in blocks)
    print(f'  блоков {len(blocks)}: ' + ', '.join(f'{k}×{v}' for k, v in types.most_common()))

print('=' * 70)
print('ОШИБОК:', bad)
