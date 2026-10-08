"""Spotlight 4 → wowspeak-train/media/spotlight4/<файл>.webp и SQL с адресами.
Числа рисуем сами (цифры), остальное — нарезка out/<лист>/. Пишет url_rows.json, sql_urls.sql."""
import os, sys, json
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '..')
from lib import fname
from sheets import S
DST = '/home/user/wowspeak-train/media/spotlight4'
URL = 'https://train.wowteach.ru/media/spotlight4/'
os.makedirs(DST, exist_ok=True)
rows = []  # (термин в базе, колода-признак для омонимов, url)
for n, (_, _, items) in enumerate(S, 1):
    for term, cap, _ in items:
        src = f'out/{n}/{fname(cap)}'
        f = fname(cap)[:-4] + '.webp'
        Image.open(src).save(f'{DST}/{f}', 'WEBP', quality=82, method=6)
        rows.append((term, {'lamb (meat)': 'meal', 'lamb': 'rhyme', 'pass (give)': 'u5', 'pass (go by)': 'u11'}.get(cap, ''), URL + f))
# числа: цифры в стиле листов — тёплый цвет, тёмно-коричневый контур
DIG = {'seventy': '70', 'eighty': '80', 'ninety': '90', 'hundred': '100', 'first': '1st', 'second': '2nd', 'third': '3rd'}
COL = [(240, 120, 60), (70, 150, 220), (90, 180, 90), (230, 80, 120), (250, 180, 40), (150, 100, 210), (40, 170, 170)]
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
for (term, txt), col in zip(DIG.items(), COL):
    im = Image.new('RGBA', (300, 300), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    size = 170 if len(txt) <= 2 else 120
    fnt = ImageFont.truetype(font_path, size)
    while d.textbbox((0, 0), txt, font=fnt, stroke_width=10)[2] > 280:
        size -= 6; fnt = ImageFont.truetype(font_path, size)
    b = d.textbbox((0, 0), txt, font=fnt, stroke_width=10)
    x, y = (300 - (b[2] - b[0])) // 2 - b[0], (300 - (b[3] - b[1])) // 2 - b[1]
    d.text((x, y), txt, font=fnt, fill=col + (255,), stroke_width=10, stroke_fill=(70, 40, 20, 255))
    f = fname(term)[:-4] + '.webp'
    im.save(f'{DST}/{f}', 'WEBP', quality=90, method=6); im.save(f'out/num_{f[:-5]}.png')
    rows.append((term, '', URL + f))
json.dump(rows, open('url_rows.json', 'w'), ensure_ascii=False, indent=0)
q = lambda s: "'" + s.replace("'", "''") + "'"
vals = ',\n'.join(f'({q(t)},{q(k)},{q(u)})' for t, k, u in rows)
open('sql_urls.sql', 'w').write(f"""UPDATE words w SET image_url = v.u
FROM (VALUES
{vals}) AS v(t, k, u), word_decks d, deck_folders f
WHERE w.term = v.t AND w.image_url IS NULL AND d.id = w.deck_id AND f.id = d.folder_id
  AND f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 4' AND deleted_at IS NULL)
  AND (v.k = '' OR (v.k = 'meal' AND d.title LIKE 'Unit 6%') OR (v.k = 'rhyme' AND d.title LIKE 'Culture Corner 6%')
       OR (v.k = 'u5' AND d.title LIKE 'Unit 5:%') OR (v.k = 'u11' AND d.title LIKE 'Unit 11:%'))
RETURNING w.id;""")
print(len(rows))
