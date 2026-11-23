#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка 4 дек одной темы из компактного спека. run(spec, outdir)."""
import itertools, os, sys
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
 'arrange':[('Suggest a time','Are you free on…? / How about Saturday? / Let us say six.'),
            ('Say you cannot','Sorry, I cannot - I am busy. / That is no good for me.'),
            ('Offer another','How about Sunday instead? / I am free after five.'),
            ('Agree and confirm','Perfect, see you there. / Six at the cinema, then.')],
 'gift':[('Hand it over','This is for you. / I got you something small. / I hope you like it.'),
         ('Say thank you','Thank you so much! / You really should not have! / It is just what I wanted.'),
         ('Be honest, but kind','It is lovely, but… / Would you mind if I changed the size?'),
         ('Close it warmly','It is the thought that counts. / I will use it all the time.')],
 'storytelling':[('Start the story','A long time ago… / They say that… / In my country there is a story about…'),
                 ('Build it up','One day… / Then suddenly… / Nobody knew that…'),
                 ('The turn','But it was a trap. / That was the night everything changed.'),
                 ('Finish it','And that is why… / People still say… / Nobody has seen it since.')],
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

# Темы до этого номера считаются по старой формуле - они уже отданы Ане, и
# пересборка не должна их менять. Всё новое идёт по расписанию ниже.
LEGACY_UNTIL=33

def _third(arec,aspk,rot):
    for j in range(len(ADV_3)):
        c=ADV_3[(rot*3+j)%len(ADV_3)]
        if c not in (arec,aspk): return c
    return None

def _plan_legacy(rot):
    rec=BEG_REC[(rot*3)%5]; spk=BEG_SPK[rot%2]
    arec=ADV_REC[rot%2]; aspk=ADV_SPK[(rot*2)%3]
    return {'beg':(rec,spk),'adv':(arec,aspk,_third(arec,aspk,rot)),
            'mood':MOODS[rot%4],'lead':LEADS[(rot*2+2)%5],
            'video':VIDEOS[(rot*3+1)%5],'mini':MINIS[(rot*4+1)%5]}

# --------------------------------------------------------------- расписание
# Аня, 23.11.2026: «если делать чередования, то по-разному, чтобы меньше было
# през где задания идут одинаково. Например, игра 1, лидин 1, мини-задание 1,
# вопросы к видео 1, и потом в третьей презе те же самые, а хотелось бы игра 3,
# лидин 1».
#
# Старая формула брала лид-ин, видео и мини по одному модулю 5 и линейно от
# номера темы - значит вся тройка возвращалась РОВНО каждые пять тем. В декабре
# это темы 1, 6 и 11: у них совпадали и лид-ин, и мини, и вопросы к видео.
# Поэтому теперь не формула, а подбор: на каждую тему перебираются все наборы,
# берётся тот, где варианты не использовались дольше всего, и набор целиком
# отвергается, если он уже был или слишком похож на соседний.
_SCHED={}

def _pick(pools, hist, prev, seen, recent, max_same, veto=None):
    """Лучший набор: давно не использованные варианты, не повторять целиком,
    с предыдущей темой совпадать не больше чем в max_same местах. veto -
    дополнительный запрет: им отсекается повтор ТРОЙКИ лид-ин + видео + мини,
    даже если разминка другая. Именно этот повтор Аня и заметила."""
    best=None
    for combo in itertools.product(*pools):
        if combo in seen: continue
        if combo in recent: continue
        if veto and veto(combo): continue
        # сравниваем не с одной предыдущей темой, а с несколькими: если
        # смотреть только на соседа, наборы расходятся попарно и всё равно
        # возвращаются одной и той же фазой через пять тем
        if any(sum(a==b for a,b in zip(combo,q))>max_same for q in prev): continue
        # чем дольше вариант не встречался, тем лучше; при равенстве - порядок
        # перебора, он детерминированный, значит и расписание воспроизводимо
        score=sum(hist[i].get(v,-99) for i,v in enumerate(combo))
        if best is None or score<best[0]: best=(score,combo)
    return best[1] if best else None

def _build_schedule(upto):
    gp=[BEG_REC,BEG_SPK,ADV_REC,ADV_SPK,ADV_3]    # игры, третья Advanced тоже
    sp=[MOODS,LEADS,VIDEOS,MINIS]                 # разминка, лид-ин, видео, мини
    ghist=[{} for _ in gp]; shist=[{} for _ in sp]
    gseen=set(); sseen=set()
    gq=[]; sq=[]; tq=[]            # последние наборы игр, сцены и троек
    bq=[]; aq=[]                   # пары игр Beginners и тройки Advanced
    for rot in range(LEGACY_UNTIL+1, upto+1):
        trio=lambda c: (c[1],c[2],c[3]) in tq      # лид-ин, видео, мини
        # третья игра Advanced не должна совпасть с первыми двумя; и запрещаем
        # прямо то, что потом меряет rotation_check - возврат пары игр
        # Beginners и тройки Advanced. Ограничения по отдельным позициям
        # этого не дают: позиции расходятся, а пара возвращается.
        def veto_g(c, strict=True):
            if c[4] in (c[2],c[3]): return True
            if not strict: return False
            return (c[0],c[1]) in bq or (c[2],c[3],c[4]) in aq
        g=(_pick(gp,ghist,gq[-3:],set(),set(),1,veto_g)
           or _pick(gp,ghist,gq[-1:],set(),set(),2,veto_g)
           or _pick(gp,ghist,gq[-1:],set(),set(),3,veto_g)
           or _pick(gp,ghist,[],set(),set(),4,lambda c: veto_g(c,False)))
        s=(_pick(sp,shist,sq[-4:],sseen,set(sq),1,trio)
           or _pick(sp,shist,sq[-2:],sseen,set(sq),1,trio)
           or _pick(sp,shist,sq[-1:],sseen,set(),2,trio)
           or _pick(sp,shist,sq[-1:],sseen,set(),3))
        for i,v in enumerate(g): ghist[i][v]=rot
        for i,v in enumerate(s): shist[i][v]=rot
        gseen.add(g); sseen.add(s)
        gq.append(g); sq.append(s); tq.append((s[1],s[2],s[3]))
        bq.append((g[0],g[1])); aq.append((g[2],g[3],g[4]))
        if len(bq)>8: bq.pop(0)
        if len(aq)>6: aq.pop(0)
        if len(gq)>12: gq.pop(0)
        if len(sq)>10: sq.pop(0)
        if len(tq)>12: tq.pop(0)
        rec,spk,arec,aspk,third=g; mood,lead,video,mini=s
        _SCHED[rot]={'beg':(rec,spk),'adv':(arec,aspk,third),
                     'mood':mood,'lead':lead,'video':video,'mini':mini}

def plan(rot):
    """Какие механики достаются теме №rot."""
    if rot<=LEGACY_UNTIL: return _plan_legacy(rot)
    if rot not in _SCHED: _build_schedule(max(rot, LEGACY_UNTIL+60))
    return _SCHED[rot]

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
            # board есть только у Advanced - только там словарь состоит из фраз
            if t=='quiz' and s.get('adv_unit') and board is not None:
                spec['unit']=s['adv_unit']; spec['title']='🎯 '+s['adv_unit'].capitalize()+' hunt!'
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
