import csv,sys,os
# usage: fx.py "<term>" field "old" "new" "reason"   (matches row by term+field old value)
OUT='/home/user/classroom/tools/spotlight/work/fix_11.tsv'
SRC='/home/user/classroom/tools/spotlight/tsv/grade_11.tsv'
rows=list(csv.DictReader(open(SRC,encoding='utf-8'),delimiter='\t'))
new=not os.path.exists(OUT)
w=csv.writer(open(OUT,'a',encoding='utf-8',newline=''),delimiter='\t',lineterminator='\n')
if new: w.writerow(['grade','module','section','term','field','old','new','reason'])
args=sys.argv[1:]
for i in range(0,len(args),5):
    term,field,old,nw,reason=args[i:i+5]
    sec=None
    if "@" in term: term,sec=term.split("@",1)
    m=[r for r in rows if r['term']==term and r[field]==old and (sec is None or r["section"]==sec)]
    if not m: print('NO MATCH',term,field,old); continue
    for r in m:
        w.writerow([r['grade'],r['module'],r['section'],r['term'],field,old,nw,reason])
    print('ok',len(m),term,field,old,'->',nw)
