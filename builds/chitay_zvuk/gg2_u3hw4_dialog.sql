-- GG2 юнит 3 ДЗ 4: подводка «сыграем ситуацию» уходит внутрь блока со сценарием,
-- отдельный блок 12 удаляется, урок перенумеровывается (20.11.2026)
create table if not exists classroom_backup_gg2_u3hw4_dialog_20261120 as
select * from classroom_blocks
where lesson_id = (select lesson_id from classroom_blocks where id='b711d755-3622-4788-ac6b-0c64b80cd17d');

update classroom_blocks set payload = jsonb_set(payload,'{html}',
  to_jsonb('<p>А теперь давай попробуем сыграть ситуацию, похожую на ту, что мы уже изучили. Представь, что ты Елена или Миша. Включи запись и в паузах зачитывай свои реплики (они выделены). Давай попробуем!</p>' || (payload->>'html')))
where id='b711d755-3622-4788-ac6b-0c64b80cd17d'
  and payload->>'html' not like '<p>А теперь давай попробуем сыграть%';

delete from classroom_blocks where id='160bc1d6-b271-44cc-8d8f-18bac02eccbc';

do $$
declare u uuid := (select lesson_id from classroom_blocks where id='b711d755-3622-4788-ac6b-0c64b80cd17d');
        r record; i int := 0;
begin
  update classroom_blocks set sort_order = -1 - sort_order where lesson_id = u;
  for r in select id from classroom_blocks where lesson_id = u order by sort_order desc loop
    update classroom_blocks set sort_order = i where id = r.id; i := i + 1;
  end loop;
end $$;
