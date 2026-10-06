#!/usr/bin/env python3
"""Unit 3: кадры из выгрузки, которым нужна доработка после извлечения.

Берёт картинку прямо из PDF (а не из готового webp), поэтому переприменяемый:
повторный прогон даёт тот же файл, а не пережимает уже сжатый.

  * prepositions_living_room — гостиная «Prepositions of Place» (HW2 (2)):
    на экране телевизора логотип NETFLIX, закрашиваем цветом экрана.
  * kids_room_test — детская к SPEAKING TASK теста: сверху в кадр влезает
    чужое лицо, срезаем полосу.
  * prep_* — шарик и куб из карточки «предлоги места» (HW2 (2), xref 199)
    по отдельности, без подписи: для match «предлог ↔ картинка».

  python3 tools/gg1_u3_frames.py <папка с PDF выгрузки u3>
"""
import io, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "media", "gg1", "u3")

# (x0, y0, x1, y1) в карточке 718×285 — только куб с шариком, без слова
PREP_CROPS = {
    "prep_behind": (140, 2, 285, 118),
    "prep_in": (330, 2, 460, 118),
    "prep_in_front_of": (590, 2, 715, 125),
    "prep_next_to": (90, 150, 260, 272),
    "prep_on": (335, 140, 455, 272),
    "prep_under": (595, 145, 715, 280),
}

# подписи: behind, in, in front of, next to, on, under
TEXT_BOXES = [(25, 35, 152, 85), (295, 35, 343, 85), (475, 35, 603, 128),
              (25, 155, 150, 205), (295, 155, 350, 205), (475, 155, 590, 205)]


def main():
    import pymupdf
    from PIL import Image, ImageDraw

    src = sys.argv[1]

    def load(pdf, xref):
        doc = pymupdf.open(os.path.join(src, pdf))
        return Image.open(io.BytesIO(doc.extract_image(xref)["image"])).convert("RGB")

    def save(im, name, q=88):
        path = os.path.join(OUT, name + ".webp")
        im.save(path, "WEBP", quality=q, method=6)
        print(os.path.relpath(path, ROOT), im.size)

    im = load("hw2_2.pdf", 208)
    ImageDraw.Draw(im).rectangle((758, 305, 852, 355), fill=(238, 238, 238))
    save(im, "prepositions_living_room", 82)

    im = load("test.pdf", 712)
    save(im.crop((0, 56, im.width, im.height)), "kids_room_test", 82)

    card = load("hw2_2.pdf", 199)
    # подписи стоят вплотную к кубам — сначала стираем их цветом фона
    bg = card.getpixel((5, 140))
    for box in TEXT_BOXES:
        ImageDraw.Draw(card).rectangle(box, fill=bg)
    for name, box in PREP_CROPS.items():
        piece = card.crop(box)
        side = max(piece.size)
        sq = Image.new("RGB", (side, side), bg)
        sq.paste(piece, ((side - piece.width) // 2, (side - piece.height) // 2))
        save(sq.resize((240, 240), Image.LANCZOS), name)


if __name__ == "__main__":
    main()
