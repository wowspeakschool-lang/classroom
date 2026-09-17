#!/usr/bin/env python3
"""Звёздочка-подсказка в игре «Собери слово из букв» (Урок 1).

На экране 1-3 Хранительница вручает звёздочку и говорит, что она подсказывает.
До этого обещание ничем не подкреплялось: предмет лежал в рюкзаке и больше нигде
не появлялся. Теперь в анаграмме есть кнопка со звёздочкой — она ставит
следующую букву.

Подсказка не дублирует логику игры, а нажимает нужную плитку сама: так проверка,
звук и завершение слова остаются в одном месте.

Запуск: python3 tools/add_star_hint.py
"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSON = os.path.join(ROOT, "lessons", "wowspeak-mini", "lesson-1.html")

ANCHOR = "      card.appendChild(tilesRow);"

BLOCK = '''      card.appendChild(tilesRow);

      /* Звёздочка из рюкзака: ставит следующую букву. Нажимаем нужную плитку
         сами, чтобы проверка и озвучка остались в одном месте. */
      const hintBtn = el("button", { class: "star-hint" });
      hintBtn.appendChild(el("span", { class: "star-hint-pic" }, picNode("star", "⭐")));
      hintBtn.appendChild(el("span", {}, "Подсказка"));
      hintBtn.addEventListener("click", function() {
        if (currentIdx >= lettersOnly.length) return;
        const expected = lettersOnly[currentIdx];
        const tiles = tilesRow.querySelectorAll(".anagram-tile");
        for (let i = 0; i < tiles.length; i++) {
          if (!tiles[i].classList.contains("used") && tiles[i].textContent === expected) {
            tiles[i].click();
            break;
          }
        }
      });
      card.appendChild(hintBtn);'''

CSS = """
/* звёздочка-подсказка в анаграмме */
.star-hint { display:flex; align-items:center; gap:8px; margin:14px auto 0; cursor:pointer;
  background:var(--gold-bg, #FFF6E2); border:2px solid #F0C44C; color:#8A6A12;
  font-weight:700; font-size:16px; padding:8px 16px; border-radius:999px; }
.star-hint:hover { background:#FFEFC9; }
.star-hint .star-hint-pic { display:inline-flex; }
.star-hint .star-hint-pic .asset-img { height:26px; width:auto; }
"""

CSS_MARK = "/* звёздочка-подсказка в анаграмме */"


def main():
    s = open(LESSON, encoding="utf-8").read()
    steps = []
    if "star-hint" not in s:
        assert s.count(ANCHOR) == 1, "не найден якорь в анаграмме"
        s = s.replace(ANCHOR, BLOCK, 1)
        steps.append("кнопка добавлена")
    else:
        steps.append("кнопка уже стоит")
    if CSS_MARK not in s:
        assert s.count("</style>") >= 1
        s = s.replace("</style>", CSS + "</style>", 1)
        steps.append("стиль добавлен")
    else:
        steps.append("стиль уже есть")
    open(LESSON, "w", encoding="utf-8").write(s)
    print("Урок 1: " + "; ".join(steps))


if __name__ == "__main__":
    main()
