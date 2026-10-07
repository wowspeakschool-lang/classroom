# -*- coding: utf-8 -*-
"""Планировщик уроков: Spotlight_темы_уроков.xlsx.

Строка — подтема (урок), колонки — классы: модуль и статус (новое / расширение / повторение),
и отметки о видео отдельно для двух возрастных групп вебинаров.
Подтемы грамматики — data/subtopics/*.json; Use of English — из data/gN.json.
Отметки о видео — data/videos.json: {"<подтема>": {"7–9": "ссылка или название", "10+": "..."}}.

    python3 spotlight/matrix.py
"""
import json, os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.comments import Comment
from openpyxl.formatting.rule import CellIsRule
from openpyxl.worksheet.datavalidation import DataValidation
from build import D, CATS, LEX, load_rows, sort_rows, modnum, header, body, BOX, WRAP, ALIAS, CATFIX

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


STRONG = {'7–9': 'F4B183', '10+': '9DC3E6'}
MID = {'7–9': 'F8CBAD', '10+': 'BDD7EE'}
LIGHT = {'7–9': 'FCE4D6', '10+': 'DDEBF7'}
RANK = {'новое': 3, 'расширение': 2, 'повторение': 1}
SHORT = {'новое': 'новое', 'расширение': 'расш.', 'повторение': 'повт.'}


def load_units():
    """Подтема = будущий урок. Грамматика — из data/subtopics/*.json, Use of English — из строк учебника."""
    rows = sort_rows(load_rows())
    cat_of = {r['topic']: r['category'] for r in rows}
    units = {}
    def unit(block, cat, topic, name, order):
        return units.setdefault(name, {'block': block, 'cat': cat, 'topic': topic, 'order': order, 'cells': {}})
    for f in sorted(glob.glob(os.path.join(D, 'data', 'subtopics', '*.json'))):
        for e in json.load(open(f)):
            t = ALIAS.get(e['topic'], e['topic'])
            u = unit('Грамматика', CATFIX.get(t, cat_of.get(t, '')), t, e['subtopic'].strip(), int(e.get('order') or 99))
            u['cells'].setdefault(int(e['grade']), []).append(
                {'module': e['module'], 'lesson': e.get('lesson') or '', 'status': e['status'], 'detail': e.get('detail') or ''})
    seen = set()
    for r in rows:
        if r['category'] not in LEX:
            continue
        block, cat, name = lex_topic(r)
        topic = name.split(':')[0]
        u = unit(block, cat, topic, name, 1)
        st = 'повторение' if name in seen else 'новое'
        seen.add(name)
        u['cells'].setdefault(r['grade'], []).append(
            {'module': r['module'], 'lesson': r['lesson'], 'status': st, 'detail': r['scope'][:300]})
    return units


def main():
    units = load_units()
    grades = sorted({g for u in units.values() for g in u['cells']})
    videos = {}
    p = os.path.join(D, 'data', 'videos.json')
    if os.path.exists(p):
        videos = json.load(open(p))

    first = {}
    for n, u in units.items():
        first[u['topic']] = min(first.get(u['topic'], 99), min(u['cells']))
    LEXCATS = ['Фразовые глаголы', 'Словообразование', 'Предлоги и сочетания']
    def key(n):
        u = units[n]
        if u['block'] == 'Грамматика':
            return (0, CATS.index(u['cat']) if u['cat'] in CATS else 99, first[u['topic']], u['topic'], u['order'], n)
        return (1, LEXCATS.index(u['cat']), min(u['cells']), u['topic'], n)
    order = sorted(units, key=key)

    wb = Workbook()
    ws = wb.active; ws.title = 'Как пользоваться'
    for line in [
        'План уроков по грамматике Spotlight',
        '',
        '«Темы × классы»: строка = подтема (один короткий урок: видео → правило → мини-тест). Подтемы сгруппированы по темам: Past Simple делится на правильные/неправильные глаголы, утверждение, отрицание, вопросы, орфографию, каждое значение; сравнения времён — отдельными подтемами.',
        'В клетке класса — где в учебнике (М9 (9b) = Module 9, урок 9b) и статус: «новое» — подтема в Spotlight впервые; «расш.» — была, здесь добавлено; «повт.» — дана снова. Наведите на клетку — во всплывающей подсказке что именно дано (лица, слова-сигналы, список глаголов).',
        'Цвет клетки: оттенок = группа вебинара (оранжевый 7–9 лет, голубой 10+), насыщенность = статус (ярче — новое, бледнее — повторение).',
        'Группы вебинаров: 7–9 лет = 1–3 класс → Spotlight 2–3 (у Spotlight 2 нет грамматического справочника, поэтому 2 класса нет). 10+ = Spotlight 4–11; 4 класс (9–10 лет) отнесён к 10+.',
        '«Видео 7–9» / «Видео 10+»: «есть» / «нет» (выпадающий список), рядом — название или ссылка вебинара. «—» — подтема этой группе не нужна.',
        '«Папки уроков»: Spotlight / класс / модуль / тема (папка) / подтема (урок). Видео подтягивается из «Темы × классы» само; колонка «Готовность» — для отметок.',
        '«Итоги»: сколько уроков нужно каждой группе, у скольких есть видео.',
        '',
        'Источник: грамматический справочник учебников (Use of English — оглавление и приложения). Подробный объём по строкам — в Spotlight_грамматика.xlsx.',
    ]:
        ws.append([line])
    ws['A1'].font = Font(bold=True, size=14)
    ws.column_dimensions['A'].width = 140
    for row in ws.iter_rows(min_row=2):
        row[0].alignment = Alignment(wrap_text=True)

    # --- Темы × классы
    ws = wb.create_sheet('Темы × классы')
    gcols = [f'{g} кл.' for g in grades]
    cols = ['№', 'Блок', 'Категория', 'Тема', 'Подтема (урок)', 'Группы'] + gcols + \
           ['Видео 7–9', 'Вебинар 7–9 (название / ссылка)', 'Видео 10+', 'Вебинар 10+ (название / ссылка)', 'Комментарий']
    header(ws, cols, [5, 12, 16, 22, 46, 8] + [12] * len(grades) + [10, 28, 10, 28, 26])
    ws.freeze_panes = 'F2'
    G0 = 7
    V = G0 + len(grades)
    dv = DataValidation(type='list', formula1='"есть,нет"', allow_blank=True)
    ws.add_data_validation(dv)
    prev = None
    thick = Side(style='medium', color='555555')
    for i, n in enumerate(order, 1):
        u = units[n]
        gs = {group(g) for g in u['cells']}
        grp = 'обе' if len(gs) == 2 else next(iter(gs))
        cells = []
        for g in grades:
            es = u['cells'].get(g, [])
            lines = []
            for e in es:
                l = where(e) + ' · ' + SHORT.get(e['status'], e['status'])
                if l not in lines:
                    lines.append(l)
            cells.append('\n'.join(lines))
        vid = []
        for gname in GROUPS:
            need = grp in (gname, 'обе')
            have = videos.get(n, {}).get(gname, '')
            vid += [('есть' if have else 'нет') if need else '—', have if need else '']
        ws.append([i, u['block'], u['cat'], u['topic'], n, grp] + cells + vid + [''])
        r = ws.max_row
        newtopic = u['topic'] != prev
        prev = u['topic']
        for c in ws[r]:
            c.alignment = WRAP
            c.border = Border(left=BOX.left, right=BOX.right, bottom=BOX.bottom, top=thick if newtopic else BOX.top)
        ws.cell(row=r, column=4).font = Font(bold=newtopic, color='000000' if newtopic else '888888')
        for j, g in enumerate(grades):
            es = u['cells'].get(g)
            if not es:
                continue
            c = ws.cell(row=r, column=G0 + j)
            best = max(RANK.get(e['status'], 1) for e in es)
            pal = {3: STRONG, 2: MID, 1: LIGHT}[best]
            c.fill = PatternFill('solid', fgColor=pal[group(g)])
            c.alignment = Alignment(wrap_text=True, vertical='top', horizontal='center')
            if best == 3:
                c.font = Font(bold=True)
            txt = '\n'.join(f"{where(e)}: {e['detail']}" for e in es if e['detail'])
            if txt:
                c.comment = Comment(txt[:1500], 'Spotlight')
                c.comment.width, c.comment.height = 320, 160
        for off in (0, 2):
            c = ws.cell(row=r, column=V + off)
            c.alignment = Alignment(horizontal='center', vertical='top')
            if c.value == '—':
                c.fill = GREY; ws.cell(row=r, column=V + off + 1).fill = GREY
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
    header(ws2, ['Класс', 'Модуль', 'Урок учебника', 'Тема (папка)', 'Подтема (урок)', 'В учебнике', 'Что именно',
                 'Группа', 'Видео', 'Вебинар', 'Готовность', 'Путь'],
           [7, 26, 9, 22, 44, 11, 50, 8, 9, 26, 18, 60])
    ws2.freeze_panes = 'F2'
    dv2 = DataValidation(type='list', formula1='"не начат,готов без видео,готов с видео,опубликован"', allow_blank=True)
    ws2.add_data_validation(dv2)
    items = []
    for n in order:
        u = units[n]
        for g, es in u['cells'].items():
            mods = {}
            for e in es:
                m = mods.setdefault(e['module'], {'lessons': [], 'status': e['status'], 'detail': []})
                if e['lesson'] and e['lesson'] not in m['lessons']:
                    m['lessons'].append(e['lesson'])
                if RANK.get(e['status'], 1) > RANK.get(m['status'], 1):
                    m['status'] = e['status']
                if e['detail']:
                    m['detail'].append(e['detail'])
            for m, v in mods.items():
                items.append((g, m, n, v))
    items.sort(key=lambda x: (x[0], modnum(x[1]), order.index(x[2])))
    mt = "'Темы × классы'"
    for i, (g, m, n, v) in enumerate(items, 2):
        grp = group(g)
        u = units[n]
        ws2.append([g, m, ', '.join(v['lessons']), u['topic'], n, v['status'], '; '.join(v['detail'])[:400], grp,
                    f'=IFERROR(INDEX({mt}!${vcol[grp]}:${vcol[grp]},MATCH(E{i},{mt}!$E:$E,0)),"")',
                    f'=IFERROR(INDEX({mt}!${wcol[grp]}:${wcol[grp]},MATCH(E{i},{mt}!$E:$E,0))&"","")',
                    'не начат', f"Spotlight / {g} класс / {m} / {u['topic']} / {n}"])
        dv2.add(ws2.cell(row=i, column=11))
    body(ws2)
    for row in ws2.iter_rows(min_row=2):
        grp = row[7].value
        row[0].fill = PatternFill('solid', fgColor=LIGHT[grp]); row[7].fill = PatternFill('solid', fgColor=LIGHT[grp])
        pal = {3: STRONG, 2: MID, 1: LIGHT}[RANK.get(row[5].value, 1)]
        row[5].fill = PatternFill('solid', fgColor=pal[grp])
        row[4].font = Font(bold=True)
    rng = f'I2:I{ws2.max_row}'
    ws2.conditional_formatting.add(rng, CellIsRule(operator='equal', formula=['"есть"'], fill=YES))
    ws2.conditional_formatting.add(rng, CellIsRule(operator='equal', formula=['"нет"'], fill=NO))
    ws2.auto_filter.ref = ws2.dimensions

    # --- Итоги
    ws3 = wb.create_sheet('Итоги')
    header(ws3, ['Группа', 'Классы', 'Подтем (уроков) нужно', 'Видео есть', 'Видео нет', 'Уроков в папках (с повторами по классам)'],
           [10, 14, 14, 11, 11, 22])
    for k, gname in enumerate(GROUPS, 2):
        c = vcol[gname]
        cls = ', '.join(str(g) for g in grades if group(g) == gname) or '—'
        ws3.append([gname, cls,
                    f'=COUNTIF({mt}!{c}:{c},"есть")+COUNTIF({mt}!{c}:{c},"нет")',
                    f'=COUNTIF({mt}!{c}:{c},"есть")', f'=COUNTIF({mt}!{c}:{c},"нет")',
                    f"=COUNTIF('Папки уроков'!H:H,\"{gname}\")"])
    body(ws3)
    for row in ws3.iter_rows(min_row=2):
        row[0].fill = PatternFill('solid', fgColor=LIGHT[row[0].value])

    wb.save(OUT)
    print(OUT, len(order), 'подтем;', len({u['topic'] for u in units.values()}), 'тем;', len(items), 'уроков в папках')
    return units, order


if __name__ == '__main__':
    main()
