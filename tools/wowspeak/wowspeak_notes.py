#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Заметки преподавателю — по одной на КАЖДЫЙ слайд, в поле «Заметки к слайду».

Аня, 25.11.2026: «инструкции нужно расписывать для преподавателя в Teachers
Notes, что делают, какие там, может быть, слова elicit из ученика. Не прям
супер подробно, но не так коротко, как ты, и на английском языке. И плюс для
каждого слайда. Не просто затем видео, затем вот это вот, а именно прям по
слайдам».

Слайд 2 с общим планом остаётся как был, по-русски — он для методиста. Здесь
то, что преподаватель читает под слайдом во время урока.

Формат каждой заметки: что делает учитель → что вытягиваем из ученика → время.
Держим в три-пять строк: длиннее никто не читает на уроке.
"""

A = '— '   # маркер строки

def _j(*lines): return '\n'.join(l for l in lines if l)

TITLE = _j(
 'OPEN THE CLUB.',
 'Read the theme aloud and ask: "What comes into your head when you hear this?"',
 'Take two or three answers. Do NOT correct anything here — you are only warming',
 'up the room and showing that talking is safe.',
 'ELICIT: single words, any level. 1 minute.')

NOTES_SLIDE = _j(
 'YOUR NOTES — the students never see this one.',
 'Right-click the slide in the left-hand strip and choose Hide Slide, or simply',
 'press the arrow twice at the start.')

MOOD = {
 'emoji': _j('WARM-UP: how are you today?',
   'Every student picks a face and says why, in ONE sentence.',
   'ELICIT the full frame: "I am ... because ...". Model it yourself first.',
   'Do not correct grammar here. If a student gives one word, ask "Why?" once.',
   '2-3 minutes for the whole group.'),
 'scale': _j('WARM-UP: rate your day from 1 to 5.',
   'Every student gives a number and ONE reason.',
   'ELICIT: "Today is a four because ...". Push for the reason, not the number.',
   'Do not correct grammar here.',
   '2-3 minutes for the whole group.'),
 'weather': _j('WARM-UP: what is your weather today?',
   'Every student picks a weather word for their mood and says why.',
   'ELICIT: "I am sunny today because ...". Model it yourself first.',
   'This is the one place where a strange answer is a good answer — let it run.',
   '2-3 minutes for the whole group.'),
 'oneword': _j('WARM-UP: one word about today.',
   'Every student gives ONE word, then explains it in one sentence.',
   'ELICIT: the word first, the reason second — do not let them start with the story.',
   'Do not correct grammar here.',
   '2-3 minutes for the whole group.'),
}

LEAD = {
 'questions': _j('LEAD-IN: open questions.',
   'Ask the questions down the list. Nominate by name — do not wait for volunteers.',
   'ELICIT opinions and personal examples. Two students per question is enough.',
   'Reformulate a good answer back in better English instead of correcting it.',
   'The target words are NOT here on purpose: they come on the next slide. 4-5 minutes.'),
 'truefalse': _j('LEAD-IN: true or false about me.',
   'Read each line about YOURSELF. The group guesses TRUE or FALSE and says why.',
   'ELICIT: "I think it is false because you ...". Push for the "because".',
   'Reveal the answer after each line — the surprise is what gets them talking.',
   '4-5 minutes.'),
 'finish': _j('LEAD-IN: finish the sentence.',
   'Each student finishes a line their own way, out loud.',
   'ELICIT a full sentence, not just the ending. Ask one follow-up question each.',
   'If a student is stuck, give YOUR ending first and let them copy the shape.',
   '4-5 minutes.'),
 'handsup': _j('LEAD-IN: hands up if...',
   'Read each line. Everybody who agrees puts a hand up — then you pick one and ask why.',
   'ELICIT: "I put my hand up because ...". Count the hands aloud: it makes it a game.',
   'Fast and physical; do not let it slow into a discussion yet.',
   '3-4 minutes.'),
 'associations': _j('LEAD-IN: first three words.',
   'Read each prompt. Each student says the first three words that come to mind.',
   'ELICIT: the three words, then "Why that one?" for ONE of them.',
   'Write the best words up where everybody can see them — you will reuse them later.',
   '4-5 minutes.'),
}

VOCAB_BEG = _j(
 'NEW WORDS — the heart of the lesson. Do not rush it.',
 '1. Point at a picture and ELICIT the word first. Never read it out before they try.',
 '2. If nobody has it, give it, then drill: whole group twice, then three students alone.',
 '3. Check meaning, not repetition: "Show me", "When do you ...?", "Is this ... ?"',
 'Watch the stress — mark the stressed syllable with your hand as they repeat.',
 '5-6 minutes for six words.')

VOCAB_ADV = _j(
 'NEW WORDS — definition first, word second.',
 '1. Read the definition and ELICIT the word from the group before you show it.',
 '2. When it comes, ask ONE student for an example sentence with it.',
 '3. Ask the group: "Would you use this with a friend, or in an essay?"',
 'These are the words you will demand in the main speaking task — say so now.',
 '6 minutes for six items.')

USEFUL = _j(
 'USEFUL LANGUAGE — do not drill this slide.',
 'Read the four blocks aloud and tell the group plainly: these are the phrases you',
 'want to HEAR in the discussion later, and you will be ticking them off.',
 'ELICIT one example per block from a volunteer, then move on.',
 '2 minutes. Leave the slide up if you can — they will look back at it.')

GAMES = {
 'quiz': _j('GAME — word hunt.',
   'Slideshow mode only (F5): the buttons are dead in editing view.',
   'Read the question, the group chooses. A wrong card sends you back to the same',
   'question, a right one moves on. ELICIT the reason: "Why that one?"',
   'Let a quiet student answer first — the game is easy on purpose.'),
 'pic2word': _j('GAME — look and say.',
   'Slideshow mode only (F5). Show the picture, the group picks the word.',
   'ELICIT the word in a sentence after the correct answer, not just the word.',
   'If two students shout at once, make them take turns by name.'),
 'silhouette': _j('GAME — what is in the shadow?',
   'Slideshow mode only (F5). Only the outline is visible, so guessing is the point.',
   'ELICIT guesses with "I think it is ... because of the shape".',
   'Take two wrong guesses before you accept the right one — the wrong ones are speech.'),
 'zoom': _j('GAME — zoomed in.',
   'Slideshow mode only (F5). A close-up detail, the group names the whole object.',
   'ELICIT: "It could be ...", "Maybe it is ...". Hedging language is the prize here.',
   'Ask what part of the picture gave it away.'),
 'missing': _j('GAME — what is missing?',
   'Slideshow mode only (F5). Give the group ten seconds to look, then advance.',
   'ELICIT the full sentence: "The ... is missing", not just the word.',
   'Second round goes faster — warn them.'),
 'flip': _j('GAME — card by card.',
   'Slideshow mode only (F5). A card comes up, the student makes a sentence with it.',
   'ELICIT a sentence about THEMSELVES, not a dictionary example.',
   'Keep the pace: one card, one student, no discussion.'),
 'truefalse': _j('GAME — true or false.',
   'Slideshow mode only (F5). Read the statement under the picture; the group decides.',
   'ELICIT the correction when it is false: "No, it is a ...".',
   'The fastest game in the pack — do not stretch it.'),
 'odd': _j('GAME — odd one out.',
   'Slideshow mode only (F5). Four words, one does not belong.',
   'ELICIT the REASON, not the answer: "The others are all ..., but ... is ...".',
   'Accept any reason they can defend, even one you did not plan.'),
 'taboo': _j('GAME — taboo.',
   'Slideshow mode only (F5). One student describes the word WITHOUT the banned words.',
   'ELICIT paraphrase: "It is a thing you use when ...", "It is the opposite of ...".',
   'Stop them the moment a banned word slips out — that is the whole game.',
   'The describer faces the class, the slide faces away from them if you can manage it.'),
 'board': _j('GAME — question board.',
   'Slideshow mode only (F5). A student picks a number, you open that question.',
   'ELICIT a real answer plus one follow-up question from another student.',
   'This is the slowest and the most valuable activity in the deck — give it room.'),
 'twotruths': _j('GAME — two truths, one lie.',
   'Slideshow mode only (F5). Each student makes three statements with the new words.',
   'ELICIT the challenge from the group: "I think number two is a lie because ...".',
   'Insist that the lie is plausible — a silly lie kills the game.'),
}

MINI = {
 'thisorthat': _j('MINI TASK — this or that.',
   'Read each pair. Every student picks ONE and says why in a sentence.',
   'ELICIT: "I would rather ... because ...". No sitting on the fence.',
   '4 minutes.'),
 'finish': _j('MINI TASK — finish the sentence.',
   'Every student finishes every line in their own way, round the group.',
   'ELICIT full sentences and use the new words from the vocabulary slide.',
   'Read two of the best ones out again at the end. 4-5 minutes.'),
 'findsomeone': _j('MINI TASK — find someone who.',
   'Students walk around and ask each other until every line has a name on it.',
   'ELICIT the QUESTION form first — drill "Do you ...?" before they start.',
   'Report back: "I found Masha, she ...". That report is the real task. 6 minutes.'),
 'guess': _j('MINI TASK — guess who.',
   'You read one student\'s answer, the group guesses whose it is.',
   'ELICIT: "I think it is ... because he/she ...". Push for the reason.',
   'Collect the answers on paper first if the group is shy. 5 minutes.'),
 'chain': _j('MINI TASK — word chain.',
   'Each student repeats what the others said, then adds their own line.',
   'ELICIT accurate repetition — this is memory plus listening, not invention.',
   'Start again from the beginning if the chain breaks. 5 minutes.'),
}

VIDEO = {
 'after': _j('VIDEO.',
   'The button opens the clip in a browser — click the BUTTON, not the text.',
   'Watch once straight through. Then put the questions on screen and discuss.',
   'ELICIT opinions, not plot retelling. 6-8 minutes with the discussion.'),
 'count': _j('VIDEO — watch and count.',
   'Give the counting task BEFORE you press play: they must watch for something.',
   'Watch once, compare numbers, then watch again to settle the argument.',
   'ELICIT the numbers and then the examples behind them. 6-8 minutes.'),
 'predict': _j('VIDEO — predict first.',
   'Read the questions BEFORE watching and take guesses. Write them up.',
   'ELICIT: "I think they will ...". Then watch and check who was right.',
   'The guessing is worth more than the watching. 6-8 minutes.'),
 'threewords': _j('VIDEO — three words.',
   'Each student writes down three words they hear. Warn them before you play.',
   'Watch twice: nobody catches three words on one pass.',
   'ELICIT the words, then make each student use one in a sentence. 7-8 minutes.'),
 'nosound': _j('VIDEO — sound off first.',
   'Play the first half with NO sound. The group guesses what is being said.',
   'ELICIT: "Maybe he is saying ...". Then play it again with sound and compare.',
   'Big laughs here, and a lot of speech. 7-8 minutes.'),
}

PROP = _j(
 'PROP SLIDE — the task lives on this slide.',
 'Leave it on screen for the whole activity: the students need to look at it while',
 'they talk. Read the line at the bottom aloud before they start.',
 'ELICIT the first move from one student so the rest see what is expected.')

SPEAK_BEG = _j(
 'MAIN SPEAKING — the point of the whole lesson.',
 'Give the frames a minute of silent reading, then start. One student at a time.',
 'ELICIT the new words — if a student avoids them, ask "Can you say that with ... ?"',
 'After each speaker: TWO questions from the group. Nominate who asks.',
 'Correct at the END, not during. Write mistakes down and do three of them together.',
 '10-12 minutes.')

SPEAK_ADV = _j(
 'MAIN SPEAKING — the point of the whole lesson.',
 'Read the task, give thirty seconds of thinking time, then start. No notes if possible.',
 'ELICIT the target words and the useful-language phrases — tick them off as you hear them.',
 'Push back at least once per speaker: "But why?", "What about ... ?"',
 'Correct at the END. Pick three mistakes that matter and fix them with the group.',
 '12-15 minutes.')

BYE = _j(
 'CLOSING.',
 'Each student says ONE word from today they will use this week, and where.',
 'ELICIT the word plus the situation: "I will use ... when ...".',
 'Then give one specific piece of praise per student, by name. Not "well done" —',
 'name the thing they did: "You used three new words without looking."')

SERVICE = _j(
 'SERVICE SCREEN — part of a game, not a lesson slide.',
 'These Correct / Try again screens live at the end of the file on purpose, so that',
 'paging through the lesson never runs into them. In slideshow mode the game jumps',
 'here by itself and comes back. Do not present them in order.')
