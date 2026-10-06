import pymupdf, subprocess, os, glob, sys
os.makedirs('ocr', exist_ok=True); os.makedirs('png', exist_ok=True)
for f in sorted(glob.glob('pdf/*.pdf')):
    b=os.path.basename(f)[:-4].replace(' ','_')
    d=pymupdf.open(f)
    for i,p in enumerate(d):
        png=f'png/{b}_{i:02d}.png'
        if not os.path.exists(png): p.get_pixmap(dpi=300).save(png)
        out=f'ocr/{b}_{i:02d}'
        if not os.path.exists(out+'.txt'):
            subprocess.run(['tesseract',png,out,'-l','eng+rus','--psm','4'],capture_output=True)
        print(out, flush=True)
