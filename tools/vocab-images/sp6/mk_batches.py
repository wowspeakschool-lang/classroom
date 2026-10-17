"""Промпты пачками по 10 для GPT (просьба Анны 16.10.2026): одно сообщение — 10 листов,
каждый лист — одна строка «N <промпт>». python3 mk_batches.py → docs/Тренажёр_Spotlight6_пачки.md"""
import sys
from sheets import S
from mk_prompts_style import STYLE

START = int(sys.argv[1]) if len(sys.argv) > 1 else 1
NUM = {1: 'одну отдельную картинку', 2: 'две отдельные картинки', 3: 'три отдельные картинки',
       4: 'четыре отдельные картинки', 5: 'пять отдельных картинок', 6: 'шесть отдельных картинок',
       7: 'семь отдельных картинок', 8: 'восемь отдельных картинок', 9: 'девять отдельных картинок',
       10: 'десять отдельных картинок'}
ROWS = {3: [3], 4: [2, 2], 5: [3, 2], 6: [3, 3]}


def one(ws, note):
    rows, k, parts = ROWS[len(ws)], 0, []
    for r, n in enumerate(rows, 1):
        items = '; '.join(f'«{cap}» — {what.rstrip(".")}' for _, cap, what in ws[k:k + n])
        parts.append(f'Ряд {r}, слева направо: {items}.')
        k += n
    grid = f'{max(rows)}×{len(rows)}' if len(rows) > 1 else f'{rows[0]}×1'
    cnt = len(ws)
    word = 'картинки' if cnt in (2, 3, 4) else 'картинок'
    return (f'{STYLE.replace(" --ar 3:2", "")} Сетка {grid}, ровно {cnt} {word}; подпись под каждой — '
            f'английское слово из кавычек, сами кавычки не рисовать. {note} ' + ' '.join(parts) + ' --ar 3:2')


sheets = list(range(START, len(S) + 1))
out = ['# Spotlight 6 — пачки по 10 для GPT', '',
       'Каждый блок — одно сообщение целиком. Номер в сообщении (1–10) → номер листа указан в заголовке.', '']
for b in range(0, len(sheets), 10):
    chunk = sheets[b:b + 10]
    out.append(f'**Сообщение {b // 10 + 1}** — листы {chunk[0]}–{chunk[-1]} '
               f'(1 = лист {chunk[0]}{", 10 = лист " + str(chunk[-1]) if len(chunk) == 10 else ""})')
    msg = [f'Сгенерируй {NUM[len(chunk)]}', ' одна цифра - одно изображение отдельное', '']
    for i, n in enumerate(chunk, 1):
        title, note, ws = S[n - 1]
        msg += [f'{i} {one(ws, note.strip())}', '']
    out += ['```'] + msg[:-1] + ['```', '']
open('../../../docs/Тренажёр_Spotlight6_пачки.md', 'w').write('\n'.join(out))
print(len(sheets), (len(sheets) + 9) // 10)
