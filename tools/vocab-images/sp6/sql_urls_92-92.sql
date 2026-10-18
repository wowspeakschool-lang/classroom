UPDATE words w SET image_url = v.u
FROM (VALUES
('hire a car','','https://app.wowteach.ru/trainer/media/spotlight6/hire_a_car.webp','https://app.wowteach.ru/trainer/media/spotlight6/hire_a_car.webp')) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND (f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 6' AND deleted_at IS NULL)
       OR f.parent_folder_id IN (SELECT id FROM deck_folders WHERE parent_folder_id =
           (SELECT id FROM deck_folders WHERE title = 'Spotlight 6' AND deleted_at IS NULL)))  -- подпапки «Другие слова»
  AND (v.k = '' OR w.translation = v.k)
RETURNING w.id;