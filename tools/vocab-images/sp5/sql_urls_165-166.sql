UPDATE words w SET image_url = v.u
FROM (VALUES
('at ... o''clock','','https://app.wowteach.ru/trainer/media/spotlight5/at_seven_o_clock_v2.webp','https://app.wowteach.ru/trainer/media/spotlight5/at_seven_o_clock.webp'),
('at midnight/at night','','https://app.wowteach.ru/trainer/media/spotlight5/at_midnight_v2.webp','https://app.wowteach.ru/trainer/media/spotlight5/at_midnight.webp'),
('at noon','','https://app.wowteach.ru/trainer/media/spotlight5/at_noon_v2.webp','https://app.wowteach.ru/trainer/media/spotlight5/at_noon.webp'),
('half past seven','','https://app.wowteach.ru/trainer/media/spotlight5/half_past_seven_v2.webp','https://app.wowteach.ru/trainer/media/spotlight5/half_past_seven.webp'),
('quarter past seven','','https://app.wowteach.ru/trainer/media/spotlight5/quarter_past_seven_v2.webp','https://app.wowteach.ru/trainer/media/spotlight5/quarter_past_seven.webp'),
('quarter to seven','','https://app.wowteach.ru/trainer/media/spotlight5/quarter_to_seven_v2.webp','https://app.wowteach.ru/trainer/media/spotlight5/quarter_to_seven.webp'),
('hour hand','','https://app.wowteach.ru/trainer/media/spotlight5/hour_hand_v2.webp','https://app.wowteach.ru/trainer/media/spotlight5/hour_hand.webp'),
('minute hand','','https://app.wowteach.ru/trainer/media/spotlight5/minute_hand_v2.webp','https://app.wowteach.ru/trainer/media/spotlight5/minute_hand.webp'),
('See you at ... o''clock.','','https://app.wowteach.ru/trainer/media/spotlight5/See_you_at_six_v2.webp','https://app.wowteach.ru/trainer/media/spotlight5/See_you_at_six.webp'),
('tonight','','https://app.wowteach.ru/trainer/media/spotlight5/tonight_v2.webp','https://app.wowteach.ru/trainer/media/spotlight5/tonight.webp')) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 5' AND deleted_at IS NULL)
  AND (v.k = '' OR d.title LIKE v.k || ' %')
RETURNING w.id;