"""GG3 · Unit 4 · Gadgets — тест. Источник: docs/GG3_разбор_u4.md."""
from gg3_kit import unit, gimg, match_block, letters_block, q, quiz_block, order_block, speaking

U = "u4"
UNIT = unit(4, "Unit 4 · Gadgets")

LESSONS = {
    "u4_test": {**UNIT, "lesson_title": "Unit 4 Test", "lesson_sort": 0, "kind": "test", "blocks": [
        # 1
        match_block(U, [("blender", "blender"), ("microwave", "microwave oven"), ("smart_tv", "smart TV"),
                        ("usb_stick", "USB stick"), ("unplug", "unplug"), ("plug_in", "plug in")]),
        # 2
        letters_block(U, [("turn_on", "turn on"), ("remote", "remote control"), ("hairdryer", "hairdryer"),
                          ("games_console", "games console"), ("toaster", "toaster"), ("turn_off", "turn off")]),
        # 3 — 8 пропусков: по вопросу на пропуск
        quiz_block([
            q("He ___ a film on his smart TV when the power went off.",
              ["watched", "was watching", "were watching"], 1),
            q("He was watching a film on his smart TV when the power ___.",
              ["went off", "go off", "wented off"], 0),
            q("They ___ dinner in the kitchen at eight o'clock.", ["was cooking", "cook", "were cooking"], 2),
            q("When I ___, she was drying her hair with the hairdryer.", ["arrives", "arrived"], 1),
            q("When I arrived, she ___ her hair with the hairdryer.", ["was drying", "dried"], 0),
            q("The dog ran ___ to the door when it heard the noise.", ["fastly", "fast"], 1),
            q("He ___ on his games console when his mum turned off the Wi-Fi.",
              ["played", "plays", "was playing"], 2),
            q("He was playing on his games console when his mum ___ the Wi-Fi.",
              ["turned off", "was turning", "turning off"], 0),
        ]),
        # 4–8
        order_block("He", "was", "using", "the blender", "when", "I", "came in."),
        order_block("They", "turned on", "the smart TV", "carefully."),
        order_block("She", "plugged in", "the hairdryer", "and", "started", "drying her hair."),
        order_block("We", "were watching", "a DVD", "at eight o'clock."),
        order_block("He", "unplugged", "the toaster", "quickly."),
        # 9–10
        speaking("SPEAKING TASK 1 🎤", "Опиши картинку, ответь на вопросы.", [
            "What is the girl doing?",
            "What appliance is she using?",
            "How often do you use a hairdryer at home?",
            "Is it safe or dangerous?"], image=gimg(U, "scene_hairdryer"), ordered=False),
        speaking("SPEAKING TASK 2 🎤", "Ответь на вопросы (не забудь отвечать полными предложениями).", [
            "Do you have a smart TV at home?",
            "How often do you use a microwave oven?",
            "What do you usually plug in every day?",
            "What appliance do you use most often?",
            "What do you turn on in the morning?",
            "What do you turn off before leaving home?",
            "What were you doing at eight o'clock yesterday?",
            "What were your parents doing ten minutes ago?"]),
    ]},
}
