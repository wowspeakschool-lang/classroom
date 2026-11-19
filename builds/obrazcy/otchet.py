# -*- coding: utf-8 -*-
"""Список «было → стало» по образцам ответов из builds/obrazcy/plan.json.

    python3.13 builds/obrazcy/otchet.py
    python3.13 builds/vychitka_ot_vas.py builds/obrazcy/obrazcy_proverit.md \
        "builds/Образцы ответов — проверить.docx"
"""
import json, io
from collections import OrderedDict

NAZV = OrderedDict([
    ("wow-dragon-1", "Wow Dragon 1"), ("wow-dragon-2", "Wow Dragon 2"),
    ("sm0", "Super Minds Starter"), ("sm1", "Super Minds 1"),
    ("sm2", "Super Minds 2"), ("sm3", "Super Minds 3"),
    ("gg1", "Go Getter 1"), ("gg2", "Go Getter 2"), ("gg3", "Go Getter 3"),
    ("holidays", "Holidays"),
])

plan = json.load(open("builds/obrazcy/plan.json", encoding="utf-8"))
bez = json.load(open("builds/obrazcy/bez_teksta.json", encoding="utf-8"))
cht = json.load(open("builds/obrazcy/chtenie_vsluh.json", encoding="utf-8"))
ch = [r for r in plan if r["menyaem"]]


def nomer(r):
    """Сортировка уроков: Homework 2 раньше Homework 13, тест в конце."""
    t = r["urok"]
    cif = "".join(c for c in t if c.isdigit())
    return (0 if cif else 1, int(cif) if cif else 0, t, r["blok"])


def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


out = io.StringIO()
w = out.write
w("# Образцы ответов — проверить\n\n")
w("Решение Анны от 09.11.2026: образец к заданию «расскажи / назови» не должен\n"
  "проговаривать готовый ответ («45 верно», «46 б»). Правило, по которому резали:\n\n")
w("- предложения образца сведены по **грамматической конструкции**: одинаковые — к одному;\n")
w("- **разные конструкции остаются** — по одному предложению каждой, в исходном порядке\n"
  "  («It's a teddy bear. I like it.» — два построения фразы, оба нужны);\n")
w("- перечисление без глагола («Teddy bear, lego, robot», «Слова на T») режется до одного пункта;\n")
w("- рассказ о себе исключением не считается: «I can run! I can jump! I can swim!» → «I can run!»;\n")
w("- задания **«прочитай вслух»** и **«повтори»** не трогали: там образец — эталон чтения.\n\n")
w("Всего блоков `speaking` с образцом — 501. Изменено **%d**, оставлено как было **%d**,\n"
  "«прочитай вслух» — %d, без текста образца (записаны голосом Анны) — %d.\n\n"
  % (len(ch), len(plan) - len(ch), len(cht), len(bez)))
w("🟥 **Нужно нажать «Озвучить пачкой»** («Контент» → «Медиа»): у всех %d изменённых\n"
  "образцов старая запись снята, новый текст озвучится сам.\n\n" % len(ch))
w("---\n\n")

for slug, name in NAZV.items():
    rows = sorted([r for r in ch if r["slug"] == slug], key=nomer)
    if not rows:
        continue
    w("## %s — %d образцов\n\n" % (name, len(rows)))
    w("| урок | блок | задание | было | стало |\n|---|---|---|---|---|\n")
    for r in rows:
        w("| %s | %s | %s | %s | %s |\n"
          % (r["urok"], r["blok"], esc(r["zag"]), esc(r["obr"]), esc(r["novyy"])))
    w("\n")

import re as _re
PESNYA = _re.compile(r"спой|чант|повтори за|подпевай", _re.I)
pesni = [r for r in bez if PESNYA.search((r["zag"] or "") + " " + (r["txt"] or ""))]
slushat = [r for r in bez if r not in pesni]

if slushat:
    w("---\n\n## Образцы, записанные голосом — послушать (%d)\n\n" % len(slushat))
    w("Эти образцы записаны голосом, текста в блоке нет — программой их не\n"
      "проверить. 🟥 Послушать и сказать, если образец проговаривает готовый ответ:\n"
      "перезапишем или снимем. Ещё %d записанных образца — песни, чанты и «повтори\n"
      "за героем»; там запись и есть материал задания, проверять нечего.\n\n" % len(pesni))
    w("| курс | урок | блок | задание |\n|---|---|---|---|\n")
    for r in sorted(slushat, key=lambda r: (list(NAZV).index(r["slug"]) if r["slug"] in NAZV else 99,) + nomer(r)):
        w("| %s | %s | %s | %s |\n"
          % (NAZV.get(r["slug"], r["slug"]), r["urok"], r["blok"], esc(r["zag"])))
    w("\n")

open("builds/obrazcy/obrazcy_proverit.md", "w", encoding="utf-8").write(out.getvalue())
print("изменено:", len(ch), "| без текста:", len(bez), "| чтение вслух:", len(cht))
