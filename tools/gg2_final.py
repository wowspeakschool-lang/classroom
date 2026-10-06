"""Go Getter 2 · Final Test — итоговый тест курса.

Источник содержания — docs/GG2_разбор_final.md. Комикс SPEAKING I — кадр учебника,
берём как есть (Анна: кадры с нарисованными людьми — как есть).
"""
from gg2_build import img, todo, video

U = "final"
UNIT = {"unit": U, "unit_title": "Final Test", "unit_sort": 9}


def q(question, options, correct):
    return {"q": question, "type": "single", "options": [{"text": o} for o in options], "correct": [correct]}


DICTATION = [
    ("wardrobe", "шкаф для одежды"), ("dictionary", "словарь"), ("vegetables", "овощи"),
    ("headphones", "наушники"), ("waterfall", "водопад"), ("museum", "музей"),
    ("builder", "строитель"), ("suitcase", "чемодан"), ("sleepover", "ночёвка"),
    ("dangerous", "опасный"),
]

LESSONS = {
    "final": {**UNIT, "lesson_title": "Final Test", "lesson_sort": 0, "kind": "test", "blocks": [
        ("text", {"html": "<h3>DICTATION ✍️</h3><p>Впиши слова по-английски.</p>"}),
        ("exact_input", {"items": [
            {"prompt": f"Напиши по-английски: {ru}", "accept": [en], "audio_tts": en} for en, ru in DICTATION]}),

        ("text", {"html": "<h3>VOCABULARY 📚</h3><p>Выбери правильный ответ.</p>"}),
        ("quiz", {"title": "VOCABULARY. Выбери правильный ответ", "questions": [
            q("We have P.E. lessons in the school ___.", ["library", "gym", "kitchen", "garden"], 1),
            q("In ___ we learn about countries, cities and maps.", ["Maths", "Music", "Art", "Geography"], 3),
            q("Can I have a ___ of chocolate, please?", ["bar", "bottle", "jar", "cup"], 0),
            q("I download songs to my ___.", ["calculator", "bookcase", "phone", "armchair"], 2),
            q("Etna is a famous ___ in Italy. Look at its lava. It's amazing!",
              ["waterfall", "volcano", "lake", "island"], 1),
            q("We can buy clothes and shoes at the ___.",
              ["post office", "police station", "hospital", "shopping centre"], 3),
            q("A person who helps sick animals is a ___.", ["builder", "chef", "vet", "doctor"], 2),
        ]}),

        ("text", {"html": "<h3>GRAMMAR ✏️</h3><p>Выбери правильный ответ.</p>"}),
        ("quiz", {"title": "GRAMMAR. Выбери правильный ответ", "questions": [
            q("My sister ___ thirteen years old.", ["am", "is", "are"], 1),
            q("I ___ two brothers and one sister.", ["am got", "has got", "have got"], 2),
            q("This is my brother. ___ name is Tom.", ["His", "Her", "Their"], 0),
            q("Anna ___ tennis every Sunday morning.", ["play", "playing", "plays"], 2),
            q("We haven't got ___ milk for breakfast.", ["any", "some", "a"], 0),
            q("How ___ eggs are there in the fridge?", ["much", "many", "a lot"], 1),
            q("Look! The boy ___ a selfie with his phone.", ["take", "takes", "is taking"], 2),
            q("Russia is ___ than Italy.", ["the biggest", "big", "bigger"], 2),
            q("Yesterday my parents ___ at work all day.", ["were", "was", "are"], 0),
            q("Last Saturday I ___ a great film at the cinema.", ["watch", "watches", "watched"], 2),
            q("___ you go to school yesterday?", ["Did", "Do", "Was"], 0),
            q("Tomorrow we ___ a film at the cinema with my friends.",
              ["watch", "are going to watch", "watched"], 1),
        ]}),

        ("text", {"html":
            "<h3>READING 📖</h3><p>Прочитай текст и выбери правильный ответ на каждый вопрос.</p>"
            "<h4>My Best Year</h4>"
            "<p>I'm thirteen years old and last year was the best year of my life. Let me tell you about it.</p>"
            "<p>In September I started a new school in Manchester. At first, I was scared because I didn't know "
            "anyone. But on the first day, I met Lily – she became my best friend! She lives next to my house, so "
            "we walk to school together every morning.</p>"
            "<p>My favourite subject is Geography. Last term, we learned about the longest rivers and the highest "
            "mountains in the world. Our teacher, Mrs Green, is very kind and always makes us laugh.</p>"
            "<p>In July, my family went on holiday to Italy. We visited Rome, ate pizza every day, and I bought "
            "lots of souvenirs. Italy was hotter than England and the food was amazing!</p>"
            "<p>Next year I'm going to study harder because I want to get good marks. I'm also going to do "
            "karate!</p>"}),
        ("quiz", {"title": "READING. Выбери правильный ответ", "questions": [
            q("How old is the writer of the text?", ["12", "13", "14", "15"], 1),
            q("Where is her new school?", ["London", "Rome", "Manchester", "Italy"], 2),
            q("Why was she scared on the first day of school?",
              ["The school was very big.", "She didn't know anyone.", "The teachers were strict.", "She got lost."], 1),
            q("Where does Lily live?",
              ["In Italy.", "Far from the writer.", "Next to the writer's house.", "In the same house as the writer."], 2),
            q("What is the writer's favourite subject?", ["Maths", "English", "History", "Geography"], 3),
            q("What did the family do in Italy?",
              ["They learned Italian.", "They visited Rome and ate pizza.", "They went to the mountains.",
               "They stayed in a hotel for a year."], 1),
            q("What is the writer's plan for next year?",
              ["Change school.", "Study less and watch more TV.", "Study harder and do karate.", "Move to Italy."], 2),
        ]}),

        video("LISTENING 🎧 Послушай разговор Софи с её мамой.",
              "аудио итогового теста: разговор Софи с мамой (библиотека, Том, папа любит путешествовать, "
              "Лили, день рождения папы в понедельник, торговый центр); из выгрузки не выгрузилось"),
        ("truefalse", {"title": "Выбери TRUE (верно) или FALSE (неверно)", "statements": [
            {"text": "Yesterday Sophie was at the library.", "correct": True},
            {"text": "Sophie did her homework with Tom.", "correct": False},
            {"text": "Sophie's dad likes travelling.", "correct": True},
            {"text": "Lily and Sophie are going to have lunch at a restaurant.", "correct": False},
            {"text": "Sophie's dad's birthday is on Monday.", "correct": True},
            {"text": "Sophie is going to walk to the shopping centre.", "correct": False},
        ]}),

        ("speaking", {"title": "SPEAKING I 🎤", "needs_review": True, "image": img(U, "book_tom_surprise"),
                      "html": "<p>Посмотри на 5 картинок и расскажи историю. Используй Past Simple. "
                              "Помогут вопросы ниже. Запиши ответ, нажав на кнопку микрофона (до 5 минут).</p><ol>"
                              "<li>Where was Tom in the first picture? What did he see on his pillow?</li>"
                              "<li>What did the card say? Who was it from?</li>"
                              "<li>Where did Tom go in the afternoon? Who did he take with him?</li>"
                              "<li>What was waiting for Tom at the park? Who was there?</li>"
                              "<li>What did Tom do in the last picture? How did he feel?</li></ol>"}),
        ("speaking", {"title": "SPEAKING II 🎤", "needs_review": True,
                      "html": "<p>Ответь на вопросы полными предложениями. Запиши ответ, нажав на кнопку "
                              "микрофона (до 5 минут).</p><ol>"
                              "<li>Have you got any brothers or sisters?</li>"
                              "<li>What's your favourite school subject? Why do you like it?</li>"
                              "<li>What do you usually have for breakfast? What food don't you like?</li>"
                              "<li>What gadgets have you got? What do you usually use them for?</li>"
                              "<li>What's the most beautiful place in your country? Why?</li>"
                              "<li>Where were you last Saturday afternoon? What did you do there?</li>"
                              "<li>What did you do yesterday after school?</li>"
                              "<li>Where did you go on your last holiday? How did you travel?</li>"
                              "<li>What are you going to do next weekend?</li></ol>"}),
    ]},
}
