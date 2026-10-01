#!/usr/bin/env python3
"""Достаёт картинки заданий из PDF-выгрузки «Взнания» и кладёт в media/sm3/uN/.

В выгрузке у каждой домашки два файла: `.txt` (только текст) и `.pdf` того же
имени. Кадры истории Ben & Lucy, грамматические таблички и прочие картинки
учебника лежат только в PDF — текстовый файл показывает на их месте пустой
блок «Загрузите картинку».

  python3 tools/sm3_pdf_frames.py --pdf hw5.pdf                 что внутри
  python3 tools/sm3_pdf_frames.py --pdf hw5.pdf --dump out/     всё в папку
  python3 tools/sm3_pdf_frames.py --pdf hw5.pdf --unit u1 \
          --take 203:story_library_1 213:story_library_2 384:story_code

Галерею фонов редактора (900×506, по несколько штук на странице, после блока
«Выберите новое задание для урока») скрипт сам не фильтрует — её видно по
размеру в листинге, брать её не нужно.
"""
import argparse, io, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUALITY = 88          # в кадрах есть реплики мелким шрифтом


def main():
    try:
        import pymupdf
    except ImportError:
        sys.exit("нет pymupdf: pip install pymupdf")
    from PIL import Image

    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--unit", help="папка media/sm3/<unit>/")
    ap.add_argument("--take", nargs="*", default=[], metavar="XREF:ИМЯ")
    ap.add_argument("--dump", help="выгрузить все картинки в эту папку")
    args = ap.parse_args()

    doc = pymupdf.open(args.pdf)

    if not args.take and not args.dump:
        for n, page in enumerate(doc, start=1):
            for xref, _, w, h, *_ in page.get_images(full=True):
                print(f"стр. {n:>2}  xref {xref:<5} {w}×{h}")
        return

    def save(xref, path):
        raw = doc.extract_image(xref)["image"]
        im = Image.open(io.BytesIO(raw)).convert("RGB")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        im.save(path, "WEBP", quality=QUALITY, method=6)
        print(f"{os.path.relpath(path, ROOT)}  {im.width}×{im.height}  "
              f"{os.path.getsize(path) // 1024} КБ")

    if args.dump:
        for n, page in enumerate(doc, start=1):
            for xref, _, w, h, *_ in page.get_images(full=True):
                save(xref, os.path.join(args.dump, f"p{n:02d}_{xref}_{w}x{h}.webp"))

    for item in args.take:
        xref, name = item.split(":", 1)
        if not args.unit:
            sys.exit("--take требует --unit")
        save(int(xref), os.path.join(ROOT, "media", "sm3", args.unit, name + ".webp"))


if __name__ == "__main__":
    main()
