import csv, sys, json
# usage: python3 add.py CROP < lines ; each line: module|section|term|pos|translation|note
crop = sys.argv[1]
rows = []
for line in sys.stdin:
    line = line.rstrip('\n')
    if not line.strip(): continue
    p = [x.strip().replace('’', "'").replace('‘', "'") for x in line.split('|')]
    p += [''] * (6 - len(p))
    rows.append(['9'] + p[:6])
with open('/home/user/classroom/tools/spotlight/tsv/grade_9.tsv', 'a', encoding='utf-8', newline='') as f:
    csv.writer(f, delimiter='\t', lineterminator='\n').writerows(rows)
json.dump({'last_crop': crop, 'added': len(rows)}, open('state.json', 'w'))
print(crop, len(rows))
