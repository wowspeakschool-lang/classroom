UPDATE words w SET image_url = v.u
FROM (VALUES
('beast','','https://app.wowteach.ru/trainer/media/spotlight7/beast.webp','https://app.wowteach.ru/trainer/media/spotlight7/beast.webp'),
('tan','','https://app.wowteach.ru/trainer/media/spotlight7/tan.webp','https://app.wowteach.ru/trainer/media/spotlight7/tan.webp'),
('guard','','https://app.wowteach.ru/trainer/media/spotlight7/guard.webp','https://app.wowteach.ru/trainer/media/spotlight7/guard.webp'),
('guide','','https://app.wowteach.ru/trainer/media/spotlight7/guide.webp','https://app.wowteach.ru/trainer/media/spotlight7/guide.webp'),
('shake hands with','','https://app.wowteach.ru/trainer/media/spotlight7/shake_hands.webp','https://app.wowteach.ru/trainer/media/spotlight7/shake_hands.webp'),
('crayon','','https://app.wowteach.ru/trainer/media/spotlight7/crayon.webp','https://app.wowteach.ru/trainer/media/spotlight7/crayon.webp'),
('wrist','','https://app.wowteach.ru/trainer/media/spotlight7/wrist.webp','https://app.wowteach.ru/trainer/media/spotlight7/wrist.webp'),
('MP3 music player','','https://app.wowteach.ru/trainer/media/spotlight7/MP3_player.webp','https://app.wowteach.ru/trainer/media/spotlight7/MP3_player.webp'),
('digital music player (MP3)','','https://app.wowteach.ru/trainer/media/spotlight7/digital_music_player.webp','https://app.wowteach.ru/trainer/media/spotlight7/digital_music_player.webp')) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND (f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 7' AND deleted_at IS NULL)
       OR f.parent_folder_id IN (SELECT id FROM deck_folders WHERE parent_folder_id =
           (SELECT id FROM deck_folders WHERE title = 'Spotlight 7' AND deleted_at IS NULL)))  -- подпапки «Другие слова»
  AND (v.k = '' OR w.translation = v.k)
RETURNING w.id;