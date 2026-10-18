with r as (select id from deck_folders where title='Spotlight' and parent_folder_id is null and deleted_at is null),
g as (insert into deck_folders (title, description, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
  select 'Spotlight 7', '7 класс', (select id from r), '📗', 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, 7
  where not exists (select 1 from deck_folders where title='Spotlight 7' and deleted_at is null) returning id)
insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select v.t, g.id, '📘', 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, v.o from g, (values ('Module 1: Lifestyles', 1), ('Module 2: Tale time', 2), ('Module 3: Profiles', 3), ('Module 4: In the news', 4), ('Module 5: What the future holds', 5), ('Module 6: Having fun', 6), ('Module 7: In the spotlight', 7), ('Module 8: Green issues', 8), ('Module 9: Shopping time', 9), ('Module 10: In good health', 10)) v(t, o)
returning id, title;