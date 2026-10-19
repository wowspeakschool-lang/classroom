-- classroom_no_mic — учительская часть, шаг 4 (HANDOVER 8.1б):
-- «Не работает микрофон — написать текстом».
--   * задание «Запись голоса» засчитывается и текстом, если ученик отметил,
--     что микрофон не работает (answers.no_mic = true, answers.text);
--   * при отправке домашки учителю приходит уведомление: сколько заданий ответил
--     текстом и в который раз за 30 дней (payload.repeat; с 3-го — совет
--     попросить ассистентов связаться с родителями, это пишет интерфейс).
-- Обе функции — копия текущих из базы (16.10.2026) с добавлением. Ничего не удаляет.

CREATE OR REPLACE FUNCTION public.classroom__block_complete(b classroom_blocks, p_answers jsonb)
 RETURNS boolean
 LANGUAGE plpgsql
 STABLE
 SET search_path TO 'public'
AS $function$
declare
  v_a jsonb := coalesce(p_answers, '{}'::jsonb);
  v_n int; v_i int; v_q jsonb;
begin
  if p_answers is null then return false; end if;   -- ответа нет совсем

  if b.type = 'quiz' then
    v_i := 0;
    for v_q in select * from jsonb_array_elements(coalesce(b.payload->'questions', '[]'::jsonb)) loop
      if coalesce(v_q->>'type', '') <> 'text'
         and coalesce(jsonb_array_length(case when jsonb_typeof(v_a->v_i::text) = 'array'
                                              then v_a->v_i::text end), 0) = 0 then
        return false;
      end if;
      v_i := v_i + 1;
    end loop;
    return true;

  elsif b.type in ('exact_input', 'match', 'gaps', 'truefalse', 'sequence', 'hotspot') then
    v_n := case b.type
      when 'exact_input' then jsonb_array_length(coalesce(b.payload->'items', '[]'::jsonb))
      when 'match'       then jsonb_array_length(coalesce(b.payload->'pairs', '[]'::jsonb))
      when 'gaps'        then jsonb_array_length(public.classroom__gaps_accept(b.payload->>'text'))
      when 'truefalse'   then jsonb_array_length(coalesce(b.payload->'statements', '[]'::jsonb))
      when 'sequence'    then jsonb_array_length(coalesce(b.payload->'items', '[]'::jsonb))
      when 'hotspot'     then jsonb_array_length(coalesce(b.payload->'points', '[]'::jsonb))
    end;
    for v_i in 0 .. coalesce(v_n, 0) - 1 loop
      if not (v_a ? v_i::text) then return false; end if;
      -- в точках пустая строка = ребёнок промахнулся, это ответ (неверный);
      -- в остальных пустое поле = не ответил
      if b.type not in ('hotspot', 'truefalse', 'sequence')
         and btrim(coalesce(v_a->>v_i::text, '')) = '' then
        return false;
      end if;
    end loop;
    return true;

  elsif b.type = 'order' then
    return coalesce(jsonb_array_length(case when jsonb_typeof(v_a->'order') = 'array'
                                            then v_a->'order' end), 0)
         = coalesce(jsonb_array_length(b.payload->'words'), 0);

  elsif b.type = 'sort' then
    select coalesce(sum(jsonb_array_length(coalesce(g->'items', '[]'::jsonb))), 0) into v_n
      from jsonb_array_elements(coalesce(b.payload->'groups', '[]'::jsonb)) g;
    return (select count(*) from jsonb_object_keys(
              case when jsonb_typeof(v_a->'assign') = 'object' then v_a->'assign' else '{}'::jsonb end))
           >= v_n;

  elsif b.type = 'speaking' then
    -- запись голоса; или текст, если у ученика не работает микрофон
    return btrim(coalesce(v_a->>'audio', '')) <> ''
        or (coalesce(v_a->>'no_mic', '') = 'true' and btrim(coalesce(v_a->>'text', '')) <> '');

  elsif b.type = 'task' then
    return btrim(coalesce(v_a->>'text', '')) <> '' or btrim(coalesce(v_a->>'audio', '')) <> '';

  elsif b.type = 'video' then
    return coalesce((v_a->>'watched')::boolean, false);   -- досмотрел до конца
  elsif b.type = 'flashcards' then
    return coalesce(jsonb_array_length(case when jsonb_typeof(v_a->'seen') = 'array' then v_a->'seen' end), 0)
         >= jsonb_array_length(coalesce(b.payload->'cards', '[]'::jsonb));   -- открыл каждую карточку
  end if;
  return true;   -- embed: «пройдено по факту»
end $function$;

CREATE OR REPLACE FUNCTION public.classroom_finish_lesson(p_enrollment_id uuid, p_lesson_id uuid)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
declare
  v_check jsonb; v_prog public.classroom_progress%rowtype;
  v_auto int; v_student uuid; v_teacher uuid; v_title text;
  v_nomic int; v_repeat int; v_name text; v_slug text; v_unit int;
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

    -- «Не работает микрофон»: сколько заданий ответил текстом и в который раз за месяц
    select count(*) into v_nomic
      from public.classroom_submissions s join public.classroom_blocks b on b.id = s.block_id
     where s.enrollment_id = p_enrollment_id and b.lesson_id = p_lesson_id and s.section_key is null
       and s.answers->>'no_mic' = 'true';
    if v_nomic > 0 then
      select count(distinct b.lesson_id) into v_repeat
        from public.classroom_submissions s
        join public.classroom_blocks b on b.id = s.block_id
        join public.classroom_enrollments e on e.id = s.enrollment_id
       where e.student_id = v_student and s.answers->>'no_mic' = 'true'
         and s.submitted_at > now() - interval '30 days';
      select name into v_name from public.students where id = v_student;
      select c.slug, u.sort_order into v_slug, v_unit
        from public.classroom_lessons l join public.classroom_units u on u.id = l.unit_id
        join public.classroom_courses c on c.id = u.course_id where l.id = p_lesson_id;
      insert into public.classroom_notifications (recipient_kind, recipient_id, kind, title, body, payload)
      values ('teacher', v_teacher, 'info', coalesce(v_name, 'Ученик') || ': не работает микрофон',
              'Ответил(а) текстом: ' || v_nomic,
              jsonb_build_object('event', 'no_mic', 'lesson_id', p_lesson_id, 'enrollment_id', p_enrollment_id,
                                 'student_id', v_student, 'blocks', v_nomic, 'repeat', greatest(v_repeat, 1),
                                 'course_slug', v_slug, 'unit_no', v_unit, 'lesson_title', v_title));
    end if;
  end if;

  return jsonb_build_object('ok', true, 'status', 'submitted');
end $function$;
