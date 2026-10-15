-- classroom_quality — учительская часть, шаг 3 (HANDOVER 8.1б):
--   * ⚑ «Ошибка в задании» и сообщение методисту по всей домашке — из просмотра урока
--     учителем и с экрана проверки (таблица classroom_feedback);
--   * «Контроль качества» методиста: сообщения учителей (исправлено / не ошибка,
--     учитель получает ответ), сложные задания (ошибаются от 60%, минимум 5 ответов),
--     сводка по учителям (сколько ждёт проверки и сколько дней самая старая).
-- Накатывать после classroom_freeze_first_answer. Ничего не удаляет.

create table if not exists public.classroom_feedback (
  id uuid primary key default gen_random_uuid(),
  lesson_id uuid not null,
  block_id uuid,                 -- null — сообщение про всю домашку
  item text,                     -- пункт задания, если отмечен
  body text not null,
  context text not null default 'preview' check (context in ('preview', 'review')),
  enrollment_id uuid,            -- если отправлено с проверки конкретного ученика
  author_user_id uuid,
  status text not null default 'open' check (status in ('open', 'fixed', 'not_error')),
  reply text,
  resolved_by uuid,
  resolved_at timestamptz,
  created_at timestamptz not null default now()
);
create index if not exists classroom_feedback_status_idx on public.classroom_feedback (status, created_at);
alter table public.classroom_feedback enable row level security;
do $$
begin
  if not exists (select 1 from pg_policies where tablename = 'classroom_feedback'
                  and policyname = 'classroom_feedback_read') then
    create policy classroom_feedback_read on public.classroom_feedback
      for select using (public.classroom_is_editor() or author_user_id = public.classroom__my_user_id());
  end if;
end $$;

-- Учитель или методист: «здесь ошибка» / сообщение про всю домашку
create or replace function public.classroom_feedback_send(
  p_lesson_id uuid, p_block_id uuid, p_item text, p_body text,
  p_context text default 'preview', p_enrollment_id uuid default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare v_id uuid;
begin
  if not (public.classroom_is_editor() or public.classroom__current_teacher_id() is not null) then
    raise exception 'Писать методисту может только учитель';
  end if;
  if btrim(coalesce(p_body, '')) = '' then raise exception 'Напишите, что не так'; end if;
  insert into public.classroom_feedback (lesson_id, block_id, item, body, context, enrollment_id, author_user_id)
  values (p_lesson_id, p_block_id, nullif(p_item, ''), btrim(p_body),
          case when p_context = 'review' then 'review' else 'preview' end, p_enrollment_id,
          public.classroom__my_user_id())
  returning id into v_id;
  return jsonb_build_object('ok', true, 'id', v_id);
end $$;

-- Список сообщений: методист — все, учитель — свои
create or replace function public.classroom_feedback_list(p_status text default 'open')
returns jsonb language sql stable security definer set search_path = public as $$
  select coalesce(jsonb_agg(jsonb_build_object(
           'id', f.id, 'lesson_id', f.lesson_id, 'block_id', f.block_id, 'item', f.item,
           'body', f.body, 'context', f.context, 'status', f.status, 'reply', f.reply,
           'created_at', f.created_at, 'resolved_at', f.resolved_at,
           'author', u.name,
           'student', (select s.name from public.classroom_enrollments e join public.students s on s.id = e.student_id
                        where e.id = f.enrollment_id),
           'course_slug', c.slug, 'unit_no', un.sort_order, 'lesson_title', l.title,
           'block_no', b.sort_order + 1, 'block_type', b.type,
           'block_title', b.payload->>'title'
         ) order by f.created_at desc), '[]'::jsonb)
    from public.classroom_feedback f
    left join public.users u on u.id = f.author_user_id
    left join public.classroom_lessons l on l.id = f.lesson_id
    left join public.classroom_units un on un.id = l.unit_id
    left join public.classroom_courses c on c.id = un.course_id
    left join public.classroom_blocks b on b.id = f.block_id
   where (p_status = 'all' or (p_status = 'open' and f.status = 'open') or (p_status = 'closed' and f.status <> 'open'))
     and (public.classroom_is_editor() or f.author_user_id = public.classroom__my_user_id());
$$;

-- Методист: «исправлено» / «не ошибка»; учитель получает ответ в колокольчик
create or replace function public.classroom_feedback_resolve(p_id uuid, p_status text, p_reply text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare v_f public.classroom_feedback%rowtype; v_teacher uuid; v_title text;
begin
  if not public.classroom_is_editor() then raise exception 'Отвечать может только методист'; end if;
  if p_status not in ('fixed', 'not_error', 'open') then raise exception 'Неизвестный статус'; end if;
  update public.classroom_feedback
     set status = p_status, reply = nullif(btrim(coalesce(p_reply, '')), ''),
         resolved_by = case when p_status = 'open' then null else public.classroom__my_user_id() end,
         resolved_at = case when p_status = 'open' then null else now() end
   where id = p_id returning * into v_f;
  if not found then raise exception 'Сообщение не найдено'; end if;
  if p_status <> 'open' then
    select t.id into v_teacher from public.teachers t where t.user_id = v_f.author_user_id limit 1;
    select title into v_title from public.classroom_lessons where id = v_f.lesson_id;
    if v_teacher is not null then
      insert into public.classroom_notifications (recipient_kind, recipient_id, kind, title, body, payload)
      values ('teacher', v_teacher, 'info',
              case when p_status = 'fixed' then 'Методист исправил: ' else 'Методист ответил: ' end || coalesce(v_title, ''),
              coalesce(v_f.reply, case when p_status = 'fixed' then 'Исправлено' else 'Не ошибка' end),
              jsonb_build_object('event', 'feedback', 'feedback_id', v_f.id, 'status', p_status, 'lesson_id', v_f.lesson_id));
    end if;
  end if;
  return jsonb_build_object('ok', true);
end $$;

-- Сложные задания: где система ставит «неверно» от p_threshold% ответов.
-- Поправка учителя «на самом деле верно» — главный признак ошибки в ключе.
create or replace function public.classroom_hard_items(p_threshold int default 60, p_min int default 5)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare v_out jsonb;
begin
  if not public.classroom_is_editor() then raise exception 'Только для методиста'; end if;
  with it as (
    select s.block_id, r.key as item, (r.value #>> '{}')::boolean as auto_ok,
           (s.overrides ->> r.key)::boolean as teacher_ok,
           case when jsonb_typeof(s.answers -> r.key) = 'string' then s.answers ->> r.key
                when jsonb_typeof(s.answers -> 'order') = 'array' then s.answers -> 'order' ->> r.key::int
                else (s.answers -> r.key)::text end as ans
      from public.classroom_submissions s
      cross join lateral jsonb_each(case when jsonb_typeof(s.answers -> '__results') = 'object'
                                         then s.answers -> '__results' else '{}'::jsonb end) r
     where s.section_key is null
  ), agg as (
    select block_id, item, count(*) as n,
           count(*) filter (where auto_ok is false) as wrong,
           count(*) filter (where auto_ok is false and teacher_ok is true) as teacher_fixed,
           (select a2.ans from it a2 where a2.block_id = it.block_id and a2.item = it.item and a2.auto_ok is false
             group by a2.ans order by count(*) desc limit 1) as top_wrong
      from it group by block_id, item
  )
  select coalesce(jsonb_agg(jsonb_build_object(
           'block_id', a.block_id, 'item', a.item, 'answers', a.n, 'wrong', a.wrong,
           'rate', round(a.wrong * 100.0 / a.n), 'teacher_fixed', a.teacher_fixed, 'top_wrong', a.top_wrong,
           'lesson_id', l.id, 'lesson_title', l.title, 'unit_no', un.sort_order, 'course_slug', c.slug,
           'block_no', b.sort_order + 1, 'block_type', b.type, 'block_title', b.payload->>'title'
         ) order by a.wrong * 1.0 / a.n desc, a.n desc), '[]'::jsonb)
    into v_out
    from agg a
    join public.classroom_blocks b on b.id = a.block_id
    join public.classroom_lessons l on l.id = b.lesson_id
    join public.classroom_units un on un.id = l.unit_id
    join public.classroom_courses c on c.id = un.course_id
   where a.n >= p_min and a.wrong * 100.0 / a.n >= p_threshold;
  return v_out;
end $$;

-- Сводка по учителям: сколько ждёт проверки, сколько дней самая старая, проверено за неделю
create or replace function public.classroom_teacher_load()
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare v_out jsonb;
begin
  if not public.classroom_is_editor() then raise exception 'Только для методиста'; end if;
  with p as (
    select pr.*, coalesce(
             (select a.assigned_teacher_id from public.classroom_assignments a
               where a.lesson_id = pr.lesson_id and a.target_type = 'student' and a.target_id = e.student_id
                 and a.assigned_teacher_id is not null order by a.assigned_at desc limit 1),
             e.teacher_id) as teacher_id
      from public.classroom_progress pr
      join public.classroom_enrollments e on e.id = pr.enrollment_id
  )
  select coalesce(jsonb_agg(jsonb_build_object(
           'teacher_id', t.id, 'name', t.name,
           'pending', x.pending, 'oldest_at', x.oldest_at, 'reviewed_week', x.reviewed_week
         ) order by x.pending desc, x.oldest_at), '[]'::jsonb)
    into v_out
    from (select teacher_id,
                 count(*) filter (where status = 'submitted') as pending,
                 min(submitted_at) filter (where status = 'submitted') as oldest_at,
                 count(*) filter (where reviewed_at > now() - interval '7 days') as reviewed_week
            from p where teacher_id is not null group by teacher_id) x
    join public.teachers t on t.id = x.teacher_id
   where x.pending > 0 or x.reviewed_week > 0;
  return v_out;
end $$;
