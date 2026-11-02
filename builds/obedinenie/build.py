# Объединение «текст с записью → задание» (решение Анны 02.11.2026, пункт 21).
# Источник данных — выборка из базы 02.11.2026; запуск: python3 build.py → plan.json, spisok.md, apply.sql
import json
C = {'gg1': 'Go Getter 1', 'gg2': 'Go Getter 2', 'gg3': 'Go Getter 3', 'sm1': 'Super Minds 1', 'sm2': 'Super Minds 2', 'sm3': 'Super Minds 3'}
# (курс, юнит, урок, № текста, id текста, lesson_id, снимков, было (текст), запись,
#  [(id задания, было заголовок, станет заголовок)], оставить — причина или None)
R = [
 ('gg1',1,'Homework 5',2,'ffbefe89-47e1-4c8d-b008-2a562d1ad4ce','dc6dc1eb-c9d5-4b1a-9a69-a66f506ecefa',0,'Прочитай, что ребята рассказывают о себе 😃 Simon: Hi. My name\'s Simon…','https://classroom.wowteach.ru/media/gg1/audio/gg1_u1_hw5_b2.mp3',[],'в тексте — сами рассказы ребят, их надо читать'),
 ('gg1',1,'Homework 6',2,'855e65ca-08a6-4e4d-9d5f-32bac22c361c','141442fa-dc99-4ed0-bc09-0c5c9754aff4',0,'Послушай аудио: Роб рассказывает о своём друге Викторе и кузине Мел.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u1_hw6_b2.mp3',
   [('1fcba56f-cd71-4387-b61c-422e49102861','Послушай аудио и скажи: верно или неверно','Послушай, как Роб рассказывает о Викторе и кузине Мел, и скажи: верно или неверно'),
    ('ac010de8-0740-4f69-90aa-8e500d8c0811','Послушай аудио и впиши информацию в пропуски','Послушай ещё раз и впиши информацию в пропуски')],None),
 ('gg1',1,'Unit 1 Test',15,'66d05574-8d9e-42d8-9b1f-a7107d744534','685ab91c-e949-4592-b754-f0132d775375',0,'LISTENING. Прослушай Эмму и реши: правда или неправда? + картинка','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u1_test_b14.mp3',[],'в тексте картинка (Эмма в парке) — у задания «верно/неверно» своей картинки нет, она бы пропала'),
 ('gg1',2,'Homework 6',3,'25fcefec-3045-4153-9f40-f059cadedc33','fad3f15e-756a-4e1d-840a-2dea8def50a5',0,'Послушай, о чём говорят Люк и Роза. Потом выполни задания ниже.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u2_hw6_b3.mp3',
   [('f2445db4-5c7f-423b-882d-bdac543b34de','Какие предметы упоминают Люк и Роза? Отметь все','Послушай разговор Люка и Розы. Какие предметы они упоминают? Отметь все'),
    ('6c54d003-79ff-4929-8486-21186207d858','Послушай аудио ещё раз и допиши предложения','Послушай ещё раз и допиши предложения')],None),
 ('gg1',2,'Unit 2 Test',15,'2c8e8cfe-5395-46bb-a9f6-aeafee6f889f','ec79ff6a-669a-472f-9ee9-acfb46e9cfbc',0,'LISTENING. Прослушай Эмму: она показывает свои школьные вещи.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u2_test_b14.mp3',
   [('a18ab296-bf66-46c2-b232-6be7131fb671','LISTENING. Перетащи правильное прилагательное в каждый пропуск','LISTENING. Послушай, как Эмма показывает школьные вещи, и перетащи прилагательные в пропуски')],None),
 ('gg1',3,'Homework 6',2,'f25415c0-09d2-4663-a73e-4862e2eb4af7','f3fe8b5e-e96f-40c5-a745-9e28669044a3',0,'Послушай, что Дэнни рассказывает о своём новом доме.','https://classroom.wowteach.ru/media/gg1/audio/gg1_u3_hw6_b2.mp3',
   [('f82eebd2-31f0-447a-aed9-1fd014ea41f4','О чём рассказ? Выбери правильный ответ','Послушай Дэнни о его новом доме. О чём рассказ? Выбери правильный ответ'),
    ('37205e28-01f3-4a09-be95-c843e6a3516c','Послушай ещё раз. Эти предложения неверные — впиши правильное слово','Послушай ещё раз. Эти предложения неверные — впиши правильное слово')],None),
 ('gg1',3,'Unit 3 Test',12,'20171b81-70cc-49d5-b387-dc0528408b57','4f91cdd3-7c75-4cfa-a24d-3cb86cdfc972',0,'LISTENING. Прослушай 5 коротких описаний.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u3_test_b11.mp3',
   [('c7c36406-9ae5-49de-ac9e-114fd8205038','LISTENING. Соедини каждый номер с названием комнаты в доме','LISTENING. Послушай 5 коротких описаний и соедини каждый номер с названием комнаты')],None),
 ('gg1',4,'Homework 6',2,'3d8cf87b-2ad8-42cd-bf33-6515e1e4a552','7923975f-d05a-4a7b-aedb-148760ed4f42',0,'Наше первое задание — послушать и запомнить как можно больше о Дарле (Darla).','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u4_hw6_b2.mp3',
   [('74be9d52-3f74-4276-acbb-5144a317ea16','А теперь заполни пропуски нужным словом. Ты можешь прослушать аудио ещё раз','Послушай о Дарле (Darla) и заполни пропуски нужным словом')],None),
 ('gg1',4,'Unit 4 Test',12,'dc08e821-38b3-4089-8fb2-a9a94d68e589','2534353e-9ed2-48a5-995d-0a8daf0e1dcd',0,'LISTENING. Послушай рассказ девочки о её младшей сестре Мие (Mia).','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u4_test_b11.mp3',
   [('82780405-895a-48b8-aabb-5517ba6167e1','LISTENING. Выбери правильный ответ','LISTENING. Послушай рассказ о младшей сестре Мие (Mia) и выбери правильный ответ')],None),
 ('gg1',5,'Homework 6',3,'381befb6-511e-4262-b9cd-b7d72c4f3110','7177dcd7-df37-4427-9278-13a78bcbf199',0,'Послушай рассказ о кружке и выполни задания ниже.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u5_hw6_b3.mp3',
   [('e9d3832c-a637-480e-9dc4-e7a32fe4aa0b','Послушай и выбери правильный вариант ответа','Послушай рассказ о кружке и выбери правильный вариант ответа'),
    ('b1af5d62-deb8-4a2e-a9d9-ce012279cebf','Послушай и выбери правильного мишку','Послушай ещё раз и выбери правильного мишку')],None),
 ('gg1',5,'Unit 5 Test',11,'546d25aa-413f-4bd6-b979-b4593f290438','08c69ee4-7d0d-43f5-8b15-8ccd810de3df',0,'LISTENING. Прослушай рассказ Джека о себе и своей сестре Лили.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u5_test_b10.mp3',
   [('545f318d-6767-49d1-b7a7-9453933aa1b3','LISTENING. Перетащи каждое умение в нужный столбик','LISTENING. Послушай Джека о нём и сестре Лили и перетащи каждое умение в нужный столбик')],None),
 ('gg1',6,'Homework 6',2,'d1abe05a-7617-4a22-a055-d2123f838594','2813cf81-2328-4c68-b1e3-f592006f48db',0,'Послушай рассказ Энди о его каникулах. Потом выполни два задания ниже.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u6_hw6_b2.mp3',
   [('ce86889e-59cf-4202-9de8-1a56ef9173dd','Заполни таблицу. В каждом пропуске — только ОДНО слово','Послушай рассказ Энди о каникулах и заполни таблицу — в каждом пропуске одно слово'),
    ('34faad7b-2bc8-45fb-8be1-66969980b286','Послушай рассказ Энди ещё раз и выбери правильный ответ. Сначала внимательно прочитай предложения','Послушай ещё раз и выбери правильный ответ. Сначала прочитай предложения')],None),
 ('gg1',6,'Unit 6 Test',15,'69ec8130-6b03-41da-8a96-559f05a362a5','5dbafdc6-c32f-4a91-aaad-abb343c22a36',0,'LISTENING. Прослушай рассказ Алекса о его обычной субботе.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u6_test_b14.mp3',
   [('40a5b09e-6dc8-4607-8c4d-8ea99bcd9946','LISTENING. Правда или неправда?','LISTENING. Послушай рассказ Алекса о его обычной субботе: правда или неправда?')],None),
 ('gg1',7,'Homework 6',2,'8b16f67a-ead0-428c-8ba5-d1487a737db5','b62c3514-b467-4836-832f-19e688ff8a17',0,'Послушай аудио: Эмма рассказывает о своих домашних питомцах.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u7_hw6_b2.mp3',
   [('6f52e1de-aa83-4a8f-85d1-ba02615ef36d','Какое домашнее животное есть у Эммы?','Послушай Эмму о её питомцах. Какое домашнее животное есть у Эммы?'),
    ('613e7e90-7361-4a8a-a935-672d520a7a7c','Послушай ещё раз и ответь на вопросы','Послушай ещё раз и ответь на вопросы')],None),
 ('gg1',7,'Unit 7 Test',15,'22b2846f-130a-4eba-a808-ff2955e78e30','e81b9c6a-f72a-4bb8-a646-7fca8da36c7d',0,'LISTENING. Прослушай объявление в Лондонском зоопарке.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u7_test_b14.mp3',
   [('2878d389-f607-4d01-89e0-1e1fd3180425','LISTENING. Перетащи пропущенные числа и слова','LISTENING. Послушай объявление в Лондонском зоопарке и перетащи пропущенные числа и слова')],None),
 ('gg1',8,'Homework 6',3,'b80a44e6-cc82-49c7-b588-b482481f0735','14dbe647-f4f3-4c54-b015-eb15318e687f',0,'Пришло время серьёзной работы! Послушай, как Том отвечает на вопросы о своём образе жизни.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u8_hw6_b3.mp3',
   [('40c971a2-3a36-478b-addc-c70ee5788690','Соедини номера вопросов из аудио с темами','Послушай, как Том отвечает на вопросы о своём образе жизни, и соедини номера вопросов с темами')],None),
 ('gg1',9,'Final Test',2,'8cfed43b-ea3b-4e22-b830-fcd9cb304ba1','e7ace143-b17e-4797-b28f-6d8a30b944e9',0,'LISTENING Part 1. Послушай аудио и выполни задание ниже.','https://classroom.wowteach.ru/media/gg1/audio/gg1_ft_test_b2.mp3',
   [('6abff15a-2550-4fbe-89db-6f37ca0c62e6','Послушай аудио выше и расставь предметы по местам','LISTENING Part 1. Послушай и расставь предметы по местам')],None),
 ('gg1',9,'Final Test',4,'f0a8359d-3502-4566-8d98-fc5cddbe5d0a','e7ace143-b17e-4797-b28f-6d8a30b944e9',0,'LISTENING Part 2. Послушай и выбери верный ответ. Пример: What is the girl\'s name? — Lucy…','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_ft_test_b4.mp3',
   [('d201f4b9-bc72-4f33-95ac-63597cb30f89','Послушай и выбери верный ответ','LISTENING Part 2. Послушай и выбери верный ответ. Пример: What is the girl\'s name? — Lucy')],None),
 ('gg1',9,'Final Test',6,'4c2f8c81-e717-4dc1-8f22-dfb83e172aaf','e7ace143-b17e-4797-b28f-6d8a30b944e9',0,'LISTENING Part 3. Послушай рассказ о семье Браун и выполни задание ниже.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_final_b7.mp3',
   [('257dfade-97ee-4016-81c2-c1912eea8fb4','Послушай аудио выше и выбери правильный ответ','LISTENING Part 3. Послушай рассказ о семье Браун и выбери правильный ответ')],None),
 ('gg2',2,'Homework 6',2,'880c8001-d94e-46b5-8d52-8f815d6e6d8a','52eaf7a4-b1a7-4a23-9f36-0b9e599a940f',0,'А начнём мы с аудио 🎧 Это Пенни. Прослушай её диалог с папой… + картинка','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg2%20%2B%20gg3/gg2_u2_hw6_b2.mp3',[],'в тексте картинка (завтрак Пенни) — у викторины своей картинки нет, она бы пропала'),
 ('gg2',2,'Unit 2 Test',12,'339652ca-4a33-4e54-8d7a-28b2a76d5477','805cc97e-2cd7-4d10-b770-6f84d894a12a',0,'LISTENING 🎧 Послушай рассказ Мии о покупках в супермаркете. Затем отметь True / False.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg2%20%2B%20gg3/gg2_u2_test_b12.mp3',
   [('233cf04b-c1c0-4f29-a14c-32bcaf87cb39','True or False?','LISTENING. Послушай рассказ Мии о покупках в супермаркете: True (верно) или False (неверно)?')],None),
 ('gg2',3,'Homework 4',6,'b711d755-3622-4788-ac6b-0c64b80cd17d','9c298871-50b1-4392-b74a-e436e93e54a9',0,'Elena/Misha: Hello? Amy\'s Dad: Hi, it\'s Amy\'s dad…','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg2%20%2B%20gg3/gg2_u3_hw4_b6.mp3',[],'в тексте — сам диалог для чтения; задания ниже про другой диалог (Нил, миссис Грин)'),
 ('gg2',3,'Homework 6',2,'bdb6b14d-7a90-4cf1-8b06-bee8427705cb','83a0074c-62b9-4ba7-9716-fede0dc09d26',0,'Сначала мы с тобой познакомимся с Гарри и Лили. Послушай их разговор…','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg2%20%2B%20gg3/gg2_u3_hw6_b2.mp3',
   [('22b8af04-6e18-4e82-bc1b-31e9e2458aa4','(без заголовка)','Послушай разговор Гарри и Лили и выбери любимый гаджет каждого'),
    ('fa701666-ecd3-492c-bf86-4f396de538b8','(без заголовка)','Послушай разговор Гарри и Лили и выбери любимый гаджет каждого')],None),
 ('gg2',3,'Unit 3 Test',12,'8242b168-6187-4903-aea7-5ce93f9a40b3','93339dc2-9ebd-404b-9326-5a9a97e9a311',0,'LISTENING Послушай разговор по телефону между Эммой и её мамой…','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg2%20%2B%20gg3/gg2_u3_test_b11.mp3',
   [('705e2982-5e27-4aa2-8111-6248ba0a2f0a','(без заголовка)','LISTENING. Послушай разговор Эммы с мамой: True (верно), False (неверно) или Not stated (не сказано)?')],None),
 ('gg2',4,'Homework 6',2,'2eb84e4b-8453-4a4b-aabc-f869d8087153','f88cf616-d2dd-48a9-a486-0dc0d6909fbd',0,'Для начала послушай аудио. Во время прослушивания представляй друзей…','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg2%20%2B%20gg3/gg2_u4_hw6_b2.mp3',
   [('ebcbec43-e564-4efe-88a4-2f554fdef4eb','Послушай аудио ещё раз и соедини друзей.','Послушай, как ребята описывают друзей, и соедини друзей'),
    ('be3a2e9c-8cfd-431b-8d0c-c803a47dd192','Прочитай предложения и вставь пропущенные слова. Если трудно — послушай аудио ещё раз.','Прочитай предложения и вставь пропущенные слова. Если трудно — послушай ещё раз')],None),
]
GG3 = [(0,'Unit 0 Test',19,'9793286d-f711-4ea8-8cd9-5766c1ae198e','c78d7483-02fc-4da9-aab7-6777206ece34',0,'Эмму','gg2%20%2B%20gg3/gg3_u0_test_b17.mp3','c7d300fd-52c3-476f-93e1-a39ef13106e0'),
       (1,'Unit 1 Test',13,'781e55e9-bd4e-4f25-8451-20f9069a1137','87f1ce1e-8300-43d2-82b0-594ff8099a0f',0,'Оливера','gg1/gg3_u1_test_b17.mp3','ee7dd40c-493d-4dc4-a945-dd1ac5233cc1'),
       (2,'Unit 2 Test',13,'e7eff1e6-03d3-4899-bd6d-a50a99b12e3f','ad6fefbc-b1f5-4acd-a6f7-d79cd15e6c88',2,'Зои','gg1/gg3_u2_test_b13.mp3','b871b8b4-aca0-4301-98b8-4b92716615aa'),
       (3,'Unit 3 Test',12,'726716b1-d522-4291-bb03-0c5e6903d92a','58db3616-b9e6-4113-8f1a-d87ab4f7bff4',0,'Дэниела','gg1/gg3_u3_test_b12.mp3','e9202c13-352c-4969-9607-ccc9beef56ec'),
       (4,'Unit 4 Test',13,'7ba4ab38-567b-4f2b-bedf-36ac3b300fcc','2763c9bf-4b1a-4bff-830c-6f5da5c98e2d',0,'Нину','gg1/gg3_u4_test_b13.mp3','92344348-a37f-4565-9cfe-a54bbcc04499'),
       (5,'Unit 5 Test',13,'a34c4b25-a91d-4727-b38b-549ae8ab8f9c','a941b58c-a7df-4877-aa62-41bbe488ea2c',0,'Макса','gg1/gg3_u5_test_b13.mp3','0f9f1b52-fd16-4b4d-aebc-fd4fafa2a9ac'),
       (6,'Unit 6 Test',13,'366c2bcd-a23f-4ea7-9bd7-85ded0819e06','e6eeecd4-070f-4818-9cfb-cdc837c7361c',0,'Феликса','gg1/gg3_u6_test_b13.mp3','a43b2278-2f5b-404a-8ad7-242e5a8a97a5'),
       (7,'Unit 7 Test',14,'dbeeb8ce-b490-4500-ba9e-3892dbaae881','d72b1e55-b713-4966-9f8d-4fc505021d7a',0,'Руби','gg1/gg3_u7_test_b14.mp3','e2b1c593-57b9-425f-8023-f4a958960943'),
       (8,'Unit 8 Test',13,'ad49b7d0-de42-4ae4-9c89-15ec5c480f17','e77318f0-9a9f-4c41-a86a-b7df375ec266',0,'Элли','gg1/gg3_u8_test_b13.mp3','4f6f73a9-9ea9-4197-9dac-51e3dff213dd')]
ST = 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/'
for un, lt, n, tid, lid, sn, who, f, q in GG3:
    R.append(('gg3', un, lt, n, tid, lid, sn, f'LISTENING 🎧 Послушай рассказ про {who}. Текста не будет — слушай и отвечай на вопросы ниже. Можно послушать два раза.', ST + f,
              [(q, 'Послушай ещё раз и выбери правильный ответ.', f'LISTENING 🎧 Послушай рассказ про {who} и выбери правильный ответ. Можно послушать два раза')], None))
R += [
 ('sm1',1,'Homework 1',17,'5856394b-dd1d-45ab-80d2-ef485c9b4296','ea3aaa0b-76af-494b-968a-19632ec6c483',0,'Тебя также ждёт особенная волшебная миссия ✨ … шепчи волшебные слова как в аудио-примере: It\'s a blue pencil','https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/1791396586630_tts_1791396586630.mp3',
   [('8ea3f29b-2440-492f-99b8-c57abbb9e8f9','Посмотри на картинку и выбери правильный вариант','Выбери цвет, которого не хватает, и шёпотом скажи всё предложение, как в аудио-примере')],None),
 ('sm1',1,'Homework 5',2,'7cdd8acf-36ee-4c3b-8de4-9bf94cca2a6b','ed2fb4e6-848e-4f02-8af0-bda2295c9f05',0,'Супер! Теперь давай перейдем к следующему упражнению — на этот раз мы будем слушать!…','https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/1791457837047_tts_1791457837047.mp3',
   [('f3983f5e-f14d-4315-b05c-4c86e61d848e','Соедини цифры с предметами: нажми на номер на картинке, потом на слово.','Послушай и узнай, какой номер у какого предмета: нажми кружок на картинке, потом слово')],None),
 ('sm1',3,'Homework 5',3,'a48f98be-de7c-4ede-ab8e-2a4c6d2ca770','e1751bdd-951a-4b47-bbe7-a2855838c42d',0,'Отлично, ты здорово справляешься! … послушай аудиозапись и расставь зверюшек…','https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/1791399253624_tts_1791399253624.mp3',
   [('e811a444-e108-46ac-a373-765fed7a41f7','Расставь зверюшек в правильные места.','Послушай и расставь зверюшек по местам. Ослик уже на своём месте — under the tree')],None),
 ('sm1',4,'Homework 4',4,'7d466c9f-4068-40cb-b298-435e63a58611','d9c638fc-2298-4987-9d7c-c6a966e1905b',0,'А теперь послушай историю и проверь, правильно ли ты ответил. + картинка','https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/1793088756161_SM2ed_Student_s_Book_L1_Track_57.mp3',[],'в тексте картинка к истории — у викторины своей картинки нет, она бы пропала'),
 ('sm1',4,'Homework 5',13,'beb2c701-c935-4930-bfcf-3c04cfd50ed1','0fcc69fc-2b29-4598-888d-85cd9462b171',0,'Прочитай описание корзинок и нарисуй их. Linda: I have got twelve apples…','https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/1792619791611_tts_1792619791611.mp3',[],'в тексте — описания корзинок, их надо читать (и задание «нарисуй»)'),
 ('sm1',5,'Homework 2',11,'08d7a1f3-d919-4918-a6e2-1e935c50f99b','9068f8af-8b75-457f-9435-a148c545b41d',0,'Девочка по имени Сьюзи очень хочет с тобой поговорить…','https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/1791457610168_tts_1791457610168.mp3',
   [('27ab7a0d-d398-4dfe-810c-9961312aa486','Послушай Сьюзи ещё раз. Правда это или нет?','Послушай, что Сьюзи делает в разные дни недели. Правда это или нет?')],None),
 ('sm1',7,'Homework 3',9,'8c7b4e2c-3492-435e-b968-61c5ae3ed534','640772e4-5270-4813-af66-1f7e5def1add',0,'Молодец! Теперь время практики. … Прослушай аудио и соедини имена с одеждой. (+ смайлик «молодец»)','https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/1792619575078_tts_1792619575078.mp3',
   [('ff1380c2-67ee-4b54-942d-902faa10a3b4','Прослушай аудио и отметь, где чья одежда (соедини имя и картинку).','Послушай и соедини имя с одеждой: где чья одежда?')],None),
 ('sm1',7,'Homework 4',3,'20a84dbd-9d37-41e7-8b72-3a2547da4a50','17a18c98-8aa0-48bc-97ec-ed69bbabf928',0,'Твоё первое задание — послушать аудио … Название истории — The cap … + обложка','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm1/sm1_u7_hw4_b3.mp3',[],'в тексте обложка истории и «угадай по картинке» — картинка бы пропала'),
 ('sm1',7,'Homework 6',2,'0bffc63e-dfba-4012-b599-3bb75fc7eaed','53caf30e-8430-4896-a58d-b33e936e3ceb',0,'Давай повторим всё, что выучили с тобой на уроке: stripes, spots… (с картинками)','https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/1791401010821_tts_1791401010820.mp3',[],'это повторение слов с картинками, а не инструкция к заданию'),
 ('sm2',3,'Homework 5',4,'1ba8204e-4c35-4816-a0b5-31c977f126e1','904813dc-51e2-4dcf-b5be-5157b0ec7ff0',0,'“I go to my favourite shop with my mum on Saturdays…” — Grace (+ картинка)','https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/1791484378270_tts_1791484378270.mp3',[],'в тексте — слова Грейс, их надо читать, и картинка'),
 ('sm2',4,'Homework 4',3,'5f72e39c-5401-4fb7-ac27-240dd96a7a20','2105be4b-fb53-4d82-8915-27f24dfa7037',0,'Твоё первое задание — послушать запись истории … посмотри на картинку (+ картинка)','https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/1791459006986_tts_1791459006986.mp3',[],'в тексте картинка к истории и «угадай по картинке» — она бы пропала'),
 ('sm2',9,'Homework 4',3,'e8143442-d48e-4200-8682-f79378ebfd8c','ea878672-fc97-49bb-bd19-f273b33d5e2d',0,'Читай и слушай: (+ страницы истории)','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm2/u9/sm2_u9_hw4_b4.mp3',[],'в тексте — страницы истории, их читают вместе с записью'),
 ('sm3',0,'Test',16,'281535a0-7cee-4fb0-b17d-e951a0a694a6','3fee5793-968e-4196-b878-65eab514da46',0,'LISTENING 🎧 Послушай рассказ про Пенни. Текста не будет…','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm3/sm3_u0_test_b16.mp3',
   [('608acaff-9a70-4c8b-b2a2-308292492d4b','Послушай ещё раз и выбери правильный ответ.','LISTENING 🎧 Послушай рассказ про Пенни и выбери правильный ответ. Можно послушать два раза')],None),
 ('sm3',1,'Homework 5',2,'514f4744-7934-4e7f-8914-ca5375082c9a','c1504c6f-93ba-4a86-a576-0ae751f73eac',0,'Ben and Lucy in the library (+ страницы истории)','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm3/sm3_u1_hw5_b2.mp3',[],'в тексте — страницы истории, их читают вместе с записью'),
 ('sm3',2,'Homework 5',2,'fbe254b5-5747-4794-b845-d3f534da7346','1bc8cead-4629-4d42-aa20-e7e6015504a2',0,'🎧 Послушай два диалога: сначала Ким и Дэниэль, потом Том и Мэри.','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm3/sm3_u2_hw5_b2_v2.mp3',
   [('0376eb5c-1ff8-446f-86ef-aa91337bc8b0','Впиши пропущенные слова ⏬','Послушай два диалога (Ким и Дэниэль, потом Том и Мэри) и впиши пропущенные слова')],None),
 ('sm3',2,'Homework 5',4,'827de31d-0716-4716-a9a2-2e417689baa4','1bc8cead-4629-4d42-aa20-e7e6015504a2',0,'🎧 Послушай образец к игре «I spy with my little eye».','https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm3/sm3_u2_hw5_b4_v2.mp3',[],'запись — образец к игре (следующее говорение), а у вопросов викторины свой звук: было бы два источника'),
]
assert len(R) == 50, len(R)
plan = []
for (c, un, lt, n, tid, lid, sn, was, au, tasks, keep) in R:
    plan.append({'course': c, 'unit': un, 'lesson_title': lt, 'text_block_no': n, 'text_block_id': tid, 'lesson_id': lid,
                 'task_block_ids': [t[0] for t in tasks], 'new_titles': {t[0]: t[2] for t in tasks}, 'audio_url': au,
                 'snapshots': sn, 'keep': keep or False})
json.dump(plan, open('plan.json', 'w'), ensure_ascii=False, indent=1)
merge = [r for r in R if not r[10]]; keepl = [r for r in R if r[10]]
two = sum(1 for r in merge if len(r[9]) == 2)
L = ['# Объединение блоков — проверить', '',
     f'Всего мест: {len(R)}. Объединяем: {len(merge)} (из них {two} — запись нужна двум заданиям подряд). Оставляем как есть: {len(keepl)}.', '',
     'Как будет: текстовый блок с записью убираем, запись встаёт прямо в задание (в оба, если заданий два — запись при переходе не прерывается), '
     'инструкция становится заголовком задания. Номера блоков — как в редакторе, до объединения; после него номера ниже сдвинутся на один.', '',
     'В базу пока ничего не записано: сделаем после вашей проверки. Где заголовок не нравится — напишите «курс, юнит, урок, блок → новый текст».', '']
if any(r[6] for r in merge):
    L += ['У Go Getter 3, Unit 2 Test двое учеников уже начали тест — у них останется прежний вид, остальные увидят новый.', '']
for c in C:
    rows = [r for r in merge if r[0] == c]
    if not rows: continue
    L += [f'## {C[c]}', '', '| юнит · урок | блоки | было | станет |', '|---|---|---|---|']
    for (cc, un, lt, n, tid, lid, sn, was, au, tasks, keep) in rows:
        bl = f'текст {n} → задание ' + ', '.join(str(n + 1 + i) for i in range(len(tasks)))
        was_t = was[:100] + ('…' if len(was) > 100 else '')
        old = ' / '.join(f'«{t[1]}»' for t in tasks)
        new = ' / '.join(f'«{t[2]}»' for t in tasks)
        L.append(f'| Unit {un} · {lt} | {bl} | {was_t}<br>Задание: {old} | {new}<br>Запись — {"в оба задания" if len(tasks) > 1 else "в задание"} |')
    L.append('')
L += ['## Оставить как есть', '', '| курс · юнит · урок | блок | почему |', '|---|---|---|']
for (c, un, lt, n, tid, lid, sn, was, au, tasks, keep) in keepl:
    L.append(f'| {C[c]} · Unit {un} · {lt} | текст {n} | {keep} |')
open('spisok.md', 'w').write('\n'.join(L) + '\n')
# apply.sql
q = lambda s: "'" + s.replace("'", "''") + "'"
upd = []
for r in merge:
    for t in r[9]:
        upd.append(f"({q(t[0])}::uuid, {q(t[2])}, {q(r[8])})")
dels = ', '.join(q(r[4]) + '::uuid' for r in merge)
lessons = sorted({r[5] for r in merge})
tasks_ids = ', '.join(q(t[0]) + '::uuid' for r in merge for t in r[9])
S = f"""-- Объединение «текст с записью → задание» (решение Анны 02.11.2026). НЕ ЗАПУСКАТЬ без «да».
-- Сборка: builds/obedinenie/build.py. Мест к объединению: {len(merge)}.
begin;
-- 1. Копия всех затронутых блоков (и текстов, и заданий), RLS включён
create table if not exists classroom_backup_obedinenie_20261102 as
  select * from classroom_blocks where id in ({dels}, {tasks_ids});
alter table classroom_backup_obedinenie_20261102 enable row level security;
-- 2. Запись и новый заголовок — в задание
update classroom_blocks b set payload = b.payload || jsonb_build_object('title', v.t, 'audio', v.a)
from (values
  {(','+chr(10)+'  ').join(upd)}
) v(id, t, a)
where b.id = v.id;
-- 3. Убрать текстовые блоки (только если запись уже переехала в задание)
delete from classroom_blocks t
where t.id in ({dels})
  and t.type = 'text'
  and exists (select 1 from classroom_blocks x where x.lesson_id = t.lesson_id and x.payload->>'audio' = t.payload->>'audio' and x.id <> t.id);
-- 4. Сомкнуть нумерацию в затронутых уроках: через сдвиг, чтобы не задеть уникальность (lesson_id, sort_order)
update classroom_blocks set sort_order = sort_order + 100000 where lesson_id in ({', '.join(q(x)+'::uuid' for x in lessons)});
update classroom_blocks b set sort_order = r.rn - 1
from (select id, row_number() over (partition by lesson_id order by sort_order) rn from classroom_blocks
      where lesson_id in ({', '.join(q(x)+'::uuid' for x in lessons)})) r
where b.id = r.id;
commit;
-- Проверка: у заданий есть запись, текстов не осталось, нумерация без дыр
select (select count(*) from classroom_blocks where id in ({tasks_ids}) and coalesce(payload->>'audio','') <> '') tasks_with_audio,
       (select count(*) from classroom_blocks where id in ({dels})) texts_left;
"""
open('apply.sql', 'w').write(S)
print(len(merge), len(keepl), two)
