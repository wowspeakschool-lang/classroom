"""Spotlight 8: сверка смысла для переиспользования картинок. plan/g8_db_images.json — выгрузка тренажёра
(lower(term), перевод, id) для слов 8 класса с картинкой (19.10.2026). Совпадение — общий корень в переводах
(первые 4 буквы слова от 3 букв). Берём самый свежий id (новые картинки 512×512). Пишет plan/g8_reuse_auto.tsv."""
import csv, json, os, re, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
STOP = {'что', 'кто', 'кого', 'чем', 'чего', 'либо', 'нибудь', 'себя', 'свой', 'быть', 'очень', 'такой', 'этот', 'который'}
def roots(t):
    ws = re.findall(r'[а-яё]+', t.lower().replace('ё', 'е'))
    return {w[:4] for w in ws if len(w) >= 3 and w not in STOP}
db = collections.defaultdict(list)
for term, tr, i in json.load(open('plan/g8_db_images.json')):
    db[term].append((i, tr))
def match(term, tr):
    c = db.get(term.lower().strip())
    if not c: return None, None
    r = roots(tr)
    ok = [(i, t) for i, t in c if roots(t) & r]
    if ok: return 'reuse', max(ok)
    return 'mismatch', max(c)
if __name__ == '__main__':
    rows = list(csv.DictReader(open('tsv/grade_8.tsv'), delimiter='\t'))
    w = csv.writer(open('plan/g8_reuse_auto.tsv', 'w'), delimiter='\t', lineterminator='\n')
    w.writerow(['section', 'term', 'translation', 'kind', 'id', 'db_translation'])
    cnt = collections.Counter()
    for r in rows:
        k, best = match(r['term'], r['translation'])
        cnt[k] += 1
        if k: w.writerow([r['section'], r['term'], r['translation'], k, best[0], best[1]])
    print(cnt)
