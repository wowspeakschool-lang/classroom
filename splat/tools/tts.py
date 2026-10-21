"""Озвучка Splat-проекта через Yandex SpeechKit (ключ подставляет прокси).

python3 splat/tools/tts.py          — синтезирует недостающие файлы в splat/audio/
Имена файлов — ключи словаря; уже существующие не перезаписываются.
"""
import os, sys, urllib.parse, urllib.request

OUT = os.path.join(os.path.dirname(__file__), '..', 'audio')
URL = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'

EN = {  # английский голос — слова и фразы урока
    'w_tooth': 'tooth', 'w_teeth': 'teeth', 'w_toothbrush': 'toothbrush',
    'w_toothpaste': 'toothpaste', 'w_water': 'water', 'w_cup': 'cup',
    'w_smile': 'smile', 'w_brush': 'brush', 'w_clean': 'clean',
    'w_fairy': 'Tooth Fairy', 'w_castle': 'castle', 'w_germ': 'germ',
    'p_hello': 'Hello!', 'p_bye': 'Goodbye!', 'p_goodjob': 'Good job!',
    'p_wow': 'Wow! Super!', 'p_tryagain': 'Try again!',
    'p_brushteeth': 'Brush your teeth!', 'p_updown': 'Up and down, up and down!',
    'p_roundround': 'Round and round, round and round!',
    'p_bigsmile': 'Big smile!', 'p_clean': 'Clean teeth! Shiny teeth!',
    'p_where': 'Where is the toothbrush?', 'p_whatisit': 'What is it?',
    'p_count': 'One, two, three, four, five!',
    'chant': 'Brush, brush, brush your teeth. Up and down, up and down. '
             'Brush, brush, brush your teeth. Round and round, round and round. '
             'Brush, brush, brush your teeth. Big, big smile!',
}
RU = {  # русский голос — подсказки тренажёра для детей, которые ещё не читают
    'r_welcome': 'Привет! Это Зубной замок Сплат Кидс. Нажми «Играть» — и полетели!',
    'r_menu': 'Выбирай игру!',
    'r_brush': 'Почисти зубки! Води щёткой по микробам, пока зубки не заблестят.',
    'r_memory': 'Найди пары! Открывай карточки и ищи одинаковые.',
    'r_listen': 'Послушай слово и нажми на правильную картинку.',
    'r_timer': 'Чистим зубки две минуты вместе! Нажми на щётку, чтобы начать.',
    'r_timer_end': 'Ура! Две минуты прошли. Зубки чистые и блестят!',
    'r_challenge': 'Семь дней чистим зубки и учим слова. Каждый день — новая звёздочка!',
    'r_star': 'Звёздочка твоя! До завтра!',
    'r_win': 'Молодец! Ты справился!',
}

def synth(text, lang, voice):
    data = {'text': text, 'lang': lang, 'voice': voice, 'format': 'mp3', 'speed': '0.9'}
    if os.environ.get('YANDEX_FOLDER_ID'):
        data['folderId'] = os.environ['YANDEX_FOLDER_ID']
    req = urllib.request.Request(URL, urllib.parse.urlencode(data).encode())
    return urllib.request.urlopen(req, timeout=60).read()

def main():
    os.makedirs(OUT, exist_ok=True)
    jobs = [(k, v, 'en-US', 'john') for k, v in EN.items()] + \
           [(k, v, 'ru-RU', 'alena') for k, v in RU.items()]
    for name, text, lang, voice in jobs:
        path = os.path.join(OUT, name + '.mp3')
        if os.path.exists(path):
            continue
        open(path, 'wb').write(synth(text, lang, voice))
        print('ok', name)

if __name__ == '__main__':
    sys.exit(main())
