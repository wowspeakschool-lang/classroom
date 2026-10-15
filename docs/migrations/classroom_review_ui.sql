-- classroom_review_ui — учительская часть, шаг 1: проверка домашки (HANDOVER 8.1б).
-- Накатывать ПОСЛЕ classroom_submit_review_model. Запускает Анна в SQL Editor.
--
--  * срок переделки: classroom_progress.retake_deadline_at, первый срок не трогаем;
--  * переделка по пунктам: classroom_progress.retake_items {block_id: ["0","2"]} —
--    у этих заданий стираются только отмеченные пункты, остальные ответы остаются;
--  * classroom_retake: обязательный срок + пункты (старая сигнатура удаляется);
--  * classroom_finish_lesson: при повторной отправке сбрасывает retake_items;
--  * classroom_run_meta: на переделке срок — срок переделки; огоньки — по первой сдаче;
--  * classroom_lesson_grade: отдаёт retake_items и retake_deadline_at;
--  * classroom_pending_reviews: шифр (курс, юнит), срок, опоздание, номер попытки.

alter table public.classroom_progress
  add column if not exists retake_items jsonb,
  add column if not exists retake_deadline_at timestamptz;

-- Первая сдача — из истории (submitted_at переписывается при повторной отправке)
create or replace function public.classroom__first_submitted(p public.classroom_progress)
returns timestamptz language sql immutable as $$
  select coalesce(
    (select min((h->>'at')::timestamptz) from jsonb_array_elements(coalesce(p.history, '[]'::jsonb)) h
      where h->>'event' = 'submitted'),
    p.submitted_at);
$$;

-- Задание, у которого можно вернуть отдельные пункты
create or replace function public.classroom__itemized(b public.classroom_blocks)
returns boolean language sql immutable as $$
  select b.type in ('quiz', 'exact_input', 'match', 'gaps', 'truefalse', 'sort')
      or (b.type = 'hotspot' and coalesce(b.payload->>'mode', '') <> 'find');
$$;

-- ── Переделка: целиком, по заданиям или по пунктам; срок обязателен ─────────

drop function if exists public.classroom_retake(uuid, uuid, uuid[], text);

create or replace function public.classroom_retake(
  p_enrollment_id uuid, p_lesson_id uuid, p_deadline timestamptz,
  p_blocks uuid[] default null, p_items jsonb default null, p_note text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_prog public.classroom_progress%rowtype; v_all boolean; v_blocks uuid[]; v_whole uuid[];
  v_items jsonb := '{}'::jsonb; v_req uuid[]; v_old jsonb; v_student uuid; v_title text;
  b public.classroom_blocks; v_keys text[];
begin
  if not public.classroom__can_review(p_enrollment_id) then
    raise exception 'Проверять может только учитель ученика или методист';
  end if;
  if p_deadline is null then raise exception 'Укажите новый срок'; end if;
  if p_deadline < now() then raise exception 'Новый срок уже прошёл'; end if;
  select * into v_prog from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = p_lesson_id for update;
  if not found or v_prog.status not in ('submitted', 'reviewed') then
    raise exception 'Домашка ещё не отправлена';
  end if;

  -- пункты берём только у заданий, где их можно вернуть по отдельности;
  -- у остальных отметка пункта = всё задание
  if jsonb_typeof(p_items) = 'object' then
    for b in select * from public.classroom__lesson_blocks(p_enrollment_id, p_lesson_id) x
              where p_items ? x.id::text and public.classroom__block_counts(x) loop
      if public.classroom__itemized(b) and jsonb_array_length(coalesce(p_items->(b.id::text), '[]'::jsonb)) > 0 then
        v_items := v_items || jsonb_build_object(b.id::text, p_items->(b.id::text));
      end if;
    end loop;
  end if;

  v_req := coalesce(p_blocks, '{}') ||
           coalesce((select array_agg(k::uuid) from jsonb_object_keys(coalesce(
             case when jsonb_typeof(p_items) = 'object' then p_items end, '{}'::jsonb)) k), '{}');
  v_all := cardinality(v_req) = 0;

  select coalesce(array_agg(x.id order by x.sort_order), '{}') into v_blocks
    from public.classroom__lesson_blocks(p_enrollment_id, p_lesson_id) x
   where public.classroom__block_counts(x) and (v_all or x.id = any (v_req));
  if not v_all and cardinality(v_blocks) <> (select count(distinct u) from unnest(v_req) u) then
    raise exception 'Часть выбранных заданий не из этого урока';
  end if;
  select coalesce(array_agg(u), '{}') into v_whole from unnest(v_blocks) u where not (v_items ? u::text);

  select coalesce(jsonb_agg(jsonb_build_object(
           'block_id', s.block_id, 'section_key', s.section_key, 'answers', s.answers,
           'auto_score', s.auto_score, 'overrides', s.overrides, 'teacher_score', s.teacher_score,
           'reviewer_note', s.reviewer_note, 'storage_path', s.storage_path,
           'submitted_at', s.submitted_at)), '[]'::jsonb)
    into v_old
    from public.classroom_submissions s
   where s.enrollment_id = p_enrollment_id and s.block_id = any (v_blocks);

  -- задания целиком: ответы стираются
  delete from public.classroom_grades
   where enrollment_id = p_enrollment_id and block_id = any (v_whole);
  delete from public.classroom_submissions
   where enrollment_id = p_enrollment_id and block_id = any (v_whole);

  -- по пунктам: стираются только отмеченные пункты, остальные ответы остаются
  for b in select * from public.classroom__lesson_blocks(p_enrollment_id, p_lesson_id) x
            where v_items ? x.id::text loop
    select array_agg(k) into v_keys from jsonb_array_elements_text(v_items->(b.id::text)) k;
    update public.classroom_submissions s
       set answers = case when b.type = 'sort'
                          then jsonb_set(s.answers, '{assign}', coalesce(s.answers->'assign', '{}'::jsonb) - v_keys)
                          else s.answers - v_keys end,
           overrides = coalesce(s.overrides, '{}'::jsonb) - v_keys,
           teacher_score = null, review_status = null
     where s.enrollment_id = p_enrollment_id and s.block_id = b.id and s.section_key is null;
    update public.classroom_submissions s
       set answers = jsonb_set(s.answers, '{__results}', coalesce(s.answers->'__results', '{}'::jsonb) - v_keys)
     where s.enrollment_id = p_enrollment_id and s.block_id = b.id and s.section_key is null
       and s.answers ? '__results';
  end loop;

  update public.classroom_progress
     set status = 'retake', retake_blocks = case when v_all then null else v_blocks end,
         retake_items = nullif(v_items, '{}'::jsonb), retake_deadline_at = p_deadline,
         teacher_note = p_note, score = null, teacher_score = null,
         completed_at = null, show_answers = false,
         history = history || jsonb_build_object('event', 'retake', 'at', now(),
                     'blocks', to_jsonb(v_blocks), 'items', nullif(v_items, '{}'::jsonb), 'whole', v_all,
                     'deadline', p_deadline, 'note', p_note,
                     'score', v_prog.score, 'auto_score', v_prog.auto_score,
                     'submissions', v_old)
   where id = v_prog.id;

  select student_id into v_student from public.classroom_enrollments where id = p_enrollment_id;
  select title into v_title from public.classroom_lessons where id = p_lesson_id;
  if v_student is not null then
    insert into public.classroom_notifications (recipient_kind, recipient_id, kind, title, body, payload)
    values ('student', v_student, 'info', 'Нужно переделать: ' || coalesce(v_title, ''), p_note,
            jsonb_build_object('event', 'retake', 'lesson_id', p_lesson_id, 'enrollment_id', p_enrollment_id,
                               'blocks', to_jsonb(v_blocks), 'deadline', p_deadline));
  end if;

  return jsonb_build_object('ok', true, 'whole', v_all, 'blocks', to_jsonb(v_blocks),
                            'items', nullif(v_items, '{}'::jsonb), 'deadline', p_deadline);
end $$;

-- ── Отправка: сбросить и пункты переделки ──────────────────────────────────

create or replace function public.classroom_finish_lesson(p_enrollment_id uuid, p_lesson_id uuid)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_check jsonb; v_prog public.classroom_progress%rowtype;
  v_auto int; v_student uuid; v_teacher uuid; v_title text;
begin
  if not public.classroom__can_see_enrollment(p_enrollment_id) then
    raise exception 'Нет доступа к этой работе';
  end if;

  v_check := public.classroom__completion_check(p_enrollment_id, p_lesson_id);
  if not coalesce((v_check->>'can_finish')::boolean, false) then
    raise exception 'Выполнены не все задания. Осталось: %',
      (select string_agg(x->>'no', ', ') from jsonb_array_elements(v_check->'incomplete') x);
  end if;

  select * into v_prog from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = p_lesson_id for update;
  if found and v_prog.status in ('submitted', 'reviewed') then
    raise exception 'Домашка уже отправлена';
  end if;

  v_auto := public.classroom__lesson_auto_score(p_enrollment_id, p_lesson_id);

  insert into public.classroom_progress
    (enrollment_id, lesson_id, started_at, status, submitted_at, auto_score, history)
  values (p_enrollment_id, p_lesson_id, now(), 'submitted', now(), v_auto,
          jsonb_build_array(jsonb_build_object('event', 'submitted', 'at', now(), 'auto_score', v_auto)))
  on conflict (enrollment_id, lesson_id) do update
    set status = 'submitted', submitted_at = now(), auto_score = v_auto,
        retake_blocks = null, retake_items = null,
        history = public.classroom_progress.history
                  || jsonb_build_object('event', 'submitted', 'at', now(), 'auto_score', v_auto);

  select e.student_id, e.teacher_id into v_student, v_teacher
    from public.classroom_enrollments e where e.id = p_enrollment_id;
  v_teacher := coalesce((
    select a.assigned_teacher_id from public.classroom_assignments a
     where a.lesson_id = p_lesson_id and a.target_type = 'student' and a.target_id = v_student
       and a.assigned_teacher_id is not null
     order by a.assigned_at desc limit 1), v_teacher);
  select title into v_title from public.classroom_lessons where id = p_lesson_id;
  if v_teacher is not null then
    insert into public.classroom_notifications (recipient_kind, recipient_id, kind, title, payload)
    values ('teacher', v_teacher, 'info', 'Домашка отправлена: ' || coalesce(v_title, ''),
            jsonb_build_object('event', 'submitted', 'lesson_id', p_lesson_id, 'enrollment_id', p_enrollment_id,
                               'student_id', v_student));
  end if;

  return jsonb_build_object('ok', true, 'status', 'submitted');
end $$;

-- ── Страница ученика: срок переделки, огоньки по первой сдаче ──────────────

create or replace function public.classroom_run_meta(p_enrollment_id uuid, p_lesson_id uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_student uuid; v_out jsonb; v_streak int := 0; r record; v_prog public.classroom_progress%rowtype;
  v_deadline timestamptz;
begin
  if not public.classroom__can_see_enrollment(p_enrollment_id) then
    raise exception 'Нет доступа к этой работе';
  end if;
  select student_id into v_student from public.classroom_enrollments where id = p_enrollment_id;

  -- серия: отправленные домашки от последней к первой, пока ПЕРВАЯ сдача не позже
  -- первого срока; переделка на серию не влияет (решение Анны 15.10)
  for r in
    select public.classroom__first_submitted(p) as first_at, a.deadline_at
      from public.classroom_progress p
      left join public.classroom_assignments a
        on a.lesson_id = p.lesson_id and a.target_type = 'student' and a.target_id = v_student
     where p.enrollment_id = p_enrollment_id and p.submitted_at is not null
     order by 1 desc
  loop
    exit when r.deadline_at is not null and r.first_at > r.deadline_at;
    v_streak := v_streak + 1;
  end loop;

  select * into v_prog from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = p_lesson_id;
  select a.deadline_at into v_deadline from public.classroom_assignments a
   where a.lesson_id = p_lesson_id and a.target_type = 'student' and a.target_id = v_student
   order by a.assigned_at desc limit 1;

  select jsonb_build_object(
           'course_title', c.title, 'course_slug', c.slug,
           'unit_title', u.title, 'unit_no', u.sort_order,
           'lesson_title', l.title, 'kind', l.kind,
           'deadline_at', case when v_prog.status = 'retake' and v_prog.retake_deadline_at is not null
                               then v_prog.retake_deadline_at else v_deadline end,
           'first_deadline_at', v_deadline,
           'status', coalesce(v_prog.status, 'new'),
           'streak', v_streak)
    into v_out
    from public.classroom_lessons l
    join public.classroom_units u on u.id = l.unit_id
    join public.classroom_courses c on c.id = u.course_id
   where l.id = p_lesson_id;
  return v_out;
end $$;

-- ── Сводка домашки: + пункты и срок переделки ───────────────────────────────

create or replace function public.classroom_lesson_grade(p_enrollment_id uuid, p_lesson_id uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_prog public.classroom_progress%rowtype; v_teacher boolean; v_open boolean;
  v_blocks jsonb; v_check jsonb;
begin
  if not public.classroom__can_see_enrollment(p_enrollment_id) then
    raise exception 'Нет доступа к этой работе';
  end if;
  v_teacher := public.classroom__can_review(p_enrollment_id);
  select * into v_prog from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = p_lesson_id;
  v_check := public.classroom__completion_check(p_enrollment_id, p_lesson_id);

  if not v_teacher and coalesce(v_prog.status, 'in_progress') <> 'reviewed' then
    return jsonb_build_object(
      'status', coalesce(v_prog.status, 'in_progress'),
      'submitted_at', v_prog.submitted_at,
      'retake_blocks', to_jsonb(v_prog.retake_blocks),
      'retake_items', case when v_prog.status = 'retake' then v_prog.retake_items end,
      'retake_deadline_at', case when v_prog.status = 'retake' then v_prog.retake_deadline_at end,
      'teacher_note', case when v_prog.status = 'retake' then v_prog.teacher_note end,
      'comments', case when v_prog.status = 'retake' then (
         select coalesce(jsonb_agg(jsonb_build_object('id', c.id, 'block_id', c.block_id,
                  'item', c.item, 'body', c.body, 'created_at', c.created_at)
                  order by c.created_at), '[]'::jsonb)
           from public.classroom_comments c
          where c.enrollment_id = p_enrollment_id and c.lesson_id = p_lesson_id) end,
      'submittable', v_check->'submittable', 'submitted', v_check->'submitted',
      'can_finish', v_check->'can_finish', 'incomplete', v_check->'incomplete');
  end if;

  v_open := v_teacher or coalesce(v_prog.show_answers, false);

  select coalesce(jsonb_agg(jsonb_build_object(
           'block_id', b.id, 'type', b.type, 'sort_order', b.sort_order,
           'title', coalesce(b.payload->>'title', ''),
           'needs_review', public.classroom__block_needs_review(b),
           'itemized', public.classroom__itemized(b),
           'submitted', s.id is not null,
           'answers', case when s.id is null then null else s.answers - '__results' end,
           'storage_path', s.storage_path,
           'results', case when v_open then s.answers->'__results' end,
           'overrides', case when v_open then s.overrides end,
           'auto_score', case when v_teacher then s.auto_score end,
           'teacher_score', case when v_teacher then s.teacher_score end,
           'score', case when v_open then public.classroom__block_score(b, s) end,
           'review_pending', s.review_status = 'pending',
           'parts', case when v_teacher and b.type = 'task' then (
              select jsonb_agg(jsonb_build_object('section_key', g.section_key, 'score', g.score,
                                                  'max_score', g.max_score, 'comment', g.comment))
                from public.classroom_grades g
               where g.enrollment_id = p_enrollment_id and g.block_id = b.id) end
         ) order by b.sort_order), '[]'::jsonb)
    into v_blocks
    from public.classroom__lesson_blocks(p_enrollment_id, p_lesson_id) b
    left join public.classroom_submissions s
      on s.block_id = b.id and s.enrollment_id = p_enrollment_id and s.section_key is null
   where public.classroom__block_counts(b);

  return jsonb_build_object(
    'status', coalesce(v_prog.status, 'in_progress'),
    'submitted_at', v_prog.submitted_at,
    'first_submitted_at', case when v_prog.id is not null then public.classroom__first_submitted(v_prog) end,
    'reviewed_at', v_prog.reviewed_at,
    'score', v_prog.score,
    'auto_score', case when v_teacher
                       then public.classroom__lesson_auto_score(p_enrollment_id, p_lesson_id) end,
    'teacher_score', case when v_teacher then v_prog.teacher_score end,
    'teacher_note', v_prog.teacher_note,
    'comments', (select coalesce(jsonb_agg(jsonb_build_object('id', c.id, 'block_id', c.block_id,
                    'item', c.item, 'body', c.body, 'created_at', c.created_at,
                    'updated_at', c.updated_at) order by c.created_at), '[]'::jsonb)
                   from public.classroom_comments c
                  where c.enrollment_id = p_enrollment_id and c.lesson_id = p_lesson_id),
    'show_answers', coalesce(v_prog.show_answers, false),
    'retake_blocks', to_jsonb(v_prog.retake_blocks),
    'retake_items', v_prog.retake_items,
    'retake_deadline_at', v_prog.retake_deadline_at,
    'history', case when v_teacher then v_prog.history end,
    'submittable', v_check->'submittable', 'submitted', v_check->'submitted',
    'can_finish', v_check->'can_finish', 'incomplete', v_check->'incomplete',
    'blocks', v_blocks);
end $$;

-- ── Очередь проверки: всё для строки списка ─────────────────────────────────

create or replace function public.classroom_pending_reviews()
returns jsonb language sql stable security definer set search_path = public as $$
  select coalesce(jsonb_agg(r order by sub_at), '[]'::jsonb)
  from (
    select p.submitted_at as sub_at, jsonb_build_object(
           'enrollment_id', p.enrollment_id, 'student_id', e.student_id,
           'lesson_id', p.lesson_id, 'lesson_title', l.title, 'kind', l.kind,
           'unit_title', u.title, 'unit_no', u.sort_order,
           'course_title', c.title, 'course_slug', c.slug,
           'submitted_at', p.submitted_at, 'auto_score', p.auto_score,
           'attempt', (select count(*) from jsonb_array_elements(p.history) h
                        where h->>'event' = 'submitted'),
           'deadline_at', coalesce(
              case when exists (select 1 from jsonb_array_elements(p.history) h where h->>'event' = 'retake')
                   then p.retake_deadline_at end, a.deadline_at),
           'late', p.submitted_at > coalesce(
              case when exists (select 1 from jsonb_array_elements(p.history) h where h->>'event' = 'retake')
                   then p.retake_deadline_at end, a.deadline_at),
           'has_manual', exists (
              select 1 from public.classroom__lesson_blocks(p.enrollment_id, p.lesson_id) b
               where public.classroom__block_counts(b) and public.classroom__block_needs_review(b))
         ) as r
    from public.classroom_progress p
    join public.classroom_enrollments e on e.id = p.enrollment_id
    join public.classroom_lessons l on l.id = p.lesson_id
    join public.classroom_units u on u.id = l.unit_id
    join public.classroom_courses c on c.id = u.course_id
    left join lateral (
      select a.deadline_at from public.classroom_assignments a
       where a.lesson_id = p.lesson_id and a.target_type = 'student' and a.target_id = e.student_id
       order by a.assigned_at desc limit 1) a on true
   where p.status = 'submitted'
     and (public.classroom_is_editor()
          or (public.classroom__current_teacher_id() is not null
              and public.classroom__can_see_student(e.student_id)))
  ) t;
$$;
