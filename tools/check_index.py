#!/usr/bin/env python3
"""Проверка index.html перед публикацией (HANDOVER, раздел 9).

1. Синтаксис JS: встроенные <script> вырезаются и прогоняются через node --check.
2. Вызовы из атрибутов: каждое имя функции из onclick/onchange/oninput/…
   (и в разметке, и в шаблонных строках JS) должно быть объявлено в файле.
   Это ловит то, что пропускает шаг 1: однажды при переписывании куска файла
   пропали edTtsOpen/edTtsOpenCb/edTtsRun, синтаксис остался верным,
   а «Озвучить» молча перестала работать.

Запуск: python3 tools/check_index.py [путь к index.html]
Код выхода 0 — всё чисто, 1 — есть ошибки.
"""
import os
import re
import subprocess
import sys
import tempfile

# Имена, которые законно вызываются из атрибутов, но не объявлены в файле
BUILTINS = {
    'if', 'for', 'while', 'switch', 'return', 'function', 'typeof', 'new', 'void',
    'alert', 'confirm', 'prompt', 'setTimeout', 'clearTimeout', 'setInterval',
    'clearInterval', 'parseInt', 'parseFloat', 'Number', 'String', 'Boolean',
    'JSON', 'Math', 'Date', 'Object', 'Array', 'encodeURIComponent',
    'decodeURIComponent', 'open', 'print', 'fetch', 'isNaN', 'requestAnimationFrame',
}


def main(path):
    src = open(path, encoding='utf-8').read()
    errors = []

    # 1. синтаксис
    scripts = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', src, re.S | re.I)
    with tempfile.TemporaryDirectory() as tmp:
        for n, code in enumerate(scripts):
            js = os.path.join(tmp, f'script{n}.js')
            open(js, 'w', encoding='utf-8').write(code)
            r = subprocess.run(['node', '--check', js], capture_output=True, text=True)
            if r.returncode != 0:
                errors.append(f'node --check, <script> №{n + 1}:\n{r.stderr.strip()}')

    # 2. вызовы из атрибутов
    js_all = '\n'.join(scripts)
    declared = set(re.findall(r'\bfunction\s+([A-Za-z_$][\w$]*)\s*\(', js_all))
    declared |= set(re.findall(r'\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=', js_all))
    declared |= set(re.findall(r'^\s*([A-Za-z_$][\w$]*)\s*=\s*(?:async\s+)?(?:function|\()', js_all, re.M))
    declared |= set(re.findall(r'window\.([A-Za-z_$][\w$]*)\s*=', js_all))

    handlers = re.findall(r'\bon[a-z]+\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', src)
    called = {}
    for dq, sq in handlers:
        body = dq or sq
        body = re.sub(r'\$\{[^}]*\}', '0', body)          # подстановки шаблонных строк
        body = re.sub(r'(["\'`]).*?\1', '""', body)        # строковые литералы
        for name in re.findall(r'(?<![\w$.])([A-Za-z_$][\w$]*)\s*\(', body):
            if name not in BUILTINS:
                called.setdefault(name, 0)
                called[name] += 1
    missing = sorted(n for n in called if n not in declared)
    if missing:
        errors.append('Вызываются из атрибутов, но не объявлены: ' + ', '.join(missing))

    if errors:
        print('\n\n'.join(errors))
        return 1
    print(f'index.html в порядке: {len(scripts)} <script>, '
          f'{len(called)} функций из атрибутов, все объявлены.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'index.html'))
