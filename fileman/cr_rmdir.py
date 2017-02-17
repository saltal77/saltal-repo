# coding: utf-8
__author__ = "saltal"    



import os



def dir_create(path):
    '''
    Функция создания каталога в текущей директории
    '''
    try:
        os.makedirs(path)
        print('Успешно создан')

    except FileExistsError:
        print('Такия директория уже существуют')



def dir_remove(path):
    '''
    Функция удаления каталога(ов) в текущей директории
    '''
    try:
        os.removedirs(path)         
        print('Успешно удален')

    except FileNotFoundError:
        print('Такие директории не существуют')

