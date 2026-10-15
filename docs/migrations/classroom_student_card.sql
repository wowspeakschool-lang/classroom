-- classroom_student_card — учительская часть, шаг 2: карточка ученика (HANDOVER 8.1б).
-- Накатывать ПОСЛЕ classroom_review_ui. Только замена одной функции, ничего не удаляет.
-- Накатана 15.10.2026.
--
-- classroom_student_lessons отдаёт ещё: шифр (course_slug, unit_no), первую сдачу
-- (для огоньков и «сдано»), срок переделки, номер попытки, сколько заданий
-- выполнено из скольких (для «в работе · 6 из 11»).

create or replace function public.classroom_student_lessons(p_student_id uuid, p_course_id uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_enroll uuid; v_out jsonb; v_teacher boolean; v_slug text;
begin
  if not (public.classroom_is_editor() or public.classroom__can_see_student(p_student_id)) then
    raise exception 'Нет доступа к ученику';
  end if;
  v_teacher := public.classroom_is_editor() or public.classroom__current_teacher_id() is not null;
  select id into v_enroll from public.classroom_enrollments
   where course_id = p_course_id and student_id = p_student_id;
  select slug into v_slug from public.classroom_courses where id = p_course_id;
  select coalesce(jsonb_agg(item order by u_sort, l_sort), '[]'::jsonb) into v_out
  from (
    select u.sort_order as u_sort, l.sort_order as l_sort,
      jsonb_build_object(
        'lesson_id', l.id,
        'unit_title', u.title,
        'unit_no', u.sort_order,
        'course_slug', v_slug,
        'title', l.title,
        'kind', l.kind,
        'is_published', l.is_published,
        'assigned', a.id is not null,
        'active', coalesce(a.status, '') = 'active',
        'status', a.status,
        'deadline_at', a.deadline_at,
        'retake_deadline_at', case when pr.status = 'retake' then pr.retake_deadline_at end,
        'hw_status', coalesce(pr.status, case when pr.id is null then null else 'in_progress' end),
        'submitted_at', pr.submitted_at,
        'first_submitted_at', case when pr.submitted_at is not null then public.classroom__first_submitted(pr) end,
        'attempt', (select count(*) from jsonb_array_elements(coalesce(pr.history, '[]'::jsonb)) h
                     where h->>'event' = 'submitted'),
        'reviewed_at', pr.reviewed_at,
        'completed', pr.status = 'reviewed',
        'score', case when pr.status = 'reviewed' then pr.score end,
        'auto_score', case when v_teacher then pr.auto_score end,
        'submitted', coalesce(pr.status in ('submitted', 'reviewed'), false),
        'review_pending', coalesce(pr.status = 'submitted', false),
        'retake', coalesce(pr.status = 'retake', false),
        'retake_n', case when pr.status = 'retake' then coalesce(cardinality(pr.retake_blocks), 0) end,
        'progress', case when v_enroll is not null and pr.status in ('in_progress', 'retake')
                         then public.classroom__completion_check(v_enroll, l.id) end
      ) as item
    from public.classroom_units u
    join public.classroom_lessons l on l.unit_id = u.id
    left join public.classroom_assignments a
      on a.lesson_id = l.id and a.target_type = 'student' and a.target_id = p_student_id
    left join public.classroom_progress pr
      on pr.enrollment_id = v_enroll and pr.lesson_id = l.id
    where u.course_id = p_course_id
  ) t;
  return jsonb_build_object('enrollment_id', v_enroll, 'course_slug', v_slug, 'lessons', v_out);
end $$;
