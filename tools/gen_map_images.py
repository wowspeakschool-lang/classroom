#!/usr/bin/env python3
"""Генерация картинок карты «Волшебная страна» через OpenAI Images API.

Промпты — из docs/WowSpeak_карта_ТЗ.md §3. Блок стиля во всех островах
дословно одинаковый: стиль утверждён Анной на пробе острова 1, менять нельзя.
Правки допустимы только в описании содержания сцены.

Запуск:  OPENAI_API_KEY=... python3 tools/gen_map_images.py [--draft|--final] [ключ ...]
Без аргументов — генерирует всё.

Про деньги. Картинка 1536x1024 стоит примерно: low $0.016, medium $0.063, high $0.25.
Порядок работы: гоняем промпт в --draft (low), пока содержание не сойдётся — пропавшая
юбка или буквы на компасе видны и в черновике, — и только потом один прогон в medium.
На карте остров показывается шириной около 430 px, там medium от high неотличим;
high осмыслен только если картинка понадобится крупно.
"""
import base64, json, os, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

# Утверждённый стиль островов — не редактировать.
ISLAND_STYLE = ("Same floating chunk of earth with grass on top and rock underneath: "
    "the thick rocky underside is clearly visible below the grass, chunky jagged rock "
    "tapering downwards to a point, the whole island floating in mid-air. "
    "Same three-quarter top-down view and top-left lighting. "
    "Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, "
    "vivid saturated colors - violet, pink, gold, turquoise. ")
NO_TEXT = "No text, no letters, no signs, no numbers, no labels. "

JOBS = {
    "island-1-fair": dict(size="1536x1024", transparent=True, prompt=(
        "A small floating fantasy market island: striped awnings, wooden stalls, bunting flags. "
        "A washing line strung between two wooden poles crosses the island, and colourful "
        "triangular bunting flags are strung beside it. Four garments hang from the line in a "
        "row, left to right: first a purple baseball cap, second a yellow T-shirt, third blue "
        "jeans, and fourth, at the right-hand end of the line, a pink skirt - a short flared "
        "skirt shaped like a bell, narrow at the waist and wide at the hem, with no legs, "
        "clearly not trousers. Four garments hanging, not three. "
        "The stalls display only clothing - folded shirts, stacked hats, rolls of colourful fabric. "
        "Absolutely no food on the stalls: no fruit, no oranges, no vegetables, no jars, no barrels. "
        "The island sits on a chunk of earth, grass on top, rough rock underneath, floating in the air. "
        "Three-quarter top-down view, lighting from the top-left. " + ISLAND_STYLE
        + NO_TEXT + "No people. Transparent background.")),

    "island-2-mirrors": dict(size="1536x1024", transparent=True, prompt=(
        "A small floating fantasy island with tall ornate standing mirrors in golden frames "
        "among soft grass and glowing crystals, sparkling reflections. " + ISLAND_STYLE
        + NO_TEXT + "No people. Transparent background.")),

    "island-3-friends": dict(size="1536x1024", transparent=True, prompt=(
        "A small floating fantasy island: a cosy green hill with a treehouse, two small round huts, "
        "a picnic blanket and a flower meadow. Deep saturated colours: rich green grass, "
        "a bright pink-and-white checked blanket, a lush violet tree canopy, glossy toy-like "
        "surfaces with crisp highlights - not pale, not washed out, not painterly. " + ISLAND_STYLE
        + NO_TEXT + "No people. Transparent background.")),

    "island-4-castle-closed": dict(size="1536x1024", transparent=True, prompt=(
        "A small floating fantasy castle island: a fairytale castle with pink and violet towers "
        "and golden roofs, tall closed wooden gates, a winding path leading up to them. "
        + ISLAND_STYLE + NO_TEXT + "No people, no dragon. Transparent background.")),

    "island-4-castle-festive": dict(size="1536x1024", transparent=True, prompt=(
        "The same fairytale castle island, now celebrating: the tall gates are wide open with warm "
        "golden light pouring out, festive garlands and glowing lanterns strung between the towers, "
        "confetti and sparkles in the air, small fireworks above the roofs. Same pink and violet "
        "towers with golden roofs, same floating rock island with grass underneath, same "
        "three-quarter top-down view, same top-left lighting, same scale as the closed castle. "
        "Bright 3D rendered cartoon style, Pixar-like, glossy soft shapes, vivid saturated colors. "
        + NO_TEXT + "No characters, no dragon. Transparent background.")),

    # Отдельное небо для широких экранов. Вертикальное при растягивании на ноутбук
    # мылится: у него всего 1024 px по ширине.
    "map-background-wide": dict(size="1536x1024", transparent=False, prompt=(
        "Children's storybook background, empty scene with no objects: a calm turquoise magical "
        "sea along the lower part of the frame with soft foam swirls, a wide sky above with "
        "scattered fluffy white and lilac clouds, tiny sparkles and stars, warm golden light "
        "from the top. Bright 3D rendered cartoon style, Pixar-like, soft glossy shapes, vivid "
        "saturated colors - turquoise, violet, pink, gold. Lots of open empty space across the "
        "middle of the composition. " + NO_TEXT
        + "No characters, no buildings, no islands. Horizontal, aspect ratio 3:2.")),

    "map-background": dict(size="1024x1536", transparent=False, prompt=(
        "Children's storybook background, empty scene with no objects: a calm turquoise magical sea "
        "with soft foam swirls, scattered fluffy white clouds, tiny sparkles and stars, warm golden "
        "light from the top. Bright 3D rendered cartoon style, Pixar-like, soft glossy shapes, "
        "vivid saturated colors - turquoise, violet, pink, gold. Lots of open empty space in the "
        "middle of the composition. " + NO_TEXT
        + "No characters, no buildings, no islands. Vertical, aspect ratio 2:3.")),

    "parchment-map": dict(size="1024x1024", transparent=False, prompt=(
        "An old treasure map on warm parchment, drawn in a soft children's cartoon style: "
        "a turquoise sea containing exactly four islands and nothing else - no extra islets, no "
        "sandbanks, no rocks, four landmasses in total, counted as one, two, three, four. "
        "A single dotted trail links them in one chain: it starts at the first island, passes "
        "through the second and the third and ends at the fourth, and every island is touched "
        "by the trail. The fourth and last island carries a castle. "
        "a compass rose in one corner, tiny waves and a whale spout. The compass rose is drawn as "
        "a plain eight-pointed star with no letters and no initials on or around it. "
        "Warm cream and beige parchment with soft brown ink and gentle watercolour tints of "
        "turquoise, pink and gold. Flat top-down illustration, even lighting, no drop shadows. "
        "The illustration bleeds off all four edges of the square: the sea reaches every edge, "
        "with no border, no frame, no outline and no empty margin around the drawing. "
        + NO_TEXT + "No writing of any kind anywhere in the image, not even on the compass. "
        "Square, aspect ratio 1:1.")),
}

QUALITY = "medium"   # переключается флагами --draft / --final
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "map")


def generate(key):
    job = JOBS[key]
    body = {"model": "gpt-image-1", "prompt": job["prompt"], "size": job["size"],
            "quality": QUALITY, "output_format": "png", "n": 1}
    if job["transparent"]:
        body["background"] = "transparent"
    req = urllib.request.Request("https://api.openai.com/v1/images/generations",
        data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
                 "Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=900))
    except urllib.error.HTTPError as e:
        return key, "ОШИБКА HTTP %s: %s" % (e.code, e.read().decode()[:300])
    path = os.path.join(OUT_DIR, key + ".png")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(path, "wb") as f:
        f.write(base64.b64decode(r["data"][0]["b64_json"]))
    return key, "готово: %s (%.1f МБ)" % (path, os.path.getsize(path) / 1e6)


FESTIVE_EDIT_PROMPT = (
    "Keep this exact castle island unchanged in shape, size, position, colours and art style - "
    "the same pink and violet towers, the same grass, the same jagged rocky underside, the same "
    "three-quarter top-down view and top-left lighting, the same glossy 3D cartoon look. "
    "Only add a celebration: open the tall wooden gates wide so warm golden light pours out of the "
    "doorway, string festive garlands and glowing lanterns between the towers, and add confetti, "
    "sparkles and small fireworks in the air above the roofs. "
    + NO_TEXT + "No characters, no dragon, no people. Keep the background fully transparent.")


def edit_festive():
    """Праздничный замок = закрытый замок + правка, чтобы остров совпал один в один."""
    src = os.path.join(OUT_DIR, "island-4-castle-closed.png")
    fields = {"model": "gpt-image-1", "prompt": FESTIVE_EDIT_PROMPT, "size": "1536x1024",
              "quality": "high", "background": "transparent", "input_fidelity": "high", "n": "1"}
    boundary = "----wowspeak" + base64.b16encode(os.urandom(8)).decode()
    body = b""
    for k, v in fields.items():
        body += ("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n"
                 % (boundary, k, v)).encode()
    body += ("--%s\r\nContent-Disposition: form-data; name=\"image\"; filename=\"castle.png\"\r\n"
             "Content-Type: image/png\r\n\r\n" % boundary).encode()
    body += open(src, "rb").read() + ("\r\n--%s--\r\n" % boundary).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/edits", data=body,
        headers={"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
                 "Content-Type": "multipart/form-data; boundary=" + boundary})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=900))
    except urllib.error.HTTPError as e:
        return "island-4-castle-festive", "ОШИБКА HTTP %s: %s" % (e.code, e.read().decode()[:300])
    path = os.path.join(OUT_DIR, "island-4-castle-festive.png")
    with open(path, "wb") as f:
        f.write(base64.b64decode(r["data"][0]["b64_json"]))
    return "island-4-castle-festive", "готово: %s (%.1f МБ)" % (path, os.path.getsize(path) / 1e6)


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--draft" in args:
        QUALITY = "low"
        args.remove("--draft")
    elif "--final" in args:
        QUALITY = "high"
        args.remove("--final")
    print("качество: %s" % QUALITY)
    keys = args or list(JOBS)
    if "festive" in keys:
        print(*edit_festive()); sys.exit()
    bad = [k for k in keys if k not in JOBS]
    if bad:
        sys.exit("неизвестные ключи: %s; доступны: %s" % (bad, list(JOBS)))
    with ThreadPoolExecutor(max_workers=3) as pool:
        for key, msg in pool.map(generate, keys):
            print(key, "->", msg)
