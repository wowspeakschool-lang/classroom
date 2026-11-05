with r as (select id from deck_folders where title='Spotlight' and parent_folder_id is null and deleted_at is null),
g as (insert into deck_folders (title, description, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
  select 'Spotlight 9', '9 класс', (select id from r), '📗', 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, -1
  where not exists (select 1 from deck_folders where title='Spotlight 9' and deleted_at is null) returning id)
insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select v.t, g.id, '📘', 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, v.o from g, (values ('Module 1: Celebrations', 8), ('Module 2: Life & Living', 7), ('Module 3: See it to believe it', 6), ('Module 4: Technology', 5), ('Module 5: Art & Literature', 4), ('Module 6: Town & Community', 3), ('Module 7: Staying safe', 2), ('Module 8: Challenges', 1)) v(t, o)
returning id, title;