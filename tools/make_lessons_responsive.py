#!/usr/bin/env python3
"""Приводит уроки в порядок на больших экранах.

На ноутбуке содержимое урока прижималось к верху, а снизу оставалась пустая
половина экрана. Здесь добавляется блок стилей, который центрирует содержимое
по вертикали между шапкой и низом окна. Шапка с прогрессом остаётся наверху.

На телефоне ничего не меняется: правило включается только на широких и
достаточно высоких экранах.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")
MARKER = "/* --- адаптация под большие экраны --- */"

CSS = """
%s
@media (min-width: 900px) and (min-height: 640px) {
  #app {
    display: flex;
    flex-direction: column;
  }
  #app > header { flex: 0 0 auto; }

  /* Резерв высоты под контент на больших экранах не нужен: он оставлял пустоту
     снизу и съедал место, из-за которого центрирование не срабатывало вовсе. */
  #app main { min-height: 0; }

  /* Большой нижний отступ нужен только когда учитель закреплён в углу.
     В фазе рассказа он стоит в потоке и ничего не перекрывает. */
  #app:has(#teacher-widget.intro-mode) { padding-bottom: 56px; }

  /* В фазе рассказа учитель стоит в потоке: поднимаем пару «учитель + контент»
     к центру. В фазе задания учитель закреплён в углу и из потока выпадает,
     поэтому центрируем один контент. */
  #teacher-widget.intro-mode { margin-top: auto; }
  #teacher-widget:not(.intro-mode) ~ #content { margin-top: auto; }
  #content { margin-bottom: auto; }
}
""" % MARKER


def patch(n):
    path = os.path.join(LESSONS, "lesson-%d.html" % n)
    s = open(path, encoding="utf-8").read()
    if MARKER in s:
        return "уже применено"
    assert s.count("</style>") == 1
    s = s.replace("</style>", CSS + "</style>", 1)
    open(path, "w", encoding="utf-8").write(s)
    return "готово"


if __name__ == "__main__":
    for n in (1, 2, 3, 4):
        print("Урок %d: %s" % (n, patch(n)))
