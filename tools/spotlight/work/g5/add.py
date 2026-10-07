import csv,sys
# usage: add.py module section  < lines "term|pos|translation|note"
mod,sec=sys.argv[1],sys.argv[2]
rows=[]
for line in sys.stdin:
    line=line.rstrip('\n')
    if not line.strip(): continue
    p=line.split('|')+['','','']
    term,pos,tr,note=[x.strip().replace('’',"'").replace('‘',"'") for x in p[:4]]
    rows.append(['5',mod,sec,term,pos,tr,note])
with open('/home/user/classroom/tools/spotlight/tsv/grade_5.tsv','a',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerows(rows)
print(len(rows))
