# Сборщик вебинара WOW Speak по описанию темы (spec): презентация, самостоятельная, план.
# Структура и анимации — по vebinary/PRAVILA.md. Образец — 03.12 A / an.
import os, re, random
from wow import *
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

INK = '2A2140'
ROOT = os.path.dirname(os.path.abspath(__file__))


def mk(t, base=INK, size=None):
    """[x] — бирюзовым, {x} — малиновым; остальное base."""
    out = []
    for part in re.split(r'(\[[^\]]+\]|\{[^}]+\})', t):
        if not part:
            continue
        if part[0] == '[':
            r = (part[1:-1], TEAL2)
        elif part[0] == '{':
            r = (part[1:-1], PINK)
        else:
            r = (part, base)
        out.append(r if size is None else r + (size,))
    return out


def plain(t):
    return re.sub(r'[\[\]{}]', '', t)


def mark(s):
    return len(s.shapes)


def since(s, n):
    return list(s.shapes)[n:]


def show(s, shapes, kind='appear'):
    click(s, *[(kind, x) for x in shapes])


class Lesson:
    def __init__(self, sp):
        self.sp = sp
        self.img = os.path.join(ROOT, sp['imgdir'])
        self.d = Deck()
        self.stages = []      # (этап, первый слайд, последний слайд)
        self.keys = {}        # этап -> [ключи]

    def P(self, n):
        for d in (self.img, os.path.join(ROOT, 'kartinki', '10plus'), os.path.join(ROOT, 'kartinki', '7-9'),
                  os.path.join(ROOT, 'kartinki', 'scenes')):
            p = os.path.join(d, n + '.png')
            if os.path.exists(p):
                return p
        raise FileNotFoundError(n)

    def stage(self, name):
        self.stages.append([name, self.d.n + 1, None])

    def end(self):
        self.stages[-1][2] = self.d.n

    def key(self, name, k):
        self.keys.setdefault(name, []).append(k)

    # ---------- общие куски ----------
    def head(self, title, pill=True, star=False):
        s = self.d.slide()
        p = None
        if pill:
            p = ('⭐ ' if star else '') + self.sp['pill']
        header(s, mk(title) if ('[' in title or '{' in title) else title, pill=p)
        return s

    def options(self, s, x0, y, w, h, opts, ok, size=24, gap=0.3, labels='ABCD'):
        covs = [option(s, x0 + k * (w + gap), y, w, h, labels[k], t, k == ok, size=size) for k, t in enumerate(opts)]
        return [c for c in covs if c][0]

    def row_opts(self, s, y, opts, ok, h=1.0, size=24, maxw=3.5):
        n = len(opts); gap = 0.3
        w = min(maxw, (11.6 - gap * (n - 1)) / n)
        x0 = (13.33 - n * w - (n - 1) * gap) / 2
        return self.options(s, x0, y, w, h, opts, ok, size=size, gap=gap)

    def cover_answer(self, s, x, y, w, h, answer, size=30, q='?'):
        text(s, x + 0.03, y + 0.03, w - 0.06, h - 0.06, mk(answer, GREEN), size=size, color=GREEN,
             fill=GREENBG, line=GREEN, lw=2)
        return text(s, x, y, w, h, q, size=40 if q == '?' else 22, color=PINK, fill='FFE9F4', line=PINK, lw=3)

    # ---------- этапы ----------
    def title(self):
        s = self.d.slide(DARK)
        text(s, 1, 1.3, 11.3, 1.0, 'WOW Speak', size=44, color=WHITE)
        text(s, 1, 2.35, 11.3, 0.6, [('Hello! ', GOLD), ('Welcome to your English lesson!', WHITE)], size=24, bold=False)
        for k, e in enumerate(self.sp['title_emoji']):
            text(s, 4.35 + k * 1.2, 3.25, 1.0, 1.0, e, size=30, fill=WHITE, bold=False)
        text(s, 4.1, 4.65, 5.1, 0.6, 'Your teacher:  ______________', size=17, color=WHITE, bold=False, fill='3A2D5C')

    def warmup(self):
        w = self.sp['warmup']; t = w['type']
        s = self.head(w['title'], pill=False)
        rows = w['rows']
        for r, row in enumerate(rows):
            y = 1.75 + r * 1.45
            n0 = mark(s)
            text(s, 0.7, y, 0.6, 1.0, f'{r+1}', size=26, color=PINK)
            if t == 'odd':
                ws, ok = row
                cv = self.options(s, 1.5, y, 2.6, 1.0, ws, ok, size=24, gap=0.25)
                self.key('warmup', f'{r+1} — {"ABCD"[ok]} ({ws[ok]})')
            elif t == 'quiz':
                q, ws, ok = row
                text(s, 1.4, y - 0.05, 4.6, 1.1, q, size=22, color=INK, align='l')
                cv = self.options(s, 6.0, y, 2.15, 1.0, ws, ok, size=22, gap=0.2)
                self.key('warmup', f'{r+1} — {"ABC"[ok]} ({ws[ok]})')
            else:  # scramble / emoji: карточка-загадка → ответ под крышкой
                clue, ans = row
                text(s, 1.5, y, 5.4, 1.0, clue, size=30 if t == 'emoji' else 28, color=INK, fill=WHITE, line=TEAL)
                text(s, 7.1, y, 0.6, 1.0, '→', size=28, color=PINK)
                cv = self.cover_answer(s, 7.9, y, 4.4, 1.0, ans, size=28)
                self.key('warmup', f'{r+1} — {ans}')
            if r:
                show(s, since(s, n0))
            click(s, ('hide', cv))
        chat(s, w['chat'])

    def leadin(self):
        L = self.sp['leadin']; t = L['type']
        s = self.head(L['title'], pill=False)
        if t == 'guess':
            text(s, 3.9, 1.6, 5.5, 4.3, '', fill=WHITE, line=PINK, lw=3)
            pic(s, self.P(L['img']), 4.3, 1.8, 4.7, 3.9)
            cv = text(s, 3.9, 1.6, 5.5, 4.3, [[(L['q'], INK, 26)], [(L['emoji'], INK, 64)], [('?', PINK, 50)]],
                      fill='FFE9F4', line=PINK, lw=3)
            click(s, ('hide', cv))
            self.key('leadin', f'под крышкой — {L["answer"]}')
        elif t == 'poll':
            text(s, 1.5, 1.55, 10.3, 1.0, mk(L['q']), size=30, fill=WHITE, line=PINK, lw=2.5)
            for k, (im, cap) in enumerate(L['opts']):
                x = 0.9 + k * (11.6 / len(L['opts']))
                ww = 11.6 / len(L['opts']) - 0.3
                n0 = mark(s)
                text(s, x, 2.85, ww, 3.0, '', fill=WHITE, line=TEAL)
                pic(s, self.P(im), x + 0.15, 2.95, ww - 0.3, 2.15)
                text(s, x, 5.15, ww, 0.6, [('ABCD'[k] + ')  ', PINK), (cap, INK)], size=20)
                if k:
                    show(s, since(s, n0))
            self.key('leadin', 'опрос — правильного ответа нет')
        else:  # question: большой вопрос + эмодзи, отвечают свободно
            text(s, 1.5, 1.7, 10.3, 1.3, mk(L['q']), size=34, fill=WHITE, line=PINK, lw=2.5)
            text(s, 1.5, 3.3, 10.3, 2.4, L['emoji'], size=80, bold=False)
            self.key('leadin', 'свободные ответы')
        chat(s, L['chat'])

    def today(self):
        s = self.head('Today we will learn', pill=False)
        a, b = self.sp['today']
        c1 = text(s, 1.6, 1.8, 10.1, 1.6, [[(a[0], TEAL2, 30)], [(a[1], '555555', 20)]], fill=WHITE, line=TEAL, lw=2.5)
        c2 = text(s, 1.6, 3.7, 10.1, 1.6, [[(b[0], PINK, 30)], [(b[1], '555555', 22)]], fill=WHITE, line=PINK, lw=2.5)
        click(s, ('appear', c1)); click(s, ('appear', c2))

    def lexis(self):
        s = self.head(self.sp.get('lexis_title', 'Look and repeat'))
        for k, (im, cap) in enumerate(self.sp['lexis']):
            x = 1.2 + (k % 3) * 3.75; y = 1.55 + (k // 3) * 2.55
            card = text(s, x, y, 3.3, 2.35, '', fill=WHITE, line=TEAL)
            p = pic(s, self.P(im), x + 0.2, y + 0.12, 2.9, 1.6)
            lb = text(s, x, y + 1.78, 3.3, 0.5, mk(cap), size=22 if len(cap) < 18 else 18, color=INK)
            kind = 'fade' if k % 2 else 'appear'
            click(s, (kind, card), (kind, p), (kind, lb))

    def game(self):
        g = self.sp['game']; t = g['type']; lex = self.sp['lexis']
        if t == 'missing':
            s = self.head('Remember the pictures')
            for k, (im, cap) in enumerate(lex):
                x = 1.2 + (k % 3) * 3.75; y = 1.75 + (k // 3) * 2.2
                text(s, x, y, 3.3, 2.05, '', fill=WHITE, line=TEAL)
                pic(s, self.P(im), x + 0.2, y + 0.1, 2.9, 1.4)
                text(s, x, y + 1.52, 3.3, 0.48, mk(cap), size=18, color=INK)
            click(s, timer(s, 6.4, 15))
            for rnd, gone in enumerate(g['gone'], 1):
                order = lex[:]
                random.Random(rnd * 7).shuffle(order)
                s = self.head('Write the missing word')
                for k, (im, cap) in enumerate(order):
                    x = 1.2 + (k % 3) * 3.75; y = 1.75 + (k // 3) * 2.2
                    if im == gone:
                        text(s, x + 0.03, y + 0.03, 3.24, 1.99, mk(cap, GREEN), size=24, color=GREEN, fill=GREENBG, line=GREEN, lw=2)
                        cv = text(s, x, y, 3.3, 2.05, [[("What's missing?", INK, 18)], [('?', PINK, 54)]], fill='FFE9F4', line=PINK, lw=3)
                        click(s, ('hide', cv))
                        self.key('game', f'раунд {rnd} — {plain(cap)}')
                    else:
                        text(s, x, y, 3.3, 2.05, '', fill=WHITE, line=TEAL)
                        pic(s, self.P(im), x + 0.2, y + 0.15, 2.9, 1.75)
                chat(s, 'Type the missing word!')
        elif t == 'peek':
            for rnd, (im, cap) in enumerate(g['items'], 1):
                s = self.head('What is it? Guess!')
                text(s, 3.4, 1.55, 6.5, 4.0, '', fill=WHITE, line=TEAL, lw=2.5)
                pic(s, self.P(im), 3.6, 1.65, 6.1, 3.8)
                tiles = []
                for k in range(4):
                    tx = 3.4 + (k % 2) * 3.25; ty = 1.55 + (k // 2) * 2.0
                    tiles.append(text(s, tx, ty, 3.25, 2.0, '?', size=44, color=WHITE, fill=PINK if k in (0, 3) else TEAL2,
                                      line=WHITE, lw=2, shape='rect'))
                cv = self.cover_answer(s, 4.4, 5.7, 4.5, 0.8, cap, size=26, q='Answer')
                for k in g.get('order', [1, 2, 0, 3]):
                    click(s, ('hide', tiles[k]))
                click(s, ('hide', cv))
                self.key('game', f'раунд {rnd} — {plain(cap)}')
                chat(s, 'Type your guess!')
        else:  # letters: картинка + слово с пропусками, по одному
            s = self.head('Write the word')
            for r, (im, mask, cap) in enumerate(g['items']):
                y = 1.6 + r * 1.65
                n0 = mark(s)
                pic(s, self.P(im), 1.0, y, 2.0, 1.45)
                text(s, 3.3, y + 0.15, 4.2, 1.15, mask, size=32, color=INK, fill=WHITE, line=TEAL)
                text(s, 7.6, y + 0.15, 0.6, 1.15, '→', size=28, color=PINK)
                cv = self.cover_answer(s, 8.3, y + 0.15, 4.0, 1.15, cap, size=28)
                if r:
                    show(s, since(s, n0))
                click(s, ('hide', cv))
                self.key('game', f'{r+1} — {plain(cap)}')
            chat(s, 'Type the word!')

    def discovery(self):
        D = self.sp['discovery']
        s = self.head('Look and read')
        lines = D['lines']; two = D.get('two_cols', len(lines) > 4)
        if D.get('scene'):
            pic(s, self.P(D['scene']), 0.5, 1.5, 5.4, 4.2)
        for k, (im, t) in enumerate(lines):
            if D.get('scene'):
                x = 6.1; y = 1.55 + k * 1.05; w = 6.8; two = False
            elif two:
                col, row = k % 2, k // 2; x = 0.9 + col * 5.95; y = 1.55 + row * 1.42; w = 5.6
            else:
                x = 1.4; y = 1.55 + k * 1.05; w = 10.5
            h = 1.25 if two else 0.92
            n0 = mark(s)
            text(s, x, y, w, h, '', fill=WHITE, line=TEAL, lw=2)
            if im:
                pic(s, self.P(im), x + 0.12, y + 0.08, 1.3 if two else 1.0, h - 0.16)
            tx = x + (1.5 if im else 0.2)
            text(s, tx, y, w - (1.6 if im else 0.3), h, mk(t), size=24 if two else 24, align='l')
            if k:
                show(s, since(s, n0))
        q = text(s, 2.0, 5.85, 9.3, 0.72, mk(D['q']), size=24, fill='FFF3E6', line=ORANGE, lw=2.5)
        click(s, ('appear', q))

    def rule(self):
        s = self.head('The rule')
        cols = [(TEAL, 'E6F9FC'), (PINK, 'FDE8F2'), (ORANGE, 'FFF3E6')]
        for k, (a, b) in enumerate(self.sp['rule']):
            ln, bg = cols[k]
            c = text(s, 1.3, 1.55 + k * 1.62, 10.7, 1.42, [mk(a, INK, 21), mk(b, '555555', 19)], fill=bg, line=ln, lw=2.5)
            click(s, ('appear', c))

    def ccq(self):
        s = self.head('Answer yes or no')
        for r, (q, ok) in enumerate(self.sp['ccq']):
            y = 1.75 + r * 2.15
            n0 = mark(s)
            text(s, 0.8, y, 11.7, 0.75, [(f'{r+1})  ', PINK)] + mk(q), size=25)
            cv = self.options(s, 3.2, y + 0.85, 3.0, 0.9, ['Yes', 'No'], ok, size=24, gap=0.6)
            if r:
                show(s, since(s, n0))
            click(s, ('hide', cv))
            self.key('ccq', f'{r+1} — {"AB"[ok]} ({["Yes", "No"][ok]})')
        chat(s, 'Type A or B')

    def drill(self, dr, star=False, stage='controlled'):
        s = self.head(dr['title'], star=star)
        kind = dr.get('kind', 'gap')
        imgs = dr.get('imgs') or ([dr['img']] if dr.get('img') else [])
        if imgs:
            if len(imgs) == 1:
                pic(s, self.P(imgs[0]), 0.8, 1.6, 3.6, 2.5)
            else:
                for k, im in enumerate(imgs[:3]):
                    pic(s, self.P(im), 0.6 + k * 1.3, 1.9, 1.25, 1.8)
            sx, sw = 4.6, 8.0
        else:
            sx, sw = 1.3, 10.7
        sent = dr['s']
        text(s, sx, 1.85, sw, 1.6, mk(sent), size=30 if len(plain(sent)) < 34 else 25, color=INK, fill=WHITE, line=PINK, lw=2.5)
        if kind == 'write':
            cv = self.cover_answer(s, 1.6, 4.1, 10.1, 1.2, dr['answer'], size=28)
            k = plain(dr['answer'])
        elif kind == 'wide':
            covs = [option(s, 1.0, 3.95 + j * 0.74, 11.3, 0.64, 'ABC'[j], t, j == dr['ok'], size=21) for j, t in enumerate(dr['opts'])]
            cv = [c for c in covs if c][0]
            k = f'{"ABC"[dr["ok"]]} ({plain(dr["opts"][dr["ok"]])})'
        else:
            cv = self.row_opts(s, 4.25, dr['opts'], dr['ok'], h=1.05, size=24)
            k = f'{"ABCD"[dr["ok"]]} ({plain(dr["opts"][dr["ok"]])})'
        if not star:
            click(s, timer(s, 6.38, 10))
        click(s, ('hide', cv))
        self.key(stage, k)
        chat(s, dr.get('chat', 'Type the sentence!' if kind == 'write' else f'Type {", ".join("ABCD"[:len(dr.get("opts", [0, 0, 0]))-1])} or {"ABCD"[len(dr.get("opts", [0, 0, 0]))-1]}'))

    def freer(self, F):
        s = self.head(F['title'])
        ims = F.get('imgs', [])
        if F.get('scene'):
            pic(s, self.P(F['scene']), 0.6, 1.5, 6.6, 4.9)
            text(s, 7.4, 1.6, 5.4, 4.6, [mk(F['q'], PINK, 22), [('Example: ', HEAD, 18)] + mk(F['example'], INK, 20)],
                 fill='FFF3E6', line=ORANGE, lw=2.5)
            chat(s, F.get('chat', 'Type your sentences!'))
            return
        if ims:
            n = len(ims); w = min(2.0, 11.8 / n - 0.15)
            x0 = (13.33 - n * (w + 0.15) + 0.15) / 2
            for k, (im, cap) in enumerate(ims):
                x = x0 + k * (w + 0.15)
                text(s, x, 1.5, w, 2.15, '', fill=WHITE, line=TEAL)
                pic(s, self.P(im), x + 0.1, 1.57, w - 0.2, 1.5)
                text(s, x, 3.08, w, 0.52, mk(cap), size=15 if len(cap) > 14 else 17, color=INK)
            y = 3.95
        else:
            y = 1.9
        text(s, 1.2, y, 10.9, 2.3 if not ims else 2.0,
             [mk(F['q'], PINK, 24), [('Example: ', HEAD, 19)] + mk(F['example'], INK, 21)],
             fill='FFF3E6', line=ORANGE, lw=2.5)
        chat(s, F.get('chat', 'Type your sentences!'))

    def ican(self):
        s = self.d.slide(PASTELS[1])
        header(s, 'I can …')
        for k, t in enumerate(self.sp['ican']):
            text(s, 1.6, 1.75 + k * 1.3, 10.1, 1.05, [('✅  ', GREEN)] + mk(t), size=21, fill=WHITE, line=GREEN, align='l')
        chat(s, 'Send ✅ for every “I can”!')

    def welldone(self):
        s = self.d.slide(DARK)
        text(s, 10.3, 0.22, 2.8, 0.5, [('WOW', WHITE), (' Speak', GOLD)], size=18, align='r')
        text(s, 1, 0.55, 11.3, 1.0, 'Well done!  🎉', size=44, color=GOLD)
        text(s, 2.9, 1.75, 7.5, 1.2, [[('How was the lesson?', HEAD, 20)], [('⭐  ⭐⭐  ⭐⭐⭐  ⭐⭐⭐⭐  ⭐⭐⭐⭐⭐', GOLD, 20)]], fill='F7F3FF')
        text(s, 2.9, 3.1, 7.5, 1.2, [[('Rate your teacher!', ORANGE, 20)], [('😊   😁   🤩   🥳   💯', INK, 26)]], fill='FFF5EE')
        text(s, 2.9, 4.45, 7.5, 0.75, 'What did you like?', size=20, color=GREEN, fill=GREENBG)
        text(s, 2.9, 5.4, 7.5, 0.75, 'Homework  📝', size=20, color=WHITE, fill=PINK)
        chat(s, 'Type your stars!')

    def build(self, path):
        S = self.stage
        S('Блок школы'); self.title(); self.end()
        S('Warm-up'); self.warmup(); self.end()
        S('Lead-in'); self.leadin(); self.end()
        S('Тема урока'); self.today(); self.end()
        S('Лексика'); self.lexis(); self.end()
        S('Игра на слова'); self.game(); self.end()
        S('Guided discovery'); self.discovery(); self.end()
        S('Правило'); self.rule(); self.end()
        S('Проверка понимания'); self.ccq(); self.end()
        S('Controlled practice')
        for dr in drill_order(self.sp):
            self.drill(dr)
        self.end()
        S('⭐ If time')
        for dr in self.sp['iftime']:
            self.drill(dr, star=True, stage='iftime')
        self.end()
        S('Freer practice 1'); self.freer(self.sp['freer'][0]); self.end()
        S('Freer practice 2'); self.freer(self.sp['freer'][1]); self.end()
        S('Feedback'); self.ican(); self.welldone(); self.end()
        self.d.save(path)


# ---------- самостоятельная ----------
def selfstudy(sp, path):
    L = Lesson(sp); d = L.d
    st = sp['self']

    def thead(title, en, ru):
        s = d.slide()
        header(s, title, pill=sp['pill'])
        if en:
            text(s, 1.0, 1.35, 11.3, 0.45, mk(en), size=18, color=INK)
        if ru:
            text(s, 1.0, 1.75, 11.3, 0.4, mk(ru, '555555'), size=15, color='555555', italic=True)
        return s

    s = d.slide(DARK)
    text(s, 1, 1.4, 11.3, 0.6, 'Homework', size=24, color=GOLD)
    text(s, 1, 2.2, 11.3, 1.0, st['title'], size=40, color=WHITE)
    text(s, 1, 3.3, 11.3, 0.6, st['sub'], size=24, color=TEAL)
    text(s, 1, 5.6, 11.3, 0.5, 'WOW Speak', size=18, color=PINK)
    s = thead('Our words  📚', '', 'Повтори слова урока вслух.')
    for k, (im, cap) in enumerate(sp['lexis']):
        x = 1.2 + (k % 3) * 3.75; y = 2.2 + (k // 3) * 2.15
        text(s, x, y, 3.3, 2.0, '', fill=WHITE, line=TEAL)
        pic(s, L.P(im), x + 0.2, y + 0.1, 2.9, 1.35)
        text(s, x, y + 1.48, 3.3, 0.48, mk(cap), size=19 if len(cap) < 18 else 16, color=INK)
    s = thead('Правило  📐', '', '')
    cols = [(TEAL, 'E6F9FC'), (PINK, 'FDE8F2'), (ORANGE, 'FFF3E6')]
    for k, (a, b) in enumerate(sp.get('self_rule', sp['rule'])):
        ln, bg = cols[k]
        text(s, 1.3, 1.6 + k * 1.62, 10.7, 1.42, [mk(a, INK, 21), mk(b, '555555', 19)], fill=bg, line=ln, lw=2.5)

    for n, ex in enumerate(st['ex'], 1):
        emo = ['✍️', '🧩', '🔎'][n - 1]
        for ans in (False, True):
            s = thead(f'Exercise {n}' + (' — answers  ✅' if ans else f'  {emo}'),
                      '' if ans else ex['en'], '' if ans else ex['ru'])
            t = ex['type']
            if t == 'pics':
                for k, (im, q, a) in enumerate(ex['items']):
                    x = 0.7 + (k % 3) * 4.0; y = 2.35 + (k // 3) * 2.1
                    text(s, x, y, 3.85, 1.95, '', fill=GREENBG if ans else WHITE, line=GREEN if ans else 'E3DCF2')
                    pic(s, L.P(im), x + 0.12, y + 0.2, 1.25, 1.55)
                    body = mk(a, GREEN) if ans else mk(q)
                    text(s, x + 1.4, y, 2.45, 1.95, [(f'{k+1}) ', PINK)] + body, size=17, align='l')
            elif t == 'list':
                lx, lw_ = 1.5, 10.3
                if ex.get('scene'):
                    pic(s, L.P(ex['scene']), 0.5, 2.3, 4.6, 3.6); lx, lw_ = 5.3, 7.6
                for k, (q, a) in enumerate(ex['items']):
                    y = 2.3 + k * 0.72
                    if ans:
                        text(s, lx, y, lw_, 0.62, [(f'{k+1})  ', PINK)] + mk(a, GREEN), size=20 if lw_ > 9 else 17, fill=GREENBG, line=GREEN, align='l')
                    else:
                        text(s, lx, y, lw_, 0.62, [(f'{k+1})  ', PINK)] + mk(q), size=20 if lw_ > 9 else 17, fill=WHITE, line='E3DCF2', align='l')
            elif t == 'sort':
                chips = ex['chips']
                if not ans:
                    n_ = len(chips); w = min(1.9, 11.8 / n_ - 0.12)
                    x0 = (13.33 - n_ * (w + 0.12) + 0.12) / 2
                    for k, c in enumerate(chips):
                        text(s, x0 + k * (w + 0.12), 2.35, w, 0.75, c, size=17 if len(c) > 10 else 19, color=INK, fill=WHITE, line=TEAL)
                for j, (h, items) in enumerate(ex['groups']):
                    c = [TEAL2, PINK][j]
                    yy = 2.35 if ans else 3.4
                    text(s, 1.6 + j * 5.3, yy, 4.8, 0.65, h, size=22, color=WHITE, fill=c)
                    text(s, 1.6 + j * 5.3, yy + 0.7, 4.8, 2.4 if ans else 2.2,
                         [[(t_, GREEN, 21)] for t_ in items] if ans else '', fill=GREENBG if ans else WHITE,
                         line=GREEN if ans else c, lw=2.5)
            elif t == 'match':
                left, right, key = ex['left'], ex['right'], ex['key']
                for k, q in enumerate(left):
                    text(s, 0.8, 2.3 + k * 0.78, 5.6, 0.66, [(f'{k+1})  ', PINK)] + mk(q), size=18, fill=WHITE, line='E3DCF2', align='l')
                if ans:
                    for k, q in enumerate(left):
                        a = right[key[k]]
                        text(s, 6.6, 2.3 + k * 0.78, 5.9, 0.66, [('abcdef'[key[k]] + ')  ', GREEN)] + mk(a, GREEN), size=18,
                             fill=GREENBG, line=GREEN, align='l')
                else:
                    for k, a in enumerate(right):
                        text(s, 6.6, 2.3 + k * 0.78, 5.9, 0.66, [('abcdef'[k] + ')  ', TEAL2)] + mk(a), size=18, fill=WHITE, line=TEAL, align='l')
    s = d.slide(DARK)
    text(s, 10.3, 0.22, 2.8, 0.5, [('WOW', WHITE), (' Speak', GOLD)], size=18, align='r')
    text(s, 1, 2.3, 11.3, 1.1, 'Well done!  🎉', size=48, color=GOLD)
    text(s, 1, 3.5, 11.3, 0.6, st['sub'], size=24, color=WHITE, bold=False)
    d.save(path)
    return len(d.prs.slides._sldIdLst)


# ---------- план ----------
TIME = {'Блок школы': '3 мин', 'Warm-up': '1,5 мин', 'Lead-in': '1 мин', 'Тема урока': '0,5 мин', 'Лексика': '3 мин',
        'Игра на слова': '2 мин', 'Guided discovery': '3 мин', 'Правило': '1 мин', 'Проверка понимания': '1 мин',
        'Controlled practice': '7 мин', '⭐ If time': '0–3 мин', 'Freer practice 1': '3 мин',
        'Freer practice 2': '2 мин', 'Feedback': '1,5 мин'}
KEYMAP = {'Warm-up': 'warmup', 'Lead-in': 'leadin', 'Игра на слова': 'game', 'Проверка понимания': 'ccq',
          'Controlled practice': 'controlled', '⭐ If time': 'iftime'}


def plan(L, path):
    sp = L.sp
    HEADC, GREENC, GREY = '3D2B5A', '2E7D32', '222222'
    doc = Document()
    sec = doc.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
    for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'):
        setattr(sec, m, Cm(1.27))
    st = doc.styles['Normal']; st.font.name = 'Arial'; st.font.size = Pt(9.5)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')

    def para(c, parts, space=2):
        p = c.add_paragraph(); p.paragraph_format.space_after = Pt(space)
        for t, color, bold, italic, *sz in parts:
            r = p.add_run(t); r.bold = bold; r.italic = italic
            r.font.name = 'Arial'; r.font.size = Pt(sz[0] if sz else 9.5); r.font.color.rgb = RGBColor.from_string(color)

    def shade(cell, h):
        tcPr = cell._tc.get_or_add_tcPr(); e = OxmlElement('w:shd')
        e.set(qn('w:val'), 'clear'); e.set(qn('w:color'), 'auto'); e.set(qn('w:fill'), h); tcPr.append(e)

    para(doc, [(f'WOW Speak   •   {sp["topic"]}   •   {sp["theme"]}', HEADC, True, False, 15)])
    para(doc, [(f'Группа {sp["group"]} · 30 минут · Zoom, дети пишут в чат · вебинар {sp["date"]}', GREY, False, False)])
    para(doc, [('Лексика (6): ', HEADC, True, False), (', '.join(plain(c) for _, c in sp['lexis']), GREY, False, False)])
    para(doc, [('Грамматика: ', HEADC, True, False), (sp['plan']['grammar'], GREY, False, False)])
    para(doc, [('Речь учителя', GREENC, False, True),
               (' — зелёным курсивом. Ответ на слайде открывается по клику: исчезает крышка. '
                'Пункты на слайде появляются по одному: пункт → клик ответ → клик следующий пункт.', GREY, False, False)], 6)
    t = doc.add_table(rows=1, cols=5); t.style = 'Table Grid'; t.autofit = False
    widths = [Cm(3.3), Cm(1.7), Cm(5.0), Cm(10.8), Cm(6.3)]
    for k, h in enumerate(['Этап', 'Время', 'Цель', 'Задание', 'Комментарий']):
        c = t.rows[0].cells[k]; c.width = widths[k]; shade(c, PINK)
        c.paragraphs[0]._element.getparent().remove(c.paragraphs[0]._element)
        para(c, [(h, 'FFFFFF', True, False)])
    P = sp['plan']
    for i, (name, a, b) in enumerate(L.stages):
        cells = t.add_row().cells
        for j, c in enumerate(cells):
            c.width = widths[j]; c.paragraphs[0]._element.getparent().remove(c.paragraphs[0]._element)
            if i % 2: shade(c, 'F7F3FF')
        para(cells[0], [(name, HEADC, True, False)])
        para(cells[1], [(TIME[name], GREY, False, False)])
        para(cells[2], [(P['goal'].get(name, ''), GREY, False, False)])
        sl = f'Слайд {a}.' if a == b else f'Слайды {a}–{b}.'
        para(cells[3], [(sl, GREY, True, False), (' ' + P['task'].get(name, ''), GREY, False, False)])
        for line in P['say'].get(name, []):
            para(cells[3], [(line, GREENC, False, True)])
        com = P['com'].get(name, '')
        ks = L.keys.get(KEYMAP.get(name, ''), [])
        if ks:
            com = (com + ' ' if com else '') + 'Ключ: ' + ' · '.join(ks) + '.'
        para(cells[4], [(com, GREY, False, False)])
    for k, gc in enumerate(t._tbl.tblGrid.findall(qn('w:gridCol'))):
        gc.set(qn('w:w'), str(int(widths[k].twips)))
    para(doc, [('', GREY, False, False)])
    para(doc, [('Итого: 30 минут без ⭐. ', HEADC, True, False), ('⭐ берём из запаса, если группа идёт быстрее.', GREY, False, False)])
    doc.save(path)


def build_all(sp, outdir):
    fill_plan(sp)
    os.makedirs(outdir, exist_ok=True)
    # Имена файлов (решение Анны 23.11.2026): сначала тема, потом что это за файл.
    base = re.sub(r'[:?…/\\*"<>|]', '', sp.get('file_topic', sp['topic'])).strip()
    base = re.sub(r'\s+', ' ', base) + f' {sp["group"].replace("–", "-")}'
    L = Lesson(sp)
    les = os.path.join(outdir, base + ' - Presentation.pptx')
    L.build(les)
    plan(L, os.path.join(outdir, base + ' - Lesson plan.docx'))
    selfp = os.path.join(outdir, base + ' - Homework.pptx')
    n = selfstudy(sp, selfp)
    return les, selfp, L, n


def drill_order(sp):
    """Порядок форматов дриллинга меняется от темы к теме (PRAVILA: «Разнообразие»):
    середина (2–7) сдвигается на (день % 6), первое и последнее задание на месте."""
    d = sp['drills']; r = int(sp['date'][:2]) % 6; mid = d[1:7]
    rest = mid[r:] + mid[:r]
    out = [d[0]]
    while rest:   # одинаковое задание не ставим два раза подряд, если есть другое
        j = next((k for k, x in enumerate(rest) if x['title'] != out[-1]['title']
                  and not (len(rest) == 1 and x['title'] == d[7]['title'])), 0)
        out.append(rest.pop(j))
    return out + [d[7]]


def fill_plan(sp):
    """План по умолчанию из описания темы; sp['plan'] дополняет и переопределяет."""
    P = sp.setdefault('plan', {})
    young = sp['group'] == '7–9'
    lex = ', '.join(plain(c) for _, c in sp['lexis'])
    g = sp['game']['type']
    gtask = {'missing': '«Remember the pictures» (15 секунд), затем два раунда «Write the missing word».',
             'peek': 'Картинка под четырьмя плитками: каждый клик убирает плитку, дети угадывают; последний клик — ответ.',
             'letters': 'Картинка и слово с пропущенными буквами, пункты по одному.'}[g]
    goal = {'Блок школы': 'Познакомиться, настроить на урок.',
            'Warm-up': 'Разогреться на знакомом материале, без темы урока.',
            'Lead-in': f'Ввести лексическую тему: {sp["theme_ru"]}.',
            'Тема урока': 'Назвать цель урока: слова и грамматика.',
            'Лексика': f'Ввести 6 слов: {lex}.',
            'Игра на слова': 'Запомнить слова, узнавать их по картинке.',
            'Guided discovery': 'Дети сами замечают форму и формулируют правило.',
            'Правило': 'Закрепить вывод детей.',
            'Проверка понимания': 'Убедиться, что правило понятно.',
            'Controlled practice': f'Отработать {sp["topic"]} в предложениях.',
            '⭐ If time': 'Шаг сложнее — только если группа отвечает легко.',
            'Freer practice 1': 'Сказать о себе с новой грамматикой.',
            'Freer practice 2': 'Ещё одно своё высказывание, другой формат.',
            'Feedback': 'Подвести итог, получить оценку, выдать домашнее задание.'}
    drills = ' · '.join(plain(d['title']) for d in drill_order(sp))
    task = {'Блок школы': 'Приветствие, рассказ о школе WOW Speak.',
            'Warm-up': f'{sp["warmup"]["title"]}. Пункты по одному: пункт → клик ответ → клик следующий.',
            'Lead-in': f'{sp["leadin"]["title"]}: {plain(sp["leadin"].get("q", ""))}',
            'Тема урока': 'Today we will learn — два пункта по клику.',
            'Лексика': 'Слова появляются по одному по клику (появление и выцветание чередуются).',
            'Игра на слова': gtask,
            'Guided discovery': 'Look and read: предложения по одному по клику, форма выделена цветом; '
                                'последний клик — вопрос к детям.',
            'Правило': 'Три пункта по клику.',
            'Проверка понимания': 'Вопрос → клик ответ → клик следующий вопрос.',
            'Controlled practice': 'Одно предложение на слайд. Клик 1 — полоса «подумай» (10 с), клик 2 — ответ. '
                                   f'Задания: {drills}.',
            '⭐ If time': ' · '.join(plain(d['title']) for d in sp['iftime']) + '. Без таймера, один клик — ответ.',
            'Freer practice 1': plain(sp['freer'][0]['q']) + ' Образец на слайде.',
            'Freer practice 2': plain(sp['freer'][1]['q']) + ' Образец на слайде.',
            'Feedback': 'I can · Well done: звёзды, оценка учителя, домашнее задание.'}
    if young:
        say = {'Блок школы': ['Hello! Welcome to WOW Speak!', 'Напишите в чат, как вас зовут.'],
               'Warm-up': ["Let's warm up!", 'Пишите ответ в чат.'],
               'Тема урока': ['Сегодня мы выучим новые слова и новое правило.'],
               'Лексика': ['Look and repeat!', 'Повторяйте за мной вслух, а в чат пишите слово.'],
               'Controlled practice': ['Think for 10 seconds!', 'Пишите в чат букву или ответ.'],
               'Freer practice 1': ['Напишите про себя. Посмотрите на образец.'],
               'Freer practice 2': ['А теперь ещё одно задание — про вас.'],
               'Feedback': ['Send ✅ for every “I can”. Rate the lesson!']}
    else:
        say = {'Блок школы': ['Hello! Welcome to WOW Speak!', 'Type your name in the chat.'],
               'Warm-up': ["Let's warm up! Type your answers in the chat."],
               'Тема урока': ["Today we'll learn new words and a new grammar rule."],
               'Лексика': ['Look and repeat after me.'],
               'Controlled practice': ['Think for 10 seconds, then type your answer.'],
               'Freer practice 1': ['Now write about yourself. Look at the example.'],
               'Freer practice 2': ["One more — it's about you!"],
               'Feedback': ['Send ✅ for every “I can”. Rate the lesson!']}
    com = {'Блок школы': 'Пока дети подключаются — здороваемся по именам из чата.',
           'Лексика': 'Называем слова целиком, как на карточке; дети повторяют вслух.',
           'Guided discovery': 'Правило не говорим сами — ждём, пока дети его сформулируют.',
           '⭐ If time': 'Делаем, только если на дриллинге отвечали легко; иначе — сразу к freer practice.',
           'Freer practice 1': 'Читаем вслух 4–5 ответов, хвалим; ошибку исправляем мягко, повтором верной формы.',
           'Freer practice 2': 'Читаем вслух 3–4 ответа.',
           'Feedback': 'После урока — разослать домашнее задание (PPTX / PDF).'}
    for k, dflt in (('goal', goal), ('task', task), ('say', say), ('com', com)):
        cur = P.setdefault(k, {})
        for kk, v in dflt.items():
            cur.setdefault(kk, v)
    return sp
