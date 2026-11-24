"""Фон леса: три варианта «волшебно-новогоднего» звука, по ~45 с, зацикливаются.
A — волшебная пыльца: мягкий «хор»-пэд + россыпь колокольчиков + тихий ветер.
B — шкатулка в лесу: «O Tannenbaum» (народная мелодия, общественное достояние) медленно, челестой, с эхом и ветром.
C — сани вдалеке: ветер, проезжающие бубенцы, редкие искорки."""
import numpy as np, wave, subprocess, os
SR=44100; rng=np.random.default_rng(11)
NOTE={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
def hz(n): return 440*2**((NOTE[n[:-1]]+12*(int(n[-1])+1)-69)/12)
T=lambda n:np.arange(n)/SR
def lowpass(x,a):  # простой однополюсный фильтр
    y=np.empty_like(x); s=0.0
    for i in range(len(x)): s+=a*(x[i]-s); y[i]=s
    return y
def wind(D,amp):
    n=int(D*SR); w=rng.normal(0,1,n)
    w=lowpass(w,.02); w=lowpass(w,.05)
    m=.55+.45*np.sin(2*np.pi*T(n)/9.0+1)*np.sin(2*np.pi*T(n)/4.3)
    return amp*w/np.abs(w).max()*m
def bell(f,amp,dec=2.2):
    n=int(3.5*SR); tt=T(n)
    s=np.sin(2*np.pi*f*tt)+.4*np.sin(2*np.pi*f*2.76*tt)*np.exp(-tt*5)+.2*np.sin(2*np.pi*f*5.4*tt)*np.exp(-tt*9)
    return amp*s*np.exp(-tt*dec)*np.minimum(1,tt/.003)
def pad(f,D,amp):  # мягкий хор: несколько расстроенных синусов, медленная атака
    n=int(D*SR); tt=T(n); s=np.zeros(n)
    for dt in (-.6,0,.7): s+=np.sin(2*np.pi*(f+dt)*tt)+.25*np.sin(2*np.pi*2*(f+dt)*tt)
    env=np.minimum(1,tt/1.5)*np.minimum(1,(D-tt)/1.5)
    return amp*s/3*env
def jingles(n_at,amp):
    n=int(.2*SR); tt=T(n); s=np.zeros(n)
    for _ in range(5): s+=np.sin(2*np.pi*rng.uniform(4000,7500)*tt+rng.uniform(0,6))*np.exp(-tt*rng.uniform(22,40))
    return amp*s/5
def put(out,sig,at):
    i=int(at*SR)
    if i>=len(out): return
    j=min(len(out),i+len(sig)); out[i:j]+=sig[:j-i]
def reverb(x,wet=.6):
    r=np.zeros_like(x)
    for d,g in [(.037,.4),(.053,.35),(.079,.3),(.121,.25),(.173,.2),(.251,.16),(.367,.12),(.53,.08)]:
        k=int(d*SR); r[k:]+=x[:-k]*g
    return x+wet*r
def finish(x,name,D):
    n=int(D*SR); x=x[:n].copy()
    f=int(2.5*SR); x[:f]*=np.linspace(0,1,f); x[-f:]*=np.linspace(1,0,f)
    x=x/np.abs(x).max()*.8
    os.makedirs('audio',exist_ok=True); w=f'audio/{name}.wav'
    with wave.open(w,'wb') as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((x*32767).astype(np.int16).tobytes())
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',w,'-codec:a','libmp3lame','-q:a','5',f'audio/{name}.mp3']); os.remove(w)

D=46
# --- A: волшебная пыльца
out=np.zeros(int((D+4)*SR))
chords=[['G3','B3','D4'],['E3','G3','B3'],['C3','E3','G3'],['D3','F#3','A3']]
for k in range(int(D/8)+1):
    for nn in chords[k%4]: put(out,pad(hz(nn),9,.10),k*8)
PENT=['G5','A5','B5','D6','E6','G6','A6','B6']
t=0.5
while t<D:
    put(out,bell(hz(PENT[rng.integers(len(PENT))]),rng.uniform(.06,.14),dec=rng.uniform(1.5,3)),t)
    t+=rng.choice([.25,.35,.5,.8,1.4],p=[.25,.25,.2,.2,.1])
out=reverb(out,.7); out[:int(D*SR)]+=wind(D,.05)
finish(out,'les_A_pylca',D)

# --- B: шкатулка в лесу (O Tannenbaum, медленно)
Q=60/66
MEL=[('D4',1),('G4',.75),('G4',.25),('G4',1.5),('A4',.5),('B4',.75),('B4',.25),('B4',1.5),('B4',.5),
     ('A4',.5),('B4',.5),('C5',1),('F#4',1),('A4',1),('G4',2),('R',1),
     ('D5',.5),('D5',.5),('B4',.5),('E5',1.5),('D5',.5),('D5',.5),('C5',.5),('C5',1.5),
     ('C5',.5),('C5',.5),('A4',.5),('D5',1.5),('C5',.5),('C5',.5),('B4',.5),('B4',1.5),('R',1)]
HAR={0:'G',4:'G',8:'D',12:'G',16:'G',20:'C',24:'D',28:'G'}
CH={'G':['G2','D3','B3'],'C':['C3','G3','E4'],'D':['D3','A3','F#4']}
out=np.zeros(int((D+4)*SR)); pos=1.0; L=sum(d for _,d in MEL)*Q
while pos<D:
    p=pos
    for nt,d in MEL:
        if nt!='R': put(out,bell(hz(nt)*2,.22,dec=1.8),p)
        p+=d*Q
    beats=int(sum(d for _,d in MEL))
    for b in range(0,beats,2):
        ch=CH[HAR.get((b//4)*4%32,'G')] if (b//4)*4 in HAR else CH['G']
        for k,nn in enumerate(ch): put(out,bell(hz(nn),.05,dec=2.5),pos+b*Q+k*.18)
    pos+=L+2*Q
out=reverb(out,.8); out[:int(D*SR)]+=wind(D,.07)
finish(out,'les_B_shkatulka',D)

# --- C: сани вдалеке
out=np.zeros(int((D+4)*SR)); out[:int(D*SR)]+=wind(D,.16)
for start in (3,24):  # два проезда саней: громче к середине, потом тише
    dur=14
    for k in range(int(dur/.21)):
        at=start+k*.21; x=k*.21/dur; a=.13*np.sin(np.pi*x)**2
        put(out,jingles(0,a),at)
for t in (10,17,33,40):
    for i,nn in enumerate(['E6','G6','B6','D7']): put(out,bell(hz(nn),.06,dec=2.5),t+i*.09)
out=reverb(out,.6)
finish(out,'les_C_sani',D)
print('ok')
