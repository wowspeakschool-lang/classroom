# -*- coding: utf-8 -*-
"""Сборка урока: блоки на питоне → миграция SQL.

Один файл `uN_build.py` на юнит: вызывает setup(), объявляет Lesson'ы,
складывает блоки методом .add(), в конце пишет по файлу SQL на урок.

    import sys; sys.path.insert(0, '/home/user/classroom/tools')
    import lib as L
    from lib import Lesson, url, simg, img

    L.setup('Unit 1 · Family', 1, 'sm3/u1', course='sm3')
"""
import json, random

TYPE_RU = {
    'text': 'Материал', 'video': 'Видео/аудио', 'quiz': 'Тест',
    'exact_input': 'Короткий ответ', 'match': 'Найди пару', 'task': 'Задание',
    'embed': 'Тренажёр', 'order': 'Составь предложение', 'sort': 'Классификация',
    'flashcards': 'Карточки', 'gaps': 'Заполни пропуски',
    'truefalse': 'Верно / неверно', 'speaking': 'Запись голоса',
    'sequence': 'Порядок предложений', 'hotspot': 'Точки на картинке',
}

M  = '@@MEDIA@@'
SH = M + 'shared/'

COURSE = None        # всё это задаёт setup()
UNIT = None
UNIT_ORDER = None
UDIR = None


def setup(title, order, folder, course='sm2'):
    """Настраивает модуль на юнит: курс, заголовок, порядок и папку картинок.

    folder — путь внутри media/ без слэшей по краям: 'sm3/u1'.
    """
    global COURSE, UNIT, UNIT_ORDER, UDIR
    COURSE, UNIT, UNIT_ORDER, UDIR = course, title, order, M + folder + '/'


def url(name):
    return f'{UDIR}{name}.webp'


def surl(name):
    return f'{SH}{name}.webp'


def img(name, h=None):
    st = f'height:{h}px' if h else 'max-width:100%'
    return f'<p><img src="{url(name)}" alt="" style="{st}"></p>'


def simg(name, h=180):
    return f'<p><img src="{surl(name)}" alt="" style="height:{h}px"></p>'


def accept(t):
    """Варианты ответа для exact_input: со строчной и с заглавной буквы."""
    lo = t.strip()
    return [lo, lo[:1].upper() + lo[1:]]


def scramble(word, seed):
    """Буквы вперемешку для «собери слово»; seed — чтобы не менялось при пересборке."""
    rnd = random.Random(seed)
    parts = []
    for w in word.split(' '):
        ls = list(w)
        for _ in range(60):
            rnd.shuffle(ls)
            if ''.join(ls) != w:
                break
        parts.append(' '.join(ls))
    return ' / '.join(parts)


def distract(correct, pool, n, seed):
    rnd = random.Random(seed)
    others = [x for x in pool if x != correct]
    rnd.shuffle(others)
    return others[:n]


def q_single(text, correct, options, image=None, audio_tts=None):
    """Один вопрос квиза: correct — строка из options."""
    d = {'q': text, 'type': 'single',
         'correct': [options.index(correct)],
         'options': [{'text': x} for x in options]}
    if image:
        d['image'] = url(image)
    if audio_tts:
        d['audio_tts'] = audio_tts
    return d


def q_multi(text, correct, options, image=None):
    """Вопрос с несколькими верными ответами: correct — список строк из options."""
    d = {'q': text, 'type': 'multiple',
         'correct': sorted(options.index(c) for c in correct),
         'options': [{'text': x} for x in options]}
    if image:
        d['image'] = url(image)
    return d


class Lesson:
    def __init__(self, title, summary, order, kind='homework', threshold=60):
        self.title = title
        self.summary = summary
        self.order = order
        self.kind = kind
        self.threshold = threshold
        self.blocks = []              # (type, payload, comment, todo)

    def add(self, t, payload, comment='', todo=None):
        """todo=(что нужно от вас, как выглядит в уроке, почему) — строка в файл методиста."""
        self.blocks.append((t, payload, comment, todo))
        return self

    def text(self, html, comment='', todo=None):
        return self.add('text', {'html': html}, comment, todo)

    def todo_rows(self):
        """Строки для файла «доработать руками»; номер блока — как в редакторе."""
        rows = []
        for i, (t, _, _, todo) in enumerate(self.blocks):
            if todo:
                need, look, why = todo
                rows.append([str(i + 1), TYPE_RU.get(t, t), look, need, why])
        return rows

    def sql(self):
        rows = []
        for i, (t, p, c, _) in enumerate(self.blocks):
            body = json.dumps(p, ensure_ascii=False)
            assert '$blk$' not in body, f'$blk$ в payload блока {i}'
            pre = (f'    -- блок {i + 1} (sort_order {i}) · {c}\n' if c
                   else f'    -- блок {i + 1} (sort_order {i})\n')
            rows.append(pre + f"    (v_lesson, '{t}', replace($blk${body}$blk$, '@@MEDIA@@', v_media)::jsonb, {i})")
        title = self.title.replace("'", "''")
        summary = self.summary.replace("'", "''")
        unit = UNIT.replace("'", "''")
        return (
f"""-- {COURSE.upper()} · {UNIT} · {self.title}
do $mig$
declare
  v_course uuid; v_unit uuid; v_lesson uuid;
  v_media text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = '{COURSE}';
  if v_course is null then raise exception 'course {COURSE} not found'; end if;

  select id into v_unit from classroom_units
   where course_id = v_course and title = '{unit}' limit 1;
  if v_unit is null then
    insert into classroom_units (course_id, title, sort_order)
    values (v_course, '{unit}', {UNIT_ORDER}) returning id into v_unit;
  end if;

  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = '{title}' limit 1;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, summary, sort_order, is_published, pass_threshold, kind)
    values (v_unit, '{title}', '{summary}', {self.order}, false, {self.threshold}, '{self.kind}')
    returning id into v_lesson;
  else
    update classroom_lessons set summary = '{summary}', sort_order = {self.order},
           is_published = false, pass_threshold = {self.threshold}, kind = '{self.kind}'
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
""" + ",\n".join(rows) + f"""
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  delete from classroom_blocks where lesson_id = v_lesson and sort_order >= {len(self.blocks)};
end
$mig$;
""")


def write_sql(lessons, out_dir):
    """Пишет по файлу SQL на урок: 00_homework_1.sql, 01_homework_2.sql …"""
    import os, re
    os.makedirs(out_dir, exist_ok=True)
    for i, les in enumerate(lessons):
        slug = re.sub(r'[^a-z0-9]+', '_', les.title.lower()).strip('_')
        fn = f'{out_dir}/{i:02d}_{slug}.sql'
        open(fn, 'w').write(les.sql())
        print(f'{fn}: {len(les.blocks)} блоков')
