#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WOW Speak in-deck games. No WordWall, no internet, no accounts.

Two mechanisms underneath:
  * slide-to-slide hyperlinks (work in every viewer);
  * real PowerPoint "Appear / Disappear on click" animations, written straight
    into the slide's <p:timing>.

THE RULES (each one was paid for - do not break them)
 1. One card = one shape, text INSIDE the shape (btn / card_text). A label on
    top of a button eats the click (only the thin rim stays alive) and an
    animated card made of three objects needs three clicks to vanish.
    A picture on top is allowed, but it needs the same link, and for animation
    the card and the picture are passed as ONE group.
 2. The task must be honest - captions must not give the answer away. Captions
    live only on the New Words slide. No captions and no give-away emoji in the
    quiz, in "what's missing" and on the board.
 3. One round PER WORD, not one round per lesson. Right -> next word, wrong ->
    same question again. Counter 1/6 ... 6/6 in the corner, final slide at the end.
 4. The correct answer never walks 1-2-3-4: its position is (k*3) % nopt.
 5. A click past a button must not flip the slide -> no_click_advance() on the
    quiz and on the board. It also puts a small '→' in the corner, so the teacher
    is never stuck on a slide where clicks do nothing.
 6. Service screens go to the END of the file via finish(prs, helpers).
 7. Feedback screens carry a real button ('Next word' / 'Back to the question').
    The whole slide is linked too, but a button is what the teacher can see and
    aim at - 'click anywhere' looks broken when a click does nothing.
 8. A card must never be the colour of the slide background -> pal(bg, i),
    never PASTELS[i % 6].
 9. Rewrite the teacher notes for the games (F5 only, click past a button does
    not advance, captions removed on purpose).
10. The deck gets longer. If the lesson does not fit, cut rounds knowingly
    (new or hard words only).
"""
import os
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml

import wowspeak_builder as B

PICS=('.png','.jpg','.jpeg','.webp','.gif','.bmp')
# Card colours. Deliberately NOT B.PASTELS - those are the slide backgrounds.
CARD_COLOURS=['FFB6D9','A9D6FF','FFE89A','C9B3F0','9EE9C6','FFC79E']
GREEN='2E9E5B'; AMBER='E8A33D'

# ----------------------------------------------------------------- basics
def pal(bgc,i):
    """Card colour #i that can never come out equal to the slide background."""
    bgc=(bgc or '').upper().lstrip('#')
    cand=[c for c in CARD_COLOURS if c.upper()!=bgc] or CARD_COLOURS
    return cand[i%len(cand)]

def card_text(sh,txt,size=20,col=None,bold=True,font=None,emoji=''):
    """Write the text INSIDE the shape (rule 1)."""
    col=col or B.INK
    tf=sh.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    for m in ('left','right','top','bottom'): setattr(tf,f'margin_{m}',Pt(3))
    p=tf.paragraphs[0]; p.alignment=PP_ALIGN.CENTER
    if emoji:
        r=p.add_run(); r.text=emoji+' '; r.font.size=Pt(size); r.font.bold=bold; r.font.name=B.BF; r.font.color.rgb=B.C(col)
    r=p.add_run(); r.text=txt; r.font.size=Pt(size); r.font.bold=bold
    r.font.name=font or (B.BF if _is_emoji_only(txt) else B.TF); r.font.color.rgb=B.C(col)
    return sh

def _is_emoji_only(t):
    return bool(t) and all(ord(c)>0x2190 or c==' ' for c in t)

def btn(slide,x,y,w,h,txt='',fill=None,size=20,col=None,target=None,url=None,rad=0.14,bold=True,font=None,shade=True):
    """One shape = one card = one button. Text lives inside it."""
    sh=B.card(slide,x,y,w,h,fill=fill or B.WHITE,rad=rad,sh=shade)
    if txt: card_text(sh,txt,size=size,col=col,bold=bold,font=font)
    if target is not None: sh.click_action.target_slide=target
    if url: sh.click_action.hyperlink.address=url
    return sh

def media_on(slide,sh,media,pad=0.22,size=60,target=None,url=None,panel=True):
    """Put a picture (or a big emoji) on the card. Everything laid on top of the
    card swallows the click, so every piece gets the SAME link (rule 1) and the
    whole lot is returned as one list - that is also the animation group.
    The picture sits on a white panel: icons are cut from a white sheet, and
    without the panel a bare white rectangle shows on the coloured card."""
    if not media: return []
    x,y=sh.left/914400.0,sh.top/914400.0
    w,h=sh.width/914400.0,sh.height/914400.0
    if isinstance(media,str) and media.lower().endswith(PICS):
        if not os.path.exists(media): return []
        out=[]
        if panel: out.append(B.card(slide,x+pad,y+pad,w-2*pad,h-2*pad,fill=B.WHITE,rad=0.12,sh=False))
        q=pad+(0.14 if panel else 0.0)
        out.append(B.fit(slide,media,x+q,y+q,w-2*q,h-2*q))
        if target is None and url is None:
            try: target=sh.click_action.target_slide
            except Exception: target=None
        for e in out:
            if target is not None: e.click_action.target_slide=target
            elif url: e.click_action.hyperlink.address=url
        return out
    card_text(sh,media,size=size,font=B.BF)   # emoji straight into the shape
    return []

def _bg_of(slide,default=B.WHITE):
    try: return str(slide.background.fill.fore_color.rgb)
    except Exception: return default

def _backdrop(slide,bg=None):
    """A full-slide rectangle in the background colour, pushed to the very back:
    invisible, but it catches every click that misses a button."""
    sh=slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,0,0,B.Emu(12192000),B.Emu(6858000))
    sh.fill.solid(); sh.fill.fore_color.rgb=B.C(bg or _bg_of(slide))
    sh.line.fill.background(); sh.shadow.inherit=False
    el=sh._element; tree=el.getparent(); tree.remove(el); tree.insert(2,el)
    return sh

def _action(sh,action):
    """Write a built-in PowerPoint click action (noaction / nextslide)."""
    cNvPr=sh._element._nvXxPr.cNvPr
    for h in cNvPr.findall(qn('a:hlinkClick')): cNvPr.remove(h)
    hl=cNvPr.makeelement(qn('a:hlinkClick'),{qn('r:id'):'','action':action})
    ext=cNvPr.find(qn('a:extLst'))
    ext.addprevious(hl) if ext is not None else cNvPr.append(hl)
    return sh

def link_whole_slide(slide,target,bg=None):
    """Rule 7: the whole slide becomes one big button. A no-fill shape only reacts
    on its rim, so the catcher is painted in the background colour instead."""
    sh=_backdrop(slide,bg); sh.click_action.target_slide=target
    return sh

def next_arrow(slide,x=0.42,y=6.78,w=0.8,h=0.5):
    """A small '→' in the corner that fires PowerPoint's built-in Next Slide action.
    It needs no target, so it keeps working after finish() reorders the file - and
    it gives the teacher a way forward on a slide where clicks are switched off."""
    sh=B.card(slide,x,y,w,h,fill=B.WHITE,rad=0.4,sh=False)
    card_text(sh,'→',size=18,col='8A7AA8',font=B.BF)
    return _action(sh,'ppaction://hlinkshowjump?jump=nextslide')

def no_click_advance(slide,arrow=True,bg=None):
    """Rule 5: a click past a button must not flip the slide.

    Done with an invisible click-catcher carrying PowerPoint's 'no action', not
    with <p:transition advClick="0">: the transition switch also kills the clicks
    the teacher expects to work, and that reads as 'the game slide is stuck'.
    The '→' in the corner is the way on."""
    sh=_action(_backdrop(slide,bg),'ppaction://noaction')
    if arrow: next_arrow(slide)
    return sh

# ------------------------------------------------------- click animations
_P='http://schemas.openxmlformats.org/presentationml/2006/main'

def _eff(ids,spid,kind,first):
    cid=next(ids); bid=next(ids)
    cls='entr' if kind=='entr' else 'exit'
    val='visible' if kind=='entr' else 'hidden'
    node='clickEffect' if first else 'withEffect'
    return (f'<p:par><p:cTn id="{cid}" presetID="1" presetClass="{cls}" presetSubtype="0" '
            f'fill="hold" grpId="0" nodeType="{node}">'
            f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst><p:set><p:cBhvr>'
            f'<p:cTn id="{bid}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
            f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>'
            f'<p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
            f'<p:to><p:strVal val="{val}"/></p:to></p:set></p:childTnLst></p:cTn></p:par>')

def animate(slide,steps):
    """steps = [(kind, [shape|group of shapes]), ...] - one mouse click per step.
    kind: 'entr' (Appear) or 'exit' (Disappear). Everything inside one step
    happens on the same click (rule 1: card + picture travel together)."""
    steps=[s for s in steps if s[1]]
    if not steps: return None
    ids=iter(range(2,100000)); seq=next(ids); clicks=[]
    for kind,shapes in steps:
        if not isinstance(shapes,(list,tuple)): shapes=[shapes]
        spids=[sh.shape_id for sh in shapes if sh is not None]
        if not spids: continue
        outer=next(ids); inner=next(ids)
        effs=''.join(_eff(ids,sp,kind,i==0) for i,sp in enumerate(spids))
        clicks.append(f'<p:par><p:cTn id="{outer}" fill="hold">'
                      f'<p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>'
                      f'<p:par><p:cTn id="{inner}" fill="hold">'
                      f'<p:stCondLst><p:cond delay="0"/></p:stCondLst>'
                      f'<p:childTnLst>{effs}</p:childTnLst></p:cTn></p:par>'
                      f'</p:childTnLst></p:cTn></p:par>')
    cond=('<p:cond evt="{e}" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond>')
    xml=(f'<p:timing xmlns:p="{_P}"><p:tnLst><p:par>'
         f'<p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
         f'<p:seq concurrent="1" nextAc="seek"><p:cTn id="{seq}" dur="indefinite" nodeType="mainSeq">'
         f'<p:childTnLst>{"".join(clicks)}</p:childTnLst></p:cTn>'
         f'<p:prevCondLst>{cond.format(e="onPrev")}</p:prevCondLst>'
         f'<p:nextCondLst>{cond.format(e="onNext")}</p:nextCondLst>'
         f'</p:seq></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>')
    sld=slide._element
    for t in sld.findall(qn('p:timing')): sld.remove(t)
    tim=parse_xml(xml); sld.append(tim)
    return tim

# ------------------------------------------------------------- structure
def finish(prs,helpers):
    """Rule 6: push every service screen to the very end of the file, so that
    arrowing through the lesson never lands on 'Correct / Try again'."""
    lst=prs.slides._sldIdLst; els=list(lst)
    by_id={prs.slides[i].slide_id:els[i] for i in range(len(els))}
    seen=set()
    for sl in helpers:
        if sl is None or sl.slide_id in seen: continue
        seen.add(sl.slide_id); el=by_id[sl.slide_id]
        lst.remove(el); lst.append(el)
    return prs

def _head(slide,title,bg,counter=None,dark=False):
    B.band(slide,title,dark=dark,size=28)
    if counter:
        c=B.card(slide,11.75,0.5,1.35,0.7,fill=B.WHITE if not dark else '3A2E55',rad=0.4)
        card_text(c,counter,size=19,col=B.HOTPINK if not dark else B.GOLD)
    B.logo(slide,dark=dark)

# ------------------------------------------------------------ THE GAMES
def g_quiz_series(prs,bg,items,helpers=None,title=None,mode='picture',nopt=4,
                  final='🏆 Well done! You know all the words!'):
    """A round for EVERY word (rule 3).
    items : [(word, media)] for mode='picture' (media = icon path or emoji)
            [(word, definition)] for mode='word'
    Right answer -> 'Correct' -> next word. Wrong -> 'Try again' -> same word."""
    helpers=[] if helpers is None else helpers
    n=len(items); nopt=max(2,min(nopt,n))
    qs=[B.new_slide(prs,bg) for _ in range(n)]
    fin=B.new_slide(prs,bg)
    outs=[]
    for k in range(n):
        ok=B.new_slide(prs,GREEN); bad=B.new_slide(prs,AMBER)
        outs.append((ok,bad)); helpers+=[ok,bad]
    for k,(word,extra) in enumerate(items):
        s=qs[k]; ok,bad=outs[k]
        nxt=qs[k+1] if k+1<n else fin
        q=f'Which one is "{word}"?' if mode=='picture' else f'Which word means: "{extra}"?'
        _head(s,title or ('🎯 Point & Race!' if mode=='picture' else '🎯 Word hunt!'),bg,counter=f'{k+1}/{n}')
        B.text(s,0.9,1.62,11.5,0.7,[[(q,22,'5A4A7A',True,B.TF)]],align=PP_ALIGN.CENTER)
        pos=(k*3)%nopt                                  # rule 4
        order=[None]*nopt; order[pos]=k
        others=[(k+1+j)%n for j in range(n-1)][:nopt-1]
        for slot in range(nopt):
            if order[slot] is None: order[slot]=others.pop(0)
        cw=min(2.75,(11.6-(nopt-1)*0.35)/nopt); gap=0.35
        gx=(B.SLIDE_W-(nopt*cw+(nopt-1)*gap))/2
        gy,ch=(2.5,3.3) if mode=='picture' else (3.0,2.1)
        for slot,idx in enumerate(order):
            x=gx+slot*(cw+gap)
            tgt=ok if idx==k else bad
            c=btn(s,x,gy,cw,ch,fill=pal(bg,slot),target=tgt)
            if mode=='picture': media_on(s,c,items[idx][1],target=tgt)
            else: card_text(c,items[idx][0],size=24,col=B.INK)
        no_click_advance(s)                              # rule 5
        # feedback screens: a real button to press (rule 7). The whole slide is
        # linked as well, but the button is the one the teacher aims at - an
        # invisible click-anywhere layer is not something you can see or trust.
        link_whole_slide(ok,nxt,GREEN)
        B.text(ok,1.0,1.95,11.3,1.4,[[('YES! Correct! 🎉',54,B.GOLD,True,B.TF)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        btn(ok,4.2,3.95,4.93,1.05,'Next word  →' if k+1<n else 'See the result  →',
            fill=B.GOLD,size=24,col='1B6B3F',rad=0.4,target=nxt)
        link_whole_slide(bad,s,AMBER)
        B.text(bad,1.0,1.95,11.3,1.4,[[('Try again! 🤔',54,B.WHITE,True,B.TF)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        btn(bad,4.2,3.95,4.93,1.05,'↩  Back to the question',fill=B.WHITE,size=22,col='A35C0E',rad=0.4,target=s)
    B.blob(fin,0.4,0.6,3.2,B.BLOB[2]); B.blob(fin,12.8,7.0,3.6,B.BLOB[1])
    c=B.card(fin,2.6,2.3,8.13,2.4,fill=B.WHITE,rad=0.25)
    card_text(c,final,size=30,col=B.HOTPINK)
    B.text(fin,1.5,5.1,10.3,0.8,[[('⭐ 🎉 ⭐ 🎉 ⭐',40,B.INK,False,B.BF)]],align=PP_ALIGN.CENTER)
    B.logo(fin)
    return helpers

def g_quiz(prs,bg,items,helpers=None,**kw):
    """Same quiz on emoji instead of icons (items = [(word, '🐶')])."""
    return g_quiz_series(prs,bg,items,helpers,**kw)

def _missing_board(prs,bg,items,title,subtitle,hide=()):
    """One 'what's missing' screen. hide = indexes of the cards already gone."""
    s=B.new_slide(prs,bg); _head(s,title,bg)
    B.text(s,0.9,1.6,11.5,0.6,[[(subtitle,18,'5A4A7A',True,B.TF)]],align=PP_ALIGN.CENTER)
    n=len(items); cols=3 if n>4 else n
    cw=min(3.3,(11.5-(cols-1)*0.4)/cols); gap=0.4; rows=(n+cols-1)//cols
    ch=min(2.2,(4.45-(rows-1)*0.3)/rows)          # keep clear of the logo line
    gx=(B.SLIDE_W-(cols*cw+(cols-1)*gap))/2; gy=2.35
    groups=[]
    for i,(word,media) in enumerate(items):
        if i in hide: groups.append([]); continue
        r=i//cols; c=i%cols; x=gx+c*(cw+gap); y=gy+r*(ch+0.3)
        sh=B.card(s,x,y,cw,ch,fill=pal(bg,i))     # rule 8
        groups.append([sh]+media_on(s,sh,media,size=66))   # rule 1: one click
    B.logo(s)
    return s,groups

def g_missing_pics(prs,bg,items,helpers=None,title='👀 What is missing?',order=None,
                   rounds=None,anim=False):
    """The card really disappears. items = [(word, media)].

    anim=False (default): every step is its own slide, so it can only work -
    a click or the arrow key takes the class to the next screen.
    anim=True: one slide with PowerPoint 'Disappear on click' in <p:timing>.
    Same thing on screen; the animated version is the one to test in PowerPoint."""
    helpers=[] if helpers is None else helpers
    n=len(items)
    seq=list(order) if order is not None else [(i*3+1)%n for i in range(n)]
    seen=[]
    for i in seq:
        if 0<=i<n and i not in seen: seen.append(i)
    seen+=[i for i in range(n) if i not in seen]
    seen=seen[:rounds or min(n,4)]
    look='Look and remember. Then say what disappeared!'
    if anim:
        s,groups=_missing_board(prs,bg,items,title,look)
        animate(s,[('exit',groups[i]) for i in seen])
        return helpers
    _missing_board(prs,bg,items,title,look)
    gone=[]
    for i in seen:
        gone.append(i)
        _missing_board(prs,bg,items,title,'What is missing? Say the word!',hide=set(gone))
    return helpers

def g_missing_anim(prs,bg,items,helpers=None,**kw):
    """Same game on emoji (items = [(word,'🍂')]) - no icons needed."""
    return g_missing_pics(prs,bg,items,helpers,**kw)

def g_reveal(prs,bg,lines,helpers=None,title='💡 Answers',subtitle=None):
    """Answers appear one per click. lines = ['...', ...] or [(left, right)]."""
    helpers=[] if helpers is None else helpers
    s=B.new_slide(prs,bg)
    _head(s,title,bg)
    if subtitle:
        B.text(s,0.9,1.6,11.5,0.6,[[(subtitle,18,'5A4A7A',True,B.TF)]],align=PP_ALIGN.CENTER)
    n=len(lines); top=2.3; h=min(0.95,(4.9-(n-1)*0.18)/max(n,1)); gap=0.18
    steps=[]
    for i,ln in enumerate(lines):
        y=top+i*(h+gap)
        if isinstance(ln,(list,tuple)):
            left,right=ln
            B.text(s,1.3,y,5.2,h,[[(left,19,B.INK,True,B.BF)]],align=PP_ALIGN.LEFT,anchor=MSO_ANCHOR.MIDDLE)
            sh=B.card(s,6.6,y,5.4,h,fill=pal(bg,i)); card_text(sh,right,size=19,col=B.INK)
        else:
            sh=B.card(s,2.2,y,8.9,h,fill=pal(bg,i)); card_text(sh,ln,size=19,col=B.INK)
        steps.append(('entr',[sh]))
    animate(s,steps)
    B.logo(s)
    return helpers

def g_board(prs,bg,questions,helpers=None,title='🎲 Choose a number!',back='⬅️ Back to the board'):
    """Clickable board: number -> question -> back. Question screens are service
    slides and end up at the end of the file (rule 6)."""
    helpers=[] if helpers is None else helpers
    board=B.new_slide(prs,bg)
    _head(board,title,bg)
    n=len(questions); rows=max(1,-(-n//5)); cols=-(-n//rows)
    cw=min(2.4,(11.4-(cols-1)*0.4)/cols); ch=min(2.0,(4.7-(rows-1)*0.35)/rows)
    gx=(B.SLIDE_W-(cols*cw+(cols-1)*0.4))/2
    gy=2.0+max(0.0,(4.7-(rows*ch+(rows-1)*0.35))/2)
    for i,q in enumerate(questions):
        qs=B.new_slide(prs,bg); helpers.append(qs)
        r=i//cols; c=i%cols
        btn(board,gx+c*(cw+0.4),gy+r*(ch+0.35),cw,ch,txt=str(i+1),fill=pal(bg,i),size=40,target=qs)
        _head(qs,f'Question {i+1}',bg)
        card=B.card(qs,1.3,2.0,10.73,3.0,fill=B.WHITE,rad=0.1)
        card_text(card,q,size=26,col=B.INK,bold=True)
        btn(qs,4.9,5.4,3.53,0.85,txt=back,fill=pal(bg,i),size=17,target=board)
        no_click_advance(qs,arrow=False)                  # rule 5 ('⬅️ Back' is the way out)
    no_click_advance(board)
    return helpers

# --------------------------------------------------- builder entry point
# -------------------------------------------------- общие части игр
def _tmpdir():
    """Куда класть сгенерированные картинки (тени, увеличенные куски)."""
    import tempfile
    d=os.path.join(tempfile.gettempdir(),'wowspeak_media'); os.makedirs(d,exist_ok=True); return d

def _ink_box(a):
    """Рамка вокруг нарисованного: всё, что не белое."""
    import numpy as np
    m=(np.abs(a-255).sum(axis=2)>40)
    if not m.any(): return None
    ys,xs=np.where(m)
    return int(xs.min()),int(ys.min()),int(xs.max())+1,int(ys.max())+1

def fit_size(txt,base=24,wide=14,floor=12):
    """Кегль для текста ВНУТРИ кнопки: длинная фраза иначе вылезает за край.
    Функциональные темы держат на карточке целую реплику, а не слово."""
    n=len(str(txt))
    if n<=wide: return base
    return max(floor,round(base*wide/n,1))

def _feedback(prs,q,nxt,last=False,helpers=None):
    """Два служебных экрана к одному вопросу: Correct и Try again.
    На каждом - настоящая кнопка (правило 7), слайд целиком тоже кликается."""
    helpers=[] if helpers is None else helpers
    ok=B.new_slide(prs,GREEN); bad=B.new_slide(prs,AMBER)
    helpers+=[ok,bad]
    link_whole_slide(ok,nxt,GREEN)
    B.text(ok,1.0,1.95,11.3,1.4,[[('YES! Correct! 🎉',54,B.GOLD,True,B.TF)]],
           align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    btn(ok,4.2,3.95,4.93,1.05,'See the result  →' if last else 'Next one  →',
        fill=B.GOLD,size=24,col='1B6B3F',rad=0.4,target=nxt)
    link_whole_slide(bad,q,AMBER)
    B.text(bad,1.0,1.95,11.3,1.4,[[('Try again! 🤔',54,B.WHITE,True,B.TF)]],
           align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    btn(bad,4.2,3.95,4.93,1.05,'↩  Back to the question',fill=B.WHITE,size=22,
        col='A35C0E',rad=0.4,target=q)
    return ok,bad

def _win(prs,bg,final='🏆 Well done!'):
    s=B.new_slide(prs,bg)
    B.blob(s,0.4,0.6,3.2,B.BLOB[2]); B.blob(s,12.8,7.0,3.6,B.BLOB[1])
    c=B.card(s,2.6,2.3,8.13,2.4,fill=B.WHITE,rad=0.25)
    card_text(c,final,size=30,col=B.HOTPINK)
    B.text(s,1.5,5.1,10.3,0.8,[[('⭐ 🎉 ⭐ 🎉 ⭐',40,B.INK,False,B.BF)]],align=PP_ALIGN.CENTER)
    B.logo(s)
    return s

# ------------------------------------------------- картинка -> другой вид
def silhouette(path,col='4A3B6E'):
    """Тень предмета: цвет убираем, форму и внутренние грани оставляем.
    Плоская заливка превращала карту, чемодан и снеки в три одинаковых пятна -
    задание становилось угадайкой. Яркость пикселя переходит в оттенок одного
    цвета: сгибы и колёса видно, а цвет не подсказывает."""
    from PIL import Image, ImageDraw
    import numpy as np
    im=Image.open(path).convert('RGB'); a=np.asarray(im).astype(float)
    ink=(np.abs(a-255).sum(axis=2)>40)
    flat=Image.fromarray(np.where(ink,0,255).astype('uint8'),'L').copy()
    # .copy() обязателен: у картинки на буфере floodfill молча ничего не делает
    for xy in ((0,0),(im.width-1,0),(0,im.height-1),(im.width-1,im.height-1)):
        ImageDraw.floodfill(flat,xy,128)
    body=(np.asarray(flat)!=128)                  # объект вместе с дырками внутри
    base=np.array([int(col[i:i+2],16) for i in (0,2,4)],dtype=float)
    k=(0.55+0.45*(a.mean(axis=2)/255.0))[...,None]
    out=np.full(a.shape,255.0)
    out[body]=np.clip(base*k[body],0,255)
    o=os.path.join(_tmpdir(),'sil_%x.png'%abs(hash(path)))
    Image.fromarray(out.astype('uint8')).save(o); return o

def zoom(path,frac=0.45,bias=0.45):
    """Кусок рисунка крупно - "слишком близко, что это?".

    Окно выбирается по содержимому, а не по центру: центр предмета часто пуст
    (у смартфона там чистый экран, у монитора - стык подставки), и в игре
    появлялся белый прямоугольник. Считаем плотность краски, плотность контуров
    (у морды кота их больше, чем у живота) и сдвигаем вверх - у персонажа
    опознаётся лицо, а не ботинки. Предмет, нарисованный одним контуром,
    показываем почти целиком: узнаваем силуэт, а не выдуманная деталь."""
    from PIL import Image
    import numpy as np
    im=Image.open(path).convert('RGB'); a=np.asarray(im).astype(float)
    bb=_ink_box(a.astype(int))
    if bb is None: return path
    x0,y0,x1,y1=bb
    ink=(np.abs(a-255).sum(axis=2)>40)
    m=a.mean(axis=2)
    grad=np.abs(np.diff(m,axis=0,prepend=m[:1]))+np.abs(np.diff(m,axis=1,prepend=m[:,:1]))
    fr=0.9 if float(ink[y0:y1,x0:x1].mean())<0.25 else frac
    w=max(24,int((x1-x0)*fr)); h=max(24,int((y1-y0)*fr))
    span=max(1,(y1-y0)-h); best=None
    for ty in np.linspace(y0,max(y0,y1-h),9):
        for tx in np.linspace(x0,max(x0,x1-w),9):
            tx=int(tx); ty=int(ty)
            win=ink[ty:ty+h,tx:tx+w]
            if win.size==0: continue
            score=(grad[ty:ty+h,tx:tx+w].mean()*(win.mean()**0.5)
                   *(1.0-bias*((ty-y0)/span)))
            if best is None or score>best[0]: best=(score,tx,ty)
    if best is None: return path
    _,tx,ty=best
    cut=im.crop((tx,ty,min(im.width,tx+w),min(im.height,ty+h)))
    o=os.path.join(_tmpdir(),'zoom_%x.png'%abs(hash(path)))
    cut.resize((cut.width*3,cut.height*3),Image.LANCZOS).save(o)
    return o

# --------------------------------------------------------- картинка -> слово
def g_pic2word(prs,bg,items,helpers=None,style='plain',nopt=4,
               title=None,final='🏆 You named them all!'):
    """Картинка одна, выбираем из четырёх СЛОВ - зеркало квиза.
    style: plain - как есть; silhouette - только тень; zoom - кусок крупно.
    Подписей под картинкой нет: иначе задание проверяет чтение."""
    helpers=[] if helpers is None else helpers
    titles={'plain':'🔎 Look and say!','silhouette':'🌑 Shadow game!','zoom':'🔍 Too close!'}
    subs={'plain':'What is it? Choose the word.',
          'silhouette':'Only the shadow is left. What is it?',
          'zoom':'Way too close. What are we looking at?'}
    n=len(items); nopt=max(2,min(nopt,n))
    qs=[B.new_slide(prs,bg) for _ in range(n)]
    fin=_win(prs,bg,final)
    for k,(word,media) in enumerate(items):
        s=qs[k]; nxt=qs[k+1] if k+1<n else fin
        ok,bad=_feedback(prs,s,nxt,last=(k+1==n),helpers=helpers)
        _head(s,title or titles[style],bg,counter=f'{k+1}/{n}')
        B.text(s,0.9,1.5,11.5,0.6,[[(subs[style],20,'5A4A7A',True,B.TF)]],align=PP_ALIGN.CENTER)
        shown=media
        if isinstance(media,str) and media.lower().endswith(PICS) and os.path.exists(media):
            if style=='silhouette': shown=silhouette(media)
            elif style=='zoom': shown=zoom(media)
        c=B.card(s,4.55,2.15,4.23,2.9,fill=B.WHITE,rad=0.2)
        media_on(s,c,shown,size=90,panel=False)
        pos=(k*3)%nopt
        order=[None]*nopt; order[pos]=k
        others=[(k+1+j)%n for j in range(n-1)][:nopt-1]
        for slot in range(nopt):
            if order[slot] is None: order[slot]=others.pop(0)
        cw=min(2.75,(11.6-(nopt-1)*0.35)/nopt); gx=(B.SLIDE_W-(nopt*cw+(nopt-1)*0.35))/2
        for slot,idx in enumerate(order):
            x=gx+slot*(cw+0.35)
            c2=btn(s,x,5.3,cw,1.1,fill=pal(bg,slot),target=ok if idx==k else bad)
            card_text(c2,items[idx][0],size=fit_size(items[idx][0],22,13),col=B.INK)
        no_click_advance(s)
    return helpers

# ------------------------------------------------------------ открой карточку
def g_flip(prs,bg,items,helpers=None,title='🃏 Flip a card!',
           prompt='Say a sentence with this word! 🗣️',back='⬅️ Back to the cards'):
    """Доска из рубашек: номер открывает карточку, по ней строят предложение.
    Отвечает не один ученик, а тот, чей номер выпал."""
    helpers=[] if helpers is None else helpers
    board=B.new_slide(prs,bg); _head(board,title,bg)
    B.text(board,0.9,1.5,11.5,0.5,[[(prompt,18,'5A4A7A',True,B.TF)]],align=PP_ALIGN.CENTER)
    n=len(items); cols=3 if n>4 else n; rows=-(-n//cols)
    cw=min(3.3,(11.4-(cols-1)*0.4)/cols); ch=min(2.1,(4.3-(rows-1)*0.35)/rows)
    gx=(B.SLIDE_W-(cols*cw+(cols-1)*0.4))/2; gy=2.2
    for i,(word,media) in enumerate(items):
        face=B.new_slide(prs,bg); helpers.append(face)
        _head(face,title,bg,counter=f'{i+1}/{n}')
        c=B.card(face,4.55,1.95,4.23,3.0,fill=B.WHITE,rad=0.2)
        media_on(face,c,media,size=90,panel=False)
        B.text(face,1.0,5.15,11.3,0.6,[[(word,30,B.HOTPINK,True,B.TF)]],align=PP_ALIGN.CENTER)
        B.text(face,1.0,5.8,11.3,0.5,[[(prompt,17,'5A4A7A',True,B.BF)]],align=PP_ALIGN.CENTER)
        btn(face,9.6,6.45,3.2,0.75,back,fill=B.WHITE,size=16,col=B.INK,rad=0.4,target=board)
        no_click_advance(face,arrow=False)
        r=i//cols; c2=i%cols
        sh=btn(board,gx+c2*(cw+0.4),gy+r*(ch+0.35),cw,ch,fill=pal(bg,i),target=face)
        card_text(sh,str(i+1),size=40,col=B.INK)
    no_click_advance(board)
    return helpers

# ------------------------------------------------------------- лишнее слово
def g_odd(prs,bg,rounds,helpers=None,title='🚫 Odd one out!',
          ask='Which one does NOT belong?',final='🏆 Sharp eyes!'):
    """rounds = [([четыре слова], индекс лишнего)]. Ответ проверяемый, а
    объяснять, почему лишнее, они будут словами - ради этого игра и нужна."""
    helpers=[] if helpers is None else helpers
    n=len(rounds)
    qs=[B.new_slide(prs,bg) for _ in range(n)]
    fin=_win(prs,bg,final)
    for k,(words,odd) in enumerate(rounds):
        s=qs[k]; nxt=qs[k+1] if k+1<n else fin
        ok,bad=_feedback(prs,s,nxt,last=(k+1==n),helpers=helpers)
        _head(s,title,bg,counter=f'{k+1}/{n}')
        B.text(s,0.9,1.5,11.5,0.6,[[(ask,20,'5A4A7A',True,B.TF)]],align=PP_ALIGN.CENTER)
        m=len(words); cw=min(2.75,(11.6-(m-1)*0.35)/m); gx=(B.SLIDE_W-(m*cw+(m-1)*0.35))/2
        for i,w in enumerate(words):
            c=btn(s,gx+i*(cw+0.35),2.9,cw,2.1,fill=pal(bg,i),target=ok if i==odd else bad)
            card_text(c,w,size=fit_size(w,22,13),col=B.INK)
        B.text(s,0.9,5.5,11.5,0.5,[[('…and say why! 🗣️',18,B.HOTPINK,True,B.TF)]],align=PP_ALIGN.CENTER)
        no_click_advance(s)
    return helpers

# -------------------------------------------------------------------- табу
def g_taboo(prs,bg,cards,helpers=None,title='🤐 Taboo!',back='⬅️ Back to the words'):
    """cards = [(слово, [три запрещённых])]. Объясняешь слово, не называя их:
    приходится говорить своими словами, а не зачитывать определение."""
    helpers=[] if helpers is None else helpers
    board=B.new_slide(prs,bg); _head(board,title,bg)
    B.text(board,0.9,1.5,11.5,0.5,
           [[('Explain the word - but never say the three red ones.',18,'5A4A7A',True,B.TF)]],
           align=PP_ALIGN.CENTER)
    n=len(cards); cols=3 if n>4 else n; rows=-(-n//cols)
    cw=min(3.3,(11.4-(cols-1)*0.4)/cols); ch=min(2.1,(4.3-(rows-1)*0.35)/rows)
    gx=(B.SLIDE_W-(cols*cw+(cols-1)*0.4))/2; gy=2.2
    for i,(word,ban) in enumerate(cards):
        face=B.new_slide(prs,bg); helpers.append(face)
        _head(face,title,bg,counter=f'{i+1}/{n}')
        c=B.card(face,2.9,1.9,7.53,1.25,fill=B.WHITE,rad=0.2)
        card_text(c,word,size=fit_size(word,34,16),col=B.HOTPINK)
        B.text(face,2.9,3.3,7.53,0.5,[[('Do NOT say:',18,'5A4A7A',True,B.TF)]],align=PP_ALIGN.CENTER)
        for j,b in enumerate(ban[:3]):
            x=2.9+j*2.6
            cb=B.card(face,x,3.9,2.33,0.95,fill='FFD6D6',rad=0.3)
            card_text(cb,b,size=fit_size(b,18,11),col=B.RED)
        btn(face,9.6,6.45,3.2,0.75,back,fill=B.WHITE,size=16,col=B.INK,rad=0.4,target=board)
        no_click_advance(face,arrow=False)
        r=i//cols; c2=i%cols
        sh=btn(board,gx+c2*(cw+0.4),gy+r*(ch+0.35),cw,ch,fill=pal(bg,i),target=face)
        card_text(sh,str(i+1),size=40,col=B.INK)
    no_click_advance(board)
    return helpers

# ------------------------------------------------------------ правда / ложь
def g_truefalse(prs,bg,items,helpers=None,title='✅ True or False?',
                template='This is a {w}.',final='🏆 Nobody tricked you!'):
    """Картинка плюс утверждение. Верно - TRUE, слово подменили - FALSE.
    Самая быстрая игра пула: решение одно, думать надо про слово."""
    helpers=[] if helpers is None else helpers
    n=len(items)
    qs=[B.new_slide(prs,bg) for _ in range(n)]
    fin=_win(prs,bg,final)
    for k,(word,media) in enumerate(items):
        s=qs[k]; nxt=qs[k+1] if k+1<n else fin
        ok,bad=_feedback(prs,s,nxt,last=(k+1==n),helpers=helpers)
        truth=(k%2==0)                                   # через одну - ложь
        said=word if truth else items[(k+2)%n][0]
        _head(s,title,bg,counter=f'{k+1}/{n}')
        B.text(s,0.9,1.5,11.5,0.6,[[('"'+template.format(w=said)+'"',22,'5A4A7A',True,B.TF)]],
               align=PP_ALIGN.CENTER)
        c=B.card(s,4.55,2.15,4.23,2.9,fill=B.WHITE,rad=0.2)
        media_on(s,c,media,size=90,panel=False)
        btn(s,2.85,5.35,3.4,1.1,'TRUE  ✅',fill=pal(bg,4),size=26,col=B.INK,
            target=ok if truth else bad)
        btn(s,7.1,5.35,3.4,1.1,'FALSE  ❌',fill=pal(bg,0),size=26,col=B.INK,
            target=bad if truth else ok)
        no_click_advance(s)
    return helpers

# -------------------------------------------------- две правды и одна ложь
def g_twotruths(prs,bg,words,helpers=None,title='🎭 Two truths and a lie',
                back='⬅️ Back to the words',unit='word'):
    """Слово открывается по номеру: три предложения с ним, одно враньё, класс
    ищет какое. Говорит не один ученик, а все - и говорят предложениями."""
    helpers=[] if helpers is None else helpers
    board=B.new_slide(prs,bg); _head(board,title,bg)
    B.text(board,0.9,1.5,11.5,0.5,
           [[(f'Pick a {unit}. Three sentences with it - one of them is a lie.',18,'5A4A7A',True,B.TF)]],
           align=PP_ALIGN.CENTER)
    n=len(words); cols=3 if n>4 else n; rows=-(-n//cols)
    cw=min(3.3,(11.4-(cols-1)*0.4)/cols); ch=min(2.1,(4.3-(rows-1)*0.35)/rows)
    gx=(B.SLIDE_W-(cols*cw+(cols-1)*0.4))/2; gy=2.2
    steps=[f'Say THREE sentences with this {unit} - two true, one false.',
           'The class asks you one question about each sentence.',
           'Then they vote: which one was the lie?']
    for i,w in enumerate(words):
        face=B.new_slide(prs,bg); helpers.append(face)
        _head(face,title,bg,counter=f'{i+1}/{n}')
        c=B.card(face,2.9,1.9,7.53,1.25,fill=B.WHITE,rad=0.2)
        card_text(c,w,size=fit_size(w,32,16),col=B.HOTPINK)
        runs=[[(f'{j+1}. ',17,B.HOTPINK,True,B.BF),(t,17,B.INK,False,B.BF)] for j,t in enumerate(steps)]
        B.card(face,2.9,3.35,7.53,2.4,fill=B.WHITE,rad=0.08)
        B.text(face,3.2,3.55,6.93,2.0,runs,align=PP_ALIGN.LEFT,sa=10,ls=1.05)
        btn(face,9.6,6.45,3.2,0.75,back,fill=B.WHITE,size=16,col=B.INK,rad=0.4,target=board)
        no_click_advance(face,arrow=False)
        r=i//cols; c2=i%cols
        sh=btn(board,gx+c2*(cw+0.4),gy+r*(ch+0.35),cw,ch,fill=pal(bg,i),target=face)
        card_text(sh,str(i+1),size=40,col=B.INK)
    no_click_advance(board)
    return helpers

def play(prs,spec,cfg):
    """cfg['games'] = [{'type':'quiz'}, {'type':'missing'}, ...] -> slides."""
    t=spec.get('type','quiz'); bg=spec.get('bg') or B.PASTELS['yellow']
    lvl=cfg.get('level','beg'); vocab=cfg.get('vocab',[])
    items=spec.get('items') or vocab
    mode=spec.get('mode') or ('word' if lvl=='adv' else 'picture')
    def kw(*names): return {k:v for k,v in spec.items() if k in names}
    if t=='quiz':
        return g_quiz_series(prs,bg,items,mode=mode,**kw('title','nopt','final'))
    if t=='missing':
        if mode=='word':
            emo=spec.get('emoji',{}); items=[(w,emo.get(w,'💬')) for w,_ in items]
        return g_missing_pics(prs,bg,items,**kw('title','order','rounds','anim'))
    if t=='reveal':
        return g_reveal(prs,bg,spec.get('lines') or [w for w,_ in items],**kw('title','subtitle'))
    if t=='board':
        return g_board(prs,bg,spec.get('questions',[]),**kw('title','back'))
    if t in ('pic2word','silhouette','zoom'):
        st=spec.get('style') or ('plain' if t=='pic2word' else t)
        return g_pic2word(prs,bg,items,style=st,**kw('title','nopt','final'))
    if t=='flip':
        return g_flip(prs,bg,items,**kw('title','prompt','back'))
    if t=='odd':
        return g_odd(prs,bg,spec.get('rounds',[]),**kw('title','ask','final'))
    if t=='taboo':
        return g_taboo(prs,bg,spec.get('cards',[]),**kw('title','back'))
    if t=='truefalse':
        return g_truefalse(prs,bg,items,**kw('title','final','template'))
    if t=='twotruths':
        return g_twotruths(prs,bg,spec.get('words') or [w for w,_ in items],**kw('title','back','unit'))
    raise ValueError(f'unknown game type: {t}')
