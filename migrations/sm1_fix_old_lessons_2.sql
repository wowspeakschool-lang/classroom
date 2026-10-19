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
