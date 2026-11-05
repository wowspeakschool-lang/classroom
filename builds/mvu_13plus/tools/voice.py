"""Голосовые сообщения «Quest Master» через Yandex SpeechKit (ключ подставляет прокси).
Предложения синтезируются по одному, между ними пауза 0.8 с. → scratchpad/audio/<name>.mp3
python3 builds/mvu_13plus/tools/voice.py <outdir>"""
import sys, os, re, subprocess, requests
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import data
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
def synth(text, path):
    r = requests.post('https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize',
                      headers={'Authorization': 'Api-Key dummy'},
                      data={'text': text, 'lang': 'en-US', 'voice': 'john', 'format': 'mp3', 'speed': '0.9'}, timeout=60)
    r.raise_for_status(); open(path, 'wb').write(r.content)
for part in (data.P1, data.P2, data.P3):
    for o in part:
        for t in o['tasks']:
            if t['kind'] != 'listen':
                continue
            sents = re.split(r'(?<=[.!?])\s+', t['text'].strip())
            parts = []
            for i, s in enumerate(sents):
                p = f'{OUT}/_{t["audio"]}_{i}.mp3'; synth(s, p); parts.append(p)
            sil = f'{OUT}/_sil.mp3'
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=mono', '-t', '0.8', '-b:a', '64k', sil], check=True)
            lst = f'{OUT}/_list.txt'
            open(lst, 'w').write(''.join(f"file '{p}'\nfile '{sil}'\n" for p in parts))
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst,
                            '-ar', '48000', '-ac', '1', '-b:a', '64k', f'{OUT}/{t["audio"]}.mp3'], check=True)
            for p in parts: os.remove(p)
            print(t['audio'], len(sents), 'sentences')
