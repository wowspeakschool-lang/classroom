# -*- coding: utf-8 -*-
"""Один общий документ «Что нужно от вас» — SM0, SM3, GG3, нулевые юниты.

    python3.13 builds/todo_all.py "builds/Что нужно от вас.docx"

Заменяет три отдельных файла (builds/sm0/u0, builds/sm3/u0, builds/gg3/u0):
методист держит открытым один документ. Порядок разделов — по регламенту:
вопросы наверху, потом общий список действий, потом подробности по курсам и
тексты, которые нужно начитать.
"""
import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

INK   = RGBColor(0x1F, 0x29, 0x37)
HEADC = RGBColor(0x14, 0x3A, 0x6B)
ACC   = RGBColor(0xB1, 0x3E, 0x0F)
MUTED = RGBColor(0x5A, 0x63, 0x72)
HEAD_FILL = '1F3A6B'
Q_FILL    = '8C2B12'       # шапка таблицы вопросов — красная
SOFT_FILL = 'F3F7FC'
GRID      = 'C9D4E4'

OUT = sys.argv[1] if len(sys.argv) > 1 else 'builds/Что нужно от вас.docx'
doc = Document()
s = doc.sections[0]
s.left_margin = s.right_margin = Cm(1.6)
s.top_margin = s.bottom_margin = Cm(1.5)
doc.styles['Normal'].font.name = 'Calibri'
doc.styles['Normal'].font.size = Pt(10)
doc.styles['Normal'].font.color.rgb = INK
WIDTH = 17.9                                  # полезная ширина страницы, см


def para(text='', *, size=10, bold=False, italic=False, colour=None, after=6,
         before=0):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.space_before = Pt(before)
    if text:
        r = p.add_run(text)
        r.font.size = Pt(size); r.bold = bold; r.italic = italic
        r.font.color.rgb = colour or INK
    return p


def head(text, *, size=13, colour=None, after=5, before=12):
    return para(text, size=size, bold=True, colour=colour or HEADC,
                after=after, before=before)


def shade(cell, fill):
    tc = cell._tc.get_or_add_tcPr()
    el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto')
    el.set(qn('w:fill'), fill)
    tc.append(el)


def grid(table):
    borders = OxmlElement('w:tblBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement(f'w:{edge}')
        el.set(qn('w:val'), 'single'); el.set(qn('w:sz'), '4')
        el.set(qn('w:space'), '0'); el.set(qn('w:color'), GRID)
        borders.append(el)
    table._tbl.tblPr.append(borders)


def fixed_widths(table, cms):
    layout = OxmlElement('w:tblLayout')
    layout.set(qn('w:type'), 'fixed')
    table._tbl.tblPr.append(layout)
    gridel = table._tbl.find(qn('w:tblGrid'))
    for gc, cm in zip(gridel.findall(qn('w:gridCol')), cms):
        gc.set(qn('w:w'), str(int(cm * 567)))
    for row in table.rows:
        for c, cm in zip(row.cells, cms):
            c.width = Cm(cm)


def cell_margins(table):
    el = OxmlElement('w:tblCellMar')
    for side, val in (('top', 70), ('left', 100), ('bottom', 70), ('right', 100)):
        node = OxmlElement(f'w:{side}')
        node.set(qn('w:w'), str(val)); node.set(qn('w:type'), 'dxa')
        el.append(node)
    table._tbl.tblPr.append(el)


def table(headers, rows, widths, *, fill=HEAD_FILL, first_bold=True, size=9.5):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    grid(t); cell_margins(t)
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]; shade(c, fill); c.text = ''
        p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h); r.bold = True; r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    for ri, row in enumerate(rows, start=1):
        for ci, val in enumerate(row):
            c = t.rows[ri].cells[ci]; c.text = ''
            if ci == 0:
                shade(c, SOFT_FILL)
            for li, line in enumerate(str(val).split('\n')):
                p = c.paragraphs[0] if li == 0 else c.add_paragraph()
                p.paragraph_format.space_after = Pt(1)
                r = p.add_run(line); r.font.size = Pt(size)
                if ci == 0 and first_bold:
                    r.bold = True; r.font.color.rgb = HEADC
                elif ci == len(headers) - 1:
                    r.font.color.rgb = MUTED
                else:
                    r.font.color.rgb = INK
    fixed_widths(t, widths)
    return t


def quote(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(10)
    p.paragraph_format.left_indent = Cm(0.6)
    r = p.add_run(text); r.font.size = Pt(11)
    return p


# ─────────────────────────────── шапка ────────────────────────────────────
para('Что нужно от вас', size=20, bold=True, colour=HEADC, after=2)
para('Нулевые юниты трёх курсов: SM0 (Super Minds Starter), SM3 (Super Minds 3), '
     'GG3 (Get Great 3). Обновлено 18.10.',
     size=9.5, italic=True, colour=MUTED, after=3)
para('В базу ничего не залито: платформа переезжает на WowSpeak Team, и всё, что '
     'попадёт в старую базу, потеряется вместе с ней. Пока всё лежит файлами — '
     'SQL для домашек и тестов, Word для планов, PowerPoint для презентации.',
     size=9.5, italic=True, colour=MUTED, after=10)

# ───────────────────────── вопросы и решения ──────────────────────────────
head('🟥 Вопросы и решения', colour=ACC, before=2)
para('Отвечать можно прямо в этом файле — я заберу ответы отсюда.',
     size=9, italic=True, colour=MUTED, after=5)
table(['№', 'Вопрос', 'Что будет, если не ответить'],
      [['1', 'GG3: сгенерировать пять картинок для диктанта\n'
             'Промпт на лист прислан в чат: bus, taxi, train, motorbike, plane',
        'Диктант в тесте GG3 останется на слух. В SM3 он уже переделан: '
        'картинка → слово, картинки были'],
       ['2', 'Куда переехали и где теперь редактор',
        'Ничего нельзя залить: ни ДЗ, ни тесты. Всё лежит файлами в '
        'репозитории и ждёт адреса'],
       ['3', 'SM0: менять ли старые картинки цветов на новые шарики',
        'В тесте и в домашках 2–5 цвета останутся картинками из выгрузки '
        '92×150 — на вариантах ответа они мылятся. Новые шарики готовы '
        '(media/sm0/u0). Договорились смотреть при вычитке SM0'],
       ['4', 'SM0, ДЗ 2 юнита 0, блок 7',
        '«Послушай цвет и выбери его», а варианты — русские слова. Это '
        'задание на перевод, которых мы не делаем. Останется как есть, '
        'пока не решим, на что менять'],
       ['5', 'SM0: что перерисовываем по всему курсу',
        '128 картинок из 150 меньше 300 px по большей стороне. Без решения '
        'не соберу промпты листами — а генерировать удобнее за один присест']],
      [1.0, 6.4, 10.5], fill=Q_FILL)

# ──────────────────────── общий список действий ───────────────────────────
head('Весь список — что сделать руками')
table(['№', 'Курс', 'Что', 'Где', 'Без этого'],
      [['1', 'SM0', 'Записать звук /s/ и /æ/ — звук, а не имя буквы',
        'ДЗ 1, блок 2, вопросы 1 и 2 (поле audio пустое)',
        'Ребёнку нечего слушать'],
       ['2', 'SM3', 'Начитать текст аудирования',
        'Тест, блок 16. Текст — ниже в этом файле',
        'Пять вопросов после рассказа не решаются'],
       ['3', 'GG3', 'Начитать текст аудирования',
        'Тест, блок 17. Текст — ниже в этом файле',
        'То же: слушать нечего'],
       ['4', 'все три', 'Нажать «Озвучить пачкой»',
        'SM0: ДЗ 1 блоки 4–6 и тест блок 6. SM3: ДЗ 1–4 и тест. GG3: тест.\n'
        'Блок аудирования и диктант SM3 кнопка не тронет — там audio_tts '
        'нет специально',
        'Вопросы на слух без звука'],
       ['5', 'SM0', 'Прокликать игры в презентации Lesson 6',
        'PowerPoint на компьютере: слайд 5 — шарики, слайд 18 — карточки',
        'Не увидим, если переход ведёт не туда'],
       ['6', 'SM0', 'Вставить ссылку на тест в презентацию',
        'Слайд 25, плашка «paste the test link here»',
        'Учитель не запустит тест с урока'],
       ['7', 'SM3', 'Вставить ссылку на тест в план урока 5',
        'Unit 0 Lesson 5.docx, этап Test',
        'То же для SM3'],
       ['8', 'SM0, SM3', 'Разложить планы и презентацию туда, где '
        'преподаватели их берут',
        'SM0: Unit 0 Lesson 6.docx + .pptx. SM3: Unit 0 Lesson 1–5.docx',
        'Учителю нечего открыть на уроке'],
       ['9', 'все три', 'Посмотреть глазами домашки и тесты после заливки',
        'На новом месте',
        'Ошибку найдёт ученик, а не мы'],
       ['10', 'все три', 'Включить публикацию',
        'Все уроки залиты с is_published = false',
        'Уроки не видны ученикам']],
      [0.9, 1.9, 4.4, 5.6, 5.1])

# ───────────────────────── тексты для записи ──────────────────────────────
head('Тексты для записи')
para('Три записи. Присылайте файлы с такими именами — имя само говорит, в какой '
     'блок их вставить, остальное сделаю я.', size=9, italic=True, colour=MUTED,
     after=6)

para('1. SM3, тест, блок 16 — файл sm3_u0_test_b16.mp3', size=10, bold=True,
     colour=HEADC, after=3)
para('Читать спокойно, один раз: ученик сам слушает запись дважды. Текста на '
     'экране нет, поэтому рассказ идёт от третьего лица.', size=9, italic=True,
     colour=MUTED, after=4)
quote('This is Penny. Penny is seven years old. She lives with her mum Claire, '
      'her dad Ted and her brother Nick. Penny’s bedroom is upstairs. Penny is '
      'good at dancing and she is good at telling stories, but she isn’t good '
      'at swimming. Her grandmother Julia is good at making cakes. Penny has '
      'got twenty-four books in her room.')

para('2. GG3, тест, блок 17 — файл gg3_u0_test_b17.mp3', size=10, bold=True,
     colour=HEADC, after=3)
quote('This is Emma. Emma is thirteen years old. She lives with her mum and her '
      'gran Bertie. Emma usually goes to school by bike, but when it rains her '
      'mum drives her. Emma is good at dancing and she has got dance classes '
      'twice a week. This year she is going to study Geography more. Emma is '
      'scared of spiders. Her favourite food is pancakes: her gran always makes '
      'pancakes for breakfast on Sunday.')

para('3. SM0, ДЗ 1, блок 2 — файлы sm0_u0_hw1_b2_s.mp3 и sm0_u0_hw1_b2_a.mp3',
     size=10, bold=True, colour=HEADC, after=3)
para('Нужен звук, а не имя буквы: /s/ как в «snake» и /æ/ как в «apple». '
     'Фразы урока (Hello! · What’s your name? · How are you? · I’m Misty) '
     'записывать не нужно — они идут синтезом, ваше решение от 17.10.',
     size=9, italic=True, colour=MUTED, after=10)

# ─────────────────────── подробности по курсам ────────────────────────────
head('Что в каждом курсе готово')
table(['Курс', 'Файлы', 'Что заливается в базу'],
      [['SM0\nюнит 0',
        'Unit 0 Lesson 6.docx — план урока «Revision + Test»\n'
        'Unit 0 Lesson 6.pptx — презентация, 31 слайд, две игры внутри\n'
        'u0_hw1.sql, u0_test.sql',
        'ДЗ 1 — восстановленная: Hello! · What’s your name? — I’m… · буквы S и A.\n'
        'Тест юнита — 14 блоков, порог 90, звук переиспользован из домашек 2–5.\n'
        'Чужую «Homework 1» юнита 0 не переносим вовсе: это копия ДЗ 4 юнита 1, '
        'на её место встаёт восстановленная ДЗ 1 (ваше решение от 17.10).\n'
        'План и презентация в базу не идут — это файлы для преподавателей'],
       ['SM3\nюнит 0',
        'Unit 0 Lesson 1–5.docx — пять планов\n'
        'u0_hw1.sql … u0_hw4.sql, u0_test.sql',
        'Юнита 0 в базе нет — SQL заводит его сам: «Unit 0 · Meet The Explorers».\n'
        'Четыре домашки (порог 60) и тест пятым уроком (20 блоков, порог 90, '
        'внутри reading, listening и диктант).\n'
        'Картинки уже в репозитории: шесть действий для be good at, три дома '
        'в разрезе, семейное дерево, восемь кадров истории.\n'
        'Презентаций в SM3 нет — урок идёт по учебнику и вашим ссылкам Wordwall'],
       ['GG3\nюнит 0',
        'u0_test.sql',
        'Юнит «Unit 0» и урок «Unit 0 Test» SQL заводит сам: 21 блок по '
        'страницам 4–9 — Present Simple и наречия частотности, город и '
        'транспорт, профессии и вопросительные слова, be going to и школа, '
        'прилагательные с предлогами, еда с some/any и контейнеры, плюс '
        'reading, listening и диктант.\n'
        'Картинок нет: материал страниц целиком текстовый.\n'
        'Домашек и планов в GG3 нет по вашему решению']],
      [2.2, 5.6, 10.1], first_bold=True)

head('Уже решено — чтобы не возвращаться')
for line in (
    'Озвучка остаётся на нашем сервере (Piper), на Яндекс не переходим.',
    'Аудирование — рассказ от третьего лица, без диалогов: английский голос '
    'в синтезе один, реплики диалога не различаются.',
    'Аудирование начитываете вы, синтезом его не озвучиваем: в этих блоках '
    'разметки audio_tts нет, кнопка их не тронет.',
    'Игры в SM0 — внутри презентации, без Wordwall. Инструкции на слайдах '
    'только по-английски.',
    'SM3: в каждом уроке speaking task; лексика — картинками и флеш-карточками; '
    'грамматика — guided discovery с CCQ, без объяснений по-русски.',
    'Диктант — не на слух: ученик видит картинку и пишет слово. Пять слов из '
    'целевой лексики первого урока (SM3: upstairs, downstairs, cellar и два '
    'числа; GG3: транспорт со страниц 4–5, ждём картинки).',
    'Все уроки заливаются с is_published = false — публикацию включаете вы.',
):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(line); r.font.size = Pt(9.5); r.font.color.rgb = INK

doc.save(OUT)
print('документ сохранён:', OUT)
