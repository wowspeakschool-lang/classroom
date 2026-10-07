-- Super Minds 1 · Unit 3 · My pets · Unit 3 Test
-- собрано tools/sm1_build.py --lesson u3_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 3 · My pets', 3
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 3 · My pets');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 3 · My pets';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Unit 3 Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Unit 3 Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Unit 3 Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Напиши по-английски: слон", "accept": ["elephant", "Elephant"]}, {"prompt": "Напиши по-английски: крыса", "accept": ["rat", "Rat"]}, {"prompt": "Напиши по-английски: ящерица", "accept": ["lizard", "Lizard"]}, {"prompt": "Напиши по-английски: лягушка", "accept": ["frog", "Frog"]}, {"prompt": "Напиши по-английски: паук", "accept": ["spider", "Spider"]}, {"prompt": "Напиши по-английски: собака", "accept": ["dog", "Dog"]}, {"prompt": "Напиши по-английски: кошка", "accept": ["cat", "Cat"]}, {"prompt": "Напиши по-английски: утка", "accept": ["duck", "Duck"]}, {"prompt": "Напиши по-английски: осёл", "accept": ["donkey", "Donkey"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm1/u3/animal_duck.webp", "right": "duck"}, {"left_image": "@@MEDIA@@sm1/u3/animal_spider.webp", "right": "spider"}, {"left_image": "@@MEDIA@@sm1/u3/animal_lizard.webp", "right": "lizard"}, {"left_image": "@@MEDIA@@sm1/u3/animal_dog.webp", "right": "dog"}, {"left_image": "@@MEDIA@@sm1/u3/animal_elephant.webp", "right": "elephant"}, {"left_image": "@@MEDIA@@sm1/u3/animal_cat.webp", "right": "cat"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'speaking', replace($blk${"title": "Прочитай предложения вслух 🎤", "html": "<p>Внимательно <b>прочитай предложения глазками</b> 👀</p><p><b>Нажми на микрофон 🎤 и проговори их вслух.</b> У тебя получится! 🌟</p><ol><li>The bread is on the tray.</li><li>I can bake a cake today.</li><li>Write your name here.</li><li>I can hear a coin drop.</li><li>My sister has long hair.</li></ol>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "The ___ is ___ the plane.", "type": "single", "image": "@@MEDIA@@sm1/u3/test_elephant_plane.webp", "options": [{"text": "lizard … in"}, {"text": "elephant … on"}, {"text": "spider … under"}, {"text": "elephant … under"}], "correct": [1]}, {"q": "The frog is ___ the desk.", "type": "single", "image": "@@MEDIA@@sm1/u3/test_frog_table.webp", "options": [{"text": "on"}, {"text": "in"}, {"text": "under"}], "correct": [2]}, {"q": "The rat is ___ the bag.", "type": "single", "image": "@@MEDIA@@sm1/u3/test_rat_bag.webp", "options": [{"text": "in"}, {"text": "on"}, {"text": "under"}], "correct": [0]}, {"q": "A: Do you like ___?<br>B: No, I ___.", "type": "single", "image": "@@MEDIA@@sm1/u3/test_spider.webp", "options": [{"text": "elephants … do"}, {"text": "lizards … do like"}, {"text": "spiders … do"}, {"text": "spiders … don't"}], "correct": [3]}, {"q": "A: I love dogs. Do you ___ dogs?<br>B: Yes, I ___. I ___ dogs, too.", "type": "single", "image": "@@MEDIA@@sm1/u3/test_dogs.webp", "options": [{"text": "likes … do … don't like"}, {"text": "like … do … like"}, {"text": "do like … like … liking"}, {"text": "like … don't … like"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u3/test_elephants_ruler.webp", "words": ["The elephants", "are", "on", "the ruler."], "sentence": "The elephants are on the ruler."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u3/test_lizards.webp", "words": ["I", "don't", "like", "lizards."], "sentence": "I don't like lizards."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u3/test_ducks_books.webp", "words": ["The ducks", "are", "on", "the books."], "sentence": "The ducks are on the books."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u3/test_dog_desk.webp", "words": ["The dog", "is", "under", "the desk."], "sentence": "The dog is under the desk."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u3/test_cat.webp", "words": ["I", "like", "cats,", "too."], "sentence": "I like cats, too."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'gaps', replace($blk${"title": "READING. Посмотри на картинку. Где находятся животные? Перетащи слово в каждое предложение.", "mode": "drag", "image": "@@MEDIA@@sm1/u3/test_animals_where.webp", "text": "1. The __frog__ is on the box.\n2. The spider is __under__ the chair.\n3. The lizard is __in__ the bag.\n4. The dog is __on__ the sofa.\n5. The __rat__ is under the table."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Посмотри на картинку и расскажи, кто где находится.</p><p><i>For example: The dog is on the table. The elephant is under the table.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>", "image": "@@MEDIA@@sm1/u3/test_attic_animals.webp", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
