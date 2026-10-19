# tools — конвейер переноса юнита

Скрипты, которыми перенесены Super Minds 2, юниты 0–9 и финальный тест.
Сессия временная, поэтому рабочие файлы юнита (сборки, PDF, PNG, SQL) живут в
скретчпаде и пропадают вместе с контейнером — в репозиторий попадают только эти
инструменты, картинки в `media/` и правки `CLAUDE.md`.

Порядок работы над юнитом — в `CLAUDE.md`, раздел «Регламент работы над юнитом».
Здесь — чем на каждом шаге пользоваться.

## Что где

| файл | зачем |
|---|---|
| `unpack.py` | разложить скачанные с Диска PDF по папкам `uNpdf/` |
| `ptext.py` | текст выгрузки постранично, без палитры блоков в конце |
| `ximg.py` | вытащить картинки из PDF в `uNimg/` |
| `sheetgen.py` | контактный лист вытащенных картинок — посмотреть глазами |
| `marks.py` | снять отметки вариантов: отмечен тот, у кого **нет** пустого чекбокса |
| `cut.py` | разрезать присланный методистом лист на отдельные картинки |
| `conv.py` | PNG → webp в `media/<курс>/uN/` по таблице |
| `lib.py` | сборка урока: блоки на питоне → миграция SQL |
| `val.py` | проверка payload до заливки — обязательный шаг |
| `dump_todo.py` | данные для файла «доработать руками» → JSON |
| `doc/build_unit.js` | JSON + `units.js` → docx для методиста |

## Как это выглядит целиком

Рабочая папка — скретчпад сессии. Всё, что ниже, запускается оттуда.

```bash
# 1. файлы с Диска: папка курса → папка юнита, список получать перечислением
#    по parentId (поиск по названию теряет часть файлов)
python3 /home/user/classroom/tools/unpack.py        # → u1pdf/hw1.pdf …

# 2. разобрать выгрузку
python3 /home/user/classroom/tools/ptext.py u1pdf/*.pdf | less
for f in u1pdf/*.pdf; do
  python3 /home/user/classroom/tools/ximg.py "$f" u1img "$(basename "$f" .pdf)"
done
python3 /home/user/classroom/tools/sheetgen.py u1img hw1
python3 /home/user/classroom/tools/marks.py u1pdf/hw3.pdf

# 3. промпты на картинки — текстом в чат, на весь юнит сразу. Ждём картинки.

# 4. присланные листы разрезать, сжать, показать превью
python3 cut_u1.py          # обёртка вокруг cut.sheet(), см. ниже
python3 conv_u1.py         # обёртка вокруг conv.run(), см. ниже

# 5. ждём подтверждения. 6. собираем и заливаем:
python3 u1_build.py                                  # → u1sql/*.sql
python3 /home/user/classroom/tools/val.py u1sql sm3/u1   # должно быть «ОШИБОК: 0»
# каждый файл — отдельный apply_migration через Supabase MCP
python3 /home/user/classroom/tools/dump_todo.py u1_build doc/u1.json
cd doc && npm i && node build_unit.js u1
```

## Обёртки на юнит

`cut_uN.py` — какой лист на какие куски режется:

```python
import sys; sys.path.insert(0, '/home/user/classroom/tools')
from cut import sheet, whole, preview

NAMES = ['f_mother', 'f_father', 'f_sister']     # построчно, слева направо
sheet('u1in/sheet1.png', rows=[3], names=NAMES, dst='u1cut')
whole('u1in/street.png', 'street_scene', dst='u1cut')
preview(NAMES + ['street_scene'], 'u1cut/preview.png', src='u1cut')
```

`conv_uN.py` — что во что сжимается:

```python
import sys; sys.path.insert(0, '/home/user/classroom/tools')
from conv import run

run([('hw2_p02_0', 'card_can', 900, 88)], 'u1img', 'sm3/u1')   # из выгрузки
run([('f_mother', 'f_mother', 380, 82)], 'u1cut', 'sm3/u1')    # свои нарезки
```

`uN_build.py` — сам юнит:

```python
import sys; sys.path.insert(0, '/home/user/classroom/tools')
import lib as L
from lib import Lesson, url, img, simg, accept, q_single, q_multi

L.setup('Unit 1 · Family', 1, 'sm3/u1', course='sm3')

hw1 = Lesson('Homework 1', 'Слова про семью', 0)
hw1.text('<h2>Homework 1</h2>')
hw1.add('flashcards', {...}, 'карточки из выгрузки')
hw1.add('video', {'title': 'Видео к уроку', 'url': ''}, 'НУЖНО ВИДЕО',
        todo=('Ссылка на видео', 'блок «Видео/аудио» в начале урока',
              'в выгрузке медиафайла нет — платформа его не отдаёт'))

LESSONS = [hw1, ...]
if __name__ == '__main__':
    L.write_sql(LESSONS, 'u1sql')
```

Третий аргумент `.add()` — комментарий, он уезжает в SQL строкой над блоком.
Два его значения читает `dump_todo.py`: «СОСТАВ МОЙ» — задание собрано мной,
попадёт в таблицу пересобранных игр; «опечатка» — попадёт в таблицу исправлений.
Четвёртый, `todo=(что нужно от вас, как выглядит в уроке, почему)`, — строка в
файл методиста; `build_unit.js` сам разложит её по разделам сводки по началу
первого поля («Ссылка на видео», «Ссылка на аудио», «Проверить, куда встали
точки», «Прочитать текст для READING», «Посмотреть…»), остальное сложит как есть.

## Зависимости

Python: `pillow`, `numpy`, `pypdf`, `pypdfium2`. Node: `docx` (`npm i` в `doc/`).
