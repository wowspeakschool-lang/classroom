UPDATE words w SET image_url = v.u
FROM (VALUES
('Stirling','','https://app.wowteach.ru/trainer/media/spotlight5/Stirling.webp','https://app.wowteach.ru/trainer/media/spotlight5/Stirling.webp'),
('Agra','','https://app.wowteach.ru/trainer/media/spotlight5/Agra.webp','https://app.wowteach.ru/trainer/media/spotlight5/Agra.webp'),
('Ballater','','https://app.wowteach.ru/trainer/media/spotlight5/Ballater.webp','https://app.wowteach.ru/trainer/media/spotlight5/Ballater.webp'),
('Barranquilla','','https://app.wowteach.ru/trainer/media/spotlight5/Barranquilla.webp','https://app.wowteach.ru/trainer/media/spotlight5/Barranquilla.webp'),
('Cork','','https://app.wowteach.ru/trainer/media/spotlight5/Cork.webp','https://app.wowteach.ru/trainer/media/spotlight5/Cork.webp'),
('Oban','','https://app.wowteach.ru/trainer/media/spotlight5/Oban.webp','https://app.wowteach.ru/trainer/media/spotlight5/Oban.webp'),
('Springfield','','https://app.wowteach.ru/trainer/media/spotlight5/Springfield.webp','https://app.wowteach.ru/trainer/media/spotlight5/Springfield.webp'),
('Surrey','','https://app.wowteach.ru/trainer/media/spotlight5/Surrey.webp','https://app.wowteach.ru/trainer/media/spotlight5/Surrey.webp'),
('Northern India','','https://app.wowteach.ru/trainer/media/spotlight5/Northern_India.webp','https://app.wowteach.ru/trainer/media/spotlight5/Northern_India.webp'),
('South Asia','','https://app.wowteach.ru/trainer/media/spotlight5/South_Asia.webp','https://app.wowteach.ru/trainer/media/spotlight5/South_Asia.webp'),
('Southwest Alaska','','https://app.wowteach.ru/trainer/media/spotlight5/Southwest_Alaska.webp','https://app.wowteach.ru/trainer/media/spotlight5/Southwest_Alaska.webp'),
('the River Stirling','','https://app.wowteach.ru/trainer/media/spotlight5/the_River_Stirling.webp','https://app.wowteach.ru/trainer/media/spotlight5/the_River_Stirling.webp'),
('Forth','','https://app.wowteach.ru/trainer/media/spotlight5/Forth.webp','https://app.wowteach.ru/trainer/media/spotlight5/Forth.webp'),
('Dona Lola','','https://app.wowteach.ru/trainer/media/spotlight5/Dona_Lola.webp','https://app.wowteach.ru/trainer/media/spotlight5/Dona_Lola.webp'),
('St George Island','','https://app.wowteach.ru/trainer/media/spotlight5/St_George_Island.webp','https://app.wowteach.ru/trainer/media/spotlight5/St_George_Island.webp'),
('St Lawrence Island','','https://app.wowteach.ru/trainer/media/spotlight5/St_Lawrence_Island.webp','https://app.wowteach.ru/trainer/media/spotlight5/St_Lawrence_Island.webp'),
('St Matthew Island','','https://app.wowteach.ru/trainer/media/spotlight5/St_Matthew_Island.webp','https://app.wowteach.ru/trainer/media/spotlight5/St_Matthew_Island.webp'),
('St Paul Island','','https://app.wowteach.ru/trainer/media/spotlight5/St_Paul_Island.webp','https://app.wowteach.ru/trainer/media/spotlight5/St_Paul_Island.webp'),
('Nunivak Island','','https://app.wowteach.ru/trainer/media/spotlight5/Nunivak_Island.webp','https://app.wowteach.ru/trainer/media/spotlight5/Nunivak_Island.webp'),
('Kiska Island','','https://app.wowteach.ru/trainer/media/spotlight5/Kiska_Island.webp','https://app.wowteach.ru/trainer/media/spotlight5/Kiska_Island.webp'),
('Kodiak Island','','https://app.wowteach.ru/trainer/media/spotlight5/Kodiak_Island.webp','https://app.wowteach.ru/trainer/media/spotlight5/Kodiak_Island.webp'),
('Pribilof Islands','','https://app.wowteach.ru/trainer/media/spotlight5/Pribilof_Islands.webp','https://app.wowteach.ru/trainer/media/spotlight5/Pribilof_Islands.webp'),
('Aleutian Islands','','https://app.wowteach.ru/trainer/media/spotlight5/Aleutian_Islands.webp','https://app.wowteach.ru/trainer/media/spotlight5/Aleutian_Islands.webp')) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 5' AND deleted_at IS NULL)
  AND (v.k = '' OR d.title LIKE v.k || ' %')
RETURNING w.id;