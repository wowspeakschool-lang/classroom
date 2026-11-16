#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка самой проверки: подкладываем те ошибки, которые уже случались,
и смотрим, поймает ли их wowspeak_lint. Отчёт «замечаний: 0» сам по себе
ничего не доказывает - так же выглядел бы отчёт сломанной проверки."""
import sys, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wowspeak_lint as L

CASES=[]
def case(name,fn): CASES.append((name,fn))

def run_prop(pr):
    out=[]; L.check_prop(pr,'prop',out.append); return out
def run_tpl(S):
    out=[]; L.check_template(S,out.append); return out

# 1. ровно та ошибка из «Making holiday plans»: общего свободного дня нет
case('расписание без решения', lambda: run_prop({'kind':'week',
    'people':['Masha','Dima','Katya','Oleg'],
    'busy':{'Masha':['Mon','Wed','Sat'],'Dima':['Tue','Wed','Thu'],
            'Katya':['Mon','Fri','Sat'],'Oleg':['Wed','Thu','Sun']}}))
# 2. обратная крайность: свободны почти все дни
case('расписание слишком лёгкое', lambda: run_prop({'kind':'week',
    'people':['A','B'],'busy':{'A':['Mon'],'B':['Tue']}}))
# 3. у человека занята вся неделя
case('участник занят всегда', lambda: run_prop({'kind':'week',
    'people':['A','B'],'busy':{'A':L.DAYS,'B':['Tue']}}))
# 4. бюджета не хватает ни на что
case('бюджет ни на что', lambda: run_prop({'kind':'pricelist','title':'💰 You have 1 000 ₽',
    'rows':[('a','1 200 ₽'),('b','2 000 ₽')]}))
# 5. бюджета хватает на всё сразу - торга не будет
case('бюджет на всё сразу', lambda: run_prop({'kind':'pricelist','title':'💰 You have 1 000 ₽',
    'rows':[('a','100 ₽'),('b','200 ₽')]}))
# 6. двенадцать месяцев плюс лишний шаг
case('шагов больше двенадцати', lambda: run_prop({'kind':'route','steps':['s%d'%i for i in range(13)]}))
# 7. повтор подписи в ленте
case('повтор шага в ленте', lambda: run_prop({'kind':'route','steps':['Home','Park','Home']}))
# 8. «This is a save» - артикль перед глаголом
case('артикль перед глаголом', lambda: run_tpl({'tf_template':'This is a {w}.',
    'w1012':['money','save','spend'],'w13':[]}))
# 9. «This is a less screen time»
case('артикль перед фразой', lambda: run_tpl({'tf_template':'This is a {w}.',
    'w1012':['phone'],'w13':['less screen time']}))
# 10. шаблон без подстановки
case('шаблон без {w}', lambda: run_tpl({'tf_template':'This is a word.','w1012':['hat'],'w13':[]}))

print('эталон: безупречный реквизит и шаблон')
clean = run_prop({'kind':'week','people':['A','B','C'],
                  'busy':{'A':['Mon','Wed','Fri'],'B':['Tue','Wed','Sat'],
                          'C':['Mon','Fri','Sun']}}) \
      + run_prop({'kind':'pricelist','title':'💰 You have 1 000 ₽',
                  'rows':[('a','400 ₽'),('b','900 ₽'),('c','1 200 ₽')]}) \
      + run_tpl({'tf_template':'This is a {w}.','w1012':['hat','dog'],'w13':['ticket']})
print('  на исправном:', '; '.join(clean) if clean else 'замечаний нет')

caught=0
for name,fn in CASES:
    res=fn()
    if res: caught+=1; print(f'  [поймала] {name} → {res[0]}')
    else:   print(f'  [ПРОПУСТИЛА] {name}')
print(f'\nпоймано {caught} из {len(CASES)} подложенных дефектов')
sys.exit(0 if caught==len(CASES) and not clean else 1)
