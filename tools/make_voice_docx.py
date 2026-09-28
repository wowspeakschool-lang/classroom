#!/usr/bin/env python3
"""Собирает файл озвучки в Word: каждая реплика отдельным блоком.

    python3 tools/make_voice_docx.py

Кладёт `docs/WowSpeak_озвучка_4-6.docx`. Текст тот же, что в markdown-файле,
но с паузами, расставленными тегами, и разбитый так, чтобы каждую реплику
было видно отдельно: номер, интонация, текст — и линейка между ними.

Документ собирается из голого OOXML через `zipfile`: .docx — это zip с
несколькими xml внутри. Для такого простого документа это надёжнее, чем
тянуть зависимость, которой может не оказаться в контейнере.
"""

import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_kids46 import build_script, ROOT

OUT = ROOT / "docs" / "WowSpeak_озвучка_4-6.docx"

# Тире и многоточие движок сам паузой не считает — ставим тег явно.
BREAK_DASH = '<break time="400ms"/>'
BREAK_DOTS = '<break time="600ms"/>'
BREAK_TRACK = '<break time="2s"/>'


def ssml(text):
    t = re.sub(r"\s*—", " " + BREAK_DASH + "—", text)
    return t.replace("…", "… " + BREAK_DOTS)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def run(text, *, bold=False, italic=False, color=None, size=None, mono=False):
    """Порядок свойств внутри rPr задан схемой: rFonts, b, i, color, sz.

    Переставишь — и файл не откроется вовсе: LibreOffice отвечает «source
    file could not be loaded», не уточняя, что именно не так.
    """
    rpr = []
    if mono:
        rpr.append('<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>')
    if bold:
        rpr.append("<w:b/>")
    if italic:
        rpr.append("<w:i/>")
    if color:
        rpr.append(f'<w:color w:val="{color}"/>')
    if size:
        rpr.append(f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>')
    pr = f"<w:rPr>{''.join(rpr)}</w:rPr>" if rpr else ""
    return f"<w:r>{pr}<w:t xml:space=\"preserve\">{esc(text)}</w:t></w:r>"


def para(runs, *, style=None, space_after=120, border=False, ind=0):
    """И здесь порядок схемный: pStyle, pBdr, spacing, ind — именно такой."""
    pr = ["<w:pPr>"]
    if style:
        pr.append(f'<w:pStyle w:val="{style}"/>')
    if border:
        pr.append('<w:pBdr><w:bottom w:val="single" w:sz="4" w:space="6" '
                  'w:color="D8D8E0"/></w:pBdr>')
    pr.append(f'<w:spacing w:after="{space_after}"/>')
    if ind:
        pr.append(f'<w:ind w:left="{ind}"/>')
    pr.append("</w:pPr>")
    return "<w:p>" + "".join(pr) + "".join(runs) + "</w:p>"


def build():
    script, *_ = build_script()
    by = {}
    for key, _voice, text, tone, where in script:
        by.setdefault(where, []).append((key, text, tone))

    body = [
        para([run("Озвучка лид-магнита 4–6 «Дорога на праздник»",
                  bold=True, size="40")], space_after=80),
        para([run("Текст с расставленными паузами. Каждая реплика — отдельный "
                  "блок: номер дорожки, интонация, текст.", color="555555",
                  size="20")], space_after=300),
        para([run("Как вставлять в сервис", bold=True, size="26")], space_after=80),
        para([run("Включите режим SSML (кнопка ", size="20"),
              run("</> SSML", mono=True, size="20"),
              run(" на панели) — без него теги прочитаются вслух как текст. "
                  "Можно вставлять весь раздел целиком: между репликами стоит "
                  "пауза в две секунды, по ней длинный файл потом режется на "
                  "отдельные дорожки.", size="20")], space_after=300),
    ]

    for where, items in by.items():
        body.append(para([run(where, bold=True, size="30")], space_after=160))
        for key, text, tone in items:
            head = [run(key, bold=True, size="22")]
            if tone:
                head.append(run("   " + tone, italic=True, color="7A7A8A", size="18"))
            body.append(para(head, space_after=40))
            body.append(para([run(ssml(text), size="22")],
                             space_after=60, ind=200))
            body.append(para([run(BREAK_TRACK, mono=True, color="A0A0B0", size="16")],
                             space_after=180, border=True, ind=200))

    doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
           "<w:body>" + "".join(body) +
           '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
           '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134"/>'
           "</w:sectPr></w:body></w:document>")

    types = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
             '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
             '<Default Extension="xml" ContentType="application/xml"/>'
             '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
             "</Types>")

    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" '
            'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
            'Target="word/document.xml"/></Relationships>')

    # Связи документа: пустые, но часть обязана быть — без неё
    # LibreOffice файл не открывает.
    doc_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<Relationships xmlns="http://schemas.openxmlformats.org/'
                'package/2006/relationships"/>')

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/_rels/document.xml.rels", doc_rels)
        z.writestr("word/document.xml", doc)

    n = sum(len(v) for v in by.values())
    print(f"{OUT.name}: реплик {n}, разделов {len(by)}, "
          f"{OUT.stat().st_size // 1024} КБ")


if __name__ == "__main__":
    build()
