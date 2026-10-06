"""Go Getter 2 · Unit 0 · Get started! — только тест (повторение GG1).

Источник: docs/GG2_разбор_u0.md. Блоки 4 и 5 выгрузки разложены: пять
предложений → пять order, текст Marta → text + quiz.
"""
from gg2_build import img, shared, todo, video

U = "u0"
UNIT = {"unit": U, "unit_title": "Unit 0", "unit_sort": 0}


def order(parts, image=None):
    sentence = " ".join(parts)
    p = {"words": list(parts), "sentence": sentence, "audio_tts": sentence.replace("’", "'")}
    if image:
        p["image"] = image
    return ("order", p)


def single(q, options, right):
    return {"q": q, "type": "single", "options": [{"text": o} for o in options],
            "correct": [options.index(right)]}


LESSONS = {
    "u0_test": {**UNIT, "lesson_title": "Unit 0 Test", "lesson_sort": 0, "kind": "test", "blocks": [
        ("text", {"html":
            f'<p><img src="{shared("good_luck_clover")}" alt="" style="height:180px"></p>'
            "<h2>Тест: вспоминаем Go Getter 1 📝</h2>"
            "<p>В этом тесте ты повторишь всё, что учил в прошлом году: семью, комнату и мебель, "
            "месяцы, глаголы <i>have got</i> и <i>can</i>, <i>there is / there are</i>.</p>"
            "<p>Чтобы пройти тест, нужно набрать 90 баллов. Не торопись и внимательно читай задания. Удачи!</p>"}),

        ("exact_input", {"title": "Напиши слова по-английски", "items": [
            {"prompt": "1. Напиши по-английски: февраль", "image": img(U, "february"),
             "accept": ["February", "february"], "audio_tts": "February"},
            {"prompt": "2. Напиши по-английски: кататься на скейтборде", "image": img(U, "skateboard"),
             "accept": ["skateboard", "Skateboard"], "audio_tts": "skateboard"},
            {"prompt": "3. Напиши по-английски: рисовать", "image": img(U, "draw"),
             "accept": ["draw", "Draw"], "audio_tts": "draw"},
            {"prompt": "4. Напиши по-английски: кресло", "image": img(U, "armchair"),
             "accept": ["armchair", "Armchair", "an armchair"], "audio_tts": "armchair"},
            {"prompt": "5. Напиши по-английски: шкаф для одежды", "image": img(U, "wardrobe"),
             "accept": ["wardrobe", "Wardrobe", "a wardrobe"], "audio_tts": "wardrobe"},
            {"prompt": "6. Напиши по-английски: полки", "image": img(U, "shelves"),
             "accept": ["shelves", "Shelves"], "audio_tts": "shelves"},
        ]}),

        ("quiz", {"title": "Выбери правильный вариант, чтобы предложение было грамматически верным", "questions": [
            single("My sister ___ thirteen years old.", ["am", "is", "are"], "is"),
            single("They ___ got a friendly dog called Max.", ["are", "has", "have"], "have"),
            single("___ you ride a bike? — Yes, I can.", ["Can", "Do", "Are"], "Can"),
            single("___ two armchairs in the living room.", ["There is", "Are there", "There are"], "There are"),
            single("___ trainers are new. Look!", ["This", "These", "That"], "These"),
        ]}),

        ("gaps", {
            "title": "Поставь слово в скобках в правильную форму. Используй притяжательные "
                     "прилагательные (my, your, his, her, its, our, their) или 's",
            "mode": "type",
            "text": "1. This is __my|My__ new desk. (I)\n"
                    "2. __Her|her__ name is Maria. (She)\n"
                    "3. __Their|their__ house is big and modern. (They)\n"
                    "4. __Anna's|Anna’s__ brother is in my class. (Anna)\n"
                    "5. The cat is sleeping on the __children's|children’s__ bed. (children)",
            "gaps_expected": 5,
        }),

        ("text", {"html": "<h3>Расставь части предложения в правильном порядке</h3>"
                          "<p>В следующих пяти заданиях собери предложения из частей.</p>"}),
        order(["My friend", "has got", "a new", "black", "skateboard."]),
        order(["There are", "two armchairs", "next to", "the window."]),
        order(["Can", "your sister", "play", "the piano?"]),
        order(["My", "cousins", "are", "from", "Argentina."]),
        order(["These", "shoes", "are", "my", "brother’s."]),

        ("text", {"html":
            "<h3>READING</h3><p>Прочитай текст и выбери правильный ответ на каждый вопрос.</p>"
            "<h3>Meet Marta</h3>"
            "<p>Hi! My name's Marta and I'm thirteen years old. I'm from Warsaw, Poland. My mum is Italian, "
            "so I can speak Italian. I can also speak Polish and English. My birthday is in September.</p>"
            "<p>I've got a big family. I've got two brothers, one sister, and a friendly cat called Bruno. "
            "We're a happy family!</p>"
            "<p>My bedroom is my favourite room. There's a desk next to the window and a tall wardrobe in "
            "the corner. My bed is under the shelves and my old armchair is next to the bed.</p>"
            "<p>I love sport. I can swim and ride a bike, but I can't skateboard. My brother Daniel is sporty "
            "too. He's twelve and he can play football very well!</p>"}),
        ("quiz", {"title": "READING. Выбери правильный ответ на каждый вопрос", "questions": [
            single("How old is Marta?", ["12", "13", "14", "15"], "13"),
            single("Why can Marta speak Italian?",
                   ["Her dad is Italian.", "She lives in Italy.", "She learns it at school.", "Her mum is Italian."],
                   "Her mum is Italian."),
            single("Where is the wardrobe?",
                   ["In the corner", "Next to the window", "Under the shelves", "Next to the bed"],
                   "In the corner"),
            single("Where is Marta's bed?",
                   ["Next to the window", "In the corner", "Under the shelves", "Next to the wardrobe"],
                   "Under the shelves"),
            single("What CAN'T Marta do?", ["Swim", "Ride a bike", "Skateboard", "Play football"], "Skateboard"),
        ]}),

        todo(("video", {"title": "Послушай, как три подростка рассказывают о себе на видеозвонке",
                        "url": "", "provider": "file"}),
             ("audio", "аудио «видеозвонок трёх подростков: Tom, Léa, Aylin» к следующему заданию")),
        ("sort", {"title": "Послушай запись ещё раз и соедини каждого подростка с двумя фактами о нём", "groups": [
            {"name": "Tom", "items": [{"text": "is from Manchester, the UK"}, {"text": "can play tennis"}]},
            {"name": "Léa", "items": [{"text": "has no brothers or sisters"}, {"text": "plays the guitar"}]},
            {"name": "Aylin", "items": [{"text": "loves cooking"}, {"text": "has a red hoodie"}]},
        ]}),

        ("speaking", {"title": "SPEAKING I 🎤", "needs_review": True, "image": img(U, "scene_bedroom"),
                      "html": "<p>Опиши картинку и ответь на вопросы. Нажми на микрофон и запиши ответ.</p>"
                              "<ol><li>What can you see in the room?</li><li>Where is the boy?</li>"
                              "<li>Where is his bag?</li><li>What has he got on his shelves?</li>"
                              "<li>Can the boy play the guitar?</li></ol>"}),
        ("speaking", {"title": "SPEAKING II 🎤", "needs_review": True,
                      "html": "<p>Ответь на вопросы полными предложениями. Нажми на микрофон и запиши ответ.</p>"
                              "<ol><li>What's your name? How old are you?</li><li>Where are you from?</li>"
                              "<li>Have you got a pet?</li><li>Can you swim?</li>"
                              "<li>What's your favourite room in your house?</li>"
                              "<li>What is there in your bedroom?</li></ol>"}),

        ("text", {"html":
            f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
            "<h3>Тест пройден! 🎉</h3><p>Ты отлично вспомнил прошлый год. Теперь — вперёд, к Unit 1!</p>"}),
    ]},
}
