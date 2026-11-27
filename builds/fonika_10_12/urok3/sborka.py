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
ANCH = [('c', None, 'кошка (cat) · звук /k/'), ('k', None, 'ключ (key) · звук /k/'), ('e', None, 'яйцо (egg) · звук /e/'), ('u', None, 'зонт (umbrella) · звук /ʌ/'), ('r', None, 'ракета (rocket) · звук /r/')]
HW.append(('flashcards', {'title': 'Новые буквы. Нажми на карточку — услышишь звук буквы.',
  'cards': [{'text': l, 'image': img(p) if p else 'https://classroom.wowteach.ru/media/reading10/cipher/' + l + '.webp', 'audio': Z + l + '.mp3', 'translation': t} for l, p, t in ANCH]}))
QZ = [('e', ['e', 'a', 'i']), ('u', ['o', 'u', 'a']), ('r', ['n', 'm', 'r']), ('c', ['c', 'd', 'g']), ('k', ['t', 'k', 'p'])]
HW.append(('quiz', {'title': 'Послушай звук и выбери букву.',
  'questions': [{'q': '', 'type': 'single', 'audio': Z + s + '.mp3', 'correct': [o.index(s)], 'options': [{'text': x} for x in o]} for s, o in QZ]}))
READW = ['cat', 'kid', 'pen', 'sun', 'red', 'cup', 'rat', 'net', 'dog', 'map', 'sit', 'tap']
HW.append(('speaking', {'title': 'Прочитай слова вслух и запиши себя 🎤',
  'html': '<p style="font-size:1.5em;line-height:1.7;word-spacing:.4em">' + ' · '.join(READW) + '</p>',
  'sample': '', 'sample_tts': tts(', '.join(READW)), 'needs_review': True}))
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
PHR = ['a red cup', 'a pet rat', 'Sam and Dan', 'Get the pen!', 'Run, Dan, run!']
HW.append(('speaking', {'title': 'Прочитай фразы вслух и запиши себя 🎤',
  'html': '<p style="font-size:1.4em;line-height:1.8">' + '<br>'.join(PHR) + '</p>',
  'sample': '', 'sample_tts': tts('. '.join(PHR)), 'needs_review': True}))
STORY = ('<p><img src="' + img('scene_cup') + '" alt="" style="height:auto;max-width:100%;border-radius:12px"></p>'
  '<p style="font-size:1.25em;line-height:1.6">“Run! Get the red cup!” said Sam.<br>The red cup sits on a mat.<br>'
  'Dan gets it. In the cup — a map!<br>Sam and Dan run.</p>')
HW.append(('quiz', {'title': 'Прочитай историю и ответь: верно или неверно?', 'material': STORY,
  'questions': [{'q': q, 'type': 'single', 'correct': [0 if y else 1], 'options': [{'text': 'Верно'}, {'text': 'Неверно'}]}
                for q, y in [('The cup is red.', 1), ('The cup sits on a pen.', 0), ('In the cup — a map.', 1)]]}))
STORYTXT = '"Run! Get the red cup!" said Sam. The red cup sits on a mat. Dan gets it. In the cup — a map! Sam and Dan run.'
HW.append(('speaking', {'title': 'Прочитай историю вслух и запиши себя 🎤',
  'html': STORY, 'sample': '', 'sample_tts': tts(STORYTXT), 'needs_review': True}))
CHANT = 'Run, run, run in the sun!\nGet a cup, get a nut!\nA red cat, a red pen,\nTen red cups — run, run, run!'
HW.append(('speaking', {'title': 'Прочитай вслух скороговорку и запиши себя 🎤',
  'html': '<p style="font-size:1.3em;line-height:1.6">' + CHANT.replace('\n', '<br>') + '</p>',
  'sample': '', 'sample_tts': tts(CHANT.replace('\n', ' ')), 'needs_review': True}))
HW.append(('text', {'html': f'<p><img src="{img("dan_wave")}" alt="" style="height:auto;max-width:140px;float:right;margin:0 0 8px 12px">'
  '<b>Миссия выполнена!</b></p><p>Новое сообщение Агента X придёт на следующем уроке. До встречи, агент!</p>'}))

# ---------- ПЛАН УРОКА ----------
# (этап, мин, что делаем — рус., teacher's language, student's language, примечания)
ST = [
 ('1 · Mission', '1', 'Мотивация: пришло сообщение, часть значков ещё не знаем.', '"New message from Agent X! Look — some code is new."', '"We can\'t read it!"', 'Старые буквы уже вписаны, новые — серые. Сообщение прочитаем в конце урока.'),
 ('2 · Agent check', '1,5', 'Минутная проверка: ученик называет звуки всех значков в ключе.', '"Say the sounds! Go!"', '/s/, /æ/, /t/, /p/…', 'Нажатие — зелёная рамка и звук. Ошибся — нажмите ещё раз: рамка станет красной. Красные — повторить в уроке и отметить для себя.'),
 ('3 · Tricky words', '0,5', 'Повтор слов-исключений прошлых уроков.', '"Read the tricky words."', '"I · the · a"', 'Читаются целиком, по звукам не разбираем.'),
 ('4 · Chant', '0,5', 'Скороговорка урока 2, строки 3–4.', '"Read slowly… now fast!"', '"A dog, a pot, a map, a pan — Dig it, Sam! Dig it, Dan!"', 'Кнопки 🐢 / ⚡ подсвечивают слова в ритме.'),
 ('+ Speed run', '+3', 'Беглость: 18 слов на время.', '"Read fast! Go!"', 'sat, pin, dog, map…', 'Рекорд сохраняется. Сравниваем только с собой.'),
 ('5 · HW check', '1', 'Ошибки ДЗ.', '"Read this word. Sound by sound."', '"p-e-n — pen."', '1–2 слова из «Журнала ДЗ».'),
 ('6–10 · New code ×5', '3', 'Новые звуки c, k, e, u, r — экран на букву.', '"Tap to unlock! This is c. Sound /k/. Cat. Say /k/."', '"/k/ /k/ /k/ — cat."', 'c и k — одна буква-звук /k/ (скажите по-русски). e — короткое «э» без «й»; u — ближе к «а»; r — язык не дрожит. Значок попадает в ключ внизу.'),
 ('11 · Hear it', '1,5', 'Фонематический слух: есть ли звук /e/.', '"Listen. Do you hear /e/?"', '"Yes!" / "No!"', 'pen, pin, ten, tan, net, nut. Затем устно разделить: c-a-t, r-e-d.'),
 ('12 · Write it', '1,5', 'Письмо новых букв по прописям.', '"Look. Start at 1. Follow the arrows. Write c — three times."', '(пишет, говорит звук)', 'Ученик пишет и одновременно произносит звук — так буква запоминается быстрее.'),
 ('13 · Copy', '1', 'Списать слова.', '"Copy: cat, red. Show me!"', '(показывает тетрадь)', '—'),
 ('+ Copy more', '+2', 'Списать ещё 3 слова.', '"Copy and check."', 'sun, kid, pen', ''),
 ('14 · Blending', '3', 'Слияние звуков в слово.', '"Tap the letters. Say the sounds. Blend. Read!"', '"c-a… cat!"', 'Приём «слияние» — см. «Приёмы» выше. После последнего слова — «✔ Done →».'),
 ('15 · Word chain', '1,5', 'Цепочка: меняется одна буква.', '"One letter is new. Read!"', 'rat → cat → cut → cup → pup → pop → pot → pet → pen → ten', 'Новая буква — розовая. Самый сильный приём на внимание к каждой букве.'),
 ('+ Real or fake?', '+3', 'Чтение без угадывания.', '"Read it. Real or fake?"', '"Dut — fake!"', 'Выдуманные слова тоже читаются вслух.'),
 ('16 · Word building', '1,5', 'Собрать слово из букв-магнитов.', '"Make the word."', 'c-a-t', 'Ошибся — нажать на последнюю букву в слове.'),
 ('17 · Tricky words', '1', 'Новые слова-исключения.', '"These words are tricky. Remember them!"', '"said · are · you"', 'По-русски: «читаются не по правилам, запоминаем целиком».'),
 ('18 · Read', '0,5', 'Слова-исключения во фразе.', '"Read."', '"You are a cat!" said Sam.', ''),
 ('19 · Dictation', '3', 'Письмо на слух.', '"Listen and write."', 'pen · cup · rat · kit', 'Приём «звуки на пальцах»: ученик говорит слово, отгибает палец на каждый звук, пишет по звуку. Check — сверка.'),
 ('+ Dictation', '+2', 'Фраза на слух.', '"Listen and write."', 'a red cup', ''),
 ('20 · Phrases', '0,5', 'Чтение фраз.', '"Read."', 'a red cup · a pet rat · Sam and Dan', ''),
 ('21 · Decode', '1', 'Расшифровка: старые буквы вписаны, новые открывает ученик.', '"Tap the new code. Read the message!"', '"Run! Get the red cup."', 'Слова-исключения стоят в сообщении целиком.'),
 ('22 · Story', '1,5', 'Чтение текста.', '"Read the story."', '(читает 4 строки)', 'Перед чтением по-русски: ребята расшифровали сообщение и бегут в столовую.'),
 ('23 · True or false?', '0,5', 'Понимание.', '"True or false?"', '"True!" / "False!"', ''),
 ('24 · Chant', '0,5', 'Скороговорка урока 3, строки 1–2.', '"Read slowly… now fast!"', '"Run, run, run in the sun! Get a cup, get a nut!"', 'Строки 3–4 — в начале урока 4.'),
 ('25 · Now I can', '1', 'Итог (I CAN).', '"What can you do now?"', '"I can read c, k, e, u, r!"', 'Ученик отмечает галочки; счётчик слов. По-русски: что получилось сегодня.'),
 ('26 · Assign HW', '1', 'Выдать ДЗ.', '"Your homework: read aloud!"', '—', '«Материалы» → «Задать ДЗ» → «Homework 3 · The Red Cup». Скажите: в ДЗ много чтения вслух.'),
 ('27 · Finishing', '2', 'Обратная связь в обе стороны, оценка урока.', '"Well done, agent! How was the mission?"', '"Easy!" / "OK" / "Hard"', 'Монетки — за что. Что получилось хорошо + над чем поработать. Что было лёгким и трудным. Звёзды. Зацепка: «Куда ведёт карта? — Mission 4».'),
]
td = 'style="border:1px solid #CFE6F4;padding:6px 8px;vertical-align:top"'
th = 'style="background:#0A5C86;color:#fff;padding:7px 8px;text-align:left"'
rows = ''.join(f'<tr><td {td}><b>{a}</b><br><span style="color:#6F6A8A">{b} мин</span></td><td {td}>{c}</td><td {td}><i>{d}</i></td><td {td}>{e}</td><td {td}>{f}</td></tr>' for a, b, c, d, e, f in ST)
PRIEMY = ('<div style="background:#fff;border:1px solid #CFE6F4;border-radius:12px;padding:12px 16px;margin:10px 0">'
 '<b>Приёмы — одинаковые на всех уроках</b>'
 '<p style="margin:6px 0"><b>Слияние (blending).</b> Звуки не «рубим» по одному. Тянущиеся звуки (s, m, n, a, e…) тянем и сразу ведём к следующему: «ssa-a-a-t → sat». Короткие (c, k, t, p, d, g) не тянутся — соединяем с гласной: «ca… t → cat». Учитель показывает (I do) → вместе (We do) → ученик сам (You do).</p>'
 '<p style="margin:6px 0"><b>Ошибка.</b> Не называть слово за ученика. Показать на букву: <i>"What sound?"</i> → ученик называет → <i>"Blend again."</i> → читает слово заново. Ошибся в звуке дважды — отметить для «Agent check» следующего урока.</p>'
 '<p style="margin:6px 0"><b>Звуки.</b> Звук, а не имя буквы: «к», а не «си». Без призвука «э» на конце (не «пэ», а «п»). u — ближе к русскому «а»; e — короткое «э» без «й»; r — язык не дрожит.</p>'
 '<p style="margin:6px 0"><b>Экран ученика</b> — только короткие инструкции по-английски. Историю, задания и объяснения даёт учитель.</p></div>')
PLAN = [
 ('embed', {'url': 'https://classroom.wowteach.ru/lessons/reading10/u3.html'}),
 ('text', {'html': '<div style="padding:16px 18px;background:#F2FAFE;border-radius:14px;border:2px solid #CFE6F4">'
   '<h3 style="margin:0 0 6px;color:#0A5C86">🔐 Как провести урок</h3>'
   '<p style="margin:0 0 8px">«Планы уроков» → этот урок → <b>«▶ Показ»</b>: урок откроется на весь экран. Демонстрируйте в Zoom <b>эту вкладку</b>. На экране ученика — только короткие инструкции по-английски: историю, задания и объяснения даёт учитель по этому плану.</p>'
   '<p style="margin:0 0 8px">Вверху справа выберите <b>30</b> или <b>40</b> минут — в режиме 40 появятся дополнительные экраны (розовые точки внизу). '
   '<b>⭐ Extra</b> — игры «If time», если осталось время: Code breaker, What\'s missing?, Find 5 words. Листать можно стрелками на клавиатуре.</p>'
   '<p style="margin:0">Ученику к уроку нужны <b>тетрадь и ручка</b> — напомните заранее. Звуки букв играют по нажатию; слова можно произносить самому.</p></div>'}),
 ('text', {'html': '<h3>План урока · Lesson 3 · The Red Cup</h3>'
   '<div style="background:#fff;border:1px solid #CFE6F4;border-radius:12px;padding:12px 16px;margin:10px 0">'
   '<b>Пройдено:</b> s a t p i n m d o g · I, the, a. &nbsp; <b>Новое:</b> c k e u r · said, are, you. &nbsp; '
   '<b>Длительность:</b> 30 мин (40 — с экранами «+»). &nbsp; <b>История:</b> Агент X прислал сообщение «Run! Get the red cup.» &nbsp; <b>К концу урока ученик:</b> называет звуки c k e u r, читает слова из пройденных букв, пишет их на слух, читает 4 строки истории. &nbsp; <b>Материалы:</b> тетрадь и ручка у ученика.</div>'
   + PRIEMY +
   f'<table style="width:100%;border-collapse:collapse;font-size:14px"><tr><th {th}>Этап</th><th {th}>Что делаем</th><th {th}>Teacher\'s language</th><th {th}>Student\'s language</th><th {th}>Примечания</th></tr>{rows}</table>'
   '<p style="margin-top:10px"><b>If time (⭐ Extra):</b> Code breaker — слово символами, ввести на время · What\'s missing? — c_t, s_n, r_d, p_n, k_d · Find 5 words — сетка букв.</p>'}),
 ('text', {'html': '<h3>Домашнее задание</h3><p>Материал <b>«Homework 3 · The Red Cup»</b> в этом же юните: новые буквы, звук → буква, <b>слова вслух</b>, слово ↔ картинка, '
   'сортировка /e/ и /u/, собери слово, впиши букву, <b>фразы вслух</b>, история «верно / неверно», <b>история вслух</b>, скороговорка вслух. В ДЗ много чтения вслух. «Материалы» → «Задать ДЗ» → ученик → отметить.</p>'}),
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
for w in re.findall(r'[A-Za-z]+', CHANT + ' ' + STORYTXT + ' ' + ' '.join(READW + PHR + MW + [w for w, _ in GW] + ['pen', 'ten', 'red', 'net', 'sun', 'cup', 'run', 'mug'])):
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
