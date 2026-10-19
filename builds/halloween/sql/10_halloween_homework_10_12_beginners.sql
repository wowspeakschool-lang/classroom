-- HOLIDAYS · Halloween · Halloween Homework · 10–12 · beginners
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
   where unit_id = v_unit and title = 'Halloween Homework · 10–12 · beginners' limit 1;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, summary, sort_order, is_published, pass_threshold, kind)
    values (v_unit, 'Halloween Homework · 10–12 · beginners', 'Хэллоуин: witch, vampire, mummy, werewolf, skeleton, ghost', 13, false, 60, 'homework')
    returning id into v_lesson;
  else
    update classroom_lessons set summary = 'Хэллоуин: witch, vampire, mummy, werewolf, skeleton, ghost', sort_order = 13,
           is_published = false, pass_threshold = 60, kind = 'homework'
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    -- блок 1 (sort_order 0)
    (v_lesson, 'flashcards', replace($blk${"title": "Карточки: смотри, слушай, повторяй", "cards": [{"text": "a witch", "image": "@@MEDIA@@halloween/10-12/s_witch.webp", "audio_tts": "witch"}, {"text": "a vampire", "image": "@@MEDIA@@halloween/10-12/s_vampire.webp", "audio_tts": "vampire"}, {"text": "a mummy", "image": "@@MEDIA@@halloween/10-12/s_mummy.webp", "audio_tts": "mummy"}, {"text": "a werewolf", "image": "@@MEDIA@@halloween/10-12/s_werewolf.webp", "audio_tts": "werewolf"}, {"text": "a skeleton", "image": "@@MEDIA@@halloween/10-12/s_skeleton.webp", "audio_tts": "skeleton"}, {"text": "a ghost", "image": "@@MEDIA@@halloween/10-12/s_ghost.webp", "audio_tts": "ghost"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    -- блок 2 (sort_order 1)
    (v_lesson, 'speaking', replace($blk${"title": "🎤 Повтори слова", "html": "<p>Нажми на запись и скажи по-английски все слова по порядку.</p><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/10-12/s_witch.webp\" alt=\"\" style=\"height:110px\"><br><b>witch</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/10-12/s_vampire.webp\" alt=\"\" style=\"height:110px\"><br><b>vampire</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/10-12/s_mummy.webp\" alt=\"\" style=\"height:110px\"><br><b>mummy</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/10-12/s_werewolf.webp\" alt=\"\" style=\"height:110px\"><br><b>werewolf</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/10-12/s_skeleton.webp\" alt=\"\" style=\"height:110px\"><br><b>skeleton</b></div><div style=\"display:inline-block;text-align:center;margin:6px 10px\"><img src=\"@@MEDIA@@halloween/10-12/s_ghost.webp\" alt=\"\" style=\"height:110px\"><br><b>ghost</b></div>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    -- блок 3 (sort_order 2)
    (v_lesson, 'quiz', replace($blk${"title": "🔊 Послушай и выбери картинку", "questions": [{"q": "", "type": "single", "audio_tts": "skeleton", "correct": [0], "options": [{"text": "skeleton", "image": "@@MEDIA@@halloween/10-12/s_skeleton.webp"}, {"text": "vampire", "image": "@@MEDIA@@halloween/10-12/s_vampire.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/10-12/s_ghost.webp"}]}, {"q": "", "type": "single", "audio_tts": "vampire", "correct": [1], "options": [{"text": "werewolf", "image": "@@MEDIA@@halloween/10-12/s_werewolf.webp"}, {"text": "vampire", "image": "@@MEDIA@@halloween/10-12/s_vampire.webp"}, {"text": "mummy", "image": "@@MEDIA@@halloween/10-12/s_mummy.webp"}]}, {"q": "", "type": "single", "audio_tts": "mummy", "correct": [2], "options": [{"text": "werewolf", "image": "@@MEDIA@@halloween/10-12/s_werewolf.webp"}, {"text": "vampire", "image": "@@MEDIA@@halloween/10-12/s_vampire.webp"}, {"text": "mummy", "image": "@@MEDIA@@halloween/10-12/s_mummy.webp"}]}, {"q": "", "type": "single", "audio_tts": "ghost", "correct": [2], "options": [{"text": "mummy", "image": "@@MEDIA@@halloween/10-12/s_mummy.webp"}, {"text": "werewolf", "image": "@@MEDIA@@halloween/10-12/s_werewolf.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/10-12/s_ghost.webp"}]}, {"q": "", "type": "single", "audio_tts": "witch", "correct": [0], "options": [{"text": "witch", "image": "@@MEDIA@@halloween/10-12/s_witch.webp"}, {"text": "werewolf", "image": "@@MEDIA@@halloween/10-12/s_werewolf.webp"}, {"text": "mummy", "image": "@@MEDIA@@halloween/10-12/s_mummy.webp"}]}, {"q": "", "type": "single", "audio_tts": "werewolf", "correct": [2], "options": [{"text": "vampire", "image": "@@MEDIA@@halloween/10-12/s_vampire.webp"}, {"text": "skeleton", "image": "@@MEDIA@@halloween/10-12/s_skeleton.webp"}, {"text": "werewolf", "image": "@@MEDIA@@halloween/10-12/s_werewolf.webp"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    -- блок 4 (sort_order 3)
    (v_lesson, 'match', replace($blk${"title": "Соедини картинку и слово", "pairs": [{"left_image": "@@MEDIA@@halloween/10-12/s_witch.webp", "right": "witch", "right_audio_tts": "witch"}, {"left_image": "@@MEDIA@@halloween/10-12/s_vampire.webp", "right": "vampire", "right_audio_tts": "vampire"}, {"left_image": "@@MEDIA@@halloween/10-12/s_mummy.webp", "right": "mummy", "right_audio_tts": "mummy"}, {"left_image": "@@MEDIA@@halloween/10-12/s_werewolf.webp", "right": "werewolf", "right_audio_tts": "werewolf"}, {"left_image": "@@MEDIA@@halloween/10-12/s_skeleton.webp", "right": "skeleton", "right_audio_tts": "skeleton"}, {"left_image": "@@MEDIA@@halloween/10-12/s_ghost.webp", "right": "ghost", "right_audio_tts": "ghost"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    -- блок 5 (sort_order 4)
    (v_lesson, 'exact_input', replace($blk${"title": "Собери слово из букв", "items": [{"prompt": "H T I W C", "image": "@@MEDIA@@halloween/10-12/s_witch.webp", "accept": ["witch", "Witch", "a witch", "A witch"]}, {"prompt": "P I M R A V E", "image": "@@MEDIA@@halloween/10-12/s_vampire.webp", "accept": ["vampire", "Vampire", "a vampire", "A vampire"]}, {"prompt": "U M M M Y", "image": "@@MEDIA@@halloween/10-12/s_mummy.webp", "accept": ["mummy", "Mummy", "a mummy", "A mummy"]}, {"prompt": "W O L E E R W F", "image": "@@MEDIA@@halloween/10-12/s_werewolf.webp", "accept": ["werewolf", "Werewolf", "a werewolf", "A werewolf"]}, {"prompt": "E L N K E T S O", "image": "@@MEDIA@@halloween/10-12/s_skeleton.webp", "accept": ["skeleton", "Skeleton", "a skeleton", "A skeleton"]}, {"prompt": "G H O T S", "image": "@@MEDIA@@halloween/10-12/s_ghost.webp", "accept": ["ghost", "Ghost", "a ghost", "A ghost"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    -- блок 6 (sort_order 5)
    (v_lesson, 'speaking', replace($blk${"title": "🎤 Что ты видишь?", "html": "<p>Нажми на запись и назови всё, что видишь на картинке.</p><p><i>I can see a witch, a vampire…</i></p>", "image": "@@MEDIA@@halloween/10-12/hw_scene_b.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  delete from classroom_blocks where lesson_id = v_lesson and sort_order >= 6;
end
$mig$;
