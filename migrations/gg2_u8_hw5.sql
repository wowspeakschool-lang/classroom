-- Go Getter 2 · Unit 8 · Homework 5
-- собрано tools/gg2_build.py --lesson u8_hw5
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 8', 8 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 8');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 5', 'homework', 60, false, 4
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 8'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 5');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 4
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 8' and l.title = 'Homework 5';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 8' and l.title = 'Homework 5';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Сегодня мы с тобой попрактикуемся в чтении и сделаем много интересных упражнений!</p><p>Не забудь про дополнительное задание! Оно тебе понравится! Готов начать?</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Running for fun! 🏃</h3><p>Для начала внимательно прочитай текст ниже!</p><p><img src=\"@@MEDIA@@gg2/u8/book_running_poster.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'match', replace($blk${"title": "Прочитай текст ещё раз и соедини картинки с названиями!", "pairs": [{"left_image": "@@MEDIA@@gg2/u8/fun_races.webp", "right": "Fun Races!", "right_audio_tts": "Fun Races"}, {"left_image": "@@MEDIA@@gg2/u8/winter_run.webp", "right": "Winter Run!", "right_audio_tts": "Winter Run"}, {"left_image": "@@MEDIA@@gg2/u8/costume_run.webp", "right": "Costume Run!", "right_audio_tts": "Costume Run"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'text', replace($blk${"html": "<p>Молодец! Прочитай вопросы по тексту и выбери правильный ответ: <b>yes</b> или <b>no</b>.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'quiz', replace($blk${"title": "Yes or no?", "questions": [{"q": "Can families run in all the events?", "type": "single", "options": [{"text": "yes"}, {"text": "no"}], "correct": [1]}, {"q": "Is there a hot meal for the runners in the Winter Run?", "type": "single", "options": [{"text": "yes"}, {"text": "no"}], "correct": [0]}, {"q": "Can children over 12 run in the Fun Races?", "type": "single", "options": [{"text": "yes"}, {"text": "no"}], "correct": [1]}, {"q": "Are there three races in the Winter Run?", "type": "single", "options": [{"text": "yes"}, {"text": "no"}], "correct": [1]}, {"q": "Are there three races in the Costume Run?", "type": "single", "options": [{"text": "yes"}, {"text": "no"}], "correct": [0]}, {"q": "Is there a picnic at the Tree Park event?", "type": "single", "options": [{"text": "yes"}, {"text": "no"}], "correct": [0]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'text', replace($blk${"html": "<p>Давай ещё немного потренируемся! Как хорошо ты прочитал текст? Ответь на вопросы ниже!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'quiz', replace($blk${"title": "Ответь на вопросы по тексту", "questions": [{"q": "Which event is in a forest?", "type": "single", "options": [{"text": "Winter Run!"}, {"text": "Fun Races!"}, {"text": "Costume Run!"}], "correct": [0]}, {"q": "Which event is in a park?", "type": "single", "options": [{"text": "Winter Run!"}, {"text": "Fun Races!"}, {"text": "Costume Run!"}], "correct": [2]}, {"q": "Who can run in the Costume Run?", "type": "single", "options": [{"text": "families"}, {"text": "children aged 7–12"}, {"text": "children in costumes"}], "correct": [2]}, {"q": "What can you do in the afternoon at New Park School?", "type": "single", "options": [{"text": "play basketball"}, {"text": "have some soup"}, {"text": "have a picnic"}], "correct": [0]}, {"q": "What do you wear in the basketball game after the Fun Races?", "type": "single", "options": [{"text": "a costume"}, {"text": "gloves"}, {"text": "a hat"}], "correct": [1]}, {"q": "What food do you need for the Fun Races event?", "type": "single", "options": [{"text": "a soup"}, {"text": "an egg"}, {"text": "an apple"}], "correct": [1]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'task', replace($blk${"title": "Дополнительное задание — для настоящих чемпионов! 🏅", "needs_review": true, "html": "<p>Ответь на вопросы:</p><ol><li>What is your favourite running event in the text?</li><li>Do you like running?</li><li>Can you run 50 metres?</li><li>Can you run two kilometres?</li><li>Do you think running is better in winter or summer?</li></ol><p>Не забудь прочитать свои ответы учителю на уроке!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! 🎉</h3><p>Ты справился с домашним заданием! Ты — мегакрут! Увидимся на занятии. Goodbye!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8)
returning sort_order, type;
