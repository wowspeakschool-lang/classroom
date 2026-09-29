#!/usr/bin/env python3
"""Озвучивает лид-магнит 4–6 и раскладывает файлы по именам.

    python3 tools/tts_kids46.py --list      что будет записано и сколько знаков
    python3 tools/tts_kids46.py --voices    по образцу на каждый голос-кандидат
    python3 tools/tts_kids46.py            записать недостающее
    python3 tools/tts_kids46.py --force RU-05 RU-06   переделать конкретные дорожки

Пишем **только русские реплики**, через Yandex SpeechKit: у него родной
русский — ударения и вопросительная интонация. Английские слова читает
синтез браузера прямо у ребёнка, и читает хорошо, поэтому файлов под них
не нужно — `--en` по умолчанию `off`.

Переключается флагами: `--ru openai`, `--en openai`. Ключи берутся из
окружения — `YANDEX_API_KEY` (и `YANDEX_FOLDER_ID`, если ключ его требует)
и `OPENAI_API_KEY`; нужен только ключ того движка, который вызываете.

Файлы ложатся в `assets/audio-4-6/`, сборка подхватывает их сама. Уже
записанное не трогается — так можно переделать одну реплику, не трогая
остальные.

Интонация у движков задаётся по-разному, и это не мелочь: OpenAI принимает
её текстом («удивлённо, потом растерянно») — туда уходит ровно то, что
написано в колонке «интонация» файла озвучки. У Yandex вместо текста
короткий список ролей (`neutral`, `good`, `evil`, `whisper`), и поддержаны
они не у каждого голоса, поэтому роль подбирается по голосу, а на отказ
сервиса запрос повторяется без неё.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kids46_lessons as LS
from build_kids46 import build_script

OUT = Path(__file__).resolve().parent.parent / "assets" / "audio-4-6"

# ─────────────────────────────────────────────────────────── OpenAI ──

OA_MODEL = "gpt-4o-mini-tts"
OA_URL = "https://api.openai.com/v1/audio/speech"

# Голоса героев у OpenAI. Меняются одной строкой — послушайте образцы
# через --voices и впишите другой.
OA_VOICE = {
    "firefly":  "shimmer",   # светлячок Искорка: звонкий, тёплый
    "bunny":    "nova",      # зайчик: мягкий, чуть робкий
    "hedgehog": "ash",       # ёжик: пониже, деловитый
    "fox":      "ballad",    # лисёнок: быстрый, озорной
    "en":       "alloy",     # английский: взрослый, спокойный, чёткий
}
OA_SAMPLES = ("alloy", "ash", "ballad", "coral", "echo", "fable",
              "nova", "onyx", "sage", "shimmer", "verse")

BASE_RU = ("Ты — герой сказки для ребёнка четырёх лет. Говори тепло и небыстро, "
           "как будто рассказываешь сказку, сидя рядом. Короткие фразы, паузы между "
           "предложениями. Не диктор новостей. ")
BASE_EN = ("Speak as a calm, friendly adult native speaker teaching a very young "
           "child. Very clear articulation, unhurried, warm. ")
SLOW_EN = BASE_EN + "Speak noticeably slower than usual, stretching the word."

# ────────────────────────────────────────────────── Yandex SpeechKit ──

YA_URL = "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize"

# Голоса героев у Yandex и роль к каждому. Роль — не любая: у большинства
# голосов есть `neutral` и `good`, у некоторых нет ни одной. Не подошла —
# впишите None, запрос уйдёт без неё.
YA_VOICE = {
    "firefly":  ("alena", "good"),      # Искорка: тёплая, живая
    "bunny":    ("jane",  "good"),      # зайчик
    "hedgehog": ("ermil", "good"),      # ёжик
    "fox":      ("zahar", "good"),      # лисёнок
    "en":       ("john",  None),        # английский
}
# Кого прогоняет --voices. Список нарочно шире рабочего: какие голоса
# сервис знает сегодня, видно только по ответу — неизвестное имя он
# отвергает, и скрипт просто пишет «нет такого» и идёт дальше. Детские
# голоса (`zorro`, `ermolaev`) здесь именно поэтому: они упоминаются в
# обзорах, но на слово этому верить нельзя.
YA_SAMPLES = ("alena", "jane", "omazh", "dasha", "julia", "lera", "masha",
              "marina", "filipp", "ermil", "zahar", "alexander", "kirill",
              "anton", "madi_ru", "zorro", "ermolaev")
YA_SPEED = "0.95"        # чуть медленнее обычного: слушает четырёхлетка


def speak_openai(text, who, tone, voice=None):
    lang_en = who.startswith("en")
    instructions = (SLOW_EN if who == "en_slow" else BASE_EN) if lang_en \
        else BASE_RU + (tone or "")
    body = json.dumps({"model": OA_MODEL, "input": text,
                       "voice": voice or OA_VOICE["en" if lang_en else who],
                       "instructions": instructions,
                       "response_format": "mp3"}).encode()
    req = urllib.request.Request(OA_URL, data=body, headers={
        "Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
        "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def speak_yandex(text, who, tone, voice=None, emotion=None):
    lang_en = who.startswith("en")
    if voice is None:
        voice, emotion = YA_VOICE["en" if lang_en else who]
    form = {"text": text, "voice": voice, "format": "mp3",
            "lang": "en-US" if lang_en else "ru-RU",
            # медленное английское слово — то же самое, но ещё тише темпом
            "speed": "0.7" if who == "en_slow" else YA_SPEED}
    if emotion:
        form["emotion"] = emotion
    if os.environ.get("YANDEX_FOLDER_ID"):
        form["folderId"] = os.environ["YANDEX_FOLDER_ID"]
    # Ключа в окружении может не быть намеренно: если он лежит в API
    # credentials окружения, заголовок подставит прокси уже за пределами
    # контейнера, и сам ключ сюда не попадает. Свой заголовок в этом
    # случае не шлём, иначе спорим с прокси за одно и то же поле.
    head = {}
    if os.environ.get("YANDEX_API_KEY"):
        head["Authorization"] = "Api-Key " + os.environ["YANDEX_API_KEY"]
    req = urllib.request.Request(YA_URL, data=urllib.parse.urlencode(form).encode(),
                                 headers=head)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        # Роль поддержана не у каждого голоса, и отказ из-за неё выглядит
        # как отказ вообще. Пробуем ещё раз без роли, прежде чем сдаться.
        if e.code == 400 and emotion and b"emotion" in e.read()[:400].lower():
            return speak_yandex(text, who, tone, voice=voice, emotion=None)
        raise


ENGINES = {"openai": speak_openai, "yandex": speak_yandex}
KEY_ENV = {"openai": "OPENAI_API_KEY", "yandex": "YANDEX_API_KEY"}


def tracks():
    """Что нужно озвучить: (имя файла, текст, кто говорит, интонация).

    Кто говорит — это герой (`firefly`, `bunny`, …) или `en`/`en_slow`;
    в голос его переводит уже движок, у каждого своя таблица.

    Русские дорожки берём целиком из `script`: со временем в build_script
    добавлялись новые группы реплик (похвалы, финал, реплики карты), и
    жёсткий разбор по позициям отставал, а `ru()` складывает туда каждую
    реплику, какой бы группе она ни принадлежала.
    """
    script, *_, en_list = build_script()
    out = [(key, text, who, tone) for key, who, text, tone, _where in script]
    for key, text in en_list:
        out.append((key, text, "en", None))
        if len(text.split()) <= 3:        # слова и сочетания — ещё и медленно
            out.append((key + "-slow", text, "en_slow", None))
    return out


def opt(args, name, default):
    """Значение флага «--имя значение»; флаг последним в строке — без него."""
    i = args.index(name) + 1 if name in args else len(args)
    return args[i] if i < len(args) else default


def main():
    args = sys.argv[1:]
    todo = tracks()
    ru_engine = opt(args, "--ru", "yandex")
    en_engine = opt(args, "--en", "off")      # английский — синтез браузера
    todo = [t for t in todo if not (en_engine == "off" and t[2].startswith("en"))]
    for e in (ru_engine, en_engine):
        if e not in ENGINES and e != "off":
            sys.exit(f"движок «{e}» неизвестен, есть: off, " + ", ".join(ENGINES))

    def engine_of(who):
        return en_engine if who.startswith("en") else ru_engine

    if "--list" in args:
        total = sum(len(t) for _, t, _, _ in todo)
        print(f"дорожек {len(todo)}, знаков {total}")
        print(f"русские — {ru_engine}, английские — {en_engine}\n")
        for key, text, who, _ in todo:
            mark = "есть" if (OUT / (key + ".mp3")).exists() else "  — "
            print(f"  {mark} {key:12s} {who:8s} {text[:60]}")
        return

    if "--voices" in args:
        line = "Смотри! Мы на Драконьем Острове. Ой… а где же все?"
        engine = opt(args, "--voices", None)
        engine = engine if engine in ENGINES else ru_engine
        need_key(engine)
        samples = YA_SAMPLES if engine == "yandex" else OA_SAMPLES
        for v in samples:
            f = OUT.parent / "voice-samples" / f"{engine}-{v}.mp3"
            f.parent.mkdir(parents=True, exist_ok=True)
            try:
                f.write_bytes(ENGINES[engine](line, "firefly",
                                              "удивлённо, потом растерянно", voice=v))
                print("  образец:", f.name)
            except urllib.error.HTTPError as e:
                print(f"  {v:10s} — не вышло: {e.code} {e.read().decode()[:120]}")
        return

    for engine in {engine_of(w) for _, _, w, _ in todo}:
        need_key(engine)
    OUT.mkdir(parents=True, exist_ok=True)

    force = set(a for a in args if a.startswith(("RU-", "EN-")))
    done = skipped = 0
    for key, text, who, tone in todo:
        f = OUT / (key + ".mp3")
        if f.exists() and (not force or key not in force):
            skipped += 1
            continue
        engine = engine_of(who)
        for attempt in range(3):
            try:
                f.write_bytes(ENGINES[engine](text, who, tone))
                done += 1
                print(f"  {key:12s} {engine:6s} {who:8s} {len(text):3d} знаков")
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


def need_key(engine):
    """Чего не хватает, чтобы движок заработал.

    У Yandex ключ может лежать не в окружении, а в API credentials — тогда
    его подставляет прокси, и проверять здесь нечего. Обязателен только
    идентификатор каталога: он уходит в теле запроса, и прокси его не знает.
    """
    if engine == "yandex":
        if not os.environ.get("YANDEX_FOLDER_ID"):
            sys.exit("нет YANDEX_FOLDER_ID в окружении")
        return
    if not os.environ.get(KEY_ENV[engine]):
        sys.exit(f"нет {KEY_ENV[engine]} в окружении (движок {engine})")


if __name__ == "__main__":
    main()
