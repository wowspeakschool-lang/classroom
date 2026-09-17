#!/usr/bin/env python3
"""Временная панель для просмотра: стрелки по экранам и «начать сначала».

Нужна Анне, чтобы смотреть уроки, не проходя задания, и чтобы вернуть карту
в исходное состояние с закрытыми островами. Это НЕ для публикации.

  python3 tools/dev_arrows.py        — включить
  python3 tools/dev_arrows.py --off  — убрать

Панель ставится и в уроки, и на карту, снимается одной командой оттуда и оттуда.

Имена намеренно начинаются с wsdev-: в исходной вёрстке уроков 2-4 уже есть
правило `#dev-nav { left:12px }`, и наша панель с прежним именем уезжала за
левый край экрана — кнопка «назад» была не видна.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")
MAP = os.path.join(ROOT, "map.html")
START = "<!-- DEV-ARROWS-START -->"
END = "<!-- DEV-ARROWS-END -->"

STYLE = """
<style>
  #wsdev-nav{position:fixed; left:50%; bottom:14px; transform:translateX(-50%); z-index:99000;
           display:flex; gap:10px; align-items:center; width:auto; right:auto;
           background:rgba(61,46,104,.88); color:#fff; padding:7px 12px; border-radius:999px;
           font:700 14px/1 -apple-system,Segoe UI,Roboto,sans-serif; box-shadow:0 6px 20px rgba(0,0,0,.3)}
  #wsdev-nav button{all:unset; cursor:pointer; padding:5px 11px; border-radius:999px;
                  background:rgba(255,255,255,.18); white-space:nowrap}
  #wsdev-nav button:hover{background:rgba(255,255,255,.34)}
  #wsdev-nav .wsdev-pos{opacity:.85; min-width:74px; text-align:center}
  #wsdev-nav .wsdev-reset{background:rgba(255,214,110,.28)}
</style>"""

RESET_JS = """
/* Сброс всего прогресса: карта снова с закрытыми островами, уроки — с начала. */
function wsdevReset(){
  var keys = ["wowspeak_journey", "wowspeak_lesson1_progress", "wowspeak_lesson2_progress",
              "wowspeak_lesson3_progress", "wowspeak_lesson4_progress"];
  keys.forEach(function(k){ try { localStorage.removeItem(k); } catch(e) {} });
  /* Урок в едином файле живёт в iframe: перезагружать надо страницу-карту,
     иначе карта останется с прежним прогрессом в памяти. */
  if (window.parent !== window) {
    try { window.parent.postMessage({ type: "wowspeak:reset" }, "*"); return; } catch(e) {}
  }
  location.reload();
}"""

LESSON_BLOCK = START + STYLE + """
<div id="wsdev-nav">
  <button id="wsdev-prev">← назад</button>
  <span class="wsdev-pos" id="wsdev-pos">—</span>
  <button id="wsdev-next">вперёд →</button>
  <button class="wsdev-reset" id="wsdev-reset">↻ начать сначала</button>
</div>
<script>
/* Временная навигация по экранам. Удаляется вместе с этим блоком. */
(function(){
  function idx(){ return linearOrder.indexOf(state.currentId); }
  function show(){
    document.getElementById("wsdev-pos").textContent = (idx() + 1) + " / " + linearOrder.length;
  }
  function step(d){
    var i = idx() + d;
    if (i < 0 || i >= linearOrder.length) return;
    goTo(linearOrder[i]);
    /* экраны с заданием показываем сразу в рабочей фазе, а не на реплике гида */
    var s = screens[screenById[linearOrder[i]]];
    if (s && !s.singlePhase) advancePhase();
    show();
  }
""" + RESET_JS + """
  document.getElementById("wsdev-prev").onclick = function(){ step(-1); };
  document.getElementById("wsdev-next").onclick = function(){ step(1); };
  document.getElementById("wsdev-reset").onclick = wsdevReset;
  document.addEventListener("keydown", function(e){
    if (e.key === "ArrowLeft") step(-1);
    if (e.key === "ArrowRight") step(1);
  });
  setInterval(show, 400);
  show();
})();
</script>
""" + END + "\n"

MAP_BLOCK = START + STYLE + """
<div id="wsdev-nav">
  <span class="wsdev-pos">карта</span>
  <button class="wsdev-reset" id="wsdev-reset">↻ начать сначала</button>
</div>
<script>
/* Временная кнопка сброса на карте. Удаляется вместе с этим блоком. */
(function(){
""" + RESET_JS + """
  document.getElementById("wsdev-reset").onclick = wsdevReset;
  /* Урок из iframe просит сбросить всё — чистим и перезагружаем карту. */
  window.addEventListener("message", function(e){
    if (e && e.data && e.data.type === "wowspeak:reset") wsdevReset();
  });
})();
</script>
""" + END + "\n"


def patch(path, block, on):
    s = open(path, encoding="utf-8").read()
    if START in s:  # снимаем старый блок, чтобы не копился
        s = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", s, flags=re.S)
    if on:
        assert s.count("</body>") == 1, "не найден конец страницы: " + path
        s = s.replace("</body>", block + "</body>", 1)
    open(path, "w", encoding="utf-8").write(s)
    return "включены" if on else "убраны"


if __name__ == "__main__":
    on = "--off" not in sys.argv
    for n in (1, 2, 3, 4):
        print("Урок %d: панель %s" % (n, patch(os.path.join(LESSONS, "lesson-%d.html" % n),
                                               LESSON_BLOCK, on)))
    print("Карта: панель %s" % patch(MAP, MAP_BLOCK, on))
