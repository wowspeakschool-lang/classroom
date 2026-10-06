-- Go Getter 1 · Unit 6 · My day · Homework 7
-- собрано tools/gg1_build.py --lesson u6_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · My day', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · My day');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · My day';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Сегодня мы закрепим знания, полученные в этом месяце. На следующем занятии тебя ждёт тест, и сегодня мы будем к нему готовиться вместе.</p><p>В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых сильных учеников 💪</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски недостающими по смыслу словами. Посмотри на пример под номером 0", "mode": "drag", "image": "@@MEDIA@@gg1/u6/girl_routine.webp", "text": "0. In the morning I get up at 7 o'clock.\n1. We __have__ lessons all day.\n2. After school, I __hang__ out with friends.\n3. We __play__ computer games on Saturdays.\n4. Before bed, I __watch__ TV.\n5. At night, I __go__ to bed at 9 o'clock."}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на слова и впиши пропущенное. Посмотри на пример под номером 0", "mode": "type", "text": "0. January — February — March\n1. July — __August__ — September\n2. Friday — __Saturday__ — Sunday\n3. October — __November__ — December\n4. March — __April__ — May\n5. Tuesday — __Wednesday__ — Thursday"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай предложения и выбери правильный вариант. Пример: Tom gets up early.", "questions": [{"q": "We ___ to a big school.", "type": "single", "options": [{"text": "goes"}, {"text": "go"}, {"text": "gos"}], "correct": [1]}, {"q": "Sally ___ chocolate ice cream.", "type": "single", "options": [{"text": "liks"}, {"text": "like"}, {"text": "likes"}], "correct": [2], "image": "@@MEDIA@@gg1/u6/obj_ice_cream_chocolate.webp"}, {"q": "Harry ___ his room on Sundays.", "type": "single", "options": [{"text": "tidies"}, {"text": "tidys"}, {"text": "tidy"}], "correct": [0]}, {"q": "They ___ their homework in the living room.", "type": "single", "options": [{"text": "does"}, {"text": "do"}, {"text": "dos"}], "correct": [1]}, {"q": "I ___ lunch in the park.", "type": "single", "options": [{"text": "has"}, {"text": "haves"}, {"text": "have"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["I", "am", "always", "busy."], "sentence": "I am always busy.", "audio_tts": "I am always busy.", "image": "@@MEDIA@@gg1/u6/obj_busy_planner.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["We", "often", "play", "tennis."], "sentence": "We often play tennis.", "audio_tts": "We often play tennis.", "image": "@@MEDIA@@gg1/u6/obj_tennis.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Mom", "never", "watches", "TV."], "sentence": "Mom never watches TV.", "audio_tts": "Mom never watches TV.", "image": "@@MEDIA@@gg1/u6/da_watch_tv.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["I", "sometimes", "tidy", "my", "room."], "sentence": "I sometimes tidy my room.", "audio_tts": "I sometimes tidy my room.", "image": "@@MEDIA@@gg1/u6/da_tidy_my_room.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Jess", "is", "usually", "late."], "sentence": "Jess is usually late.", "audio_tts": "Jess is usually late.", "image": "@@MEDIA@@gg1/u6/obj_late_clock.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'gaps', replace($blk${"title": "Дополнительное задание ⭐ Прочитай диалоги и вставь пропущенные по смыслу слова", "mode": "type", "image": "@@MEDIA@@gg1/u6/clock_1230.svg", "text": "1. A: What time is lunch? B: It's at half __past__ twelve.\n2. A: What time __is__ it? B: It's ten __minutes__ to five.\n3. A: What time is the film? B: It's __at__ six __o'clock|oclock__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'speaking', replace($blk${"title": "Моя неделя 🎤", "html": "<p>Нажми на микрофон и расскажи о своей типичной неделе.</p><p><i>Пример: On weekdays I always go to school. On Tuesday I usually have a music lesson. At the weekend I often hang out with my friends. I never get up early on Sunday.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Соедини картинку и фразу ⭐", "pairs": [{"left_image": "@@MEDIA@@gg1/u6/da_get_up.webp", "right": "get up", "right_audio_tts": "get up"}, {"left_image": "@@MEDIA@@gg1/u6/da_go_to_school.webp", "right": "go to school", "right_audio_tts": "go to school"}, {"left_image": "@@MEDIA@@gg1/u6/da_have_breakfast.webp", "right": "have breakfast", "right_audio_tts": "have breakfast"}, {"left_image": "@@MEDIA@@gg1/u6/da_have_a_shower.webp", "right": "have a shower", "right_audio_tts": "have a shower"}, {"left_image": "@@MEDIA@@gg1/u6/da_do_homework.webp", "right": "do my homework", "right_audio_tts": "do my homework"}, {"left_image": "@@MEDIA@@gg1/u6/da_hang_out_with_friends.webp", "right": "hang out with my friends", "right_audio_tts": "hang out with my friends"}, {"left_image": "@@MEDIA@@gg1/u6/da_go_to_bed.webp", "right": "go to bed", "right_audio_tts": "go to bed"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ⭐", "questions": [{"q": "She ___ up at 7 o'clock.", "type": "single", "options": [{"text": "get"}, {"text": "gets"}], "correct": [1]}, {"q": "My friends ___ football after school.", "type": "single", "options": [{"text": "play"}, {"text": "plays"}], "correct": [0]}, {"q": "Dad ___ the dishes after dinner.", "type": "single", "options": [{"text": "washs"}, {"text": "washes"}], "correct": [1]}, {"q": "You ___ lunch at school.", "type": "single", "options": [{"text": "have"}, {"text": "has"}], "correct": [0]}, {"q": "My cat ___ a lot.", "type": "single", "options": [{"text": "sleep"}, {"text": "sleeps"}], "correct": [1]}, {"q": "Ben ___ to music in his room.", "type": "single", "options": [{"text": "listens"}, {"text": "listen"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'match', replace($blk${"title": "Соедини наречие и перевод ⭐", "pairs": [{"left": "always", "right": "всегда", "left_audio_tts": "always"}, {"left": "usually", "right": "обычно", "left_audio_tts": "usually"}, {"left": "often", "right": "часто", "left_audio_tts": "often"}, {"left": "sometimes", "right": "иногда", "left_audio_tts": "sometimes"}, {"left": "never", "right": "никогда", "left_audio_tts": "never"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Уверена, ты справишься с тестом на все сто! Удачи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14);
end
$mig$;
