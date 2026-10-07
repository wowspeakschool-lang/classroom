"""Super Minds 1 · Unit 2 · My toys — тест юнита.

Домашки Unit 2 уже в базе (на base64, не трогаем), здесь только тест.
Выгрузка ShkolaApp «Super Minds 1 Unit 2 Test», разбор —
docs/SM1_разбор_u5_t1_t2.md. Картинки игрушек для «Соедини слова с
картинками» в выгрузке отсутствуют — лист ЛТ2.1 (toy_*). Остальные картинки
вырезаны из PDF (t_*).
"""
from sm1_build import *

U = "u2"
UNIT = "Unit 2 · My toys"


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
    "u2_test": {
        "unit": U, "unit_title": UNIT, "unit_sort": 2,
        "lesson_title": "Unit 2 Test", "lesson_sort": 7, "kind": "test",
        # 8 блоков выгрузки → 14. «Заполни пропуски» (1) — игра «впиши
        # недостающие буквы»; какие буквы были скрыты, выгрузка не показывает,
        # маска моя. Аудио к «Диаграмме» — отдельный блок 10. Картинка к
        # «Верно / неверно» — отдельным блоком 12: у truefalse поля image
        # в рендере нет.
        "blocks": [
            # 1
            ("exact_input", {"items": [
                {"prompt": f"Впиши слово целиком: {mask} ({ru})", "accept": [en], "audio_tts": en}
                for en, mask, ru in [
                    ("doll", "d _ l l", "кукла"),
                    ("ball", "b _ l l", "мяч"),
                    ("kite", "k _ t e", "воздушный змей"),
                    ("car", "c _ r", "машина"),
                    ("bike", "b i _ e", "велосипед"),
                    ("go-kart", "g o - k _ r t", "картинг"),
                    ("train", "t r _ _ n", "поезд"),
                    ("monster", "m o n s _ e r", "монстр"),
                    ("plane", "p l _ n e", "самолёт"),
                ]]}),

            # 2
            ("match", {
                "title": "Соедини слова с картинками",
                "pairs": [{"left_image": c(f), "right": en, "right_audio_tts": en} for en, f in [
                    ("doll", "toy_doll"),
                    ("kite", "toy_kite"),
                    ("go-kart", "toy_go_kart"),
                    ("monster", "toy_monster"),
                    ("car", "toy_car"),
                    ("train", "toy_train"),
                ]]}),

            # 3
            ("speaking", {
                "title": "Прочитай предложения вслух 🎤",
                "html": "<p>Внимательно прочитай предложения глазками 👀</p>"
                        "<p>Нажми на микрофон 🎤 и проговори их вслух. У тебя получится! 🌟</p>"
                        "<ol>"
                        "<li>I can see a big tree.</li>"
                        "<li>The car is in the yard.</li>"
                        "<li>This is a long string.</li>"
                        "<li>The boat is old.</li>"
                        "<li>The kite flies high in the sky.</li>"
                        "</ol>",
                "needs_review": True,
            }),

            # 4 — «Выбери правильный вариант»: пять диалогов, вопрос на пропуск
            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                single("A: ___ her favourite toy?<br>B: Her favourite toy is a plane.",
                       ["Who’s", "What’s", "Whose"], 1, c("t_plane")),
                single("A: What’s her favourite toy?<br>B: Her ___ toy is a plane.",
                       ["favourite", "the", "a"], 0),
                single("A: How ___ is she?<br>B: She’s seven.",
                       ["young", "happy", "old"], 2, c("t_girl_seven")),
                single("A: How old is she?<br>B: ___ seven.",
                       ["She’re", "She’s", "She"], 1),
                single("A: What’s ___ name?<br>B: My name is Alex.",
                       ["your", "you", "my"], 0, c("t_meeting")),
                single("A: What’s your name?<br>B: ___ name is Alex.",
                       ["You", "Your", "My"], 2),
                single("A: What ___ it?<br>B: It’s an ugly monster.",
                       ["am", "is", "are"], 1, c("t_monster_blue")),
                single("A: What is it?<br>B: It’s ___ ugly monster.",
                       ["a", "an"], 1),
                single("It’s ___ small yellow ball.",
                       ["a", "an"], 0, c("t_yellow_ball")),
            ]}),

            # 5–9 — «Составь предложение»
            order("His favourite number is ten.", ["His", "favourite", "number", "is", "ten."],
                  c("t_number_ten")),
            order("It’s a new beautiful bike.", ["It’s", "a", "new", "beautiful", "bike."], c("t_bike")),
            order("What is her favourite toy?", ["What", "is", "her", "favourite", "toy?"], c("t_toys")),
            order("It’s a short green train.", ["It’s", "a", "short", "green", "train."],
                  c("t_green_train")),
            order("It’s a funny purple monster.", ["It’s", "a", "funny", "purple", "monster."],
                  c("t_purple_monster")),

            # 10 — аудио к «Диаграмме»
            ("video", {"title": "Послушай аудио и выполни задание ниже 🎧", "url": "", "provider": "file"}),

            # 11 — «Диаграмма»: в выгрузке точка k ↔ вариант k, лишних нет
            ("hotspot", {
                "title": "Послушай аудио выше и соедини имя с ребёнком",
                "mode": "label",
                "image": c("t_kids_toys"),
                "points": [
                    {"x": 11.0, "y": 70, "text": "Amy", "audio_tts": "Amy"},
                    {"x": 30.0, "y": 70, "text": "Tom", "audio_tts": "Tom"},
                    {"x": 53.0, "y": 70, "text": "Sam", "audio_tts": "Sam"},
                    {"x": 70.0, "y": 70, "text": "Ben", "audio_tts": "Ben"},
                    {"x": 88.0, "y": 70, "text": "Lily", "audio_tts": "Lily"},
                ]}),

            # 12 — картинка к «Верно / неверно»
            ("text", {"html":
                "<p>Посмотри на картинку. Прочитай предложения ниже и укажи, верно или неверно.</p>"
                f'<p><img src="{c("t_toy_shelf")}" alt="" style="max-width:100%"></p>'}),

            # 13
            ("truefalse", {
                "title": "Верно или неверно?",
                "statements": [
                    {"text": "The ball is big.", "correct": True},
                    {"text": "The car is big.", "correct": False},
                    {"text": "The train is short.", "correct": False},
                    {"text": "The kite is old.", "correct": False},
                    {"text": "The doll is beautiful.", "correct": True},
                ]}),

            # 14 — SPEAKING TASK
            ("speaking", {
                "title": "SPEAKING TASK 🎤",
                "html": "<p>Ответь на вопросы:</p><ol>"
                        "<li>What’s your favourite toy?</li>"
                        "<li>What’s your favourite number?</li>"
                        "<li>What’s your favourite colour?</li>"
                        "<li>What’s your name?</li>"
                        "<li>How old are you?</li>"
                        "<li>What’s your sister’s/brother’s favourite toy?</li>"
                        "<li>What’s your sister’s/brother’s favourite number?</li>"
                        "<li>What’s your sister’s/brother’s favourite colour?</li>"
                        "<li>What’s your sister’s/brother’s name?</li>"
                        "<li>How old is your sister/brother?</li>"
                        "</ol><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>",
                "needs_review": True,
            }),
        ],
    },
}
