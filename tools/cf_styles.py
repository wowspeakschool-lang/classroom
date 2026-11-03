import base64, json, os, urllib.request, concurrent.futures as cf

ACCOUNT = "de106aecd4f629fa2e8c12e6184b5f4f"
TOKEN = os.environ["CF_TOKEN"]
MODEL = "@cf/black-forest-labs/flux-1-schnell"
OUT = "/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/cf_styles"
os.makedirs(OUT, exist_ok=True)

BASE = ("plain flat pure white background, no shadow on the background, the object centred "
        "with empty margin on every side, complete and not touching the edge, "
        "no text, no letters, no labels, no numbers")

SUBJ = "a child's school backpack, blue with a yellow zip"

STYLES = {
  "1_3d_render":   "3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting",
  "2_flat_vector": "flat vector illustration, bold clean outlines, simple geometric shapes, limited bright palette, no gradients",
  "3_watercolour": "soft watercolour children's book illustration, gentle washes, visible paper texture in the object only",
  "4_cartoon_2d":  "hand-drawn 2D cartoon, thick black outlines, flat cel-shaded colours, playful style for very young children",
  "5_photo":       "clean studio product photograph, sharp focus, natural colours, soft even lighting",
  "6_pencil":      "coloured pencil drawing, light sketchy outlines, gentle shading, storybook feel",
}

url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/{MODEL}"


def one(item):
    name, style = item
    prompt = f"{SUBJ}. {style}. {BASE}"
    body = json.dumps({"prompt": prompt, "steps": 8}).encode()
    req = urllib.request.Request(url, data=body, headers={
        "Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            data = json.loads(r.read().decode())
        img = data["result"]["image"]
        p = os.path.join(OUT, name + ".jpg")
        with open(p, "wb") as fh:
            fh.write(base64.b64decode(img))
        return name + " ok"
    except Exception as e:
        return name + " ОШИБКА " + str(e)


with cf.ThreadPoolExecutor(max_workers=3) as ex:
    for r in ex.map(one, STYLES.items()):
        print(r)
