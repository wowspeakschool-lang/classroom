"""Новая разбивка чек-листа 13+ в формате Assessment chart Анны (20.11.2026).

Берём её исходник (ishodnik/…docx) и меняем только таблицы частей 2 и 3:
у каждого Prepare вместо двух блоков «Unit 0-9 / Unit 10-20» — четыре.
Строки копируются из исходных (заголовок блока и строка темы), так что
оформление, колонки 0 / 1 / 2 и всё остальное в документе остаются как было.

    python3 builds/mvu_13plus/karty_kursa/make_chart.py
"""
import copy, os, sys
import docx

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'ishodnik', 'Assessment chart and link to Vznaniya_13-17.docx')
OUT = os.path.join(HERE, 'Assessment chart 13+ — новая разбивка (проект).docx')

# (название блока, [3 лексики + 3 грамматики]) — по картам курса, karty_kursa/prepareN.md
sys.path.insert(0, os.path.join(HERE, '..'))
from data import NEW  # один список тем на урок и на docx
TABLES = {1: (2, 3, 4), 2: (5, 6, 7)}   # таблица документа → какие Prepare в её трёх колонках
COLS = (0, 5, 10)                        # колонка с названием темы у каждого Prepare


def set_text(cell, text):
    p = cell.paragraphs[0]
    runs = p.runs
    if runs:
        runs[0].text = text
        for r in runs[1:]: r.text = ''
    else:
        p.add_run(text)
    for extra in cell.paragraphs[1:]:
        for r in extra.runs: r.text = ''


def main():
    d = docx.Document(SRC)
    for ti, prs in TABLES.items():
        t = d.tables[ti]
        rows = t.rows
        head_tpl, topic_tpl = copy.deepcopy(rows[1]._tr), copy.deepcopy(rows[2]._tr)
        for r in list(rows)[1:]: t._tbl.remove(r._tr)
        for b in range(4):
            tr = copy.deepcopy(head_tpl); t._tbl.append(tr)
            row = t.rows[-1]
            for pr, col in zip(prs, COLS): set_text(row.cells[col], NEW[pr][b][0])
            for k in range(6):
                tr = copy.deepcopy(topic_tpl); t._tbl.append(tr)
                row = t.rows[-1]
                for pr, col in zip(prs, COLS): set_text(row.cells[col], NEW[pr][b][1][k])
    d.save(OUT)
    print('сохранено:', OUT)


if __name__ == '__main__':
    main()
