#!/usr/bin/env python3
"""Озвучка текстов GG1, которых нет в выгрузке, — Яндекс SpeechKit, голос john.

Английских женских голосов у Яндекса нет (решение Анны 19.10.2026: рассказчиков
там, где можно, делаем мальчиками). Файлы → media/gg1/audio/<имя>.mp3, отдаются
с classroom.wowteach.ru, как картинки. Имя файла — как у остальных медиа курса:
курс_юнит_урок_блок (блок как в редакторе).

Доступ к Яндексу — настройка окружения: хост tts.api.cloud.yandex.net в Network
access и ключ в API credentials (заголовок Authorization, префикс Api-Key);
каталог — YANDEX_FOLDER_ID. Подробно — CLAUDE.md, раздел «Озвучка» лид-магнита 4–6.

  python3 tools/gg1_tts.py --list     что будет записано
  python3 tools/gg1_tts.py            записать недостающее
  python3 tools/gg1_tts.py --force gg1_u7_test_b12
"""
import argparse, base64, json, os, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "media", "gg1", "audio")
YA_URL = "https://tts.api.cloud.yandex.net/tts/v3/utteranceSynthesis"
VOICE, SPEED = "john", 0.9          # чуть медленнее обычного: читают дети 9–11 лет

TRACKS = {
    # Unit 1, Homework 5, блок 2 — чтение (ТЕКСТ МОЙ)
    "gg1_u1_hw5_b2": (
        "Simon. Hi. My name's Simon. I'm 12 and I'm British. My brother is 9. My dad is "
        "Spanish. Ellie is my aunt. She's Spanish too. Ben is my friend. Sweep is a dog. "
        "He's our dog! "
        "Nick. Hello! I'm Nick. I'm British. I'm at a party today. It's my cousin's birthday. "
        "My mum and dad are at the party too. "
        "Ben. Hi! I'm Ben. My mother is Italian and my father is British. We aren't at school "
        "today. My granny and my grandad are in the park and my sister and my mother are in "
        "the garden."),
    # Unit 3, Homework 6, блок 2 — рассказ Дэнни о доме (ТЕКСТ МОЙ, под блоки 3–5)
    "gg1_u3_hw6_b2": (
        "Hi, I'm Danny. This is my new house. It's white and it's got a red door. It's got two "
        "floors and a big garden with an apple tree. Downstairs there's a kitchen, a living room "
        "and a bathroom. Upstairs there are three bedrooms. So there are six rooms in my house! "
        "My bedroom is small, but it's cool. There's a bed, a desk and a computer. There isn't a "
        "TV in my bedroom. The TV is in the living room."),
    # Unit 7, Test, блок 12 — письмо Макса (ТЕКСТ МОЙ)
    "gg1_u7_test_b12": (
        "Hi Oliver, How are you? I'm fine. I have great news! We have a new pet. It's a small "
        "rabbit and her name is Coco. She is white and grey and she is very cute. Coco doesn't "
        "eat meat or fish. She eats leaves and vegetables. She drinks about one litre of water "
        "in a week. Every day my brother walks Coco in the garden. She loves it! I wanted a cat "
        "too, but we don't have one because my mum doesn't like cats. Write soon! Max."),
    # Unit 8, Test, блок 12 — рассказ Лео (ТЕКСТ МОЙ)
    "gg1_u8_test_b12": (
        "Hi! I'm Leo and I love sports! In summer I go swimming every day, and in winter I go "
        "ice-skating with my brother. I go to bed at half past nine and I get up at seven "
        "o'clock. I drink two litres of water a day. I eat a lot of fruit. Apples and bananas "
        "are my favourite. I brush my teeth two times a day, in the morning and in the evening. "
        "I've got a lot of friends, and we often play volleyball in the park at the weekend."),
    # Final Test, блок 2 — Listening Part 1, под метки блока 3 (ТЕКСТ МОЙ)
    "gg1_ft_test_b2": (
        "Listen and put the things in the right places. "
        "One. Put the radio on the bookcase. "
        "Two. Put the ball on the floor, next to the table. "
        "Three. Put the kite on the rug. "
        "Four. Put the clock on the cupboard. "
        "Five. Put the robot on the table. "
        "Six. Put the bag on the yellow armchair."),
    # Final Test, блок 6 — Listening Part 3, под вопросы блока 7 (ТЕКСТ МОЙ)
    "gg1_ft_test_b6": (
        "Listen and choose the right answer. "
        "One. What's Pat doing? Pat isn't reading a book and she isn't playing football. "
        "She's in the pool. She's swimming. "
        "Two. Which is May? May hasn't got short hair and she hasn't got glasses. "
        "She's the girl with long hair. "
        "Three. Which is Nick's favourite ice-cream? Nick doesn't like lemon ice-cream and he "
        "doesn't like strawberry. His favourite is chocolate. "
        "Four. What's Ben doing? Ben has got a kite. He's in the park and he's flying his kite. "
        "Five. Where's Kim's doll? It isn't on the bed and it isn't under the table. "
        "Kim's doll is in the box. "
        "Six. What's Dad doing? Dad isn't sleeping and he isn't washing the car. "
        "He's in the kitchen. He's cooking dinner."),
}


def speak(text):
    body = json.dumps({"text": text, "hints": [{"voice": VOICE}, {"speed": SPEED}],
                       "outputAudioSpec": {"containerAudio": {"containerAudioType": "MP3"}}}).encode()
    head = {"Content-Type": "application/json"}
    if os.environ.get("YANDEX_FOLDER_ID"):
        head["x-folder-id"] = os.environ["YANDEX_FOLDER_ID"]
    # ключа в окружении может не быть намеренно: его подставляет прокси
    if os.environ.get("YANDEX_API_KEY"):
        head["Authorization"] = "Api-Key " + os.environ["YANDEX_API_KEY"]
    req = urllib.request.Request(YA_URL, data=body, headers=head)
    with urllib.request.urlopen(req, timeout=180) as r:
        raw = r.read().decode()
    audio = b""
    for line in raw.splitlines():
        if line.strip():
            res = json.loads(line).get("result") or {}
            audio += base64.b64decode((res.get("audioChunk") or {}).get("data", ""))
    if not audio:
        sys.exit("Yandex вернул ответ без звука: " + raw[:200])
    return audio


def chunks(text, limit=230):
    """Яндекс v3 принимает не больше ~250 знаков за запрос: режем по предложениям."""
    import re
    parts, cur = [], ""
    for sent in re.split(r"(?<=[.!?])\s+", text.strip()):
        if cur and len(cur) + 1 + len(sent) > limit:
            parts.append(cur)
            cur = sent
        else:
            cur = (cur + " " + sent).strip()
    if cur:
        parts.append(cur)
    return parts


def speak_long(text, pause=0.5):
    """Куски по отдельности, склейка ffmpeg с паузой между кусками."""
    import subprocess, tempfile
    with tempfile.TemporaryDirectory() as tmp:
        files = []
        for i, part in enumerate(chunks(text)):
            f = os.path.join(tmp, f"{i:02d}.mp3")
            with open(f, "wb") as fh:
                fh.write(speak(part))
            files.append(f)
        silence = os.path.join(tmp, "pause.mp3")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "lavfi", "-i",
                        "anullsrc=r=48000:cl=mono", "-t", str(pause), "-q:a", "4", silence], check=True)
        lst = os.path.join(tmp, "list.txt")
        with open(lst, "w") as fh:
            for k, f in enumerate(files):
                if k:
                    fh.write(f"file '{silence}'\n")
                fh.write(f"file '{f}'\n")
        out = os.path.join(tmp, "out.mp3")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                        "-ar", "48000", "-ac", "1", "-b:a", "96k", out], check=True)
        return open(out, "rb").read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--force", nargs="*", default=[])
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    for name, text in TRACKS.items():
        path = os.path.join(OUT, name + ".mp3")
        if args.list:
            print(f"{name}: {len(text)} знаков, {'есть' if os.path.exists(path) else 'нет'}")
            continue
        if os.path.exists(path) and name not in args.force:
            continue
        data = speak_long(text)
        with open(path, "wb") as f:
            f.write(data)
        print(os.path.relpath(path, ROOT), len(data) // 1024, "КБ")


if __name__ == "__main__":
    main()
