#!/usr/bin/env python3
"""Озвучивает лид-магнит 4–6 через OpenAI и раскладывает файлы по именам.

    python3 tools/tts_kids46.py --list      что будет сгенерировано и сколько знаков
    python3 tools/tts_kids46.py --voices    по одному образцу на каждый голос
    python3 tools/tts_kids46.py            сгенерировать недостающее
    python3 tools/tts_kids46.py --force RU-05 RU-06   переделать конкретные дорожки

Файлы ложатся в `assets/audio-4-6/`, сборка подхватывает их сама. Уже
записанное не трогается — так можно переделать одну реплику, не трогая
остальные.

Интонацию модель принимает отдельным полем, и мы отдаём ей ровно то, что
написано в колонке «интонация» файла озвучки. Ради этого колонка и заводилась.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kids46_lessons as LS
from build_kids46 import build_script

OUT = Path(__file__).resolve().parent.parent / "assets" / "audio-4-6"
MODEL = "gpt-4o-mini-tts"
URL = "https://api.openai.com/v1/audio/speech"

# Голоса героев. Меняются одной строкой — если какой-то не понравится,
# послушайте образцы через --voices и впишите другой.
VOICE = {
    "firefly":  "shimmer",   # светлячок Искорка: звонкий, тёплый
    "bunny":    "nova",      # зайчик: мягкий, чуть робкий
    "hedgehog": "ash",       # ёжик: пониже, деловитый
    "fox":      "ballad",    # лисёнок: быстрый, озорной
}
EN_VOICE = "alloy"           # английский: взрослый, спокойный, чёткий

BASE_RU = ("Ты — герой сказки для ребёнка четырёх лет. Говори тепло и небыстро, "
           "как будто рассказываешь сказку, сидя рядом. Короткие фразы, паузы между "
           "предложениями. Не диктор новостей. ")
BASE_EN = ("Speak as a calm, friendly adult native speaker teaching a very young "
           "child. Very clear articulation, unhurried, warm. ")
SLOW_EN = BASE_EN + "Speak noticeably slower than usual, stretching the word."


def tracks():
    """Что нужно озвучить: (имя файла, текст, голос, указание интонации)."""
    script, praise, retry, ask, en_list = build_script()
    out = []
    for key, voice, text, tone, _where in script:
        out.append((key, text, VOICE[voice], BASE_RU + (tone or "")))
    for key, text in en_list:
        out.append((key, text, EN_VOICE, BASE_EN))
        if len(text.split()) <= 3:        # слова и сочетания — ещё и медленно
            out.append((key + "-slow", text, EN_VOICE, SLOW_EN))
    return out


def speak(text, voice, instructions):
    body = json.dumps({"model": MODEL, "voice": voice, "input": text,
                       "instructions": instructions,
                       "response_format": "mp3"}).encode()
    req = urllib.request.Request(URL, data=body, headers={
        "Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
        "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def main():
    args = sys.argv[1:]
    todo = tracks()

    if "--list" in args:
        total = sum(len(t) for _, t, _, _ in todo)
        print(f"дорожек {len(todo)}, знаков {total}")
        for key, text, voice, _ in todo:
            mark = "есть" if (OUT / (key + ".mp3")).exists() else "  — "
            print(f"  {mark} {key:12s} {voice:8s} {text[:60]}")
        return

    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("нет OPENAI_API_KEY в окружении")
    OUT.mkdir(parents=True, exist_ok=True)

    if "--voices" in args:
        line = "Смотри! Мы на Драконьем Острове. Ой… а где же все?"
        for v in ("alloy", "ash", "ballad", "coral", "echo", "fable",
                  "nova", "onyx", "sage", "shimmer", "verse"):
            f = OUT.parent / "voice-samples" / f"{v}.mp3"
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(speak(line, v, BASE_RU + "удивлённо, потом растерянно"))
            print("  образец:", f.name)
        return

    force = set(a for a in args if a.startswith(("RU-", "EN-")))
    done = skipped = 0
    for key, text, voice, instr in todo:
        f = OUT / (key + ".mp3")
        if f.exists() and (not force or key not in force):
            skipped += 1
            continue
        for attempt in range(3):
            try:
                f.write_bytes(speak(text, voice, instr))
                done += 1
                print(f"  {key:12s} {voice:8s} {len(text):3d} знаков")
                break
            except urllib.error.HTTPError as e:
                msg = e.read().decode()[:200]
                if e.code == 429 and "quota" not in msg and "credits" not in msg:
                    time.sleep(2 * (attempt + 1))
                    continue
                sys.exit(f"{key}: {e.code} {msg}")
        time.sleep(0.2)
    print(f"\nзаписано {done}, уже было {skipped}")
    print("теперь пересоберите: python3 tools/build_kids46.py")


if __name__ == "__main__":
    main()
