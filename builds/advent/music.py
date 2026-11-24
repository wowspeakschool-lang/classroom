"""Фоновая музыка адвента: Jingle Bells (Дж. Пирпонт, 1857 — общественное достояние),
своя аранжировка «музыкальная шкатулка + бубенцы + мягкий бас», без слов.
Синтез в numpy, на выходе wav → mp3 (ffmpeg)."""
import numpy as np, wave, os
SR=44100; BPM=126; Q=60/BPM
NOTE={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
def hz(n):
    name,octv=n[:-1],int(n[-1]); return 440*2**((NOTE[name]+12*(octv+1)-69)/12)
# мелодия: (нота, длительность в четвертях); 'R' — пауза
V1=[('D4',1),('B4',1),('A4',1),('G4',1),('D4',3),('D4',.5),('D4',.5),('D4',1),('B4',1),('A4',1),('G4',1),('E4',4),
    ('E4',1),('C5',1),('B4',1),('A4',1),('F#4',4),('D5',1),('D5',1),('C5',1),('A4',1),('B4',4)]
V2=[('D4',1),('B4',1),('A4',1),('G4',1),('D4',4),('D4',1),('B4',1),('A4',1),('G4',1),('E4',3),('E4',1),
    ('E4',1),('C5',1),('B4',1),('A4',1),('D5',1),('D5',1),('D5',1),('D5',1),('E5',1),('D5',1),('C5',1),('A4',1),('G4',2),('D5',2)]
CH1=[('B4',1),('B4',1),('B4',2),('B4',1),('B4',1),('B4',2),('B4',1),('D5',1),('G4',1.5),('A4',.5),('B4',4)]
CH2=[('C5',1),('C5',1),('C5',1.5),('C5',.5),('C5',1),('B4',1),('B4',1),('B4',.5),('B4',.5),('B4',1),('A4',1),('A4',1),('B4',1),('A4',2),('D5',2)]
CH4=[('C5',1),('C5',1),('C5',1),('C5',1),('C5',1),('B4',1),('B4',1),('B4',.5),('B4',.5),('D5',1),('D5',1),('C5',1),('A4',1),('G4',4)]
MEL=V1+V2+CH1+CH2+CH1+CH4
# гармония по тактам (4 четверти)
HAR=['G','G','G','C','C','D','D','G',  'G','G','G','C','C','D7','D7','G',
     'G','G','G','G','C','G','A7','D7',  'G','G','G','G','C','G','D7','G']
CHORD={'G':['G2','B3','D4','G4'],'C':['C3','E4','G4','C5'],'D':['D3','F#4','A4','D5'],'D7':['D3','F#4','C5','A4'],'A7':['A2','C#4','G4','E4']}
total=sum(d for _,d in MEL)*Q
N=int((total+3)*SR); out=np.zeros(N); L=np.zeros(N)
t=lambda n:np.arange(n)/SR
def bell(f,dur,amp):  # шкатулка/челеста: негармоничные обертоны, быстрый спад
    n=int(min(dur+1.6,3)*SR); tt=t(n)
    s=(np.sin(2*np.pi*f*tt)+.45*np.sin(2*np.pi*f*2.0*tt)*np.exp(-tt*6)+.25*np.sin(2*np.pi*f*3.01*tt)*np.exp(-tt*9)+.12*np.sin(2*np.pi*f*4.2*tt)*np.exp(-tt*14))
    env=np.exp(-tt*2.6)*np.minimum(1,tt/0.004); return amp*s*env
def pluck(f,dur,amp):
    n=int((dur+.4)*SR); tt=t(n); s=np.sin(2*np.pi*f*tt)+.3*np.sin(2*np.pi*2*f*tt); env=np.exp(-tt*3.2)*np.minimum(1,tt/0.01); return amp*s*env
def add(sig,at):
    i=int(at*SR); j=min(N,i+len(sig)); out[i:j]+=sig[:j-i]
rng=np.random.default_rng(7)
def jingle(at,amp):  # бубенцы: короткие высокие звоночки + шорох
    n=int(.18*SR); tt=t(n); s=np.zeros(n)
    for _ in range(6):
        f=rng.uniform(3800,7200); s+=np.sin(2*np.pi*f*tt+rng.uniform(0,6))*np.exp(-tt*rng.uniform(25,45))
    noise=rng.normal(0,1,n)*np.exp(-tt*40); noise=np.diff(np.concatenate([[0],noise]))
    add(amp*(s/6+.35*noise),at)
# мелодия
pos=0.0
for nt,d in MEL:
    if nt!='R': add(bell(hz(nt)*2,d*Q,.34),pos)  # на октаву выше — звонче
    pos+=d*Q
# аккомпанемент: бас на 1 и 3, аккорд-арпеджио тихо
for b,ch in enumerate(HAR):
    at=b*4*Q; notes=CHORD[ch]
    add(pluck(hz(notes[0]),1.6*Q,.32),at); add(pluck(hz(notes[0])*1.5,1.6*Q,.18),at+2*Q)
    for k,nn in enumerate(notes[1:]):
        add(bell(hz(nn),Q,.07),at+(k+0.5)*Q*1.0)
# бубенцы на каждую четверть, акцент на долях 2 и 4
nb=int(total/Q)
for k in range(nb):
    jingle(k*Q,.10 if k%2 else .06); jingle(k*Q+Q/2,.04)
# лёгкая реверберация (несколько задержек)
rev=np.zeros(N)
for dly,g in [(.031,.35),(.047,.3),(.071,.25),(.113,.2),(.163,.15),(.241,.1)]:
    d=int(dly*SR); rev[d:]+=out[:-d]*g
mix=out+.6*rev
# плавное начало и конец — для зацикливания
fade=int(.6*SR); mix[:int(.05*SR)]*=np.linspace(0,1,int(.05*SR)); mix[-fade:]*=np.linspace(1,0,fade)
mix=mix/np.abs(mix).max()*.8
D=os.path.dirname(os.path.abspath(__file__))
with wave.open(D+'/jingle.wav','wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype('<i2').tobytes())
print(round(total,1),'сек')
