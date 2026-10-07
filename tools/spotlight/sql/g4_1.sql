with root as (
  insert into deck_folders (title, description, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
  select 'Spotlight', 'Английский в фокусе · 2–11 класс', null, '🔦', 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, 11
  where not exists (select 1 from deck_folders where title='Spotlight' and parent_folder_id is null and deleted_at is null)
  returning id),
r as (select id from root union all select id from deck_folders where title='Spotlight' and parent_folder_id is null and deleted_at is null),
g as (insert into deck_folders (title, description, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
  select 'Spotlight 4', '4 класс', (select id from r limit 1), '📗', 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, 4 returning id)
insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select v.t, g.id, v.e, 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, v.o from g, (values ('Module 1', '📘', 1), ('Module 2', '📘', 2), ('Module 3', '📘', 3), ('Module 4', '📘', 4), ('Module 5', '📘', 5), ('Module 6', '📘', 6), ('Module 7', '📘', 7), ('Module 8', '📘', 8), ('Другие разделы', '📎', 9)) v(t, e, o)
returning id, title;