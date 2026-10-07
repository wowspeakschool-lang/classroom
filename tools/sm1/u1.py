"""Super Minds 1 · Unit 1 · My school — тест юнита.

Домашки Unit 1 уже в базе (на base64, не трогаем), здесь только тест.
Выгрузка ShkolaApp «Super Minds 1 Unit 1 Test», разбор —
docs/SM1_разбор_u5_t1_t2.md. Картинки школьных вещей для «Соедини слова с
картинками» в выгрузке отсутствуют — лист ЛТ1.1 (school_*). Остальные
картинки вырезаны из PDF (t_*).
"""
from sm1_build import *

U = "u1"
UNIT = "Unit 1 · My school"


def c(name):
    return img(U, name)


def single(q, options, correct, image=None):
    d = {"q": q, "type": "single", "options": [{"text": o} for o in options], "correct": [correct]}
    if image:
        d["image"] = image
    return d


def order(sentence, words, image):
    return ("order", {"title": "Расставь слова в правильном порядке", "words": words,
                      "sentence": sentence, "audio_tts": sentence, "image": image})


LESSONS = {
    "u1_test": {
        "unit": U, "unit_title": UNIT, "unit_sort": 1,
        "lesson_title": "Unit 1 Test", "lesson_sort": 7, "kind": "test",
        # 8 блоков выгрузки → 14. Аудио к «Тесту» (3) и к «Диаграмме» (4)
        # вынесены отдельными блоками 3 и 5. «Выбери правильный вариант» —
        # один quiz, по вопросу на пропуск (8). «Составь предложение» из пяти
        # предложений — пять order (9–13).
        "blocks": [
            # 1 — «Открытый вопрос»
            ("task", {
                "title": "🎒 Смотри и пиши!",
                "image": c("t_school_things"),
                "html": "<p>1️⃣ Внимательно посмотри на картинку 👀 — какие школьные предметы "
                        "ты видишь?</p>"
                        "<p>2️⃣ В поле под картинкой впиши их названия на английском ✏️</p>"
                        "<p>Молодец! 👏</p>",
                "needs_review": True,
            }),

            # 2 — «Запись голоса»
            ("speaking", {
                "title": "Прочитай предложения вслух 🎤",
                "image": c("t_reading_kids"),
                "html": "<p>Внимательно прочитай предложения глазками 👀</p>"
                        "<p>Нажми на микрофон 🎤 и проговори их вслух. У тебя получится! 🌟</p>"
                        "<ol>"
                        "<li>I spin a top. The top stops.</li>"
                        "<li>Ken, the pet, is in the cup.</li>"
                        "<li>Ron is a red rat. It can jump.</li>"
                        "<li>Fip and Fop can hop and jog.</li>"
                        "<li>Will can sell the bell.</li>"
                        "<li>Next to the box is a taxi.</li>"
                        "<li>I yell “Yes!”. Mum yells “Yes!”</li>"
                        "</ol>",
                "needs_review": True,
            }),

            # 3 — аудио к блоку 4
            ("video", {"title": "Внимательно послушай аудио 🎧", "url": "", "provider": "file"}),

            # 4
            ("quiz", {"questions": [{
                "q": "Выбери предметы, которые ты услышишь.",
                "type": "multiple",
                "image": c("t_listen_boy"),
                "options": [{"text": t} for t in [
                    "book", "notebook", "pen", "pencil", "pencil case",
                    "rubber", "ruler", "bag", "desk", "paper"]],
                "correct": [1, 3, 4, 5, 7],
            }]}),

            # 5 — аудио к «Диаграмме»
            ("video", {"title": "Послушай аудио и узнай, какой номер принадлежит какой картинке 🎧",
                       "url": "", "provider": "file"}),

            # 6 — «Диаграмма»: метки 1–5 стояли в углах картинок, ставим по центрам
            ("hotspot", {
                "title": "Соедини картинки с правильным номером",
                "mode": "label",
                "image": c("t_classroom_scenes"),
                "points": [
                    {"x": 66.5, "y": 73, "text": "1"},
                    {"x": 17.0, "y": 24, "text": "2"},
                    {"x": 83.0, "y": 24, "text": "3"},
                    {"x": 50.0, "y": 24, "text": "4"},
                    {"x": 33.5, "y": 73, "text": "5"},
                ]}),

            # 7
            ("match", {
                "title": "Соедини слова с картинками",
                "pairs": [{"left_image": c(f), "right": en, "right_audio_tts": en} for en, f in [
                    ("book", "school_book"),
                    ("pen", "school_pen"),
                    ("rubber", "school_rubber"),
                    ("pencil", "school_pencil"),
                    ("bag", "school_bag"),
                    ("ruler", "school_ruler"),
                ]]}),

            # 8 — «Выбери правильный вариант»: пять диалогов, вопрос на пропуск
            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                single("A: What ___ this?<br>B: It is a pencil case.",
                       ["it", "is", "are"], 1, c("t_pencil_case")),
                single("A: What is this?<br>B: It ___ a pencil case.",
                       ["is", "are", "it"], 0),
                single("A: ___ a desk?<br>B: Yes, it is.",
                       ["Is", "Is it", "Are it"], 1, c("t_desk_chair")),
                single("A: Is it a desk?<br>B: Yes, ___.",
                       ["it isn’t", "it are", "it is"], 2),
                single("A: Open your notebook, ___.<br>B: OK.",
                       ["please", "thank you", "welcome"], 0, c("t_notebook")),
                single("A: ___ your book, please.<br>B: Sure.",
                       ["Sit at", "Open", "Write"], 1, c("t_book")),
                single("A: Open your book, ___.<br>B: Sure.",
                       ["thank you", "welcome", "please"], 2),
                single("A: ___ a pencil case?<br>B: No, it isn’t. It’s a rubber.",
                       ["Is it", "Is", "Are it"], 0, c("t_rubber")),
                single("A: Is it a pencil case?<br>B: No, ___. It’s a rubber.",
                       ["it is", "it isn’t", "it are"], 1),
            ]}),

            # 9–13 — «Составь предложение»
            order("It is a yellow desk.", ["It", "is", "a", "yellow", "desk."], c("t_yellow_desk")),
            order("Pass me a pencil, please.", ["Pass", "me", "a", "pencil,", "please."], c("t_pencil")),
            order("Open your pencil case, please.",
                  ["Open", "your", "pencil", "case,", "please."], c("t_pencil_case_open")),
            order("Sit at your desk, please.", ["Sit", "at", "your", "desk,", "please."],
                  c("t_wooden_desk")),
            order("It is a blue notebook.", ["It", "is", "a", "blue", "notebook."], c("t_blue_notebook")),

            # 14 — SPEAKING TASK
            ("speaking", {
                "title": "SPEAKING TASK 🎤",
                "image": c("t_classroom"),
                "html": "<p>Посмотри на картинку и ответь на вопросы:</p>"
                        "<p>What can you see?<br>Do you see a book?<br>"
                        "What colour is the book?<br>How many rubbers do you see?</p>"
                        "<p><i>For example:<br>It’s a blue desk.<br>It’s a red book.</i></p>"
                        "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>",
                "needs_review": True,
            }),
        ],
    },
}
