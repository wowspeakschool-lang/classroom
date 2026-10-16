import sys, json, numpy as np
from PIL import Image
def runs(mask, minlen):
    out=[];s=None
    for i,v in enumerate(list(mask)+[False]):
        if v and s is None: s=i
        if not v and s is not None:
            if i-s>=minlen: out.append((s,i))
            s=None
    return out
def panels(path):
    im=Image.open(path).convert('RGB'); a=np.asarray(im).astype(int); H,W,_=a.shape
    white=(a.min(axis=2)>235)
    # columns: full-height white gutter
    colw=white.mean(axis=0)>0.97
    cols=runs(~colw, W//10)
    res=[]
    for (x0,x1) in cols:
        roww=white[:,x0:x1].mean(axis=1)>0.97
        for (y0,y1) in runs(~roww, H//10): res.append((x0,y0,x1,y1))
    # order: left-col panels top->bottom are 1,3 ; mid col 2,4 ; right 5
    return im,res
out={}
for f in sys.argv[2:]:
    im,res=panels(f); n=f.split('/')[-1].split('.')[0]; out[n]=res
    print(n, im.size, res)
json.dump(out,open(sys.argv[1],'w'))
