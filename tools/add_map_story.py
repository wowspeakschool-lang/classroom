#!/usr/bin/env python3
"""Встраивает в уроки сюжет карты (§6.5 ТЗ).

В каждый урок добавляется:
  * экран истории на входе («ты на таком-то острове, вот что тут случилось»),
  * экран истории на выходе с ключиком от следующего острова,
  * запись общего прогресса в localStorage под ключом wowspeak_journey,
  * кнопка «Вернуться на карту» на прощальном экране.

Большие литералы screens и linearOrder не трогаются: экраны досылаются push-ем,
а порядок правится splice-ом сразу после объявления. Так правка не зависит от
форматирования этих массивов и одинаково ложится на все четыре файла.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")

STORY = {
 1: dict(island="Ярмарка Слов", icon="🎪", nextKey="Острова Зеркал",
     intro="Это Ярмарка Слов — самое пёстрое место в Волшебной стране! Только Ветер тут всё "
           "перепутал и раскидал одежду по прилавкам. Назови вещь по-английски, и она вернётся "
           "на свою полку.",
     outro="Ты вернул порядок всей ярмарке! Хозяева прилавков говорят спасибо и отдают тебе "
           "ключик от Острова Зеркал. Беги открывать!"),
 2: dict(island="Остров Зеркал", icon="🪞", nextKey="Острова Друзей",
     intro="Ты открыл Остров Зеркал! Здесь живут зеркала-примерочные. Загляни в зеркало и скажи, "
           "что у тебя уже есть, а чего пока нет.",
     outro="Все зеркала снова тебя видят! За это они отдают тебе ключик от Острова Друзей."),
 3: dict(island="Остров Друзей", icon="👫", nextKey="Замка Дракона",
     intro="Ты открыл Остров Друзей! Здесь живут Бен и Мия. Ветер смешал их вещи в одну кучу — "
           "помоги разобрать, кому что.",
     outro="Бен и Мия разобрали свои вещи — и теперь они твои друзья! Они дают тебе ключик "
           "от Замка Дракона."),
 4: dict(island="Замок Дракона", icon="🏰", nextKey=None,
     intro="Вот он, Замок Дракона! Праздник вот-вот начнётся, но ворота ещё закрыты. Собери "
           "своего героя и расскажи, во что он одет, — и ворота откроются.",
     outro="Ворота Замка распахнулись, Дракон проснулся — Праздник начался! Четвёртый ключик "
           "твой, и вся Волшебная страна теперь открыта."),
}

STORY_BRANCH = '''} else if (s.type === "story") {
    if (s.icon) {
      const section = el("div", { class: "screen-section" });
      const v = el("div", { class: "placeholder" });
      v.appendChild(el("div", { class: "placeholder-emoji" }, s.icon));
      if (s.iconLabel) v.appendChild(el("div", { class: "placeholder-label" }, s.iconLabel));
      section.appendChild(v);
      screenEl.appendChild(section);
    }
    if (s.island) markIslandDone(s.island);
  }

  // Button area'''

MAP_BUTTON = '''    const mapBtn = el("button", {
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
    }, s.introDelay || 2500);'''

# В Уроке 1 счётчик прогресса захардкожен (total: 22) с поправкой на развилку
# 2-2A/2-2B, которая считается одним шагом. Два новых экрана сдвигают индексы,
# поэтому пересчитываем границы. В уроках 2-4 total берётся из linearOrder.length
# и подстраивается сам.
PROGRESS_OLD = """  const idx = linearOrder.indexOf(state.currentId);
  if (idx < 0) return { current: 1, total: 22 };
  let current;
  if (idx <= 3) current = idx + 1;
  else if (idx === 4 || idx === 5) current = 5;
  else current = idx;
  return { current, total: 22 };"""

PROGRESS_NEW = """  const idx = linearOrder.indexOf(state.currentId);
  if (idx < 0) return { current: 1, total: 24 };
  let current;
  if (idx <= 4) current = idx + 1;
  else if (idx === 5 || idx === 6) current = 6;
  else current = idx;
  return { current, total: 24 };"""

OLD_BUTTONS = '''    btnArea.appendChild(restartBtn);
    btnArea.appendChild(finishBtn);
    buttonRevealTimer = setTimeout(() => {
      restartBtn.classList.remove("invisible");
      finishBtn.classList.remove("invisible");
    }, s.introDelay || 2500);'''


def journey_block(n):
    st = STORY[n]
    key_label = ("Ключик от " + st["nextKey"]) if st["nextKey"] else "Четвёртый ключик"
    return '''

// ═══════════════════════════════════════════════════════
// СЮЖЕТ КАРТЫ: вход на остров, ключик на выходе, общий прогресс
// ═══════════════════════════════════════════════════════
const JOURNEY_KEY = "wowspeak_journey";
const MAP_URL = "../../map.html";

/* Карта и уроки лежат на одном домене, поэтому localStorage у них общий.
   Пишем только свой остров, остальные поля карты не трогаем. */
function markIslandDone(n) {
  try {
    const raw = localStorage.getItem(JOURNEY_KEY);
    const j = raw ? JSON.parse(raw) : {};
    if (j["island" + n] === true) return;
    j["island" + n] = true;
    localStorage.setItem(JOURNEY_KEY, JSON.stringify(j));
  } catch (e) { /* приватный режим — прогресс просто не сохранится */ }
}

screens.push(
  { id: "map-in", type: "story", emotion: "smile", singlePhase: true,
    speech: %s,
    icon: "%s", iconLabel: "%s", buttonLabel: "Вперёд!", introDelay: 2600 },
  { id: "map-out", type: "story", emotion: "excited", singlePhase: true, island: %d,
    speech: %s,
    icon: "🔑", iconLabel: "%s", buttonLabel: "Дальше", introDelay: 2600 }
);
linearOrder.splice(1, 0, "map-in");                        // сразу после приветствия
linearOrder.splice(linearOrder.length - 1, 0, "map-out");  // перед прощанием

/* Индекс screenById строится выше, до добавления этих экранов, поэтому перестраиваем:
   без этого currentScreen() вернёт undefined на сюжетном экране и урок упадёт. */
screens.forEach((s, i) => { screenById[s.id] = i; });
''' % (json_str(st["intro"]), st["icon"], st["island"], n, json_str(st["outro"]), key_label)


def json_str(text):
    return '"' + text.replace('\\', '\\\\').replace('"', '\\"') + '"'


def patch(n):
    path = os.path.join(LESSONS, "lesson-%d.html" % n)
    s = open(path, encoding="utf-8").read()
    if "markIslandDone" in s:
        return "уже встроено, пропускаю"

    # 1. ветка отрисовки сюжетного экрана
    assert s.count("\n  // Button area") == 1
    s = s.replace("  }\n\n  // Button area", "  " + STORY_BRANCH, 1)

    # 2. кнопка возврата на карту
    assert s.count(OLD_BUTTONS) == 1
    s = s.replace(OLD_BUTTONS, MAP_BUTTON, 1)

    # 3. экраны, порядок и запись прогресса — после объявления linearOrder
    if n == 1:
        assert s.count(PROGRESS_OLD) == 1, "счётчик прогресса Урока 1 выглядит иначе"
        s = s.replace(PROGRESS_OLD, PROGRESS_NEW, 1)

    m = re.search(r"linearOrder\s*=\s*\[", s)
    end = s.index("];", m.end()) + 2
    s = s[:end] + journey_block(n) + s[end:]

    open(path, "w", encoding="utf-8").write(s)
    return "готово"


if __name__ == "__main__":
    for n in (1, 2, 3, 4):
        print("Урок %d: %s" % (n, patch(n)))
