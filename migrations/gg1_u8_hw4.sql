-- Go Getter 1 · Unit 8 · Sport and health · Homework 4
-- собрано tools/gg1_build.py --lesson u8_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · Sport and health', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · Sport and health');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · Sport and health';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Добро пожаловать на домашнее задание! Сегодня мы с тобой закрепим знания, полученные на уроке, и ты без проблем сможешь говорить о погоде. В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых сильных учеников 💪</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u8/card_weather.webp\" alt=\"Weather\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Внимательно посмотри видео и постарайся запомнить, как правильно говорить о погоде на английском. Повторяй фразы за видео!", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Сопоставь страны и прогнозы погоды из видео", "pairs": [{"left": "Russia", "right_image": "@@MEDIA@@gg1/u8/weather_cold.webp"}, {"left": "Mexico", "right_image": "@@MEDIA@@gg1/u8/weather_warm.webp"}, {"left": "Japan", "right_image": "@@MEDIA@@gg1/u8/weather_cloudy.webp"}, {"left": "Australia", "right_image": "@@MEDIA@@gg1/u8/weather_hot.webp"}, {"left": "France", "right_image": "@@MEDIA@@gg1/u8/weather_rainy.webp"}, {"left": "England", "right_image": "@@MEDIA@@gg1/u8/weather_foggy.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'sequence', replace($blk${"title": "Расставь предложения в правильном порядке так, чтобы получился складный диалог", "image": "@@MEDIA@@gg1/u8/mandy_phone.webp", "items": [{"text": "Hi, Mandy. Is the weather nice in Scotland?"}, {"text": "No, it isn't. It's rainy and cold!"}, {"text": "Oh dear. That's horrible."}, {"text": "Yes, it's really horrible. What's the weather like in France?"}, {"text": "It's cold and snowy here."}, {"text": "Well, I hope it's snowy in Scotland too!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Соедини предложения по смыслу: какие занятия и действия подойдут к какой погоде", "pairs": [{"left": "It's hot.", "right": "Let's go swimming."}, {"left": "It's very cold.", "right": "Let's go skiing."}, {"left": "It's windy.", "right": "Let's go sailing."}, {"left": "It's rainy and wet.", "right": "Wear a coat."}, {"left": "It's snowy.", "right": "Wear your boots."}, {"left": "It's warm.", "right": "Wear a T-shirt."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'hotspot', replace($blk${"title": "Давай-ка вспомним времена года! Подпиши каждое деревце", "mode": "label", "image": "@@MEDIA@@gg1/u8/four_trees.webp", "points": [{"x": 22.0, "y": 22.0, "text": "spring"}, {"x": 76.0, "y": 22.0, "text": "summer"}, {"x": 22.0, "y": 70.0, "text": "autumn"}, {"x": 76.0, "y": 70.0, "text": "winter"}], "extras": []}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'gaps', replace($blk${"title": "И последнее задание на сегодня! Прочитай диалог и расставь слова по смыслу. Ты справишься!", "mode": "drag", "text": "A: Hi, __what__'s the weather __like__ in New York today?\nB: It's windy and __rainy__. I've got an umbrella!\nA: I hate getting __wet__!\nB: Me too! I __hope__ it's sunny and __warm__ tomorrow."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'speaking', replace($blk${"title": "Погода 🎤", "html": "<p>Нажми на микрофон и расскажи о погоде сегодня и о погоде в твоё любимое время года.</p><p><i>Пример: Today it's warm and sunny. My favourite season is summer. In summer it's hot and sunny. I love it! In winter it's cold and snowy.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
