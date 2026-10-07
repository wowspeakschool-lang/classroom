import csv, sys, json, os
D=os.path.dirname(os.path.abspath(__file__))
OUT='/home/user/classroom/tools/spotlight/tsv/grade_11_b.tsv'
ST=os.path.join(D,'state.json')
if len(sys.argv)>1 and sys.argv[1]=='init':
    with open(OUT,'w',encoding='utf-8',newline='') as f:
        csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['grade','module','section','term','pos','translation','note'])
    json.dump({'m':'','s':'','crop':''},open(ST,'w')); sys.exit()
st=json.load(open(ST))
rows=[]
crop=sys.argv[1] if len(sys.argv)>1 else ''
for line in sys.stdin.read().split('\n'):
    line=line.strip()
    if not line: continue
    if line.startswith('#M '): st['m']=line[3:].strip(); continue
    if line.startswith('#S '): st['s']=line[3:].strip(); continue
    p=[x.strip() for x in line.split('|')]
    while len(p)<4: p.append('')
    t=lambda x:x.replace('’',"'").replace('‘',"'")
    rows.append(['11',st['m'],st['s'],t(p[0]),p[1],t(p[2]),t(p[3])])
with open(OUT,'a',encoding='utf-8',newline='') as f:
    csv.writer(f,delimiter='\t',lineterminator='\n').writerows(rows)
st['crop']=crop; json.dump(st,open(ST,'w'),ensure_ascii=False)
print(len(rows),'rows; state',st)
