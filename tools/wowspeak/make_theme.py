#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка 4 дек одной темы из компактного спека. run(spec, outdir)."""
import os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wowspeak_builder import build
HERE=os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------- разнообразие
# Аня: «почти во всех презентациях однотипные задания». Поэтому набор игр
# берётся не один и тот же, а по кругу: у каждой деки своя пара, соседние темы
# не совпадают. rot в спеке темы — номер темы, с него начинается отсчёт.
# Единица чередования — ТЕМА: все четыре деки темы получают один набор механик
# (Аня, 05.10: «между возрастами можно оставить одни игры»). Пул тратится в
# четыре раза медленнее, и один и тот же вариант возвращается не чаще, чем
# через три темы.
BEG_REC=['quiz','pic2word','silhouette','zoom','truefalse']   # узнавание
BEG_SPK=['missing','flip']                                     # говорение
ADV_REC=['quiz','odd']
ADV_SPK=['taboo','board','twotruths']
ADV_3=['board','taboo','twotruths','odd']                      # третья у Advanced
MOODS=['emoji','scale','weather','oneword']
LEADS=['questions','truefalse','finish','handsup','associations']
VIDEOS=['after','count','predict','threewords','nosound']
MINIS=['thisorthat','finish','findsomeone','guess','chain']

MOOD_BAND={'emoji':'😊 How are you today? 😊','scale':'📊 Rate your day: 1 to 5 📊',
           'weather':'🌦️ What is your weather today? 🌦️','oneword':'💬 One word about today 💬'}
LEAD_BAND={'questions':'💬 Lead-in – let’s talk! ','truefalse':'🤔 True or false about me? ',
           'finish':'✍️ Finish the sentence ','handsup':'🙋 Hands up if… ',
           'associations':'💭 First three words that come to mind '}
LEAD_HINT={'questions':'Discuss with your teacher:','truefalse':'Teacher reads it - true or false? Say why:',
           'finish':'Finish every line your own way:','handsup':'Hands up - and then say why:',
           'associations':'Say the first three words you think of - and why:'}
VIDEO_HINT={'after':'💬 After watching, discuss:','count':'🔢 Watch and count - then tell us:',
            'predict':'🔮 Before you watch - guess the answers:',
            'threewords':'📝 Write 3 words you hear - then use them:',
            'nosound':'🔇 Sound off - what are they saying? Then watch again:'}

# Подсказки-фразы под КОНКРЕТНЫЙ формат финального задания: общий набор
# «соглашаюсь / возражаю» бесполезен там, где идёт ролевая игра или опрос.
USEFUL_BY_FORMAT={
 'role-play':[('Start it off','Excuse me… / Hello, could I…? / Sorry to bother you…'),
              ('Something is wrong','I think there is a mistake. / This is not what I ordered. / It does not fit.'),
              ('Sort it out','No problem, I will change it. / Let me check that for you. / Would this one work?'),
              ('Finish politely','Thanks a lot. / That is perfect. / Have a good day!')],
 'debate':[('Give your opinion','In my opinion… / I think… / If you ask me…'),
           ('Agree','I agree because… / Good point! / Exactly!'),
           ('Disagree','I am not sure… / I see your point, but… / On the other hand…'),
           ('React & ask','Really? / That is interesting! / Why do you think so?')],
 'pitch':[('Open it','Let me show you… / Here is the plan…'),
          ('Sell it','The best part is… / You should come because… / Trust me, it is worth…'),
          ('Answer doubts','Yes, but think about… / It only takes… / We can always…'),
          ('Close it','So, who is in? / That is my route — any questions?')],
 'press':[('Ask as the press','Could you tell us…? / What made you…? / Is it true that…?'),
          ('Push harder','But why exactly…? / How do you answer people who say…?'),
          ('Answer','Good question. / To be honest… / I would rather not spoil it, but…'),
          ('Close it','Thank you, that is all we have time for.')],
 'survey':[('Ask','How often do you…? / Which one do you…? / And why that one?'),
           ('Note it down','So that is a yes / a no / sometimes.'),
           ('Report numbers','Most of us… / Only two people… / Nobody said…'),
           ('Conclude','So the class prefers… / It looks like…')],
 'ranking':[('Put it in order','I would put ___ first because… / ___ comes last for me.'),
            ('Compare','___ matters more than ___ . / Without ___ the rest is useless.'),
            ('Negotiate','Can we agree on…? / I will swap ___ and ___ if you…'),
            ('Defend it','I would never give up ___ , because…')],
 'hotseat':[('Ask the hot seat','How often do you…? / How much time does it take? / What do you miss because of it?'),
            ('Push','Be honest - is it a phase? / What would make you stop?'),
            ('Answer','Honestly, I… / I would say… / Fair point, but…'),
            ('Swap','Okay, next person - same questions.')],
 'wouldyourather':[('Choose','I would rather… / I would pick the first one. / Definitely the second.'),
                   ('Say why','…because I hate… / …because at least I can…'),
                   ('Reject the other','No way, that means… / I could never…'),
                   ('Ask back','What about you? / Would you really? / Same for you?')],
 'interview':[('Ask the past you','Can you remember…? / What were you like when…? / What did you worry about?'),
              ('Answer in role','Back then I… / At that time I…'),
              ('Compare','What changed since then? / What stayed the same?'),
              ('Finish','One thing I would tell you is…')],
}

# Windows не создаёт файл, в имени которого есть ? * : " < > | / \\ , а его
# встроенный распаковщик такой файл из архива молча пропускает - методист
# видит пустую папку. Так пропала тема «Can boys and girls be best friends?»:
# четыре деки лежали в архиве и не извлекались. Название темы на слайдах
# остаётся полным, чистим только имя файла.
WIN_BAD = '?*:"<>|/\\'
def safe_name(t):
    for ch in WIN_BAD: t=t.replace(ch,'')
    return ' '.join(t.split()).strip(' .')

def plan(rot):
    """Какие механики достаются теме №rot. Шаги подобраны так, чтобы ни один
    вариант не вернулся раньше, чем через три темы."""
    rec=BEG_REC[(rot*3)%5]; spk=BEG_SPK[rot%2]
    arec=ADV_REC[rot%2]; aspk=ADV_SPK[(rot*2)%3]
    third=None
    for j in range(len(ADV_3)):
        c=ADV_3[(rot*3+j)%len(ADV_3)]
        if c not in (arec,aspk): third=c; break
    return {'beg':(rec,spk),'adv':(arec,aspk,third),
            'mood':MOODS[rot%4],'lead':LEADS[(rot*2+2)%5],
            'video':VIDEOS[(rot*3+1)%5],'mini':MINIS[(rot*4+1)%5]}

STOP=set('a an the to of and or in on at for with without you your it is are be'
         ' that this something someone very not do does so than then when who'
         ' what which how they them their there here again over about into'
         ' have has had make makes making made get gets got give gives take takes'
         ' keep keeps every each some more most much many other another thing things'
         ' also even only still often always never usually really quite from but'.split())

def auto_taboo(vocab,extra=(),n=3):
    """Карточки Taboo прямо из определений: запрещаем самые «мясные» слова
    определения — описать придётся своими словами, а не зачитать словарь.
    Если определение короткое и слов не хватает, добираем соседними словами
    темы: их всё равно нельзя произносить, и это только усложняет задачу."""
    words=[w for w,_ in vocab]
    out=[]
    for w,d in vocab:
        ws=[x.strip('.,;:!?()"\'').lower() for x in d.split()]
        ws=[x for x in ws if x and x not in STOP and x not in w.lower() and len(x)>3]
        ban=[]
        for x in sorted(ws,key=len,reverse=True):
            if x not in ban: ban.append(x)
        for x in list(words)+list(extra):                 # добор соседями темы
            if len(ban)>=n: break
            x=str(x).lower()
            if x!=w.lower() and x not in ban: ban.append(x)
        out.append((w,ban[:n]))
    return out

def odd_rounds(words,foreign,rounds=4):
    """«Лишнее слово»: три слова нашей темы и одно из чужой. Ответ проверяемый,
    а объяснять, почему лишнее, они будут словами — ради этого игра и нужна."""
    out=[]
    n=len(words)
    for k in range(rounds):
        trio=[words[(k+j*2)%n] for j in range(3)]       # каждый раз другая тройка
        pos=k%4
        out.append(([*trio[:pos],foreign[k%len(foreign)],*trio[pos:]][:4],pos))
    return out

# Чужие слова для «лишнего» — из тем, которых в этой деке точно нет.
FOREIGN=['helicopter','toothbrush','volcano','saxophone','penguin','glacier',
         'lighthouse','hedgehog','skateboard','pineapple']

GAME_RU={
 'quiz':'«Point & Race» - слово названо, ищем картинку',
 'pic2word':'«Look and say» - картинка одна, выбираем слово',
 'silhouette':'«Shadow game» - угадываем по тени',
 'zoom':'«Too close» - угадываем по увеличенному кусочку',
 'missing':'«What is missing» - карточка исчезает, называем её',
 'flip':'«Flip a card» - открыли карточку и составили с ней предложение',
 'odd':'«Odd one out» - лишнее слово, и обязательно ПОЧЕМУ',
 'taboo':'«Taboo» - объясни слово, не называя три запрещённых',
 'board':'доска вопросов - номер открывает вопрос',
 'truefalse':'«True or False» - утверждение про картинку, верно или нет',
 'twotruths':'«Two truths and a lie» - три предложения со словом, одно враньё',
}
def NOTE_GAMES(games):
    lst='; '.join(GAME_RU.get(g,g) for g in games)
    return ('ИГРЫ внутри презентации: '+lst+'. Работают ТОЛЬКО в режиме показа (F5). '
            'Клик мимо кнопки НЕ листает слайд - дальше стрелкой → или маленькой «→» в левом нижнем '
            'углу. Подписи под картинками убраны специально: с ними задание проверяло бы чтение, '
            'а не знание слова.')
NOTE_SERVICE=('Служебные экраны игры (Correct / Try again / вопросы доски). '
              'Открываются сами по клику, листать их не надо.')
S5_BEG='Разбери новые слова по картинкам (единственный слайд с подписями).'
S5_ADV='Разбери слова и определения, проси пример в предложении.'
S6_BEG='Слайд "поговорим словами": рамка на доске, ученики говорят по ней и объясняют почему.'
S6_ADV='Разбери "Useful language for discussion" - фразы нужны весь урок.'

MOOD_NOTE={'emoji':'Mood check: смайлики - "How are you today?"',
 'scale':'Mood check: шкала 1-5, каждый называет цифру и объясняет почему.',
 'weather':'Mood check: "погода настроения" - выбирают значок и объясняют.',
 'oneword':'Mood check: одно слово о сегодняшнем дне, и почему именно оно.'}
LEAD_NOTE={'questions':'LEAD-IN: разговори учеников вопросами, пусть говорят свободно.',
 'truefalse':'LEAD-IN: читаешь утверждения о себе, ученики угадывают правда/неправда и спорят.',
 'finish':'LEAD-IN: ученики заканчивают каждую фразу по-своему.',
 'handsup':'LEAD-IN: "руки вверх, если…" - подняли руку и объяснили почему.',
 'associations':'LEAD-IN: первые три слова, которые приходят в голову по теме, и почему.'}
VIDEO_NOTE={'after':'Смотрим видео','count':'Смотрим видео и считаем заданное, потом отвечаем,',
 'predict':'Сначала отвечают на вопросы ДО просмотра, потом смотрим видео','threewords':'Смотрим видео, выписывают три услышанных слова,',
 'nosound':'Первый раз смотрим БЕЗ звука и угадываем реплики, потом со звуком,'}

def notes(url,s5,s6,s9,red=None,games=(),mood='emoji',lead='questions',video='after',prop=None):
    n=[{'label':'SLIDE 1-2:','text':'Титул и эти заметки. Заметки не показывай ученикам.'},
       {'label':'SLIDE 3:','text':MOOD_NOTE[mood]},
       {'label':'SLIDE 4:','text':LEAD_NOTE[lead]},
       {'label':'SLIDE 5:','text':s5},
       {'label':'SLIDE 6:','text':s6},
       {'label':'SLIDES {GAMES}:','text':NOTE_GAMES(games)}]
    v={'label':'SLIDE {VIDEO}:','text':VIDEO_NOTE[video],'tail':' затем обсуждаем вопросы со слайда.'}
    if url: v['url']=url
    if red: v['red']=red
    n.append(v)                                   # порядок строк = порядок слайдов
    if prop: n.append({'label':'SLIDE {PROP}:','text':prop})
    n+=[{'label':'SLIDE {SPEAKING}:','text':s9},
        {'label':'LAST SLIDE:','text':'Feedback.'},
        {'label':'SLIDES {SERVICE}:','text':NOTE_SERVICE}]
    return n

def game_specs(names,s,vocab,board):
    """Пара игр деки -> spec'и для билдера. Контент для odd и taboo считается
    из самого словаря, отдельно писать его в теме не нужно."""
    out=[]
    for i,t in enumerate(names):
        bg=[s.get('g1','D4ECFF'),s.get('g2','FFE6D0'),s.get('g3','D4F5E6')][i%3]
        if t in ('quiz','pic2word','silhouette','zoom','missing','truefalse'):
            spec={'type':t,'bg':bg}
            if t=='truefalse' and s.get('tf_template'): spec['template']=s['tf_template']
            out.append(spec)
        elif t=='flip':
            out.append({'type':'flip','bg':bg,
                        'prompt':s.get('flip_prompt','Say a sentence with this word! 🗣️')})
        elif t=='odd':
            # у функциональных тем словарь - это целые фразы, автораунды из них
            # не читаются: тема может задать свои короткие раунды.
            out.append({'type':'odd','bg':bg,
                        'rounds':s.get('odd_rounds') or
                                 odd_rounds([w for w,_ in vocab],s.get('odd_foreign',FOREIGN))})
        elif t=='taboo':
            out.append({'type':'taboo','bg':bg,
                        'cards':auto_taboo(vocab,s.get('w1012',[])+s.get('w13',[]))})
        elif t=='twotruths':
            spec={'type':'twotruths','bg':bg,'words':[w for w,_ in vocab]}
            if s.get('adv_unit'): spec['unit']=s['adv_unit']   # у функциональных тем это фразы
            spec.setdefault('back','⬅️ Back to the '+(s.get('adv_unit','word')+'s'))
            out.append(spec)
        elif t=='board':
            out.append({'type':'board','bg':bg,'questions':board})
    return out

def _prop(s,key,ico,age):
    """Реквизит для конкретной версии деки плюс пути к иконкам нужного возраста."""
    pr=s.get('prop_'+key) or s.get('prop_'+('beg' if key.startswith('beg') else 'adv')) or s.get('prop')
    if not pr: return None
    pr=dict(pr)
    d=os.path.join(ico,age)
    if os.path.isdir(d):
        pr['pics']={os.path.splitext(f)[0]:os.path.join(d,f) for f in os.listdir(d) if f.endswith('.png')}
    return pr

def run(s,outdir):
    """s - словарь темы, см. run_hobbies.py."""
    ICO=os.path.join(HERE,'icons',s['icons'])
    os.makedirs(outdir,exist_ok=True)
    rot=s.get('rot')
    if rot is None: rot=sum(map(ord,s['theme']))%8
    def beg(sub,words,items,ico,games,mini=None,prop=None):
        return {'level':'beg','theme':s['theme'],'emoji':s['emoji'],'title_bg':s.get('bg','FFF7D4'),
            'subtitle':sub,'mood_q':s['mood_beg'],'moods':s['moods_beg'],
            'lead_in':s['lead'],'video_url':s.get('video'),'video_qs':s['vq'],
            'vocab_title':s['vocab_title'],
            'vocab':[(w,os.path.join(ICO,ico,f'{w}.png')) for w in words],
            'games':games,
            'mini':mini or {'title':s['mini_title'],'frame':s['mini_frame'],'items':items},
            'speak_title':s['speak_title'],'frame_hint':s['frame_hint'],'frames':s['frames'],
            'prop':prop,'bye':s['bye']}
    def adv(sub,vocab,disc,board,games,prop=None):
        u=USEFUL_BY_FORMAT.get(s.get('useful_kind'))
        return {'useful':u,'level':'adv','theme':s['theme'],'emoji':s['emoji'],'title_bg':s.get('bg','FFF7D4'),
            'subtitle':sub,'mood_q':s['mood_adv'],'moods':s['moods_adv'],
            'lead_in':s['lead_adv'],'video_url':s.get('video'),'video_qs':s['vq'],
            'vocab_title':s['vocab_title'],'vocab':vocab,
            'games':games,
            'disc':disc,'prop':prop,'bye':s['bye']}
    red=None if s.get('video') else '🟥 ВСТАВЬ ССЫЛКУ НА ВИДЕО ВРУЧНУЮ'
    pl=plan(rot)
    gb1=gb2=s.get('games_beg') or pl['beg']          # одна тема - один набор игр
    ga1=ga2=s.get('games_adv') or pl['adv']          # у Advanced их три
    stage={'mood_band':MOOD_BAND[pl['mood']],'lead_band':LEAD_BAND[pl['lead']],
           'lead_hint':LEAD_HINT[pl['lead']],'video_hint':VIDEO_HINT[pl['video']]}
    for k in stage:                                   # тема может переопределить
        if s.get(k): stage[k]=s[k]
    mini13=None
    if s.get('mini_title13'):
        mini13={'title':s['mini_title13'],'frame':s.get('mini_frame13',s['mini_frame']),
                'items':s.get('it13_mini') or s['it13']}
    versions=[
      ('10-12 Beginners',beg('Speaking Club · 10-12 Beginners',s['w1012'],s['it1012'],'1012',
       game_specs(gb1,s,[(w,None) for w in s['w1012']],None),None,
       _prop(s,'beg1012',ICO,'1012')),S5_BEG,S6_BEG,s['s9_beg'],gb1),
      ('10-12 Advanced',adv('Speaking Club · 10-12 Advanced',s['adv1012'],s['disc1012'],s['board1012'],
       game_specs(ga1,s,s['adv1012'],s['board1012']),
       _prop(s,'adv1012',ICO,'1012')),S5_ADV,S6_ADV,s['s9_adv1012'],ga1),
      ('13+ Beginners',beg('Speaking Club · 13+ Beginners',s['w13'],s['it13'],'13',
       game_specs(gb2,s,[(w,None) for w in s['w13']],None),mini13,
       _prop(s,'beg13',ICO,'13')),S5_BEG,S6_BEG,s['s9_beg'],gb2),
      ('13+ Advanced',adv('Speaking Club · 13+ Advanced',s['adv13'],s['disc13'],s['board13'],
       game_specs(ga2,s,s['adv13'],s['board13']),
       _prop(s,'adv13',ICO,'13')),S5_ADV,S6_ADV,s['s9_adv13'],ga2),
    ]
    for grp,cfg,s5,s6,s9,games in versions:
        cfg.update(stage)
        cfg['notes']=notes(s.get('video'),s5,s6,s9,red,games,pl['mood'],pl['lead'],pl['video'],
                           s.get('prop_note') if cfg.get('prop') else None)
        build(cfg,f"{outdir}/{safe_name(f'Speaking Clubs {grp} ' + s['theme'])}.pptx")
    print('ALL DONE ->',outdir)
