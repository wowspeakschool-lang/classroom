#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Заметки преподавателю — по одной на КАЖДЫЙ слайд, в поле «Заметки к слайду».

Аня, 25.11.2026: «инструкции нужно расписывать для преподавателя в Teachers
Notes, что делают, какие там, может быть, слова elicit из ученика… и плюс для
каждого слайда». На образце: «короче».

Поэтому формат жёсткий: что делает учитель → что вытягиваем (ELICIT) → минуты.
Две-три строки, не больше. Слайд 2 с общим планом остаётся по-русски — он для
методиста, а не для урока.
"""

def _j(*l): return '\n'.join(x for x in l if x)

TITLE = _j('OPEN THE CLUB. Read the theme and ask what comes to mind.',
           'ELICIT single words, no correcting. 1 min.')

NOTES_SLIDE = _j('YOUR NOTES — students never see this slide.',
                 'Hide it (right-click → Hide Slide) or arrow past it.')

MOOD = {
 'emoji':   _j('WARM-UP. Each student picks a face and says why in one sentence.',
               'ELICIT "I am … because …". No correcting here. 2-3 min.'),
 'scale':   _j('WARM-UP. Each student gives a number 1-5 and one reason.',
               'ELICIT the reason, not the number. No correcting. 2-3 min.'),
 'weather': _j('WARM-UP. Each student picks a weather word for their mood.',
               'ELICIT "I am sunny because …". Odd answers are good. 2-3 min.'),
 'oneword': _j('WARM-UP. One word about today, then one sentence to explain it.',
               'ELICIT the word first, the story second. 2-3 min.'),
}

LEAD = {
 'questions':    _j('LEAD-IN. Ask down the list, nominate by name.',
                    'ELICIT opinions and examples, two students per question. 4-5 min.'),
 'truefalse':    _j('LEAD-IN. Read each line about yourself; the group guesses true or false.',
                    'ELICIT "I think it is false because …". Reveal after each. 4-5 min.'),
 'finish':       _j('LEAD-IN. Each student finishes a line their own way.',
                    'ELICIT a full sentence plus one follow-up question. 4-5 min.'),
 'handsup':      _j('LEAD-IN. Hands up on each line, then pick one student and ask why.',
                    'ELICIT "I put my hand up because …". Keep it fast. 3-4 min.'),
 'associations': _j('LEAD-IN. First three words that come to mind for each prompt.',
                    'ELICIT the three words, then "why that one?" for one. 4-5 min.'),
}

VOCAB_BEG = _j('NEW WORDS. Elicit each word from the picture BEFORE you show it,',
               'then drill: group twice, three students alone. Watch the stress.',
               'ELICIT meaning, not repetition: "When do you …?" 5-6 min.')

VOCAB_ADV = _j('NEW WORDS. Read the definition, elicit the word before showing it.',
               'ELICIT one example sentence per item from a different student.',
               'Say plainly: these are the words you want in the final task. 6 min.')

USEFUL = _j('USEFUL LANGUAGE. Do not drill. Say you will tick these off in the discussion.',
            'ELICIT one example per block, then move on. 2 min.')

GAMES = {
 'quiz':       _j('GAME: word hunt. Slideshow mode only (F5).',
                  'Wrong card returns to the question. ELICIT "why that one?"'),
 'pic2word':   _j('GAME: look and say. Slideshow mode only (F5).',
                  'ELICIT the word inside a sentence, not on its own.'),
 'silhouette': _j('GAME: what is in the shadow? Slideshow mode only (F5).',
                  'ELICIT "I think it is … because of the shape". Take two wrong guesses first.'),
 'zoom':       _j('GAME: zoomed in. Slideshow mode only (F5).',
                  'ELICIT hedging: "It could be …", "Maybe it is …".'),
 'missing':    _j('GAME: what is missing? Ten seconds to look, then advance. F5 only.',
                  'ELICIT the full sentence: "The … is missing".'),
 'flip':       _j('GAME: card by card. Slideshow mode only (F5).',
                  'ELICIT a sentence about themselves, not a dictionary example.'),
 'truefalse':  _j('GAME: true or false. Slideshow mode only (F5).',
                  'ELICIT the correction when it is false: "No, it is a …".'),
 'odd':        _j('GAME: odd one out. Slideshow mode only (F5).',
                  'ELICIT the reason, not the answer. Any defendable reason counts.'),
 'taboo':      _j('GAME: taboo. Slideshow mode only (F5). Slide faces away from the describer.',
                  'ELICIT paraphrase. Stop them the moment a banned word slips out.'),
 'board':      _j('GAME: question board. A student picks a number. F5 only.',
                  'ELICIT a real answer plus a follow-up question from somebody else.',
                  'The slowest and most valuable part of the deck — give it room.'),
 'twotruths':  _j('GAME: two truths, one lie, using the new words. F5 only.',
                  'ELICIT the challenge: "I think two is a lie because …". No silly lies.'),
}

MINI = {
 'thisorthat': _j('MINI TASK: this or that. Each student picks one and says why.',
                  'ELICIT "I would rather … because …". No sitting on the fence. 4 min.'),
 'finish':     _j('MINI TASK: finish each line, round the group.',
                  'ELICIT full sentences with the new words. Read two best again. 4-5 min.'),
 'findsomeone':_j('MINI TASK: find someone who. Drill the question form first.',
                  'ELICIT the report: "I found Masha, she …". That is the task. 6 min.'),
 'guess':      _j('MINI TASK: guess who. You read an answer, the group guesses whose.',
                  'ELICIT "I think it is … because …". 5 min.'),
 'chain':      _j('MINI TASK: word chain. Repeat the others, then add your line.',
                  'ELICIT accurate repetition. Start again if the chain breaks. 5 min.'),
}

VIDEO = {
 'after':      _j('VIDEO. Click the BUTTON, not the text. Watch once, then the questions.',
                  'ELICIT opinions, not plot retelling. 6-8 min.'),
 'count':      _j('VIDEO. Give the counting task BEFORE you press play. Watch twice.',
                  'ELICIT the numbers, then the examples behind them. 6-8 min.'),
 'predict':    _j('VIDEO. Guess the answers BEFORE watching, write them up, then check.',
                  'ELICIT "I think they will …". The guessing is the point. 6-8 min.'),
 'threewords': _j('VIDEO. Three words each, warn them first, play twice.',
                  'ELICIT the words, then a sentence with one of them. 7-8 min.'),
 'nosound':    _j('VIDEO. First half with no sound, then again with sound.',
                  'ELICIT "Maybe he is saying …". 7-8 min.'),
}

PROP = _j('PROP SLIDE. Leave it up for the whole task — they need to look at it.',
          'Read the bottom line aloud and elicit the first move from one student.')

SPEAK_BEG = _j('MAIN SPEAKING. One minute to read the frames, then one student at a time.',
               'ELICIT the new words; two questions from the group after each speaker.',
               'Correct at the END, three mistakes together. 10-12 min.')

SPEAK_ADV = _j('MAIN SPEAKING. Thirty seconds thinking, then go. No notes if possible.',
               'ELICIT the target words and the useful phrases — tick them off.',
               'Push back once per speaker. Correct at the END. 12-15 min.')

BYE = _j('CLOSING. Each student names one word they will use this week, and where.',
         'Then one specific piece of praise per student, by name — not "well done".')

SERVICE = _j('SERVICE SCREEN — part of a game, not a lesson slide.',
             'They sit at the end on purpose. In F5 the game jumps here and back.')
