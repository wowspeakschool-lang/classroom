#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Worked example: one theme x 4 versions, with the games built into the .pptx.
Copy this file for a new theme. Icons come from crop_grid_auto (Beginners only).
"""
import os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wowspeak_builder import build

ICO=os.path.join(os.path.dirname(os.path.abspath(__file__)),'icons','smell')
VID='https://youtu.be/cj6RmvPGqlI'          # one video for all four decks, keep it under ~4 min
EMO=['🍂','👃','☕',['🍂','☕','🕯️','🌧️','🎃','🌰']]

LEAD=[('Do you like autumn?','🍂'),('What is your favourite smell?','👃'),
      ('Do you drink tea or coffee?','☕'),('Do you like the smell of rain?','🌧️'),
      ('Do you light candles at home?','🕯️'),('What does your home smell like?','🏠')]
LEAD_ADV=[('Which smell takes you straight back to childhood?','💭'),
          ('Why do smells bring memories back so fast?','🧠'),
          ('Is there a smell you cannot stand?','🙅'),
          ('Do seasons really have their own smell?','🍂'),
          ('Would you buy a perfume that smells like autumn rain?','🌧️'),
          ('Can a smell change your mood?','😌')]
VQ=[('Which smells did you notice?','👃'),('Which one do you like most?','❤️'),('What does autumn smell like for you?','🍂')]

def notes(lvl,url,s5,s6,s9):
    return [
        {'label':'SLIDE 1-2:','text':'Титул и эти заметки. Заметки не показывай ученикам.'},
        {'label':'SLIDE 3:','text':'Mood check - "How are you today?"'},
        {'label':'SLIDE 4:','text':'LEAD-IN: разговори учеников, пусть говорят свободно.'},
        {'label':'SLIDE 5:','text':s5},
        {'label':'SLIDE 6:','text':s6},
        {'label':'SLIDES {GAMES}:','text':
            'ИГРА внутри презентации (Wordwall не нужен). Раунд на каждое слово: правильный ответ - '
            'следующее слово, ошибка - тот же вопрос. Работает ТОЛЬКО в режиме показа (F5). '
            'Клик мимо кнопки НЕ листает слайд - дальше стрелкой →. Подписи под картинками убраны '
            'специально: с подписями задание проверяло бы чтение, а не знание слова. '
            'Экраны "Correct / Try again" лежат в конце файла - листая урок стрелками, ты их не увидишь.'},
        {'label':'SLIDE {VIDEO}:','text':'Смотрим видео','url':url,'tail':' затем обсуждаем вопросы со слайда.'},
        {'label':'SLIDE {SPEAKING}:','text':s9},
        {'label':'LAST SLIDE:','text':'Feedback.'},
        {'label':'SLIDES {SERVICE}:','text':'Служебные экраны игры (Correct / Try again / вопросы доски). Открываются сами по клику, листать их не надо.'},
    ]

def beg(sub,ico,words):
    vocab=[(w,f'{ico}/{w.split()[0]}.png') for w in words]
    return {'level':'beg','theme':'What autumn smells like','emoji':EMO,'title_bg':'FFE6D0','subtitle':sub,
        'mood_q':'What does autumn smell like? 🍂','moods':[('😄','Great'),('😌','Calm'),('🙂','Good'),('😐','OK'),('😴','Sleepy')],
        'lead_in':LEAD,'video_url':VID,'video_qs':VQ,'vocab_title':'👃 New words! 🍂','vocab':vocab,
        'games':[{'type':'quiz','bg':'FFF7D4'},{'type':'missing','bg':'D4F5E6'}],
        'mini':{'title':'👃 This or That!','frame':'I like ___  /  I don’t like ___','items':[
            ('rain 🌧️ or sunshine ☀️?','🌦️'),('coffee ☕ or hot chocolate 🍫?','☕'),
            ('candles 🕯️ or flowers 🌸?','🕯️'),('a bonfire 🔥 or fresh air 🌬️?','🔥'),
            ('sweet 🍪 or fresh 🌿 smells?','👃'),('new books 📚 or old books 📖?','📚')]},
        'speak_title':'🗣️ Autumn smells like… 🍂','frame_hint':'Use the sentences to talk about autumn!',
        'frames':['Autumn smells like ___ .','My favourite smell is ___ .','It reminds me of ___ .',
                  'I smell it when ___ .','I don’t like the smell of ___ .'],
        'bye':'🍂 See you next time! 💜'}

def adv(sub,vocab,disc):
    return {'level':'adv','theme':'What autumn smells like','emoji':EMO,'title_bg':'FFE6D0','subtitle':sub,
        'mood_q':'Which smell takes you back? 👃','moods':[('😄','Great'),('😌','Calm'),('🙂','Good'),('🤔','Thoughtful'),('😴','Sleepy')],
        'lead_in':LEAD_ADV,'video_url':VID,'video_qs':VQ,'vocab_title':'👃 New words! 🍂','vocab':vocab,
        'games':[{'type':'quiz','bg':'FFF7D4'},
                 {'type':'board','bg':'D4ECFF','questions':[
                     'Describe a smell you love - without naming it. We guess!',
                     'A smell that instantly brings a memory back. Tell us the memory.',
                     'Which smell should a perfume company bottle for autumn? Why?',
                     'Is there a smell everybody likes except you?',
                     'Sweet or fresh scents - and why?',
                     'What does YOUR home smell like to a guest?']}],
        'disc':disc,'bye':'🍂 See you next time! 💜'}

W1012=['rain','pumpkin','wood','leaves','coffee','candle']
W13  =['rain','pumpkin','coffee','leaves','candle','cinnamon']
ADV1012=[('smell','what you notice with your nose'),('scent','a pleasant, light smell'),
         ('damp','slightly wet and cold'),('earthy','smelling of soil and wet ground'),
         ('fresh','clean and new, like air after rain'),('comforting','making you feel safe and calm')]
ADV13=[('scent','a pleasant smell, often a light one'),('aroma','a strong, pleasant smell of food or drink'),
       ('damp','slightly wet, the way air feels in autumn'),('earthy','smelling of soil, leaves and wet ground'),
       ('linger','to stay in the air long after it appeared'),('evoke','to bring a feeling or a memory back')]

DISC1012={'headline':'Ranking 🏆','statement':'🍂 Rank the coziest autumn smells:',
  'options':['rain 🌧️','coffee ☕','bonfire 🔥','cinnamon 🌰'],
  'tasks':['Put them in order and explain your number one.','Compare with a partner - do you agree? Why / why not?',
           'Describe one smell so well that we can almost smell it.']}
DISC13={'headline':'Role-play 🎭','statement':'👃 Describe a smell - we guess the memory.',
  'options':['Describe 🗣️','Guess 🤔'],
  'tasks':['Think of a smell tied to a real memory. Describe the scene, never name the smell.',
           'The others ask questions and guess both the smell and the memory.',
           'Swap roles. Then: which memory was the easiest to guess, and why?']}

VERSIONS=[
  ('10-12 Beginners',beg('Speaking Club · 10-12 Beginners',ICO,W1012),
      'Разбери новые слова по картинкам (это единственный слайд с подписями).',
      'Beginners говорят по рамке "This or That".','Beginners рассказывают про запахи осени по рамкам.'),
  ('10-12 Advanced',adv('Speaking Club · 10-12 Advanced',ADV1012,DISC1012),
      'Разбери слова и определения, проси пример в предложении.',
      'Разбери "Useful language for discussion" - фразы нужны весь урок.',
      'MAIN SPEAKING (Ranking): ранжируем запахи, требуем аргументы и уточняющие вопросы.'),
  ('13+ Beginners',beg('Speaking Club · 13+ Beginners',ICO,W13),
      'Разбери новые слова по картинкам (это единственный слайд с подписями).',
      'Beginners говорят по рамке "This or That".','Beginners рассказывают про запахи осени по рамкам.'),
  ('13+ Advanced',adv('Speaking Club · 13+ Advanced',ADV13,DISC13),
      'Разбери слова и определения, проси пример в предложении.',
      'Разбери "Useful language for discussion" - фразы нужны весь урок.',
      'MAIN SPEAKING (Role-play): описываем запах, остальные угадывают воспоминание.'),
]

if __name__=='__main__':
    out=sys.argv[1] if len(sys.argv)>1 else 'final'
    os.makedirs(out,exist_ok=True)
    for grp,cfg,s5,s6,s9 in VERSIONS:
        cfg['notes']=notes(cfg['level'],VID,s5,s6,s9)
        build(cfg,f'{out}/Speaking Clubs {grp} {cfg["theme"]}.pptx')
    print('ALL DONE ->',out)
