#!/usr/bin/env python3
"""Вынуть картинки base64 из блоков курса в файлы media/<папка>/legacy/.

Читает опубликованные блоки через публичный REST (тот же ключ, что в index.html),
находит каждое вхождение data:image/…;base64,… и пишет байты как есть, без
пересжатия, в media/<папка>/legacy/<md5 байтов, 12 знаков>.<расширение>.
Одинаковые картинки внутри курса — один файл.

Байты в вывод не попадают: печатаются только число блоков, вхождений, файлов
и отпечаток — md5 от отсортированного списка имён через запятую. Тот же
отпечаток считается в SQL, этим сверяется, что файлы и база говорят об одном.

    python3 tools/b64_extract.py wow-dragon-1 [--lesson <uuid>[,<uuid>…]]

У неопубликованного курса (Wow Dragon 2) юниты публичному ключу не видны —
список уроков тогда передать через --lesson, взяв его запросом в базу.
"""
import base64, hashlib, json, re, sys, urllib.request
from pathlib import Path

API = 'https://api.wowteach.ru/rest/v1/'
KEY = 'sb_publishable_nZIl9kzPNhkd9Gbsm7aAgA_cAeY1s4x'
COURSES = {  # папка в media/ → id курса (у Wow Dragon 2 нет slug)
    'sm0': '0b68efad-7c9e-4517-b5df-062ed07c638f',
    'sm1': '2b377cef-afc3-4dd1-b4e5-a767bacc87de',
    'wow-dragon-1': '1722b1a5-99bb-442d-8752-60bdd65a0e8a',
    'wow-dragon-2': '2b4c8528-ae7e-4e97-bfca-c34ac2ed4efa',
}
RX = re.compile(r'data:image/([a-zA-Z0-9+.-]+);base64,([A-Za-z0-9+/=]+)')
EXT = {'webp': 'webp', 'png': 'png', 'jpeg': 'jpg', 'jpg': 'jpg', 'gif': 'gif', 'svg+xml': 'svg'}
ROOT = Path(__file__).resolve().parent.parent


def get(path):
    req = urllib.request.Request(API + path, headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.load(r)


def lesson_ids(course_id):
    units = get(f'classroom_units?select=id&course_id=eq.{course_id}')
    ids = []
    for i in range(0, len(units), 30):
        part = ','.join(u['id'] for u in units[i:i + 30])
        ids += [l['id'] for l in get(f'classroom_lessons?select=id&unit_id=in.({part})')]
    return ids


def main():
    folder = sys.argv[1]
    lessons = sys.argv[3].split(',') if '--lesson' in sys.argv else lesson_ids(COURSES[folder])
    out = ROOT / 'media' / folder / 'legacy'
    out.mkdir(parents=True, exist_ok=True)
    seen, blocks, occ, written = {}, 0, 0, 0
    for i in range(0, len(lessons), 10):
        part = ','.join(lessons[i:i + 10])
        for b in get(f'classroom_blocks?select=id,payload&lesson_id=in.({part})'):
            found = RX.findall(json.dumps(b['payload'], ensure_ascii=False))
            blocks += bool(found)
            for mime, b64 in found:
                occ += 1
                raw = base64.b64decode(b64, validate=True)
                h = hashlib.md5(raw).hexdigest()
                name = f'{h[:12]}.{EXT[mime]}'
                if seen.setdefault(name, h) != h:
                    sys.exit(f'коллизия имени {name}')
                f = out / name
                if not f.exists():
                    f.write_bytes(raw)
                    written += 1
    names = sorted(seen)
    fp = hashlib.md5(','.join(names).encode()).hexdigest()
    print(json.dumps({'folder': folder, 'lessons': len(lessons), 'blocks': blocks, 'occ': occ,
                      'files': len(names), 'written': written, 'fingerprint': fp}, ensure_ascii=False))


if __name__ == '__main__':
    main()
