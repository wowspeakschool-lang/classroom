"""Выносит data:-картинки из собранного урока в media/halloween/<grp>/, музыку — в mus_out/ (для Storage)."""
import re, json, base64, hashlib, io, os, sys
from PIL import Image
REPO='/home/user/classroom'
MEDIA_URL='https://classroom.wowteach.ru/media/'
STORE_URL='https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/halloween/'
os.makedirs('mus_out',exist_ok=True)
def run(src, grp, dst):
    s=open(src).read()
    # имена по ключам ASSETS
    names={}
    for m in re.finditer(r'"([A-Za-z0-9_]+)"\s*:\s*"(data:[^"]+)"',s):
        names.setdefault(m.group(2),m.group(1))
    out=os.path.join(REPO,'media/halloween',grp);os.makedirs(out,exist_ok=True)
    cache={}
    def repl(m):
        uri=m.group(0)
        if uri in cache:return cache[uri]
        mime,b=re.match(r'data:([^;]+);base64,(.*)',uri,re.S).groups()
        raw=base64.b64decode(b);h=hashlib.sha1(raw).hexdigest()[:8]
        if mime.startswith('audio'):
            fn=f'music_{h}.mp3';open('mus_out/'+fn,'wb').write(raw);url=STORE_URL+fn
        else:
            nm=names.get(uri) or ('img_'+h)
            nm=re.sub(r'[^a-z0-9_]','_',nm.lower())
            im=Image.open(io.BytesIO(raw))
            fn=nm+'.webp';p=os.path.join(out,fn)
            if os.path.exists(p) and hashlib.sha1(open(p,'rb').read()).hexdigest()[:8]!=cache.get(('h',fn)):
                # имя занято другим содержимым — добавить хэш
                old=open(p,'rb').read()
            if not os.path.exists(p):
                if im.mode in('RGBA','LA','P'):im=im.convert('RGBA');im.save(p,'WEBP',quality=88,method=6)
                else:im.convert('RGB').save(p,'WEBP',quality=82,method=6)
                cache[('h',fn)]=h;cache[('src',fn)]=h
            elif cache.get(('src',fn)) not in (None,h):
                fn=f'{nm}_{h}.webp';p=os.path.join(out,fn)
                if not os.path.exists(p):
                    (im.convert('RGBA') if im.mode in('RGBA','LA','P') else im.convert('RGB')).save(p,'WEBP',quality=85,method=6)
            url=MEDIA_URL+f'halloween/{grp}/{fn}'
        cache[uri]=url;return url
    t=re.sub(r'data:[a-z]+/[a-z0-9+.-]+;base64,[A-Za-z0-9+/=]+',repl,s)
    # предзагрузка: раньше картинки были вшиты и показывались мгновенно; теперь грузятся
    # по сети — без предзагрузки урок «заедает» при первом показе каждой картинки (20.10.2026)
    urls=sorted(set(re.findall(r'https://classroom\.wowteach\.ru/media/[^"\'\s)]+\.webp',t)))
    pre=('<div id="hwPre" style="position:fixed;inset:0;z-index:99999;background:#1a1024;color:#ffe9c9;display:flex;flex-direction:column;'
         'align-items:center;justify-content:center;font:700 22px Arial,sans-serif;gap:14px"><div>Loading…</div>'
         '<div style="width:260px;height:10px;border-radius:6px;background:#3a2a4a;overflow:hidden"><div id="hwPreBar" style="height:100%;width:0;background:#f0a040"></div></div></div>'
         '<script>(function(){var U='+json.dumps(urls)+',n=0,done=false,K=window.__hwImgs=[];'
         'function fin(){if(done)return;done=true;var e=document.getElementById("hwPre");if(e)e.remove();}'
         'function one(){n++;var b=document.getElementById("hwPreBar");if(b)b.style.width=Math.round(100*n/U.length)+"%";if(n>=U.length)fin();}'
         'U.forEach(function(u){var i=new Image();i.onload=function(){(i.decode?i.decode():Promise.resolve()).then(one,one)};i.onerror=one;i.src=u;K.push(i);});'
         'if(!U.length)fin();setTimeout(fin,20000);})();</script>')
    t=re.sub(r'(<body[^>]*>)',lambda m:m.group(1)+pre,t,count=1)
    # картинки для canvas (сертификат, значок, фото комнаты) — с CORS, иначе «Save» не сработает вне своего домена
    t=t.replace('new Image()',"Object.assign(new Image(),{crossOrigin:'anonymous'})")
    # слова по клику — записанным голосом Piper (тем же, что в домашках), а не голосом браузера:
    # он на каждом устройстве свой (решение Анны от 21.10.2026). Нет записи — молчим.
    SAY='function say(t){try{const u=new SpeechSynthesisUtterance(t);u.lang="en-GB";u.rate=.85;speechSynthesis.cancel();speechSynthesis.speak(u);}catch(e){}}'
    # 23.10.2026: озвучку слов в уроках 10–12 и 13+ убрали совсем (решение Анны) — say() молчит
    if SAY in t and os.environ.get('HW_VOICE')!='1':
        t=t.replace(SAY,'function say(t){}')
    if SAY in t:
        V=json.load(open(os.path.join(REPO,'builds/halloween/voice.json')))
        # слов, которых нет в домашках, — синтез тем же Piper en_US-amy-medium здесь (builds/halloween/voice_gen.sh),
        # вшиты в урок: в платформе под них ничего не заводим (решение Анны от 21.10.2026)
        VD=os.path.join(os.path.dirname(os.path.abspath(__file__)),'piper/out')
        for k in ['golden pumpkin','zombie','pirate','superhero','bonfires','costumes','ghosts']:
            if k in t.lower() and k not in V:
                V[k]='data:audio/mpeg;base64,'+base64.b64encode(open(os.path.join(VD,'hw_voice_'+k.replace(' ','_')+'.mp3'),'rb').read()).decode()
        t=t.replace(SAY,'const VOICE='+json.dumps(V)+',VA={};let sayA=null;'
            'Object.keys(VOICE).forEach(k=>{try{const a=new Audio();a.preload="auto";a.src=VOICE[k];VA[k]=a;}catch(e){}});'
            'function say(t){const k=String(t).toLowerCase().trim().replace(/^(a|an|the) /,"");const a=VA[k];if(!a)return;'
            'try{if(sayA&&sayA!==a)sayA.pause();a.currentTime=0;sayA=a;a.play().catch(()=>{});}catch(e){}}')
    assert 'speechSynthesis' not in t and 'const VOICE=' not in t, src
    # план урока можно скачать: Word и PDF лежат рядом, в lessons/halloween/plans/ (решение Анны от 21.10.2026)
    m=re.search(r'const PLAN_HTML=("(?:[^"\\]|\\.)*");',t)
    if m:
        h=json.loads(m.group(1)); base='https://classroom.wowteach.ru/lessons/halloween/plans/halloween_'+os.path.basename(dst)[:-5]
        B='display:inline-block;margin:0 8px 0 0;padding:8px 16px;border-radius:10px;background:#e8631a;color:#fff;font-weight:700;text-decoration:none'
        dl=('<p class="dl" style="margin:0 0 14px"><a href="'+base+'.docx" download style="'+B+'">⬇ Скачать план (Word)</a>'
            '<a href="'+base+'.pdf" download style="'+B+';background:#7b4bd6">⬇ Скачать план (PDF)</a></p>')
        if 'class="dl"' not in h: h=re.sub(r'(</h1>)',lambda x:x.group(1)+dl,h,count=1)
        t=t[:m.start(1)]+json.dumps(h,ensure_ascii=False).replace('</','<\\/')+t[m.end(1):]
    os.makedirs(os.path.dirname(dst),exist_ok=True);open(dst,'w').write(t)
    print(src,'->',dst,len(t)//1024,'KB')
if __name__=='__main__':
    L=os.path.join(REPO,'lessons/halloween')
    for src,grp,name in [('halloween_lesson_4-6.html','4-6','4-6.html'),
        ('halloween_lesson_7-9_beginners.html','7-9','7-9_beginners.html'),('halloween_lesson_7-9_advanced.html','7-9','7-9_advanced.html'),
        ('halloween_lesson_10-12_beginners.html','10-12','10-12_beginners.html'),('halloween_lesson_10-12_advanced.html','10-12','10-12_advanced.html'),
        ('halloween_lesson_13plus_beginners.html','13','13plus_beginners.html'),('halloween_lesson_13plus_advanced.html','13','13plus_advanced.html')]:
        run(src,grp,os.path.join(L,name))
