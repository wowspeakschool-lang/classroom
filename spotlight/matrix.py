# -*- coding: utf-8 -*-
"""Планировщик уроков: Spotlight_темы_уроков.xlsx.

Строка — тема (будущая папка-урок), колонки — классы с модулями, где тема встречается,
и отметки о видео отдельно для двух возрастных групп вебинаров.
Отметки о видео живут в data/videos.json: {"<тема>": {"7–9": "ссылка или название", "10+": "..."}}.

    python3 spotlight/matrix.py
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.formatting.rule import CellIsRule
from openpyxl.worksheet.datavalidation import DataValidation
from build import D, CATS, LEX, load_rows, sort_rows, modnum, header, body, BOX, WRAP

OUT = os.path.join(D, 'Spotlight_темы_уроков.xlsx')

# 7–9 лет — 1–3 класс; Spotlight начинается со 2-го. С 4 класса (9–10 лет) — группа 10+.
JUNIOR = {2, 3}
GROUPS = ['7–9', '10+']
def group(g):
    return '7–9' if g in JUNIOR else '10+'

FILL = {'7–9': PatternFill('solid', fgColor='FCE4D6'), '10+': PatternFill('solid', fgColor='DDEBF7')}
GREY = PatternFill('solid', fgColor='EDEDED')
YES = PatternFill('solid', fgColor='C6EFCE')
NO = PatternFill('solid', fgColor='FFC7CE')

WF = [  # модели словообразования, когда в строке нет явных суффиксов
    ('national', 'national'), ('compound noun', 'compound nouns'), ('сложные существ', 'compound nouns'),
    ('compound adj', 'compound adjectives'), ('сложные прилаг', 'compound adjectives'),
    ('abstract', 'abstract nouns'), ('абстрактн', 'abstract nouns'),
    ('negative adj', 'negative adjectives'), ('отрицательных прилаг', 'negative adjectives'),
    ('nouns from adjectives', 'nouns from adjectives'), ('nouns from verbs', 'nouns from verbs'),
    ('verbs from', 'verbs from nouns/adjectives'), ('with prefixes', 'verbs with prefixes'),
    ('лиц', 'personal nouns'), ('приставки (toc', 'prefixes'), ('конверсия', 'conversion (a dress – to dress)'),
    ('revision', 'revision'), ('образование прилагательных (toc', 'forming adjectives'),
    ('образование глаголов (toc', 'forming verbs'),
]
AFFIX = re.compile(r'(?<![\w-])(-[a-z]+|[a-z]{1,3}-)(?![\w-])')


def lex_topic(r):
    s, t = r['scope'], r['topic']
    if t == 'Phrasal verbs':
        m = re.match(r'(\w+):', s) or re.search(r' с (\w+)', s) or re.match(r'(\w+) \+', s)
        return 'Use of English', 'Фразовые глаголы', f'Phrasal verbs: {m.group(1)}' if m else 'Phrasal verbs'
    if t == 'Word formation':
        low = s.lower()
        if 'national' in low or '-ese' in low:
            name = 'nationalities -an/-ish/-ian/-ese'
        elif 'participl' in low or ('-ed' in low and '-ing' in low and 'able' not in low):
            name = 'participle adjectives -ed/-ing'
        else:
            aff = [a for a in dict.fromkeys(AFFIX.findall(s)) if a not in ('-ing',) or '-able' in s]
            name = ', '.join(aff) if aff else next((n for k, n in WF if k in low), s[:40])
        return 'Use of English', 'Словообразование', f'Word formation: {name}'
    if t in ('Collocations / Fixed phrases',):
        return 'Use of English', 'Предлоги и сочетания', 'Idioms & collocations'
    if 'confused' in t.lower():
        return 'Use of English', 'Предлоги и сочетания', 'Words often confused'
    return 'Use of English', 'Предлоги и сочетания', 'Dependent prepositions'


def where(r):
    m = re.search(r'Module (\d+)', r['module'])
    if m:
        return f"М{m.group(1)}" + (f" ({r['lesson']})" if r['lesson'] else '')
    return r['module'].split('·')[0].strip()


def main():
    rows = sort_rows(load_rows())
    grades = sorted({r['grade'] for r in rows})
    videos = {}
    p = os.path.join(D, 'data', 'videos.json')
    if os.path.exists(p):
        videos = json.load(open(p))

    topics = {}
    for r in rows:
        if r['category'] in LEX:
            block, cat, name = lex_topic(r)
        else:
            block, cat, name = 'Грамматика', r['category'], r['topic']
        t = topics.setdefault(name, {'block': block, 'cat': cat, 'cells': {}, 'rows': []})
        t['rows'].append(r)
        cell = t['cells'].setdefault(r['grade'], [])
        w = where(r)
        if w not in cell:
            cell.append(w)

    LEXCATS = ['Фразовые глаголы', 'Словообразование', 'Предлоги и сочетания']
    def key(n):
        t = topics[n]
        if t['block'] == 'Грамматика':
            return (0, CATS.index(t['cat']) if t['cat'] in CATS else 99, min(t['cells']), n)
        return (1, LEXCATS.index(t['cat']), min(t['cells']), n)
    order = sorted(topics, key=key)

    wb = Workbook()
    # --- Как пользоваться
    ws = wb.active; ws.title = 'Как пользоваться'
    for line in [
        'План уроков по грамматике Spotlight',
        '',
        '«Темы × классы» — все темы, из которых будут уроки-папки. Строка = тема; в колонке класса — модули (и урок), где она есть в учебнике. Цвет клетки = возрастная группа вебинара.',
        'Группы вебинаров: 7–9 лет = 1–3 класс → Spotlight 2–3 (Spotlight начинается со 2 класса; у 2 класса нет грамматического справочника, поэтому в таблице он пуст). 10+ = Spotlight 4–11. 4 класс (9–10 лет) отнесён к 10+.',
        'Колонки «Видео 7–9» и «Видео 10+»: «есть» / «нет» (выпадающий список), рядом — название или ссылка вебинара. «—» значит, что темы для этой группы нет.',
        '«Папки уроков» — будущая структура: Spotlight / класс / модуль / тема. Отметка о видео подтягивается из «Темы × классы» сама.',
        '«Итоги» — сколько тем нужно каждой группе, у скольких уже есть видео и сколько понедельников (по одному вебинару на группу) нужно на остальные.',
        '',
        'Источник тем — лист «Сводка по темам» в Spotlight_грамматика.xlsx: грамматика из справочника, Use of English из оглавления и приложений.',
    ]:
        ws.append([line])
    ws['A1'].font = Font(bold=True, size=14)
    ws.column_dimensions['A'].width = 140
    for row in ws.iter_rows(min_row=2):
        row[0].alignment = Alignment(wrap_text=True)

    # --- Темы × классы
    ws = wb.create_sheet('Темы × классы')
    gcols = [f'{g} кл.' for g in grades]
    cols = ['№', 'Блок', 'Категория', 'Тема', 'Группы'] + gcols + \
           ['Видео 7–9', 'Вебинар 7–9 (название / ссылка)', 'Видео 10+', 'Вебинар 10+ (название / ссылка)', 'Комментарий']
    header(ws, cols, [5, 13, 20, 34, 9] + [11] * len(grades) + [10, 30, 10, 30, 30])
    ws.freeze_panes = 'E2'
    G0 = 6  # первая колонка класса
    V = G0 + len(grades)  # «Видео 7–9»
    dv = DataValidation(type='list', formula1='"есть,нет"', allow_blank=True)
    ws.add_data_validation(dv)
    for i, n in enumerate(order, 1):
        t = topics[n]
        gs = {group(g) for g in t['cells']}
        grp = 'обе' if len(gs) == 2 else gs.pop()
        cells = ['\n'.join(t['cells'].get(g, [])) for g in grades]
        vid = []
        for gname in GROUPS:
            need = grp in (gname, 'обе')
            have = videos.get(n, {}).get(gname, '')
            vid += [('есть' if have else 'нет') if need else '—', have if need else '']
        ws.append([i, t['block'], t['cat'], n, grp] + cells + vid + [''])
    body(ws)
    for row in ws.iter_rows(min_row=2):
        row[3].font = Font(bold=True)
        for j, g in enumerate(grades):
            c = row[G0 - 1 + j]
            if c.value:
                c.fill = FILL[group(g)]
                c.alignment = Alignment(wrap_text=True, vertical='top', horizontal='center')
        for off in (0, 2):
            c = row[V - 1 + off]
            c.alignment = Alignment(horizontal='center', vertical='top')
            if c.value == '—':
                c.fill = GREY; row[V + off].fill = GREY
            else:
                dv.add(c)
    last = ws.max_row
    for off in (0, 2):
        col = ws.cell(row=1, column=V + off).column_letter
        rng = f'{col}2:{col}{last}'
        ws.conditional_formatting.add(rng, CellIsRule(operator='equal', formula=['"есть"'], fill=YES))
        ws.conditional_formatting.add(rng, CellIsRule(operator='equal', formula=['"нет"'], fill=NO))
    ws.auto_filter.ref = ws.dimensions
    vcol = {g: ws.cell(row=1, column=V + 2 * k).column_letter for k, g in enumerate(GROUPS)}
    wcol = {g: ws.cell(row=1, column=V + 2 * k + 1).column_letter for k, g in enumerate(GROUPS)}

    # --- Папки уроков
    ws2 = wb.create_sheet('Папки уроков')
    header(ws2, ['Класс', 'Модуль', 'Урок', 'Тема (папка)', 'Группа', 'Видео', 'Вебинар', 'Статус', 'Путь'],
           [8, 30, 9, 34, 8, 9, 30, 18, 70])
    ws2.freeze_panes = 'E2'
    dv2 = DataValidation(type='list', formula1='"не начат,готов без видео,готов с видео,опубликован"', allow_blank=True)
    ws2.add_data_validation(dv2)
    seen = {}
    for n in order:
        for r in topics[n]['rows']:
            k = (r['grade'], r['module'], n)
            if k in seen:
                if r['lesson'] and r['lesson'] not in seen[k]:
                    seen[k].append(r['lesson'])
                continue
            seen[k] = [r['lesson']] if r['lesson'] else []
    items = sorted(seen, key=lambda k: (k[0], modnum(k[1]), order.index(k[2])))
    for i, (g, m, n) in enumerate(items, 2):
        grp = group(g)
        mt = "'Темы × классы'"
        ws2.append([g, m, ', '.join(seen[(g, m, n)]), n, grp,
                    f'=IFERROR(INDEX({mt}!${vcol[grp]}:${vcol[grp]},MATCH(D{i},{mt}!$D:$D,0)),"")',
                    f'=IFERROR(INDEX({mt}!${wcol[grp]}:${wcol[grp]},MATCH(D{i},{mt}!$D:$D,0))&"","")',
                    'не начат', f'Spotlight / {g} класс / {m} / {n}'])
        dv2.add(ws2.cell(row=i, column=8))
    body(ws2)
    for row in ws2.iter_rows(min_row=2):
        row[0].fill = FILL[row[4].value]; row[4].fill = FILL[row[4].value]
        row[3].font = Font(bold=True)
    rng = f'F2:F{ws2.max_row}'
    ws2.conditional_formatting.add(rng, CellIsRule(operator='equal', formula=['"есть"'], fill=YES))
    ws2.conditional_formatting.add(rng, CellIsRule(operator='equal', formula=['"нет"'], fill=NO))
    ws2.auto_filter.ref = ws2.dimensions

    # --- Итоги
    ws3 = wb.create_sheet('Итоги')
    header(ws3, ['Группа', 'Классы', 'Тем нужно', 'Видео есть', 'Видео нет', 'Понедельников на остальные (1 вебинар группы в неделю)', 'Папок-уроков'],
           [10, 14, 11, 11, 11, 26, 13])
    mt = "'Темы × классы'"
    for k, gname in enumerate(GROUPS, 2):
        c = vcol[gname]
        cls = ', '.join(str(g) for g in grades if group(g) == gname) or '—'
        ws3.append([gname, cls,
                    f'=COUNTIF({mt}!{c}:{c},"есть")+COUNTIF({mt}!{c}:{c},"нет")',
                    f'=COUNTIF({mt}!{c}:{c},"есть")', f'=COUNTIF({mt}!{c}:{c},"нет")', f'=E{k}',
                    f"=COUNTIF('Папки уроков'!E:E,\"{gname}\")"])
    body(ws3)
    for row in ws3.iter_rows(min_row=2):
        row[0].fill = FILL[row[0].value]

    wb.save(OUT)
    print(OUT, len(order), 'тем;', len(items), 'папок')
    return topics, order


if __name__ == '__main__':
    topics, order = main()
    for n in order:
        if topics[n]['block'] != 'Грамматика':
            print(' ', n, sorted(topics[n]['cells']))
