import subprocess,json,os
F={'ball':('ball','red blue green gold purple silver'),'star':('star','gold silver red blue'),'bell':('bell','gold silver red'),
'candy_cane':('candy cane','red green blue'),'snowflake':('snowflake','white blue gold pink'),'bow':('bow','red blue green purple'),
'stocking':('stocking','red green blue'),'present':('present','red pink purple yellow blue green'),'tinsel':('tinsel','gold silver red green blue'),
'heart':('heart','pink red purple'),'sweet':('sweet','pink blue green purple'),'mitten':('mitten','blue red green pink'),'top_star':('tree topper','gold silver')}
os.makedirs('../advent/audio',exist_ok=True);m={}
for f,(w,cs) in F.items():
  v='en_GB-jenny_dioco-medium' if f in('bell','snowflake') else 'en_GB-alba-medium'
  for c in cs.split():
    ph=f'{c} {w}';out=f'../advent/audio/p_{c}_{f}.mp3'
    subprocess.run(['./venv/bin/piper','-m',v+'.onnx','--length-scale','1.15','-f','t.wav'],input=(ph+'.').encode(),check=True,capture_output=True)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i','t.wav','-af','silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,adelay=80','-codec:a','libmp3lame','-q:a','5',out],check=True)
    m[ph]='audio/p_'+c+'_'+f+'.mp3'
json.dump(m,open('phrases.json','w'));print(len(m))
