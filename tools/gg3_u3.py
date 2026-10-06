"""GG3 · Unit 3 · Holidays — тест. Источник: docs/GG3_разбор_u3.md."""
from gg3_kit import unit, gimg, match_block, letters_block, q, quiz_block, order_block, speaking

U = "u3"
UNIT = unit(3, "Unit 3 · Holidays")

LESSONS = {
    "u3_test": {**UNIT, "lesson_title": "Unit 3 Test", "lesson_sort": 0, "kind": "test", "blocks": [
        # 1
        match_block(U, [("hiking", "go hiking"), ("camping", "go camping"),
                        ("boat_trip", "go on a boat trip"), ("local_food", "try the local food"),
                        ("cycling", "go cycling"), ("explore_city", "explore a city")]),
        # 2
        letters_block(U, [("snorkelling", "go snorkelling"), ("guided_tour", "go on a guided tour"),
                          ("beach", "go to the beach"), ("get_tired", "get tired"),
                          ("get_lost", "get lost"), ("get_bored", "get bored")]),
        # 3
        quiz_block([
            q("We ___ to the beach yesterday.", ["goed", "went"], 1),
            q("He ___ tired on the day trip.", ["didn't get", "wasn't get"], 0),
            q("___ the local food?", ["Do you try", "Did you try"], 1),
            q("They ___ lost in the city centre.", ["were", "was", "weren't"], 0),
            q("She ___ on a guided tour last weekend.", ["didn't went", "wasn't go", "didn't go"], 2),
        ]),
        # 4–8
        order_block("We", "went", "on a day trip", "last Saturday."),
        order_block("Did", "you", "go snorkelling", "on holiday?"),
        order_block("They", "didn't", "explore", "the town", "yesterday."),
        order_block("Was", "the weather", "cold", "at the beach?"),
        order_block("He", "got", "bored", "on the guided tour."),
        # 9–10
        speaking("SPEAKING TASK 1 🎤", "Опиши картинку, ответь на вопросы.", [
            "Where were the people?",
            "What did they do on their trip?",
            "Did they go hiking or cycling?",
            "What did they carry with them?",
            "Did they get tired?",
            "What was the weather like?",
            "Were they happy on the trip?",
            "What else can you see?"], image=gimg(U, "scene_trip")),
        speaking("SPEAKING TASK 2 🎤", "Ответь на вопросы (не забудь отвечать полными предложениями).", [
            "Where did you go last weekend?",
            "Did you go to the beach last summer?",
            "Did you try any local food on holiday?",
            "What city or area did you explore last year?",
            "Did you get bored on your trip?",
            "Did you get lost in a new place?",
            "What was the weather like on your last holiday?",
            "What did you enjoy most on your trip?",
            "Were you with friends or family?",
            "Did you buy any souvenirs?"]),
    ]},
}
