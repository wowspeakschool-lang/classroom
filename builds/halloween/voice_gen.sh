#!/bin/sh
# Слова для уроков 10–12 и 13+, которых нет в домашках: тот же голос, что на сервере озвучки
# (tts/tts_server.py: Piper en_US-amy-medium, ffmpeg -b:a 96k). Кладёт mp3 в piper/out рядом с externalize.py.
# pip install piper-tts; модель: huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/
mkdir -p piper/out
for w in "a golden pumpkin" zombie pirate superhero bonfires costumes ghosts; do
  f=$(echo "$w" | sed 's/^a //; s/ /_/g')
  echo "$w" | python3 -m piper -m piper/en_US-amy-medium.onnx -f piper/out/$f.wav
  ffmpeg -y -loglevel error -i piper/out/$f.wav -b:a 96k piper/out/hw_voice_$f.mp3
done
