-- ПРОБНЫЙ ПРОГОН миграции classroom_review_ui — НИЧЕГО НЕ СОХРАНЯЕТ.
--
-- Вставить целиком в Supabase → SQL Editor → Run.
-- Внутри: сама миграция и тест полного цикла (ответы → отправка → проверка →
-- переделка одного задания и одного пункта со сроком → повторная отправка).
-- В конце — намеренная ошибка «ТЕСТ {...}», из-за неё всё откатывается.
--
-- Ожидаемый результат — красное сообщение «ERROR: P0001: ТЕСТ {». Его целиком
-- скопировать и прислать в чат. Любая другая ошибка — тоже прислать.

begin;

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


do $t$
declare
  e uuid := 'a0f5fccd-ec6d-41cf-9aec-9e5ff3dd0c94';
  l uuid; b record; r jsonb; ans jsonb; o jsonb := '{}'; v_q uuid; v_sp uuid; v_ord uuid; v_other uuid;
begin
  perform set_config('request.jwt.claims', '{"sub":"141f6dee-8786-414c-b937-d2f436617523","role":"authenticated"}', true);
  perform set_config('request.jwt.claim.sub', '141f6dee-8786-414c-b937-d2f436617523', true);
  o := o || jsonb_build_object('is_editor', public.classroom_is_editor(),
     'snapshots_backfilled', (select count(*) from public.classroom_lesson_snapshots));

  select l2.id into l
    from public.classroom_lessons l2
    join public.classroom_units u on u.id = l2.unit_id
    join public.classroom_enrollments en on en.course_id = u.course_id and en.id = e
   where exists (select 1 from public.classroom_blocks x where x.lesson_id = l2.id and x.type = 'quiz')
     and exists (select 1 from public.classroom_blocks x where x.lesson_id = l2.id and x.type = 'order')
   order by (select count(distinct x.type) from public.classroom_blocks x where x.lesson_id = l2.id) desc
   limit 1;
  o := o || jsonb_build_object('lesson', l,
     'types', (select jsonb_agg(type order by sort_order) from public.classroom_blocks x where x.lesson_id = l and public.classroom__block_counts(x)));

  -- неполный ответ: отправка должна отказать
  for b in select * from public.classroom_blocks x where x.lesson_id = l and public.classroom__block_counts(x) order by sort_order limit 1 loop
    perform public.classroom_submit_block(b.id, e, '{}'::jsonb);
  end loop;
  begin
    perform public.classroom_finish_lesson(e, l);
    o := o || '{"incomplete_refused":"НЕТ — ошибка"}';
  exception when others then o := o || jsonb_build_object('incomplete_refused', sqlerrm); end;
  for b in select * from public.classroom_blocks x where x.lesson_id = l and public.classroom__block_counts(x) order by sort_order loop
    ans := case b.type
      when 'quiz' then (select coalesce(jsonb_object_agg(i-1, coalesce(q->'correct', '[0]'::jsonb)), '{}') from jsonb_array_elements(b.payload->'questions') with ordinality t(q,i))
      when 'exact_input' then (select coalesce(jsonb_object_agg(i-1, coalesce(q->'accept'->0, '"x"'::jsonb)), '{}') from jsonb_array_elements(b.payload->'items') with ordinality t(q,i))
      when 'match' then (select coalesce(jsonb_object_agg(i-1, coalesce(q->'right', '"x"'::jsonb)), '{}') from jsonb_array_elements(b.payload->'pairs') with ordinality t(q,i))
      when 'gaps' then (select coalesce(jsonb_object_agg(i-1, coalesce(q->0, '"x"'::jsonb)), '{}') from jsonb_array_elements(public.classroom__gaps_accept(b.payload->>'text')) with ordinality t(q,i))
      when 'truefalse' then (select coalesce(jsonb_object_agg(i-1, to_jsonb(coalesce((q->>'correct')::boolean, false))), '{}') from jsonb_array_elements(b.payload->'statements') with ordinality t(q,i))
      when 'sequence' then (select coalesce(jsonb_object_agg(i-1, i-1), '{}') from jsonb_array_elements(b.payload->'items') with ordinality t(q,i))
      when 'hotspot' then (select coalesce(jsonb_object_agg(i-1, coalesce(q->'text', '""'::jsonb)), '{}') from jsonb_array_elements(b.payload->'points') with ordinality t(q,i))
      when 'order' then jsonb_build_object('order', b.payload->'words')
      when 'sort' then jsonb_build_object('assign', (select coalesce(jsonb_object_agg(z.n - 1, z.grp), '{}') from (
          select row_number() over (order by g.ord, it.iord) n, g.ord - 1 grp
            from jsonb_array_elements(b.payload->'groups') with ordinality g(v, ord)
            cross join lateral jsonb_array_elements(g.v->'items') with ordinality it(x, iord)) z))
      when 'speaking' then '{"audio":"https://x/a.webm"}'::jsonb
      when 'task' then '{"text":"мой ответ"}'::jsonb
      when 'video' then '{"watched":true}'::jsonb
      when 'flashcards' then jsonb_build_object('seen', (select coalesce(jsonb_agg(i-1), '[]') from jsonb_array_elements(b.payload->'cards') with ordinality t(q,i)))
      else '{}'::jsonb end;
    r := public.classroom_submit_block(b.id, e, ans);
    if b.type = 'quiz' and v_q is null then v_q := b.id; end if;
    if b.type = 'order' and v_ord is null then v_ord := b.id; end if;
    if b.type in ('speaking','task') and v_sp is null then v_sp := b.id; end if;
    if b.type not in ('quiz','order') and v_other is null then v_other := b.id; end if;
    o := o || jsonb_build_object('submit_' || b.sort_order || '_' || b.type, r);
  end loop;

  o := o || jsonb_build_object('order_results',
     (select answers->'__results' from public.classroom_submissions where enrollment_id = e and block_id = v_ord));
  o := o || jsonb_build_object('finish', public.classroom_finish_lesson(e, l));
  begin
    perform public.classroom_submit_block(v_q, e, '{}'::jsonb);
    o := o || '{"locked":"НЕТ — ошибка"}';
  exception when others then o := o || jsonb_build_object('locked', sqlerrm); end;
  begin
    perform public.classroom_finish_lesson(e, l);
    o := o || '{"refinish":"НЕТ — ошибка"}';
  exception when others then o := o || jsonb_build_object('refinish', sqlerrm); end;

  o := o || jsonb_build_object('pending', (select jsonb_agg(x) from jsonb_array_elements(public.classroom_pending_reviews()) x where x->>'enrollment_id' = e::text));
  o := o || jsonb_build_object('item_override', public.classroom_review_item(e, v_q, '0', false));
  o := o || jsonb_build_object('item_override_undo', public.classroom_review_item(e, v_q, '0', null));
  o := o || jsonb_build_object('order_word_off', public.classroom_review_item(e, v_ord, '0', false));
  if v_sp is not null then
    o := o || jsonb_build_object('block_score', public.classroom_review_block(e, v_sp, 80));
  end if;
  o := o || jsonb_build_object('comment_block', public.classroom_comment_save(e, l, v_ord, '0', 'Сначала подлежащее: I have…', null));
  o := o || jsonb_build_object('comment_all', public.classroom_comment_save(e, l, null, null, 'Молодец, повтори правило про have got', null));
  o := o || jsonb_build_object('review_finish', public.classroom_review_finish(e, l, null, true, null));
  r := public.classroom_lesson_grade(e, l);
  o := o || jsonb_build_object('grade_head', r - 'blocks' - 'history', 'grade_block0', r->'blocks'->0, 'history_len', jsonb_array_length(r->'history'));
  o := o || jsonb_build_object('student_lessons_row',
     (select x from jsonb_array_elements(public.classroom_student_lessons(
        (select student_id from public.classroom_enrollments where id = e),
        (select course_id from public.classroom_enrollments where id = e))->'lessons') x where x->>'lesson_id' = l::text));

  begin
    perform public.classroom_retake(e, l, null, array[v_ord], null, 'x');
    o := o || '{"retake_no_deadline":"НЕТ — ошибка"}';
  exception when others then o := o || jsonb_build_object('retake_no_deadline', sqlerrm); end;
  o := o || jsonb_build_object('retake', public.classroom_retake(e, l, now() + interval '3 days', array[v_ord],
       jsonb_build_object(v_q::text, jsonb_build_array('1')), 'Собери предложение ещё раз'));
  o := o || jsonb_build_object('quiz_after_item_retake', (select answers from public.classroom_submissions where enrollment_id = e and block_id = v_q));
  o := o || jsonb_build_object('meta_in_retake', public.classroom_run_meta(e, l));
  o := o || jsonb_build_object('grade_student_view_items', (public.classroom_lesson_grade(e, l))->'retake_items');
  o := o || jsonb_build_object('complete_before_fix', (public.classroom__completion_check(e, l))->'incomplete');
  begin
    perform public.classroom_submit_block(v_q, e, '{}'::jsonb);
    o := o || '{"accepted_locked":"НЕТ — ошибка"}';
  exception when others then o := o || jsonb_build_object('accepted_locked', sqlerrm); end;
  o := o || jsonb_build_object('resubmit_quiz', public.classroom_submit_block(v_q, e,
       (select coalesce(jsonb_object_agg(i-1, coalesce(q->'correct', '[0]'::jsonb)), '{}') from jsonb_array_elements((select payload from public.classroom_blocks where id = v_q)->'questions') with ordinality t(q,i))));
  o := o || jsonb_build_object('resubmit_retake', public.classroom_submit_block(v_ord, e, jsonb_build_object('order', (select payload->'words' from public.classroom_blocks where id = v_ord))));
  o := o || jsonb_build_object('finish2', public.classroom_finish_lesson(e, l));
  o := o || jsonb_build_object('final_progress',
     (select jsonb_build_object('status', status, 'auto', auto_score, 'score', score, 'retake', retake_blocks,
             'events', (select jsonb_agg(h->>'event') from jsonb_array_elements(history) h))
        from public.classroom_progress where enrollment_id = e and lesson_id = l));
  o := o || jsonb_build_object('pending2', (select jsonb_agg(x) from jsonb_array_elements(public.classroom_pending_reviews()) x where x->>'enrollment_id' = e::text));
  o := o || jsonb_build_object('notifs', (select jsonb_agg(kind || ': ' || title) from public.classroom_notifications where created_at > now() - interval '1 minute'));
  o := o || jsonb_build_object('comments_after_retake', jsonb_array_length(public.classroom_lesson_grade(e, l)->'comments'));
  o := o || jsonb_build_object('run_meta', public.classroom_run_meta(e, l),
     'run_blocks_n', jsonb_array_length(public.classroom_run_blocks(e, l)),
     'video_unwatched_incomplete', (select not public.classroom__block_complete(x, '{"watched":false}'::jsonb)
        from public.classroom_blocks x where x.type = 'video' limit 1),
     'cards_partial_incomplete', (select not public.classroom__block_complete(x, '{"seen":[0]}'::jsonb)
        from public.classroom_blocks x where x.type = 'flashcards' and jsonb_array_length(x.payload->'cards') > 1 limit 1));
  raise exception 'ТЕСТ %', o;
end $t$;
