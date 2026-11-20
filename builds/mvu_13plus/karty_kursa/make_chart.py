"""Новая разбивка чек-листа 13+ в формате Assessment chart Анны (20.11.2026).

Берём её исходник (ishodnik/…docx) и меняем только таблицы частей 2 и 3:
у каждого Prepare вместо двух блоков «Unit 0-9 / Unit 10-20» — четыре.
Строки копируются из исходных (заголовок блока и строка темы), так что
оформление, колонки 0 / 1 / 2 и всё остальное в документе остаются как было.

    python3 builds/mvu_13plus/karty_kursa/make_chart.py
"""
import copy, os, sys
import docx

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'ishodnik', 'Assessment chart and link to Vznaniya_13-17.docx')
OUT = os.path.join(HERE, 'Assessment chart 13+ — новая разбивка (проект).docx')

# (название блока, [3 лексики + 3 грамматики]) — по картам курса, karty_kursa/prepareN.md
NEW = {
    2: [('PR 2 Unit 0-4', ['Sports', 'Daily routines and food', 'Emotions', 'Present Simple vs Present Continuous', 'Like / love / hate + -ing', 'Past Simple of be (was / were)']),
        ('PR 2 Unit 5-9', ['Jobs and work', 'Holidays', 'Clothes and materials', 'Past Simple: regular and irregular verbs', 'Past Simple: negatives and questions', 'Someone, anyone, everyone']),
        ('PR 2 Unit 10-15', ['Buying and selling', 'Technology and the internet', 'Health and illness', 'Some, any, a lot of, a few', 'Comparatives and superlatives', 'Should / shouldn’t']),
        ('PR 2 Unit 16-20', ['Animals', 'Television and entertainment', 'School and trips', 'Past Simple vs Past Continuous', 'Going to', 'Have to / don’t have to'])],
    3: [('PR 3 Unit 1-4', ['Personality adjectives', 'Geographical features and animals', 'Homes', 'Present Simple vs Present Continuous', 'Past Simple', 'Past Continuous vs Past Simple']),
        ('PR 3 Unit 5-9', ['School subjects', 'Materials and describing objects', 'Household appliances', 'Comparative and superlative adverbs', 'Future with will, may, might', 'Must / have to / don’t have to']),
        ('PR 3 Unit 10-15', ['Relationships and the internet', 'Places in a city', 'Films', 'Gerunds and infinitives', 'Relative pronouns who / which / that', 'Present Perfect (ever, never, just, yet, already, for, since)']),
        ('PR 3 Unit 16-20', ['Body parts and health', 'Books and reading', 'Cooking and ingredients', 'Present Perfect vs Past Simple', '1st Conditional', 'Present Simple and Past Simple Passive'])],
    4: [('PR 4 Unit 1-4', ['Describing people', 'Clothes', 'Sports', 'Present Simple vs Present Continuous', 'Comparatives and superlatives (not as … as)', 'Past Continuous']),
        ('PR 4 Unit 5-9', ['Crime and criminals', 'City problems', 'Money and shopping', 'Past Simple vs Past Continuous', 'Have to / must / should', 'Be going to vs Present Continuous for future']),
        ('PR 4 Unit 10-15', ['Food and drink adjectives', 'Body, health and illnesses', 'Computer phrases', 'Present Perfect vs Past Simple (for / since)', 'Modals of probability', 'Relative clauses']),
        ('PR 4 Unit 16-20', ['Jobs', 'Arts and entertainment', 'Collocations with look, see, watch', 'Zero and 1st Conditional', '2nd Conditional', 'Reported speech'])],
    5: [('PR 5 Unit 1-4', ['Shopping', 'Personality adjectives', 'Sport phrases', 'Determiners', 'Ing forms', 'Past Simple and used to']),
        ('PR 5 Unit 5-9', ['Health verbs', 'Music', 'Technology', 'Modals of obligation and advice', 'Present Perfect vs Past Simple', 'Future forms and Future Continuous']),
        ('PR 5 Unit 10-15', ['Nature and wildlife', 'Social media', 'Cooking verbs', '2nd Conditional', 'Past Perfect', 'Passive (incl. modal passives)']),
        ('PR 5 Unit 16-20', ['Film', 'Verbs of communication', 'Hopes and dreams', 'Reported speech and reporting verbs', 'Reported questions', 'Causative have'])],
    6: [('PR 6 Unit 1-4', ['Education', 'Phrasal verbs for relationships', 'Natural disasters', 'Question forms (complex)', 'Past tense review', 'Making comparisons (too, so, such)']),
        ('PR 6 Unit 5-9', ['Food and drink phrasal verbs', 'Fiction', 'Money', 'Relative clauses', 'Modals of ability and possibility', 'Future: plans, intentions, predictions']),
        ('PR 6 Unit 10-15', ['Personality adjectives', 'Accidents and emergencies', 'Reporting verbs', 'Passive: complex forms', 'Reported questions and requests', 'Causative (have / get something done)']),
        ('PR 6 Unit 16-20', ['Climate change', 'Art', 'Crime and criminals', '2nd Conditional and I wish', 'Modals of deduction in the past', '3d conditional and wish + past perfect'])],
    7: [('PR 7 Unit 1-4', ['Online, films and media', 'Abstract nouns', 'Stress and health', 'Simple, continuous or perfect', 'Present Perfect Simple and Continuous', 'Modals of necessity and obligation']),
        ('PR 7 Unit 5-9', ['History', 'Expressing emotions', 'Community', 'Present and past habits', 'Narrative tenses', 'Future Continuous and perfect']),
        ('PR 7 Unit 10-15', ['Phrasal verbs: relationships', 'Leadership and achievement', 'Global issues', 'Modals in the past', 'Passive and causative', 'Reported speech']),
        ('PR 7 Unit 16-20', ['Advertising', 'The world of work', 'Idioms', '3d and mixed Conditionals', 'Uses of verb + -ing', 'Determiners'])],
}
TABLES = {1: (2, 3, 4), 2: (5, 6, 7)}   # таблица документа → какие Prepare в её трёх колонках
COLS = (0, 5, 10)                        # колонка с названием темы у каждого Prepare


def set_text(cell, text):
    p = cell.paragraphs[0]
    runs = p.runs
    if runs:
        runs[0].text = text
        for r in runs[1:]: r.text = ''
    else:
        p.add_run(text)
    for extra in cell.paragraphs[1:]:
        for r in extra.runs: r.text = ''


def main():
    d = docx.Document(SRC)
    for ti, prs in TABLES.items():
        t = d.tables[ti]
        rows = t.rows
        head_tpl, topic_tpl = copy.deepcopy(rows[1]._tr), copy.deepcopy(rows[2]._tr)
        for r in list(rows)[1:]: t._tbl.remove(r._tr)
        for b in range(4):
            tr = copy.deepcopy(head_tpl); t._tbl.append(tr)
            row = t.rows[-1]
            for pr, col in zip(prs, COLS): set_text(row.cells[col], NEW[pr][b][0])
            for k in range(6):
                tr = copy.deepcopy(topic_tpl); t._tbl.append(tr)
                row = t.rows[-1]
                for pr, col in zip(prs, COLS): set_text(row.cells[col], NEW[pr][b][1][k])
    d.save(OUT)
    print('сохранено:', OUT)


if __name__ == '__main__':
    main()
