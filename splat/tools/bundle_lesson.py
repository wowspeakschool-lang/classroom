"""Автономная копия урока одним файлом: картинки и звук вшиты внутрь (data:).

python3 splat/tools/bundle_lesson.py <куда.html>
Такой файл можно переслать и открыть двойным щелчком — без сайта и без папок рядом.
"""
import base64, json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


def data(path, mime):
    return f'data:{mime};base64,' + base64.b64encode(open(path, 'rb').read()).decode()


def main(out):
    s = open(os.path.join(ROOT, 'lesson.html'), encoding='utf-8').read()
    media = os.path.join(ROOT, 'media', 'lesson')
    used = set(re.findall(r"'([a-z_0-9]+)'", s))
    img = {f[:-5]: data(os.path.join(media, f), 'image/webp') for f in sorted(os.listdir(media))
           if f.endswith('.webp') and f[:-5] in used | {'home_hero'} and f != 'home_hero.webp'}
    aud = {w: data(os.path.join(ROOT, 'audio', w + '.mp3'), 'audio/mpeg') for w in ['tooth', 'toothbrush', 'toothpaste', 'cup']}
    s = re.sub(r'/\*IMG\*/null/\*IMG_END\*/', lambda _: json.dumps(img), s)
    s = re.sub(r'/\*AUD\*/null/\*AUD_END\*/', lambda _: json.dumps(aud), s)
    open(out, 'w', encoding='utf-8').write(s)
    print(len(img), 'картинок,', len(aud), 'звуков,', round(os.path.getsize(out) / 1e6, 1), 'МБ')


if __name__ == '__main__':
    main(sys.argv[1])
