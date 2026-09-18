from pypdf import PdfReader
import sys, os, io
from PIL import Image

# после любой из этих надписей в выгрузке идёт служебная часть: палитра типов
# блоков и галерея фоновых картинок 900×506 — содержимого урока там уже нет
STOP = ('Выберите новое задание для урока',
        'Выберите фоновое изображение',
        'Доступные фоны')

def dump(pdf, out_dir, tag, min_px=40000):
    os.makedirs(out_dir, exist_ok=True)
    r = PdfReader(pdf); n = 0
    for pi, page in enumerate(r.pages, 1):
        txt = page.extract_text() or ''
        if any(m in txt for m in STOP):
            break                      # дальше палитра блоков и галерея фонов
        for k, im in enumerate(page.images):
            try:
                img = Image.open(io.BytesIO(im.data))
            except Exception:
                continue
            if img.width * img.height < min_px:
                continue
            p = f'{out_dir}/{tag}_p{pi:02d}_{k}.png'
            img.convert('RGB').save(p); n += 1
    return n

if __name__ == '__main__':
    print(sys.argv[3], dump(sys.argv[1], sys.argv[2], sys.argv[3]))
