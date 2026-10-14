#!/bin/bash
# Установка синтеза речи Piper на VPS. Запускать от root.
# Повторный прогон безопасен.
set -e

echo "== 1. Пакеты =="
apt-get update -qq
apt-get install -y python3-pip python3-venv ffmpeg curl

echo "== 2. Piper в отдельном окружении =="
mkdir -p /opt/piper/voices
python3 -m venv /opt/piper/venv
/opt/piper/venv/bin/pip install --upgrade pip -q
/opt/piper/venv/bin/pip install piper-tts -q

echo "== 3. Голоса =="
# Четыре: женский и мужской, американский и британский.
BASE="https://huggingface.co/rhasspy/piper-voices/resolve/main/en"
get () {  # get <путь> <имя файла>
  for ext in onnx onnx.json; do
    if [ ! -f "/opt/piper/voices/$2.$ext" ]; then
      echo "  качаю $2.$ext"
      curl -fsSL "$BASE/$1/$2.$ext" -o "/opt/piper/voices/$2.$ext"
    else
      echo "  $2.$ext уже есть"
    fi
  done
}
get "en_US/amy/medium"  "en_US-amy-medium"
get "en_US/ryan/medium" "en_US-ryan-medium"
get "en_GB/alba/medium" "en_GB-alba-medium"
get "en_GB/alan/medium" "en_GB-alan-medium"

echo "== 4. Проверка синтеза =="
echo "Listen and say" | /opt/piper/venv/bin/piper \
  -m /opt/piper/voices/en_US-amy-medium.onnx -f /tmp/tts_check.wav
ls -lh /tmp/tts_check.wav

echo
echo "Готово. Файл /tmp/tts_check.wav — пробная озвучка."
echo "Скачать к себе и послушать:"
echo "  scp root@217.198.9.78:/tmp/tts_check.wav ."
