# -*- coding: utf-8 -*-
"""Общие кирпичики для сборки домашек Go Getter 3 по рабочей тетради."""
import json

MEDIA = 'https://classroom.wowteach.ru/media/'
AUDIO = 'https://api.wowteach.ru/storage/v1/object/public/classroom-media/gg3%20wb/'
GOLOS = 'en_GB-alba'

PRIVET = ['hello_teen_wave.webp', 'hello_girl_wave.webp', 'hello_highfive.webp']
POKA = ['bye_star.webp', 'bye_trophy.webp', 'bye_medal.webp', 'bye_thumb.webp',
        'bye_popper.webp', 'bye_certificate.webp']


def tts(t):
    return {'text': t if t[-1:] in '.?!' else t + '.', 'voice': GOLOS}


def privet(n, zagolovok, text):
    k = PRIVET[n % len(PRIVET)]
    return ('text', {'html': f'<p><img src="{MEDIA}shared/gg/{k}" alt="" style="height:200px"></p>'
                             f'<h2>{zagolovok}</h2><p>{text}</p>'})


def poka(n, text):
    k = POKA[n % len(POKA)]
    return ('text', {'html': f'<p><img src="{MEDIA}shared/gg/{k}" alt="" style="height:200px"></p><p>{text}</p>'})


def kartochki(zagolovok, slova):
    return ('flashcards', {'title': zagolovok,
                           'cards': [{'text': w, 'translation': p, 'audio': '', 'audio_tts': tts(w)}
                                     for w, p in slova]})


def kviz(zagolovok, voprosy, material=None):
    """voprosy: [(q, [варианты], индекс верного)]"""
    p = {'title': zagolovok, 'questions': [
        {'q': q, 'type': 'single', 'correct': [k],
         'options': [{'text': o} for o in opts]} for q, opts, k in voprosy]}
    if material:
        p['material'] = material
    return ('quiz', p)


def pary(zagolovok, p, material=None):
    pl = {'title': zagolovok, 'pairs': [{'left': a, 'right': b} for a, b in p]}
    if material:
        pl['material'] = material
    return ('match', pl)


def propuski(zagolovok, text, mode='type', choices=None, material=None):
    p = {'title': zagolovok, 'mode': mode, 'text': text}
    if choices:
        p['choices'] = choices
    if material:
        p['material'] = material
    return ('gaps', p)


def gruppy(zagolovok, g):
    return ('sort', {'title': zagolovok,
                     'groups': [{'name': n, 'items': [{'text': t} for t in it]} for n, it in g]})


def predlozheniya(zagolovok, punkty):
    """punkty: [(подпись, 'целое предложение')] — слова режутся по пробелу."""
    items = []
    for podpis, s in punkty:
        it = {'words': s.split(' '), 'sentence': s}
        if podpis:
            it['prompt'] = podpis
        items.append(it)
    sklejka = [(' '.join(i['words']), i['sentence']) for i in items]
    for a, b in sklejka:
        assert a == b, f'склейка не сходится: {a!r} != {b!r}'
    return ('order', {'title': zagolovok, 'items': items})


def vpisat(zagolovok, punkty):
    """punkty: [(подсказка, [варианты ответа])]"""
    return ('exact_input', {'title': zagolovok,
                            'items': [{'prompt': pr, 'accept': acc} for pr, acc in punkty]})


def govorenie(zagolovok, html, obrazec=None):
    p = {'title': zagolovok, 'needs_review': True, 'html': html}
    if obrazec:
        p['sample'] = ''
        p['sample_tts'] = tts(obrazec)
    return ('speaking', p)


def pismo(zagolovok, html):
    return ('task', {'title': zagolovok, 'needs_review': True, 'html': html})


def tekst(html):
    return ('text', {'html': html})


def sql_uroka(unit_id, nazvanie, sort_order, bloki):
    out = [f"""
do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '{unit_id}' and title = '{nazvanie}';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('{unit_id}', '{nazvanie}', {sort_order}, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = {sort_order}, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;"""]
    for i, (tip, payload) in enumerate(bloki):
        j = json.dumps(payload, ensure_ascii=False)
        assert '$blk$' not in j
        out.append(f"  insert into classroom_blocks (lesson_id, type, payload, sort_order)\n"
                   f"  values (v_lesson, '{tip}', $blk${j}$blk$::jsonb, {i});")
    out.append("end $$;")
    return '\n'.join(out)


def posledovatelnost(zagolovok, stroki, audio=None):
    """Расставь реплики по порядку: stroki — в правильном порядке."""
    p = {'title': zagolovok, 'items': [{'text': s} for s in stroki]}
    if audio:
        p['audio'] = audio
    return ('sequence', p)
