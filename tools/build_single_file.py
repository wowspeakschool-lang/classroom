#!/usr/bin/env python3
"""Собирает весь лид-магнит в один файл wowspeak.html.

Внутрь кладутся карта (с картинками data-URI) и все четыре урока целиком.
Работать продолжаем по частям — в map.html и lessons/, — а единый файл
пересобирается одной командой:  python3 tools/build_single_file.py

Как устроено: урок хранится текстом в <script type="text/plain"> и при клике
по острову открывается в iframe через srcdoc. Так у каждого урока остаётся своя
область видимости, и четыре скрипта с одинаковыми именами переменных не дерутся
между собой — код уроков при сборке почти не меняется.
"""
import base64, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "assets", "map", "web")
OUT = os.path.join(ROOT, "wowspeak.html")

ASSET_NAMES = ["map-background", "map-background-wide", "island-1-fair", "island-2-mirrors", "island-3-friends",
               "island-4-castle-closed", "island-4-castle-festive", "dragon", "crown"]

# ---- что подменяем в карте ----
ASSET_FN_OLD = '  function asset(name){ return WEB + name + ".webp"; }'
ASSET_FN_NEW = '  function asset(name){ return WOWSPEAK_ASSETS[name]; }'

OPEN_FN_OLD = '  function openLesson(item){ location.href = item.lesson; }'
OPEN_FN_NEW = '''  var lessonFrame = null;

  /* Урок лежит текстом в этой же странице и открывается в iframe:
     своя область видимости, никаких конфликтов между четырьмя уроками. */
  function openLesson(item){
    var node = document.getElementById("lesson-" + item.n);
    if(!node){ showHint("Урок ещё загружается, подожди пару секунд ⏳"); return; }
    var frame = document.createElement("iframe");
    frame.className = "lesson-frame";
    frame.setAttribute("title", item.name);
    /* Оба литерала экранированы: незаэкранированный закрывающий тег скрипта
       оборвал бы этот скрипт прямо здесь — даже внутри строки или комментария. */
    frame.srcdoc = node.textContent.split("<\\\\/script>").join("<\\/script>");
    document.body.appendChild(frame);
    document.body.classList.add("in-lesson");
    lessonFrame = frame;
  }

  function closeLesson(){
    if(lessonFrame && lessonFrame.parentNode) lessonFrame.parentNode.removeChild(lessonFrame);
    lessonFrame = null;
    document.body.classList.remove("in-lesson");
    window.scrollTo(0, 0);
  }'''

# ---- слушатель сообщений от урока, дописывается в конец карты ----
LISTENER = '''
  /* Урок в iframe сообщает о себе сюда: пройден остров и «вернуться на карту». */
  window.addEventListener("message", function(e){
    var msg = e && e.data;
    if(!msg || typeof msg !== "object") return;
    if(msg.type === "wowspeak:done" && msg.island >= 1 && msg.island <= 4){
      journey["island" + msg.island] = true;
      saveJourney(journey);
    } else if(msg.type === "wowspeak:back"){
      closeLesson();
      var seenBefore = journey.seen;
      var openNow = unlockedUpTo();
      render(journey.seen < openNow ? openNow : 0);
      popNewPieces(Math.max(0, seenBefore - 1));
      if(journey.seen !== openNow){
        journey.seen = openNow;
        saveJourney(journey);
      }
    }
  });
'''

EXTRA_CSS = '''
  /* урок поверх карты */
  .lesson-frame{position:fixed; inset:0; width:100%; height:100%; border:0; z-index:60; background:#f6f4fc}
  body.in-lesson{overflow:hidden}
  .loading{
    position:fixed; left:50%; bottom:18px; transform:translateX(-50%);
    background:rgba(61,46,104,.88); color:#fff; font-size:13px; font-weight:700;
    padding:8px 14px; border-radius:999px; z-index:35;
  }
  body.ready .loading{display:none}
'''

# ---- что подменяем в уроке ----
DONE_OLD = """function markIslandDone(n) {
  try {"""
DONE_NEW = """function markIslandDone(n) {
  // в едином файле урок живёт в iframe и сообщает о прохождении наружу
  if (window.parent !== window) {
    try { window.parent.postMessage({ type: "wowspeak:done", island: n }, "*"); } catch (e) {}
  }
  try {"""

BACK_OLD = "onclick: function() { location.href = MAP_URL; },"
BACK_NEW = ("onclick: function() {\n"
            "        if (window.parent !== window) window.parent.postMessage({ type: \"wowspeak:back\" }, \"*\");\n"
            "        else location.href = MAP_URL;\n"
            "      },")


def data_uri(name):
    with open(os.path.join(WEB, name + ".webp"), "rb") as f:
        return "data:image/webp;base64," + base64.b64encode(f.read()).decode()


def build():
    page = open(os.path.join(ROOT, "map.html"), encoding="utf-8").read()

    assets = {n: data_uri(n) for n in ASSET_NAMES}
    assets_js = "<script>\nvar WOWSPEAK_ASSETS = {\n" + ",\n".join(
        '"%s": "%s"' % (n, assets[n]) for n in ASSET_NAMES) + "\n};\n</script>\n"

    for old, new in ((ASSET_FN_OLD, ASSET_FN_NEW), (OPEN_FN_OLD, OPEN_FN_NEW)):
        assert page.count(old) == 1, "не найдено в map.html: " + old[:60]
        page = page.replace(old, new, 1)

    # слушатель — перед закрытием обёртки карты
    assert page.count("})();") == 1
    page = page.replace("})();", LISTENER + "})();", 1)
    page = page.replace("</style>", EXTRA_CSS + "</style>", 1)
    page = page.replace("<title>Карта Волшебной страны · WowSpeak</title>",
                        "<title>WowSpeak · Волшебная страна</title>", 1)
    # картинки должны быть объявлены до скрипта карты
    page = page.replace("<script>\n(function(){", assets_js + "<script>\n(function(){", 1)

    # уроки — в самом конце: карта успевает показаться, пока они ещё качаются
    blobs = []
    for n in (1, 2, 3, 4):
        src = open(os.path.join(ROOT, "lessons", "wowspeak-mini", "lesson-%d.html" % n),
                   encoding="utf-8").read()
        for old, new in ((DONE_OLD, DONE_NEW), (BACK_OLD, BACK_NEW)):
            assert src.count(old) == 1, "не найдено в уроке %d: %s" % (n, old[:40])
            src = src.replace(old, new, 1)
        # все закрывающие теги скриптов урока экранируем, иначе первый же
        # закроет наш контейнер (в уроке их может быть несколько)
        assert src.count("</script>") >= 1
        src = src.replace("</script>", "<\\/script>")
        blobs.append('<script type="text/plain" id="lesson-%d">%s</script>' % (n, src))

    tail = "\n".join(blobs) + '\n<script>document.body.classList.add("ready");</script>\n'
    page = page.replace("</body>", '<div class="loading">Загружаем уроки…</div>\n' + tail + "</body>", 1)

    # Каждый живой </script> должен быть настоящим концом своего блока: их 7 —
    # картинки, карта, четыре урока и флаг готовности. Лишний означает, что
    # литерал "</script>" в коде разрывает скрипт пополам.
    # Открывающих <script внутри текста уроков сколько угодно — парсер внутри
    # скрипта ищет только закрывающий тег. А вот живых </script> должно быть ровно 7:
    # картинки, карта, четыре урока и флаг готовности. Лишний означает, что литерал
    # "</script>" в коде разрывает скрипт пополам.
    assert page.count("</script>") == 7, "закрывающих тегов: %d" % page.count("</script>")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(page)
    print("собрано: %s (%.1f МБ)" % (OUT, os.path.getsize(OUT) / 1048576))


if __name__ == "__main__":
    build()
