import subprocess, json, os
W=["snow globe","nutcracker","lantern","polar bear","rocking horse","teddy bear","penguin","owl","fox","toy train","drum","ice skates","gingerbread house","carousel","hot chocolate","golden unicorn","Santa's sleigh","ice palace"]
V=["en_GB-alba-medium","en_GB-jenny_dioco-medium","en_GB-cori-high","en_GB-alan-medium","en_US-amy-medium","en_US-lessac-high","en_US-hfc_female-medium"]
os.makedirs('out2',exist_ok=True); meta=[]; n=300
for w in W:
  t=w if w.endswith('!') else w+'.'
  for v in V:
    n+=1; f=f'out2/{n:03d}.mp3'
    if not os.path.exists(f):
      subprocess.run(['./venv/bin/piper','-m',v+'.onnx','--length-scale','1.15','-f','t.wav'],input=t.encode(),check=True,capture_output=True)
      subprocess.run(['ffmpeg','-y','-loglevel','error','-i','t.wav','-af','silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,adelay=80','-codec:a','libmp3lame','-q:a','5',f],check=True)
    meta.append({'n':n,'w':w,'v':v})
json.dump(meta,open('meta2.json','w'))
print(n)
