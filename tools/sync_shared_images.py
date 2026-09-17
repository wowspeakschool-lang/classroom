#!/usr/bin/env python3
"""Переносит общие картинки из Урока 1 в остальные уроки.

Половина ключей повторяется во всех четырёх уроках: три состояния Хранительницы,
пять волшебных предметов, семь предметов одежды и рюкзак. Обновили в первом —
переносим в остальные, чтобы не генерировать одно и то же четыре раза.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")
SHARED = ["neutral", "smile", "excited", "star", "bottle", "boots", "bell",
          "cap", "tshirt", "jeans", "skirt", "jacket", "shoes", "socks", "backpack"]


def uris_from(path):
    s = open(path, encoding="utf-8").read()
    out = {}
    for key in SHARED:
        m = re.search(r'\b%s\s*:\s*"(data:image/[a-z]+;base64,[^"]+)"' % key, s)
        if m:
            out[key] = m.group(1)
    return out


def main():
    src = uris_from(os.path.join(LESSONS, "lesson-1.html"))
    print("в Уроке 1 найдено общих картинок:", len(src))
    for n in (2, 3, 4):
        path = os.path.join(LESSONS, "lesson-%d.html" % n)
        s = open(path, encoding="utf-8").read()
        done = []
        for key, uri in src.items():
            pat = re.compile(r'(\b%s\s*:\s*)"data:image/[a-z]+;base64,[^"]+"' % key)
            if pat.search(s):
                s = pat.sub(lambda m: m.group(1) + '"' + uri + '"', s, count=1)
                done.append(key)
        open(path, "w", encoding="utf-8").write(s)
        print("Урок %d: перенесено %d, файл %.1f МБ"
              % (n, len(done), os.path.getsize(path) / 1048576))


if __name__ == "__main__":
    main()
