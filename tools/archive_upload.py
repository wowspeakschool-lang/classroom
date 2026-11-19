"""Отправить три файла архива чата в «почтовый ящик» базы (chat_archive_inbox).

Зачем: в закрытый репозиторий wowspeak-archive большинство чатов записать не
может (подключить его посреди работы не даёт система защиты), а classroom
открытый — переписку с именами учеников туда класть нельзя. Поэтому чат
кладёт файлы в закрытую таблицу базы, а чат «Classroom» забирает их оттуда
в архив. Решение Анны 19.11.2026 («141 да»).

Положить в таблицу может любой с публичным ключом, прочитать снаружи нельзя.

Использование (из корня classroom):
    python3 tools/export_chat.py <сессия.jsonl> /tmp/arh/perepiska.md "Название чата"
    # vyzhimka.md и meta.json — пишет сам чат, как в INSTRUKCIYA.md архива
    python3 tools/archive_upload.py <slug-чата> /tmp/arh "Название чата"

slug — латиницей, как папка в архиве: chats/<slug>/ (например splat-kids).
Если чат в архиве уже есть, можно прислать только новое с прошлого
сохранения — Classroom допишет.
"""
import json, os, re, subprocess, sys, tempfile, uuid

URL = 'https://vtcxghsqymwkyiogpndf.supabase.co/rest/v1/chat_archive_inbox'
FILES = ('perepiska.md', 'vyzhimka.md', 'meta.json')
SECRET = re.compile(r'(sk-[A-Za-z0-9_-]{16,}|sb_secret_[A-Za-z0-9_-]+|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})')


def publishable_key():
    # Публичный ключ уже лежит в index.html (им пользуется сайт); берём оттуда,
    # чтобы не держать вторую копию.
    here = os.path.dirname(os.path.abspath(__file__))
    html = open(os.path.join(here, '..', 'index.html'), encoding='utf-8').read()
    m = re.search(r'sb_publishable_[A-Za-z0-9_-]+', html)
    if not m:
        sys.exit('не нашёл публичный ключ в index.html')
    return m.group(0)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    slug, folder = sys.argv[1], sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else None
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{1,59}', slug):
        sys.exit('slug — только латиница, цифры и дефис: splat-kids')
    rows = []
    for f in FILES:
        p = os.path.join(folder, f)
        if not os.path.exists(p):
            sys.exit(f'нет файла {p}')
        text = open(p, encoding='utf-8').read()
        if SECRET.search(text):
            sys.exit(f'в {f} похоже на ключ или токен — вычистите и запустите снова')
        rows.append({'id': str(uuid.uuid4()), 'chat': slug, 'file': f, 'content': text, 'title': title})
    key = publishable_key()
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as t:
        json.dump(rows, t, ensure_ascii=False)
        body = t.name
    r = subprocess.run(['curl', '-sS', '-o', '/dev/stderr', '-w', '%{http_code}', '-X', 'POST', URL,
                        '-H', f'apikey: {key}', '-H', 'Content-Type: application/json',
                        '-H', 'Prefer: return=minimal', '--data-binary', f'@{body}'],
                       capture_output=True, text=True)
    os.unlink(body)
    if r.stdout.strip() != '201':
        sys.exit(f'не отправилось: код {r.stdout.strip()} {r.stderr.strip()[:300]}')
    size = sum(len(x['content'].encode()) for x in rows) // 1024
    print(f'отправлено в ящик архива: {slug}, 3 файла, {size} КБ. '
          f'Напишите Анне: «сохранено в ящик архива, {slug}» — Classroom заберёт.')


if __name__ == '__main__':
    main()
