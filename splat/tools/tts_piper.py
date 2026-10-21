"""Озвучка слов Splat-проекта через Piper — тем же голосом, что в курсах (en_US-amy, как tts/tts_server.py).

python3 splat/tools/tts_piper.py <папка с моделями>
  → splat/audio/<слово>.mp3 (amy) и scratch-страница прослушивания со всеми голосами.
Модели: huggingface.co/rhasspy/piper-voices, *-medium.onnx (+ .onnx.json).
"""
import base64, os, subprocess, sys, tempfile

WORDS = ['tooth', 'toothbrush', 'toothpaste', 'cup']
VOICES = ['en_US-amy', 'en_US-ryan', 'en_GB-alba', 'en_GB-alan']  # первый — основной
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


def synth(text, model):
    with tempfile.TemporaryDirectory() as tmp:
        wav, mp3 = os.path.join(tmp, 'o.wav'), os.path.join(tmp, 'o.mp3')
        subprocess.run(['piper', '-m', model, '-f', wav], input=text.encode(), check=True, capture_output=True)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav, '-b:a', '96k', mp3], check=True)
        return open(mp3, 'rb').read()


def main(models, page):
    out = os.path.join(ROOT, 'audio')
    os.makedirs(out, exist_ok=True)
    rows = []
    for w in WORDS:
        cells = []
        for i, v in enumerate(VOICES):
            data = synth(w, os.path.join(models, v + '-medium.onnx'))
            if i == 0:
                open(os.path.join(out, w + '.mp3'), 'wb').write(data)
            src = 'data:audio/mpeg;base64,' + base64.b64encode(data).decode()
            cells.append(f'<td><button onclick="new Audio(\'{src}\').play()">▶</button></td>')
        rows.append(f'<tr><th>{w}</th>{"".join(cells)}</tr>')
    head = ''.join(f'<th>{v}{" (основной)" if i == 0 else ""}</th>' for i, v in enumerate(VOICES))
    open(page, 'w').write(f'''<!doctype html><meta charset="utf-8"><title>Splat — слова на прослушивание</title>
<style>body{{font-family:sans-serif;padding:16px}}table{{border-collapse:collapse}}td,th{{border:1px solid #ccc;padding:8px 14px;text-align:center}}
button{{font-size:22px;border:none;background:#33c7b0;color:#fff;border-radius:50%;width:48px;height:48px;cursor:pointer}}</style>
<h2>Splat Kids — слова урока</h2><p>Основной голос — как в курсах (amy). Если слово звучит плохо — напишите, какой голос взять.</p>
<table><tr><th>слово</th>{head}</tr>{"".join(rows)}</table>''')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
