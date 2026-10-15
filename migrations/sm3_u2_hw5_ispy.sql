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


-- Дополнение того же дня: второе выброшенное задание, «соедини людей и блюда».
-- В выгрузке пусты обе колонки, и даже заменить его молча было нечем: ни люди,
-- ни блюда нигде не названы. Анна: «замени». Людей рисовать нельзя, но они
-- и не нужны — слева имя и то, чего человек хочет, справа наша карточка еды.
--
-- Блок встал последним перед прощанием: так не поехал ни один номер, кроме
-- самого прощания. Игра «I spy» осталась рядом со своим образцом.

update classroom_blocks set sort_order = sort_order + 100
where lesson_id = '1bc8cead-4629-4d42-aa20-e7e6015504a2' and sort_order >= 6;

insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('1bc8cead-4629-4d42-aa20-e7e6015504a2', 'match', replace($blk${"title": "Прочитай, чего хочет каждый, и подбери ему еду", "pairs": [{"left": "Kim: I’m thirsty. I’d like something cold with lemon.", "right": "lemonade", "right_audio_tts": "lemonade", "right_image": "@@MEDIA@@sm3/u2/food_lemonade.webp"}, {"left": "Daniel: It’s cold today. Shall I have something hot?", "right": "soup", "right_audio_tts": "soup", "right_image": "@@MEDIA@@sm3/u2/food_soup.webp"}, {"left": "Tom: I don’t want meat. I’d like something green.", "right": "salad", "right_audio_tts": "salad", "right_image": "@@MEDIA@@sm3/u2/food_salad.webp"}, {"left": "Mary: I’d like some fruit — something big and yellow.", "right": "pineapple", "right_audio_tts": "pineapple", "right_image": "@@MEDIA@@sm3/u2/food_pineapple.webp"}, {"left": "Ben: I’m very hungry! I’d like something with meat.", "right": "sausages", "right_audio_tts": "sausages", "right_image": "@@MEDIA@@sm3/u2/food_sausages.webp"}, {"left": "Lucy: I’d like a drink, but not juice and not lemonade.", "right": "water", "right_audio_tts": "water", "right_image": "@@MEDIA@@sm3/u2/food_water.webp"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6);

update classroom_blocks set sort_order = sort_order - 99
where lesson_id = '1bc8cead-4629-4d42-aa20-e7e6015504a2' and sort_order >= 100;
