-- Super Minds 1 · Unit 5 · My week · Homework 4
-- собрано tools/sm1_build.py --lesson u5_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · My week', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · My week');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · My week';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнюю работу!</h2><p>Здесь тебя ждут задания по истории, которую мы обсуждали на уроке. Будет очень-очень интересно.</p><p>В конце тебя ждёт вторая часть — интерактивное видео. Делать его необязательно, но если у тебя получится его выполнить, ты будешь супер крут 😀</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p><p><img src=\"@@MEDIA@@sm1/u5/card_lost_phrases.webp\" alt=\"\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@sm1/u5/card_phonics_u.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Прежде чем мы послушаем и прочитаем текст, попробуй вспомнить — <b>куда шли ребята:</b> <i>lake</i> (озеро), <i>forest</i> (лес), <i>river</i> (речка)?</p><p>Прочитай и прослушай текст — правильно ли ты угадал?</p><p><img src=\"@@MEDIA@@sm1/u5/story_lost_forest.webp\" alt=\"\" style=\"max-width:567px;width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "Послушай историю «We’re lost!» 🎧", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm1/u5/story_lost_comic.webp\" alt=\"\" style=\"max-width:630px;width:100%\"></p><p><b>1.</b> <b>Misty:</b> Where’s the lake? <b>Flash:</b> I don’t know. <b>Thunder:</b> We’re lost!<br><b>2.</b> <b>Whisper:</b> I’ve got an idea. <b>Flash:</b> What?<br><b>3.</b> <b>Whisper:</b> Wait and see. <b>Thunder:</b> This isn’t much fun.<br><b>4.</b> <b>Whisper:</b> Rabbit, we’re lost. Where’s the lake? <b>Rabbit:</b> Come with me.<br><b>5.</b> <b>Whisper:</b> Thank you very much. <b>Thunder:</b> Here you are, Rabbit.<br><b>6.</b> <b>Rabbit:</b> Yippee! <b>Whisper:</b> Watch out!<br><b>7.</b> <b>Whisper:</b> Are you OK, Rabbit?<br><b>8.</b> <b>Rabbit:</b> Now, I’m lost! <b>Whisper:</b> Now, he’s lost!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Отлично! А теперь прочитай, послушай и выбери предложения, которые произнёс зайчик 🐰", "type": "multiple", "options": [{"text": "Now, he’s lost.", "audio_tts": "Now, he’s lost."}, {"text": "Yippee!", "audio_tts": "Yippee!"}, {"text": "Here you are.", "audio_tts": "Here you are."}, {"text": "Come with me.", "audio_tts": "Come with me."}, {"text": "Now, I’m lost.", "audio_tts": "Now, I’m lost."}, {"text": "Wait and see.", "audio_tts": "Wait and see."}], "correct": [1, 3, 4]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Давай вспомним то, что говорили ребята в этой истории. Выбери правильный ответ.", "questions": [{"q": "Where’s the ___?", "type": "single", "options": [{"text": "frog"}, {"text": "lake"}], "correct": [1], "image": "@@MEDIA@@sm1/u5/story_lost_flash.webp"}, {"q": "Wait and ___.", "type": "single", "options": [{"text": "see"}, {"text": "swim"}], "correct": [0], "image": "@@MEDIA@@sm1/u5/story_lost_whisper.webp"}, {"q": "Are you OK, ___?", "type": "single", "options": [{"text": "Misty"}, {"text": "rabbit"}], "correct": [1], "image": "@@MEDIA@@sm1/u5/story_lost_rabbit.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'match', replace($blk${"title": "Класс! Все задания выполнены просто отлично. Давай сделаем ещё одно? Соедини вопросы с ответами. Похожие фразы встречались тебе в тексте — можешь заглянуть туда, чтобы понять, что они означают.", "pairs": [{"left": "Where’s my bag?", "right": "I don’t know.", "right_audio_tts": "I don't know."}, {"left": "Are you OK?", "right": "Yes, I am.", "right_audio_tts": "Yes, I am."}, {"left": "Where’s my classroom?", "right": "Come with me.", "right_audio_tts": "Come with me."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ну вот и всё! Первая часть домашней работы выполнена 🎉</h3><p>А это значит, что ты невероятный молодец.</p><p>Дальше — дополнительная часть: интерактивное видео с вопросами. Делать её не обязательно, но она очень-очень интересная. Давай посмотрим видео и сделаем все упражнения 👍</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'video', replace($blk${"title": "Дополнительное задание: мультфильм «We’re lost!»", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Домашнее задание сделано!</h3><p>Ты отлично потрудился. Увидимся на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
