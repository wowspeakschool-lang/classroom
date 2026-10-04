-- Super Minds 3 · Unit 8 · Countries · Homework 4
-- собрано tools/sm3_build.py --lesson u8_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · Countries', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · Countries');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · Countries';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Сегодня тебя ждёт новое домашнее задание!</h2><p>Будет много интересного, тебе понравится :) А ещё есть дополнительное задание — необязательное, но если выполнишь, получишь звание покорителя английского языка!</p><p>Для начала посмотри видео: как думаешь, останавливался ли Хэмми в отеле во время отпуска?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: каникулы Хэмми", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Посмотри видео ещё раз и отметь, как Хэмми ответил на вопросы", "pairs": [{"left": "Did you stay in a hotel?", "right": "No, I didn’t.", "right_audio_tts": "No, I didn't."}, {"left": "Did you have a good holiday?", "right": "Yes, I did!", "right_audio_tts": "Yes, I did!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["Did", "you", "have", "fun", "there?"], "sentence": "Did you have fun there?", "audio_tts": "Did you have fun there?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["How", "long", "did", "you", "stay", "in Mexico?"], "sentence": "How long did you stay in Mexico?", "audio_tts": "How long did you stay in Mexico?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["Where", "did", "you", "stay?"], "sentence": "Where did you stay?", "audio_tts": "Where did you stay?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Did", "you", "go", "to", "a", "museum", "there?"], "sentence": "Did you go to a museum there?", "audio_tts": "Did you go to a museum there?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["Did", "you", "buy", "me", "a", "present?"], "sentence": "Did you buy me a present?", "audio_tts": "Did you buy me a present?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'match', replace($blk${"title": "Подбери ответы на вопросы. Если сложно — пропусти и вернись, когда сделаешь остальные", "pairs": [{"left": "Did you play in the park yesterday?", "right": "Yes, I did! The weather was great!", "right_audio_tts": "Yes, I did! The weather was great!"}, {"left": "Where did you go last Sunday?", "right": "I went to the supermarket to buy some food.", "right_audio_tts": "I went to the supermarket to buy some food."}, {"left": "How long did you play computer games last weekend?", "right": "For 3 hours. My mum was angry!", "right_audio_tts": "For three hours. My mum was angry!"}, {"left": "Who did you go to the park with?", "right": "With my parents.", "right_audio_tts": "With my parents."}, {"left": "When did you get up last Saturday?", "right": "At 10 o’clock.", "right_audio_tts": "At ten o'clock."}, {"left": "Did you go to a museum last weekend?", "right": "No, I didn’t. It was closed.", "right_audio_tts": "No, I didn't. It was closed."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'speaking', replace($blk${"title": "Дополнительное задание 🎤", "needs_review": true, "audio": "", "html": "<p>Ответь на вопросы и запиши себя на диктофон.</p><p>1. Did you play in the park yesterday?<br>2. Did you do your homework yesterday?<br>3. What did you do last Sunday?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Вот это да! Ты завершил домашнее задание!</h3><p>Кто настоящий молодец? Это ты! До встречи на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
