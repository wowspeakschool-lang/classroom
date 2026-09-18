# -*- coding: utf-8 -*-
"""Раскладывает скачанные с Диска PDF по папкам юнитов.

Коннектор Google Drive не пишет файл на диск — он возвращает JSON с base64,
и этот JSON остаётся в результатах вызовов текущей сессии. Скрипт обходит их
и раскладывает PDF по именам из поля title:

  «SM3 Unit 1 Homework 4 (1).pdf»      → u1pdf/hw4a.pdf
  «Super Minds 3 Unit 1 Test.pdf»      → u1pdf/test.pdf
  «Super Minds 3. Final test (1).pdf»  → finalpdf/final_a.pdf

    python3 tools/unpack.py                 # результаты текущей сессии
    python3 tools/unpack.py <tool-results>  # явная папка
"""
import json, base64, glob, os, re, sys

PROJECTS = '/root/.claude/projects'
PART = {'1': 'a', '2': 'b'}


def results_dir(argv):
    if len(argv) > 1:
        return argv[1]
    dirs = glob.glob(f'{PROJECTS}/*/*/tool-results') + glob.glob(f'{PROJECTS}/*/tool-results')
    if not dirs:
        raise SystemExit('не нашёл папку tool-results — укажите её аргументом')
    return max(dirs, key=os.path.getmtime)


def target(title):
    t = title.replace('.pdf', '')
    m = re.search(r'Unit (\d+) Homework (\d+)(?:\s*\((\d)\))?', t)
    if m:
        unit, hw, part = m.group(1), m.group(2), m.group(3)
        return f'u{unit}pdf/hw{hw}{PART.get(part, "")}.pdf'
    m = re.search(r'Unit (\d+) Test', t, re.I)
    if m:
        return f'u{m.group(1)}pdf/test.pdf'
    m = re.search(r'Final test(?:\s*\((\d)\))?', t, re.I)
    if m:
        return f'finalpdf/final_{PART.get(m.group(1), "a")}.pdf'
    return None


if __name__ == '__main__':
    res = results_dir(sys.argv)
    done = []
    for f in sorted(glob.glob(f'{res}/mcp-Google_Drive-download_file_content-*.txt')):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        if d.get('mimeType') != 'application/pdf':
            continue
        dst = target(d.get('title', ''))
        if not dst:
            print('  ?? не понял название:', d.get('title')); continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        raw = base64.b64decode(d['content'])
        if os.path.exists(dst) and os.path.getsize(dst) == len(raw):
            continue
        open(dst, 'wb').write(raw)
        done.append((dst, len(raw)))
    for dst, n in done:
        print(f'  {dst:20} {n // 1024} КБ')
    print(f'разложено: {len(done)} (из {res})')
