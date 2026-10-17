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

# Лист 78 — замены не прошедших проверку (сгенерирован 16.10.2026, images/177.webp)
S.append(('Замены', '', [
    ('culture', 'culture', 'Дети в школьной форме в музее рассматривают расписную вазу в витрине и пейзажи в рамах. Без статуй людей.'),
    ('carnival', 'carnival', 'Карнавальное шествие: дети в закрытых костюмах зверей и птиц, маски, конфетти.'),
    ('street parade', 'street parade', 'Мальчик-барабанщик впереди, платформа из цветов в виде слона, люди с флажками.'),
    ('nightclub', 'nightclub', 'Вход в ночной клуб вечером: неоновые ноты, диско-шар.'),
    ('Thanksgiving (Day)', 'Thanksgiving', 'Семья за праздничным столом, индейка, пирог, сок в стаканах.'),
]))
# Листы 79 и дальше — оставшиеся слова по 6 на лист (16.10.2026); прежние номера — sheets_6.REPLACED
from sheets_6 import S as _S6, REPLACED
S += _S6

# Лист 160 — замены 2 (17.10.2026): не прошли проверку листов 126, 141, 142
S.append(('Замены 2', '', [
    ("That's not my kind of place.", 'not my kind of place', 'Мальчик с книгой хмуро стоит у входа в шумный зал игровых автоматов с мигающими огнями и громкими колонками; внутри никого не видно.'),
    ('keep out', 'keep out', 'Забор с закрытой калиткой и знаком: красный круг с перечёркнутой ладонью; за забором большая злая собака на цепи, смешная, не страшная.'),
    ('face', 'face (difficulty)', 'Мальчик-скалолаз в каске смело смотрит на высокую крутую стену для лазания и берётся за первый зацеп.'),
]))
