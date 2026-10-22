"""Автономная копия мини-сайта одним файлом: картинки и звук вшиты внутрь (data:).

python3 splat/tools/bundle_site.py <куда.html> [--all]
--all — все льдинки открыты сразу (копия для проверки; у файла нет адреса, куда дописать ?all).
Файл открывается двойным щелчком — без сайта и без папок рядом. Прогресс челленджа
хранится в браузере, поэтому у копии он свой, не общий с сайтом.
"""
import base64, json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


def data(path, mime):
    return f'data:{mime};base64,' + base64.b64encode(open(path, 'rb').read()).decode()


def main(out):
    s = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    used = set(re.findall(r"'([a-z_0-9]+)'", s))
    img = {}
    for sub in ('lesson', 'site'):
        d = os.path.join(ROOT, 'media', sub)
        for f in sorted(os.listdir(d)):
            if f.endswith('.webp') and f[:-5] in used:
                img[f[:-5]] = data(os.path.join(d, f), 'image/webp')
    aud = {w: data(os.path.join(ROOT, 'audio', w + '.mp3'), 'audio/mpeg') for w in ['tooth', 'toothbrush', 'toothpaste', 'cup', 'penguin']}
    s = re.sub(r'/\*IMG\*/null/\*IMG_END\*/', lambda _: json.dumps(img), s)
    s = re.sub(r'/\*AUD\*/null/\*AUD_END\*/', lambda _: json.dumps(aud), s)
    if '--all' in sys.argv:
        s = s.replace('const ALL = /[?&]all\\b/.test(location.search);', 'const ALL = true;')
        assert 'const ALL = true;' in s
    open(out, 'w', encoding='utf-8').write(s)
    print(len(img), 'картинок,', len(aud), 'звуков,', round(os.path.getsize(out) / 1e6, 1), 'МБ')


if __name__ == '__main__':
    main(sys.argv[1])
