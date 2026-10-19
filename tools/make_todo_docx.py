#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Собирает Word-файл «Что нужно от вас» для методиста.

Запуск:  python3 tools/make_todo_docx.py [куда_положить.docx]

В файле только то, что требует её действия или решения: закрытые пункты,
промпты и отчёты о сделанном сюда не попадают.
"""

import os
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.shared import Pt, RGBColor, Cm

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RED = RGBColor(0xC0, 0x1A, 0x1A)
GREY = RGBColor(0x66, 0x66, 0x66)


def style_doc(doc):
    normal = doc.styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(11)
    for name, size in (('Heading 1', 16), ('Heading 2', 13)):
        st = doc.styles[name]
        st.font.name = 'Calibri'
        st.font.size = Pt(size)
        st.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
        st.font.bold = True


def para(doc, text='', color=None, italic=False, space_after=6):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.italic = italic
    if color is not None:
        run.font.color.rgb = color
    p.paragraph_format.space_after = Pt(space_after)
    return p


def table(doc, header, rows, widths):
    t = doc.add_table(rows=1, cols=len(header))
    t.style = 'Light Grid Accent 1'
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    for i, h in enumerate(header):
        t.rows[0].cells[i].text = ''
        t.rows[0].cells[i].paragraphs[0].add_run(h).bold = True
    for row in rows:
        cells = t.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = ''
            p = cells[i].paragraphs[0]
            p.add_run(str(value))
            p.paragraph_format.space_after = Pt(2)
    for row in t.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return t


BLOCKING = [
    ('Юнит 0, тест, блок 9',
     'Сверить по записи sm2_u0_test_b7.mp3: шкаф у окна? Ключ поставлен по картинке — near the window.'),
    ('Юнит 1, тест, блок 16',
     'Расписание Эммы приведено к тексту READING, получасовые времена убраны. Запись sm2_u1_test_b14.mp3 сверить или перезаписать.'),
    ('Юнит 7, ДЗ 4, блок 7',
     'Кто говорит «Now it is my turn to help you» — водитель (как в комиксе) или Thunder (как в плане)? Ключ стоит по комиксу.'),
    ('Юнит 8, ДЗ 5, запись Мэдди',
     'Нужна расшифровка sm2_u8_hw5_b6.mp3, иначе автопроверяемых вопросов по ней не будет.'),
]

DECISIONS = [
    ('Юнит 0, тест, текст READING',
     'В тексте шкаф у окна и тридцать детей, на картинке шкаф у двери и детей четверо. Что первично?'),
    ('Юнит 1, ДЗ 4, блок 11',
     'Пара «He goes to school at three o clock» проверяется только по аудио истории — сверить время.'),
    ('Юнит 1, ДЗ 7',
     '11 заданий при ориентире 8. Убрать один из двух похожих квизов (блоки 12 и 14)?'),
    ('Юнит 8, ДЗ 3, карточка card_like',
     'Поправить одну строку в редакторе слайдов: было «I don’t like hockey. — I don’t.» / «Я тоже не люблю хоккей», надо «I like hockey. — I don’t.» / «А я не люблю хоккей».'),
    ('Юниты 2 и 3, написание cafe',
     'В заданиях везде cafe, принимаются оба написания. На карточке card_places — café, на карте map_greenville — Cafè (опечатка генератора).'),
    ('Юнит 3, ДЗ 1, карточки',
     'На card_places 11 слов, в карточках урока 10. Добавлять одиннадцатую?'),
    ('Юнит 3, план урока 4',
     'План требует «Never give up!», в тексте истории и на кадрах этой фразы нет. Пропуск в выгрузке или ошибка плана?'),
    ('Юнит 3, чант',
     'На уроке 7 учитель просит спеть чант, которого ребёнок дома не слышал. Нужна запись.'),
    ('Юнит 3, ДЗ 3, блок 12',
     'План предлагал развернуть задание — вписывать место, а не предлог. Для этого надо сверить ч/б карту по каждому пункту. Разворачивать?'),
    ('Юнит 4, f_lemon',
     'На картинке целый лимон и половинка. Ответ lemon, lemons тоже принимается. Нужно строго множественное?'),
    ('Юнит 4, веса продуктов',
     'ДЗ 6 и ДЗ 7 опираются на две картинки с разными весами. Свести к одному набору — это перерисовка weights_hw7.'),
    ('Юниты 6 и 7, «собери слово из букв»',
     'Озвучка проговаривает искомое слово. Там, где блоки пересобирали, звук сняли. Снимать везде или оставить как подсказку?'),
    ('Юнит 6, ДЗ 6, блок 9',
     'Состав ответов по видео (birds, a pig, a dog) сверить с залитым мультиком; вариант «a cat» добавлен как неверный.'),
    ('Юнит 7, тест, пять фотографий',
     'tt_skate, tt_football, tt_book, tt_plane, tt_kite — стоковые фото среди 3D-рисунков. Перерисовывать?'),
    ('Юнит 7, media/sm2/u7/',
     'Четыре файла больше не используются: d_plane, d_train, d_jump, d_dance. Удалять из репозитория?'),
    ('Юнит 8, ДЗ 4, блок 7, точка (50, 75)',
     'Подпись поставлена по кадру 8 комикса. Если на мультфильме это не финальная сцена — заменить.'),
    ('Юнит 9, ДЗ 6, три новые фразы',
     'Добавлены recycling bins, take your rubbish home, pick the flowers — иначе в корзинах не набиралось восемь карточек. Оставляем?'),
    ('Финальный тест, блок 16',
     'Текст READING про Джейка написан мной, в выгрузке его не было. Прочитать: по нему решаются шесть утверждений блока 17.'),
    ('Super Minds 1, юнит 1, ДЗ 3',
     'В блоке «картинка → команда» 5 вопросов из 9: команды без предмета картинкой не покажешь. Все девять остались в соседнем блоке.'),
    ('Super Minds 1, юнит 5, ДЗ 1',
     'Картинок для дней недели нет, поэтому два блока подряд на порядок дней. Удалить один?'),
    ('Super Minds 3, юнит 5, to dive',
     'Картинки действия нет, стоит снаряжение (маска, трубка, ласты). Нужна отдельная картинка?'),
]

LOOK = [
    ('88 пересобранных игр Wordwall',
     'Содержимого выгрузка не отдаёт, состав подобрала я.'),
    ('14 блоков с точками на картинке',
     'Листы для проверки — builds/sm2/hotspot_check/: картинка с пронумерованными кружками и подписи списком.'),
    ('Тексты READING, которых не было в выгрузке',
     'Написаны мной так, чтобы сходились все ответы.'),
    ('18 новых блоков фонетики',
     'ДЗ 4 юнитов 1–9, механика узнавания чередуется.'),
]


def build(path):
    doc = Document()
    style_doc(doc)

    doc.add_heading('Что нужно от вас', level=0)
    para(doc, 'Super Minds 2 и другие курсы.', color=GREY, italic=True, space_after=14)

    doc.add_heading('Два действия', level=1)
    p = doc.add_paragraph('Нажать «Озвучить пачкой»: Super Minds 2 — 182 места, '
                          'Super Minds 1 — 51, Super Minds 3 — 41, Go Getter 1 — 17. '
                          'Без этого у новых заданий нет звука.', style='List Number')
    p.paragraph_format.space_after = Pt(3)
    p = doc.add_paragraph('Включить публикацию уроков. Тесты — после того, как закроете '
                          'четыре пункта из первой таблицы.', style='List Number')
    p.paragraph_format.space_after = Pt(10)

    doc.add_heading('Без этого тесты включать нельзя', level=1)
    para(doc, 'Ключи стоят по моей догадке — проверить может только тот, кто слышит запись.',
         color=GREY, italic=True)
    table(doc, ['№', 'Где', 'Что сделать'],
          [(i + 1, w, t) for i, (w, t) in enumerate(BLOCKING)], [1.0, 4.5, 11.0])

    doc.add_heading('Решения за вами', level=1)
    para(doc, 'Если пункт не решить, задание останется в нынешнем виде.', color=GREY, italic=True)
    table(doc, ['№', 'Где', 'Что решить'],
          [(i + 5, w, t) for i, (w, t) in enumerate(DECISIONS)], [1.0, 4.5, 11.0])

    doc.add_heading('Посмотреть глазами', level=1)
    para(doc, 'Не ошибки — места, где состав придумала я.', color=GREY, italic=True)
    for head, note in LOOK:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(head + '. ').bold = True
        p.add_run(note)
        p.paragraph_format.space_after = Pt(3)

    doc.save(path)
    return path


if __name__ == '__main__':
    out = (sys.argv[1] if len(sys.argv) > 1
           else os.path.join(ROOT, 'builds', 'sm2', 'Что нужно от вас.docx'))
    print(build(out))
