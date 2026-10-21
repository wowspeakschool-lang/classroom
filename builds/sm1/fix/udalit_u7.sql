-- SM1 · юнит 7 «Get dressed» · блоки на удаление (запускает Анна в SQL Editor)
-- Копия всех 104 блоков юнита до правок: classroom_backup_sm1_fix_u7_20261021
-- Нумерацию sort_order после удаления не чиню — её выровняет координатор.
-- Номера блоков — как в редакторе на момент 21.10.2026, уже после вставки новых блоков.

-- Два заголовка к одному заданию: старый текст и разделитель, поставленный
-- централизованно 20.10. Остаётся разделитель.
delete from classroom_blocks where id = '4a0e60b8-9dac-4253-b2e0-ac0168774304'; -- юнит 7 · ДЗ 2 · блок 14 · text «А теперь давай расставим слова в правильном порядке…» — дубль разделителя «Теперь соберём предложения 📝» (блок 15)
delete from classroom_blocks where id = 'f61e4ef1-d518-4fd7-a70c-732ecd62aea4'; -- юнит 7 · ДЗ 5 · блок 9 · text «А в следующем упражнении мы с тобой потренируемся…» — дубль разделителя (блок 10)

-- ДЗ 2 была на 11 заданий, из них четыре почти одинаковых «Do you like this/these…?».
-- Остаются два: jacket (this) и jeans (these).
delete from classroom_blocks where id = 'e893d9a0-d135-415c-bec1-53ada7ef188f'; -- юнит 7 · ДЗ 2 · блок 18 · order «Do you like these shoes?» — то же самое задание в четвёртый раз (и оно же стоит в тесте, блок 6)
delete from classroom_blocks where id = 'ba3e282d-9894-4245-b461-8d7c3692404f'; -- юнит 7 · ДЗ 2 · блок 19 · order «Do you like this cap?» — то же самое задание в пятый раз

-- ДЗ 5 была на 13 заданий, из них шесть «Составь предложение» подряд.
-- Остаются три — вопрос, вопрос и утверждение: «What is Bob doing?» (блок 12),
-- «Is Amy riding a bike?» (13), «Emma is watching TV.» (14).
delete from classroom_blocks where id = '51a71093-52c2-42ac-a776-b0b9cc3a96bc'; -- юнит 7 · ДЗ 5 · блок 11 · order «Anna is wearing a blue skirt.» — та же конструкция уже отработана в ДЗ 3
delete from classroom_blocks where id = '70534559-df31-4f07-a8d8-a37958aeac20'; -- юнит 7 · ДЗ 5 · блок 15 · order «Is Sam eating a sandwich?» — то же предложение есть в тесте (блок 9)
delete from classroom_blocks where id = '299c259a-9575-4271-8bd5-2dbf065e490d'; -- юнит 7 · ДЗ 5 · блок 16 · order «Is Oscar playing football?» — шестое подряд; заодно уходит мелкая картинка football_ball.webp (204×217)
