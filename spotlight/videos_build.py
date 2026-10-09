# -*- coding: utf-8 -*-
"""Собирает data/videos.json и data/planned.json (отметки «есть» / «будет» для плана уроков).

Источники: data/video_subtopics.json (видео 10+ → подтемы), data/remap_7-9_and_october.json
(видео 7-9 и октябрьские вебинары → подтемы), EXCLUDE — решения методиста.

    python3 spotlight/videos_build.py && python3 spotlight/matrix.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import D
from matrix import load_units, group

# видео, которые методист решила не засчитывать ни за одну подтему
EXCLUDE = {
    'Get be used to + Global issues': 'не подходит к теме: в материалах только used to, be/get used to нет — не засчитываем',
}


def main():
    units = load_units()
    valid = {g: {n for n, u in units.items() if any(group(x) == g for x in u['cells'])} for g in ('7–9', '10+')}
    videos, planned = {}, {}

    def add(d, s, g, txt):
        cur = d.setdefault(s, {}).get(g, '')
        if txt not in cur.split('\n'):
            d[s][g] = (cur + '\n' if cur else '') + txt

    for v in json.load(open(os.path.join(D, 'data', 'video_subtopics.json'))):
        if v['group'] != '10+' or v['video'] in EXCLUDE:
            continue
        for s in v['subtopics']:
            if s in valid['10+']:
                add(videos, s, '10+', v['video'] + (' (по названию)' if v['confidence'] == 'по названию' else ''))
    for v in json.load(open(os.path.join(D, 'data', 'remap_7-9_and_october.json'))):
        if v['name'] in EXCLUDE:
            continue
        g = '7–9' if v['group'] == '7-9' else '10+'
        for s in v['subtopics']:
            if v['kind'] == 'video':
                add(videos, s, g, v['name'])
            else:
                d = v['kind'].split()[1]
                add(planned, s, g, f"вебинар {d[8:10]}.{d[5:7]}: {v['name']}")
    json.dump(videos, open(os.path.join(D, 'data', 'videos.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(planned, open(os.path.join(D, 'data', 'planned.json'), 'w'), ensure_ascii=False, indent=1)

    # опись: исключённое видео отвязываем от папки, оно уходит в «Видео без папки» с причиной
    p = os.path.join(D, 'data', 'video_map.json')
    m = json.load(open(p))
    for v in m:
        if v['video'] in EXCLUDE:
            v['folder'] = ''
            v['note'] = EXCLUDE[v['video']]
    json.dump(m, open(p, 'w'), ensure_ascii=False, indent=1)
    print('subtopics with video:', len(videos), 'planned:', len(planned))


if __name__ == '__main__':
    main()
