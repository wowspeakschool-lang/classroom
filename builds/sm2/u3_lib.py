# -*- coding: utf-8 -*-
import json, random

M  = '@@MEDIA@@'
SH = M + 'shared/'
U3 = M + 'sm2/u3/'

# слово · перевод · картинка
WORDS = [
    ('playground',    'детская площадка',        'p_playground'),
    ('cinema',        'кинотеатр',               'p_cinema'),
    ('swimming pool', 'бассейн',                 'p_swimming_pool'),
    ('park',          'парк',                    'p_park'),
    ('hospital',      'больница',                'p_hospital'),
    ('bus stop',      'автобусная остановка',    'p_bus_stop'),
    ('shop',          'магазин',                 'p_shop'),
    ('street',        'улица',                   'p_street'),
    ('cafe',          'кафе',                    'p_cafe'),
    ('train station', 'железнодорожный вокзал',  'p_train_station'),
]

# новые слова ДЗ 6
WORDS6 = [
    ('market',        'рынок',              'm_market'),
    ('car park',      'парковка',           'm_car_park'),
    ('monument',      'памятник',           'm_monument'),
    ('sports centre', 'спортивный центр',   'm_sports_centre'),
    ('museum',        'музей',              'm_museum'),
]


def url(name):
    return f'{U3}{name}.webp'


def surl(name):
    return f'{SH}{name}.webp'


def img(name, h=None, maxw=True):
    st = f'height:{h}px' if h else ('max-width:100%' if maxw else '')
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
    o = [{'text': x} for x in options]
    d = {'q': text, 'type': 'single', 'correct': [options.index(correct)], 'options': o}
    if image:
        d['image'] = url(image)
    if audio_tts:
        d['audio_tts'] = audio_tts
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
            pre = f'    -- блок {i + 1} (sort_order {i}) · {c}\n' if c else f'    -- блок {i + 1} (sort_order {i})\n'
            rows.append(pre + f"    (v_lesson, '{t}', replace($blk${body}$blk$, '@@MEDIA@@', v_media)::jsonb, {i})")
        title = self.title.replace("'", "''")
        summary = self.summary.replace("'", "''")
        return (
f"""-- SM2 · Unit 3 · {self.title}
do $mig$
declare
  v_course uuid; v_unit uuid; v_lesson uuid;
  v_media text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm2';
  if v_course is null then raise exception 'course sm2 not found'; end if;

  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 3 · My town' limit 1;
  if v_unit is null then
    insert into classroom_units (course_id, title, sort_order)
    values (v_course, 'Unit 3 · My town', 3) returning id into v_unit;
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
