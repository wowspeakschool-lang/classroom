"""Промпты листов Spotlight 4 → docs/Тренажёр_Spotlight4_промпты.md (стиль как у Prepare)."""
from sheets import S
STYLE = ("Стиль: hand-drawn children's storybook illustration, bold dark brown outlines of even thickness, "
 "rich saturated colours with soft shading and volume, hand-drawn textures, friendly rounded shapes. "
 "NOT flat vector icons, NOT clip-art. Чистый белый фон, строгая сетка, широкие белые промежутки между "
 "картинками и рядами, ничего не касается соседних клеток. Под каждой картинкой подпись — английское слово, "
 "чёрный sans-serif по центру, с отступом от рисунка. Никакого текста внутри рисунков, без рамок. "
 "Всё мягко, без крови, ран и слёз. --ar 3:2")
GRID = {6: '3×2', 7: '4+3', 8: '4×2', 9: '5+4', 10: '5×2'}
out = ['# Spotlight 4 — промпты', '', 'Первое сообщение в GPT: «Нужны изображения. Одна цифра — одно изображение».', '']
START = int(__import__('sys').argv[1]) if len(__import__('sys').argv) > 1 else 1
for i, (title, note, ws) in enumerate(S, 1):
    if i < START: continue
    out += [f'**{i}** — {title}', '```', STYLE, '',
            f'Сетка {GRID[len(ws)]}, ровно {len(ws)} картинок. {note}']
    out += [f'{j}. {cap} — {what}' for j, (_, cap, what) in enumerate(ws, 1)]
    out += ['```', '']
open('../../../docs/Тренажёр_Spotlight4_промпты' + ('' if START == 1 else '_2') + '.md', 'w').write('\n'.join(out))
