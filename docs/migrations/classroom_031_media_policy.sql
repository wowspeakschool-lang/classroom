-- ============================================================
-- 031. Бакет classroom-media: закрыть запись для учеников
--
-- Было: политика classroom_media_write разрешала INSERT любому
-- залогиненному пользователю без проверки роли. Ученик мог залить
-- в бакет что угодно и сколько угодно.
--
-- Снести её нельзя: через неё же уходят записи голоса учеников
-- (типы speaking и task с устным ответом). Поэтому не убираем
-- право, а сужаем — ученик пишет только в свою папку.
--
-- ТРЕБУЕТ обновлённого index.html: записи учеников должны уходить
-- в submissions/<uid>/. Старый файл кладёт их в uploads/ и после
-- этой миграции получит отказ. Сначала сайт, потом SQL.
-- ============================================================

-- ---------- 1. Что стоит сейчас ----------
select policyname, cmd, roles,
       coalesce(qual::text, with_check::text) as условие
  from pg_policies
 where schemaname='storage' and tablename='objects'
   and policyname like 'classroom_media%'
 order by policyname;

-- ---------- 2. Замена ----------
-- Дубль чтения: classroom_media_read и classroom_media_select
-- делают одно и то же. Оставляем один.
drop policy if exists classroom_media_select on storage.objects;

-- Широкая запись уходит
drop policy if exists classroom_media_write on storage.objects;

-- Редактор пишет куда угодно (эта политика уже есть, пересоздаём
-- для определённости — вдруг её правили руками)
drop policy if exists classroom_media_insert on storage.objects;
create policy classroom_media_insert on storage.objects
  for insert to authenticated
  with check ( bucket_id = 'classroom-media' and classroom_is_editor() );

-- Ученик пишет только в submissions/<свой uid>/
create policy classroom_media_student_write on storage.objects
  for insert to authenticated
  with check (
    bucket_id = 'classroom-media'
    and (storage.foldername(name))[1] = 'submissions'
    and (storage.foldername(name))[2] = (auth.uid())::text
  );

-- ---------- 3. Проверка ----------
select policyname, cmd, roles,
       coalesce(qual::text, with_check::text) as условие
  from pg_policies
 where schemaname='storage' and tablename='objects'
   and policyname like 'classroom_media%'
 order by policyname;
