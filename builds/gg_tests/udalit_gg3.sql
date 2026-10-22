-- GG3 — объединение пяти коротких quiz-блоков Unit 1 Test в один и удаление
-- освободившихся блоков. Собрано 22.10.2026 при вычитке тестов Go Getter.
--
-- Зачем. В Unit 1 Test грамматика разложена на ПЯТЬ отдельных блоков «Прочитай
-- предложение и выбери пропущенное слово» — в четырёх из них по одному вопросу,
-- в одном два. Ребёнок видит пять одинаковых рамок с одной строкой в каждой и
-- жмёт «Проверить» пять раз. Во всех остальных тестах курса (юниты 2–8) эта
-- грамматика — один блок на 5 вопросов. Скрипт сводит Unit 1 к тому же виду:
-- шесть вопросов в блоке 3, блоки 4–7 удаляются, тест становится из 15 блоков
-- одиннадцатиблочным, как и соседние.
--
-- Ничего не теряется: все шесть вопросов переезжают в блок 3 в прежнем порядке.
--
-- Скрипт идемпотентен: повторный запуск ничего не сломает (блоков уже нет,
-- payload уже такой). Запускать в SQL Editor целиком, одним куском.
--
-- 🟥 Это НЕ обязательная правка. Если решите оставить пять блоков как есть —
-- просто не запускайте файл, на работу теста это не влияет.

begin;

-- 1. Шесть вопросов собираются в блок 3 (sort_order 2) урока Unit 1 Test.
update classroom_blocks
set payload = jsonb_build_object(
  'title', 'Прочитай предложение и выбери пропущенное слово',
  'questions', $q$[
    {"q": "She ___ the dog now.", "type": "single", "correct": [1],
     "options": [{"text": "feeds"}, {"text": "is feeding"}, {"text": "is feed"}]},
    {"q": "He usually ___ out the washing on Fridays.", "type": "single", "correct": [2],
     "options": [{"text": "is hanging"}, {"text": "hang"}, {"text": "hangs"}]},
    {"q": "___ you ___ your room now? (первый пропуск)", "type": "single", "correct": [0],
     "options": [{"text": "Are"}, {"text": "Do"}, {"text": "Does"}, {"text": "Is"}]},
    {"q": "___ you ___ your room now? (второй пропуск)", "type": "single", "correct": [1],
     "options": [{"text": "vacuums"}, {"text": "vacuuming"}, {"text": "vacuum"}]},
    {"q": "They ___ their beds at the moment.", "type": "single", "correct": [2],
     "options": [{"text": "isn't making"}, {"text": "don't make"}, {"text": "aren't making"}]},
    {"q": "I ___ this homework.", "type": "single", "correct": [1],
     "options": [{"text": "am not understanding"}, {"text": "don't understand"}, {"text": "doesn't understand"}]}
  ]$q$::jsonb)
where id = '1c4ed0a5-08ae-4e26-b472-bc72e2ba4664';

-- 2. Блоки 4–7 (sort_order 3–6) того же урока удаляются.
create temporary table udalyaem_gg3 (id uuid) on commit drop;
insert into udalyaem_gg3 (id) values
  ('6a17bb34-f401-4844-8ad2-13a79d8a7d98'::uuid),   -- блок 4, вопрос про hang out
  ('160b5675-8569-4c57-bf48-86f3b229eb42'::uuid),   -- блок 5, два вопроса про vacuum
  ('e4b3f0bd-c3c3-4665-afd0-d284d3c51fc1'::uuid),   -- блок 6, вопрос про make the beds
  ('c513e35a-30c1-452f-b236-d35fd37f4b9c'::uuid);   -- блок 7, вопрос про understand

create temporary table zatronutye_uroki_gg3 on commit drop as
select distinct lesson_id from classroom_blocks where id in (select id from udalyaem_gg3);

delete from classroom_blocks where id in (select id from udalyaem_gg3);

-- 3. Перенумерация оставшихся блоков урока (через +1000, чтобы не ловить
--    уникальный ключ (lesson_id, sort_order) на промежуточных значениях).
with novyy as (
  select b.id, row_number() over (partition by b.lesson_id order by b.sort_order) - 1 as n
  from classroom_blocks b
  where b.lesson_id in (select lesson_id from zatronutye_uroki_gg3))
update classroom_blocks b set sort_order = novyy.n + 1000
from novyy where b.id = novyy.id;

update classroom_blocks set sort_order = sort_order - 1000
where lesson_id in (select lesson_id from zatronutye_uroki_gg3) and sort_order >= 1000;

commit;

-- Проверка после запуска: ostalos_udalyaemyh = 0, blokov_v_teste = 11,
-- voprosov_v_bloke_3 = 6, dyr_v_numeratsii = 0.
select
  (select count(*) from classroom_blocks where id in (
     '6a17bb34-f401-4844-8ad2-13a79d8a7d98',
     '160b5675-8569-4c57-bf48-86f3b229eb42',
     'e4b3f0bd-c3c3-4665-afd0-d284d3c51fc1',
     'c513e35a-30c1-452f-b236-d35fd37f4b9c')) as ostalos_udalyaemyh,
  (select count(*) from classroom_blocks
     where lesson_id = '87f1ce1e-8300-43d2-82b0-594ff8099a0f') as blokov_v_teste,
  (select jsonb_array_length(payload->'questions') from classroom_blocks
     where id = '1c4ed0a5-08ae-4e26-b472-bc72e2ba4664') as voprosov_v_bloke_3,
  (select count(*) from classroom_blocks
     where lesson_id = '87f1ce1e-8300-43d2-82b0-594ff8099a0f'
       and sort_order <> (select count(*) from classroom_blocks x
                          where x.lesson_id = '87f1ce1e-8300-43d2-82b0-594ff8099a0f'
                            and x.sort_order < classroom_blocks.sort_order)) as dyr_v_numeratsii;
