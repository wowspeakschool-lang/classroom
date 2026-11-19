import re, subprocess, urllib.request, urllib.parse, pathlib, json, sys, time
src = pathlib.Path(sys.argv[1]).read_text()
out_dir = pathlib.Path(sys.argv[2]); out_dir.mkdir(exist_ok=True)
texts = {}
for m in re.finditer(r'Файл: `([^`]+\.mp3)`\n.*?```\n(.*?)\n```', src, re.S):
    texts[m.group(1)] = m.group(2).strip()
only = set(sys.argv[3:])
if only: texts = {k:v for k,v in texts.items() if k in only}
json.dump(texts, open(out_dir/'texts.json','w'), ensure_ascii=False, indent=1)
SUB = []
EXTRA = json.load(open(pathlib.Path(__file__).with_name('podmeny.json')))
SUB += [tuple(x) for x in EXTRA]
URL='https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
for s in (1,2): subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=48000:cl=mono','-t',str(s),str(out_dir/f'sil{s}.wav')],check=True)
n=0
for out,t in texts.items():
    sents=re.split(r'(?<=[.!?])\s+', t.replace('\n',' '))
    parts=[]; subs=[]
    for i,s in enumerate(sents):
        gap = 2 if (i and re.match(r'(Number\s+\w+|One|Two|Three|Four|Five|Six|Seven|Eight)\.', s)) else 1
        ss=s
        for a,b in SUB:
            if re.search(a,ss): subs.append(f'{re.search(a,ss).group(0)}→{b}'); ss=re.sub(a,b,ss)
        n+=1
        d=urllib.parse.urlencode(dict(text=ss,lang='en-US',voice='john',speed='0.9',format='mp3')).encode()
        for attempt in range(5):
            try:
                with urllib.request.urlopen(urllib.request.Request(URL,data=d), timeout=60) as r: (out_dir/f'seg{n}.mp3').write_bytes(r.read()); break
            except Exception as e:
                if attempt==4: raise
                time.sleep(3*(attempt+1))
        af='silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse'
        subprocess.run(['ffmpeg','-v','error','-y','-i',str(out_dir/f'seg{n}.mp3'),'-af',af,'-ar','48000','-ac','1',str(out_dir/f'seg{n}.wav')],check=True)
        if i: parts.append(f'sil{gap}.wav')
        parts.append(f'seg{n}.wav')
    (out_dir/'list.txt').write_text(''.join(f"file '{p}'\n" for p in parts))
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(out_dir/'list.txt'),'-c:a','libmp3lame','-b:a','128k',str(out_dir/out)],check=True)
    print(out, len(sents),'sent', subs, flush=True)
