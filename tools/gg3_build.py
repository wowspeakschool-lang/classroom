#!/usr/bin/env python3
"""Сборка тестов Go Getter 3 — тот же код, что tools/gg2_build.py, свой курс.

В GG3 только тесты: у каждого урока kind='test' и порог 90 (проверка это
требует). Уроки — tools/gg3_u1.py … tools/gg3_u8.py, tools/gg3_final.py.
Картинки — img(unit, name, course="gg3") → media/gg3/<юнит>/.

  python3 tools/gg3_build.py --list
  python3 tools/gg3_build.py --lesson u1_test --setup | --clear ID | --chunks ID | --verify ID | --sql
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gg2_build as base  # noqa: E402

COURSE = {"slug": "gg3", "title": "Go Getter 3",
          "modules": ["gg3_u1", "gg3_u2", "gg3_u3", "gg3_u4", "gg3_u5",
                      "gg3_u6", "gg3_u7", "gg3_u8", "gg3_final"]}

_check = base.check


def check(lesson, errors):
    # В gg2_build.check регулярка ссылок записана r"[^\"'\\s)<]+": в сыром
    # строковом литерале \\s — это обратная косая и буква «s», и ссылка
    # обрывается на первой «s» (hang_washing → hang_wa). Его ошибки «нет файла»
    # выкидываем и проверяем ссылки заново правильной регуляркой.
    own = []
    _check(lesson, own)
    errors.extend(e for e in own if "нет файла media/" not in e)
    for i, (btype, payload, _) in enumerate(base.blocks_of(lesson), start=1):
        dump = json.dumps(payload, ensure_ascii=False)
        for link in re.findall(r"@@MEDIA@@([^\"'\s)<\\]+)", dump):
            if not os.path.exists(os.path.join(base.ROOT, "media", link)):
                errors.append(f"блок {i} ({btype}): нет файла media/{link}")
    if lesson.get("kind") != "test":
        errors.append("в GG3 только тесты: kind должен быть 'test'")


base.check = check

if __name__ == "__main__":
    base.main(COURSE)
