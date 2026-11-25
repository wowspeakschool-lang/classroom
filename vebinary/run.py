# Сборка тем: python3 run.py 10plus [дата ...]  → vyhod/<группа>/<ДД.ММ Тема>/ + контактные листы в scratchpad
import sys, os, subprocess, glob, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import build_all
from wow import count_anims
from PIL import Image

grp = sys.argv[1]; dates = sys.argv[2:]
mod = importlib.import_module('specs_10plus' if grp == '10plus' else 'specs_7_9')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vyhod', grp)
CHK = os.environ.get('CHK', '/tmp/chk')
for sp in mod.S:
    if dates and sp['date'] not in dates:
        continue
    import re as _re
    name = _re.sub(r'\s+', ' ', _re.sub(r'[:?…/\\*"<>|]', '', sp.get('file_topic', sp['topic']))).strip()
    folder = os.path.join(OUT, name)   # без даты (решение Анны 25.11)
    les, selfp, L, n = build_all(sp, folder)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', folder, selfp], capture_output=True)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', CHK, les], capture_output=True)
    pdf = os.path.join(CHK, os.path.basename(les)[:-5] + '.pdf')
    pre = os.path.join(CHK, sp['date'] + grp)
    subprocess.run(['pdftoppm', '-r', '40', '-png', pdf, pre])
    subprocess.run(['pdftoppm', '-r', '40', '-png', selfp[:-5] + '.pdf', pre + 'S'])
    for tag, pat in (('L', pre + '-*.png'), ('S', pre + 'S-*.png')):
        fs = sorted(glob.glob(pat)); ims = [Image.open(f) for f in fs]; w, h = ims[0].size
        cols = 5; rows = (len(ims) + cols - 1) // cols
        sh = Image.new('RGB', (cols * (w + 4), rows * (h + 4)), 'black')
        for k, im in enumerate(ims): sh.paste(im, ((k % cols) * (w + 4), (k // cols) * (h + 4)))
        sh.save(os.path.join(CHK, f'sheet_{grp}_{sp["date"]}_{tag}.png'))
        for f in fs: os.remove(f)
    print(sp['date'], grp, 'слайдов', len(L.d.prs.slides._sldIdLst), 'анимаций', count_anims(les)[0], 'самост.', n)
