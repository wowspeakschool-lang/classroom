"""Prepare (пробелы): out512 → wowspeak-platform/public/trainer/media/prepareN/<файл>.webp + gh-pages.
Имя занято другим файлом — берём <имя>_g.webp, чужие картинки не перезаписываем."""
import os, sys, json
from PIL import Image
sys.path.insert(0, '..')
from lib import fname
from words import S, SKIP
LV = {}
for i, ws in enumerate(S[:7], 1):
    for t, c, d, deck in ws:
        LV[c] = 7 if i == 7 else 6 if i == 6 or c in ('difference','generosity','happiness','importance','organisation','patience','qualification') else \
                5 if i in (4,) and c != 'speak a language' or c == 'perform' else 4 if c in ('cost (noun)','cost (verb)','pay (noun)','pay (verb)','charge (noun)','charge (verb)','speak a language') else \
                3 if c in ('thousand','billion') else 2
rows = []
for i, ws in enumerate(S[:7], 1):
    for t, c, d, deck in ws:
        if c in SKIP and not os.environ.get('ALLOW'): continue
        lv = LV[c]; stem = fname(c)[:-4]
        for root in ('/home/user/wowspeak-platform/public/trainer/media', '/home/user/gp/trainer/media'):
            os.makedirs(f'{root}/prepare{lv}', exist_ok=True)
        name = stem
        if os.path.exists(f'/home/user/wowspeak-platform/public/trainer/media/prepare{lv}/{name}.webp') and not os.path.exists(f'.done/{lv}_{name}'):
            name = stem + '_g'
        im = Image.open(f'out512/{i}/{fname(c)}'); assert im.size == (512, 512)
        for root in ('/home/user/wowspeak-platform/public/trainer/media', '/home/user/gp/trainer/media'):
            im.save(f'{root}/prepare{lv}/{name}.webp', 'WEBP', quality=82, method=6)
        rows.append((t, deck, lv, f'https://app.wowteach.ru/trainer/media/prepare{lv}/{name}.webp'))
json.dump(rows, open('urls.json', 'w'), ensure_ascii=False, indent=0)
from collections import Counter
print(len(rows), Counter(r[2] for r in rows), [r[3] for r in rows if r[3].endswith('_g.webp')])
