"""Spotlight 9 через Cloudflare Workers AI (FLUX.1 schnell) — по картинке на слово.
python3 cf_gen.py jobs.json            jobs: {"term": "English scene description", ...}
Ключ подставляет прокси (сетевой секрет окружения для api.cloudflare.com), в скрипте заглушка.
Выход: raw/<term>.jpg (исходник 1024), out512/<term>.png (512×512, прозрачный фон).
Лимит ~70 картинок в сутки (скользящее окно); на 429 скрипт останавливается."""
import base64, json, os, sys, urllib.request, urllib.error, io
from PIL import Image
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import lib
from lib import fname, make_soft_transparent, to_square
lib.BG_MIN, lib.BG_GREY, lib.KEEP_SOFT = 246, 10, True
ACCOUNT = os.environ.get("CF_ACCOUNT_ID", "de106aecd4f629fa2e8c12e6184b5f4f")
MODEL = "@cf/black-forest-labs/flux-1-schnell"
URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/{MODEL}"
STYLE = ("Hand-drawn children's storybook illustration, bold dark brown outlines of even thickness, "
 "rich saturated colours with soft shading and volume, hand-drawn textures, friendly rounded cartoon shapes, warm palette. "
 "Not flat vector, not clip-art, not 3D render, not photo. ")
RULES = (" Single centred illustration on a plain pure white background, no ground, no shadow on the background, "
 "wide white margin on every side, nothing touches the edges. No text, no letters, no words, no captions, no logos, no frame. "
 "Child-friendly: covered clothing, normal anatomy with five fingers, no weapons, no alcohol, no tears.")
here = os.path.dirname(os.path.abspath(__file__))
jobs = json.load(open(sys.argv[1]))
os.makedirs(f'{here}/raw', exist_ok=True); os.makedirs(f'{here}/out512', exist_ok=True)
for term, desc in jobs.items():
    stem = fname(term)[:-4]
    if os.path.exists(f'{here}/raw/{stem}.jpg'):
        print('уже есть', term); continue
    body = json.dumps({"prompt": STYLE + desc + RULES, "steps": 8}).encode()
    req = urllib.request.Request(URL, data=body, headers={"Authorization": "Bearer proxy-injected", "Content-Type": "application/json"})
    try:
        d = json.load(urllib.request.urlopen(req, timeout=180))
    except urllib.error.HTTPError as e:
        print('ОШИБКА', term, e.code, e.read()[:300].decode('utf-8', 'replace'))
        if e.code == 429: break
        continue
    raw = base64.b64decode(d["result"]["image"])
    open(f'{here}/raw/{stem}.jpg', 'wb').write(raw)
    im = make_soft_transparent(Image.open(io.BytesIO(raw)))
    bb = im.getchannel('A').getbbox()
    to_square(im.crop(bb), size=512, pad=10).save(f'{here}/out512/{stem}.png')
    print('ok', term)
