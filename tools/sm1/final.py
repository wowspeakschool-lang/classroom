"""Super Minds 1 · Final Test — один урок из двух файлов выгрузки.

Выгрузка ShkolaApp, папка Test SM1/Final: «Final test. Listening» (идёт
первым) и «Final test. Reading - Writing». Разбор — docs/SM1_разбор_u9_final.md.

Listening, блоки 2–6 («Послушай диалог и выбери картинку»: Tom, Anna, Sue,
Ben, Nick) в урок НЕ положены: в выгрузке у вариантов только плейсхолдеры
«Введите вариант ответа», картинок и аудио нет, есть лишь отметки верного.
Это строка в «доработать руками» (там же — номера верных вариантов).

Картинки — media/sm1/ft/ (вырезаны из PDF).
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


LESSONS = {
    "final_test": {
        "unit": FT, "unit_title": "Final Test", "unit_sort": 10,
        "lesson_title": "Final Test", "lesson_sort": 0, "kind": "test",
        "blocks": [
            # ---------------- Listening
            # 1 — аудио 2:46 на всю часть Listening
            ("video", {"title": "Final test · Listening. Послушай аудио и выполни задание ниже",
                       "url": "", "provider": "file"}),

            # 2 — «Диаграмма»: точка k ↔ вариант k (Jane, Mike, Laura, Clare, Paul);
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
