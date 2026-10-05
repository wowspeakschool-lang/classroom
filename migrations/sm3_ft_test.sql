-- Super Minds 3 · Final Test · Final Test
-- собрано tools/sm3_build.py --lesson ft_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Final Test', 10
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Final Test');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Final Test';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Final Test', 'test',
         90, false, 0
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Final Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Final Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/ft/scene_final_hall.webp\" alt=\"\" style=\"max-width:100%\"></p><h2>Super Minds 3 · Final Test</h2><p>Это итоговый тест за весь курс. Не торопись, читай задания внимательно — ты всё это уже знаешь!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>LISTENING</h3><p>Послушай аудио и выполни два задания ниже.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Аудио к заданиям «имена людей» и «дни недели»", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'hotspot', replace($blk${"title": "Послушай аудио и подпиши людей на картинке", "mode": "label", "image": "@@MEDIA@@sm3/ft/scene_library.webp", "points": [{"x": 18, "y": 20, "text": "Peter", "audio_tts": "Peter"}, {"x": 90, "y": 28, "text": "Paul", "audio_tts": "Paul"}, {"x": 42, "y": 39, "text": "Jane", "audio_tts": "Jane"}, {"x": 21, "y": 57, "text": "Fred", "audio_tts": "Fred"}, {"x": 60, "y": 57, "text": "Daisy", "audio_tts": "Daisy"}, {"x": 74, "y": 86, "text": "Sally", "audio_tts": "Sally"}], "extras": [{"text": "Mary", "audio_tts": "Mary"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'match', replace($blk${"title": "Послушай аудио и соедини дни недели и занятия", "pairs": [{"left": "Monday", "right_image": "@@MEDIA@@sm3/ft/act_swimming.webp", "right": "go swimming"}, {"left": "Tuesday", "right_image": "@@MEDIA@@sm3/ft/act_football.webp", "right": "play football"}, {"left": "Wednesday", "right_image": "@@MEDIA@@sm3/ft/act_guitar.webp", "right": "play the guitar"}, {"left": "Thursday", "right_image": "@@MEDIA@@sm3/ft/act_shopping.webp", "right": "go shopping"}, {"left": "Friday", "right_image": "@@MEDIA@@sm3/ft/act_cycling.webp", "right": "ride a bike"}, {"left": "Saturday", "right_image": "@@MEDIA@@sm3/ft/act_baking.webp", "right": "bake a cake"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'video', replace($blk${"title": "Аудио к заданию «выбери подходящую картинку»", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай аудио и выбери подходящую картинку", "questions": [{"q": "Which sport does John like?", "type": "single", "options": [{"image": "@@MEDIA@@sm3/ft/opt_football.webp"}, {"image": "@@MEDIA@@sm3/ft/opt_tennis.webp"}, {"image": "@@MEDIA@@sm3/ft/opt_swimming.webp"}], "correct": [1]}, {"q": "How did Jack go to school yesterday?", "type": "single", "options": [{"image": "@@MEDIA@@sm3/ft/opt_walking.webp"}, {"image": "@@MEDIA@@sm3/ft/opt_school_bus.webp"}, {"image": "@@MEDIA@@sm3/ft/opt_bicycle.webp"}], "correct": [1]}, {"q": "Where’s Vicky?", "type": "single", "options": [{"image": "@@MEDIA@@sm3/ft/opt_kitchen.webp"}, {"image": "@@MEDIA@@sm3/ft/opt_bedroom.webp"}, {"image": "@@MEDIA@@sm3/ft/opt_garden.webp"}], "correct": [2]}, {"q": "How old is Jim?", "type": "single", "options": [{"image": "@@MEDIA@@sm3/ft/cake_7.webp"}, {"image": "@@MEDIA@@sm3/ft/cake_9.webp"}, {"image": "@@MEDIA@@sm3/ft/cake_10.webp"}], "correct": [1]}, {"q": "What did Nick get for his birthday?", "type": "single", "options": [{"image": "@@MEDIA@@sm3/ft/gift_bicycle.webp"}, {"image": "@@MEDIA@@sm3/ft/gift_puppy.webp"}, {"image": "@@MEDIA@@sm3/ft/gift_console.webp"}], "correct": [1]}, {"q": "What’s in the bowl?", "type": "single", "options": [{"image": "@@MEDIA@@sm3/ft/bowl_fruit.webp"}, {"image": "@@MEDIA@@sm3/ft/bowl_soup.webp"}, {"image": "@@MEDIA@@sm3/ft/bowl_salad.webp"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<h3>READING &amp; WRITING</h3>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай предложения и заполни пропуски", "mode": "drag", "text": "1. You can eat this food in a sandwich. __cheese__\n2. This is a part of your body. All food and drinks go there first. __a stomach__\n3. You can have this brown drink hot or cold. Some people put milk in it. __coffee__\n4. People sit inside here and watch films. __a cinema__\n5. This animal is clever. It swims and jumps in the water. __a dolphin__\n6. We eat it for lunch, it is hot with vegetables and meat. __soup__\n7. You can use it to travel between floors in the building. __a lift__"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'truefalse', replace($blk${"title": "Посмотри на картинку и выбери «верно» или «неверно». hold — держать · scarf — шарф · curly — кудрявый · skip — прыгать на скакалке", "image": "@@MEDIA@@sm3/ft/scene_house.webp", "statements": [{"text": "The woman in the garden is holding a kite.", "answer": true}, {"text": "The window which is above the door is round.", "answer": true}, {"text": "The boy with the scarf has curly hair.", "answer": true}, {"text": "The man on the balcony is taller than the woman who is next to him.", "answer": false}, {"text": "The girl who is wearing a red sweater is skipping.", "answer": true}, {"text": "There are some birds on top of the house.", "answer": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p>Прочитай текст и заполни пропуски в задании ниже. <i>take off — снимать</i></p><p><img src=\"@@MEDIA@@sm3/ft/reading_jim_story.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай и впиши пропущенные слова", "text": "1. Jim and his mother ate __a cake|some cake|cake__ in the kitchen.\n2. Jim’s father was in the __living room|the living room__.\n3. The clown __smiled__ at Jim.\n4. The clown was Jim’s __dad|father|Dad|daddy__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Это конец итогового теста!</h3><p>Ты прошёл весь курс Super Minds 3 — это целый год работы. Поздравляю!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
