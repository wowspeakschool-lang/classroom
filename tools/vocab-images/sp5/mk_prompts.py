"""Промпты листов Spotlight 4 → docs/Тренажёр_Spotlight4_промпты.md (стиль как у Prepare)."""
from sheets import S
STYLE = ("Стиль: hand-drawn children's storybook illustration, bold dark brown outlines of even thickness, "
 "rich saturated colours with soft shading and volume, hand-drawn textures, friendly rounded shapes. "
 "NOT flat vector icons, NOT clip-art. Чистый белый фон, строгая сетка, широкие белые промежутки между "
 "картинками и рядами, ничего не касается соседних клеток. Под каждой картинкой подпись — английское слово, "
 "чёрный sans-serif по центру, с отступом от рисунка. Никакого текста внутри рисунков, без рамок. "
 "Всё мягко, без крови, ран и слёз. Для детей: без сигарет и алкоголя, одежда закрытая, "
 "у людей по пять пальцев и обычная анатомия. --ar 3:2")
GRID = {3: '3×1', 4: '2×2', 5: '3+2', 6: '3×2', 7: '4+3', 8: '4×2', 9: '5+4', 10: '5×2', 11: '4+4+3', 12: '4×3'}
out = ['# Spotlight 5 — промпты', '', 'Первое сообщение в GPT: «Нужны изображения. Одна цифра — одно изображение».', '']
START = int(__import__('sys').argv[1]) if len(__import__('sys').argv) > 1 else 1
for i, (title, note, ws) in enumerate(S, 1):
    if i < START: continue
    out += [f'**{i}** — {title}', '```', STYLE, '',
            f'Сетка {GRID[len(ws)]}, ровно {len(ws)} {"картинки" if len(ws) in (2, 3, 4) else "картинок"}. {note}']
    out += [f'{j}. {cap} — {what}' for j, (_, cap, what) in enumerate(ws, 1)]
    out += ['```', '']
if START >= 79:  # листы по 6 (16.10.2026) — отдельным файлом, прежний остаётся как был
    out[0] = '# Spotlight 5 — промпты, листы по 6 картинок (с 79-го)'
    open('../../../docs/Тренажёр_Spotlight5_промпты_по6.md', 'w').write('\n'.join(out))
else:
    open('../../../docs/Тренажёр_Spotlight5_промпты.md', 'w').write('\n'.join(out))
