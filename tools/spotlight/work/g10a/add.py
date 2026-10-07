# usage: python3 add.py <rows-file>  ; rows-file lines: module|section|term|pos|translation|note  (pipe-separated)
import csv,sys,os
out='/home/user/classroom/tools/spotlight/tsv/grade_10_a.tsv'
new=not os.path.exists(out)
rows=[]
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip(): continue
    p=line.split('|')
    assert len(p)==6,(line,len(p))
    p=[x.strip().replace('’',"'").replace('‘',"'") for x in p]
    rows.append(['10']+p)
with open(out,'a',encoding='utf-8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    if new: w.writerow(['grade','module','section','term','pos','translation','note'])
    w.writerows(rows)
print(len(rows))
