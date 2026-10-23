# -*- coding: utf-8 -*-
"""Карта замены картинок SM0: старый файл из выгрузки → новая картинка.

Старые лежат в media/sm0/legacy (имена — хеши), новые в media/sm0/new.
Одна новая картинка закрывает по два-три старых дубля: в выгрузке один и тот же
предмет приходил разными файлами. Счётные картинки (звёзды, мячи, котики)
сверены пересчётом пятен, а не на глаз.
"""

MAP = {
    # части тела
    'ears': ['018bb90d821d', '09a3ddb4fa55', '26413b9783a6', '327cbf012cc8', '772e3f8a3805'],
    'eyes': ['06b58e227fd2', '09292b15aee7', '71d43fa6d5bd', 'ab4077190424'],
    'nose': ['5d73fd3af7b5', '74145e72e897', 'ed09e1c7eb00'],
    'mouth': ['90fd947057e0', 'd8b4ce65d0bd', 'e3d93f8477eb', 'e9daf0b33f99'],
    'arms': ['01a76672120c', '0bd1f4db7942', '7563d4453bb3', '7c7cdca373a0'],
    'legs': ['2734a58cf6be', '79fcbd75c340', 'd6c80ecc4a37'],
    'leg': ['93940f9452d4', 'c7cb77387db5'],
    'clap': ['f4bf7e472b51'],
    'face_boy1': ['1624f9a51653', '250368dde30c', 'bf632978677b'],
    'face_boy2': ['fcf7a6f009d2'],
    # семья
    'mum': ['6b6e58037b86', 'e72350'],
    'dad': ['829643d9facb', 'b8c60992f974'],
    'brother': ['7b6a75b39d7b', 'ee6d2f37e5b9'],
    'sister': ['1b8ec433051a', '8f7569490539'],
    'grandma': ['b857a6789f85', 'c1f7416a38b6'],
    'grandpa': ['058b6494bd2f', '99f361'],
    'family': ['63c3ad983a54'],
    # профессии
    'doctor': ['06c5ef9bbbfd', 'c86389d6b971'],
    'teacher': ['37345f9d4b6f', '7ee78f154d7a', 'ca36163c2d96'],
    'vet': ['68ab9f819c76', '83a842dbecd1'],
    'firefighter': ['270d52820d9c', '696424dd217c', 'b8f017ec35f4'],
    'police': ['94316a5bec86', 'f33ab3ad5f64'],
    'gardener': ['1a83c7c3886e', 'bd8bc18c77ed', 'cef5c9575d75'],
    # действия
    'running': ['7a34bfdbb313', '9e7552f463db', 'eefe59be9b1a'],
    'swimming': ['d1cb40b18a9d', 'f7ce7df0863f'],
    'reading': ['24b3b3106355', '8ead4b4deffe', '9fd80aa05f06'],
    'painting': ['1c2cccf87a08', '362d57ed3438', '87624db7099c'],
    'football': ['268d76131e66', '9433d31926fe', '998615449f7d'],
    'dancing': ['619b46f4d24f', '669c8379bd1b', '7defd70f0df5'],
    'jumping': ['6d05a76d114c'],
    'waving': ['872ffc8cf5ac'],
    # монстрики
    'mon_blue': ['35a44efa9683', 'a8399c'],
    'mon_red': ['3c2fe663ee74'],
    'mon_pink': ['5c0ca3b7818e'],
    'mon_green': ['82b30bb492be'],
    'mon_orange': ['a26409ba67f8'],
    'mon_yellow': ['e2b1da28bf42'],
    'mon_purple': ['b728859e16c1'],
    'mon_turq': ['9356ea82a7cc', 'd6254b4bd4b2'],
    'mon_blue2': ['db88a8'],
    # счёт — числа подтверждены пересчётом пятен
    'n1': ['2e6b2f736824'],
    'n2': ['9a9138ec0856'],
    'n3': ['57db0223b8cd'],
    'n4': ['7bd5e3a78bca'],
    'n5': ['627e87247d6d', '867189999314'],
    'n6': ['d47d9d3dd042'],
    'n7': ['bc2e3bc25e5c'],
    'n8': ['8f07476d8537', 'b1483e6028be'],
    'n9': ['c654dcd0ec0b', 'e07c573efd61'],
    'n10': ['5390b2ec3d05', '8d0a58402bcf'],
    'apples3': ['650f0649a153'],
    'balls6': ['f966d289ee7c'],
    'balls10': ['3e60f33f33f5'],
    'cats3': ['e56d237e9198'],
    'cats6': ['3512708446b9'],
    # предметы для чтения
    'hat': ['2b0cb62d2ad0'],
    'ham': ['312cbf84ab9a'],
    'mat': ['879e9cc326f4'],
    'hen': ['7714215c7c0a'],
    'net': ['5909748d0ee5'],
    'pen': ['d11d3c388f28'],
    'cave': ['2f95d73de8d9'],
    # служебные
    'star': ['230077617f69'],
    'clover': ['22cbf81391e4', '51b0cb648597'],
    'trophy': ['991bce28e595'],
    'popper': ['dc459b4a52db'],
    'rocket': ['8edf1a3c1391'],
    'medal': ['96e49eaf06ad'],
    'highfive': ['5ea8024245d6'],
    'party': ['4df76fc19cb2'],
}

# цвета — уже нарисованные шарики из media/sm0/u0
BALLOONS = {
    'balloon_blue': ['34b8efecd4b2', '3d17eb38fdd9'],
    'balloon_green': ['481214562a38', '6619730ebb40'],
    'balloon_pink': ['65018b00aa91', 'f40c937be9f8', 'cf3f940ebd2f'],
    'balloon_yellow': ['a48a71b4f56e', 'fccf971c0287'],
    'balloon_orange': ['c102748abf99', 'ce01e4bbf55f'],
    'balloon_red': ['8b38abac4dbc', 'e7a097c2dcaf'],
}
