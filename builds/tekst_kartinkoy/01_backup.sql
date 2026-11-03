-- Копия блоков до переборки текста, свёрстанного картинкой (03.11.2026, чат GG/SM3)
insert into classroom_backup_tekst_kartinkoy_20261103 (id, lesson_id, type, payload, sort_order, note)
select b.id, b.lesson_id, b.type, b.payload, b.sort_order, 'gg1-gg3/sm3: tekst kartinkoy'
from classroom_blocks b
where b.id in (
  '73d50a2c-9dfc-4151-a38a-f15cc78bfc1f',  -- gg2 u8 hw5 b2  book_running_poster
  'ee45e228-2b82-4e1b-92ec-59c56c8107e4',  -- gg2 u3 hw5 b9  book_penny_diary
  'db36599e-b046-4df7-aa79-fa96249d5829',  -- gg2 u4 hw5 b2  book_school_records
  'f1ce56d2-baf5-4b03-bf58-45093364e26f',  -- sm3 u4 hw4 b9  postcard_ali
  '85bd3f3e-6f8c-4410-b3c1-58be41bab6c1',  -- sm3 u4 hw6 b2  dialog_paul_daisy_1
  'b00eb912-fbe5-4624-bcda-9381bbf005a8',  -- sm3 u4 hw6 b3  dialog_paul_daisy_2
  '264913d5-4a88-4773-b625-b10fe44bd5c1',  -- sm3 u5 hw8 b2  reading_megalodon
  '2cc2c6b0-3b1b-4de6-a6c3-301362750416',  -- sm3 u5 hw8 b9  project_turtles
  '831eabb4-9e01-4365-9101-8ef290f9bd07',  -- sm3 u7 hw7 b2  reading_keep_healthy
  'e3991284-8415-40ae-8f5a-5db9dffdfdf4',  -- sm3 u8 hw5 b6  reading_food_culture
  '9988528f-2f5f-4a1c-adf1-4e00f6f7ccc5',  -- sm3 u8 hw7 b2  reading_wonders_1..3
  '3a5f2af3-9be3-4f7a-bc93-f34e3dc97513',  -- sm3 u9 hw7 b3  reading_100_years
  'b6cb7a57-77a4-4506-9a01-2568a74f523b'   -- sm3 ft b9      reading_jim_story
)
and not exists (select 1 from classroom_backup_tekst_kartinkoy_20261103 t where t.id = b.id);
