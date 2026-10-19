-- HOLIDAYS · Halloween · Halloween Homework · 13+ · continuing
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
   where unit_id = v_unit and title = 'Halloween Homework · 13+ · continuing' limit 1;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, summary, sort_order, is_published, pass_threshold, kind)
    values (v_unit, 'Halloween Homework · 13+ · continuing', 'Хэллоуин: 8 слов с переводом, текст о Самайне', 16, false, 60, 'homework')
    returning id into v_lesson;
  else
    update classroom_lessons set summary = 'Хэллоуин: 8 слов с переводом, текст о Самайне', sort_order = 16,
           is_published = false, pass_threshold = 60, kind = 'homework'
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    -- блок 1 (sort_order 0)
    (v_lesson, 'flashcards', replace($blk${"title": "Новые слова: слово, перевод, звук", "cards": [{"text": "a pumpkin", "image": "@@MEDIA@@halloween/13/w_pumpkin.webp", "audio_tts": "pumpkin", "translation": "тыква"}, {"text": "a turnip", "image": "@@MEDIA@@halloween/13/w_turnip.webp", "audio_tts": "turnip", "translation": "репа"}, {"text": "a bonfire", "image": "@@MEDIA@@halloween/13/w_bonfire.webp", "audio_tts": "bonfire", "translation": "костёр"}, {"text": "a costume", "image": "@@MEDIA@@halloween/13/w_costume.webp", "audio_tts": "costume", "translation": "костюм"}, {"text": "a ghost", "image": "@@MEDIA@@halloween/13/w_ghost.webp", "audio_tts": "ghost", "translation": "привидение"}, {"text": "a candle", "image": "@@MEDIA@@halloween/13/w_candle.webp", "audio_tts": "candle", "translation": "свеча"}, {"text": "a lantern", "image": "@@MEDIA@@halloween/13/w_lantern.webp", "audio_tts": "lantern", "translation": "фонарь"}, {"text": "the harvest", "image": "@@MEDIA@@halloween/13/w_harvest.webp", "audio_tts": "the harvest", "translation": "урожай"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    -- блок 2 (sort_order 1)
    (v_lesson, 'match', replace($blk${"title": "Соедини слово и определение", "pairs": [{"left": "pumpkin", "right": "a big orange vegetable; people carve faces in it on Halloween", "left_audio_tts": "pumpkin"}, {"left": "turnip", "right": "a round white-and-purple vegetable; the first lanterns were made from it", "left_audio_tts": "turnip"}, {"left": "bonfire", "right": "a big fire outside", "left_audio_tts": "bonfire"}, {"left": "costume", "right": "clothes you wear to look like someone or something else", "left_audio_tts": "costume"}, {"left": "ghost", "right": "the spirit of a dead person", "left_audio_tts": "ghost"}, {"left": "candle", "right": "a stick of wax that gives light when it burns", "left_audio_tts": "candle"}, {"left": "lantern", "right": "a light in a case that you can carry", "left_audio_tts": "lantern"}, {"left": "harvest", "right": "the time when farmers collect fruit and vegetables", "left_audio_tts": "harvest"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    -- блок 3 (sort_order 2)
    (v_lesson, 'exact_input', replace($blk${"title": "Собери слово из букв", "items": [{"prompt": "N K M U P I P", "image": "@@MEDIA@@halloween/13/w_pumpkin.webp", "accept": ["pumpkin", "Pumpkin", "a pumpkin", "A pumpkin"]}, {"prompt": "N P R I T U", "image": "@@MEDIA@@halloween/13/w_turnip.webp", "accept": ["turnip", "Turnip", "a turnip", "A turnip"]}, {"prompt": "O R E I B F N", "image": "@@MEDIA@@halloween/13/w_bonfire.webp", "accept": ["bonfire", "Bonfire", "a bonfire", "A bonfire"]}, {"prompt": "C S M E T U O", "image": "@@MEDIA@@halloween/13/w_costume.webp", "accept": ["costume", "Costume", "a costume", "A costume"]}, {"prompt": "H O S G T", "image": "@@MEDIA@@halloween/13/w_ghost.webp", "accept": ["ghost", "Ghost", "a ghost", "A ghost"]}, {"prompt": "D L C A N E", "image": "@@MEDIA@@halloween/13/w_candle.webp", "accept": ["candle", "Candle", "a candle", "A candle"]}, {"prompt": "N E T N L R A", "image": "@@MEDIA@@halloween/13/w_lantern.webp", "accept": ["lantern", "Lantern", "a lantern", "A lantern"]}, {"prompt": "R T H A S V E", "image": "@@MEDIA@@halloween/13/w_harvest.webp", "accept": ["harvest", "Harvest", "the harvest", "The harvest"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    -- блок 4 (sort_order 3)
    (v_lesson, 'exact_input', replace($blk${"title": "🔊 Послушай и напиши слово", "items": [{"prompt": "", "audio_tts": "candle", "accept": ["candle", "Candle", "a candle", "A candle"]}, {"prompt": "", "audio_tts": "turnip", "accept": ["turnip", "Turnip", "a turnip", "A turnip"]}, {"prompt": "", "audio_tts": "costume", "accept": ["costume", "Costume", "a costume", "A costume"]}, {"prompt": "", "audio_tts": "pumpkin", "accept": ["pumpkin", "Pumpkin", "a pumpkin", "A pumpkin"]}, {"prompt": "", "audio_tts": "ghost", "accept": ["ghost", "Ghost", "a ghost", "A ghost"]}, {"prompt": "", "audio_tts": "bonfire", "accept": ["bonfire", "Bonfire", "a bonfire", "A bonfire"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    -- блок 5 (sort_order 4)
    (v_lesson, 'gaps', replace($blk${"mode": "drag", "title": "Samhain: вставь слова", "text": "Long ago in Ireland, people celebrated Samhain at the end of the __harvest__. They made big __bonfires__ on the hills. They believed that a __ghost__ could walk on Earth that night, so they wore a __costume__ and a mask. Children carved a scary face into a __turnip__, put a __candle__ inside and made a __lantern__. Later, in America, people used a __pumpkin__ instead."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    -- блок 6 (sort_order 5)
    (v_lesson, 'truefalse', replace($blk${"title": "Прочитай текст ещё раз: верно или неверно?", "statements": [{"text": "Samhain was at the end of the harvest.", "correct": true}, {"text": "People made bonfires in their houses.", "correct": false}, {"text": "People wore costumes and masks.", "correct": true}, {"text": "The first lanterns were made from pumpkins.", "correct": false}, {"text": "Children put a candle inside the turnip.", "correct": true}, {"text": "In America people used a pumpkin.", "correct": true}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    -- блок 7 (sort_order 6)
    (v_lesson, 'speaking', replace($blk${"title": "🎤 Как ты празднуешь Хэллоуин?", "html": "<p>Прочитай пример. Нажми на запись и расскажи, как ты празднуешь Хэллоуин.</p><p><i>On Halloween I wear a costume. This year I'm a vampire! My friends and I carve a pumpkin and put a candle inside — now it's a lantern. In the evening we watch a scary film and eat lots of sweets. I don't believe in ghosts, but I love scary stories!</i></p><p><b>What do you wear? Do you carve a pumpkin? What do you eat? What do you do in the evening?</b></p>", "image": "@@MEDIA@@halloween/13/lead13.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  delete from classroom_blocks where lesson_id = v_lesson and sort_order >= 7;
end
$mig$;
