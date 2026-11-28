with recursive t as (select id from deck_folders where title='Spotlight 9' and deleted_at is null
 union all select f.id from deck_folders f join t on f.parent_folder_id=t.id where f.deleted_at is null),
u as (update words w set image_url=v.u from (values
('contest','соревнование','https://app.wowteach.ru/trainer/media/spotlight9/contest.webp'),
('pirate','пират','https://app.wowteach.ru/trainer/media/spotlight9/pirate.webp'),
('rowing boat','гребная лодка','https://app.wowteach.ru/trainer/media/spotlight9/rowing_boat.webp'),
('strong','зд. устоявшийся','https://app.wowteach.ru/trainer/media/spotlight9/strong.webp'),
('symbolise','символизировать','https://app.wowteach.ru/trainer/media/spotlight9/symbolise.webp'),
('transform','изменять, преобразовывать','https://app.wowteach.ru/trainer/media/spotlight9/transform.webp'),
('bright idea','умная мысль или предложение','https://app.wowteach.ru/trainer/media/spotlight9/bright_idea.webp'),
('colourful street parade','красочный (уличный) парад','https://app.wowteach.ru/trainer/media/spotlight9/colourful_street_parade.webp'),
('cooking contest','кулинарный конкурс','https://app.wowteach.ru/trainer/media/spotlight9/cooking_contest.webp'),
('enter a competition','принять участие в соревновании','https://app.wowteach.ru/trainer/media/spotlight9/enter_a_competition.webp'),
('fireworks display','фейерверк, салют','https://app.wowteach.ru/trainer/media/spotlight9/fireworks_display.webp'),
('raise money for charity','собирать деньги на благотворительность','https://app.wowteach.ru/trainer/media/spotlight9/raise_money_for_charity.webp'),
('spare change of clothes','запасная сменная одежда','https://app.wowteach.ru/trainer/media/spotlight9/spare_change_of_clothes.webp'),
('strong tradition','устоявшаяся традиция','https://app.wowteach.ru/trainer/media/spotlight9/strong_tradition.webp'),
('a load of rubbish','чепуха, ерунда','https://app.wowteach.ru/trainer/media/spotlight9/a_load_of_rubbish.webp'),
('attention','внимание','https://app.wowteach.ru/trainer/media/spotlight9/attention.webp'),
('coincidence','совпадение','https://app.wowteach.ru/trainer/media/spotlight9/coincidence.webp'),
('four-leaf clover','четырехлистный клевер','https://app.wowteach.ru/trainer/media/spotlight9/four_leaf_clover.webp'),
('full moon','полная луна, полнолуние','https://app.wowteach.ru/trainer/media/spotlight9/full_moon.webp'),
('old wives'' tale','бабушкины сказки','https://app.wowteach.ru/trainer/media/spotlight9/old_wives_tale.webp'),
('on one''s mind','все время думать о чем-либо','https://app.wowteach.ru/trainer/media/spotlight9/on_one_s_mind.webp'),
('pass one''s exams','сдать экзамены','https://app.wowteach.ru/trainer/media/spotlight9/pass_one_s_exams.webp'),
('reassure','успокаивать, утешать','https://app.wowteach.ru/trainer/media/spotlight9/reassure.webp')) v(term,tr,u), word_decks d
where w.deck_id=d.id and d.deleted_at is null and d.folder_id in (select id from t) and w.term=v.term and w.translation=v.tr and w.image_url is null returning 1)
select count(*) from u;
