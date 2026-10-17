with r as (select id from deck_folders where title='Spotlight' and parent_folder_id is null and deleted_at is null),
g as (insert into deck_folders (title, description, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
  select 'Spotlight 6', '6 класс', (select id from r), '📗', 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, 6
  where not exists (select 1 from deck_folders where title='Spotlight 6' and deleted_at is null) returning id)
insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select v.t, g.id, v.e, 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, v.o from g, (values ('Module 1: Who''s who?', '📘', 1), ('Module 2: Here we are!', '📘', 2), ('Module 3: Getting around', '📘', 3), ('Module 4: Day after day', '📘', 4), ('Module 5: Feasts', '📘', 5), ('Module 6: Leisure activities', '📘', 6), ('Module 7: Now and then', '📘', 7), ('Module 8: Rules and regulations', '📘', 8), ('Module 9: Food and refreshments', '📘', 9), ('Module 10: Holiday time', '📘', 10)) v(t, e, o)
returning id, title;