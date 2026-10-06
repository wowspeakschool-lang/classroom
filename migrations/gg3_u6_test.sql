-- Go Getter 3 · Unit 6 · Unit 6 Test
-- собрано tools/gg3_build.py --lesson u6_test
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 6', 6 from classroom_courses c
where c.slug = 'gg3'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 6');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Unit 6 Test', 'test', 90, false, 0
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg3' and u.title = 'Unit 6'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Unit 6 Test');
update classroom_lessons l set kind = 'test', pass_threshold = 90, sort_order = 0
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg3' and u.title = 'Unit 6' and l.title = 'Unit 6 Test';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg3' and u.title = 'Unit 6' and l.title = 'Unit 6 Test';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'match', replace($blk${"title": "Соедини фразу с картинкой", "pairs": [{"left_image": "@@MEDIA@@gg3/u6/bake.webp", "right": "bake", "right_audio_tts": "bake"}, {"left_image": "@@MEDIA@@gg3/u6/bowl.webp", "right": "bowl", "right_audio_tts": "bowl"}, {"left_image": "@@MEDIA@@gg3/u6/fry.webp", "right": "fry", "right_audio_tts": "fry"}, {"left_image": "@@MEDIA@@gg3/u6/mix.webp", "right": "mix", "right_audio_tts": "mix"}, {"left_image": "@@MEDIA@@gg3/u6/peel.webp", "right": "peel", "right_audio_tts": "peel"}, {"left_image": "@@MEDIA@@gg3/u6/fork.webp", "right": "fork", "right_audio_tts": "fork"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'exact_input', replace($blk${"title": "Посмотри на картинку и впиши пропущенные буквы", "items": [{"image": "@@MEDIA@@gg3/u6/cake_tin.webp", "prompt": "1. Напиши фразу целиком: c_k_ t_n", "accept": ["cake tin", "Cake tin"]}, {"image": "@@MEDIA@@gg3/u6/chop.webp", "prompt": "2. Напиши слово целиком: ch_p", "accept": ["chop", "Chop"]}, {"image": "@@MEDIA@@gg3/u6/oven.webp", "prompt": "3. Напиши слово целиком: ov_n", "accept": ["oven", "Oven"]}, {"image": "@@MEDIA@@gg3/u6/pot.webp", "prompt": "4. Напиши слово целиком: p_t", "accept": ["pot", "Pot"]}, {"image": "@@MEDIA@@gg3/u6/spoon.webp", "prompt": "5. Напиши слово целиком: sp__n", "accept": ["spoon", "Spoon"]}, {"image": "@@MEDIA@@gg3/u6/slice.webp", "prompt": "6. Напиши слово целиком: sl_c_", "accept": ["slice", "Slice"]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'quiz', replace($blk${"title": "Прочитай предложение и выбери пропущенное слово", "questions": [{"q": "I ___ a cake today.", "type": "single", "options": [{"text": "have bake"}, {"text": "have baked"}], "correct": [1]}, {"q": "She ___ spicy food.", "type": "single", "options": [{"text": "has never tried"}, {"text": "have ever tried"}, {"text": "never try"}], "correct": [0]}, {"q": "They ___ anything salty.", "type": "single", "options": [{"text": "hasn't eaten"}, {"text": "haven't eaten"}], "correct": [1]}, {"q": "___ dinner for your family?", "type": "single", "options": [{"text": "Do you ever cook"}, {"text": "Have you cooked ever"}, {"text": "Have you ever cooked"}], "correct": [2]}, {"q": "He ___ the vegetables yet.", "type": "single", "options": [{"text": "haven't chopped"}, {"text": "hasn't chopped"}, {"text": "didn't chopped"}], "correct": [1]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'order', replace($blk${"words": ["I", "have", "never", "baked", "a cake", "in this oven."], "sentence": "I have never baked a cake in this oven.", "audio_tts": "I have never baked a cake in this oven."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'order', replace($blk${"words": ["Have", "you", "ever", "tried", "sour soup?"], "sentence": "Have you ever tried sour soup?", "audio_tts": "Have you ever tried sour soup?"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'order', replace($blk${"words": ["She", "has", "sliced", "the vegetables."], "sentence": "She has sliced the vegetables.", "audio_tts": "She has sliced the vegetables."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'order', replace($blk${"words": ["They", "haven't", "mixed", "the ingredients", "yet."], "sentence": "They haven't mixed the ingredients yet.", "audio_tts": "They haven't mixed the ingredients yet."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'order', replace($blk${"words": ["He", "has", "added", "salt", "to the pot."], "sentence": "He has added salt to the pot.", "audio_tts": "He has added salt to the pot."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'speaking', replace($blk${"title": "SPEAKING TASK 1 🎤", "needs_review": true, "html": "<p>Опиши картинку, ответь на вопросы.</p><ul><li>What is she doing now?</li><li>What has she done already?</li><li>What kitchen tools can you see?</li><li>Has she peeled or chopped anything?</li><li>Do you like cooking? Why / why not?</li><li>What have you cooked recently?</li></ul><p>Нажми на микрофон и запиши ответ.</p>", "image": "@@MEDIA@@gg3/u6/scene_cooking.webp"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8),
('<lesson_id>', 'speaking', replace($blk${"title": "SPEAKING TASK 2 🎤", "needs_review": true, "html": "<p>Ответь на вопросы (не забудь отвечать полными предложениями).</p><ol><li>Have you ever baked a cake?</li><li>Have you ever tried something spicy?</li><li>What delicious food have you eaten recently?</li><li>What disgusting food have you tried?</li><li>Have you ever cooked dinner for your family?</li><li>Have you ever chopped vegetables?</li><li>Have you ever eaten something very sour?</li></ol><p>Нажми на микрофон и запиши ответ.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 9)
returning sort_order, type;
