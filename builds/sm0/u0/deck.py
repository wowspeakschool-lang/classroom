# -*- coding: utf-8 -*-
"""Презентация «Unit 0 · Say Hello! — Lesson 6 (Revision + Test)».

    python3.13 builds/sm0/u0/deck.py <шаблон.pptx> <png-папка> <куда.pptx>

Оформление берётся из присланного методистом файла Unit 1 Lesson 7.pptx:
скрипт открывает его как шаблон, удаляет слайды и собирает свои в том же
стиле — те же фоны (FFE4EA / E3F0FB), белые круги по углам, белая карточка,
Verdana и Trebuchet MS, те же цвета заголовков.

На слайдах — только английский: короткая инструкция вида «Click the colour!».
Русский остаётся в плане урока и на слайде «Я могу!», как в образце.

Игры собраны переходами по клику: клик по фигуре открывает слайд-ответ,
кнопка возвращает назад. Работает в PowerPoint без настройки.
"""
import sys, os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

TEMPLATE, OUT = sys.argv[1], sys.argv[2]


# ── палитра образца ───────────────────────────────────────────────────────
PINK_BG = RGBColor(0xFF, 0xE4, 0xEA)
BLUE_BG = RGBColor(0xE3, 0xF0, 0xFB)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BLUE = RGBColor(0x15, 0x65, 0xC0)
PURPLE = RGBColor(0x7B, 0x1F, 0xA2)
TEAL = RGBColor(0x0E, 0x74, 0x90)
INK = RGBColor(0x3A, 0x2A, 0x4D)
GREY = RGBColor(0x6B, 0x72, 0x80)
GREEN = RGBColor(0x2E, 0xA8, 0x4F)
HEAD = 'Verdana'
BODY = 'Trebuchet MS'

prs = Presentation(TEMPLATE)
RID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
for sld in list(prs.slides._sldIdLst):          # шаблон чистим, дизайн остаётся
    prs.part.drop_rel(sld.get(RID))
    prs.slides._sldIdLst.remove(sld)
LAYOUT = prs.slide_layouts[0]
W, H = prs.slide_width, prs.slide_height
_n = [0]


def slide(bg=None):
    """Новый слайд: фон через один розовый/голубой, два белых круга по углам."""
    s = prs.slides.add_slide(LAYOUT)
    _n[0] += 1
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = bg or (PINK_BG if _n[0] % 2 else BLUE_BG)
    for left, top, size in ((Inches(-1.3), Inches(-1.3), Inches(3.2)),
                            (Inches(11.4), Inches(5.5), Inches(3.4))):
        blob = s.shapes.add_shape(MSO_SHAPE.OVAL, left, top, size, size)
        blob.fill.solid()
        blob.fill.fore_color.rgb = WHITE
        blob.line.fill.background()
        blob.shadow.inherit = False
    return s


def text(s, txt, *, top, size, color=INK, font=HEAD, bold=True,
         left=Inches(0.6), width=None, height=Inches(1.1), align=PP_ALIGN.CENTER):
    box = s.shapes.add_textbox(left, top, width or (W - Inches(1.2)), height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    for i, line in enumerate(txt.split('\n')):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run()
        r.text = line
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.name = font
        r.font.color.rgb = color
    return box


def title(s, txt, color=None):
    return text(s, txt, top=Inches(0.5), size=38, color=color or
                (PURPLE if _n[0] % 2 else BLUE))


def card(s, left, top, width, height):
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    sh.fill.solid()
    sh.fill.fore_color.rgb = WHITE
    sh.line.fill.background()
    sh.shadow.inherit = False
    sh.adjustments[0] = 0.04
    return sh


def tile(s, txt, *, left, top, width, height, size=28, color=INK, target=None):
    sh = card(s, left, top, width, height)
    tf = sh.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = txt
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.name = HEAD
    r.font.color.rgb = color
    if target is not None:
        sh.click_action.target_slide = target
    return sh


BALLOON = {'red': RGBColor(0xFD, 0x20, 0x1F), 'green': RGBColor(0x67, 0xC1, 0x2E),
           'blue': RGBColor(0x00, 0x9D, 0xFE), 'orange': RGBColor(0xFE, 0x7E, 0x03),
           'pink': RGBColor(0xFF, 0x69, 0xAB), 'yellow': RGBColor(0xFF, 0xD7, 0x03)}
CHEEK = RGBColor(0xFF, 0xA8, 0xBD)
DARK = RGBColor(0x2B, 0x2B, 0x2B)


def _oval(s, left, top, w, h, fill, line=None):
    sh = s.shapes.add_shape(MSO_SHAPE.OVAL, int(left), int(top), int(w), int(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line
    sh.shadow.inherit = False
    return sh


def balloon(s, name, left, top, height, target=None):
    """Шарик фигурами: овал, узелок, ниточка, глаза, щёки, ротик.

    Вектор — на любом размере чёткий, растровых картинок в презентации нет.
    """
    col = BALLOON[name]
    h = int(height * 0.78)                 # тело; остальное — ниточка
    w = int(h * 0.70)
    cx = int(left + w / 2)
    body = _oval(s, left, top, w, h, col)
    if target is not None:
        body.click_action.target_slide = target

    knot = s.shapes.add_shape(MSO_SHAPE.ISOSCELES_TRIANGLE,
                              int(cx - h * 0.055), int(top + h * 0.98),
                              int(h * 0.11), int(h * 0.08))
    knot.fill.solid(); knot.fill.fore_color.rgb = col
    knot.line.fill.background(); knot.shadow.inherit = False
    knot.rotation = 180

    string = s.shapes.add_shape(MSO_SHAPE.ARC, int(cx - h * 0.09),
                                int(top + h * 1.05), int(h * 0.18), int(h * 0.26))
    string.fill.background()
    string.line.color.rgb = col
    string.line.width = Pt(1.75)
    string.shadow.inherit = False

    eye_w, eye_h = int(h * 0.15), int(h * 0.19)
    for dx in (-0.17, 0.17):
        _oval(s, cx + h * dx - eye_w / 2, top + h * 0.33, eye_w, eye_h, DARK)
        _oval(s, cx + h * dx - eye_w / 2 + eye_w * 0.22, top + h * 0.36,
              eye_w * 0.34, eye_h * 0.3, WHITE)
    for dx in (-0.29, 0.29):
        _oval(s, cx + h * dx - h * 0.07, top + h * 0.54, h * 0.14, h * 0.09, CHEEK)
    _oval(s, cx - h * 0.1, top + h * 0.55, h * 0.2, h * 0.13, DARK)
    return body


COLOURS = ['red', 'green', 'blue', 'orange', 'pink', 'yellow']
WORDS = ['sat', 'pin', 'ten', 'red', 'kit', 'dad']
ROUNDS = [('red', 4, 'four'), ('blue', 5, 'five'), ('yellow', 3, 'three')]

# 1 · титул ────────────────────────────────────────────────────────────────
s = slide(PINK_BG)
text(s, 'Unit 0 · Lesson 6', top=Inches(2.1), size=40, color=BLUE, height=Inches(1.2))
text(s, 'Say Hello! 👋', top=Inches(3.3), size=60, color=PURPLE, height=Inches(1.5))
text(s, 'Revision + Test · Super Minds Starter · WowSpeak',
     top=Inches(5.0), size=20, color=GREY, font=BODY, bold=False, height=Inches(0.7))

# 2 · greeting ─────────────────────────────────────────────────────────────
s = slide()
title(s, 'How are you?')
card(s, Inches(1.6), Inches(1.9), Inches(10.1), Inches(4.6))
for i, (emo, word) in enumerate([('😀', 'happy'), ('😢', 'sad'), ('😠', 'angry')]):
    left = Inches(2.2) + i * Inches(3.2)
    text(s, emo, top=Inches(2.4), size=96, left=left, width=Inches(2.8), height=Inches(2.2))
    text(s, word, top=Inches(4.6), size=28, left=left, width=Inches(2.8), height=Inches(0.9))

# 3 · warm-up reading ──────────────────────────────────────────────────────
s = slide()
title(s, 'Read! 📖')
card(s, Inches(1.4), Inches(1.9), Inches(10.5), Inches(4.4))
box = s.shapes.add_textbox(Inches(1.6), Inches(2.1), Inches(10.1), Inches(3.9))
tf = box.text_frame
tf.word_wrap = True
tf.vertical_anchor = MSO_ANCHOR.MIDDLE
for i, row in enumerate([['sat', 'pin', 'ten', 'red'], ['kit', 'dad', 'rat', 'pen']]):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    for j, w in enumerate(row):
        if j:
            sp = p.add_run(); sp.text = '    '
            sp.font.size = Pt(38); sp.font.name = HEAD
        r = p.add_run()
        r.text = w
        r.font.size = Pt(38)
        r.font.bold = True
        r.font.name = HEAD
        r.font.color.rgb = (PURPLE, TEAL, INK, BLUE)[j % 4]

# 4 · HW check ─────────────────────────────────────────────────────────────
s = slide()
text(s, 'HW check ✅', top=Inches(2.8), size=60, color=BLUE, height=Inches(1.6))

# 5–11 · игра 1: цвета ─────────────────────────────────────────────────────
board1 = slide()
colour_slides = {c: slide() for c in COLOURS}

title(board1, 'Colours 🎈', color=PURPLE)
text(board1, 'Click the colour!', top=Inches(1.35), size=20, color=GREY,
     font=BODY, bold=False, height=Inches(0.6))
card(board1, Inches(1.4), Inches(1.95), Inches(10.5), Inches(4.5))
for i, c in enumerate(COLOURS):
    col, row = i % 3, i // 3
    balloon(board1, c, Inches(2.4) + col * Inches(3.1), Inches(2.2) + row * Inches(2.2),
            Inches(2.0), target=colour_slides[c])
for c, sc in colour_slides.items():
    title(sc, c, color=PURPLE)
    card(sc, Inches(4.2), Inches(1.7), Inches(4.9), Inches(4.1))
    balloon(sc, c, int((W - Inches(2.1)) / 2), Inches(2.0), Inches(3.4))
    tile(sc, '↩ Back', left=Inches(5.4), top=Inches(6.1), width=Inches(2.5),
         height=Inches(0.8), size=20, color=GREY, target=board1)

# 12–17 · How many ─────────────────────────────────────────────────────────
q_slides = [slide() for _ in ROUNDS]
a_slides = [slide() for _ in ROUNDS]
for i, (colour, n, word) in enumerate(ROUNDS):
    sq, sa = q_slides[i], a_slides[i]
    title(sq, 'How many? 🔢', color=BLUE)
    card(sq, Inches(1.4), Inches(1.9), Inches(10.5), Inches(3.6))
    step = Inches(1.95)
    start = int((W - n * step) / 2 + (step - Inches(1.6)) / 2)
    for k in range(n):
        balloon(sq, colour, start + k * step, Inches(2.3), Inches(2.6))
    tile(sq, 'Check →', left=int((W - Inches(3.2)) / 2), top=Inches(5.8),
         width=Inches(3.2), height=Inches(0.9), size=24, color=BLUE, target=sa)
    title(sa, 'How many? 🔢', color=BLUE)
    card(sa, Inches(3.0), Inches(2.0), Inches(7.3), Inches(3.4))
    text(sa, f'{n} — {word} 🎉', top=Inches(2.9), size=66, color=GREEN, height=Inches(1.6))
    if i + 1 < len(ROUNDS):
        tile(sa, 'Next →', left=int((W - Inches(3.0)) / 2), top=Inches(5.8),
             width=Inches(3.0), height=Inches(0.9), size=24, color=BLUE,
             target=q_slides[i + 1])

# 18–24 · игра 2: кубик и чтение ───────────────────────────────────────────
board2 = slide()
card_slides = [slide() for _ in WORDS]
title(board2, 'Pick & read 🃏', color=PURPLE)
text(board2, 'Pick a card and read!', top=Inches(1.3), size=20,
     color=GREY, font=BODY, bold=False, height=Inches(0.5))
card(board2, Inches(1.4), Inches(1.95), Inches(10.5), Inches(4.3))
for i, w in enumerate(WORDS):
    col, row = i % 3, i // 3
    tile(board2, '?', left=Inches(2.2) + col * Inches(3.1),
         top=Inches(2.3) + row * Inches(1.8), width=Inches(2.6), height=Inches(1.5),
         size=44, color=(PURPLE, TEAL, BLUE)[i % 3], target=card_slides[i])
for i, w in enumerate(WORDS):
    sd = card_slides[i]
    title(sd, 'Read it! 🃏', color=BLUE)
    card(sd, Inches(3.0), Inches(1.8), Inches(7.3), Inches(3.5))
    text(sd, w, top=Inches(2.4), size=96, color=PURPLE, height=Inches(2.3))
    tile(sd, '↩ Back', left=int((W - Inches(2.6)) / 2), top=Inches(5.7),
         width=Inches(2.6), height=Inches(0.9), size=20, color=GREY, target=board2)

# 25 · тест ────────────────────────────────────────────────────────────────
s = slide()
title(s, 'Test 📝', color=BLUE)
card(s, Inches(3.0), Inches(2.0), Inches(7.3), Inches(3.9))
text(s, 'Unit 0', top=Inches(2.4), size=44, color=PURPLE, height=Inches(1.3))
text(s, '💪', top=Inches(3.7), size=54, height=Inches(1.1))
text(s, 'paste the test link here', top=Inches(4.9), size=18, color=GREY,
     font=BODY, bold=False, height=Inches(0.9))

# 26 · я могу ──────────────────────────────────────────────────────────────
s = slide()
title(s, 'Я могу! 🎉', color=PURPLE)
card(s, Inches(2.0), Inches(1.9), Inches(9.3), Inches(4.5))
text(s, 'Здороваться и знакомиться: Hello! I’m …\n'
        'Называть цвета: red, green, blue, orange, pink, yellow\n'
        'Считать до 10\n'
        'Читать слова: sat, pin, ten, red, kit, dad',
     top=Inches(2.3), size=24, color=INK, font=BODY, bold=False,
     left=Inches(2.7), width=Inches(7.9), height=Inches(3.7), align=PP_ALIGN.LEFT)

# 27 · домашнее задание ────────────────────────────────────────────────────
s = slide()
text(s, 'Assign HW 📝', top=Inches(2.6), size=60, color=BLUE, height=Inches(1.6))
text(s, 'NO HW', top=Inches(4.2), size=32, color=GREY, font=BODY, bold=False)

# 28 · финал ───────────────────────────────────────────────────────────────
s = slide()
title(s, 'Rate the lesson', color=PURPLE)
card(s, Inches(2.2), Inches(2.2), Inches(8.9), Inches(3.4))
text(s, '⭐ ⭐ ⭐ ⭐ ⭐', top=Inches(2.5), size=60, height=Inches(2.0))
text(s, 'Bye-bye! 👋', top=Inches(5.7), size=32, color=PURPLE, height=Inches(0.8))

# 29–31 · запас ────────────────────────────────────────────────────────────
s = slide()
title(s, '⏱ Reading race', color=BLUE)
card(s, Inches(1.4), Inches(2.0), Inches(10.5), Inches(3.4))
text(s, 'sat   pin   ten   red   kit   dad   rat   pen   den   as',
     top=Inches(3.0), size=36, color=INK, height=Inches(1.4))
text(s, 'Read the line. Faster!', top=Inches(5.7), size=20, color=GREY,
     font=BODY, bold=False, height=Inches(0.7))

s = slide()
title(s, '🔍 Find & read', color=PURPLE)
card(s, Inches(3.2), Inches(1.7), Inches(7.0), Inches(4.3))
for r, row in enumerate([['sat', 'pin', 'ten'], ['red', 'kit', 'dad'], ['rat', 'pen', 'as']]):
    for c, w in enumerate(row):
        text(s, w, top=Inches(1.9) + r * Inches(1.35), size=36,
             color=(PURPLE, TEAL, BLUE)[c], left=Inches(3.4) + c * Inches(2.2),
             width=Inches(2.0), height=Inches(1.0))

s = slide()
title(s, '🎯 Colour bingo', color=BLUE)
card(s, Inches(1.4), Inches(1.6), Inches(10.5), Inches(4.6))
for i, c in enumerate(COLOURS):
    col, row = i % 3, i // 3
    balloon(s, c, Inches(2.4) + col * Inches(3.1), Inches(1.9) + row * Inches(2.3),
            Inches(2.1))

prs.save(OUT)
print(f'слайдов: {_n[0]} → {OUT}')
