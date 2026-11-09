#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Переполнение рамок по метрикам настоящего шрифта.

Грубая оценка в wowspeak_audit (символы на строку) ловит только явные случаи.
Здесь текст переносится по словам ровно так, как это сделает PowerPoint, и
сравнивается реальная высота с высотой рамки.
"""
import sys, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from pptx import Presentation
from wowspeak_builder import _needed_height

def check(path):
    prs=Presentation(path); P=[]
    for i,sl in enumerate(prs.slides,1):
        for sh in sl.shapes:
            if not sh.has_text_frame: continue
            txt=sh.text_frame.text.strip()
            if not txt: continue
            runs=[]
            for p in sh.text_frame.paragraphs:
                para=[(r.text,(r.font.size.pt if r.font.size else 12),'000000',False,'Calibri')
                      for r in p.runs if r.text]
                if para: runs.append(para)
            if not runs: continue
            w=sh.width/914400.0*72; h=sh.height/914400.0*72
            if w<40 or h<14: continue
            need=_needed_height(runs,w)
            if need>h+1:
                P.append((i,round((need-h)/72.0,2),txt[:46].replace('\n',' ')))
    return P

if __name__=='__main__':
    tot=0
    for f in sys.argv[1:]:
        P=check(f)
        if P:
            tot+=1; print('\n===',os.path.basename(f))
            for i,over,t in sorted(P,key=lambda x:-x[1])[:8]:
                print(f'  слайд {i}: не хватает {over:.2f}" — "{t}"')
    print(f'\nфайлов с переполнением: {tot} из {len(sys.argv)-1}')
