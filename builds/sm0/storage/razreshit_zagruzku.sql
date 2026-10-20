-- Открыть загрузку в бакет classroom-media, папка sm0/, на время заливки четырёх
-- записей историй SM0 (Track 6, 39, 66, 83).
-- Запускать в Supabase → SQL Editor: через MCP не проходит, нет прав владельца
-- таблицы storage.objects.
--
-- Политика tmp_halloween_music_insert осталась с заливки музыки Halloween и
-- сейчас обезврежена (with check false). Переименовываем её в нейтральное имя
-- и переиспользуем, чтобы не плодить политики: удалить их всё равно можно
-- только руками.

alter policy "tmp_halloween_music_insert" on storage.objects
  rename to tmp_upload_insert;

alter policy tmp_upload_insert on storage.objects
  with check (
    bucket_id = 'classroom-media'
    and (storage.foldername(name))[1] = 'sm0'
  );
