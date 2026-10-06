"""GG3 · Unit 1 · Chores — тест. Источник: docs/GG3_разбор_u1.md."""
from gg2_build import todo
from gg3_kit import unit, gimg, match_block, letters_block, q, quiz_block, order_block, speaking

U = "u1"
UNIT = unit(1, "Unit 1")

LESSONS = {
    "u1_test": {**UNIT, "lesson_title": "Unit 1 Test", "lesson_sort": 0, "kind": "test", "blocks": [
        # 1
        match_block(U, [("clear_table", "clear the table"), ("feed_dog", "feed the dog"),
                        ("hang_washing", "hang out the washing"), ("iron_tshirt", "iron your T-shirt"),
                        ("take_rubbish", "take out the rubbish"), ("water_plants", "water the plants")]),
        # 2
        letters_block(U, [("load_dishwasher", "load the dishwasher"), ("make_bed", "make your bed"),
                          ("vacuum_room", "vacuum your room"), ("empty_dishwasher", "empty the dishwasher"),
                          ("set_table", "set the table"), ("put_away_clothes", "put away your clothes")]),
        # 3–7
        quiz_block([q("She ___ the dog now.", ["feeds", "is feeding", "is feed"], 1)]),
        quiz_block([q("He usually ___ out the washing on Fridays.", ["is hanging", "hang", "hangs"], 2)]),
        quiz_block([q("___ you ___ your room now? — первый пропуск", ["Are", "Do", "Does", "Is"], 0),
                    q("___ you ___ your room now? — второй пропуск", ["vacuums", "vacuuming", "vacuum"], 1)]),
        quiz_block([q("They ___ their beds at the moment.", ["isn't making", "don't make", "aren't making"], 2)]),
        quiz_block([q("I ___ this homework.", ["am not understanding", "don't understand",
                                               "doesn't understand"], 1)]),
        # 8–12
        order_block("She", "is", "watering", "the plants", "now."),
        order_block("They", "usually", "set", "the table", "at the weekend."),
        order_block("I", "never", "load", "the dishwasher."),
        order_block("He", "is", "ironing", "his T-shirt", "at the moment."),
        order_block("Do", "you", "like", "easy-going", "people?"),
        # 13–14
        speaking("SPEAKING TASK 1 🎤",
                 "Опиши картинку. Расскажи, кто чем занят. Используй Present Continuous и лексику по теме "
                 "«домашние обязанности».<br><i>Example: The woman is sweeping the floor.</i>",
                 image=gimg(U, "scene_chores")),
        speaking("SPEAKING TASK 2 🎤", "Ответь на вопросы. Используй Present Simple и Present Continuous.", [
            "What chores do you usually do at home?",
            "What chore do you never do?",
            "What are you doing right now?",
            "How often do you make your bed?",
            "Who usually vacuums your home?"]),
    ]},
}
