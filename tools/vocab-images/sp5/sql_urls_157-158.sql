UPDATE words w SET image_url = v.u
FROM (VALUES
('the River Nile','','https://app.wowteach.ru/trainer/media/spotlight5/the_Nile.webp','https://app.wowteach.ru/trainer/media/spotlight5/the_Nile.webp'),
('the Thames','','https://app.wowteach.ru/trainer/media/spotlight5/the_Thames.webp','https://app.wowteach.ru/trainer/media/spotlight5/the_Thames.webp'),
('the Himalayas','','https://app.wowteach.ru/trainer/media/spotlight5/the_Himalayas.webp','https://app.wowteach.ru/trainer/media/spotlight5/the_Himalayas.webp'),
('Valley of the Kings','','https://app.wowteach.ru/trainer/media/spotlight5/Valley_of_the_Kings.webp','https://app.wowteach.ru/trainer/media/spotlight5/Valley_of_the_Kings.webp'),
('Korea','','https://app.wowteach.ru/trainer/media/spotlight5/Korea.webp','https://app.wowteach.ru/trainer/media/spotlight5/Korea.webp'),
('Nepal','','https://app.wowteach.ru/trainer/media/spotlight5/Nepal.webp','https://app.wowteach.ru/trainer/media/spotlight5/Nepal.webp'),
('Northern Ireland','','https://app.wowteach.ru/trainer/media/spotlight5/Northern_Ireland.webp','https://app.wowteach.ru/trainer/media/spotlight5/Northern_Ireland.webp'),
('Pakistan','','https://app.wowteach.ru/trainer/media/spotlight5/Pakistan.webp','https://app.wowteach.ru/trainer/media/spotlight5/Pakistan.webp'),
('Switzerland','','https://app.wowteach.ru/trainer/media/spotlight5/Switzerland.webp','https://app.wowteach.ru/trainer/media/spotlight5/Switzerland.webp'),
('the Philippines','','https://app.wowteach.ru/trainer/media/spotlight5/the_Philippines.webp','https://app.wowteach.ru/trainer/media/spotlight5/the_Philippines.webp')) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 5' AND deleted_at IS NULL)
  AND (v.k = '' OR d.title LIKE v.k || ' %')
RETURNING w.id;