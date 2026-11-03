"""Промпты Prepare одним сообщением: python3 mk_batches.py → docs/Тренажёр_Prepare_пачки.md"""
from words import S, NOTE
from mk_prompts_style import STYLE
NUM = {7: 'семь отдельных картинок'}
def one(ws):
    rows, k, parts = [4, 4], 0, []
    for r, n in enumerate(rows, 1):
        parts.append(f'Ряд {r}, слева направо: ' + '; '.join(f'«{c}» — {d}' for _, c, d, _ in ws[k:k+n]) + '.')
        k += n
    notes = ' '.join(dict.fromkeys(NOTE[t] for t, *_ in ws if t in NOTE))
    return (f'{STYLE.replace(" --ar 3:2", "")} Сетка 4×2, ровно 8 картинок; подпись под каждой — '
            f'английское слово из кавычек, сами кавычки не рисовать. {notes} ' + ' '.join(parts) + ' --ar 3:2')
msg = [f'Сгенерируй {NUM[len(S)]}', ' одна цифра - одно изображение отдельное', '']
for i, ws in enumerate(S, 1):
    msg += [f'{i} {one(ws)}', '']
open('../../../docs/Тренажёр_Prepare_пачки.md', 'w').write('# Prepare — пробелы, одно сообщение\n\n```\n' + '\n'.join(msg[:-1]) + '\n```\n')
print(len(S), [len(s) for s in S])
