#!/usr/bin/env python3
"""Проверить, что каждый файл media/*/legacy/ отдаётся с сайта и совпадает побайтно.

    python3 tools/b64_verify.py [папка …]     # по умолчанию все четыре
Печатает число проверенных, число не отвечающих 200 и число несовпавших по md5.
"""
import hashlib, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SITE = 'https://classroom.wowteach.ru/media/'
ROOT = Path(__file__).resolve().parent.parent / 'media'
folders = sys.argv[1:] or ['sm0', 'sm1', 'wow-dragon-1', 'wow-dragon-2']
files = [f for d in folders for f in sorted((ROOT / d / 'legacy').iterdir())]


def check(f):
    url = SITE + f.relative_to(ROOT).as_posix()
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            body = r.read()
    except Exception as e:
        return 'http', url, str(e)[:80]
    if hashlib.md5(body).digest() != hashlib.md5(f.read_bytes()).digest():
        return 'md5', url, ''
    return 'ok', url, ''


with ThreadPoolExecutor(16) as ex:
    res = list(ex.map(check, files))
bad = [r for r in res if r[0] != 'ok']
print(f'проверено {len(res)}, не отвечают {sum(r[0] == "http" for r in res)}, '
      f'не совпали {sum(r[0] == "md5" for r in res)}')
for r in bad[:10]:
    print(*r)
sys.exit(1 if bad else 0)
