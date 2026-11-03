-- Go Getter 2, юнит 4 — выравнивание домашек по планам уроков.
-- Решение Анны от 03.11.2026: «делаем как должно быть по планам».
-- Сверка планов 1–8 («GG2 remastered» → Unit 4) подтвердила сдвиг на урок:
--   ДЗ 3 ↔ план 4, ДЗ 4 ↔ план 5, ДЗ 5 ↔ план 6, ДЗ 6 ↔ план 7,
--   у плана урока 3 (p.49) домашки нет вовсе, ДЗ 7 — повторение перед тестом.
--
-- Целевой вид: семь домашек, ДЗ N ↔ план урока N, ДЗ 7 — план 7 + повторение.
--
-- Копия всех затронутых блоков (сделана до правки):
--   classroom_backup_gg2_u4_i_korotkie_20261103
--
-- Уроки юнита 4:
--   53da9bd3-957e-452b-aa34-e2c3e6a9e86a  Homework 1 (план 1)   — не трогаем
--   fc4092e5-0444-469a-8841-6630676c8358  Homework 2 (план 2)   — не трогаем
--   11e3a724-a913-4674-b995-9cc5b5730766  Homework 3 (план 4)   → Homework 4
--   321da4d6-a5a9-47ca-9287-6f347c511ab9  Homework 4 (план 5)   → Homework 5
--   4cf4c755-dd7e-4892-b62b-a7bbbae90542  Homework 5 (план 6)   → Homework 6
--   f88cf616-d2dd-48a9-a486-0dc0d6909fbd  Homework 6 (план 7)   → Homework 7 (принимает повторение)
--   b34421bf-19d0-4098-989f-1c4dc259a384  Homework 7 (повторение) → пустеет и становится Homework 3 (план 3, p.49)
--   75bf6d66-f275-4ce5-94d6-450d30971c5d  Unit 4 Test           — не трогаем
--
-- is_published нигде не трогаем.

begin;

-- ---------------------------------------------------------------------------
-- 1. Удаляем материал юнита 3 из нынешней ДЗ 7 (блоки 20–24 как в редакторе).
--    Блок 20 — подводка «Технологии и объявления», блоки 21–23 — три истории
--    про технику, блок 24 — задание по ним (good at / worried about /
--    excited about). Это лексика и грамматика юнита 3.
--    Заодно убираем приветствие ДЗ 7 (блок 1): в слитой домашке оно одно.
-- ---------------------------------------------------------------------------

delete from classroom_blocks
where lesson_id = 'b34421bf-19d0-4098-989f-1c4dc259a384'
  and sort_order in (0, 19, 20, 21, 22, 23);

-- Прощание нынешней ДЗ 6 убираем — в слитой домашке остаётся прощание ДЗ 7.
delete from classroom_blocks
where lesson_id = 'f88cf616-d2dd-48a9-a486-0dc0d6909fbd'
  and sort_order = 10;

-- ---------------------------------------------------------------------------
-- 2. Новая ДЗ 7 = нынешняя ДЗ 6 (материал плана урока 7) + повторение из ДЗ 7.
--    Приветствие одно (из ДЗ 6, дополнено), между частями — разделитель,
--    прощание одно (из ДЗ 7, без упоминания технологий).
-- ---------------------------------------------------------------------------

update classroom_blocks
set payload = jsonb_build_object('html',
  '<p><img src="https://classroom.wowteach.ru/media/shared/hello_highfive.webp" alt="" style="height:200px"></p>'
  '<h2>Огромный привет!</h2>'
  '<p>Как твоё настроение? Как погода? Самое время сделать новое домашнее задание. '
  'Сначала ты будешь много слушать и кое-что напишешь, а потом повторим весь юнит перед тестом. Давай начнём 😉</p>')
where lesson_id = 'f88cf616-d2dd-48a9-a486-0dc0d6909fbd' and sort_order = 0;

-- Разделитель между частью плана урока 7 и повторением юнита.
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('f88cf616-d2dd-48a9-a486-0dc0d6909fbd', 'text', jsonb_build_object('html',
  '<h3>А теперь повторим весь юнит 🧭</h3>'
  '<p>Представляешь, ты уже заканчиваешь четвёртый юнит! Дальше тебя ждёт повторение того, что ты прошёл. '
  'Ты наверняка всё отлично помнишь. Let’s go 🚀</p>'), 10);

-- Переносим блоки повторения. Хвост (блоки 25–31 как в редакторе) — первым,
-- чтобы диапазоны не пересекались; оба диапазона свободны в целевом уроке.
update classroom_blocks
set lesson_id = 'f88cf616-d2dd-48a9-a486-0dc0d6909fbd', sort_order = sort_order + 5
where lesson_id = 'b34421bf-19d0-4098-989f-1c4dc259a384' and sort_order between 24 and 31;

update classroom_blocks
set lesson_id = 'f88cf616-d2dd-48a9-a486-0dc0d6909fbd', sort_order = sort_order + 10
where lesson_id = 'b34421bf-19d0-4098-989f-1c4dc259a384' and sort_order between 1 and 18;

-- Прощание: убираем «узнал много нового о технологиях» — этого материала
-- в домашке больше нет.
update classroom_blocks
set payload = jsonb_build_object('html',
  '<p><img src="https://classroom.wowteach.ru/media/shared/well_done_trophy.webp" alt="" style="height:180px"></p>'
  '<h3>Великолепная работа!</h3>'
  '<p>Поздравляю тебя с окончанием большой-пребольшой темы! Ты научился сравнивать места и предметы, '
  'рассказывать о рекордах и описывать лучшего друга. Твой учитель очень-очень гордится тобой! Увидимся на занятии 😎</p>')
where lesson_id = 'f88cf616-d2dd-48a9-a486-0dc0d6909fbd' and sort_order = 36;

commit;

-- ---------------------------------------------------------------------------
-- 3. Новая ДЗ 3 по плану урока 3 (учебник, с. 49, раздел 4.2 продолжение):
--    прилагательные-противоположности (Vocabulary Adjectives (1)),
--    отработка сравнительной степени, сравнение двух центров отдыха.
--    Урок занимает освободившийся ряд b34421bf (прежняя ДЗ 7): её блоки
--    целиком переехали в новую ДЗ 7, новых уроков не заводим.
--    Карточки лексики не дублируем — они стоят в ДЗ 2 (блок 2).
--    Лесенка сложности: пары противоположностей → классификация форм →
--    собери предложение → впиши форму → сравни по табличке → своё мнение.
-- ---------------------------------------------------------------------------

begin;

insert into classroom_blocks (lesson_id, type, payload, sort_order) values

-- 1. Приветствие
('b34421bf-19d0-4098-989f-1c4dc259a384', 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>На уроке ты познакомился с прилагательными-противоположностями и потренировался сравнивать. Давай закрепим это дома. Поехали 🚀</p>"}$blk$::jsonb, 0),

-- 2. Противоположности (p.49 ex.6)
('b34421bf-19d0-4098-989f-1c4dc259a384', 'match', $blk${"title": "Соедини прилагательное с его противоположностью.", "pairs": [
 {"left": "boring",    "right": "exciting",  "right_audio": "", "right_audio_tts": {"text": "exciting",  "voice": "en_US-amy"}},
 {"left": "cheap",     "right": "expensive", "right_audio": "", "right_audio_tts": {"text": "expensive", "voice": "en_US-amy"}},
 {"left": "dangerous", "right": "safe",      "right_audio": "", "right_audio_tts": {"text": "safe",      "voice": "en_US-amy"}},
 {"left": "difficult", "right": "easy",      "right_audio": "", "right_audio_tts": {"text": "easy",      "voice": "en_US-amy"}},
 {"left": "high",      "right": "low",       "right_audio": "", "right_audio_tts": {"text": "low",       "voice": "en_US-amy"}}
]}$blk$::jsonb, 1),

-- 3. Как образуется сравнительная степень (табличка Grammar, p.49)
('b34421bf-19d0-4098-989f-1c4dc259a384', 'sort', $blk${"title": "Распредели прилагательные по тому, как у них образуется сравнительная степень. Можешь подсматривать в правило из урока.", "groups": [
 {"name": "Короткие: + -er", "items": [{"text": "cheap"}, {"text": "high"}, {"text": "low"}, {"text": "safe"}, {"text": "easy"}]},
 {"name": "Длинные: more + …", "items": [{"text": "boring"}, {"text": "dangerous"}, {"text": "difficult"}, {"text": "exciting"}, {"text": "expensive"}]},
 {"name": "Особая форма", "items": [{"text": "good"}, {"text": "bad"}]}
]}$blk$::jsonb, 2),

-- 4. Разделитель перед серией «собери предложение»
('b34421bf-19d0-4098-989f-1c4dc259a384', 'text', $blk${"html": "<h3>Теперь соберём предложения 📝</h3><p>В каждом задании расставь слова по порядку. Не забудь про than — «чем».</p>"}$blk$::jsonb, 3),

-- 5–9. Собери предложение (p.49 ex.8)
('b34421bf-19d0-4098-989f-1c4dc259a384', 'order', $blk${"words": ["Summer", "is", "hotter", "than", "winter."], "sentence": "Summer is hotter than winter."}$blk$::jsonb, 4),
('b34421bf-19d0-4098-989f-1c4dc259a384', 'order', $blk${"words": ["Japanese", "is", "more", "difficult", "than", "English."], "sentence": "Japanese is more difficult than English."}$blk$::jsonb, 5),
('b34421bf-19d0-4098-989f-1c4dc259a384', 'order', $blk${"words": ["Tigers", "are", "more", "dangerous", "than", "lions."], "sentence": "Tigers are more dangerous than lions."}$blk$::jsonb, 6),
('b34421bf-19d0-4098-989f-1c4dc259a384', 'order', $blk${"words": ["Mount", "Everest", "is", "higher", "than", "Kilimanjaro."], "sentence": "Mount Everest is higher than Kilimanjaro."}$blk$::jsonb, 7),
('b34421bf-19d0-4098-989f-1c4dc259a384', 'order', $blk${"words": ["A", "Ferrari", "is", "more", "expensive", "than", "a", "Fiat."], "sentence": "A Ferrari is more expensive than a Fiat."}$blk$::jsonb, 8),

-- 10. Впиши сравнительную форму (p.49 ex.7)
('b34421bf-19d0-4098-989f-1c4dc259a384', 'gaps', $blk${"mode": "type", "title": "Впиши сравнительную форму слова из скобок. Пример: Amy’s hair is longer (long) than Elena’s hair.", "text": "1. Elena wants to climb the __lower__ (low) wall.\n2. Walking is __safer__ (safe) than kayaking.\n3. Cycling is __easier__ (easy) than climbing.\n4. The higher wall is __more exciting__ (exciting) than the lower wall.\n5. Elena is __better__ (good) at climbing than Tom."}$blk$::jsonb, 9),

-- 11. Сравни два центра отдыха (p.49 ex.10) — табличка внутри задания
('b34421bf-19d0-4098-989f-1c4dc259a384', 'task', $blk${"title": "Сравни два центра отдыха", "needs_review": true, "html": "<p>Посмотри на табличку и напиши четыре предложения: сравни Adventure Island и Volcano World. Чем больше квадратиков, тем лучше.</p><p><i>Пример: Adventure Island is more expensive than Volcano World. Volcano World is cheaper than Adventure Island.</i></p><table style=\"border-collapse:collapse;margin:10px 0\"><tr><th style=\"border:1px solid #bbb;padding:6px\"></th><th style=\"border:1px solid #bbb;padding:6px\">Adventure Island</th><th style=\"border:1px solid #bbb;padding:6px\">Volcano World</th></tr><tr><td style=\"border:1px solid #bbb;padding:6px\">How expensive are the tickets?</td><td style=\"border:1px solid #bbb;padding:6px\">£20</td><td style=\"border:1px solid #bbb;padding:6px\">£10</td></tr><tr><td style=\"border:1px solid #bbb;padding:6px\">How safe is it?</td><td style=\"border:1px solid #bbb;padding:6px\">🟦🟦🟦🟦🟦</td><td style=\"border:1px solid #bbb;padding:6px\">🟦🟦🟦🟦</td></tr><tr><td style=\"border:1px solid #bbb;padding:6px\">How exciting is it?</td><td style=\"border:1px solid #bbb;padding:6px\">🟦🟦</td><td style=\"border:1px solid #bbb;padding:6px\">🟦🟦🟦🟦🟦</td></tr><tr><td style=\"border:1px solid #bbb;padding:6px\">Is the food good?</td><td style=\"border:1px solid #bbb;padding:6px\">🟦🟦🟦🟦</td><td style=\"border:1px solid #bbb;padding:6px\">🟦🟦🟦</td></tr></table><p>Используй слова: expensive, cheap, safe, exciting, good.</p>"}$blk$::jsonb, 10),

-- 12. Своё мнение (p.49 ex.9)
('b34421bf-19d0-4098-989f-1c4dc259a384', 'task', $blk${"title": "Напиши своё мнение", "needs_review": true, "html": "<p>Напиши пять предложений, которые верны для тебя. В каждой паре сравни одно с другим.</p><p><i>Пример: interesting: History / Maths — I think History is more interesting than Maths.</i></p><ol><li>easy: English / Science</li><li>exciting: football / basketball</li><li>bad: a visit to the doctor / a visit to the dentist</li><li>good: strawberry ice cream / chocolate ice cream</li><li>nice: cats / dogs</li></ol>"}$blk$::jsonb, 11),

-- 13. Прощание
('b34421bf-19d0-4098-989f-1c4dc259a384', 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа!</h3><p>Теперь ты умеешь сравнивать что угодно 😃 Увидимся на занятии!</p>"}$blk$::jsonb, 12);

commit;

-- ---------------------------------------------------------------------------
-- 4. Перенумерация уроков: ДЗ N ↔ план урока N, sort_order 0…6 без дыр,
--    тест последним. Сдвиг +1000, затем значения подряд.
-- ---------------------------------------------------------------------------

begin;

update classroom_lessons set sort_order = sort_order + 1000
where id in ('53da9bd3-957e-452b-aa34-e2c3e6a9e86a','fc4092e5-0444-469a-8841-6630676c8358',
             '11e3a724-a913-4674-b995-9cc5b5730766','321da4d6-a5a9-47ca-9287-6f347c511ab9',
             '4cf4c755-dd7e-4892-b62b-a7bbbae90542','f88cf616-d2dd-48a9-a486-0dc0d6909fbd',
             'b34421bf-19d0-4098-989f-1c4dc259a384','75bf6d66-f275-4ce5-94d6-450d30971c5d');

update classroom_lessons set title = 'Homework 1', sort_order = 0 where id = '53da9bd3-957e-452b-aa34-e2c3e6a9e86a';
update classroom_lessons set title = 'Homework 2', sort_order = 1 where id = 'fc4092e5-0444-469a-8841-6630676c8358';
update classroom_lessons set title = 'Homework 3', sort_order = 2 where id = 'b34421bf-19d0-4098-989f-1c4dc259a384';
update classroom_lessons set title = 'Homework 4', sort_order = 3 where id = '11e3a724-a913-4674-b995-9cc5b5730766';
update classroom_lessons set title = 'Homework 5', sort_order = 4 where id = '321da4d6-a5a9-47ca-9287-6f347c511ab9';
update classroom_lessons set title = 'Homework 6', sort_order = 5 where id = '4cf4c755-dd7e-4892-b62b-a7bbbae90542';
update classroom_lessons set title = 'Homework 7', sort_order = 6 where id = 'f88cf616-d2dd-48a9-a486-0dc0d6909fbd';
update classroom_lessons set title = 'Unit 4 Test', sort_order = 7 where id = '75bf6d66-f275-4ce5-94d6-450d30971c5d';

commit;
