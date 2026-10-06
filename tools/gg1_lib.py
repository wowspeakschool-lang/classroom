#!/usr/bin/env python3
"""Общие помощники уроков Go Getter 1: пути к картинкам, типовые блоки.

Уроки лежат по юнитам в tools/gg1_u0.py … gg1_u8.py, gg1_final.py, каждый
модуль отдаёт словарь LESSONS. Собирает и проверяет их tools/gg1_build.py.
"""
import argparse, json, os, random, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = "@@MEDIA@@"
MEDIA_URL = "https://classroom.wowteach.ru/media/"
COURSE = "Go Getter 1"
# Курса в базе ещё нет. Место в списке курсов — 4 (договорились с чатом GG2/GG3:
# Wow Dragon сдвинуты на 7–8, GG2 — 5, GG3 — 6). Заводится один раз перед
# первой заливкой, без сдвигов:
#   insert into classroom_courses (slug, title, sort_order, is_published)
#   values ('gg1', 'Go Getter 1', 4, false);



def img(unit, name):
    return f"{MEDIA}gg1/{unit}/{name}.webp"


def colour(name):
    """Кляксы цветов рисует tools/gg1_colours.py — svg, а не генератор."""
    return f"{MEDIA}gg1/u0/colour_{name}.svg"


def shared(name):
    return f"{MEDIA}shared/{name}.webp"


def pic(src, alt="", height=None):
    style = f"height:{height}px" if height else "max-width:100%"
    return f'<p><img src="{src}" alt="{alt}" style="{style}"></p>'


# Все словари, по которым строятся вопросы «как по-английски», — сюда же
# смотрит проверка: correct должен указывать на английскую пару русского слова.
VOCAB = []


def vocab(rows):
    VOCAB.extend(rows)
    return rows


def quiz_ru_to_en(words, per_question=4, title=None):
    """Вопросы «как по-английски».

    Отвлекающие берём по кругу от самого слова, а не первые из списка: иначе
    во всех вопросах стоят одни и те же три варианта, и правильный вычисляется
    исключением, не читая вопроса.

    Варианты перемешиваются, но не случайно, а от самого слова: сборка
    повторяется байт в байт. По алфавиту ставить нельзя — у соседних по кругу
    отвлекающих верный ответ тогда почти всегда первый, и ребёнок отвечает по
    позиции (так вышло в первой сборке Unit 0, поймано до заливки).
    """
    qs = []
    n = len(words)
    for i, (en, ru, _) in enumerate(words):
        wrong = [words[(i + k) % n][0] for k in range(1, per_question)]
        options = sorted([en] + wrong, key=str.lower)
        random.Random(en).shuffle(options)
        qs.append({
            "q": f"Как по-английски «{ru}»?",
            "type": "single",
            "options": [{"text": o} for o in options],
            "correct": [options.index(en)],
        })
    out = {"questions": qs}
    if title:
        out = {"title": title, **out}
    return out


def choose(title, items):
    """«Выбери правильный вариант» отдельного типа у нас нет — quiz по вопросу
    на пропуск. items: (предложение с ___, [варианты], верный)."""
    return ("quiz", {"title": title, "questions": [
        {"q": q, "type": "single", "options": [{"text": o} for o in opts],
         "correct": [opts.index(ok)]}
        for q, opts, ok in items]})


def order(sentence, words=None, title=None, image=None):
    words = words or sentence.split(" ")
    out = {"words": words, "sentence": sentence, "audio_tts": sentence}
    if title:
        out = {"title": title, **out}
    if image:
        out["image"] = image
    return ("order", out)


def hello(html, picture="hello_wave"):
    return ("text", {"html": pic(shared(picture), height=200) + html})


def bye(html="<h3>Поздравляю! Ты завершил домашнее задание, ты замечательный ученик! 🎉</h3>"
             "<p>Увидимся на занятии!</p>", picture="well_done_trophy"):
    return ("text", {"html": pic(shared(picture), height=180) + html})


def mcq(title, items):
    """Тест «выбери вариант». items: (вопрос, [варианты], верный[, картинка]).

    В выгрузке верный вариант всегда стоит первым — перемешиваем, но не
    случайно, а от текста вопроса: сборка повторяется байт в байт.

    Позицию верного ответа не отдаём случаю: на шести вопросах случай
    поставил его первым пять раз. Неверные перемешиваются, а верный идёт
    по кругу — от вопроса к вопросу на следующее место.
    """
    qs = []
    shift = len(title or "")
    for i, it in enumerate(items):
        q, opts, ok = it[:3]
        wrong = [o for o in opts if o != ok]
        random.Random(q + "|" + ok).shuffle(wrong)
        opts = wrong[:]
        opts.insert((i + shift) % len(opts + [ok]), ok)
        one = {"q": q, "type": "single", "options": [{"text": o} for o in opts],
               "correct": [opts.index(ok)]}
        if len(it) > 3 and it[3]:
            one["image"] = it[3]
        qs.append(one)
    out = {"questions": qs}
    if title:
        out = {"title": title, **out}
    return ("quiz", out)


def true_false(title, items):
    """«Верно / неверно» с картинкой. У блока truefalse картинки нет, поэтому
    это quiz с двумя вариантами в постоянном порядке.
    items: (утверждение, верно ли[, картинка])."""
    qs = []
    for it in items:
        st, ok = it[:2]
        one = {"q": st, "type": "single",
               "options": [{"text": "Верно"}, {"text": "Неверно"}],
               "correct": [0 if ok else 1]}
        if len(it) > 2 and it[2]:
            one["image"] = it[2]
        qs.append(one)
    return ("quiz", {"title": title, "questions": qs})


def anagram(word):
    """Буквы слова вперемешку, от самого слова; совпасть со словом не может."""
    letters = list(word)
    rnd = random.Random(word)
    while True:
        rnd.shuffle(letters)
        if "".join(letters) != word:
            return " ".join(l.upper() for l in letters)


def gapped(word):
    """«m _ t _ e r»: видна каждая вторая буква и последняя."""
    return " ".join(c if i % 2 == 0 or i == len(word) - 1 else "_"
                    for i, c in enumerate(word))


def listening(title, picture=None):
    """Аудио из выгрузки не приходит никогда. Блок с пустым audio ставим, чтобы
    методист вставила файл и номера блоков не сдвинулись; у quiz и truefalse
    своего поля audio в редакторе нет, поэтому аудио — в текстовом блоке перед ними."""
    html = f"<p><b>{title}</b></p>"
    if picture:
        html += pic(picture)
    return ("text", {"audio": "", "html": html})

