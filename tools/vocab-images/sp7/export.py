"""Spotlight 7 → wowspeak-platform/public/trainer/media/spotlight7/<файл>.webp (512×512) и SQL с адресами.
python3 export.py 1 2 ... 10 — какие листы выгружать; цифры (out/digits) идут всегда.
Пишет sql_urls_<первый>-<последний>.sql: адрес ставится словам без картинки и тем, у кого
прежний вариант этой картинки (300×300 под тем же именем → новый файл …_v2.webp)."""
import os, sys
from PIL import Image
sys.path.insert(0, '..')
from lib import fname
from sheets import S, DIGITS
# с 14.10.2026 тренажёр живёт на app.wowteach.ru, картинки — в wowspeak-platform/public/trainer/media
DST = '/home/user/wowspeak-platform/public/trainer/media/spotlight7'
URL = 'https://app.wowteach.ru/trainer/media/spotlight7/'
SKIP = {'beast', 'tan', 'guard', 'guide', 'shake hands', 'crayon', 'rich', 'wrist', 'MP3 player', 'digital music player', 'unemployment', 'funk', 'polar region', 'direct debit'}  # подписи, не прошедшие проверку: не выгружать
SKIP -= set(filter(None, os.environ.get('ALLOW', '').split('|')))  # ALLOW='keep out|…' — выгрузить перерисованные (после перерисовки)
# омонимы: подпись из столбца caption плана → перевод слова (у омонимов в плане подпись своя)
import csv
from sheets import PLAN
HOMO = {r['caption']: r['translation'] for r in csv.DictReader(open(PLAN), delimiter='\t') if r['caption']}
os.makedirs(DST, exist_ok=True)
sheets = list(map(int, sys.argv[1:]))


def put(src, stem, q):
    """Кладёт 512×512; если под этим именем уже выложен 300×300 — рядом …_v2. → (новый адрес, прежний)"""
    old = f'{DST}/{stem}.webp'
    name = stem
    # FORCE_V2=1 — перерисованная картинка: новое имя, чтобы браузеры не показывали прежнюю
    if os.path.exists(old) and (Image.open(old).size != (512, 512) or os.environ.get('FORCE_V2')):
        name = stem + '_v2'
    dst = f'{DST}/{name}.webp'
    # уже выгружено из этой же нарезки — не пережимаем заново (method=6 медленный)
    if not (os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src) and Image.open(dst).size == (512, 512)):
        im = Image.open(src)
        assert im.size == (512, 512), src
        im.save(dst, 'WEBP', quality=q, method=6)
    return URL + name + '.webp', URL + stem + '.webp'

rows = []  # (термин, колода-признак, url)
for n in sheets:
    for term, cap, _ in S[n - 1][2]:
        if cap in SKIP: continue
        if cap in HOMO and HOMO[cap] is None:
            sys.exit(f'омоним {cap}: впишите перевод в HOMO')
        rows.append((term, HOMO.get(cap) or '', *put(f'out512/{n}/{fname(cap)}', fname(cap)[:-4], 82)))
for term, cap, _ in ([] if os.environ.get('NO_DIGITS') else DIGITS):  # NO_DIGITS=1 — без порядковых чисел
    rows.append((term, '', *put(f'out512/digits/{fname(cap)}', fname(cap)[:-4], 90)))
q = lambda s: "'" + s.replace("'", "''") + "'"
vals = ',\n'.join(f'({q(t)},{q(k)},{q(u)},{q(o)})' for t, k, u, o in rows)
out = f'sql_urls_{sheets[0]}-{sheets[-1]}.sql' if len(sys.argv) > 1 else 'sql_urls.sql'
open(out, 'w').write(f"""UPDATE words w SET image_url = v.u
FROM (VALUES
{vals}) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND (f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 7' AND deleted_at IS NULL)
       OR f.parent_folder_id IN (SELECT id FROM deck_folders WHERE parent_folder_id =
           (SELECT id FROM deck_folders WHERE title = 'Spotlight 7' AND deleted_at IS NULL)))  -- подпапки «Другие слова»
  AND (v.k = '' OR w.translation = v.k)
RETURNING w.id;""")
print(len(rows), out)
