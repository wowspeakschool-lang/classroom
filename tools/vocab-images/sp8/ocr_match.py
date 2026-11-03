"""Опознание листов по подписям: python3 ocr_match.py <папка с png> → ocr_match.tsv
Подписи читает tesseract (полосы под рисунками), каждый лист Spotlight 8 получает долю найденных подписей."""
import os, sys, re, subprocess, json
from difflib import SequenceMatcher
from sheets import S
from PIL import Image
D = sys.argv[1]
norm = lambda s: re.sub(r'[^a-z0-9 ]', '', s.lower().replace('’', "'").replace("'", '')).split()
caps = [[' '.join(norm(c)) for _, c, _ in ws] for _, _, ws in S]
cache_f = os.path.join(D, '_ocr.json')
cache = {}
out = []
for f in sorted(os.listdir(D)):
    if not f.endswith('.png'): continue
    if f not in cache:
        t = os.path.join(D, '..', 'ocrtxt', f[:-4] + '.txt')
        if os.path.exists(t): cache[f] = open(t).read()
        else:
            im = Image.open(os.path.join(D, f)).convert('L')
            im = im.resize((im.width * 2, im.height * 2))
            tmp = '/tmp/claude-0/ocr_tmp.png'; im.save(tmp)
            cache[f] = subprocess.run(['tesseract', tmp, '-', '--psm', '11'], capture_output=True, text=True).stdout
    words = norm(cache[f]); text = ' '.join(words)
    def hit(c):
        if c in text: return 1
        n = len(c.split()); best = 0
        for k in range(len(words) - n + 1):
            best = max(best, SequenceMatcher(None, c, ' '.join(words[k:k + n])).ratio())
        return best >= 0.8
    sc = sorted(((sum(hit(c) for c in cs) / len(cs), i + 1) for i, cs in enumerate(caps)), reverse=True)[:2]
    out.append((f[:-4], sc[0][1], round(sc[0][0], 2), sc[1][1], round(sc[1][0], 2)))
open('ocr_match.tsv', 'w').write('\n'.join('\t'.join(map(str, r)) for r in out) + '\n')
print(len(out), 'файлов;', sum(1 for r in out if r[2] >= 0.5), 'опознано')
