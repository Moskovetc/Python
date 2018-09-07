#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
def make_dir(dir_name):
    dir_name=os.path.join(os.getcwd(),dir_name)
    try:
        os.mkdir(dir_name)
        print('папка {} создана'.format(dir_name))
    except FileExistsError:
        print('папка {} уже существует'.format(dir_name))
def rm(dir_name):
    dir_name = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_name)
        print('папка {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('Папка с именем {} не найдена'.format(dir_name))
    except PermissionError:
        print('невозможно удалить папку {}, в доступе отказано'.format(dir_name))
dirs=['dir_1','dir_2','dir_3','dir_4','dir_5','dir_6','dir_7','dir_8','dir_9']
# for i in dirs:
#     make_dir(i)
# for i in dirs:
#     rm(i)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def ls():
    print('Текущая директория {}'.format(os.getcwd()))
    elems=os.listdir(os.getcwd())
    for elem in elems:
        print(elem)
# ls()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def cp(file_name):
    if os.path.isabs(file_name):
        copy_file_name=os.path.join(os.getcwd(),'copy_'+os.path.basename(file_name))
    else:
        copy_file_name = os.path.join(os.getcwd(), 'copy_' + file_name)
    file_name = os.path.join(os.getcwd(), file_name)
    try:
        shutil.copy(file_name,copy_file_name)
        print('файл {} успешно скопирован в {}'.format(os.path.basename(file_name),os.path.basename(copy_file_name)))
    except FileNotFoundError:
        print('Файл с именем {} не найден'.format(os.path.basename(file_name)))
# cp(sys.argv[0])