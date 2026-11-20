# Урок 3 Reading Club 10+: план учителя (kind=lesson) + домашка (kind=homework) → SQL
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
M = 'https://classroom.wowteach.ru/media/reading10/u3/'
Z = 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/reading10/zvuki/'
V = 'en_GB-alba'
img = lambda n: M + n + '.webp'
tts = lambda t: {'text': t if t.endswith(('.', '!', '?')) else t + '.', 'voice': V}

# ---------- ДОМАШКА ----------
HW = []
HW.append(('text', {'html': f'<p><img src="{img("sam_phone")}" alt="" style="height:auto;max-width:160px;float:right;margin:0 0 8px 12px">'
  '<b>Агент, ключ пополнился!</b></p><p>Сегодня ты открыл пять новых символов: <b>c k e u r</b>. '
  'Потренируйся, пока не пришло новое сообщение от Агента X.</p>'}))
ANCH = [('c', 'cat', 'кошка · звук /k/'), ('k', 'kid', 'малыш · звук /k/'), ('e', 'egg', 'яйцо · звук /e/'), ('u', 'umbrella', 'зонт · звук /ʌ/'), ('r', 'red_paint', 'красный · звук /r/')]
HW.append(('flashcards', {'title': 'Новые буквы. Нажми на карточку — услышишь звук буквы.',
  'cards': [{'text': l, 'image': img(p), 'audio': Z + l + '.mp3', 'translation': t} for l, p, t in ANCH]}))
QZ = [('e', ['e', 'a', 'i']), ('u', ['o', 'u', 'a']), ('r', ['n', 'm', 'r']), ('c', ['c', 'd', 'g']), ('k', ['t', 'k', 'p'])]
HW.append(('quiz', {'title': 'Послушай звук и выбери букву.',
  'questions': [{'q': '', 'type': 'single', 'audio': Z + s + '.mp3', 'correct': [o.index(s)], 'options': [{'text': x} for x in o]} for s, o in QZ]}))
MW = ['cat', 'sun', 'pen', 'cup', 'red', 'kid']
HW.append(('match', {'title': 'Прочитай слово и найди его картинку.',
  'pairs': [{'left': w, 'right': 'картинка ' + w, 'right_image': img('red_paint' if w == 'red' else w)} for w in MW]}))
HW.append(('sort', {'title': 'Прочитай слова и распредели их: в каком слове звук /e/, а в каком — звук /u/?',
  'groups': [{'name': 'e', 'items': [{'text': w} for w in ['pen', 'ten', 'red', 'net']]},
             {'name': 'u', 'items': [{'text': w} for w in ['sun', 'cup', 'run', 'mug']]}]}))
OW = [('cat', 'cat'), ('sun', 'sun'), ('red', 'red_paint'), ('kid', 'kid')]
HW.append(('order', {'title': 'Посмотри на картинку и собери слово из букв.',
  'items': [{'words': list(w), 'sentence': w, 'image': img(p)} for w, p in OW]}))
GW = [('pen', 'e'), ('cup', 'u'), ('red', 'e'), ('sun', 'u'), ('kit', 'i')]
HW.append(('gaps', {'title': 'Послушай слово и впиши пропущенную букву.', 'mode': 'type',
  'text': '\n'.join(f'{w[0]}__{a}__{w[2]}' for w, a in GW),
  'line_audio': ['' for _ in GW], 'line_audio_tts': [tts(w) for w, _ in GW],
  'line_image': [img('red_paint' if w == 'red' else w) for w, _ in GW]}))
STORY = ('<p><img src="' + img('scene_cup') + '" alt="" style="height:auto;max-width:100%;border-radius:12px"></p>'
  '<p style="font-size:1.25em;line-height:1.6">“Run! Get the red cup!” said Sam.<br>The red cup sits on a mat.<br>'
  'Dan gets it. In the cup — a map!<br>Sam and Dan run.</p>')
HW.append(('quiz', {'title': 'Прочитай историю и ответь: верно или неверно?', 'material': STORY,
  'questions': [{'q': q, 'type': 'single', 'correct': [0 if y else 1], 'options': [{'text': 'Верно'}, {'text': 'Неверно'}]}
                for q, y in [('The cup is red.', 1), ('The cup sits on a pen.', 0), ('In the cup — a map.', 1)]]}))
CHANT = 'Run, run, run in the sun!\nGet a cup, get a nut!\nA red cat, a red pen,\nTen red cups — run, run, run!'
HW.append(('speaking', {'title': 'Прочитай вслух скороговорку и запиши себя 🎤',
  'html': '<p style="font-size:1.3em;line-height:1.6">' + CHANT.replace('\n', '<br>') + '</p>',
  'sample': '', 'sample_tts': tts(CHANT.replace('\n', ' ')), 'needs_review': True}))
HW.append(('text', {'html': f'<p><img src="{img("dan_wave")}" alt="" style="height:auto;max-width:140px;float:right;margin:0 0 8px 12px">'
  '<b>Миссия выполнена!</b></p><p>Новое сообщение Агента X придёт на следующем уроке. До встречи, агент!</p>'}))

# ---------- ПЛАН УРОКА ----------
ST = [
 ('1 · Mission briefing', '1', 'Мотивация: сообщение символами, в ключе пять «?».', 'T: «Здесь есть значки, которых мы ещё не знаем. Сегодня откроем пять новых».', '—'),
 ('2 · Code review', '2', 'Повтор символов, звуков, слов-исключений; скороговорка урока 2 (строки 3–4).', 'S называет букву и звук по символу; I, the, a; «A dog, a pot, a map, a pan — Dig it, Sam! Dig it, Dan!» медленно → быстро.', 'По кругу по символу; скороговорку хором, потом по строке.'),
 ('+ Speed run', '+3', 'Беглость: 18 слов на время, личный рекорд.', 'S читает вслух, T жмёт «Дальше».', 'Каждый на своё время; рекорд — у себя, не сравниваем.'),
 ('3 · HW check', '1', 'Ошибки ДЗ.', 'T показывает 1–2 слова из «Журнала ДЗ», S читает по звукам и целиком.', '—'),
 ('4 · New code', '4', 'Новые звуки c k e u r.', 'Карточка → символ → «This is c. Sound /k/.» → слово-якорь. S повторяет звук 2–3 раза. c и k — один звук. e без «й», u ближе к «а», r без раската.', 'Хором, потом по одному.'),
 ('5 · Hear it', '2', 'Фонематический слух.', '«Поймай звук /e/»: pen ✔ pin ten ✔ tan net ✔ nut. Устно: c-a-t, r-e-d, s-u-n.', 'Хлопок/кнопка — все сразу.'),
 ('6 · Write it', '3', 'Письмо новых букв.', 'Анимация букв; S пишет каждую 3 раза в тетради, списывает cat, red, показывает в камеру.', 'Все пишут, показывают по очереди.'),
 ('+ Copy & check', '+2', 'Списывание слов.', 'sun, kid, pen — списать и сверить.', ''),
 ('7 · Blending', '4', 'Слияние звуков в слово.', 'Звуковые кнопки: cat, kid, pen, ten, sun, cup, red, run. Картинка — после прочтения.', 'По слову на ученика, остальные проверяют.'),
 ('+ Real or fake?', '+3', 'Чтение без угадывания.', 'cup, dut, red, kep, sun, mip, ten, gog — прочитать и решить.', 'По очереди.'),
 ('8 · Word building', '2', 'Сборка слова.', 'Буквы-магниты: cat, sun, red, kid по картинке.', 'Ученик собирает, группа проверяет.'),
 ('9 · Tricky words', '2', 'Слова-исключения said, are, you.', 'Карточки → услышать → «You are a cat!» said Sam.', 'Хором.'),
 ('10 · Dictation', '3', 'Письмо на слух.', 'pen, cup, rat, kit — в тетради, сверить.', 'Все пишут.'),
 ('+ Фраза', '+2', 'Письмо фразы.', 'a red cup.', ''),
 ('11 · Decode the message', '4', 'Чтение фраз и текста.', 'Фразы → «Run! Get the red cup.» символами → история → 3 «верно / неверно».', 'Расшифровываем по символу по кругу.'),
 ('12 · Code chant', '1', 'Беглость, ритм.', '«Run, run, run in the sun! / Get a cup, get a nut!» медленно → быстро.', 'Хором, потом по строке.'),
 ('13 · Mission complete', '1', 'Итог.', 'Счётчик слов, что умею, монетки, ДЗ.', 'Каждый говорит, что получилось.'),
]
td = 'style="border:1px solid #CFE6F4;padding:6px 8px;vertical-align:top"'
th = 'style="background:#0A5C86;color:#fff;padding:7px 8px;text-align:left"'
rows = ''.join(f'<tr><td {td}><b>{a}</b></td><td {td}>{b}</td><td {td}>{c}</td><td {td}>{d}</td><td {td}>{e}</td></tr>' for a, b, c, d, e in ST)
PLAN = [
 ('embed', {'url': 'https://classroom.wowteach.ru/lessons/reading10/u3.html'}),
 ('text', {'html': '<div style="padding:16px 18px;background:#F2FAFE;border-radius:14px;border:2px solid #CFE6F4">'
   '<h3 style="margin:0 0 6px;color:#0A5C86">🔐 Как провести урок</h3>'
   '<p style="margin:0 0 8px">«Планы уроков» → этот урок → <b>«▶ Показ»</b>: урок откроется на весь экран. Демонстрируйте в Zoom <b>эту вкладку</b>.</p>'
   '<p style="margin:0 0 8px">Вверху выберите <b>30 мин</b> или <b>40 мин</b> — в режиме 40 появятся дополнительные экраны (фиолетовые точки внизу). '
   '<b>⭐ Extra</b> — игры «If time», если осталось время: «Взломщик», «Вставь букву», «Найди слово».</p>'
   '<p style="margin:0">Ученику к уроку нужны <b>тетрадь и ручка</b> — напомните заранее. Звуки букв играют по нажатию; слова можно произносить самому.</p></div>'}),
 ('text', {'html': '<h3>План урока · Lesson 3 · The Red Cup</h3>'
   '<div style="background:#fff;border:1px solid #CFE6F4;border-radius:12px;padding:12px 16px;margin:10px 0">'
   '<b>Пройдено:</b> s a t p i n m d o g · I, the, a. &nbsp; <b>Новое:</b> c k e u r · said, are, you. &nbsp; '
   '<b>Длительность:</b> 30 мин (40 — с экранами «+»). &nbsp; <b>История:</b> Агент X прислал сообщение «Run! Get the red cup.»</div>'
   f'<table style="width:100%;border-collapse:collapse;font-size:14px"><tr><th {th}>Этап</th><th {th}>Мин</th><th {th}>Цель</th><th {th}>Ход (индивидуально)</th><th {th}>В группе</th></tr>{rows}</table>'
   '<p style="margin-top:10px"><b>If time:</b> «Взломщик» (слово символами на время) · «Вставь букву» (c_t, s_n, r_d, p_n, k_d) · «Найди слово» в сетке.</p>'}),
 ('text', {'html': '<h3>Домашнее задание</h3><p>Материал <b>«Homework 3 · The Red Cup»</b> в этом же юните: новые буквы, звук → буква, слово ↔ картинка, '
   'сортировка /e/ и /u/, собери слово, впиши букву, история «верно / неверно», скороговорка вслух. «Материалы» → «Задать ДЗ» → ученик → отметить.</p>'}),
]

# ---------- проверки ----------
for t, p in HW:
    if t == 'quiz':
        for q in p['questions']: assert 0 <= q['correct'][0] < len(q['options']); assert len({o['text'] for o in q['options']}) == len(q['options'])
    if t == 'match': assert len({x['right'] for x in p['pairs']}) == len(p['pairs'])
    if t == 'order':
        for it in p['items']: assert ''.join(it['words']) == it['sentence']
    if t == 'gaps': assert len(re.findall(r'__[^_]+__', p['text'])) == len(GW)
used = set(re.findall(r'media/reading10/u3/([a-z_]+)\.webp', json.dumps([HW, PLAN])))
miss = [u for u in used if not os.path.exists(os.path.join(HERE, '../../../media/reading10/u3', u + '.webp'))]
assert not miss, miss
learned = set('satpinmdogckeur'); tricky = {'i', 'the', 'a', 'said', 'are', 'you'}
for w in re.findall(r'[A-Za-z]+', CHANT + ' ' + STORY.split('</p><p')[1] + ' ' + ' '.join(MW + [w for w, _ in GW] + ['pen', 'ten', 'red', 'net', 'sun', 'cup', 'run', 'mug'])):
    lw = w.lower()
    if lw in tricky or lw in ('style', 'font', 'size', 'em', 'line', 'height', 'br', 'p'): continue
    assert set(lw) <= learned, w
print('проверки ок; заданий ДЗ:', len(HW) - 2)

def blk(lesson_var, rows):
    out = []
    for k, (t, p) in enumerate(rows):
        js = json.dumps(p, ensure_ascii=False)
        assert '$blk$' not in js
        out.append(f"  ({lesson_var}, '{t}', $blk${js}$blk$::jsonb, {k})")
    return ',\n'.join(out)
sql = f"""-- Reading Club 10+ · урок 3: курс, юнит, план (kind=lesson) и ДЗ (kind=homework). Черновики.
do $$
declare v_course uuid; v_unit uuid; v_plan uuid; v_hw uuid;
begin
  select id into v_course from classroom_courses where slug = 'reading10';
  if v_course is null then
    insert into classroom_courses (slug, title, description, sort_order)
    values ('reading10', 'Reading Club 10+', 'Курс чтения (фоника) для 10–12 лет · 10 уроков', 10) returning id into v_course;
  end if;
  select id into v_unit from classroom_units where course_id = v_course and sort_order = 1;
  if v_unit is null then
    insert into classroom_units (course_id, title, sort_order) values (v_course, 'Module 1 · Code', 1) returning id into v_unit;
  end if;
  select id into v_plan from classroom_lessons where unit_id = v_unit and sort_order = 2 and kind = 'lesson';
  if v_plan is null then
    insert into classroom_lessons (unit_id, title, kind, sort_order, is_published) values (v_unit, 'Lesson 3 · The Red Cup', 'lesson', 2, false) returning id into v_plan;
  end if;
  select id into v_hw from classroom_lessons where unit_id = v_unit and sort_order = 12 and kind = 'homework';
  if v_hw is null then
    insert into classroom_lessons (unit_id, title, kind, sort_order, is_published) values (v_unit, 'Homework 3 · The Red Cup', 'homework', 12, false) returning id into v_hw;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
{blk('v_plan', PLAN)}
  on conflict (lesson_id, sort_order) do update set type = excluded.type, payload = excluded.payload;
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
{blk('v_hw', HW)}
  on conflict (lesson_id, sort_order) do update set type = excluded.type, payload = excluded.payload;
end $$;
"""
open(os.path.join(HERE, 'sql', 'u3.sql'), 'w').write(sql); print(len(sql), 'байт')
