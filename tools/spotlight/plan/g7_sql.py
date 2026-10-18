"""SQL заливки Spotlight 7 из plan/g7_plan.tsv → sql/g7_1.sql (папки модулей), g7_1b.sql (подпапки
«Другие слова»), g7_2.sql (колоды), g7_3_N.sql (слова кусками по 150), g7_4.sql (word_count).
Отличие от gen_sql.py — подпапки. Колоды нумеруются sort_order = 10, 20, … в порядке плана
(разделы — как в учебнике); слова привязываются к колоде по этому sort_order."""
import csv, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
N, AUTHOR = 7, 'd0912d22-5cf7-4273-8113-33b42ad2cdf9'
rows = list(csv.DictReader(open(f'plan/g{N}_plan.tsv'), delimiter='\t'))
q = lambda s: "'" + s.replace("'", "''") + "'"
folders, subs, decks = [], [], []
for r in rows:
    if r['folder'] not in folders: folders.append(r['folder'])
    if r['subfolder'] and (r['folder'], r['subfolder']) not in subs: subs.append((r['folder'], r['subfolder']))
    k = (r['folder'], r['subfolder'], r['deck'])
    if k not in decks: decks.append(k)
G = f"(select id from deck_folders where title='Spotlight {N}' and deleted_at is null)"
SP = f"(select id from deck_folders where parent_folder_id = {G} and deleted_at is null)"
ALL = f"(select id from deck_folders where deleted_at is null and (parent_folder_id = {G} or parent_folder_id in {SP}))"
s1 = f"""with r as (select id from deck_folders where title='Spotlight' and parent_folder_id is null and deleted_at is null),
g as (insert into deck_folders (title, description, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
  select 'Spotlight {N}', '{N} класс', (select id from r), '📗', '{AUTHOR}', true, {N}
  where not exists (select 1 from deck_folders where title='Spotlight {N}' and deleted_at is null) returning id)
insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select v.t, g.id, '📘', '{AUTHOR}', true, v.o from g, (values {', '.join(f"({q(f)}, {i})" for i, f in enumerate(folders, 1))}) v(t, o)
returning id, title;"""
s1b = f"""insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select v.s, f.id, '🧺', '{AUTHOR}', true, 99 from (values {', '.join(f"({q(f)}, {q(s)})" for f, s in subs)}) v(f, s)
join deck_folders f on f.title = v.f and f.parent_folder_id = {G} and f.deleted_at is null
where not exists (select 1 from deck_folders x where x.parent_folder_id = f.id and x.title = v.s and x.deleted_at is null)
returning id, title;"""
# «Module N · другие слова» без подпапки — в конец модуля, остальное в порядке плана
fi = {f: i for i, f in enumerate(folders)}
decks.sort(key=lambda k: (fi[k[0]], k[1] != '' or ' · другие слова' in k[2]))
so = {k: 10 * i for i, k in enumerate(decks, 1)}
s2 = f"""with v(f, s, d, o) as (values {', '.join(f"({q(f)}, {q(s)}, {q(d)}, {so[(f, s, d)]})" for f, s, d in decks)}),
t as (select v.*, coalesce(sf.id, mf.id) fid from v
  join deck_folders mf on mf.title = v.f and mf.parent_folder_id = {G} and mf.deleted_at is null
  left join deck_folders sf on v.s <> '' and sf.parent_folder_id = mf.id and sf.title = v.s and sf.deleted_at is null),
i as (insert into word_decks (title, level, cover_emoji, author_id, is_school_library, folder_id, sort_order)
  select t.d, 'A1', '📚', '{AUTHOR}', true, t.fid, t.o from t
  where not exists (select 1 from word_decks x where x.folder_id = t.fid and x.title = t.d and x.deleted_at is null) returning id)
select count(*) from i;"""
order, wv = {}, []
for r in rows:
    k = (r['folder'], r['subfolder'], r['deck']); order[k] = order.get(k, 0) + 1
    src = r['image'].split(':')[1] if r['image'].startswith('reuse') else 'null'
    wv.append(f"({so[k]}, {q(r['term'])}, {q(r['translation'])}, {order[k]}, {src})")
def s3(part): return f"""with i as (insert into words (deck_id, term, translation, "order", image_url)
select d.id, v.t, v.tr, v.o, (select image_url from words x where x.id = v.src)
from (values {', '.join(part)}) v(s, t, tr, o, src)
join word_decks d on d.sort_order = v.s and d.deleted_at is null and d.folder_id in {ALL}
returning id) select count(*) from i;"""
s4 = f"""with u as (update word_decks d set word_count = (select count(*) from words w where w.deck_id = d.id)
where d.folder_id in {ALL} returning id) select count(*) from u;"""
os.makedirs('sql', exist_ok=True)
for name, s in [('1', s1), ('1b', s1b), ('2', s2), ('4', s4)]: open(f'sql/g{N}_{name}.sql', 'w').write(s)
n = 0
for i in range(0, len(wv), 150):
    n += 1; open(f'sql/g{N}_3_{n}.sql', 'w').write(s3(wv[i:i + 150]))
print(len(folders), 'папок', len(subs), 'подпапок', len(decks), 'колод', len(rows), 'слов', n, 'кусков')
