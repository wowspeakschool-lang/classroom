import csv, sys, os
# usage: add.py CROPNUM < lines ; lines: module|section|term|pos|translation|note  ("|"-sep)
out='/home/user/classroom/tools/spotlight/tsv/grade_10_b.tsv'
crop=sys.argv[1]
new=not os.path.exists(out)
rows=[]
for line in sys.stdin:
    line=line.rstrip('\n')
    if not line.strip(): continue
    p=[x.strip() for x in line.split('|')]
    while len(p)<6: p.append('')
    assert len(p)==6, line
    p=[x.replace('’',"'").replace('‘',"'") for x in p]
    rows.append(['10']+p)
with open(out,'a',encoding='utf-8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    if new: w.writerow(['grade','module','section','term','pos','translation','note'])
    w.writerows(rows)
open('/home/user/classroom/tools/spotlight/work/g10b/state.txt','a').write(f'{crop} {len(rows)}\n')
print(crop,len(rows))
