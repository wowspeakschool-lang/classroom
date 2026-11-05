import json, re, sys, collections

SRC = '/root/.claude/projects/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/tool-results/mcp-Supabase-execute_sql-1793885014221.txt'
raw = json.load(open(SRC))['result']
m = re.search(r'<untrusted-data-[0-9a-f-]+>\s*(\[.*?\])\s*</untrusted-data-', raw, re.S)
blob = json.loads(m.group(1))[0]['t']

MATERIAL = {'text', 'video', 'flashcards', 'embed'}
GLUE = re.compile(r'ещё раз|еще раз|снова|тот же|по этой записи|по рассказу|по тексту|прочитай ещё|прочитай еще', re.I)
RECOG = {'match', 'sort', 'sequence'}
HEAD = re.compile(r'^[^A-Za-zА-Яа-я]{0,4}(READING|LISTENING|SPEAKING|WRITING)\b', re.I)

def head_rank(title):
    m = HEAD.match(title.strip())
    if not m: return None
    up = title.upper()
    if 'READING' in up:   return 5
    if 'LISTENING' in up: return 6
    if 'SPEAKING' in up:  return 7
    return 4

lessons = collections.OrderedDict()
for line in blob.split('\n'):
    lid, slug, un, ltitle, so, btype, skill, aud, *rest = line.split('\t')
    title = rest[0] if rest else ''
    lessons.setdefault((lid, slug, int(un), ltitle), []).append(
        dict(so=int(so), type=btype, skill=skill, aud=(aud == 'A'), title=title))

def rank_of(task):
    s, t, ti = task['skill'], task['type'], task['title']
    if s == 'writing' and t == 'exact_input' and re.search(r'dictation|диктант', ti, re.I):
        return 2
    if s == 'reading':  return 5
    if s == 'listening': return 6
    if s == 'speaking':  return 7
    return 4

plan, report = [], []
for (lid, slug, un, ltitle), blocks in lessons.items():
    blocks.sort(key=lambda b: b['so'])
    n = len(blocks)
    greet = blocks[0] if blocks and blocks[0]['type'] == 'text' else None
    farew = blocks[-1] if n > 1 and blocks[-1]['type'] == 'text' else None
    mid = blocks[(1 if greet else 0):(n - 1 if farew else n)]

    units, buf = [], []
    for b in mid:
        if b['type'] in MATERIAL and b['skill'] == '-':
            hr = head_rank(b['title']) if b['type'] == 'text' else None
            if hr is not None:
                units.append(dict(blocks=buf + [b], task=None, head=hr)); buf = []
            else:
                buf.append(b)
            continue
        units.append(dict(blocks=buf + [b], task=b)); buf = []
    if buf:
        if units: units[-1]['blocks'] += buf
        else: units.append(dict(blocks=buf, task=None))

    # склейка «послушай ещё раз», «прочитай текст ещё раз» — к предыдущему заданию
    merged = []
    for u in units:
        t = u['task']
        glue = False
        if t is not None and merged:
            prev = merged[-1]['task']
            if GLUE.search(t['title']): glue = True
            elif (prev is not None and prev['aud'] and not t['aud']
                  and re.search(r'послушай|аудио', t['title'], re.I)): glue = True
        if glue: merged[-1]['blocks'] += u['blocks']
        else: merged.append(u)
    units = merged

    for i, u in enumerate(units):
        if u.get('head') is not None:
            u['rank'] = u['head']; u['first'] = True
        else:
            u['rank'] = rank_of(u['task']) if u['task'] else 4
            u['first'] = False
        u['idx'] = i
    # разминка: первое задание на узнавание среди «прочих»
    cand = [u for u in units if u['rank'] == 4 and u['task'] is not None and not u['first']
            and (u['task']['type'] in RECOG
                 or (u['task']['type'] == 'quiz' and u['task']['skill'] == 'vocabulary'))]
    if not cand:
        cand = [u for u in units if u['rank'] == 4 and u['task'] is not None and not u['first']]
    if cand: cand[0]['rank'] = 1

    order = ([greet] if greet else [])
    for u in sorted(units, key=lambda u: (u['rank'], 0 if u['first'] else 1, u['idx'])):
        order += u['blocks']
    if farew: order.append(farew)

    assert len(order) == n, (slug, un, ltitle, len(order), n)
    old = [b['so'] for b in order]
    if old == list(range(n)):
        continue
    plan.append((lid, [b['so'] for b in order]))
    report.append((slug, un, ltitle, [(b['so'] + 1, b['type'], b['skill'],
                                      b['title'][:34]) for b in order]))

print(f'уроков-тестов всего: {len(lessons)}, переставляется: {len(plan)}')
json.dump(plan, open('reorder_plan.json', 'w'))
with open('reorder_report.md', 'w') as f:
    f.write('# Порядок заданий в тестах — приведён к структуре 05.11.2026\n\n')
    f.write('Структура: приветствие · разминка (узнавание) · диктант · остальные\n'
            'задания · чтение · аудирование · говорение · прощание.\n\n')
    for slug, un, ltitle, seq in report:
        f.write(f'## {slug} · юнит {un} · {ltitle}\n\n')
        f.write('| новый блок | был блоком | тип | раздел | заголовок |\n|---|---|---|---|---|\n')
        for i, (oldno, t, s, ti) in enumerate(seq, 1):
            f.write(f'| {i} | {oldno} | {t} | {s} | {ti} |\n')
        f.write('\n')
print('готово: reorder_plan.json, reorder_report.md')
