#!/usr/bin/env python3
"""Кнопки в конце урока по решению Анны.

Было: на экране прощания три кнопки сразу — «Вернуться на карту», «Пройти урок
ещё раз», «Завершить урок». Выбор из трёх на последнем экране сбивает: ребёнку
непонятно, урок уже закончен или нет.

Стало: на прощании две кнопки — «Пройти урок ещё раз» и «Завершить урок».
Кнопка «Вернуться на карту» появляется после неё, на табличке «Урок завершён»,
и она там единственная — мимо карты не пройти.

В едином файле урок живёт в iframe, поэтому возврат идёт сообщением наружу,
как и кнопка «на карту» внутри урока.

Запуск: python3 tools/fix_end_buttons.py
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")

OLD_BTNS = """    const mapBtn = el("button", {
      class: "btn btn-primary btn-big invisible",
      onclick: function() { location.href = MAP_URL; },
    }, "Вернуться на карту 🗺️");
    btnArea.appendChild(mapBtn);
    btnArea.appendChild(restartBtn);
    btnArea.appendChild(finishBtn);
    buttonRevealTimer = setTimeout(() => {
      mapBtn.classList.remove("invisible");
      restartBtn.classList.remove("invisible");
      finishBtn.classList.remove("invisible");
    }, s.introDelay || 2500);"""

NEW_BTNS = """    /* Карта — не здесь: она ждёт на табличке «Урок завершён», см. goToMap(). */
    btnArea.appendChild(restartBtn);
    btnArea.appendChild(finishBtn);
    buttonRevealTimer = setTimeout(() => {
      restartBtn.classList.remove("invisible");
      finishBtn.classList.remove("invisible");
    }, s.introDelay || 2500);"""

GO_TO_MAP = '''
/* Возврат на карту: в едином файле урок лежит в iframe и просит карту закрыть
   его сообщением, отдельной страницей — уходит по ссылке. */
function goToMap() {
  if (window.parent !== window) {
    try { window.parent.postMessage({ type: "wowspeak:back" }, "*"); return; } catch (e) {}
  }
  location.href = MAP_URL;
}
'''

# В Уроке 4 табличка другая: под ней карточка для родителей, и кнопка оформлена
# иначе. Поэтому вариантов замены два.
OLD_CLOSE = """  const closeBtn = el("button", {
    class: "btn btn-big",
    style: { background: "white", color: "var(--primary)", borderColor: "white" },
    onclick: () => {
      overlay.remove();
      resetProgress();
    },
  }, "Закрыть");"""

NEW_CLOSE = """  const closeBtn = el("button", {
    class: "btn btn-big",
    style: { background: "white", color: "var(--primary)", borderColor: "white" },
    onclick: () => {
      overlay.remove();
      resetProgress();
      goToMap();
    },
  }, "Вернуться на карту 🗺️");"""

OLD_CLOSE_L4 = """  const closeBtn = el("button", {
    class: "btn",
    style: { background: "transparent", color: "white", borderColor: "rgba(255,255,255,0.6)", marginTop: "18px" },
    onclick: () => { overlay.remove(); resetProgress(); },
  }, "Закрыть");"""

NEW_CLOSE_L4 = """  const closeBtn = el("button", {
    class: "btn",
    style: { background: "transparent", color: "white", borderColor: "rgba(255,255,255,0.6)", marginTop: "18px" },
    onclick: () => { overlay.remove(); resetProgress(); goToMap(); },
  }, "Вернуться на карту 🗺️");"""


def patch(n):
    path = os.path.join(LESSONS, "lesson-%d.html" % n)
    s = open(path, encoding="utf-8").read()
    steps = []
    if OLD_BTNS in s:
        s = s.replace(OLD_BTNS, NEW_BTNS, 1); steps.append("карта убрана с прощания")
    elif NEW_BTNS in s:
        steps.append("прощание уже поправлено")
    else:
        return "НЕ НАЙДЕН блок кнопок прощания"
    if "function goToMap()" not in s:
        assert s.count("function showFinishOverlay") == 1
        s = s.replace("function showFinishOverlay", GO_TO_MAP + "\nfunction showFinishOverlay", 1)
        steps.append("добавлен переход на карту")
    for old, new in ((OLD_CLOSE, NEW_CLOSE), (OLD_CLOSE_L4, NEW_CLOSE_L4)):
        if old in s:
            s = s.replace(old, new, 1); steps.append("кнопка на табличке заменена"); break
        if new in s:
            steps.append("табличка уже поправлена"); break
    else:
        steps.append("НЕ НАЙДЕНА кнопка «Закрыть»")
    open(path, "w", encoding="utf-8").write(s)
    return "; ".join(steps)


if __name__ == "__main__":
    for n in (1, 2, 3, 4):
        print("Урок %d: %s" % (n, patch(n)))
