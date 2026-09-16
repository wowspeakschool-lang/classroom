#!/usr/bin/env python3
"""Новый образ учителя (он же Хранительница Слов) в стиле карты.

В уроках учитель нужен в трёх состояниях: neutral, smile, excited. Чтобы это был
один и тот же человек, а не три разных, базовый портрет генерируется один раз,
а остальные два делаются правкой базового через /v1/images/edits — как праздничный
замок из закрытого.

Запуск: python3 tools/gen_teacher.py [--final] вариант...
"""
import base64, json, os, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "teacher")
QUALITY = "medium"

STYLE = ("Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid "
         "saturated colors - violet, pink, gold, turquoise. Warm friendly lighting from the "
         "top-left. Waist-up portrait, facing the viewer, looking straight at the camera, "
         "head and shoulders centred in the frame with room around them. "
         "No text, no letters, no numbers, no signs. Transparent background.")

VARIANTS = {
    # А: современная учительница — ближе к нынешнему образу, но ярче и объёмнее
    "teacher-a-tutor": (
        "A friendly young woman English teacher for children, warm open smile, kind eyes. "
        "Wavy chestnut hair loosely tied back, a soft violet cardigan over a white blouse, "
        "small gold star earrings. She looks welcoming and cheerful, like a favourite teacher. "
        + STYLE),
    # Б: Хранительница Слов — сказочный образ из сюжета
    "teacher-b-guardian": (
        "A friendly fairy-tale Keeper of Words: a young woman with a warm gentle smile, "
        "wavy chestnut hair, wearing a flowing violet and turquoise cloak with golden trim and "
        "a delicate golden circlet with a small star. Soft golden sparkles float around her "
        "shoulders. She looks magical but kind and approachable for a child. " + STYLE),
}


def generate(key):
    body = {"model": "gpt-image-1", "prompt": VARIANTS[key], "size": "1024x1024",
            "quality": QUALITY, "background": "transparent", "output_format": "png", "n": 1}
    req = urllib.request.Request("https://api.openai.com/v1/images/generations",
        data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
                 "Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=900))
    except urllib.error.HTTPError as e:
        return key, "ОШИБКА %s: %s" % (e.code, e.read().decode()[:200])
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, key + ".png")
    open(path, "wb").write(base64.b64decode(r["data"][0]["b64_json"]))
    tok = r["usage"]["output_tokens"]
    return key, "готово (%.0f КБ, ~$%.3f)" % (os.path.getsize(path) / 1024, tok * 40 / 1e6)


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--final" in args:
        QUALITY = "high"; args.remove("--final")
    keys = args or list(VARIANTS)
    with ThreadPoolExecutor(max_workers=2) as pool:
        for k, msg in pool.map(generate, keys):
            print(k, "->", msg)


# ── Состояния лица ────────────────────────────────────────────────────────────
# Делаются правкой базового портрета, а не генерацией с нуля: иначе вместо одного
# персонажа в трёх настроениях получатся три разных человека.
KEEP = ("Keep this exact character completely unchanged: same face and features, same wavy "
        "chestnut hair, same violet and turquoise cloak with golden trim, same golden circlet "
        "with a star, same art style, same pose, same framing and scale, same lighting, "
        "same transparent background. ")

EMOTIONS = {
    "neutral": KEEP + ("Change only her expression: calm, kind and attentive, with a gentle "
                       "closed-mouth smile, looking warmly at the viewer."),
    "excited": KEEP + ("Change only her expression: delighted and excited, a big happy open "
                       "smile, bright wide eyes, eyebrows raised with joy, a few extra golden "
                       "sparkles around her."),
}


def edit_emotion(name, base="teacher-b-guardian"):
    src = os.path.join(OUT, base + ".png")
    fields = {"model": "gpt-image-1", "prompt": EMOTIONS[name], "size": "1024x1024",
              "quality": QUALITY, "background": "transparent", "input_fidelity": "high", "n": "1"}
    boundary = "----wowspeak" + base64.b16encode(os.urandom(8)).decode()
    body = b""
    for k, v in fields.items():
        body += ("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n"
                 % (boundary, k, v)).encode()
    body += ("--%s\r\nContent-Disposition: form-data; name=\"image\"; filename=\"base.png\"\r\n"
             "Content-Type: image/png\r\n\r\n" % boundary).encode()
    body += open(src, "rb").read() + ("\r\n--%s--\r\n" % boundary).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/edits", data=body,
        headers={"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
                 "Content-Type": "multipart/form-data; boundary=" + boundary})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=900))
    except urllib.error.HTTPError as e:
        return name, "ОШИБКА %s: %s" % (e.code, e.read().decode()[:200])
    path = os.path.join(OUT, "teacher-" + name + ".png")
    open(path, "wb").write(base64.b64decode(r["data"][0]["b64_json"]))
    return name, "готово (%.0f КБ)" % (os.path.getsize(path) / 1024)
