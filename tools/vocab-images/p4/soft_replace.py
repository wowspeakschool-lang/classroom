"""Мягкие замены (без крови и слёз): лист 2×2 из картинки 70 → break, cut, hurt, injure.
Запускать после cut.py, если листы 25/26 перенарезались."""
import sys; sys.path.insert(0, '..')
from widen import row
from cut import bands
I = '/tmp/claude-0/-home-user-classroom/d4a2a0a4-519c-5b81-af84-18451bfcf9dd/images/70.webp'
pics = [b for b in bands(I) if b[1] - b[0] > 60]
assert len(pics) == 2, pics
row(I, *pics[0], ['break', 'cut'], 'soft', gap=12, min_area=150)
# подписи первого ряда стоят вплотную к верху второго — второй ряд начинаем под ними
from lib import row as plain_row
plain_row(I, 470, pics[1][1], ['hurt', 'injure'], 'soft', gap=12, min_area=150)
import shutil
for w, sheet in [('break', 26), ('cut', 25), ('hurt', 26), ('injure', 26)]:
    shutil.copy(f'soft/{w}.png', f'out/{sheet}/{w}.png')
print('ok')
