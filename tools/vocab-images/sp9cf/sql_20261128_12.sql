with recursive t as (select id from deck_folders where title='Spotlight 9' and deleted_at is null
 union all select f.id from deck_folders f join t on f.parent_folder_id=t.id where f.deleted_at is null),
u as (update words w set image_url=v.u from (values
('bonfire','костер','https://app.wowteach.ru/trainer/media/spotlight9/bonfire.webp'),
('burst','лопать(ся)','https://app.wowteach.ru/trainer/media/spotlight9/burst.webp'),
('change of clothes','сменная одежда','https://app.wowteach.ru/trainer/media/spotlight9/change_of_clothes.webp'),
('enter','зд. принять участие','https://app.wowteach.ru/trainer/media/spotlight9/enter.webp'),
('enter','принимать участие','https://app.wowteach.ru/trainer/media/spotlight9/enter.webp'),
('fancy dress costume','маскарадный костюм','https://app.wowteach.ru/trainer/media/spotlight9/fancy_dress_costume.webp'),
('farewell','прощание','https://app.wowteach.ru/trainer/media/spotlight9/farewell.webp'),
('final','завершающий, конечный, последний','https://app.wowteach.ru/trainer/media/spotlight9/final.webp')) v(term,tr,u), word_decks d
where w.deck_id=d.id and d.deleted_at is null and d.folder_id in (select id from t) and w.term=v.term and w.translation=v.tr and w.image_url is null returning 1)
select count(*) from u;
