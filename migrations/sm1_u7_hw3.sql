-- Super Minds 1 · Unit 7 · Get dressed · Homework 3
-- собрано tools/sm1_build.py --lesson u7_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · Get dressed', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · Get dressed');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · Get dressed';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание! 👋</h2><p>Впереди тебя ждут несколько интересных видео и увлекательных упражнений, а также 1 дополнительное задание, которое можно выполнить по желанию.</p><p>За каждое задание ты будешь получать ⭐️. Собери максимальное количество звёздочек и стань ЧЕМПИОНОМ!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p><p><img src=\"@@MEDIA@@sm1/u7/grammar_is_he_wearing.webp\" alt=\"Grammar 2 — Is he/she wearing …?\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Мы начнём с видео, но прежде чем смотреть, как думаешь, во что одеты главные персонажи видео? A T-shirt? A skirt? A cap?</p><p>Теперь посмотри видео один раз, внимательно слушай, что говорит персонаж, и проверь себя — угадал ли ты?</p><p>Затем посмотри видео снова и повторяй за персонажами.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "Видео 1: She's wearing a pink jumper and a purple skirt", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'match', replace($blk${"title": "Сейчас посмотри видео ещё раз и соедини предложения и подходящие картинки! За это задание ты получишь 1 ⭐️.", "pairs": [{"left": "He's wearing a white T-shirt.", "left_audio_tts": "He's wearing a white T-shirt.", "right": "Darius", "right_image": "@@MEDIA@@sm1/u7/char_darius.webp"}, {"left": "She's wearing a pink jumper.", "left_audio_tts": "She's wearing a pink jumper.", "right": "Mabel", "right_image": "@@MEDIA@@sm1/u7/char_mabel_card.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p>Посмотри ещё одно видео. Но сначала посмотри на картинку и угадай, о каких персонажах будем смотреть видео.</p><p><img src=\"@@MEDIA@@sm1/u7/gf_family_party.webp\" alt=\"\" style=\"max-width:480px\"></p><p>Теперь посмотри видео один раз и проверь себя — угадал ли ты?</p><p>Затем посмотри видео снова и повторяй за персонажами.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'video', replace($blk${"title": "Видео 2: Gravity Falls", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'match', replace($blk${"title": "Сейчас посмотри видео ещё раз и соедини вопрос с правильным ответом. Так ты сможешь получить ещё 1 ⭐️.", "pairs": [{"left": "Is Dipper wearing a cap?", "right": "Yes, he is.", "right_audio_tts": "Yes, he is."}, {"left": "Is Mabel wearing a yellow sweater?", "right": "No, she isn’t.", "right_audio_tts": "No, she isn't."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:140px\"></p><p>Молодец!</p><p>Теперь время практики. Внизу ты найдёшь картинку с одеждой четырёх ребят. Прослушай аудио и соедини имена с одеждой. Это задание оценивается в целых 2 ⭐️⭐️.</p>", "audio": "", "audio_tts": "Kate is wearing a red sweater, a white skirt and red boots. Tom is wearing a black coat, a white shirt and black jeans. Any is wearing a pink sweater and a red skirt. Sam is wearing a grey T-shirt, red shorts and a cap."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'match', replace($blk${"title": "Прослушай аудио и отметь, где чья одежда (соедини имя и картинку).", "pairs": [{"left": "Kate", "right": "одежда Kate", "right_image": "@@MEDIA@@sm1/u7/outfit_kate.webp"}, {"left": "Tom", "right": "одежда Tom", "right_image": "@@MEDIA@@sm1/u7/outfit_tom.webp"}, {"left": "Any", "right": "одежда Any", "right_image": "@@MEDIA@@sm1/u7/outfit_any.webp"}, {"left": "Sam", "right": "одежда Sam", "right_image": "@@MEDIA@@sm1/u7/outfit_sam.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p>Отлично! Ты справился с большей частью заданий. Ты — молодец.</p><p>Посмотри ещё раз на картинку из предыдущего задания и ответь на вопросы ниже. За это задание ты получишь 2 ⭐️⭐️.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'quiz', replace($blk${"title": "Ответь на вопросы", "questions": [{"q": "Is Tom wearing a grey T-shirt?", "type": "single", "image": "@@MEDIA@@sm1/u7/hw3_four_outfits.webp", "options": [{"text": "Yes, he is."}, {"text": "No, he isn't."}], "correct": [1]}, {"q": "Is Kate wearing a white skirt?", "type": "single", "image": "@@MEDIA@@sm1/u7/hw3_four_outfits.webp", "options": [{"text": "No, she isn't."}, {"text": "Yes, she is."}], "correct": [1]}, {"q": "Is Sam wearing a cap?", "type": "single", "image": "@@MEDIA@@sm1/u7/hw3_four_outfits.webp", "options": [{"text": "Yes, he is."}, {"text": "No, he isn't."}], "correct": [0]}, {"q": "Is Any wearing a red sweater?", "type": "single", "image": "@@MEDIA@@sm1/u7/hw3_four_outfits.webp", "options": [{"text": "Yes, she is."}, {"text": "No, she isn't."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "Опиши одного из героев 🎤", "needs_review": true, "image": "@@MEDIA@@sm1/u7/gf_mabel_dipper.webp", "sample": "", "sample_tts": "This is Mabel. She is wearing a pink sweater and a purple skirt.", "html": "<p>Посмотри на картинку. На ней герои мультфильма Gravity Falls — Mabel и Dipper. Опиши одного из героев.</p><p>Сначала послушай пример ответа.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'gaps', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Заполни пропуски: is или isn't.", "text": "1. __Is__ Dipper wearing a cap? — Yes, he is.\n2. Is Mabel wearing a yellow sweater? — No, she __isn't|isn’t|is not__.\n3. Darius __is__ wearing a white T-shirt.\n4. Is Mabel wearing a purple skirt? — Yes, she __is__.\n5. Is Dipper wearing a dress? — No, he __isn't|isn’t|is not__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'order', replace($blk${"words": ["Is", "Mabel", "wearing", "a", "pink", "sweater?"], "sentence": "Is Mabel wearing a pink sweater?", "audio_tts": "Is Mabel wearing a pink sweater?", "image": "@@MEDIA@@sm1/u7/char_mabel_card.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'order', replace($blk${"words": ["He", "is", "wearing", "a", "white", "T-shirt."], "sentence": "He is wearing a white T-shirt.", "audio_tts": "He is wearing a white T-shirt.", "image": "@@MEDIA@@sm1/u7/char_darius.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 15),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание, ты молодец!</h3><p>Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 16);
end
$mig$;
