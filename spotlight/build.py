# -*- coding: utf-8 -*-
"""Собирает Spotlight_грамматика.xlsx из out/*.json (+ full.json — полный объём тем)."""
import json, glob, os, re, sys
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

D = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, 'Spotlight_грамматика.xlsx')

CATS = ["Глаголы: времена", "Глаголы: to be / have got / модальные", "Глаголы: другое",
        "Существительные и артикли", "Местоимения", "Прилагательные и наречия", "Числительные",
        "Предлоги", "Предложение и вопросы", "Словообразование", "Фразовые глаголы",
        "Зависимые предлоги и устойчивые сочетания"]
LEX = {"Словообразование", "Фразовые глаголы", "Зависимые предлоги и устойчивые сочетания"}

rows = []
for f in sorted(glob.glob(os.path.join(D, 'data', 'g*.json'))):
    rows += json.load(open(f))
for r in rows:
    for k in ('module', 'lesson', 'category', 'topic', 'scope', 'example', 'comment', 'source'):
        r[k] = (r.get(k) or '').strip()
    r['grade'] = int(r['grade'])
    if r['category'] not in CATS:
        r['category'] = 'Глаголы: другое' if 'Глагол' in r['category'] else r['category']


ALIAS = {
    'Modal verbs (criticism)': 'Modal verbs (functions)', 'Modal verbs (criticism, offers, probability)': 'Modal verbs (functions)',
    'Modal verbs (general)': 'Modal verbs (functions)', 'Modal verbs (offers/suggestions)': 'Modal verbs (functions)',
    'Modal verbs (revision)': 'Modal verbs (functions)', 'Modal verbs (overview)': 'Modal verbs (functions)',
    'Modal verbs (probability)': 'Modal verbs (deduction)',
    'Past Perfect / Past Perfect Continuous': 'Past Perfect',
    'Present Perfect (have gone to / have been to / have been in)': 'have gone to / have been to / have been in',
    'Irregular verbs': 'Irregular verbs (list)',
    'Expressing preference': 'Expressing preference (prefer / would rather)',
    'Infinitive (to / bare)': 'Infinitive / -ing form',
    'Infinitive vs -ing (difference in meaning)': 'Infinitive / -ing form (difference in meaning)',
    'Reported Speech (introductory verbs)': 'Reporting verbs', 'Reporting verbs (special introductory verbs)': 'Reporting verbs',
    'Reported Speech (orders, requests, suggestions)': 'Reported commands/requests',
    'Modal verbs in Reported Speech': 'Reported Speech: modal verbs',
    'Reported questions / Indirect questions': 'Reported questions',
    'used to / be used to / get used to': 'be/get used to',
    'Determiners (every / each)': 'Determiners (every/each)',
    'Conditional linkers': 'Conditional linkers (unless, provided…)',
    'Conditionals: linking words & inversion': 'Conditional linkers (unless, provided…)',
    'It-sentences (impersonal it)': 'Impersonal it',
    'Adjectives & adverbs in descriptions': 'Adjectives & adverbs in writing', 'Adjectives (descriptive)': 'Adjectives & adverbs in writing',
    'Adjectives and adverbs (narrative)': 'Adjectives & adverbs in writing',
    'Types of comparison': 'Comparative structures',
    'Reported Speech (commands, requests, suggestions)': 'Reported commands/requests',
    'Reported Speech (modals)': 'Reported Speech: modal verbs',
    'Reported Speech (questions)': 'Reported questions',
    'Like (verb vs preposition)': 'Like / As',
    'Partitives (a bottle of, a packet of)': 'Partitives (a bottle of…)',
}
CATFIX = {
    'Stative verbs': 'Глаголы: времена', 'Irregular verbs (list)': 'Глаголы: другое',
    'have gone to / have been to / have been in': 'Глаголы: времена',
    'Demonstratives (this/that/these/those)': 'Местоимения',
    'Determiners (both/either/neither/all/none)': 'Местоимения', 'Determiners (every/each)': 'Местоимения',
    'Months': 'Числительные', 'Telling the time': 'Числительные',
}
for r in rows:
    r['topic'] = ALIAS.get(r['topic'], r['topic'])
    r['category'] = CATFIX.get(r['topic'], r['category'])

full = json.load(open(os.path.join(D, 'data', 'full.json'))) if os.path.exists(os.path.join(D, 'data', 'full.json')) else {}

def modnum(m):
    x = re.search(r'(\d+)', m)
    return (0 if 'starter' in m.lower() or "let's go" in m.lower() else 1, int(x.group(1)) if x else 0)

def lesnum(l):
    x = re.match(r'(\d+)([a-z]?)', l)
    return (int(x.group(1)), x.group(2)) if x else (99, l)

rows.sort(key=lambda r: (r['grade'], modnum(r['module']), lesnum(r['lesson'])))

grades = sorted({r['grade'] for r in rows})
thin = Side(style='thin', color='BBBBBB')
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
HEAD = PatternFill('solid', fgColor='2F5597')
CATFILL = PatternFill('solid', fgColor='DDEBF7')
LEXFILL = PatternFill('solid', fgColor='F2F2F2')
WRAP = Alignment(wrap_text=True, vertical='top')

def header(ws, cols, widths):
    ws.append(cols)
    for i, w in enumerate(widths, 1):
        c = ws.cell(row=1, column=i)
        c.font = Font(bold=True, color='FFFFFF'); c.fill = HEAD
        c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center'); c.border = BOX
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = 'A2' if len(cols) < 8 else 'C2'

def body(ws):
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = WRAP; c.border = BOX

wb = Workbook()

# --- Как читать
ws = wb.active; ws.title = 'Как читать'
info = [
    ['Грамматика Spotlight 3–11: что, где и в каком объёме'],
    [''],
    ['Лист «Сводка по темам» — общий список правил. Строка = тема, колонки = классы. В клетке класса — объём темы именно в этом классе и модуль(и). «Полный объём темы» — все формы и значения правила, справочно.'],
    ['Листы «3 класс» … «11 класс» — то же по учебнику: модуль → урок → тема → объём → пример → комментарий.'],
    ['Лист «Все строки» — все строки одной таблицей, с фильтрами.'],
    ['Лист «Use of English» — фразовые глаголы, словообразование, предлоги, words often confused по модулям.'],
    [''],
    ['Источники. Грамматика — только грамматический справочник в конце учебника (GR) и таблица неправильных глаголов. Урок (1a, 2c) — по оглавлению (ToC). Use of English — оглавление и приложения учебника (Appendix: фразовые глаголы, предлоги, идиомы). Word List не используется.'],
    ['2 класса нет: в учебнике нет грамматического справочника. В 3–4 и 7 классах справочник разбит только по модулям, поэтому урок не указан.'],
    ['«в доступных страницах только заголовок из оглавления» — тема Use of English названа в оглавлении, а самих страниц урока в файлах нет.'],
    ['«проверить: …» — неразборчивый скан/распознанный текст или неуверенный номер урока.'],
]
for line in info:
    ws.append(line)
ws['A1'].font = Font(bold=True, size=14)
ws.column_dimensions['A'].width = 140
for row in ws.iter_rows(min_row=2):
    row[0].alignment = Alignment(wrap_text=True)

# --- Сводка по темам
ws = wb.create_sheet('Сводка по темам')
gcols = [f'{g} кл.' for g in grades]
header(ws, ['Категория', 'Тема', 'Впервые', 'Полный объём темы (все формы и значения, справочно)'] + gcols,
       [18, 26, 9, 48] + [34] * len(grades))
by = {}
for r in rows:
    if r['category'] in LEX:
        continue
    by.setdefault((r['category'], r['topic']), []).append(r)
def catkey(k):
    return (CATS.index(k[0]) if k[0] in CATS else 99, min(r['grade'] for r in by[k]), k[1])
for k in sorted(by, key=catkey):
    rs = by[k]
    cells = []
    for g in grades:
        parts = []
        for r in rs:
            if r['grade'] != g:
                continue
            where = r['module'].split('·')[0].strip() + (f" ({r['lesson']})" if r['lesson'] else '')
            parts.append(f"{where}: {r['scope']}")
        cells.append('\n'.join(parts))
    ws.append([k[0], k[1], f"{min(r['grade'] for r in rs)} кл.", full.get(k[1], '')] + cells)
body(ws)
for row in ws.iter_rows(min_row=2):
    row[1].font = Font(bold=True)
    for c in row[4:]:
        if c.value:
            c.fill = CATFILL
ws.auto_filter.ref = ws.dimensions

COLS = ['Класс', 'Модуль', 'Урок', 'Категория', 'Тема', 'Объём в этом месте', 'Пример', 'Комментарий', 'Источник']
W = [7, 26, 7, 20, 26, 60, 32, 44, 11]
def put(ws, rs):
    header(ws, COLS, W)
    for r in rs:
        ws.append([r['grade'], r['module'], r['lesson'], r['category'], r['topic'],
                   r['scope'], r['example'], r['comment'], r['source']])
    body(ws)
    for i, r in enumerate(rs, 2):
        ws.cell(row=i, column=5).font = Font(bold=True)
        if r['category'] in LEX:
            for c in ws[i]:
                c.fill = LEXFILL
    ws.auto_filter.ref = ws.dimensions

put(wb.create_sheet('Все строки'), rows)
lex = [r for r in rows if r['category'] in LEX]
put(wb.create_sheet('Use of English'), lex)
for g in grades:
    put(wb.create_sheet(f'{g} класс'), [r for r in rows if r['grade'] == g])

wb.save(OUT)
print(OUT, len(rows), 'rows;', len(by), 'topics;', 'grades', grades)
missing = sorted({k[1] for k in by} - set(full))
if missing:
    print('нет полного объёма:', missing)
