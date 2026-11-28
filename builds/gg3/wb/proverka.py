# -*- coding: utf-8 -*-
"""Проверка собранного юнита до заливки: дубли вариантов, ключи, пары, пропуски, файлы."""
import importlib.util, os, re, sys

def proverit(put_k_build):
    spec = importlib.util.spec_from_file_location('m', put_k_build)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    osh = []
    for nazv, bloki in m.UROKI:
        tipy = [t for t, _ in bloki]
        if tipy[0] != 'text' or tipy[-1] != 'text':
            osh.append(f'{nazv}: нет приветствия или прощания')
        if len(bloki) < 6:
            osh.append(f'{nazv}: меньше шести блоков ({len(bloki)})')
        for i, (tip, p) in enumerate(bloki):
            no = i + 1
            if tip == 'quiz':
                for qi, q in enumerate(p['questions']):
                    o = [x['text'] for x in q['options']]
                    if len(set(o)) != len(o):
                        osh.append(f'{nazv} б{no} в{qi+1}: дубли вариантов')
                    if any(k >= len(o) for k in q['correct']):
                        osh.append(f'{nazv} б{no} в{qi+1}: correct вне диапазона')
            if tip == 'match':
                pr = [x['right'] for x in p['pairs']]
                if len(set(pr)) != len(pr): osh.append(f'{nazv} б{no}: правые повторяются')
                if any(not x.strip() for x in pr): osh.append(f'{nazv} б{no}: пустой right')
                if len(pr) > 8: osh.append(f'{nazv} б{no}: больше восьми пар')
            if tip == 'gaps':
                n = len(re.findall(r'__[^_]+__', p['text']))
                if n == 0: osh.append(f'{nazv} б{no}: нет пропусков')
                if p.get('mode') == 'drag' and n < 2: osh.append(f'{nazv} б{no}: drag с одним пропуском')
                if p.get('mode') == 'choice' and len(p.get('choices', [])) != n:
                    osh.append(f'{nazv} б{no}: choices не по числу пропусков')
            if tip == 'order':
                for it in p['items']:
                    if ' '.join(it['words']) != it['sentence']:
                        osh.append(f'{nazv} б{no}: склейка не сходится')
            if tip == 'sequence':
                t = [x['text'] for x in p['items']]
                if len(set(t)) != len(t): osh.append(f'{nazv} б{no}: повтор реплик')
            if tip == 'flashcards':
                t = [c['text'] for c in p['cards']]
                if len(set(t)) != len(t): osh.append(f'{nazv} б{no}: дубли карточек')
            if tip == 'sort':
                vse = [x['text'] for g in p['groups'] for x in g['items']]
                if len(set(vse)) != len(vse): osh.append(f'{nazv} б{no}: один элемент в двух группах')
            for s in re.findall(r'media/([a-zA-Z0-9_/\-]+\.webp)', str(p)):
                if not os.path.exists('media/' + s): osh.append(f'{nazv} б{no}: нет файла media/{s}')
    return osh, {n: len(b) for n, b in m.UROKI}

if __name__ == '__main__':
    osh, skolko = proverit(sys.argv[1])
    print('\n'.join(osh) if osh else 'проверка чистая')
    print('блоков по урокам:', skolko)
