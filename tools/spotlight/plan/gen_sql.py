"""SQL заливки класса N из plan/gN_plan.tsv: python3 plan/gen_sql.py 5 → sql/gN_1..4.sql (+ куски слов по 170).
Папки и колоды — в порядке плана. Готовая картинка копируется в базе по words.id."""
import csv, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
N = int(sys.argv[1]); AUTHOR = 'd0912d22-5cf7-4273-8113-33b42ad2cdf9'
rows = list(csv.DictReader(open(f'plan/g{N}_plan.tsv'), delimiter='\t'))
q = lambda s: "'" + s.replace("'", "''") + "'"
folders, decks = [], []
for r in rows:
    if r['folder'] not in folders: folders.append(r['folder'])
    if (r['folder'], r['deck']) not in decks: decks.append((r['folder'], r['deck']))
G = f"(select id from deck_folders where title='Spotlight {N}' and deleted_at is null)"
s1 = f"""with r as (select id from deck_folders where title='Spotlight' and parent_folder_id is null and deleted_at is null),
g as (insert into deck_folders (title, description, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
  select 'Spotlight {N}', '{N} класс', (select id from r), '📗', '{AUTHOR}', true, {N}
  where not exists (select 1 from deck_folders where title='Spotlight {N}' and deleted_at is null) returning id)
insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select v.t, g.id, v.e, '{AUTHOR}', true, v.o from g, (values {', '.join(f"({q(f)}, {q('📎' if f == 'Другие разделы' else '📘')}, {i})" for i, f in enumerate(folders, 1))}) v(t, e, o)
returning id, title;"""
s2 = f"""insert into word_decks (title, level, cover_emoji, author_id, is_school_library, folder_id, sort_order)
select v.d, 'A1', '📚', '{AUTHOR}', true, f.id, v.o from (values {', '.join(f"({q(f)}, {q(d)}, {i})" for i, (f, d) in enumerate(decks, 1))}) v(f, d, o)
join deck_folders f on f.title = v.f and f.parent_folder_id = {G} and f.deleted_at is null
returning id;"""
order, wv = {}, []
for r in rows:
    k = (r['folder'], r['deck']); order[k] = order.get(k, 0) + 1
    src = r['image'].split(':')[1] if r['image'].startswith('reuse') else 'null'
    wv.append(f"({q(r['folder'])}, {q(r['deck'])}, {q(r['term'])}, {q(r['translation'])}, {order[k]}, {src})")
def s3(part): return f"""insert into words (deck_id, term, translation, "order", image_url)
select d.id, v.t, v.tr, v.o, (select image_url from words x where x.id = v.src)
from (values {', '.join(part)}) v(f, dk, t, tr, o, src)
join deck_folders f on f.title = v.f and f.parent_folder_id = {G} and f.deleted_at is null
join word_decks d on d.folder_id = f.id and d.title = v.dk and d.deleted_at is null
returning id;"""
s4 = f"""update word_decks d set word_count = (select count(*) from words w where w.deck_id = d.id)
where d.folder_id in (select id from deck_folders where parent_folder_id = {G}) returning id;"""
os.makedirs('sql', exist_ok=True)
open(f'sql/g{N}_1.sql', 'w').write(s1); open(f'sql/g{N}_2.sql', 'w').write(s2); open(f'sql/g{N}_4.sql', 'w').write(s4)
for i in range(0, len(wv), 170): open(f'sql/g{N}_3_{i // 170 + 1}.sql', 'w').write(s3(wv[i:i + 170]))
print(len(folders), len(decks), len(rows), (len(wv) + 169) // 170, 'кусков слов')
