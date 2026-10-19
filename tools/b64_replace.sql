-- Замена картинок base64 в блоках на ссылки media/<папка>/legacy/<md5 12>.<ext>.
-- Файлы выкладывает tools/b64_extract.py; имя считается здесь тем же способом
-- (md5 декодированных байтов), так что байты через модель не идут.
-- Запускать ТОЛЬКО после того, как все ссылки отвечают 200.
--
-- Фильтр — в условии цикла: сначала один урок, потом курсами.
-- Резервная копия — один раз, до первого прогона:
--   create table classroom_blocks_backup_b64_20261014 as
--     select * from classroom_blocks where payload::text like '%data:image%';

do $$
declare
  v_media text := 'https://classroom.wowteach.ru/media/';
  r record; m record; t text; n int; total int := 0;
begin
  for r in
    select b.id, b.payload::text as p, coalesce(c.slug, 'wow-dragon-2') as folder
    from classroom_blocks b
    join classroom_lessons l on l.id = b.lesson_id
    join classroom_units u on u.id = l.unit_id
    join classroom_courses c on c.id = u.course_id
    where b.payload::text like '%data:image%'
      and b.lesson_id = 'ab50ef0e-f881-4658-9371-e33624860068'   -- @@ФИЛЬТР@@
  loop
    t := r.p; n := 0;
    -- длинные первыми: короткая строка не должна заменить начало длинной
    for m in
      select mime, b64 from (
        select distinct x[1] as mime, x[2] as b64
        from regexp_matches(r.p, 'data:image/([a-zA-Z0-9+.-]+);base64,([A-Za-z0-9+/=]+)', 'g') x
      ) d order by length(b64) desc
    loop
      t := replace(t, 'data:image/' || m.mime || ';base64,' || m.b64,
                   v_media || r.folder || '/legacy/' || left(md5(decode(m.b64, 'base64')), 12)
                   || '.' || case m.mime when 'jpeg' then 'jpg' when 'svg+xml' then 'svg' else m.mime end);
      n := n + 1;
    end loop;
    if t like '%data:image%' then
      raise exception 'блок %: data:image остался после замены', r.id;
    end if;
    update classroom_blocks set payload = t::jsonb where id = r.id;
    total := total + 1;
  end loop;
  raise notice 'обновлено блоков: %', total;
end $$;
