"""Вставляет план урока из docs/plan_uroka.md в lesson.html (между /*PLAN_START*/ и /*PLAN_END*/).

python3 splat/tools/build_lesson.py
Запускать после каждой правки плана — урок показывает учителю ровно то, что в файле плана.
"""
import html, json, os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


def md(s):
    s = html.escape(s.strip(), quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)
    return s


def main():
    rows, sec = [], ''
    for line in open(os.path.join(ROOT, 'docs', 'plan_uroka.md'), encoding='utf-8'):
        if line.startswith('## '):
            sec = line[3:].strip()
        m = re.match(r'^\|\s*(\d+)\s*\|(.*)\|\s*$', line)
        if m:
            cols = [c for c in m.group(2).split('|')]
            todo, say, ans = (cols + ['', '', ''])[:3]
            rows.append({'n': int(m.group(1)), 'sec': md(sec), 'todo': md(todo), 'say': md(say), 'ans': md(ans)})
    p = os.path.join(ROOT, 'lesson.html')
    s = open(p, encoding='utf-8').read()
    s = re.sub(r'/\*PLAN_START\*/.*?/\*PLAN_END\*/',
               lambda _: '/*PLAN_START*/' + json.dumps(rows, ensure_ascii=False) + '/*PLAN_END*/', s, flags=re.S)
    open(p, 'w', encoding='utf-8').write(s)
    print('слайдов в плане:', len(rows))


if __name__ == '__main__':
    main()
