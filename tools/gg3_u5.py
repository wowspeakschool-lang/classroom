"""GG3 · Unit 5 · Health — тест. Источник: docs/GG3_разбор_u5.md."""
from gg2_build import todo
from gg3_kit import unit, gimg, match_block, letters_block, q, quiz_block, order_block, speaking

U = "u5"
UNIT = unit(5, "Unit 5 · Health")

LESSONS = {
    "u5_test": {**UNIT, "lesson_title": "Unit 5 Test", "lesson_sort": 0, "kind": "test", "blocks": [
        # 1
        match_block(U, [("sore_throat", "sore throat"), ("blocked_nose", "blocked nose"),
                        ("headache", "headache"), ("stomachache", "a stomachache"),
                        ("cough", "cough"), ("temperature", "temperature")]),
        # 2 — пять слов, cough повторяется из блока 1 (так в выгрузке)
        letters_block(U, [("sneeze", "sneeze"), ("cough", "cough"), ("earache", "earache"),
                          ("toothache", "toothache"), ("runny_nose", "runny nose")]),
        # 3
        quiz_block([
            q("You ___ take this medicine twice a day.", ["has to", "have to"], 1),
            q("He ___ stay at home because he has a temperature.", ["should", "have to"], 0),
            q("They ___ go to school today – it's a holiday.",
              ["shouldn't", "haven't to", "don't have to"], 2),
            q("___ visit the doctor if you have a sore throat?", ["Do you have to", "Have you"], 0),
            q("You ___ drink warm tea when you have a cold.", ["should to", "should"], 1),
        ]),
        # 4–7
        order_block("He", "has", "to", "see", "a doctor."),
        todo(order_block("They", "don't", "have to", "go to school", "with a temperature."),
             ("check", "Предложение из выгрузки: «They don't have to go to school with a temperature» — "
                       "по смыслу «не обязаны» ходить с температурой; если хотите «не должны», "
                       "поменять на shouldn't")),
        order_block("She", "should", "drink", "warm tea", "because she", "has", "a sore throat."),
        order_block("Do", "you", "have", "to", "take", "this medicine", "every day?"),
        # 8–9
        speaking("SPEAKING TASK 1 🎤", "Опиши картинку, ответь на вопросы.", [
            "What's the problem?",
            "Does he have a sore throat / a temperature / a cough?",
            "What should he do?",
            "What shouldn't he do?",
            "Does he have to go to school? Why / why not?",
            "What do you do when you are sick?"], image=gimg(U, "scene_ill"), ordered=False),
        speaking("SPEAKING TASK 2 🎤", "Ответь на вопросы (не забудь отвечать полными предложениями).", [
            "What health problems do you often have?",
            "Do you often have a cold or a cough?",
            "What should you do if you have a temperature?",
            "What shouldn't you do if you have a stomachache?",
            "Do you have to go to school when you are sick?",
            "What should you drink when you have a sore throat?",
            "What do you have to do every day to stay healthy?",
            "What should people do to feel better when they have a headache?"]),
    ]},
}
