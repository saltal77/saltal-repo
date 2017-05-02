# coding: utf-8
__author__ = "saltal"

#формат запроса - export_openweather.py csv filename Town


import sys
import sqlite3
import json
import csv

#Блок проверок аргументов
try:
    f_format = sys.argv[1]
except IndexError:
    print("Необходимо ввести формат файла csv или json...")
    sys.exit()

try:
  f_name = sys.argv[2]
except IndexError:
    f_name = ''

try:
    town_name = sys.argv[3]
except IndexError:
    town_name = ''

f_name_bkp = "backup"
ending = [".json",".csv"]
user_end = ["json","csv"]
sqlbase = 'wth.db'

#Проверка формата файла
if  f_format not in user_end:
    print("Необходимо правильно ввести формат файла csv или json...")
    sys.exit()

#Блок Запросов
sql_find = 'SELECT * FROM weather WHERE Город = "'+ town_name +'"'
sql_all = 'SELECT * FROM weather'


def json_bkp(req, f_name):
    """
     Функция сохраняет данные  SQLite в json формате
    """
    if f_name:
        filename = f_name + ending[0]
    else:
        filename = f_name_bkp + ending[0]
    conn = sqlite3.connect(sqlbase)
    cur = conn.cursor()
    cur.execute(req)
    json_string = json.dumps(cur.fetchall())
    with open(filename, 'w', encoding='UTF-8', ) as f:
        json.dump(json_string, f, ensure_ascii=False)
    conn.close()
    return

def csv_bkp(req, f_name):
    """
    Функция сохраняет данные  SQLite в csv формате
    """
    if f_name:
        filename = f_name + ending[1]
    else:
        filename = f_name_bkp + ending[1]
    conn = sqlite3.connect(sqlbase)
    cur = conn.cursor()
    cur.execute(req)
    csvWriter = csv.writer(open(filename, "w"))
    rows = cur.fetchall()
    for row in rows:
            csvWriter.writerow(row)
    conn.close()

#Блок сравнения поступивших данных и запросов к SQL
if town_name:
    #print("Город введен -  Поиск данных этого города...")
    find = sql_find
    conn = sqlite3.connect(sqlbase)
    cur = conn.cursor()
    cur.execute(find)
    if cur.fetchall():
        print("Город найден в базе данных, выгружаю данные")
        if f_format == 'json':
            json_bkp(find, f_name)
        else:
            csv_bkp(find, f_name)
    else:
        print("Город не найден в базе данных, выгружаю всю базу")
        if f_format == 'json':
            json_bkp(sql_all, f_name)
            conn.close()
            sys.exit()
        else:
            csv_bkp(sql_all, f_name)
            conn.close()
            sys.exit()
    conn.close()

else:
    print("Не введен город - выгрузка данных всей базы...")
    find = sql_all
    conn = sqlite3.connect(sqlbase)
    cur = conn.cursor()
    cur.execute(find)
    if cur.fetchall():
        #print("Данные выгружаются...")
        if f_format == 'json':
            json_bkp(find, f_name)
        else:
            csv_bkp(find, f_name)
    else:
        print("Данные не найдены...")
        conn.close()
        sys.exit()
    conn.close()



