# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print('cp <file_name> - создает копию указанного файла')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')
    print('rm <file_name> - удаляет указанный файл (запросить подтверждение операции)')
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def rm(dir_name):
    dir_name = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(dir_name):
        while True:
            confirm=input('вы точно хотите удалить эту папку? y/n\n')
            if confirm.upper()=='Y' or confirm.upper()=='YES':
                try:
                    os.rmdir(dir_name)
                    print('папка {} удалена'.format(dir_name))
                except FileNotFoundError:
                    print('Папка с именем {} не найдена'.format(dir_name))
                except PermissionError:
                    print('невозможно удалить папку {}, в доступе отказано'.format(dir_name))
                except NotADirectoryError:
                    print('Путь {} не является директорией'.format(dir_name))
                finally:
                    break
            elif confirm.upper()=='N' or confirm.upper()=='NO':
                print('Удаление отменено')
                break
    if os.path.isfile(dir_name):
        while True:
            confirm=input('вы точно хотите удалить этот файл? y/n\n')
            if confirm.upper()=='Y' or confirm.upper()=='YES':
                try:
                    os.remove(dir_name)
                    print('файл {} удалена'.format(dir_name))
                except FileNotFoundError:
                    print('файл с именем {} не найдена'.format(dir_name))
                except PermissionError:
                    print('невозможно удалить файл {}, в доступе отказано'.format(dir_name))
                finally:
                    break
            elif confirm.upper()=='N' or confirm.upper()=='NO':
                print('Удаление отменено')
                break
def ls():
    print('Текущая директория {}'.format(os.getcwd()))
    elems=os.listdir(os.getcwd())
    for elem in elems:
        print(elem)

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

def cd(path):
    path = os.path.join(path)
    try:
        os.chdir(path)
        print('Вы перешли в директорию {}'.format(os.getcwd()))
    except FileNotFoundError:
        print('Директория {} не существует'.format(path))

do = {
    "help": print_help,
    "mkdir": make_dir,
    'rm':rm,
    'ls':ls,
    'cp':cp,
    'cd':cd,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if key in ['cd','rm','cp'] and dir_name:
        do[key](dir_name)
    elif do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
print("Укажите ключ help для получения справки")
# P.S. По возможности, сделайте кросс-платформенную реализацию.