# GG3 · Unit 2 · Покупки и магазины (shopping; сравнения, too / enough) — разбор выгрузки

Источник: `Go Getter 3 Unit 2 Test.pdf` (14 стр., Drive `1Bnp19NggjJEDXImwUEO6i0mfDdbhTsuE`).
Урок LMS: «Go Getter 3 Unit 2 Test», `kind='test'`, `pass_threshold=90`, `is_published=false`.
Тема/лексика: shopping basket, pay by card, shopping list, greengrocer's, cashier, department store, pay in cash,
carry the shopping, get your change, chemist's, stand in a queue, shopping trolley; грамматика — сравнительная и
превосходная степень, as … as, too / enough.

Словарные картинки в PDF не попали (у слов только плейсхолдер «Определение») — см. общую заметку в `GG3_разбор_u1.md`.
Стр. 12–14 — меню нового задания и галерея фонов (8 картинок 900×506, x411–x419) — шум.

## Тест (один файл)
| № | тип в выгрузке | → блок LMS | содержание |
|---|---|---|---|
| 1 | Найди определение (словарь) | match (`left_image` → фраза) | «Соедини фразу с картинкой:» shopping basket · pay by card · shopping list · greengrocer's · cashier · department store. Картинок нет → генерировать |
| 2 | Заполни пропуски (словарь) | exact_input ×6 (картинка + слово с пропущенными буквами) | «Посмотри на картинку и впиши букву:» pay in cash · carry the shopping · get your change · chemist's · stand in a queue · shopping trolley. Картинок нет → генерировать |
| 3 | Выбери правильный вариант | quiz ×5 (или gaps с вариантами) | «Прочитай предложение и выбери пропущенное слово:» 1) This T-shirt is ___ than that at the department store. — **cheaper** ✔ / more cheap / the cheapest. 2) The shopping bag isn't ___ for all these things. — **big enough** ✔ / too big / big too. 3) The cashier is ___ the one at the baker's. — **as friendly as** ✔ / as friendlier as / not as friendliest as. 4) This sports shop is ___ in our town. — **the most expensive** ✔ / more expensive / the expensivest. 5) The queue is ___, let's come back later. — **too long** ✔ / long enough / the longest |
| 4 | Составь предложение | order | She / is / checking / the price / now. |
| 5 | Составь предложение | order | They / pay / in cash / at the greengrocer's. |
| 6 | Составь предложение | order | This / is / the biggest / department store / in our city. |
| 7 | Составь предложение | order | He / isn't / old enough / to pay / by card. |
| 8 | Составь предложение | order | Carrying / the shopping / is / too heavy / for me. |
| 9 | Запись голоса | speaking (с картинкой) | SPEAKING TASK 1. «Опиши картинку, ответь на вопросы.» 1. What can you see in the shop? 2. What are the people buying? 3. What is the cashier doing? 4. Are people standing in a queue? 5. What items can you name? 6. Is the shop big or small? 7. Is the shopping trolley full or empty? Лимит 05:00. Картинка p10 x390 |
| 10 | Запись голоса | speaking | SPEAKING TASK 2. «Ответь на вопросы (не забудь отвечать полными предложениями).» 1. Do you like shopping? 2. What do you usually buy? 3. Do you use a shopping basket or a shopping trolley? 4. Do you pay in cash or by card? 5. What shops do you have near your home? 6. Which shop is the cheapest in your town? 7. Which shop is the most expensive? 8. Which shop is better – the baker's or the greengrocer's? Лимит 05:00 |

Картинки урока:
- p10 x390, 900×507 — **сток** (векторная иллюстрация): кассирша за кассой с бутылкой воды, пара у кассы — мужчина с тележкой продуктов, женщина с банковской картой; хлеб, молоко в корзине. Люди нарисованные (не фото). Вопросы блока 9 опираются на людей («What is the cashier doing?», «What are the people buying?») → переносим как есть: `img/GG3/u2/test_p10_x390.webp`. 🟥 Можно ли оставлять стоковую картинку с нарисованными людьми (правило «без людей» — про нашу генерацию)? Если нельзя — перерисовать кассу и тележку без людей и заменить вопросы 1–4 на «What is on the counter? What is in the trolley?».

НУЖНЫ КАРТИНКИ:
- блок 1: shopping basket (пластиковая корзинка с продуктами); pay by card (банковская карта у терминала, на экране галочка); shopping list (листок со списком и карандаш); greengrocer's (витрина овощной лавки с ящиками овощей и фруктов, навес); cashier — профессия без человека: касса с лентой, сканер, кассовый аппарат, бейдж «Cashier» на стойке; department store (большое многоэтажное здание универмага с витринами);
- блок 2: pay in cash (купюры и монеты, протянутые к кассе — без руки: на блюдце у кассы); carry the shopping (два полных пакета с покупками); get your change (монеты и чек на блюдце / в лотке кассы); chemist's (фасад аптеки с зелёным крестом); stand in a queue (ряд тележек одна за другой у кассы, стойки с лентой-ограждением); shopping trolley (тележка).
  Отличить «pay in cash» и «get your change»: купюры у кассы — оплата; монеты + чек в лотке — сдача.

Заметки: блок 3 — ключ однозначен. Сток со стр. 10 — единственная картинка теста.

## Сводка картинок юнита
| лист | что внутри (по ячейкам) | сетка | регистр | где используется |
|---|---|---|---|---|
| gg3_u2_shop_a | shopping basket · pay by card · shopping list / greengrocer's · cashier · department store | 3×2 | предмет / фасад | тест, блок 1 |
| gg3_u2_shop_b | pay in cash · carry the shopping · get your change / chemist's · stand in a queue · shopping trolley | 3×2 | предмет / фасад | тест, блок 2 |

Кадры из PDF (`книга`/сток как есть): p10 x390 — сцена у кассы → блок 9 (🟥 люди на стоке).
