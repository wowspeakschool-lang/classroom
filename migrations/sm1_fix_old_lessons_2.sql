-- Super Minds 1 · правка 36 старых уроков (Unit 0–4, Unit 5 HW1–3), 19.10.2026
-- Правка на месте: только нужные блоки, озвучка (audio) соседних блоков не трогается.
-- Номера блоков в комментариях — как в редакторе (sort_order + 1), «было → стало».
-- Удаление — только через CTE (без CTE MCP зависает).

-- 0. Бэкап блоков затронутых уроков ------------------------------------------
create table if not exists classroom_blocks_backup_sm1_edit_20261019 (
  id uuid, lesson_id uuid, sort_order int, type text, payload jsonb,
  saved_at timestamptz default now());
alter table classroom_blocks_backup_sm1_edit_20261019 enable row level security;

insert into classroom_blocks_backup_sm1_edit_20261019 (id, lesson_id, sort_order, type, payload)
select b.id, b.lesson_id, b.sort_order, b.type, b.payload from classroom_blocks b
where b.lesson_id in (
  '58470770-2b34-4271-96b2-cfa1fa05f1e5', -- U1 HW4
  '33b5871b-e8db-4fd4-8345-a62675ba0f0f', -- U2 HW4
  '0ad1129b-30c4-40dc-b4f6-5956c61d137c', -- U3 HW4
  'd9c638fc-2298-4987-9d7c-c6a966e1905b', -- U4 HW4
  '16a136ff-8db9-4059-bcc8-2883e7d375d3', -- U2 HW3
  '436d7600-4022-4e42-967c-f30e9e8f16b4', -- U0 Test
  '71133446-3777-4dbd-a5a2-1ba78fe82fe9', -- U0 HW4
  '9068f8af-8b75-457f-9435-a148c545b41d') -- U5 HW2
  and not exists (select 1 from classroom_blocks_backup_sm1_edit_20261019 k where k.id = b.id);

-- 1. Интерактивные видео убраны ---------------------------------------------

-- U1 HW4: бл. 11 (текст «ИНТЕРАКТИВНОЕ ВИДЕО») и бл. 12 (video) удалены; прощание 13 → 11
with d as (delete from classroom_blocks where lesson_id='58470770-2b34-4271-96b2-cfa1fa05f1e5'
  and sort_order in (10,11) and type in ('text','video') returning 1) select count(*) from d;
update classroom_blocks set sort_order = sort_order + 1000 where lesson_id='58470770-2b34-4271-96b2-cfa1fa05f1e5' and sort_order >= 12;
update classroom_blocks set sort_order = sort_order - 1000 - 2 where lesson_id='58470770-2b34-4271-96b2-cfa1fa05f1e5' and sort_order >= 1000;
with u as (update classroom_blocks set payload = jsonb_set(payload,'{html}', to_jsonb(
    replace(replace(payload->>'html',
      'В этом уроке тебя ждут текст и упражнения к нему, а также крутое интерактивное видео!',
      'В этом уроке тебя ждут текст и упражнения к нему!'),
      '<p>Интерактивное видео с заданием ждёт тебя в конце этого урока. Посмотришь его — будешь нереально крут!</p>','')))
  where lesson_id='58470770-2b34-4271-96b2-cfa1fa05f1e5' and sort_order=0 returning id) select count(*) from u;

-- U2 HW4: бл. 14 (video) удалён; прощание 15 → 14
with d as (delete from classroom_blocks where lesson_id='33b5871b-e8db-4fd4-8345-a62675ba0f0f'
  and sort_order = 13 and type = 'video' returning 1) select count(*) from d;
update classroom_blocks set sort_order = sort_order + 1000 where lesson_id='33b5871b-e8db-4fd4-8345-a62675ba0f0f' and sort_order >= 14;
update classroom_blocks set sort_order = sort_order - 1000 - 1 where lesson_id='33b5871b-e8db-4fd4-8345-a62675ba0f0f' and sort_order >= 1000;
with u as (update classroom_blocks set payload = jsonb_set(payload,'{html}', to_jsonb(
    replace(payload->>'html','<p>В дополнение к этому заданию тебя ждет интерактивное видео — оно в конце урока.</p>','')))
  where lesson_id='33b5871b-e8db-4fd4-8345-a62675ba0f0f' and sort_order=0 returning id) select count(*) from u;
with u as (update classroom_blocks set payload = jsonb_set(payload,'{html}', to_jsonb(
    replace(payload->>'html','<p>Не забудь про ещё одно задание — интерактивное видео выше!</p>','')))
  where lesson_id='33b5871b-e8db-4fd4-8345-a62675ba0f0f' and sort_order=13 returning id) select count(*) from u;

-- U3 HW4: бл. 10 (текст «ЕЩЁ ОДНО ЗАДАНИЕ» про видео) и бл. 11 (video) удалены; прощание 12 → 10
with d as (delete from classroom_blocks where lesson_id='0ad1129b-30c4-40dc-b4f6-5956c61d137c'
  and sort_order in (9,10) and type in ('text','video') returning 1) select count(*) from d;
update classroom_blocks set sort_order = sort_order + 1000 where lesson_id='0ad1129b-30c4-40dc-b4f6-5956c61d137c' and sort_order >= 11;
update classroom_blocks set sort_order = sort_order - 1000 - 2 where lesson_id='0ad1129b-30c4-40dc-b4f6-5956c61d137c' and sort_order >= 1000;
with u as (update classroom_blocks set payload = jsonb_set(payload,'{html}', to_jsonb(
    replace(replace(payload->>'html',
      'В этом уроке тебя ждут текст и упражнения к нему, а также крутое интерактивное видео!',
      'В этом уроке тебя ждут текст и упражнения к нему!'),
      '<p>В дополнение к этому домашнему заданию идет интерактивное видео с заданием — оно в конце этого урока.</p>','')))
  where lesson_id='0ad1129b-30c4-40dc-b4f6-5956c61d137c' and sort_order=0 returning id) select count(*) from u;

-- U4 HW4: бл. 11 (текст «Ещё одно задание — интерактивное видео») и бл. 12 (video) удалены; прощание 13 → 11
with d as (delete from classroom_blocks where lesson_id='d9c638fc-2298-4987-9d7c-c6a966e1905b'
  and sort_order in (10,11) and type in ('text','video') returning 1) select count(*) from d;
update classroom_blocks set sort_order = sort_order + 1000 where lesson_id='d9c638fc-2298-4987-9d7c-c6a966e1905b' and sort_order >= 12;
update classroom_blocks set sort_order = sort_order - 1000 - 2 where lesson_id='d9c638fc-2298-4987-9d7c-c6a966e1905b' and sort_order >= 1000;
with u as (update classroom_blocks set payload = jsonb_set(payload,'{html}', to_jsonb(
    replace(payload->>'html',
      'В этом уроке тебя ждут текст и упражнения к нему, а также крутое интерактивное видео!',
      'В этом уроке тебя ждут текст и упражнения к нему!')))
  where lesson_id='d9c638fc-2298-4987-9d7c-c6a966e1905b' and sort_order=0 returning id) select count(*) from u;

-- 2. U2 HW3 бл. 5 и 10 — ролики YouTube --------------------------------------
with u as (update classroom_blocks set payload = (payload - 'needs_review') || jsonb_build_object(
    'url','https://www.youtube.com/watch?v=juvIpZgpfTg','provider','youtube',
    'title','ADJECTIVES · Animals (Smile and Learn)')
  where lesson_id='16a136ff-8db9-4059-bcc8-2883e7d375d3' and sort_order=4 and type='video' returning id) select count(*) from u;
with u as (update classroom_blocks set payload = (payload - 'needs_review') || jsonb_build_object(
    'url','https://www.youtube.com/watch?v=54evC5ZupQg','provider','youtube',
    'title','Articles: a and an (Elearning Studio)')
  where lesson_id='16a136ff-8db9-4059-bcc8-2883e7d375d3' and sort_order=9 and type='video' returning id) select count(*) from u;
with u as (update classroom_blocks set payload = jsonb_set(payload,'{html}', to_jsonb(
    replace(payload->>'html','В этом уроке тебя ждут интерактивные видео.','В этом уроке тебя ждут видео и задания к ним.')))
  where lesson_id='16a136ff-8db9-4059-bcc8-2883e7d375d3' and sort_order=0 returning id) select count(*) from u;

-- 3. U0 Test бл. 3 — «Послушай слово и выбери его» (слова из бл. 2 теста) ------
with u as (update classroom_blocks set payload = $j${
  "title": "Послушай слово и выбери его",
  "questions": [
    {"q": "", "type": "single", "audio": "", "audio_tts": {"text": "sit", "voice": "en_US-amy"},
     "correct": [1], "options": [{"text": "sat"}, {"text": "sit"}, {"text": "sip"}]},
    {"q": "", "type": "single", "audio": "", "audio_tts": {"text": "tap", "voice": "en_US-amy"},
     "correct": [2], "options": [{"text": "tip"}, {"text": "pat"}, {"text": "tap"}]},
    {"q": "", "type": "single", "audio": "", "audio_tts": {"text": "cat", "voice": "en_US-amy"},
     "correct": [0], "options": [{"text": "cat"}, {"text": "cap"}, {"text": "can"}]},
    {"q": "", "type": "single", "audio": "", "audio_tts": {"text": "mint", "voice": "en_US-amy"},
     "correct": [1], "options": [{"text": "mat"}, {"text": "mint"}, {"text": "man"}]}
  ],
  "needs_review": false}$j$::jsonb
  where lesson_id='436d7600-4022-4e42-967c-f30e9e8f16b4' and sort_order=2 and type='quiz' returning id) select count(*) from u;

-- 4. U0 HW4 бл. 6 — «Послушай фразу и выбери её» (фразы урока из бл. 2) -----------
with u as (update classroom_blocks set payload = $j${
  "title": "Послушай фразу и выбери её",
  "questions": [
    {"q": "", "type": "single", "audio": "", "audio_tts": {"text": "Look at me!", "voice": "en_US-amy"},
     "correct": [2], "options": [{"text": "My turn."}, {"text": "Listen to me."}, {"text": "Look at me!"}]},
    {"q": "", "type": "single", "audio": "", "audio_tts": {"text": "My turn.", "voice": "en_US-amy"},
     "correct": [0], "options": [{"text": "My turn."}, {"text": "Look at me!"}, {"text": "Listen to me."}]},
    {"q": "", "type": "single", "audio": "", "audio_tts": {"text": "Listen to me.", "voice": "en_US-amy"},
     "correct": [1], "options": [{"text": "Look at me!"}, {"text": "Listen to me."}, {"text": "My turn."}]}
  ],
  "needs_review": false}$j$::jsonb
  where lesson_id='71133446-3777-4dbd-a5a2-1ba78fe82fe9' and sort_order=5 and type='quiz' returning id) select count(*) from u;

-- 5. U5 HW2 бл. 12 — варианты текстом; вопросы и их звук (уже озвучены) сохраняются --
with newopts(i, opts) as (values
  (0, $o$[{"text": "On Mondays I go to school."}, {"text": "On Saturdays I play football."}, {"text": "Yes, I do."}]$o$::jsonb),
  (1, $o$[{"text": "I'm Bob."}, {"text": "On Saturdays I ride my bike."}, {"text": "On Sundays I sleep."}]$o$::jsonb),
  (2, $o$[{"text": "On Saturdays I go swimming."}, {"text": "I'm seven."}, {"text": "On Tuesdays I do karate."}]$o$::jsonb),
  (3, $o$[{"text": "Yes, I am."}, {"text": "On Fridays I play ball."}, {"text": "On Saturdays I play the piano."}]$o$::jsonb)),
qs as (
  select jsonb_agg(q.value || jsonb_build_object('type','single','options', n.opts) order by q.ord) as arr
  from classroom_blocks b,
       jsonb_array_elements(b.payload->'questions') with ordinality q(value, ord)
       join newopts n on n.i = q.ord - 1
  where b.lesson_id='9068f8af-8b75-457f-9435-a148c545b41d' and b.sort_order=11),
u as (update classroom_blocks b set payload = b.payload || jsonb_build_object(
    'questions', qs.arr, 'needs_review', false,
    'title', 'Ребята рассказывают, что они делают по субботам. Послушай вопрос и выбери подходящий ответ.')
  from qs where b.lesson_id='9068f8af-8b75-457f-9435-a148c545b41d' and b.sort_order=11 and b.type='quiz'
  returning b.id) select count(*) from u;

-- 7. U2 HW4 бл. 7 и 9 — история про гонку ------------------------------------
-- бл. 7: после кадров 1–6 вторая картинка — кадры 7–8 (номера в кружках оставлены: история по порядку)
with u as (update classroom_blocks set payload = jsonb_set(payload,'{html}', to_jsonb(
    (payload->>'html') || '<p><img src="https://classroom.wowteach.ru/media/sm1/old/u2_hw4_story_7_8.webp"></p>'))
  where lesson_id='33b5871b-e8db-4fd4-8345-a62675ba0f0f' and sort_order=6
    and payload->>'html' not like '%u2_hw4_story_7_8%' returning id) select count(*) from u;
-- бл. 9: сетка 2×4 из 8 кадров без номеров, порядок по строкам: 3, 6 / 1, 8 / 2, 7 / 4, 5
with u as (update classroom_blocks set payload = $j${
  "mode": "label",
  "image": "https://classroom.wowteach.ru/media/sm1/old/u2_hw4_story_grid.webp",
  "title": "Картинки перемешались! Давай поможем героям восстановить порядок истории. Подпиши каждую картинку: первую картинку истории — «Picture 1», вторую — «Picture 2», и так по порядку. Постарайся не подсматривать, а в конце можешь проверить себя по тексту.",
  "points": [
    {"x": 25.3, "y": 12.9, "text": "Picture 3"},
    {"x": 74.7, "y": 12.9, "text": "Picture 6"},
    {"x": 25.3, "y": 37.6, "text": "Picture 1"},
    {"x": 74.7, "y": 37.6, "text": "Picture 8"},
    {"x": 25.3, "y": 62.4, "text": "Picture 2"},
    {"x": 74.7, "y": 62.4, "text": "Picture 7"},
    {"x": 25.3, "y": 87.1, "text": "Picture 4"},
    {"x": 74.7, "y": 87.1, "text": "Picture 5"}
  ],
  "extras": [],
  "needs_review": false}$j$::jsonb
  where lesson_id='33b5871b-e8db-4fd4-8345-a62675ba0f0f' and sort_order=8 and type='hotspot' returning id) select count(*) from u;

-- 6. НЕ ПРИМЕНЕНО — ждёт картинок Анны (лист «звуки U3/U4»). После нарезки в media/sm1/old/:
-- U3 HW2 бл. 4 (lesson 5965d94d-9279-42fe-a70c-66d70268a340, sort_order 3):
-- update classroom_blocks set payload = $j${"questions": [
--   {"q": "Послушай звук. Посмотри на картинки. В названии каких предметов есть этот звук? Выбери все подходящие картинки!",
--    "type": "multiple", "audio": "", "audio_tts": {"text": "day, play, name", "voice": "en_US-amy"}, "correct": [0, 1],
--    "options": [{"image": "https://classroom.wowteach.ru/media/sm1/old/u3_hw2_cake.webp"}, {"image": "https://classroom.wowteach.ru/media/sm1/old/u3_hw2_snake.webp"},
--                {"image": "https://classroom.wowteach.ru/media/sm1/old/u3_hw2_spy.webp"},  {"image": "https://classroom.wowteach.ru/media/sm1/old/u3_hw2_fly.webp"}]},
--   {"q": "…то же…", "type": "multiple", "audio": "", "audio_tts": {"text": "my, by, why", "voice": "en_US-amy"}, "correct": [2, 3],
--    "options": [plane, gate, fly, spy]}], "needs_review": false}$j$::jsonb
--   where lesson_id='5965d94d-9279-42fe-a70c-66d70268a340' and sort_order=3 and type='quiz';
-- U4 HW5 бл. 9 (lesson 0fcc69fc-2b29-4598-888d-85cd9462b171, sort_order 8):
--   q1 audio_tts "saw, draw, jaw", options [straw, cloud, house], correct [0];
--   q2 audio_tts "how, now, wow",  options [paw, mouse, cloud],  correct [1, 2]; файлы u4_hw5_<слово>.webp

-- =====================================================================
-- Часть 2 (решения Анны 19.10, вечер)
-- =====================================================================
insert into classroom_blocks_backup_sm1_edit_20261019 (id, lesson_id, sort_order, type, payload)
select b.id, b.lesson_id, b.sort_order, b.type, b.payload from classroom_blocks b
where b.lesson_id in (
  '036693ef-62ce-4a5a-9dbf-fb996b1b86ee', -- U0 HW1
  '9ad9086c-a2c7-4af7-8a01-92119918e456', -- U0 HW2
  'a56bc2b0-cd78-466e-9dcb-da787da7d949', -- U0 HW3
  '46f00a36-3fad-4ce0-9912-1a7a4896b8f8', -- U2 HW1
  '364038a5-b711-4f8d-8c0e-a791b60692e7', -- U3 HW1
  '575d831e-e9a5-4af9-b3a8-cd6e7ac543ca') -- U5 HW1
  and not exists (select 1 from classroom_blocks_backup_sm1_edit_20261019 k where k.id = b.id);

-- A. U2 HW3: ролики YouTube убраны, на их месте — карточки-правила (text с картинкой)
with u0 as (update classroom_blocks set payload = jsonb_set(payload,'{html}', to_jsonb(
    replace(payload->>'html','В этом уроке тебя ждут видео и задания к ним.','В этом уроке тебя ждут два правила и задания к ним.')))
  where lesson_id='16a136ff-8db9-4059-bcc8-2883e7d375d3' and sort_order=0 returning id),
u3 as (update classroom_blocks set payload = jsonb_build_object('html',
    '<p>А теперь давай узнаем, как описывать животных и игрушки!</p><p><b>Прочитай правило и запомни его.</b></p>')
  where lesson_id='16a136ff-8db9-4059-bcc8-2883e7d375d3' and sort_order=3 and type='text' returning id),
u4 as (update classroom_blocks set type='text', payload = jsonb_build_object('html',
    '<p><img src="https://classroom.wowteach.ru/media/sm1/old/u2_hw3_rule_adjectives.webp"></p>')
  where lesson_id='16a136ff-8db9-4059-bcc8-2883e7d375d3' and sort_order=4 and type='video' returning id),
u8 as (update classroom_blocks set payload = jsonb_build_object('html',
    '<p>Ух ты! Тебя ждёт ещё одно правило — про маленькие слова <b>a</b> и <b>an</b>.</p><p><b>Прочитай его внимательно!</b></p>')
  where lesson_id='16a136ff-8db9-4059-bcc8-2883e7d375d3' and sort_order=8 and type='text' returning id),
u9 as (update classroom_blocks set type='text', payload = jsonb_build_object('html',
    '<p><img src="https://classroom.wowteach.ru/media/sm1/old/u2_hw3_rule_a_an.webp"></p>')
  where lesson_id='16a136ff-8db9-4059-bcc8-2883e7d375d3' and sort_order=9 and type='video' returning id),
u10 as (update classroom_blocks set payload = jsonb_set(payload,'{title}',
    '"Молодец! Посмотри на правило ещё раз и выбери правильный артикль в предложениях!"')
  where lesson_id='16a136ff-8db9-4059-bcc8-2883e7d375d3' and sort_order=10 and type='gaps' returning id)
select (select count(*) from u0)+(select count(*) from u3)+(select count(*) from u4)+(select count(*) from u8)+(select count(*) from u9)+(select count(*) from u10) as n; -- ждём 6

-- B. U2 HW4 бл. 5: история до конца (кадры 7–8), audio обнулён под «Озвучить пачкой»
with u as (update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{audio}','""'),'{audio_tts,text}', to_jsonb(
    (payload->'audio_tts'->>'text') || ' Misty: Woah! Red team driver: No! Man: Congratulations, Misty! You''re first! Misty: Thank you!'))
  where lesson_id='33b5871b-e8db-4fd4-8345-a62675ba0f0f' and sort_order=4 and type='text'
    and payload->'audio_tts'->>'text' not like '%Congratulations%' returning id) select count(*) from u;

-- C. «Слово — перевод» → «картинка — слово». Картинка слева (left_image), английское слово справа;
--    уже нажатая озвучка слова переезжает left_audio → right_audio.
create or replace function pg_temp.pic_pairs(p_lesson uuid, p_sort int, p_map jsonb, p_title text) returns int
language plpgsql as $f$
declare v_arr jsonb; v_n int; v_total int; v_cnt int;
begin
  select jsonb_agg(jsonb_strip_nulls(jsonb_build_object(
           'left', '', 'left_image', p_map->>(t.p->>'left'),
           'right', t.p->>'left', 'right_audio', t.p->'left_audio', 'right_audio_tts', t.p->'left_audio_tts')) order by t.ord),
         count(*) filter (where p_map ? (t.p->>'left')), count(*)
    into v_arr, v_n, v_total
    from classroom_blocks b, jsonb_array_elements(b.payload->'pairs') with ordinality t(p, ord)
   where b.lesson_id = p_lesson and b.sort_order = p_sort and b.type = 'match';
  if v_total = 0 or v_n <> v_total then raise exception 'нет картинки для части слов: % из %', v_n, v_total; end if;
  update classroom_blocks set payload = payload || jsonb_build_object('pairs', v_arr, 'title', p_title, 'needs_review', false)
   where lesson_id = p_lesson and sort_order = p_sort and type = 'match';
  get diagnostics v_cnt = row_count; return v_cnt;
end $f$;

select pg_temp.pic_pairs('036693ef-62ce-4a5a-9dbf-fb996b1b86ee', 3, $m${
  "friends": "https://classroom.wowteach.ru/media/sm1/old/u0_friends.webp",
  "Thunder": "https://classroom.wowteach.ru/media/sm1/legacy/af307dbdc2ee.webp",
  "Misty":   "https://classroom.wowteach.ru/media/sm1/legacy/eb68810585d6.webp",
  "Whisper": "https://classroom.wowteach.ru/media/sm1/legacy/746c511616d8.webp",
  "Flash":   "https://classroom.wowteach.ru/media/sm1/legacy/32dd089617ca.webp"}$m$::jsonb,
  'Соедини картинку и слово');
select pg_temp.pic_pairs('036693ef-62ce-4a5a-9dbf-fb996b1b86ee', 5, $m${
  "friends": "https://classroom.wowteach.ru/media/sm1/old/u0_friends.webp",
  "Thunder": "https://classroom.wowteach.ru/media/sm1/legacy/af307dbdc2ee.webp",
  "Misty":   "https://classroom.wowteach.ru/media/sm1/legacy/eb68810585d6.webp",
  "Whisper": "https://classroom.wowteach.ru/media/sm1/legacy/746c511616d8.webp",
  "Flash":   "https://classroom.wowteach.ru/media/sm1/legacy/32dd089617ca.webp"}$m$::jsonb,
  'Найди пару: послушай слово и найди картинку');
select pg_temp.pic_pairs('9ad9086c-a2c7-4af7-8a01-92119918e456', 4, (
  select jsonb_object_agg(w, 'https://classroom.wowteach.ru/media/sm1/old/num_' || n || '.webp')
  from unnest(array['one','two','three','four','five','six','seven','eight','nine','ten']) with ordinality x(w, n)),
  'Соедини цифру и слово');
select pg_temp.pic_pairs('a56bc2b0-cd78-466e-9dcb-da787da7d949', 4, (
  select jsonb_object_agg(w, 'https://classroom.wowteach.ru/media/sm1/old/color_' || w || '.webp')
  from unnest(array['yellow','red','orange','purple','blue','green']) w), 'Соедини цвет и слово');
select pg_temp.pic_pairs('a56bc2b0-cd78-466e-9dcb-da787da7d949', 7, (
  select jsonb_object_agg(w, 'https://classroom.wowteach.ru/media/sm1/old/color_' || w || '.webp')
  from unnest(array['yellow','red','orange','purple','blue','green']) w), 'Найди пару: послушай слово и найди цвет');
select pg_temp.pic_pairs('46f00a36-3fad-4ce0-9912-1a7a4896b8f8', 3, $m${
  "doll": "https://classroom.wowteach.ru/media/sm1/u2/toy_doll.webp",
  "ball": "https://classroom.wowteach.ru/media/sm1/u2/t_yellow_ball.webp",
  "kite": "https://classroom.wowteach.ru/media/sm1/u2/toy_kite.webp",
  "car":  "https://classroom.wowteach.ru/media/sm1/u2/toy_car.webp",
  "bike": "https://classroom.wowteach.ru/media/sm1/u2/t_bike.webp",
  "computer game": "https://classroom.wowteach.ru/media/sm1/u5/act_computer_games.webp",
  "go-kart": "https://classroom.wowteach.ru/media/sm1/u2/toy_go_kart.webp",
  "train": "https://classroom.wowteach.ru/media/sm1/u2/toy_train.webp",
  "monster": "https://classroom.wowteach.ru/media/sm1/u2/toy_monster.webp",
  "plane": "https://classroom.wowteach.ru/media/sm1/u2/t_plane.webp"}$m$::jsonb,
  'Найди пару: картинка и слово');
select pg_temp.pic_pairs('364038a5-b711-4f8d-8c0e-a791b60692e7', 3, (
  select jsonb_object_agg(w, 'https://classroom.wowteach.ru/media/sm1/u3/animal_' || w || '.webp')
  from unnest(array['elephant','rat','lizard','frog','spider','dog','cat','duck','donkey']) w),
  'Найди пару: картинка и слово');

-- U2 HW3 бл. 6: слова-противоположности (подводит правило бл. 5); озвучка обоих слов сохранена
with old as (select p->>'left' w, p->'left_audio' a, p->'left_audio_tts' t
    from classroom_blocks b, jsonb_array_elements(b.payload->'pairs') p
    where b.lesson_id='16a136ff-8db9-4059-bcc8-2883e7d375d3' and b.sort_order=5 and b.type='match'),
pr(i,l,r) as (values (1,'big','small'),(2,'fast','slow'),(3,'long','short'),(4,'clean','dirty'),(5,'fat','thin')),
arr as (select jsonb_agg(jsonb_strip_nulls(jsonb_build_object('left',pr.l,'left_audio',ol.a,'left_audio_tts',ol.t,
          'right',pr.r,'right_audio',orr.a,'right_audio_tts',orr.t)) order by pr.i) a, count(*) n
        from pr join old ol on ol.w=pr.l join old orr on orr.w=pr.r),
u as (update classroom_blocks b set payload = b.payload || jsonb_build_object('pairs', arr.a,
    'title','Перейдём к практике! Посмотри на правило ещё раз и соедини слова-противоположности.','needs_review',false)
  from arr where arr.n=5 and b.lesson_id='16a136ff-8db9-4059-bcc8-2883e7d375d3' and b.sort_order=5 and b.type='match'
  returning b.id) select count(*) from u;

-- U2 HW4 бл. 12: кадр истории ↔ фраза из него (кадры без номеров)
with old as (select p->'left_audio' a, p->'left_audio_tts' t from classroom_blocks b, jsonb_array_elements(b.payload->'pairs') p
    where b.lesson_id='33b5871b-e8db-4fd4-8345-a62675ba0f0f' and b.sort_order=11 and p->>'left'='that isn''t fair'),
np as (select jsonb_build_array(
  jsonb_build_object('left','','left_image','https://classroom.wowteach.ru/media/sm1/old/u2_hw4_frame_1.webp','right','What an ugly old go-kart!','right_audio','','right_audio_tts',jsonb_build_object('text','What an ugly old go-kart!','voice','en_US-amy')),
  jsonb_build_object('left','','left_image','https://classroom.wowteach.ru/media/sm1/old/u2_hw4_frame_2.webp','right','One, two, three – go!','right_audio','','right_audio_tts',jsonb_build_object('text','One, two, three, go!','voice','en_US-amy')),
  jsonb_build_object('left','','left_image','https://classroom.wowteach.ru/media/sm1/old/u2_hw4_frame_3.webp','right','She''s first! Stop her!','right_audio','','right_audio_tts',jsonb_build_object('text','She''s first! Stop her!','voice','en_US-amy')),
  jsonb_strip_nulls(jsonb_build_object('left','','left_image','https://classroom.wowteach.ru/media/sm1/old/u2_hw4_frame_5.webp','right','That isn''t fair!','right_audio',(select a from old),'right_audio_tts',(select t from old))),
  jsonb_build_object('left','','left_image','https://classroom.wowteach.ru/media/sm1/old/u2_hw4_frame_6.webp','right','Hold on, Misty!','right_audio','','right_audio_tts',jsonb_build_object('text','Hold on, Misty!','voice','en_US-amy')),
  jsonb_build_object('left','','left_image','https://classroom.wowteach.ru/media/sm1/old/u2_hw4_frame_8.webp','right','Congratulations, Misty! You''re first!','right_audio','','right_audio_tts',jsonb_build_object('text','Congratulations, Misty! You''re first!','voice','en_US-amy'))) a),
u as (update classroom_blocks b set payload = b.payload || jsonb_build_object('pairs', np.a,
    'title','Посмотри на картинки из истории и соедини каждую с фразой, которая там звучит.','needs_review',false)
  from np where b.lesson_id='33b5871b-e8db-4fd4-8345-a62675ba0f0f' and b.sort_order=11 and b.type='match' returning b.id)
select count(*) from u;

-- U3 HW1 бл. 18: match «слово — перевод» → sort по буквосочетаниям EA / AY, озвучка слов сохранена
with old as (select p->>'left' w, jsonb_strip_nulls(jsonb_build_object('text',p->>'left','audio',p->'left_audio','audio_tts',p->'left_audio_tts')) it
    from classroom_blocks b, jsonb_array_elements(b.payload->'pairs') p
    where b.lesson_id='364038a5-b711-4f8d-8c0e-a791b60692e7' and b.sort_order=17 and b.type='match'),
g as (select jsonb_build_array(
   jsonb_build_object('name','EA','items',(select jsonb_agg(it order by w desc) from old where w in ('head','bread'))),
   jsonb_build_object('name','AY','items',(select jsonb_agg(it order by w desc) from old where w in ('tray','day')))) a,
   (select count(*) from old) n),
u as (update classroom_blocks b set type='sort', payload = jsonb_build_object('groups', g.a,
    'title','Посмотри на буквосочетания и слова. Разложи слова по группам: где EA, а где AY? Послушай, как они звучат.')
  from g where g.n=4 and b.lesson_id='364038a5-b711-4f8d-8c0e-a791b60692e7' and b.sort_order=17 and b.type='match' returning b.id)
select count(*) from u;

-- U5 HW1 бл. 6: дни недели — match «день — перевод» → sequence «расставь по порядку», озвучка сохранена
with it as (select jsonb_agg(jsonb_strip_nulls(jsonb_build_object('text',p->>'left','audio',p->'left_audio','audio_tts',p->'left_audio_tts')) order by ord) a, count(*) n
    from classroom_blocks b, jsonb_array_elements(b.payload->'pairs') with ordinality t(p,ord)
    where b.lesson_id='575d831e-e9a5-4af9-b3a8-cd6e7ac543ca' and b.sort_order=5 and b.type='match'),
u as (update classroom_blocks b set type='sequence', payload = jsonb_build_object('items', it.a,
    'title','Дни недели перепутались! Расставь их по порядку — от первого дня недели до последнего.')
  from it where it.n=7 and b.lesson_id='575d831e-e9a5-4af9-b3a8-cd6e7ac543ca' and b.sort_order=5 and b.type='match' returning b.id)
select count(*) from u;

-- Ждут листа картинок Анны (не применено): U1 HW1 бл. 4 (paper), U1 HW6 бл. 5 (look, touch, smell, taste).
-- Применено 19.10.2026: части A, B, C (функция pg_temp.pic_pairs создаётся и вызывается в одном запросе).
