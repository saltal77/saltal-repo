# coding: utf-8
__author__ = "saltal"    



import os
import shutil




def copy(fl, pt):
    '''
    Функция копирования файла
    '''
    try:
        shutil.copy(fl, pt)
        print("Успешно")
    except FileNotFoundError:
        print('Такого файла не существует.')




