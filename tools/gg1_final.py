#!/usr/bin/env python3
"""Go Getter 1 · Final Test — итоговый тест курса (разбор: docs/GG1_разбор/final.md).

Формат Cambridge YLE Starters: Listening (три части) и Reading & Writing
(yes/no по картинке, yes/no по сцене, слово из букв). В выгрузке почти нет
картинок (распечатка сделана до их загрузки) и нет ни одного аудио, поэтому:

* сцена гостиной для «диаграммы» — наша, без людей (final_living_room);
  места точек и предметы — СОСТАВ МОЙ, текст для записи аудио — в заметках;
* Listening Part 3: варианты-картинки пропали — варианты текстом
  (СОСТАВ МОЙ), номер верного сохранён как в выгрузке;
* картинки к yes/no — лист ЛФ.2 и готовые картинки юнитов 0, 7;
* сцена Reading Part 2 — final_family_room (рисованная семья, лист ЛФ.3),
  утверждения как в выгрузке;
* картинки к спеллингу — из юнитов 2, 3, 7, 8.
"""
from gg1_lib import *  # noqa: F401,F403

U = "final"
UF = {"unit": U, "unit_title": "Final Test", "unit_sort": 9}


def u(name):
    return img(U, name)


def red(title):
    return f'<h2 style="color:#d32f2f">{title}</h2>'


def fixed_quiz(title, items, image=None):
    """Варианты в том порядке, как в выгрузке: верный стоит на своём месте
    (там он не первый). items: (вопрос, [варианты], номер верного с 1)."""
    qs = []
    for q, opts, n in items:
        one = {"q": q, "type": "single", "options": [{"text": o} for o in opts],
               "correct": [n - 1]}
        if image:
            one["image"] = image
        qs.append(one)
    return ("quiz", {"title": title, "questions": qs})


def yes_no(title, items):
    """yes / no по картинке: варианты YES и NO в постоянном порядке, как в
    выгрузке. items: (утверждение, верно ли, картинка)."""
    return ("quiz", {"title": title, "questions": [
        {"q": st, "type": "single", "options": [{"text": "YES"}, {"text": "NO"}],
         "correct": [0 if ok else 1], "image": pic_}
        for st, ok, pic_ in items]})


def spell(word, picture):
    """Слово из букв. Склейка order — через пробел, поэтому sentence — буквы
    через пробел; озвучивается само слово."""
    letters = list(word)
    return ("order", {"title": "Посмотри на картинку и собери слово из букв",
                      "words": letters, "sentence": " ".join(letters),
                      "audio_tts": word, "image": picture})


LESSONS = {
    "final_test": {
        **UF,
        "lesson_title": "Final Test",
        "lesson_sort": 0,
        "kind": "test",
        "blocks": [
            ("text", {"html": pic(shared("hello_headphones"), height=200)
                      + "<h2>Final Test</h2><p>Это итоговый тест по всему курсу. "
                        "Не торопись и внимательно слушай аудио!</p>"
                      + red("LISTENING")}),

            # Listening Part 1 — аудио в выгрузке пустое
            listening("LISTENING Part 1. Послушай аудио и выполни задание ниже."),

            # «Диаграмма»: в выгрузке рисованная гостиная с человеком (xref 220),
            # из шести вариантов уцелел один — радио на полку шкафа. Сцена наша,
            # без людей; места ②–⑥ и предметы — СОСТАВ МОЙ, текст для аудио в заметках.
            ("hotspot", {
                "title": "Послушай аудио выше и расставь предметы по местам",
                "mode": "label",
                "image": u("final_living_room"),
                "points": [
                    {"x": 36.0, "y": 31.0, "text": "radio"},
                    {"x": 66.0, "y": 78.0, "text": "ball"},
                    {"x": 30.0, "y": 86.0, "text": "kite"},
                    {"x": 60.0, "y": 42.0, "text": "clock"},
                    {"x": 61.0, "y": 68.0, "text": "robot"},
                    {"x": 27.0, "y": 60.0, "text": "bag"},
                ],
                "extras": [],
            }),

            # Listening Part 2 — аудио пустое, ответы из выгрузки
            listening("LISTENING Part 2. Послушай и выбери верный ответ. "
                      "Пример: What is the girl's name? — Lucy. How old is she? — 7."),
            mcq("Послушай и выбери верный ответ", [
                ("What is Lucy's friend's name?", ["Alex", "Bob", "Mark"], "Alex"),
                ("Which class are the two children in at school?", ["8", "6", "7"], "8"),
                ("How many dogs are there at Lucy's house?", ["3", "2", "4"], "3"),
                ("What's the name of Lucy's favourite dog?", ["Socks", "Sock", "Sockes"], "Socks"),
                ("How many fish has Lucy's friend got?", ["12", "20", "11"], "12"),
            ]),

            # Listening Part 3 — аудио пустое, варианты-картинки в выгрузке пропали.
            # Варианты текстом — СОСТАВ МОЙ; номер верного как в выгрузке (3,1,2,2,3,1).
            listening("LISTENING Part 3. Послушай аудио и выполни задания ниже."),
            fixed_quiz("Послушай аудио выше и выбери правильный ответ", [
                ("What's Pat doing?", ["reading a book", "playing football", "swimming"], 3),
                ("Which is May?", ["the girl with long hair", "the girl with short hair",
                                   "the girl with glasses"], 1),
                ("Which is Nick's favourite ice-cream?", ["lemon", "chocolate", "strawberry"], 2),
                ("What's Ben doing?", ["riding a bike", "flying a kite", "playing tennis"], 2),
                ("Where's Kim's doll?", ["on the bed", "under the table", "in the box"], 3),
                ("What's Dad doing?", ["cooking", "sleeping", "washing the car"], 1),
            ]),

            ("text", {"html": red("READING AND WRITING")}),

            # картинки в выгрузке потеряны; для NO — другой предмет (СОСТАВ МОЙ).
            # «Her hair is wavy» (про человека) заменено на «It is a dog.» с котом — NO.
            yes_no("Посмотри на картинку и выбери: верно (YES) или неверно (NO)", [
                ("These are grapes.", True, u("final_grapes")),
                ("This is a house.", False, u("final_car")),
                ("It is a clock.", True, img("u0", "obj_clock")),
                ("This is a sock.", False, u("final_boot")),
                ("These are chairs.", True, u("final_chairs")),
                ("It is a television.", False, u("final_radio")),
                ("It is a dog.", False, img("u7", "animal_cat")),
                ("It is a spider.", True, img("u7", "animal_spider")),
            ]),

            # Reading Part 2: сцена в выгрузке потеряна — рисованная семья ЛФ.3
            yes_no("Посмотри на картинку и выбери yes или no. Пример: There are two "
                   "armchairs in the living room — YES. The big window is open — NO.", [
                ("The man has got black hair and glasses.", True, u("final_family_room")),
                ("There is a lamp on the bookcase.", True, u("final_family_room")),
                ("Some of the children are singing.", False, u("final_family_room")),
                ("The woman is holding some drinks.", True, u("final_family_room")),
                ("The cat is sleeping under an armchair.", True, u("final_family_room")),
            ]),

            # спеллинг: картинки в выгрузке потеряны — берём из юнитов
            spell("butterfly", img("u7", "animal_butterfly")),
            spell("jacket", img("u2", "clothes_jacket")),
            spell("kitchen", img("u3", "room_kitchen")),
            spell("whale", img("u7", "animal_whale")),
            spell("hockey", img("u8", "sport_hockey")),

            # прощального блока в выгрузке нет — ТЕКСТ МОЙ, это конец курса
            bye("<h3>Поздравляю! Ты прошёл весь курс Go Getter 1! 🎉</h3>"
                "<p>Ты замечательный ученик. Увидимся на занятии!</p>", "congrats_popper"),
        ],
    },
}
