"""Общие помощники тестов Go Getter 3 (модули tools/gg3_u1.py … gg3_final.py).

Блоки тестов GG3 устроены одинаково: «Соедини фразу с картинкой» (match),
«Посмотри на картинку и впиши букву» (exact_input), «Выбери правильный
вариант» (quiz), «Составь предложение» (order), две записи голоса.
"""
import random

from gg2_build import img, todo

COURSE = "gg3"


def unit(n, title):
    return {"unit": f"u{n}", "unit_title": title, "unit_sort": n}


def gimg(u, name):
    return img(u, name, COURSE)


def match_block(u, pairs, title="Соедини фразу с картинкой"):
    """pairs: [(имя картинки, фраза)]."""
    return ("match", {"title": title, "pairs": [
        {"left_image": gimg(u, name), "right": text, "right_audio_tts": text.replace("’", "'")}
        for name, text in pairs]})


def mask(phrase):
    """Скрыть гласные, кроме первой буквы каждого слова: load the dishwasher → l__d the d_shw_sh_r."""
    out = []
    for word in phrase.split(" "):
        chars = [c if (i == 0 or c.lower() not in "aeiou") else "_" for i, c in enumerate(word)]
        out.append("".join(chars))
    return " ".join(out)


def accept(phrase):
    forms = [phrase, phrase[0].upper() + phrase[1:]]
    out = []
    for f in forms:
        for v in (f, f.replace("’", "'"), f.replace("'", "’")):
            if v not in out:
                out.append(v)
    return out


def letters_block(u, items, title="Посмотри на картинку и впиши пропущенные буквы"):
    """items: [(имя картинки, фраза)] — ребёнок пишет фразу целиком.

    Какие буквы были пропущены в выгрузке, не видно — скрываем гласные."""
    block = ("exact_input", {"title": title, "items": [
        {"image": gimg(u, name), "prompt": f"{n}. Напиши фразу целиком: {mask(text)}", "accept": accept(text)}
        for n, (name, text) in enumerate(items, start=1)]})
    return todo(block, ("check", "СОСТАВ МОЙ: какие буквы пропущены в выгрузке, не видно — "
                                 "скрыты гласные (кроме первой буквы слова), ребёнок пишет фразу целиком"))


def scramble(phrase, seed):
    """Перемешать буквы в каждом слове (seed — чтобы сборка была повторяемой)."""
    rnd = random.Random(seed)
    words = []
    for w in phrase.split(" "):
        letters = list(w)
        if len(set(letters)) > 1:
            for _ in range(50):
                rnd.shuffle(letters)
                if "".join(letters) != w:
                    break
        words.append("".join(letters))
    return " ".join(words)


def q(text, options, correct):
    """Вопрос квиза: options — список строк, correct — индекс верного."""
    assert 0 <= correct < len(options)
    return {"q": text, "type": "single", "options": [{"text": o} for o in options], "correct": [correct]}


def quiz_block(questions, title="Прочитай предложение и выбери пропущенное слово"):
    return ("quiz", {"title": title, "questions": questions})


def order_block(*parts):
    sentence = " ".join(parts)
    return ("order", {"words": list(parts), "sentence": sentence, "audio_tts": sentence.replace("’", "'")})


def speaking(title, intro, questions=None, image=None, ordered=True):
    html = f"<p>{intro}</p>"
    if questions:
        tag = "ol" if ordered else "ul"
        html += f"<{tag}>" + "".join(f"<li>{x}</li>" for x in questions) + f"</{tag}>"
    html += "<p>Нажми на микрофон и запиши ответ.</p>"
    payload = {"title": title, "needs_review": True, "html": html}
    if image:
        payload["image"] = image
    return ("speaking", payload)
