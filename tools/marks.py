# -*- coding: utf-8 -*-
"""Снимает отметки вариантов ответа с выгрузки «Взнания».

В редакторе у НЕотмеченного варианта слева стоит пустой квадратик, у
отмеченного его нет — это и есть правильный ответ. Квадратик светло-серый,
в вектор не попадает, поэтому страница рендерится и полоса слева от номера
варианта проверяется на чернила.

    python3 marks.py u6pdf/hw3.pdf          # все страницы
    python3 marks.py u6pdf/hw3.pdf 9 10     # только эти
"""
import pypdfium2 as pdfium
import numpy as np
import sys, re

SCALE   = 2.0
NUM_X   = (126, 138)   # pt: колонка с номером варианта
BOX_X   = (88, 120)    # pt: полоса, где стоит пустой квадратик
TXT_X   = 150          # pt: левее этого начинается служебная часть строки
ROW_H   = 16           # pt: половина высоты строки варианта


def options(path, pages=None):
    """[(стр., номер, текст, отмечен?)] по всем блокам «Варианты ответов»."""
    doc = pdfium.PdfDocument(path)
    out = []
    live = 0          # варианты идут на странице с «Варианты ответов» и следующей
    for pi in range(len(doc)):
        if pages and pi + 1 not in pages:
            continue
        page = doc[pi]
        tp = page.get_textpage()
        txt = tp.get_text_range()
        if 'Выберите новое задание для урока' in txt:
            break
        live = 2 if 'Варианты ответов' in txt else max(0, live - 1)
        if not live:
            continue
        H = page.get_height()
        img = np.array(page.render(scale=SCALE).to_pil().convert('L'))

        # номера вариантов: одиночные цифры в своей колонке
        rows = []
        for i in range(tp.count_chars()):
            c = tp.get_text_range(i, 1)
            if not c.isdigit():
                continue
            l, b, r, t = tp.get_charbox(i)
            if NUM_X[0] <= l <= NUM_X[1] and b > 40:   # ниже 40 pt — колонтитул
                rows.append((round((t + b) / 2, 1), c, l))
        # склеиваем двузначные номера, идущие подряд по x
        rows.sort(key=lambda z: -z[0])
        merged = []
        for y, c, l in rows:
            if merged and abs(merged[-1][0] - y) < 4:
                merged[-1][1] += c
            else:
                merged.append([y, c])

        for y, num in merged:
            py = int((H - y) * SCALE)
            strip = img[max(0, py - ROW_H):py + ROW_H,
                        int(BOX_X[0] * SCALE):int(BOX_X[1] * SCALE)]
            if strip.size == 0:
                continue
            has_box = (strip < 245).mean() > 0.01
            # текст варианта — справа от номера на той же строке
            line = tp.get_text_bounded(TXT_X, y - 6, page.get_width(), y + 6)
            line = re.sub(r'\s+', ' ', line).strip()
            if (not line or 'lesson/update/assessment' in line
                    or re.fullmatch(r'[\d:.\sx]+', line)):
                continue                        # колонтитул или плеер, не вариант
            out.append((pi + 1, num, line, not has_box))
    return out


if __name__ == '__main__':
    path = sys.argv[1]
    pages = {int(x) for x in sys.argv[2:]} or None
    page_now = None
    for pg, num, text, marked in options(path, pages):
        if pg != page_now:
            print(f'--- стр. {pg}')
            page_now = pg
        print(f'  {"✔" if marked else " "} {num:>2}  {text[:70]}')
