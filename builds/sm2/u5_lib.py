# -*- coding: utf-8 -*-
import json, random

M  = '@@MEDIA@@'
SH = M + 'shared/'
U5 = M + 'sm2/u5/'

UNIT = 'Unit 5 · My room'
UNIT_ORDER = 5

# слово · перевод
WORDS = [
    ('lamp',     'лампа'),
    ('armchair', 'кресло'),
    ('sofa',     'диван'),
    ('mirror',   'зеркало'),
    ('bed',      'кровать'),
    ('rug',      'ковёр'),
    ('table',    'стол'),
    ('wardrobe', 'шкаф'),
    ('poster',   'плакат'),
]

MATERIALS = [
    ('wood',    'дерево'),
    ('metal',   'металл'),
    ('plastic', 'пластик'),
    ('glass',   'стекло'),
    ('fabric',  'ткань'),
]


def url(name):
    return f'{U5}{name}.webp'


def surl(name):
    return f'{SH}{name}.webp'


def img(name, h=None):
    st = f'height:{h}px' if h else 'max-width:100%'
    return f'<p><img src="{url(name)}" alt="" style="{st}"></p>'


def simg(name, h=180):
    return f'<p><img src="{surl(name)}" alt="" style="height:{h}px"></p>'


def accept(t):
    lo = t.strip()
    return [lo, lo[:1].upper() + lo[1:]]


def scramble(word, seed):
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
        self.blocks = []              # (type, payload, comment)

    def add(self, t, payload, comment=''):
        self.blocks.append((t, payload, comment))
        return self

    def text(self, html, comment=''):
        return self.add('text', {'html': html}, comment)

    def sql(self):
        rows = []
        for i, (t, p, c) in enumerate(self.blocks):
            body = json.dumps(p, ensure_ascii=False)
            assert '$blk$' not in body, f'$blk$ в payload блока {i}'
            pre = (f'    -- блок {i + 1} (sort_order {i}) · {c}\n' if c
                   else f'    -- блок {i + 1} (sort_order {i})\n')
            rows.append(pre + f"    (v_lesson, '{t}', replace($blk${body}$blk$, '@@MEDIA@@', v_media)::jsonb, {i})")
        title = self.title.replace("'", "''")
        summary = self.summary.replace("'", "''")
        return (
f"""-- SM2 · {UNIT} · {self.title}
do $mig$
declare
  v_course uuid; v_unit uuid; v_lesson uuid;
  v_media text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm2';
  if v_course is null then raise exception 'course sm2 not found'; end if;

  select id into v_unit from classroom_units
   where course_id = v_course and title = '{UNIT}' limit 1;
  if v_unit is null then
    insert into classroom_units (course_id, title, sort_order)
    values (v_course, '{UNIT}', {UNIT_ORDER}) returning id into v_unit;
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
