#!/usr/bin/env python3
"""
Синтез речи для classroom.wowteach.ru.
Слушает только localhost; наружу выходит через Nginx.

Запрос:
    POST /tts
    Authorization: Bearer <токен пользователя Supabase>
    {"text": "mouth", "voice": "en_US-amy"}

Ответ: аудио (audio/mpeg или audio/wav).

Ключей и паролей не хранит. Право на озвучку проверяется у Supabase:
токен пользователя передаётся ему на проверку, свой сервисный ключ
здесь не нужен.
"""
import json
import os
import shutil
import subprocess
import tempfile
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VOICES_DIR = os.environ.get("PIPER_VOICES", "/opt/piper/voices")
PIPER_BIN = os.environ.get("PIPER_BIN", "piper")
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://vtcxghsqymwkyiogpndf.supabase.co")
SUPABASE_ANON = os.environ.get("SUPABASE_ANON_KEY", "")
PORT = int(os.environ.get("TTS_PORT", "8088"))
MAX_CHARS = 600

VOICES = {
    "en_US-amy":   "en_US-amy-medium.onnx",
    "en_US-ryan":  "en_US-ryan-medium.onnx",
    "en_GB-alba":  "en_GB-alba-medium.onnx",
    "en_GB-alan":  "en_GB-alan-medium.onnx",
}

HAS_FFMPEG = shutil.which("ffmpeg") is not None


def check_user(token: str) -> bool:
    """Токен действителен, если Supabase отдаёт по нему пользователя."""
    if not token or not SUPABASE_ANON:
        return False
    req = urllib.request.Request(
        SUPABASE_URL.rstrip("/") + "/auth/v1/user",
        headers={"Authorization": "Bearer " + token, "apikey": SUPABASE_ANON},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status == 200
    except Exception:
        return False


def synth(text: str, voice: str):
    model = os.path.join(VOICES_DIR, VOICES[voice])
    with tempfile.TemporaryDirectory() as tmp:
        wav = os.path.join(tmp, "out.wav")
        subprocess.run(
            [PIPER_BIN, "-m", model, "-f", wav],
            input=text.encode("utf-8"),
            check=True, capture_output=True, timeout=60,
        )
        if HAS_FFMPEG:
            mp3 = os.path.join(tmp, "out.mp3")
            subprocess.run(
                ["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-b:a", "96k", mp3],
                check=True, capture_output=True, timeout=60,
            )
            with open(mp3, "rb") as f:
                return f.read(), "audio/mpeg"
        with open(wav, "rb") as f:
            return f.read(), "audio/wav"


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _send(self, code, body=b"", ctype="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            self.wfile.write(body)

    def _err(self, code, msg):
        self._send(code, json.dumps({"error": msg}, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        if self.path == "/tts/health":
            missing = [v for v, f in VOICES.items()
                       if not os.path.exists(os.path.join(VOICES_DIR, f))]
            self._send(200, json.dumps({
                "ok": not missing,
                "voices": sorted(set(VOICES) - set(missing)),
                "missing": missing,
                "mp3": HAS_FFMPEG,
            }, ensure_ascii=False).encode("utf-8"))
        else:
            self._err(404, "not found")

    def do_POST(self):
        if self.path != "/tts":
            return self._err(404, "not found")

        auth = self.headers.get("Authorization", "")
        token = auth[7:].strip() if auth.lower().startswith("bearer ") else ""
        if not check_user(token):
            return self._err(401, "нужен вход в платформу")

        try:
            n = int(self.headers.get("Content-Length") or 0)
            data = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            return self._err(400, "неверный запрос")

        text = (data.get("text") or "").strip()
        voice = data.get("voice") or "en_US-amy"
        if not text:
            return self._err(400, "пустой текст")
        if len(text) > MAX_CHARS:
            return self._err(400, f"текст длиннее {MAX_CHARS} символов")
        if voice not in VOICES:
            return self._err(400, "неизвестный голос")

        try:
            audio, ctype = synth(text, voice)
        except subprocess.CalledProcessError as e:
            return self._err(500, (e.stderr or b"")[:300].decode("utf-8", "replace"))
        except Exception as e:
            return self._err(500, str(e)[:300])

        self._send(200, audio, ctype)

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
