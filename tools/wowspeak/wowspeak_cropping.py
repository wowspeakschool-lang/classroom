#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WOW Speak icon sheets: generate (OpenAI), whiten, cut apart, preview.

Order of work - do not change it:
    sheet = gen_sheet(...)          # or a file you already have
    whiten(sheet)                   # GPT's background is cream (254,253,248),
                                    # on a white card it shows up as a grey square
    crop_grid_auto(sheet, names, outdir)
    preview([(outdir, names)], 'preview.png')   # montage -> WAIT for "ок"

Why crop_grid_auto and never crop_grid: the old cropper splits the sheet into
equal columns, GPT lays the drawings out unevenly, and equal columns cut objects
in half. crop_grid_auto finds the objects themselves, groups them by how close
their centres are (the ball stays with the boy, two figures in one scene do not
drive apart) and paints white over anything foreign that fell into the frame.
"""
import os, base64, json, urllib.request
from PIL import Image, ImageDraw
import numpy as np

# ---------------------------------------------------------------- generation
STYLE=("Style: bright, vivid, saturated children's cartoon illustration - playful and joyful. "
       "Use a RICH and VARIED colour palette: bright blues, greens, yellows, reds, purples and pinks "
       "together, not a single muted earth-tone scheme. High colour contrast between neighbouring shapes, "
       "cheerful sunny mood, soft rounded friendly shapes. "
       "Avoid beige, brown, ochre and washed-out desaturated colours.")
SHEET_RULES=("One sheet, up to 10 separate drawings, evenly spread out with LARGE WHITE GAPS between them. "
             "Plain white background. ABSOLUTELY NO text, no letters, no captions, no labels anywhere.")

def sheet_prompt(words,extra=''):
    """Describe abstract words with a concrete scene, and keep neighbouring
    abstractions from looking the same (chill / break / tired blur together)."""
    lst='; '.join(f'{i+1}) {w}' for i,w in enumerate(words))
    return f"{SHEET_RULES} Draw: {lst}. {STYLE} {extra}".strip()

def gen_sheet(words,out,extra='',size='1536x1024',quality='high',model='gpt-image-1',prompt=None):
    """Generate one icon sheet straight through the OpenAI API (OPENAI_API_KEY).
    background='opaque' on purpose: the cropper and the white cards expect a
    white background, transparency eats the white parts of the characters."""
    key=os.environ['OPENAI_API_KEY']
    body=json.dumps({'model':model,'prompt':prompt or sheet_prompt(words,extra),
                     'size':size,'quality':quality,'background':'opaque','n':1}).encode()
    req=urllib.request.Request('https://api.openai.com/v1/images/generations',data=body,
        headers={'Authorization':f'Bearer {key}','Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=600) as r:
        data=json.load(r)
    open(out,'wb').write(base64.b64decode(data['data'][0]['b64_json']))
    print('sheet saved',out); return out

# ------------------------------------------------------------------ whiten
def whiten(path,out=None,thr=238):
    """Cream (254,253,248) -> pure white, so no grey square shows on the cards."""
    im=Image.open(path).convert('RGB'); a=np.asarray(im).astype(np.uint8)
    m=(a.min(axis=2)>=thr); a=a.copy(); a[m]=255
    im2=Image.fromarray(a); im2.save(out or path); return out or path

# ------------------------------------------------------- object-aware crop
def _label(mask):
    """8-connected components, iterative flood fill (no scipy needed)."""
    h,w=mask.shape; lab=np.zeros((h,w),np.int32); cur=0
    nbr=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for y in range(h):
        for x in range(w):
            if not mask[y,x] or lab[y,x]: continue
            cur+=1; stack=[(y,x)]; lab[y,x]=cur
            while stack:
                cy,cx=stack.pop()
                for dy,dx in nbr:
                    ny,nx=cy+dy,cx+dx
                    if 0<=ny<h and 0<=nx<w and mask[ny,nx] and not lab[ny,nx]:
                        lab[ny,nx]=cur; stack.append((ny,nx))
    return lab,cur

def _boxes(lab,n,min_area):
    out={}
    for i in range(1,n+1):
        ys,xs=np.where(lab==i)
        if len(ys)<min_area: continue
        out[i]=(xs.min(),ys.min(),xs.max()+1,ys.max()+1)
    return out

def _merge(boxes,gap):
    """Group objects whose boxes are within `gap` of each other (a boy and his
    ball are one icon, two neighbouring drawings are not)."""
    keys=list(boxes); grp={k:k for k in keys}
    def root(k):
        while grp[k]!=k: grp[k]=grp[grp[k]]; k=grp[k]
        return k
    for i,a in enumerate(keys):
        for b in keys[i+1:]:
            ax0,ay0,ax1,ay1=boxes[a]; bx0,by0,bx1,by1=boxes[b]
            dx=max(0,max(ax0,bx0)-min(ax1,bx1)); dy=max(0,max(ay0,by0)-min(ay1,by1))
            if dx<=gap and dy<=gap:
                ra,rb=root(a),root(b)
                if ra!=rb: grp[ra]=rb
    out={}
    for k in keys: out.setdefault(root(k),[]).append(k)
    return list(out.values())

def crop_grid_auto(path,names,outdir,f=3,thr=26,min_area=90,gap=None,pad=10,row_tol=0.35,verbose=True):
    """Cut the sheet into len(names) icons, reading the objects themselves.
    names may be flat ['a','b',...] or row-major [['a','b','c'],['d','e','f']].
    Anything foreign that falls inside a crop is painted white.

    gap is how close two blobs must be to count as one drawing (a boy and his
    ball). Left as None it is tuned automatically: the widest gap that still
    yields exactly len(names) drawings, so a tight sheet does not glue
    neighbours together and an airy one does not fall apart."""
    flat=[n for row in names for n in row] if names and isinstance(names[0],(list,tuple)) else list(names)
    os.makedirs(outdir,exist_ok=True)
    im=Image.open(path).convert('RGB'); W,H=im.size
    a=np.asarray(im).astype(int)
    full=(np.abs(a-255).sum(axis=2)>thr)
    sh,sw=H//f,W//f
    small=full[:sh*f,:sw*f].reshape(sh,f,sw,f).max(axis=(1,3))
    lab,n=_label(small); boxes=_boxes(lab,n,min_area)
    if not boxes: raise RuntimeError(f'{path}: nothing found - is the sheet blank?')
    if gap is None:
        tries=[g for g in (16,14,12,10,8,6,5,4,3,2) if len(_merge(boxes,g))==len(flat)]
        gap=tries[0] if tries else 8
        if verbose: print(f'{os.path.basename(path)}: gap={gap}'+('' if tries else ' (no gap gives the expected count)'))
    clusters=_merge(boxes,gap)
    cl=[]
    for g in clusters:
        xs0=min(boxes[k][0] for k in g); ys0=min(boxes[k][1] for k in g)
        xs1=max(boxes[k][2] for k in g); ys1=max(boxes[k][3] for k in g)
        cl.append({'ids':set(g),'box':(xs0,ys0,xs1,ys1),'cy':(ys0+ys1)/2,'cx':(xs0+xs1)/2,
                   'h':ys1-ys0,'w':xs1-xs0})
    cl=[c for c in cl if c['w']>=18 and c['h']>=18]
    cl.sort(key=lambda c:c['cy'])
    rows=[[cl[0]]]
    for c in cl[1:]:
        ref=rows[-1][0]
        if abs(c['cy']-ref['cy'])<=row_tol*max(ref['h'],c['h'],1)*2: rows[-1].append(c)
        else: rows.append([c])
    ordered=[c for r in rows for c in sorted(r,key=lambda c:c['cx'])]
    if verbose: print(f'{os.path.basename(path)}: {len(ordered)} objects found, {len(flat)} names given')
    if len(ordered)!=len(flat):
        raise RuntimeError(f'{path}: found {len(ordered)} objects for {len(flat)} names '
                           f'(rows: {[len(r) for r in rows]}). Tune gap= / min_area=, '
                           f'or regenerate the sheet with bigger white gaps.')
    paths=[]
    for c,name in zip(ordered,flat):
        x0,y0,x1,y1=c['box']
        X0=max(0,x0*f-pad); Y0=max(0,y0*f-pad); X1=min(W,x1*f+pad); Y1=min(H,y1*f+pad)
        foreign=(lab>0)&(~np.isin(lab,list(c['ids'])))
        fo=foreign.copy()                                   # dilate by one block
        fo[1:,:]|=foreign[:-1,:]; fo[:-1,:]|=foreign[1:,:]
        fo[:,1:]|=foreign[:,:-1]; fo[:,:-1]|=foreign[:,1:]
        big=np.repeat(np.repeat(fo,f,axis=0),f,axis=1)
        arr=np.asarray(im).copy()
        arr[:sh*f,:sw*f][big]=255
        out=f'{outdir}/{name}.png'
        Image.fromarray(arr[Y0:Y1,X0:X1]).save(out); paths.append(out)
    if verbose: print(f'  -> {len(paths)} icons in {outdir}')
    return paths

def crop_grid(path,names,outdir,thr=26,pad=8):
    """LEGACY - equal columns. Kept only for old sheets; use crop_grid_auto."""
    def _spans(profile,min_size,min_gap=18):
        runs=[]; s=None
        for i,v in enumerate(profile):
            if v and s is None: s=i
            elif not v and s is not None: runs.append((s,i)); s=None
        if s is not None: runs.append((s,len(profile)))
        if not runs: return []
        m=[runs[0]]
        for a,b in runs[1:]:
            if a-m[-1][1]<min_gap: m[-1]=(m[-1][0],b)
            else: m.append((a,b))
        return [r for r in m if r[1]-r[0]>min_size]
    os.makedirs(outdir,exist_ok=True)
    im=Image.open(path).convert('RGB'); W,H=im.size
    arr=np.asarray(im).astype(int); mask=(np.abs(arr-255).sum(axis=2)>thr)
    for r,(y0,y1) in enumerate([(0,H//2),(H//2,H)]):
        ys=_spans(mask[y0:y1].sum(axis=1)>4,110)
        ys=sorted(ys,key=lambda t:t[1]-t[0],reverse=True)
        if not ys: continue
        ry0,ry1=ys[0]; ry0+=y0; ry1+=y0
        xs=[]
        for cov in [4,10,20,35,55,80]:
            xs=sorted(_spans(mask[ry0:ry1].sum(axis=0)>cov,110))
            if len(xs)>=3: xs=xs[:3]; break
        for c,(x0,x1) in enumerate(xs):
            im.crop((max(0,x0-pad),max(0,ry0-pad),min(W,x1+pad),min(H,ry1+pad))).save(f'{outdir}/{names[r][c]}.png')

# ----------------------------------------------------------------- preview
def preview(folders_order,out_png,tw=300,th=260):
    """folders_order = [(folder,[name,...]), ...] -> one montage PNG.
    Mandatory: send it to Anna and wait for "ок" before building the decks."""
    rows=[]
    for folder,order in folders_order:
        cols=3; g=Image.new('RGB',(cols*tw,((len(order)+2)//3)*th),'#eeeeee'); d=ImageDraw.Draw(g)
        for i,n in enumerate(order):
            p=f'{folder}/{n}.png'
            if not os.path.exists(p): continue
            im=Image.open(p).convert('RGB'); im.thumbnail((tw-16,th-38))
            x=(i%3)*tw; y=(i//3)*th; g.paste(im,(x+8,y+8)); d.text((x+8,y+th-26),n,fill='black')
        rows.append(g)
    W=max(r.width for r in rows); Hs=sum(r.height for r in rows)
    out=Image.new('RGB',(W,Hs),'white'); yy=0
    for r in rows: out.paste(r,(0,yy)); yy+=r.height
    out.save(out_png); print('preview',out_png); return out_png
