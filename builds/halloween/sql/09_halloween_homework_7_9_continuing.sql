-- HOLIDAYS · Halloween · Halloween Homework · 7–9 · continuing
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
   where unit_id = v_unit and title = 'Halloween Homework · 7–9 · continuing' limit 1;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, summary, sort_order, is_published, pass_threshold, kind)
    values (v_unit, 'Halloween Homework · 7–9 · continuing', 'Хэллоуин: 8 слов, there is / there are, in / on / under', 12, false, 60, 'homework')
    returning id into v_lesson;
  else
    update classroom_lessons set summary = 'Хэллоуин: 8 слов, there is / there are, in / on / under', sort_order = 12,
           is_published = false, pass_threshold = 60, kind = 'homework'
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    -- блок 1 (sort_order 0)
    (v_lesson, 'flashcards', replace($blk${"title": "Карточки: смотри, слушай, повторяй", "cards": [{"text": "a ghost", "image": "@@MEDIA@@halloween/7-9/w_ghost.webp", "audio_tts": "ghost"}, {"text": "a spider", "image": "@@MEDIA@@halloween/7-9/w_spider.webp", "audio_tts": "spider"}, {"text": "a witch", "image": "@@MEDIA@@halloween/7-9/w_witch.webp", "audio_tts": "witch"}, {"text": "a skeleton", "image": "@@MEDIA@@halloween/7-9/w_skeleton.webp", "audio_tts": "skeleton"}, {"text": "a vampire", "image": "@@MEDIA@@halloween/7-9/w_vampire.webp", "audio_tts": "vampire"}, {"text": "a mummy", "image": "@@MEDIA@@halloween/7-9/w_mummy.webp", "audio_tts": "mummy"}, {"text": "a broom", "image": "@@MEDIA@@halloween/7-9/w_broom.webp", "audio_tts": "broom"}, {"text": "a haunted house", "image": "@@MEDIA@@halloween/7-9/w_house.webp", "audio_tts": "haunted house"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    -- блок 2 (sort_order 1)
    (v_lesson, 'match', replace($blk${"title": "Соедини картинку и слово", "pairs": [{"left_image": "@@MEDIA@@halloween/7-9/w_ghost.webp", "right": "ghost", "right_audio_tts": "ghost"}, {"left_image": "@@MEDIA@@halloween/7-9/w_spider.webp", "right": "spider", "right_audio_tts": "spider"}, {"left_image": "@@MEDIA@@halloween/7-9/w_witch.webp", "right": "witch", "right_audio_tts": "witch"}, {"left_image": "@@MEDIA@@halloween/7-9/w_skeleton.webp", "right": "skeleton", "right_audio_tts": "skeleton"}, {"left_image": "@@MEDIA@@halloween/7-9/w_vampire.webp", "right": "vampire", "right_audio_tts": "vampire"}, {"left_image": "@@MEDIA@@halloween/7-9/w_mummy.webp", "right": "mummy", "right_audio_tts": "mummy"}, {"left_image": "@@MEDIA@@halloween/7-9/w_broom.webp", "right": "broom", "right_audio_tts": "broom"}, {"left_image": "@@MEDIA@@halloween/7-9/w_house.webp", "right": "haunted house", "right_audio_tts": "haunted house"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    -- блок 3 (sort_order 2)
    (v_lesson, 'exact_input', replace($blk${"title": "Собери слово из букв", "items": [{"prompt": "O G S T H", "image": "@@MEDIA@@halloween/7-9/w_ghost.webp", "accept": ["ghost", "Ghost", "a ghost", "A ghost"]}, {"prompt": "P E S D I R", "image": "@@MEDIA@@halloween/7-9/w_spider.webp", "accept": ["spider", "Spider", "a spider", "A spider"]}, {"prompt": "T C H I W", "image": "@@MEDIA@@halloween/7-9/w_witch.webp", "accept": ["witch", "Witch", "a witch", "A witch"]}, {"prompt": "O N E T L K E S", "image": "@@MEDIA@@halloween/7-9/w_skeleton.webp", "accept": ["skeleton", "Skeleton", "a skeleton", "A skeleton"]}, {"prompt": "V P A R M I E", "image": "@@MEDIA@@halloween/7-9/w_vampire.webp", "accept": ["vampire", "Vampire", "a vampire", "A vampire"]}, {"prompt": "M Y U M M", "image": "@@MEDIA@@halloween/7-9/w_mummy.webp", "accept": ["mummy", "Mummy", "a mummy", "A mummy"]}, {"prompt": "O R M O B", "image": "@@MEDIA@@halloween/7-9/w_broom.webp", "accept": ["broom", "Broom", "a broom", "A broom"]}, {"prompt": "A D E N U T H   S O H U E", "image": "@@MEDIA@@halloween/7-9/w_house.webp", "accept": ["haunted house", "Haunted house", "a haunted house", "A haunted house"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    -- блок 4 (sort_order 3)
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку: is или are?", "questions": [{"q": "There ___ a witch in the room.", "type": "single", "correct": [0], "options": [{"text": "is"}, {"text": "are"}], "image": "@@MEDIA@@halloween/7-9/hw_room.webp"}, {"q": "There ___ three pumpkins under the bed.", "type": "single", "correct": [1], "options": [{"text": "is"}, {"text": "are"}], "image": "@@MEDIA@@halloween/7-9/hw_room.webp"}, {"q": "There ___ a ghost on the bed.", "type": "single", "correct": [0], "options": [{"text": "is"}, {"text": "are"}], "image": "@@MEDIA@@halloween/7-9/hw_room.webp"}, {"q": "There ___ two spiders on the table.", "type": "single", "correct": [1], "options": [{"text": "is"}, {"text": "are"}], "image": "@@MEDIA@@halloween/7-9/hw_room.webp"}, {"q": "There ___ a mummy in the box.", "type": "single", "correct": [0], "options": [{"text": "is"}, {"text": "are"}], "image": "@@MEDIA@@halloween/7-9/hw_room.webp"}, {"q": "There ___ a vampire next to the window.", "type": "single", "correct": [0], "options": [{"text": "is"}, {"text": "are"}], "image": "@@MEDIA@@halloween/7-9/hw_room.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    -- блок 5 (sort_order 4)
    (v_lesson, 'quiz', replace($blk${"title": "In, on или under?", "questions": [{"q": "The ghost is ___ the bed.", "type": "single", "correct": [1], "options": [{"text": "in"}, {"text": "on"}, {"text": "under"}], "image": "@@MEDIA@@halloween/7-9/hw_r_ghostbed.webp"}, {"q": "The pumpkins are ___ the bed.", "type": "single", "correct": [2], "options": [{"text": "in"}, {"text": "on"}, {"text": "under"}], "image": "@@MEDIA@@halloween/7-9/hw_r_pumpkins.webp"}, {"q": "The spiders are ___ the table.", "type": "single", "correct": [1], "options": [{"text": "in"}, {"text": "on"}, {"text": "under"}], "image": "@@MEDIA@@halloween/7-9/hw_r_spiders.webp"}, {"q": "The broom is ___ the table.", "type": "single", "correct": [2], "options": [{"text": "in"}, {"text": "on"}, {"text": "under"}], "image": "@@MEDIA@@halloween/7-9/hw_r_broom.webp"}, {"q": "The mummy is ___ the box.", "type": "single", "correct": [0], "options": [{"text": "in"}, {"text": "on"}, {"text": "under"}], "image": "@@MEDIA@@halloween/7-9/hw_r_mummy.webp"}, {"q": "The skeleton is ___ the chair.", "type": "single", "correct": [1], "options": [{"text": "in"}, {"text": "on"}, {"text": "under"}], "image": "@@MEDIA@@halloween/7-9/hw_r_skeleton.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    -- блок 6 (sort_order 5)
    (v_lesson, 'truefalse', replace($blk${"title": "Посмотри на картинку: верно или неверно?", "image": "@@MEDIA@@halloween/7-9/hw_room.webp", "statements": [{"text": "There is a ghost on the bed.", "correct": true}, {"text": "There are two pumpkins under the bed.", "correct": false}, {"text": "The broom is on the table.", "correct": false}, {"text": "There is a mummy in the box.", "correct": true}, {"text": "The skeleton is on the chair.", "correct": true}, {"text": "There are three spiders on the table.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    -- блок 7 (sort_order 6)
    (v_lesson, 'speaking', replace($blk${"title": "🎤 Расскажи про комнату", "html": "<p>Нажми на запись и расскажи, что есть в комнате и где.</p><p><i>There is a ghost on the bed. There are three pumpkins under the bed. The broom is under the table…</i></p>", "image": "@@MEDIA@@halloween/7-9/hw_room.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  delete from classroom_blocks where lesson_id = v_lesson and sort_order >= 7;
end
$mig$;
