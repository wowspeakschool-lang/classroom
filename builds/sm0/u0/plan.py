# -*- coding: utf-8 -*-
"""План урока «Unit 0 · Say Hello! — Lesson 6 (Revision + Test)» в Word.

    python3.13 builds/sm0/u0/plan.py <куда-положить.docx>

Формат повторяет действующие планы SM0: шапка, таблица из восьми колонок,
ядро 30 минут, пометки ⏱ +40 мин и Class Dojo, блок обратной связи с
родителями в конце (как в Unit 1 Lesson 7).
"""
import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = sys.argv[1]
doc = Document()

sec = doc.sections[0]
sec.orientation = WD_ORIENT.LANDSCAPE
sec.page_width, sec.page_height = sec.page_height, sec.page_width
for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'):
    setattr(sec, m, Cm(1.2))

st = doc.styles['Normal']
st.font.name = 'Calibri'
st.font.size = Pt(9)


def para(text, *, size=9, bold=False, italic=False, align=None, space_after=4,
         color=None):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color:
        r.font.color.rgb = color
    return p


def cell_text(cell, text, *, size=8, bold=False):
    cell.text = ''
    for i, line in enumerate(text.split('\n')):
        p = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(line)
        r.font.size = Pt(size)
        r.bold = bold


para('Unit 0 · Say Hello! — Lesson 6 (Revision + Test)', size=18, bold=True)
para('Super Minds Starter (2ed) · поурочный план · формат SM2 · v3',
     size=10, italic=True, space_after=10)

head = doc.add_table(rows=4, cols=2)
head.style = 'Table Grid'
for i, (k, v) in enumerate([
    ('Тип урока', 'Revision + Test'),
    ('Лексика / грамматика',
     'Повторение Unit 0: Hello! · What’s your name? — I’m… · How are you? · '
     'цвета (red, green, blue, orange, pink, yellow) · числа 1–10'),
    ('Фоника', 'повторение: s a t p i n e d r k'),
    ('Подготовка ученика',
     'Лист/тетрадь + карандаш; тест на платформе настроен заранее '
     '(сообщить родителям ДО урока)'),
]):
    cell_text(head.rows[i].cells[0], k, size=9, bold=True)
    cell_text(head.rows[i].cells[1], v, size=9)
head.columns[0].width = Cm(5.0)
head.columns[1].width = Cm(22.0)

para('')
para('Ход урока — ядро 30 мин (повторение юнита + тест на платформе; '
     'БЕЗ новой фоники и БЕЗ free practice)', size=10, bold=True)
para('Слайд 1 — титул урока (в плане не этап); этапы — со слайда 2. '
     'Обе игры собраны прямо в презентации: ребёнок кликает по картинке, '
     'слайд сам открывает ответ и возвращается назад. Wordwall не нужен.',
     size=9, italic=True, space_after=8)

COLS = ['Этап', 'Время', 'Aim', 'Задание (ресурс)', 'Ход урока (individual)',
        'Адаптация для групп', 'Комментарий методиста', 'Слайд']
WIDTHS = [3.2, 1.3, 3.2, 3.0, 8.4, 4.4, 3.6, 1.3]

ROWS = [
    ('1 · Greeting', '2 мин', 'How are you? then Hello.', 'Слайд 2',
     'T: "(wave) How are you? I’m happy!" (TPR)\n'
     'S: I’m happy / sad / angry.\n'
     'T: "Say: Hello!"\nS: Hello!',
     'Ученик→ученик по кругу: S1 «How are you?» → S2 отвечает → дальше.',
     '💡 How are you? — целым чанком, по словам не разбираем.', '2'),

    ('2 · Warm-up reading — повтор юнита', '2 мин',
     'Read cumulative words independently.', 'Слайд 3',
     'T: "Read!"\nS: sat… pin… ten… red… kit… dad… rat… pen (читает САМ)\n'
     'T: "Great! Faster!"\n'
     '⏱ +40 мин: чтение на время — побить рекорд.\n'
     '🏅 Class Dojo: +1 балл за самостоятельное чтение.',
     'Хором 1-я строка → дальше по одному слову; сосед проверяет 👍.',
     '💡 Слова на все буквы юнита: s a t p i n e d r k.', '3'),

    ('3 · HW check', '1 мин', 'Check the previous homework.', 'Слайд 4',
     'Не забудьте перед уроком проверить домашнее задание.\n'
     'Выполнено → T: «Молодец!» (+ что именно получилось).\n'
     'Не выполнено → напомнить, как важно его делать.',
     'По кругу: каждый коротко показывает/говорит своё ДЗ.', '—', '4'),

    ('Lead-in — переход к повторению', '—', 'Set up revision + test.', 'No slide',
     '(RU) «Сегодня мы заканчиваем наш самый первый юнит — тебя ждёт '
     'небольшой тест. Но сначала всё повторим!»', '—', '', '—'),

    ('4 · Revision — Hello / цвета / числа', '6 мин',
     'Recycle greetings, colours and numbers in a game.',
     'Игра «Поймай цвет» и «How many?» в презентации',
     'T: "What’s your name?" / S: I’m (Sasha).\n'
     'T: "How are you?" / S: I’m happy!\n'
     'Игра «Поймай цвет» (слайд 5): T: "Click red!" — ребёнок кликает шар, '
     'слайд открывает название цвета, кнопка «↩ назад» возвращает на поле. '
     '5–6 цветов вразнобой.\n'
     '«How many?» (слайды 12–17): на экране 4 красных шара — S: "Four!", '
     'клик «Проверить» показывает ответ. Три круга.\n'
     '🏅 Class Dojo: +1 балл за быстрые верные ответы.',
     'Кликает по очереди один, остальные отвечают хором; '
     'в «How many?» считаем хором, называет — один.',
     '💡 Цвет называем только по-английски; русского в игре нет.', '5–17'),

    ('5 · Revision — чтение', '4 мин',
     'Revise reading with cumulative real words.',
     'Игра «Кубик и чтение» в презентации',
     'T: "Let’s play! Roll the dice!"\n'
     'Ребёнок кликает кубик (слайд 18) — открывается слово под выпавшим '
     'номером: sat · pin · ten · red · kit · dad.\n'
     'S: (читает САМ) — «🎲 ещё раз» крутит дальше, «↩ к словам» '
     'возвращает на поле.\n'
     '🏅 Class Dojo: +1 балл за каждое прочитанное слово.',
     'По очереди бросают кубик и читают; группа хором подтверждает.',
     '💡 Кубик идёт по кругу 1→6, порядок слов не важен. '
     'Имя буквы не называем — только звук.', '18–24'),

    ('6 · Test — на платформе', '10 мин',
     'Unit 0 test (auto-checked + два устных задания).',
     '🔴 Тест на платформе · слайд 25',
     '(RU) Запустите тест. Ребёнок выполняет самостоятельно; учитель '
     'поддерживает, но не называет правильные ответы.\n'
     'T: "Now a little test! You can do it! 💪"\n'
     'S: (проходит тест)\n'
     '⏱ +40 мин: разобрать после теста то, что не получилось.',
     'Каждый проходит тест индивидуально (по своей ссылке / по очереди).',
     '💡 Тест — без подсказок, это диагностика. Хвалим за старание, '
     'не только за результат. В тесте два задания с микрофоном: '
     'запись проверяет методист, итоговый балл появится после проверки.', '25'),

    ('7 · I CAN — итоги Unit 0', '2 мин', 'Recap the whole unit (in Russian).',
     'Слайд 26',
     '(RU) «Ты прошёл весь первый юнит! Умеешь здороваться и знакомиться, '
     'знаешь шесть цветов, считаешь до десяти и сам читаешь слова с буквами '
     's a t p i n e d r k. И тест прошёл — молодец! 🎉»',
     'Каждый говорит, что узнал за юнит (по очереди).', '—', '26'),

    ('8 · Assign HW', '1 мин', 'Remind: set homework.', 'Слайд 27',
     '(RU) NO HW — юнит закончен.', 'Так же для группы.', '—', '27'),

    ('9 · Finishing the lesson', '2 мин',
     'Wrap up; two-way feedback; rate the lesson.', 'Слайд 28',
     '🏅 Class Dojo: выдайте баллы и проговорите, за что (повторение, '
     'старание в тесте, активная работа).\n'
     'Обратная связь ученику: итоги юнита — что получилось хорошо '
     '+ мягко над чем поработать.\n'
     'Сбор ОС от ученика: что понравилось, что было лёгким/трудным '
     '(трудно — это нормально).\n'
     'Rate the lesson — 5 звёзд на слайде. Bye-bye!',
     'Каждый даёт короткую ОС по очереди; баллы Dojo — индивидуально.',
     '—', '28'),

    ('⏱ If time — запас', 'запас', 'Добрать время играми.', 'Слайды 29–31',
     '1) Reading race ⏱ (слайд 29) — кто быстрее и без ошибок прочитает '
     'строку слов.\n'
     '2) Find & read 🔍 (слайд 30) — учитель называет слово, ребёнок находит '
     'его на слайде и читает.\n'
     '3) Colour bingo 🎯 (слайд 31) — учитель называет цвета подряд, '
     'ребёнок отмечает свои.',
     'Race — командами на скорость; Find & read — один ищет, группа '
     'подсказывает.', '—', '29–31'),
]

tbl = doc.add_table(rows=1 + len(ROWS), cols=len(COLS))
tbl.style = 'Table Grid'
tbl.autofit = False
for i, c in enumerate(COLS):
    cell_text(tbl.rows[0].cells[i], c, size=8, bold=True)
for r, row in enumerate(ROWS, start=1):
    for i, v in enumerate(row):
        cell_text(tbl.rows[r].cells[i], v, size=8)
for row in tbl.rows:
    for i, w in enumerate(WIDTHS):
        row.cells[i].width = Cm(w)

para('')
para('⚠️ Обратная связь с родителями (по результатам периода)', size=11, bold=True,
     color=RGBColor(0xC0, 0x00, 0x00))
para('Если по графику на этот урок запланирована ОС с родителями — порядок '
     'тот же, что в Unit 1 Lesson 7: начинайте за 10 минут до конца урока, '
     'покажите результаты ребёнка и пройденное, хвалите, соберите вопросы и '
     'пожелания, напомните про РК, МК, ЧК. Если родителя на уроке нет — '
     'впишите результаты теста (особенно устные задания) в МК, заполните '
     'форму с результатами и напишите родителю.', size=9)

doc.save(OUT)
print('план сохранён:', OUT)
