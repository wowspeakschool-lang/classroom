"""Сопоставление листов от Анны с номерами листов по OCR подписей: python3 match.py raw/ → match.tsv"""
import sys, os, re, subprocess
from sheets import S
def toks(s): return set(re.findall(r"[a-z]{3,}", s.lower()))
caps = [[c for _, c, _ in it] for _, _, it in S]
d = sys.argv[1]; out = []
for f in sorted(os.listdir(d)):
    txt = subprocess.run(['tesseract', os.path.join(d, f), '-', '--psm', '11'], capture_output=True, text=True).stdout
    tt = toks(txt)
    sc = []
    for i, cs in enumerate(caps, 1):
        hit = sum(1 for c in cs if toks(c) and toks(c) <= tt)
        sc.append((hit, i))
    sc.sort(reverse=True)
    out.append(f"{f}\t{sc[0][1]}\t{sc[0][0]}\t{sc[1][1]}:{sc[1][0]}")
    print(out[-1], flush=True)
open('match.tsv', 'w').write('\n'.join(out) + '\n')
