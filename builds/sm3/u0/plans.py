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
import re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

INK = RGBColor(0x1F, 0x29, 0x37)        # основной текст
HEADC = RGBColor(0x14, 0x3A, 0x6B)      # заголовки и названия этапов
ENG = RGBColor(0x0B, 0x61, 0x6E)        # реплики на английском
ACC = RGBColor(0xB1, 0x3E, 0x0F)        # пометки: CCQ, SPEAKING, +40 мин
LINK = RGBColor(0x11, 0x55, 0xCC)
HEAD_FILL = '1F3A6B'                    # шапка таблицы — тёмно-синяя
STAGE_FILL = 'F3F7FC'                   # колонка «Stage»
ALT = RGBColor(0x5A, 0x63, 0x72)        # колонка «Alternative» — приглушённая
GRID = 'C9D4E4'


def grid(table):
    tbl = table._tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement(f'w:{edge}')
        el.set(qn('w:val'), 'single'); el.set(qn('w:sz'), '4')
        el.set(qn('w:space'), '0'); el.set(qn('w:color'), GRID)
        borders.append(el)
    tbl.append(borders)


def fixed_widths(table, cms):
    layout = OxmlElement('w:tblLayout')
    layout.set(qn('w:type'), 'fixed')
    table._tbl.tblPr.append(layout)
    gridel = table._tbl.find(qn('w:tblGrid'))
    for gc, cm in zip(gridel.findall(qn('w:gridCol')), cms):
        gc.set(qn('w:w'), str(int(cm * 567)))


def cell_margins(table, top=60, bottom=60, left=90, right=90):
    el = OxmlElement('w:tblCellMar')
    for side, val in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        node = OxmlElement(f'w:{side}')
        node.set(qn('w:w'), str(val)); node.set(qn('w:type'), 'dxa')
        el.append(node)
    table._tbl.tblPr.append(el)


def shade(cell, fill):
    tc = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill)
    tc.append(shd)


def hyperlink(par, url, label, size=9):
    rid = par.part.relate_to(url, RT.HYPERLINK, is_external=True)
    hl = OxmlElement('w:hyperlink'); hl.set(qn('r:id'), rid)
    r = OxmlElement('w:r'); rPr = OxmlElement('w:rPr')
    for tag, val in (('w:color', '1155CC'), ('w:sz', str(int(size * 2)))):
        el = OxmlElement(tag); el.set(qn('w:val'), val); rPr.append(el)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rPr.append(u)
    r.append(rPr)
    tnode = OxmlElement('w:t'); tnode.text = label; tnode.set(qn('xml:space'), 'preserve')
    r.append(tnode); hl.append(r); par._p.append(hl)


MARKS = ('GUIDED DISCOVERY', 'SPEAKING TASK', 'SPEAKING', 'CCQ:', 'EXTRA',
         '⏱ +40 мин:', '⏱ If time', 'FAMILY WORDS', 'GRAMMAR ’s', 'NO HW')
LINK_RE = re.compile(r'\[\[([^|\]]+)\|([^\]]+)\]\]')


def rich(par, line, size=9, base_colour=None, italic=False):
    """Строка с разметкой: [[подпись|url]] — ссылка, реплики T:/S: цветом,
    пометки вроде CCQ и SPEAKING — жирным оранжевым, ссылки на учебник жирным."""
    base = base_colour or (ENG if re.match(r'^\s*(T|S|S1|S2):', line) else INK)
    pos = 0
    for m in LINK_RE.finditer(line):
        _plain(par, line[pos:m.start()], base, size, italic)
        hyperlink(par, m.group(2), m.group(1), size)
        pos = m.end()
    _plain(par, line[pos:], base, size, italic)


def _plain(par, text, base, size, italic=False):
    if not text:
        return
    # жирным: пометки, ссылки на учебник (SB p. 5 ex. 2), подписи T:/S:
    pat = re.compile('(' + '|'.join(re.escape(m) for m in MARKS) +
                     r'|SB pp?\.\s?\d+(?:[-–]\d+)?(?:\s?ex\.\s?\d+)?'
                     r'|^\s*(?:T|S|S1|S2):)')
    i = 0
    for m in pat.finditer(text):
        if m.start() > i:
            _run(par, text[i:m.start()], base, size, False, italic)
        hit = m.group(0)
        colour = ACC if hit.strip() in MARKS else (base if hit.strip().endswith(':') else HEADC)
        _run(par, hit, colour, size, True, italic)
        i = m.end()
    if i < len(text):
        _run(par, text[i:], base, size, False, italic)


def _run(par, text, colour, size, bold, italic=False):
    r = par.add_run(text)
    r.font.size = Pt(size)
    r.font.color.rgb = colour
    r.bold = bold
    r.italic = italic

OUT = sys.argv[1]

BAAM = ('[[Baamboozle — name 3|https://www.baamboozle.com/game/202322]]\n'
        'Hangman\n“Simon says…”')
BYE = ('Ask to send a reaction\n'
       'Goodbye song [[Goodbye song (YouTube)|https://www.youtube.com/watch?v=UQfvAlmr5g0]] you can use the '
       'link or you can find the video "See You Later Alligator  Goodbye Songs" '
       'in the folder.')
DOJO = ('[[Class Dojo|https://www.classdojo.com/]]\n'
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
   ('PLAN of the lesson', '',
    'Meet the characters\nLearn new words\nRevise numbers\nPlay and have fun', ''),
   ('LEAD in', '2-5',
    'SB p. 4 - look at the picture, books closed is not needed here. Ask:\n'
    'Who can you see? Where are they? What is the dog doing?\n'
    'Then read the text about The Explorers together and ask: What do Ben and '
    'Lucy do? Do you like adventures?',
    'Show the picture of a castle and ask what can be inside.'),
   ('Presentation', '10-15',
    'Pre-teach the words with pictures (match the word to the picture): '
    '[[Wordwall — соедини слово с картинкой|https://wordwall.net/resource/4108558/english/sm3-unit-0]]\n'
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
    'Numbers: flashcards [[Wordwall — флеш-карточки чисел 0–100|https://wordwall.net/resource/121672835/numbers-0-100-flashcards]] '
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
    'Play a game [[Baamboozle — name 3|https://www.baamboozle.com/game/202322]]'),
   ('PLAN of the lesson CHECK', '', CHECK, ''),
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
   ('PLAN of the lesson', '',
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
    'OR instead of ex. 2: [[Wordwall — good at (вместо ex. 2)|https://wordwall.net/resource/21668829/sm3-good-at]]\n'
    'SB p. 5 ex. 4 - look at the table and make sentences: Lucy isn’t good at '
    'painting.',
    'Ask students to correct wrong sentences you say: “Ben is good at play the '
    'guitar” - students fix it.'),
   ('Freer Practice', '10-15',
    'SPEAKING - activity cards: [[Wordwall — карточки активностей (speaking)|https://wordwall.net/resource/21590223/english/good-at-bad-at]]\n'
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
   ('PLAN of the lesson CHECK', '', CHECK, ''),
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
   ('PLAN of the lesson', '',
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
    'Choose the right answer: [[Wordwall — выбери правильный ’s|https://wordwall.net/resource/27447398/u1-p13-possessive-s-s]]',
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
    'Play a game [[Baamboozle — name 3|https://www.baamboozle.com/game/202322]]'),
   ('PLAN of the lesson CHECK', '', CHECK, ''),
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
   ('PLAN of the lesson', '',
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
    '[[Wordwall — расставь кадры истории|https://wordwall.net/resource/75226934/sm3-unit-0-story]]\n'
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
   ('PLAN of the lesson CHECK', '', CHECK, ''),
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

    def para(text, size=10, bold=False, after=2, colour=INK):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(after)
        r = p.add_run(text)
        r.font.size = Pt(size)
        r.bold = bold
        r.font.color.rgb = colour
        return p

    para(f'Unit 0 Lesson {les["num"]}', size=16, bold=True, colour=HEADC)
    para(f'Topic: {les["topic"]}', size=11, bold=True, after=6, colour=ACC)
    para('Aims:', bold=True, colour=HEADC)
    for a in les['aims']:
        para('•  ' + a)
    para('')
    para('HOMEWORK:', bold=True, colour=HEADC)
    para(f'Домашнее задание на платформе. Название: {les["hw"]}', bold=True)
    para('Зайдите на платформу, добавьте урок, войдите в Мой класс и впишите '
         'домашнее задание.', after=8)

    rows = [('Stage', 'Time', 'Tasks', 'Alternative')] + les['rows']
    t = doc.add_table(rows=len(rows), cols=4)
    t.style = 'Table Grid'
    t.autofit = False
    grid(t)
    cell_margins(t)
    WIDTHS = (2.6, 1.8, 12.9, 7.4)
    fixed_widths(t, WIDTHS)
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = t.rows[ri].cells[ci]
            cell.text = ''
            if ri == 0:
                shade(cell, HEAD_FILL)
            elif ci == 0:
                shade(cell, STAGE_FILL)
            for li, line in enumerate(str(val).split('\n')):
                p = cell.paragraphs[0] if li == 0 else cell.add_paragraph()
                p.paragraph_format.space_after = Pt(2)
                if ci == 1:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                if ri == 0:
                    r = p.add_run(line); r.font.size = Pt(10)
                    r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                elif ci == 0:
                    r = p.add_run(line); r.font.size = Pt(10)
                    r.bold = True; r.font.color.rgb = HEADC
                elif ci == 1:
                    r = p.add_run(line); r.font.size = Pt(10)
                    r.font.color.rgb = HEADC; r.bold = True
                elif ci == 3:
                    rich(p, line, size=9, base_colour=ALT, italic=True)
                else:
                    rich(p, line, size=9.5)
    for row in t.rows:
        for i, w in enumerate(WIDTHS):
            row.cells[i].width = Cm(w)

    path = os.path.join(OUT, f'Unit 0 Lesson {les["num"]}.docx')
    doc.save(path)
    print('сохранён:', path)


LESSONS.append(dict(
  num=5,
  topic='Revision + Test',
  aims=['Revise the whole unit',
        'Do the unit test',
        'See what you can do now'],
  hw='NO HW - the unit is finished',
  rows=[
   ('Warm-up', '3-5',
    'Ask students about their mood, if they have anything new, anything '
    'interesting, etc.', BAAM),
   ('Revision\\HW check', '5',
    'Give a little feedback on the students’ homework. Ask two or three questions '
    'from the story: Who’s got the book at the end? Who is Horax?', ''),
   ('PLAN of the lesson', '',
    'Revise the unit\nDo the test\nSee what you can do now', ''),
   ('Revision - words and numbers', '5-7',
    'Quick rounds, no marks - this is a warm-up before the test, keep the pace up.\n'
    'Numbers: say a number 21-100, students write it; then one student says a '
    'number for the others.\n'
    'Words: Where is your bedroom? Where is the kitchen? What is in the cellar?\n'
    'Family: use the tree from SB p. 7 - Who is Nick’s grandmother? Who is Zoe’s '
    'sister?',
    'Play the flashcards again: '
    '[[Wordwall — флеш-карточки чисел 0–100|https://wordwall.net/resource/121672835/numbers-0-100-flashcards]]'),
   ('Revision - grammar', '5-7',
    'be good at + Ving: each student says one true sentence about himself and one '
    'about a friend - I’m good at…, He isn’t good at…\n'
    '’s: say a pair of names from the family tree (Jack - Nick) and students make '
    'the sentence: Nick is Jack’s grandson.',
    '[[Wordwall — выбери правильный ’s|https://wordwall.net/resource/27447398/u1-p13-possessive-s-s]]'),
   ('Test', '10-15',
    'Start the test on the platform (the link is set before the lesson).\n'
    'Students work on their own; support them, but do not give the answers.\n'
    'T: "Now a little test. You can do it!"\n'
    'There is one speaking task at the end - the recording is checked by the '
    'methodologist, so the final mark appears later.',
    'If a student finishes early, ask him to write two more sentences: one with '
    'be good at and one with ’s.'),
   ('PLAN of the lesson CHECK', '', CHECK, ''),
   ('Feedback\\HW', '5',
    DOJO + '\nNO HW - the unit is finished. Tell the students what they did well '
    'in the test and what to revise.', BYE),
   ('Cooler', '5',
    'Ask the students to say one thing they can do now that they could not do '
    'before this unit: Now I can talk about my family / Now I can say what I’m '
    'good at.', 'Play a game [[Baamboozle — name 3|https://www.baamboozle.com/game/202322]]'),
  ]))

for l in LESSONS:
    build(l)
