# Упаковка: переименование папок, СОСТАВ.txt, два архива и проверка распаковкой.
import os, shutil, zipfile, glob, sys
from pptx import Presentation
import docx
NAMES = {'03.12': '03.12 A-an', '07.12': '07.12 Is there - Are there', '10.12': '10.12 Present Simple -s -es',
         '14.12': '14.12 opposite - between', '17.12': '17.12 Have to - questions', '21.12': '21.12 Ordinal numbers and dates',
         '24.12': '24.12 Comparatives -y - the most', '28.12': '28.12 Imperative and Lets', '31.12': '31.12 Would like',
         '01.12': '01.12 Plurals', '04.12': '04.12 Prepositions of place', '08.12': '08.12 Prepositions of time',
         '11.12': '11.12 Present Simple', '15.12': '15.12 Present Continuous', '18.12': '18.12 Simple vs Continuous',
         '22.12': '22.12 Comparatives', '25.12': '25.12 Can - requests', '29.12': '29.12 Countable - Uncountable'}
CHK = sys.argv[1]
for g, label in [('7-9', '7–9'), ('10plus', '10+')]:
    for d in glob.glob(f'vyhod/{g}/*/'):
        d = d.rstrip('/'); new = os.path.join(f'vyhod/{g}', NAMES[os.path.basename(d)[:5]])
        if d != new:
            if os.path.exists(new): shutil.rmtree(new)
            os.rename(d, new)
    dirs = sorted([d for d in glob.glob(f'vyhod/{g}/*') if os.path.isdir(d)], key=lambda p: os.path.basename(p)[:2])
    lines = [f'WOW Speak — вебинары Spotlight, декабрь 2026, группа {label}', '']
    for d in dirs:
        lines.append(os.path.basename(d) + '/')
        lines += ['   ' + f for f in sorted(os.listdir(d))]
    lines += ['', f'Итого: {len(dirs)} тем × 4 файла = {4 * len(dirs)} файлов.', 'Перед эфиром прогнать каждую презентацию F5 на машине эфира.']
    open(f'vyhod/{g}/СОСТАВ.txt', 'w').write('\n'.join(lines) + '\n')
    z = f'vyhod/{g}.zip'
    if os.path.exists(z): os.remove(z)
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        for d in dirs:
            for f in sorted(os.listdir(d)): zf.write(os.path.join(d, f), os.path.join(os.path.basename(d), f))
        zf.write(f'vyhod/{g}/СОСТАВ.txt', 'СОСТАВ.txt')
    chk = os.path.join(CHK, 'unz_' + g); shutil.rmtree(chk, ignore_errors=True); zipfile.ZipFile(z).extractall(chk)
    ok = 0; tops = [p for p in os.listdir(chk) if os.path.isdir(os.path.join(chk, p))]
    for t in tops:
        fs = os.listdir(os.path.join(chk, t)); assert len(fs) == 4, (t, fs)
        for f in fs:
            p = os.path.join(chk, t, f)
            if f.endswith('.pptx'): Presentation(p)
            elif f.endswith('.docx'): docx.Document(p)
            else: assert open(p, 'rb').read(4) == b'%PDF'
            ok += 1
    print(g, 'тем', len(tops), 'файлов открывается', ok, 'МБ', round(os.path.getsize(z) / 1e6, 1))
