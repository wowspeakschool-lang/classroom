-- Super Minds 3 · Unit 6 · Gadgets · Homework 4
-- собрано tools/sm3_build.py --lesson u6_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · Gadgets', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · Gadgets');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · Gadgets';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет, добро пожаловать в домашнее задание!</h2><p>Сегодня мы посмотрим видео и выполним упражнения. А в конце тебя ждёт дополнительное задание — оно по желанию, но ты будешь МЕГА крут, когда справишься с ним!</p><p>Для начала посмотри видео ниже и ответь на вопрос устно: <b>Who is the fastest — the boy, the girl or Hammy?</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: превосходная степень прилагательных", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'order', replace($blk${"words": ["I’m", "the", "strongest!"], "sentence": "I’m the strongest!", "audio_tts": "I'm the strongest!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["I’m", "the", "most", "intelligent!"], "sentence": "I’m the most intelligent!", "audio_tts": "I'm the most intelligent!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'sort', replace($blk${"title": "Отлично! Теперь распредели прилагательные по категориям", "groups": [{"name": "the … + est", "items": [{"text": "fast"}, {"text": "cheap"}, {"text": "big"}, {"text": "small"}, {"text": "funny"}, {"text": "old"}]}, {"name": "the most …", "items": [{"text": "interesting"}, {"text": "dangerous"}, {"text": "expensive"}, {"text": "beautiful"}, {"text": "boring"}, {"text": "exciting"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Поставь прилагательные из скобок в превосходную форму («самый …»). Первый пропуск уже заполнен как образец", "text": "Jack can run, he can run very fast, he’s the fastest (fast) boy in school. And Jane tells jokes like no one else, she’s __the funniest__ (funny) and she’s cool. Robert’s __the happiest__ (happy) — a friendly boy, he laughs and smiles all day, while Sally’s __the quietest__ (quiet), she doesn’t speak up, she says she’s got nothing to say. __The best__ (good) student in our year is Beth McBeth — she’s with me, I’m going to tell her everything and introduce Class 6C."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание — ответь на вопросы письменно", "needs_review": true, "html": "<p>Его можно сделать по желанию. Но если сделаешь, будешь нереально крут и получишь дополнительную ⭐</p><p>1. Who is the funniest person in your class? <i>Например: Alex is the funniest person in my class.</i><br>2. Who is the oldest person in your class?<br>3. Who is the youngest person in your class?<br>4. Who is best at drawing in your class?<br>5. Who is the most intelligent person in your class?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю, ты завершил домашнее задание! Ты просто супер!</h3><p>Увидимся на занятии ;)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
