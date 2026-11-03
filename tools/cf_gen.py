"""Генерация картинок через Cloudflare Workers AI (FLUX.1 schnell).

Бесплатно 10 000 «нейронов» в сутки — это примерно 50 картинок, сброс в 00:00 UTC.
Ключ НЕ хранить в репозитории: он лежит в переменных среды окружения
(CF_TOKEN), заводится в «Изменить облачную среду» → «Переменные среды».
Домен api.cloudflare.com должен быть в разрешённых («Доступ к сети»).

Запуск:  CF_TOKEN=... python3.13 -I tools/cf_gen.py

Что умеет модель и чего не умеет (проверено 03.11.2026):
  + стиль 3D-рендера, как в курсах; фон честно белый; предметы не слипаются;
  - порядок «Row 1, left to right» НЕ соблюдает, раскладывает как хочет;
  - дублирует предметы и иногда подменяет (яблоко вышло помидором).
Отсюда: просить 4-6 предметов на лист, а не девять, и перегенерировать то,
что вышло не тем. Перегенерация бесплатна в пределах суточного лимита.
"""
import base64, json, os, sys, urllib.request

ACCOUNT = os.environ.get("CF_ACCOUNT_ID", "de106aecd4f629fa2e8c12e6184b5f4f")
TOKEN = os.environ["CF_TOKEN"]
MODEL = "@cf/black-forest-labs/flux-1-schnell"
OUT = "/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/cf_test"
os.makedirs(OUT, exist_ok=True)

STYLE = ("3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, "
         "clean studio lighting, no shadow on the background, plain flat pure white background, "
         "wide empty white gaps between the items, every item complete and not touching "
         "any other item or the edge of the image, no text, no letters, no labels, no numbers")

SHEETS = {
  "school": "A 3 by 3 grid of nine separate school objects. Row 1, left to right: a pencil, a ruler, a rubber. "
            "Row 2, left to right: a pencil case, a notebook, a school bag. "
            "Row 3, left to right: a pair of scissors, a glue stick, a set of coloured pencils. " + STYLE,
  "food":   "A 3 by 3 grid of nine separate food items. Row 1, left to right: an apple, a banana, a bunch of grapes. "
            "Row 2, left to right: a loaf of bread, a piece of cheese, an egg. "
            "Row 3, left to right: a carrot, a tomato, a glass of milk. " + STYLE,
}

url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/{MODEL}"
for name, prompt in SHEETS.items():
    body = json.dumps({"prompt": prompt, "steps": 8}).encode()
    req = urllib.request.Request(url, data=body, headers={
        "Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.loads(r.read().decode())
    except Exception as e:
        print(name, "ОШИБКА", e)
        continue
    if not data.get("success"):
        print(name, "НЕ ВЫШЛО", json.dumps(data)[:300])
        continue
    img = data["result"].get("image")
    if not img:
        print(name, "нет поля image", list(data["result"])[:5])
        continue
    raw = base64.b64decode(img)
    p = os.path.join(OUT, name + ".jpg")
    with open(p, "wb") as fh:
        fh.write(raw)
    print(name, p, len(raw))
