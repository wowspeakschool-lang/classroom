-- Переборка текста, свёрстанного картинкой, обычным html. SM1 + SM2.
-- Решение Анны от 03.11.2026. Копия затронутых блоков — classroom_backup_tekst_kartinkoy_20261103.

create table if not exists classroom_backup_tekst_kartinkoy_20261103 (
  id uuid, lesson_id uuid, type text, payload jsonb, sort_order int,
  saved_at timestamptz default now(), note text
);

insert into classroom_backup_tekst_kartinkoy_20261103 (id, lesson_id, type, payload, sort_order, note)
select b.id, b.lesson_id, b.type, b.payload, b.sort_order,
       c.slug||' u'||u.sort_order||' '||l.title||' b'||(b.sort_order+1)||' — текст картинкой, до переборки'
from classroom_blocks b
join classroom_lessons l on l.id = b.lesson_id
join classroom_units  u on u.id = l.unit_id
join classroom_courses c on c.id = u.course_id
where (c.slug, u.sort_order, l.title, b.sort_order) in (
  ('sm1', 9, 'Unit 9 Test', 10),
  ('sm1', 8, 'Homework 5',   9),
  ('sm1', 9, 'Homework 5',  10),
  ('sm1', 5, 'Homework 5',   4),
  ('sm2', 7, 'Homework 5',   1),
  ('sm2', 7, 'Homework 5',   5),
  ('sm2', 8, 'Homework 3',   8)
);

-- 1. SM1 · Unit 9 Test · блок 11 — открытка Эммы
update classroom_blocks b
set payload = jsonb_set(b.payload, '{html}', to_jsonb(replace($h$<p>Прочитай открытку Эммы. Потом впиши в пропуски недостающие слова — <b>только ОДНО слово</b> в каждый пропуск.</p>
<h3 style="text-align:center;color:#1f4e79;margin-bottom:6px">✉️ Emma’s Postcard</h3>
<blockquote style="margin:0;border:2px solid #1f4e79;border-radius:12px;background:#f4f8fd;padding:14px 20px">
<p><i>Dear Sophie,</i></p>
<p>I am on holiday! We are at the beach. It is hot and sunny. I love it here!</p>
<p>Every morning I swim in the sea with my brother Max. The water is blue and warm. After that, we play in the sand and look for shells. I have got ten shells now! They are in a box on my table.</p>
<p>Max loves the sea. He paints a picture of it every day. I eat ice cream every day, too — my favourite is chocolate! Mum is under the umbrella with her book.</p>
<p>Where is Dad? He is on the big rocks. He wants to catch a fish for dinner!</p>
<p>Tomorrow we want to take a photo of the sunset. And I want to read a book on the beach, too.</p>
<p>I miss you! Let’s go to the beach together next summer!</p>
<p><i>Love, Emma</i></p>
</blockquote>$h$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')))
from classroom_lessons l, classroom_units u, classroom_courses c
where b.lesson_id = l.id and l.unit_id = u.id and u.course_id = c.id
  and c.slug = 'sm1' and u.sort_order = 9 and l.title = 'Unit 9 Test' and b.sort_order = 10;

-- 2. SM1 · Unit 8 · ДЗ 5 · блок 10 — страница форума о питомцах
update classroom_blocks b
set payload = jsonb_set(b.payload, '{html}', to_jsonb(replace($h$<p>Ты такой молодец! Ты выполнил уже два задания. А сейчас тебя ждут интересные истории.</p>
<p>Ребята подготовили для тебя рассказ о своих питомцах. Как думаешь, какие у них домашние животные? Прочитай текст вслух и проверь себя.</p>
<h3 style="color:#5a9e12;margin-bottom:2px">💬 Pet forum</h3>
<p style="color:#d6336c;font-weight:bold;margin-top:0">Super pets!</p>
<p style="background:#fdf2cc;border-radius:12px;padding:12px 16px">
<img src="@@MEDIA@@sm1/u8/forum_alice.webp" alt="Alice" style="max-width:64px;width:100%;border-radius:8px;vertical-align:middle">
<b> Alice</b><br>
<b>Can your cat sing?!</b><br>
My cat is called Bob. He’s black with one white foot! He’s two years old. He can run and jump AND he can sing! What can your pet do?
</p>
<p style="background:#e8f5d8;border-radius:12px;padding:12px 16px">
<img src="@@MEDIA@@sm1/u8/forum_harry.webp" alt="Harry" style="max-width:64px;width:100%;border-radius:8px;vertical-align:middle">
<b> Harry</b><br>
Wow! No way! My cat can’t sing. I’ve got a dog too. His name is Patch. He can swim and he can play football – we play football in the garden! Look at my photo.<br>
<img src="@@MEDIA@@sm1/u8/forum_dog_photo.webp" alt="Patch" style="max-width:240px;width:100%;border-radius:10px;margin-top:8px">
</p>
<p style="background:#ece3f7;border-radius:12px;padding:12px 16px">
<img src="@@MEDIA@@sm1/u8/forum_sally.webp" alt="Sally" style="max-width:64px;width:100%;border-radius:8px;vertical-align:middle">
<b> Sally</b><br>
Cool! I haven’t got a cat or a dog, but I’ve got a horse. Her name is Jazzy. She’s a big black horse – she’s beautiful. She can’t sing. She can jump up high, stand on two legs and she can skip.
</p>$h$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')))
from classroom_lessons l, classroom_units u, classroom_courses c
where b.lesson_id = l.id and l.unit_id = u.id and u.course_id = c.id
  and c.slug = 'sm1' and u.sort_order = 8 and l.title = 'Homework 5' and b.sort_order = 9;

-- 3. SM1 · Unit 9 · ДЗ 5 · блок 11 — две афиши
update classroom_blocks b
set payload = jsonb_set(b.payload, '{html}', to_jsonb(replace($h$<h3>Читаем афиши 📖</h3>
<p>Две страны зовут в гости. Прочитай, что они обещают.</p>
<p style="border:2px solid #b22234;border-radius:12px;background:#fbf6f6;padding:14px 18px">
<img src="@@MEDIA@@sm1/u9/flag_usa.webp" alt="Флаг США" style="max-width:84px;width:100%;border-radius:6px;vertical-align:middle">
<b style="font-size:19px;color:#1f4e79"> 1. Come to the <span style="color:#b22234">USA</span></b><br>
<span style="color:#1f4e79">★ ★ ★</span><br>
Go to a National Park. Look at the beautiful old trees. Catch a fish in a lake. Sleep in a tent under the stars.
</p>
<p style="border:2px solid #007a4d;border-radius:12px;background:#f5fbf8;padding:14px 18px">
<img src="@@MEDIA@@sm1/u9/flag_sa.webp" alt="Флаг ЮАР" style="max-width:84px;width:100%;border-radius:6px;vertical-align:middle">
<b style="font-size:19px;color:#007a4d"> 2. Come to <span style="color:#1f4e79">South</span> <span style="color:#de3831">Africa</span></b><br>
<span style="color:#f0b323">━━━━━</span><br>
Go on a safari. See the animals – lions, hippos and giraffes. Go to Boulder’s Beach and see the penguins. Our beaches are great!
</p>$h$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')))
from classroom_lessons l, classroom_units u, classroom_courses c
where b.lesson_id = l.id and l.unit_id = u.id and u.course_id = c.id
  and c.slug = 'sm1' and u.sort_order = 9 and l.title = 'Homework 5' and b.sort_order = 10;

-- 4. SM1 · Unit 5 · ДЗ 5 · блок 5 — дневник Милы
update classroom_blocks b
set payload = jsonb_set(b.payload, '{html}', to_jsonb(replace($h$<p>Мы с тобой сейчас познакомимся с Милой и узнаем, как проходит её неделя.</p>
<p>Мила ведёт дневник. Посмотри, как проходит её неделя!</p>
<p style="text-align:center"><img src="@@MEDIA@@sm1/u5/hw5_mila_pics.webp" alt="" style="max-width:420px;width:100%"></p>
<blockquote style="margin:0;border:2px solid #c9b48a;border-radius:12px;background:#fffdf5;padding:14px 20px">
<h3 style="margin-top:0;text-decoration:underline">My Week</h3>
<ul>
<li>On Mondays I watch TV for two hours. I play football for one hour and I read for one hour.</li>
<li>On Tuesdays I watch TV for three hours. I don’t do sport and I read for two hours.</li>
<li>On Wednesdays I watch TV for one hour. I play tennis for one hour and I read for one hour.</li>
<li>On Thursdays I don’t watch TV. I swim for one hour and I read for two hours.</li>
<li>On Fridays I watch TV for two hours. I play football for one hour, but I don’t read.</li>
<li>On Saturdays and Sundays I do nothing!</li>
</ul>
</blockquote>$h$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')))
from classroom_lessons l, classroom_units u, classroom_courses c
where b.lesson_id = l.id and l.unit_id = u.id and u.course_id = c.id
  and c.slug = 'sm1' and u.sort_order = 5 and l.title = 'Homework 5' and b.sort_order = 4;

-- 5. SM2 · Unit 7 · ДЗ 5 · блок 2 — рассказ Мэри
update classroom_blocks b
set payload = jsonb_set(b.payload, '{html}', to_jsonb(replace($h$<p>А теперь тебя ждёт текст! Прочитай историю Мэри про её путешествие.</p>
<p style="text-align:center"><img src="@@MEDIA@@sm2/u7/mary_photo.webp" alt="Мэри" style="max-width:150px;width:100%;border-radius:50%"></p>
<h3 style="text-align:center;margin-top:0">🌈 Mary</h3>
<blockquote style="margin:0;border-left:4px solid #f5a623;background:#fffaf0;border-radius:10px;padding:12px 18px">
<p>Hi. My name’s Mary. I like travelling. My family and friends live in different countries.</p>
<p>My grandmother Jessica lives in the UK. When we visit her, we go by plane.</p>
<p>I’ve got a friend. His name’s Boris. When we visit Boris, we go by train.</p>
<p>My cousin Sara lives next to me. When I go to her house, I ride my bike. I love riding bikes and scooters.</p>
<p>My favourite place is Italy. We go there by car. I like eating ice cream and pizza in Italy!</p>
</blockquote>$h$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')))
from classroom_lessons l, classroom_units u, classroom_courses c
where b.lesson_id = l.id and l.unit_id = u.id and u.course_id = c.id
  and c.slug = 'sm2' and u.sort_order = 7 and l.title = 'Homework 5' and b.sort_order = 1;

-- 6. SM2 · Unit 7 · ДЗ 5 · блок 6 — тот же текст Мэри в задании «прочитай вслух»
update classroom_blocks b
set payload = jsonb_set(b.payload, '{html}', to_jsonb(replace($h$<p>Нажми на микрофончик и запиши, как ты читаешь этот текст 😁</p>
<blockquote style="margin:0;border-left:4px solid #f5a623;background:#fffaf0;border-radius:10px;padding:12px 18px">
<p>Hi. My name’s Mary. I like travelling. My family and friends live in different countries.</p>
<p>My grandmother Jessica lives in the UK. When we visit her, we go by plane.</p>
<p>I’ve got a friend. His name’s Boris. When we visit Boris, we go by train.</p>
<p>My cousin Sara lives next to me. When I go to her house, I ride my bike. I love riding bikes and scooters.</p>
<p>My favourite place is Italy. We go there by car. I like eating ice cream and pizza in Italy!</p>
</blockquote>$h$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')))
from classroom_lessons l, classroom_units u, classroom_courses c
where b.lesson_id = l.id and l.unit_id = u.id and u.course_id = c.id
  and c.slug = 'sm2' and u.sort_order = 7 and l.title = 'Homework 5' and b.sort_order = 5;

-- 7. SM2 · Unit 8 · ДЗ 3 · блок 9 — образец, вшитый в фотографию
update classroom_blocks b
set payload = jsonb_set(b.payload, '{html}', to_jsonb(replace($h$<p>Иии — ещё одно задание! Посмотри на фото и допиши предложения по образцу :)</p>
<p style="text-align:center"><img src="@@MEDIA@@sm2/u8/ex_tennis_photo.webp" alt="" style="max-width:300px;width:100%"></p>
<p style="background:#f4f8fd;border-radius:10px;padding:12px 16px">
<b>Образец:</b><br>
✔ I like playing tennis.<br>
✔ So do I.
</p>$h$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')))
from classroom_lessons l, classroom_units u, classroom_courses c
where b.lesson_id = l.id and l.unit_id = u.id and u.course_id = c.id
  and c.slug = 'sm2' and u.sort_order = 8 and l.title = 'Homework 3' and b.sort_order = 8;
