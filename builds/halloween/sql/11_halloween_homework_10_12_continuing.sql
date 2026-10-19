-- HOLIDAYS · Halloween · Halloween Homework · 10–12 · continuing
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
   where unit_id = v_unit and title = 'Halloween Homework · 10–12 · continuing' limit 1;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, summary, sort_order, is_published, pass_threshold, kind)
    values (v_unit, 'Halloween Homework · 10–12 · continuing', 'Хэллоуин: 6 монстров + улики (watch, scarf, glasses, boots, lollipop, ticket)', 14, false, 60, 'homework')
    returning id into v_lesson;
  else
    update classroom_lessons set summary = 'Хэллоуин: 6 монстров + улики (watch, scarf, glasses, boots, lollipop, ticket)', sort_order = 14,
           is_published = false, pass_threshold = 60, kind = 'homework'
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    -- блок 1 (sort_order 0)
    (v_lesson, 'flashcards', replace($blk${"title": "Карточки: смотри, слушай, повторяй", "cards": [{"text": "a witch", "image": "@@MEDIA@@halloween/10-12/s_witch.webp", "audio_tts": "witch"}, {"text": "a vampire", "image": "@@MEDIA@@halloween/10-12/s_vampire.webp", "audio_tts": "vampire"}, {"text": "a mummy", "image": "@@MEDIA@@halloween/10-12/s_mummy.webp", "audio_tts": "mummy"}, {"text": "a werewolf", "image": "@@MEDIA@@halloween/10-12/s_werewolf.webp", "audio_tts": "werewolf"}, {"text": "a skeleton", "image": "@@MEDIA@@halloween/10-12/s_skeleton.webp", "audio_tts": "skeleton"}, {"text": "a ghost", "image": "@@MEDIA@@halloween/10-12/s_ghost.webp", "audio_tts": "ghost"}, {"text": "a watch", "image": "@@MEDIA@@halloween/10-12/o_watch.webp", "audio_tts": "watch"}, {"text": "a scarf", "image": "@@MEDIA@@halloween/10-12/o_scarf.webp", "audio_tts": "scarf"}, {"text": "glasses", "image": "@@MEDIA@@halloween/10-12/o_glasses.webp", "audio_tts": "glasses"}, {"text": "boots", "image": "@@MEDIA@@halloween/10-12/o_boot.webp", "audio_tts": "boots"}, {"text": "a lollipop", "image": "@@MEDIA@@halloween/10-12/o_lollipops.webp", "audio_tts": "lollipop"}, {"text": "a ticket", "image": "@@MEDIA@@halloween/10-12/o_ticket.webp", "audio_tts": "ticket"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    -- блок 2 (sort_order 1)
    (v_lesson, 'match', replace($blk${"title": "Соедини картинку и слово", "pairs": [{"left_image": "@@MEDIA@@halloween/10-12/s_witch.webp", "right": "witch", "right_audio_tts": "witch"}, {"left_image": "@@MEDIA@@halloween/10-12/s_vampire.webp", "right": "vampire", "right_audio_tts": "vampire"}, {"left_image": "@@MEDIA@@halloween/10-12/s_mummy.webp", "right": "mummy", "right_audio_tts": "mummy"}, {"left_image": "@@MEDIA@@halloween/10-12/s_werewolf.webp", "right": "werewolf", "right_audio_tts": "werewolf"}, {"left_image": "@@MEDIA@@halloween/10-12/s_skeleton.webp", "right": "skeleton", "right_audio_tts": "skeleton"}, {"left_image": "@@MEDIA@@halloween/10-12/s_ghost.webp", "right": "ghost", "right_audio_tts": "ghost"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    -- блок 3 (sort_order 2)
    (v_lesson, 'match', replace($blk${"title": "Соедини картинку и слово", "pairs": [{"left_image": "@@MEDIA@@halloween/10-12/o_watch.webp", "right": "watch", "right_audio_tts": "watch"}, {"left_image": "@@MEDIA@@halloween/10-12/o_scarf.webp", "right": "scarf", "right_audio_tts": "scarf"}, {"left_image": "@@MEDIA@@halloween/10-12/o_glasses.webp", "right": "glasses", "right_audio_tts": "glasses"}, {"left_image": "@@MEDIA@@halloween/10-12/o_boot.webp", "right": "boots", "right_audio_tts": "boots"}, {"left_image": "@@MEDIA@@halloween/10-12/o_lollipops.webp", "right": "lollipop", "right_audio_tts": "lollipop"}, {"left_image": "@@MEDIA@@halloween/10-12/o_ticket.webp", "right": "ticket", "right_audio_tts": "ticket"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    -- блок 4 (sort_order 3)
    (v_lesson, 'exact_input', replace($blk${"title": "Собери слово из букв", "items": [{"prompt": "T S O O B", "image": "@@MEDIA@@halloween/10-12/o_boot.webp", "accept": ["boots", "Boots"]}, {"prompt": "N E S K E L O T", "image": "@@MEDIA@@halloween/10-12/s_skeleton.webp", "accept": ["skeleton", "Skeleton", "a skeleton", "A skeleton"]}, {"prompt": "G S T H O", "image": "@@MEDIA@@halloween/10-12/s_ghost.webp", "accept": ["ghost", "Ghost", "a ghost", "A ghost"]}, {"prompt": "L A G S S E S", "image": "@@MEDIA@@halloween/10-12/o_glasses.webp", "accept": ["glasses", "Glasses"]}, {"prompt": "C W I H T", "image": "@@MEDIA@@halloween/10-12/s_witch.webp", "accept": ["witch", "Witch", "a witch", "A witch"]}, {"prompt": "T C A H W", "image": "@@MEDIA@@halloween/10-12/o_watch.webp", "accept": ["watch", "Watch", "a watch", "A watch"]}, {"prompt": "E O W L W R E F", "image": "@@MEDIA@@halloween/10-12/s_werewolf.webp", "accept": ["werewolf", "Werewolf", "a werewolf", "A werewolf"]}, {"prompt": "E V I M P A R", "image": "@@MEDIA@@halloween/10-12/s_vampire.webp", "accept": ["vampire", "Vampire", "a vampire", "A vampire"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    -- блок 5 (sort_order 4)
    (v_lesson, 'exact_input', replace($blk${"title": "🔊 Послушай и напиши слово", "items": [{"prompt": "", "audio_tts": "boots", "accept": ["boots", "Boots"]}, {"prompt": "", "audio_tts": "vampire", "accept": ["vampire", "Vampire", "a vampire", "A vampire"]}, {"prompt": "", "audio_tts": "scarf", "accept": ["scarf", "Scarf", "a scarf", "A scarf"]}, {"prompt": "", "audio_tts": "skeleton", "accept": ["skeleton", "Skeleton", "a skeleton", "A skeleton"]}, {"prompt": "", "audio_tts": "witch", "accept": ["witch", "Witch", "a witch", "A witch"]}, {"prompt": "", "audio_tts": "ticket", "accept": ["ticket", "Ticket", "a ticket", "A ticket"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    -- блок 6 (sort_order 5)
    (v_lesson, 'quiz', replace($blk${"title": "Какое слово лишнее?", "questions": [{"q": "", "type": "single", "correct": [2], "options": [{"text": "witch", "image": "@@MEDIA@@halloween/10-12/s_witch.webp"}, {"text": "mummy", "image": "@@MEDIA@@halloween/10-12/s_mummy.webp"}, {"text": "scarf", "image": "@@MEDIA@@halloween/10-12/o_scarf.webp"}, {"text": "vampire", "image": "@@MEDIA@@halloween/10-12/s_vampire.webp"}]}, {"q": "", "type": "single", "correct": [2], "options": [{"text": "watch", "image": "@@MEDIA@@halloween/10-12/o_watch.webp"}, {"text": "glasses", "image": "@@MEDIA@@halloween/10-12/o_glasses.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/10-12/s_ghost.webp"}, {"text": "boots", "image": "@@MEDIA@@halloween/10-12/o_boot.webp"}]}, {"q": "", "type": "single", "correct": [1], "options": [{"text": "skeleton", "image": "@@MEDIA@@halloween/10-12/s_skeleton.webp"}, {"text": "ticket", "image": "@@MEDIA@@halloween/10-12/o_ticket.webp"}, {"text": "werewolf", "image": "@@MEDIA@@halloween/10-12/s_werewolf.webp"}, {"text": "witch", "image": "@@MEDIA@@halloween/10-12/s_witch.webp"}]}, {"q": "", "type": "single", "correct": [3], "options": [{"text": "lollipop", "image": "@@MEDIA@@halloween/10-12/o_lollipops.webp"}, {"text": "scarf", "image": "@@MEDIA@@halloween/10-12/o_scarf.webp"}, {"text": "watch", "image": "@@MEDIA@@halloween/10-12/o_watch.webp"}, {"text": "mummy", "image": "@@MEDIA@@halloween/10-12/s_mummy.webp"}]}, {"q": "", "type": "single", "correct": [2], "options": [{"text": "vampire", "image": "@@MEDIA@@halloween/10-12/s_vampire.webp"}, {"text": "ghost", "image": "@@MEDIA@@halloween/10-12/s_ghost.webp"}, {"text": "boots", "image": "@@MEDIA@@halloween/10-12/o_boot.webp"}, {"text": "skeleton", "image": "@@MEDIA@@halloween/10-12/s_skeleton.webp"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    -- блок 7 (sort_order 6)
    (v_lesson, 'gaps', replace($blk${"mode": "drag", "title": "The Golden Pumpkin: вставь слова", "text": "Last night someone stole the Golden Pumpkin! The detectives found a broken __watch__ in the square. It stopped at 9:15. A witness saw a long red __scarf__ in the park. Next to the old tower there were footprints of big __boots__. Somebody ate all the __lollipops__ at the cafe. Is the thief the __vampire__? Or the __werewolf__? The __mummy__ has got an alibi: a cinema __ticket__ for nine o'clock."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    -- блок 8 (sort_order 7)
    (v_lesson, 'speaking', replace($blk${"title": "🎤 Опиши подозреваемого", "html": "<p>Нажми на запись и расскажи, что ты видишь на картинке.</p><p><i>I can see a vampire. I can see a red scarf, glasses…</i></p>", "image": "@@MEDIA@@halloween/10-12/hw_suspect.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  delete from classroom_blocks where lesson_id = v_lesson and sort_order >= 8;
end
$mig$;
