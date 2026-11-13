# План вебинара 03.12 · A / an · еда · 7–9 — DOCX в виде прошлых вебинаров.
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '7-9', 'WOW_Speak_A_An_Food_7-9_PLAN.docx')
HEAD, PINK, GREEN, GREY = '3D2B5A', 'E91E8C', '2E7D32', '222222'

doc = Document()
sec = doc.sections[0]
sec.orientation = WD_ORIENT.LANDSCAPE
sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'):
    setattr(sec, m, Cm(1.27))
st = doc.styles['Normal']; st.font.name = 'Arial'; st.font.size = Pt(9.5)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')


def para(cell_or_doc, parts, space=2):
    p = cell_or_doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space)
    for t, color, bold, italic, *sz in parts:
        r = p.add_run(t); r.bold = bold; r.italic = italic
        r.font.name = 'Arial'; r.font.size = Pt(sz[0] if sz else 9.5)
        r.font.color.rgb = RGBColor.from_string(color)
    return p


def shade(cell, hexc):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement('w:shd'); sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), hexc)
    tcPr.append(sh)


pass
para(doc, [('WOW Speak   •   A / an   •   Food', HEAD, True, False, 15)])
para(doc, [('Группа 7–9 лет · 30 минут · Zoom, дети пишут в чат · вебинар 03.12', GREY, False, False)])
para(doc, [('Лексика (6 слов): ', HEAD, True, False), ('apple, egg, orange, banana, pear, sandwich', GREY, False, False)])
para(doc, [('Грамматика: ', HEAD, True, False),
           ('a перед согласным звуком, an перед гласным; с множественным числом a / an не ставим.', GREY, False, False)])
para(doc, [('Речь учителя', GREEN, False, True), (' — зелёным курсивом. Ответ на слайде открывается по клику: исчезает крышка.', GREY, False, False)], 6)

# Этап · Время · Цель · Задание (слайды) · Комментарий
S = lambda t: (t, GREEN, False, True)
N = lambda t: (t, GREY, False, False)
B = lambda t: (t, GREY, True, False)
rows = [
    ('Блок школы', '3 мин', 'Познакомиться, настроить на урок.',
     [[B('Слайд 1.'), N(' Приветствие, рассказ о школе WOW Speak.')],
      [S('Hello! Welcome to WOW Speak!')], [S('Напишите в чат, как вас зовут и откуда вы.')]],
     'Пока дети подключаются — здороваемся по именам из чата.'),
    ('Warm-up', '2 мин', 'Разогреться на знакомых словах (цвета, числа, вещи).',
     [[B('Слайд 2. Кто лишний?'), N(' Три ряда по 4 слова.')],
      [S('Найди лишнее слово в каждом ряду. Напиши в чат: 1 — буква, 2 — буква, 3 — буква.')]],
     'Ключ: 1 — C (cat), 2 — B (dog), 3 — D (sun). Клик по ряду открывает ответ.'),
    ('Lead-in', '2 мин', 'Ввести тему «еда».',
     [[B('Слайд 3. Что в ланч-боксе?')],
      [S('Как думаете, что у меня в ланч-боксе? Пишите в чат — можно по-русски!')]],
     'Читаем 3–4 догадки, клик — открывается сэндвич. Тему урока не называем словами «артикль».'),
    ('Лексика', '3 мин', 'Ввести 6 слов: apple, egg, orange, banana, pear, sandwich.',
     [[B('Слайд 4. Food.'), N(' Слова появляются по одному по клику.')],
      [S('Look! An apple.')], [S('Повторяйте за мной вслух, а в чат пишите слово.')]],
     'Называем каждое слово с артиклем (an apple, a banana) — дети слышат форму до правила.'),
    ('Игра на слова', '4 мин', 'Запомнить слова, узнавать их по картинке.',
     [[B('Слайд 5. Запомни!'), N(' Клик — 15 секунд на запоминание (полоса уменьшается).')],
      [B('Слайды 6–7. Что исчезло?'), N(' Два раунда.')],
      [S('Какой картинки не стало? Напиши слово в чат!')]],
     'Ключ: раунд 1 — pear, раунд 2 — egg. Клик открывает ответ.'),
    ('Грамматика: вводная', '1 мин', 'Создать вопрос: a или an?',
     [[B("Слайд 8. I've got…"), N(' a banana или an banana? a apple или an apple?')],
      [S('Как правильно? Напиши в чат: 1 — A или B, 2 — A или B.')]],
     'Ключ: 1 — A (a banana), 2 — B (an apple). Не объясняем, пока не увидим ответы чата.'),
    ('Правило', '2 мин', 'Понять, когда a, когда an.',
     [[B('Слайд 9. Правило.'), N(' Три пункта по клику.')],
      [S('A ставим перед согласным звуком. An — перед гласным: a, e, i, o, u.')],
      [S('Если предметов много — a и an не нужны.')]],
     'Произносим: an apple звучит слитно — «энэпл». Это и есть причина: так легче сказать.'),
    ('Проверка понимания', '2 мин', 'Убедиться, что правило понятно.',
     [[B('Слайд 10. Проверим!'), N(' Два вопроса да / нет.')],
      [S('Напиши в чат: 1 — A или B, 2 — A или B.')]],
     'Ключ: 1 — A (да), 2 — B (нет).'),
    ('Controlled practice', '7 мин', 'Выбирать a / an / — в предложении.',
     [[B('Слайды 11–18.'), N(' Одно предложение на слайд. Клик 1 — полоса «подумай» (10 с), клик 2 — ответ.')],
      [N('11 выбери · 12 раскрой скобки · 13 найди ошибку · 14 один или много · 15 вопрос · '
         '16 отрицание · 17 что на картинке · 18 ошибка в вопросе')],
      [S('Подумай 10 секунд и напиши букву в чат!')]],
     'Ключ: 11 B (an orange) · 12 a pear · 13 B (an → a) · 14 C (apples) · 15 B (an egg) · '
     '16 C (a sandwich) · 17 C · 18 A.'),
    ('⭐ If time', '0–3 мин', 'Шаг сложнее: прилагательное, выбор по звуку, порядок слов.',
     [[B('Слайды 19–21.'), N(' Большой апельсин · Найди лишнее · Собери предложение.')],
      [S('Смотрите на слово сразу после a или an.')]],
     'Делаем, только если на дриллинге отвечали легко и идём с опережением; иначе — сразу к слайду 22. '
     "Ключ: 19 A (a big orange) · 20 B (egg) · 21 I've got an apple."),
    ('Freer practice', '3 мин', 'Сказать о себе, используя a / an.',
     [[B('Слайд 22. Мой ланч-бокс.'), N(' Шесть картинок с подписями и образец.')],
      [S('Что у тебя в ланч-боксе? Напиши 2–3 предложения.')], [S("For example: I've got an apple.")]],
     'Читаем вслух ответы, хвалим за верный артикль; ошибку исправляем мягко, повтором верной формы.'),
    ('Feedback', '1 мин', 'Подвести итог, получить оценку, выдать самостоятельную.',
     [[B('Слайды 23–24. I CAN · Well done!')],
      [S('Отправьте ✅ за то, что получается. Поставьте уроку звёзды от 1 до 5!')]],
     'После урока — разослать самостоятельную (PPTX / PDF).'),
]
tot = sum(int(r[1].split()[0].split('–')[-1]) if not r[1].startswith('0') else 0 for r in rows)

t = doc.add_table(rows=1, cols=5)
t.style = 'Table Grid'
t.autofit = False
widths = [Cm(3.3), Cm(1.7), Cm(5.2), Cm(10.6), Cm(6.3)]
for k, h in enumerate(['Этап', 'Время', 'Цель', 'Задание', 'Комментарий']):
    c = t.rows[0].cells[k]; c.width = widths[k]; shade(c, PINK)
    c.paragraphs[0]._element.getparent().remove(c.paragraphs[0]._element)
    para(c, [(h, 'FFFFFF', True, False)])
for k, (stage, tm, goal, task, com) in enumerate(rows):
    cells = t.add_row().cells
    for j, c in enumerate(cells):
        c.width = widths[j]
        c.paragraphs[0]._element.getparent().remove(c.paragraphs[0]._element)
        if k % 2: shade(c, 'F7F3FF')
    para(cells[0], [(stage, HEAD, True, False)])
    para(cells[1], [N(tm)])
    para(cells[2], [N(goal)])
    for line in task:
        para(cells[3], line)
    para(cells[4], [N(com)])
para(doc, [('', GREY, False, False)])
para(doc, [(f'Итого: {tot} минут без ⭐. ', HEAD, True, False),
           ('⭐ берём из запаса, если группа идёт быстрее.', GREY, False, False)])
for k, gc in enumerate(t._tbl.tblGrid.findall(qn('w:gridCol'))):
    gc.set(qn('w:w'), str(int(widths[k].twips)))
doc.save(OUT)
print(OUT, 'итого', tot)
