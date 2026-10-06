"""GG3 · Unit 8 · The future — тест. Источник: docs/GG3_разбор_u8.md."""
from gg2_build import todo
from gg3_kit import unit, gimg, match_block, letters_block, q, quiz_block, order_block, speaking

U = "u8"
UNIT = unit(8, "Unit 8")

LESSONS = {
    "u8_test": {**UNIT, "lesson_title": "Unit 8 Test", "lesson_sort": 0, "kind": "test", "blocks": [
        # 1
        match_block(U, [("be_rich", "be rich"), ("have_family", "have a family"),
                        ("foreign_language", "learn a foreign language"), ("wait_turn", "wait your turn"),
                        ("hug", "give someone a hug"), ("shake_hands", "shake hands")]),
        # 2
        letters_block(U, [("be_doctor", "be a doctor"), ("invite", "invite"), ("learn_drive", "learn to drive"),
                          ("call", "call"), ("arrive_on_time", "arrive on time"), ("be_famous", "be famous")]),
        # 3
        todo(quiz_block([
            q("I think she ___ abroad one day.", ["is going to live", "will live", "lives"], 1),
            q("He ___ a famous singer in the future.", ["will be", "is", "will being"], 0),
            q("___ when I called you last night?",
              ["What did you do", "What are you doing", "What were you doing"], 2),
            q("___ tonight?", ["Where do you go", "Where are you going", "Where were you going"], 1),
            q("___ at the party yesterday?",
              ["When did he arrive", "When does he arrive", "When is he arriving"], 0),
        ]), ("check", "Вопрос 1 «I think she ___ abroad one day»: неверный вариант «is going to live» тоже "
                      "грамматически возможен (ключ will live — по правилу I think + will). Оставлено как в "
                      "выгрузке; при пороге 90% лучше заменить его на «will to live»")),
        # 4–8
        order_block("She", "will", "learn", "a foreign language", "in the future."),
        order_block("They", "are", "visiting", "their grandparents", "tomorrow."),
        order_block("When", "will", "you", "arrive", "at the cinema?"),
        order_block("He", "is", "going", "to", "have", "his own business", "one day."),
        order_block("Why", "are", "you", "asking", "for permission?"),
        # 9–10
        speaking("SPEAKING TASK 1 🎤", "Опиши картинку, ответь на вопросы.", [
            "How are the boys greeting each other?",
            "Are they polite?",
            "What will they do next?",
            "Do they look happy?",
            "When do you usually hug your friends?"], image=gimg(U, "scene_greeting"), ordered=False),
        speaking("SPEAKING TASK 2 🎤", "Ответь на вопросы (не забудь отвечать полными предложениями).", [
            "Will you live abroad one day?",
            "What foreign language do you want to learn?",
            "Do you want to have your own business?",
            "Are you going to call anyone today?",
            "Who do you usually hug?",
            "Do you always arrive on time?",
            "What should people do to be polite?",
            "What did you do yesterday evening?",
            "What were you doing at six o'clock yesterday?",
            "Where are you going this weekend?"]),
    ]},
}
