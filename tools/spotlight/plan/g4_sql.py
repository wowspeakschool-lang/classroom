"""SQL заливки Spotlight 4 в тренажёр из plan/g4_plan.tsv: папки → колоды → слова.
Готовая картинка копируется в базе подзапросом из words.id, байты через нас не идут."""
import csv, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
AUTHOR = 'd0912d22-5cf7-4273-8113-33b42ad2cdf9'
rows = list(csv.DictReader(open('plan/g4_plan.tsv'), delimiter='\t'))
q = lambda s: "'" + s.replace("'", "''") + "'"
folders, decks = [], []
for r in rows:
    if r['folder'] not in folders: folders.append(r['folder'])
    if (r['folder'], r['deck']) not in decks: decks.append((r['folder'], r['deck']))
import re
TOP = ['вещи', 'внешность и характер', 'профессии', 'места', 'дела и как часто', 'спорт', 'другие слова',
       'фрукты и овощи', 'продукты и на кухне', 'упаковка и количество', 'еда', 'животные', 'путешествие']
OTH = ['Goldilocks', 'Arthur', 'Special', 'Months', 'Numbers', 'Geographical Names and Nationalities · страны',
       'Geographical Names and Nationalities · города', 'Useful']
def dkey(fd):
    f, d = fd
    if f == 'Другие разделы': return (0, [i for i, o in enumerate(OTH) if d.startswith(o)][0], 0)
    if d == 'Starter Unit': return (0, 0, 0)
    m = re.match(r'Unit (\d+)', d)
    if m: return (1, int(m.group(1)), TOP.index(d.split(' · ')[1]) if ' · ' in d else 0)
    return (2 if d.startswith('Culture') else 3, 0, 0)
decks.sort(key=lambda fd: dkey(fd))
folders.sort(key=lambda f: (f.startswith('Module') is False, f))
EMO = {'Другие разделы': '📎'}
s1 = f"""with root as (
  insert into deck_folders (title, description, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
  select 'Spotlight', 'Английский в фокусе · 2–11 класс', null, '🔦', '{AUTHOR}', true, 11
  where not exists (select 1 from deck_folders where title='Spotlight' and parent_folder_id is null and deleted_at is null)
  returning id),
r as (select id from root union all select id from deck_folders where title='Spotlight' and parent_folder_id is null and deleted_at is null),
g as (insert into deck_folders (title, description, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
  select 'Spotlight 4', '4 класс', (select id from r limit 1), '📗', '{AUTHOR}', true, 4 returning id)
insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select v.t, g.id, v.e, '{AUTHOR}', true, v.o from g, (values {', '.join(f"({q(f)}, {q(EMO.get(f, '📘'))}, {i})" for i, f in enumerate(folders, 1))}) v(t, e, o)
returning id, title;"""
G = "(select id from deck_folders where title='Spotlight 4' and deleted_at is null)"
vals = ', '.join(f"({q(f)}, {q(d)}, {i})" for i, (f, d) in enumerate(decks, 1))
s2 = f"""insert into word_decks (title, level, cover_emoji, author_id, is_school_library, folder_id, sort_order)
select v.d, 'A1', '📚', '{AUTHOR}', true, f.id, v.o from (values {vals}) v(f, d, o)
join deck_folders f on f.title = v.f and f.parent_folder_id = {G} and f.deleted_at is null
returning id;"""
order = {}
wv = []
for r in rows:
    k = (r['folder'], r['deck']); order[k] = order.get(k, 0) + 1
    wv.append(f"({q(r['folder'])}, {q(r['deck'])}, {q(r['term'])}, {q(r['translation'])}, {order[k]}, {r['image'].split(':')[1] if r['image'].startswith('reuse') else 'null'})")
s3 = f"""insert into words (deck_id, term, translation, "order", image_url)
select d.id, v.t, v.tr, v.o, (select image_url from words x where x.id = v.src)
from (values {', '.join(wv)}) v(f, dk, t, tr, o, src)
join deck_folders f on f.title = v.f and f.parent_folder_id = {G} and f.deleted_at is null
join word_decks d on d.folder_id = f.id and d.title = v.dk and d.deleted_at is null
returning id;"""
s4 = f"""update word_decks d set word_count = (select count(*) from words w where w.deck_id = d.id)
where d.folder_id in (select id from deck_folders where parent_folder_id = {G}) returning id;"""
for i, s in enumerate([s1, s2, s3, s4], 1): open(f'sql/g4_{i}.sql', 'w').write(s)
print(len(folders), len(decks), len(rows))
