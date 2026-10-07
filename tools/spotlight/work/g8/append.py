import csv,sys
# usage: append.py rowsfile   (rowsfile: module|section|term|pos|translation|note per line, '|' separated)
out='/home/user/classroom/tools/spotlight/tsv/grade_8.tsv'
rows=[]
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip(): continue
    p=line.split('|')
    while len(p)<6: p.append('')
    p=[x.strip().replace('’',"'").replace('‘',"'") for x in p]
    rows.append(['8']+p[:6])
with open(out,'a',encoding='utf-8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerows(rows)
print(len(rows),'rows appended')
