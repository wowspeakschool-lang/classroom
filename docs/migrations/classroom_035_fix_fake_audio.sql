-- ============================================================
-- 035. Убрать ссылки-заглушки на несуществующий домен
--
-- В payload попали адреса вида
--   https://ВАШ-ПРОЕКТ.supabase.co/storage/v1/object/public/audio/...
-- Это незаменённая заглушка из шаблона миграции. Домена нет,
-- звук не играет, но поле заполнено — поэтому карточки считаются
-- озвученными и пропускаются пакетной озвучкой.
--
-- Часть 1 только смотрит. Часть 2 чистит.
-- Прогоняй по частям.
-- ============================================================

-- ---------- ЧАСТЬ 1: где вообще такие ссылки ----------
select b.type                       as тип_блока,
       count(*)                     as блоков,
       count(distinct b.lesson_id)  as материалов
  from public.classroom_blocks b
 where b.payload::text like '%ВАШ-ПРОЕКТ%'
 group by b.type
 order by блоков desc;

-- ---------- ЧАСТЬ 2: подробно по карточкам ----------
select u.title as юнит, l.title as материал,
       c->>'text'  as слово,
       c->>'audio' as ссылка
  from public.classroom_blocks b
  join public.classroom_lessons l on l.id = b.lesson_id
  join public.classroom_units   u on u.id = l.unit_id
 cross join lateral jsonb_array_elements(b.payload->'cards') as c
 where b.type = 'flashcards'
   and c->>'audio' like '%ВАШ-ПРОЕКТ%'
 order by u.title, l.title;

-- ============================================================
-- ЧАСТЬ 3: очистка. Прогоняй, только посмотрев части 1 и 2.
--
-- Удаляет ключ audio у карточек, где он ведёт на заглушку.
-- Настоящие ссылки и записи голосом не трогаются.
-- Повторный прогон безопасен.
-- ============================================================

update public.classroom_blocks b
   set payload = jsonb_set(
         b.payload,
         '{cards}',
         (select coalesce(jsonb_agg(
                   case when t.c->>'audio' like '%ВАШ-ПРОЕКТ%'
                        then t.c - 'audio'
                        else t.c end
                   order by t.ord), '[]'::jsonb)
            from jsonb_array_elements(b.payload->'cards')
                 with ordinality as t(c, ord))
       )
 where b.type = 'flashcards'
   and b.payload::text like '%ВАШ-ПРОЕКТ%';

-- ---------- ЧАСТЬ 4: проверка ----------
select 'карточек с заглушкой осталось' as проверка,
       count(*)::text as значение
  from public.classroom_blocks b
 cross join lateral jsonb_array_elements(b.payload->'cards') as c
 where b.type = 'flashcards'
   and c->>'audio' like '%ВАШ-ПРОЕКТ%'
union all
select 'карточек без звука теперь',
       count(*)::text
  from public.classroom_blocks b
 cross join lateral jsonb_array_elements(b.payload->'cards') as c
 where b.type = 'flashcards'
   and coalesce(c->>'text','') <> ''
   and coalesce(c->>'audio','') = ''
union all
select 'заглушки в блоках других типов',
       count(*)::text
  from public.classroom_blocks
 where type <> 'flashcards'
   and payload::text like '%ВАШ-ПРОЕКТ%';
