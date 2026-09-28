#!/usr/bin/env python3
"""Режет один длинный файл озвучки на отдельные дорожки.

    python3 tools/split_audio_4-6.py запись.mp3 "Урок 1. Солнечная Полянка"
    python3 tools/split_audio_4-6.py запись.mp3 --список

Сервисы озвучки отдают один файл на весь вставленный текст. Скачивать 120
дорожек по одной — час кликанья, поэтому текст для сервиса
(`docs/WowSpeak_озвучка_4-6_для_сервиса.md`) собран блоками по разделам, и
между репликами стоит пауза в две секунды. По ней и режем.

Имена берём не на глаз, а из того же списка, что и сам урок: раздел задаёт,
какие номера дорожек в нём лежат и в каком порядке. Если кусков вышло не
столько, сколько реплик, скрипт не раскладывает ничего — показывает, где
разошлось, и предлагает подвинуть порог тишины.
"""

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_kids46 import build_script, AUDIO_DIR

# Готовые дорожки кладём полегче: файл урока их вшивает целиком, и каждый
# лишний килобайт звука превращается в полтора килобайта страницы.
BITRATE = "32k"
RATE = "24000"
SILENCE_DB = "-38dB"      # тише этого считаем тишиной
SILENCE_MIN = "1.2"       # секунд подряд — значит, граница между репликами


def ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return "ffmpeg"


def sections():
    """Разделы и номера дорожек в них — из того же списка, что и урок."""
    script, *_ = build_script()
    out = {}
    for key, _voice, _text, _tone, where in script:
        out.setdefault(where, []).append(key)
    return out


def silences(path):
    """Где в файле тишина: (начало, конец) в секундах."""
    p = subprocess.run(
        [ffmpeg(), "-i", str(path), "-af",
         f"silencedetect=noise={SILENCE_DB}:d={SILENCE_MIN}", "-f", "null", "-"],
        capture_output=True, text=True)
    starts, ends, out = [], [], []
    for line in p.stderr.splitlines():
        if "silence_start:" in line:
            starts.append(float(line.split("silence_start:")[1].strip()))
        if "silence_end:" in line:
            ends.append(float(line.split("silence_end:")[1].split("|")[0].strip()))
    for i, s in enumerate(starts):
        if i < len(ends):
            out.append((s, ends[i]))
    return out


def duration(path):
    p = subprocess.run([ffmpeg(), "-i", str(path), "-f", "null", "-"],
                       capture_output=True, text=True)
    for line in p.stderr.splitlines():
        if "Duration:" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    sys.exit("не удалось прочитать длину файла")


def main():
    args = sys.argv[1:]
    secs = sections()
    if not args or "--список" in args or "--list" in args:
        print("разделы и сколько в них дорожек:")
        for w, keys in secs.items():
            print(f"  {len(keys):3d}  {w}   ({keys[0]}…{keys[-1]})")
        print("\nвызов: python3 tools/split_audio_4-6.py файл.mp3 \"название раздела\"")
        return

    src = Path(args[0])
    if not src.exists():
        sys.exit(f"нет файла {src}")
    if len(args) < 2:
        sys.exit("вторым аргументом — название раздела, см. --список")
    name = args[1]
    keys = next((v for k, v in secs.items() if k.startswith(name) or name in k), None)
    if not keys:
        sys.exit(f"раздел «{name}» не найден, см. --список")

    total = duration(src)
    gaps = [g for g in silences(src) if g[0] > 0.3 and g[1] < total - 0.3]
    print(f"файл {src.name}: {total:.1f} с, тишин внутри {len(gaps)}, "
          f"дорожек в разделе {len(keys)}")

    if len(gaps) != len(keys) - 1:
        print("\nНе сходится. Куски по границам тишины:")
        cuts = [0.0] + [(a + b) / 2 for a, b in gaps] + [total]
        for i in range(len(cuts) - 1):
            print(f"   {i+1:3d}  {cuts[i]:7.2f} – {cuts[i+1]:7.2f}")
        print("\nНичего не разложено. Если пауз вышло больше — они внутри реплик:"
              f"\nподнимите SILENCE_MIN (сейчас {SILENCE_MIN} с). Если меньше —"
              f"\nопустите SILENCE_DB (сейчас {SILENCE_DB}) или удлините паузу"
              "\nмежду репликами в сервисе.")
        return

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    cuts = [0.0] + [(a + b) / 2 for a, b in gaps] + [total]
    for i, key in enumerate(keys):
        start, end = cuts[i], cuts[i + 1]
        dst = AUDIO_DIR / f"{key}.mp3"
        subprocess.run(
            [ffmpeg(), "-y", "-i", str(src), "-ss", f"{start:.3f}",
             "-to", f"{end:.3f}", "-ac", "1", "-ar", RATE, "-b:a", BITRATE,
             # обрезаем тишину по краям куска, чтобы реплика начиналась сразу
             "-af", "silenceremove=start_periods=1:start_silence=0.1:"
                    "start_threshold=-40dB,areverse,"
                    "silenceremove=start_periods=1:start_silence=0.1:"
                    "start_threshold=-40dB,areverse",
             str(dst)], capture_output=True)
        print(f"  {key}.mp3  {end - start:5.2f} с  {dst.stat().st_size // 1024} КБ")
    print(f"\nразложено {len(keys)} дорожек в {AUDIO_DIR}")
    print("теперь пересоберите: python3 tools/build_kids46.py")


if __name__ == "__main__":
    main()
