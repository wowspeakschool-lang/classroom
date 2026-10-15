import sys, json, os, subprocess
sys.path.insert(0, sys.argv[1]+'/tools'); from comics_data import *
from PIL import Image
S=sys.argv[1]; R='/home/user/classroom/media/wow-dragon-2/comics'; os.makedirs(R,exist_ok=True)
P=json.load(open(S+'/comics/panels.json')); ORD=[1,3,2,4,5]
A=S+'/comics/aud'; OUT=S+'/comics/merged'; os.makedirs(OUT,exist_ok=True)
for n,src in SRC.items():
    im=Image.open(S+'/comics/img/'+src).convert('RGB')
    full=im.copy(); full.thumbnail((900,900),Image.LANCZOS); full.save(f'{R}/hw{n}.webp',quality=82)
    boxes=P[src.split('.')[0]]
    for i,b in enumerate(boxes):
        k=ORD[i]; c=im.crop(tuple(b)); c.thumbnail((600,600),Image.LANCZOS); c.save(f'{R}/hw{n}_k{k}.webp',quality=82)
    # склейка реплик кадра
    for k,codes in enumerate(FRAMES[n],1):
        ins=[]; flt=''
        files=[f"{A}/{AUD[n].format(c).replace('/','__').replace(' ','_')}" for c in codes]
        for f in files: assert os.path.exists(f), f
        args=['ffmpeg','-loglevel','error','-y']
        for f in files: args+=['-i',f]
        parts=''.join(f'[{i}:a]aresample=44100,aformat=channel_layouts=mono,apad=pad_dur=0.5[a{i}];' for i in range(len(files)))
        cat=''.join(f'[a{i}]' for i in range(len(files)))+f'concat=n={len(files)}:v=0:a=1[o]'
        args+=['-filter_complex',parts+cat,'-map','[o]','-c:a','libmp3lame','-b:a','96k',f'{OUT}/hw{n}_k{k}.mp3']
        subprocess.run(args,check=True)
for h in ['dragon','unicorn','princess','granny','bunny','martian']:
    im=Image.open(f'{S}/comics/heroes/{h}.png').convert('RGB')
    if im.size[1]<260: im=im.resize((im.size[0]*260//im.size[1],260),Image.LANCZOS)
    im.thumbnail((360,360),Image.LANCZOS); im.save(f'{R}/hero_{h}.webp',quality=82)
print('done')
