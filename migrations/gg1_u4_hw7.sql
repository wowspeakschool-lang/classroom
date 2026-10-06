-- Go Getter 1 · Unit 4 · Look at me · Homework 7
-- собрано tools/gg1_build.py --lesson u4_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 4 · Look at me', 4
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 4 · Look at me');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 4 · Look at me';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На следующем уроке тебя ожидает тест. Давай сегодня постараемся к нему получше подготовиться!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'gaps', replace($blk${"title": "Вначале вспомним части тела. Впиши слова", "mode": "type", "image": "@@MEDIA@@gg1/u4/clown_bonzo.webp", "text": "Look at Bonzo's face! He's got big __ears__, big brown __eyes__, a big red __mouth__ and very white __teeth__. His __nose__ is red and he's got grey __curly__ hair."}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Подбери подходящую по смыслу фразу", "mode": "drag", "text": "A: I love golf and football. B: __You're sporty__.\nA: I've got a lovely present for my best friend. B: __You're nice__.\nA: I've got good marks at school. B: __You're clever__.\nA: I help my brother with his homework. B: __You're helpful__.\nA: I speak to everyone. B: __You're friendly__.\nA: I tell good jokes. B: __You're funny__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "И-и-и… немножечко грамматики! Заполни пропуски", "mode": "drag", "text": "A: __Have__ you got wavy hair? B: __Yes__, I have.\nA: __Has__ Maria __got__ long blond hair? B: No, she __hasn't__.\nA: __Have__ you and Alex got blue eyes? B: Yes, we __have__.\nA: __Have__ Jane and I got white teeth? B: No, you __haven't__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Вспомним притяжательные прилагательные. Заполни пропуски", "mode": "drag", "image": "@@MEDIA@@gg1/u4/card_possessives.webp", "text": "We've got wavy hair. __Our__ hair is wavy.\nThe dog has got short legs. __Its__ legs are short.\nThe students have got good marks. __Their__ marks are good.\nJack and I have got brown hair. __Our__ hair is brown.\nYou and Anna have got a nice brother. __Your__ brother is nice."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ну что же! Теперь ты готов к тесту на все 100% 🎉</h3>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Задание со звёздочкой ⭐", "needs_review": true, "html": "<p>Напиши о своей подруге Веронике, посмотрев на табличку ниже.</p><table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\"><tr><td>Name</td><td>Veronica</td></tr><tr><td>Personality</td><td>helpful</td></tr><tr><td>Eyes</td><td>big, green</td></tr><tr><td>Hair</td><td>long, straight, brown</td></tr><tr><td>Bedroom ✓</td><td>a bed, a wardrobe, a desk, a chair</td></tr><tr><td>Bedroom ✗</td><td>a carpet, a television</td></tr></table><p><i>Начало: My friend's name is Veronica. She is helpful. She has got…</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Соедини ⭐", "pairs": [{"left_image": "@@MEDIA@@gg1/u4/body_arm.webp", "right": "arm", "right_audio_tts": "arm"}, {"left_image": "@@MEDIA@@gg1/u4/body_leg.webp", "right": "leg", "right_audio_tts": "leg"}, {"left_image": "@@MEDIA@@gg1/u4/body_head.webp", "right": "head", "right_audio_tts": "head"}, {"left_image": "@@MEDIA@@gg1/u4/body_neck.webp", "right": "neck", "right_audio_tts": "neck"}, {"left_image": "@@MEDIA@@gg1/u4/hair_spiky.webp", "right": "spiky hair", "right_audio_tts": "spiky hair"}, {"left_image": "@@MEDIA@@gg1/u4/hair_curly.webp", "right": "curly hair", "right_audio_tts": "curly hair"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'truefalse', replace($blk${"title": "Предложение написано правильно? Выбери верно или неверно ⭐", "statements": [{"text": "She has got long hair.", "correct": true}, {"text": "They has got a big house.", "correct": false}, {"text": "I have got two sisters.", "correct": true}, {"text": "My dog have got big ears.", "correct": false}, {"text": "We haven't got a car.", "correct": true}, {"text": "He haven't got a bike.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'match', replace($blk${"title": "Соедини вопрос и ответ ⭐", "pairs": [{"left": "Have you got a pet?", "right": "Yes, I have."}, {"left": "Has she got blue eyes?", "right": "Yes, she has."}, {"left": "Has he got curly hair?", "right": "No, he hasn't."}, {"left": "Have they got a car?", "right": "No, they haven't."}, {"left": "Has it got big ears?", "right": "Yes, it has."}, {"left": "Have we got time?", "right": "Yes, we have."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты отлично справился с заданиями, молодец! 🎉</h3><p>Удачи на тесте!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
