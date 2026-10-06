-- Go Getter 1 · Unit 6 · My day · Homework 3
-- собрано tools/gg1_build.py --lesson u6_hw3
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
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Сегодня мы закрепим знания, полученные на уроке, и ты без проблем сможешь использовать разные наречия, чтобы говорить о том, как часто что-то происходит.</p><p>В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых сильных учеников 💪</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u6/card_adverbs.webp\" alt=\"Adverbs of frequency\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@gg1/u6/card_days.webp\" alt=\"Days of the week\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Ребята рассказывают, как они обычно проводят выходные. Посмотри на картинку и попробуй угадать: <b>How often does Hammy play computer games?</b></p><p><img src=\"@@MEDIA@@gg1/u6/hammy_weekend.webp\" alt=\"Hammy\" style=\"height:240px\"></p><p>Посмотри видео и проверь, угадал ли ты. Повторяй вопросы и ответы за героями, чтобы хорошенько запомнить правила.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "Max and Hammy: at the weekend", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на таблицу и на кружочки: сколько закрашено, так часто это бывает. Впиши нужное слово", "mode": "drag", "image": "@@MEDIA@@gg1/u6/adverbs_table.webp", "text": "1. Jack sometimes cycles to school. 🔴⚪⚪⚪ (пример)\n2. Emma __always__ has breakfast at home. 🔴🔴🔴🔴\n3. Pete __usually__ does his homework in his bedroom. 🔴🔴🔴⚪\n4. I __sometimes__ play in the park. 🔴⚪⚪⚪\n5. We __never__ watch TV in the morning. ⚪⚪⚪⚪\n6. My parents __often__ go out with their friends. 🔴🔴⚪⚪"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке. Подсказка — на карточке выше 👆", "words": ["I'm", "often", "busy", "on", "Saturdays."], "sentence": "I'm often busy on Saturdays.", "audio_tts": "I'm often busy on Saturdays."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Kit", "often", "helps", "me", "at", "home."], "sentence": "Kit often helps me at home.", "audio_tts": "Kit often helps me at home."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Uncle Roberto", "sometimes", "visits", "me."], "sentence": "Uncle Roberto sometimes visits me.", "audio_tts": "Uncle Roberto sometimes visits me."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["I", "never", "cook", "dinner."], "sentence": "I never cook dinner.", "audio_tts": "I never cook dinner."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Kit", "is", "always", "happy."], "sentence": "Kit is always happy.", "audio_tts": "Kit is always happy."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Kit", "and I", "usually", "have", "fun."], "sentence": "Kit and I usually have fun.", "audio_tts": "Kit and I usually have fun."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'sequence', replace($blk${"title": "Ты уже на финишной прямой! Расставь дни недели в правильном порядке 👏", "items": [{"text": "Monday"}, {"text": "Tuesday"}, {"text": "Wednesday"}, {"text": "Thursday"}, {"text": "Friday"}, {"text": "Saturday"}, {"text": "Sunday"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'task', replace($blk${"title": "Как часто? ✍️", "needs_review": true, "html": "<p>Напиши 3 предложения о себе: как часто ты что-то делаешь?</p><p><i>Посмотри, это мои предложения: I usually get up at 9 o'clock. I sometimes watch TV in the evening. I am never late for the train.</i></p><p>Удачи, у тебя всё получится!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Соедини наречие и то, как часто это бывает ⭐", "pairs": [{"left": "always", "right": "100% — всегда", "left_audio_tts": "always"}, {"left": "usually", "right": "75% — обычно", "left_audio_tts": "usually"}, {"left": "often", "right": "50% — часто", "left_audio_tts": "often"}, {"left": "sometimes", "right": "25% — иногда", "left_audio_tts": "sometimes"}, {"left": "never", "right": "0% — никогда", "left_audio_tts": "never"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["I", "always", "have", "breakfast."], "sentence": "I always have breakfast.", "audio_tts": "I always have breakfast."}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["She", "usually", "goes", "to", "school", "by", "bus."], "sentence": "She usually goes to school by bus.", "audio_tts": "She usually goes to school by bus."}$blk$, '@@MEDIA@@', v_media)::jsonb, 15),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["He", "is", "never", "late."], "sentence": "He is never late.", "audio_tts": "He is never late."}$blk$, '@@MEDIA@@', v_media)::jsonb, 16),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 17);
end
$mig$;
