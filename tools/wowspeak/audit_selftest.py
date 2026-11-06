#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка самой вычитки: ломаем заведомо исправную деку — по одной поломке на
копию — и смотрим, поймает ли её wowspeak_audit. Нужна потому, что отчёт «0 из 28»
сам по себе ничего не доказывает: так же выглядел бы отчёт сломанной проверки."""
import sys, os, shutil, subprocess, tempfile
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

SRC=sys.argv[1] if len(sys.argv)>1 else 'new7/Speaking Clubs 10-12 Beginners My morning routine.pptx'
TMP=tempfile.mkdtemp(prefix='selftest_')

def save(prs,name):
    p=os.path.join(TMP,name); prs.save(p); return p

def box(sl,txt,x=1.0,y=0.2,w=6.0,h=0.5,size=14):
    tb=sl.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=txt; r.font.size=Pt(size)
    return tb

CASES=[]
def case(name,expect,fn): CASES.append((name,expect,fn))

def c_perfect(prs): box(prs.slides[3],'I have seen this film three times.')
def c_american(prs): box(prs.slides[3],'My favorite color is blue.')
def c_usedto(prs): box(prs.slides[3],'I used to play football every day.')
def c_nopics(prs):
    sl=prs.slides[4]
    for sh in list(sl.shapes):
        if getattr(sh,'image',None) is not None: sh._element.getparent().remove(sh._element)
def c_token(prs):
    for sh in prs.slides[1].shapes:
        if sh.has_text_frame and 'SLIDE 1-2' in sh.text_frame.text:
            sh.text_frame.paragraphs[0].runs[0].text+=' SLIDES {GAMES}: игры'
            break
def c_bgcard(prs):
    sl=prs.slides[3]
    r=sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(2),Inches(2),Inches(3),Inches(1.5))
    r.fill.solid(); r.fill.fore_color.rgb=RGBColor.from_string('FFF7D4'); r.line.fill.background()
def c_deadbtn(prs):
    sl=prs.slides[3]
    r=sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(8),Inches(6),Inches(2.5),Inches(0.8))
    r.fill.solid(); r.fill.fore_color.rgb=RGBColor.from_string('FFD700'); r.line.fill.background()
    run=r.text_frame.paragraphs[0].add_run(); run.text='Back to the words'; run.font.size=Pt(18)
def c_tinypic(prs):
    sl=prs.slides[3]
    pic=[sh for sh in prs.slides[4].shapes if getattr(sh,'image',None) is not None][0]
    import io
    sl.shapes.add_picture(io.BytesIO(pic.image.blob),Inches(1),Inches(5),Inches(0.5),Inches(0.5))
def c_overflow(prs):
    box(prs.slides[3],'Очень длинная строка, которая заведомо не помещается в свою рамку, '
        'потому что в неё насыпано слишком много символов для такого кегля и такого размера.',
        x=1.0,y=6.6,w=2.0,h=0.4,size=20)

case('Present Perfect у Beginners','грамматика выше A1',c_perfect)
case('used to у Beginners','грамматика выше A1',c_usedto)
case('американское написание','американское написание',c_american)
case('иконки не нарезаны','иконки не нарезаны',c_nopics)
case('незаменённый токен в заметках','остался токен',c_token)
case('карточка цвета фона','карточка цвета фона',c_bgcard)
case('кнопка без действия','мёртвая кнопка',c_deadbtn)
case('мелкая картинка','мелкая картинка',c_tinypic)
case('текст не влезает в рамку','не влезть',c_overflow)

def run_audit(path):
    out=subprocess.run([sys.executable,'-I','wowspeak_audit.py',path],
                       capture_output=True,text=True).stdout
    return out

print('эталон:',os.path.basename(SRC))
base=run_audit(SRC)
print('  на исправном файле замечаний:', 'нет' if 'замечаниями: 0' in base else 'ЕСТЬ (!)')
ok=0
for name,expect,fn in CASES:
    prs=Presentation(SRC); fn(prs)
    p=save(prs,name.replace(' ','_')+'.pptx')
    out=run_audit(p)
    hit=expect in out
    ok+=hit
    line=[l.strip() for l in out.splitlines() if expect in l]
    print(f'  [{"поймала" if hit else "ПРОПУСТИЛА"}] {name}' + (f' → {line[0]}' if line else ''))
print(f'\nпоймано {ok} из {len(CASES)} подложенных дефектов')
shutil.rmtree(TMP,ignore_errors=True)
