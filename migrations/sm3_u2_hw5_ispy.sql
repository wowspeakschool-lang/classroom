-- SM3 · Unit 2 Homework 5: вместо выброшенного задания своё, 15.10.2026
--
-- В выгрузке было «послушай аудио и соедини картинку с её номером» — пустое
-- с обеих сторон: ни записи, где диктор называет номера, ни картинок. Анна:
-- «замени задание на другое, с нашими картинками». Поставлен квиз по игре
-- самого урока: услышал букву → нашёл картинку, карточки еды наши.
--
-- Блок вставлен ПЕРЕД устной игрой (стал пятым), поэтому игра и прощание
-- уехали на 6 и 7. Блоки 2 и 4 при этом не тронуты — на них висят
-- sm3_u2_hw5_b2.mp3 и sm3_u2_hw5_b4.mp3, имена в бакете остались верными.
--
-- Сдвиг идёт через временное +100: на (lesson_id, sort_order) уникальный ключ.

update classroom_blocks set sort_order = sort_order + 100
where lesson_id = '1bc8cead-4629-4d42-aa20-e7e6015504a2' and sort_order >= 4;

insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('1bc8cead-4629-4d42-aa20-e7e6015504a2', 'quiz', replace($blk${"title": "Потренируемся перед игрой: слушай букву и выбирай картинку", "questions": [{"q": "I spy with my little eye something beginning with «c».", "type": "single", "audio": "", "audio_tts": "I spy with my little eye something beginning with «c».", "options": [{"image": "@@MEDIA@@sm3/u2/food_peas.webp"}, {"image": "@@MEDIA@@sm3/u2/food_cheese.webp"}, {"image": "@@MEDIA@@sm3/u2/food_water.webp"}, {"image": "@@MEDIA@@sm3/u2/food_onions.webp"}], "correct": [1]}, {"q": "I spy with my little eye something beginning with «s».", "type": "single", "audio": "", "audio_tts": "I spy with my little eye something beginning with «s».", "options": [{"image": "@@MEDIA@@sm3/u2/food_soup.webp"}, {"image": "@@MEDIA@@sm3/u2/food_bread_rolls.webp"}, {"image": "@@MEDIA@@sm3/u2/food_lemonade.webp"}, {"image": "@@MEDIA@@sm3/u2/food_pineapple.webp"}], "correct": [0]}, {"q": "I spy with my little eye something beginning with «p».", "type": "single", "audio": "", "audio_tts": "I spy with my little eye something beginning with «p».", "options": [{"image": "@@MEDIA@@sm3/u2/food_onions.webp"}, {"image": "@@MEDIA@@sm3/u2/food_water.webp"}, {"image": "@@MEDIA@@sm3/u2/food_cheese.webp"}, {"image": "@@MEDIA@@sm3/u2/food_peas.webp"}], "correct": [3]}, {"q": "I spy with my little eye something beginning with «l».", "type": "single", "audio": "", "audio_tts": "I spy with my little eye something beginning with «l».", "options": [{"image": "@@MEDIA@@sm3/u2/food_salad.webp"}, {"image": "@@MEDIA@@sm3/u2/food_lemonade.webp"}, {"image": "@@MEDIA@@sm3/u2/food_bread_rolls.webp"}, {"image": "@@MEDIA@@sm3/u2/food_onions.webp"}], "correct": [1]}, {"q": "I spy with my little eye something beginning with «w».", "type": "single", "audio": "", "audio_tts": "I spy with my little eye something beginning with «w».", "options": [{"image": "@@MEDIA@@sm3/u2/food_vegetables.webp"}, {"image": "@@MEDIA@@sm3/u2/food_pineapple.webp"}, {"image": "@@MEDIA@@sm3/u2/food_water.webp"}, {"image": "@@MEDIA@@sm3/u2/food_cheese.webp"}], "correct": [2]}, {"q": "I spy with my little eye something beginning with «o».", "type": "single", "audio": "", "audio_tts": "I spy with my little eye something beginning with «o».", "options": [{"image": "@@MEDIA@@sm3/u2/food_onions.webp"}, {"image": "@@MEDIA@@sm3/u2/food_sausages.webp"}, {"image": "@@MEDIA@@sm3/u2/food_apple_juice.webp"}, {"image": "@@MEDIA@@sm3/u2/food_bread_rolls.webp"}], "correct": [0]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4);

update classroom_blocks set sort_order = sort_order - 99
where lesson_id = '1bc8cead-4629-4d42-aa20-e7e6015504a2' and sort_order >= 100;
