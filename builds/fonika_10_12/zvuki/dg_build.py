import subprocess, base64, os, sys, json
P=sys.argv[1]; os.chdir(P)
# (подпись, пример, фонема GB, фонема US)
S=[("sh","ship","ʃː","ʃː"),("ch","chip","tʃ","tʃ"),("th","thin — глухой","θː","θː"),("th","this — звонкий","ðː","ðː"),
("qu","quiz","kw","kw"),("ng","ring","ŋː","ŋː"),
("ee / ea","tree, sea","iː","iː"),("oo","moon — длинный","uː","uː"),("oo","book — краткий","ʊ","ʊ"),("ar","car","ɑː","ɑɹ"),
("ai / ay","rain, day","eɪ","eɪ"),("oa / ow","boat, snow","əʊ","oʊ"),("igh / y","night, fly","aɪ","aɪ"),
("or","fork","ɔː","ɔɹ"),("ur / er / ir","burn, her, girl","ɜː","ɝ"),("ow / ou","cow, out","aʊ","aʊ"),("oi / oy","coin, boy","ɔɪ","ɔɪ")]
V=[("en_GB-alba","Британский, женский (alba)","GB"),("en_US-amy","Американский, женский (amy)","US"),
   ("en_GB-alan","Британский, мужской (alan)","GB"),("en_US-joe","Американский, мужской (joe)","US")]
SP=[(1.0,"обычно"),(1.6,"медленнее")]
subprocess.run("ffmpeg -loglevel error -y -f lavfi -i anullsrc=r=22050:cl=mono -t 0.7 dg/sil.wav",shell=True,check=True)
data={}
for i,(lab,ex,gb,us) in enumerate(S):
  for v,_,acc in V:
    ph=gb if acc=="GB" else us
    for ls,_ in SP:
      w=f"dg/{i}_{v}_{ls}.wav"
      subprocess.run(["./venv/bin/piper","-m",f"{v}-medium.onnx","--length-scale",str(ls),"-f",w],input=f"[[ {ph} ]]".encode(),check=True,capture_output=True)
      r=f"dg/r.wav"; subprocess.run(f"ffmpeg -loglevel error -y -i {w} -ar 22050 -ac 1 {r}",shell=True,check=True)
      m=f"dg/{i}_{v}_{ls}.mp3"
      subprocess.run(f"ffmpeg -loglevel error -y -i {r} -i dg/sil.wav -i {r} -i dg/sil.wav -i {r} -filter_complex concat=n=5:v=0:a=1 -codec:a libmp3lame -q:a 5 {m}",shell=True,check=True)
      data[(i,v,ls)]=base64.b64encode(open(m,'rb').read()).decode()
rows=[]
for i,(lab,ex,gb,us) in enumerate(S):
  cells=[]
  for v,_,_ in V:
    btn=" ".join(f'<button onclick="pl(this)" data-a="data:audio/mpeg;base64,{data[(i,v,ls)]}">▶ {sl}</button>' for ls,sl in SP)
    cells.append(f"<td>{btn}</td>")
  rows.append(f'<tr><th><b>{lab}</b><span>{ex}</span></th>{"".join(cells)}</tr>')
head="".join(f"<th>{n}</th>" for _,n,_ in V)
html=f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Звуки сочетаний — пробы</title><style>
:root{{--bg:#fff;--fg:#1d1d1f;--mut:#6b6b70;--line:#e3e3e8;--acc:#2f6fe4;--btn:#eef3fd}}
@media (prefers-color-scheme:dark){{:root{{--bg:#16171a;--fg:#ececf0;--mut:#9a9aa2;--line:#2c2d33;--acc:#7aa6ff;--btn:#22283a}}}}
body{{margin:0;padding:16px;background:var(--bg);color:var(--fg);font:15px/1.4 system-ui,sans-serif}}
h1{{font-size:20px;margin:0 0 6px}} p{{color:var(--mut);margin:0 0 14px;max-width:760px}}
.wrap{{overflow-x:auto}} table{{border-collapse:collapse;min-width:720px}}
td,th{{border-bottom:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:middle}}
thead th{{font-size:13px;color:var(--mut);font-weight:600}}
tbody th b{{font-size:20px;display:block}} tbody th span{{font-size:12px;color:var(--mut);font-weight:400}}
button{{border:1px solid var(--line);background:var(--btn);color:var(--acc);border-radius:8px;padding:6px 10px;margin:2px;cursor:pointer;font:inherit;font-size:13px}}
button.on{{background:var(--acc);color:#fff}}
</style></head><body><h1>Звуки сочетаний — выбрать голос</h1>
<p>Каждая запись — звук три раза подряд, без слова. Слово справа от сочетания — только подсказка, какой звук имеется в виду. «Медленнее» — тот же голос, звук растянут. Британский и американский варианты различаются в <b>ar</b>, <b>or</b>, <b>ur</b>, <b>oa</b>.</p>
<div class="wrap"><table><thead><tr><th>сочетание</th>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>
<script>let a=new Audio(),cur;function pl(b){{if(cur)cur.classList.remove('on');a.pause();a=new Audio(b.dataset.a);cur=b;b.classList.add('on');a.onended=()=>b.classList.remove('on');a.play()}}</script>
</body></html>'''
open("zvuki_sochetaniy.html","w").write(html); print(len(html)//1024,"KB")
