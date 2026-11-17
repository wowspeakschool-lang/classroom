import json,glob,os,sys
D=os.path.dirname(os.path.abspath(__file__))
mods=[]
for f in sorted(glob.glob(D+"/data/m*.json")):
    m=json.load(open(f))
    merged={}
    for s in m['sections']:
        k=s['section'].strip()
        if k in merged: merged[k]['words']+=s['words']
        else: merged[k]={'section':k,'words':list(s['words'])}
    m['sections']=list(merged.values())
    for s in m['sections']:
        seen=set(); ws=[]
        for w in s['words']:
            k=(w['en'].strip().lower())
            if k in seen or not w['en'].strip(): continue
            seen.add(k); ws.append({'en':w['en'].strip(),'ru':w['ru'].strip()})
        s['words']=ws
    m['sections']=[s for s in m['sections'] if s['words']]
    mods.append({'module':m['module'],'sections':[{'section':s['section'],'words':s['words']} for s in m['sections']]})
t=open(D+"/template.html").read()
out=sys.argv[1] if len(sys.argv)>1 else D+"/index.html"
open(out,'w').write(t.replace('/*DATA*/[]',json.dumps(mods,ensure_ascii=False)))
print(out, sum(len(s['words']) for m in mods for s in m['sections']))
