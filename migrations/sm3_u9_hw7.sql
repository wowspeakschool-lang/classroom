-- Super Minds 3 · Unit 9 · Weather · Homework 7
-- собрано tools/sm3_build.py --lesson u9_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 9 · Weather', 9
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 9 · Weather');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 9 · Weather';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>В этом уроке тебя ждут классные упражнения! Выполни все задания, если хочешь стать чемпионом английского!</p><p>В дополнение к этому домашнему заданию идёт дополнительное! Его можно выполнить по желанию, НО если ты его выполнишь, то будешь мега крут!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Давай вспомним, о чём мы говорили на уроке, и прочитаем текст!</h3><p>Ответь на вопрос: Did people go on holiday by plane or by train?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u9/reading_100_years.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sort', replace($blk${"title": "Внимательно посмотри на фразы и распредели их по категориям: Did people have it 100 years ago?", "groups": [{"name": "Yes", "items": [{"text": "puppet show"}, {"text": "donkey ride"}, {"text": "steam train"}, {"text": "swimming boots"}, {"text": "ice-cream cart"}, {"text": "crowded beach"}, {"text": "picnic basket"}]}, {"name": "No", "items": [{"text": "electric train"}, {"text": "flip-flops"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Отлично! Ты почти справился с домашним заданием. Следующее задание — прочитай письмо и заполни пропуски подходящими словами", "mode": "drag", "text": "Dear Elsa,\nThank you for your letter. You asked what I did on my holiday last week. Well, we went to Brighton beach. The steam train was comfortable but very noisy. It is better than travelling by horse though. There were so many people at the beach – it was very __crowded__. I was upset because I bought new __swimming boots__, but I couldn’t wear them! We couldn’t have a picnic there either, so we went to Victoria Park. Mum brought a __picnic basket__ filled with sandwiches, lemonade and fruit. Then Uncle Joe bought us some ice-cream from the __cart__. It was delicious. In the afternoon we saw a __puppet show__ with Punch and Judy and I liked it. I didn’t go on the __donkey rides__ because I’m afraid of them.\nWe are going to take the train to Manchester to see Aunt Emma next week. Are you going to be there?\nYours truly,\nSandra"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ — отпуск в прошлом", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@sm3/u9/example_holiday_diary.webp\" alt=\"\" style=\"max-width:100%\"></p><p>Ты большой молодец и выполнил основную часть домашнего задания, супер!</p><p>Представь, что ты отправился в отпуск в прошлое. Опиши своё путешествие! Эти вопросы помогут тебе:</p><p>1. Where were you?<br>2. How did you travel there?<br>3. What did you do there?</p><p>Посмотри на картинку и текст выше — воспользуйся ими как примером. Удачи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа — первая часть позади!</h3><p>Во второй части тебя ждут упражнения на повторение всего, что мы успели пройти за прошедший месяц.</p><p>Для начала посмотри видео ниже. Как ты думаешь, какой питомец отправится к ветеринару — a cat or a dog? Watch and check!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'video', replace($blk${"title": "Видео: going to — планы", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'match', replace($blk${"title": "Отлично, ты посмотрел видео! Теперь соедини предложения с картинками по смыслу", "pairs": [{"left": "I’m going to buy a car.", "right_image": "@@MEDIA@@sm3/u9/going_buy_car.webp", "right": "car"}, {"left": "She is going to take her dog to the vet.", "right_image": "@@MEDIA@@sm3/u9/going_vet.webp", "right": "vet"}, {"left": "He’s going to take piano lessons.", "right_image": "@@MEDIA@@sm3/u9/going_play_piano.webp", "right": "piano"}, {"left": "We’re going to order pizza for dinner.", "right_image": "@@MEDIA@@sm3/u9/going_order_pizza.webp", "right": "pizza"}, {"left": "The student’s going to watch TV tonight.", "right_image": "@@MEDIA@@sm3/u9/going_watch_tv.webp", "right": "TV"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'gaps', replace($blk${"title": "Итак, приступим к практике! Внимательно посмотри на слова: not rain · cook · build · phone · not have. Их нужно вставить в предложения и поставить в правильную форму. Посмотри на пример в предложении 1", "text": "1. I’m going to phone Lisa this evening.\n2. It __isn’t going to rain|isn't going to rain|is not going to rain__ this afternoon.\n3. You’re __going to cook__ dinner.\n4. We __aren’t going to have|aren't going to have|are not going to have__ fish and chips for dinner.\n5. Dad’s __going to build__ a tree house."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["Are", "you", "going", "to", "do", "homework", "this", "evening?"], "sentence": "Are you going to do homework this evening?", "audio_tts": "Are you going to do homework this evening?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"words": ["Are", "you", "going", "to", "go", "swimming", "this", "weekend?"], "sentence": "Are you going to go swimming this weekend?", "audio_tts": "Are you going to go swimming this weekend?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'order', replace($blk${"words": ["What", "are", "you", "going", "to", "do", "after", "school?"], "sentence": "What are you going to do after school?", "audio_tts": "What are you going to do after school?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'order', replace($blk${"words": ["Are", "you", "going", "to", "go", "to bed", "early", "tonight?"], "sentence": "Are you going to go to bed early tonight?", "audio_tts": "Are you going to go to bed early tonight?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'gaps', replace($blk${"title": "Ура, ты на финишной прямой! Поставь слова в скобках в правильную форму и впиши её в пропуски. Пиши внимательно и обязательно проверь себя!", "text": "1. Are you going to visit your grandparents this weekend? (visit)\n2. Is he __going to sleep__ at your house tonight? (sleep)\n3. Are your mum and dad __going to help__ you with your school project? (help)\n4. Is your sister __going to give__ you a birthday present? (give)\n5. Are we __going to have__ pizza tonight? (have)"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'speaking', replace($blk${"title": "ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ — ответь голосом", "sample": "", "html": "<p>Внимательно прочитай вопросы ниже. Твоя задача — ответить на них голосовым сообщением!</p><p>1. Are you going to go swimming this weekend?<br>2. What are you going to do after school?<br>3. Are you going to visit your grandparents this weekend?<br>4. Are you going to go to bed early tonight?<br>5. What are you going to do this weekend?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 15),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание и теперь готов к уроку. Ты — СУПЕР КРУТ!</h3><p>Жду тебя на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 16);
end
$mig$;
