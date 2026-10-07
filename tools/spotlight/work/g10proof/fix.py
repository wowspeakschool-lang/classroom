import csv
rows=list(csv.reader(open('/home/user/classroom/tools/spotlight/tsv/grade_10.tsv'),delimiter='\t'))
idx={'term':3,'pos':4,'translation':5,'note':6}
F=[ (25,'translation','развлечение, времяпрепровождение','орфография: времяпрепровождение'),
 (160,'translation','приятный','pleasant = приятный, не «довольный»'),
 (199,'term','advice/advise','advice — только сущ.; глагол advise (pos n/v)'),
 (629,'translation','собирать деньги','raise money = собирать (средства), не зарабатывать'),
 (762,'translation','сдавать экзамен','sit an exam = сдавать экзамен'),
 (1189,'translation','полог леса, верхний ярус крон','canopy (ярус леса) = полог, не поросль'),
 (1222,'translation','ошейник','collar у тигра = ошейник (с радиомаяком)'),
 (1420,'translation','позабавленный, развеселившийся','amused = позабавленный, не изумленный'),
 (1472,'translation','беспокойный, встревоженный','uneasy (чувство) = беспокойный'),
 (1585,'translation','пищевая добавка','additive = добавка, не приправа'),
 (1643,'translation','жирный, маслянистый','oily = жирный, маслянистый'),
 (1725,'translation','тупая, ноющая боль/страдание, боль','лишний пробел после /'),
 (1775,'pos','adv','totally — наречие'),
 (1895,'pos','adj','main — прилагательное'),
 (2171,'translation','экономка','housekeeper = экономка, не домохозяйка'),
 (2377,'pos','adj','перевод — прилагательное'),
 (2391,'translation','строительные леса','scaffolding = леса, не зависание'),
 (2460,'pos','adj','перевод «беспроводной» — прилагательное'),
 (2492,'translation','поток, течение','flow (n) = поток, «течь» — глагол'),
]
out=csv.writer(open('/home/user/classroom/tools/spotlight/work/fix_10.tsv','w',newline=''),delimiter='\t',lineterminator='\n')
out.writerow('grade module section term field old new reason'.split())
for ln,f,new,why in F:
    r=rows[ln-1]; old=r[idx[f]]; assert old!=new
    out.writerow([r[0],r[1],r[2],r[3],f,old,new,why]); print(ln,r[3],f,old,'->',new)
