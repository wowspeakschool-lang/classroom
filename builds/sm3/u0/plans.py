# -*- coding: utf-8 -*-
"""Поурочные планы SM3 · Unit 0 — четыре урока, формат SM3.

    python3.13 builds/sm3/u0/plans.py builds/sm3/u0

Формат повторяет действующие планы SM3 (Unit 1 Lesson 2, Unit 2 Lesson 1):
шапка «Unit · Topic · Aims · HOMEWORK» и таблица Stage · Time · Tasks ·
Alternative. Презентаций в SM3 нет — урок идёт по учебнику и ссылкам.

Требования методиста: в каждом уроке speaking task; презентация лексики —
картинками и флеш-карточками; презентация грамматики — guided discovery,
без объяснений по-русски и без лекции, обязательно CCQ.
"""
import sys, os
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.section import WD_ORIENT

OUT = sys.argv[1]

BAAM = ('Baamboozle - name 3 https://www.baamboozle.com/game/202322\n'
        'Hangman\n“Simon says…”')
BYE = ('Ask to send a reaction\n'
       'Goodbye song https://www.youtube.com/watch?v=UQfvAlmr5g0 you can use the '
       'link or you can find the video "See You Later Alligator  Goodbye Songs" '
       'in the folder.')
DOJO = ('Class Dojo https://www.classdojo.com/\n'
        'Give students feedback and give them start/points. ALWAYS tell them what '
        'that point is for - for hard work, for correct answers, for behavior, for '
        'homework. Tell what they need to improve.\n'
        'Ask students for the feedback: what activities they liked, what was easy '
        'or difficult. You may spend 1-2 mins for this and perform this in Russian')
CHECK = ('Ask kids to remember the goals and ask whether you have completed '
         'everything (you can write it on the white board and ask students to tick).')

LESSONS = [
 dict(
  num=1,
  topic='Meet The Explorers: upstairs, downstairs, cellar; numbers 21–100',
  aims=['Meet the characters of the course',
        'Learn new words: upstairs, downstairs, cellar',
        'Revise numbers 21–100'],
  hw='SM3 Unit 0 Homework 1',
  rows=[
   ('Warm-up', '3-5',
    'Ask students about their mood, if they have anything new, anything '
    'interesting, etc.', BAAM),
   ('Revision\\HW check', '5', 'Start of the course - no homework.', ''),
   ('PlAN of the lesson', '',
    'Meet the characters\nLearn new words\nRevise numbers\nPlay and have fun', ''),
   ('LEAD in', '2-5',
    'SB p. 4 - look at the picture, books closed is not needed here. Ask:\n'
    'Who can you see? Where are they? What is the dog doing?\n'
    'Then read the text about The Explorers together and ask: What do Ben and '
    'Lucy do? Do you like adventures?',
    'Show the picture of a castle and ask what can be inside.'),
   ('Presentation', '10-15',
    'Pre-teach the words with pictures (match the word to the picture): '
    'https://wordwall.net/resource/4108558/english/sm3-unit-0\n'
    'SB p. 4 ex. 1 (audio 001) - listen and say the words: upstairs, '
    'twenty-one – fifty, downstairs, fifty-one – one hundred, cellar.\n'
    'CCQ: Is the cellar under the house or on the top? Is it usually dark there? '
    'If my room is on the second floor, is it upstairs or downstairs?\n'
    'Say a word - students point at it on the picture.',
    'Draw a simple house on the board: top floor / ground floor / cellar, and '
    'put the words on it.'),
   ('Controlled Practice', '10-15',
    'SB p. 4 ex. 2 (audio 002) - listen and answer: What do Ben and Lucy want to '
    'find? Where are they? Where does Lucy want to go? Where is the cellar?\n'
    'Numbers: flashcards https://wordwall.net/resource/121672835/numbers-0-100-flashcards '
    '- open about 10 cards only, students read the number aloud. '
    '(не открывайте все карточки, 10 достаточно)',
    'Dictation: say 6 numbers (34, 48, 55, 67, 81, 100), students write them down '
    'and then read back.'),
   ('Freer Practice', '10-15',
    'SPEAKING - “Hide the treasure”.\n'
    'Each student draws a quick house: upstairs, downstairs, cellar, and writes a '
    'room number from 21 to 100 in each part. Then they hide the treasure in one '
    'room and keep it secret.\n'
    'The others guess: Is it upstairs? Is it in room 45? - the owner answers Yes, '
    'it is / No, it isn’t. The one who guesses hides the treasure next.\n'
    'Model it yourself first: hide your treasure and let the students ask.',
    'SB p. 4 ex. 3 - close your book and play the memory game: Where’s …? - '
    'Upstairs.'),
   ('Cooler', '5',
    'Number race: say a number (21-100), students write it as fast as they can and '
    'show you; then one student says a number and the others write.',
    'Play a game https://www.baamboozle.com/game/202322'),
   ('PlAN of the lesson CHECK', '', CHECK, ''),
   ('Feedback\\HW', '5', DOJO, BYE),
  ]),

 dict(
  num=2,
  topic='be good at + Ving',
  aims=['Learn new grammar: be good at + Ving',
        'Practise talking about what you are good at',
        'Sing the song and have fun'],
  hw='SM3 Unit 0 Homework 2',
  rows=[
   ('Warm-up', '3-5',
    'Ask students about their mood, if they have anything new, anything '
    'interesting, etc.', BAAM),
   ('Revision\\HW check', '5',
    'Give a little feedback on the students’ homework. Check the words: upstairs, '
    'downstairs, cellar, and a few numbers 21-100.', ''),
   ('PlAN of the lesson', '',
    'Learn new grammar\nPractise new grammar\nSing a song\nHave fun', ''),
   ('LEAD in', '2-5',
    'Mime two things: one you do well and one you do badly (dancing, cooking, '
    'drawing). Ask: Am I good at this? Let students answer yes/no and guess what '
    'you are doing.', 'Show two pictures: a person playing football well and '
    'falling down. Ask: Who is good at football?'),
   ('Presentation', '10-15',
    'GUIDED DISCOVERY - no Russian explanations, no teacher lecture.\n'
    'Write on the board the sentences from SB p. 5 Language focus:\n'
    'I’m good at climbing trees. / I’m good at playing football. / '
    'I’m not good at telling lies.\n'
    'Ask students to look and answer:\n'
    '1 What word comes after good at - climb or climbing?\n'
    '2 How do we make it negative?\n'
    '3 Can you say “I’m good at climb trees”? Why not?\n'
    'Let them give you the rule in their own words, then show SB p. 5 ex. 3 '
    '(audio 003) - watch, listen and say.\n'
    'CCQ: “Lucy is good at riding bikes” - does she ride well or badly? Does she '
    'do it often? Is “riding” a noun or a verb here? Do we always use -ing after '
    'good at?',
    'Elicit three more examples from the students and write them on the board in '
    'two columns: good at / not good at.'),
   ('Controlled Practice', '10-15',
    'SB p. 5 ex. 1 - look, read and write B (Ben) or L (Lucy).\n'
    'SB p. 5 ex. 2 - put the words in order and say the sentences.\n'
    'OR instead of ex. 2: https://wordwall.net/resource/21668829/sm3-good-at\n'
    'SB p. 5 ex. 4 - look at the table and make sentences: Lucy isn’t good at '
    'painting.',
    'Ask students to correct wrong sentences you say: “Ben is good at play the '
    'guitar” - students fix it.'),
   ('Freer Practice', '10-15',
    'SPEAKING - activity cards: https://wordwall.net/resource/21590223/english/good-at-bad-at\n'
    'A student opens a card and says a true sentence about himself: I’m good at '
    'dancing / I’m not good at dancing. Then he asks another student: Are you good '
    'at dancing?\n'
    'Keep a score: who finds two things they are both good at.',
    'Chain game: S1 “I’m good at swimming.” S2 “He’s good at swimming and I’m good '
    'at drawing.” - each student repeats the previous one.'),
   ('Cooler', '5',
    'EXTRA (if there is time) - SB p. 6 ex. 1 (audio 004): listen and sing the song '
    '“The Explorers”. SB p. 6 ex. 3 - write your own verse: I’m good at … And … '
    'I’m an action hero. Just like Ben and Lucy.',
    'SB p. 6 ex. 2 - ask and answer in pairs: What are you good at?'),
   ('PlAN of the lesson CHECK', '', CHECK, ''),
   ('Feedback\\HW', '5', DOJO, BYE),
  ]),

 dict(
  num=3,
  topic='Family; possessive ’s',
  aims=['Learn family words',
        'Learn the possessive ’s',
        'Talk about your own family'],
  hw='SM3 Unit 0 Homework 3',
  rows=[
   ('Warm-up', '3-5',
    'Ask students about their mood, if they have anything new, anything '
    'interesting, etc.', BAAM),
   ('Revision\\HW check', '5',
    'Give a little feedback on the students’ homework. Ask two or three students: '
    'What are you good at? What are you not good at?', ''),
   ('PlAN of the lesson', '',
    'Learn family words\nLearn how to use ’s\nTalk about your family\nHave fun', ''),
   ('LEAD in', '2-5',
    'Show your own family photo or a drawing of a family tree on the board. Point '
    'at the people and ask: Who is this? How many people are there in my family?',
    'Show a picture of a famous cartoon family and ask who is who.'),
   ('Presentation', '10-15',
    'FAMILY WORDS - with the picture, not with translation.\n'
    'SB p. 7 - look at the family tree. Point at the people and present the words: '
    'grandfather, grandmother, parents, son, daughter, grandson, granddaughter, '
    'uncle, aunt, cousins.\n'
    'CCQ: Jack is Nick’s grandfather - is Jack young or old? Is Oliver Jack’s son '
    'or Jack’s brother? Are cousins in the same family?\n\n'
    'GRAMMAR ’s - guided discovery. Write two sentences on the board:\n'
    'This is Greg. He’s Gina’s brother.\n'
    'Ask: In “He’s” what does ’s mean? And in “Gina’s brother”? Who has got a '
    'brother - Greg or Gina?\n'
    'Let the students tell you the rule, then show SB p. 7 ex. 3 (audio 006) - '
    'watch, listen and say.\n'
    'CCQ: “Nick’s dog” - who has got the dog? “She’s Greg’s sister” - is ’s here '
    'is or belongs to?',
    'Draw a simple tree on the board with the students’ own names and present the '
    'words on it.'),
   ('Controlled Practice', '10-15',
    'SB p. 7 ex. 1 - look at the family tree and circle the right word (brother / '
    'father, cousin / sister, uncle / father, mother / sister).\n'
    'SB p. 7 ex. 2 - add the missing ’s: Tom is Simon father. Simon is Tom son.\n'
    'Choose the right answer: https://wordwall.net/resource/27447398/u1-p13-possessive-s-s',
    'Say a sentence with a mistake - “Nick is Julia grandson” - students correct it.'),
   ('Freer Practice', '10-15',
    'SPEAKING - “Guess who”.\n'
    'SB p. 7 ex. 4 - each student quickly draws his own family tree (3-6 people, '
    'names only).\n'
    'Then he describes one person without naming the relation: This is Sue. She’s '
    'Ron’s daughter and she’s my mother. The others ask: Is she your aunt? Is she '
    'your sister? and guess who it is.\n'
    'Every guess must use ’s or a family word.',
    'In pairs: students swap trees and ask about each other’s families - Who’s '
    'this? Is Anna your cousin?'),
   ('Cooler', '5',
    'Quick chain: teacher says “Nick’s grandmother” - students answer “Julia”, and '
    'so on by the family tree from SB p. 7.',
    'Play a game https://www.baamboozle.com/game/202322'),
   ('PlAN of the lesson CHECK', '', CHECK, ''),
   ('Feedback\\HW', '5', DOJO, BYE),
  ]),

 dict(
  num=4,
  topic='Story “The old book”; phonics: short vowel sounds',
  aims=['Read and understand the story',
        'Practise short vowel sounds',
        'Act out the story'],
  hw='SM3 Unit 0 Homework 4',
  rows=[
   ('Warm-up', '3-5',
    'Ask students about their mood, if they have anything new, anything '
    'interesting, etc.', BAAM),
   ('Revision\\HW check', '5',
    'Give a little feedback on the students’ homework. Ask: Who is Nick’s '
    'grandfather? Who is your mother’s sister?', ''),
   ('PlAN of the lesson', '',
    'Read the story\nFind out who gets the book\nPractise sounds\nAct and have fun', ''),
   ('LEAD in', '2-5',
    'SB p. 8 - look at the pictures only, do not read yet. Ask: Who is in the '
    'story? Where are they? What is Buster doing? What do you think the two adults '
    'want?', 'Ask students to predict in one sentence: I think they want … '),
   ('Reading', '10-15',
    'SB pp. 8-9 (audio 007) - “The old book”. First listen and follow, then read it '
    'by roles: Ben, Lucy, Horax, Zelda. Ask after each pair of pictures: Who’s got '
    'the book now?\n'
    'SB p. 9 ex. 2 - write t (true) or f (false): Ben and Lucy go to the cellar; '
    'Buster finds the old book; Horax and Zelda are good people; Horax and Zelda '
    'want the book; Buster is a dog; Buster helps The Explorers to get the book '
    'back.',
    'Read one picture each, round the class; the next student has to say what '
    'happened before.'),
   ('Listening', '10-15',
    'Put the pictures of the story in the right order: '
    'https://wordwall.net/resource/75226934/sm3-unit-0-story\n'
    'Then close the books and retell the story together: first…, then…, after '
    'that…, at the end…',
    'Say a line from the story - students say who said it and what happened next.'),
   ('Phonics focus', '10-15',
    'SB p. 9 ex. 3 - find who says “Let’s get them” (Zelda).\n'
    'SB p. 9 ex. 4 (audio 008) - listen and say: Gus pats his pets a lot.\n'
    'Short vowel sounds: /a/ /e/ /i/ /o/ /u/ - say the sentence slowly, students '
    'clap on every short vowel. Then sort words you say into five groups: cat, '
    'pet, big, dog, cup, hat, ten, fish, box, run.\n'
    'CCQ: Is the sound in “pets” long or short? Does “Gus” sound like “goose”?',
    'Tongue twister race: who can say “Gus pats his pets a lot” three times '
    'without a mistake.'),
   ('Freer Practice', '10-15',
    'SPEAKING - act out the story.\n'
    'In pairs or threes students choose two pictures from the story and act them '
    'out with their own words (Ben, Lucy, Horax, Zelda, Buster). The others guess '
    'which pictures they are showing.\n'
    'Then ask: What happens next? Each student gives one sentence to continue the '
    'story.',
    'Hot seat: one student is Horax, the others ask him questions - Why do you '
    'want the book? Are you a good person?'),
   ('PlAN of the lesson CHECK', '', CHECK, ''),
   ('Feedback\\HW', '5', DOJO, BYE),
  ]),
]


def build(les):
    doc = Document()
    sec = doc.sections[0]
    # как в образцах SM3: альбомная А4, поля 2.5 см
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
    for m in ('left_margin', 'right_margin'):
        setattr(sec, m, Cm(2.5))
    for m in ('top_margin', 'bottom_margin'):
        setattr(sec, m, Cm(1.6))
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(10)

    def para(text, size=10, bold=False, after=2):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(after)
        r = p.add_run(text)
        r.font.size = Pt(size)
        r.bold = bold
        return p

    para(f'Unit 0 Lesson {les["num"]}', size=14, bold=True)
    para(f'Topic: {les["topic"]}', size=11, bold=True, after=4)
    para('Aims:', bold=True)
    for a in les['aims']:
        para(a)
    para('')
    para('HOMEWORK:', bold=True)
    para(f'Домашнее задание на платформе. Название: {les["hw"]}')
    para('Зайдите на платформу, добавьте урок, войдите в Мой класс и впишите '
         'домашнее задание.', after=8)

    rows = [('Stage', 'Time', 'Tasks', 'Alternative')] + les['rows']
    t = doc.add_table(rows=len(rows), cols=4)
    t.style = 'Table Grid'
    t.autofit = False
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = t.rows[ri].cells[ci]
            cell.text = ''
            for li, line in enumerate(str(val).split('\n')):
                p = cell.paragraphs[0] if li == 0 else cell.add_paragraph()
                p.paragraph_format.space_after = Pt(1)
                r = p.add_run(line)
                r.font.size = Pt(9)
                r.bold = (ri == 0) or (ci == 0 and ri > 0)
    for row in t.rows:
        for i, w in enumerate((2.5, 2.2, 12.5, 8.5)):   # как в образцах
            row.cells[i].width = Cm(w)

    path = os.path.join(OUT, f'Unit 0 Lesson {les["num"]}.docx')
    doc.save(path)
    print('сохранён:', path)


for l in LESSONS:
    build(l)
