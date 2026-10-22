-- GG2, тесты — удаление текстовых блоков-инструкций (9 штук)
-- Собран 22.10.2026 при вычитке тестов Go Getter 2 (builds/gg_tests/gg2.md).
--
-- Почему удаляются. Решение из брифа: «Заголовков-разделителей в тестах
-- не ставим». Все девять блоков — не содержание, а инструкция, которой
-- место в поле `title` самого задания:
--
--   Unit 0 Test, блок 5   «Расставь части предложения…»  — перед пятью order
--   Unit 1 Test, блок 5   то же
--   Unit 2 Test, блок 4   то же
--   Unit 4 Test, блок 2   «Выбери правильный вариант…»   — перед quiz
--   Unit 4 Test, блок 5   «Расставь части предложения…»  — перед пятью order
--   Unit 8 Test, блок 4   то же
--   Final Test,  блок 1   «DICTATION ✍️ … переведи русское слово»
--   Final Test,  блок 3   «VOCABULARY 📚 Выбери правильный ответ.»
--   Final Test,  блок 5   «GRAMMAR ✏️ Выбери правильный ответ.»
--
-- Инструкции уже перенесены в заголовки заданий миграциями
-- gg2_test_order_titles_i_porog, gg2_test_quiz_zagolovki и
-- gg2_test_diktant_u5_final, поэтому после удаления ученик
-- ничего не теряет: в Final Test блоки 4 и 6 и так назывались
-- «VOCABULARY. Выбери правильный ответ» и «GRAMMAR. Выбери правильный ответ» —
-- инструкция шла дважды подряд.
--
-- Копии блоков лежат в classroom_backup_gg_tests_20261022 (все 145 блоков тестов).
-- Скрипт идемпотентен: повторный запуск ничего не сломает.
-- Запускать в SQL Editor целиком, одним куском.

begin;

create temporary table udalyaem_gg2 (id uuid) on commit drop;
insert into udalyaem_gg2 (id) values
  ('4abf945b-ff3d-4035-8697-40ed5d328722'::uuid),  -- Unit 0 Test, блок 5
  ('3929123c-38d2-4a1e-b8a9-876d56056de9'::uuid),  -- Unit 1 Test, блок 5
  ('4e66bb8e-f80d-457d-8030-6eae52a58a75'::uuid),  -- Unit 2 Test, блок 4
  ('425a605d-b2c7-4790-a714-af37476ad571'::uuid),  -- Unit 4 Test, блок 2
  ('9f540d79-5bf6-456d-a1f0-88bc5a16a019'::uuid),  -- Unit 4 Test, блок 5
  ('0ae940d9-80dc-4185-8182-816b14bc3144'::uuid),  -- Unit 8 Test, блок 4
  ('5d381331-0cd5-4bfc-9073-60035e408965'::uuid),  -- Final Test, блок 1
  ('1021e7b2-b796-43a9-bf97-33e9495df052'::uuid),  -- Final Test, блок 3
  ('d1484fad-d54d-4f58-b888-e30122f9a97f'::uuid);  -- Final Test, блок 5

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

-- Проверка после запуска: обе цифры должны быть 0, а список уроков —
-- показать новое число блоков (17→16, 16→15, 15→14, 15→13, 15→14, 12→9).
select
  (select count(*) from classroom_blocks where id in (
     '4abf945b-ff3d-4035-8697-40ed5d328722','3929123c-38d2-4a1e-b8a9-876d56056de9',
     '4e66bb8e-f80d-457d-8030-6eae52a58a75','425a605d-b2c7-4790-a714-af37476ad571',
     '9f540d79-5bf6-456d-a1f0-88bc5a16a019','0ae940d9-80dc-4185-8182-816b14bc3144',
     '5d381331-0cd5-4bfc-9073-60035e408965','1021e7b2-b796-43a9-bf97-33e9495df052',
     'd1484fad-d54d-4f58-b888-e30122f9a97f')) as ostalos_udalyaemyh,
  (select count(*) from (
     select b.lesson_id, b.sort_order, count(*)
     from classroom_courses c
     join classroom_units u on u.course_id = c.id
     join classroom_lessons l on l.unit_id = u.id
     join classroom_blocks b on b.lesson_id = l.id
     where c.slug = 'gg2' and l.kind = 'test'
     group by 1, 2 having count(*) > 1) d) as dubli_sort_order;

select u.sort_order as unit, l.title, count(*) as blokov,
       max(b.sort_order) + 1 as max_nomer
from classroom_courses c
join classroom_units u on u.course_id = c.id
join classroom_lessons l on l.unit_id = u.id
join classroom_blocks b on b.lesson_id = l.id
where c.slug = 'gg2' and l.kind = 'test'
group by 1, 2 order by 1;
