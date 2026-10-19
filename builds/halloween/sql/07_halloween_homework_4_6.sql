-- HOLIDAYS · Halloween · Halloween Homework · 4–6
do $mig$
declare
  v_course uuid; v_unit uuid; v_lesson uuid;
  v_media text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'holidays';
  if v_course is null then raise exception 'course holidays not found'; end if;

  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Halloween' limit 1;
  if v_unit is null then
    insert into classroom_units (course_id, title, sort_order)
    values (v_course, 'Halloween', 1) returning id into v_unit;
  end if;

  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Halloween Homework · 4–6' limit 1;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, summary, sort_order, is_published, pass_threshold, kind)
    values (v_unit, 'Halloween Homework · 4–6', 'Хэллоуин: ghost, bat, spider, monster', 10, false, 60, 'homework')
    returning id into v_lesson;
  else
    update classroom_lessons set summary = 'Хэллоуин: ghost, bat, spider, monster', sort_order = 10,
           is_published = false, pass_threshold = 60, kind = 'homework'
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    -- блок 1 (sort_order 0)
    (v_lesson, 'flashcards', replace($blk${"title": "Посмотри карточки, послушай и повтори", "cards": [{"text": "ghost", "image": "@@MEDIA@@halloween/4-6/word_ghost.webp", "audio_tts": "ghost"}, {"text": "bat", "image": "@@MEDIA@@halloween/4-6/word_bat.webp", "audio_tts": "bat"}, {"text": "spider", "image": "@@MEDIA@@halloween/4-6/word_spider.webp", "audio_tts": "spider"}, {"text": "monster", "image": "@@MEDIA@@halloween/4-6/word_monster.webp", "audio_tts": "monster"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    -- блок 2 (sort_order 1)
    (v_lesson, 'quiz', replace($blk${"title": "🔊 Послушай и выбери картинку", "questions": [{"q": "", "type": "single", "audio_tts": "ghost", "correct": [1], "options": [{"text": "monster", "image": "@@MEDIA@@halloween/4-6/word_monster.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/4-6/word_ghost.webp"}, {"text": "bat", "image": "@@MEDIA@@halloween/4-6/word_bat.webp"}]}, {"q": "", "type": "single", "audio_tts": "bat", "correct": [1], "options": [{"text": "monster", "image": "@@MEDIA@@halloween/4-6/word_monster.webp"}, {"text": "bat", "image": "@@MEDIA@@halloween/4-6/word_bat.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/4-6/word_ghost.webp"}]}, {"q": "", "type": "single", "audio_tts": "monster", "correct": [0], "options": [{"text": "monster", "image": "@@MEDIA@@halloween/4-6/word_monster.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/4-6/word_ghost.webp"}, {"text": "spider", "image": "@@MEDIA@@halloween/4-6/word_spider.webp"}]}, {"q": "", "type": "single", "audio_tts": "spider", "correct": [1], "options": [{"text": "monster", "image": "@@MEDIA@@halloween/4-6/word_monster.webp"}, {"text": "spider", "image": "@@MEDIA@@halloween/4-6/word_spider.webp"}, {"text": "bat", "image": "@@MEDIA@@halloween/4-6/word_bat.webp"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    -- блок 3 (sort_order 2) · вместо игры «найди пару»
    (v_lesson, 'match', replace($blk${"title": "Найди одинаковые картинки и назови их", "pairs": [{"left_image": "@@MEDIA@@halloween/4-6/word_ghost.webp", "right": "ghost", "right_image": "@@MEDIA@@halloween/4-6/word_ghost.webp"}, {"left_image": "@@MEDIA@@halloween/4-6/word_bat.webp", "right": "bat", "right_image": "@@MEDIA@@halloween/4-6/word_bat.webp"}, {"left_image": "@@MEDIA@@halloween/4-6/word_spider.webp", "right": "spider", "right_image": "@@MEDIA@@halloween/4-6/word_spider.webp"}, {"left_image": "@@MEDIA@@halloween/4-6/word_monster.webp", "right": "monster", "right_image": "@@MEDIA@@halloween/4-6/word_monster.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    -- блок 4 (sort_order 3)
    (v_lesson, 'quiz', replace($blk${"title": "🔊 Послушай: это то слово? 👍 или 👎", "questions": [{"q": "", "type": "single", "image": "@@MEDIA@@halloween/4-6/word_spider.webp", "audio_tts": "bat", "correct": [1], "options": [{"text": "Yes", "image": "@@MEDIA@@shared/yes_thumb_up.webp"}, {"text": "No", "image": "@@MEDIA@@shared/no_thumb_down.webp"}]}, {"q": "", "type": "single", "image": "@@MEDIA@@halloween/4-6/word_ghost.webp", "audio_tts": "ghost", "correct": [0], "options": [{"text": "Yes", "image": "@@MEDIA@@shared/yes_thumb_up.webp"}, {"text": "No", "image": "@@MEDIA@@shared/no_thumb_down.webp"}]}, {"q": "", "type": "single", "image": "@@MEDIA@@halloween/4-6/word_bat.webp", "audio_tts": "bat", "correct": [0], "options": [{"text": "Yes", "image": "@@MEDIA@@shared/yes_thumb_up.webp"}, {"text": "No", "image": "@@MEDIA@@shared/no_thumb_down.webp"}]}, {"q": "", "type": "single", "image": "@@MEDIA@@halloween/4-6/word_monster.webp", "audio_tts": "monster", "correct": [0], "options": [{"text": "Yes", "image": "@@MEDIA@@shared/yes_thumb_up.webp"}, {"text": "No", "image": "@@MEDIA@@shared/no_thumb_down.webp"}]}, {"q": "", "type": "single", "image": "@@MEDIA@@halloween/4-6/word_bat.webp", "audio_tts": "ghost", "correct": [1], "options": [{"text": "Yes", "image": "@@MEDIA@@shared/yes_thumb_up.webp"}, {"text": "No", "image": "@@MEDIA@@shared/no_thumb_down.webp"}]}, {"q": "", "type": "single", "image": "@@MEDIA@@halloween/4-6/word_spider.webp", "audio_tts": "spider", "correct": [0], "options": [{"text": "Yes", "image": "@@MEDIA@@shared/yes_thumb_up.webp"}, {"text": "No", "image": "@@MEDIA@@shared/no_thumb_down.webp"}]}, {"q": "", "type": "single", "image": "@@MEDIA@@halloween/4-6/word_ghost.webp", "audio_tts": "spider", "correct": [1], "options": [{"text": "Yes", "image": "@@MEDIA@@shared/yes_thumb_up.webp"}, {"text": "No", "image": "@@MEDIA@@shared/no_thumb_down.webp"}]}, {"q": "", "type": "single", "image": "@@MEDIA@@halloween/4-6/word_monster.webp", "audio_tts": "spider", "correct": [1], "options": [{"text": "Yes", "image": "@@MEDIA@@shared/yes_thumb_up.webp"}, {"text": "No", "image": "@@MEDIA@@shared/no_thumb_down.webp"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    -- блок 5 (sort_order 4)
    (v_lesson, 'speaking', replace($blk${"title": "🎤 Что ты видишь?", "html": "<p>Нажми на запись и назови всё, что видишь на картинке.</p><p><i>ghost, bat, spider, monster…</i></p>", "image": "@@MEDIA@@halloween/4-6/hw_scene.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  delete from classroom_blocks where lesson_id = v_lesson and sort_order >= 5;
end
$mig$;
