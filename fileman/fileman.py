# coding: utf-8
__author__ = "saltal"    

# Простейший файловый менеджер

import os
import chdir
import cr_rmdir
import filecopy

q = None

print("Fileman v.1.0")


while q != 'q':
    q = input('Введие  команду: up/dwn/lst/cp/mk/del, hlp - помощь, q - выход:  ')

    if q == 'dwn':
        n = input('Введите имя каталога: ')
        chdir.change_dir(n)
        print('Текущий каталог: ', os.getcwd())

    elif q == 'mk':
        n = input('Введите имя создаваемого каталога: ')
        dir_path = os.path.join(os.getcwd(), n)
        cr_rmdir.dir_create(dir_path)
        print('Текущий каталог: ', os.getcwd())

    elif q == 'del':
        n = input('Введите имя удаляемого каталога: ')
        dir_path = os.path.join(os.getcwd(), n)
        cr_rmdir.dir_remove(dir_path)
        print('Текущий каталог: ', os.getcwd())

    elif q == 'up':
        chdir.up_dir()
        print('Текущий каталог: ', os.getcwd())

    elif q == 'lst':
        chdir.dir_list()

    elif q == 'cp':
        f = input("Введите полное имя файла:  ")
        p = input("Введите полный путь для копии: ")
        filecopy.copy(f, p)

    elif q == 'hlp':
        
        print('HELP: "up"- поднятся на каталог выше\n "dwn"- спустится на каталог ниже\n \
    "lst" - просмотр каталога\n "mk" - создание каталога\n "del" - удаление каталога\n \
    "cp" - копирование файла\n "q" - выход    ')



