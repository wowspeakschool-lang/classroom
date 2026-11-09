#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Вычитка собранных дек машиной. Запуск: python3 wowspeak_audit.py final/*.pptx

Что ловит (по списку Ани):
  целостность ссылок · мёртвые кнопки · заметки с неверными номерами слайдов ·
  опечатки и американское написание · текст не влезает · карточка цвета фона ·
  одна картинка на два слова · мелкие иконки · лишнее листание по клику ·
  уровень языка у Beginners · пустые карточки словаря.

Проверять саму проверку: python3 audit_selftest.py — он подкладывает в исправную
деку по одному дефекту и смотрит, ловится ли каждый. Отчёт «0 из N» без этого
ничего не значит: так же выглядел бы отчёт сломанной вычитки.
"""
import sys, os, re, hashlib, collections
from pptx import Presentation
from pptx.util import Emu

AMERICAN={'color':'colour','favorite':'favourite','realize':'realise','organize':'organise',
          'traveling':'travelling','center':'centre','theater':'theatre','gray':'grey',
          'apologize':'apologise','recognize':'recognise','math':'maths'}
# practice в британском - существительное и ошибкой не является; американским
# оно становится только в роли глагола, поэтому ищем формы с to/-d/-s.
VERB_US=[(r'\bto practice\b','to practise'),(r'\bpracticed\b','practised'),
         (r'\bpractices\b','practises'),(r'\bpracticing\b','practising')]
HARD_FOR_A1=['rather than','in spite of','despite','nevertheless','whereas']
# Грамматика выше A1: Present Perfect во всех видах, used to, перфектные модальные.
HARD_RE=[(r"\b(have|has|'ve|'s)\s+(been|seen|done|had|got|made|gone|taken|given|"
          r"found|bought|eaten|written|read|met|told|heard|lost|won|kept|left|"
          r"brought|thought|spent|slept|driven|flown|broken|chosen|forgotten)\b",'Present Perfect'),
         (r'\bused to\b','used to'),
         (r"\b(would|could|should|must)\s+have\b",'перфектный модальный')]
BAD_TYPO=[' teh ',' adn ',' recieve ',' seperate ',' alot ',' thier ']

def inches(v): return (v or 0)/914400.0

def texts(sl):
    out=[]
    for sh in sl.shapes:
        if sh.has_text_frame:
            t=sh.text_frame.text.strip()
            if t: out.append((sh,t))
    return out

def fill_hex(sh):
    try:
        f=sh.fill
        if f.type is not None and f.type==1: return str(f.fore_color.rgb)
    except Exception: pass
    return None

def slide_bg(sl):
    try:
        f=sl.background.fill
        if f.type is not None and f.type==1: return str(f.fore_color.rgb)
    except Exception: pass
    return None

def action_of(sh):
    try:
        ca=sh.click_action
        if ca.target_slide is not None: return 'slide'
        if ca.hyperlink.address: return 'url'
    except Exception: pass
    el=sh._element.find('.//'+'{http://schemas.openxmlformats.org/drawingml/2006/main}hlinkClick')
    if el is None: return None
    return el.get('action') or 'rel'

def audit(path):
    prs=Presentation(path); P=[]
    name=os.path.basename(path)
    # уровень берём из имени файла, но если файл переименовали - из подзаголовка
    # титульного слайда. Иначе правила A1 молча отключаются на копии.
    beginner='Beginners' in name
    if not beginner and len(prs.slides._sldIdLst):
        first=' '.join(sh.text_frame.text for sh in list(prs.slides)[0].shapes if sh.has_text_frame)
        beginner='Beginners' in first

    # ---- картинки: дубли, размер, разрешение
    seen={}
    for i,sl in enumerate(prs.slides,1):
        for sh in sl.shapes:
            if getattr(sh,'image',None) is None: continue
            try: h=hashlib.md5(sh.image.blob).hexdigest()
            except Exception: continue
            w,hh=inches(sh.width),inches(sh.height)
            # узкая, но высокая фигурка человека - норма; плохо, когда мелко по обеим сторонам
            if w<0.9 and hh<0.9: P.append(f'мелкая картинка {w:.2f}x{hh:.2f}" на слайде {i}')
            if min(sh.image.size)<120: P.append(f'картинка низкого разрешения {sh.image.size} на слайде {i}')
            seen.setdefault(h,[]).append(i)

    # ---- пустые карточки словаря
    # Если лист иконок ещё не нарезан, билдер молча рисует пустые карточки:
    # дека собирается, выглядит целой и едет к методисту без картинок.
    if beginner and len(prs.slides._sldIdLst)>5:
        s5=list(prs.slides)[4]
        pics=sum(1 for sh in s5.shapes if getattr(sh,'image',None) is not None)
        if pics<6: P.append(f'на слайде слов только {pics} картинок из 6 - иконки не нарезаны')

    # ---- ссылки и мёртвые кнопки
    for i,sl in enumerate(prs.slides,1):
        for rid,rel in sl.part.rels.items():
            if rel.reltype.endswith('/slide') and rel.target_part not in [s.part for s in prs.slides]:
                P.append(f'ссылка в никуда на слайде {i}')
            if rel.reltype.endswith('/hyperlink'):
                url=str(rel.target_ref)
                if not url.startswith(('http://','https://','ppaction://')):
                    P.append(f'странная ссылка "{url}" на слайде {i}')
        # мёртвая кнопка: небольшая залитая фигура с коротким текстом-указанием,
        # у которой нет действия. Крупные заголовки ("Try again! 🤔") - не кнопки.
        for sh,t in texts(sl):
            low=t.lower()
            if len(t)>40: continue
            try: sz=max([r.font.size.pt for pr in sh.text_frame.paragraphs for r in pr.runs if r.font.size] or [0])
            except Exception: sz=0
            if sz>32 or fill_hex(sh) is None or t.rstrip().endswith('?'): continue
            if any(k in low for k in ('next word','next one','back to','see the result','open the video','→','⬅')):
                if action_of(sh) is None:
                    P.append(f'мёртвая кнопка: "{t[:28]}" на слайде {i}')
        # карточки-варианты в играх: каждая должна кликаться. Проверяем только
        # там, где карточки вообще кликабельны: на mood-слайде их не нажимают.
        opts=[sh for sh in sl.shapes if sh.has_text_frame and fill_hex(sh)
              and 1.6<inches(sh.width)<3.2 and 0.8<inches(sh.height)<2.4]
        if len(opts)>=3 and any(action_of(sh) is not None for sh in opts):
            dead=[sh for sh in opts if action_of(sh) is None]
            if dead: P.append(f'вариант ответа без клика ({len(dead)} шт.) на слайде {i}')

    # ---- карточка цвета фона
    for i,sl in enumerate(prs.slides,1):
        bg=slide_bg(sl)
        if not bg: continue
        for sh in sl.shapes:
            f=fill_hex(sh)
            if not f or f!=bg or action_of(sh) is not None: continue   # ловушка клика - так задумано
            if inches(sh.width)>11 or inches(sh.height)>6: continue     # подложка во весь слайд
            if inches(sh.width)>1.5 and inches(sh.height)>0.8:
                P.append(f'карточка цвета фона ({f}) на слайде {i}')

    # ---- текст не влезает (грубая оценка ёмкости)
    for i,sl in enumerate(prs.slides,1):
        for sh,t in texts(sl):
            try: sizes=[r.font.size.pt for p in sh.text_frame.paragraphs for r in p.runs if r.font.size]
            except Exception: sizes=[]
            if not sizes: continue
            sz=max(sizes); w,h=inches(sh.width)*72,inches(sh.height)*72
            if w<10 or h<10: continue
            per_line=max(1,int(w/(sz*0.5))); lines=max(1,int(h/(sz*1.25)))
            if len(t)>per_line*lines*1.15:
                P.append(f'текст может не влезть ({len(t)} симв., {sz:.0f}pt, '
                         f'{inches(sh.width):.1f}x{inches(sh.height):.1f}") на слайде {i}')

    # ---- наложения: две «живые» фигуры налезают друг на друга
    for i,sl in enumerate(prs.slides,1):
        boxes=[]
        for sh in sl.shapes:
            if getattr(sh,'image',None) is None and not (sh.has_text_frame and sh.text_frame.text.strip()):
                continue
            if inches(sh.width)>11.5 or inches(sh.height)>6.5: continue
            boxes.append((inches(sh.left),inches(sh.top),
                          inches(sh.left)+inches(sh.width),inches(sh.top)+inches(sh.height),sh))
        for a in range(len(boxes)):
            for b in range(a+1,len(boxes)):
                x0,y0,x1,y1,sa=boxes[a]; u0,v0,u1,v1,sb=boxes[b]
                ox=min(x1,u1)-max(x0,u0); oy=min(y1,v1)-max(y0,v0)
                if ox<=0.25 or oy<=0.25: continue
                pic_on_card=(getattr(sa,'image',None) is None)!=(getattr(sb,'image',None) is None)
                if pic_on_card: continue            # картинка внутри карточки - так и надо
                if getattr(sa,'image',None) is not None and getattr(sb,'image',None) is not None:
                    P.append(f'наложение картинок на слайде {i}'); break

    # ---- заметки учителю
    notes=''; notes_idx=None
    for i,sl in enumerate(prs.slides,1):
        for sh,t in texts(sl):
            if 'ONLY FOR THE TEACHER' in t.upper() or 'SLIDE 1-2' in t:
                notes=t; notes_idx=i
    if notes:
        for tok in ('{GAMES}','{VIDEO}','{SPEAKING}','{SERVICE}','{PROP}'):
            if tok in notes: P.append(f'в заметках остался токен {tok}')
        m=re.search(r'SLIDE (\d+):\s*(?:Смотрим|Первый раз|Сначала)',notes)
        if m:
            v=int(m.group(1))
            if 1<=v<=len(prs.slides._sldIdLst):
                has=any(rel.reltype.endswith('/hyperlink') and 'youtu' in str(rel.target_ref)
                        for rel in list(prs.slides)[v-1].part.rels.values())
                if not has: P.append(f'в заметках видео указано на слайде {v}, а ссылки там нет')
            else: P.append(f'в заметках номер слайда {v} вне файла')
    else:
        P.append('не нашёл слайд с заметками учителю')

    # ---- орфография и уровень
    # заметки учителю пишутся по-русски и в проверку языка не идут
    alltext=' '.join(t for sl in prs.slides for _,t in texts(sl)
                     if 'ONLY FOR THE TEACHER' not in t.upper() and 'SLIDE 1-2' not in t)
    low=' '+alltext.lower()+' '
    for a,b in AMERICAN.items():
        if re.search(r'\b'+a+r'\b',low): P.append(f'американское написание "{a}" (британское: {b})')
    for rx,b in VERB_US:
        m=re.search(rx,low)
        if m: P.append(f'американское написание "{m.group(0).strip()}" (британское: {b})')
    for t in BAD_TYPO:
        if t in low: P.append(f'опечатка "{t.strip()}"')
    if beginner:
        for h in HARD_FOR_A1:
            if h in low: P.append(f'сложно для A1: "{h}"')
        for rx,nm in HARD_RE:
            m=re.search(rx,low)
            if m: P.append(f'грамматика выше A1 ({nm}): "{m.group(0)}"')

    # ---- одна картинка на два слова в пределах слайда словаря
    for i,sl in enumerate(prs.slides,1):
        hs=[]
        for sh in sl.shapes:
            if getattr(sh,'image',None) is None: continue
            try: hs.append(hashlib.md5(sh.image.blob).hexdigest())
            except Exception: pass
        dup=[h for h,c in collections.Counter(hs).items() if c>1]
        if dup and i==5: P.append(f'одна картинка на два слова на слайде {i}')
    return P

def main(paths):
    bad=0
    for p in paths:
        P=audit(p)
        if P:
            bad+=1
            print(f'\n=== {os.path.basename(p)}')
            for x,c in collections.Counter(P).items():
                print(f'  [{c}x] {x}' if c>1 else f'  {x}')
    print(f'\nфайлов с замечаниями: {bad} из {len(paths)}')

if __name__=='__main__':
    main(sys.argv[1:])
