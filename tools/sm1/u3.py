"""Super Minds 1 · Unit 3 · My pets — тест юнита (домашки юнита уже в базе).

Выгрузка: «Super Minds 1 Unit 3 Test». Разбор — docs/SM1_разбор_u6_t3.md.
Карточки животных animal_*.webp — лист ЛТ3.1, ещё не сгенерирован
(в базе они есть только в base64 внутри старых уроков, вытаскивать не стали).
Остальные картинки вырезаны из PDF.
"""
from sm1_build import *  # noqa: F401,F403  img, shared

U = "u3"

ANIMALS = [  # (en, ru, файл)
    ("elephant", "слон", "animal_elephant"),
    ("rat", "крыса", "animal_rat"),
    ("lizard", "ящерица", "animal_lizard"),
    ("frog", "лягушка", "animal_frog"),
    ("spider", "паук", "animal_spider"),
    ("dog", "собака", "animal_dog"),
    ("cat", "кошка", "animal_cat"),
    ("duck", "утка", "animal_duck"),
    ("donkey", "осёл", "animal_donkey"),
]
FILE = {en: f for en, ru, f in ANIMALS}


def order(words, image):
    return ("order", {"title": "Расставь слова в правильном порядке.", "image": img(U, image),
                      "words": words, "sentence": " ".join(words)})


LESSONS = {
    "u3_test": {
        "unit": U, "unit_title": "Unit 3 · My pets", "unit_sort": 3,
        "lesson_title": "Unit 3 Test", "lesson_sort": 7, "kind": "test",
        "blocks": [
            # Блок 1 выгрузки — словарный тест «Впиши буквы» по 9 словам.
            ("exact_input", {"items": [
                {"prompt": f"Напиши по-английски: {ru}", "accept": [en, en.capitalize()]}
                for en, ru, f in ANIMALS]}),

            # Блок 2 «Соедини слова с картинками»: справа в выгрузке пусто,
            # картинок нет — ставим карточки ЛТ3.1.
            ("match", {"title": "Соедини слова с картинками",
                       "pairs": [{"left_image": img(U, FILE[w]), "right": w}
                                 for w in ("duck", "spider", "lizard", "dog", "elephant", "cat")]}),

            ("speaking", {"title": "Прочитай предложения вслух 🎤",
                          "html": "<p>Внимательно <b>прочитай предложения глазками</b> 👀</p>"
                                  "<p><b>Нажми на микрофон 🎤 и проговори их вслух.</b> У тебя получится! 🌟</p>"
                                  "<ol><li>The bread is on the tray.</li><li>I can bake a cake today.</li>"
                                  "<li>Write your name here.</li><li>I can hear a coin drop.</li>"
                                  "<li>My sister has long hair.</li></ol>",
                          "needs_review": True}),

            # Блок 4 «Выбери правильный вариант» (выпадающие списки в каждом
            # пропуске) — квиз; варианты на несколько пропусков даём набором.
            ("quiz", {"questions": [
                {"q": "The ___ is ___ the plane.", "type": "single", "image": img(U, "test_elephant_plane"),
                 "options": [{"text": "lizard … in"}, {"text": "elephant … on"},
                             {"text": "spider … under"}, {"text": "elephant … under"}],
                 "correct": [1]},
                {"q": "The frog is ___ the desk.", "type": "single", "image": img(U, "test_frog_table"),
                 "options": [{"text": "on"}, {"text": "in"}, {"text": "under"}],
                 "correct": [2]},
                {"q": "The rat is ___ the bag.", "type": "single", "image": img(U, "test_rat_bag"),
                 "options": [{"text": "in"}, {"text": "on"}, {"text": "under"}],
                 "correct": [0]},
                {"q": "A: Do you like ___?<br>B: No, I ___.", "type": "single", "image": img(U, "test_spider"),
                 "options": [{"text": "elephants … do"}, {"text": "lizards … do like"},
                             {"text": "spiders … do"}, {"text": "spiders … don't"}],
                 "correct": [3]},
                {"q": "A: I love dogs. Do you ___ dogs?<br>B: Yes, I ___. I ___ dogs, too.", "type": "single",
                 "image": img(U, "test_dogs"),
                 "options": [{"text": "likes … do … don't like"}, {"text": "like … do … like"},
                             {"text": "do like … like … liking"}, {"text": "like … don't … like"}],
                 "correct": [1]},
            ]}),

            order(["The elephants", "are", "on", "the ruler."], "test_elephants_ruler"),
            # В выгрузке «I don't like lizards, too.» — с отрицанием так не говорят
            # (нужно either). Убрали «too», строка в доработке.
            order(["I", "don't", "like", "lizards."], "test_lizards"),
            order(["The ducks", "are", "on", "the books."], "test_ducks_books"),
            order(["The dog", "is", "under", "the desk."], "test_dog_desk"),
            order(["I", "like", "cats,", "too."], "test_cat"),

            ("gaps", {"title": "READING. Посмотри на картинку. Где находятся животные? "
                               "Перетащи слово в каждое предложение.",
                      "mode": "drag", "image": img(U, "test_animals_where"),
                      "text": "1. The __frog__ is on the box.\n"
                              "2. The spider is __under__ the chair.\n"
                              "3. The lizard is __in__ the bag.\n"
                              "4. The dog is __on__ the sofa.\n"
                              "5. The __rat__ is under the table.",
                      "gaps_expected": 5}),

            # Блок 7 LISTENING «Какое животное нравится каждому ребёнку?» —
            # справа плейсхолдеры, аудио нет: по-настоящему пустой, в урок не кладём.

            ("speaking", {"title": "SPEAKING TASK 🎤",
                          "html": "<p>Посмотри на картинку и расскажи, кто где находится.</p>"
                                  "<p><i>For example: The dog is on the table. The elephant is under the table.</i></p>"
                                  "<p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>",
                          "image": img(U, "test_attic_animals"),
                          "needs_review": True}),
        ],
    },
}
