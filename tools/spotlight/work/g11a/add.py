import csv,sys
# usage: add.py init | add.py <file-with-rows>  (rows: module|section|term|pos|translation|note, '|'-separated)
OUT='/home/user/classroom/tools/spotlight/tsv/grade_11_a.tsv'
if sys.argv[1]=='init':
    with open(OUT,'w',newline='',encoding='utf-8') as f:
        csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['grade','module','section','term','pos','translation','note'])
    sys.exit()
rows=[]
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip(): continue
    p=line.split('|')
    while len(p)<6: p.append('')
    p=[x.strip().replace('’',"'").replace('‘',"'") for x in p[:6]]
    rows.append(['11']+p)
with open(OUT,'a',newline='',encoding='utf-8') as f:
    csv.writer(f,delimiter='\t',lineterminator='\n').writerows(rows)
print(len(rows))
