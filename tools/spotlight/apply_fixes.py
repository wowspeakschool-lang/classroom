"""work/fix_N.tsv → правки в tsv/grade_N.tsv; журнал в work/fixes_applied.tsv."""
import csv, glob
F = {'term': 3, 'pos': 4, 'translation': 5, 'note': 6}
log = [['grade', 'module', 'section', 'term', 'field', 'old', 'new', 'reason', 'status']]
for g in range(2, 12):
    f = f'tsv/grade_{g}.tsv'; rows = list(csv.reader(open(f), delimiter='\t'))
    try: fixes = list(csv.DictReader(open(f'work/fix_{g}.tsv'), delimiter='\t'))
    except FileNotFoundError: continue
    ok = miss = 0
    for x in fixes:
        i = F[x['field']]; hit = False
        for r in rows[1:]:
            if r[1] == x['module'] and r[2] == x['section'] and r[3] in (x['term'], x['new'] if x['field'] == 'term' else x['term']) and r[i] == x['old']:
                r[i] = x['new']; hit = True
        ok += hit; miss += not hit
        log.append([g, x['module'], x['section'], x['term'], x['field'], x['old'], x['new'], x['reason'], 'ok' if hit else 'не найдено'])
    csv.writer(open(f, 'w'), delimiter='\t', lineterminator='\n').writerows(rows)
    print(g, 'applied', ok, 'missed', miss)
csv.writer(open('work/fixes_applied.tsv', 'w'), delimiter='\t', lineterminator='\n').writerows(log)
