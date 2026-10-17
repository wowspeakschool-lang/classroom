UPDATE words w SET image_url = v.u
FROM (VALUES
('sign','','https://app.wowteach.ru/trainer/media/spotlight5/sign.webp','https://app.wowteach.ru/trainer/media/spotlight5/sign.webp'),
('per day','','https://app.wowteach.ru/trainer/media/spotlight5/per_day.webp','https://app.wowteach.ru/trainer/media/spotlight5/per_day.webp'),
('bottled water','','https://app.wowteach.ru/trainer/media/spotlight5/bottled_water.webp','https://app.wowteach.ru/trainer/media/spotlight5/bottled_water.webp'),
('leaflet','','https://app.wowteach.ru/trainer/media/spotlight5/leaflet.webp','https://app.wowteach.ru/trainer/media/spotlight5/leaflet.webp'),
('Africa','','https://app.wowteach.ru/trainer/media/spotlight5/Africa.webp','https://app.wowteach.ru/trainer/media/spotlight5/Africa.webp'),
('America','','https://app.wowteach.ru/trainer/media/spotlight5/America.webp','https://app.wowteach.ru/trainer/media/spotlight5/America.webp'),
('Antarctica','','https://app.wowteach.ru/trainer/media/spotlight5/Antarctica.webp','https://app.wowteach.ru/trainer/media/spotlight5/Antarctica.webp'),
('Asia','','https://app.wowteach.ru/trainer/media/spotlight5/Asia.webp','https://app.wowteach.ru/trainer/media/spotlight5/Asia.webp'),
('Europe','','https://app.wowteach.ru/trainer/media/spotlight5/Europe.webp','https://app.wowteach.ru/trainer/media/spotlight5/Europe.webp'),
('North America','','https://app.wowteach.ru/trainer/media/spotlight5/North_America.webp','https://app.wowteach.ru/trainer/media/spotlight5/North_America.webp'),
('South America','','https://app.wowteach.ru/trainer/media/spotlight5/South_America.webp','https://app.wowteach.ru/trainer/media/spotlight5/South_America.webp'),
('Belfast','','https://app.wowteach.ru/trainer/media/spotlight5/Belfast.webp','https://app.wowteach.ru/trainer/media/spotlight5/Belfast.webp'),
('Canberra','','https://app.wowteach.ru/trainer/media/spotlight5/Canberra.webp','https://app.wowteach.ru/trainer/media/spotlight5/Canberra.webp'),
('Dublin','','https://app.wowteach.ru/trainer/media/spotlight5/Dublin.webp','https://app.wowteach.ru/trainer/media/spotlight5/Dublin.webp'),
('Edinburgh','','https://app.wowteach.ru/trainer/media/spotlight5/Edinburgh.webp','https://app.wowteach.ru/trainer/media/spotlight5/Edinburgh.webp'),
('Glasgow','','https://app.wowteach.ru/trainer/media/spotlight5/Glasgow.webp','https://app.wowteach.ru/trainer/media/spotlight5/Glasgow.webp'),
('New York City','','https://app.wowteach.ru/trainer/media/spotlight5/New_York_City.webp','https://app.wowteach.ru/trainer/media/spotlight5/New_York_City.webp'),
('Ottawa','','https://app.wowteach.ru/trainer/media/spotlight5/Ottawa.webp','https://app.wowteach.ru/trainer/media/spotlight5/Ottawa.webp'),
('St Andrews','','https://app.wowteach.ru/trainer/media/spotlight5/St_Andrews.webp','https://app.wowteach.ru/trainer/media/spotlight5/St_Andrews.webp'),
('Washington DC','','https://app.wowteach.ru/trainer/media/spotlight5/Washington_DC.webp','https://app.wowteach.ru/trainer/media/spotlight5/Washington_DC.webp'),
('Wellington','','https://app.wowteach.ru/trainer/media/spotlight5/Wellington.webp','https://app.wowteach.ru/trainer/media/spotlight5/Wellington.webp'),
('York','','https://app.wowteach.ru/trainer/media/spotlight5/York.webp','https://app.wowteach.ru/trainer/media/spotlight5/York.webp'),
('Alaska','','https://app.wowteach.ru/trainer/media/spotlight5/Alaska.webp','https://app.wowteach.ru/trainer/media/spotlight5/Alaska.webp'),
('Colombia','','https://app.wowteach.ru/trainer/media/spotlight5/Colombia.webp','https://app.wowteach.ru/trainer/media/spotlight5/Colombia.webp'),
('(Great) Britain','','https://app.wowteach.ru/trainer/media/spotlight5/Great_Britain.webp','https://app.wowteach.ru/trainer/media/spotlight5/Great_Britain.webp'),
('Bering Sea','','https://app.wowteach.ru/trainer/media/spotlight5/Bering_Sea.webp','https://app.wowteach.ru/trainer/media/spotlight5/Bering_Sea.webp'),
('Loch Ness','','https://app.wowteach.ru/trainer/media/spotlight5/Loch_Ness.webp','https://app.wowteach.ru/trainer/media/spotlight5/Loch_Ness.webp'),
('Mallorca','','https://app.wowteach.ru/trainer/media/spotlight5/Mallorca.webp','https://app.wowteach.ru/trainer/media/spotlight5/Mallorca.webp'),
('Mount Kilimanjaro','','https://app.wowteach.ru/trainer/media/spotlight5/Kilimanjaro.webp','https://app.wowteach.ru/trainer/media/spotlight5/Kilimanjaro.webp'),
('Pacific Ocean','','https://app.wowteach.ru/trainer/media/spotlight5/Pacific_Ocean.webp','https://app.wowteach.ru/trainer/media/spotlight5/Pacific_Ocean.webp')) AS v(t, k, u, o), word_decks d, deck_folders f
WHERE w.term = v.t AND (w.image_url IS NULL OR w.image_url = v.o) AND w.image_url IS DISTINCT FROM v.u AND d.id = w.deck_id AND f.id = d.folder_id
  AND d.deleted_at IS NULL
  AND f.parent_folder_id = (SELECT id FROM deck_folders WHERE title = 'Spotlight 5' AND deleted_at IS NULL)
  AND (v.k = '' OR d.title LIKE v.k || ' %')
RETURNING w.id;