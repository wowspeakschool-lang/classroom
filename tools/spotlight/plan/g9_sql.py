"""SQL заливки Spotlight 9 из plan/g9_plan.tsv → sql/g9_*.sql (с подпапками «Другие слова»).
Картинка для reuse берётся в базе: то же слово с картинкой, у перевода общий корень (как g8_match);
для строк из SAME (смысл совпал при другом переводе) — любая картинка того же слова. Самый свежий id."""
import csv, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
sys.path.insert(0, 'plan')
AUTHOR = 'd0912d22-5cf7-4273-8113-33b42ad2cdf9'
rows = list(csv.DictReader(open('plan/g9_plan.tsv'), delimiter='\t'))
import importlib.util
spec = importlib.util.spec_from_file_location('p', 'plan/g9_plan.py')
SAME = None
src = open('plan/g9_plan.py').read()
SAME = eval(src[src.index('SAME = {') + 7: src.index('}', src.index('SAME = {')) + 1])
q = lambda s: "'" + s.replace("'", "''") + "'"
mods = list(dict.fromkeys(r['folder'] for r in rows))
subs = list(dict.fromkeys(r['folder'] for r in rows if r['subfolder']))
decks = list(dict.fromkeys((r['folder'], r['subfolder'], r['deck']) for r in rows))
G = "(select id from deck_folders where title='Spotlight 9' and deleted_at is null)"
s1 = f"""with r as (select id from deck_folders where title='Spotlight' and parent_folder_id is null and deleted_at is null),
g as (insert into deck_folders (title, description, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
  select 'Spotlight 9', '9 класс', (select id from r), '📗', '{AUTHOR}', true, -1
  where not exists (select 1 from deck_folders where title='Spotlight 9' and deleted_at is null) returning id)
insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select v.t, g.id, '📘', '{AUTHOR}', true, v.o from g, (values {', '.join(f"({q(m)}, {len(mods) - i})" for i, m in enumerate(mods))}) v(t, o)
returning id, title;"""
s2 = f"""insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select 'Другие слова', f.id, '🧺', '{AUTHOR}', true, 99 from (values {', '.join(f"({q(m)})" for m in subs)}) v(m)
join deck_folders f on f.title = v.m and f.parent_folder_id = {G} and f.deleted_at is null
where not exists (select 1 from deck_folders x where x.parent_folder_id = f.id and x.title = 'Другие слова' and x.deleted_at is null)
returning id;"""
FOLD = f"""join deck_folders m on m.title = v.f and m.parent_folder_id = {G} and m.deleted_at is null
left join deck_folders s on s.parent_folder_id = m.id and s.title = 'Другие слова' and s.deleted_at is null"""
s3 = f"""insert into word_decks (title, level, cover_emoji, author_id, is_school_library, folder_id, sort_order)
select v.d, 'A1', '📚', '{AUTHOR}', true, case when v.sub then s.id else m.id end, v.o
from (values {', '.join(f"({q(f)}, {'true' if sf else 'false'}, {q(d)}, {10 * i})" for i, (f, sf, d) in enumerate(decks, 1))}) v(f, sub, d, o)
{FOLD}
returning id;"""
ROOTS = lambda x: f"""(select coalesce(array_agg(distinct left(w,4)),'{{}}') from regexp_split_to_table(replace(lower(coalesce({x},'')),'ё','е'), '[^а-я]+') w
  where length(w)>=3 and w not in ('что','кто','кого','чем','чего','либо','нибудь','себя','свой','быть','очень','такой','этот','который'))"""
order, wv = {}, []
for r in rows:
    k = (r['folder'], r['deck']); order[k] = order.get(k, 0) + 1
    if r['image'].startswith('reuse'):
        i = int(r['image'].split(':')[1]); kind = 's' if i in SAME else 'r'
    else: kind = ''
    wv.append(f"({q(r['folder'])}, {'true' if r['subfolder'] else 'false'}, {q(r['deck'])}, {q(r['term'])}, {q(r['translation'])}, {order[k]}, {q(kind)})")
def s4(part): return f"""insert into words (deck_id, term, translation, "order", image_url)
select d.id, v.t, v.tr, v.o, case when v.k = '' then null else (
  select x.image_url from words x join word_decks xd on xd.id = x.deck_id and xd.deleted_at is null
  where x.image_url is not null and lower(trim(x.term)) = lower(trim(v.t))
    and (v.k = 's' or {ROOTS('x.translation')} && {ROOTS('v.tr')})
  order by x.id desc limit 1) end
from (values {', '.join(part)}) v(f, sub, dk, t, tr, o, k)
{FOLD}
join word_decks d on d.folder_id = case when v.sub then s.id else m.id end and d.title = v.dk and d.deleted_at is null
where not exists (select 1 from words y where y.deck_id = d.id and y.term = v.t and y."order" = v.o)
returning id;"""
s5 = f"""update word_decks d set word_count = (select count(*) from words w where w.deck_id = d.id)
where d.folder_id in (select id from deck_folders where parent_folder_id = {G}
   or parent_folder_id in (select id from deck_folders where parent_folder_id = {G})) returning id;"""
os.makedirs('sql', exist_ok=True)
for n, s in (('1', s1), ('2', s2), ('3', s3), ('5', s5)): open(f'sql/g9_{n}.sql', 'w').write(s)
for i in range(0, len(wv), 170): open(f'sql/g9_4_{i // 170 + 1}.sql', 'w').write(s4(wv[i:i + 170]))
print(len(mods), len(subs), len(decks), len(rows), (len(wv) + 169) // 170, 'кусков слов')
