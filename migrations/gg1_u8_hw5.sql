-- Go Getter 1 · Unit 8 · Sport and health · Homework 5
-- собрано tools/gg1_build.py --lesson u8_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · Sport and health', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · Sport and health');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · Sport and health';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Добро пожаловать на домашнее задание! Сегодня мы с тобой закрепим знания, полученные на уроке. Как ты помнишь, на уроке мы читали текст и выполняли упражнения по нему. Сегодня ты тоже будешь читать текст и выполнять задания, но уже самостоятельно!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u8/card_healthy.webp\" alt=\"Healthy Lifestyle\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Начнём с текста. Внимательно его прочитай — после него тебя ждут упражнения.</b></p><p><i>Sam is twelve. He's very sporty. He likes getting up early but he goes to bed very late. He goes swimming before school. After school he plays football. At the weekend he goes cycling with his friends. Sam's sister Tammy is ten. She doesn't like sport and she never does exercise. She likes reading and cooking. She goes to bed at nine, and she gets up at half past six.</i></p><p><i>Sam loves cakes and chocolate and he often eats pizza and chips, but Tammy doesn't usually eat them. He doesn't like fruit and he hates vegetables – but Tammy loves them. Tammy likes chocolate but she doesn't eat it a lot. Sam usually drinks cola, but Tammy doesn't like it. She drinks fruit juice or water.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Найди в тексте главное: выбери правильный вариант для Сэма и Тэмми", "questions": [{"q": "Sam ___ does exercise.", "type": "single", "options": [{"text": "often"}, {"text": "sometimes"}], "correct": [0]}, {"q": "Tammy ___ does exercise.", "type": "single", "options": [{"text": "usually"}, {"text": "never"}], "correct": [1]}, {"q": "Does Sam eat healthy food?", "type": "single", "options": [{"text": "no"}, {"text": "yes"}], "correct": [0]}, {"q": "Does Tammy eat healthy food?", "type": "single", "options": [{"text": "no"}, {"text": "yes"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай текст ещё раз и ответь на вопросы: впиши пропущенные слова", "mode": "type", "text": "1. What exercise does Sam do in the morning? — He goes __swimming__.\n2. When does Tammy do exercise? — She __never__ does exercise.\n3. What does Tammy like doing? — She likes __reading__ and __cooking__.\n4. What does Sam like eating? — He loves __cakes__ and __chocolate__.\n5. Does Tammy like fruit and vegetables? — __Yes|yes__, she does. She __loves__ them.\n6. What does Sam usually drink? — He usually drinks __cola__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Составь пары так, чтобы получились фразы о здоровом образе жизни", "pairs": [{"left": "eat", "right": "fruit and vegetables"}, {"left": "drink", "right": "a lot of water"}, {"left": "do", "right": "exercise"}, {"left": "brush", "right": "your teeth"}, {"left": "have", "right": "friends"}, {"left": "go", "right": "to bed early"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Мой образ жизни ✍️", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@gg1/u8/life_healthy_heart.webp\" alt=\"Healthy lifestyle\" style=\"height:200px\"></p><p>Давай напишем небольшой рассказ о твоём образе жизни! Что ты делаешь, чтобы быть здоровым, а что не делаешь?</p><p><i>Например: I always brush my teeth in the morning. I often drink water.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
