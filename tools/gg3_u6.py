"""GG3 · Unit 6 · Cooking — тест. Источник: docs/GG3_разбор_u6.md."""
from gg3_kit import unit, gimg, match_block, letters_block, q, quiz_block, order_block, speaking

U = "u6"
UNIT = unit(6, "Unit 6 · Cooking")

LESSONS = {
    "u6_test": {**UNIT, "lesson_title": "Unit 6 Test", "lesson_sort": 0, "kind": "test", "blocks": [
        # 1
        match_block(U, [("bake", "bake"), ("bowl", "bowl"), ("fry", "fry"),
                        ("mix", "mix"), ("peel", "peel"), ("fork", "fork")]),
        # 2
        letters_block(U, [("cake_tin", "cake tin"), ("chop", "chop"), ("oven", "oven"),
                          ("pot", "pot"), ("spoon", "spoon"), ("slice", "slice")]),
        # 3
        quiz_block([
            q("I ___ a cake today.", ["have bake", "have baked"], 1),
            q("She ___ spicy food.", ["has never tried", "have ever tried", "never try"], 0),
            q("They ___ anything salty.", ["hasn't eaten", "haven't eaten"], 1),
            q("___ dinner for your family?", ["Do you ever cook", "Have you cooked ever", "Have you ever cooked"], 2),
            q("He ___ the vegetables yet.", ["haven't chopped", "hasn't chopped", "didn't chopped"], 1),
        ]),
        # 4–8
        order_block("I", "have", "never", "baked", "a cake", "in this oven."),
        order_block("Have", "you", "ever", "tried", "sour soup?"),
        order_block("She", "has", "sliced", "the vegetables."),
        order_block("They", "haven't", "mixed", "the ingredients", "yet."),
        order_block("He", "has", "added", "salt", "to the pot."),
        # 9–10
        speaking("SPEAKING TASK 1 🎤", "Опиши картинку, ответь на вопросы.", [
            "What is she doing now?",
            "What has she done already?",
            "What kitchen tools can you see?",
            "Has she peeled or chopped anything?",
            "Do you like cooking? Why / why not?",
            "What have you cooked recently?"], image=gimg(U, "scene_cooking"), ordered=False),
        speaking("SPEAKING TASK 2 🎤", "Ответь на вопросы (не забудь отвечать полными предложениями).", [
            "Have you ever baked a cake?",
            "Have you ever tried something spicy?",
            "What delicious food have you eaten recently?",
            "What disgusting food have you tried?",
            "Have you ever cooked dinner for your family?",
            "Have you ever chopped vegetables?",
            "Have you ever eaten something very sour?"]),
    ]},
}
