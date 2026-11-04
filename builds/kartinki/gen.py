"""Генерация картинок через Cloudflare Workers AI. CF_TOKEN — из среды.
Запуск: CF_TOKEN=... python3.13 -I gen.py задания.json папка"""
import base64, json, os, sys, urllib.request, urllib.error
ACCOUNT = os.environ.get("CF_ACCOUNT_ID", "de106aecd4f629fa2e8c12e6184b5f4f")
TOKEN = os.environ["CF_TOKEN"]
MODEL = "@cf/black-forest-labs/flux-1-schnell"
jobs = json.load(open(sys.argv[1]))
out = sys.argv[2]; os.makedirs(out, exist_ok=True)
url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/{MODEL}"
for name, prompt in jobs.items():
    dst = os.path.join(out, name + ".png")
    if os.path.exists(dst):
        print("уже есть", name); continue
    req = urllib.request.Request(url, data=json.dumps({"prompt": prompt, "steps": 8}).encode(),
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"})
    try:
        d = json.load(urllib.request.urlopen(req, timeout=180))
        img = d["result"]["image"]
        open(dst, "wb").write(base64.b64decode(img))
        print("ok", name)
    except urllib.error.HTTPError as e:
        body = e.read()[:300].decode("utf-8", "replace")
        print("ОШИБКА", name, e.code, body)
        if e.code == 429: break
    except Exception as e:
        print("ОШИБКА", name, type(e).__name__, str(e)[:200])
