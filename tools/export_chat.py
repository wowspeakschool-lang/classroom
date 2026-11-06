"""Переписка сессии Claude Code (jsonl) → читаемый markdown: сообщения человека и ответы,
без служебного вывода инструментов. Подозрительное на секреты вычищается."""
import json, re, sys
src, dst, title = sys.argv[1], sys.argv[2], sys.argv[3]
SECRET = re.compile(r'(sk-[A-Za-z0-9_-]{16,}|sb_secret_[A-Za-z0-9_-]+|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})')
out, n_u, n_a, last = [f'# {title}\n'], 0, 0, None
for line in open(src, encoding='utf-8'):
    try: d = json.loads(line)
    except Exception: continue
    t, m = d.get('type'), d.get('message') or {}
    if t not in ('user', 'assistant') or d.get('isSidechain'): continue
    c = m.get('content')
    parts = []
    if isinstance(c, str): parts = [c]
    elif isinstance(c, list):
        for x in c:
            if isinstance(x, dict) and x.get('type') == 'text': parts.append(x.get('text', ''))
    txt = '\n'.join(p for p in parts if p and p.strip())
    if not txt.strip(): continue
    if t == 'user' and (txt.startswith('<system-reminder>') or 'tool_use_id' in txt or txt.startswith('Stop hook feedback') or '<task-notification>' in txt): 
        continue
    txt = SECRET.sub('[скрыто]', txt)
    ts = (d.get('timestamp') or '')[:16].replace('T', ' ')
    who = '## 👤 Анна' if t == 'user' else '### 🤖 Claude'
    if t == 'user': n_u += 1
    else: n_a += 1
    out.append(f'\n{who} · {ts} UTC\n\n{txt.strip()}\n')
open(dst, 'w', encoding='utf-8').write(''.join(out))
print(f'сообщений Анны: {n_u}, ответов: {n_a}, размер: {sum(map(len,out))//1024} КБ')
