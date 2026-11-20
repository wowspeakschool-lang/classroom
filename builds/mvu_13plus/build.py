"""Сборка вводного урока 13+ → lessons/mvu_13plus/index.html + план (HTML/Word/PDF) в lessons/mvu_13plus/plans/.
python3 builds/mvu_13plus/build.py            — урок и html плана
python3 builds/mvu_13plus/build.py --docs     — ещё Word (LibreOffice) и PDF (Playwright)
"""
import json, os, re, sys, html, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import data

OUT = os.path.join(REPO, 'lessons', 'mvu_13plus'); os.makedirs(OUT + '/plans', exist_ok=True)
SITE = 'https://classroom.wowteach.ru/lessons/mvu_13plus/plans/'
AUDIO = 'https://api.wowteach.ru/storage/v1/object/public/classroom-media/mvu_13plus/'  # свой домен: supabase.co у части учеников не открывается
e = html.escape

# ── проверка данных ─────────────────────────────────────────────────────────────────────
media = set(f[:-5] for f in os.listdir(os.path.join(REPO, 'media', 'mvu_13plus')) if f.endswith('.webp'))
used, topics_used, problems = set(), set(), []
for P in data.PARTS:
    used.add(P['room'])
    for o in P['objects']:
        used.add(o['img']); topics_used.update(o['name_t'])
        for _, ts in o['you']: topics_used.update(ts)
        for t in o['tasks']:
            for k in ('image',):
                if t.get(k): used.add(t[k])
            for q in t.get('qs', []): topics_used.update(q[1])
            for it in t.get('items', []):
                topics_used.update(it.get('t', []))
                for g in it.get('gaps', []): topics_used.update(g)
                if it.get('gaps'):   # два пропуска — каждый неверный вариант неверен ровно в одном пропуске
                    parts = [x.split(' … ') for x in it['o']]
                    if any(len(p) != 2 for p in parts): problems.append(('gaps: вариант не из двух частей', it['q']))
                    elif any(sum(a != b for a, b in zip(p, parts[0])) != 1 for p in parts[1:]): problems.append(('gaps: неверный вариант должен отличаться ровно одним пропуском', it['q']))
                for k in ('img',):
                    if it.get(k): used.add(it[k])
                for x in it.get('img2', []): used.add(x)
                if 'o' in it and len(set(it['o'])) != len(it['o']): problems.append(('дубль вариантов', it['q']))
                if 'q' in it and it.get('o') and '___' not in it['q'] and not it['q'].endswith('?') and t['kind'] == 'choice':
                    pass
            if t['kind'] == 'match':
                rights = [it.get('img') or it.get('d') for it in t['items']]
                if len(set(rights)) != len(rights): problems.append(('match: правые не уникальны', t['title']))
used |= {'door_open'}
missing = sorted(u for u in used if u not in media)
all_topics = {data.tid(p['part'], bi, ti) for p in data.CHECKLIST for bi, (_, ts) in enumerate(p['blocks'], 1) for ti in range(1, len(ts) + 1)}
names_all = data.topic_names()
canon = lambda n: data.ALIAS.get(n, n)
covered_names = {canon(names_all[t]) for t in topics_used}
uncovered = sorted(t for t in all_topics - topics_used if canon(names_all[t]) not in covered_names)  # одинаковые темы получают балл друг от друга
if missing: print('!! нет картинок:', missing)
if uncovered:
    names = {data.tid(p['part'], bi, ti): t for p in data.CHECKLIST for bi, (_, ts) in enumerate(p['blocks'], 1) for ti, t in enumerate(ts, 1)}
    print('!! темы чек-листа без задания:', [(u, names[u]) for u in uncovered])
for p in problems: print('!!', p)
if missing or uncovered or problems:
    sys.exit(1)

# ── план урока ──────────────────────────────────────────────────────────────────────────
def ans(it):
    if 'o' in it and it.get('gaps'): return it['o'][0] + ' (каждый пропуск — свой балл)'
    if 'o' in it: return it['o'][0] + (f' → потом устно отвечает на вопрос: {it["then_exp"]} (оцените в «Сейчас на экране»)' if it.get('then') else '')
    if 'a' in it and isinstance(it['a'], bool): return 'True' if it['a'] else f'False → {it["fix"]}'
    if 'a' in it: return it['a']
    if 's' in it: return it['s']
    if it.get('suspect'): return 'suspect №1 (curly dark hair, beard, glasses, leather jacket)'
    if 'bad' in it: w = it['s'].split(' '); return f'ошибка «{w[it["bad"]]}» → {it["fix"]}: ' + ' '.join(it['fix'] if i == it['bad'] else x for i, x in enumerate(w))
    if 'w' in it: return it['w']
    return ''

KIND_RU = {'choice': 'выбор ответа', 'tf': 'верно / неверно', 'hotspot': 'стрелка на картинке, выбрать слово',
           'order': 'собрать предложение', 'sort': 'разложить по группам', 'match': 'соединить пары', 'listen': 'голосовое сообщение + вопросы',
           'oral': 'устные вопросы по картинке', 'fix': 'найти ошибку'}
HOW = {'choice': 'Пункты по одному: следующий — Next, предыдущий — ←.', 'hotspot': 'Пункты по одному: следующий — Next, предыдущий — ←.',
       'fix': 'Ученик нажимает на неверное слово и говорит предложение правильно вслух. Пункты по одному.',
       'order': 'Слова можно нажимать или перетаскивать; нажатие на слово в строке возвращает его назад. Верно/неверно видно только после кнопки «Check».',
       'sort': 'Картинки можно нажимать (потом нажать на группу) или перетаскивать; переложить можно до кнопки «Check». После разложения ученик называет каждую вещь вслух.',
       'match': 'Пары соединяются нажатием (левое → правое) или перетаскиванием; нажатие на левое снимает пару. Верно/неверно — только после «Check».',
       'listen': 'Слева запись, справа сразу все вопросы — ученик читает их до прослушивания и слушает один раз (можно ещё раз, если просит).',
       'oral': 'На экране картинка и один вопрос, вариантов нет; следующий вопрос — по Next. Спросите, ученик отвечает устно — оцените 0/1/2 в чек-листе ✅ («Сейчас на экране»).'}
rows = []
def row(step, do, tl, exp):
    rows.append(f'<tr><td class="st">{step}</td><td>{do}</td><td class="tl">{tl}</td><td class="sa">{exp}</td></tr>')
row('Старт', 'Вверху урока две кнопки: ✅ — чек-лист, 📋 — этот план. Каждая открывает своё окно. В чек-листе впишите имя ученика по-русски, пол и возраст — они попадут в отчёт. Демонстрируйте экран урока, оба окна держите на втором мониторе или рядом.', '—', '—')
row('1. Welcome', 'На экране только «Welcome to WowSpeak School!». Скажите сами (по-русски или по-английски): это не тест — мы просто познакомимся и посмотрим, что ты уже умеешь; отвечай как получается, ошибаться можно и нужно.', 'Hi! Welcome to WowSpeak School! This is not a test — it’s a game. Let’s have fun! Are you ready?', 'Yes! / I’m ready.')
row('2. Get to know you', 'Три вопроса по одной карточке: следующий — Next (или нажатие на карточку), предыдущий — ←. Баллов нет — смотрим, как ученик держится, и решаем, нужен ли облегчённый режим 💡.', 'What’s your name? How old are you? What do you like doing in your free time?', 'My name is… I’m 14. I like playing football / drawing…')
row('3. Briefing', 'На экране только название. Расскажите историю сами: дверь закрыта на кодовый замок, в комнате спрятаны кусочки старой записки с кодом; нажимай на предметы, называй их по-английски и выполняй задания — за каждое получишь кусочек записки. Сколько цифр в коде — не говорите.', 'You are locked in the escape room! Find the pieces of the secret note to open the door. Choose a glowing object and say what it is in English.', '—')
for P in data.PARTS:
    rows.append(f'<tr class="part"><td colspan="4">PART {P["n"]} · {e(P["room_name"])} · {len(P["objects"])} предметов → записка с {P["digits"]} цифрами</td></tr>')
    if P['n'] > 1:
        row(f'Переход в Part {P["n"]}', 'Только если в предыдущей части каждый блок ≥ 9 из 12 (или вы хотите проверить ещё пару заданий). Нажмите «Keep looking». На экране только название комнаты — расскажите сами: ' + e(P['intro']) + ' Не говорите «нам нужно ещё цифр» — просто нашлась новая комната.', e(P['intro_en']), '—')
    for o in P['objects']:
        name = o['name'].split(' — ')[0]
        row(f'🔎 {e(o["id"].replace("_", " "))}', 'Ученик выбирает предмет, вы нажимаете. <b>Назвать предмет</b>. Не знает по-английски — пусть назовёт по-русски, предмет всё равно открывается.'
            + (' Оцените в чек-листе ✅, панель «Сейчас на экране» (✓ / ~ / ✗).' if o['name_t'] else ' Без балла.'), e(o['ask']), e(o['name']))
        for t in o['tasks']:
            exp = '<br>'.join(e(ans(it)) for it in t.get('items', []) if ans(it))
            if t['kind'] == 'sort':
                exp = '<br>'.join(f'<b>{e(g)}:</b> ' + ', '.join(e(it['w']) for it in t['items'] if it['g'] == gi) for gi, g in enumerate(t['groups']))
            if t['kind'] == 'match':
                exp = '<br>'.join(f'{e(it["w"])} — {e(it["d"])}' for it in t['items']) if t.get('halves') else ', '.join(e(it['w']) for it in t['items']) + ' (к каждому слову — своя картинка)'
            if t['kind'] == 'hotspot':
                exp = ', '.join(it['a'] for it in t['items'])
            if t['kind'] == 'oral':
                exp = '<br>'.join(f'{e(q)} — {e(x)}' for q, _, x in t['qs'])
            do = f'<b>{KIND_RU[t["kind"]]}</b>. Скажите своими словами: «{e(t["title"])}». На экране только «{e(t["en"])}». ' + HOW[t['kind']]
            if t['kind'] == 'listen':
                do += f'<br><i>Текст записи (ученику не показываем):</i> {e(t["text"])}'
            tl = e(t['en'])
            row('', do, tl, exp)
        for q, _ in o['you']:
            row('', '<b>And you?</b> Устные вопросы о самом ученике — по одному на карточке, следующий по нажатию или Next — оцените 0/1/2 в чек-листе ✅, панель «Сейчас на экране». После Next ученик получает обрывок записки и возвращается в комнату.', e(q), 'Полный ответ по теме, без подсказки = 2')
    row(f'📜 Записка Part {P["n"]}', 'Когда все предметы открыты — «Put the note together»: кусочки слетаются, видны цифры.', 'Look! The pieces make a note. What’s the code?', ' '.join(['X'] * P['digits']))
    if P['n'] < 3:
        row(f'Чекпойнт Part {P["n"]}', 'Посмотрите суммы блоков в чек-листе. ≥ 9 из 12 в каждом блоке → «Keep looking» (следующая часть). Иначе → «Open the lock» (финал).', 'Great job! Let’s keep looking! / Great job! Shall we open the lock?', '—')
row('🔐 Замок', 'Попросите ученика прочитать код вслух по-английски (на экране — только «Read your code in English!»), вы нажимаете «Enter the code». Кнопка 🚪 вверху ведёт сюда в любой момент.', 'Read the code in English, please!', 'four, seven, two, nine…')
row('🎉 Финал', 'Дверь открыта. Нажмите «📝 Отчёт» внизу слева: откроется чек-лист сразу на отчёте. Допишите комментарий, если нужно, нажмите «Скопировать отчёт» и переходите к предзакрытию.', 'Well done! You escaped! How did you like the game?', '—')
PLAN_INNER = (
    '<h1 style="color:#6e3510;margin:4px 0 10px">🗝 План урока: Escape Room 13+ (вводный урок)</h1>'
    f'<p class="dl"><a href="{SITE}mvu_13plus_plan.docx" download>⬇ Скачать план (Word)</a><a class="pdf" href="{SITE}mvu_13plus_plan.pdf" download>⬇ Скачать план (PDF)</a></p>'
    '<div class="legend"><b>Длительность:</b> 40 мин, из них ~25 на задания, остальное — маркетинговые этапы. <b>Порядок:</b> всегда с Part 1; дальше — по результату. '
    'Каждый предмет: назвать → задание(я) → вопрос «And you?» → обрывок записки. Ничего не листается само — только Next. '
    '<b>✅</b> — чек-лист, <b>📋</b> — план (отдельные окна). <b>💡</b> — облегчённый режим (меньше вариантов, подсказки). <b>🚪</b> — сразу к замку. Цифра/обрывок даётся всегда, даже если ученик не справился.</div>'
    '<table class="plan"><tr><th>Шаг</th><th>Что делать</th><th>Teacher’s language</th><th>Ожидаемые ответы</th></tr>' + ''.join(rows) + '</table>'
)
PLAN_STYLE = ('table.plan td.st{font-weight:700;white-space:nowrap}table.plan td.tl{color:#7a3d10;font-style:italic;width:24%}'
              'table.plan td.sa{color:#1f5fa8;width:22%}table.plan tr.part td{background:#2b2240;color:#ffd889;font-weight:700}')

# ── новые комнаты с вырезками (вариант «а», 12.11): предмет вырезан из самой комнаты и лежит поверх ──
RJ = os.path.join(REPO, 'media', 'mvu_13plus', 'rooms', 'rooms.json')
if os.path.exists(RJ):
    cuts = json.load(open(RJ))
    for P in data.PARTS:
        ids = [o['id'] for o in P['objects']]
        if all(i in cuts for i in ids):
            P['room'] = cuts[ids[0]]['room']; used.add(P['room'])
            for o in P['objects']:
                o['cut'] = cuts[o['id']]; used.add('rooms/' + o['cut']['room'] + '_' + o['id'])
# то, что в комнате стоит ПЕРЕД предметом, кладём поверх без свечения (лампа перед шкафом, замечание 63)
FRONT = {'room2_v2': [dict(file='rooms/room2_v2_front_desk', x=0.0, y=48.828, w=23.438, h=9.766),   # стол под шкафом: свечение шкафа только сверху и справа (65)
                      dict(file='rooms/room2_v2_front_lamp', x=0.0, y=37.891, w=10.938, h=24.707)]}
for P in data.PARTS:
    P['front'] = FRONT.get(P['room'], [])
    for f in P['front']: used.add(f['file'])
# ── данные для страницы ─────────────────────────────────────────────────────────────────
preload = set(used)
D = dict(media=data.M, audio=AUDIO, family=data.FAMILY,
         checklist=[dict(title=p['title'], blocks=[[b, ts] for b, ts in p['blocks']]) for p in data.CHECKLIST],
         parts=[dict(room=P['room'], room_name=P['room_name'], intro=P['intro'] if P['n'] > 1 else '', intro_en=P['intro_en'], objects=P['objects'], front=P.get('front', [])) for P in data.PARTS],
         topic_ru=data.TOPIC_RU, alias=data.ALIAS, preload=sorted(preload))
mw = open(os.path.join(HERE, 'manager.html')).read()
D['plan_html'] = ('<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><title>План урока — Escape Room 13+</title><style>'
    "body{font-family:'Segoe UI',Arial,sans-serif;background:#f6efe2;color:#2a1a10;padding:18px 22px;max-width:1200px;margin:0 auto;font-size:14px}"
    'table{border-collapse:collapse;width:100%;background:#fff}th,td{border:1px solid #d9cdb8;padding:5px 8px;vertical-align:top}th{background:#6e3510;color:#fff;text-align:left}'
    '.legend{background:#fffaf0;border-left:4px solid #f2b544;padding:8px 12px;margin:8px 0}'
    '.dl a{display:inline-block;margin:0 8px 10px 0;padding:8px 16px;border-radius:10px;background:#e8631a;color:#fff;font-weight:700;text-decoration:none}.dl a.pdf{background:#7b4bd6}'
    + PLAN_STYLE + '</style></head><body>' + PLAN_INNER + '</body></html>')
D['mw_html'] = mw
tpl = open(os.path.join(HERE, 'template.html')).read()
page = tpl.replace('/*DATA*/null', json.dumps(D, ensure_ascii=False).replace('</', '<\\/'))
open(os.path.join(OUT, 'index.html'), 'w').write(page)
print('index.html', len(page) // 1024, 'KB')

plan_html = ('<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><title>План урока — Escape Room 13+</title><style>'
             'body{font-family:Arial,sans-serif;color:#2a1a10;font-size:11pt}table{border-collapse:collapse;width:100%}'
             'th,td{border:1px solid #bfb3a0;padding:4px 6px;vertical-align:top}th{background:#6e3510;color:#fff}'
             '.legend{border-left:4px solid #f2b544;padding:6px 10px;margin:8px 0}' + PLAN_STYLE + '</style></head><body>'
             + re.sub(r'<p class="dl">.*?</p>', '', PLAN_INNER) + '</body></html>')
open(os.path.join(OUT, 'plans', 'mvu_13plus_plan.html'), 'w').write(plan_html)

if '--docs' in sys.argv:
    d = os.path.join(OUT, 'plans')
    subprocess.run(['soffice', '--headless', '--convert-to', 'docx:MS Word 2007 XML', '--outdir', d, os.path.join(d, 'mvu_13plus_plan.html')], check=True, capture_output=True)
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();"
          f"await p.goto('file://{d}/mvu_13plus_plan.html');await p.pdf({{path:'{d}/mvu_13plus_plan.pdf',format:'A4',landscape:true,printBackground:true,"
          "margin:{top:'10mm',bottom:'10mm',left:'10mm',right:'10mm'}});await b.close();})();")
    subprocess.run(['node', '-e', js], check=True)
    print(sorted(os.listdir(d)))
