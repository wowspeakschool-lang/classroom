import csv,sys,os
# usage: add.py grade  (reads lines from stdin: line_no|field|new|reason)
g=sys.argv[1]
src=f'/home/user/classroom/tools/spotlight/tsv/grade_{g}.tsv'
rows=list(csv.reader(open(src,encoding='utf-8'),delimiter='\t'))
out=f'/home/user/classroom/tools/spotlight/work/fix_{g}.tsv'
new=not os.path.exists(out)
f=open(out,'a',encoding='utf-8',newline='')
w=csv.writer(f,delimiter='\t',lineterminator='\n')
if new: w.writerow(['grade','module','section','term','field','old','new','reason'])
idx={'term':3,'pos':4,'translation':5,'note':6}
for line in sys.stdin:
    line=line.rstrip('\n')
    if not line.strip(): continue
    n,field,newv,reason=line.split('|')
    r=rows[int(n)-1]
    r=r+['']*(7-len(r))
    old=r[idx[field]]
    if old==newv: print('SAME',n); continue
    w.writerow([r[0],r[1],r[2],r[3],field,old,newv,reason]); print('ok',n,field,repr(old),'->',repr(newv))
