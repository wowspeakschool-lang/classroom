#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA for a built deck:  python3 wowspeak_qa.py final/*.pptx
Checks the things that actually broke before:
  * the file survives a double round-trip (open-save twice) with its animations,
    transitions and links intact;
  * every button carries a link, and every picture lying on a button carries
    the SAME link (otherwise the centre of the card is dead);
  * no card is painted in the slide's own background colour;
  * the feedback screens sit at the END of the file;
  * click-advance is off on the quiz and board slides.
Animations themselves can only be checked in real PowerPoint - LibreOffice
renders a PDF without playing them.
"""
import sys, os, shutil, tempfile
from pptx import Presentation
from pptx.oxml.ns import qn

GREEN='2E9E5B'; AMBER='E8A33D'

def _bg(s):
    try: return str(s.background.fill.fore_color.rgb)
    except Exception: return ''
def _fill(sh):
    try: return str(sh.fill.fore_color.rgb)
    except Exception: return ''
def _target(sh):
    try: return sh.click_action.target_slide
    except Exception: return None

def scan(path):
    p=Presentation(path); sl=list(p.slides); idx={s.slide_id:i+1 for i,s in enumerate(sl)}
    out={'slides':len(sl),'timing':0,'transition':0,'links':0,'problems':[],'service':[],'bye':0}
    for i,s in enumerate(sl,1):
        x=s._element
        out['timing']+=len(x.findall(qn('p:timing')))
        out['transition']+=len(x.findall(qn('p:transition')))
        out['links']+=len(x.findall('.//'+qn('a:hlinkClick')))
        bg=_bg(s)
        if bg in (GREEN,AMBER): out['service'].append(i)
        if any('Thank you!' in (sh.text_frame.text if sh.has_text_frame else '') for sh in s.shapes):
            out['bye']=i
        pics=[sh for sh in s.shapes if sh.shape_type is not None and sh.shape_type==13]
        dead=[sh.shape_id for sh in pics if _target(sh) is None and
              any(_target(o) is not None for o in s.shapes if o.shape_id!=sh.shape_id
                  and o.left<=sh.left and o.top<=sh.top
                  and o.left+o.width>=sh.left+sh.width and o.top+o.height>=sh.top+sh.height)]
        if dead: out['problems'].append(f'slide {i}: picture(s) {dead} lie on a button but carry no link')
        for sh in s.shapes:
            f=_fill(sh)
            full=sh.width>=12190000 and sh.height>=6855000      # the invisible click layer
            if f and bg and f==bg and sh.width>800000 and not full:
                out['problems'].append(f'slide {i}: a card is painted in the background colour {bg}')
                break
        greens=[sh for sh in s.shapes if _target(sh) is not None and _bg(_target(sh))==GREEN]
        ambers=[sh for sh in s.shapes if _target(sh) is not None and _bg(_target(sh))==AMBER]
        if greens or ambers:
            if not greens:
                out['problems'].append(f'slide {i}: quiz round without a correct answer')
            if not x.findall(qn('p:transition')):
                out['problems'].append(f'slide {i}: quiz round without no_click_advance()')
    if out['service'] and out.get('bye') and min(out['service'])<out['bye']:
        out['problems'].append('feedback screens sit inside the lesson (finish() not called?)')
    return out

def roundtrip(path,times=2):
    tmp=tempfile.mkdtemp(); cur=os.path.join(tmp,'rt.pptx'); shutil.copy(path,cur)
    before=scan(cur)
    for _ in range(times):
        Presentation(cur).save(cur+'.n'); shutil.move(cur+'.n',cur)
    after=scan(cur); shutil.rmtree(tmp)
    keys=('slides','timing','transition','links')
    return {k:(before[k],after[k]) for k in keys}, before

def main(paths):
    bad=0
    for f in paths:
        rt,info=roundtrip(f)
        drift=[k for k,(a,b) in rt.items() if a!=b]
        print(f'\n=== {os.path.basename(f)}')
        print(f'  slides={info["slides"]}  animations={info["timing"]}  '
              f'no-click slides={info["transition"]}  links={info["links"]}  '
              f'service screens={len(info["service"])}')
        print('  double round-trip: '+('OK' if not drift else 'DRIFT in '+', '.join(drift)))
        for pr in info['problems']: print('  🟥 '+pr)
        bad+=len(info['problems'])+len(drift)
    print('\n'+('ALL GOOD' if not bad else f'{bad} problem(s) found')); return 1 if bad else 0

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))
