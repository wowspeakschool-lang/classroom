"""Super Minds 1 · Unit 4 · Food — тест юнита.

Домашки Unit 4 уже в базе (HW1–HW7, сделаны руками, картинки base64);
здесь только тест. Выгрузка — «Super Minds 1 Unit 4 Test» (PDF 5.9 МБ
скачался целиком). Разбор — docs/SM1_разбор_u7_t4.md.

Картинки еды — наши (листы ЛТ4.1, ЛТ4.2): у «соедини слова с картинками»
картинок в выгрузке нет, а стоковые фото к пропускам и «составь
предложение» — с руками людей (пицца, мороженое) и разного стиля.
Холодильник для speaking вырезан из PDF.
"""
from sm1_build import *

U = "u4"


def f(name):
    return img(U, name)


def q(text, image, options, correct, **extra):
    d = {"q": text, "type": "single", "options": [{"text": o} for o in options],
         "correct": [correct]}
    if image:
        d["image"] = image
    d.update(extra)
    return d


LESSONS = {
    "u4_test": {
        "unit": U, "unit_title": "Unit 4 · Food", "unit_sort": 4,
        "lesson_title": "Unit 4 Test", "lesson_sort": 7, "kind": "test",
        "blocks": [
            # 1 — словарный тренажёр «Впиши буквы» (11 слов)
            ("exact_input", {"items": [
                {"prompt": f"Напиши по-английски: {ru}", "accept": [en, en.capitalize()],
                 "audio_tts": en}
                for en, ru in [
                    ("banana", "банан"), ("cake", "торт"), ("sandwich", "бутерброд"),
                    ("apple", "яблоко"), ("pizza", "пицца"), ("sausage", "сосиска"),
                    ("chicken", "курица"), ("steak", "стейк"), ("peas", "горох"),
                    ("carrots", "морковь"), ("fish", "рыба"),
                ]
            ]}),

            # 2 — в выгрузке правые картинки не выгрузились (плейсхолдеры)
            ("match", {"title": "Соедини слова с картинками:", "pairs": [
                {"left": w, "left_audio_tts": w, "right": "картинка " + w,
                 "right_image": f(n)}
                for w, n in [("chicken", "food_chicken"),
                             ("cheese sandwich", "food_cheese_sandwich"),
                             ("cake", "food_cake"), ("sausage", "food_sausage"),
                             ("banana", "food_banana"), ("steak", "food_steak")]
            ]}),

            ("speaking", {
                "title": "Прочитай вслух 🎤",
                "needs_review": True,
                "html":
                    "<p>Внимательно прочитай предложения глазками 👀</p>"
                    "<p>Нажми на микрофон 🎤 и проговори их вслух.</p>"
                    "<ol><li>Look at the photo of the turtle.</li>"
                    "<li>The crow sits on a rope.</li>"
                    "<li>Chew the cute little cube.</li>"
                    "<li>I draw a big cloud.</li>"
                    "<li>The giraffe is very tall.</li></ol>"
                    "<p>У тебя получится! 🌟</p>"}),

            # 4 — в выгрузке пять блоков «Выбери правильный вариант» (выпадающие
            # списки в пропусках); здесь вопрос на каждый пропуск, варианты те же.
            # В выгрузке опечатка «ccarrots» — исправлено.
            ("quiz", {"title": "Заполни пропуски — выбери подходящий вариант", "questions": [
                q("Заполни пропуски — выбери подходящий вариант.<br>"
                  "A: Have we ___ any pizza?<br>B: Yes, we have.",
                  f("food_pizza"), ["have", "got", "have got"], 1),
                q("A: Have we got any pizza?<br>B: Yes, we ___.",
                  f("food_pizza"), ["got", "haven't got", "have"], 2),
                q("We ___ any steak.", f("food_steak"),
                  ["haven't got", "don't got", "haven't"], 0),
                q("A: What ___ you got?<br>B: I've got an apple and a banana.",
                  f("food_apple_banana"), ["has", "have", "got"], 1),
                q("A: What have you got?<br>B: I've ___ an apple and a banana.",
                  f("food_apple_banana"), ["have", "have got", "got"], 2),
                q("A: ___ we got any milk?<br>B: No, we haven't.",
                  f("food_milk"), ["Has", "Got", "Have"], 2),
                q("A: Have we got any milk?<br>B: No, we ___.",
                  f("food_milk"), ["haven't", "have", "don't"], 0),
                q("A: What ___ you got in your lunch box?<br>B: I have got peas and carrots.",
                  f("food_peas_carrots"), ["got", "have", "do"], 1),
                q("A: What have you got in your lunch box?<br>B: I ___ peas and carrots.",
                  f("food_peas_carrots"), ["'ve", "got", "have got"], 2),
            ]}),

            ("order", {"image": f("food_cake"),
                       "words": ["Have", "we", "got", "any", "cake?"],
                       "sentence": "Have we got any cake?",
                       "audio_tts": "Have we got any cake?"}),
            ("order", {"image": f("food_chicken_carrots"),
                       "words": ["I've", "got", "chicken", "and", "carrots."],
                       "sentence": "I've got chicken and carrots.",
                       "audio_tts": "I've got chicken and carrots."}),
            ("order", {"image": f("food_pizza"),
                       "words": ["Have", "we", "got", "any", "pizza?"],
                       "sentence": "Have we got any pizza?",
                       "audio_tts": "Have we got any pizza?"}),
            ("order", {"image": f("food_orange_juice"),
                       "words": ["I", "haven't", "got", "orange", "juice."],
                       "sentence": "I haven't got orange juice.",
                       "audio_tts": "I haven't got orange juice."}),
            ("order", {"image": f("food_ice_cream"),
                       "words": ["Have", "you", "got", "any", "ice", "cream?"],
                       "sentence": "Have you got any ice cream?",
                       "audio_tts": "Have you got any ice cream?"}),

            # 10 — READING: текст в выгрузке был картинкой (900×94), здесь текстом
            ("truefalse", {
                "title": "READING. Прочитай текст. Прочитай предложения и выбери Верно или "
                         "Неверно. — Hi! My name is Ben. Look at my lunch box! I've got a "
                         "cheese sandwich and an apple. I've got some carrots too. Yummy! "
                         "But I haven't got a banana. And I haven't got any cake. Oh no!",
                "statements": [
                    {"text": "Ben has got a cheese sandwich.", "correct": True},
                    {"text": "Ben has got a banana.", "correct": False},
                    {"text": "Ben has got an apple.", "correct": True},
                    {"text": "Ben has got a cake.", "correct": False},
                    {"text": "Ben has got some carrots.", "correct": True},
                ]}),

            # 11 — LISTENING: аудио в выгрузке нет, ждём от методиста
            ("quiz", {"title": "LISTENING. Послушай запись. Выбери правильный ответ.",
                      "questions": [
                q("LISTENING. Послушай запись. Выбери правильный ответ.<br>"
                  "1. Have they got any bananas?", None,
                  ["Yes, they have.", "No, they haven't."], 1, audio=""),
                q("2. What has Sam got?", None, ["a steak", "a cake", "pizza"], 1),
                q("3. Have they got any peas?", None,
                  ["Yes, they have.", "No, they haven't."], 0),
                q("4. What hasn't Lisa got?", None, ["carrots", "an apple", "a chicken"], 2),
                q("5. Have they got any cheese?", None,
                  ["No, they haven't.", "Yes, they have."], 1),
            ]}),

            ("speaking", {
                "title": "SPEAKING TASK 🎤",
                "needs_review": True,
                "image": f("fridge"),
                "html":
                    "<p>Посмотри на картинку. Представь, что это твой холодильник. "
                    "Расскажи, что у тебя есть и чего нет.</p>"
                    "<p><i>For example:<br>I’ve got cheese.<br>I’ve got steak.<br>"
                    "I haven’t got pizza.</i></p>"
                    "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>"}),
        ],
    },
}
