#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Тема «Small talk I hate» — 4 деки. Запуск: python3 run_smalltalk.py final
Иконки: icons/smalltalk/1012/ (стиль младших) и icons/smalltalk/13/ (стиль старших).
"""
import os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wowspeak_builder import build

ICO=os.path.join(os.path.dirname(os.path.abspath(__file__)),'icons','smalltalk')  # + подпапка возраста
VID='https://youtu.be/9X4mQFDFutc'           # одно видео на все четыре деки
THEME='Small talk I hate'
EMO=['🙃','💬','😬',['💬','🙃','😬','🗣️','🤐','😑']]

LEAD=[('Do you like talking to new people?','💬'),('Who do you talk to every day?','🗣️'),
      ('What do adults always ask you about?','🙄'),('Do you talk a lot or a little?','😶'),
      ('Is it easy to talk to your neighbours?','🏠'),('Who is easy to talk to?','😊')]
LEAD_ADV=[('Why do people talk about nothing?','🤔'),('Is small talk polite or fake?','🎭'),
          ('What question are you tired of answering?','🙄'),('Is silence always awkward?','🤐'),
          ('Can you leave a boring conversation politely?','🚪'),('Who is good at small talk, and why?','🗣️')]
VQ=[('What was awkward in the video?','😬'),('Does this happen to you?','🙃'),('What would you say?','💬')]

def notes(url,s5,s6,s9):
    return [
        {'label':'SLIDE 1-2:','text':'Титул и эти заметки. Заметки не показывай ученикам.'},
        {'label':'SLIDE 3:','text':'Mood check - "How are you today?"'},
        {'label':'SLIDE 4:','text':'LEAD-IN: разговори учеников, пусть говорят свободно.'},
        {'label':'SLIDE 5:','text':s5},
        {'label':'SLIDE 6:','text':s6},
        {'label':'SLIDES {GAMES}:','text':
            'ИГРА внутри презентации. Раунд на каждое слово: правильный ответ - следующее слово, '
            'ошибка - тот же вопрос. Работает ТОЛЬКО в режиме показа (F5). Клик мимо кнопки НЕ листает '
            'слайд - дальше стрелкой → или маленькой «→» в левом нижнем углу. Подписи под картинками '
            'убраны специально: с ними задание проверяло бы чтение, а не знание слова.'},
        {'label':'SLIDE {VIDEO}:','text':'Смотрим видео','url':url,'tail':' затем обсуждаем вопросы со слайда.'},
        {'label':'SLIDE {SPEAKING}:','text':s9},
        {'label':'LAST SLIDE:','text':'Feedback.'},
        {'label':'SLIDES {SERVICE}:','text':'Служебные экраны игры (Correct / Try again / вопросы доски). '
                                            'Открываются сами по клику, листать их не надо.'},
    ]

def beg(sub,words,items,ico):
    return {'level':'beg','theme':THEME,'emoji':EMO,'title_bg':'EDE4FA','subtitle':sub,
        'mood_q':'Do you like talking to people today? 💬',
        'moods':[('😄','Great'),('🙂','Good'),('😐','OK'),('😬','Awkward'),('😴','Tired')],
        'lead_in':LEAD,'video_url':VID,'video_qs':VQ,'vocab_title':'💬 New words! 🙃',
        'vocab':[(w,os.path.join(ICO,ico,f'{w}.png')) for w in words],
        'games':[{'type':'quiz','bg':'FFF7D4'},{'type':'missing','bg':'D4F5E6'}],
        'mini':{'title':'💬 This or That!','frame':'I prefer talking about ___','items':items},
        'speak_title':'🗣️ Topics I like and hate! 🙃','frame_hint':'Use the sentences to talk about your topics!',
        'frames':['I don’t like talking about ___ .','___ is boring for me.','I like talking about ___ .',
                  'Adults always ask me about ___ .','My favourite topic is ___ .'],
        'bye':'💬 See you next time! 💜'}

def adv(sub,vocab,disc,board):
    return {'level':'adv','theme':THEME,'emoji':EMO,'title_bg':'EDE4FA','subtitle':sub,
        'mood_q':'How do you feel about small talk? 🙃',
        'moods':[('😄','Great'),('🙂','Good'),('😐','OK'),('😬','Awkward'),('🤔','Thoughtful')],
        'lead_in':LEAD_ADV,'video_url':VID,'video_qs':VQ,'vocab_title':'💬 New words! 🙃','vocab':vocab,
        'games':[{'type':'quiz','bg':'FFF7D4'},{'type':'board','bg':'D4ECFF','questions':board}],
        'disc':disc,'bye':'💬 See you next time! 💜'}

W1012=['weather','school','food','family','pets','holidays']
W13  =['weather','school','food','music','plans','holidays']
IT1012=[('school 🏫 or food 🍕?','💬'),('pets 🐶 or family 👨‍👩‍👧?','🗣️'),
        ('weather 🌦️ or holidays 🧳?','😬'),('sport ⚽ or films 🎬?','🎭'),
        ('a long talk 🕰️ or a short one ⏱️?','😶'),('talking 💬 or listening 👂?','😊')]
IT13  =[('music 🎧 or films 🎬?','💬'),('school 🏫 or weekend plans 📅?','🗣️'),
        ('weather 🌦️ or holidays 🧳?','😬'),('food 🍕 or sport ⚽?','🎭'),
        ('a text 📱 or a phone call 📞?','😶'),('talking 💬 or listening 👂?','😊')]

ADV1012=[('chit-chat','light talk about nothing important'),('awkward','not comfortable or natural'),
         ('uncomfortable','not relaxed, a little unpleasant'),('polite','saying the nice, expected thing'),
         ('avoid','to stay away from something on purpose'),('prefer','to like one thing more than another')]
ADV13=[('small talk','polite conversation about unimportant things'),
       ('cringe','to feel so embarrassed you want to disappear'),
       ('painful','so uncomfortable it is hard to sit through'),
       ('forced','not natural, done because you have to'),
       ('genuine','real and honest, not pretended'),
       ('escape','to get out of a situation you do not want to be in')]

DISC1012={'headline':'Debate 🗣️','statement':'💬 Small talk is a waste of time.',
  'options':['Agree ✅','Disagree ❌'],
  'tasks':['Choose a side and give 3 reasons.',
           'Answer the other side: why are they wrong?',
           'Together: name one situation where small talk really helps.']}
DISC13={'headline':'Ranking 💎','statement':'🙃 Rank these small-talk topics: bearable → unbearable',
  'options':['the weather 🌦️','school 🏫','your plans 📅','your family 👨‍👩‍👧','how tall you got 📏'],
  'tasks':['Rank them and defend your worst one.',
           'Compare with a partner - what makes a topic unbearable: the topic, or the person asking?',
           'Rewrite the worst question into one you would actually enjoy answering.']}
BOARD1012=['What do adults always ask you?','Talk about the weather for 30 seconds.',
           'A question you are tired of answering?','Who is easy to talk to, and why?',
           'How do you politely end a boring talk?','Is silence always awkward?']
BOARD13=['What question makes you cringe every time?','Talk about the weather for 30 seconds - make it genuine.',
         'Small talk with a teacher vs with a stranger: what changes?','How do you escape a forced conversation?',
         'Is polite small talk a kind of lying?','When did small talk turn into a real conversation for you?']

VERSIONS=[
  ('10-12 Beginners',beg('Speaking Club · 10-12 Beginners',W1012,IT1012,'1012'),
      'Разбери новые слова по картинкам (единственный слайд с подписями).',
      'Рамка "This or That": ученики выбирают тему и объясняют почему.',
      'Beginners рассказывают про любимые и нелюбимые темы по рамкам.'),
  ('10-12 Advanced',adv('Speaking Club · 10-12 Advanced',ADV1012,DISC1012,BOARD1012),
      'Разбери слова и определения, проси пример в предложении.',
      'Разбери "Useful language for discussion" - фразы нужны весь урок.',
      'MAIN SPEAKING (Debate): спорим, нужен ли small talk. Требуй аргументы и встречные вопросы.'),
  ('13+ Beginners',beg('Speaking Club · 13+ Beginners',W13,IT13,'13'),
      'Разбери новые слова по картинкам (единственный слайд с подписями).',
      'Рамка "This or That": ученики выбирают тему и объясняют почему.',
      'Beginners рассказывают про любимые и нелюбимые темы по рамкам.'),
  ('13+ Advanced',adv('Speaking Club · 13+ Advanced',ADV13,DISC13,BOARD13),
      'Разбери слова и определения, проси пример в предложении.',
      'Разбери "Useful language for discussion" - фразы нужны весь урок.',
      'MAIN SPEAKING (Ranking): ранжируем темы small talk и переписываем худший вопрос.'),
]

if __name__=='__main__':
    out=sys.argv[1] if len(sys.argv)>1 else 'final'
    os.makedirs(out,exist_ok=True)
    for grp,cfg,s5,s6,s9 in VERSIONS:
        cfg['notes']=notes(VID,s5,s6,s9)
        build(cfg,f'{out}/Speaking Clubs {grp} {THEME}.pptx')
    print('ALL DONE ->',out)
