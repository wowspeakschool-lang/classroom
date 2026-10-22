# -*- coding: utf-8 -*-
"""Тексты аудирования для тестов юнитов 1–8 курса Go Getter 3.

Собраны 22.10.2026 при вычитке тестов. Блоки аудирования залиты в базу
ЗАГОТОВКАМИ: у блока пустой `audio` и НЕТ `audio_tts` — кнопка «Озвучить
пачкой» нашла бы такую пару и затёрла место под нормальную запись.

Озвучивает Yandex SpeechKit английским голосом из отдельной сессии
(см. docs/ozvuchka_speechkit.md). Рассказ — третье лицо, без диалогов:
голос один, реплики двух людей не различить.

Готовый mp3 кладётся в бакет classroom-media, папка gg3/, имя — из NARRATIONS
(поле `file`). Ссылка вписывается в поле `audio` блока-заготовки.

Номер блока в имени файла — как в редакторе (sort_order + 1) на 22.10.2026.
ВНИМАНИЕ: после запуска builds/gg_tests/udalit_gg3.sql блок аудирования юнита 1
переедет с 17-го места на 13-е. Имя файла при этом НЕ меняем.

Тексты держим здесь константами, чтобы они не потерялись вместе с контейнером.
"""

NARRATIONS = {
    1: {
        "file": "gg3_u1_test_b17.mp3",
        "block": 17,
        "hero": "Оливер",
        "text": (
            "This is a story about a boy called Oliver. Oliver is eleven and he lives in a flat "
            "with his mum, his dad and his little brother Ben. In Oliver's family everybody helps "
            "at home. Oliver sets the table every evening and he takes out the rubbish on Mondays "
            "and Thursdays. He doesn't like taking out the rubbish, but he doesn't mind setting "
            "the table. His brother Ben is only five, so he doesn't do many chores. Ben feeds the "
            "cat and puts away his toys. Oliver's mum says Ben is very patient for a small boy. "
            "Oliver's dad irons the shirts on Sunday mornings and he always listens to music when "
            "he irons. Right now Oliver isn't at home. He is at his grandmother's house and he is "
            "helping her in the garden. He is watering the plants. His grandmother is making a "
            "cake for him."
        ),
    },
    2: {
        "file": "gg3_u2_test_b13.mp3",
        "block": 13,
        "hero": "Зои",
        "text": (
            "This is a story about a girl called Zoe. Zoe is twelve and she lives in a small town. "
            "She goes shopping with her dad every Saturday morning. They always make a shopping "
            "list at home first. There are three shops near Zoe's house: a baker's, a greengrocer's "
            "and a big supermarket. The supermarket is the biggest shop in the town, but Zoe's dad "
            "says the fruit at the greengrocer's is fresher and cheaper. So they buy their bread at "
            "the baker's, their fruit at the greengrocer's and everything else at the supermarket. "
            "Zoe's dad never pays in cash. He always pays by card. The queue at the supermarket is "
            "usually long on Saturdays, but today it isn't too long. Zoe carries the shopping home. "
            "The bags are heavy, but she is strong enough."
        ),
    },
    3: {
        "file": "gg3_u3_test_b12.mp3",
        "block": 12,
        "hero": "Дэниел",
        "text": (
            "This is a story about a boy called Daniel and his holiday last year. Daniel went to "
            "Italy with his parents and his sister. They were there for two weeks. They stayed in a "
            "small flat near the beach. Every morning Daniel went to the beach and went snorkelling "
            "with his father. He saw a lot of colourful fish. In the afternoon it was too hot, so "
            "the family stayed inside. One day they went on a day trip to a big city. They explored "
            "the old streets and visited a museum. Daniel didn't like the museum and he got bored, "
            "but his sister loved it. On the last day the family tried the local food in a small "
            "restaurant. Daniel ate pizza and his sister ate fish. Daniel didn't want to go home. "
            "He was sad at the airport."
        ),
    },
    4: {
        "file": "gg3_u4_test_b13.mp3",
        "block": 13,
        "hero": "Нина",
        "text": (
            "This is a story about a girl called Nina and a strange evening at her house. Last "
            "Friday Nina was doing her homework in her bedroom. Her laptop battery was low, so she "
            "plugged in the charger. Her brother was watching a film on the smart TV downstairs and "
            "her mother was making toast in the kitchen. The toaster was very old. Suddenly there "
            "was a loud noise and all the lights in the house went off. Nina ran quickly downstairs. "
            "Her brother was angry, because the film was very good. Her mother looked at the toaster "
            "carefully. It was black inside. Nina's father came home ten minutes later. He unplugged "
            "the old toaster and the lights came back on. The next day the family bought a new "
            "toaster."
        ),
    },
    5: {
        "file": "gg3_u5_test_b13.mp3",
        "block": 13,
        "hero": "Макс",
        "text": (
            "This is a story about a boy called Max and a bad week. Max is ten years old. On Monday "
            "he fell off his bike in the park and he got a bruise on his leg and a small cut on his "
            "hand. His mother put some cream on the cut. On Tuesday Max had a bad headache and a "
            "temperature, so he stayed at home. His mother says he has to drink a lot of water when "
            "he has a temperature. On Wednesday the doctor visited him. The doctor says Max "
            "shouldn't play football for a week and he has to rest. Max doesn't like this, because "
            "football is his favourite sport. On Thursday Max felt better. His throat wasn't sore "
            "and his headache was gone. On Friday he went back to school, but he didn't play "
            "football."
        ),
    },
    6: {
        "file": "gg3_u6_test_b13.mp3",
        "block": 13,
        "hero": "Феликс",
        "text": (
            "This is a story about a boy called Felix and his first dinner. Felix is thirteen and he "
            "has never cooked dinner for his family. Last Sunday he decided to try. He chose a "
            "simple recipe: pasta with tomato sauce. First he chopped an onion and some garlic. "
            "Then he fried them in a pan with a little oil. He added the tomatoes and some salt. "
            "While the sauce was cooking, he boiled the water for the pasta in a big pot. Felix put "
            "too much salt in the sauce, so it was very salty. His sister said it was disgusting, "
            "but his mother said it was delicious. His father ate two plates. Felix was happy. He "
            "has cooked dinner three times since that Sunday, and now he never puts too much salt "
            "in his food."
        ),
    },
    7: {
        "file": "gg3_u7_test_b14.mp3",
        "block": 14,
        "hero": "Руби",
        "text": (
            "This is a story about a girl called Ruby. Ruby lives in a terraced house in a small "
            "village near the sea. Her house isn't big, but it has got a basement and a balcony. "
            "Ruby's favourite place is the balcony, because she can see the sea from it. There is "
            "an old bookcase in her bedroom and a big mirror next to the window. Ruby is twelve and "
            "she has got two brothers, so she must share her room with her little brother. She "
            "doesn't like that. Next month the family are moving to a bigger house. The new house "
            "is a detached house with four bedrooms, and Ruby is getting her own room. This weekend "
            "the family are cleaning up the new house. On Sunday Ruby's cousins are coming to help. "
            "Ruby must pack all her books on Saturday."
        ),
    },
    8: {
        "file": "gg3_u8_test_b13.mp3",
        "block": 13,
        "hero": "Элли",
        "text": (
            "This is a story about a girl called Ellie and her plans. Ellie is thirteen and she "
            "lives in a small town. She says she will not live in this town when she is older. She "
            "thinks she will live in a big city, or maybe abroad. Ellie wants to be a vet, because "
            "she loves animals. She has got two dogs and a cat. Her mother says the job is "
            "difficult, but Ellie says she will study hard. Ellie will learn Spanish at school next "
            "year. She says she will need it, because she wants to work in South America for a few "
            "years. Ellie doesn't think she will be rich, but she thinks she will be happy. She "
            "also says she will have a big family one day, with three or four children and a lot of "
            "animals."
        ),
    },
}

if __name__ == "__main__":
    for unit, n in sorted(NARRATIONS.items()):
        words = len(n["text"].split())
        print(f"Unit {unit} · блок {n['block']} · {n['file']} · {words} слов")
