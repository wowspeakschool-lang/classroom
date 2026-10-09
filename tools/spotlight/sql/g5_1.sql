with r as (select id from deck_folders where title='Spotlight' and parent_folder_id is null and deleted_at is null),
g as (insert into deck_folders (title, description, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
  select 'Spotlight 5', '5 класс', (select id from r), '📗', 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, 5
  where not exists (select 1 from deck_folders where title='Spotlight 5' and deleted_at is null) returning id)
insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select v.t, g.id, v.e, 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, v.o from g, (values ('Starter Unit', '📘', 1), ('Module 1: School days', '📘', 2), ('Module 2: That''s me!', '📘', 3), ('Module 3: My home, my castle', '📘', 4), ('Module 4: Family ties', '📘', 5), ('Module 5: World animals', '📘', 6), ('Module 6: Round the clock', '📘', 7), ('Module 7: In all weathers', '📘', 8), ('Module 8: Special days', '📘', 9), ('Module 9: Modern living', '📘', 10), ('Module 10: Holidays', '📘', 11), ('Другие разделы', '📎', 12)) v(t, e, o)
returning id, title;