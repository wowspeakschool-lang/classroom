"""Super Minds 1 · Final Test — один урок из двух файлов выгрузки.

Выгрузка ShkolaApp, папка Test SM1/Final: «Final test. Listening» (идёт
первым) и «Final test. Reading - Writing». Разбор — docs/SM1_разбор_u9_final.md.

Listening, блоки 2–6 («Послушай диалог и выбери картинку»: Tom, Anna, Sue,
Ben, Nick) в урок НЕ положены: в выгрузке у вариантов только плейсхолдеры
«Введите вариант ответа», картинок и аудио нет, есть лишь отметки верного.
Это строка в «доработать руками» (там же — номера верных вариантов).

Картинки — media/sm1/ft/ (вырезаны из PDF).

19.10.2026 Анна решила: аудирование делаем своё. Рассказ (NARRATION_STORY) и
описание пикника для «Диаграммы» (NARRATION_PICNIC) Анна начитывает одним
файлом sm1_final_b1.mp3 — сначала рассказ, потом пикник; до записи у блока 1
пустой url. Варианты квиза (блок 2) — только уже готовые картинки media/sm1/**.
"""
from sm1_build import *

FT = "ft"


def f(name):
    return img(FT, name)


def yes_no(sentence, image, ok):
    """«Галочка или крестик»: верный ✅, если картинка совпадает с предложением."""
    return {"q": sentence, "type": "single", "image": image,
            "options": [{"text": "✅ совпадает"}, {"text": "❌ не совпадает"}],
            "correct": [0 if ok else 1]}


# Текст для записи Анной (CLAUDE.md: аудирование синтезом не озвучиваем).
NARRATION_STORY = (
    "Look at these five children. "
    "This is Tom. Tom is seven. He has got a new kite. It's red and yellow. He hasn't got a train. "
    "This is Anna. Anna likes pizza. She doesn't like cake. "
    "This is Sue. Sue has got a pet. It's a dog. It's brown and white. She hasn't got a cat. "
    "This is Ben. Ben can't swim and he can't play football. But he can ride a bike! His bike is red. "
    "This is Nick. Today Nick is wearing a brown jacket. He isn't wearing a cap."
)
# Вторая часть той же записи — к «Диаграмме» с пикником (блок 3): прежде её
# озвучивало оригинальное аудирование, которое заменяется.
NARRATION_PICNIC = (
    "Now look at the picnic. "
    "Mike is a boy. He is wearing a blue T-shirt and red shorts. He is running. "
    "Paul is Mike's dad. He is wearing a red T-shirt. He is running, too. "
    "Jane is the grandma. She has got grey hair. She is eating an apple. "
    "Clare is a little girl. She has got yellow hair. She has got a doll. "
    "Laura is the mum. She is wearing a pink skirt. She has got a flower."
)


def listen_pic(q, options, correct):
    """Вопрос аудирования: варианты — картинки (unit, файл)."""
    return {"q": q, "type": "single", "options": [{"image": img(u, n)} for u, n in options],
            "correct": [options.index(correct)]}


LESSONS = {
    "final_test": {
        "unit": FT, "unit_title": "Final Test", "unit_sort": 10,
        "lesson_title": "Final Test", "lesson_sort": 0, "kind": "test",
        "blocks": [
            # ---------------- Listening
            # 1 — запись Анны (NARRATION_STORY + NARRATION_PICNIC), будет под тем же
            # именем sm1_final_b1.mp3; пока url пустой
            ("video", {"title": "Final test · Listening. Послушай рассказ",
                       "url": "", "provider": "file"}),

            # 2 — по рассказу; верный на разных местах
            ("quiz", {"title": "Послушай рассказ ещё раз и выбери правильную картинку.", "questions": [
                listen_pic("What has Tom got?",
                           [("u2", "toy_train"), ("u2", "toy_kite"), ("u2", "toy_car")], ("u2", "toy_kite")),
                listen_pic("What does Anna like?",
                           [("u4", "food_cake"), ("u4", "food_banana"), ("u4", "food_pizza")], ("u4", "food_pizza")),
                listen_pic("What pet has Sue got?",
                           [("u3", "animal_dog"), ("u3", "animal_cat"), ("u3", "animal_rat")], ("u3", "animal_dog")),
                listen_pic("What can Ben do?",
                           [("u5", "act_go_swimming"), ("u5", "act_ride_bike"), ("u5", "act_play_football")],
                           ("u5", "act_ride_bike")),
                listen_pic("What is Nick wearing today?",
                           [("u7", "clothes_cap"), ("u7", "clothes_shorts"), ("u7", "clothes_jacket")],
                           ("u7", "clothes_jacket")),
            ]}),

            # 3 — «Диаграмма»: точка k ↔ вариант k (Jane, Mike, Laura, Clare, Paul);
            # координаты сняты с маркеров на странице PDF
            ("hotspot", {
                "title": "Послушай аудио и соедини имена людей с их изображениями",
                "mode": "label",
                "image": f("ft_picnic"),
                "points": [
                    {"x": 30.7, "y": 70.1, "text": "Jane", "audio_tts": "Jane"},
                    {"x": 18.2, "y": 27.3, "text": "Mike", "audio_tts": "Mike"},
                    {"x": 63.5, "y": 65.6, "text": "Laura", "audio_tts": "Laura"},
                    {"x": 15.2, "y": 70.1, "text": "Clare", "audio_tts": "Clare"},
                    {"x": 40.9, "y": 26.2, "text": "Paul", "audio_tts": "Paul"},
                ],
                "extras": [],
            }),

            # ---------------- Reading & Writing
            # 3 — в выгрузке пять отдельных «Тест» с ✅/❌; верные сверены по PDF
            ("quiz", {"title": "Посмотри на картинку и прочитай предложение. Выбери ✅, если картинка "
                               "и предложение совпадают, и ❌, если они отличаются.",
                      "questions": [
                          yes_no("This is a ruler.", f("ft_eraser"), False),
                          yes_no("This is a spider.", f("ft_spider"), True),
                          yes_no("This is a bike.", f("ft_bike"), True),
                          yes_no("This is a face.", f("ft_arm"), False),
                          yes_no("This is a chicken.", f("ft_chicken"), True),
                      ]}),

            # 4
            ("text", {"html":
                "<p>Посмотри на картинку. В следующем задании прочитай предложения и выбери "
                "<b>Верно</b>, если предложение соответствует картинке, и <b>Неверно</b>, если нет.</p>"
                f'<p><img src="{f("ft_kitchen")}" alt="Семья за завтраком" style="max-width:100%"></p>'}),

            # 5
            ("truefalse", {
                "title": "Верно или неверно?",
                "statements": [
                    {"text": "There is a banana on the table.", "correct": True},
                    {"text": "They are sitting in the bedroom.", "correct": False},
                    {"text": "There is 1 girl.", "correct": True},
                    {"text": "There is a red lamp under the table.", "correct": False},
                    {"text": "There is one chair.", "correct": False},
                ],
            }),

            # 6 — в выгрузке пять «Открытых вопросов» (буквы вразброс + клеточки);
            # ответ однозначен, поэтому exact_input
            ("exact_input", {"items": [
                {"prompt": "Посмотри на картинку и буквы и напиши слово (6 букв)",
                 "image": f("ft_word_pencil"), "accept": ["pencil"]},
                {"prompt": "Посмотри на картинку и буквы и напиши слово (7 букв)",
                 "image": f("ft_word_monster"), "accept": ["monster"]},
                {"prompt": "Посмотри на картинку и буквы и напиши слово (4 буквы)",
                 "image": f("ft_word_duck"), "accept": ["duck"]},
                {"prompt": "Посмотри на картинку и буквы и напиши слово (8 букв)",
                 "image": f("ft_word_bathroom"), "accept": ["bathroom"]},
                {"prompt": "Посмотри на картинку и буквы и напиши слово (7 букв)",
                 "image": f("ft_word_sweater"), "accept": ["sweater"]},
            ]}),
        ],
    },
}
