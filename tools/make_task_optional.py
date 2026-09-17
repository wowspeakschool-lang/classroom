#!/usr/bin/env python3
"""Второе письменное задание Урока 3 — по желанию.

В конце Урока 3 подряд идут два задания на письмо: описать Бена и Мию, а потом
ещё три предложения про друга или родственника. Для бесплатного мини-курса это
много: ребёнок устаёт на первом и бросает урок перед самой наградой.

Задание остаётся на месте, но под ним появляется «Пропустить» — кто хочет,
пишет, остальные идут дальше.

Запуск: python3 tools/make_task_optional.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSON = os.path.join(ROOT, "lessons", "wowspeak-mini", "lesson-3.html")

ANCHOR = '    submitWrap.appendChild(submitBtn); root.appendChild(submitWrap);'

BLOCK = ANCHOR + '''
    /* Задание по желанию: два письменных подряд — много для мини-курса. */
    const skipWrap = el("div", { class: "skip-area" });
    const skipBtn = el("button", { class: "skip-btn", onclick: next }, "Пропустить");
    skipWrap.appendChild(skipBtn); root.appendChild(skipWrap);'''

CSS = """
/* «Пропустить» под необязательным заданием */
.skip-area { text-align:center; margin-top:10px; }
.skip-btn { background:none; border:none; cursor:pointer; font-size:15px; font-weight:600;
  color:var(--muted, #8a7fb0); text-decoration:underline; padding:6px 10px; }
.skip-btn:hover { color:var(--primary, #3D2E68); }
"""


def main():
    s = open(LESSON, encoding="utf-8").read()
    steps = []
    if "skip-btn" not in s:
        # такая же строка есть и в других заданиях урока, поэтому правим
        # только внутри нужной рисовалки
        m = re.search(r'  describeperson: function.*?\n  \},', s, re.S)
        assert m, "не найдена рисовалка describeperson"
        part = m.group(0)
        assert part.count(ANCHOR) == 1, "не найден якорь задания"
        s = s[:m.start()] + part.replace(ANCHOR, BLOCK, 1) + s[m.end():]
        s = s.replace("</style>", CSS + "</style>", 1)
        steps.append("кнопка «Пропустить» добавлена")
    else:
        steps.append("уже стоит")
    open(LESSON, "w", encoding="utf-8").write(s)
    print("Урок 3: " + "; ".join(steps))


if __name__ == "__main__":
    main()
