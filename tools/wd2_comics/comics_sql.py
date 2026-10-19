import sys, json
sys.path.insert(0, sys.argv[1]+'/tools'); from comics_data import *
M='https://classroom.wowteach.ru/media/wow-dragon-2/comics/'
ST='https://api.wowteach.ru/storage/v1/object/public/classroom-media/'
import urllib.parse
def au(n,code): return ST+urllib.parse.quote(AUD[n].format(code))
def fr(n,k): return f'{M}hw{n}_k{k}.webp'
def hero(h): return f'{M}hero_{h}.webp'
LID={11:'db5c8da0-05e0-4331-a4f6-b24a67df901c',18:'e7bbbdac-3731-4665-ada9-84ea2604fa08',26:'06c1d09a-1b63-41d4-b692-fc4b51b1e5c1',
     34:'7b4622b7-baf6-42b9-b7b8-c20882ad9fb6',42:'860ac950-c2c4-4796-84e8-e34eaede6573',50:'79d4fd15-cf8b-4894-b153-7f4cbd12f08b',
     59:'8729d632-0660-4d33-9c04-c1795b49fa96',67:'fd2d9236-b2b4-4e95-84eb-3f17bfa8f555',75:'6be7a768-5401-4f46-aa64-e14f0b817a9a'}
REPL={42:('414fde93-aa9d-480c-adc4-24d652390388',70),50:('cd5ca949-9d91-4943-80d5-3cf6d4bb5fb7',70),59:('ef871b04-f8d8-4bd4-b8a5-4c458580f18e',80),
      67:('59c2a14e-767e-47f7-b14d-d34aa59f6505',70),75:('ef7d8033-08ab-4989-b736-4eebe4b489b8',60)}
def comic(n):
    rows=''.join(f'<div style="display:flex;align-items:center;gap:10px;margin:6px 0;flex-wrap:wrap"><b style="min-width:70px">Кадр {k}</b>'
                 f'<audio controls preload="none" src="{ST}wowdragon/comics/hw{n}_k{k}.mp3" style="height:34px;max-width:260px"></audio></div>'
                 for k in range(1,6))
    html=(f'<p style="font-size:1.2em;text-align:center"><b>Комикс: {TITLE[n]} 📖</b></p>'
          f'<div style="text-align:center"><img src="{M}hw{n}.webp" style="max-width:100%;border-radius:12px"></div>'
          f'<p style="text-align:center">Посмотри комикс и послушай, что говорят герои. Нажимай по порядку: кадр 1, кадр 2, кадр 3…</p>'
          f'<div style="max-width:380px;margin:0 auto">{rows}</div>')
    return 'text',{'html':html}
def task(n,t):
    k=t[0]
    if k=='Q':
        qs=[]
        import random
        for qi,(code,h) in enumerate(t[1]):
            opts=list(t[2]); random.Random(n*100+qi+3).shuffle(opts); qs.append({'q':'Послушай. Кто это сказал?','type':'single','audio':au(n,code),
                'options':[{'image':hero(o)} for o in opts],'correct':[opts.index(h)]})
        return 'quiz',{'title':'Послушай. Кто это сказал?','questions':qs}
    if k=='S':
        return 'sequence',{'title':'Расставь картинки из комикса по порядку.','items':[{'text':'','audio':'','image':fr(n,x)} for x in t[1]]}
    if k=='M':
        return 'match',{'title':'Послушай и соедини с картинкой из комикса.','pairs':[{'left':'🔊','left_audio':au(n,c),'right':f'кадр {f}','right_image':fr(n,f)} for f,c in t[1]]}
    if k=='H':
        return 'hotspot',{'title':'Послушай и нажми на героя, который это говорит.','image':fr(n,t[1]),'mode':'find','extras':[],
            'points':[{'x':x,'y':y,'text':f'кто говорит? ({i})','audio':au(n,c)} for i,(c,x,y) in enumerate(t[2],1)]}
    if k=='N':
        return 'speaking',{'title':'Что ты видишь? 🎤','image':fr(n,t[1]),'sample':'',
            'html':'<p>Посмотри на картинку из комикса. Нажми на микрофон и назови по-английски, кого и что ты видишь.</p>'}
    if k=='R':
        c,f=t[1]
        return 'speaking',{'title':'Повтори за героем 🎤','image':fr(n,f),'sample':au(n,c),
            'html':'<p>Послушай, что говорит герой, и повтори. Нажми на микрофон и скажи так же.</p>'}
def lit(p):
    s=json.dumps(p,ensure_ascii=False).replace(';','~').replace("'",'^')
    assert '$c$' not in s
    return f"replace(replace($c${s}$c$,'~',chr(59)),'^',chr(39))::jsonb"
out=[]
for n in TASKS:
    blocks=[comic(n)]+[task(n,t) for t in TASKS[n]]
    lid=LID[n]; st=[]
    if n in REPL:
        bid,so=REPL[n]; ty,p=blocks[0]
        st.append(f"update classroom_blocks set type='{ty}', payload={lit(p)} where id='{bid}'")
        for i,(ty,p) in enumerate(blocks[1:],1):
            st.append(f"insert into classroom_blocks(lesson_id,type,payload,sort_order) values('{lid}','{ty}',{lit(p)},{so+2*i})")
    elif n==34:
        for i,(ty,p) in enumerate(blocks):
            st.append(f"insert into classroom_blocks(lesson_id,type,payload,sort_order) values('{lid}','{ty}',{lit(p)},{82+2*i})")
    else:
        st.append(f"update classroom_blocks set sort_order=sort_order+1000 where lesson_id='{lid}' and sort_order>=10")
        st.append(f"update classroom_blocks set sort_order=sort_order-1000+{len(blocks)} where lesson_id='{lid}' and sort_order>=1000")
        for i,(ty,p) in enumerate(blocks):
            st.append(f"insert into classroom_blocks(lesson_id,type,payload,sort_order) values('{lid}','{ty}',{lit(p)},{10+i})")
    open(f'{sys.argv[1]}/comics/sql_hw{n}.sql','w').write(';\n'.join(st)+';\n')
    json.dump(blocks,open(f'{sys.argv[1]}/comics/blocks_hw{n}.json','w'),ensure_ascii=False,indent=1)
    print(n, len(blocks), [b[0] for b in blocks], sum(len(s) for s in st))
