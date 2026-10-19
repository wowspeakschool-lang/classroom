-- HOLIDAYS · Halloween · Halloween Homework · 7–9 · beginners
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
   where unit_id = v_unit and title = 'Halloween Homework · 7–9 · beginners' limit 1;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, summary, sort_order, is_published, pass_threshold, kind)
    values (v_unit, 'Halloween Homework · 7–9 · beginners', 'Хэллоуин: ghost, bat, spider, witch, pumpkin, skeleton', 11, false, 60, 'homework')
    returning id into v_lesson;
  else
    update classroom_lessons set summary = 'Хэллоуин: ghost, bat, spider, witch, pumpkin, skeleton', sort_order = 11,
           is_published = false, pass_threshold = 60, kind = 'homework'
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    -- блок 1 (sort_order 0)
    (v_lesson, 'flashcards', replace($blk${"title": "Карточки: смотри, слушай, повторяй", "cards": [{"text": "a ghost", "image": "@@MEDIA@@halloween/7-9/w_ghost.webp", "audio_tts": "ghost"}, {"text": "a bat", "image": "@@MEDIA@@halloween/7-9/w_bat.webp", "audio_tts": "bat"}, {"text": "a spider", "image": "@@MEDIA@@halloween/7-9/w_spider.webp", "audio_tts": "spider"}, {"text": "a witch", "image": "@@MEDIA@@halloween/7-9/w_witch.webp", "audio_tts": "witch"}, {"text": "a pumpkin", "image": "@@MEDIA@@halloween/7-9/w_pumpkin.webp", "audio_tts": "pumpkin"}, {"text": "a skeleton", "image": "@@MEDIA@@halloween/7-9/w_skeleton.webp", "audio_tts": "skeleton"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    -- блок 2 (sort_order 1)
    (v_lesson, 'speaking', replace($blk${"title": "🎤 Повтори слова", "html": "<p>Нажми на запись и скажи по-английски все слова по порядку.</p><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/7-9/w_ghost.webp\" alt=\"\" style=\"height:110px\"><br><b>ghost</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/7-9/w_bat.webp\" alt=\"\" style=\"height:110px\"><br><b>bat</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/7-9/w_spider.webp\" alt=\"\" style=\"height:110px\"><br><b>spider</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/7-9/w_witch.webp\" alt=\"\" style=\"height:110px\"><br><b>witch</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/7-9/w_pumpkin.webp\" alt=\"\" style=\"height:110px\"><br><b>pumpkin</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/7-9/w_skeleton.webp\" alt=\"\" style=\"height:110px\"><br><b>skeleton</b></div>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    -- блок 3 (sort_order 2)
    (v_lesson, 'quiz', replace($blk${"title": "🔊 Послушай и выбери картинку", "questions": [{"q": "", "type": "single", "audio_tts": "spider", "correct": [2], "options": [{"text": "witch", "image": "@@MEDIA@@halloween/7-9/w_witch.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/7-9/w_ghost.webp"}, {"text": "spider", "image": "@@MEDIA@@halloween/7-9/w_spider.webp"}]}, {"q": "", "type": "single", "audio_tts": "pumpkin", "correct": [1], "options": [{"text": "skeleton", "image": "@@MEDIA@@halloween/7-9/w_skeleton.webp"}, {"text": "pumpkin", "image": "@@MEDIA@@halloween/7-9/w_pumpkin.webp"}, {"text": "bat", "image": "@@MEDIA@@halloween/7-9/w_bat.webp"}]}, {"q": "", "type": "single", "audio_tts": "ghost", "correct": [1], "options": [{"text": "witch", "image": "@@MEDIA@@halloween/7-9/w_witch.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/7-9/w_ghost.webp"}, {"text": "skeleton", "image": "@@MEDIA@@halloween/7-9/w_skeleton.webp"}]}, {"q": "", "type": "single", "audio_tts": "bat", "correct": [2], "options": [{"text": "spider", "image": "@@MEDIA@@halloween/7-9/w_spider.webp"}, {"text": "witch", "image": "@@MEDIA@@halloween/7-9/w_witch.webp"}, {"text": "bat", "image": "@@MEDIA@@halloween/7-9/w_bat.webp"}]}, {"q": "", "type": "single", "audio_tts": "witch", "correct": [1], "options": [{"text": "ghost", "image": "@@MEDIA@@halloween/7-9/w_ghost.webp"}, {"text": "witch", "image": "@@MEDIA@@halloween/7-9/w_witch.webp"}, {"text": "skeleton", "image": "@@MEDIA@@halloween/7-9/w_skeleton.webp"}]}, {"q": "", "type": "single", "audio_tts": "skeleton", "correct": [0], "options": [{"text": "skeleton", "image": "@@MEDIA@@halloween/7-9/w_skeleton.webp"}, {"text": "spider", "image": "@@MEDIA@@halloween/7-9/w_spider.webp"}, {"text": "bat", "image": "@@MEDIA@@halloween/7-9/w_bat.webp"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    -- блок 4 (sort_order 3) · вместо игры «найди пару»
    (v_lesson, 'match', replace($blk${"title": "Найди одинаковые картинки и назови их", "pairs": [{"left_image": "@@MEDIA@@halloween/7-9/w_ghost.webp", "right": "ghost", "right_image": "@@MEDIA@@halloween/7-9/w_ghost.webp"}, {"left_image": "@@MEDIA@@halloween/7-9/w_bat.webp", "right": "bat", "right_image": "@@MEDIA@@halloween/7-9/w_bat.webp"}, {"left_image": "@@MEDIA@@halloween/7-9/w_spider.webp", "right": "spider", "right_image": "@@MEDIA@@halloween/7-9/w_spider.webp"}, {"left_image": "@@MEDIA@@halloween/7-9/w_witch.webp", "right": "witch", "right_image": "@@MEDIA@@halloween/7-9/w_witch.webp"}, {"left_image": "@@MEDIA@@halloween/7-9/w_pumpkin.webp", "right": "pumpkin", "right_image": "@@MEDIA@@halloween/7-9/w_pumpkin.webp"}, {"left_image": "@@MEDIA@@halloween/7-9/w_skeleton.webp", "right": "skeleton", "right_image": "@@MEDIA@@halloween/7-9/w_skeleton.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    -- блок 5 (sort_order 4)
    (v_lesson, 'match', replace($blk${"title": "Соедини картинку и слово", "pairs": [{"left_image": "@@MEDIA@@halloween/7-9/w_ghost.webp", "right": "ghost", "right_audio_tts": "ghost"}, {"left_image": "@@MEDIA@@halloween/7-9/w_bat.webp", "right": "bat", "right_audio_tts": "bat"}, {"left_image": "@@MEDIA@@halloween/7-9/w_spider.webp", "right": "spider", "right_audio_tts": "spider"}, {"left_image": "@@MEDIA@@halloween/7-9/w_witch.webp", "right": "witch", "right_audio_tts": "witch"}, {"left_image": "@@MEDIA@@halloween/7-9/w_pumpkin.webp", "right": "pumpkin", "right_audio_tts": "pumpkin"}, {"left_image": "@@MEDIA@@halloween/7-9/w_skeleton.webp", "right": "skeleton", "right_audio_tts": "skeleton"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    -- блок 6 (sort_order 5)
    (v_lesson, 'speaking', replace($blk${"title": "🎤 Что ты видишь?", "html": "<p>Нажми на запись и назови всё, что видишь на картинке.</p><p><i>I can see a ghost, a bat…</i></p>", "image": "@@MEDIA@@halloween/7-9/hw_scene_b.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  delete from classroom_blocks where lesson_id = v_lesson and sort_order >= 6;
end
$mig$;
