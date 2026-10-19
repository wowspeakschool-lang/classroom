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
    # картинки для canvas (сертификат, значок, фото комнаты) — с CORS, иначе «Save» не сработает вне своего домена
    t=t.replace('new Image()',"Object.assign(new Image(),{crossOrigin:'anonymous'})")
    os.makedirs(os.path.dirname(dst),exist_ok=True);open(dst,'w').write(t)
    print(src,'->',dst,len(t)//1024,'KB')
if __name__=='__main__':
    L=os.path.join(REPO,'lessons/halloween')
    for src,grp,name in [('halloween_lesson_4-6.html','4-6','4-6.html'),
        ('halloween_lesson_7-9_beginners.html','7-9','7-9_beginners.html'),('halloween_lesson_7-9_continuing.html','7-9','7-9_continuing.html'),
        ('halloween_lesson_10-12_beginners.html','10-12','10-12_beginners.html'),('halloween_lesson_10-12_continuing.html','10-12','10-12_continuing.html'),
        ('halloween_lesson_13plus_beginners.html','13','13plus_beginners.html'),('halloween_lesson_13plus_continuing.html','13','13plus_continuing.html')]:
        run(src,grp,os.path.join(L,name))
