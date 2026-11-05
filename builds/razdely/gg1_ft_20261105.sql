-- Подписи разделов отдельным блоком убираем (решение Анны 05.11.2026:
-- «мне вообще не нравится, что такие подписи отдельным блоком идут… да вообще
-- можно убрать. Главное, чтобы было разделение для преподавателя»).
-- Разделение у преподавателя остаётся: у каждого задания теста стоит skill.
--
-- GG1 Final Test: блок 4 «READING AND WRITING» — единственный такой блок во всех
-- курсах. Плюс из приветствия (блок 1) убирается слово LISTENING: оно было
-- подписью к разделу, который после правки порядка заданий уехал в конец.

do $$
declare L uuid := 'e7ace143-b17e-4797-b28f-6d8a30b944e9';
begin
  create table if not exists classroom_backup_razdely_podpisi_20261105 as
    select * from classroom_blocks where lesson_id = L;

  update classroom_blocks
     set payload = jsonb_set(payload, '{html}',
         to_jsonb(regexp_replace(payload->>'html', '<p[^>]*>\s*<strong>\s*LISTENING\s*</strong>\s*</p>', '', 'gi')))
   where lesson_id = L and sort_order = 0;

  update classroom_blocks
     set payload = jsonb_set(payload, '{html}',
         to_jsonb(regexp_replace(payload->>'html', 'LISTENING', '', 'g')))
   where lesson_id = L and sort_order = 0 and payload->>'html' like '%LISTENING%';

  delete from classroom_blocks where id = '8e21e49f-c578-4e99-a0ae-cbcc90885a94';

  update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = L;
  update classroom_blocks t set sort_order = z.rn - 1
    from (select id, row_number() over (order by sort_order) rn
            from classroom_blocks where lesson_id = L) z
   where t.id = z.id;
end $$;
