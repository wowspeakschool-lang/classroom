-- SM1 · заголовки-разделители перед длинными сериями одинаковых заданий
-- Решение Анны от 20.10.2026: перед серией из четырёх и более одинаковых
-- заданий ставим текстовый блок-заголовок, чтобы ребёнок видел, что тема
-- сменилась, а не десять одинаковых рамок подряд.
--
-- Формулировки: «Теперь соберём слова 🔤» / «Теперь соберём предложения 📝»;
-- если серия предложений идёт сразу за серией слов — «А теперь целые предложения 📝».
-- Тесты юнитов не трогаем: в тесте разговорный заголовок не к месту.
-- 12 заголовков в 12 домашках. Применено через MCP 20.10.2026.

-- 1. отодвигаем существующие блоки: 0,1,2… → 1000,1010,1020…
update classroom_blocks set sort_order = sort_order * 10 + 1000
where lesson_id in (
  select l.id
  from classroom_courses c
  join classroom_units u on u.course_id = c.id
  join classroom_lessons l on l.unit_id = u.id
  where c.slug = 'sm1'
    and (u.sort_order, l.title) in ((1,'Homework 7'),(2,'Homework 2'),(2,'Homework 5'),
        (3,'Homework 7'),(4,'Homework 3'),(5,'Homework 2'),(6,'Homework 5'),
        (7,'Homework 2'),(7,'Homework 5'),(8,'Homework 5'),(9,'Homework 5')));

-- 2. заголовок встаёт в освободившийся зазор перед нужным блоком
insert into classroom_blocks (lesson_id, type, payload, sort_order)
select l.id, 'text', jsonb_build_object('html', r.html), r.before_so * 10 + 995
from (values
  (1,'Homework 7', 3,'<h3>Теперь соберём слова 🔤</h3>'),
  (1,'Homework 7',13,'<h3>А теперь целые предложения 📝</h3>'),
  (2,'Homework 2',14,'<h3>Теперь соберём предложения 📝</h3>'),
  (2,'Homework 5', 3,'<h3>Теперь соберём предложения 📝</h3>'),
  (3,'Homework 7', 4,'<h3>Теперь соберём слова 🔤</h3>'),
  (4,'Homework 3', 8,'<h3>Теперь соберём предложения 📝</h3>'),
  (5,'Homework 2',14,'<h3>Теперь соберём предложения 📝</h3>'),
  (6,'Homework 5', 8,'<h3>Теперь соберём предложения 📝</h3>'),
  (7,'Homework 2',14,'<h3>Теперь соберём предложения 📝</h3>'),
  (7,'Homework 5', 8,'<h3>Теперь соберём предложения 📝</h3>'),
  (8,'Homework 5', 4,'<h3>Теперь соберём предложения 📝</h3>'),
  (9,'Homework 5', 4,'<h3>Теперь соберём предложения 📝</h3>')
) as r(un, lt, before_so, html)
join classroom_courses c on c.slug = 'sm1'
join classroom_units u on u.course_id = c.id and u.sort_order = r.un
join classroom_lessons l on l.unit_id = u.id and l.title = r.lt;

-- 3. нумерация снова подряд с нуля
with novyy as (
  select b.id, row_number() over (partition by b.lesson_id order by b.sort_order) - 1 as n
  from classroom_blocks b
  where b.sort_order >= 995 and b.lesson_id in (
    select l.id from classroom_courses c
    join classroom_units u on u.course_id = c.id
    join classroom_lessons l on l.unit_id = u.id
    where c.slug = 'sm1'))
update classroom_blocks b set sort_order = novyy.n
from novyy where b.id = novyy.id;
