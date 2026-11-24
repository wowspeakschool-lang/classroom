# -*- coding: utf-8 -*-
"""Таблички с правилами для GG3, юнит 1. Сначала показываем Анне, потом заливаем."""
import json, pathlib

def card(colour, head, body):
    return ('<div style="max-width:680px;border:1px solid #E6E0D8;border-radius:14px;'
            'overflow:hidden;font-size:15px;line-height:1.35">'
            f'<div style="background:{colour};color:#fff;padding:7px 12px;font-weight:700">{head}</div>'
            f'<div style="padding:10px 12px;background:#fff">{body}</div></div>')

TD  = 'padding:4px 8px;border-bottom:1px solid #F0ECE6;vertical-align:top'
RU  = TD + ';color:#6B7280'
TH  = 'text-align:left;padding:4px 8px;'

def rows(pairs, accent):
    out = []
    for en, ru in pairs:
        out.append(f'<tr><td style="{TD}"><b style="color:{accent}">{en}</b></td>'
                   f'<td style="{RU}">{ru}</td></tr>')
    return '<table style="width:100%;border-collapse:collapse">' + ''.join(out) + '</table>'

def warn(colour, bg, text):
    return (f'<p style="margin:10px 0 0;padding:8px 10px;background:{bg};'
            f'border-left:4px solid {colour};border-radius:8px">{text}</p>')

CARDS = {}

# ── ДЗ 2 · Present Continuous ────────────────────────────────────────────
body = (
 '<p style="margin:0 0 8px">Present Continuous — действие идёт <b>прямо сейчас</b>, '
 'в момент разговора. Строится так: <b>am / is / are</b> + глагол + <b>-ing</b>.</p>'
 '<table style="width:100%;border-collapse:collapse;background:#F2F7FC">'
 f'<tr><th style="{TH}color:#1F4E7A">Кто</th><th style="{TH}color:#1F4E7A">Форма</th>'
 f'<th style="{TH}color:#1F4E7A">Пример</th></tr>'
 f'<tr><td style="{TD}">I</td><td style="{TD}"><b>am</b></td>'
 f'<td style="{TD}"><b>I’m cooking.</b> <span style="color:#6B7280">Я готовлю.</span></td></tr>'
 f'<tr><td style="{TD}">He / She / It</td><td style="{TD}"><b>is</b></td>'
 f'<td style="{TD}"><b>She’s tidying.</b> <span style="color:#6B7280">Она убирается.</span></td></tr>'
 f'<tr><td style="{TD}">You / We / They</td><td style="{TD}"><b>are</b></td>'
 f'<td style="{TD}"><b>They’re helping.</b> <span style="color:#6B7280">Они помогают.</span></td></tr>'
 '</table>'
 '<p style="margin:10px 0 4px"><b>Отрицание и вопрос</b></p>'
 + rows([('He <u>isn’t</u> cooking.', 'Он не готовит.'),
         ('<u>Are</u> you cooking? — Yes, I am. / No, I’m not.',
          'Ты готовишь? — Да. / Нет.')], '#2F6FB8') +
 '<p style="margin:10px 0 0;color:#6B7280">Подсказки в предложении: <b>now, right now, '
 'at the moment, today</b>.</p>'
 + warn('#D94A77', '#FDF0F4',
   '⚠️ Глаголы <b>like, love, hate, want, need, know, understand, see, hear</b> '
   'в Present Continuous не ставят — это не действия, а состояния.<br>'
   '<b>I am needing help</b> ✗ → <b>I need help</b> ✓ &nbsp;·&nbsp; '
   '<b>Are you liking films?</b> ✗ → <b>Do you like films?</b> ✓')
)
CARDS['hw2'] = card('#2F6FB8', 'Unit 1 · Present Continuous — что происходит сейчас', body)

# ── ДЗ 3 · Present Simple vs Present Continuous ──────────────────────────
body = (
 '<p style="margin:0 0 8px">Два времени про настоящее. Разница — <b>когда</b> происходит действие.</p>'
 '<table style="width:100%;border-collapse:collapse;background:#F1FAF5">'
 f'<tr><th style="{TH}color:#1B6B49">Present Simple — обычно</th>'
 f'<th style="{TH}color:#1B6B49">Present Continuous — сейчас</th></tr>'
 f'<tr><td style="{TD}"><b>He works in his lab every day.</b><br>'
 '<span style="color:#6B7280">Он работает в лаборатории каждый день.</span></td>'
 f'<td style="{TD}"><b>Today he is working outside.</b><br>'
 '<span style="color:#6B7280">Сегодня он работает на улице.</span></td></tr>'
 f'<tr><td style="{TD}">глагол в начальной форме,<br>у <b>he / she / it</b> добавляем '
 '<b>-s</b>: <b>works, goes</b></td>'
 f'<td style="{TD}"><b>am / is / are</b> + глагол + <b>-ing</b>:<br><b>is working</b></td></tr>'
 f'<tr><td style="{TD}">always, usually, often, sometimes, never,<br>'
 'every week, on Mondays, at the weekend</td>'
 f'<td style="{TD}">now, right now, at the moment, today</td></tr>'
 '</table>'
 + warn('#2E9E6B', '#F1FAF5',
   '✅ Слово-подсказка решает всё: <b>He never skateboards.</b> (никогда — обычно) '
   '· <b>Right now they are skateboarding!</b> (прямо сейчас)')
)
CARDS['hw3'] = card('#2E9E6B', 'Unit 1 · Present Simple и Present Continuous', body)

# ── ДЗ 4 · Просьба и предложение помощи ──────────────────────────────────
body = (
 '<p style="margin:0 0 8px">Фразы урока. Послушай запись и повтори вслух.</p>'
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;'
 'font-weight:700;margin:0 0 6px">🙋 Просим о помощи</div>'
 + rows([('Can you help me <i>with the sofa</i>, please?',
          'Помоги мне с диваном, пожалуйста.'),
         ('Can you move <i>the coffee table</i>, please?',
          'Подвинь журнальный столик, пожалуйста.')], '#B4530F') +
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;'
 'font-weight:700;margin:12px 0 6px">🗣️ Отвечаем на просьбу</div>'
 + rows([('No problem. / Yes, of course.', 'Без проблем. / Да, конечно.'),
         ('I’m sorry, I can’t. I’m busy right now.',
          'Извини, не могу. Я сейчас занят.')], '#B4530F') +
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;'
 'font-weight:700;margin:12px 0 6px">🤝 Предлагаем помощь</div>'
 + rows([('Can I help you <i>with the lamp</i>?', 'Помочь тебе с лампой?'),
         ('Do you need any help <i>with the lamp</i>?', 'Тебе нужна помощь с лампой?')], '#B4530F') +
 '<div style="background:#E8732A;color:#fff;padding:5px 10px;border-radius:8px;'
 'font-weight:700;margin:12px 0 6px">🗣️ Отвечаем на предложение</div>'
 + rows([('Yes, please.', 'Да, пожалуйста.'),
         ('No, that’s fine, thank you.', 'Нет, всё в порядке, спасибо.')], '#B4530F') +
 '<p style="margin:10px 0 0;color:#6B7280">Курсивом — то, что меняется: '
 'вместо <i>the sofa</i> подставь любой предмет.</p>'
)
CARDS['hw4'] = card('#E8732A', 'Unit 1 · Как попросить о помощи и предложить свою', body)

out = pathlib.Path('builds/gg3/tablichki')
(out / 'tablichki.json').write_text(json.dumps(CARDS, ensure_ascii=False, indent=1), encoding='utf-8')

PREV = ('<!doctype html><meta charset="utf-8"><title>Таблички GG3 юнит 1</title>'
        '<body style="font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;'
        'background:#FAF8F5;padding:24px;max-width:760px;margin:0 auto">'
        '<h1 style="font-size:20px">Таблички с правилами — Go Getter 3, юнит 1</h1>'
        '<p style="color:#6B7280;font-size:14px">Как это увидит ученик. '
        'Согласуем — тогда ставлю в уроки.</p>')
podpis = {'hw2': 'ДЗ 2 — новый блок 2 (после приветствия)',
          'hw3': 'ДЗ 3 — новый блок 2 (после приветствия)',
          'hw4': 'ДЗ 4 — заменяет нынешний блок 2 (сейчас там те же фразы без перевода и без оформления)'}
for k in ('hw2', 'hw3', 'hw4'):
    PREV += (f'<h2 style="font-size:15px;color:#B4530F;margin:26px 0 8px">{podpis[k]}</h2>'
             + CARDS[k])
PREV += '</body>'
(out / 'preview.html').write_text(PREV, encoding='utf-8')
print('ok', sum(len(v) for v in CARDS.values()))
