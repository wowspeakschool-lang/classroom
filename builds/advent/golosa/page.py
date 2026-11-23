import json,base64
meta=json.load(open('meta.json'))
RU={"Christmas tree":"ёлка","ball":"шар","star":"звезда","bell":"колокольчик","garland":"гирлянда","candy cane":"леденец-тросточка","snowflake":"снежинка","gingerbread man":"пряничный человечек","bow":"бантик","fairy lights":"гирлянда-огоньки","pine cone":"шишка","stocking":"новогодний носок","present":"подарок","snowy tree":"заснеженная ёлка","tinsel":"мишура","heart":"сердечко","snowman":"снеговик","icicle":"сосулька","reindeer":"олень","sweet":"конфета","mitten":"варежка","angel":"ангел","golden tree":"золотая ёлка","cracker":"хлопушка","clock":"часы","tree topper":"верхушка ёлки","red":"красный","blue":"синий","green":"зелёный","gold":"золотой","silver":"серебряный","purple":"фиолетовый","pink":"розовый","white":"белый","yellow":"жёлтый","orange":"оранжевый","Merry Christmas!":"С Рождеством!","Happy New Year!":"С Новым годом!"}
VN={"en_GB-alba-medium":"британский, женский","en_GB-jenny_dioco-medium":"британский, женский, мягкий","en_GB-cori-high":"британский, женский, звонкий","en_GB-alan-medium":"британский, мужской","en_US-amy-medium":"американский, женский","en_US-lessac-high":"американский, женский, чёткий","en_US-hfc_female-medium":"американский, женский, тёплый"}
words=[];cur=None
for m in meta:
  if not cur or cur['w']!=m['w']:
    cur={'w':m['w'],'t':RU[m['w']],'v':[]};words.append(cur)
  cur['v'].append({'n':m['n'],'l':VN[m['v']],'a':'data:audio/mpeg;base64,'+base64.b64encode(open(f"out/{m['n']:03d}.mp3",'rb').read()).decode()})
html=open('tpl.html',encoding='utf-8').read().replace('/*DATA*/[]',json.dumps(words,ensure_ascii=False))
open('../advent/golosa.html','w',encoding='utf-8').write(html)
print(len(html)//1024,'KB')
