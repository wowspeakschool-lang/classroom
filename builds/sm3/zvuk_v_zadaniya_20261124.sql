-- SM3: три блока, где аудио стояло видео-блоком, — звук переезжает в сами задания.
-- Решение Анны 24.11.2026 («223 да»). Копий учеников у этих уроков нет.
do $$
declare
  l3 uuid := '978ef474-602c-44ac-9501-ab7a1ee6a0fa';
  l4 uuid := 'a0115c7e-fa7b-4f56-8f95-cafb19d91ddb';
  l9 uuid := 'ad9697f1-a008-4c60-82c7-cf313a9173f8';
  u3 text := 'https://api.wowteach.ru/storage/v1/object/public/classroom-media/sm3/sm3_u3_hw3_b2.mp3';
  u4 text := 'https://api.wowteach.ru/storage/v1/object/public/classroom-media/sm3/sm3_u4_hw3_b2.mp3';
  u9 text := 'https://api.wowteach.ru/storage/v1/object/public/classroom-media/sm3/sm3_u9_hw2_b7.mp3';
begin
  create table if not exists classroom_backup_sm3_zvuk_zadanij_20261124 as
  select * from classroom_blocks where lesson_id in (l3, l4, l9);

  update classroom_blocks set payload = jsonb_set(payload, '{audio}', to_jsonb(u3))
   where lesson_id = l3 and sort_order in (2, 3);
  update classroom_blocks
     set payload = jsonb_set(payload, '{title}', to_jsonb(
         replace(payload->>'title', 'Послушай песню ещё раз', 'Послушай песню')))
   where lesson_id = l3 and sort_order = 2;
  delete from classroom_blocks where lesson_id = l3 and sort_order = 1;

  update classroom_blocks set payload = jsonb_set(payload, '{audio}', to_jsonb(u4))
   where lesson_id = l4 and sort_order = 2;
  update classroom_blocks
     set payload = jsonb_set(payload, '{title}', to_jsonb(
         replace(payload->>'title', 'Послушай песню ещё раз', 'Послушай песню')))
   where lesson_id = l4 and sort_order = 2;
  delete from classroom_blocks where lesson_id = l4 and sort_order = 1;

  update classroom_blocks set payload = jsonb_set(payload, '{audio}', to_jsonb(u9))
   where lesson_id = l9 and sort_order in (4, 6);
  delete from classroom_blocks where lesson_id = l9 and sort_order = 5;

  update classroom_blocks set sort_order = sort_order + 1000 where lesson_id in (l3, l4, l9);
  with n as (select id, lesson_id, row_number() over (partition by lesson_id order by sort_order) - 1 pos
             from classroom_blocks where lesson_id in (l3, l4, l9))
  update classroom_blocks b set sort_order = n.pos from n where n.id = b.id;
end $$;
