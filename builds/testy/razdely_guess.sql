-- Разделы заданий в тестах (решение Анны 23.10.2026): ключ payload.skill —
-- grammar | vocabulary | speaking | listening | reading | writing, как шесть
-- разделов трекера прогресса. Диктант — writing. Текст и видео без раздела:
-- это материал, не задание. Методист проверяет по списку из rasdely_spisok.
with b as (
  select c.slug, u.sort_order as unit_no, l.title as lesson, b.id, b.type, b.sort_order,
         lower(coalesce(b.payload->>'title','')) as t,
         lower(left(regexp_replace(coalesce(b.payload->>'html', b.payload->>'text',
           b.payload->'questions'->0->>'q', b.payload->'items'->0->>'prompt', ''), '<[^>]+>', ' ', 'g'), 300)) as x,
         lag(b.type) over w as prev_type,
         lower(coalesce(lag(b.payload->>'title') over w, '') || ' ' ||
           left(regexp_replace(coalesce(lag(b.payload->>'html') over w, ''), '<[^>]+>', ' ', 'g'), 300)) as prev_x
  from classroom_courses c join classroom_units u on u.course_id = c.id
  join classroom_lessons l on l.unit_id = u.id join classroom_blocks b on b.lesson_id = l.id
  where l.kind = 'test'
  window w as (partition by b.lesson_id order by b.sort_order)
)
select b.*,
  case
    when type in ('text','video','flashcards','embed') then null
    when type = 'speaking' or t ~ 'speaking|говорени|расскажи|скажи' then 'speaking'
    when t ~ 'диктант|dictation|spelling' then 'writing'
    when t ~ 'listening|послушай|прослушай|аудио|запис|услышишь|рассказ про' or x ~ '^\s*listening' or prev_type = 'video' then 'listening'
    when t ~ 'writing|напиши (письмо|текст|о себе|сообщение|открытку|рассказ|историю|предложени)|письмо' or (type = 'task' and t !~ 'reading|прочитай') then 'writing'
    when t ~ 'reading|прочитай текст|прочитай (историю|письмо|открытку|рассказ)|по тексту|в тексте|прочитай предложения и|прочитай и' or x ~ '^\s*reading'
      or (prev_type = 'text' and prev_x ~ 'reading|прочитай (текст|историю|письмо|открытку|рассказ|предложени)') then 'reading'
    when type = 'order' or t ~ 'grammar|грамматик|пропуск|вставь|закончи|this или these|в правильной форме|форму глагола|расставь слова|составь предложение|выбери подходящ' then 'grammar'
    when type = 'truefalse' then 'reading'
    else 'vocabulary'
  end as skill
from b
