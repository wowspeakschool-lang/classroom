#!/usr/bin/env python3
"""Мелкие правки внешнего вида по разбору с Анной 17.09.

1. Кусочек в угадайке показывается в круглом окошке — «через лупу». Прямоугольный
   обрезок читался как испорченная картинка: у кепки срезан верх.
2. Пустые слоты рюкзака показывают бледный силуэт будущего предмета — видно,
   что впереди ещё три вещи, а не просто серые кружки.
3. Подпись под картинкой острова была 14 px серым курсивом — ребёнок не прочтёт.
4. Кнопка «Дальше» появляется не позже 2.5 с: раньше ждали до 4.5 с и это
   выглядело как зависание.
5. Счётчик считает задания, а не экраны. Сюжетные экраны (приветствие, награда,
   рюкзак, прощание) в знаменатель не идут: их девять на урок, и полоса из-за
   них почти не двигалась.

Запуск: python3 tools/polish_ui.py
"""
import base64, io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")
ITEM_ORDER = ["star", "bottle", "boots", "bell", "crown"]

MARK = "/* правки внешнего вида 17.09 */"

CSS = MARK + """
/* кусочек показываем через круглое окошко: прямоугольный обрезок читался
   как испорченная картинка */
.frag-box { width:min(230px, 62vw); height:min(230px, 62vw); min-height:0 !important;
  margin:0 auto; border-radius:50%; overflow:hidden; padding:0 !important; }
.frag-img { width:100%; height:100%; max-height:none; object-fit:contain; padding:10%;
  box-sizing:border-box; }
/* на ответе показываем вещь целиком */
.frag-img.frag-reveal { object-fit:contain; padding:12%; box-sizing:border-box; }
/* слот с картинкой: в Уроке 1 таких стилей не было */
.shadow-slot.has-icon { display:flex; align-items:center; justify-content:center; overflow:hidden; }
.shadow-slot .slot-icon { width:78%; height:78%; object-fit:contain; display:block; }
/* силуэт будущего предмета в пустом слоте */
.shadow-slot .slot-icon.slot-ghost { opacity:.45; filter:grayscale(.45); }
/* подпись под картинкой острова */
.placeholder-label { font-size:18px; font-style:normal; font-weight:700;
  color:var(--primary, #3D2E68); opacity:.85; }
"""

# В Уроке 1 рюкзак рисуется иначе: там счётчик filledSlots, а не список наград,
# и даже у заполненных слотов не было картинки — только кружок.
GHOST_OLD_L1 = """    for (let i = 0; i < 5; i++) {
      grid.appendChild(el("div", { class: "shadow-slot" + (i < (s.filledSlots || 0) ? " filled" : "") }));
    }"""

GHOST_NEW_L1 = """    for (let i = 0; i < 5; i++) {
      const got = i < (s.filledSlots || 0);
      const slot = el("div", { class: "shadow-slot" + (got ? " filled" : "") });
      const key = BACKPACK_ORDER[i];
      if (key && IMG[key]) {
        slot.classList.add("has-icon");
        slot.appendChild(el("img", {
          class: "slot-icon" + (got ? "" : " slot-ghost"),
          src: IMG[key], alt: "", draggable: "false",
        }));
      }
      grid.appendChild(slot);
    }"""

GHOST_OLD = """      } else {
        grid.appendChild(el("div", { class: "shadow-slot" }));
      }"""

GHOST_NEW = """      } else {
        /* бледный силуэт того, что ещё предстоит получить */
        const slot = el("div", { class: "shadow-slot" });
        const nextKey = BACKPACK_ORDER[i];
        if (nextKey && IMG[nextKey]) {
          slot.classList.add("has-icon");
          slot.appendChild(el("img", { class: "slot-icon slot-ghost", src: IMG[nextKey],
                                       alt: "", draggable: "false" }));
        }
        grid.appendChild(slot);
      }"""

ORDER_CONST = """const BACKPACK_ORDER = ["star", "bottle", "boots", "bell", "crown"];
"""

PROGRESS_NEW = '''function getProgress() {
  /* Считаем задания, а не экраны: сюжетные (приветствие, рюкзак, награда,
     остров, прощание) идут одной фазой и в знаменатель не попадают. */
  const isTask = function(id) {
    const sc = screens[screenById[id]];
    return !!sc && !sc.singlePhase;
  };
  const tasks = linearOrder.filter(isTask);
  const idx = linearOrder.indexOf(state.currentId);
  if (idx < 0) return { current: 1, total: tasks.length };
  let current = 0;
  for (let i = 0; i <= idx; i++) if (isTask(linearOrder[i])) current++;
  if (idx === linearOrder.length - 1) current = tasks.length;   // на прощании — всё
  return { current: Math.max(1, current), total: tasks.length };
}'''


def crown_uri():
    """Корона лежит только в Уроке 4 — для силуэта пятого слота берём её оттуда."""
    s = open(os.path.join(LESSONS, "lesson-4.html"), encoding="utf-8").read()
    m = re.search(r'\bcrown\s*:\s*"(data:image/[a-z]+;base64,[^"]+)"', s)
    return m.group(1) if m else None


def patch(n, crown):
    path = os.path.join(LESSONS, "lesson-%d.html" % n)
    s = open(path, encoding="utf-8").read()
    steps = []

    # блок помечен, поэтому переприменяется: старый вырезаем, новый кладём
    old_css = re.search(re.escape(MARK) + r".*?(?=</style>)", s, re.S)
    if old_css:
        if old_css.group(0) != CSS:
            s = s[:old_css.start()] + CSS + s[old_css.end():]; steps.append("стили обновлены")
    else:
        s = s.replace("</style>", CSS + "</style>", 1); steps.append("стили")

    if "BACKPACK_ORDER" not in s:
        assert s.count("function getProgress()") == 1
        s = s.replace("function getProgress()", ORDER_CONST + "\nfunction getProgress()", 1)
    for old, new in ((GHOST_OLD, GHOST_NEW), (GHOST_OLD_L1, GHOST_NEW_L1)):
        if old in s:
            s = s.replace(old, new, 1); steps.append("силуэты в рюкзаке"); break

    # корона нужна для силуэта пятого слота, но лежит только в Уроке 4
    if crown and not re.search(r'\bcrown\s*:\s*"data:image', s):
        s = re.sub(r'(\n(\s*)bell\s*:\s*"data:image/[a-z]+;base64,[^"]*",)',
                   lambda m: m.group(1) + '\n%scrown: "%s",' % (m.group(2), crown), s, count=1)
        steps.append("корона для силуэта")

    # кнопка «Дальше» — не ждём дольше 2.5 с
    slow = len([m for m in re.finditer(r'introDelay:\s*(\d+)', s) if int(m.group(1)) > 2500])
    if slow:
        s = re.sub(r'introDelay:\s*(\d+)',
                   lambda m: "introDelay: " + str(min(int(m.group(1)), 2500)), s)
        steps.append("задержки ≤ 2.5 с (укорочено %d)" % slow)

    old = re.search(r'function getProgress\(\) \{.*?\n\}', s, re.S)
    if old and old.group(0) != PROGRESS_NEW:
        s = s[:old.start()] + PROGRESS_NEW + s[old.end():]
        steps.append("счётчик по заданиям")

    open(path, "w", encoding="utf-8").write(s)
    return ", ".join(steps) or "всё уже на месте"


if __name__ == "__main__":
    crown = crown_uri()
    for n in (1, 2, 3, 4):
        print("Урок %d: %s" % (n, patch(n, crown)))
