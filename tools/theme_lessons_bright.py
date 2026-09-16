#!/usr/bin/env python3
"""Яркая тема уроков — тот же мир, что на карте.

Уроки были бледно-сиреневые и плоские, карта — яркая и объёмная. Здесь в каждый
урок дописывается блок стилей: то же небо, что на карте, белые объёмные карточки,
кнопки с нажимаемой гранью, золотая полоса прогресса.

Разметка и логика не трогаются — только оформление, поэтому правка снимается
откатом файла и не может сломать задания.
"""
import base64, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")
WEB = os.path.join(ROOT, "assets", "map", "web")
SKY_TALL = os.path.join(WEB, "sky-lesson-tall.webp")   # телефон, планшет в портрете
SKY_WIDE = os.path.join(WEB, "sky-lesson-wide.webp")   # ноутбук, альбомная ориентация
MARKER = "/* --- яркая тема «Волшебная страна» --- */"


def css():
    tall = base64.b64encode(open(SKY_TALL, "rb").read()).decode()
    wide = base64.b64encode(open(SKY_WIDE, "rb").read()).decode()
    return MARKER + """
:root{
  --accent:#e08a2b;
  --border:#cfe3ef; --border-soft:#e4f1f7;
  --shadow-sm:0 5px 16px rgba(61,46,104,.13);
  --shadow:0 9px 26px rgba(61,46,104,.17);
  --shadow-lg:0 16px 44px rgba(61,46,104,.24);
}

/* Небо уроков — та же картинка, что на карте, но без моря: полоса горизонта
   под текстом смотрелась чужеродно. Вешаем на страницу, а не отдельным слоем. */
html{
  background:#5fd0e8 url("data:image/webp;base64,%s") center top/cover no-repeat fixed;
  min-height:100%%;
}
@media (min-aspect-ratio: 11/10){
  html{ background-image:url("data:image/webp;base64,%s"); background-position:center; }
}
body{ background:transparent; }

/* Под кнопкой «Дальше» в исходной вёрстке лежит белая подложка шириной 100vw
   (.continue-area::before). На бледном фоне её не было видно, на ярком небе
   она резала экран белой полосой во всю ширину. Кнопки контрастные сами. */
.continue-area::before, .intro-button-area::before, .l2-check::before, .l2-sticky::before{
  display:none !important;
}

/* шапка и карточки — белые, объёмные, с крупными скруглениями */
#app > header{
  background:rgba(255,255,255,.9); border-radius:0 0 22px 22px;
  padding:10px 18px 14px; margin:0 -8px 10px; box-shadow:0 4px 16px rgba(61,46,104,.14);
  backdrop-filter:blur(6px);
}
.screen-section{
  border-radius:26px; border:3px solid #fff; padding:28px;
  background:rgba(255,255,255,.95); box-shadow:var(--shadow);
}
#speech-bubble{ border-radius:26px; border:3px solid #fff; box-shadow:var(--shadow); }
#teacher-img{ border-color:#fff !important; box-shadow:var(--shadow-lg); }

/* заголовки лежат прямо на небе — добавляем светлую обводку для читаемости */
.screen-title, .content-instruction{
  text-shadow:0 2px 0 rgba(255,255,255,.95), 0 0 14px rgba(255,255,255,.9);
}

/* кнопки с гранью: нажимается «по-настоящему» */
.btn{ border-radius:18px; font-weight:800; }
.btn-primary{
  background:linear-gradient(180deg,#8a6ad0,#5c3fa2);
  box-shadow:0 5px 0 #46307e, 0 10px 20px rgba(61,46,104,.28);
  border:0;
}
.btn-primary:active{ transform:translateY(4px); box-shadow:0 1px 0 #46307e; }

.progress-bar{ background:rgba(255,255,255,.65); height:9px; border-radius:6px; }
.progress-fill{ background:linear-gradient(90deg,#ffd469,#e08a2b); border-radius:6px; }
""" % (tall, wide)


def patch(n):
    path = os.path.join(LESSONS, "lesson-%d.html" % n)
    s = open(path, encoding="utf-8").read()
    assert s.count("</style>") == 1
    if MARKER in s:
        # блок темы всегда последний перед </style> — вырезаем и кладём заново,
        # иначе повторный запуск молча оставлял бы старую версию оформления
        s = s[:s.index(MARKER)] + s[s.index("</style>"):]
    s = s.replace("</style>", css() + "\n</style>", 1)
    open(path, "w", encoding="utf-8").write(s)
    return "готово (+%.0f КБ)" % (len(css()) / 1024)


if __name__ == "__main__":
    for n in (1, 2, 3, 4):
        print("Урок %d: %s" % (n, patch(n)))
