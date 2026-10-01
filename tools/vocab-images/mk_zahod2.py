"""SQL для захода 2 Prepare 3: по файлу на колоду, base64 WebP 300×300, пара (deck_id, term).
Список термов — выгрузка из базы 01.10.2026 (db_terms_zahod2.json), картинки — out/<лист>/."""
import io, os, json, base64
from PIL import Image
from lib import fname

SHEETS = {178: ['1.1'], 180: ['1.2'], 181: ['1.3', '1.4'], 182: ['2.1', '2.2'], 183: ['1.4'],
          184: ['2.3'], 185: ['3.1'], 187: ['3.2'], 188: ['3.3'], 189: ['3.4'], 190: ['4.1'],
          191: ['4.2'], 192: ['5.1'], 193: ['4.3'], 194: ['5.2'], 195: ['5.3']}
NAMES = {178: 'Outdoor adventures', 180: 'Shops', 181: 'Quantities and units', 182: 'Hobbies',
         183: 'Describing activities', 184: 'Feelings and enjoyment', 185: 'Language learning',
         187: 'Body parts', 188: 'Feelings', 189: 'Phrasal verbs', 190: 'Parts of a book',
         191: 'Cooking verbs', 192: 'Food', 193: 'Do and make collocations', 194: 'Meanings of change',
         195: 'Life events'}

def webp_uri(path, q=80):
    buf = io.BytesIO(); Image.open(path).convert('RGBA').save(buf, 'WEBP', quality=q, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode()

db = json.load(open('db_terms_zahod2.json'))
out = 'sql'; os.makedirs(out, exist_ok=True)
missing = []; total = 0
for deck in sorted(SHEETS):
    rows = []
    for d, term in [(d, t) for d, t in db if d == deck]:
        src = [os.path.join('out', s, fname(term)) for s in SHEETS[deck]]
        src = [p for p in src if os.path.exists(p)]
        if len(src) != 1: missing.append((deck, term, len(src))); continue
        t = term.replace("'", "''")
        rows.append(f"UPDATE words SET image_url = '{webp_uri(src[0])}' WHERE deck_id = {deck} AND term = '{t}';")
    body = f"-- deck {deck} {NAMES[deck]}: {len(rows)} слов\nBEGIN;\n\n" + "\n\n".join(rows) + "\n\nCOMMIT;\n"
    p = f'{out}/deck_{deck}.sql'; open(p, 'w').write(body)
    kb = os.path.getsize(p) / 1024; total += len(rows)
    print(f'deck {deck}: {len(rows):2d} слов, {kb:4.0f} KB' + ('  !!! >500KB' if kb > 500 else ''))
print('итого', total, 'MISSING/AMBIGUOUS:', missing)
