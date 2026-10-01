# -*- coding: utf-8 -*-
"""SM2 · Final Test — отдельный юнит с одним уроком."""
import os
import u_lib as L
from u_lib import Lesson, url, simg, img

L.setup('Final Test', 10, 'sm2/u9')
OUT = 'finalsql'

AUDIO = ('Ссылка на аудио', 'блок «Видео/аудио» пустой',
         'в выгрузке медиафайла нет — платформа его не отдаёт')

t = Lesson('Final Test', 'Итоговый тест за курс Super Minds 2', 0,
           kind='test', threshold=90)

t.text('<h2>Super Minds 2 · Final Test</h2>'
       '<p>Это итоговый тест за весь курс. Не торопись, читай задания внимательно — '
       'у теста высокий проходной балл.</p>'
       '<p>Удачи! 🍀</p>')

t.text(img('banner_listen', 200) + '<h3>LISTENING</h3>'
       '<p>Послушай аудио и выполни задание ниже.</p>',
       'баннер «Listening» из выгрузки')

t.add('video', {'title': 'Аудио к заданию «Соедини человека с картинкой»', 'url': '@@MEDIA@@sm2/u9/sm2_final_b3.mp3', 'provider': 'file'},
      'медиафайл прислала методист')

t.add('match', {'title': 'Послушай аудио и соедини человека с картинкой',
                'pairs': [
                    {'left': 'her parents', 'left_audio_tts': 'her parents',
                     'right_image': url('fam_parents'), 'right': 'её родители'},
                    {'left': 'her son', 'left_audio_tts': 'her son',
                     'right_image': url('fam_son'), 'right': 'её сын'},
                    {'left': 'her daughter', 'left_audio_tts': 'her daughter',
                     'right_image': url('fam_daughter'), 'right': 'её дочь'},
                    {'left': 'her uncle', 'left_audio_tts': 'her uncle',
                     'right_image': url('fam_uncle'), 'right': 'её дядя'},
                    {'left': 'her brother', 'left_audio_tts': 'her brother',
                     'right_image': url('fam_brother'), 'right': 'её брат'},
                    {'left': 'her cousin', 'left_audio_tts': 'her cousin',
                     'right_image': url('fam_cousin'), 'right': 'её двоюродная сестра'}]},
      'в выгрузке правая колонка пустая — картинки нарисовала методист')

t.text(img('banner_read') + '<h3>READING & WRITING</h3>')

t.add('match', {'title': 'Соедини слово с его значением', 'pairs': [
    {'left': 'BOOKCASE', 'left_audio_tts': 'bookcase',
     'right': 'You can keep books there.'},
    {'left': 'MONKEY', 'left_audio_tts': 'monkey',
     'right': 'This is a kind of animal. It likes bananas.'},
    {'left': 'CINEMA', 'left_audio_tts': 'cinema',
     'right': 'You can watch films there.'},
    {'left': 'WARDROBE', 'left_audio_tts': 'wardrobe',
     'right': 'You can keep clothes there.'},
    {'left': 'EYES', 'left_audio_tts': 'eyes',
     'right': 'There are two of them on the face. We can see with them.'},
    {'left': 'PLANE', 'left_audio_tts': 'plane',
     'right': 'It is a kind of transport. You can fly on it.'}]},
      'в выгрузке опечатка «We can see with it» — исправил на with them')

t.add('gaps', {'title': 'Посмотри на картинку и впиши ответ', 'mode': 'drag',
               'image': url('yard_scene'),
               'text': "1. The boy is riding a __bike__.\n"
                       "2. The dog is learning to __swim__.\n"
                       "3. There is one table and a __chair__ in the yard.\n"
                       "4. Is there __any__ orange juice in the picture?\n"
                       "5. Children are playing in the __playground__."},
      'к первому пропуску в выгрузке указан альтернативный ответ «bicycle»')

t.text(simg('good_luck_clover') +
       '<p>Это конец итогового теста. Ты прошёл весь курс Super Minds 2 — '
       'это большая работа. Молодец! 🎉</p>')

LESSONS = [t]

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for i, les in enumerate(LESSONS):
        fn = f'{OUT}/{i:02d}_final_test.sql'
        open(fn, 'w').write(les.sql())
        print(f'{fn}: {len(les.blocks)} блоков')
