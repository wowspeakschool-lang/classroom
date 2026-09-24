#!/usr/bin/env python3
"""Собирает лид-магнит 4–6 «Дорога на праздник» одним файлом.

    python3 tools/build_kids46.py

На выходе два файла:
  wowspeak-4-6.html              карта и три урока, картинки внутри
  docs/WowSpeak_озвучка_4-6.md   что озвучивать — собирается из тех же реплик

Уроки здесь не правятся руками: вся структура лежит в LESSONS ниже. Реплики
пишутся текстом прямо в спецификации, номера дорожек (RU-01, RU-02, …)
скрипт раздаёт сам по порядку — поэтому файл озвучки не может разойтись
с тем, что реально звучит в уроке.

Звук: если в `assets/audio-4-6/` лежат `RU-01.mp3`, `EN-01.mp3` и прочие,
они вшиваются в файл. Русский синтез браузера не используем — звучит плохо;
без записи реплика молчит, текст для взрослого остаётся в пузыре.
"""

import base64
import io
import json
import math
import re
import struct
import sys
from pathlib import Path

from PIL import Image

# 🟥 Перед публикацией поставить False и пересобрать: пока панель включена,
# ребёнок пролистает урок мимо заданий.
DEV_PANEL = True

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "wowspeak-4-6.html"
VOICE_DOC = ROOT / "docs" / "WowSpeak_озвучка_4-6.md"
AUDIO_DIR = ROOT / "assets" / "audio-4-6"


# ──────────────────────────────────────────────────────────── картинки ──

def cut_white(im, bright=250, neutral=3, holes=True):
    """Убирает фон генератора: светлый И бесцветный.

    Одной яркости мало. Фон у генератора строго серый (max−min = 0), а белые
    места самой картинки тонированные — у облака розоватые и желтоватые.
    Заливка «по яркости» уходила прямо внутрь облака и выедала его: у
    облачка исчезало 19% картинки, у облачного острова 9.5%, у камушка блик.
    Второе условие — «бесцветный» — эту дорогу закрывает: цепочка серых
    пикселей внутри облака рвётся на первом же розовом.

    `holes` добивает замкнутые бесцветные области: под радугой оставался
    белый кусок, до которого заливка от краёв не дотягивалась. С проверкой
    на бесцветность этот проход безопасен — тонированное он не трогает.
    """
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()

    def is_bg(x, y):
        r, g, b, a = px[x, y]
        return a > 0 and min(r, g, b) >= bright and max(r, g, b) - min(r, g, b) <= neutral

    seen = bytearray(w * h)

    def flood(seeds, collect=None):
        stack = list(seeds)
        while stack:
            x, y = stack.pop()
            if x < 0 or y < 0 or x >= w or y >= h or seen[y * w + x] or not is_bg(x, y):
                continue
            seen[y * w + x] = 1
            if collect is None:
                r, g, b, a = px[x, y]
                px[x, y] = (r, g, b, 0)
            else:
                collect.append((x, y))
            stack.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))

    flood([(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)])

    if holes:
        floor = int(w * h * 0.0008)
        for sy in range(0, h, 4):
            for sx in range(0, w, 4):
                if seen[sy * w + sx] or not is_bg(sx, sy):
                    continue
                blob = []
                flood([(sx, sy)], blob)
                if len(blob) >= floor:
                    for x, y in blob:
                        r, g, b, a = px[x, y]
                        px[x, y] = (r, g, b, 0)
    return im


def prepare(path, width, transparent=True, quality=80):
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
#
# Ширина — не «сколько хватит на глаз», а вдвое больше самого крупного места,
# где картинка показывается: на телефоне пиксель экрана вдвое мельче пикселя
# картинки, и вшитая впритык выглядит мыльной. Проверка сравнивает
# натуральный размер с показанным и ругается на растяжение.
PICTURES = {
    "map_bg":        ("assets/kids-4-6/map-background-wide.webp", 1536, False),
    "meadow":        ("assets/kids-4-6/island-meadow.webp",        900, True),
    "clouds":        ("assets/kids-4-6/island-clouds.webp",        900, True),
    "dragon":        ("assets/kids-4-6/island-dragon.webp",        900, True),
    "firefly":       ("assets/kids-4-6/firefly-neutral.webp",      900, True),
    "firefly_smile": ("assets/kids-4-6/firefly-smile.webp",        900, True),
    "firefly_wow":   ("assets/kids-4-6/firefly-excited.webp",      900, True),
    "firefly_lamp":  ("assets/kids-4-6/firefly-lantern.webp",      900, False),
    "stone":         ("assets/kids-4-6/stone.webp",                900, True),
    "cloudlet":      ("assets/kids-4-6/cloudlet.webp",             900, True),
    "egg":           ("assets/kids-4-6/egg.webp",                 1100, True),
    "cave_closed":   ("assets/kids-4-6/cave-closed.webp",         1100, True),
    "cave_open":     ("assets/kids-4-6/cave-open.webp",           1100, True),
    "bunny":         ("assets/kids-4-6/animal-bunny.webp",         760, True),
    "hedgehog":      ("assets/kids-4-6/animal-hedgehog.webp",      760, True),
    "fox":           ("assets/kids-4-6/animal-fox.webp",           760, True),
    "push":          ("assets/kids-4-6/friends-push.webp",        1400, True),
    "cap":           ("assets/lesson-1/cap.webp",                  1100, True),
    "top":           ("assets/lesson-1/tshirt.webp",               1100, True),
    "jeans":         ("assets/lesson-1/jeans.webp",                1100, True),
    "shoes":         ("assets/lesson-1/shoes.webp",                1100, True),
    "skirt":         ("assets/lesson-1/skirt.webp",                1100, True),
    "jacket":        ("assets/lesson-1/jacket.webp",               1100, True),
    "socks":         ("assets/lesson-1/socks.webp",                1100, True),
    "backpack":      ("assets/lesson-1/backpack.webp",             1100, True),
}

# слово → (как звучит, номер английской дорожки)
WORDS = {
    "cap":   ("a cap", "EN-01"),
    "top":   ("a top", "EN-02"),
    "jeans": ("jeans", "EN-03"),
    "shoes": ("shoes", "EN-04"),
    "skirt": ("a skirt", "EN-05"),
}

# фраза третьего острова
PHRASES = {
    "cap":   ("I have a cap", "EN-06"),
    "top":   ("I have a top", "EN-07"),
    "jeans": ("I have jeans", "EN-08"),
    "shoes": ("I have shoes", "EN-09"),
    "skirt": ("I have a skirt", "EN-10"),
}

VOICES = {
    "firefly":  "Искорка",
    "bunny":    "Зайчик",
    "hedgehog": "Ёжик",
    "fox":      "Лисёнок",
}

FRIENDS = ["bunny", "hedgehog", "fox"]


# ─────────────────────────────────────────────────────────────── уроки ──
#
# Типы экранов:
#   story   картинка и реплика, кнопка «дальше» появляется сама
#   word    слово крупно: слушаем, повторяем вслух, жмём «я сказал»
#   phrase  то же, но фразой «I have …»
#   name    назови сам: показываем вещь, ребёнок говорит, потом слышит эталон
#   pick    два варианта, показать названное
#   pick4   четыре варианта — то же, но труднее
#   pairs   найди пару
#   parent  экран для взрослого: назвать вслух всё выученное
#
# `token: True` — после задания ребёнок получает камушек (облачко, друга),
# и сразу показывается карта, где камушек ложится в воду. Экран награды
# скрипт вставляет сам, тексты берёт из token_lines.

LESSONS = [
    {
        "id": 1,
        "title": "Солнечная Полянка",
        "island": "meadow",
        "token": "stone",
        "token_lines": [
            ("Молодец! За помощь зверята дали тебе волшебный камушек. Смотри — "
             "он лёг в воду.", "радостно, с благодарностью"),
            ("И ещё камушек! Дорожка растёт.", "весело"),
            ("Третий! Уже половина пути.", "подбадривающе"),
            ("Четвёртый камушек. Смотри, как блестит.", "любуемся"),
            ("Пятый! Ещё чуть-чуть.", "нетерпеливо, весело"),
            ("Последний камушек! Дорожка до Облачного Острова готова. Идём!",
             "торжественно, зовём за собой"),
        ],
        "screens": [
            {"t": "story", "solo": True, "btn": "Полетели!",
             "text": "Привет! Я светлячок Искорка. Смотри, что мне принесли — "
                     "приглашение! Нас зовут на праздник на Драконий Остров. Полетели!",
             "tone": "знакомство, радостно, с приглашением"},
            {"t": "story", "pic": "meadow",
             "text": "Мы на Солнечной Полянке! Тут живут зверята. Ой, ветер "
                     "разбросал все их вещи. Давай поможем собрать.",
             "tone": "сначала восхищённо, на «ой» — сочувственно"},

            {"t": "word", "key": "cap",
             "text": "Смотри, это кепка. По-английски — a cap. Скажи вслух: a cap.",
             "tone": "показываем, «a cap» отчётливо и чуть медленнее"},
            {"t": "pick", "token": True,
             "text": "Найди кепку. Где тут a cap?", "tone": "вопрос, с интересом",
             "rounds": [
                 {"target": "cap", "other": "jacket"},
                 {"target": "cap", "other": "socks"},
                 {"target": "cap", "other": "backpack"},
             ]},

            {"t": "word", "key": "top",
             "text": "А это кофточка. По-английски — a top. Скажи вслух: a top.",
             "tone": "показываем"},
            {"t": "pick", "token": True,
             "text": "Слушай внимательно и показывай.", "tone": "мягко, без нажима",
             "rounds": [
                 {"target": "top", "other": "cap"},
                 {"target": "cap", "other": "top"},
                 {"target": "top", "other": "socks"},
                 {"target": "cap", "other": "jacket"},
             ]},

            {"t": "name", "token": True, "keys": ["cap", "top"],
             "text": "А теперь ты назови сам. Что это по-английски?",
             "tone": "с интересом, ждём ответа"},

            {"t": "pick4", "token": True,
             "text": "Теперь вещей много. Найди ту, которую я назову.",
             "tone": "подзадориваем",
             "rounds": [
                 {"target": "cap", "others": ["jacket", "socks", "jeans"]},
                 {"target": "top", "others": ["shoes", "backpack", "skirt"]},
                 {"target": "cap", "others": ["top", "shoes", "socks"]},
             ]},

            {"t": "pairs", "token": True, "keys": ["cap", "top", "socks", "backpack"],
             "text": "Помоги разложить вещи по парам. Нажимай на две одинаковые.",
             "tone": "деловито, спокойно"},

            {"t": "pick", "token": True,
             "text": "Зверята ждут свои вещи. Дай каждому то, что он просит.",
             "tone": "тепло",
             "rounds": [
                 {"who": "bunny", "target": "cap", "other": "top",
                  "line": ("bunny", "Ой, где же моя a cap?", "растерянно, жалобно")},
                 {"who": "hedgehog", "target": "top", "other": "cap",
                  "line": ("hedgehog", "А я ищу свой a top!", "деловито")},
                 {"who": "fox", "target": "cap", "other": "socks",
                  "line": ("fox", "И мне нужна a cap!", "быстро, нетерпеливо")},
             ]},

            {"t": "parent", "keys": ["cap", "top"],
             "text": "А теперь позови маму или папу и назови всё, что ты сегодня выучил.",
             "tone": "доверительно, чуть тише"},
        ],
    },

    {
        "id": 2,
        "title": "Облачный Остров",
        "island": "clouds",
        "token": "cloudlet",
        "token_lines": [
            ("Молодец! Вот тебе облачко. Оно село прямо над пропастью.",
             "радостно"),
            ("Ещё облачко! Мостик начинается.", "весело"),
            ("Третье. Уже можно шагнуть.", "подбадривающе"),
            ("Четвёртое, мягкое, как подушка.", "нежно"),
            ("Пятое! Почти готово.", "нетерпеливо"),
            ("Последнее! Мостик до Драконьего Острова готов. Прыгаем!",
             "торжественно, зовём за собой"),
        ],
        "screens": [
            {"t": "story", "pic": "clouds",
             "text": "Мы на Облачном Острове! Тут всё мягкое, как подушки.",
             "tone": "восхищённо"},
            {"t": "story", "pic": "clouds",
             "text": "Ой… впереди пропасть, а мостика нет. Надо что-то придумать.",
             "tone": "озадаченно, но не испуганно"},

            {"t": "word", "key": "jeans",
             "text": "Смотри, это джинсы. По-английски — jeans. Скажи вслух: jeans.",
             "tone": "показываем"},
            {"t": "pick", "token": True,
             "text": "Где тут jeans? Покажи.", "tone": "вопрос",
             "rounds": [
                 {"target": "jeans", "other": "cap"},
                 {"target": "jeans", "other": "top"},
                 {"target": "jeans", "other": "backpack"},
             ]},

            {"t": "word", "key": "shoes",
             "text": "А это ботинки. По-английски — shoes. Скажи вслух: shoes.",
             "tone": "показываем"},
            {"t": "pick", "token": True,
             "text": "Слушай и показывай.", "tone": "мягко",
             "rounds": [
                 {"target": "shoes", "other": "jeans"},
                 {"target": "jeans", "other": "shoes"},
                 {"target": "shoes", "other": "cap"},
             ]},

            {"t": "word", "key": "skirt",
             "text": "А это юбка. По-английски — a skirt. Скажи вслух: a skirt.",
             "tone": "показываем"},
            {"t": "pick", "token": True,
             "text": "А теперь найди юбку.", "tone": "вопрос",
             "rounds": [
                 {"target": "skirt", "other": "jeans"},
                 {"target": "skirt", "other": "shoes"},
                 {"target": "jeans", "other": "skirt"},
             ]},

            {"t": "name", "token": True, "keys": ["jeans", "shoes", "skirt"],
             "text": "Теперь ты назови сам. Что это по-английски?",
             "tone": "с интересом, ждём ответа"},

            {"t": "pick4", "token": True,
             "text": "Вещей стало много! Найди ту, которую я назову.",
             "tone": "подзадориваем",
             "rounds": [
                 {"target": "shoes", "others": ["jeans", "cap", "top"]},
                 {"target": "skirt", "others": ["shoes", "top", "jacket"]},
                 {"target": "jeans", "others": ["skirt", "socks", "cap"]},
             ]},

            {"t": "pick", "token": True,
             "text": "Зверята тоже собираются на праздник. Помоги им одеться!",
             "tone": "весело",
             "rounds": [
                 {"who": "fox", "target": "jeans", "other": "top",
                  "line": ("fox", "Где мои jeans? Без них на праздник не пойду!",
                           "возмущённо-весело")},
                 {"who": "bunny", "target": "shoes", "other": "cap",
                  "line": ("bunny", "А мне нужны shoes!", "мягко просит")},
                 {"who": "hedgehog", "target": "skirt", "other": "jeans",
                  "line": ("hedgehog", "И я хочу a skirt!", "ворчливо")},
             ]},

            {"t": "parent", "keys": ["cap", "top", "jeans", "shoes", "skirt"],
             "text": "Позови маму или папу и назови всё, что ты выучил сегодня.",
             "tone": "доверительно"},
        ],
    },

    {
        "id": 3,
        "title": "Драконий Остров",
        "island": "dragon",
        "token": "friend",
        "token_lines": [
            ("Слышишь? Это зайчик! Он услышал тебя и прибежал помогать.",
             "обрадованно, с удивлением"),
            ("А вот и ёжик! Он тоже с нами.", "весело"),
            ("И лисёнок прибежал! Теперь мы все вместе.", "торжествующе"),
        ],
        "screens": [
            {"t": "story", "pic": "dragon",
             "text": "Мы на Драконьем Острове! Вот и праздник: флажки, фонарики… "
                     "А где же все? Никого нет. Как странно.",
             "tone": "радость, потом недоумение"},
            {"t": "story", "solo": True,
             "text": "А давай научимся рассказывать о себе! Это пригодится на "
                     "празднике — там надо со всеми знакомиться.",
             "tone": "заговорщицки, с идеей"},

            {"t": "phrase", "key": "cap",
             "text": "Смотри: у меня есть кепка. По-английски — I have a cap. "
                     "Скажи вслух: I have a cap.",
             "tone": "показываем, фразу отчётливо и чуть медленнее"},
            {"t": "pick", "say": "phrase", "token": True,
             "text": "Слушай и показывай, о чём я говорю.", "tone": "спокойно",
             "rounds": [
                 {"target": "cap", "other": "jeans"},
                 {"target": "top", "other": "shoes"},
                 {"target": "shoes", "other": "cap"},
             ]},

            {"t": "phrase", "key": "skirt",
             "text": "А так: I have a skirt. Скажи вслух: I have a skirt.",
             "tone": "показываем"},
            {"t": "pick4", "say": "phrase", "token": True,
             "text": "Теперь труднее. Слушай внимательно!", "tone": "подзадориваем",
             "rounds": [
                 {"target": "skirt", "others": ["jeans", "cap", "top"]},
                 {"target": "jeans", "others": ["shoes", "skirt", "cap"]},
                 {"target": "top", "others": ["cap", "jeans", "shoes"]},
             ]},

            {"t": "name", "say": "phrase", "token": True,
             "keys": ["cap", "jeans", "shoes"],
             "text": "А теперь ты расскажи! Что у тебя есть?",
             "tone": "с интересом, ждём ответа"},

            {"t": "story", "pic": "dragon",
             "text": "Ой, смотри! Кто-то тут был. Следы ведут вон туда, к камням.",
             "tone": "шёпотом, загадочно"},
            {"t": "pairs", "keys": ["cap", "top", "jeans", "shoes"],
             "text": "По дороге разберём вещи. Нажимай на две одинаковые.",
             "tone": "деловито"},
            {"t": "story", "pic": "cave_closed",
             "text": "Следы привели нас к пещере. А вход завален большим камнем. "
                     "Одному не сдвинуть… Хорошо, что с нами друзья!",
             "tone": "интрига, потом с усилием и решительно"},
            {"t": "story", "pic": "push", "btn": "Помочь!",
             "text": "Раз, два, взяли! Толкаем все вместе!",
             "tone": "с натугой, весело"},
            {"t": "story", "pic": "cave_open",
             "text": "Получилось! Как темно… Подожди, я посвечу. Смотри — гнёздышко!",
             "tone": "радость, потом тише, в темноте"},
            {"t": "story", "pic": "egg",
             "text": "А в нём яйцо! Интересно, кто же там внутри? Неужели дракончик? "
                     "Узнаем на первом уроке!",
             "tone": "изумление, тайна, предвкушение"},

            {"t": "parent", "say": "phrase",
             "keys": ["cap", "top", "jeans", "shoes", "skirt"],
             "text": "Позови маму или папу и расскажи, что у тебя есть. По-английски!",
             "tone": "доверительно"},
        ],
    },
]

PRAISE = [
    ("Молодец!", "живо"),
    ("Правильно!", "радостно"),
    ("Верно! Умница!", "тепло"),
    ("Получилось!", "с восторгом"),
    ("Ух ты, как здорово!", "восхищённо"),
]
RETRY = [
    ("Ой, не то. Попробуй ещё разок.", "спокойно, без тени упрёка"),
    ("Почти! Давай ещё раз.", "подбадривающе"),
]


# ────────────────────────────────── номера дорожек и экраны наград ──

def build_script():
    """Раздаёт номера RU-NN по порядку и вставляет экраны наград.

    Файл озвучки собирается из этого же списка, поэтому разойтись с уроком
    он не может: номер живёт в одном месте.
    """
    script = []          # (ключ, кто говорит, текст, интонация, где звучит)
    counter = [0]

    def key(voice, text, tone, where):
        counter[0] += 1
        k = "RU-%02d" % counter[0]
        script.append((k, voice, text, tone, where))
        return k

    for les in LESSONS:
        where = "Урок %d. %s" % (les["id"], les["title"])
        out, earned = [], 0
        for s in les["screens"]:
            s["ru"] = key("firefly", s["text"], s.get("tone", ""), where)
            for r in s.get("rounds", []):
                if "line" in r:
                    voice, text, tone = r["line"]
                    r["line"] = key(voice, text, tone, where)
            out.append(s)
            if s.pop("token", False):
                text, tone = les["token_lines"][earned]
                earned += 1
                out.append({
                    "t": "token", "n": earned,
                    "kind": "friends" if les["token"] == "friend" else "map",
                    "text": text, "ru": key("firefly", text, tone, where),
                })
        les["screens"] = out
        les["tokens"] = earned
        if earned != len(les["token_lines"]):
            sys.exit("в уроке %d %d наград, а реплик к ним %d"
                     % (les["id"], earned, len(les["token_lines"])))

    where = "Похвалы — звучат во всех трёх уроках"
    praise_keys = [key("firefly", t, tone, where) for t, tone in PRAISE]
    retry_keys = [key("firefly", t, tone, where) for t, tone in RETRY]
    return script, praise_keys, retry_keys


def write_voice_doc(script):
    rows = {}
    for k, voice, text, tone, where in script:
        rows.setdefault(where, []).append((k, voice, text, tone))

    counts = {}
    for _, voice, _, _, _ in script:
        counts[voice] = counts.get(voice, 0) + 1

    doc = ["""# Озвучка лид-магнита 4–6 «Дорога на праздник»

> Файл собирается скриптом `tools/build_kids46.py` вместе с самим уроком.
> Руками не правим: номера дорожек здесь и в уроке всегда одни и те же.

Ребёнок ещё не читает, поэтому **всё держится на голосе**. Текст на экране —
только для взрослого рядом.
"""]

    doc.append("## Кого озвучиваем\n")
    doc.append("| Кто | Каким голосом | Реплик | Характер |")
    doc.append("|---|---|---|---|")
    doc.append("| **Искорка**, светлячок-проводник | детский, звонкий, тёплый | "
               "%d | Ведёт всё приключение. Радуется, удивляется, зовёт за собой. |"
               % counts.get("firefly", 0))
    for v, desc in (("bunny", "детский, мягкий, чуть робкий|Потерял свои вещи, просит помочь."),
                    ("hedgehog", "детский, пониже, забавный|Деловитый, немного ворчливый."),
                    ("fox", "детский, быстрый, озорной|Торопится на праздник.")):
        voice_desc, character = desc.split("|")
        doc.append("| **%s** | %s | %d | %s |"
                   % (VOICES[v], voice_desc, counts.get(v, 0), character))
    doc.append("""
Если четыре разных голоса получить не выйдет — **обязательно** отдельный
голос у Искорки и хотя бы один общий «звериный», отличный от неё. Один голос
на всё приключение четырёхлетку усыпит.
""")

    doc.append("""## Как записывать

**Тон:** тёплый, небыстрый, как будто рассказываете сказку четырёхлетке.
Короткие фразы, паузы между предложениями. Не «диктор новостей».

**Интонации важнее дикции.** Там, где в тексте «Ой…» — настоящее удивление,
где «Смотри!» — радость. Ровно прочитанная строчка убивает сцену.

**Английские слова внутри русских реплик** (`a cap`, `jeans`) произносятся
по-английски, но той же интонацией — это часть фразы, а не вставка из
словаря. Если сервис читает их по-русски («а сар»), разбейте реплику на две
дорожки или возьмите многоязычный голос.

**Файлы.** Каждая реплика — отдельный файл, имя ровно как в таблице:
`RU-01.mp3`, `RU-02.mp3`, …, `EN-01.mp3`. Положить в `assets/audio-4-6/`.
Сборка подхватит их сама. Если сервис отдаёт одним файлом — пришлите как
есть, с паузами в 2 секунды между репликами, нарежу.
""")

    for where, items in rows.items():
        doc.append("## %s\n" % where)
        doc.append("| Файл | Кто | Текст | Интонация |")
        doc.append("|---|---|---|---|")
        for k, voice, text, tone in items:
            doc.append("| %s | %s | %s | %s |" % (k, VOICES[voice], text, tone))
        doc.append("")

    doc.append("""## Английские слова и фразы

Отдельным голосом: **носитель языка, взрослый, спокойный и чёткий**. Не
детский — здесь нужен эталон произношения, а не характер.
""")
    doc.append("| Файл | Текст |")
    doc.append("|---|---|")
    for key, (text, code) in list(WORDS.items()) + list(PHRASES.items()):
        doc.append("| %s | %s |" % (code, text))
    doc.append("""
Слова (EN-01…EN-05) нужны **дважды**: обычно и чуть медленнее. Второй
вариант — с суффиксом в имени: `EN-01.mp3` и `EN-01-slow.mp3`. Фразам
(EN-06…EN-10) медленный вариант не нужен.
""")

    doc.append("""## Где это сделать бесплатно

Проверьте голос **на одной реплике** — возьмите самую длинную, где больше
всего смен интонации. Если сервис прочтёт её ровно, он прочтёт ровно и всё
остальное.

**[ElevenLabs](https://elevenlabs.io)** — лучшее качество русского и
единственный, где интонации звучат живыми. В библиотеке есть детские голоса;
многоязычная модель правильно читает английские слова внутри русской фразы.
Бесплатно около 10 000 символов в месяц — на весь наш текст хватает с
запасом. **Рекомендую начать с него.**

**[TTSMaker](https://ttsmaker.com/ru)** — бесплатно и без регистрации,
русские голоса есть, скачивает mp3 сразу. Интонации беднее, детских голосов
почти нет. Запасной вариант или для похвал.

**Яндекс SpeechKit** — родной русский с правильными ударениями, бесплатный
лимит через облако. Минус: нужен аккаунт в Яндекс.Облаке.

Обзор сервисов с актуальными лимитами:
[подборка на DTF](https://dtf.ru/howto/5127825-besplatnaya-ii-ozvuchka-teksta-na-russkom).

**Свой голос — тоже вариант, и часто лучший.** Живая интонация мамы бьёт
любой синтез, а записать эти фразы на телефон — минут двадцать.

## Пока озвучки нет

Русские реплики **молчат** — текст виден в пузыре, и взрослый читает его
вслух. Английские слова проговаривает синтез браузера. На верный и неверный
ответ звучат короткие сигналы, чтобы ребёнок получал отклик на нажатие.
""")
    VOICE_DOC.write_text("\n".join(doc), encoding="utf-8")


# ──────────────────────────────────────────────────────────────── звук ──

def tone_wav(notes, volume=0.22, rate=22050):
    """Короткий звук отклика: без русской озвучки ребёнку нужен хоть какой-то
    ответ на нажатие. Собираем WAV сами, чтобы ничего не скачивать."""
    frames = bytearray()
    for freq, dur in notes:
        n = int(rate * dur)
        for i in range(n):
            # мягкое нарастание и затухание, иначе на краях слышен щелчок
            env = min(1.0, i / (rate * 0.01), (n - i) / (rate * 0.05))
            v = int(32767 * volume * env * math.sin(2 * math.pi * freq * i / rate))
            frames += struct.pack("<h", v)
    header = b"RIFF" + struct.pack("<I", 36 + len(frames)) + b"WAVEfmt " + \
        struct.pack("<IHHIIHH", 16, 1, 1, rate, rate * 2, 2, 16) + \
        b"data" + struct.pack("<I", len(frames))
    return "data:audio/wav;base64," + base64.b64encode(header + bytes(frames)).decode()


def collect_audio():
    out = {}
    if AUDIO_DIR.is_dir():
        for f in sorted(AUDIO_DIR.iterdir()):
            ext = f.suffix.lower().lstrip(".")
            if ext not in ("mp3", "m4a", "ogg", "wav"):
                continue
            mime = {"mp3": "audio/mpeg", "m4a": "audio/mp4",
                    "ogg": "audio/ogg", "wav": "audio/wav"}[ext]
            out[f.stem.upper()] = ("data:%s;base64," % mime +
                                   base64.b64encode(f.read_bytes()).decode())
    out.setdefault("SFX-OK", tone_wav([(880, 0.10), (1318, 0.16)]))
    out.setdefault("SFX-NO", tone_wav([(330, 0.18)], volume=0.16))
    return out


HTML = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Волшебная страна — дорога на праздник</title>
<style>
:root{
  --sky:#bfe9ff; --card:#fffdf7; --ink:#3a2f4a;
  --accent:#ff9d3c; --good:#5ec26a; --bad:#ff8a8a;
  --shadow:0 10px 24px rgba(60,40,90,.18);
}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;height:100%;overflow:hidden}
body{
  font-family:"Nunito","Comic Sans MS",system-ui,-apple-system,"Segoe UI",sans-serif;
  color:var(--ink); background:var(--sky); user-select:none; -webkit-user-select:none;
}
img{-webkit-user-drag:none}
#app{position:fixed;inset:0}

/* ───────── карта ───────── */
#map{position:absolute;inset:0;display:none;background:#bfe9ff center/cover no-repeat}
#map.on{display:block}
.island{position:absolute;transform:translate(-50%,-50%);width:30%;max-width:420px;
  border:0;background:none;padding:0;cursor:pointer;transition:transform .2s}
.island img{width:100%;display:block;filter:drop-shadow(0 12px 18px rgba(40,60,90,.25))}
.island:active{transform:translate(-50%,-50%) scale(.96)}
.island .name{display:block;margin-top:-6px;font-size:clamp(13px,2.4vw,22px);font-weight:800;
  color:#fff;text-shadow:0 2px 6px rgba(40,60,90,.6)}
.island.locked img{filter:grayscale(.9) brightness(.82) contrast(.9)
  drop-shadow(0 12px 18px rgba(40,60,90,.25));opacity:.75}
.island.locked .name{opacity:.7}
.island.shake{animation:islandshake .4s}
@keyframes islandshake{25%{transform:translate(calc(-50% - 10px),-50%)}
                       75%{transform:translate(calc(-50% + 10px),-50%)}}
.island .tick{position:absolute;top:2%;right:8%;font-size:clamp(22px,4vw,40px)}
.island .lock{position:absolute;top:8%;left:50%;transform:translateX(-50%);
  font-size:clamp(20px,3.6vw,36px);filter:drop-shadow(0 2px 4px rgba(0,0,0,.35))}
/* камушки в воде — мелкие: это шаги по воде, а не валуны */
.dot{position:absolute;transform:translate(-50%,-50%);width:4%;max-width:54px;
  opacity:0;transition:opacity .4s}
.dot.on{opacity:1}
.dot.pop{animation:drop .6s both}
.dot img{width:100%;display:block;filter:drop-shadow(0 4px 6px rgba(40,60,90,.3))}
@keyframes drop{0%{transform:translate(-50%,-160%) scale(1.5);opacity:0}
                60%{transform:translate(-50%,-50%) scale(1.1);opacity:1}
                100%{transform:translate(-50%,-50%) scale(1);opacity:1}}
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
.topbar .tokens img{width:34px;height:34px;object-fit:contain}
.topbar .tokens .ghost{width:34px;height:34px;border-radius:50%;
  background:rgba(255,255,255,.45);border:2px dashed rgba(120,110,140,.35)}

.stage{flex:1 1 auto;display:flex;align-items:center;gap:2vw;padding:0 3vw 6px;
  min-height:0;overflow:hidden}
.guide{flex:0 0 22%;max-width:240px;display:flex;flex-direction:column;align-items:center}
.guide img{width:100%;max-width:190px;display:block}
.bubble{background:var(--card);border-radius:20px;padding:10px 14px;box-shadow:var(--shadow);
  font-size:clamp(13px,1.7vw,19px);line-height:1.35;text-align:center;margin-top:-6px}

/* Высота картинок считается от свободного места, а не в vh: иначе на низком
   экране содержимое наползает на кнопку и перехватывает нажатие. */
.content{flex:1 1 auto;display:flex;flex-direction:column;align-items:center;
  justify-content:center;gap:1vh;min-width:0;min-height:0;height:100%;overflow:hidden}
.picarea{flex:1 1 0;min-height:0;width:100%;display:flex;align-items:center;
  justify-content:center;gap:2vw}
.picarea img{height:100%;max-width:100%;object-fit:contain;
  filter:drop-shadow(0 8px 16px rgba(40,60,90,.2))}
.picarea.who{flex:0 1 38%;min-height:20%}
.picarea.items{gap:4vw}
.picarea.items img{height:auto;max-height:100%;width:auto;max-width:24%}
.below{flex:0 0 auto;display:flex;flex-direction:column;align-items:center;gap:1vh}
.wordline{font-size:clamp(22px,4vw,46px);font-weight:900;letter-spacing:.5px;text-align:center}

/* Экран, где говорит только светлячок: он занимает середину. Второй копии
   героя на экране быть не должно. */
.stage.solo{justify-content:center}
.stage.solo .guide{flex:0 0 auto;width:min(46%,420px);max-width:none}
.stage.solo .guide img{max-width:none;width:100%}
.stage.solo .bubble{font-size:clamp(15px,2.1vw,24px)}
.stage.solo .content{display:none}

/* Карта внутри урока: тот же фон и те же места островов. */
.mapview{flex:1 1 0;min-height:0;width:100%;position:relative;border-radius:24px;
  background-position:center;background-size:cover;box-shadow:var(--shadow);overflow:hidden}
.mapview>img{position:absolute;transform:translate(-50%,-50%);width:26%;
  filter:drop-shadow(0 8px 14px rgba(40,60,90,.25))}

/* Карточки — квадратные: сторона считается от реального размера ряда,
   который js кладёт в --bw/--bh. */
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
  <div id="map"></div>
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
const PHRASES = __PHRASES__;
const FRIENDS = __FRIENDS__;
const DEV_PANEL = __DEV__;
const STORE = "ws46_progress";
const ISLAND_POS = [[20, 60], [50, 38], [80, 62]];

/* ─────────────────────────── звук ─────────────────────────── */
let current = null;
function stopSound(){
  if (current){ try{ current.pause(); }catch(e){} current = null; }
  try{ speechSynthesis.cancel(); }catch(e){}
}
function play(key, text, lang){
  stopSound();
  return new Promise(resolve => {
    // Страховка по времени: без неё экран навсегда ждёт события, которое
    // может не прийти — синтез в вебвью и на телефоне молча не отвечает.
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
    // Русский синтез не используем: звучит плохо. Без записи реплика молчит,
    // текст для взрослого остаётся в пузыре. Английское ребёнку надо слышать.
    if (!text || lang !== "en-US" || !("speechSynthesis" in window)){ finish(); return; }
    try{
      const u = new SpeechSynthesisUtterance(text);
      u.lang = "en-US";
      u.rate = 0.8;
      u.onend = u.onerror = finish;
      speechSynthesis.speak(u);
    } catch(e){ finish(); }
  });
}
const choice = arr => arr[Math.floor(Math.random() * arr.length)];
function praise(){ return play(choice(PRAISE)); }
function retry(){ return play(choice(RETRY)); }
/* Короткий сигнал поверх всего: пока похвалы не записаны, ребёнку нужен
   отклик на нажатие. Отдельный объект, чтобы не гасить его вместе с репликой. */
function blip(key){
  try { const a = new Audio(AUDIO[key]); a.volume = 0.7; a.play().catch(() => {}); }
  catch(e){}
}
function shuffle(a){
  a = a.slice();
  for (let i = a.length - 1; i > 0; i--){
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
function saying(s, key){
  return s.say === "phrase" ? PHRASES[key] : WORDS[key];
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

/* Камушки ложатся по прямой между островами. Позиция считается от их
   числа, поэтому добавить задание — значит просто добавить камушек. */
function dotPos(i, k, total){
  const t = (k + 1) / (total + 1);
  return [ISLAND_POS[i][0] + (ISLAND_POS[i+1][0] - ISLAND_POS[i][0]) * t,
          ISLAND_POS[i][1] + (ISLAND_POS[i+1][1] - ISLAND_POS[i][1]) * t + 13];
}
function addDots(host, i, shown, popLast){
  const les = LESSONS[i];
  const total = les.tokens;
  for (let k = 0; k < total; k++){
    const d = document.createElement("div");
    const p = dotPos(i, k, total);
    d.className = "dot" + (k < shown ? " on" : "") +
                  (popLast && k === shown - 1 ? " pop" : "");
    d.style.left = p[0] + "%";
    d.style.top = p[1] + "%";
    d.innerHTML = '<img src="' + IMG[les.token] + '" alt="">';
    host.appendChild(d);
  }
}

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
      if (unlocked(les.id)){ startLesson(i); return; }
      // закрыто — качнём остров, чтобы было видно, что нажатие услышано
      b.classList.remove("shake");
      void b.offsetWidth;
      b.classList.add("shake");
      blip("SFX-NO");
    };
    mapEl.appendChild(b);
    if (i < LESSONS.length - 1) addDots(mapEl, i, isDone(les.id) ? les.tokens : 0, false);
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

let L = 0, S = 0, round = 0, earned = 0, token = 0;

function startLesson(i){
  L = i; S = 0; round = 0; earned = 0;
  mapEl.classList.remove("on");
  lessonEl.classList.add("on");
  render();
}
function lesson(){ return LESSONS[L]; }
function screen(){ return lesson().screens[S]; }

function drawTokens(){
  let html = "";
  for (let i = 0; i < lesson().tokens; i++){
    const key = lesson().token === "friend" ? FRIENDS[i] : lesson().token;
    html += i < earned ? '<img src="' + IMG[key] + '" alt="">' : '<div class="ghost"></div>';
  }
  tokensEl.innerHTML = html;
}

function render(){
  stopSound();
  token++;
  const s = screen();
  guideImg.src = IMG[s.solo ? "firefly_wow" : (s.t === "token" ? "firefly_wow" : "firefly")];
  bubble.textContent = s.text || "";
  content.innerHTML = "";
  btnNext.hidden = true;
  btnNext.textContent = s.btn || "Дальше ▶";
  lessonEl.querySelector(".stage").classList.toggle("solo", !!s.solo);
  if (s.t === "token") earned = s.n;
  drawTokens();
  RENDER[s.t](s);
  fit();
  say();
}

/* Реплики идут очередью, а не по таймеру: без записи русского звука пауза
   перед английским словом — пустая тишина. Маркер обрывает очередь, если
   экран уже сменился. */
async function queue(steps){
  const mine = token;
  for (const step of steps){
    if (mine !== token) return;
    await play(step[0], step[1], step[2]);
  }
}
function say(){
  const s = screen();
  const steps = [[s.ru]];
  if (s.t === "word"){
    steps.push([WORDS[s.key][1], WORDS[s.key][0], "en-US"],
               [WORDS[s.key][1] + "-slow", WORDS[s.key][0], "en-US"]);
  }
  if (s.t === "phrase"){
    steps.push([PHRASES[s.key][1], PHRASES[s.key][0], "en-US"]);
  }
  if (s.t === "pick" || s.t === "pick4"){
    const r = s.rounds[round];
    if (r.line) steps.push([r.line]);
    const w = saying(s, r.target);
    steps.push([w[1], w[0], "en-US"]);
  }
  return queue(steps);
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
function cardsArea(keys, onPick, n){
  const cards = document.createElement("div");
  cards.className = "picarea cards";
  cards.style.setProperty("--n", n || keys.length);
  keys.forEach(key => {
    const c = document.createElement("button");
    c.className = "card";
    c.innerHTML = '<img src="' + IMG[key] + '" alt="">';
    c.onclick = () => onPick(c, key);
    cards.appendChild(c);
  });
  return cards;
}

RENDER.story = function(s){
  if (s.solo){
    // светлячок уже стоит в середине и говорит
  } else {
    content.appendChild(picArea([s.pic]));
  }
  setTimeout(() => { btnNext.hidden = false; }, 2000);
};

RENDER.token = function(s){
  if (s.kind === "friends"){
    content.appendChild(picArea(FRIENDS.slice(0, s.n), "items"));
  } else {
    const view = document.createElement("div");
    view.className = "mapview";
    view.style.backgroundImage = "url(" + IMG.map_bg + ")";
    LESSONS.forEach((les, i) => {
      const im = document.createElement("img");
      im.src = IMG[les.island];
      im.style.left = ISLAND_POS[i][0] + "%";
      im.style.top = ISLAND_POS[i][1] + "%";
      view.appendChild(im);
    });
    addDots(view, L, s.n, true);
    content.appendChild(view);
  }
  setTimeout(() => { btnNext.hidden = false; }, 2200);
};

function speakScreen(s, key, line){
  content.appendChild(picArea([key]));
  const below = document.createElement("div");
  below.className = "below";
  const text = document.createElement("div");
  text.className = "wordline";
  text.textContent = line;
  below.appendChild(text);
  const said = document.createElement("button");
  said.className = "btn big";
  said.textContent = "🗣 Я сказал!";
  below.appendChild(said);
  content.appendChild(below);
  return said;
}

RENDER.word = function(s){
  speakScreen(s, s.key, WORDS[s.key][0]).onclick = () => { stopSound(); next(); };
};
RENDER.phrase = function(s){
  speakScreen(s, s.key, PHRASES[s.key][0]).onclick = () => { stopSound(); next(); };
};

/* Назови сам: слово на экране не пишем — ребёнок не читает. Сначала он
   говорит, потом слышит эталон и сравнивает. */
RENDER.name = function(s){
  const key = s.keys[round];
  content.appendChild(picArea([key]));
  const below = document.createElement("div");
  below.className = "below";
  const said = document.createElement("button");
  said.className = "btn big";
  said.textContent = "🗣 Я сказал!";
  said.onclick = async () => {
    said.disabled = true;
    const w = saying(s, key);
    const line = document.createElement("div");
    line.className = "wordline";
    line.textContent = w[0];
    below.insertBefore(line, said);
    blip("SFX-OK");
    await play(w[1], w[0], "en-US");
    await praise();
    round++;
    if (round >= s.keys.length){ round = 0; next(); } else { render(); }
  };
  below.appendChild(said);
  content.appendChild(below);
};

RENDER.pick = function(s){
  const r = s.rounds[round];
  if (r.who) content.appendChild(picArea([r.who], "who"));
  const opts = r.others ? [r.target].concat(r.others) : [r.target, r.other];
  content.appendChild(cardsArea(shuffle(opts),
    (c, key) => answer(c, key === r.target, s, r)));
};
RENDER.pick4 = RENDER.pick;

async function answer(card, ok, s, r){
  if (card.dataset.locked) return;
  if (!ok){
    card.classList.add("wrong");
    blip("SFX-NO");
    setTimeout(() => card.classList.remove("wrong"), 500);
    await retry();
    return;
  }
  content.querySelectorAll(".card").forEach(c => c.dataset.locked = "1");
  card.classList.add("right");
  blip("SFX-OK");
  await praise();
  round++;
  if (round >= s.rounds.length){ round = 0; next(); } else { render(); }
}

RENDER.pairs = function(s){
  const grid = document.createElement("div");
  grid.className = "grid";
  let picked = null, left = s.keys.length;
  shuffle(s.keys.concat(s.keys)).forEach(key => {
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
        blip("SFX-OK");
        await praise();
        if (left === 0) next();
      } else {
        c.classList.add("wrong");
        blip("SFX-NO");
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
  content.appendChild(cardsArea(s.keys, (c, key) => {
    const w = saying(s, key);
    if (w) play(w[1], w[0], "en-US");
  }));
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
      ? "Ты прошёл всю дорогу до праздника. А кто в яйце — узнаешь на первом уроке с преподавателем."
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
}

btnNext.onclick = next;
btnListen.onclick = () => { say(); };
lessonEl.querySelector(".home").onclick = showMap;

/* ─────────── панель просмотра ─────────── */
if (DEV_PANEL && !/[?&]dev=0/.test(location.search)){
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
    script, praise_keys, retry_keys = build_script()
    write_voice_doc(script)
    print(f"  реплик в файле озвучки: {len(script)}")

    images = {}
    for name, (rel, width, transparent) in PICTURES.items():
        path = ROOT / rel
        if not path.exists():
            sys.exit(f"нет картинки: {rel}")
        images[name] = prepare(path, width, transparent)

    audio = collect_audio()
    print(f"  дорожек озвучки: {len([k for k in audio if not k.startswith('SFX')])}")

    # каждая ссылка из спецификации должна указывать на существующую картинку
    for les in LESSONS:
        for key in ("island", "token"):
            if les[key] not in images and les[key] != "friend":
                sys.exit(f"в уроке {les['id']} нет картинки «{les[key]}»")
        for s in les["screens"]:
            keys = list(s.get("keys", []))
            if "pic" in s:
                keys.append(s["pic"])
            for r in s.get("rounds", []):
                keys += [r["target"]] + ([r["other"]] if "other" in r else r.get("others", []))
                if "who" in r:
                    keys.append(r["who"])
            for k in keys:
                if k not in images:
                    sys.exit(f"экран {s['t']} ссылается на картинку «{k}», а её нет")
            if s["t"] in ("word", "phrase") and s["key"] not in WORDS:
                sys.exit(f"слово «{s['key']}» не описано в WORDS")

    page = HTML
    for mark, value in (("__DEV__", DEV_PANEL), ("__IMG__", images), ("__AUDIO__", audio),
                        ("__LESSONS__", LESSONS), ("__PRAISE__", praise_keys),
                        ("__RETRY__", retry_keys), ("__WORDS__", WORDS),
                        ("__PHRASES__", PHRASES), ("__FRIENDS__", FRIENDS)):
        page = page.replace(mark, json.dumps(value, ensure_ascii=False))

    # литерал закрывающего тега внутри скрипта оборвал бы страницу
    if page.count("</script>") != 1:
        sys.exit("в собранной странице лишний закрывающий тег скрипта")

    OUT.write_text(page, encoding="utf-8")
    total = sum(len(l["screens"]) for l in LESSONS)
    print(f"  экранов: {total}, из них наград: "
          f"{sum(l['tokens'] for l in LESSONS)}")
    print(f"\n{OUT.name}: {len(page.encode()) / 1024 / 1024:.2f} МБ")


if __name__ == "__main__":
    main()
