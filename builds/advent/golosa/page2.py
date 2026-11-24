import json,base64
meta=json.load(open('meta2.json'))
RU={"snow globe":"снежный шар","nutcracker":"Щелкунчик","lantern":"фонарик","polar bear":"белый медведь","rocking horse":"лошадка-качалка","teddy bear":"плюшевый мишка","penguin":"пингвин","owl":"сова","fox":"лиса","toy train":"игрушечный поезд","drum":"барабан","ice skates":"коньки","gingerbread house":"пряничный домик","carousel":"карусель","hot chocolate":"горячий шоколад","golden unicorn":"золотой единорог","Santa's sleigh":"сани Санты","ice palace":"ледяной дворец"}
VN={"en_GB-alba-medium":"британский, женский","en_GB-jenny_dioco-medium":"британский, женский, мягкий","en_GB-cori-high":"британский, женский, звонкий","en_GB-alan-medium":"британский, мужской","en_US-amy-medium":"американский, женский","en_US-lessac-high":"американский, женский, чёткий","en_US-hfc_female-medium":"американский, женский, тёплый"}
words=[];cur=None
for m in meta:
  if not cur or cur['w']!=m['w']:
    cur={'w':m['w'],'t':RU[m['w']],'v':[]};words.append(cur)
  cur['v'].append({'n':m['n'],'l':VN[m['v']],'a':'data:audio/mpeg;base64,'+base64.b64encode(open(f"out2/{m['n']:03d}.mp3",'rb').read()).decode()})
html=open('tpl.html',encoding='utf-8').read().replace('/*DATA*/[]',json.dumps(words,ensure_ascii=False))
open('../advent/golosa2.html','w',encoding='utf-8').write(html)
print(len(html)//1024,'KB')
