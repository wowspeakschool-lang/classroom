"""Какие страницы pdf — Word List: распознаём только шапку страницы."""
import pymupdf, subprocess, glob, os, json
res = {}
for f in sorted(glob.glob('pdf/*.pdf')):
    d = pymupdf.open(f); hits = []
    for i, p in enumerate(d):
        r = p.rect
        p.get_pixmap(dpi=150, clip=pymupdf.Rect(0, 0, r.width, r.height * 0.12)).save('/tmp/h.png')
        t = subprocess.run(['tesseract', '/tmp/h.png', '-', '-l', 'eng', '--psm', '6'],
                           capture_output=True, text=True).stdout.lower()
        if 'word' in t and 'list' in t:
            hits.append(i)
    res[os.path.basename(f)] = hits
    print(f, len(d), hits, flush=True)
json.dump(res, open('wl_pages.json', 'w'), ensure_ascii=False, indent=0)
