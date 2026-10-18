UPDATE words w SET image_url = v.u
FROM (VALUES
('architecture','','https://app.wowteach.ru/trainer/media/spotlight6/architecture.webp','https://app.wowteach.ru/trainer/media/spotlight6/architecture.webp'),
('lifetime','','https://app.wowteach.ru/trainer/media/spotlight6/lifetime.webp','https://app.wowteach.ru/trainer/media/spotlight6/lifetime.webp'),
('provide','','https://app.wowteach.ru/trainer/media/spotlight6/provide.webp','https://app.wowteach.ru/trainer/media/spotlight6/provide.webp'),
('remind smb. of smth.','','https://app.wowteach.ru/trainer/media/spotlight6/remind.webp','https://app.wowteach.ru/trainer/media/spotlight6/remind.webp'),
('bagpipes','','https://app.wowteach.ru/trainer/media/spotlight6/bagpipes.webp','https://app.wowteach.ru/trainer/media/spotlight6/bagpipes.webp'),
('band','','https://app.wowteach.ru/trainer/media/spotlight6/band.webp','https://app.wowteach.ru/trainer/media/spotlight6/band.webp'),
('reserve a table','','https://app.wowteach.ru/trainer/media/spotlight6/reserve_a_table.webp','https://app.wowteach.ru/trainer/media/spotlight6/reserve_a_table.webp')) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND (f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 6' AND deleted_at IS NULL)
       OR f.parent_folder_id IN (SELECT id FROM deck_folders WHERE parent_folder_id =
           (SELECT id FROM deck_folders WHERE title = 'Spotlight 6' AND deleted_at IS NULL)))  -- подпапки «Другие слова»
  AND (v.k = '' OR w.translation = v.k)
RETURNING w.id;