# -*- coding: utf-8 -*-
# Добавление образца туда, где его не было совсем (решение Анны 12.11.2026).
# Тесты не трогаем. Там, где фраза уже выдана в задании («скажи: Hello! I'm …»),
# шаблон есть или стоит отсылка к соседнему аудио, — тоже не трогаем.

# 1. Пример текстом в теле задания — курсы, где дети читают.
TEKSTOM = {
 "41c3cb51-20ee-450c-a832-2545039e6cbc": "Пример: Can I see your room? — Yes, of course. Come in!",
 "f7441bce-1eaf-4b11-8d3d-e89198f0fa01": "Пример: There are five rooms in my house. My favourite room is the kitchen.",
 "56f37a23-6e0d-4dc1-891b-42448ff5c4cf": "Пример: Yes, I have. I've got a cat. No, she hasn't.",
 "f2bc369a-f1b7-474f-a596-dab054663715": "Пример: Oh no! I'm sorry, Mum.",
 "23642479-71af-4c3a-aadb-c63abb32e552": "Пример: My favourite character is Masha. She's got long brown hair.",
 "8478e7cc-5581-4590-9d44-0ca07a3969a4": "Пример: Yes, I do. My cat eats fish. No, they don't.",
 "e1175113-e7b7-407f-b15b-47f650613899": "Пример: thirty-five, twelve…",
 "5f7da51e-8b2a-40f3-b9d4-6040866e1b2d": "For example: There is a table. There aren't any chairs.",
 "460cdb4a-2f78-4c99-8954-4d431af391e6": "For example: I'm in the castle. I feel scared.",
}
# 2. Готовый пример в теле заменить (он слово в слово описывал картинку = выдавал ответ).
ZAMENIT = {
 "408e8e5a-7362-4a31-933f-1b34c48918c9": "There is a cat on the chair. There are two books on the table.",
}
# 3. Образец записью — SM0 и SM1, там дети ещё не читают.
ZVUKOM = {
 "73666aea-a527-4d73-bd84-0777ef1a6bf6": "Red and blue.",
 "ce10a8e2-d829-446d-a560-2bbde8168b8b": "Three cars.",
 "a511cc8c-bffa-49c9-acbe-0b63bef8b842": "Four cats.",
 "f160db63-42b3-4f4b-a306-a93f49933ff5": "Two dogs.",
 "f2db20a3-057e-4b5e-b101-48f30ef796d9": "My nose.",
 "9720ec40-0071-4a60-8b11-a2dcdcc0cb32": "How many legs?",
 "f0bb58ca-e8d6-4a8c-bba0-cbb9522a8da3": "Mum and dad.",
 "3a4a3262-5568-439a-bd22-c8d7b22fae0d": "Mum and dad.",
 "f374f436-bd32-4397-8e8d-80250d38d2df": "A doctor.",
 "b37f3d58-440c-4154-9ae5-a686448f1aa5": "A doctor.",
 "cd8ec437-b7e9-4238-9fb5-34030749b09c": "Swimming.",
 "db524f54-8215-4d91-ba98-45e247e44e38": "Swimming.",
 "d63608d4-2782-4152-9941-65f4649871a5": "What's your name?",
 "3ba7e614-865c-4470-ab51-a2d5ea6d7979": "The cat is under the table. The books are on the chair.",
}
