import os, re
import numpy as np
from PIL import Image
from scipy.ndimage import label, binary_dilation, binary_erosion, binary_fill_holes

def fname(w):
    return re.sub(r"[^A-Za-z0-9]+", "_", w).strip("_") + '.png'

def min_rgb_of(im):
    arr = np.array(im.convert('RGB')).astype(np.int32)
    return np.minimum(np.minimum(arr[...,0], arr[...,1]), arr[...,2]).astype(np.uint8)

# порог фона: 240 — как было; строже (250 + бесцветность) — для листов, где
# белое внутри рисунка (облака, экраны, бумага) уходило вместе с фоном
BG_MIN, BG_GREY = 240, 255
# KEEP_SOFT: маска рисунка — всё непрозрачное, что связано с тёмными частями,
# а не только пиксели темнее 235 (+grow). Иначе белая середина облака пропадает.
KEEP_SOFT = False

def widen_keep(alpha, m):
    if not KEEP_SOFT:
        return m
    lab, n = label(alpha > 0)
    ids = np.unique(lab[m & (alpha > 0)]); ids = ids[ids > 0]
    return m | np.isin(lab, ids)

def make_soft_transparent(im):
    arr = np.array(im.convert('RGBA'))
    r,g,b = arr[...,0].astype(np.int32), arr[...,1].astype(np.int32), arr[...,2].astype(np.int32)
    min_rgb = np.minimum(np.minimum(r,g),b).astype(np.uint8)
    bg = (min_rgb >= BG_MIN) & ((np.maximum(np.maximum(r,g),b) - min_rgb) <= BG_GREY)
    labeled,_ = label(bg)
    edge=set(); h,w = labeled.shape
    for y in [0,h-1]: edge.update(np.unique(labeled[y,:]).tolist())
    for x in [0,w-1]: edge.update(np.unique(labeled[:,x]).tolist())
    edge.discard(0)
    true_bg = np.isin(labeled, list(edge))
    obj = ~true_bg
    dil = binary_dilation(obj, iterations=2)
    alpha = np.zeros_like(min_rgb, dtype=np.float32)
    alpha[obj]=255
    tr = dil & ~obj
    alpha[tr] = np.clip((255-min_rgb[tr].astype(np.float32))*8,0,255)
    out = arr.copy(); out[...,3]=alpha.astype(np.uint8)
    return Image.fromarray(out,'RGBA')

def to_square(obj, size=300, pad=6):
    canvas = Image.new('RGBA',(size,size),(0,0,0,0))
    inner = size-pad*2
    ow,oh = obj.size
    if max(ow,oh)>inner:
        s = inner/max(ow,oh)
        obj = obj.resize((max(1,int(ow*s)),max(1,int(oh*s))), Image.LANCZOS)
    w,h = obj.size
    canvas.paste(obj, ((size-w)//2,(size-h)//2), obj)
    return canvas

def clusters_of(sheet, y0, y1, min_area=600, thr=235, gap=40):
    im = Image.open(sheet).convert('RGB'); mr = min_rgb_of(im)
    reg = mr[y0:y1,:] < thr
    lab,n = label(reg)
    comps=[]
    for i in range(1,n+1):
        ys,xs = np.where(lab==i)
        if len(ys)<min_area: continue
        comps.append((xs.min(), xs.max()+1, ys.min(), ys.max()+1, i))
    comps.sort()
    cl=[]
    for c in comps:
        if cl and c[0] <= cl[-1]['x1']+gap:
            k=cl[-1]; k['x0']=min(k['x0'],c[0]); k['x1']=max(k['x1'],c[1])
            k['y0']=min(k['y0'],c[2]); k['y1']=max(k['y1'],c[3]); k['ids'].append(c[4])
        else:
            cl.append(dict(x0=c[0],x1=c[1],y0=c[2],y1=c[3],ids=[c[4]]))
    return im, mr, reg, lab, cl

def row(sheet, y0, y1, words, outdir, min_area=600, pad=6, grow=3, thr=235, gap=40):
    im,mr,reg,lab,cl = clusters_of(sheet,y0,y1,min_area,thr,gap)
    if len(cl)!=len(words):
        print(f'  MISMATCH {outdir} y{y0}-{y1}: {len(cl)} vs {len(words)}')
        return False
    os.makedirs(outdir,exist_ok=True)
    for k,w in zip(cl,words):
        keep=np.zeros_like(reg,dtype=bool)
        for i in k['ids']: keep |= (lab==i)
        keep=binary_dilation(keep,iterations=grow)
        ax0=max(0,k['x0']-pad); ay0=max(0,k['y0']-pad)
        ax1=min(reg.shape[1],k['x1']+pad); ay1=min(reg.shape[0],k['y1']+pad)
        crop=im.crop((ax0,y0+ay0,ax1,y0+ay1))
        rgba=np.array(make_soft_transparent(crop))
        m=widen_keep(rgba[...,3], keep[ay0:ay1,ax0:ax1])
        rgba[...,3]=(rgba[...,3]*m).astype(np.uint8)
        to_square(Image.fromarray(rgba,'RGBA')).save(os.path.join(outdir,fname(w)))
    return True

def row_x(sheet, y0, y1, words, outdir, cuts, min_area=150, pad=6, grow=3, thr=235, fill=(), fill_thr=250, fill_close=5):
    """Как row(), но клетки заданы границами по x (cuts — len(words)-1 значений).
    Для рядов, где соседние рисунки касаются и кластеры по зазору слипаются.
    Граница — число или ступенька (y_листа, x_выше, x_ниже), если рисунки заходят
    друг за друга по горизонтали на разной высоте.
    fill — слова, у которых светлая середина (доска, лист) обведена контуром:
    ей не даём стать прозрачной, заливаем дырки маски."""
    im = Image.open(sheet).convert('RGB'); mr = min_rgb_of(im)
    reg = mr[y0:y1, :] < thr
    H, W = reg.shape
    def bound(c):
        a = np.full(H, c if isinstance(c, (int, np.integer)) else 0)
        if not isinstance(c, (int, np.integer)):
            ys, xt, xb_ = c; k = max(0, min(H, ys - y0)); a[:k] = xt; a[k:] = xb_
        return a
    bs = [np.zeros(H, int)] + [bound(c) for c in cuts] + [np.full(H, W)]
    cols = np.arange(W)[None, :]
    os.makedirs(outdir, exist_ok=True)
    for w, la, lb in zip(words, bs, bs[1:]):
        inside = (cols >= la[:, None]) & (cols < lb[:, None])
        xa, xb = int(la.min()), int(lb.max())
        part = reg & inside
        lab, n = label(part)
        keep = np.zeros_like(reg)
        for i in range(1, n + 1):
            if (lab == i).sum() >= min_area: keep |= (lab == i)
        ys, xx = np.where(keep)
        ax0 = max(xa, xx.min() - pad); ax1 = min(xb, xx.max() + 1 + pad)
        ay0 = max(0, ys.min() - pad); ay1 = min(reg.shape[0], ys.max() + 1 + pad)
        keep = binary_dilation(keep, iterations=grow) & inside
        crop = im.crop((ax0, y0 + ay0, ax1, y0 + ay1))
        rgba = np.array(make_soft_transparent(crop))
        if w in fill:
            light = (mr[y0 + ay0:y0 + ay1, ax0:ax1] < fill_thr) & inside[ay0:ay1, ax0:ax1]
            solid = binary_erosion(binary_fill_holes(binary_dilation(light, iterations=fill_close)), iterations=fill_close)
        else:
            solid = np.zeros((ay1 - ay0, ax1 - ax0), bool)
        m = widen_keep(rgba[..., 3], keep[ay0:ay1, ax0:ax1] & inside[ay0:ay1, ax0:ax1]) & inside[ay0:ay1, ax0:ax1]
        rgba[..., 3] = (rgba[..., 3] * m).astype(np.uint8)
        rgba[..., 3] = np.maximum(rgba[..., 3], solid.astype(np.uint8) * 255)
        to_square(Image.fromarray(rgba, 'RGBA')).save(os.path.join(outdir, fname(w)))
    return True
