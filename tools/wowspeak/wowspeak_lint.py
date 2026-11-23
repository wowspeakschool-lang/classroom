#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Вычитка СПЕКА темы — до сборки, не после.

wowspeak_audit проверяет готовую деку: написание, уровень, вёрстку, мёртвые
кнопки. Но три рода ошибок деку проходят насквозь, потому что в файле всё
красиво, а неправильно оно по смыслу:

1. Реквизит без решения. В «Making holiday plans» было расписание четверых,
   и ни одного дня, свободного для всех. Задание невыполнимо; слайд при этом
   безупречен.
2. Шаблон, который не согласуется со словом. «This is a save», «His promise:
   less screen time» - грамматика формально цела, по-английски не читается.
3. Повтор темы. Повтор отдельных слов Анна разрешила, повтор самой темы - нет.

Запуск:  python3 wowspeak_lint.py t*.py
"""
import importlib.util, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- 1. реквизит
DAYS = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

def _money(s):
    """Число из «1 200 ₽», «400 ₽ / hour», «33 to 45» -> int или None."""
    s = str(s).replace(' ',' ').replace('\xa0',' ')
    m = re.search(r'(\d[\d\s]*)\s*₽', s)
    if not m: return None
    return int(m.group(1).replace(' ',''))

def check_prop(pr, where, bad):
    kind = pr.get('kind')
    if kind == 'week':
        people = pr.get('people') or []
        days   = pr.get('days') or DAYS
        busy   = pr.get('busy') or {}
        if len(people) < 2:
            bad(f'{where}: в расписании меньше двух человек - договариваться не с кем')
        unknown = {d for v in busy.values() for d in v} - set(days)
        if unknown:
            bad(f'{where}: занятые дни, которых нет в сетке: {sorted(unknown)}')
        free = [d for d in days if not any(d in (busy.get(p) or []) for p in people)]
        if not free:
            bad(f'{where}: НЕТ дня, свободного для всех - задача нерешаема')
        elif len(free) > 2:
            bad(f'{where}: свободных для всех дней {len(free)} ({", ".join(free)}) - '
                f'искать нечего, договорятся за десять секунд')
        for p in people:
            if len(busy.get(p) or []) >= len(days):
                bad(f'{where}: у «{p}» занята вся неделя - он не сможет прийти никогда')

    elif kind in ('menu','pricelist'):
        rows = pr.get('rows') or []
        if not rows: bad(f'{where}: прайс-лист пустой')
        if len(rows) > 6: bad(f'{where}: в прайс-листе {len(rows)} строк, на слайде помещается 6')
        budget = _money(pr.get('title','')) or _money(pr.get('hint',''))
        if budget:
            prices = [(w,_money(p)) for w,p in rows]
            named  = [(w,c) for w,c in prices if c]
            if not named:
                bad(f'{where}: бюджет {budget} ₽ назван, а цен в строках нет')
            else:
                if not any(c <= budget for _,c in named):
                    bad(f'{where}: на {budget} ₽ не хватает НИ НА ЧТО - выбирать не из чего')
                if all(c <= budget for _,c in named) and sum(c for _,c in named) <= budget:
                    bad(f'{where}: на {budget} ₽ хватает на ВСЁ сразу - торга не выйдет')

    elif kind == 'route':
        steps = pr.get('steps') or []
        if not 2 <= len(steps) <= 12:
            bad(f'{where}: шагов в ленте {len(steps)} - нужно от 2 до 12')
        if len(set(steps)) != len(steps):
            bad(f'{where}: в ленте повторяются подписи шагов')

    elif kind == 'scale':
        rows, heads = pr.get('rows') or [], pr.get('heads') or ['1','2','3','4','5']
        if not 2 <= len(rows) <= 6: bad(f'{where}: строк в таблице {len(rows)} - нужно от 2 до 6')
        if not 2 <= len(heads) <= 5: bad(f'{where}: колонок {len(heads)} - нужно от 2 до 5')

    elif kind == 'wall':
        words = pr.get('words') or []
        if len(words) > 6: bad(f'{where}: на стене {len(words)} картинок, помещается 6')

# ------------------------------------------------------- 2. шаблон и слово
# Глаголы и начала фраз, перед которыми артикль не ставится. Список намеренно
# короткий: ловим очевидное, спорное оставляем человеку.
VERBS = set("""read eat go do help learn save spend buy study sleep break check share
believe decorate wrap invite bake stay make keep give start remind practise teach
revise panic catch put drink swim cook draw sing play run walk take look set achieve
rent try pay meet agree ask answer skate watch wish celebrate""".split())
NO_ARTICLE_START = ('at ','less ','more ','too ','to ','in ','on ','any ','how ')

def check_template(S, bad):
    tpl = S.get('tf_template')
    words = list(S.get('w1012') or []) + list(S.get('w13') or [])
    games = (S.get('games_beg') or ())
    uses_tf = ('truefalse' in games) if games else True   # без переопределения решает rot
    if not tpl:
        return
    if '{w}' not in tpl:
        bad(f'tf_template без {{w}}: "{tpl}"'); return
    if not re.search(r'\b(a|an)\s*\{w\}', tpl):
        return                                            # артикля нет - придираться не к чему
    for w in words:
        first = w.split()[0].lower()
        if first in VERBS or w.lower().startswith(NO_ARTICLE_START):
            bad(f'шаблон "{tpl}" с артиклем, а слово «{w}» артикля не берёт - '
                f'возьми «The word is: {{w}}.»')
            return

# --------------------------------------------- 2б. форма слова против рамки
# Аня, 23.11.2026, глядя на слайд слов: «фразы с инговым окончанием, но как
# будто бы они не должны быть с инговым. И в speaking project и в других
# заданиях чаще нужны инфинитивы». В «Can boys and girls be best friends?»
# все шесть слов были герундием, а из восьми мест, куда ученик их вставляет,
# -ing подходил ровно одному: «We playing football together» - не предложение.

# что стоит прямо перед пропуском и требует голого инфинитива
BARE = set('we they i you can could must will both never also always please let'.split())
# что требует -ing. Только сильные признаки: «about» и «like» одинаково берут
# и существительное («It is about family», «I like football»), на них проверка
# ругалась на «Holiday Movies» и «Saver or Spender» зря.
GERUND = set('at enjoy practise finish keep stop worth'.split())
# основы, по которым слово на -ing опознаётся как глагольное, а не как
# существительное: stocking, king, bowling, happy ending трогать нельзя
VERB_STEMS = set("""talk play do laugh share walk study game sing swim cook bake draw
edit read write run help work watch eat sleep learn teach practise skate dance
ride drive climb paint build shop travel""".split())

def _is_gerund(word):
    first = word.split()[0].lower()
    if not first.endswith('ing') or len(first) < 5: return False
    stem = first[:-3]
    return stem in VERB_STEMS or stem.rstrip(stem[-1]) in VERB_STEMS or stem+'e' in VERB_STEMS

def _slots(S):
    out = []
    for fr in S.get('frames') or []: out.append(('финал', fr))
    for k in ('it1012','it13'):
        for t,_ in S.get(k) or []: out.append(('мини', t))
    for t,_ in S.get('lead') or []: out.append(('лид-ин', t))
    return [(w,t) for w,t in out if '___' in t]

def check_word_form(S, bad):
    words = list(S.get('w1012') or []) + list(S.get('w13') or [])
    if not words: return
    slots = _slots(S)
    if not slots: return
    bare = ger = 0
    for _,t in slots:
        before = t.split('___')[0].strip().split()
        key = before[-1].lower().strip('.,') if before else ''
        if key in BARE: bare += 1
        elif key in GERUND: ger += 1
    gerunds = [w for w in words if _is_gerund(w)]
    plain   = [w for w in words if not _is_gerund(w)]
    if bare >= 2 and len(gerunds) > len(words)//2:
        ex = next((t for _,t in slots
                   if (t.split('___')[0].strip().split() or [''])[-1].lower() in BARE), '')
        bad(f'слова на -ing ({", ".join(gerunds[:3])}…), а рамок под инфинитив {bare}: '
            f'«{ex.replace("___", gerunds[0])}» не читается')
    # обратный случай: рамки просят герундий, а слова даны инфинитивом. Ругаемся
    # только если слова - действительно глаголы: существительное после «good at»
    # стоит законно («good at maths»).
    verbs = [w for w in plain if w.split()[0].lower() in VERB_STEMS]
    if ger >= 2 and bare == 0 and len(verbs) == len(words) and len(words) >= 4:
        bad(f'рамки требуют -ing ({ger} шт.), а слова даны инфинитивом - проверь форму')
    # слово уже содержит «together», а рамка добавляет его второй раз
    for w in words:
        if 'together' in w.lower():
            for _,t in slots:
                if re.search(r'___\s*together', t):
                    bad(f'«{w}» в рамке «{t}» даёт together дважды'); return

# ------------------------------------ 2в. целевое слово до слайда со словами
# Аня, 23.11.2026: «иногда в презах слова из целевой лексики попадаются до её
# презентации, это не есть очень хорошо». До слайда слов идут только разминка
# и лид-ин - значит там целевых слов быть не должно. Проверка нашла 109 таких
# мест в 23 темах, в четырнадцати лид-ин раздавал по три слова и больше.
# Слово из названия темы не считается: оно и так на титуле.

def _targets(S, keys):
    out = set()
    for k in keys:
        for w in S.get(k) or []:
            out.add((w[0] if isinstance(w, tuple) else w).lower())
    return out

def check_before_vocab(S, bad):
    title = S['theme'].lower()
    for adv, keys, moodk, moodsk, leadk in (
            (False, ('w1012','w13'),     'mood_beg', 'moods_beg', 'lead'),
            (True,  ('adv1012','adv13'), 'mood_adv', 'moods_adv', 'lead_adv')):
        texts = [S.get(moodk) or '']
        texts += [l for _, l in S.get(moodsk) or []]
        texts += [t for t, _ in S.get(leadk) or []]
        leaked = []
        for w in sorted(_targets(S, keys)):
            if len(w) < 3 or w in title: continue
            for t in texts:
                if re.search(r'\b' + re.escape(w) + r'\b', t, re.I):
                    leaked.append((w, t)); break
        if not leaked: continue
        lvl = 'Advanced' if adv else 'Beginners'
        if len(leaked) >= 3:
            bad(f'{lvl}: лид-ин раздаёт словарь - {len(leaked)} целевых слова до слайда слов '
                f'({", ".join(w for w, _ in leaked[:4])})')
        else:
            for w, t in leaked:
                bad(f'{lvl}: «{w}» встречается до слайда слов - «{t}»')

# ----------------------------------------------------------- 3. повтор темы
def words_of(S):
    out = set()
    for k in ('w1012','w13'):
        out |= {w.lower() for w in (S.get(k) or [])}
    for k in ('adv1012','adv13'):
        out |= {w.lower() for w,_ in (S.get(k) or [])}
    return out

def check_bank(specs, bad):
    bank = os.path.join(HERE,'WORD_BANK.md')
    known = open(bank,encoding='utf-8').read().lower() if os.path.exists(bank) else ''
    titles = {}
    for name,S in specs:
        t = S['theme'].strip().lower()
        if t in titles: bad(f'{name}: тема «{S["theme"]}» уже есть в {titles[t]}')
        titles[t] = name
        # ищем именно строку банка «- **Тема** — слова», а не любое вхождение:
        # «Christmas» встречается в банке внутри чужих слов и проходила молча
        if f'**{S["theme"]}**'.lower() not in known:
            bad(f'{name}: темы «{S["theme"]}» нет в WORD_BANK.md - допиши строку')
    for i in range(len(specs)):
        for j in range(i+1,len(specs)):
            (n1,s1),(n2,s2) = specs[i],specs[j]
            common = words_of(s1) & words_of(s2)
            if len(common) >= 4:
                bad(f'{n1} и {n2}: общих слов {len(common)} '
                    f'({", ".join(sorted(common)[:6])}) - темы начинают сливаться')

# ------------------------------------------------------------------- запуск
def load(path):
    spec = importlib.util.spec_from_file_location('spec_'+os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    sys.argv = [path]                       # чтобы спек не ушёл в сборку
    spec.loader.exec_module(mod)
    return mod.S

def main(paths):
    specs, total = [], 0
    for p in paths:
        name = os.path.basename(p)
        try: S = load(p)
        except Exception as e:
            print(f'=== {name}\n  спек не читается: {e}\n'); total += 1; continue
        specs.append((name,S))
        found = []
        bad = found.append
        for key in [k for k in S if k=='prop' or k.startswith('prop_')]:
            if key == 'prop_note': continue
            pr = S[key]
            if isinstance(pr,dict) and pr.get('kind'): check_prop(pr,key,bad)
        check_template(S,bad)
        check_word_form(S,bad)
        check_before_vocab(S,bad)
        if found:
            print(f'=== {name}')
            for f in found: print('  '+f)
            print()
            total += len(found)
    shared = []
    check_bank(specs, shared.append)
    if shared:
        print('=== словарь и темы')
        for f in shared: print('  '+f)
        print()
        total += len(shared)
    print(f'замечаний: {total} на {len(specs)} темах')
    return 1 if total else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or sorted(
        os.path.join(HERE,f) for f in os.listdir(HERE) if re.match(r't\d+_.*\.py$',f))))
