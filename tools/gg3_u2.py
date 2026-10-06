"""GG3 · Unit 2 · Shopping — тест. Источник: docs/GG3_разбор_u2.md."""
from gg3_kit import unit, gimg, match_block, letters_block, q, quiz_block, order_block, speaking

U = "u2"
UNIT = unit(2, "Unit 2")

LESSONS = {
    "u2_test": {**UNIT, "lesson_title": "Unit 2 Test", "lesson_sort": 0, "kind": "test", "blocks": [
        # 1
        match_block(U, [("basket", "shopping basket"), ("pay_card", "pay by card"),
                        ("list", "shopping list"), ("greengrocers", "greengrocer's"),
                        ("cashier", "cashier"), ("department_store", "department store")]),
        # 2
        letters_block(U, [("pay_cash", "pay in cash"), ("carry_shopping", "carry the shopping"),
                          ("get_change", "get your change"), ("chemists", "chemist's"),
                          ("queue", "stand in a queue"), ("trolley", "shopping trolley")]),
        # 3
        quiz_block([
            q("This T-shirt is ___ than that at the department store.",
              ["more cheap", "cheaper", "the cheapest"], 1),
            q("The shopping bag isn't ___ for all these things.", ["big enough", "too big", "big too"], 0),
            q("The cashier is ___ the one at the baker's.",
              ["as friendlier as", "not as friendliest as", "as friendly as"], 2),
            q("This sports shop is ___ in our town.",
              ["more expensive", "the most expensive", "the expensivest"], 1),
            q("The queue is ___, let's come back later.", ["long enough", "the longest", "too long"], 2),
        ]),
        # 4–8
        order_block("She", "is", "checking", "the price", "now."),
        order_block("They", "pay", "in cash", "at the greengrocer's."),
        order_block("This", "is", "the biggest", "department store", "in our city."),
        order_block("He", "isn't", "old enough", "to pay", "by card."),
        order_block("Carrying", "the shopping", "is", "too heavy", "for me."),
        # 9–10
        speaking("SPEAKING TASK 1 🎤", "Опиши картинку, ответь на вопросы.", [
            "What can you see in the shop?",
            "What are the people buying?",
            "What is the cashier doing?",
            "Are people standing in a queue?",
            "What items can you name?",
            "Is the shop big or small?",
            "Is the shopping trolley full or empty?"], image=gimg(U, "scene_shop")),
        speaking("SPEAKING TASK 2 🎤", "Ответь на вопросы (не забудь отвечать полными предложениями).", [
            "Do you like shopping?",
            "What do you usually buy?",
            "Do you use a shopping basket or a shopping trolley?",
            "Do you pay in cash or by card?",
            "What shops do you have near your home?",
            "Which shop is the cheapest in your town?",
            "Which shop is the most expensive?",
            "Which shop is better – the baker's or the greengrocer's?"]),
    ]},
}
