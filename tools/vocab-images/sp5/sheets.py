"""Spotlight 5: листы для генерации, собранные из sheets_1..4.py (описания писали по частям).
Слова с описанием «ЦИФРЫ» рисует скрипт — на листы не идут, лежат в DIGITS."""
import importlib, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
S, DIGITS = [], []
for k in (1, 2, 3, 4):
    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'sheets_{k}.py')): break
    for title, note, ws in importlib.import_module(f'sheets_{k}').S:
        keep = [w for w in ws if w[2].strip().upper() != 'ЦИФРЫ']
        DIGITS += [w for w in ws if w[2].strip().upper() == 'ЦИФРЫ']
        if keep: S.append((title, note, keep))
