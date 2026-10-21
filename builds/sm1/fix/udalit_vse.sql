-- SM1 · все блоки на удаление после вычитки — один скрипт вместо одиннадцати
-- Запускать в Supabase → SQL Editor целиком. Всего удаляется 59 блоков.
--
-- Что удаляется: остатки фоники, полные дубли блоков, рекламные баннеры,
-- задания, замененные новыми. Копии всех затронутых юнитов до правок лежат
-- в таблицах classroom_backup_sm1_fix_u0_20261021 … _u10_20261021 —
-- любой блок можно вернуть оттуда.
--
-- После удаления скрипт сам выравнивает нумерацию блоков в задетых уроках.

begin;

create temporary table zatronutye_uroki_sm1 on commit drop as
select distinct lesson_id from classroom_blocks where id in ('0c5031ef-6098-4fa9-8424-6d4684e6e6b9', '6436d0c3-1888-4def-8450-6c7bed525418', '36aa365e-b364-4699-83ee-2da3e86474a2', '6d322769-b435-4220-9704-1d3a308e16f6', '2bbd0908-e12f-4e7e-8d65-691d9bd8bde5', '56408011-e824-4d08-a6e9-53f31314b98e', 'f6344408-8f6d-48ee-94b1-51267fa95234', '87990160-7971-4935-968a-fc303151908a', '6f4c737a-e95d-4f60-945c-fdbc2a2d9fd6', '727b1f7a-cc74-4c1d-9794-690061d80bb8', '983d7c89-02fe-4ebd-86cd-a872501a7144', 'ff83901c-ca47-4c2a-a6ba-01135d5ec5dc', '9f8b95c0-f4fb-4e11-830f-8743c2c6ed3e', 'd88ee1c8-fc40-47bc-868a-ccb8f0757842', 'eb5e4288-24eb-46b7-b86c-55aec9e34273', '903263a1-c286-44c9-876e-ae985db0c408', '1233a146-7fa4-4cc9-a76e-eded971caecc', 'ab0f48ca-23af-4c8c-afc9-6620bdbdfd87', '8f7c279d-8d2c-44a8-8058-3a500bab6340', 'ba5470bb-6905-4aa1-973f-d49c313b0424', 'ba5e41e6-5c8a-4ffd-b46e-faed4217206e', '54b38a0b-4323-4181-9db8-31e2123ae745', '86359964-eac5-4fd2-b279-e2a4bb4bfb3c', '8c52bc7f-ce30-4db8-af4f-3c14af567bd5', 'ca74cd17-f866-4d41-b2c9-1d1afd4162a3', '2abd9de9-0096-44af-91b6-b5664fbd5432', '54f9c9a9-437d-4c3e-81cf-28600764d6b2', '19a9c799-fa1f-410d-b576-b30f1b739a73', '26049fcb-e245-4fce-9aa0-57780d9b49a5', '5e4f7ae2-a4f3-4da0-ba82-14c9052a364a', 'f1ba0328-5714-44a3-a36f-3b896beb0530', 'd65feea7-0b66-4209-a578-19cf4485f2a4', '8c0708ef-f936-4d4c-9cc0-a9562d34a81b', 'f6b46847-bbac-4442-9e95-2f4abf51873f', '6df6d031-eb4f-4b6e-a527-a5ec7e7c3b22', '329d6515-4489-4a2c-9348-97e806f345b5', '63def77f-ca2b-4c8f-a045-71d89aeaef81', '66c2e933-c4c3-4216-948d-11a07bf71491', '851a19a5-9d79-4c39-aec1-176003f52a6e', 'c6fec3c6-85d1-442b-a4cb-caddd8105406', '6ed74b16-2ce7-44e9-9ebd-2fbf2d7ba442', '89cbeceb-1348-4455-87f3-6156fb1512ea', 'c9b0ffa2-d747-47e0-8bca-1acf4cb40394', 'bd69f418-ef84-4eee-ad7c-c1f6727f4e2e', 'a1142212-00ab-4876-8a73-192ec3480c40', '891c24c3-b5d8-4abe-894c-53490fc397f5', '28b2149b-d63d-4bdd-9961-30dba2e91679', 'a2b6bed6-9427-4481-9e29-97dfe4cd3396', '734b9ca3-4a71-4b5d-9f4a-d4d06884c87e', '2bee98a6-9ccb-470e-9f39-805c3839e6f1', 'de55d72d-a6f8-4240-aa62-21962ead93b5', '4a0e60b8-9dac-4253-b2e0-ac0168774304', 'f61e4ef1-d518-4fd7-a70c-732ecd62aea4', 'e893d9a0-d135-415c-bec1-53ada7ef188f', 'ba3e282d-9894-4245-b461-8d7c3692404f', '51a71093-52c2-42ac-a776-b0b9cc3a96bc', '70534559-df31-4f07-a8d8-a37958aeac20', '299c259a-9575-4271-8bd5-2dbf065e490d', '7451bc62-3f60-4757-81bf-ca2087ccc719');

-- ───── u0 (9) ─────
delete from classroom_blocks where id = '0c5031ef-6098-4fa9-8424-6d4684e6e6b9'; -- юнит 0 · ДЗ 1 · блок 3 · flashcards, полный дубль блока 2
delete from classroom_blocks where id = '6436d0c3-1888-4def-8450-6c7bed525418'; -- юнит 0 · ДЗ 2 · блок 3 · flashcards, полный дубль блока 2
delete from classroom_blocks where id = '36aa365e-b364-4699-83ee-2da3e86474a2'; -- юнит 0 · ДЗ 3 · блок 3 · flashcards, полный дубль блока 2
delete from classroom_blocks where id = '6d322769-b435-4220-9704-1d3a308e16f6'; -- юнит 0 · ДЗ 1 · блок 7 · match, полный дубль блока 6 без звука
delete from classroom_blocks where id = '2bbd0908-e12f-4e7e-8d65-691d9bd8bde5'; -- юнит 0 · ДЗ 3 · блок 9 · match, полный дубль блока 7 без звука
delete from classroom_blocks where id = '56408011-e824-4d08-a6e9-53f31314b98e'; -- юнит 0 · ДЗ 1 · блок 4 · text, фоника Ss/Ii/Tt + дубль карточек
delete from classroom_blocks where id = 'f6344408-8f6d-48ee-94b1-51267fa95234'; -- юнит 0 · ДЗ 3 · блок 4 · text, фоника Mm/Dd/Gg + дубль карточек
delete from classroom_blocks where id = '87990160-7971-4935-968a-fc303151908a'; -- юнит 0 · ДЗ 2 · блок 7 · text, инструкция уехала в заголовок блока «Послушай и выбери, сколько лет герою»
delete from classroom_blocks where id = '6f4c737a-e95d-4f60-945c-fdbc2a2d9fd6'; -- юнит 0 · ДЗ 4 · блок 3 · text, инструкция уехала в заголовок блока «Послушай и выбери, как зовут котика»
-- ───── u1 (6) ─────
delete from classroom_blocks where id = '727b1f7a-cc74-4c1d-9794-690061d80bb8'; -- юнит 1 · ДЗ 1 · блок 4 · фоника: «послушай слово» на pet, net, mum, cup, red, rat
delete from classroom_blocks where id = '983d7c89-02fe-4ebd-86cd-a872501a7144'; -- юнит 1 · ДЗ 2 · блок 3 · фоника: hat, hippo, bed, rabbit, fig, frog
delete from classroom_blocks where id = 'ff83901c-ca47-4c2a-a6ba-01135d5ec5dc'; -- юнит 1 · ДЗ 3 · блок 3 · фоника: doll, bell, jump, jog, van, vet
delete from classroom_blocks where id = '9f8b95c0-f4fb-4e11-830f-8743c2c6ed3e'; -- юнит 1 · ДЗ 4 · блок 3 · фоника: well, west, box, taxi, yell, yes
delete from classroom_blocks where id = 'd88ee1c8-fc40-47bc-868a-ccb8f0757842'; -- юнит 1 · ДЗ 5 · блок 2 · текст с карточкой букв Zz/Qq, другого содержания в блоке нет
delete from classroom_blocks where id = 'eb5e4288-24eb-46b7-b86c-55aec9e34273'; -- юнит 1 · ДЗ 5 · блок 3 · фоника: buzz, zigzag, queen, quest
-- ───── u2 (6) ─────
delete from classroom_blocks where id = '903263a1-c286-44c9-876e-ae985db0c408'; -- юнит 2 · ДЗ 1 · блок 12 · «Собери слово: компьютерная игра» — десять слов подряд по одной и той же десятке, длинные слова сняты
delete from classroom_blocks where id = '1233a146-7fa4-4cc9-a76e-eded971caecc'; -- юнит 2 · ДЗ 1 · блок 13 · «Собери слово: картинг» — то же
delete from classroom_blocks where id = 'ab0f48ca-23af-4c8c-afc9-6620bdbdfd87'; -- юнит 2 · ДЗ 1 · блок 15 · «Собери слово: монстр» — то же
delete from classroom_blocks where id = '8f7c279d-8d2c-44a8-8058-3a500bab6340'; -- юнит 2 · ДЗ 1 · блок 16 · «Собери слово: самолет» — то же
delete from classroom_blocks where id = 'ba5470bb-6905-4aa1-973f-d49c313b0424'; -- юнит 2 · ДЗ 2 · блок 13 · quiz «выбери ответ» по тем же шести репликам Kim и Tim: средний из трёх одинаковых заходов (блок 8 — найди пару, блоки 15–20 — собери предложение)
delete from classroom_blocks where id = 'ba5e41e6-5c8a-4ffd-b46e-faed4217206e'; -- юнит 2 · ДЗ 4 · блок 10 · вторая инструкция к тому же заданию («расставь картинки» ↔ «подпиши картинки»), противоречит заголовку hotspot
-- ───── u3 (8) ─────
delete from classroom_blocks where id = '54b38a0b-4323-4181-9db8-31e2123ae745'; -- юнит 3 · ДЗ 2 · блок 3 · quiz «послушай звук» на A_E и Yy (cake/snake/spy/fly)
delete from classroom_blocks where id = '86359964-eac5-4fd2-b279-e2a4bb4bfb3c'; -- юнит 3 · ДЗ 5 · блок 3 · quiz на OI и EAR (coin/hear/oil/near), к тому же по два варианта ответа
delete from classroom_blocks where id = '8c52bc7f-ce30-4db8-af4f-3c14af567bd5'; -- юнит 3 · ДЗ 6 · блок 3 · sort «er или air» (hair/chair/sister/brother)
delete from classroom_blocks where id = 'ca74cd17-f866-4d41-b2c9-1d1afd4162a3'; -- юнит 3 · ДЗ 7 · блок 17 · order «Составь слово: chair», пятый фоничный, замены ему не нашлось; стоит последним, пока не удалён
delete from classroom_blocks where id = '2abd9de9-0096-44af-91b6-b5664fbd5432'; -- юнит 3 · ДЗ 1 · блок 7  · order «Собери слово: слон»
delete from classroom_blocks where id = '54f9c9a9-437d-4c3e-81cf-28600764d6b2'; -- юнит 3 · ДЗ 1 · блок 9  · order «Собери слово: ящерица»
delete from classroom_blocks where id = '19a9c799-fa1f-410d-b576-b30f1b739a73'; -- юнит 3 · ДЗ 1 · блок 11 · order «Собери слово: паук»
delete from classroom_blocks where id = '26049fcb-e245-4fce-9aa0-57780d9b49a5'; -- юнит 3 · ДЗ 1 · блок 15 · order «Собери слово: осел»
-- ───── u4 (6) ─────
delete from classroom_blocks where id = '5e4f7ae2-a4f3-4da0-ba82-14c9052a364a'; -- юнит 4 · ДЗ 4 · блок 3  · match «соедини картинку со словами» — new / screw / cube / flute
delete from classroom_blocks where id = 'f1ba0328-5714-44a3-a36f-3b896beb0530'; -- юнит 4 · ДЗ 5 · блок 3  · quiz «послушай звук» — saw/draw/jaw → straw, how/now/wow → mouse, cloud
delete from classroom_blocks where id = 'd65feea7-0b66-4209-a578-19cf4485f2a4'; -- юнит 4 · ДЗ 6 · блок 3  · sort по звукам |ɪ| heavy/baby, |s| ice/fence, |dʒ| giraffe/orange
delete from classroom_blocks where id = '8c0708ef-f936-4d4c-9cc0-a9562d34a81b'; -- юнит 4 · ДЗ 7 · блок 2  · quiz «выбери слово, в котором есть этот звук» — straw / bone / giraffe
delete from classroom_blocks where id = 'f6b46847-bbac-4442-9e95-2f4abf51873f'; -- юнит 4 · тест · блок 3 · speaking «прочитай вслух» — turtle, crow, rope, cube, cloud, giraffe
delete from classroom_blocks where id = '6df6d031-eb4f-4b6e-a527-a5ec7e7c3b22'; -- юнит 4 · ДЗ 5 · блок 7 · quiz «слово → цифра», десять вопросов, дубль блока 6
-- ───── u5 (7) ─────
delete from classroom_blocks where id = '329d6515-4489-4a2c-9348-97e806f345b5'; -- юнит 5 · ДЗ 1 · блок 7 · дубль блока 6: те же семь слов тем же способом, 14 вопросов подряд; блок 6 пересобран смешанным
delete from classroom_blocks where id = '63def77f-ca2b-4c8f-a045-71d89aeaef81'; -- юнит 5 · ДЗ 1 · блок 11 · «Составь слово: вторник» — из семи блоков подряд оставлены четыре
delete from classroom_blocks where id = '66c2e933-c4c3-4216-948d-11a07bf71491'; -- юнит 5 · ДЗ 1 · блок 13 · «Составь слово: четверг» — то же
delete from classroom_blocks where id = '851a19a5-9d79-4c39-aec1-176003f52a6e'; -- юнит 5 · ДЗ 1 · блок 15 · «Составь слово: суббота» — то же
delete from classroom_blocks where id = 'c6fec3c6-85d1-442b-a4cb-caddd8105406'; -- юнит 5 · ДЗ 2 · блок 3 · рекламный баннер «ИНФОРМАЦИЯ ДЛЯ РОДИТЕЛЕЙ, 3 бесплатных урока»: уцелел от централизованной чистки, в блоке нет текста — только <img>
delete from classroom_blocks where id = '6ed74b16-2ce7-44e9-9ebd-2fbf2d7ba442'; -- юнит 5 · ДЗ 6 · блок 4 · дубль блока 3: та же шестёрка go-слов; на его место встали три задания на I like / I don't like
delete from classroom_blocks where id = '89cbeceb-1348-4455-87f3-6156fb1512ea'; -- юнит 5 · ДЗ 6 · блок 12 · второй прощальный текст подряд; содержимое перенесено в блок 11
-- ───── u6 (9) ─────
delete from classroom_blocks where id = 'c9b0ffa2-d747-47e0-8bca-1acf4cb40394'; -- юнит 6 · ДЗ 1 · блок 6  · quiz «картинка → слово», дословно повторяет match в блоке 5
delete from classroom_blocks where id = 'bd69f418-ef84-4eee-ad7c-c1f6727f4e2e'; -- юнит 6 · ДЗ 1 · блок 10 · order «Собери слово: living room», десять букв без пробела
delete from classroom_blocks where id = 'a1142212-00ab-4876-8a73-192ec3480c40'; -- юнит 6 · ДЗ 1 · блок 11 · order «Собери слово: hall», самое короткое слово юнита
delete from classroom_blocks where id = '891c24c3-b5d8-4abe-894c-53490fc397f5'; -- юнит 6 · ДЗ 1 · блок 12 · order «Собери слово: dining room», та же склейка без пробела
delete from classroom_blocks where id = '28b2149b-d63d-4bdd-9961-30dba2e91679'; -- юнит 6 · ДЗ 1 · блок 14 · order «Собери слово: stairs», слово остаётся в блоках 16 и 17
delete from classroom_blocks where id = 'a2b6bed6-9427-4481-9e29-97dfe4cd3396'; -- юнит 6 · ДЗ 3 · блок 7 · quiz «вставь Is / Are», слит в блок 6
delete from classroom_blocks where id = '734b9ca3-4a71-4b5d-9f4a-d4d06884c87e'; -- юнит 6 · ДЗ 5 · блок 9  · текст «Тебя ждут 5 таких предложений», повторён разделителем в блоке 10
delete from classroom_blocks where id = '2bee98a6-9ccb-470e-9f39-805c3839e6f1'; -- юнит 6 · ДЗ 5 · блок 14 · order «There is a kitchen.», самый короткий из пяти подряд
delete from classroom_blocks where id = 'de55d72d-a6f8-4240-aa62-21962ead93b5'; -- юнит 6 · тест · блок 2 · match «Соедини слова с картинками», выдаёт ответы диктанта
-- ───── u7 (7) ─────
delete from classroom_blocks where id = '4a0e60b8-9dac-4253-b2e0-ac0168774304'; -- юнит 7 · ДЗ 2 · блок 14 · text «А теперь давай расставим слова в правильном порядке…» — дубль разделителя «Теперь соберём предложения 📝» (блок 15)
delete from classroom_blocks where id = 'f61e4ef1-d518-4fd7-a70c-732ecd62aea4'; -- юнит 7 · ДЗ 5 · блок 9 · text «А в следующем упражнении мы с тобой потренируемся…» — дубль разделителя (блок 10)
delete from classroom_blocks where id = 'e893d9a0-d135-415c-bec1-53ada7ef188f'; -- юнит 7 · ДЗ 2 · блок 18 · order «Do you like these shoes?» — то же самое задание в четвёртый раз (и оно же стоит в тесте, блок 6)
delete from classroom_blocks where id = 'ba3e282d-9894-4245-b461-8d7c3692404f'; -- юнит 7 · ДЗ 2 · блок 19 · order «Do you like this cap?» — то же самое задание в пятый раз
delete from classroom_blocks where id = '51a71093-52c2-42ac-a776-b0b9cc3a96bc'; -- юнит 7 · ДЗ 5 · блок 11 · order «Anna is wearing a blue skirt.» — та же конструкция уже отработана в ДЗ 3
delete from classroom_blocks where id = '70534559-df31-4f07-a8d8-a37958aeac20'; -- юнит 7 · ДЗ 5 · блок 15 · order «Is Sam eating a sandwich?» — то же предложение есть в тесте (блок 9)
delete from classroom_blocks where id = '299c259a-9575-4271-8bd5-2dbf065e490d'; -- юнит 7 · ДЗ 5 · блок 16 · order «Is Oscar playing football?» — шестое подряд; заодно уходит мелкая картинка football_ball.webp (204×217)
-- ───── u9 (1) ─────
delete from classroom_blocks where id = '7451bc62-3f60-4757-81bf-ca2087ccc719'; -- юнит 9 · ДЗ 7 · блок 3 · утвердительный Present Continuous (True/False, два варианта); тема урока 7 — лексика, «Let's», «Where's/Where are», на её место поставлены пейзажи и вопросы Where

-- нумерация блоков снова подряд с нуля
with novyy as (
  select b.id, row_number() over (partition by b.lesson_id order by b.sort_order) - 1 as n
  from classroom_blocks b
  where b.lesson_id in (select lesson_id from zatronutye_uroki_sm1))
update classroom_blocks b set sort_order = novyy.n + 1000
from novyy where b.id = novyy.id;

update classroom_blocks set sort_order = sort_order - 1000
where lesson_id in (select lesson_id from zatronutye_uroki_sm1) and sort_order >= 1000;

commit;

-- проверка: должно быть два нуля
select
  (select count(*) from (values ('0c5031ef-6098-4fa9-8424-6d4684e6e6b9'), ('6436d0c3-1888-4def-8450-6c7bed525418'), ('36aa365e-b364-4699-83ee-2da3e86474a2'), ('6d322769-b435-4220-9704-1d3a308e16f6'), ('2bbd0908-e12f-4e7e-8d65-691d9bd8bde5'), ('56408011-e824-4d08-a6e9-53f31314b98e'), ('f6344408-8f6d-48ee-94b1-51267fa95234'), ('87990160-7971-4935-968a-fc303151908a'), ('6f4c737a-e95d-4f60-945c-fdbc2a2d9fd6'), ('727b1f7a-cc74-4c1d-9794-690061d80bb8'), ('983d7c89-02fe-4ebd-86cd-a872501a7144'), ('ff83901c-ca47-4c2a-a6ba-01135d5ec5dc'), ('9f8b95c0-f4fb-4e11-830f-8743c2c6ed3e'), ('d88ee1c8-fc40-47bc-868a-ccb8f0757842'), ('eb5e4288-24eb-46b7-b86c-55aec9e34273'), ('903263a1-c286-44c9-876e-ae985db0c408'), ('1233a146-7fa4-4cc9-a76e-eded971caecc'), ('ab0f48ca-23af-4c8c-afc9-6620bdbdfd87'), ('8f7c279d-8d2c-44a8-8058-3a500bab6340'), ('ba5470bb-6905-4aa1-973f-d49c313b0424'), ('ba5e41e6-5c8a-4ffd-b46e-faed4217206e'), ('54b38a0b-4323-4181-9db8-31e2123ae745'), ('86359964-eac5-4fd2-b279-e2a4bb4bfb3c'), ('8c52bc7f-ce30-4db8-af4f-3c14af567bd5'), ('ca74cd17-f866-4d41-b2c9-1d1afd4162a3'), ('2abd9de9-0096-44af-91b6-b5664fbd5432'), ('54f9c9a9-437d-4c3e-81cf-28600764d6b2'), ('19a9c799-fa1f-410d-b576-b30f1b739a73'), ('26049fcb-e245-4fce-9aa0-57780d9b49a5'), ('5e4f7ae2-a4f3-4da0-ba82-14c9052a364a'), ('f1ba0328-5714-44a3-a36f-3b896beb0530'), ('d65feea7-0b66-4209-a578-19cf4485f2a4'), ('8c0708ef-f936-4d4c-9cc0-a9562d34a81b'), ('f6b46847-bbac-4442-9e95-2f4abf51873f'), ('6df6d031-eb4f-4b6e-a527-a5ec7e7c3b22'), ('329d6515-4489-4a2c-9348-97e806f345b5'), ('63def77f-ca2b-4c8f-a045-71d89aeaef81'), ('66c2e933-c4c3-4216-948d-11a07bf71491'), ('851a19a5-9d79-4c39-aec1-176003f52a6e'), ('c6fec3c6-85d1-442b-a4cb-caddd8105406'), ('6ed74b16-2ce7-44e9-9ebd-2fbf2d7ba442'), ('89cbeceb-1348-4455-87f3-6156fb1512ea'), ('c9b0ffa2-d747-47e0-8bca-1acf4cb40394'), ('bd69f418-ef84-4eee-ad7c-c1f6727f4e2e'), ('a1142212-00ab-4876-8a73-192ec3480c40'), ('891c24c3-b5d8-4abe-894c-53490fc397f5'), ('28b2149b-d63d-4bdd-9961-30dba2e91679'), ('a2b6bed6-9427-4481-9e29-97dfe4cd3396'), ('734b9ca3-4a71-4b5d-9f4a-d4d06884c87e'), ('2bee98a6-9ccb-470e-9f39-805c3839e6f1'), ('de55d72d-a6f8-4240-aa62-21962ead93b5'), ('4a0e60b8-9dac-4253-b2e0-ac0168774304'), ('f61e4ef1-d518-4fd7-a70c-732ecd62aea4'), ('e893d9a0-d135-415c-bec1-53ada7ef188f'), ('ba3e282d-9894-4245-b461-8d7c3692404f'), ('51a71093-52c2-42ac-a776-b0b9cc3a96bc'), ('70534559-df31-4f07-a8d8-a37958aeac20'), ('299c259a-9575-4271-8bd5-2dbf065e490d'), ('7451bc62-3f60-4757-81bf-ca2087ccc719')) v(id)
     where exists (select 1 from classroom_blocks b where b.id = v.id::uuid)) as ostalos_udalyaemyh,
  (select count(*) from (
      select b.lesson_id, count(*) as n, min(b.sort_order) as mn, max(b.sort_order) as mx
      from classroom_courses c
      join classroom_units u on u.course_id = c.id
      join classroom_lessons l on l.unit_id = u.id
      join classroom_blocks b on b.lesson_id = l.id
      where c.slug = 'sm1' group by b.lesson_id) t
    where t.mn <> 0 or t.mx <> t.n - 1) as urokov_s_dyroy;
