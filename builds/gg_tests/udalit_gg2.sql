-- GG2, тесты — удаление лишних блоков (11 штук)
-- Собран 22.10.2026 при вычитке тестов Go Getter 2 (builds/gg_tests/gg2.md).
--
-- Номера блоков — как сейчас в редакторе платформы, то есть УЖЕ ПОСЛЕ того,
-- как в восьми тестах первым блоком встало приветствие.
--
-- 1. Девять текстовых блоков-инструкций. Решение из брифа: «Заголовков-
--    разделителей в тестах не ставим». Это не содержание, а инструкция,
--    которой место в поле `title` самого задания:
--
--      Unit 0 Test, блок 5   «Расставь части предложения…»  — перед пятью order
--      Unit 1 Test, блок 5   то же
--      Unit 2 Test, блок 5   то же
--      Unit 4 Test, блок 3   «Выбери правильный вариант…»   — перед quiz
--      Unit 4 Test, блок 6   «Расставь части предложения…»  — перед пятью order
--      Unit 8 Test, блок 5   то же
--      Final Test,  блок 2   «DICTATION ✍️ … переведи русское слово»
--      Final Test,  блок 4   «VOCABULARY 📚 Выбери правильный ответ.»
--      Final Test,  блок 6   «GRAMMAR ✏️ Выбери правильный ответ.»
--
--    Инструкции уже перенесены в заголовки заданий миграциями
--    gg2_test_order_titles_i_porog, gg2_test_quiz_zagolovki и
--    gg2_test_diktant_u5_final, поэтому после удаления ученик ничего
--    не теряет. В Final Test блоки 4 и 6 и так дублировали заголовки
--    следующих за ними блоков слово в слово.
--
-- 2. Два лишних прощания. В Unit 0 и Unit 1 прощание уже было, и миграция
--    gg2_test_privetstvie_i_proshanie добавила второе. Остаётся прежнее
--    (его текст приведён к общему виду), дубль в самом конце удаляется:
--
--      Unit 0 Test, блок 18
--      Unit 1 Test, блок 17
--
-- Копии всех блоков тестов — в classroom_backup_gg_tests_20261022.
-- Скрипт идемпотентен: повторный запуск ничего не сломает.
-- Запускать в SQL Editor целиком, одним куском.

begin;

create temporary table udalyaem_gg2 (id uuid) on commit drop;
insert into udalyaem_gg2 (id) values
  ('4abf945b-ff3d-4035-8697-40ed5d328722'::uuid),  -- Unit 0 Test, блок 5
  ('ea11006f-06fe-4240-aac1-6a8a73876db2'::uuid),  -- Unit 0 Test, блок 18 (дубль прощания)
  ('3929123c-38d2-4a1e-b8a9-876d56056de9'::uuid),  -- Unit 1 Test, блок 5
  ('c0c345fa-426c-4cd1-b38b-681cea1a9040'::uuid),  -- Unit 1 Test, блок 17 (дубль прощания)
  ('4e66bb8e-f80d-457d-8030-6eae52a58a75'::uuid),  -- Unit 2 Test, блок 5
  ('425a605d-b2c7-4790-a714-af37476ad571'::uuid),  -- Unit 4 Test, блок 3
  ('9f540d79-5bf6-456d-a1f0-88bc5a16a019'::uuid),  -- Unit 4 Test, блок 6
  ('0ae940d9-80dc-4185-8182-816b14bc3144'::uuid),  -- Unit 8 Test, блок 5
  ('5d381331-0cd5-4bfc-9073-60035e408965'::uuid),  -- Final Test, блок 2
  ('1021e7b2-b796-43a9-bf97-33e9495df052'::uuid),  -- Final Test, блок 4
  ('d1484fad-d54d-4f58-b888-e30122f9a97f'::uuid);  -- Final Test, блок 6

create temporary table zatronutye_uroki_gg2 on commit drop as
select distinct lesson_id from classroom_blocks where id in (select id from udalyaem_gg2);

delete from classroom_blocks where id in (select id from udalyaem_gg2);

-- перенумеровать затронутые уроки без дыр.
-- Два прохода: уникальный ключ (lesson_id, sort_order) не даёт
-- сдвигать номера на месте.
with novyy as (
  select b.id, row_number() over (partition by b.lesson_id order by b.sort_order) - 1 as n
  from classroom_blocks b
  where b.lesson_id in (select lesson_id from zatronutye_uroki_gg2))
update classroom_blocks b set sort_order = novyy.n + 1000
from novyy where b.id = novyy.id;

update classroom_blocks set sort_order = sort_order - 1000
where lesson_id in (select lesson_id from zatronutye_uroki_gg2) and sort_order >= 1000;

commit;

-- Проверка после запуска: обе цифры должны быть 0.
select
  (select count(*) from classroom_blocks where id in (
     '4abf945b-ff3d-4035-8697-40ed5d328722','ea11006f-06fe-4240-aac1-6a8a73876db2',
     '3929123c-38d2-4a1e-b8a9-876d56056de9','c0c345fa-426c-4cd1-b38b-681cea1a9040',
     '4e66bb8e-f80d-457d-8030-6eae52a58a75','425a605d-b2c7-4790-a714-af37476ad571',
     '9f540d79-5bf6-456d-a1f0-88bc5a16a019','0ae940d9-80dc-4185-8182-816b14bc3144',
     '5d381331-0cd5-4bfc-9073-60035e408965','1021e7b2-b796-43a9-bf97-33e9495df052',
     'd1484fad-d54d-4f58-b888-e30122f9a97f')) as ostalos_udalyaemyh,
  (select count(*) from (
     select b.lesson_id, b.sort_order
     from classroom_courses c
     join classroom_units u on u.course_id = c.id
     join classroom_lessons l on l.unit_id = u.id
     join classroom_blocks b on b.lesson_id = l.id
     where c.slug = 'gg2' and l.kind = 'test'
     group by 1, 2 having count(*) > 1) d) as dubli_sort_order;

-- Должно стать: Unit 0 — 16, Unit 1 — 15, Unit 2 — 16, Unit 3 — 16,
-- Unit 4 — 15, Unit 5 — 15, Unit 6 — 16, Unit 7 — 16, Unit 8 — 16,
-- Final Test — 11. И у каждого теста приветствие первым блоком,
-- прощание последним и ровно одно.
select u.sort_order as unit, l.title, count(*) as blokov,
       max(b.sort_order) + 1 as max_nomer,
       count(*) filter (where b.payload->>'html' like '%well_done_trophy%') as proshaniy
from classroom_courses c
join classroom_units u on u.course_id = c.id
join classroom_lessons l on l.unit_id = u.id
join classroom_blocks b on b.lesson_id = l.id
where c.slug = 'gg2' and l.kind = 'test'
group by 1, 2 order by 1;
