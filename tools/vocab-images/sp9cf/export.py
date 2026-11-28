"""Выкладка одобренных картинок Spotlight 9 (Cloudflare): python3 export.py term1 term2 ...  (или --file batch.json)
real/out512/<stem>.png → webp 512 в wowspeak-platform (main) и gh-pages; пишет sql_<дата>.sql:
адрес ставится словам Spotlight 9 с этим term и переводом из плана, у которых картинки ещё нет."""
import os, sys, csv, json, datetime
from PIL import Image
sys.path.insert(0, '..')
from lib import fname
here = os.path.dirname(os.path.abspath(__file__))
DST = ['/home/user/wowspeak-platform/public/trainer/media/spotlight9', '/home/user/gp/trainer/media/spotlight9']
URL = 'https://app.wowteach.ru/trainer/media/spotlight9/'
a = sys.argv[1:]
terms = list(json.load(open(a[1]))) if a[:1] == ['--file'] else a
for d in DST: os.makedirs(d, exist_ok=True)
plan = list(csv.DictReader(open(f'{here}/../../spotlight/plan/g9_plan.tsv'), delimiter='\t'))
rows = []
for t in terms:
    stem = fname(t)[:-4]
    im = Image.open(f'{here}/real/out512/{stem}.png').convert('RGB'); assert im.size == (512, 512)
    for d in DST: im.save(f'{d}/{stem}.webp', 'WEBP', quality=82, method=4)
    trs = sorted({r['translation'] for r in plan if r['term'] == t and r['image'] == 'new'})
    assert trs, t
    rows += [(t, tr, URL + stem + '.webp') for tr in trs]
q = lambda s: "'" + s.replace("'", "''") + "'"
vals = ',\n'.join(f'({q(t)},{q(tr)},{q(u)})' for t, tr, u in rows)
out = f'{here}/sql_{datetime.date.today():%Y%m%d}_{len(os.listdir(here))}.sql'
open(out, 'w').write(f"""with recursive t as (select id from deck_folders where title='Spotlight 9' and deleted_at is null
 union all select f.id from deck_folders f join t on f.parent_folder_id=t.id where f.deleted_at is null),
u as (update words w set image_url=v.u from (values
{vals}) v(term,tr,u), word_decks d
where w.deck_id=d.id and d.deleted_at is null and d.folder_id in (select id from t) and w.term=v.term and w.translation=v.tr and w.image_url is null returning 1)
select count(*) from u;
""")
print(out, len(rows))
