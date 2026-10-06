"""GG3 · Final Test — итоговый тест по Units 1–8. Источник: docs/GG3_разбор_final.md.

Разделы Listening / Reading and Writing / Speaking — заголовками-текстом, как в
выгрузке. Картинка к «верно/неверно» — наша перерисованная сцена кемпинга
(у truefalse нет поля картинки, поэтому она в текстовом блоке перед ним,
вместе с заголовком раздела Reading and Writing).
"""
from gg2_build import todo, video
from gg3_kit import gimg, accept, scramble, q, quiz_block, speaking

U = "final"
UNIT = {"unit": U, "unit_title": "Final Test", "unit_sort": 9}

SCRAMBLE = [("u1", "water_plants", "water the plants"), ("u4", "hairdryer", "hairdryer"),
            ("u2", "cashier", "cashier"), ("u5", "bruise", "bruise"), ("u6", "bake", "bake"),
            ("u7", "cottage", "cottage"), ("u8", "shake_hands", "shake hands")]

LESSONS = {
    "final": {**UNIT, "lesson_title": "Final Test", "lesson_sort": 0, "kind": "test", "blocks": [
        # 1–3 · Listening
        ("text", {"html": "<h2>Listening 🎧</h2>"}),
        video("Listen to five people talking about health problems.",
              "аудио к заданию Listening: пять человек рассказывают о проблемах со здоровьем "
              "(Ben, Molly, Duncan, Olivia, Stuart) — в выгрузке плеер пустой"),
        ("truefalse", {"title": "Listen to five people talking about health problems. Choose T (true) or F (false).",
                       "statements": [
                           {"text": "Ben doesn't want to stop snorkelling.", "correct": True},
                           {"text": "Molly got headaches, because her eyes got tired.", "correct": True},
                           {"text": "Molly wears glasses now.", "correct": True},
                           {"text": "Duncan got the flu eight months ago.", "correct": False},
                           {"text": "Olivia's dad put cold tea on her mosquito bites.", "correct": False},
                           {"text": "Spicy food is bad for Stuart's stomach.", "correct": True},
                       ]}),
        # 4–5 · Reading and Writing
        ("text", {"html": "<h2>Reading and Writing 📖</h2>"
                          "<p>Look at the picture. Then choose True (Верно) or False (Неверно).</p>"
                          f'<p><img src="{gimg(U, "scene_camping")}" alt="Camping" style="max-width:100%"></p>'}),
        ("truefalse", {"title": "Look at the picture. Choose True or False.", "statements": [
            {"text": "Two people are walking together, and they are carrying their backpacks.", "correct": True},
            {"text": "The man near the fire is singing, and the woman next to him is playing the guitar.",
             "correct": False},
            {"text": "The tents in the picture are bigger than the backpacks.", "correct": True},
            {"text": "The boy near the lake is going to swim.", "correct": False},
        ]}),
        # 6 · скрэмбл
        todo(("exact_input", {"title": "Unjumble the letters. Картинка — подсказка.", "items": [
            {"image": gimg(u, name), "prompt": f"{n}. {scramble(text, seed=n)}", "accept": accept(text)}
            for n, (u, name, text) in enumerate(SCRAMBLE, start=1)]}),
            ("check", "СОСТАВ МОЙ: в выгрузке буквы перемешаны, но сам порядок букв не виден — "
                      "перемешал заново; картинки-подсказки добавлены из листов юнитов")),
        # 7 · Home Sweet Home (текст прислан Анной 05.10.2026)
        ("gaps", {"title": "Complete the text with the words in the box. Первое слово (cottage) — пример, "
                           "оно уже вставлено.",
                  "mode": "drag",
                  "text": "HOME SWEET HOME by Helen Todd\n\n"
                          "My family and I live in a cottage in a small __village__ in Yorkshire. "
                          "My parents have their own __business__ here and my brother and I go to the local school.\n"
                          "People here are very friendly. They smile, say good morning and __shake__ hands when "
                          "they meet in the street. They chat to their neighbours when they __water__ the plants "
                          "in the garden or take __out__ the rubbish. It's a great place to live.",
                  "gaps_expected": 5}),
        # 8–9
        quiz_block([
            q("Dad ___ the office a few minutes ago.", ["leaves", "left"], 1),
            q("___ to do this exercise, but I don't understand it.", ["I'm trying", "I try"], 0),
            q("I can't come with you tomorrow. ___ tennis with Paula.", ["I play", "I'm playing"], 1),
            q("She ___ the plants yesterday, so please water them now.", ["didn't water", "doesn't water"], 0),
            q("We ___ the old town when we got lost.", ["explored", "were exploring"], 1),
        ], title="Choose the correct answer."),
        quiz_block([
            q("I can't play basketball. I'm not ___.", ["tall enough", "too tall"], 0),
            q("He always listens ___ to his teachers.", ["careful", "carefully"], 1),
            q("Do we ___ ask for permission?", ["should", "have to"], 1),
            q("I ___ be late! Mum will be angry.", ["mustn't", "can"], 0),
            q("That's the ___ programme on TV.", ["worse", "worst"], 1),
        ], title="Choose the correct answer."),
        # 10–11 · Speaking
        ("text", {"html": "<h2>Speaking 🎤</h2>"}),
        speaking("Answer the questions 🎤", "Answer the questions:", [
            "What chores do you usually do at home?",
            "Do you prefer paying in cash or by card when you go shopping? Why?",
            "Where did you go on your last day trip or holiday? What did you do there?",
            "What were you doing yesterday at eight o'clock?",
            "What should you do if you have a cold or a headache?",
            "Have you ever tried cooking something difficult? What did you make?",
            "Where do you live: in a city, in a town, or in a village? Do you like it? Why?",
            "Are you doing anything special tomorrow or next week?",
            "Do you think you will live in a house or in a flat? Why?"]),
    ]},
}
