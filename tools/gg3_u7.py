"""GG3 · Unit 7 · Homes — тест. Источник: docs/GG3_разбор_u7.md."""
from gg3_kit import unit, gimg, match_block, letters_block, q, quiz_block, order_block, speaking

U = "u7"
UNIT = unit(7, "Unit 7")

LESSONS = {
    "u7_test": {**UNIT, "lesson_title": "Unit 7 Test", "lesson_sort": 0, "kind": "test", "blocks": [
        # 1
        match_block(U, [("detached", "detached house"), ("terraced", "terraced house"), ("attic", "attic"),
                        ("balcony", "balcony"), ("lift", "lift"), ("stairs", "stairs")]),
        # 2
        letters_block(U, [("block_of_flats", "block of flats"), ("basement", "basement"), ("mirror", "mirror"),
                          ("drawer", "drawer"), ("tap", "tap"), ("semi_detached", "semi-detached house")]),
        # 3
        quiz_block([
            q("We ___ our grandparents tomorrow morning.", ["are visiting", "visit"], 0),
            q("She ___ to a new flat next week.", ["moves", "is moving"], 1),
            q("You ___ run on the stairs – it's dangerous.", ["must", "mustn't"], 1),
            q("He ___ use the lift because his leg is broken.", ["can't", "can to", "can"], 2),
            q("Students ___ clean up the classroom after school.", ["must", "mustn't", "can't"], 0),
        ]),
        # 4–8
        order_block("We", "are", "checking out", "a new house", "this evening."),
        order_block("She", "must", "clean up", "her room", "today."),
        order_block("They", "are", "meeting", "friends", "tomorrow", "at six o'clock."),
        order_block("He", "is", "looking for", "the book", "in the attic."),
        order_block("You", "mustn't", "wake up", "the baby", "in the next room."),
        # 9–10
        speaking("SPEAKING TASK 1 🎤", "Опиши картинку, ответь на вопросы.", [
            "What kind of house is it?",
            "What are the people doing now?",
            "Are they moving in or moving out?",
            "What can you see around the house?",
            "What must they do before they finish moving?"], image=gimg(U, "scene_moving"), ordered=False),
        speaking("SPEAKING TASK 2 🎤", "Ответь на вопросы (не забудь отвечать полными предложениями).", [
            "Where do you live: in a city, in a town or in a village?",
            "What kind of home would you like to live in?",
            "What floor do you live on?",
            "Do you have an attic or a basement?",
            "What can you see from your balcony?",
            "What must you do at home every day?",
            "Can you use the lift in your building?",
            "What room do you clean up most often?",
            "What are you doing tomorrow evening?",
            "What are you doing after school today?"]),
    ]},
}
