-- Super Minds 3 · Unit 9 · Weather · Homework 4
-- собрано tools/sm3_build.py --lesson u9_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 9 · Weather', 9
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 9 · Weather');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 9 · Weather';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>В этом уроке тебя ждут несколько упражнений. Выполни все задания, если хочешь выучить тему на все 100!</p><p>В конце урока есть дополнительное задание — по желанию, НО если ты сделаешь его, то будешь нереально крут!</p><p>Для начала посмотри видео и повтори материал, пройденный на занятии.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: Are you going to…?", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Посмотри видео ещё раз, найди вопросы в видео и соедини их с правильным ответом", "pairs": [{"left": "Are you going to climb some trees?", "right": "No, I’m not.", "right_audio_tts": "No, I’m not."}, {"left": "Are you going to eat some sweets?", "right": "Yes, I am.", "right_audio_tts": "Yes, I am."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["Are", "you", "going", "to", "go", "snorkelling?"], "sentence": "Are you going to go snorkelling?", "audio_tts": "Are you going to go snorkelling?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["Are", "you", "going", "to", "take", "photos?"], "sentence": "Are you going to take photos?", "audio_tts": "Are you going to take photos?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["Are", "you", "going", "to", "listen", "to", "music?"], "sentence": "Are you going to listen to music?", "audio_tts": "Are you going to listen to music?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Are", "you", "going", "to", "read", "a", "book?"], "sentence": "Are you going to read a book?", "audio_tts": "Are you going to read a book?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["Are", "you", "going", "to", "eat", "lots", "of", "food?"], "sentence": "Are you going to eat lots of food?", "audio_tts": "Are you going to eat lots of food?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание — для самых больших умников!", "needs_review": true, "html": "<p>Напиши 3–4 вопроса для своих одноклассников об их планах на каникулы — что они собираются делать?</p><p><i>Например: Are you going to read a book?</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание — ты МЕГА КРУТ!</h3><p>Жду тебя на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
