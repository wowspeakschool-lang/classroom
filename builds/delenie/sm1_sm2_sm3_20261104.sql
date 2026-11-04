-- Деления домашек на «основную» и «дополнительную» часть нет нигде
-- (решение Анны 03.11.2026). 03.11 закрыто в GG1 и SM2 частично;
-- 04.11 добираем SM1, SM2 и SM3 — 19 блоков.
-- Плюс три точечные правки, найденные тем же проходом.

create table if not exists classroom_backup_delenie_20261104 as
select * from classroom_blocks where id in (
  '23a64c61-35dd-4d7a-a0eb-151e7aaf3419','a62e02c4-9eea-435a-b4ce-66d2accc06ad',
  'd1c18b0b-31f9-4212-a451-3f30a969a3e1','05dfedd7-d42c-45e8-8447-ecb354ba2c9d',
  'f2395838-d524-470b-9be0-569830eff322','0523ef53-d328-4ff5-a601-716d12f21cc8',
  '7ebbdd15-c880-46b2-a4fd-3cd388cd9e0a','d3125fec-f880-41cb-90c6-aec2ced86794',
  'ade6a834-666e-455e-9b1b-3edc3c928b81','38d03796-aefb-4662-9f17-719e6b06c5a7',
  '3e08eccd-f2e1-4036-9d12-747afc56e4e0','dc246a8c-6308-4a3a-9e7f-5d7ec00cec69',
  '2b0f66b2-406c-4a65-83c8-730b65f2cef7','d78fa07d-8c28-43f6-bec3-801307a12485',
  '964769bc-493e-4764-922e-b919187ddf95','d7824ea8-ae8f-492c-849c-e9c621355cd4',
  '2d8100d9-abf0-4071-b780-af4df3e5ae23','f5785e68-6fef-463e-a32d-a7a53013e2f3',
  '79b31860-daf1-42b6-af4f-b15003b39d1e',
  '28d9fc4d-1235-4bb6-8ae9-5c1ea0369eeb','a3af8111-2aa5-4da1-ac1a-8fdf69f2b563',
  '4cb7ced3-e490-42bd-96d9-7dad5aa25484');

-- 1. SM1 u9 ДЗ 1 блок 9 — «Дополнительное задание ✨»
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<h3>Закрепим новые слова ✨</h3><p>Выполни задание, чтобы хорошенько запомнить новые слова.</p>$t$::text))
where id = '23a64c61-35dd-4d7a-a0eb-151e7aaf3419';

-- 2. SM1 u9 ДЗ 5 блок 10 — «выполнил основную часть»
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<p>Ты большой молодец! Осталось последнее задание 💪</p>$t$::text))
where id = 'a62e02c4-9eea-435a-b4ce-66d2accc06ad';

-- 3. SM2 u3 ДЗ 3 блок 11 — «последнее задание для супер чемпионов»
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<p>Отлично. Ты просто чудесно потрудился. Осталось последнее задание. Твой учитель уверен, ты с ним справишься 💪</p>$t$::text))
where id = 'd1c18b0b-31f9-4212-a451-3f30a969a3e1';

-- 4. SM3 u6 ДЗ 6 блок 4 — «ещё одно задание — для ЧЕМПИОНОВ»
--    Вторая фраза дублировала заголовок блока 5, убрана.
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<p><img src="https://classroom.wowteach.ru/media/shared/good_luck_clover.webp" alt="" style="height:180px"></p><h3>Осталось последнее задание!</h3>$t$::text))
where id = '05dfedd7-d42c-45e8-8447-ecb354ba2c9d';

-- 5. SM3 u7 ДЗ 7 блок 6 — «основная часть / вторая часть» → разделитель по теме
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<p><img src="https://classroom.wowteach.ru/media/shared/good_luck_clover.webp" alt="" style="height:180px"></p><h3>Теперь — приём у врача 🩺</h3>$t$::text))
where id = 'f2395838-d524-470b-9be0-569830eff322';

-- 6. SM3 u8 ДЗ 5 блок 1 — обещание «в конце ещё несколько заданий»
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<p><img src="https://classroom.wowteach.ru/media/shared/hello_book.webp" alt="" style="height:200px"></p><h2>Привет! Как здорово, что ты решил сделать домашнее задание!</h2><p>Сегодня тебя ждёт текст и интересные задания.</p><p>Начни с того, что прочитай историю ещё раз. Кстати, ты помнишь, что Бен и Люси ели на обед?</p>$t$::text))
where id = '0523ef53-d328-4ff5-a601-716d12f21cc8';

-- 7. SM3 u8 ДЗ 6 блок 1 — «ещё ещё одно задание — для чемпионов»
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<p><img src="https://classroom.wowteach.ru/media/shared/hello_laptop.webp" alt="" style="height:200px"></p><h2>Привет!</h2><p>В этом задании тебя ждут текст и аудирование.</p><p>Прочитай текст и ответь на вопрос: <b>Why did Max get sick?</b></p>$t$::text))
where id = '7ebbdd15-c880-46b2-a4fd-3cd388cd9e0a';

-- 8. SM3 u9 ДЗ 5 блок 1 — «в конце ещё одно задание — для чемпионов»
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<p><img src="https://classroom.wowteach.ru/media/shared/hello_book.webp" alt="" style="height:200px"></p><h2>Hello! Welcome to your homework!</h2><p>Прочитай текст, который мы разбирали на уроке, и выполни два упражнения к нему.</p>$t$::text))
where id = 'd3125fec-f880-41cb-90c6-aec2ced86794';

-- 9–10. SM1 u3 ДЗ 2 и u4 ДЗ 2, блок 1 — «получишь звание чемпиона английского»
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<h2>Привет! Как здорово, что ты решил сделать домашнее задание.</h2><p>Сегодня тебя ждет видео и интересные задания. Я знаю, ты очень классный ученик, поэтому у тебя все получится :)</p><p><img src="https://classroom.wowteach.ru/media/sm1/legacy/872ffc8cf5ac.webp"></p>$t$::text))
where id = 'ade6a834-666e-455e-9b1b-3edc3c928b81';

update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<h2>Привет! Как здорово, что ты решил сделать домашнее задание.</h2><p>Сегодня тебя ждет видео и интересные упражнения. Я знаю, ты очень классный ученик, поэтому у тебя все получится :)</p><p><img src="https://classroom.wowteach.ru/media/sm1/legacy/872ffc8cf5ac.webp"></p>$t$::text))
where id = '38d03796-aefb-4662-9f17-719e6b06c5a7';

-- 11. SM1 u1 ДЗ 2 блок 16 (speaking) — «задание для настоящих чемпионов»
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<p>Посмотри на картинку. Узнаёшь? Это та самая из прошлого задания!<br>Сегодня мы произносим <b>новое волшебное заклинание!</b> 🔮</p><p><b>Задай 5 вопросов</b> <i>«Is it a…?»</i> к предметам на картинке.<br>Чтобы вспомнить заклинание — послушай запись выше! А после <b>запиши свой ответ</b> внизу 👇</p>$t$::text))
where id = '3e08eccd-f2e1-4036-9d12-747afc56e4e0';

-- 12–18. Заголовки заданий: «для ЧЕМПИОНОВ» вместо инструкции
update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb($t$Посмотри на картинку и напиши слово$t$::text))
where id = 'dc246a8c-6308-4a3a-9e7f-5d7ec00cec69';

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb($t$Дневник каникул ✍️$t$::text))
where id = '2b0f66b2-406c-4a65-83c8-730b65f2cef7';

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb($t$Прошлые выходные ✍️$t$::text))
where id = 'd78fa07d-8c28-43f6-bec3-801307a12485';

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb($t$Рассказ о болезни или травме ✍️$t$::text))
where id = '964769bc-493e-4764-922e-b919187ddf95';

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb($t$Чудо света ✍️$t$::text))
where id = 'd7824ea8-ae8f-492c-849c-e9c621355cd4';

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb($t$Тайное послание 🔐$t$::text))
where id = '2d8100d9-abf0-4071-b780-af4df3e5ae23';

update classroom_blocks set payload = jsonb_set(jsonb_set(payload, '{title}',
    to_jsonb($t$Отпуск в прошлом ✈️$t$::text)), '{html}',
  to_jsonb($t$<p><img src="https://classroom.wowteach.ru/media/sm3/u9/example_holiday_diary.webp" alt="" style="max-width:100%"></p><p>Представь, что ты отправился в отпуск в прошлое. Опиши своё путешествие! Эти вопросы помогут тебе:</p><p>1. Where were you?<br>2. How did you travel there?<br>3. What did you do there?</p><p>Посмотри на картинку и текст выше — воспользуйся ими как примером. Удачи!</p>$t$::text))
where id = 'f5785e68-6fef-463e-a32d-a7a53013e2f3';

-- 19. SM3 u6 ДЗ 7 блок 5 — «настоящие чемпионы обязательно справятся»
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<p>Рисовать можно самыми разными материалами.</p><p>Потом напиши небольшое описание по плану:</p><p><i>1. I draw my pictures on …<br>2. I use …<br>3. In this picture you can see …</i></p>$t$::text))
where id = '79b31860-daf1-42b6-af4f-b15003b39d1e';

-- 20. GG1 u6 ДЗ 3 блок 7 — «Подсказка — на карточке выше 👆»:
--     карточка пятью экранами раньше, ученик её на этом экране не видит.
update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb($t$Расставь слова в правильном порядке$t$::text))
where id = '28d9fc4d-1235-4bb6-8ae9-5c1ea0369eeb';

-- 21. GG2 u8 ДЗ 7 блок 7 — «Прочитай приглашение ещё раз»:
--     само приглашение лежит внутри предыдущего gaps, на экране квиза его нет.
update classroom_blocks set payload = jsonb_set(payload, '{material}',
  to_jsonb($t$<p><b>PARTY INVITATION</b></p><p>On: Tuesday, 3rd August, at 4:30 p.m.<br>At: Fun Times Sport Centre<br>We're going to go swimming and then eat pancakes.<br>Please bring towels for the swimming.<br>Your parents can collect you from Patty's Pancakes at 9 o'clock.<br>Please reply to 678954321.</p>$t$::text))
where id = 'a3af8111-2aa5-4da1-ac1a-8fdf69f2b563';

-- 22. GG1 Unit 0 Test блок 12 (speaking) — вопросы не сходились с картинкой:
--     сумок на ней четыре разного цвета, стульев пять, книг на партах нет вовсе.
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb($t$<p>Внимательно посмотри на картинку. Нажми на микрофон и ответь на вопросы.</p><ol><li>What's your name?</li><li>How do you spell your name?</li><li>What colour is the teacher's chair?</li><li>How many backpacks are there?</li><li>What colour is the board?</li><li>What's on the teacher's desk?</li></ol>$t$::text))
where id = '4cb7ced3-e490-42bd-96d9-7dad5aa25484';
