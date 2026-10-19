-- HOLIDAYS · Halloween · Halloween Homework · 13+ · beginners
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
   where unit_id = v_unit and title = 'Halloween Homework · 13+ · beginners' limit 1;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, summary, sort_order, is_published, pass_threshold, kind)
    values (v_unit, 'Halloween Homework · 13+ · beginners', 'Хэллоуин: pumpkin, turnip, bonfire, costume, ghost, candle', 15, false, 60, 'homework')
    returning id into v_lesson;
  else
    update classroom_lessons set summary = 'Хэллоуин: pumpkin, turnip, bonfire, costume, ghost, candle', sort_order = 15,
           is_published = false, pass_threshold = 60, kind = 'homework'
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    -- блок 1 (sort_order 0)
    (v_lesson, 'flashcards', replace($blk${"title": "Карточки: смотри, слушай, повторяй", "cards": [{"text": "a pumpkin", "image": "@@MEDIA@@halloween/13/w_pumpkin.webp", "audio_tts": "pumpkin"}, {"text": "a turnip", "image": "@@MEDIA@@halloween/13/w_turnip.webp", "audio_tts": "turnip"}, {"text": "a bonfire", "image": "@@MEDIA@@halloween/13/w_bonfire.webp", "audio_tts": "bonfire"}, {"text": "a costume", "image": "@@MEDIA@@halloween/13/w_costume.webp", "audio_tts": "costume"}, {"text": "a ghost", "image": "@@MEDIA@@halloween/13/w_ghost.webp", "audio_tts": "ghost"}, {"text": "a candle", "image": "@@MEDIA@@halloween/13/w_candle.webp", "audio_tts": "candle"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    -- блок 2 (sort_order 1)
    (v_lesson, 'speaking', replace($blk${"title": "🎤 Повтори слова", "html": "<p>Нажми на запись и скажи по-английски все слова по порядку.</p><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/13/w_pumpkin.webp\" alt=\"\" style=\"height:110px\"><br><b>pumpkin</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/13/w_turnip.webp\" alt=\"\" style=\"height:110px\"><br><b>turnip</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/13/w_bonfire.webp\" alt=\"\" style=\"height:110px\"><br><b>bonfire</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/13/w_costume.webp\" alt=\"\" style=\"height:110px\"><br><b>costume</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/13/w_ghost.webp\" alt=\"\" style=\"height:110px\"><br><b>ghost</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/13/w_candle.webp\" alt=\"\" style=\"height:110px\"><br><b>candle</b></div>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    -- блок 3 (sort_order 2)
    (v_lesson, 'quiz', replace($blk${"title": "🔊 Послушай и выбери картинку", "questions": [{"q": "", "type": "single", "audio_tts": "bonfire", "correct": [1], "options": [{"text": "pumpkin", "image": "@@MEDIA@@halloween/13/w_pumpkin.webp"}, {"text": "bonfire", "image": "@@MEDIA@@halloween/13/w_bonfire.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/13/w_ghost.webp"}]}, {"q": "", "type": "single", "audio_tts": "candle", "correct": [0], "options": [{"text": "candle", "image": "@@MEDIA@@halloween/13/w_candle.webp"}, {"text": "turnip", "image": "@@MEDIA@@halloween/13/w_turnip.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/13/w_ghost.webp"}]}, {"q": "", "type": "single", "audio_tts": "pumpkin", "correct": [2], "options": [{"text": "ghost", "image": "@@MEDIA@@halloween/13/w_ghost.webp"}, {"text": "bonfire", "image": "@@MEDIA@@halloween/13/w_bonfire.webp"}, {"text": "pumpkin", "image": "@@MEDIA@@halloween/13/w_pumpkin.webp"}]}, {"q": "", "type": "single", "audio_tts": "turnip", "correct": [1], "options": [{"text": "bonfire", "image": "@@MEDIA@@halloween/13/w_bonfire.webp"}, {"text": "turnip", "image": "@@MEDIA@@halloween/13/w_turnip.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/13/w_ghost.webp"}]}, {"q": "", "type": "single", "audio_tts": "ghost", "correct": [2], "options": [{"text": "pumpkin", "image": "@@MEDIA@@halloween/13/w_pumpkin.webp"}, {"text": "costume", "image": "@@MEDIA@@halloween/13/w_costume.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/13/w_ghost.webp"}]}, {"q": "", "type": "single", "audio_tts": "costume", "correct": [1], "options": [{"text": "bonfire", "image": "@@MEDIA@@halloween/13/w_bonfire.webp"}, {"text": "costume", "image": "@@MEDIA@@halloween/13/w_costume.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/13/w_ghost.webp"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    -- блок 4 (sort_order 3)
    (v_lesson, 'match', replace($blk${"title": "Соедини картинку и слово", "pairs": [{"left_image": "@@MEDIA@@halloween/13/w_pumpkin.webp", "right": "pumpkin", "right_audio_tts": "pumpkin"}, {"left_image": "@@MEDIA@@halloween/13/w_turnip.webp", "right": "turnip", "right_audio_tts": "turnip"}, {"left_image": "@@MEDIA@@halloween/13/w_bonfire.webp", "right": "bonfire", "right_audio_tts": "bonfire"}, {"left_image": "@@MEDIA@@halloween/13/w_costume.webp", "right": "costume", "right_audio_tts": "costume"}, {"left_image": "@@MEDIA@@halloween/13/w_ghost.webp", "right": "ghost", "right_audio_tts": "ghost"}, {"left_image": "@@MEDIA@@halloween/13/w_candle.webp", "right": "candle", "right_audio_tts": "candle"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    -- блок 5 (sort_order 4)
    (v_lesson, 'exact_input', replace($blk${"title": "Собери слово из букв", "items": [{"prompt": "U K I P P N M", "image": "@@MEDIA@@halloween/13/w_pumpkin.webp", "accept": ["pumpkin", "Pumpkin", "a pumpkin", "A pumpkin"]}, {"prompt": "U T I R P N", "image": "@@MEDIA@@halloween/13/w_turnip.webp", "accept": ["turnip", "Turnip", "a turnip", "A turnip"]}, {"prompt": "N I O R B F E", "image": "@@MEDIA@@halloween/13/w_bonfire.webp", "accept": ["bonfire", "Bonfire", "a bonfire", "A bonfire"]}, {"prompt": "O C T M U E S", "image": "@@MEDIA@@halloween/13/w_costume.webp", "accept": ["costume", "Costume", "a costume", "A costume"]}, {"prompt": "H G T O S", "image": "@@MEDIA@@halloween/13/w_ghost.webp", "accept": ["ghost", "Ghost", "a ghost", "A ghost"]}, {"prompt": "C N E L D A", "image": "@@MEDIA@@halloween/13/w_candle.webp", "accept": ["candle", "Candle", "a candle", "A candle"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    -- блок 6 (sort_order 5)
    (v_lesson, 'speaking', replace($blk${"title": "🎤 Что ты видишь?", "html": "<p>Нажми на запись и назови всё, что видишь на картинке.</p><p><i>I can see a bonfire, a pumpkin…</i></p>", "image": "@@MEDIA@@halloween/13/hw_scene_b.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  delete from classroom_blocks where lesson_id = v_lesson and sort_order >= 6;
end
$mig$;
