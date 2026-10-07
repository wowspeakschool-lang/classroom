#!/usr/bin/env python3
"""Список недостающих аудио и видео GG1 → tools/gg1_media.json.

Ищет в собранных уроках пустые места под медиа: видео с пустым url и любые
блоки с пустым "audio" (аудирование в текстовом блоке, gaps, task…). Из этого
списка tools/gg1_media_docx.js собирает таблицу для методиста, а по именам
файлов из неё потом прописываются ссылки в блоки.

  python3 tools/gg1_media_list.py
"""
import html, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gg1_build import LESSONS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNIT_TITLES = {}


def plain(s, n=110):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def label(p):
    """Чем блок виден ученику: заголовок, иначе начало текста."""
    return plain(p.get("title") or p.get("html") or p.get("text") or
                 (p.get("questions") or [{}])[0].get("q", ""))


def main():
    rows = []
    for key, les in LESSONS.items():
        unit = les["unit"]
        lesson = ("Фин. тест" if unit == "final" else
                  "Тест" if les["kind"] == "test" else
                  "ДЗ " + les["lesson_title"].split()[-1])
        blocks = les["blocks"]
        for i, (t, p) in enumerate(blocks):
            kind = None
            if t == "video" and not p.get("url"):
                kind = "видео"
            elif "audio" in p and not p["audio"]:
                kind = "аудио"
            if not kind:
                continue
            nxt = next((label(q) for _, q in blocks[i + 1:] if label(q)), "")
            own = label(p)
            hint = (f"это блок «{own}»" if own else "") + \
                   ((", дальше «" + nxt + "»") if nxt else "")
            folder = "ft" if unit == "final" else unit
            rows.append({
                "unit": les["unit_title"], "lesson": lesson, "kind": kind,
                "hint": hint.lstrip(", "),
                "name": f"gg1_{folder}_{key.split('_', 1)[1]}_b{i + 1}",
                "folder": f"gg1/{folder}/",
                "key": key, "sort_order": i,
            })
    out = os.path.join(ROOT, "tools", "gg1_media.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    print(len(rows), "файлов:", sum(r["kind"] == "видео" for r in rows), "видео,",
          sum(r["kind"] == "аудио" for r in rows), "аудио")


if __name__ == "__main__":
    main()
