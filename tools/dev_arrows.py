#!/usr/bin/env python3
"""Временные стрелки для перелистывания экранов урока.

Нужны Анне, чтобы смотреть уроки, не проходя задания. Это НЕ для публикации.

  python3 tools/dev_arrows.py        — включить
  python3 tools/dev_arrows.py --off  — убрать

Блок помечен маркером, поэтому снимается начисто, без следов в файлах.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")
START = "<!-- DEV-ARROWS-START -->"
END = "<!-- DEV-ARROWS-END -->"

BLOCK = START + """
<style>
  .dev-nav{position:fixed; left:50%; bottom:14px; transform:translateX(-50%); z-index:9000;
           display:flex; gap:10px; align-items:center;
           background:rgba(61,46,104,.88); color:#fff; padding:7px 12px; border-radius:999px;
           font:700 14px/1 -apple-system,Segoe UI,Roboto,sans-serif; box-shadow:0 6px 20px rgba(0,0,0,.3)}
  .dev-nav button{all:unset; cursor:pointer; padding:5px 11px; border-radius:999px;
                  background:rgba(255,255,255,.18)}
  .dev-nav button:hover{background:rgba(255,255,255,.34)}
  .dev-nav span{opacity:.85; min-width:74px; text-align:center}
</style>
<div class="dev-nav" id="dev-nav">
  <button id="dev-prev">← назад</button>
  <span id="dev-pos">—</span>
  <button id="dev-next">вперёд →</button>
</div>
<script>
/* Временная навигация по экранам. Удаляется вместе с этим блоком. */
(function(){
  function idx(){ return linearOrder.indexOf(state.currentId); }
  function show(){
    document.getElementById("dev-pos").textContent = (idx() + 1) + " / " + linearOrder.length;
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
  document.getElementById("dev-prev").onclick = function(){ step(-1); };
  document.getElementById("dev-next").onclick = function(){ step(1); };
  document.addEventListener("keydown", function(e){
    if (e.key === "ArrowLeft") step(-1);
    if (e.key === "ArrowRight") step(1);
  });
  setInterval(show, 400);
  show();
})();
</script>
""" + END + "\n"


def patch(n, on):
    path = os.path.join(LESSONS, "lesson-%d.html" % n)
    s = open(path, encoding="utf-8").read()
    if START in s:  # снимаем старый блок, чтобы не копился
        s = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", s, flags=re.S)
    if on:
        assert s.count("</body>") == 1
        s = s.replace("</body>", BLOCK + "</body>", 1)
    open(path, "w", encoding="utf-8").write(s)
    return "включены" if on else "убраны"


if __name__ == "__main__":
    on = "--off" not in sys.argv
    for n in (1, 2, 3, 4):
        print("Урок %d: стрелки %s" % (n, patch(n, on)))
