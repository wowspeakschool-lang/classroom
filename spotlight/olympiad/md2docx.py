"""Простой перевод markdown-файла олимпиады в .docx: заголовки, абзацы, списки, таблицы, **жирный**.
Запуск: python3 spotlight/olympiad/md2docx.py <вход.md> <выход.docx>"""
import re, sys
from docx import Document
from docx.shared import Pt

def runs(par, text):
    for i, part in enumerate(re.split(r'\*\*(.+?)\*\*', text)):
        part = part.replace('`', '')
        if part:
            par.add_run(part).bold = bool(i % 2)

def main(src, dst):
    doc = Document()
    st = doc.styles['Normal']; st.font.name = 'Times New Roman'; st.font.size = Pt(12)
    lines = open(src, encoding='utf-8').read().splitlines()
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            t = doc.add_table(rows=len(rows), cols=max(len(r) for r in rows)); t.style = 'Table Grid'
            for r, row in enumerate(rows):
                for c, val in enumerate(row):
                    p = t.cell(r, c).paragraphs[0]; runs(p, val)
                    if r == 0 and any(rows[0]):
                        for run in p.runs: run.bold = True
            doc.add_paragraph()
            continue
        m = re.match(r'(#+) (.*)', l)
        if m:
            doc.add_heading(m.group(2), level=min(len(m.group(1)) - 1, 3) or 0)
        elif re.match(r'\s*[-*] ', l):
            runs(doc.add_paragraph(style='List Bullet'), re.sub(r'^\s*[-*] ', '', l))
        elif re.match(r'\d+\. ', l):
            runs(doc.add_paragraph(style='List Number'), re.sub(r'^\d+\. ', '', l))
        elif l.strip():
            runs(doc.add_paragraph(), l)
        i += 1
    doc.save(dst)

if __name__ == '__main__':
    main(*sys.argv[1:3])
