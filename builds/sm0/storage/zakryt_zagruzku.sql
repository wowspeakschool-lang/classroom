-- Закрыть загрузку сразу после того, как мы сообщим, что файлы залиты.
-- Политика остаётся на месте, но ничего не разрешает.

alter policy tmp_upload_insert on storage.objects
  with check (false);
