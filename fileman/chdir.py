# coding: utf-8
__author__ = "saltal"    


import os
import re
import sys


def change_dir(name):
    '''
    Функция смены каталога
    '''
    try:
        path = os.path.join(os.getcwd(), name)
        os.chdir(path)
    except FileNotFoundError:
        print('Такого каталога не существует.')


def dir_list():
    '''
    Функция вывода на экран папок текущего каталога
    '''
    dirs = os.listdir(path=os.getcwd())
    print('Папки и файлы текущего каталога :')
    for i in dirs:

        if os.path.isdir(i):
            print(i)# Каталоги печатаем первыми
    for i in dirs:
        if not os.path.isdir(i):
            print(i)
    




def up_dir():
    '''
    Функция выхода в верхний каталог
    '''
    os.chdir('..')

	


