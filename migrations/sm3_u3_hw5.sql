-- Super Minds 3 · Unit 3 · At home · Homework 5
-- собрано tools/sm3_build.py --lesson u3_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 3 · At home', 3
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 3 · At home');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 3 · At home';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>HELLO! Рад тебя видеть!</h2><p>Сегодня мы вспомним с тобой историю, которую ты смотрел на уроке. Поехали!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Прочитай историю!</h3><p><img src=\"@@MEDIA@@sm3/u3/story_letter_f_1.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u3/story_letter_f_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["Let’s", "look", "for", "it", "tomorrow", "morning."], "sentence": "Let’s look for it tomorrow morning.", "audio_tts": "Let's look for it tomorrow morning."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["Let’s", "wait", "for", "dark."], "sentence": "Let’s wait for dark.", "audio_tts": "Let's wait for dark."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["I", "don’t", "like", "this", "village."], "sentence": "I don’t like this village.", "audio_tts": "I don't like this village."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Let’s", "go", "soon."], "sentence": "Let’s go soon.", "audio_tts": "Let's go soon."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["What", "a", "mess!"], "sentence": "What a mess!", "audio_tts": "What a mess!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Look at pictures 1 and 3. What’s the same about Ben and Zelda?", "type": "single", "image": "@@MEDIA@@sm3/u3/story_letter_f_quiz.webp", "options": [{"text": "They are angry."}, {"text": "They are tired."}, {"text": "They are hungry."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Look at picture 8. What’s the same about Lucy and Ben?", "type": "single", "image": "@@MEDIA@@sm3/u3/story_letter_f_quiz.webp", "options": [{"text": "They are sad."}, {"text": "They are angry."}, {"text": "They are excited."}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Look at pictures 6 and 8. What’s different about Lucy?", "type": "single", "image": "@@MEDIA@@sm3/u3/story_letter_f_quiz.webp", "options": [{"text": "First she is happy, then she is unhappy."}, {"text": "First she is unhappy, then she is happy."}, {"text": "First she is scared, then she is not tired."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'task', replace($blk${"title": "Answer the questions about the story", "needs_review": true, "html": "<ol><li>What time do Horax and Zelda go home?</li><li>Where does Ben look for the letter first?</li><li>Where does Lucy find the letter?</li><li>What is the second letter?</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты со всем справился!</h3><p>ЛОВИ ЗВЁЗДОЧКУ! Увидимся на уроке! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
