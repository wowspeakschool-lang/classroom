-- Super Minds 1 · Unit 9 · Holidays · Homework 4
-- собрано tools/sm1_build.py --lesson u9_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 9 · Holidays', 9
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 9 · Holidays');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 9 · Holidays';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>Сегодня мы с тобой послушаем и прочитаем рассказ о наших супердрузьях!</p><p>А в конце тебя ждёт дополнительное задание — видео и задание к нему. Оно выполняется по желанию, но ты будешь МЕГА крут, когда справишься с ним!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Твоё первое задание — послушать запись истории и выполнить задание под аудио.</p><p>В этот раз Misty, Thunder, Flash и Whisper решили взобраться на вершину холма наперегонки. <b>Как думаешь, кто доберётся первым?</b></p><p>Послушай аудио и узнай, угадал ли ты.</p><p><img src=\"@@MEDIA@@sm1/u9/hw4_flash_running.webp\" alt=\"Flash\" style=\"max-width:320px\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Аудио: история «The top of the hill»", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sequence', replace($blk${"title": "Послушай историю ещё раз и расставь предложения в правильном порядке, как они идут в рассказе!", "image": "@@MEDIA@@sm1/u9/hw4_friends.webp", "items": [{"text": "A race?"}, {"text": "See you at the top of the hill!"}, {"text": "I can walk up the hill, but I can't run!"}, {"text": "This is the end of the race."}, {"text": "Let's go together."}, {"text": "What a good idea!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<h3>The top of the hill</h3><p>Внимательно прочитай историю и выполни упражнение, которое ты увидишь сразу после неё.</p><p><img src=\"@@MEDIA@@sm1/u9/hw4_story_1.webp\" alt=\"История, кадры 1–4\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@sm1/u9/hw4_story_2.webp\" alt=\"История, кадры 5–8\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'sequence', replace($blk${"title": "Смотри! История запуталась, и картинки стоят не по порядку 😱 Расставь кадры так, как они идут в истории. Постарайся не подсматривать, а в конце проверь себя по тексту.", "items": [{"image": "@@MEDIA@@sm1/u9/hw4_frame_1.webp"}, {"image": "@@MEDIA@@sm1/u9/hw4_frame_2.webp"}, {"image": "@@MEDIA@@sm1/u9/hw4_frame_3.webp"}, {"image": "@@MEDIA@@sm1/u9/hw4_frame_4.webp"}, {"image": "@@MEDIA@@sm1/u9/hw4_frame_5.webp"}, {"image": "@@MEDIA@@sm1/u9/hw4_frame_6.webp"}, {"image": "@@MEDIA@@sm1/u9/hw4_frame_7.webp"}, {"image": "@@MEDIA@@sm1/u9/hw4_frame_8.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p>Смотри, наша история ожила и превратилась в мультик! Давай посмотрим его!</p><p>Это <b>ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ</b>! Его можно выполнить по желанию, но ты будешь МЕГА крут, когда справишься с ним!</p><p>Посмотри видео и выполни упражнение под ним — вставь пропущенные слова в предложения.</p><p><img src=\"@@MEDIA@@sm1/u9/hw4_video_cover.webp\" alt=\"Unit 9 · The top of the hill\" style=\"max-width:420px\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'video', replace($blk${"title": "Мультфильм «The top of the hill»", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'gaps', replace($blk${"title": "Вставь пропущенные слова в предложения", "mode": "drag", "text": "Let's __go__.\nSee you at the __top__ of the hill.\nA race is not a __good__ idea.\nI can __walk__ up the hill, but I can't __run__.\nThis is the end of the __race__.\nLet's go __together__.\nWhat a good __idea__!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание ❤</h3><p>Ты замечательный ученик! Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
