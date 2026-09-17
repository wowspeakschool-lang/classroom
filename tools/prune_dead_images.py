#!/usr/bin/env python3
"""Выкидывает из уроков картинки, на которые никто не ссылается.

В уроках остались наборы от прежних версий заданий: в Уроке 4 гардероб
собирался из wear_* и boy2_*, потом его заменили послойной фигурой z_*,
а картинки остались лежать в файле — 1.5 МБ впустую. В Уроках 3 и 4 так же
осталась угадайка по кусочку (frag_*): рисовалка для неё в коде есть, а экрана
с type:"fragmentgame" нет.

Ключ удаляется только если он не встречается в коде урока ни прямо, ни как
хвост склейки вида IMG["frag_"+r.answer] — префиксы таких склеек скрипт
вычитывает из самого файла. Скрипт переприменяемый: во второй раз просто
не находит, что удалять.

Запуск: python3 tools/prune_dead_images.py [--dry]
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")

DECL = re.compile(r'(\n\s*)([A-Za-z_][A-Za-z0-9_]*)(\s*:\s*)"data:image/[a-z]+;base64,[^"]+",?')


def code_of(s):
    """Текст урока без самих base64-данных — по нему ищем упоминания ключей."""
    return re.sub(r'"data:image/[a-z]+;base64,[^"]+"', '""', s)


def dynamic_prefixes(code):
    """Префиксы склеек: IMG["frag_"+r.answer] → frag_."""
    return set(re.findall(r'IMG\[\s*"([A-Za-z0-9_]+)"\s*\+', code))


def prune(path, dry=False):
    s = open(path, encoding="utf-8").read()
    code = code_of(s)
    prefixes = dynamic_prefixes(code)
    dead = []
    for m in DECL.finditer(s):
        key = m.group(2)
        if any(key.startswith(p) for p in prefixes):
            continue
        uses = re.findall(r'(?<![A-Za-z0-9_])%s(?![A-Za-z0-9_])' % re.escape(key), code)
        if len(uses) <= 1:          # единственное упоминание — само объявление
            dead.append((key, len(m.group(0))))
    for key, _ in dead:
        if not dry:
            s = DECL.sub(lambda m: "" if m.group(2) == key else m.group(0), s, count=0)
    if dead and not dry:
        open(path, "w", encoding="utf-8").write(s)
    return dead


def main(dry=False):
    for n in (1, 2, 3, 4):
        path = os.path.join(LESSONS, "lesson-%d.html" % n)
        dead = prune(path, dry)
        weight = sum(w for _, w in dead) / 1048576
        print("Урок %d: выкинуто %d картинок (%.1f МБ), файл %.1f МБ%s"
              % (n, len(dead), weight, os.path.getsize(path) / 1048576,
                 " — только показ" if dry else ""))
        if dead:
            print("   " + ", ".join(k for k, _ in dead))


if __name__ == "__main__":
    main("--dry" in sys.argv)
