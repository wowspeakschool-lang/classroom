UPDATE words w SET image_url = v.u
FROM (VALUES
('art museum','','https://app.wowteach.ru/trainer/media/spotlight6/art_museum.webp','https://app.wowteach.ru/trainer/media/spotlight6/art_museum.webp'),
('currency','','https://app.wowteach.ru/trainer/media/spotlight6/currency.webp','https://app.wowteach.ru/trainer/media/spotlight6/currency.webp'),
('British pound','','https://app.wowteach.ru/trainer/media/spotlight6/British_pound.webp','https://app.wowteach.ru/trainer/media/spotlight6/British_pound.webp'),
('upright','','https://app.wowteach.ru/trainer/media/spotlight6/upright.webp','https://app.wowteach.ru/trainer/media/spotlight6/upright.webp'),
('war','','https://app.wowteach.ru/trainer/media/spotlight6/war.webp','https://app.wowteach.ru/trainer/media/spotlight6/war.webp'),
('brush my teeth','','https://app.wowteach.ru/trainer/media/spotlight6/brush_my_teeth.webp','https://app.wowteach.ru/trainer/media/spotlight6/brush_my_teeth.webp'),
('distance','','https://app.wowteach.ru/trainer/media/spotlight6/distance.webp','https://app.wowteach.ru/trainer/media/spotlight6/distance.webp')) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND (f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 6' AND deleted_at IS NULL)
       OR f.parent_folder_id IN (SELECT id FROM deck_folders WHERE parent_folder_id =
           (SELECT id FROM deck_folders WHERE title = 'Spotlight 6' AND deleted_at IS NULL)))  -- подпапки «Другие слова»
  AND (v.k = '' OR w.translation = v.k)
RETURNING w.id;