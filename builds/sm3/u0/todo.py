# -*- coding: utf-8 -*-
"""Документ «Что нужно от вас — SM3, юнит 0».

    python3.13 builds/sm0/u0/todo.py "builds/sm0/u0/Что нужно от вас — SM0.docx"

Только открытые пункты: что сделать руками и что решить. Сделанное не перечисляем.
"""
import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = sys.argv[1]
doc = Document()
for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'):
    setattr(doc.sections[0], m, Cm(1.8))
doc.styles['Normal'].font.name = 'Calibri'
doc.styles['Normal'].font.size = Pt(11)


def para(text, *, size=11, bold=False, italic=False, color=None, after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text)
    r.font.size = Pt(size); r.bold = bold; r.italic = italic
    if color:
        r.font.color.rgb = color
    return p


def table(headers, rows, widths):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = 'Table Grid'
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]; c.text = ''
        r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(10)
    for ri, row in enumerate(rows, start=1):
        for ci, v in enumerate(row):
            c = t.rows[ri].cells[ci]; c.text = ''
            for li, line in enumerate(str(v).split('\n')):
                p = c.paragraphs[0] if li == 0 else c.add_paragraph()
                p.paragraph_format.space_after = Pt(1)
                rr = p.add_run(line); rr.font.size = Pt(10)
    for row in t.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Cm(w)
    return t


para('Что нужно от вас — SM3, юнит 0', size=18, bold=True, after=2)
para('Файлы: пять планов уроков (Word), четыре домашки и тест (SQL). Презентаций '
     'в SM3 нет. В базу ничего не залито — ждём переезда на WowSpeak Team.',
     size=10, italic=True, after=12)

para('Сделать руками', size=13, bold=True, after=4)
table(['№', 'Что', 'Где', 'Без этого'],
      [['1', 'Нажать «Озвучить пачкой»',
        'ДЗ 1–4 и тест: числа, предложения для «составь предложение», диктант — '
        'всё помечено audio_tts. Блок аудирования кнопка не тронет: там '
        'audio_tts нет специально',
        'Задания на слух не работают'],
       ['2', 'Записать аудирование своим голосом',
        'Тест, блок 16 (LISTENING). Текст для записи — ниже в этом файле. '
        'Файл назвать sm3_u0_test_b16.mp3 и прислать мне — вставлю в блок',
        'Ученику нечего слушать, пять вопросов после рассказа не решаются'],
       ['3', 'Вставить ссылку на тест в план урока 5',
        'Unit 0 Lesson 5.docx, этап Test',
        'Учитель не запустит тест с урока'],
       ['4', 'Разложить планы туда, где преподаватели их берут',
        'Unit 0 Lesson 1–5.docx',
        'Учителю нечего открыть'],
       ['5', 'Посмотреть глазами домашки и тест после заливки',
        'На новом месте',
        'Ошибку найдёт ученик, а не мы'],
       ['6', 'Включить публикацию',
        'ДЗ 1–4 и тест, после проверки',
        'Уроки не видны ученикам']],
      [1.0, 5.6, 5.6, 4.8])

para('')
para('Текст аудирования — для записи', size=13, bold=True, after=4)
para('Тест, блок 16. Читать спокойно, один раз; ученик слушает запись дважды '
     'сам. На экране текста нет.', size=10, italic=True, after=6)
para('This is Penny. Penny is seven years old. She lives with her mum Claire, '
     'her dad Ted and her brother Nick. Penny\u2019s bedroom is upstairs. Penny '
     'is good at dancing and she is good at telling stories, but she isn\u2019t '
     'good at swimming. Her grandmother Julia is good at making cakes. Penny has '
     'got twenty-four books in her room.', size=11, after=10)

para('')
para('Решено 18.10: speaking в уроке 4 остаётся после Phonics focus; семейное '
     'дерево оставляем как есть, задания под него подобраны.', size=9, italic=True)

doc.save(OUT)
print('документ сохранён:', OUT)
