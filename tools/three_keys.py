#!/usr/bin/env python3
"""Три ключика вместо четырёх (решение Анны 17.09).

Ключик открывает переход с острова на остров, а переходов ровно три: Ярмарка →
Зеркала → Друзья → Замок. Четвёртый ключик выдавался в конце Урока 4, когда всё
уже открыто, и не открывал ничего — он появился ради симметрии «в каждом уроке
по ключику» и счётчика «0 из 4».

Теперь на карте «N из 3» и три слота, а на выходе из Урока 4 вместо ключика —
распахнутый Замок: наградой за последний урок и так идёт корона от Дракона.

Запуск: python3 tools/three_keys.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = os.path.join(ROOT, "map.html")
LESSON4 = os.path.join(ROOT, "lessons", "wowspeak-mini", "lesson-4.html")

MAP_EDITS = [
    # счётчик
    ('<b><span id="count">0</span> из 4</b>',
     '<b><span id="count">0</span> из 3</b>'),
    # слоты под ключики
    ("""  for(var i=1;i<=4;i++){
    var slot = document.createElement("span");
    slot.className = "slot";
    slot.appendChild(makeBarKey());
    slotsBox.appendChild(slot);
  }""",
     """  /* три слота: ключик — это переход между островами, а переходов три */
  for(var i=1;i<=3;i++){
    var slot = document.createElement("span");
    slot.className = "slot";
    slot.appendChild(makeBarKey());
    slotsBox.appendChild(slot);
  }"""),
    ("""    var slots = slotsBox.children;
    for(var s=0;s<4;s++){
      slots[s].classList.toggle("filled", journey["island"+(s+1)] === true);
    }
    countEl.textContent = String(done);""",
     """    var slots = slotsBox.children;
    for(var s=0;s<3;s++){
      slots[s].classList.toggle("filled", journey["island"+(s+1)] === true);
    }
    /* пройденный Замок ключика не даёт: он последний */
    countEl.textContent = String(Math.min(done, 3));"""),
    # анимация «прилетел новый ключик» ходила по слотам до doneCount(), а пройденный
    # Замок ключика не даёт — на четвёртом острове слота нет и анимация падала
    ("""    var slots = slotsBox.children;
    for(var s=fromCount; s<doneCount(); s++){""",
     """    var slots = slotsBox.children;
    for(var s=fromCount; s<Math.min(doneCount(), slots.length); s++){"""),
    # табличка финала
    ("""    <h2>Все четыре ключика твои! 🔑</h2>
    <p>Ворота Замка открылись, Дракон проснулся — Праздник начался!</p>""",
     """    <h2>Вся Волшебная страна открыта! 👑</h2>
    <p>Ворота Замка распахнулись, Дракон проснулся — Праздник начался!</p>"""),
]

LESSON4_EDITS = [
    ("Ворота Замка распахнулись, Дракон проснулся — Праздник начался! "
     "Четвёртый ключик твой, и вся Волшебная страна теперь открыта.",
     "Ворота Замка распахнулись, Дракон проснулся — праздник начался! "
     "Теперь вся Волшебная страна твоя."),
    ('icon: "🔑", iconLabel: "Четвёртый ключик"',
     'icon: "🏰", iconLabel: "Праздник в Замке Дракона"'),
]


def patch(path, edits):
    s = open(path, encoding="utf-8").read()
    done, already, missing = 0, 0, []
    for old, new in edits:
        if old in s:
            s = s.replace(old, new, 1); done += 1
        elif new in s:
            already += 1
        else:
            missing.append(old.strip()[:50] + "…")
    open(path, "w", encoding="utf-8").write(s)
    out = "заменено %d" % done
    if already:
        out += ", уже стояло %d" % already
    if missing:
        out += "; НЕ НАЙДЕНО: " + "; ".join(missing)
    return out


if __name__ == "__main__":
    print("Карта:  " + patch(MAP, MAP_EDITS))
    print("Урок 4: " + patch(LESSON4, LESSON4_EDITS))
