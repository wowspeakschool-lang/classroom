#!/usr/bin/env python3
"""Рисует картинку ключика из той же векторной фигуры, что на карте.

На сюжетном экране «ты получил ключик» вместо картинки стояло эмодзи 🔑.
Генерировать ключик отдельно не стали: на карте он уже нарисован, и ребёнок
должен узнать тот же самый предмет. Берём геометрию из map.html, увеличиваем
и добавляем мягкое золотое свечение, чтобы рядом с объёмными предметами рюкзака
он не выглядел плоской иконкой.

Запуск: python3 tools/render_key_svg.py   (нужен playwright)
Результат: assets/items/key.png
"""
import base64, os, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "items", "key.png")
W, H = 900, 520

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 90 52" width="%d" height="%d">
  <defs>
    <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%%" stop-color="#ffe6a3"/>
      <stop offset="45%%" stop-color="#f0b63a"/>
      <stop offset="100%%" stop-color="#c8871a"/>
    </linearGradient>
    <filter id="glow" x="-40%%" y="-40%%" width="180%%" height="180%%">
      <feDropShadow dx="0" dy="1.2" stdDeviation="1.6" flood-color="#8a5a00" flood-opacity=".35"/>
      <feDropShadow dx="0" dy="0" stdDeviation="3.4" flood-color="#ffd978" flood-opacity=".55"/>
    </filter>
  </defs>
  <g filter="url(#glow)" transform="translate(8 6) rotate(-14 37 20)">
    <rect x="14" y="17" width="44" height="9" rx="4.5" fill="url(#gold)"/>
    <rect x="19" y="23.5" width="7.2" height="11" rx="3" fill="url(#gold)"/>
    <rect x="31" y="23.5" width="7.2" height="9" rx="3" fill="url(#gold)"/>
    <circle cx="66" cy="21.5" r="12" fill="none" stroke="url(#gold)" stroke-width="6.2"/>
    <rect x="16" y="18.4" width="38" height="2.6" rx="1.3" fill="#fff3cf" opacity=".75"/>
    <path d="M58 12.5 a12 12 0 0 1 12 -3" fill="none" stroke="#fff3cf" stroke-width="2.2"
          stroke-linecap="round" opacity=".7"/>
  </g>
  <g fill="#ffe9ad">
    <circle cx="12" cy="12" r="2.2"/><circle cx="80" cy="40" r="1.8"/><circle cx="74" cy="8" r="1.4"/>
  </g>
</svg>''' % (W, H)

PAGE = '''<!doctype html><meta charset="utf-8">
<style>html,body{margin:0;background:transparent}</style>%s''' % SVG


def main():
    node = '''
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport:{width:%d,height:%d}, deviceScaleFactor:1 });
  await p.goto('file://' + process.argv[2]);
  await p.screenshot({ path: process.argv[3], omitBackground: true });
  await b.close();
})();
''' % (W, H)
    with tempfile.TemporaryDirectory() as tmp:
        page = os.path.join(tmp, "key.html")
        script = os.path.join(tmp, "shot.js")
        open(page, "w", encoding="utf-8").write(PAGE)
        open(script, "w", encoding="utf-8").write(node)
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        subprocess.run(["node", script, page, OUT], check=True)
    print("готово: %s (%.0f КБ)" % (OUT, os.path.getsize(OUT) / 1024))


if __name__ == "__main__":
    main()
