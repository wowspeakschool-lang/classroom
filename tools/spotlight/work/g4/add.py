import sys,csv,os
# usage: add.py CROPNO  < lines: module|section|term|pos|translation|note
out='/home/user/classroom/tools/spotlight/tsv/grade_4.tsv'
st=os.path.join(os.path.dirname(os.path.abspath(__file__)),'state.txt')
new=not os.path.exists(out)
rows=[]
for ln in sys.stdin.read().splitlines():
    if not ln.strip(): continue
    p=ln.split('|')
    while len(p)<6: p.append('')
    p=[x.strip().replace('’',"'").replace('‘',"'") for x in p]
    rows.append(['4']+p[:6])
with open(out,'a',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    if new: w.writerow(['grade','module','section','term','pos','translation','note'])
    w.writerows(rows)
open(st,'a').write(f'{sys.argv[1]} {len(rows)}\n')
print(len(rows),'rows')
