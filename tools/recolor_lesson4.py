#!/usr/bin/env python3
"""Перекрашивает одежду на фигурке Урока 4 под наш комплект.

Картинки для «собери аватара» пришли из другого набора: кепка там красная,
куртка салатовая, а по всему курсу кепка фиолетовая, куртка бирюзовая. Ребёнок
запоминает слово вместе с картинкой, и на финальном уроке вещь должна выглядеть
так же, как в первых трёх.

Красим сдвигом тона: берём только пиксели нужного оттенка, насыщенность
и светлоту оставляем как есть, поэтому блики и тени не плывут. Скрипт
переприменяемый: после первого прогона пиксели уходят из исходного диапазона
и второй прогон ничего не находит.

Пересохраняем без потерь: при лоссовом webp на границе перекрашенного пятна
каждый раз появляются новые пиксели прежнего оттенка, и повторный прогон
подкрашивал бы их снова и снова. Картинки плоские, без потерь они не тяжелее.

Кроссовки не трогаем: они того же синего, что и джинсы, и отделить их можно
только маской по месту — не стоит того.

Запуск: python3 tools/recolor_lesson4.py [--preview]
"""
import base64, colorsys, io, os, re, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSON = os.path.join(ROOT, "lessons", "wowspeak-mini", "lesson-4.html")

# ключ: (нижняя граница тона, верхняя граница, целевой тон, минимальная насыщенность)
# тон в градусах; диапазон может проходить через 0 (красный)
JOBS = {
    "z_head_cap":           [(345, 15, 272, 0.62), (95, 165, 180, 0.25)],
    "z_head_nocap":         [(95, 165, 180, 0.25)],   # воротник куртки виден и без кепки
    "z_jacket":             [(95, 165, 180, 0.25)],   # салатовая куртка → бирюзовая
    "z_torso_tshirt_jacket":[(95, 165, 180, 0.25)],
    "ava_boy":              [(95, 165, 180, 0.25)],
}

DECL = r'(\b%s\s*:\s*)"data:image/[a-z]+;base64,([^"]+)"'


def in_range(deg, lo, hi):
    return lo <= deg <= hi if lo <= hi else (deg >= lo or deg <= hi)


def recolor(im, jobs):
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    touched = 0
    for x in range(w):
        for y in range(h):
            r, g, b, a = px[x, y]
            if a < 8:
                continue
            hh, ss, vv = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            for lo, hi, target, minsat in jobs:
                if ss >= minsat and in_range(hh * 360, lo, hi):
                    nr, ng, nb = colorsys.hsv_to_rgb(target / 360, ss, vv)
                    px[x, y] = (int(nr * 255 + .5), int(ng * 255 + .5), int(nb * 255 + .5), a)
                    touched += 1
                    break
    return im, touched


def main(preview=False):
    s = open(LESSON, encoding="utf-8").read()
    for key, jobs in JOBS.items():
        m = re.search(DECL % re.escape(key), s)
        if not m:
            print("нет ключа %s — пропускаю" % key)
            continue
        im = Image.open(io.BytesIO(base64.b64decode(m.group(2))))
        out, touched = recolor(im, jobs)
        if preview:
            os.makedirs("/tmp/recolor", exist_ok=True)
            bg = Image.new("RGB", out.size, (255, 255, 255))
            bg.paste(out, (0, 0), out)
            bg.save("/tmp/recolor/%s.png" % key)
        buf = io.BytesIO()
        out.save(buf, "WEBP", lossless=True, method=6)
        data = "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()
        s = re.sub(DECL % re.escape(key), lambda mm: mm.group(1) + '"' + data + '"', s, count=1)
        print("%s: перекрашено %d пикселей" % (key, touched))
    if preview:
        print("превью в /tmp/recolor/")
        return
    open(LESSON, "w", encoding="utf-8").write(s)
    print("урок 4: %.1f МБ" % (os.path.getsize(LESSON) / 1048576))


if __name__ == "__main__":
    main("--preview" in sys.argv)
