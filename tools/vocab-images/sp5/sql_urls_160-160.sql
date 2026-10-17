UPDATE words w SET image_url = v.u
FROM (VALUES
('That''s not my kind of place.','','https://app.wowteach.ru/trainer/media/spotlight5/not_my_kind_of_place.webp','https://app.wowteach.ru/trainer/media/spotlight5/not_my_kind_of_place.webp'),
('keep out','','https://app.wowteach.ru/trainer/media/spotlight5/keep_out.webp','https://app.wowteach.ru/trainer/media/spotlight5/keep_out.webp'),
('face','','https://app.wowteach.ru/trainer/media/spotlight5/face_difficulty.webp','https://app.wowteach.ru/trainer/media/spotlight5/face_difficulty.webp')) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 5' AND deleted_at IS NULL)
  AND (v.k = '' OR d.title LIKE v.k || ' %')
RETURNING w.id;