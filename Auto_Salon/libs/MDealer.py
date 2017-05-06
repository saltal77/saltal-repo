# coding: utf-8
__author__ = "saltal"

import mysql.connector
from mysql.connector import Error
from libs.MAuto import Car, Lorry
from libs.MClient import Person

class Car_dealership:
    """
    Класс Автосалон
    Подключается к БД MySQL.
    Вносит авто в БД - грузовые и легковые(add_Car, add_Lorry), клиентов салона (add_Client).
    Имеет методы - Продажи авто грузовых и легковых (sell_Car, sell_Lorry)(присвоение id клиента к авто),
    Печать списка всех авто (printer_Cars), Проданных авто (print_Selled_Cars), Клиетов автосалона (print_Clients),
    поиск авто по названию (search_Cars), поиск клиента по Id(get_Client), так же методы добавления и удаления
    клиента, легкового авто и грузовика (add_Client/del_Client add_Car/del_Car add_Lorry/del_Lorry), методы обновления
    информации о клиенте - адрес и телефон (update_Client), метод обновления информации о легковом авто и грузовике -
    цвет и цена (update_Car_price/update_Lorry_price/update_Car_color/update_Lorry_Color)
    """
        # конструктор, при создании объекта класса осуществляет подключение к экземпляру БД
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        # try:
        #     conn = mysql.connector.connect(host=host, database=database, user=user, password=password)
        #     if conn.is_connected():
        #         print('<:::> Connected to MySQL database <:::>')
        # except Error as e:
        #     print(e)
    # метод закрывающий подключение к базе данных

    def stop_con(self):
        conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        conn.close()
        print('<:::> Disconnected from MySQL database <:::>')

    def print_Clients(self):
        try:
            sql = "SELECT name, adress, tel  FROM client where id_client <> 1"
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql)
            print("<:o:o:>  Cписок клиентов Дилерского центра <:o:o:>")
            rows = c.fetchall()
            for row in rows:
                decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                client = Person(decoded_row[0], decoded_row[1], decoded_row[2])
                print(client)
            return 'Успешно'

        except Error as e:
            print(e)

    def add_Client(self, name, adress, tel):
        if not name or not adress or not tel or name.isdigit() or adress.isdigit():
            raise Exception('Внимание! Имя || Адрес || Телефон не могут быть пустыми.')
        try:
            sql = 'INSERT INTO client (name, adress, tel) VALUES (%s,%s,%s)'
            args = (name, adress, tel)
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            print('add_Client - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def update_Client(self, adress, tel, id):
        if not adress or not tel or id <= 0:
            raise Exception('Внимание! Адрес || Телефон не могут быть пустыми, id не может быть менее или равен нулю')
        try:
            sql = "UPDATE client SET adress = %s, tel = %s WHERE id_client = %s"
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, (adress, tel, id))
            conn.commit()
            print('update_Client - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def get_Client(self, id):
        if id <= 0:
            raise Exception('Внимание! Id не может быть менее или равен нулю')
        try:
            sql = "SELECT name, adress, tel  FROM client WHERE id_client = %s"
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, (id,))
            rows = c.fetchall()
            if rows:
                for row in rows:
                    decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                    client = Person(decoded_row[0], decoded_row[1], decoded_row[2])
                    print(client)
                return 'Успешно'
            else:
                print('Внимание! Клиент c Id#', id,'не найден.')
        except Error as e:
            print(e)

    def del_Client(self, id):
        if id <= 0:
            raise Exception('Внимание! Id не может быть менее или равен нулю')
        try:
            sql = "DELETE FROM client WHERE id_client = %s"
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, (id,))
            conn.commit()
            print('del_Client - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def printer_Cars(self):
        try:
            sql_car = "SELECT year, color, model, a_type, power, fuel, country, price, buyed  FROM car where buyed = 1"
            sql_lorry = "SELECT year, color, model, a_type, power, fuel, country, price, buyed, cargo FROM lorry where buyed = 1"
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql_car)
            print("<:o:o:>  Cписок авто Дилерского центра <:o:o:>")
            rows = c.fetchall()
            print('Легковые:')
            for row in rows:
                decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                # print(decoded_row)
                auto = Car(decoded_row[0], decoded_row[1], decoded_row[2], decoded_row[3], decoded_row[4],
                           decoded_row[5], decoded_row[6], decoded_row[7], decoded_row[8])
                print(auto)
            c.execute(sql_lorry)
            rows = c.fetchall()
            print('Грузовые:')
            for row in rows:
                decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                lorry = Lorry(decoded_row[0], decoded_row[1], decoded_row[2], decoded_row[3], decoded_row[4],
                           decoded_row[5], decoded_row[6], decoded_row[7], decoded_row[8], decoded_row[9])
                print(lorry)
            return 'Успешно'
        except Error as e:
            print(e)

    def printer_Selled_Cars(self):
        try:
            sql_car = "SELECT year, color, model, a_type, power, fuel, country, price, buyed  FROM car where buyed <> 1"
            sql_lorry = 'SELECT year, color, model, a_type, power, fuel, country, price, buyed, cargo  FROM lorry where buyed <> 1'
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql_car)
            print("<:o:o:> Список проданных авто Дилерского центра <:o:o:>")
            print("Легковые:")
            rows = c.fetchall()
            for row in rows:
                decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                auto = Car(decoded_row[0], decoded_row[1], decoded_row[2], decoded_row[3], decoded_row[4],
                            decoded_row[5], decoded_row[6], decoded_row[7], decoded_row[8])
                print(auto)
                print('Покупатель:')
                self.get_Client(decoded_row[8])
            c.execute(sql_lorry)
            print("Грузовые:")
            rows = c.fetchall()
            for row in rows:
                decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                lorry = Lorry(decoded_row[0], decoded_row[1], decoded_row[2], decoded_row[3], decoded_row[4],
                           decoded_row[5], decoded_row[6], decoded_row[7], decoded_row[8], decoded_row[9])
                print(lorry)
                print('Покупатель:')
                self.get_Client(decoded_row[8])
            return 'Успешно'
        except Error as e:
            print(e)

    def sell_Car(self, id_buyer, id_car):
        if id_buyer <= 0 or id_car <= 0:
            raise Exception('Внимание! Id покупателя || Id автомобиля не может быть менее нуля')
        try:
            sql = 'UPDATE car SET buyed = %s WHERE id_car = %s'
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, (id_buyer, id_car))
            conn.commit()
            print('sell_Car - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def sell_Lorry(self, id_buyer, id_lorry):
        if id_buyer <= 0 or id_lorry <= 0:
            raise Exception('Внимание! Id покупателя || Id автомобиля не может быть менее нуля')
        try:
            sql = 'UPDATE lorry SET buyed = %s WHERE id_lorry = %s'
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, (id_buyer, id_lorry))
            conn.commit()
            print('sell_Lorry - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def add_Car(self, year, color, model, a_type, power, fuel, country, price, buyed):
        if year <= 0 or not color or not model or not a_type or power <= 0 or not fuel or not country or price <= 0 or buyed < 0\
             or color.isdigit() or model.isdigit() or a_type.isdigit() or fuel.isdigit() or country.isdigit():
            raise Exception('Внимание! Проверьте правильность ввода данных авто')
        try:
            sql = 'INSERT INTO car (year, color, model, a_type, power, fuel, country,' \
                      'price, buyed) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            args = (year, color, model, a_type, power, fuel, country, price, buyed)
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            print('add_Car - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def add_Lorry(self, year, color, model, a_type, power, fuel, country, price, buyed, cargo):
        if year <= 0 or not color or not model or not a_type or power <= 0 or not fuel or not country or price <= 0 or buyed < 0 or cargo <= 0 \
                or color.isdigit() or model.isdigit() or a_type.isdigit() or fuel.isdigit() or country.isdigit():
            raise Exception('Внимание! Проверьте правильность ввода данных авто')
        try:
            sql = 'INSERT INTO lorry (year, color, model, a_type, power, fuel, country,' \
                    'price, buyed, cargo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            args = (year, color, model, a_type, power, fuel, country, price, buyed, cargo)
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            print('add_Lorry - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def del_Car(self, id):
        if id <= 0:
            raise Exception('Внимание! Id авто не может быть менее или равен нулю')
        try:
            sql = "DELETE FROM car WHERE id_car = %s"
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, (id,))
            conn.commit()
            print('del_Car - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def del_Lorry(self, id):
        if id <= 0:
            raise Exception('Внимание! Id авто не может быть менее или равен нулю')
        try:
            sql = "DELETE FROM lorry WHERE id_lorry = %s"
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, (id,))
            conn.commit()
            print('del_Lorry - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def search_Cars(self, name):
        if not name:
            raise Exception('Внимание! Название не может быть пустым')
        try:
            sql_car = 'SELECT year, color, model, a_type, power, fuel, country, price, buyed  FROM car where model = %s'
            sql_lorry = 'SELECT year, color, model, a_type, power, fuel, country, price, buyed, cargo  FROM lorry where model = %s'
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql_car, (name,))
            print("Результат поиска: ")
            rows = c.fetchall()
            if rows:
                for row in rows:
                    decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                    auto = Car(decoded_row[0], decoded_row[1], decoded_row[2], decoded_row[3], decoded_row[4],
                               decoded_row[5], decoded_row[6], decoded_row[7], decoded_row[8])
                    print(auto)
            else:
                print('легковые --> не найдено...')
            c.execute(sql_lorry, (name,))
            rows = c.fetchall()
            if rows:
                for row in rows:
                    decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                    lorry = Lorry(decoded_row[0], decoded_row[1], decoded_row[2], decoded_row[3], decoded_row[4],
                               decoded_row[5], decoded_row[6], decoded_row[7], decoded_row[8], decoded_row[9])
                    print(lorry)
                return 'Успешно'
            else:
                print('грузовые --> не найдено...')
        except Error as e:
            print(e)

    def update_Car_price(self, price, id):
        if price <= 0 or id <= 0 or not price or not id:
            raise Exception('Внимание! Цена || Id авто не могут быть менее или равны нулю')
        try:
            sql = "UPDATE car SET price = %s WHERE id_car = %s"
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)

            c = conn.cursor()
            c.execute(sql, (price, id))
            conn.commit()
            print('update_Car_price - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def update_Lorry_price(self, price, id):
        if price <= 0 or id <= 0 or not price or not id:
            raise Exception('Внимание! Цена || Id авто не могут быть менее или равны нулю')
        try:
            sql = "UPDATE lorry SET price = %s WHERE id_lorry = %s"
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, (price, id))
            conn.commit()
            print('update_Lorry_price - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def update_Car_Color(self, color, id):
        if not color or id <= 0 or color.isdigit():
            raise Exception('Внимание! Цвет не может быть пусым || Id авто не может быть менее или равен нулю')
        try:
            sql = "UPDATE car SET color = %s WHERE id_car = %s"
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, (color, id))
            conn.commit()
            print('update_Car_Color - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)

    def update_Lorry_Color(self, color, id):
        if not color or id <= 0 or color.isdigit():
            raise Exception('Внимание! Цвет не может быть пусым || Id авто не может быть менее или равен нулю')
        try:
            sql = "UPDATE lorry SET color = %s WHERE id_car = %s"
            conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            c = conn.cursor()
            c.execute(sql, (color, id))
            conn.commit()
            print('update_Lorry_Color - Успешно...')
            return 'Успешно'
        except Error as e:
            print(e)
