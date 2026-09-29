#!/usr/bin/env python3
"""Собирает `tools/ozvuchka.py` — скрипт озвучки для запуска у Анны.

    python3 tools/export_voice_job.py

Зачем отдельный файл, если есть `tts_kids46.py`. Тот тянет за собой весь
репозиторий и Pillow: он берёт тексты из `build_script()`, а тот импортирует
сборщик. У Анны на машине ничего этого нет и быть не должно. Поэтому тексты
всех дорожек вписываются в один файл, и ему хватает голого Python —
`urllib` лежит в стандартной библиотеке.

Файл переписывается целиком при каждом запуске, поэтому правки текстов
доезжают: поменяли реплику в `kids46_lessons.py` — прогнали экспорт заново.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_kids46 import build_script

OUT = Path(__file__).resolve().parent / "ozvuchka.py"

# Голос и роль каждому герою. Роль поддержана не у всех голосов, поэтому
# в скрипте на отказ из-за неё запрос уходит повторно без роли.
#
# Английских дорожек здесь нет, и это решение Анны: английские слова
# читает синтез браузера, и он их читает хорошо — записываем только
# русские реплики, где браузерный голос звучит плохо.
VOICE = {
    "firefly":  ("alena", "good"),
    "bunny":    ("jane",  "good"),
    "hedgehog": ("ermil", "good"),
    "fox":      ("zahar", "good"),
}

TEMPLATE = '''# -*- coding: utf-8 -*-
"""Озвучка лид-магнита WowSpeak 4-6 через Yandex SpeechKit.

Файл собран скриптом, руками его править не нужно — кроме таблицы ГОЛОСА
ниже и двух строк с ключом.

Как пользоваться — в инструкции WowSpeak_озвучка_яндекс.md. Коротко:

    python ozvuchka.py obrazcy    записать по образцу на каждый голос
    python ozvuchka.py            записать все реплики
    python ozvuchka.py RU-05      переписать одну реплику заново
"""

# ─────────────────────────────── сюда вставить свои две строки ──

KEY = ""        # API-ключ сервисного аккаунта, начинается на AQVN
FOLDER = ""     # идентификатор каталога, начинается на b1g

# ──────────────────────────────────────────── голоса героев ──
#
# Слева — герой, справа — голос Яндекса и роль. Послушайте образцы
# (python ozvuchka.py obrazcy) и замените имя голоса, если не понравился.
# Роль можно убрать, написав None вместо "good".

VOICES = {json_voices}

# Кого прогонять в режиме obrazcy. Неизвестное сервису имя просто
# пропускается с пометкой — так и видно, какие голоса есть на самом деле.
SAMPLES = {json_samples}

SPEED = "0.95"        # чуть медленнее обычного: слушает четырёхлетка

# ───────────────────────────────────────────── сами реплики ──

TRACKS = {json_tracks}

# ─────────────────────────────────────────────────── работа ──

import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

URL = "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "audio-4-6")

try:                                   # чтобы русские буквы печатались в cmd
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def synth(text, who, voice=None, emotion=None):
    if voice is None:
        voice, emotion = VOICES[who]
    form = {{"text": text, "voice": voice, "format": "mp3",
            "lang": "ru-RU",
            "speed": SPEED,
            "folderId": FOLDER}}
    if emotion:
        form["emotion"] = emotion
    req = urllib.request.Request(
        URL, data=urllib.parse.urlencode(form).encode(),
        headers={{"Authorization": "Api-Key " + KEY}})
    try:
        return urllib.request.urlopen(req, timeout=120).read()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        # Роль есть не у каждого голоса, и отказ из-за неё выглядит как
        # отказ вообще. Пробуем ещё раз без роли, прежде чем сдаться.
        if e.code == 400 and emotion and "emotion" in body.lower():
            return synth(text, who, voice, None)
        raise RuntimeError("%s %s" % (e.code, body[:300]))


def check_keys():
    if not KEY or not FOLDER:
        stop("Не вписаны KEY и FOLDER в начале файла — без них сервис не "
             "поймёт, кто к нему пришёл.")


def stop(msg):
    print("\\n" + msg)
    try:
        input("\\nНажмите Enter, чтобы закрыть окно.")
    except Exception:
        pass
    sys.exit(1)


def main():
    args = sys.argv[1:]
    check_keys()

    if args and args[0] in ("obrazcy", "samples"):
        line = "Смотри! Мы на Драконьем Острове. Ой… а где же все?"
        out = os.path.join(HERE, "obrazcy")
        os.makedirs(out, exist_ok=True)
        for v in SAMPLES:
            try:
                data = synth(line, "firefly", v, "good")
            except RuntimeError as e:
                print("  %-12s — нет такого голоса (%s)" % (v, str(e)[:60]))
                continue
            with open(os.path.join(out, v + ".mp3"), "wb") as f:
                f.write(data)
            print("  %-12s — записан" % v)
        print("\\nОбразцы лежат в папке obrazcy рядом с этим файлом.")
        print("Послушайте и, если нужно, поменяйте имена в таблице VOICES.")
        return

    only = set(a for a in args if a.startswith("RU-"))
    os.makedirs(OUT, exist_ok=True)
    done = skipped = 0
    for key, text, who in TRACKS:
        path = os.path.join(OUT, key + ".mp3")
        if os.path.exists(path) and (not only or key not in only):
            skipped += 1
            continue
        for attempt in range(4):
            try:
                data = synth(text, who)
                break
            except RuntimeError as e:
                msg = str(e)
                if msg.startswith("429") and attempt < 3:
                    time.sleep(2 * (attempt + 1))
                    continue
                if msg.startswith("401") or msg.startswith("403"):
                    stop("Сервис не принял ключ (%s).\\nПроверьте KEY и FOLDER "
                         "и что сервисному аккаунту выдана роль "
                         "ai.speechkit-tts.user." % msg[:40])
                stop("Дорожка %s не записалась: %s" % (key, msg[:300]))
        with open(path, "wb") as f:
            f.write(data)
        done += 1
        print("  %-12s %s" % (key, text[:58]))
        time.sleep(0.2)

    print("\\nЗаписано %d, уже было %d. Файлы в папке audio-4-6." % (done, skipped))
    print("Положите эту папку в Google Drive и напишите мне.")
    try:
        input("\\nНажмите Enter, чтобы закрыть окно.")
    except Exception:
        pass


if __name__ == "__main__":
    main()
'''

SAMPLES = ("alena", "jane", "omazh", "dasha", "julia", "lera", "masha",
           "marina", "filipp", "ermil", "zahar", "alexander", "kirill",
           "anton", "madi_ru", "zorro", "ermolaev")


def one_line(obj):
    """json.dumps с русскими буквами как есть — файл читают глазами."""
    return json.dumps(obj, ensure_ascii=False)


def block(rows):
    """Список по строке на запись: так таблицу голосов правят руками."""
    return "[\n" + "".join("    %s,\n" % one_line(r) for r in rows) + "]"


def table(d):
    return "{\n" + "".join('    "%s": %s,\n' % (k, one_line(v))
                            for k, v in d.items()) + "}"


def main():
    script, *_, _en_list = build_script()
    tracks = [[key, text, who] for key, who, text, _tone, _where in script]

    voices = table({k: list(v) for k, v in VOICE.items()})
    body = TEMPLATE.replace("{json_voices}", voices.replace("null", "None")) \
                   .replace("{json_samples}", one_line(list(SAMPLES))) \
                   .replace("{json_tracks}", block(tracks)) \
                   .replace("{{", "{").replace("}}", "}")
    OUT.write_text(body, encoding="utf-8")
    chars = sum(len(t[1]) for t in tracks)
    print(f"{OUT.name}: дорожек {len(tracks)}, знаков {chars}, "
          f"{OUT.stat().st_size // 1024} КБ")


if __name__ == "__main__":
    main()
