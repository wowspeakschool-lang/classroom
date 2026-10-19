# Halloween (курс Holidays → юнит Halloween)

- `lessons/halloween/*.html` — интерактивные уроки по возрастам; картинки в `media/halloween/<возраст>/`,
  музыка в Supabase Storage `classroom-media/halloween/`.
- `externalize.py` — выносит вшитые base64-картинки и музыку из собранного урока в файлы и ссылки.
- `hwdb_build.py` — планы уроков (`kind='lesson'`) и домашки (`kind='homework'`) → `sql/*.sql`.
  Сами уроки собираются скриптами в скретчпаде сессии (build.py, build7.py, build10.py, build13.py).
