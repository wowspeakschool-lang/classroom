# Вебинар 03.12 · A / an · еда · группа 7–9: презентация и самостоятельная.
# Правки Анны 16.11: инструкции коротко по-английски, пункты по одному,
# слайд темы, guided discovery, в самостоятельной — слова и три формата.
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
ART = {'apple': 'an', 'egg': 'an', 'orange': 'an', 'banana': 'a', 'pear': 'a', 'sandwich': 'a'}
INK = '2A2140'


def mark(s):
    return len(s.shapes)


def since(s, n):
    return list(s.shapes)[n:]


def show(s, shapes, kind='appear'):
    click(s, *[(kind, x) for x in shapes])


d = Deck()

# 1 · Титул (блок школы)
s = d.slide(DARK)
text(s, 1, 1.3, 11.3, 1.0, 'WOW Speak', size=44, color=WHITE)
text(s, 1, 2.35, 11.3, 0.6, [('Hello! ', GOLD), ('Welcome to your English lesson!', WHITE)], size=24, bold=False)
for k, e in enumerate(['👋', '🍎', '🥪', '🎉']):
    text(s, 4.35 + k * 1.2, 3.25, 1.0, 1.0, e, size=30, fill=WHITE, bold=False)
text(s, 4.1, 4.65, 5.1, 0.6, 'Your teacher:  ______________', size=17, color=WHITE, bold=False, fill='3A2D5C')

# 3 · Warm-up: odd one out — ряды по одному
s = d.slide()
header(s, 'Find the odd one out')
rows = [(['red', 'blue', 'cat', 'green'], 2), (['one', 'dog', 'two', 'five'], 1), (['pen', 'book', 'ruler', 'sun'], 3)]
for r, (ws, ok) in enumerate(rows):
    y = 2.05 + r * 1.35
    n0 = mark(s)
    text(s, 0.9, y, 0.7, 1.0, f'{r+1}', size=26, color=PINK)
    cov = [option(s, 1.8 + k * 2.75, y, 2.5, 1.0, 'ABCD'[k], w_, k == ok, size=24) for k, w_ in enumerate(ws)]
    if r:
        show(s, since(s, n0))
    click(s, ('hide', [c for c in cov if c][0]))
chat(s, 'Type the letter: A, B, C or D')

# 4 · Lead-in
s = d.slide()
header(s, 'Guess')
text(s, 3.9, 2.0, 5.5, 3.9, '', fill=WHITE, line=PINK, lw=3)
pic(s, P('sandwich'), 4.4, 2.3, 4.5, 3.3)
cover = text(s, 3.9, 2.0, 5.5, 3.9, [[("What's in my lunchbox?", INK, 28)], [('🍱', INK, 70)], [('?', PINK, 54)]], fill='FFE9F4', line=PINK, lw=3)
click(s, ('hide', cover))
chat(s, 'Type your guess!')

# 4б · Тема урока — после lead-in (решение Анны 16.11)
s = d.slide()
header(s, 'Today we will learn')
c1 = text(s, 1.6, 1.8, 10.1, 1.6, [[('🍎  Food words', TEAL2, 30)], [('apple · egg · orange · banana · pear · sandwich', '555555', 20)]],
          fill=WHITE, line=TEAL, lw=2.5)
c2 = text(s, 1.6, 3.7, 10.1, 1.6, [[('🤔  a or an?', PINK, 30)], [('a banana  ·  an apple', '555555', 22)]],
          fill=WHITE, line=PINK, lw=2.5)
click(s, ('appear', c1))
click(s, ('appear', c2))

# 5 · Лексика: по одному по клику
s = d.slide()
header(s, 'Look and repeat', pill=PILL)
for k, w_ in enumerate(FOOD):
    x = 1.2 + (k % 3) * 3.75; y = 1.55 + (k // 3) * 2.55
    card = text(s, x, y, 3.3, 2.35, '', fill=WHITE, line=TEAL)
    im = pic(s, P(w_), x + 0.2, y + 0.12, 2.9, 1.6)
    lb = text(s, x, y + 1.78, 3.3, 0.5, w_, size=24, color=INK)
    kind = 'fade' if k % 2 else 'appear'
    click(s, (kind, card), (kind, im), (kind, lb))

# 6 · Remember
s = d.slide()
header(s, 'Remember the pictures', pill=PILL)
for k, w_ in enumerate(FOOD):
    x = 1.2 + (k % 3) * 3.75; y = 1.95 + (k // 3) * 2.15
    text(s, x, y, 3.3, 2.0, '', fill=WHITE, line=TEAL)
    pic(s, P(w_), x + 0.2, y + 0.1, 2.9, 1.35)
    text(s, x, y + 1.48, 3.3, 0.45, w_, size=20, color=INK)
click(s, timer(s, 6.4, 15))


def missing(order, gone, round_no):
    s = d.slide()
    header(s, 'Write the missing word', pill=PILL)
    for k, w_ in enumerate(order):
        x = 1.2 + (k % 3) * 3.75; y = 1.95 + (k // 3) * 2.15
        if w_ == gone:
            text(s, x + 0.03, y + 0.03, 3.24, 1.94, w_, size=34, color=GREEN, fill=GREENBG, line=GREEN, lw=2)
            cv = text(s, x, y, 3.3, 2.0, [[("What's missing?", INK, 18)], [('?', PINK, 54)]], fill='FFE9F4', line=PINK, lw=3)
            click(s, ('hide', cv))
        else:
            text(s, x, y, 3.3, 2.0, '', fill=WHITE, line=TEAL)
            pic(s, P(w_), x + 0.2, y + 0.15, 2.9, 1.7)
    chat(s, 'Type the missing word!')


missing(['banana', 'egg', 'sandwich', 'apple', 'pear', 'orange'], 'pear', 1)
missing(['orange', 'sandwich', 'apple', 'egg', 'banana', 'pear'], 'egg', 2)

# 9 · Guided discovery: читаем, a / an и первая буква выделены
s = d.slide()
header(s, 'Look and read', pill=PILL)
order = ['banana', 'apple', 'pear', 'egg', 'sandwich', 'orange']
for k, w_ in enumerate(order):
    col, row = k % 2, k // 2
    x = 0.9 + col * 5.95; y = 1.55 + row * 1.42
    a = ART[w_]; ac = PINK if a == 'an' else TEAL2
    n0 = mark(s)
    text(s, x, y, 5.6, 1.25, '', fill=WHITE, line=ac, lw=2.5)
    pic(s, P(w_), x + 0.15, y + 0.1, 1.3, 1.05)
    text(s, x + 1.5, y, 4.0, 1.25, [("It's ", INK), (a, ac), (' ', INK), (w_[0], ac), (w_[1:] + '.', INK)],
         size=28, align='l')
    if k:
        show(s, since(s, n0))
q = text(s, 2.6, 5.85, 8.1, 0.7, [('Why ', INK), ('an', PINK), ('? Why ', INK), ('a', TEAL2), ('?  🤔', INK)],
         size=24, fill='FFF3E6', line=ORANGE, lw=2.5)
click(s, ('appear', q))

# 10 · Правило (по-русски)
s = d.slide()
header(s, 'The rule', pill=PILL)
rules = [
    (TEAL, 'E6F9FC', [[('a', TEAL2, 30), ('  — перед согласным звуком', INK, 22)],
                      [('a banana  ·  a pear  ·  a sandwich', '555555', 20)]]),
    (PINK, 'FDE8F2', [[('an', PINK, 30), ('  — перед гласным звуком: a, e, i, o, u', INK, 22)],
                      [('an apple  ·  an egg  ·  an orange', '555555', 20)]]),
    (ORANGE, 'FFF3E6', [[('Если предметов много — a и an не ставим', INK, 22)],
                        [('apples  ·  eggs  ·  bananas', '555555', 20)]]),
]
for k, (ln, bg, runs) in enumerate(rules):
    c = text(s, 1.6, 1.6 + k * 1.6, 10.1, 1.35, runs, fill=bg, line=ln, lw=2.5)
    click(s, ('appear', c))

# 11 · Проверка понимания — по одному
s = d.slide()
header(s, 'Answer yes or no', pill=PILL)
qs = [([('Is ', INK), ('o', PINK), (' in orange a vowel?', INK)], 0),
      ([('Can we say ', INK), ('an', PINK), (' apples?', INK)], 1)]
for r, (q, ok) in enumerate(qs):
    y = 1.95 + r * 2.1
    n0 = mark(s)
    text(s, 1.0, y, 11.3, 0.7, [(f'{r+1})  ', PINK)] + q, size=26)
    cov = [option(s, 3.2 + k * 3.6, y + 0.8, 3.0, 0.9, 'AB'[k], t, k == ok, size=24) for k, t in enumerate(['Yes', 'No'])]
    if r:
        show(s, since(s, n0))
    click(s, ('hide', [c for c in cov if c][0]))
chat(s, 'Type A or B')


# 12–19 · Controlled practice: одно предложение на слайд
def drill(title, sentence, img, opts=None, ok=None, answer=None, hint='Type A, B or C', imgs=1, wide=False):
    s = d.slide()
    header(s, title, pill=PILL)
    if imgs == 1:
        pic(s, P(img), 0.9, 1.9, 3.5, 2.3)
    else:
        for k in range(imgs):
            pic(s, P(img), 0.7 + k * 1.25, 2.3, 1.3, 1.5)
    text(s, 4.7, 2.15, 7.9, 1.6, sentence, size=34, color=INK, fill=WHITE, line=PINK, lw=2.5)
    if opts:
        n = len(opts)
        if wide:
            covs = [option(s, 1.0, 4.15 + k * 0.72, 11.3, 0.62, 'ABC'[k], t, k == ok, size=22) for k, t in enumerate(opts)]
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


drill('Choose', "I've got ___ orange.", 'orange', ['a', 'an', '—'], 1)
drill(hl('Choose [a] or [an]'), 'This is (a / an) pear.', 'pear',
      answer='This is a pear.', hint='Type a or an')
drill('Find the mistake', "I've got an banana.", 'banana', ["I've", 'an', 'banana'], 1)
drill('Choose', 'I like ___ apples.', 'apple', ['an', 'a', '—'], 2, imgs=3)
drill('Choose', 'Have you got ___ egg?', 'egg', ['a', 'an', '—'], 1)
drill('Choose', "I haven't got ___ sandwich.", 'sandwich', ['an', '—', 'a'], 2)
drill('Choose the right answer', 'What is it?', 'banana',
      ["It's an banana.", "It's banana.", "It's a banana."], 2, wide=True)
drill('Correct the question', 'Have you got a apple?', 'apple',
      ['Have you got an apple?', 'Have you got apple?', 'Have you got an apples?'], 0, wide=True)

# 20–22 · ⭐ If time
STAR = '⭐ A / an'
s = d.slide()
header(s, 'Choose', pill=STAR)
pic(s, P('orange'), 0.9, 1.9, 3.5, 2.4)
text(s, 4.7, 1.95, 7.9, 0.9, 'an orange', size=30, color=INK, fill=WHITE, line=TEAL)
text(s, 4.7, 3.0, 7.9, 1.1, '___ big orange', size=34, color=INK, fill=WHITE, line=PINK, lw=2.5)
covs = [option(s, 3.0 + k * 3.9, 4.6, 3.5, 1.05, 'AB'[k], t, k == 0, size=26) for k, t in enumerate(['a', 'an'])]
click(s, ('hide', [c for c in covs if c][0]))
chat(s, 'Type A or B')

s = d.slide()
header(s, 'Choose', pill=STAR)
text(s, 3.2, 1.45, 6.9, 0.75, [('Which word needs ', INK), ('an', PINK), ('?', INK)], size=26, fill=WHITE, line=PINK, lw=2.5)
ws = ['banana', 'egg', 'pear', 'sandwich']
for k, w_ in enumerate(ws):
    pic(s, P(w_), 0.85 + k * 3.0 + 0.2, 2.35, 2.3, 1.9)
covs = [option(s, 0.85 + k * 3.0, 4.4, 2.7, 1.0, 'ABCD'[k], w_, k == 1, size=24) for k, w_ in enumerate(ws)]
click(s, ('hide', [c for c in covs if c][0]))
chat(s, 'Type A, B, C or D')

s = d.slide()
header(s, 'Put the words in order', pill=STAR)
for k, w_ in enumerate(['apple', 'got', "I've", 'an']):
    text(s, 1.5 + k * 2.65, 2.1, 2.35, 1.0, w_, size=28, color=INK, fill=WHITE, line=TEAL)
text(s, 2.43, 3.78, 8.44, 1.14, "I've got an apple.", size=32, color=GREEN, fill=GREENBG, line=GREEN, lw=3)
cv = text(s, 2.4, 3.75, 8.5, 1.2, '?', size=40, color=PINK, fill='FFE9F4', line=PINK, lw=3)
click(s, ('hide', cv))
chat(s, 'Type the sentence!')

# 23 · Freer practice
s = d.slide()
header(s, 'Write 2–3 sentences', pill=PILL)
cap = ['an apple', 'an egg', 'an orange', 'a banana', 'a pear', 'a sandwich']
for k, w_ in enumerate(FOOD):
    x = 0.6 + k * 2.05
    text(s, x, 1.95, 1.9, 2.1, '', fill=WHITE, line=TEAL)
    pic(s, P(w_), x + 0.15, 2.02, 1.6, 1.45)
    text(s, x, 3.5, 1.9, 0.5, cap[k], size=17, color=PINK if cap[k].startswith('an') else TEAL2)
text(s, 1.6, 4.4, 10.1, 1.5, [[("What's in your lunchbox?", PINK, 24)], [('Example: ', HEAD, 20), ("I've got an apple, a pear and a sandwich.", INK, 22)]],
     fill='FFF3E6', line=ORANGE, lw=2.5)
chat(s, 'Type your sentences!')

# 24 · I CAN
s = d.slide(PASTELS[1])
header(s, 'I can …')
for k, t in enumerate(['I can say: a banana, a pear, a sandwich.',
                       'I can say: an apple, an egg, an orange.',
                       "I can say: I've got an apple!"]):
    text(s, 2.0, 1.75 + k * 1.3, 9.3, 1.05, [('✅  ', GREEN), (t, INK)], size=22, fill=WHITE, line=GREEN, align='l')
chat(s, 'Send ✅ for every “I can”!')

# 25 · Well done
s = d.slide(DARK)
text(s, 10.3, 0.22, 2.8, 0.5, [('WOW', WHITE), (' Speak', GOLD)], size=18, align='r')
text(s, 1, 0.55, 11.3, 1.0, 'Well done!  🎉', size=44, color=GOLD)
text(s, 2.9, 1.75, 7.5, 1.2, [[('How was the lesson?', HEAD, 20)], [('⭐  ⭐⭐  ⭐⭐⭐  ⭐⭐⭐⭐  ⭐⭐⭐⭐⭐', GOLD, 20)]], fill='F7F3FF')
text(s, 2.9, 3.1, 7.5, 1.2, [[('Rate your teacher!', ORANGE, 20)], [('😊   😁   🤩   🥳   💯', INK, 26)]], fill='FFF5EE')
text(s, 2.9, 4.45, 7.5, 0.75, 'What did you like?', size=20, color=GREEN, fill=GREENBG)
text(s, 2.9, 5.4, 7.5, 0.75, 'Homework: self-study  📝', size=20, color=WHITE, fill=PINK)
chat(s, 'Type your stars!')

LESSON = os.path.join(OUT, 'WOW_Speak_A_An_Food_7-9_LESSON.pptx')
d.save(LESSON)

# ---------- Самостоятельная: слова → правило → 3 упражнения ----------
d2 = Deck()


def task_head(s, title, en, ru):
    header(s, title, pill=PILL)
    text(s, 1.0, 1.35, 11.3, 0.45, hl(en, INK) if en else '', size=18, color=INK)
    text(s, 1.0, 1.75, 11.3, 0.4, hl(ru, '555555') if ru else '', size=15, color='555555', italic=True)


s = d2.slide(DARK)
text(s, 1, 1.4, 11.3, 0.6, 'Self-study', size=24, color=GOLD)
text(s, 1, 2.2, 11.3, 1.0, 'a or an?', size=44, color=WHITE)
text(s, 1, 3.3, 11.3, 0.6, 'a banana  ·  an apple', size=26, color=TEAL)
text(s, 1, 5.6, 11.3, 0.5, 'WOW Speak', size=18, color=PINK)

# слова урока
s = d2.slide()
header(s, 'Our words  🍎', pill=PILL, sub='Повтори слова урока вслух.')
for k, w_ in enumerate(FOOD):
    x = 1.2 + (k % 3) * 3.75; y = 1.95 + (k // 3) * 2.2
    text(s, x, y, 3.3, 2.05, '', fill=WHITE, line=TEAL)
    pic(s, P(w_), x + 0.2, y + 0.1, 2.9, 1.4)
    a = ART[w_]
    text(s, x, y + 1.52, 3.3, 0.48, [(a + ' ', PINK if a == 'an' else TEAL2), (w_, INK)], size=22)

# правило
s = d2.slide()
header(s, 'Правило  📐', pill=PILL)
for k, (ln, bg, runs) in enumerate(rules):
    text(s, 1.6, 1.6 + k * 1.6, 10.1, 1.35, runs, fill=bg, line=ln, lw=2.5)

# Упр. 1 — картинка + впиши a / an
ex1 = ['egg', 'pear', 'orange', 'sandwich', 'apple', 'banana']
s = d2.slide()
task_head(s, 'Exercise 1  ✍️', 'Look and write [a] or [an].', 'Посмотри на картинку и впиши [a] или [an].')
for k, w_ in enumerate(ex1):
    x = 0.7 + (k % 3) * 4.0; y = 2.35 + (k // 3) * 2.1
    text(s, x, y, 3.85, 1.95, '', fill=WHITE, line='E3DCF2')
    pic(s, P(w_), x + 0.12, y + 0.2, 1.25, 1.55)
    text(s, x + 1.4, y, 2.45, 1.95, [(f'{k+1}) ', PINK), ('___ ' + w_, INK)], size=19, align='l')
s = d2.slide()
task_head(s, 'Exercise 1 — answers  ✅', '', '')
for k, w_ in enumerate(ex1):
    x = 0.7 + (k % 3) * 4.0; y = 2.35 + (k // 3) * 2.1
    text(s, x, y, 3.85, 1.95, '', fill=GREENBG, line=GREEN)
    pic(s, P(w_), x + 0.12, y + 0.2, 1.25, 1.55)
    text(s, x + 1.4, y, 2.45, 1.95, [(f'{k+1}) ', PINK), (ART[w_] + ' ', GREEN), (w_, INK)], size=19, align='l')

# Упр. 2 — раздели на две группы
ex2 = ['an egg', 'apples', 'a pear', 'an orange', 'bananas', 'a sandwich']
s = d2.slide()
task_head(s, 'Exercise 2  🧺', 'One or many? Write the words in two lists.', 'Один предмет или много? Распиши слова в два списка.')
for k, w_ in enumerate(ex2):
    text(s, 0.9 + k * 2.0, 2.4, 1.85, 0.8, w_, size=20, color=INK, fill=WHITE, line=TEAL)
for j, (h, c) in enumerate([('ONE  ☝️', TEAL2), ('MANY  🍎🍎🍎', PINK)]):
    text(s, 1.6 + j * 5.3, 3.55, 4.8, 0.7, h, size=24, color=WHITE, fill=c)
    text(s, 1.6 + j * 5.3, 4.3, 4.8, 1.9, '', fill=WHITE, line=c, lw=2.5)
s = d2.slide()
task_head(s, 'Exercise 2 — answers  ✅', '', '')
for j, (h, c, items) in enumerate([('ONE  ☝️', TEAL2, ['an egg', 'a pear', 'an orange', 'a sandwich']),
                                   ('MANY  🍎🍎🍎', PINK, ['apples', 'bananas'])]):
    text(s, 1.6 + j * 5.3, 2.4, 4.8, 0.7, h, size=24, color=WHITE, fill=c)
    text(s, 1.6 + j * 5.3, 3.15, 4.8, 2.6, [[(t, GREEN, 24)] for t in items], fill=GREENBG, line=GREEN, lw=2.5)

# Упр. 3 — найди и исправь ошибку
ex3 = [("I've got a apple.", "I've got an apple."), ('This is an sandwich.', 'This is a sandwich.'),
       ('Have you got a egg?', 'Have you got an egg?'), ("It's an pear.", "It's a pear."),
       ('I like an bananas.', 'I like bananas.')]
s = d2.slide()
task_head(s, 'Exercise 3  🔎', 'Find the mistake. Write the sentence correctly.', 'Найди ошибку и напиши предложение правильно.')
for k, (t, _) in enumerate(ex3):
    text(s, 2.0, 2.35 + k * 0.82, 9.3, 0.68, f'{k+1})  {t}', size=22, color=INK, fill=WHITE, line='E3DCF2', align='l')
s = d2.slide()
task_head(s, 'Exercise 3 — answers  ✅', '', '')
for k, (_, t) in enumerate(ex3):
    text(s, 2.0, 2.0 + k * 0.82, 9.3, 0.68, [(f'{k+1})  ', PINK), (t, GREEN)], size=22, fill=GREENBG, line=GREEN, align='l')

s = d2.slide(DARK)
text(s, 10.3, 0.22, 2.8, 0.5, [('WOW', WHITE), (' Speak', GOLD)], size=18, align='r')
text(s, 1, 2.3, 11.3, 1.1, 'Well done!  🎉', size=48, color=GOLD)
text(s, 1, 3.5, 11.3, 0.6, 'a banana  ·  an apple  ·  bananas', size=26, color=WHITE, bold=False)
SELF = os.path.join(OUT, 'WOW_Speak_A_An_Food_7-9_SELFSTUDY.pptx')
d2.save(SELF)
print(LESSON, count_anims(LESSON))
print(SELF, len(d2.prs.slides._sldIdLst))
