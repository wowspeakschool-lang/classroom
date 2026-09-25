#!/usr/bin/env python3
"""Собирает лид-магнит 4–6 «Дорога на праздник» одним файлом.

    python3 tools/build_kids46.py

На выходе:
  wowspeak-4-6.html              карта и три урока, картинки внутри
  docs/WowSpeak_озвучка_4-6.md   что озвучивать — из тех же реплик

Содержание уроков лежит в `kids46_lessons.py`, перекраска — в `recolor.py`.
Здесь картинки, вёрстка и сборка.
"""

import base64
import io
import json
import math
import struct
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kids46_lessons as LS
from recolor import recolor

# 🟥 Перед публикацией поставить False и пересобрать: пока панель включена,
# ребёнок пролистает урок мимо заданий.
DEV_PANEL = True

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "wowspeak-4-6.html"
VOICE_DOC = ROOT / "docs" / "WowSpeak_озвучка_4-6.md"
AUDIO_DIR = ROOT / "assets" / "audio-4-6"
ART = ROOT / "assets" / "kids-4-6"

COLOR_HUE = {"green": 120, "blue": 215, "yellow": 48}

# Замкнутые белые области, которые надо вырезать: доля кадра, начиная с
# которой это дырка, а не блик. Выбрано для каждой картинки глазами —
# по размеру блик от дырки не отличается. Чего тут нет, у того замкнутых
# дырок не бывает: у камушка и облачка такой проход выедал блик.
HOLES = {
    "clouds": 0.5,      # просвет под радугой
    "meadow": 0.15,     # просветы под бельевой верёвкой
    "dragon": 0.20,     # просветы под гирляндой
    "push": 0.10,       # просветы между зверятами и камнем
    "jeans": 1.00,      # просвет между штанинами
    "cup": 0.50,        # дырка в ручке (блик там же — 0.11%)
    "basket": 0.10,     # дырки в двух ручках
    "suitcase": 0.20,   # щель между крышкой и дном
}

# кончики пальцев в долях от рамки фигуры, слева направо.
# Автоматически они не ловятся: большой палец торчит вбок и по верхнему
# контуру не находится. Снято по сетке руками — картинки не меняются.
FINGER_TIPS = {
    5: [(0.07, 0.46), (0.30, 0.11), (0.47, 0.05), (0.645, 0.10), (0.86, 0.21)],
    4: [(0.17, 0.10), (0.39, 0.05), (0.62, 0.10), (0.86, 0.24)],
    3: [(0.23, 0.10), (0.51, 0.05), (0.79, 0.10)],
    2: [(0.29, 0.07), (0.70, 0.07)],
    1: [(0.23, 0.05)],
}


# ──────────────────────────────────────────────────────────── картинки ──

def cut_white(im, bright=250, neutral=6, shadow=170, shadow_n=4, holes=None):
    """Убирает фон генератора: светлый И бесцветный.

    Одной яркости мало. Фон строго серый (max−min = 0), а белые места самих
    картинок тонированные — у облака розоватые, у камушка желтоватые.
    Допуск 6, а не 0: у самого фона рядом со светящейся звёздочкой
    облачного острова разброс доходит до 5, и при допуске 3 сбоку от
    звёздочки оставался белый квадрат. При 6 ни одна картинка не теряет
    и 0.1% непрозрачных пикселей — в рисунки заливка не уходит.
    Заливка «по яркости» уходила внутрь облака и выедала его: исчезало 19%
    картинки. Условие «бесцветный» эту дорогу закрывает — цепочка серых
    пикселей внутри облака рвётся на первом же розовом. С ним же безопасен
    проход по замкнутым областям: под радугой оставался белый кусок, до
    которого заливка от краёв не дотягивается.
    """
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()

    def is_bg(x, y):
        r, g, b, a = px[x, y]
        if a == 0:
            return False
        lo, hi = min(r, g, b), max(r, g, b)
        if lo >= bright and hi - lo <= neutral:
            return True
        # Вторая полоса — запечённая тень под предметом. Она серая насквозь
        # (254 → 248 → 199 → 181) и на цветном фоне читается белым пятном.
        # Порог по яркости мягче, зато серость строгая: у одежды подошва
        # и строчка белые, но чуть тёплые, и под это правило не попадают.
        return lo >= shadow and hi - lo <= shadow_n

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
        floor = int(w * h * holes / 100)
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
    return feather(im)


def feather(im, passes=3, light=214, full=250):
    """Растушёвывает край: чем пиксель на границе белее, тем он прозрачнее.

    Вырезается только чистый фон, а сглаженные пиксели по краю фигуры под
    порог не попадают — и вокруг острова, белья и верёвки остаётся белая
    кайма. На голубом фоне карты она видна сразу.
    """
    im = im.convert("RGBA")
    r, g, b, a = im.split()
    mn = ImageChops.darker(ImageChops.darker(r, g), b)
    fade = mn.point(lambda p: 255 if p < light
                    else max(0, min(255, int((full - p) * 255 / (full - light)))))
    for _ in range(passes):
        border = ImageChops.subtract(a, a.filter(ImageFilter.MinFilter(3)))
        mask = border.point(lambda p: 255 if p > 0 else 0)
        a = Image.composite(ImageChops.darker(a, fade), a, mask)
    im.putalpha(a)
    return im


def encode(im, width, quality=80):
    box = im.getbbox()
    if box:
        im = im.crop(box)
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=quality, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


# Ширина — вдвое больше самого крупного места показа: на телефоне пиксель
# экрана вдвое мельче пикселя картинки, вшитая впритык выглядит мыльной.
# Проверка сравнивает натуральный размер с показанным и ругается.
BASE = {            # имя: (файл, ширина, резать ли фон)
    "map_bg":        ("map-background-wide.webp", 1536, False),
    "meadow":        ("island-meadow.webp",       1100, True),
    "clouds":        ("island-clouds.webp",       1100, True),
    "dragon":        ("island-dragon.webp",       1100, True),
    "firefly":       ("firefly-neutral.webp",      760, True),
    "firefly_smile": ("firefly-smile.webp",        760, True),
    "firefly_wow":   ("firefly-excited.webp",      760, True),
    "stone":         ("stone.webp",                560, True),
    "cloudlet":      ("cloudlet.webp",             560, True),
    "egg":           ("egg.webp",                 1000, True),
    "cave_closed":   ("cave-closed.webp",         1000, True),
    "cave_open":     ("cave-open.webp",           1000, True),
    "bunny":         ("animal-bunny.webp",         700, True),
    "hedgehog":      ("animal-hedgehog.webp",      700, True),
    "fox":           ("animal-fox.webp",           700, True),
    "push":          ("friends-push.webp",        1300, True),
    "suitcase":      ("suitcase.webp",             800, True),
    "machine":       ("washing-machine.webp",      800, True),
    "shelf":         ("shop-shelf.webp",          1100, True),
    "hand1":         ("hand-1.webp",               700, True),
    "hand2":         ("hand-2.webp",               700, True),
    "hand3":         ("hand-3.webp",               700, True),
    "hand4":         ("hand-4.webp",               700, True),
    "hand5":         ("hand-5.webp",               700, True),
}

# что красим в три цвета: (имя, файл, ширина)
PAINTED = (
    # 1200, а не 900: на широком экране одиночный предмет показывается
    # на 948 px, и на 900 он уже мылил.
    [(o, f"obj-{o}.webp", 1200) for o in LS.OBJS] +
    [("top", "../lesson-1/tshirt.webp", 1000),
     ("jeans", "../lesson-1/jeans.webp", 1000),
     ("shoes", "../lesson-1/shoes.webp", 1000),
     ("balloon", "balloon.webp", 560),
     ("basket", "basket.webp", 520),
     ("blob", "paint-blob.webp", 480)]
)

# Что перекрашивать не по господствующему тону. У цветка три собственных
# цвета — розовые лепестки, жёлтая середина, зелёный стебель; полоса тона
# захватывала середину и половину стебля, и синий цветок выходил в полоску.
# Красим его целиком, а насыщенность поднимаем: в исходнике он пастельный,
# и рядом с шариком его зелёный читался другим цветом.
PAINT_OPTS = {"flower": {"whole": True, "sat": 1.65}}


CACHE = ROOT / "tools" / ".kids46_images.json"


def build_images():
    sig = {"base": {k: [v[0], v[1], v[2], (ART / v[0]).stat().st_mtime]
                    for k, v in BASE.items()},
           "painted": [[n, f, w, (ART / f).stat().st_mtime, PAINT_OPTS.get(n)]
                       for n, f, w in PAINTED],
           "hue": COLOR_HUE}
    if CACHE.exists():
        old = json.loads(CACHE.read_text())
        if old.get("sig") == sig:
            print("  картинки из кэша")
            return old["images"]

    images = {}
    for name, (f, width, cut) in BASE.items():
        im = Image.open(ART / f)
        images[name] = encode(cut_white(im, holes=HOLES.get(name)) if cut
                              else im.convert("RGB"), width)
    # В пещере по сюжету яйцо, а на картинке пустое гнездо: вклеиваем.
    cave = cut_white(Image.open(ART / "cave-open.webp"), holes=HOLES.get("cave_open"))
    egg = cut_white(Image.open(ART / "egg.webp"))
    egg = egg.crop(egg.getbbox())
    w = int(cave.width * 0.21)
    egg = egg.resize((w, round(egg.height * w / egg.width)), Image.LANCZOS)
    cave.alpha_composite(egg, (int(cave.width * 0.395), int(cave.height * 0.435)))
    images["cave_egg"] = encode(cave, 1000)

    for name, f, width in PAINTED:
        src = cut_white(Image.open(ART / f), holes=HOLES.get(name))
        src = src.crop(src.getbbox())
        if src.width > width * 1.6:          # красим уже уменьшенную — быстрее
            src = src.resize((int(width * 1.6),
                              round(src.height * width * 1.6 / src.width)), Image.LANCZOS)
        for color, hue in COLOR_HUE.items():
            opts = PAINT_OPTS.get(name, {})
            images[f"{name}_{color}"] = encode(recolor(src, hue, **opts), width)
    CACHE.write_text(json.dumps({"sig": sig, "images": images}))
    return images


# ───────────────────────────────────── номера дорожек и файл озвучки ──

def build_script():
    """Раздаёт RU-NN по порядку, вставляет экраны наград, готовит дриллы."""
    en_tracks, en_key = LS.english_tracks()
    script = []
    n = [0]

    def ru(voice, text, tone, where):
        n[0] += 1
        k = "RU-%02d" % n[0]
        script.append((k, voice, text, tone, where))
        return k

    def en(text):
        return [en_key[text], text, len(text.split())]

    def say_of(mode, thing):
        item, color = thing
        if mode == "color":
            return en(color)
        if mode == "item":
            return en(LS.ITEM_EN[item])
        if mode == "combo":
            return en(LS.combo(item, color))
        return en(LS.sentence(item, color))

    for les in LS.LESSONS:
        where = "Урок %d. %s" % (les["id"], les["title"])
        out, earned = [], 0
        for s in les["screens"]:
            s["ru"] = ru("firefly", s["text"], s.get("tone", ""), where)

            if s["t"] == "fingers":
                prep_fingers(s, en, say_of)
            elif "thing" in s:
                s["voice"] = say_of(s.get("say", "color"), s["thing"])

            for r in s.get("rounds", []):
                if isinstance(r, dict) and "target" in r:
                    r["voice"] = say_of(s["say"], r["target"])
                elif isinstance(r, (list, tuple)) and s["t"] == "name":
                    r = tuple(r)
            if s["t"] == "name":
                s["rounds"] = [{"thing": list(t), "voice": say_of(s["say"], t)}
                               for t in s["rounds"]]
            if s["t"] == "sort":
                s["rounds"] = [{"thing": list(t), "voice": say_of("color", t)}
                               for t in s["rounds"]]
            if s["t"] == "vocab":
                s["things"] = [{"thing": list(t), "voice": say_of(s["say"], t)}
                               for t in s["things"]]
            if s["t"] == "truefalse":
                s["rounds"] = [{"thing": list(r["thing"]), "claim": list(r["claim"]),
                                "voice": say_of(s["say"], r["claim"]),
                                "ok": list(r["thing"]) == list(r["claim"])}
                               for r in s["rounds"]]
            if s["t"] == "findall":
                s["voice"] = en(s["color"])
            if s["t"] == "order":
                s["rounds"] = [{"seq": seq, "voices": [en(c) for c in seq]}
                               for seq in s["rounds"]]

            out.append(s)
            if s.pop("token", False):
                text, tone = les["token_lines"][earned]
                earned += 1
                out.append({"t": "token", "n": earned,
                            "kind": "friends" if les["token"] == "friend" else "map",
                            "text": text, "ru": ru("firefly", text, tone, where)})
        les["screens"] = out
        les["tokens"] = earned
        if earned != len(les["token_lines"]):
            sys.exit(f"в уроке {les['id']} наград {earned}, "
                     f"а реплик к ним {len(les['token_lines'])}")

    where = "Похвалы — звучат во всех трёх уроках"
    praise = [ru("firefly", t, tone, where) for t, tone in LS.PRAISE]
    retry = [ru("firefly", t, tone, where) for t, tone in LS.RETRY]
    ask = ru("firefly", LS.ASK_REPEAT[0], LS.ASK_REPEAT[1], where)
    finale = ru("firefly", LS.FINALE[0], LS.FINALE[1], where)
    return script, praise, retry, ask, finale, en_tracks


def prep_fingers(s, en, say_of):
    """Готовит дрилл: список слов фразы и диапазон слов на каждом шаге.

    Раньше на шаге звучала вся фраза целиком, а стрелка прыгала по пальцам —
    к третьему пальцу фраза уже кончилась. Теперь звучит слово за словом,
    палец в палец.
    """
    if s["mode"] == "swap":
        rounds, prev = [], None
        for item, color in s["things"]:
            cue = None
            if prev is not None:
                cue = en(color) if prev[1] != color else en(LS.ITEM_BARE[item])
            text = LS.sentence(item, color)
            rounds.append({"pic": f"{item}_{color}", "cue": cue,
                           "words": [en(w) for w in text.split()],
                           "line": en(text)})
            prev = (item, color)
        s["rounds"] = rounds
        s.pop("things")
        return

    item, color = s["thing"]
    text = LS.sentence(item, color)
    words = [en(w) for w in text.split()]
    n = len(words)
    s["words"] = words
    s["line"] = en(text)
    s["pic"] = f"{item}_{color}"
    if s["mode"] == "full":
        s["steps"] = [[0, n - 1]]
    elif s["mode"] == "chain":
        # по слову за шаг: I · I have · I have a · … Прыжок сразу к целой
        # фразе сводил дрилл на нет — ребёнок повторял её с двух слов.
        s["steps"] = [[0, i] for i in range(n)]
    else:                                   # back — собираем с конца
        s["steps"] = [[i, n - 1] for i in range(n - 1, -1, -1)]


def write_voice_doc(script, en_tracks):
    rows, counts = {}, {}
    for k, voice, text, tone, where in script:
        rows.setdefault(where, []).append((k, voice, text, tone))
        counts[voice] = counts.get(voice, 0) + 1

    d = ["""# Озвучка лид-магнита 4–6 «Дорога на праздник»

> Файл собирается скриптом `tools/build_kids46.py` вместе с самим уроком.
> Руками не правим: номера дорожек здесь и в уроке всегда одни и те же.

Ребёнок ещё не читает, поэтому **всё держится на голосе**. Текст на экране —
только для взрослого рядом.

## Кого озвучиваем

| Кто | Каким голосом | Реплик | Характер |
|---|---|---|---|"""]
    d.append("| **Искорка**, светлячок-проводник | детский, звонкий, тёплый | %d | "
             "Ведёт всё приключение. Радуется, удивляется, зовёт за собой. |"
             % counts.get("firefly", 0))
    for v, desc, ch in (("bunny", "детский, мягкий, чуть робкий", "Стеснительный."),
                        ("hedgehog", "детский, пониже, забавный", "Деловитый, ворчливый."),
                        ("fox", "детский, быстрый, озорной", "Торопится на праздник.")):
        if counts.get(v):
            d.append("| **%s** | %s | %d | %s |" % (LS.VOICES[v], desc, counts[v], ch))
    d.append("""
## Как записывать

**Тон:** тёплый, небыстрый, как будто рассказываете сказку четырёхлетке.
Не «диктор новостей». Интонации важнее дикции: где «Ой…» — настоящее
удивление, где «Смотри!» — радость.

**Английские слова внутри русских реплик** произносятся по-английски, но той
же интонацией. Если сервис читает их по-русски, разбейте реплику на две
дорожки или возьмите многоязычный голос.

**Файлы.** Каждая реплика — отдельный файл, имя ровно как в таблице:
`RU-01.mp3`, `EN-01.mp3`. Положить в `assets/audio-4-6/`, сборка подхватит
сама. Если сервис отдаёт одним файлом — пришлите как есть, с паузами в две
секунды, нарежу.
""")
    for where, items in rows.items():
        d.append("## %s\n" % where)
        d.append("| Файл | Кто | Текст | Интонация |")
        d.append("|---|---|---|---|")
        for k, voice, text, tone in items:
            d.append("| %s | %s | %s | %s |" % (k, LS.VOICES[voice], text, tone))
        d.append("")

    d.append("""## Английские дорожки

Отдельным голосом: **носитель языка, взрослый, спокойный и чёткий**. Не
детский — здесь нужен эталон произношения.

Слова и сочетания (EN-01…EN-15) нужны **дважды**: обычно и чуть медленнее.
Медленный вариант — с суффиксом: `EN-01.mp3` и `EN-01-slow.mp3`. Фразам
медленный вариант не нужен.
""")
    d.append("| Файл | Текст |")
    d.append("|---|---|")
    for k, text in en_tracks:
        d.append("| %s | %s |" % (k, text))

    d.append("""
## Где это сделать бесплатно

**[ElevenLabs](https://elevenlabs.io)** — лучшее качество русского и
единственный, где интонации живые; есть детские голоса, английские слова
внутри русской фразы читает правильно. Бесплатно ~10 000 символов в месяц.

**[TTSMaker](https://ttsmaker.com/ru)** — без регистрации, отдаёт mp3 сразу,
но интонации беднее.

**Яндекс SpeechKit** — родной русский с правильными ударениями, бесплатный
лимит через облако.

**Свой голос — тоже вариант, и часто лучший.** Живая интонация мамы бьёт
любой синтез.

## Пока озвучки нет

Русские реплики **молчат** — текст виден в пузыре, взрослый читает вслух.
Английские слова проговаривает синтез браузера. На верный и неверный ответ
звучат короткие сигналы.
""")
    VOICE_DOC.write_text("\n".join(d), encoding="utf-8")


# ──────────────────────────────────────────────────────────────── звук ──

def tone_wav(notes, volume=0.22, rate=22050):
    """Короткий сигнал отклика: без озвучки ребёнку нужен ответ на нажатие."""
    frames = bytearray()
    for freq, dur in notes:
        n = int(rate * dur)
        for i in range(n):
            env = min(1.0, i / (rate * 0.01), (n - i) / (rate * 0.05))
            frames += struct.pack("<h", int(32767 * volume * env *
                                            math.sin(2 * math.pi * freq * i / rate)))
    head = (b"RIFF" + struct.pack("<I", 36 + len(frames)) + b"WAVEfmt " +
            struct.pack("<IHHIIHH", 16, 1, 1, rate, rate * 2, 2, 16) +
            b"data" + struct.pack("<I", len(frames)))
    return "data:audio/wav;base64," + base64.b64encode(head + bytes(frames)).decode()


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


HTML = (Path(__file__).resolve().parent / "kids46_page.html").read_text(encoding="utf-8")


def main():
    script, praise, retry, ask, finale, en_tracks = build_script()
    write_voice_doc(script, en_tracks)
    print(f"  русских реплик: {len(script)}, английских: {len(en_tracks)}")

    images = build_images()
    print(f"  картинок: {len(images)}")

    # каждая ссылка из уроков должна указывать на существующую картинку
    def need(key):
        if key not in images:
            sys.exit(f"в уроках есть ссылка на картинку «{key}», а её нет")

    for les in LS.LESSONS:
        need(les["island"])
        if les["token"] != "friend":
            need(les["token"])
        for s in les["screens"]:
            for k in ("pic", "who"):
                if s.get(k):
                    need(s[k])
            if s["t"] == "collect":
                need(s["target"])
            for thing in ([s["thing"]] if "thing" in s else []):
                need("%s_%s" % tuple(thing))
            for r in s.get("rounds", []):
                if not isinstance(r, dict):
                    continue
                if r.get("pic"):
                    need(r["pic"])
                for t in ([r["thing"]] if "thing" in r else []):
                    need("%s_%s" % tuple(t))
                for t in ([r["target"]] if "target" in r else []) + r.get("others", []):
                    need("%s_%s" % tuple(t))
            for t in s.get("things", []):
                need("%s_%s" % tuple(t["thing"] if isinstance(t, dict) else t))
            for r in s.get("rounds", []):
                if isinstance(r, dict) and "claim" in r:
                    need("%s_%s" % tuple(r["thing"]))
            for t in s.get("pool", []):
                need("%s_%s" % tuple(t))

    audio = collect_audio()
    page = HTML
    for mark, value in (("__DEV__", DEV_PANEL), ("__IMG__", images),
                        ("__AUDIO__", audio), ("__LESSONS__", LS.LESSONS),
                        ("__PRAISE__", praise), ("__RETRY__", retry),
                        ("__ASK__", ask), ("__FINALE__", finale),
                        ("__COLORS__", LS.COLORS),
                        ("__FRIENDS__", LS.FRIENDS), ("__TIPS__", FINGER_TIPS)):
        page = page.replace(mark, json.dumps(value, ensure_ascii=False))

    if page.count("</script>") != 1:
        sys.exit("в собранной странице лишний закрывающий тег скрипта")

    OUT.write_text(page, encoding="utf-8")
    tasks = sum(1 for l in LS.LESSONS for s in l["screens"]
                if s["t"] not in ("story", "token", "word"))
    print(f"  экранов {sum(len(l['screens']) for l in LS.LESSONS)}, "
          f"заданий {tasks}, наград {sum(l['tokens'] for l in LS.LESSONS)}")
    print(f"\n{OUT.name}: {len(page.encode()) / 1024 / 1024:.2f} МБ")


if __name__ == "__main__":
    main()
