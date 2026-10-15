"""Spotlight 5 → wowspeak-train/media/spotlight5/<файл>.webp и SQL с адресами.
python3 export.py 1 2 ... 10 — какие листы выгружать; цифры (out/digits) идут всегда.
Пишет sql_urls_<первый>-<последний>.sql: UPDATE только там, где image_url IS NULL."""
import os, sys
from PIL import Image
sys.path.insert(0, '..')
from lib import fname
from sheets import S, DIGITS
# с 14.10.2026 тренажёр живёт на app.wowteach.ru, картинки — в wowspeak-platform/public/trainer/media
DST = '/home/user/wowspeak-platform/public/trainer/media/spotlight5'
URL = 'https://app.wowteach.ru/trainer/media/spotlight5/'
# не прошли проверку (дети, алкоголь) — ждут перерисовки
SKIP = {'culture', 'street parade', 'nightclub', 'Thanksgiving'}
# омонимы: подпись → начало названия колоды, где этот смысл
HOMO = {'great (excellent)': '2c', 'great (big)': '3a', 'mean': '5d', 'mean (signify)': '8c',
        'mean (intend)': '9a', 'top (of a tower)': '6d', 'top (of a box)': 'Across the Curriculum 6:',
        'holiday (celebration)': '8a', 'holiday (vacation)': '10a'}
os.makedirs(DST, exist_ok=True)
sheets = list(map(int, sys.argv[1:]))
rows = []  # (термин, колода-признак, url)
for n in sheets:
    for term, cap, _ in S[n - 1][2]:
        if cap in SKIP: continue
        if cap in HOMO and HOMO[cap] is None:
            sys.exit(f'омоним {cap}: впишите колоду в HOMO')
        f = fname(cap)[:-4] + '.webp'
        Image.open(f'out/{n}/{fname(cap)}').save(f'{DST}/{f}', 'WEBP', quality=82, method=6)
        rows.append((term, HOMO.get(cap) or '', URL + f))
for term, cap, _ in DIGITS:
    f = fname(cap)[:-4] + '.webp'
    Image.open(f'out/digits/{fname(cap)}').save(f'{DST}/{f}', 'WEBP', quality=90, method=6)
    rows.append((term, '', URL + f))
q = lambda s: "'" + s.replace("'", "''") + "'"
vals = ',\n'.join(f'({q(t)},{q(k)},{q(u)})' for t, k, u in rows)
out = f'sql_urls_{sheets[0]}-{sheets[-1]}.sql' if len(sys.argv) > 1 else 'sql_urls.sql'
open(out, 'w').write(f"""UPDATE words w SET image_url = v.u
FROM (VALUES
{vals}) AS v(t, k, u), word_decks d, deck_folders f
WHERE w.term = v.t AND w.image_url IS NULL AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 5' AND deleted_at IS NULL)
  AND (v.k = '' OR d.title LIKE v.k || ' %')
RETURNING w.id;""")
print(len(rows), out)
