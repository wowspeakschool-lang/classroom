insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select v.s, f.id, '🧺', 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, 99 from (values ('Module 2: Tale time', 'Другие слова'), ('Module 3: Profiles', 'Другие слова'), ('Module 8: Green issues', 'Другие слова')) v(f, s)
join deck_folders f on f.title = v.f and f.parent_folder_id = (select id from deck_folders where title='Spotlight 7' and deleted_at is null) and f.deleted_at is null
where not exists (select 1 from deck_folders x where x.parent_folder_id = f.id and x.title = v.s and x.deleted_at is null)
returning id, title;