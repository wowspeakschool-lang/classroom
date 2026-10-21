"""Halloween: планы уроков (kind='lesson') и домашки (kind='homework') — курс Holidays, юнит Halloween."""
import sys, re, json, random
sys.path.insert(0, '/home/user/classroom/tools')
import lib as L
from lib import Lesson

L.setup('Halloween', 1, 'halloween', course='holidays')
U = L.url                       # U('7-9/w_ghost') -> @@MEDIA@@halloween/7-9/w_ghost.webp
SH = L.surl
LESSON_URL = 'https://classroom.wowteach.ru/lessons/halloween/'


def strip(w):
    return re.sub(r'^(a|an|the) ', '', w)


def accept(w):
    b = strip(w)
    out = [b, b[:1].upper() + b[1:]]
    if b != w:
        out += [w, w[:1].upper() + w[1:]]
    return out


def cards(ws, title='Карточки: смотри, слушай, повторяй', tr=None):
    cs = []
    for k, w in ws:
        c = {'text': w, 'image': U(k), 'audio_tts': strip(w) if w.startswith('a ') else w}
        if tr:
            c['translation'] = tr[k]
        cs.append(c)
    return {'title': title, 'cards': cs}


def repeat(ws, title='🎤 Повтори слова'):
    tiles = ''.join(f'<div style="display:inline-block;text-align:center;margin:6px 10px"><img src="{U(k)}" alt="" style="height:110px"><br><b>{strip(w)}</b></div>' for k, w in ws)
    return {'title': title, 'html': '<p>Нажми на запись и скажи по-английски все слова по порядку.</p>' + tiles}


def listen(ws, seed, title='🔊 Послушай и выбери картинку'):
    rnd = random.Random(seed)
    qs = []
    for k, w in rnd.sample(ws, len(ws)):
        others = rnd.sample([x for x in ws if x[0] != k], 2)
        opts = [(k, w)] + others
        rnd.shuffle(opts)
        qs.append({'q': '', 'type': 'single', 'audio_tts': strip(w), 'correct': [opts.index((k, w))],
                   'options': [{'text': strip(o[1]), 'image': U(o[0])} for o in opts]})
    return {'title': title, 'questions': qs}


def yesno(ws, seed, title='🔊 Послушай: это то слово? 👍 или 👎'):
    rnd = random.Random(seed)
    qs = []
    pairs = [(x, x) for x in ws] + [(x, rnd.choice([y for y in ws if y != x])) for x in ws]
    rnd.shuffle(pairs)
    for (k, w), (k2, w2) in pairs:
        yes = k == k2
        qs.append({'q': '', 'type': 'single', 'image': U(k), 'audio_tts': strip(w2), 'correct': [0 if yes else 1],
                   'options': [{'text': 'Yes', 'image': SH('yes_thumb_up')}, {'text': 'No', 'image': SH('no_thumb_down')}]})
    return {'title': title, 'questions': qs}


def same(ws, title='Найди одинаковые картинки и назови их'):
    return {'title': title, 'pairs': [{'left_image': U(k), 'right': strip(w), 'right_image': U(k)} for k, w in ws]}


def match(ws, title='Соедини картинку и слово'):
    return {'title': title, 'pairs': [{'left_image': U(k), 'right': strip(w), 'right_audio_tts': strip(w)} for k, w in ws]}


def unscramble(ws, seed, title='Собери слово из букв'):
    items = []
    for i, (k, w) in enumerate(ws):
        b = strip(w)
        items.append({'prompt': L.scramble(b.upper(), seed + i).replace(' / ', '   '), 'image': U(k), 'accept': accept(w)})
    return {'title': title, 'items': items}


def dictation(ws, title='🔊 Послушай и напиши слово'):
    return {'title': title, 'items': [{'prompt': '', 'audio_tts': strip(w), 'accept': accept(w)} for k, w in ws]}


def speak(title, html, image):
    return {'title': title, 'html': html, 'image': U(image)}


# ---------------- слова ----------------
W46 = [('4-6/word_ghost', 'ghost'), ('4-6/word_bat', 'bat'), ('4-6/word_spider', 'spider'), ('4-6/word_monster', 'monster')]
W7B = [('7-9/w_ghost', 'a ghost'), ('7-9/w_bat', 'a bat'), ('7-9/w_spider', 'a spider'), ('7-9/w_witch', 'a witch'), ('7-9/w_pumpkin', 'a pumpkin'), ('7-9/w_skeleton', 'a skeleton')]
W7C = [('7-9/w_ghost', 'a ghost'), ('7-9/w_spider', 'a spider'), ('7-9/w_witch', 'a witch'), ('7-9/w_skeleton', 'a skeleton'),
       ('7-9/w_vampire', 'a vampire'), ('7-9/w_mummy', 'a mummy'), ('7-9/w_broom', 'a broom'), ('7-9/w_house', 'a haunted house')]
WM = [('10-12/s_witch', 'a witch'), ('10-12/s_vampire', 'a vampire'), ('10-12/s_mummy', 'a mummy'), ('10-12/s_werewolf', 'a werewolf'), ('10-12/s_skeleton', 'a skeleton'), ('10-12/s_ghost', 'a ghost')]
WC = [('10-12/o_watch', 'a watch'), ('10-12/o_scarf', 'a scarf'), ('10-12/o_glasses', 'glasses'), ('10-12/o_boot', 'boots'), ('10-12/o_lollipops', 'lollipops'), ('10-12/o_ticket', 'a ticket')]
W13B = [('13/w_pumpkin', 'a pumpkin'), ('13/w_turnip', 'a turnip'), ('13/w_bonfire', 'a bonfire'), ('13/w_costume', 'a costume'), ('13/w_ghost', 'a ghost'), ('13/w_candle', 'a candle')]
W13C = W13B + [('13/w_lantern', 'a lantern'), ('13/w_harvest', 'the harvest')]
TR13 = {'13/w_pumpkin': 'тыква', '13/w_turnip': 'репа', '13/w_bonfire': 'костёр', '13/w_costume': 'костюм', '13/w_ghost': 'привидение',
        '13/w_candle': 'свеча', '13/w_lantern': 'фонарь', '13/w_harvest': 'урожай'}

HW = []


# Фон страницы домашки (решение Анны 21.10.2026): ночь с тыквами из урока
# своего возраста для 4–6 и 7–9, улица с фонарями для 10–12 и 13+.
# Платформа берёт его из `page_bg` в payload первого блока.
PAGE_BG = {10: '4-6/bg_night.webp', 11: '7-9/bg7_night.webp', 12: '7-9/bg7_night.webp'}


def hw(title, summary, order, blocks):
    les = Lesson(title, summary, order, kind='homework', threshold=60)
    blocks[0][1]['page_bg'] = 'https://classroom.wowteach.ru/media/halloween/' + PAGE_BG.get(order, 'hw_bg_street.webp')
    for t, p, c in blocks:
        les.add(t, p, c)
    HW.append(les)


hw('Halloween Homework · 4–6', 'Хэллоуин: ghost, bat, spider, monster', 10, [
    ('flashcards', cards(W46, 'Посмотри карточки, послушай и повтори'), ''),
    ('quiz', listen(W46, 46, '🔊 Послушай и выбери картинку'), ''),
    ('match', same(W46, 'Найди одинаковые картинки и назови их'), 'вместо игры «найди пару»'),
    ('quiz', yesno(W46, 47, '🔊 Послушай: это то слово? 👍 или 👎'), ''),
    ('speaking', speak('🎤 Что ты видишь?', '<p>Нажми на запись и назови всё, что видишь на картинке.</p><p><i>ghost, bat, spider, monster…</i></p>', '4-6/hw_scene'), ''),
])
hw('Halloween Homework · 7–9 · beginners', 'Хэллоуин: ghost, bat, spider, witch, pumpkin, skeleton', 11, [
    ('flashcards', cards(W7B), ''),
    ('speaking', repeat(W7B), ''),
    ('quiz', listen(W7B, 71), ''),
    ('match', same(W7B), 'вместо игры «найди пару»'),
    ('match', match(W7B), ''),
    ('speaking', speak('🎤 Что ты видишь?', '<p>Нажми на запись и назови всё, что видишь на картинке.</p><p><i>I can see a ghost, a bat…</i></p>', '7-9/hw_scene_b'), ''),
])
ROOMQ = lambda s, opts, a, img=None: dict({'q': s, 'type': 'single', 'correct': [a], 'options': [{'text': o} for o in opts]}, **({'image': U(img)} if img else {}))
hw('Halloween Homework · 7–9 · continuing', 'Хэллоуин: 8 слов, there is / there are, in / on / under', 12, [
    ('flashcards', cards(W7C), ''),
    ('match', match(W7C), ''),
    ('exact_input', unscramble(W7C, 700), ''),
    ('quiz', {'title': 'Посмотри на картинку: is или are?', 'questions': [
        ROOMQ('There ___ a witch in the room.', ['is', 'are'], 0, '7-9/hw_room'),
        ROOMQ('There ___ three pumpkins under the bed.', ['is', 'are'], 1, '7-9/hw_room'),
        ROOMQ('There ___ a ghost on the bed.', ['is', 'are'], 0, '7-9/hw_room'),
        ROOMQ('There ___ two spiders on the table.', ['is', 'are'], 1, '7-9/hw_room'),
        ROOMQ('There ___ a mummy in the box.', ['is', 'are'], 0, '7-9/hw_room'),
        ROOMQ('There ___ a vampire next to the window.', ['is', 'are'], 0, '7-9/hw_room')]}, ''),
    ('quiz', {'title': 'In, on или under?', 'questions': [
        ROOMQ('The ghost is ___ the bed.', ['in', 'on', 'under'], 1, '7-9/hw_r_ghostbed'),
        ROOMQ('The pumpkins are ___ the bed.', ['in', 'on', 'under'], 2, '7-9/hw_r_pumpkins'),
        ROOMQ('The spiders are ___ the table.', ['in', 'on', 'under'], 1, '7-9/hw_r_spiders'),
        ROOMQ('The broom is ___ the table.', ['in', 'on', 'under'], 2, '7-9/hw_r_broom'),
        ROOMQ('The mummy is ___ the box.', ['in', 'on', 'under'], 0, '7-9/hw_r_mummy'),
        ROOMQ('The skeleton is ___ the chair.', ['in', 'on', 'under'], 1, '7-9/hw_r_skeleton')]}, ''),
    ('truefalse', {'title': 'Посмотри на картинку: верно или неверно?', 'image': U('7-9/hw_room'), 'statements': [
        {'text': 'There is a ghost on the bed.', 'correct': True}, {'text': 'There are two pumpkins under the bed.', 'correct': False},
        {'text': 'The broom is on the table.', 'correct': False}, {'text': 'There is a mummy in the box.', 'correct': True},
        {'text': 'The skeleton is on the chair.', 'correct': True}, {'text': 'There are three spiders on the table.', 'correct': False}]}, ''),
    ('speaking', speak('🎤 Расскажи про комнату', '<p>Нажми на запись и расскажи, что есть в комнате и где.</p><p><i>There is a ghost on the bed. There are three pumpkins under the bed. The broom is under the table…</i></p>', '7-9/hw_room'), ''),
])
hw('Halloween Homework · 10–12 · beginners', 'Хэллоуин: witch, vampire, mummy, werewolf, skeleton, ghost', 13, [
    ('flashcards', cards(WM), ''),
    ('speaking', repeat(WM), ''),
    ('quiz', listen(WM, 101), ''),
    ('match', match(WM), ''),
    ('exact_input', unscramble(WM, 1000), ''),
    ('speaking', speak('🎤 Что ты видишь?', '<p>Нажми на запись и назови всё, что видишь на картинке.</p><p><i>I can see a witch, a vampire…</i></p>', '10-12/hw_scene_b'), ''),
])
ODD = [(['s_witch', 's_mummy', 'o_scarf', 's_vampire'], 'o_scarf'), (['o_watch', 'o_glasses', 's_ghost', 'o_boot'], 's_ghost'),
       (['s_skeleton', 'o_ticket', 's_werewolf', 's_witch'], 'o_ticket'), (['o_lollipops', 'o_scarf', 'o_watch', 's_mummy'], 's_mummy'),
       (['s_vampire', 's_ghost', 'o_boot', 's_skeleton'], 'o_boot')]
WD10 = dict((k.split('/')[1], w) for k, w in WM + WC)
GOLD = ('Last night someone stole the Golden Pumpkin! The detectives found a broken __watch__ in the square. It stopped at 9:15. '
        'A witness saw a long red __scarf__ in the park. Next to the old tower there were footprints of somebody in big __boots__. '
        'Somebody ate all the __lollipops__ at the cafe. Is the thief the __vampire__ in the black cape? Or the hairy __werewolf__? '
        'The __mummy__ has got an alibi: a cinema __ticket__ for nine o\'clock.')
hw('Halloween Homework · 10–12 · continuing', 'Хэллоуин: 6 монстров + улики (watch, scarf, glasses, boots, lollipop, ticket)', 14, [
    ('flashcards', cards(WM + WC), ''),
    ('match', match(WM), ''),
    ('match', match(WC), ''),
    ('quiz', {'title': 'Найди лишнюю картинку', 'questions': [
        {'q': '', 'type': 'single', 'correct': [ks.index(odd)], 'options': [{'text': strip(WD10[k]), 'image': U('10-12/' + k)} for k in ks]} for ks, odd in ODD]}, ''),
    ('exact_input', unscramble(random.Random(5).sample(WM + WC, 8), 1100), ''),
    ('exact_input', dictation(random.Random(6).sample(WM + WC, 6)), ''),
    ('gaps', {'mode': 'drag', 'title': 'The Golden Pumpkin: вставь слова', 'text': GOLD}, ''),
    ('speaking', speak('🎤 Опиши подозреваемого', '<p>Нажми на запись и расскажи, что ты видишь на картинке.</p><p><i>I can see a vampire. I can see a red scarf, glasses…</i></p>', '10-12/hw_suspect'), ''),
])
hw('Halloween Homework · 13+ · beginners', 'Хэллоуин: pumpkin, turnip, bonfire, costume, ghost, candle', 15, [
    ('flashcards', cards(W13B), ''),
    ('speaking', repeat(W13B), ''),
    ('quiz', listen(W13B, 131), ''),
    ('match', match(W13B), ''),
    ('exact_input', unscramble(W13B, 1300), ''),
    ('speaking', speak('🎤 Что ты видишь?', '<p>Нажми на запись и назови всё, что видишь на картинке.</p><p><i>I can see a bonfire, a pumpkin…</i></p>', '13/hw_scene_b'), ''),
])
DEF = [('pumpkin', 'a big orange vegetable; people carve faces in it on Halloween'),
       ('turnip', 'a round white-and-purple vegetable; the first lanterns were made from it'),
       ('bonfire', 'a big fire outside'), ('costume', 'clothes you wear to look like someone or something else'),
       ('ghost', 'the spirit of a dead person'), ('candle', 'a stick of wax that gives light when it burns'),
       ('lantern', 'a light in a case that you can carry'), ('harvest', 'the time when farmers collect fruit and vegetables')]
SAM = ('Long ago in Ireland, people celebrated Samhain at the end of the __harvest__. They made big __bonfires__ on the hills. '
       'They believed that __ghosts__ could walk on Earth that night, so they wore __costumes__ and masks. '
       'Children carved a scary face into a __turnip__, put a __candle__ inside and made a __lantern__. '
       'Later, in America, people used a __pumpkin__ instead.')
hw('Halloween Homework · 13+ · continuing', 'Хэллоуин: 8 слов с переводом, текст о Самайне', 16, [
    ('flashcards', cards(W13C, 'Новые слова: слово, перевод, звук', TR13), ''),
    ('match', {'title': 'Соедини слово и определение', 'pairs': [{'left': w, 'right': d, 'left_audio_tts': w} for w, d in DEF]}, ''),
    ('exact_input', unscramble(W13C, 1350), ''),
    ('exact_input', dictation(random.Random(7).sample(W13C, 6)), ''),
    ('gaps', {'mode': 'drag', 'title': 'Samhain: вставь слова', 'text': SAM}, ''),
    ('truefalse', {'title': 'Прочитай текст ещё раз: верно или неверно?', 'statements': [
        {'text': 'Samhain was at the end of the harvest.', 'correct': True}, {'text': 'People made bonfires in their houses.', 'correct': False},
        {'text': 'People wore costumes and masks.', 'correct': True}, {'text': 'The first lanterns were made from pumpkins.', 'correct': False},
        {'text': 'Children put a candle inside the turnip.', 'correct': True}, {'text': 'In America people used a pumpkin.', 'correct': True}]}, ''),
    ('speaking', speak('🎤 Как ты празднуешь Хэллоуин?',
        '<p>Прочитай пример. Нажми на запись и расскажи, как ты празднуешь Хэллоуин.</p>'
        '<p><i>On Halloween I wear a costume. This year I\'m a vampire! My friends and I carve a pumpkin and put a candle inside — now it\'s a lantern. '
        'In the evening we watch a scary film and eat lots of sweets. I don\'t believe in ghosts, but I love scary stories!</i></p>'
        '<p><b>What do you wear? Do you carve a pumpkin? What do you eat? What do you do in the evening?</b></p>', '13/lead13'), ''),
])

# ---------------- планы уроков ----------------
PLANS = []


def plan_html(path):
    s = open(path).read()
    h = json.loads(re.search(r'const PLAN_HTML=("(?:[^"\\]|\\.)*");', s).group(1))
    body = re.search(r'<body>(.*)</body>', h, re.S).group(1)
    body = re.sub(r'<h1>.*?</h1>', '', body, flags=re.S)
    box = 'background:#fff;border:1px solid #e6e0f0;border-radius:12px;padding:12px 16px;margin:10px 0'
    rep = {'meta': box, 'voc': box, 'warn': 'background:#fff3cd;border:3px solid #c0392b;border-radius:12px;padding:12px 16px;margin:10px 0;font-weight:700;color:#7a1f12',
           'pg': 'font-weight:700;color:#c0392b;font-size:17px;text-align:center;width:44px', 'tl': 'color:#1a7a3a;font-style:italic;width:22%',
           'sa': 'color:#1f5fa8;font-style:italic;width:22%', 'pron': 'border-collapse:collapse;margin:8px 0'}
    body = re.sub(r'class="([a-z]+)"(?: style="([^"]*)")?', lambda m: f'style="{rep.get(m.group(1), "")}{";" + m.group(2) if m.group(2) else ""}"', body)
    body = body.replace('<table>', '<table style="width:100%;border-collapse:collapse;font-size:14px">')
    body = body.replace('<th>', '<th style="background:#6e3510;color:#fff;padding:8px 10px;text-align:left">')
    body = re.sub(r'<td(?=[ >])', '<td style="padding:8px 10px;border-bottom:1px solid #eee;vertical-align:top"', body)
    body = re.sub(r'<td style="padding:8px 10px;border-bottom:1px solid #eee;vertical-align:top" style="([^"]*)"', r'<td style="padding:8px 10px;border-bottom:1px solid #eee;vertical-align:top;\1"', body)
    return body


def plan(title, summary, order, file, src, hwtitle):
    les = Lesson(title, summary, order, kind='lesson', threshold=60)
    url = LESSON_URL + file
    # урок — первым блоком: «▶ Показ» сразу открывает его на весь экран (платформа, 19.10.2026)
    les.add('embed', {'url': url}, 'интерактивный урок')
    les.text(f'''<div style="padding:16px 18px;background:#fff7ec;border-radius:14px;border:2px solid #f3d3a3">
<h3 style="margin:0 0 6px;color:#8a3c08">🎃 Как провести урок</h3>
<p style="margin:0 0 8px">«Планы уроков» → этот урок → <b>«▶ Показ»</b>: урок откроется на весь экран. Демонстрируйте в Zoom <b>эту вкладку</b>, а не весь экран.</p>
<p style="margin:0 0 8px">План урока — кнопка 📋 вверху справа внутри урока (откроется отдельным окном) или ниже на этой странице.</p>
<p style="margin:0">Если удобнее отдельной вкладкой: <a href="{url}">открыть урок</a>. Нужен интернет: картинки и музыка загружаются с сервера.</p></div>''', 'как провести — только преподавателю')
    les.text('<h3>План урока</h3>' + plan_html(src), 'план — только преподавателю')
    les.text(f'<h3>Домашнее задание</h3><p>Материал <b>«{hwtitle}»</b> в этом же юните. «Материалы» → «Задать ДЗ» → ученик → отметить.</p>', 'ДЗ — только преподавателю')
    les.audience = {0: 'shared', 1: 'teacher', 2: 'teacher', 3: 'teacher'}
    PLANS.append(les)


S = '/tmp/claude-0/-home-user-classroom/804eac6d-911f-5112-b4f5-c1e3887b7b56/scratchpad/'
plan('Halloween · 4–6', 'Урок-игра для 4–6 лет', 0, '4-6.html', S + 'halloween_lesson_4-6.html', 'Halloween Homework · 4–6')
for i, (age, f, src, lvl) in enumerate([
        ('7–9', '7-9_beginners.html', 'halloween_lesson_7-9_beginners.html', 'beginners'), ('7–9', '7-9_continuing.html', 'halloween_lesson_7-9_continuing.html', 'continuing'),
        ('10–12', '10-12_beginners.html', 'halloween_lesson_10-12_beginners.html', 'beginners'), ('10–12', '10-12_continuing.html', 'halloween_lesson_10-12_continuing.html', 'continuing'),
        ('13+', '13plus_beginners.html', 'halloween_lesson_13plus_beginners.html', 'beginners'), ('13+', '13plus_continuing.html', 'halloween_lesson_13plus_continuing.html', 'continuing')]):
    plan(f'Halloween · {age} · {lvl}', f'Урок-игра для {age} лет, {"начинающие" if lvl == "beginners" else "продолжающие"}', i + 1, f, S + src,
         f'Halloween Homework · {age} · {lvl}')

if __name__ == '__main__':
    import os
    os.makedirs('hwsql', exist_ok=True)
    for f in os.listdir('hwsql'):
        os.remove('hwsql/' + f)
    for i, les in enumerate(PLANS + HW):
        sql = les.sql()
        aud = getattr(les, 'audience', None)
        if aud:
            upd = '\n'.join(f"  update classroom_blocks set audience = '{a}' where lesson_id = v_lesson and sort_order = {so};" for so, a in aud.items())
            sql = sql.replace('\nend\n$mig$;', '\n' + upd + '\nend\n$mig$;')
            assert upd in sql
        fn = f'hwsql/{i:02d}_' + re.sub(r'[^a-z0-9]+', '_', les.title.lower()).strip('_') + '.sql'
        open(fn, 'w').write(sql)
        print(fn, len(les.blocks), 'блоков', len(sql) // 1024, 'KB')
