-- Super Minds 1 · Unit 5 · My week · Unit 5 Test
-- собрано tools/sm1_build.py --lesson u5_test
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
  select v_unit, 'Unit 5 Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Unit 5 Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Unit 5 Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Напиши по-английски: понедельник", "accept": ["Monday"], "audio_tts": "Monday"}, {"prompt": "Напиши по-английски: вторник", "accept": ["Tuesday"], "audio_tts": "Tuesday"}, {"prompt": "Напиши по-английски: среда", "accept": ["Wednesday"], "audio_tts": "Wednesday"}, {"prompt": "Напиши по-английски: четверг", "accept": ["Thursday"], "audio_tts": "Thursday"}, {"prompt": "Напиши по-английски: пятница", "accept": ["Friday"], "audio_tts": "Friday"}, {"prompt": "Напиши по-английски: суббота", "accept": ["Saturday"], "audio_tts": "Saturday"}, {"prompt": "Напиши по-английски: воскресенье", "accept": ["Sunday"], "audio_tts": "Sunday"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm1/u5/act_ride_pony.webp", "right": "ride a pony", "right_audio_tts": "ride a pony"}, {"left_image": "@@MEDIA@@sm1/u5/act_go_swimming.webp", "right": "go swimming", "right_audio_tts": "go swimming"}, {"left_image": "@@MEDIA@@sm1/u5/act_watch_tv.webp", "right": "watch TV", "right_audio_tts": "watch TV"}, {"left_image": "@@MEDIA@@sm1/u5/act_play_football.webp", "right": "play football", "right_audio_tts": "play football"}, {"left_image": "@@MEDIA@@sm1/u5/act_computer_games.webp", "right": "play computer games", "right_audio_tts": "play computer games"}, {"left_image": "@@MEDIA@@sm1/u5/act_ride_bike.webp", "right": "ride a bike", "right_audio_tts": "ride a bike"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: Do you play computer games at the weekend?<br>B: ___", "type": "single", "options": [{"text": "Yes, I don’t."}, {"text": "Yes, I do."}, {"text": "No, I do."}], "correct": [1], "image": "@@MEDIA@@sm1/u5/t_computer_games.webp"}, {"q": "A: Do you play the piano every day?<br>B: ___", "type": "single", "options": [{"text": "No, I don’t."}, {"text": "No, I do."}, {"text": "Yes, I don’t."}], "correct": [0], "image": "@@MEDIA@@sm1/u5/t_piano.webp"}, {"q": "A: Do you play football on Sundays?<br>B: ___", "type": "single", "options": [{"text": "Yes, I do. I go swimming."}, {"text": "Yes, I don’t."}, {"text": "No, I don’t. I go swimming."}], "correct": [2], "image": "@@MEDIA@@sm1/u5/t_football.webp"}, {"q": "A: Do you watch TV at the weekend?<br>B: ___", "type": "single", "options": [{"text": "No, I do."}, {"text": "Yes, I do."}, {"text": "Yes, I don’t."}], "correct": [1], "image": "@@MEDIA@@sm1/u5/t_watch_tv.webp"}, {"q": "A: Do you do your homework every day?<br>B: ___", "type": "single", "options": [{"text": "Yes, I do."}, {"text": "No, I do."}], "correct": [0], "image": "@@MEDIA@@sm1/u5/t_homework.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Do", "you", "watch", "TV", "at the weekend?"], "sentence": "Do you watch TV at the weekend?", "audio_tts": "Do you watch TV at the weekend?", "image": "@@MEDIA@@sm1/u5/t_order_watch_tv.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Do", "you", "play", "the piano", "on", "Mondays?"], "sentence": "Do you play the piano on Mondays?", "audio_tts": "Do you play the piano on Mondays?", "image": "@@MEDIA@@sm1/u5/t_order_piano.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Do", "you", "go", "swimming", "on", "Wednesdays?"], "sentence": "Do you go swimming on Wednesdays?", "audio_tts": "Do you go swimming on Wednesdays?", "image": "@@MEDIA@@sm1/u5/act_go_swimming.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Do", "you", "play", "hide-and-seek", "on", "Saturdays?"], "sentence": "Do you play hide-and-seek on Saturdays?", "audio_tts": "Do you play hide-and-seek on Saturdays?", "image": "@@MEDIA@@sm1/u5/act_hide_and_seek.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Do", "you", "ride", "a pony", "every Friday?"], "sentence": "Do you ride a pony every Friday?", "audio_tts": "Do you ride a pony every Friday?", "image": "@@MEDIA@@sm1/u5/act_ride_pony.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'match', replace($blk${"title": "READING. Прочитай текст. Соедини день недели с действием. «Hi! I’m Sam. Here is my week! On Mondays I don’t play football – I go swimming. On Tuesdays I play computer games. On Thursdays I don’t watch TV – I play hide-and-seek with my friends. On Saturdays I sing. On Sundays I play ball with my dad.»", "pairs": [{"left": "Monday", "right": "go swimming", "right_audio_tts": "go swimming"}, {"left": "Tuesday", "right": "play computer games", "right_audio_tts": "play computer games"}, {"left": "Thursday", "right": "play hide-and-seek", "right_audio_tts": "play hide-and-seek"}, {"left": "Saturday", "right": "sing", "right_audio_tts": "sing"}, {"left": "Sunday", "right": "play ball", "right_audio_tts": "play ball"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'video', replace($blk${"title": "LISTENING. Послушай запись 🎧", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'sort', replace($blk${"title": "Перетащи дни недели и занятия в колонку нужного ребёнка", "groups": [{"name": "Tom", "items": [{"text": "Sunday"}, {"text": "Saturday"}, {"text": "play football"}, {"text": "watch TV"}]}, {"name": "Lucy", "items": [{"text": "Monday"}, {"text": "go swimming"}, {"text": "sing"}]}, {"name": "Ben", "items": [{"text": "Wednesday"}, {"text": "play hide-and-seek"}, {"text": "play computer games"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Ответь на вопросы:</p><ol><li>What do you do on Mondays?</li><li>What do you do on Tuesdays?</li><li>What do you do on Wednesdays?</li><li>What do you do on Fridays?</li><li>What do you do on Saturdays?</li><li>What do you do on Sundays?</li><li>Do you like swimming?</li><li>Do you like playing computer games?</li><li>Do you like playing football?</li><li>Do you like doing your homework?</li><li>What do you like to do in your free time?</li><li>What do you like to do with your friends?</li></ol><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
