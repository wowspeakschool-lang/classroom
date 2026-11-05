# -*- coding: utf-8 -*-
"""Аудирования тестов GG3 и SM3 — переписаны 05.11.2026.

Решение Анны: «нужно там про нескольких детей… и 3 варианта ответа — peas,
pizza, tuna», то есть все три варианта должны прозвучать в записи.

Принцип (её же пример):
  1. в рассказе два-три человека, факты у них разные;
  2. КАЖДЫЙ вариант ответа звучит в записи — у кого-то как верный, у кого-то
     как чужой или отменённый;
  3. вопрос требует удержать связь: кто именно, что изменилось, от чего отказались.

Рассказ по-прежнему в третьем лице, без диалогов: голос SpeechKit один.
Имя файла — <курс>_u<N>_test_b<номер блока как в редакторе>_v<N>.mp3.
"""

NARRATIONS = {}

def add(course, unit, block, fname, text, title, questions):
    NARRATIONS[(course, unit)] = dict(block=block, file=fname, text=" ".join(text.split()),
                                      title=title, questions=questions)

T = "LISTENING 🎧 Послушай рассказ и выбери правильный ответ. Можно послушать несколько раз."

# ------------------------------------------------ Go Getter 3
add("gg3", 0, 16, "gg3_u0_test_b16_v2.mp3", """
This is a story about three friends: Elena, Emma and Emma's brother George.
Elena is fourteen, Emma is thirteen and George is eleven.
Elena usually goes to school by bus, but Emma always goes by bike. George doesn't
like the bus, so his dad takes him to school by car.
Emma has got dance classes twice a week. Elena hasn't got dance classes — she does
karate every day after school, and George plays football at the weekend.
Elena is good at Maths and she is interested in Art, but she isn't very good at
Geography. Emma is different: she is going to study Geography more this year.
Emma isn't scared of spiders and she isn't scared of the dark. She is scared of dogs.
George is scared of the dark, and nobody in the family is scared of spiders.
""", T, [
 ("How old is Emma?", ["thirteen", "fourteen", "eleven"]),
 ("How does Emma go to school?", ["by bike", "by bus", "by car"]),
 ("How often does Elena do karate?", ["every day", "twice a week", "at the weekend"]),
 ("Who is going to study Geography more this year?", ["Emma", "Elena", "George"]),
 ("What is Emma scared of?", ["dogs", "spiders", "the dark"]),
])

add("gg3", 1, 9, "gg3_u1_test_b9_v2.mp3", """
This is a story about Oliver, his little brother Ben and their cousin Maya.
Oliver is eleven, Ben is five and Maya is thirteen.
In this family everybody helps at home. Oliver sets the table every evening, but he
never takes out the rubbish. Maya takes out the rubbish on Mondays and Thursdays.
Ben is too small for that, so he feeds the cat and puts away his toys.
Nobody likes loading the dishwasher, so their dad loads it after dinner. He irons the
shirts on Sunday mornings and he always listens to music when he irons. Maya irons her
own shirts on Saturday evenings.
Right now the three children are at their grandmother's house. Maya is vacuuming the
living room, Ben is playing in the garden, and Oliver is watering the plants.
Their grandmother isn't helping them — she is making a cake.
""", T, [
 ("What does Oliver do every evening?", ["he sets the table", "he takes out the rubbish", "he loads the dishwasher"]),
 ("Who takes out the rubbish?", ["Maya", "Oliver", "Ben"]),
 ("When does their dad iron the shirts?", ["on Sunday mornings", "on Saturday evenings", "on Mondays and Thursdays"]),
 ("What is Oliver doing right now?", ["he is watering the plants", "he is vacuuming the living room", "he is playing in the garden"]),
 ("Who is making a cake?", ["their grandmother", "Maya", "Ben"]),
 ("How old is Ben?", ["five", "eleven", "thirteen"]),
])

add("gg3", 2, 9, "gg3_u2_test_b9_v2.mp3", """
This is a story about Zoe, her dad and her friend Leo. Zoe is twelve.
Zoe goes shopping with her dad every Saturday morning. Leo goes shopping with his mum
every Sunday morning, and Leo's dad does the shopping on Saturday evening.
There are three shops near Zoe's house: a baker's, a greengrocer's and a big
supermarket. Zoe's family buy their bread at the baker's and their fruit at the
greengrocer's, because the fruit there is fresher and cheaper. Leo's family buy
everything at the supermarket, because it is nearer and the shop is bigger.
Zoe's dad never pays in cash. He always pays by card. Leo's mum pays in cash and she
always counts her change.
Last Saturday the queue at the supermarket was very long. On Sunday there was no queue
at all. Today the queue isn't too long. Zoe's dad pushes the shopping trolley and
Zoe carries the heavy bags home.
""", T, [
 ("When does Zoe go shopping with her dad?", ["every Saturday morning", "every Sunday morning", "on Saturday evening"]),
 ("Where does Zoe's family buy their bread?", ["at the baker's", "at the greengrocer's", "at the supermarket"]),
 ("Why does Leo's family go to the supermarket?", ["it is nearer and bigger", "the fruit is fresher", "it is cheaper"]),
 ("Who pays in cash?", ["Leo's mum", "Zoe's dad", "Zoe"]),
 ("What was the queue like last Saturday?", ["very long", "not too long", "there was no queue"]),
 ("Who carries the bags home?", ["Zoe", "her dad", "Leo"]),
])

add("gg3", 3, 8, "gg3_u3_test_b8_v2.mp3", """
Last summer three friends went on holiday. Daniel went to Italy with his family,
Nora went to Spain and Tom went to Scotland.
In Italy, Daniel went snorkelling with his father on the first day. His sister didn't
go snorkelling — she stayed at the hotel with their mother. In the afternoon it rained,
so the family stayed inside and played cards. They didn't go hiking and they didn't go
to the beach.
On the second day they went on a guided tour of a museum. Daniel's father was excited,
but Daniel got bored after an hour.
In the evening they ate in a restaurant. Daniel's mother had fish, his sister had soup,
and Daniel had pizza.
At the airport on the last day Daniel was sad, but his sister was happy, because she
doesn't like hot weather.
""", T, [
 ("Where did Daniel go on holiday?", ["to Italy", "to Spain", "to Scotland"]),
 ("Who went snorkelling with Daniel?", ["his father", "his sister", "his mother"]),
 ("What did the family do in the afternoon?", ["they stayed inside", "they went hiking", "they went to the beach"]),
 ("How did Daniel feel in the museum?", ["bored", "excited", "happy"]),
 ("What did Daniel eat in the restaurant?", ["pizza", "fish", "soup"]),
 ("How did Daniel feel at the airport?", ["sad", "happy", "excited"]),
])

add("gg3", 4, 9, "gg3_u4_test_b9_v2.mp3", """
Last Friday evening something happened at Nina's house. Nina was doing her homework in
her bedroom. Her brother Jack was downstairs. He was watching a film and making toast
at the same time.
Everything in the kitchen was new: a smart TV, a laptop and a hairdryer. Only the
toaster was very old.
Suddenly there was smoke in the kitchen. Jack shouted and Nina ran downstairs quickly.
Their mother walked downstairs slowly, because she was carrying the baby. Their father
came in from the garden and unplugged the toaster carefully.
Nobody was hurt. The next day the family bought a new toaster. They didn't buy a new TV
and they didn't buy a new hairdryer.
""", T, [
 ("What was Nina doing last Friday?", ["her homework", "watching a film", "making toast"]),
 ("Where was her brother?", ["downstairs", "in his bedroom", "in the garden"]),
 ("Which thing in the house was very old?", ["the toaster", "the smart TV", "the laptop"]),
 ("How did Nina run downstairs?", ["quickly", "slowly", "carefully"]),
 ("Who unplugged the toaster?", ["her father", "her mother", "her brother"]),
 ("What did the family buy the next day?", ["a new toaster", "a new TV", "a new hairdryer"]),
])

add("gg3", 5, 10, "gg3_u5_test_b10_v2.mp3", """
This is a story about Max and his sister Lily.
On Monday Max fell off his bike and cut his knee. Lily didn't fall off her bike, but
she fell down the stairs at school the same week and hurt her arm.
Their mother put some cream on Max's cut and cold water on Lily's arm.
On Tuesday Max had a headache and a temperature. Lily had a cough and a sore throat,
and their father had a blocked nose.
The doctor came on Wednesday. She said Lily should stay in bed for two days, and Max
shouldn't play football for a week. Max can play again on Monday.
On Thursday Max felt better, but Lily felt worse. On Friday Max went to school and ate
his lunch, but he didn't play football.
""", T, [
 ("What happened to Max on Monday?", ["he fell off his bike", "he fell down the stairs", "he hurt his arm"]),
 ("Who had a cough and a sore throat?", ["Lily", "Max", "their father"]),
 ("What did Max have on Tuesday?", ["a headache and a temperature", "a cough and a sore throat", "a blocked nose"]),
 ("What does the doctor say about football?", ["Max shouldn't play for a week", "Max should stay in bed for two days", "Max can play again on Monday"]),
 ("Who felt worse on Thursday?", ["Lily", "Max", "their father"]),
 ("What didn't Max do on Friday?", ["play football", "go to school", "eat his lunch"]),
])

add("gg3", 6, 9, "gg3_u6_test_b9_v2.mp3", """
This is a story about Felix and his sister Ava. Felix is thirteen and Ava is nine.
Last Sunday Felix cooked dinner for the family for the first time. He made pasta with
tomato sauce. His mother wanted fish and chips and Ava wanted an apple cake, but Felix
had already bought the pasta.
First he chopped an onion and some garlic and fried them in a pan. Then he put the
tomatoes in the pan and cooked the pasta in a pot.
There was a problem with the sauce: Felix put in too much salt. He didn't put in too
much sugar, and the sauce wasn't cold — it was very hot.
His mother said the dinner was delicious. Ava said it was too sweet. Their father said
it was disgusting, and then he laughed.
Since that Sunday Felix has cooked dinner three times. Ava has cooked once, and their
father has cooked ten times.
""", T, [
 ("How old is Felix?", ["thirteen", "nine", "three"]),
 ("What did Felix cook?", ["pasta with tomato sauce", "an apple cake", "fish and chips"]),
 ("What did he fry in the pan?", ["an onion and some garlic", "the pasta", "the tomatoes"]),
 ("What was the problem with the sauce?", ["too much salt", "too much sugar", "it was cold"]),
 ("Who said the dinner was disgusting?", ["their father", "his mother", "Ava"]),
 ("How many times has Felix cooked dinner since that Sunday?", ["three times", "once", "ten times"]),
])

add("gg3", 7, 10, "gg3_u7_test_b10_v2.mp3", """
This is a story about Ruby and her cousin Dylan.
Ruby lives in a terraced house near the sea. Dylan lives in a block of flats in the
city, and their grandparents live in a big detached house in the country.
Ruby's favourite place is the balcony, because she can see the sea from there.
The basement is warm, but she doesn't like it, and all her books are in the attic.
Ruby shares her room with her little brother. Dylan shares his room with his cousin
when he visits, and their grandparents' house is so big that nobody shares a room.
This weekend the family are cleaning up the new house. They aren't moving the furniture
yet and they aren't painting the balcony.
On Saturday Ruby must pack her books. On Sunday she is going to meet her cousins.
""", T, [
 ("What kind of house does Ruby live in?", ["a terraced house", "a detached house", "a block of flats"]),
 ("What is Ruby's favourite place in the house?", ["the balcony", "the basement", "the attic"]),
 ("Why does she like it?", ["she can see the sea", "it is warm there", "her books are there"]),
 ("Who does Ruby share her room with?", ["her little brother", "her cousin", "nobody"]),
 ("What are the family doing this weekend?", ["cleaning up the new house", "moving the furniture", "painting the balcony"]),
 ("What must Ruby do on Saturday?", ["pack her books", "paint the balcony", "meet her cousins"]),
])

add("gg3", 8, 9, "gg3_u8_test_b9_v2.mp3", """
This is a story about three friends: Ellie, Lucas and Mia. Ellie is thirteen,
Lucas is fourteen and Mia is twelve.
Ellie thinks she will live in a big city one day. Lucas says he will stay in their
small town, and Mia wants to live in a village near the mountains.
Ellie wants to be a vet, because she loves animals. Lucas thinks he will be a doctor,
and Mia is going to be a teacher.
Next year Ellie will learn Spanish at school. Lucas is learning French now, and Mia
will start German in September.
Ellie wants to work in South America. Lucas wants to work in Spain, and Mia will
probably work in Australia.
Ellie says she will not be rich, but she will be happy. Lucas says he will be rich.
Mia says she doesn't know.
""", T, [
 ("Where does Ellie think she will live?", ["in a big city", "in their small town", "in a village"]),
 ("What job does Ellie want?", ["a vet", "a doctor", "a teacher"]),
 ("Which language will Ellie learn next year?", ["Spanish", "French", "German"]),
 ("Where does Ellie want to work?", ["in South America", "in Spain", "in Australia"]),
 ("What does Ellie say about money?", ["she will not be rich", "she will be rich", "she does not know"]),
 ("Who is going to be a teacher?", ["Mia", "Ellie", "Lucas"]),
])

# ------------------------------------------------ Super Minds 3
add("sm3", 0, 10, "sm3_u0_test_b10_v2.mp3", """
This is a story about Penny and her brother Sam. Penny is seven and Sam is nine.
Their cousin Ruby is twenty-four.
Penny's bedroom is upstairs. Sam's bedroom is downstairs, next to the kitchen, and the
old bikes are in the cellar.
Penny is good at dancing and she is very good at telling stories, but she isn't good at
swimming. Sam is good at swimming.
Their grandmother is good at making cakes. Their mum makes bread, and Sam makes
sandwiches.
Penny has got twenty-four books. Sam has got fourteen books and Ruby has got forty-two.
""", T, [
 ("How old is Penny?", ["seven", "nine", "twenty-four"]),
 ("Where is Penny's bedroom?", ["upstairs", "downstairs", "in the cellar"]),
 ("What is Penny NOT good at?", ["swimming", "dancing", "telling stories"]),
 ("Who is good at making cakes?", ["her grandmother", "her mum", "her brother"]),
 ("How many books has Penny got?", ["twenty-four", "fourteen", "forty-two"]),
])

add("sm3", 1, 7, "sm3_u1_test_b7_v2.mp3", """
This is a story about Milo and his friend Ada.
Milo's favourite subject is Geography. Ada's favourite subject is Science, and Milo's
brother likes Maths best.
Milo doesn't like Maths at all. He likes Art, and Geography is his favourite.
At Milo's school the children have to wear a uniform. They don't have to wear a hat,
and they can wear trainers only on Fridays.
Milo hates singing. Ada hates dancing, and Milo's brother hates swimming.
There are nine books in Milo's school bag today. Ada has got five books and Milo's
brother has got nineteen.
""", T, [
 ("What is Milo's favourite subject?", ["Geography", "Science", "Maths"]),
 ("Which subject does Milo NOT like?", ["Maths", "Art", "Geography"]),
 ("What do the children have to wear?", ["a uniform", "a hat", "trainers"]),
 ("What does Milo hate doing?", ["singing", "dancing", "swimming"]),
 ("How many books has Milo got in his school bag?", ["nine", "five", "nineteen"]),
])

add("sm3", 2, 8, "sm3_u2_test_b8_v2.mp3", """
This is a story about Freya and her brother Noah.
Freya has got a basket. There are some apples and some rolls in the basket, but there
aren't any sausages. There is some cheese too.
Freya has got six apples. Noah has got seven apples and their mother has got sixteen.
Their mother is making a salad. There are onions and peas in the salad. There isn't any
cheese in the salad, and there aren't any rolls in it.
Noah would like some lemonade. Freya would like some water, and their mother would like
some soup.
For dinner there is some soup. There isn't any salad for dinner today — the salad is
for tomorrow.
""", T, [
 ("Are there any sausages in the basket?", ["No, there aren't.", "Yes, there are.", "Yes, there is."]),
 ("How many apples has Freya got?", ["six", "seven", "sixteen"]),
 ("What is there in the salad?", ["onions and peas", "cheese and rolls", "soup and water"]),
 ("What would Noah like?", ["some lemonade", "some water", "some soup"]),
 ("What is there for dinner?", ["some soup", "some salad", "some rolls"]),
])

add("sm3", 3, 8, "sm3_u3_test_b8_v2.mp3", """
This is a story about Hugo and his sister Iris.
Hugo gets up at half past seven. Iris gets up at quarter past seven, and their father
gets up at half past nine on Sundays.
Before school Hugo always takes the dog for a walk. Iris does the shopping with their
mother, and their father washes up before school.
Hugo doesn't like washing up. He doesn't mind sweeping the floor, and he likes tidying
up his room.
Hugo does the shopping on Monday. Iris does it on Saturday, and their grandmother does
it on Wednesday.
Hugo goes to bed at quarter past nine. Iris goes to bed at quarter to nine, and at the
weekend Hugo goes to bed at half past nine.
""", T, [
 ("What time does Hugo get up?", ["at half past seven", "at quarter past seven", "at half past nine"]),
 ("What does Hugo always do before school?", ["He takes the dog for a walk.", "He does the shopping.", "He washes up."]),
 ("What doesn't Hugo like doing?", ["washing up", "sweeping the floor", "tidying up his room"]),
 ("When does Hugo do the shopping?", ["on Monday", "on Saturday", "on Wednesday"]),
 ("What time does Hugo go to bed?", ["at quarter past nine", "at quarter to nine", "at half past nine"]),
])

add("sm3", 4, 7, "sm3_u4_test_b7_v2.mp3", """
This is a story about Greta and her friend Oscar.
Greta lives in a small town. Opposite her house there is a library. Opposite Oscar's
house there is a bank, and near the market square there is an old tower.
The bank is between the supermarket and the car park. The sports centre is near the bus
station, and the library is between two trees.
On Monday Greta is going to the library to borrow a book. Oscar is going to the sports
centre to go swimming, and Greta's mother is going to the market square to buy some
apples.
On Saturday Greta is going to the sports centre. Oscar is going to the library, and on
Sunday they are both going to the market square.
""", T, [
 ("What is opposite Greta's house?", ["the library", "the bank", "the tower"]),
 ("Where is the tower?", ["near the market square", "opposite the library", "between two trees"]),
 ("Why is Greta going to the library on Monday?", ["to borrow a book", "to go swimming", "to buy some apples"]),
 ("Where is the bank?", ["between the supermarket and the car park", "near the bus station", "between two trees"]),
 ("Where is Greta going on Saturday?", ["to the sports centre", "to the library", "to the market square"]),
])

add("sm3", 5, 7, "sm3_u5_test_b7_v2.mp3", """
This is a story about Otis and his cousin Nell.
Yesterday Otis was at the beach. Nell was in the park, and their grandfather was at
school — he is a teacher.
In the morning Otis was in a boat with his father. There were two dolphins near the boat
and three seals near the rocks. Twelve birds were sitting on the water.
There weren't any jellyfish in the sea yesterday. There were some starfish and one
seahorse.
Otis put a starfish and a seahorse in his bucket. Nell had a turtle and a shell in her
bucket, and their grandfather had nothing in his bucket.
At six o'clock Otis was in the café with his family. His father was still in the boat,
and Nell was in the sea.
""", T, [
 ("Where was Otis yesterday?", ["at the beach", "in the park", "at school"]),
 ("How many dolphins were there near the boat?", ["two", "three", "twelve"]),
 ("Were there any jellyfish?", ["No, there weren't.", "Yes, there were.", "Yes, there was."]),
 ("What was in Otis's bucket?", ["a starfish and a seahorse", "a turtle and a shell", "nothing"]),
 ("Where was Otis at six o'clock?", ["in the café", "in the boat", "in the sea"]),
])

add("sm3", 6, 8, "sm3_u6_test_b8_v2.mp3", """
This is a story about Maisie and her brother Rex.
Maisie's tablet is bigger than her mobile phone, and her laptop is bigger than the
tablet. Her torch is the smallest thing she has got.
Maisie's favourite gadget is her laptop. Rex's favourite gadget is his games console,
and their father's favourite is his old torch.
The torch is cheaper than the electric fan. The laptop is more expensive than the fan,
and the tablet is the most expensive thing in the house.
In their building the lift is slower than the stairs. The electric fan is faster than
the old digital radio, and the stairs are the fastest way to the third floor.
""", T, [
 ("Is Maisie's tablet bigger than her mobile phone?", ["Yes, it is.", "No, it isn't.", "Yes, it does."]),
 ("What is bigger than the tablet?", ["the laptop", "the mobile phone", "the torch"]),
 ("What is Maisie's favourite gadget?", ["her laptop", "her games console", "her torch"]),
 ("Which gadget is cheaper than the electric fan?", ["the torch", "the laptop", "the tablet"]),
 ("What is slower than the stairs?", ["the lift", "the electric fan", "the digital radio"]),
])

add("sm3", 7, 7, "sm3_u7_test_b7_v2.mp3", """
This is a story about Rufus and his sister Poppy.
On Monday Rufus had a headache and a cough. Poppy had a stomachache, and their
grandfather had an earache.
Rufus's mum phoned the doctor on Monday evening. Poppy phoned their grandmother, and
the nurse phoned the school.
On Tuesday Rufus stayed at home and watched TV. Poppy went to school, and their cousin
played football in the park.
Poppy cooked some soup for Rufus on Tuesday. Their mum cooked soup on Wednesday, and
the doctor brought some medicine.
Rufus went to school again on Thursday. Poppy was at school on Tuesday, and their
grandfather felt better on Wednesday.
""", T, [
 ("What did Rufus have on Monday?", ["a headache and a cough", "a stomachache", "an earache"]),
 ("Who phoned the doctor?", ["his mum", "his sister", "the nurse"]),
 ("What did Rufus do on Tuesday?", ["He watched TV.", "He went to school.", "He played football."]),
 ("Who cooked some soup for Rufus?", ["his sister", "his mum", "the doctor"]),
 ("When did Rufus go to school again?", ["on Thursday", "on Tuesday", "on Wednesday"]),
])

add("sm3", 8, 7, "sm3_u8_test_b7_v2.mp3", """
This is a story about Tessa and her brother Felix.
Last summer Tessa went to Egypt with her family. Her friend Mara went to Spain, and
Felix's school group went to China.
They stayed in a hotel for two weeks. Mara stayed in Spain for two days only, and
Felix's grandparents stayed in China for two months.
Tessa didn't go to the museum, because it was closed. Her mother went to the museum a
year later, and Felix went to the old market instead.
Tessa sent five postcards. Felix sent four, and their mother sent fifteen.
Every evening they ate fish and rice. At lunchtime they had pizza and salad, and for
breakfast there was always soup and rolls.
""", T, [
 ("Where did Tessa go last summer?", ["to Egypt", "to Spain", "to China"]),
 ("How long did they stay in the hotel?", ["two weeks", "two days", "two months"]),
 ("Did Tessa go to the museum?", ["No, she didn't.", "Yes, she did.", "No, she wasn't."]),
 ("How many postcards did Tessa send?", ["five", "four", "fifteen"]),
 ("What did they eat every evening?", ["fish and rice", "pizza and salad", "soup and rolls"]),
])

add("sm3", 9, 7, "sm3_u9_test_b7_v2.mp3", """
This is a story about Liam and his sister Orla.
Liam's grandma lives in Scotland. His aunt lives in London, and his uncle lives in Italy.
On Monday it is going to be cloudy in Scotland. In London it is going to be sunny, and
in Italy it is going to be foggy.
On Monday Liam and his grandma are going to make pizza. Orla is going to ride her bike.
On Tuesday they are going to watch a film, and on Wednesday they are going to ride their
bikes together.
Liam is going to take photos of the old castle. Orla is going to take photos of the
forest, and their grandma is going to take a photo of Liam's new bike.
""", T, [
 ("Where does Liam's grandma live?", ["in Scotland", "in London", "in Italy"]),
 ("What is the weather going to be like in Scotland on Monday?", ["cloudy", "sunny", "foggy"]),
 ("What are Liam and his grandma going to do on Monday?", ["make pizza", "ride their bikes", "watch a film"]),
 ("When are they going to watch a film?", ["on Tuesday", "on Monday", "on Wednesday"]),
 ("What is Liam going to take photos of?", ["the old castle", "the forest", "his new bike"]),
])

# Отдельная запись: SM3 Unit 0 Test, блок 9 — «Послушай и выбери число».
# У блока вообще нет звука, ребёнку нечего слушать.
CHISLA = {
 "file": "sm3_u0_test_b9.mp3",
 "text": "Number one. Twenty-four. Number two. Thirty-nine. Number three. Fifty-two. "
         "Number four. Seventy-six. Number five. One hundred.",
}
