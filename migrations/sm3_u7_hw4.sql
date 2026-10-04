-- Super Minds 3 · Unit 7 · At the doctor’s · Homework 4
-- собрано tools/sm3_build.py --lesson u7_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · At the doctor’s', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · At the doctor’s');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · At the doctor’s';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Огромный привет! Как твоё настроение?</h2><p>Самое время сделать новое домашнее задание. Сегодня нас ждут неправильные глаголы и несколько упражнений. Для начала посмотри видео ниже!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: неправильные глаголы", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Посмотри видео ещё раз и соедини пары глаголов: слева настоящее время, справа прошедшее", "pairs": [{"left": "eat", "right": "ate", "right_audio_tts": "ate"}, {"left": "drink", "right": "drank", "right_audio_tts": "drank"}, {"left": "wake up", "right": "woke up", "right_audio_tts": "woke up"}, {"left": "go", "right": "went", "right_audio_tts": "went"}, {"left": "come", "right": "came", "right_audio_tts": "came"}, {"left": "have", "right": "had", "right_audio_tts": "had"}, {"left": "say", "right": "said", "right_audio_tts": "said"}, {"left": "give", "right": "gave", "right_audio_tts": "gave"}, {"left": "feel", "right": "felt", "right_audio_tts": "felt"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Отлично! Теперь впиши прошедшую форму глагола", "text": "1. have → __had__\n2. go → __went__\n3. feel → __felt__\n4. eat → __ate__\n5. wake up → __woke up__\n6. give → __gave__\n7. drink → __drank__\n8. come → __came__\n9. say → __said__"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши слова в текст по смыслу: had · went · gave · have · said · felt", "mode": "drag", "text": "Last Saturday, Joe Freeze, the small ice-cream monster, woke up at half past eight. He __had__ a terrible headache. He __went__ into his father’s bedroom. His father __gave__ him some medicine. Then Joe said, ‘Can I __have__ some ice cream?’ ‘Of course’, he __said__. Joe had some ice-cream and he __felt__ better."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание — для самых настоящих чемпионов", "needs_review": true, "html": "<p>Напиши 3 предложения о том, что ты делал на прошлых выходных.</p><p><i>Например: I went to the park last weekend.</i></p><p>Вперёд!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Спасибо тебе огромное за твой труд!</h3><p>Ты невероятно потрудился сегодня. До встречи на занятии :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
