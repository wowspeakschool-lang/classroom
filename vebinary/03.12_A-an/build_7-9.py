# Вебинар 03.12 · A / an · еда · группа 7–9: презентация и самостоятельная.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from wow import *

IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '7-9')
os.makedirs(OUT, exist_ok=True)
P = lambda n: os.path.join(IMG, n + '.png')
PILL = 'A / an'
FOOD = ['apple', 'egg', 'orange', 'banana', 'pear', 'sandwich']

d = Deck()

# 1 · Титул (блок школы)
s = d.slide(DARK)
text(s, 1, 1.3, 11.3, 1.0, 'WOW Speak', size=44, color=WHITE)
text(s, 1, 2.35, 11.3, 0.6, [('Hello! ', GOLD), ('Welcome to your English lesson!', WHITE)], size=24, bold=False)
for k, e in enumerate(['👋', '🍎', '🥪', '🎉']):
    text(s, 4.35 + k * 1.2, 3.25, 1.0, 1.0, e, size=30, fill=WHITE, bold=False)
text(s, 4.1, 4.65, 5.1, 0.6, 'Your teacher:  ______________', size=17, color=WHITE, bold=False, fill='3A2D5C')

# 2 · Warm-up: кто лишний
s = d.slide()
header(s, 'Кто лишний?  🤔', sub='Найди в каждом ряду лишнее слово.')
rows = [(['red', 'blue', 'cat', 'green'], 2), (['one', 'dog', 'two', 'five'], 1), (['pen', 'book', 'ruler', 'sun'], 3)]
for r, (ws, ok) in enumerate(rows):
    y = 2.05 + r * 1.35
    text(s, 0.9, y, 0.7, 1.0, f'{r+1}', size=26, color=PINK)
    covers = []
    for k, w_ in enumerate(ws):
        c = option(s, 1.8 + k * 2.75, y, 2.5, 1.0, 'ABCD'[k], w_, k == ok, size=24)
        if c: covers.append(c)
    click(s, ('hide', covers[0]))
chat(s, 'Напиши в чат букву лишнего слова: 1 — ?, 2 — ?, 3 — ?')

# 3 · Lead-in: что в ланч-боксе
s = d.slide()
header(s, 'Что у меня в ланч-боксе?  🍱', sub='Угадай! Напиши в чат, какая там еда.')
text(s, 3.9, 2.0, 5.5, 3.9, '', fill='FFFFFF', line=PINK, lw=3)
pic(s, P('sandwich'), 4.4, 2.3, 4.5, 3.3)
cover = text(s, 3.9, 2.0, 5.5, 3.9, [[('🍱', '2A2140', 80)], [('?', PINK, 60)]], fill='FFE9F4', line=PINK, lw=3)
click(s, ('hide', cover))
chat(s, 'Как думаешь, что внутри? Напиши в чат!')

# 4 · Лексика: по одному по клику
s = d.slide()
header(s, 'Food  🍎', pill=PILL)
for k, w_ in enumerate(FOOD):
    x = 1.2 + (k % 3) * 3.75; y = 1.55 + (k // 3) * 2.55
    card = text(s, x, y, 3.3, 2.35, '', fill=WHITE, line=TEAL)
    im = pic(s, P(w_), x + 0.2, y + 0.12, 2.9, 1.6)
    lb = text(s, x, y + 1.78, 3.3, 0.5, w_, size=24, color='2A2140')
    kind = 'fade' if k % 2 else 'appear'
    click(s, (kind, card), (kind, im), (kind, lb))

# 5 · Запомни
s = d.slide()
header(s, 'Запомни!  👀', pill=PILL, sub='Смотри внимательно — сейчас одна картинка исчезнет.')
for k, w_ in enumerate(FOOD):
    x = 1.2 + (k % 3) * 3.75; y = 1.95 + (k // 3) * 2.15
    text(s, x, y, 3.3, 2.0, '', fill=WHITE, line=TEAL)
    pic(s, P(w_), x + 0.2, y + 0.1, 2.9, 1.35)
    text(s, x, y + 1.48, 3.3, 0.45, w_, size=20, color='2A2140')
click(s, timer(s, 6.4, 15))


def missing(order, gone, round_no):
    s = d.slide()
    header(s, 'Что исчезло?  🔍', pill=PILL, sub=f'Раунд {round_no}')
    for k, w_ in enumerate(order):
        x = 1.2 + (k % 3) * 3.75; y = 1.95 + (k // 3) * 2.15
        if w_ == gone:
            text(s, x + 0.03, y + 0.03, 3.24, 1.94, w_, size=34, color=GREEN, fill=GREENBG, line=GREEN, lw=3)
            cv = text(s, x, y, 3.3, 2.0, '?', size=60, color=PINK, fill='FFE9F4', line=PINK, lw=3)
            click(s, ('hide', cv))
        else:
            text(s, x, y, 3.3, 2.0, '', fill=WHITE, line=TEAL)
            pic(s, P(w_), x + 0.2, y + 0.15, 2.9, 1.7)
    chat(s, 'Напиши в чат слово, которое исчезло!')


missing(['banana', 'egg', 'sandwich', 'apple', 'pear', 'orange'], 'pear', 1)
missing(['orange', 'sandwich', 'apple', 'egg', 'banana', 'pear'], 'egg', 2)

# 8 · Вводная к грамматике
s = d.slide()
header(s, "I've got…  🤔", pill=PILL, sub='Как правильно? Выбери A или B.')
for r, (w_, a, b, ok) in enumerate([('banana', 'a banana', 'an banana', 0), ('apple', 'a apple', 'an apple', 1)]):
    y = 1.95 + r * 2.15
    pic(s, P(w_), 1.3, y, 2.4, 1.9)
    text(s, 3.9, y + 0.6, 0.7, 0.7, f'{r+1}', size=26, color=PINK)
    covs = [option(s, 4.7 + k * 3.7, y + 0.45, 3.4, 1.0, 'AB'[k], t, k == ok, size=26) for k, t in enumerate([a, b])]
    click(s, ('hide', [c for c in covs if c][0]))
chat(s, 'Напиши в чат: 1 — A или B? 2 — A или B?')

# 9 · Правило
s = d.slide()
header(s, 'Правило  📐', pill=PILL)
rules = [
    (TEAL, 'E6F9FC', [[('a', TEAL2, 30), ('  — перед согласным звуком', '2A2140', 22)],
                      [('a banana  ·  a pear  ·  a sandwich', '555555', 20)]]),
    (PINK, 'FDE8F2', [[('an', PINK, 30), ('  — перед гласным звуком: a, e, i, o, u', '2A2140', 22)],
                      [('an apple  ·  an egg  ·  an orange', '555555', 20)]]),
    (ORANGE, 'FFF3E6', [[('Если предметов много — a и an не ставим', '2A2140', 22)],
                        [('apples  ·  eggs  ·  bananas', '555555', 20)]]),
]
for k, (ln, bg, runs) in enumerate(rules):
    c = text(s, 1.6, 1.6 + k * 1.6, 10.1, 1.35, runs, fill=bg, line=ln, lw=2.5)
    click(s, ('appear', c))

# 10 · Проверка понимания
s = d.slide()
header(s, 'Проверим!  ✅', pill=PILL, sub='Выбери A или B.')
qs = [('Слово orange начинается с гласного звука?', ['да', 'нет'], 0),
      ('Ставим a или an, если яблок много?', ['да', 'нет'], 1)]
for r, (q, opts, ok) in enumerate(qs):
    y = 1.95 + r * 2.1
    text(s, 1.0, y, 11.3, 0.7, f'{r+1})  {q}', size=24, color='2A2140')
    covs = [option(s, 3.2 + k * 3.6, y + 0.8, 3.0, 0.9, 'AB'[k], t, k == ok, size=24) for k, t in enumerate(opts)]
    click(s, ('hide', [c for c in covs if c][0]))
chat(s, 'Напиши в чат: 1 — A или B? 2 — A или B?')


# 11–18 · Controlled practice: одно предложение на слайд
def drill(title, sub, sentence, img, opts=None, ok=None, answer=None, hint='Напиши в чат букву: A, B или C', imgs=1, wide=False):
    s = d.slide()
    header(s, title, pill=PILL, sub=sub)
    if imgs == 1:
        pic(s, P(img), 0.9, 1.9, 3.5, 2.3)
    else:
        for k in range(imgs):
            pic(s, P(img), 0.7 + k * 1.25, 2.3, 1.3, 1.5)
    text(s, 4.7, 2.15, 7.9, 1.6, sentence, size=34, color='2A2140', fill=WHITE, line=PINK, lw=2.5)
    clicks = []
    if opts:
        n = len(opts)
        if wide:
            covs = [option(s, 1.0 + 0, 4.15 + k * 0.72, 11.3, 0.62, 'ABC'[k], t, k == ok, size=22) for k, t in enumerate(opts)]
        else:
            ww = 3.5
            x0 = (13.33 - n * ww - (n - 1) * 0.35) / 2
            covs = [option(s, x0 + k * (ww + 0.35), 4.45, ww, 1.05, 'ABC'[k], t, k == ok, size=26) for k, t in enumerate(opts)]
        cv = [c for c in covs if c][0]
    else:
        text(s, 3.03, 4.38, 7.24, 1.04, answer, size=30, color=GREEN, fill=GREENBG, line=GREEN, lw=3)
        cv = text(s, 3.0, 4.35, 7.3, 1.1, '?', size=40, color=PINK, fill='FFE9F4', line=PINK, lw=3)
    click(s, timer(s, 6.33 if not wide else 6.38, 10))
    click(s, ('hide', cv))
    chat(s, hint)


drill('Выбери!  👆', 'Какое слово пропущено?', "I've got ___ orange.", 'orange', ['a', 'an', '—'], 1)
drill('Раскрой скобки  ✍️', 'Выбери нужное слово в скобках.', 'This is (a / an) pear.', 'pear',
      answer='This is a pear.', hint='Напиши в чат: a или an?')
drill('Найди ошибку  🔎', 'В каком слове ошибка?', "I've got an banana.", 'banana', ["I've", 'an', 'banana'], 1)
drill('Один или много?  🍎🍎🍎', 'Что нужно поставить?', "I like ___ apples.", 'apple', ['an', 'a', '—'], 2, imgs=3)
drill('Вопрос  ❓', 'Какое слово пропущено?', 'Have you got ___ egg?', 'egg', ['a', 'an', '—'], 1)
drill('Отрицание  ✋', 'Какое слово пропущено?', "I haven't got ___ sandwich.", 'sandwich', ['an', '—', 'a'], 2)
drill('Что на картинке?  🖼️', 'Выбери правильное предложение.', 'What is it?', 'banana',
      ["It's an banana.", "It's banana.", "It's a banana."], 2, wide=True)
drill('Ошибка в вопросе  🔎', 'Как спросить правильно?', 'Have you got a apple?', 'apple',
      ['Have you got an apple?', 'Have you got apple?', 'Have you got an apples?'], 0, wide=True)

# 19–21 · ⭐ If time
STAR = '⭐ A / an'
s = d.slide()
header(s, 'Большой апельсин  ⭐', pill=STAR, sub='Смотри на слово сразу после a / an.')
pic(s, P('orange'), 0.9, 1.9, 3.5, 2.4)
text(s, 4.7, 1.95, 7.9, 0.9, 'an orange', size=30, color='2A2140', fill=WHITE, line=TEAL)
text(s, 4.7, 3.0, 7.9, 1.1, '___ big orange', size=34, color='2A2140', fill=WHITE, line=PINK, lw=2.5)
covs = [option(s, 3.0 + k * 3.9, 4.6, 3.5, 1.05, 'AB'[k], t, k == 0, size=26) for k, t in enumerate(['a', 'an'])]
click(s, ('hide', [c for c in covs if c][0]))
chat(s, 'Напиши в чат: A или B?')

s = d.slide()
header(s, 'Найди лишнее  ⭐', pill=STAR, sub='Какому слову нужно an?')
ws = ['banana', 'egg', 'pear', 'sandwich']
for k, w_ in enumerate(ws):
    x = 0.85 + k * 3.0
    pic(s, P(w_), x + 0.2, 1.95, 2.3, 2.2)
covs = [option(s, 0.85 + k * 3.0, 4.4, 2.7, 1.0, 'ABCD'[k], w_, k == 1, size=24) for k, w_ in enumerate(ws)]
click(s, ('hide', [c for c in covs if c][0]))
chat(s, 'Напиши в чат букву: A, B, C или D')

s = d.slide()
header(s, 'Собери предложение  ⭐', pill=STAR, sub='Расставь слова по порядку.')
for k, w_ in enumerate(['apple', 'got', "I've", 'an']):
    text(s, 1.5 + k * 2.65, 2.1, 2.35, 1.0, w_, size=28, color='2A2140', fill=WHITE, line=TEAL)
text(s, 2.43, 3.78, 8.44, 1.14, "I've got an apple.", size=32, color=GREEN, fill=GREENBG, line=GREEN, lw=3)
cv = text(s, 2.4, 3.75, 8.5, 1.2, '?', size=40, color=PINK, fill='FFE9F4', line=PINK, lw=3)
click(s, ('hide', cv))
chat(s, 'Напиши в чат предложение целиком!')

# 22 · Freer practice
s = d.slide()
header(s, 'Мой ланч-бокс  🍱', pill=PILL, sub='Что у тебя в ланч-боксе? Напиши 2–3 предложения.')
cap = ['an apple', 'an egg', 'an orange', 'a banana', 'a pear', 'a sandwich']
for k, w_ in enumerate(FOOD):
    x = 0.6 + k * 2.05
    text(s, x, 1.95, 1.9, 2.1, '', fill=WHITE, line=TEAL)
    pic(s, P(w_), x + 0.15, 2.02, 1.6, 1.45)
    text(s, x, 3.5, 1.9, 0.5, cap[k], size=17, color=PINK if cap[k].startswith('an') else TEAL2)
text(s, 1.6, 4.4, 10.1, 1.5, [[('Образец:', HEAD, 18)], [("I've got an apple, a pear and a sandwich.", '2A2140', 24)]],
     fill='FFF3E6', line=ORANGE, lw=2.5)
chat(s, 'Напиши в чат, что у тебя в ланч-боксе!')

# 23 · I CAN
s = d.slide(PASTELS[1])
header(s, 'I CAN …  🌟')
for k, t in enumerate(['I can say: a banana, a pear, a sandwich.',
                       'I can say: an apple, an egg, an orange.',
                       "I can say: I've got an apple!"]):
    text(s, 2.0, 1.75 + k * 1.3, 9.3, 1.05, [('✅  ', GREEN), (t, '2A2140')], size=22, fill=WHITE, line=GREEN, align='l')
chat(s, 'Отправь в чат ✅ за всё, что у тебя получается!')

# 24 · Well done
s = d.slide(DARK)
text(s, 10.3, 0.22, 2.8, 0.5, [('WOW', WHITE), (' Speak', GOLD)], size=18, align='r')
text(s, 1, 0.55, 11.3, 1.0, 'Well done!  🎉', size=44, color=GOLD)
text(s, 2.9, 1.75, 7.5, 1.2, [[('Как прошёл урок?', HEAD, 20)], [('⭐  ⭐⭐  ⭐⭐⭐  ⭐⭐⭐⭐  ⭐⭐⭐⭐⭐', GOLD, 20)]], fill='F7F3FF')
text(s, 2.9, 3.1, 7.5, 1.2, [[('Оцени учителя!', ORANGE, 20)], [('😊   😁   🤩   🥳   💯', '2A2140', 26)]], fill='FFF5EE')
text(s, 2.9, 4.45, 7.5, 0.75, 'Что понравилось? Что было сложно?', size=20, color=GREEN, fill=GREENBG)
text(s, 2.9, 5.4, 7.5, 0.75, 'Дома: самостоятельная работа  📝', size=20, color=WHITE, fill=PINK)
chat(s, 'Напиши в чат звёзды и впечатления!')

LESSON = os.path.join(OUT, 'WOW_Speak_A_An_Food_7-9_LESSON.pptx')
d.save(LESSON)

# ---------- Самостоятельная (7 слайдов) ----------
d2 = Deck()
s = d2.slide(DARK)
text(s, 1, 1.4, 11.3, 0.6, 'Self-study', size=24, color=GOLD)
text(s, 1, 2.2, 11.3, 1.0, 'A или an', size=44, color=WHITE)
text(s, 1, 3.3, 11.3, 0.6, 'a banana  ·  an apple', size=26, color=TEAL)
text(s, 1, 5.6, 11.3, 0.5, 'WOW Speak', size=18, color=PINK)

s = d2.slide()
header(s, 'Правило  📐', pill=PILL)
for k, (ln, bg, runs) in enumerate(rules):
    text(s, 1.6, 1.6 + k * 1.6, 10.1, 1.35, runs, fill=bg, line=ln, lw=2.5)

ex1 = [("I've got (a / an) egg.", 'an', 'a'), ('This is (a / an) banana.', 'a', 'an'),
       ('She has got (a / an) orange.', 'an', 'a'), ('Have you got (a / an) pear?', 'a', 'an'),
       ("I haven't got (a / an) apple.", 'an', 'a')]
s = d2.slide()
header(s, 'Упражнение 1  ✍️', pill=PILL, sub='Выбери a или an.')
for k, (t, _, _) in enumerate(ex1):
    text(s, 2.0, 1.95 + k * 0.85, 9.3, 0.7, f'{k+1})  {t}', size=22, color='2A2140', fill=WHITE, line='E3DCF2', align='l')

s = d2.slide()
header(s, 'Упражнение 1 — ответы  ✅', pill=PILL)
for k, (t, ok, bad) in enumerate(ex1):
    pre, post = t.split('(a / an)')
    p = [(f'{k+1})  ', PINK), (pre, '2A2140'), (ok, GREEN), (post, '2A2140')]
    text(s, 2.0, 1.75 + k * 0.85, 9.3, 0.7, p, size=22, fill=GREENBG, line=GREEN, align='l')

ex2 = [("I've got a apple.", "I've got an apple."), ('This is an sandwich.', 'This is a sandwich.'),
       ('Have you got a egg?', 'Have you got an egg?'), ("It's an pear.", "It's a pear."),
       ("I like an bananas.", "I like bananas.")]
s = d2.slide()
header(s, 'Упражнение 2  📝', pill=PILL, sub='Найди ошибку и напиши предложение правильно.')
for k, (t, _) in enumerate(ex2):
    text(s, 2.0, 1.95 + k * 0.85, 9.3, 0.7, f'{k+1})  {t}', size=22, color='2A2140', fill=WHITE, line='E3DCF2', align='l')

s = d2.slide()
header(s, 'Упражнение 2 — ответы  ✅', pill=PILL)
for k, (_, t) in enumerate(ex2):
    text(s, 2.0, 1.75 + k * 0.85, 9.3, 0.7, [(f'{k+1})  ', PINK), (t, GREEN)], size=22, fill=GREENBG, line=GREEN, align='l')
text(s, 1.5, 6.15, 10.3, 0.5, 'Если яблок, бананов много — a и an не ставим.', size=16, color=ORANGE)

s = d2.slide(DARK)
text(s, 10.3, 0.22, 2.8, 0.5, [('WOW', WHITE), (' Speak', GOLD)], size=18, align='r')
text(s, 1, 2.3, 11.3, 1.1, 'Well done!  🎉', size=48, color=GOLD)
text(s, 1, 3.5, 11.3, 0.6, 'Теперь ты знаешь, когда нужно a, а когда an!', size=24, color=WHITE, bold=False)
SELF = os.path.join(OUT, 'WOW_Speak_A_An_Food_7-9_SELFSTUDY.pptx')
d2.save(SELF)
print(LESSON, count_anims(LESSON))
print(SELF)
