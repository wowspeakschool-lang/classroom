-- Super Minds 1 · Unit 5 · My week · Homework 5
-- собрано tools/sm1_build.py --lesson u5_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · My week', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · My week');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · My week';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Это новая домашняя работа. Сегодня тебя ждут много не совсем простых, но очень-очень интересных заданий! Ты познакомишься с новыми персонажами, а с одним даже пообщаешься 😉</p><p>Ну что, предлагаю начинать!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'sort', replace($blk${"title": "Начнём с интересного задания! Распредели слова по группам, чтобы получились выражения. Например: play the piano или go swimming.", "groups": [{"name": "PLAY", "items": [{"text": "hide-and-seek", "audio_tts": "play hide-and-seek"}, {"text": "with friends", "audio_tts": "play with friends"}, {"text": "with toys", "audio_tts": "play with toys"}, {"text": "computer games", "audio_tts": "play computer games"}]}, {"name": "WATCH", "items": [{"text": "TV", "audio_tts": "watch TV"}]}, {"name": "GO", "items": [{"text": "swimming", "audio_tts": "go swimming"}]}, {"name": "RIDE", "items": [{"text": "my horse", "audio_tts": "ride my horse"}, {"text": "my bike", "audio_tts": "ride my bike"}, {"text": "my pony", "audio_tts": "ride my pony"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Ты прекрасно справился с предыдущим заданием! А вот и следующее — соедини одну часть предложения со второй. Думаю, у тебя получится 😉", "pairs": [{"left": "On Saturdays I play the", "right": "piano", "right_audio_tts": "On Saturdays I play the piano."}, {"left": "On Sundays I watch", "right": "TV", "right_audio_tts": "On Sundays I watch TV."}, {"left": "On Mondays I play with", "right": "friends", "right_audio_tts": "On Mondays I play with friends."}, {"left": "On Thursdays I go", "right": "swimming", "right_audio_tts": "On Thursdays I go swimming."}, {"left": "On Tuesdays I ride", "right": "my bike", "right_audio_tts": "On Tuesdays I ride my bike."}, {"left": "On Wednesdays I play", "right": "computer games", "right_audio_tts": "On Wednesdays I play computer games."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p>Мы с тобой сейчас познакомимся с Милой и узнаем, как проходит её неделя.</p><p>Она тебе написала письмо, давай прочитаем его!</p><p><img src=\"@@MEDIA@@sm1/u5/hw5_mila_letter.webp\" alt=\"\" style=\"max-width:660px;width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "Ответное письмо Миле ✉️", "needs_review": true, "html": "<p>А теперь давай напишем ответное письмо Миле.</p><p>Ты можешь написать его в окошке здесь. А если тебе неудобно печатать текст, можешь написать его от руки и прислать фото.</p><p>Начни, пожалуйста, письмо с таких слов: <i>Hello, Mila! My name is … This is my week!</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "⭐ Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Впиши по-английски: смотреть телевизор", "accept": ["watch TV", "watch tv", "Watch TV"]}, {"prompt": "кататься на велосипеде", "accept": ["ride a bike", "ride my bike", "Ride a bike"]}, {"prompt": "играть на пианино", "accept": ["play the piano", "Play the piano"]}, {"prompt": "играть в прятки", "accept": ["play hide-and-seek", "play hide and seek", "Play hide-and-seek"]}, {"prompt": "заниматься плаванием", "accept": ["go swimming", "Go swimming"]}, {"prompt": "играть в компьютерные игры", "accept": ["play computer games", "Play computer games"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "⭐ Составь предложение из письма Милы", "words": ["On", "Mondays", "I", "watch", "TV", "for", "two", "hours."], "sentence": "On Mondays I watch TV for two hours.", "audio_tts": "On Mondays I watch TV for two hours."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "⭐ Составь предложение из письма Милы", "words": ["I", "play", "tennis", "for", "one", "hour."], "sentence": "I play tennis for one hour.", "audio_tts": "I play tennis for one hour."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "⭐ Составь предложение из письма Милы", "words": ["On", "Saturdays", "and", "Sundays", "I", "do", "nothing!"], "sentence": "On Saturdays and Sundays I do nothing!", "audio_tts": "On Saturdays and Sundays I do nothing!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ого! Вот это здорово!</h3><p>Как много заданий ты сделал сегодня. Ты потрудился на славу.</p><p>Ты самый-самый лучший ученик на свете. Молодец ⭐</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
