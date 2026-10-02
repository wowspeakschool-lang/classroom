-- Super Minds 3 · Unit 2 · Food · Homework 2
-- собрано tools/sm3_build.py --lesson u2_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · Food', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · Food');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · Food';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет!</h2><p>Ну что, готов к новой домашней работе? Она тебя уже ждёт. Давай начинать!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Посмотри видео и найди ответ на вопрос: What are they cooking? 🍰", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "What are they cooking?", "type": "single", "options": [{"text": "cupcakes"}, {"text": "candies"}, {"text": "a cake"}, {"text": "a pizza"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Соедини картинку с описанием 🧾", "pairs": [{"left_image": "@@MEDIA@@sm3/u2/tray_potatoes_peas_onions.webp", "right": "There are some potatoes. There are some peas. There are some onions."}, {"left_image": "@@MEDIA@@sm3/u2/tray_milk_lemonade_juice.webp", "right": "There is some milk. There is some lemonade. There is some orange juice."}, {"left_image": "@@MEDIA@@sm3/u2/tray_biscuits_cake_chocolate.webp", "right": "There are some biscuits. There is some cake. There is some chocolate."}, {"left_image": "@@MEDIA@@sm3/u2/tray_cake_biscuits_sandwiches.webp", "right": "There is some cake. There are some biscuits. There are some sandwiches."}, {"left_image": "@@MEDIA@@sm3/u2/tray_peas_potatoes_nuts.webp", "right": "There are some peas. There are some potatoes. There are some nuts."}, {"left_image": "@@MEDIA@@sm3/u2/tray_water_juice_milk.webp", "right": "There is some water. There is some apple juice. There is some milk."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай диалог и вставь some или any", "mode": "drag", "image": "@@MEDIA@@sm3/u2/lunchbox_roll_water.webp", "text": "Kate: Guess what’s in my lunch box!\nAlice: There’s __some__ bread. I think there’s a roll.\nKate: That’s right. What’s in it?\nAlice: Is there __any__ chicken?\nKate: No, there isn’t. I don’t like chicken.\nAlice: OK, there isn’t __any__ chicken. Is there __any__ cheese?\nKate: Cheese? Yes, there is. I love cheese.\nAlice: Is there anything else in your lunch box?\nKate: Yes, there’s __some__ water too."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "Напиши к каждому предложению вопрос и отрицание", "needs_review": true, "html": "<p><i>Образец:</i><br>There is some cheese.<br>Is there any cheese?<br>There isn’t any cheese.</p><ol><li>There are some rolls.</li><li>There is some salad.</li><li>There are some vegetables.</li><li>There is some soup.</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'speaking', replace($blk${"title": "Посмотри на картинку и расскажи, что на ней есть, а чего нет 🎤", "needs_review": true, "image": "@@MEDIA@@sm3/u2/scene_picnic.webp", "html": "<p>Используй <b>there is</b> / <b>there are</b> и <b>there isn’t</b> / <b>there aren’t</b>.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'match', replace($blk${"title": "Соедини картинку с описанием корзинки хозяина 🍎 🥦 🥕", "pairs": [{"left_image": "@@MEDIA@@sm3/u2/basket_vegetables_only.webp", "right": "There are some vegetables in my basket, but there isn’t any fruit."}, {"left_image": "@@MEDIA@@sm3/u2/basket_fruit_only.webp", "right": "There’s some fruit in my basket, but there aren’t any vegetables."}, {"left_image": "@@MEDIA@@sm3/u2/basket_mixed.webp", "right": "There’s some fruit and there are some vegetables in my basket."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'gaps', replace($blk${"title": "Корзинка Дэйзи: вставь some или any, is или are", "mode": "drag", "image": "@@MEDIA@@sm3/u2/basket_bananas_juice.webp", "text": "__Are__ there __any__ bananas in your basket? Yes, there __are__ __some__ bananas.\n__Is__ there __any__ apple juice in your basket? Yes, there __is__ __some__ apple juice.\n__Are__ there __any__ tomatoes? No, there __aren’t__ __any__ tomatoes."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'gaps', replace($blk${"title": "Песня про пикник: впиши продукты из списка ребят", "mode": "drag", "text": "Let’s make a picnic!\nIt’s going to be such fun.\nWe’re going to go shopping,\nFor a picnic in the sun.\nAre there any __tomatoes__?\nIs there any __jam__?\nYes, there are lots of yummy things,\nFor me and my friend Pam!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'task', replace($blk${"title": "Второй куплет придумай сам", "needs_review": true, "html": "<p>Впиши те продукты, которые пригодятся на пикнике тебе:</p><p><i>Are there any …?<br>Is there any …?<br>Yes, there are lots of yummy things,<br>These sandwiches look good!</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Спасибо тебе большое за твои старания!</h3><p>Ты огромный молодец. Увидимся на уроке 😊</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
