#!/usr/bin/env python3
"""Фигурки для одевалки Урока 4 — объёмные, в стиле всего курса.

Одевалка собирала ребёнка из семи плоских слоёв (голова, голова в кепке, торс,
торс с курткой, куртка, ноги в джинсах, ноги в шортах). Нарисовать такие слои
объёмными невозможно: генератор не сводит отдельные картинки пиксель в пиксель,
и на фигурке разъезжаются шея и пояс.

Поэтому рисуем фигурку целиком во всех восьми сочетаниях: кепка/без кепки ×
футболка/футболка с курткой × джинсы/шорты. Одна базовая генерация на пол,
остальные семь — правки базовой через /v1/images/edits с input_fidelity high:
лицо, поза и кадр остаются те же, меняется только одежда.

Цвета — наши: кепка фиолетовая, футболка жёлтая, куртка бирюзовая, джинсы синие,
кроссовки красно-оранжевые, носки фиолетовые.

Запуск:
    python3 tools/gen_avatar_figures.py --draft boy     дёшево, посмотреть состав
    python3 tools/gen_avatar_figures.py boy girl        итоговый прогон (medium)
Готовые файлы: assets/lesson-4/fig_<пол>_<кепка><куртка><шорты>.webp
Мастера храним в webp: png с картинки 1024x1536 весит 2.4 МБ, webp — 0.24 МБ,
а правки через images/edits webp принимают.
"""
import base64, io, json, os, sys, urllib.error, urllib.request

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "lesson-4")
QUALITY = "medium"
SIZE = "1024x1536"

STYLE = ("Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid "
         "saturated colors, smooth plastic-toy surfaces, warm soft lighting from the top-left. "
         "Full body from head to toe, standing straight and facing the viewer, arms relaxed "
         "down at the sides, feet together, the whole figure centred with clear empty margin "
         "above the head and below the feet so nothing is cut off. "
         "No text, no letters, no numbers. Transparent background, no shadow on the background.")

BASE = {
    "boy": ("A cheerful cartoon boy about eight years old with short brown hair and a friendly "
            "smile, wearing a bright yellow short-sleeve T-shirt, blue denim jeans and "
            "red-orange sneakers with white soles. " + STYLE),
    "girl": ("A cheerful cartoon girl about eight years old with shoulder-length brown hair and "
             "a friendly smile, wearing a bright yellow short-sleeve T-shirt, blue denim jeans "
             "and red-orange sneakers with white soles. " + STYLE),
}

KEEP = ("Keep this exact character completely unchanged: same face and expression, same eyes, "
        "same hair, same skin tone, same body and proportions, same pose, same framing, scale "
        "and position in the frame, same art style, same lighting, same transparent background. ")

CAP = ("a bright purple baseball cap on the head, worn straight with the peak forward")
JACKET = ("an open turquoise zip-up jacket over the yellow T-shirt, sleeves down the arms, "
          "the yellow T-shirt still clearly visible in the middle")
KEEP_LEGS = (" The legs stay exactly as they are: the same blue denim jeans and the same "
             "red-orange sneakers with white soles, unchanged in shape and colour.")
SHORTS = ("Change the legs only: instead of the jeans and sneakers the child wears light grey "
          "shorts to the knees and tall bright purple socks pulled up to below the knee, with "
          "no shoes at all - bare feet inside the socks. The socks are purple, not pink and not "
          "orange. Keep the head and the upper half exactly as they are.")

# Каждая правка делается из базовой картинки, а не из предыдущей правки: на цепочке
# из двух-трёх правок у ребёнка плывут кожа, глаза и цвет обуви.
# ключ — кепка/куртка/шорты, 0 или 1.
CHAIN = [
    ("100", "000", KEEP + "Add one thing only: " + CAP + "." + KEEP_LEGS),
    ("010", "000", KEEP + "Add one thing only: " + JACKET + "." + KEEP_LEGS),
    ("110", "000", KEEP + "Add two things only: " + CAP + ", and " + JACKET + "." + KEEP_LEGS),
    ("001", "000", KEEP + SHORTS),
    ("101", "000", KEEP + SHORTS + " Also add " + CAP + "."),
    ("011", "000", KEEP + SHORTS + " Also add " + JACKET + "."),
    ("111", "000", KEEP + SHORTS + " Also add " + CAP + ", and " + JACKET + "."),
]


def path_of(gender, code):
    return os.path.join(OUT, "fig_%s_%s.webp" % (gender, code))


def post(url, data, headers):
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        return json.load(urllib.request.urlopen(req, timeout=900)), None
    except urllib.error.HTTPError as e:
        return None, "ОШИБКА %s: %s" % (e.code, e.read().decode()[:300])


def save(r, path):
    os.makedirs(OUT, exist_ok=True)
    im = Image.open(io.BytesIO(base64.b64decode(r["data"][0]["b64_json"])))
    im.save(path, "WEBP", quality=92, method=6)
    tok = r.get("usage", {}).get("output_tokens", 0)
    return "%.0f КБ, ~$%.3f" % (os.path.getsize(path) / 1024, tok * 40 / 1e6)


def generate(gender):
    body = {"model": "gpt-image-1", "prompt": BASE[gender], "size": SIZE, "quality": QUALITY,
            "background": "transparent", "output_format": "png", "n": 1}
    r, err = post("https://api.openai.com/v1/images/generations", json.dumps(body).encode(),
                  {"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
                   "Content-Type": "application/json"})
    return err or save(r, path_of(gender, "000"))


def edit(gender, code, src_code, prompt):
    fields = {"model": "gpt-image-1", "prompt": prompt, "size": SIZE, "quality": QUALITY,
              "background": "transparent", "input_fidelity": "high", "n": "1"}
    boundary = "----wowspeak" + base64.b16encode(os.urandom(8)).decode()
    body = b""
    for k, v in fields.items():
        body += ("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n"
                 % (boundary, k, v)).encode()
    body += ("--%s\r\nContent-Disposition: form-data; name=\"image\"; filename=\"base.webp\"\r\n"
             "Content-Type: image/webp\r\n\r\n" % boundary).encode()
    body += open(path_of(gender, src_code), "rb").read() + ("\r\n--%s--\r\n" % boundary).encode()
    r, err = post("https://api.openai.com/v1/images/edits", body,
                  {"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
                   "Content-Type": "multipart/form-data; boundary=" + boundary})
    return err or save(r, path_of(gender, code))


def main(genders, codes=None):
    """codes=None — весь комплект; иначе перерисовываем только названные сочетания."""
    for g in genders:
        if codes is None:
            print("%s 000 (база) -> %s" % (g, generate(g)))
        elif "000" in codes:
            print("%s 000 (база) -> %s" % (g, generate(g)))
        for code, src, prompt in CHAIN:
            if codes is not None and code not in codes:
                continue
            print("%s %s (из %s) -> %s" % (g, code, src, edit(g, code, src, prompt)))


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--draft" in args:
        QUALITY = "low"; args.remove("--draft")
    codes = [a for a in args if len(a) == 3 and set(a) <= set("01")] or None
    main([a for a in args if a in BASE] or ["boy", "girl"], codes)
