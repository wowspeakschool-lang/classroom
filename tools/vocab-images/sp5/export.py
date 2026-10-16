"""Spotlight 5 → wowspeak-platform/public/trainer/media/spotlight5/<файл>.webp (512×512) и SQL с адресами.
python3 export.py 1 2 ... 10 — какие листы выгружать; цифры (out/digits) идут всегда.
Пишет sql_urls_<первый>-<последний>.sql: адрес ставится словам без картинки и тем, у кого
прежний вариант этой картинки (300×300 под тем же именем → новый файл …_v2.webp)."""
import os, sys
from PIL import Image
sys.path.insert(0, '..')
from lib import fname
from sheets import S, DIGITS
# с 14.10.2026 тренажёр живёт на app.wowteach.ru, картинки — в wowspeak-platform/public/trainer/media
DST = '/home/user/wowspeak-platform/public/trainer/media/spotlight5'
URL = 'https://app.wowteach.ru/trainer/media/spotlight5/'
# не прошли проверку (дети, алкоголь). culture, street parade, Thanksgiving (и carnival из Spotlight 4)
# перерисованы листом замен images/177.webp → out/78, выложены 16.10.2026 вручную; nightclub ждёт
SKIP = {'culture', 'street parade', 'nightclub', 'Thanksgiving'}
# омонимы: подпись → начало названия колоды, где этот смысл
HOMO = {'great (excellent)': '2c', 'great (big)': '3a', 'mean': '5d', 'mean (signify)': '8c',
        'mean (intend)': '9a', 'top (of a tower)': '6d', 'top (of a box)': 'Across the Curriculum 6:',
        'holiday (celebration)': '8a', 'holiday (vacation)': '10a'}
os.makedirs(DST, exist_ok=True)
sheets = list(map(int, sys.argv[1:]))


def put(src, stem, q):
    """Кладёт 512×512; если под этим именем уже выложен 300×300 — рядом …_v2. → (новый адрес, прежний)"""
    old = f'{DST}/{stem}.webp'
    name = stem
    if os.path.exists(old) and Image.open(old).size != (512, 512):
        name = stem + '_v2'
    im = Image.open(src)
    assert im.size == (512, 512), src
    im.save(f'{DST}/{name}.webp', 'WEBP', quality=q, method=6)
    return URL + name + '.webp', URL + stem + '.webp'

rows = []  # (термин, колода-признак, url)
for n in sheets:
    for term, cap, _ in S[n - 1][2]:
        if cap in SKIP: continue
        if cap in HOMO and HOMO[cap] is None:
            sys.exit(f'омоним {cap}: впишите колоду в HOMO')
        rows.append((term, HOMO.get(cap) or '', *put(f'out512/{n}/{fname(cap)}', fname(cap)[:-4], 82)))
for term, cap, _ in DIGITS:
    rows.append((term, '', *put(f'out512/digits/{fname(cap)}', fname(cap)[:-4], 90)))
q = lambda s: "'" + s.replace("'", "''") + "'"
vals = ',\n'.join(f'({q(t)},{q(k)},{q(u)},{q(o)})' for t, k, u, o in rows)
out = f'sql_urls_{sheets[0]}-{sheets[-1]}.sql' if len(sys.argv) > 1 else 'sql_urls.sql'
open(out, 'w').write(f"""UPDATE words w SET image_url = v.u
FROM (VALUES
{vals}) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 5' AND deleted_at IS NULL)
  AND (v.k = '' OR d.title LIKE v.k || ' %')
RETURNING w.id;""")
print(len(rows), out)
