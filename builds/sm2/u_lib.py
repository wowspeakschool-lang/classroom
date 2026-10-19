# -*- coding: utf-8 -*-
"""Сборки SM2 писались против модуля u_lib; теперь общая версия лежит в tools/lib.py.
Этот файл — только мост: `import u_lib` отдаёт тот самый модуль, а не копию,
иначе setup() записал бы юнит в одни глобальные переменные, а sql() читал бы другие."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
import lib
sys.modules[__name__] = lib
