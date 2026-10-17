# -*- coding: utf-8 -*-
"""Презентация «Unit 0 · Say Hello! — Lesson 6 (Revision + Test)».

    python3.13 builds/sm0/u0/deck.py <папка-с-png> <куда-положить.pptx>

Игры собраны переходами по клику: ребёнок кликает по фигуре, презентация
прыгает на слайд-ответ и возвращается назад. Работает в PowerPoint на
компьютере без настройки, ничего не ломается при показе.
"""
import sys, os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

PNG, OUT = sys.argv[1], sys.argv[2]

# шарики лежат в репозитории в webp; PowerPoint их не ест — переводим в png
HASH = {'red': '8b38abac4dbc', 'green': '481214562a38', 'blue': '34b8efecd4b2',
        'orange': 'ce01e4bbf55f', 'pink': 'f40c937be9f8', 'yellow': 'fccf971c0287'}
if not all(os.path.exists(f'{PNG}/{n}.png') for n in HASH):
    from PIL import Image
    os.makedirs(PNG, exist_ok=True)
    legacy = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          '..', '..', '..', 'media', 'sm0', 'legacy')
    for name, h in HASH.items():
        im = Image.open(f'{legacy}/{h}.webp').convert('RGBA')
        bg = Image.new('RGBA', im.size, (255, 255, 255, 255))
        bg.alpha_composite(im)
        bg.convert('RGB').save(f'{PNG}/{name}.png')

INK = RGBColor(0x1F, 0x2A, 0x44)      # тёмно-синий текст
ACC = RGBColor(0xFF, 0x6B, 0x35)      # оранжевый акцент
SOFT = RGBColor(0xEF, 0xF3, 0xFB)     # светлая плашка
GREEN = RGBColor(0x2E, 0xA8, 0x4F)
W, H = Inches(13.333), Inches(7.5)

prs = Presentation()
prs.slide_width, prs.slide_height = W, H
BLANK = prs.slide_layouts[6]


def slide():
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    return s


def text(s, txt, *, top, size, bold=True, color=INK, left=Inches(0.6),
         width=None, align=PP_ALIGN.CENTER, height=Inches(1.2)):
    width = width or (W - Inches(1.2))
    box = s.shapes.add_textbox(left, top, width, height)
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
        r.font.color.rgb = color
        r.font.name = 'Segoe UI'
    return box


def button(s, txt, *, left, top, width, height, target=None,
           fill=SOFT, color=INK, size=28):
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    sh.line.color.rgb = RGBColor(0xD6, 0xDE, 0xEC)
    sh.shadow.inherit = False
    tf = sh.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = txt
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.color.rgb = color
    r.font.name = 'Segoe UI'
    if target is not None:
        sh.click_action.target_slide = target
    return sh


def picture(s, name, left, top, height):
    return s.shapes.add_picture(f'{PNG}/{name}.png', left, top, height=height)


def footer(s, txt):
    text(s, txt, top=H - Inches(0.85), size=14, bold=False,
         color=RGBColor(0x8A, 0x93, 0xA6), height=Inches(0.5))


COLOURS = ['red', 'green', 'blue', 'orange', 'pink', 'yellow']
WORDS = ['sat', 'pin', 'ten', 'red', 'kit', 'dad']

# ── 1. титул ──────────────────────────────────────────────────────────────
s1 = slide()
text(s1, 'Unit 0 · Lesson 6', top=Inches(2.0), size=30, color=ACC)
text(s1, 'Say Hello! 👋', top=Inches(2.8), size=72)
text(s1, 'Revision + Test · Super Minds Starter · WowSpeak',
     top=Inches(4.3), size=22, bold=False, color=RGBColor(0x6B, 0x74, 0x88))

# ── 2. greeting ───────────────────────────────────────────────────────────
s2 = slide()
text(s2, 'How are you?', top=Inches(1.0), size=54)
for i, (emo, word) in enumerate([('😀', 'happy'), ('😢', 'sad'), ('😠', 'angry')]):
    left = Inches(1.6) + i * Inches(3.5)
    text(s2, emo, top=Inches(2.6), size=96, left=left, width=Inches(3.0), height=Inches(1.8))
    text(s2, word, top=Inches(4.6), size=36, left=left, width=Inches(3.0), color=ACC)

# ── 3. warm-up reading ────────────────────────────────────────────────────
s3 = slide()
text(s3, 'Read! 📖', top=Inches(0.8), size=48)
text(s3, 'sat    pin    ten    red', top=Inches(2.4), size=60)
text(s3, 'kit    dad    rat    pen', top=Inches(3.9), size=60)
footer(s3, 'Ребёнок читает сам. Второй круг — быстрее.')

# ── 4. HW check ───────────────────────────────────────────────────────────
s4 = slide()
text(s4, 'HW check ✅', top=Inches(3.0), size=60)

# ── 5–11. игра 1: поймай цвет ─────────────────────────────────────────────
board1 = slide()
colour_slides = {}
for c in COLOURS:
    sc = slide()
    text(sc, c, top=Inches(0.8), size=72, color=ACC)
    picture(sc, c, left=int((W - Inches(2.2)) / 2), top=Inches(2.2), height=Inches(3.4))
    colour_slides[c] = sc

text(board1, 'Поймай цвет! 🎈', top=Inches(0.5), size=48)
text(board1, 'Listen and click: "Click red!"', top=Inches(1.4), size=24,
     bold=False, color=RGBColor(0x6B, 0x74, 0x88), height=Inches(0.6))
for i, c in enumerate(COLOURS):
    col, row = i % 3, i // 3
    left = Inches(2.2) + col * Inches(3.2)
    top = Inches(2.2) + row * Inches(2.5)
    pic = picture(board1, c, left=left, top=top, height=Inches(2.2))
    pic.click_action.target_slide = colour_slides[c]
for c, sc in colour_slides.items():
    button(sc, '↩ назад к шарикам', left=int((W - Inches(4.6)) / 2), top=Inches(6.0),
           width=Inches(4.6), height=Inches(0.8), target=board1, size=22)
footer(board1, 'Клик по шарику открывает его название — проверка себя.')

# ── 12–17. числа: сколько шариков ─────────────────────────────────────────
rounds = [('red', 4, 'four'), ('blue', 5, 'five'), ('yellow', 3, 'three')]
q_slides, a_slides = [], []
for colour, n, word in rounds:
    q_slides.append(slide())
    a_slides.append(slide())
for i, (colour, n, word) in enumerate(rounds):
    sq, sa = q_slides[i], a_slides[i]
    text(sq, 'How many? 🔢', top=Inches(0.5), size=44)
    total = n * Inches(1.5)
    start = int((W - total) / 2)
    for k in range(n):
        picture(sq, colour, left=start + k * Inches(1.5), top=Inches(2.2), height=Inches(2.6))
    button(sq, 'Проверить →', left=int((W - Inches(3.6)) / 2), top=Inches(5.6),
           width=Inches(3.6), height=Inches(0.9), target=sa, size=26, fill=SOFT)
    text(sa, f'{n} — {word} 🎉', top=Inches(2.6), size=80, color=GREEN)
    nxt = q_slides[i + 1] if i + 1 < len(rounds) else None
    if nxt is not None:
        button(sa, 'Дальше →', left=int((W - Inches(3.2)) / 2), top=Inches(5.6),
               width=Inches(3.2), height=Inches(0.9), target=nxt, size=26)

# ── 18–24. игра 2: кубик и чтение ─────────────────────────────────────────
board2 = slide()
dice_slides = [slide() for _ in WORDS]
text(board2, 'Кубик и чтение 🎲', top=Inches(0.5), size=48)
for i, w in enumerate(WORDS):
    col, row = i % 3, i // 3
    left = Inches(2.0) + col * Inches(3.3)
    top = Inches(1.9) + row * Inches(1.6)
    button(board2, f'{i + 1}   {w}', left=left, top=top, width=Inches(2.8),
           height=Inches(1.2), size=34, target=dice_slides[i])
dice = button(board2, '🎲  бросить кубик', left=int((W - Inches(5.0)) / 2),
              top=Inches(5.4), width=Inches(5.0), height=Inches(1.0),
              target=dice_slides[0], size=28, fill=RGBColor(0xFF, 0xE8, 0xDC), color=ACC)
footer(board2, 'Кубик идёт по кругу 1→6: каждый клик — следующее слово.')
for i, w in enumerate(WORDS):
    sd = dice_slides[i]
    text(sd, f'🎲 {i + 1}', top=Inches(0.8), size=44, color=ACC)
    text(sd, w, top=Inches(2.4), size=110)
    button(sd, '🎲 ещё раз', left=Inches(3.6), top=Inches(5.8), width=Inches(3.0),
           height=Inches(0.9), target=dice_slides[(i + 1) % len(WORDS)], size=24)
    button(sd, '↩ к словам', left=Inches(6.9), top=Inches(5.8), width=Inches(3.0),
           height=Inches(0.9), target=board2, size=24)

# ── 25. тест ──────────────────────────────────────────────────────────────
s_test = slide()
text(s_test, 'Test 📝', top=Inches(1.2), size=64)
text(s_test, 'Unit 0', top=Inches(2.4), size=44, color=ACC)
button(s_test, 'ссылку на тест вставить сюда перед уроком',
       left=Inches(2.6), top=Inches(3.6), width=Inches(8.1), height=Inches(1.0), size=22)
text(s_test, 'You can do it! 💪', top=Inches(5.0), size=36, color=GREEN)

# ── 26. я могу ────────────────────────────────────────────────────────────
s_can = slide()
text(s_can, 'Я могу! ✅', top=Inches(0.6), size=48)
text(s_can,
     'Здороваться и знакомиться: Hello! I’m …\n'
     'Называть цвета: red, green, blue, orange, pink, yellow\n'
     'Считать до 10\n'
     'Читать слова: sat, pin, ten, red, kit, dad',
     top=Inches(2.0), size=30, bold=False, align=PP_ALIGN.LEFT,
     left=Inches(2.4), width=Inches(9.0), height=Inches(3.4))

# ── 27. домашнее задание ──────────────────────────────────────────────────
s_hw = slide()
text(s_hw, 'Assign HW', top=Inches(2.6), size=54)
text(s_hw, 'NO HW — юнит закончен', top=Inches(3.9), size=32, bold=False, color=ACC)

# ── 28. финал ─────────────────────────────────────────────────────────────
s_end = slide()
text(s_end, 'Rate the lesson', top=Inches(1.4), size=48)
text(s_end, '⭐ ⭐ ⭐ ⭐ ⭐', top=Inches(2.8), size=72)
text(s_end, 'Bye-bye! 👋', top=Inches(4.6), size=54, color=ACC)

# ── 29–31. запас ──────────────────────────────────────────────────────────
s_r1 = slide()
text(s_r1, '⏱ Reading race', top=Inches(0.8), size=44, color=ACC)
text(s_r1, 'sat  pin  ten  red  kit  dad  rat  pen  den  as', top=Inches(2.6), size=46)
footer(s_r1, 'Кто быстрее и без ошибок прочитает строку. Побей свой рекорд.')

s_r2 = slide()
text(s_r2, '🔍 Find & read', top=Inches(0.6), size=44, color=ACC)
grid = [['sat', 'pin', 'ten'], ['red', 'kit', 'dad'], ['rat', 'pen', 'as']]
for r, row in enumerate(grid):
    for c, w in enumerate(row):
        text(s_r2, w, top=Inches(1.8) + r * Inches(1.4), size=44,
             left=Inches(3.2) + c * Inches(2.6), width=Inches(2.4), height=Inches(1.0))
footer(s_r2, 'Учитель называет слово — ребёнок находит его и читает вслух.')

s_r3 = slide()
text(s_r3, '🎯 Colour bingo', top=Inches(0.5), size=44, color=ACC)
for i, c in enumerate(COLOURS):
    col, row = i % 3, i // 3
    picture(s_r3, c, left=Inches(2.6) + col * Inches(3.0), top=Inches(1.8) + row * Inches(2.4),
            height=Inches(2.1))
footer(s_r3, 'Учитель называет цвета подряд — ребёнок отмечает, кто первым соберёт ряд.')

prs.save(OUT)
print(f'слайдов: {len(prs.slides.__iter__.__self__._sldIdLst)} → {OUT}')
