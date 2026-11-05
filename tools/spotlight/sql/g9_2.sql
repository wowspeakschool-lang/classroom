insert into deck_folders (title, parent_folder_id, cover_emoji, author_id, is_school_library, "order")
select 'Другие слова', f.id, '🧺', 'd0912d22-5cf7-4273-8113-33b42ad2cdf9', true, 99 from (values ('Module 1: Celebrations'), ('Module 2: Life & Living'), ('Module 3: See it to believe it'), ('Module 4: Technology'), ('Module 5: Art & Literature'), ('Module 7: Staying safe')) v(m)
join deck_folders f on f.title = v.m and f.parent_folder_id = (select id from deck_folders where title='Spotlight 9' and deleted_at is null) and f.deleted_at is null
where not exists (select 1 from deck_folders x where x.parent_folder_id = f.id and x.title = 'Другие слова' and x.deleted_at is null)
returning id;