UPDATE words w SET image_url = v.u
FROM (VALUES
('scuba diving','','https://app.wowteach.ru/trainer/media/spotlight5/scuba_diving.webp','https://app.wowteach.ru/trainer/media/spotlight5/scuba_diving.webp'),
('white water rafting','','https://app.wowteach.ru/trainer/media/spotlight5/white_water_rafting.webp','https://app.wowteach.ru/trainer/media/spotlight5/white_water_rafting.webp'),
('abbreviation','','https://app.wowteach.ru/trainer/media/spotlight5/abbreviation.webp','https://app.wowteach.ru/trainer/media/spotlight5/abbreviation.webp'),
('health matters','','https://app.wowteach.ru/trainer/media/spotlight5/health_matters.webp','https://app.wowteach.ru/trainer/media/spotlight5/health_matters.webp'),
('reception','','https://app.wowteach.ru/trainer/media/spotlight5/reception.webp','https://app.wowteach.ru/trainer/media/spotlight5/reception.webp'),
('sunburn','','https://app.wowteach.ru/trainer/media/spotlight5/sunburn.webp','https://app.wowteach.ru/trainer/media/spotlight5/sunburn.webp'),
('put lotion','','https://app.wowteach.ru/trainer/media/spotlight5/put_lotion.webp','https://app.wowteach.ru/trainer/media/spotlight5/put_lotion.webp'),
('see a doctor','','https://app.wowteach.ru/trainer/media/spotlight5/see_a_doctor.webp','https://app.wowteach.ru/trainer/media/spotlight5/see_a_doctor.webp'),
('stay out of the sun','','https://app.wowteach.ru/trainer/media/spotlight5/stay_out_of_the_sun.webp','https://app.wowteach.ru/trainer/media/spotlight5/stay_out_of_the_sun.webp'),
('flat tyre','','https://app.wowteach.ru/trainer/media/spotlight5/flat_tyre.webp','https://app.wowteach.ru/trainer/media/spotlight5/flat_tyre.webp'),
('scenic','','https://app.wowteach.ru/trainer/media/spotlight5/scenic.webp','https://app.wowteach.ru/trainer/media/spotlight5/scenic.webp'),
('sit back','','https://app.wowteach.ru/trainer/media/spotlight5/sit_back.webp','https://app.wowteach.ru/trainer/media/spotlight5/sit_back.webp'),
('miss a turn','','https://app.wowteach.ru/trainer/media/spotlight5/miss_a_turn.webp','https://app.wowteach.ru/trainer/media/spotlight5/miss_a_turn.webp'),
('kind','','https://app.wowteach.ru/trainer/media/spotlight5/kind_type.webp','https://app.wowteach.ru/trainer/media/spotlight5/kind_type.webp'),
('ordinary','','https://app.wowteach.ru/trainer/media/spotlight5/ordinary.webp','https://app.wowteach.ru/trainer/media/spotlight5/ordinary.webp'),
('reasonable','','https://app.wowteach.ru/trainer/media/spotlight5/reasonable.webp','https://app.wowteach.ru/trainer/media/spotlight5/reasonable.webp'),
('rent','','https://app.wowteach.ru/trainer/media/spotlight5/rent.webp','https://app.wowteach.ru/trainer/media/spotlight5/rent.webp')) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 5' AND deleted_at IS NULL)
  AND (v.k = '' OR d.title LIKE v.k || ' %')
RETURNING w.id;