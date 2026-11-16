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
    ('Блок школы + тема', '3 мин', 'Познакомиться, назвать цель урока.',
     [[B('Слайд 1.'), N(' Приветствие, рассказ о школе WOW Speak.')],
      [S('Hello! Welcome to WOW Speak!')],
      [B('Слайд 2. Today we will learn.'), N(' Два пункта по клику: слова еды и a / an.')],
      [S('Сегодня мы выучим слова про еду и узнаем, когда говорят a, а когда an.')]],
     'Пока дети подключаются — здороваемся по именам из чата.'),
    ('Warm-up', '2 мин', 'Разогреться на знакомых словах (цвета, числа, вещи).',
     [[B('Слайд 3. Odd one out.'), N(' Ряды появляются по одному: ряд → клик ответ → клик следующий ряд.')],
      [S('Which word is different? Type the letter.')]],
     'Ключ: 1 — C (cat), 2 — B (dog), 3 — D (sun).'),
    ('Lead-in', '2 мин', 'Ввести тему «еда».',
     [[B("Слайд 4. What's in my lunchbox?")],
      [S('Как думаете, что у меня в ланч-боксе? Пишите в чат — можно по-русски!')]],
     'Читаем 3–4 догадки, клик — открывается сэндвич.'),
    ('Лексика', '3 мин', 'Ввести 6 слов: apple, egg, orange, banana, pear, sandwich.',
     [[B('Слайд 5. Food.'), N(' Слова появляются по одному по клику.')],
      [S('Look! An apple.')], [S('Повторяйте за мной вслух, а в чат пишите слово.')]],
     'Называем каждое слово с артиклем (an apple, a banana) — дети слышат форму до правила.'),
    ('Игра на слова', '3 мин', 'Запомнить слова, узнавать их по картинке.',
     [[B('Слайд 6. Remember!'), N(' Клик — 15 секунд на запоминание.')],
      [B("Слайды 7–8. What's missing?"), N(' Два раунда.')],
      [S("What's missing? Type the word!")]],
     'Ключ: раунд 1 — pear, раунд 2 — egg. Клик открывает ответ.'),
    ('Грамматика: guided discovery', '3 мин', 'Дети сами замечают, когда an.',
     [[B('Слайд 9. Look and read.'), N(' Шесть предложений по одному по клику: It\'s a banana. It\'s an apple… '
        'a / an и первая буква слова выделены цветом.')],
      [S('Прочитайте вслух. Где a, а где an?')],
      [S('Посмотрите на первый звук после an: гласный или согласный? А после a?')],
      [N('Последний клик — вопрос «Why an? Why a?»: дети пишут догадки в чат.')]],
     'Правило не говорим сами — ждём, пока дети сформулируют: «an — когда слово начинается с гласного».'),
    ('Правило', '1 мин', 'Закрепить вывод детей.',
     [[B('Слайд 10. The rule.'), N(' Три пункта по клику.')],
      [S('Правильно! An — перед гласным звуком, a — перед согласным. Если предметов много — ничего не ставим.')]],
     'Произносим: an apple звучит слитно — так легче сказать.'),
    ('Проверка понимания', '1 мин', 'Убедиться, что правило понятно.',
     [[B('Слайд 11. Check.'), N(' Вопрос → ответ → следующий вопрос.')],
      [S('Type A or B.')]],
     'Ключ: 1 — A (Yes), 2 — B (No).'),
    ('Controlled practice', '7 мин', 'Выбирать a / an / — в предложении.',
     [[B('Слайды 12–19.'), N(' Одно предложение на слайд. Клик 1 — полоса «подумай» (10 с), клик 2 — ответ.')],
      [N('12 Choose · 13 a or an · 14 Find the mistake · 15 One or many · 16 Question · '
         '17 No! · 18 What is it? · 19 Ask correctly')],
      [S('Think for 10 seconds. Type A, B or C!')]],
     'Ключ: 12 B (an orange) · 13 a pear · 14 B (an → a) · 15 C (I like apples) · 16 B (an egg) · '
     '17 C (a sandwich) · 18 C · 19 A.'),
    ('⭐ If time', '0–3 мин', 'Шаг сложнее: прилагательное, выбор по звуку, порядок слов.',
     [[B('Слайды 20–22.'), N(' A big orange · Odd one out · Make a sentence.')],
      [S('Look at the next word!')]],
     'Делаем, только если на дриллинге отвечали легко и идём с опережением; иначе — сразу к слайду 23. '
     "Ключ: 20 A (a big orange) · 21 B (egg) · 22 I've got an apple."),
    ('Freer practice', '3 мин', 'Сказать о себе, используя a / an.',
     [[B('Слайд 23. My lunchbox.'), N(' Шесть картинок с подписями и образец.')],
      [S("What's in your lunchbox? Write 2–3 sentences.")]],
     'Читаем вслух ответы, хвалим за верный артикль; ошибку исправляем мягко, повтором верной формы.'),
    ('Feedback', '2 мин', 'Подвести итог, получить оценку, выдать самостоятельную.',
     [[B('Слайды 24–25. I CAN · Well done!')],
      [S('Send ✅ for every “I can”. Rate the lesson: 1 to 5 stars!')]],
     'После урока — разослать самостоятельную (PPTX / PDF): слова, правило, три упражнения с ответами.'),
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
