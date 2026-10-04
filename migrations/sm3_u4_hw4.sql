-- Super Minds 3 · Unit 4 · In the town · Homework 4
-- собрано tools/sm3_build.py --lesson u4_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 4 · In the town', 4
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 4 · In the town');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 4 · In the town';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hi! Happy to see you!</h2><p>Сегодня тебя ждёт много интересных заданий. Готов начать?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Внимательно прочитай правило</h3><p><b>Language focus.</b> Use <b>be going to</b> + <b>infinitive of purpose</b> to tell someone where you are going and why you are going there.</p><p><i>Where are you going?</i> — I <b>am going to</b> the market <b>to buy</b> some fruit and vegetables.<br><i>Where is he / she going?</i> — He / she <b>is going to</b> the sports centre <b>to play</b> table tennis.<br><i>Where are we / they going?</i> — We / they <b>are going to</b> the café <b>to have</b> lunch.</p><p>А теперь перейдём к заданиям!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'order', replace($blk${"words": ["Mandy", "is", "going", "to", "the", "square", "to meet", "her", "cousin."], "sentence": "Mandy is going to the square to meet her cousin.", "audio_tts": "Mandy is going to the square to meet her cousin."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["Richard and Pierre", "are", "going", "to the", "cinema", "to watch", "a new", "film."], "sentence": "Richard and Pierre are going to the cinema to watch a new film.", "audio_tts": "Richard and Pierre are going to the cinema to watch a new film."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["Serge", "is", "going", "to the", "library", "to get", "some books", "for his science project."], "sentence": "Serge is going to the library to get some books for his science project.", "audio_tts": "Serge is going to the library to get some books for his science project."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["Martina", "is", "going", "to the", "market", "to buy", "a birthday present", "for her sister."], "sentence": "Martina is going to the market to buy a birthday present for her sister.", "audio_tts": "Martina is going to the market to buy a birthday present for her sister."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Emma", "is", "going", "to the", "sports centre", "to go", "swimming."], "sentence": "Emma is going to the sports centre to go swimming.", "audio_tts": "Emma is going to the sports centre to go swimming."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["We", "are", "going", "to the", "café", "to drink", "some", "milkshakes."], "sentence": "We are going to the café to drink some milkshakes.", "audio_tts": "We are going to the cafe to drink some milkshakes."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<h3>Молодец! А теперь прочитай внимательно текст</h3><p><img src=\"@@MEDIA@@sm3/u4/postcard_ali.webp\" alt=\"Reading: a postcard\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'truefalse', replace($blk${"title": "Прочитай открытку выше. Выбери «верно», если предложение верное, и «неверно», если нет", "statements": [{"text": "It’s the second (2nd) week of Ali’s school trip.", "correct": false}, {"text": "Ali’s hotel is next to a museum.", "correct": false}, {"text": "The tower isn’t a new building.", "correct": true}, {"text": "Below the tower there is a square.", "correct": true}, {"text": "There aren’t any paintings by famous artists in the museum.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'task', replace($blk${"title": "Напиши 3–6 предложений про свои планы", "needs_review": true, "html": "<p>Ура! Ты уже так много сделал. У меня для тебя ещё одно задание: представь, что ты отправился в путешествие.</p><p><i>Например:<br>I’m going to the market to…<br>I’m going to the park to…</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты просто СУПЕРКРУТ!</h3><p>Настоящий гуру английского. Так держать :) Увидимся на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
