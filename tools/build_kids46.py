#!/usr/bin/env python3
"""Собирает лид-магнит 4–6 «Дорога на праздник» одним файлом.

    python3 tools/build_kids46.py

На выходе — `wowspeak-4-6.html`: карта и три урока в одном файле, картинки
внутри, ничего не подгружается из сети.

Уроки здесь не правятся руками: вся структура лежит в LESSONS ниже, а HTML
собирается из неё. Поправили спецификацию — пересобрали.

Звук: если в `assets/audio-4-6/` лежат файлы `RU-01.mp3`, `EN-01.mp3` и так
далее, они вшиваются в файл. Пока их нет, реплики проговаривает синтез
браузера — чтобы урок можно было листать и проверять уже сейчас.
"""

import base64
import io
import json
import os
import re
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "wowspeak-4-6.html"
AUDIO_DIR = ROOT / "assets" / "audio-4-6"


# ──────────────────────────────────────────────────────────── картинки ──

def cut_white(im, tol=18):
    """Убирает белый фон в два прохода: от краёв и замкнутые белые пятна.

    Второй проход нужен из-за дырок внутри предмета — у ключика в версии
    7–9 внутри кольца оставалось белое пятно. Порог 0.3% площади: блики
    на золоте желтоватые и под него не попадают.
    """
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()
    lim = 255 - tol

    def white(x, y):
        r, g, b, a = px[x, y]
        return a > 0 and r >= lim and g >= lim and b >= lim

    seen = bytearray(w * h)
    stack = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
    while stack:
        x, y = stack.pop()
        if x < 0 or y < 0 or x >= w or y >= h or seen[y * w + x]:
            continue
        if not white(x, y):
            continue
        seen[y * w + x] = 1
        r, g, b, a = px[x, y]
        px[x, y] = (r, g, b, 0)
        stack.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))

    # второй проход: замкнутые белые области крупнее 0.3% картинки
    floor = int(w * h * 0.003)
    for sy in range(0, h, 4):
        for sx in range(0, w, 4):
            if seen[sy * w + sx] or not white(sx, sy):
                continue
            blob = []
            stack = [(sx, sy)]
            while stack:
                x, y = stack.pop()
                if x < 0 or y < 0 or x >= w or y >= h or seen[y * w + x]:
                    continue
                if not white(x, y):
                    continue
                seen[y * w + x] = 1
                blob.append((x, y))
                stack.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
            if len(blob) >= floor:
                for x, y in blob:
                    r, g, b, a = px[x, y]
                    px[x, y] = (r, g, b, 0)
    return im


def prepare(path, width, transparent=True, quality=82):
    im = Image.open(path)
    if transparent:
        im = cut_white(im)
        box = im.getbbox()
        if box:
            im = im.crop(box)
    else:
        im = im.convert("RGB")
    if im.width > width:
        height = round(im.height * width / im.width)
        im = im.resize((width, height), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=quality, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


# имя → (файл, ширина, вырезать ли белый фон)
PICTURES = {
    "map_bg":        ("assets/kids-4-6/map-background-wide.webp", 1600, False),
    "meadow":        ("assets/kids-4-6/island-meadow.webp",        560, True),
    "clouds":        ("assets/kids-4-6/island-clouds.webp",        560, True),
    "dragon":        ("assets/kids-4-6/island-dragon.webp",        560, True),
    "firefly":       ("assets/kids-4-6/firefly-neutral.webp",      300, True),
    "firefly_smile": ("assets/kids-4-6/firefly-smile.webp",        300, True),
    "firefly_wow":   ("assets/kids-4-6/firefly-excited.webp",      300, True),
    "firefly_lamp":  ("assets/kids-4-6/firefly-lantern.webp",      420, False),
    "stone":         ("assets/kids-4-6/stone.webp",                220, True),
    "cloudlet":      ("assets/kids-4-6/cloudlet.webp",             220, True),
    "egg":           ("assets/kids-4-6/egg.webp",                  560, True),
    "cave_closed":   ("assets/kids-4-6/cave-closed.webp",          620, True),
    "cave_open":     ("assets/kids-4-6/cave-open.webp",            620, True),
    "bunny":         ("assets/kids-4-6/animal-bunny.webp",         360, True),
    "hedgehog":      ("assets/kids-4-6/animal-hedgehog.webp",      360, True),
    "fox":           ("assets/kids-4-6/animal-fox.webp",           360, True),
    "push":          ("assets/kids-4-6/friends-push.webp",         900, True),
    "cap":           ("assets/lesson-1/cap.webp",                  320, True),
    "top":           ("assets/lesson-1/tshirt.webp",               320, True),
    "jeans":         ("assets/lesson-1/jeans.webp",                320, True),
    "shoes":         ("assets/lesson-1/shoes.webp",                320, True),
    "skirt":         ("assets/lesson-1/skirt.webp",                320, True),
    "jacket":        ("assets/lesson-1/jacket.webp",               320, True),
    "socks":         ("assets/lesson-1/socks.webp",                320, True),
    "backpack":      ("assets/lesson-1/backpack.webp",             320, True),
}

WORDS = {
    "cap":   ("a cap", "EN-01"),
    "top":   ("a top", "EN-02"),
    "jeans": ("jeans", "EN-03"),
    "shoes": ("shoes", "EN-04"),
    "skirt": ("a skirt", "EN-05"),
}


# ─────────────────────────────────────────────────────────────── уроки ──
#
# Типы экранов:
#   story  — картинка и реплика, кнопка «дальше» появляется сама
#   word   — слово крупно: слушаем, повторяем вслух, жмём «я сказал»
#   pick   — две картинки, показать названную; rounds = список раундов
#   pairs  — найди пару: восемь карточек, четыре пары
#   parent — экран для взрослого: назвать вслух всё выученное
#
# В pick у раунда может быть `who` (кто просит) и `join` (кто прибегает
# на помощь после верного ответа).

LESSONS = [
    {
        "id": 1,
        "title": "Солнечная Полянка",
        "island": "meadow",
        "token": "stone",
        "token_word": "камушки",
        "words": ["cap", "top"],
        "screens": [
            {"t": "story", "pic": "firefly_wow", "ru": "RU-01",
             "text": "Привет! Я светлячок Искорка. Смотри, что мне принесли — "
                     "приглашение! Нас зовут на праздник на Драконий Остров. Полетели!",
             "btn": "Полетели!"},
            {"t": "story", "pics": ["meadow", "clouds", "dragon"], "ru": "RU-02",
             "text": "Вот наша дорога. Три острова. Ой… а дорожек между ними нет. "
                     "Ничего, мы что-нибудь придумаем!"},
            {"t": "story", "pic": "meadow", "ru": "RU-03",
             "text": "Это Солнечная Полянка. Тут живут зверята. Ой, ветер разбросал "
                     "все их вещи! Давай поможем собрать."},
            {"t": "word", "key": "cap", "ru": "RU-04",
             "text": "Смотри, это кепка. По-английски — a cap. Скажи вслух: a cap."},
            {"t": "pick", "ru": "RU-05", "text": "Найди кепку. Где тут a cap?",
             "rounds": [
                 {"target": "cap", "other": "jacket"},
                 {"target": "cap", "other": "socks"},
                 {"target": "cap", "other": "backpack"},
             ]},
            {"t": "word", "key": "top", "ru": "RU-06",
             "text": "А это кофточка. По-английски — a top. Скажи вслух: a top."},
            {"t": "pick", "ru": "RU-07", "text": "Слушай внимательно и показывай.",
             "rounds": [
                 {"target": "top", "other": "cap"},
                 {"target": "cap", "other": "top"},
                 {"target": "top", "other": "socks"},
                 {"target": "cap", "other": "jacket"},
             ]},
            {"t": "pick", "ru": "RU-08",
             "text": "Зверята ждут свои вещи. Дай каждому то, что он просит.",
             "rounds": [
                 {"who": "bunny", "target": "cap", "other": "top"},
                 {"who": "hedgehog", "target": "top", "other": "cap"},
                 {"who": "fox", "target": "cap", "other": "socks"},
             ]},
            {"t": "story", "reward": "stone", "count": 3, "ru": "RU-09",
             "text": "Спасибо! За помощь зверята дают тебе три волшебных камушка."},
            {"t": "story", "path": "stone", "ru": "RU-10",
             "text": "Смотри, что получилось! Камушки легли в воду дорожкой. "
                     "Теперь можно идти дальше!"},
            {"t": "parent", "keys": ["cap", "top"], "ru": "RU-11",
             "text": "А теперь позови маму или папу и назови всё, что ты сегодня выучил."},
        ],
    },
    {
        "id": 2,
        "title": "Облачный Остров",
        "island": "clouds",
        "token": "cloudlet",
        "token_word": "облачка",
        "words": ["jeans", "shoes"],
        "screens": [
            {"t": "story", "pic": "clouds", "ru": "RU-12",
             "text": "Мы на Облачном Острове! Тут всё мягкое, как подушки."},
            {"t": "story", "pic": "clouds", "ru": "RU-13",
             "text": "Ой… впереди пропасть, а мостика нет. Надо что-то придумать."},
            {"t": "word", "key": "jeans", "ru": "RU-14",
             "text": "Смотри, это джинсы. По-английски — jeans. Скажи вслух: jeans."},
            {"t": "pick", "ru": "RU-15", "text": "Где тут jeans? Покажи.",
             "rounds": [
                 {"target": "jeans", "other": "cap"},
                 {"target": "jeans", "other": "top"},
                 {"target": "jeans", "other": "backpack"},
             ]},
            {"t": "word", "key": "shoes", "ru": "RU-16",
             "text": "А это ботинки. По-английски — shoes. Скажи вслух: shoes."},
            {"t": "pick", "ru": "RU-17", "text": "Слушай и показывай.",
             "rounds": [
                 {"target": "shoes", "other": "jeans"},
                 {"target": "jeans", "other": "shoes"},
                 {"target": "shoes", "other": "cap"},
                 {"target": "shoes", "other": "socks"},
             ]},
            {"t": "pick", "ru": "RU-18",
             "text": "Зверята тоже собираются на праздник. Помоги им одеться!",
             "rounds": [
                 {"who": "fox", "target": "jeans", "other": "top"},
                 {"who": "bunny", "target": "shoes", "other": "cap"},
                 {"who": "hedgehog", "target": "jeans", "other": "shoes"},
             ]},
            {"t": "story", "reward": "cloudlet", "count": 3, "ru": "RU-19",
             "text": "Спасибо! Вот тебе три облачка."},
            {"t": "story", "path": "cloudlet", "ru": "RU-20",
             "text": "Смотри! Облачка встали мостиком. Прыгаем на Драконий Остров!"},
            {"t": "parent", "keys": ["cap", "top", "jeans", "shoes"], "ru": "RU-21",
             "text": "Позови маму или папу и назови всё, что ты выучил сегодня."},
        ],
    },
    {
        "id": 3,
        "title": "Драконий Остров",
        "island": "dragon",
        "token": "friend",
        "token_word": "друзья",
        "words": ["skirt"],
        "screens": [
            {"t": "story", "pic": "dragon", "ru": "RU-22",
             "text": "Мы на Драконьем Острове! Вот и праздник: флажки, фонарики… "
                     "А где же все? Никого нет. Как странно."},
            {"t": "word", "key": "skirt", "ru": "RU-23",
             "text": "Смотри, это юбка. По-английски — a skirt. Скажи вслух: a skirt."},
            {"t": "pick", "ru": "RU-24", "text": "На празднике надо нарядиться! Выбирай, что наденешь.",
             "rounds": [
                 {"target": "skirt", "other": "jeans"},
                 {"target": "cap", "other": "shoes"},
                 {"target": "top", "other": "skirt"},
                 {"target": "shoes", "other": "cap"},
                 {"target": "jeans", "other": "top"},
             ]},
            {"t": "story", "pic": "dragon", "ru": "RU-25",
             "text": "Ой, смотри! Кто-то тут был. Следы ведут вон туда, к камням."},
            {"t": "pairs", "ru": "RU-26",
             "text": "Помоги разобрать вещи — и мы пойдём по следам дальше.",
             "keys": ["cap", "top", "jeans", "shoes"]},
            {"t": "story", "pic": "cave_closed", "ru": "RU-27",
             "text": "Следы привели нас к пещере. Интересно, кто там?"},
            {"t": "story", "pic": "cave_closed", "ru": "RU-28",
             "text": "Вход завален большим камнем. Одному не сдвинуть… Нужны друзья!"},
            {"t": "pick", "ru": "RU-29", "text": "Вспомни, кому мы сегодня помогали. Позови их!",
             "rounds": [
                 {"target": "cap", "other": "skirt", "join": "bunny"},
                 {"target": "shoes", "other": "top", "join": "hedgehog"},
                 {"target": "jeans", "other": "cap", "join": "fox"},
             ]},
            {"t": "story", "pic": "push", "ru": "RU-30",
             "text": "Раз, два, взяли! Толкаем все вместе!", "btn": "Помочь!"},
            {"t": "story", "pic": "cave_open", "ru": "RU-31",
             "text": "Получилось! Как темно… Подожди, я посвечу. Смотри — гнёздышко. А в нём яйцо!"},
            {"t": "story", "pic": "egg", "ru": "RU-32",
             "text": "Интересно, кто же в нём? Неужели дракончик? Узнаем на первом уроке!"},
            {"t": "parent", "keys": ["cap", "top", "jeans", "shoes", "skirt"], "ru": "RU-33",
             "text": "Позови маму или папу и назови всё, что ты выучил."},
        ],
    },
]

# Реплики, которые нужны движку вне экранов: похвала и «попробуй ещё».
PRAISE = [
    ("RU-34", "Молодец!"),
    ("RU-35", "Правильно!"),
    ("RU-36", "Верно! Умница!"),
    ("RU-37", "Получилось!"),
    ("RU-40", "Ух ты, как здорово!"),
]
RETRY = [
    ("RU-38", "Ой, не то. Попробуй ещё разок."),
    ("RU-39", "Почти! Давай ещё раз."),
]


def collect_audio():
    """Вшивает записанные дорожки, если они уже лежат в assets/audio-4-6/."""
    out = {}
    if not AUDIO_DIR.is_dir():
        return out
    for f in sorted(AUDIO_DIR.iterdir()):
        if f.suffix.lower() not in (".mp3", ".m4a", ".ogg", ".wav"):
            continue
        mime = {"mp3": "audio/mpeg", "m4a": "audio/mp4",
                "ogg": "audio/ogg", "wav": "audio/wav"}[f.suffix.lower().lstrip(".")]
        out[f.stem.upper()] = (
            f"data:{mime};base64," + base64.b64encode(f.read_bytes()).decode()
        )
    return out


HTML = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Волшебная страна — путешествие на праздник</title>
<style>
:root{
  --sky:#bfe9ff; --sea:#7fd4e8; --card:#fffdf7; --ink:#3a2f4a;
  --accent:#ff9d3c; --accent-dark:#f07c15; --good:#5ec26a; --bad:#ff8a8a;
  --shadow:0 10px 24px rgba(60,40,90,.18);
}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;height:100%;overflow:hidden}
body{
  font-family:"Nunito","Comic Sans MS",system-ui,-apple-system,"Segoe UI",sans-serif;
  color:var(--ink); background:var(--sky);
  user-select:none; -webkit-user-select:none;
}
img{-webkit-user-drag:none}
#app{position:fixed;inset:0;display:flex;flex-direction:column}

/* ───────── карта ───────── */
#map{position:absolute;inset:0;display:none;background:#bfe9ff center/cover no-repeat}
#map.on{display:block}
.island{position:absolute;transform:translate(-50%,-50%);width:30%;max-width:420px;
  border:0;background:none;padding:0;cursor:pointer;transition:transform .2s}
.island img{width:100%;display:block;filter:drop-shadow(0 12px 18px rgba(40,60,90,.25))}
.island:active{transform:translate(-50%,-50%) scale(.96)}
.island .name{display:block;margin-top:-6px;font-size:clamp(13px,2.4vw,22px);font-weight:800;
  color:#fff;text-shadow:0 2px 6px rgba(40,60,90,.6)}
.island.locked img{filter:grayscale(.55) brightness(.9) drop-shadow(0 12px 18px rgba(40,60,90,.25))}
.island.locked .name{opacity:.8}
.island .tick{position:absolute;top:2%;right:8%;font-size:clamp(22px,4vw,40px)}
.island .lock{position:absolute;top:8%;left:50%;transform:translateX(-50%);
  font-size:clamp(20px,3.6vw,36px);filter:drop-shadow(0 2px 4px rgba(0,0,0,.35))}
.bridge{position:absolute;transform:translate(-50%,-50%);width:6%;max-width:80px;
  opacity:0;transition:opacity .5s}
.bridge.on{opacity:1}
.bridge img{width:100%;display:block}
/* Светлячок стоит в пустом море по центру: у левого края он наезжал
   на подпись первого острова на узком экране. */
#map .guide{position:absolute;left:50%;bottom:1%;transform:translateX(-50%);
  width:13%;max-width:150px}
#map .guide img{width:100%;display:block}
#map .maptitle{position:absolute;left:50%;top:3%;transform:translateX(-50%);
  font-size:clamp(16px,3vw,30px);font-weight:900;color:#fff;
  text-shadow:0 3px 10px rgba(40,60,90,.55);white-space:nowrap}

/* ───────── урок ───────── */
#lesson{position:absolute;inset:0;display:none;flex-direction:column;
  background:linear-gradient(180deg,#d9f3ff 0%,#fff4de 100%)}
#lesson.on{display:flex}
.topbar{flex:0 0 auto;display:flex;align-items:center;gap:10px;padding:8px 14px}
.topbar .home{border:0;background:rgba(255,255,255,.75);border-radius:999px;
  width:44px;height:44px;font-size:22px;cursor:pointer;box-shadow:var(--shadow)}
.topbar .tokens{display:flex;gap:6px;margin-left:auto}
.topbar .tokens img{width:38px;height:38px;object-fit:contain}
.topbar .tokens .ghost{width:38px;height:38px;border-radius:50%;
  background:rgba(255,255,255,.45);border:2px dashed rgba(120,110,140,.35)}

.stage{flex:1 1 auto;display:flex;align-items:center;gap:2vw;padding:0 3vw 6px;
  min-height:0;overflow:hidden}
.guide{flex:0 0 22%;max-width:240px;display:flex;flex-direction:column;align-items:center}
.guide img{width:100%;max-width:190px;display:block}
.bubble{background:var(--card);border-radius:20px;padding:10px 14px;box-shadow:var(--shadow);
  font-size:clamp(13px,1.7vw,19px);line-height:1.35;text-align:center;margin-top:-6px}

/* Высота картинок считается от свободного места, а не подбирается в vh:
   иначе на низком экране содержимое наползает на кнопку и перехватывает
   нажатие — проверка ловила это на родительском экране. */
.content{flex:1 1 auto;display:flex;flex-direction:column;align-items:center;
  justify-content:center;gap:1vh;min-width:0;min-height:0;height:100%;overflow:hidden}
.picarea{flex:1 1 0;min-height:0;width:100%;display:flex;align-items:center;
  justify-content:center;gap:2vw}
.picarea img{height:100%;max-width:100%;object-fit:contain;
  filter:drop-shadow(0 8px 16px rgba(40,60,90,.2))}
.picarea.who{flex:0 1 38%;min-height:20%}
.below{flex:0 0 auto;display:flex;flex-direction:column;align-items:center;gap:1vh}
.wordline{font-size:clamp(24px,4.4vw,52px);font-weight:900;letter-spacing:.5px}

/* Карточки — квадратные: сторона считается от реального размера ряда,
   который js кладёт в --bw/--bh. Иначе на широком экране карточка
   растягивается в колонну, а картинка тонет в белом поле. */
.cards{--n:2;--gap:3vw;gap:var(--gap)}
.card{background:var(--card);border:4px solid transparent;border-radius:28px;
  box-shadow:var(--shadow);padding:1.4%;cursor:pointer;flex:0 0 auto;
  --side:min(calc((var(--bw,100%) - (var(--n) - 1) * var(--gap)) / var(--n)),
             var(--bh,100%), 420px);
  width:var(--side);height:var(--side);
  display:flex;align-items:center;justify-content:center;
  transition:transform .15s,border-color .2s}
.card img{height:100%;width:100%;object-fit:contain;display:block}
.card:active{transform:scale(.96)}
.card.right{border-color:var(--good);animation:pop .4s}
.card.wrong{border-color:var(--bad);animation:shake .4s}
@keyframes pop{50%{transform:scale(1.08)}}
@keyframes shake{25%{transform:translateX(-10px)}75%{transform:translateX(10px)}}

.grid{flex:1 1 0;min-height:0;width:100%;display:grid;--gap:1.4vw;gap:var(--gap);
  --cell:min(calc((var(--bw,100%) - 3 * var(--gap)) / 4),
             calc((var(--bh,100%) - var(--gap)) / 2), 190px);
  grid-template-columns:repeat(4,var(--cell));grid-template-rows:repeat(2,var(--cell));
  justify-content:center;align-content:center}
.grid .card{padding:6%;border-radius:18px;width:auto;height:auto;min-height:0}
.grid .card.gone{visibility:hidden}
.grid .card.picked{border-color:var(--accent)}

.joined{flex:0 0 auto;height:14%;display:flex;gap:1.5vw;align-items:flex-end;justify-content:center}
.joined img{height:100%;object-fit:contain;animation:pop .5s}

.bottombar{flex:0 0 auto;display:flex;gap:12px;align-items:center;justify-content:center;
  padding:6px 14px calc(10px + env(safe-area-inset-bottom))}
.btn{border:0;border-radius:999px;padding:14px 30px;font:inherit;font-weight:900;
  font-size:clamp(15px,2.2vw,22px);color:#fff;background:var(--accent);
  box-shadow:var(--shadow);cursor:pointer}
.btn:active{transform:translateY(2px)}
.btn.ghost{background:#fff;color:var(--ink)}
.btn.big{padding:16px 40px}
.btn[hidden]{display:none}

#overlay{position:absolute;inset:0;display:none;align-items:center;justify-content:center;
  background:rgba(40,30,60,.5);backdrop-filter:blur(3px);z-index:20}
#overlay.on{display:flex}
.panel{background:var(--card);border-radius:28px;padding:28px 32px;text-align:center;
  box-shadow:var(--shadow);max-width:min(90%,560px)}
.panel h2{margin:0 0 6px;font-size:clamp(20px,3.4vw,30px)}
.panel p{margin:0 0 18px;font-size:clamp(14px,2vw,19px);line-height:1.4}
.panel .row{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}

#wsdev{position:absolute;right:10px;top:10px;z-index:30;display:none;gap:6px}
#wsdev.on{display:flex}
#wsdev button{border:0;border-radius:10px;background:rgba(0,0,0,.55);color:#fff;
  font:inherit;font-size:13px;padding:6px 10px;cursor:pointer}

@media (max-aspect-ratio:1/1){
  .stage{flex-direction:column;gap:1vh;padding-top:4px}
  .guide{flex:0 0 auto;max-width:none;width:100%;flex-direction:row;align-items:center;gap:10px}
  .guide img{width:22%;max-width:110px}
  .bubble{margin-top:0;text-align:left;flex:1 1 auto;font-size:clamp(13px,3.4vw,18px)}
  .content{flex:1 1 auto;height:auto}
  .cards{gap:4vw}
}
</style>
</head>
<body>
<div id="app">
  <div id="map">
    <div class="maptitle"></div>
  </div>
  <div id="lesson">
    <div class="topbar">
      <button class="home" title="На карту">🗺️</button>
      <div class="tokens"></div>
    </div>
    <div class="stage">
      <div class="guide"><img alt=""><div class="bubble"></div></div>
      <div class="content"></div>
    </div>
    <div class="bottombar">
      <button class="btn ghost listen">🔊 Ещё раз</button>
      <button class="btn next" hidden>Дальше ▶</button>
    </div>
  </div>
  <div id="overlay"><div class="panel"></div></div>
  <div id="wsdev">
    <button data-act="prev">◀</button>
    <button data-act="next">▶</button>
    <button data-act="reset">↻ сначала</button>
  </div>
</div>
<script>
const IMG = __IMG__;
const AUDIO = __AUDIO__;
const LESSONS = __LESSONS__;
const PRAISE = __PRAISE__;
const RETRY = __RETRY__;
const WORDS = __WORDS__;
const STORE = "ws46_progress";

/* ─────────────────────────── звук ─────────────────────────── */
let current = null;
function stopSound(){
  if (current){ try{ current.pause(); }catch(e){} current = null; }
  try{ speechSynthesis.cancel(); }catch(e){}
}
function play(key, text, lang){
  stopSound();
  return new Promise(resolve => {
    // Страховка: без неё экран навсегда ждёт события, которое может не прийти —
    // синтез в вебвью и на телефоне молча не отвечает, и урок встаёт намертво.
    let done = false;
    const finish = () => { if (!done){ done = true; clearTimeout(timer); resolve(); } };
    const limit = Math.min(12000, 1800 + (text ? text.length * 90 : 0));
    const timer = setTimeout(finish, limit);
    const src = AUDIO[key];
    if (src){
      const a = new Audio(src);
      current = a;
      a.onended = a.onerror = finish;
      a.play().catch(finish);
      return;
    }
    // Записи ещё нет — проговаривает браузер, чтобы урок можно было проверять.
    if (!text || !("speechSynthesis" in window)) { finish(); return; }
    try{
      const u = new SpeechSynthesisUtterance(text);
      u.lang = lang || "ru-RU";
      u.rate = lang === "en-US" ? 0.8 : 0.95;
      u.onend = u.onerror = finish;
      speechSynthesis.speak(u);
    } catch(e){ finish(); }
  });
}
const pick = arr => arr[Math.floor(Math.random() * arr.length)];
function praise(){ const p = pick(PRAISE); return play(p[0], p[1]); }
function retry(){ const p = pick(RETRY); return play(p[0], p[1]); }
function shuffle(a){
  a = a.slice();
  for (let i = a.length - 1; i > 0; i--){
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/* ───────────────────────── прогресс ───────────────────────── */
function progress(){
  try { return JSON.parse(localStorage.getItem(STORE)) || {done:[]}; }
  catch(e){ return {done:[]}; }
}
function saveProgress(p){
  try { localStorage.setItem(STORE, JSON.stringify(p)); } catch(e){}
}
function isDone(id){ return progress().done.indexOf(id) >= 0; }
function unlocked(id){ return id === 1 || isDone(id - 1); }

/* ─────────────────────────── карта ────────────────────────── */
const mapEl = document.getElementById("map");
const lessonEl = document.getElementById("lesson");
const overlay = document.getElementById("overlay");
const ISLAND_POS = [[20, 60], [50, 38], [80, 62]];

function buildMap(){
  mapEl.style.backgroundImage = "url(" + IMG.map_bg + ")";
  mapEl.innerHTML = '<div class="maptitle">Дорога на праздник</div>';
  LESSONS.forEach((les, i) => {
    const b = document.createElement("button");
    b.className = "island" + (unlocked(les.id) ? "" : " locked");
    b.style.left = ISLAND_POS[i][0] + "%";
    b.style.top = ISLAND_POS[i][1] + "%";
    b.innerHTML = '<img src="' + IMG[les.island] + '" alt="">' +
      '<span class="name">' + les.title + "</span>" +
      (isDone(les.id) ? '<span class="tick">⭐</span>' : "") +
      (unlocked(les.id) ? "" : '<span class="lock">🔒</span>');
    b.onclick = () => {
      if (!unlocked(les.id)){
        play(null, "Сначала пройдём остров пораньше.", "ru-RU");
        return;
      }
      startLesson(i);
    };
    mapEl.appendChild(b);
    // мостик к следующему острову
    if (i < LESSONS.length - 1){
      const token = les.token === "friend" ? "stone" : les.token;
      for (let k = 0; k < 3; k++){
        const d = document.createElement("div");
        const t = (k + 1) / 4;
        d.className = "bridge" + (isDone(les.id) ? " on" : "");
        d.style.left = (ISLAND_POS[i][0] + (ISLAND_POS[i+1][0] - ISLAND_POS[i][0]) * t) + "%";
        d.style.top = (ISLAND_POS[i][1] + (ISLAND_POS[i+1][1] - ISLAND_POS[i][1]) * t + 14) + "%";
        d.innerHTML = '<img src="' + IMG[token] + '" alt="">';
        mapEl.appendChild(d);
      }
    }
  });
  const g = document.createElement("div");
  g.className = "guide";
  g.innerHTML = '<img src="' + IMG.firefly_smile + '" alt="">';
  mapEl.appendChild(g);
}
function showMap(){
  stopSound();
  buildMap();
  mapEl.classList.add("on");
  lessonEl.classList.remove("on");
  overlay.classList.remove("on");
}

/* ─────────────────────────── урок ─────────────────────────── */
const guideImg = lessonEl.querySelector(".guide img");
const bubble = lessonEl.querySelector(".bubble");
const content = lessonEl.querySelector(".content");
const tokensEl = lessonEl.querySelector(".tokens");
const btnNext = lessonEl.querySelector(".next");
const btnListen = lessonEl.querySelector(".listen");

let L = 0, S = 0, round = 0, joined = [], earned = 0;

function startLesson(i){
  L = i; S = 0; round = 0; joined = []; earned = 0;
  mapEl.classList.remove("on");
  lessonEl.classList.add("on");
  render();
}
function lesson(){ return LESSONS[L]; }
function screen(){ return lesson().screens[S]; }

function drawTokens(){
  const total = 3;
  if (lesson().token === "friend") earned = joined.length;
  let html = "";
  for (let i = 0; i < total; i++){
    const key = lesson().token === "friend" ? ["bunny","hedgehog","fox"][i] : lesson().token;
    html += i < earned
      ? '<img src="' + IMG[key] + '" alt="">'
      : '<div class="ghost"></div>';
  }
  tokensEl.innerHTML = html;
}

function say(){
  const s = screen();
  return play(s.ru, s.text, "ru-RU");
}

function render(){
  stopSound();
  const s = screen();
  guideImg.src = IMG[s.t === "story" && s.reward ? "firefly_wow" : "firefly"];
  bubble.textContent = s.text || "";
  content.innerHTML = "";
  btnNext.hidden = true;
  btnNext.textContent = s.btn || "Дальше ▶";
  btnListen.hidden = false;
  drawTokens();
  const draw = RENDER[s.t];
  draw(s);
  fit();
  say();
}

/* Ряду карточек нужен его собственный размер в пикселях: от него считается
   сторона квадрата. Зацикливания нет — высота ряда задана флексом с
   basis 0 и от содержимого не зависит. */
function fit(){
  content.querySelectorAll(".cards, .grid").forEach(el => {
    const r = el.getBoundingClientRect();
    el.style.setProperty("--bw", r.width + "px");
    el.style.setProperty("--bh", r.height + "px");
  });
}
window.addEventListener("resize", () => { fit(); setTimeout(fit, 120); });

const RENDER = {};

function picArea(keys, extraClass){
  const area = document.createElement("div");
  area.className = "picarea" + (extraClass ? " " + extraClass : "");
  keys.forEach(k => {
    const im = document.createElement("img");
    im.src = IMG[k];
    area.appendChild(im);
  });
  return area;
}

RENDER.story = function(s){
  if (s.pics){
    content.appendChild(picArea(s.pics));
  } else if (s.reward || s.path){
    const key = s.reward || s.path;
    const n = s.count || 3;
    const keys = [];
    for (let i = 0; i < n; i++) keys.push(key === "friend" ? "bunny" : key);
    const area = picArea(keys);
    [...area.children].forEach((im, i) => {
      im.style.animation = "pop .5s " + (i * 0.25) + "s both";
    });
    content.appendChild(area);
    if (s.reward) earned = n;
    drawTokens();
  } else {
    content.appendChild(picArea([s.pic]));
  }
  setTimeout(() => { btnNext.hidden = false; }, 2000);
};

RENDER.word = function(s){
  content.appendChild(picArea([s.key]));
  const below = document.createElement("div");
  below.className = "below";
  const line = document.createElement("div");
  line.className = "wordline";
  line.textContent = WORDS[s.key][0];
  below.appendChild(line);
  const said = document.createElement("button");
  said.className = "btn big";
  said.textContent = "🗣 Я сказал!";
  said.onclick = () => { stopSound(); next(); };
  below.appendChild(said);
  content.appendChild(below);
  // сначала реплика Искорки, потом само слово дважды: обычно и медленнее
  setTimeout(async () => {
    await play(WORDS[s.key][1], WORDS[s.key][0], "en-US");
    await play(WORDS[s.key][1] + "-slow", WORDS[s.key][0], "en-US");
  }, 3200);
};

RENDER.pick = function(s){
  const r = s.rounds[round];
  if (r.who) content.appendChild(picArea([r.who], "who"));
  const cards = document.createElement("div");
  cards.className = "picarea cards";
  cards.style.setProperty("--n", 2);
  shuffle([r.target, r.other]).forEach(key => {
    const c = document.createElement("button");
    c.className = "card";
    c.innerHTML = '<img src="' + IMG[key] + '" alt="">';
    c.onclick = () => answer(c, key === r.target, s, r);
    cards.appendChild(c);
  });
  content.appendChild(cards);
  if (joined.length){
    const row = document.createElement("div");
    row.className = "joined";
    joined.forEach(k => {
      const im = document.createElement("img");
      im.src = IMG[k];
      row.appendChild(im);
    });
    content.appendChild(row);
  }
  // слово называется после реплики, а на повторных раундах — сразу
  const word = WORDS[r.target];
  setTimeout(() => {
    play(word[1], word[0], "en-US");
  }, round === 0 ? 2600 : 400);
};

async function answer(card, ok, s, r){
  if (card.dataset.locked) return;
  if (!ok){
    card.classList.add("wrong");
    setTimeout(() => card.classList.remove("wrong"), 500);
    await retry();
    return;
  }
  content.querySelectorAll(".card").forEach(c => c.dataset.locked = "1");
  card.classList.add("right");
  if (r.join && joined.indexOf(r.join) < 0){ joined.push(r.join); drawTokens(); }
  await praise();
  round++;
  if (round >= s.rounds.length){ round = 0; next(); }
  else { render(); }
}

RENDER.pairs = function(s){
  const keys = s.keys.concat(s.keys);
  const grid = document.createElement("div");
  grid.className = "grid";
  let picked = null, left = s.keys.length;
  shuffle(keys).forEach(key => {
    const c = document.createElement("button");
    c.className = "card";
    c.dataset.key = key;
    c.innerHTML = '<img src="' + IMG[key] + '" alt="">';
    c.onclick = async () => {
      if (c.classList.contains("gone") || c === picked) return;
      if (!picked){
        picked = c;
        c.classList.add("picked");
        const w = WORDS[key];
        if (w) play(w[1], w[0], "en-US");
        return;
      }
      if (picked.dataset.key === key){
        picked.classList.add("gone");
        c.classList.add("gone");
        picked = null;
        left--;
        await praise();
        if (left === 0) next();
      } else {
        c.classList.add("wrong");
        setTimeout(() => c.classList.remove("wrong"), 500);
        picked.classList.remove("picked");
        picked = null;
        await retry();
      }
    };
    grid.appendChild(c);
  });
  content.appendChild(grid);
};

RENDER.parent = function(s){
  const row = document.createElement("div");
  row.className = "picarea cards";
  row.style.setProperty("--n", s.keys.length);
  s.keys.forEach(k => {
    const wrap = document.createElement("button");
    wrap.className = "card";
    wrap.innerHTML = '<img src="' + IMG[k] + '" alt="">';
    wrap.onclick = () => { const w = WORDS[k]; if (w) play(w[1], w[0], "en-US"); };
    row.appendChild(wrap);
  });
  content.appendChild(row);
  setTimeout(() => { btnNext.hidden = false; }, 2000);
  btnNext.textContent = "Готово ✔";
};

function next(){
  stopSound();
  round = 0;
  if (S >= lesson().screens.length - 1){ finish(); return; }
  S++;
  render();
}
function prev(){
  stopSound();
  round = 0;
  if (S > 0){ S--; render(); }
}

function finish(){
  const p = progress();
  if (p.done.indexOf(lesson().id) < 0) p.done.push(lesson().id);
  saveProgress(p);
  const last = L === LESSONS.length - 1;
  const panel = overlay.querySelector(".panel");
  panel.innerHTML =
    "<h2>Урок пройден!</h2>" +
    "<p>" + (last
      ? "Ты прошёл всю дорогу до праздника. А кто же в яйце — узнаешь на первом уроке с преподавателем."
      : "Дорожка на следующий остров готова.") + "</p>" +
    '<div class="row">' +
      '<button class="btn ghost" data-act="again">Пройти ещё раз</button>' +
      '<button class="btn" data-act="map">Вернуться на карту 🗺️</button>' +
    "</div>";
  panel.querySelector('[data-act="again"]').onclick = () => {
    overlay.classList.remove("on");
    startLesson(L);
  };
  panel.querySelector('[data-act="map"]').onclick = showMap;
  overlay.classList.add("on");
  play(null, last ? "Ты прошёл всю дорогу! Молодец!" : "Урок пройден! Молодец!", "ru-RU");
}

btnNext.onclick = next;
btnListen.onclick = () => { say(); };
lessonEl.querySelector(".home").onclick = showMap;

/* ─────────── панель просмотра, только по ?dev=1 ─────────── */
if (/[?&]dev=1/.test(location.search)){
  const dev = document.getElementById("wsdev");
  dev.classList.add("on");
  dev.onclick = e => {
    const act = e.target.dataset.act;
    if (act === "next") next();
    if (act === "prev") prev();
    if (act === "reset"){
      try { localStorage.removeItem(STORE); } catch(e){}
      showMap();
    }
  };
}

showMap();
</script>
</body>
</html>
"""


def main():
    images = {}
    for name, (rel, width, transparent) in PICTURES.items():
        path = ROOT / rel
        if not path.exists():
            sys.exit(f"нет картинки: {rel}")
        images[name] = prepare(path, width, transparent)
        print(f"  {name:14s} {len(images[name]) // 1024:5d} КБ")

    audio = collect_audio()
    print(f"  дорожек озвучки: {len(audio)}")

    # каждая картинка, на которую ссылается спецификация, должна существовать
    spec = json.dumps(LESSONS, ensure_ascii=False)
    for key in re.findall(r'"(?:pic|who|target|other|join|reward|path|island)":\s*"([a-z_]+)"', spec):
        if key not in images and key != "friend":
            sys.exit(f"в уроках есть ссылка на картинку «{key}», а её нет")
    for les in LESSONS:
        for s in les["screens"]:
            for k in s.get("keys", []) + s.get("pics", []):
                if k not in images:
                    sys.exit(f"в уроках есть ссылка на картинку «{k}», а её нет")
            if s["t"] == "word" and s["key"] not in WORDS:
                sys.exit(f"слово «{s['key']}» не описано в WORDS")

    page = HTML
    page = page.replace("__IMG__", json.dumps(images))
    page = page.replace("__AUDIO__", json.dumps(audio))
    page = page.replace("__LESSONS__", json.dumps(LESSONS, ensure_ascii=False))
    page = page.replace("__PRAISE__", json.dumps(PRAISE, ensure_ascii=False))
    page = page.replace("__RETRY__", json.dumps(RETRY, ensure_ascii=False))
    page = page.replace("__WORDS__", json.dumps(WORDS, ensure_ascii=False))

    # литерал закрывающего тега внутри скрипта оборвал бы страницу
    if page.count("</script>") != 1:
        sys.exit("в собранной странице лишний закрывающий тег скрипта")

    OUT.write_text(page, encoding="utf-8")
    print(f"\n{OUT.name}: {len(page.encode()) / 1024 / 1024:.2f} МБ")


if __name__ == "__main__":
    main()
