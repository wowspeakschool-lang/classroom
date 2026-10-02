-- Super Minds 3 · Unit 2 · Food · Homework 5
-- собрано tools/sm3_build.py --lesson u2_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · Food', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · Food');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · Food';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет!</h2><p>Ну что, готов к новой домашней работе? Давай начинать 😊</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Послушай диалоги Ким и Дэниэля, а потом Тома и Мэри", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши пропущенные слова ⏬", "mode": "drag", "text": "Kim: __What’s the matter__, Daniel?\nDaniel: It’s my head. It hurts.\nKim: Shall I get you some medicine?\nDaniel: No, it’s OK. It’s not too bad.\n\nTom: What are you doing, Mary?\nMary: I want this book. It’s really good.\nTom: Shall I help you?\nMary: No, thanks. __I think__ __I’ve got it__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "Послушай образец к игре «I spy with my little eye»", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'speaking', replace($blk${"title": "Поиграем в «I spy with my little eye» 🎤", "needs_review": true, "image": "@@MEDIA@@sm3/u2/scene_i_spy.webp", "html": "<p>Назови первую букву и сам предмет, который не подписан — рядом с ним стоит пустая строчка. Начинай так:</p><p><i>I spy with my little eye something beginning with…</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Большое тебе спасибо за отличную работу!</h3><p>Ты прекрасно поработал сегодня. Так держать! Теперь можно отдохнуть :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
