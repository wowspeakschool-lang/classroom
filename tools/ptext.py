from pypdf import PdfReader
import re, sys
def text(f):
    r = PdfReader(f); out=[]
    for i,p in enumerate(r.pages,1):
        t = p.extract_text() or ''
        t = re.sub(r'\n?\d{2}\.\d{2}\.\d{4}, \d{2}:\d{2} ShkolaApp.*?\d+/\d+', '', t, flags=re.S)
        out.append((i, t.strip()))
    return out
def show(f, stop_at_palette=True):
    print('='*72); print(f[9:]); print('='*72)
    for i,t in text(f):
        if stop_at_palette and any(m in t for m in ('Выберите новое задание для урока', 'Выберите фоновое изображение')):
            head = re.split('Выберите новое задание для урока|Выберите фоновое изображение', t)[0].strip()
            if head: print(f'--- стр. {i} ---'); print(head)
            print(f'[стр. {i}+ — палитра типов блоков и галерея фонов, пропущено]')
            break
        print(f'--- стр. {i} ---'); print(t)
if __name__ == '__main__':
    for f in sys.argv[1:]: show(f)
