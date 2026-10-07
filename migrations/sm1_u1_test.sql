-- Super Minds 1 · Unit 1 · My school · Unit 1 Test
-- собрано tools/sm1_build.py --lesson u1_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 1 · My school', 1
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 1 · My school');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 1 · My school';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Unit 1 Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Unit 1 Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Unit 1 Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'task', replace($blk${"title": "🎒 Смотри и пиши!", "image": "@@MEDIA@@sm1/u1/t_school_things.webp", "html": "<p>1️⃣ Внимательно посмотри на картинку 👀 — какие школьные предметы ты видишь?</p><p>2️⃣ В поле под картинкой впиши их названия на английском ✏️</p><p>Молодец! 👏</p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'speaking', replace($blk${"title": "Прочитай предложения вслух 🎤", "image": "@@MEDIA@@sm1/u1/t_reading_kids.webp", "html": "<p>Внимательно прочитай предложения глазками 👀</p><p>Нажми на микрофон 🎤 и проговори их вслух. У тебя получится! 🌟</p><ol><li>I spin a top. The top stops.</li><li>Ken, the pet, is in the cup.</li><li>Ron is a red rat. It can jump.</li><li>Fip and Fop can hop and jog.</li><li>Will can sell the bell.</li><li>Next to the box is a taxi.</li><li>I yell “Yes!”. Mum yells “Yes!”</li></ol>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Внимательно послушай аудио 🎧", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Выбери предметы, которые ты услышишь.", "type": "multiple", "image": "@@MEDIA@@sm1/u1/t_listen_boy.webp", "options": [{"text": "book"}, {"text": "notebook"}, {"text": "pen"}, {"text": "pencil"}, {"text": "pencil case"}, {"text": "rubber"}, {"text": "ruler"}, {"text": "bag"}, {"text": "desk"}, {"text": "paper"}], "correct": [1, 3, 4, 5, 7]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'video', replace($blk${"title": "Послушай аудио и узнай, какой номер принадлежит какой картинке 🎧", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'hotspot', replace($blk${"title": "Соедини картинки с правильным номером", "mode": "label", "image": "@@MEDIA@@sm1/u1/t_classroom_scenes.webp", "points": [{"x": 66.5, "y": 73, "text": "1"}, {"x": 17.0, "y": 24, "text": "2"}, {"x": 83.0, "y": 24, "text": "3"}, {"x": 50.0, "y": 24, "text": "4"}, {"x": 33.5, "y": 73, "text": "5"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm1/u1/school_book.webp", "right": "book", "right_audio_tts": "book"}, {"left_image": "@@MEDIA@@sm1/u1/school_pen.webp", "right": "pen", "right_audio_tts": "pen"}, {"left_image": "@@MEDIA@@sm1/u1/school_rubber.webp", "right": "rubber", "right_audio_tts": "rubber"}, {"left_image": "@@MEDIA@@sm1/u1/school_pencil.webp", "right": "pencil", "right_audio_tts": "pencil"}, {"left_image": "@@MEDIA@@sm1/u1/school_bag.webp", "right": "bag", "right_audio_tts": "bag"}, {"left_image": "@@MEDIA@@sm1/u1/school_ruler.webp", "right": "ruler", "right_audio_tts": "ruler"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: What ___ this?<br>B: It is a pencil case.", "type": "single", "options": [{"text": "it"}, {"text": "is"}, {"text": "are"}], "correct": [1], "image": "@@MEDIA@@sm1/u1/t_pencil_case.webp"}, {"q": "A: What is this?<br>B: It ___ a pencil case.", "type": "single", "options": [{"text": "is"}, {"text": "are"}, {"text": "it"}], "correct": [0]}, {"q": "A: ___ a desk?<br>B: Yes, it is.", "type": "single", "options": [{"text": "Is"}, {"text": "Is it"}, {"text": "Are it"}], "correct": [1], "image": "@@MEDIA@@sm1/u1/t_desk_chair.webp"}, {"q": "A: Is it a desk?<br>B: Yes, ___.", "type": "single", "options": [{"text": "it isn’t"}, {"text": "it are"}, {"text": "it is"}], "correct": [2]}, {"q": "A: Open your notebook, ___.<br>B: OK.", "type": "single", "options": [{"text": "please"}, {"text": "thank you"}, {"text": "welcome"}], "correct": [0], "image": "@@MEDIA@@sm1/u1/t_notebook.webp"}, {"q": "A: ___ your book, please.<br>B: Sure.", "type": "single", "options": [{"text": "Sit at"}, {"text": "Open"}, {"text": "Write"}], "correct": [1], "image": "@@MEDIA@@sm1/u1/t_book.webp"}, {"q": "A: Open your book, ___.<br>B: Sure.", "type": "single", "options": [{"text": "thank you"}, {"text": "welcome"}, {"text": "please"}], "correct": [2]}, {"q": "A: ___ a pencil case?<br>B: No, it isn’t. It’s a rubber.", "type": "single", "options": [{"text": "Is it"}, {"text": "Is"}, {"text": "Are it"}], "correct": [0], "image": "@@MEDIA@@sm1/u1/t_rubber.webp"}, {"q": "A: Is it a pencil case?<br>B: No, ___. It’s a rubber.", "type": "single", "options": [{"text": "it is"}, {"text": "it isn’t"}, {"text": "it are"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["It", "is", "a", "yellow", "desk."], "sentence": "It is a yellow desk.", "audio_tts": "It is a yellow desk.", "image": "@@MEDIA@@sm1/u1/t_yellow_desk.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Pass", "me", "a", "pencil,", "please."], "sentence": "Pass me a pencil, please.", "audio_tts": "Pass me a pencil, please.", "image": "@@MEDIA@@sm1/u1/t_pencil.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Open", "your", "pencil", "case,", "please."], "sentence": "Open your pencil case, please.", "audio_tts": "Open your pencil case, please.", "image": "@@MEDIA@@sm1/u1/t_pencil_case_open.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Sit", "at", "your", "desk,", "please."], "sentence": "Sit at your desk, please.", "audio_tts": "Sit at your desk, please.", "image": "@@MEDIA@@sm1/u1/t_wooden_desk.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["It", "is", "a", "blue", "notebook."], "sentence": "It is a blue notebook.", "audio_tts": "It is a blue notebook.", "image": "@@MEDIA@@sm1/u1/t_blue_notebook.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "image": "@@MEDIA@@sm1/u1/t_classroom.webp", "html": "<p>Посмотри на картинку и ответь на вопросы:</p><p>What can you see?<br>Do you see a book?<br>What colour is the book?<br>How many rubbers do you see?</p><p><i>For example:<br>It’s a blue desk.<br>It’s a red book.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 13);
end
$mig$;
