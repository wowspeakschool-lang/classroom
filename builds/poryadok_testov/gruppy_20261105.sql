-- Однотипные задания в тесте должны идти рядом (замечание Анны 05.11.2026:
-- «вставь пропущенное слово» встречалось дважды — до диктанта и после, одним
-- блоком и разными). Три теста, где задания одного раздела разъехались:
--   SM3 Unit 0 Test — два квиза «Выбери правильный вариант.» сведены в один;
--   GG3 Unit 0 Test — «Jobs» переставлен к остальным vocabulary;
--   GG1 Unit 6 Test — «Прочитай диалог» (vocabulary) переставлен к «Посмотри на часы».
-- Копия — classroom_backup_gruppy_testov_20261105.

do $$
declare
  Lsm3 uuid := '3fee5793-968e-4196-b878-65eab514da46';
  Lgg3 uuid := 'c78d7483-02fc-4da9-aab7-6777206ece34';
  Lgg1 uuid := '5dbafdc6-c32f-4a91-aaad-abb343c22a36';
begin

create table if not exists classroom_backup_gruppy_testov_20261105 as
  select * from classroom_blocks where lesson_id in (Lsm3, Lgg3, Lgg1);

-- SM3 Unit 0 Test: слить два «Выбери правильный вариант.»
update classroom_blocks a set payload = jsonb_set(a.payload, '{questions}',
       (a.payload->'questions') || (select b.payload->'questions' from classroom_blocks b
                                     where b.id = '37acb443-af17-4256-803e-b26e22bb6c3a'))
  where a.id = '48dd6bd5-3b34-4efd-9bf9-519e4a709513';
delete from classroom_blocks where id = '37acb443-af17-4256-803e-b26e22bb6c3a';
update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = Lsm3;
update classroom_blocks t set sort_order = z.rn - 1
  from (select id, row_number() over (order by sort_order) rn
          from classroom_blocks where lesson_id = Lsm3) z
 where t.id = z.id;

-- GG3 Unit 0 Test: «Jobs» (было 9-м) встаёт 7-м, грамматика сдвигается
update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = Lgg3;
update classroom_blocks t set sort_order =
    case t.id
      when 'ed9a28b7-985c-40fe-949a-e57ab03c84f2'::uuid then 6
      when 'da3a848d-d330-49a5-9afb-d24af53090af'::uuid then 7
      when '5d649b01-d2ac-4cfb-9a4c-b853b718cccd'::uuid then 8
      else t.sort_order - 1000 end
 where t.lesson_id = Lgg3 and t.sort_order >= 1000;

-- GG1 Unit 6 Test: «Прочитай диалог» (vocabulary) встаёт сразу за «Посмотри на часы»
update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = Lgg1;
update classroom_blocks t set sort_order =
    case t.id
      when 'b49fe6da-c581-4dea-b08c-d2f8aa08a9a9'::uuid then 3
      when '55528106-7fd0-4c02-92df-5081fb8370f9'::uuid then 4
      when '169316a7-1903-408d-8340-0981428a6e82'::uuid then 5
      when '426d75a7-3ca0-4666-95ed-39b3dc9396ca'::uuid then 6
      else t.sort_order - 1000 end
 where t.lesson_id = Lgg1 and t.sort_order >= 1000;

end $$;
