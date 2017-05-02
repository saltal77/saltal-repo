# coding: utf-8
__author__ = "saltal"

import gzip
import json
import codecs
import re
import os
import patoolib
import urllib.request
import sqlite3
from  datetime import date
import sys

print("Любая погода у вас дома с портала Openweathermap.org!")
print("Загружаюсь, один момент pls...")

# Чтение APP ID из файла
with open('app.id', 'r', encoding='UTF-8') as ap:
    app_id = ap.read()

# Загрузка списка городов city.list.json.gz
#destination = 'city.list.json.gz'
#url_s = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
#urllib.request.urlretrieve(url_s, destination)

# Распаковка списка городов в JSON формате
#patoolib.extract_archive("city.list.json.gz", outdir = os.getcwd())

# Чтение файла и обработка JSON списка
with open('city.list.json', 'r', encoding='UTF-8') as f:
    for line in f:
        data = f.readlines()

all_towns = {}
for towns in data:
    town_dict = json.loads(towns)
    all_towns[town_dict['_id']] = dict(name=town_dict['name'],\
        country=town_dict['country'], id = town_dict['_id'])

# Поиск города по начальным буквам
strn = input("Введите первые буквы города: ")
pattern = strn + '[a-z]+'

lst_town = []
for town in all_towns.values():
    if (re.findall(pattern, town['name'])):
        lst_town.append(re.findall(pattern, town['name']))

for town in lst_town:
    print(town)

# Поиск города по полному имени
id_town = []
strn2 = input("Введите  город: ")
for town in all_towns.values():
    if town['name'] == strn2:
        #print(town['id'], town['name'], town['country'])
        id_town.append(town['id'])

# Если данных о погоде нет - выход из прогрммы
try:
    id_town = str(id_town[0])
except IndexError:
    print("Нет данных о погоде, завершаю работу.")
    sys.exit()

# Загрузка и парсинг данных о погоде нужного города
dt = str(date.today())
url_w = 'http://api.openweathermap.org/data/2.5/weather?id=' + id_town +'&units=metric&appid=' + app_id
w_town = urllib.request.urlopen(url_w)
w_out = str(w_town.read(), 'utf-8')
town_name = str(re.findall('(?:"name":)("\w+)', w_out))[3:-2]
temp = str(re.findall('(?:"temp"):(.*?,)', w_out))[2:-3]
id_whe = str(re.findall('(?:"id":)(\d{1,3},)', w_out))[2:-3]

# Вывод на экран нужной погоды
print('id {} Город {} Дата {} Температура {} Id Погоды {}'.format(id_town, town_name, dt,temp, id_whe))

# Создание SQL базы
sqlbase = 'wth.db'

# Блок SQL Запросов
sql_start = 'INSERT INTO weather (id_города, Город, Дата, Температура, id_погоды ) \
VALUES(" ' + id_town + '","' + town_name + '","' + dt + '","' + temp + '","' + id_whe + '")'

sql_crt = 'CREATE TABLE weather (id_города  INTEGER PRIMARY KEY, Город   VARCHAR(255), \
Дата  DATE, Температура  INTEGER, id_погоды  INTEGER)'

sql_upd = 'UPDATE weather SET Температура = "'+ temp +'" WHERE id_города = "'+ id_town +'"'

sql_find = 'SELECT * FROM weather WHERE id_города = "'+ id_town +'"'

# Работа с SQL базой
conn = sqlite3.connect(sqlbase)
cur = conn.cursor()
try:
    cur.execute(sql_crt)
    conn.commit()
    print("Создана  База Погоды ...")
    cur.execute(sql_start)
    conn.commit()
    #cur.execute('SELECT * FROM weather')
    #print(cur.fetchall())
    conn.close()
# Если БД уже создавалась
except sqlite3.OperationalError:
    cur.execute(sql_find)
    data = cur.fetchone()
    if data is None:
        print("Добавляю Данные в Базу Погоды...")
        cur.execute(sql_start)
        conn.commit()
        #cur.execute('SELECT * FROM weather')
        #print(cur.fetchall())
        conn.close()
    else:
        print("Обновляю Данные в Базе Погоды...")
        cur.execute(sql_upd)
        conn.commit()
        #cur.execute('SELECT * FROM weather')
        #print(cur.fetchall())
        conn.close()

input("Програма завершена, нажмите любую клавишу ...")


