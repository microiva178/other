#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import sys, warnings

################Проверка версии python3 ##################################

if sys.version_info[0] < 3:
	warnings.warn("Для выполнения этой программы необходима как минимум версия Python 3.0", RuntimeWarning)
	quit()
else:
	print('Нормальное продолжение')

##########################################################################

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['/home/userf/Desktop/backuptest']

target_dir = '/home/userf/Desktop'

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге

today = target_dir + os.sep + time.strftime('%Y%m%d')

# Текущее время служит именем zip-архива

now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла

comment = input('Введите коментарий --> ')
if len(comment) == 0: # проверяем, введен ли коментарий
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
		comment.replace(' ', '_') + '.zip'

# Создаем каталог, если его еще нет
if not os.path.exists(today):
	os.mkdir(today) # создание каталога
print('Каталог успешно создан', today)

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
	print('Резервная копия успешно создана в', target)
else:
	print('Создание резервной копии НЕ УДАЛОСЬ')

