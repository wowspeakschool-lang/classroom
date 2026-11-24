"""Короткие звуки адвента (numpy, как music.py): открытие окошка, монетки, подарок, редкая игрушка.
И слова 18 новых игрушек голосом en_GB-alba (Piper), как выбрала Анна для остальных слов."""
import numpy as np, wave, os, subprocess
SR=44100; D=os.path.dirname(os.path.abspath(__file__)); A=D+'/audio/'
def t(sec): return np.arange(int(sec*SR))/SR
def bell(f,sec,amp=1,dec=4):
    x=t(sec); return amp*(np.sin(2*np.pi*f*x)+.4*np.sin(2*np.pi*2*f*x)*np.exp(-x*8)+.2*np.sin(2*np.pi*3.01*f*x)*np.exp(-x*12))*np.exp(-x*dec)*np.minimum(1,x/0.003)
def mix(parts,total):
    out=np.zeros(int(total*SR))
    for at,s in parts:
        i=int(at*SR); j=min(len(out),i+len(s)); out[i:j]+=s[:j-i]
    return out
def save(name,s):
    s=s/np.abs(s).max()*.7
    with wave.open(A+name+'.wav','wb') as w:
        w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((s*32767).astype('<i2').tobytes())
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',A+name+'.wav','-codec:a','libmp3lame','-q:a','5',A+name+'.mp3'],check=True); os.remove(A+name+'.wav')
rng=np.random.default_rng(3)
def sparkle(n,start,span,amp):
    return [(start+rng.uniform(0,span),bell(rng.uniform(2200,4200),.4,amp,9)) for _ in range(n)]
# открытие окошка: восходящее арпеджио + искры
notes=[784,988,1175,1568]
save('s_open',mix([(i*.07,bell(f,.9,.8)) for i,f in enumerate(notes)]+sparkle(10,.15,.5,.25),1.4))
# монетки: два коротких звона
save('s_coin',mix([(0,bell(1976,.35,1,10)),(.09,bell(2637,.5,1,8))],.7))
# подарок: маленькая фанфара
fan=[(0,523),(.12,659),(.24,784),(.42,1047)]
save('s_gift',mix([(a,bell(f,1.2,1,3)) for a,f in fan]+[(.42,bell(1319,1.2,.6,3)),(.42,bell(1568,1.2,.5,3))]+sparkle(16,.4,.9,.3),2.0))
# редкая игрушка: «волшебная» глиссада вверх + аккорд
gl=[(i*.035,bell(600*2**(i/8),.5,.5,7)) for i in range(16)]
save('s_rare',mix(gl+[(.6,bell(1047,1.6,1,2.5)),(.6,bell(1319,1.6,.8,2.5)),(.6,bell(1568,1.6,.7,2.5)),(.6,bell(2093,1.6,.5,2.5))]+sparkle(20,.6,1.2,.3),2.6))
# слова новых игрушек
W={'snow_globe':'snow globe','nutcracker':'nutcracker','lantern':'lantern','polar_bear':'polar bear','rocking_horse':'rocking horse',
   'teddy_bear':'teddy bear','penguin':'penguin','owl':'owl','fox':'fox','toy_train':'toy train','drum':'drum','ice_skates':'ice skates',
   'gingerbread_house':'gingerbread house','carousel':'carousel','hot_chocolate':'hot chocolate','golden_unicorn':'golden unicorn',
   'santa_sleigh':"Santa's sleigh",'ice_palace':'ice palace'}
TT=D+'/../tts/'
for k,w in W.items():
    subprocess.run([TT+'venv/bin/piper','-m',TT+'en_GB-alba-medium.onnx','--length-scale','1.15','-f',A+'tmp.wav'],input=(w+'.').encode(),check=True,capture_output=True)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',A+'tmp.wav','-af','silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,adelay=80','-codec:a','libmp3lame','-q:a','5',A+'w_'+k+'.mp3'],check=True)
os.remove(A+'tmp.wav'); print('ok')
