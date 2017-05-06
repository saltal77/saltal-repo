# coding: utf-8
__author__ = "saltal"

import unittest
from libs.MDealer import Car_dealership
from libs.MAuto import Car

class Test_Car_dealership(unittest.TestCase):
    """
    Тестирование основных методов класса Car_dealership (Автосалон)
    включая работу с БД MySQL на основе Unittest
    """
    def setUp(self):
        """
        Создание экземпляра класса
        """
        self.M_Dealer = Car_dealership('localhost', 'salon_saltal', 'root', '1044470')

    @unittest.skip('test_upper - пробный - отменен...')
    def test_upper(self):

        self.assertEqual('foo'.upper(), 'FOO')


    #@unittest.skip('test_print_Clients - испытан - отключен...')
    def test_print_Clients(self):
        """
        Метод  - Вывод на печать всех клиентов автосалона
        """

        result = self.M_Dealer.print_Clients()
        self.assertEqual(result, 'Успешно')

        with self.assertRaises(TypeError):
            self.M_Dealer.print_Clients(1)


    @unittest.skip('test_printer_Cars - испытан - отключен...')
    def test_printer_Cars(self):
        """
        Метод  - Вывод на печать всех авто
        """
        result = self.M_Dealer.printer_Cars()
        self.assertEqual(result, 'Успешно')

        with self.assertRaises(TypeError):
            self.M_Dealer.printer_Cars(1)


    def test_search_Cars(self):
        """
        Метод  - Поиск авто по названию
        """
        result = self.M_Dealer.search_Cars('MAN')
        self.assertEqual(result, 'Успешно')

        with self.assertRaises(Exception):
            self.M_Dealer.search_Cars(0)

        with self.assertRaises(Exception):
            self.M_Dealer.search_Cars('')


    @unittest.skip('test_add_Client - испытан - отключен...')
    def test_add_Client(self):
        """
        Метод - добавление клиента в БД
        """
        result = self.M_Dealer.add_Client('Дмитрий Нагиев', 'Москва, ул. Дооржная 34 - 45', ' +7-499-256-6870')
        self.assertEqual(result, 'Успешно')

        with self.assertRaises(Exception):
            self.M_Dealer.add_Client('', 'Москва, ул. Дооржная 34 - 45', ' +7-499-256-6870')

        with self.assertRaises(Exception):
            self.M_Dealer.add_Client('Дмитрий Нагиев', '', ' +7-499-256-6870')

        with self.assertRaises(Exception):
            self.M_Dealer.add_Client(2, 'Москва, ул. Дооржная 34 - 45', ' +7-499-256-6870')

        with self.assertRaises(Exception):
            self.M_Dealer.add_Client('Дмитрий Нагиев', '5', ' +7-499-256-6870')


    #@unittest.skip('test_update_Client - испытан - отключен...')
    def test_update_Client(self):
        """
        Метод - обновление информации о  клиенте в БД

        """
        result = self.M_Dealer.update_Client('Москва, ул. Темная 33-32', '+7-495-257-8999',6)
        self.assertEqual(result, 'Успешно')

        with self.assertRaises(Exception):
            self.M_Dealer.update_Client('', '+7-495-257-8999', 6)

        with self.assertRaises(Exception):
            self.M_Dealer.update_Client('Москва, ул. Темная 33-32', '', 6)

        with self.assertRaises(Exception):
            self.M_Dealer.update_Client('Москва, ул. Темная 33-32', '+7-495-257-8999', -6)



    def test_get_Client(self):
       """
       Метод - Поиск клиента в БД поID
       """
       result = self.M_Dealer.get_Client(5)
       self.assertEqual(result, 'Успешно')

       with self.assertRaises(TypeError):
           self.M_Dealer.get_Client('c')

       with self.assertRaises(Exception):
           self.M_Dealer.get_Client(-1)

       with self.assertRaises(Exception):
           self.M_Dealer.get_Client(0)


    #@unittest.skip('test_sell_Car - испытан - отключен...')
    def test_sell_Car(self):
        """
        Метод - продажа авто
        """
        result = self.M_Dealer.sell_Car(13, 12)
        self.assertEqual(result, 'Успешно')

        with self.assertRaises(Exception):
            self.M_Dealer.sell_Car(0, 12)

        with self.assertRaises(Exception):
            self.M_Dealer.sell_Car(13, -12)

        with self.assertRaises(TypeError):
            self.M_Dealer.sell_Car('c', 12)


    @unittest.skip('test_add_Car - испытан - отключен...')
    def test_add_Car(self):
        """
        Метод - добавление нового авто в БД
        """
        result = self.M_Dealer.add_Car(2009, 'желтый', 'BMW', 'седан', 150, 'бензин', 'Германия', 250, 1)
        self.assertEqual(result, 'Успешно')

        with self.assertRaises(Exception):
            self.M_Dealer.add_Car(2009, 'желтый', 'BMW', 'седан', 150, 'бензин', 'Германия', 250, 'b')

        with self.assertRaises(Exception):
            self.M_Dealer.add_Car('двух тысячный', 'желтый', 'BMW', 'седан', 150, 'бензин', 'Германия', 250, 1)

        with self.assertRaises(Exception):
            self.M_Dealer.add_Car(2009, 5 , 'BMW', 'седан', 150, 'бензин', 'Германия', 250, 1)

        with self.assertRaises(Exception):
            self.M_Dealer.add_Car(2009, 'желтый', 345, 'седан', 150, 'бензин', 'Германия', 250, 1)

        with self.assertRaises(Exception):
            self.M_Dealer.add_Car(2009, 'желтый', 'BMW', 6, 150, 'бензин', 'Германия', 250, 1)

        with self.assertRaises(Exception):
            self.M_Dealer.add_Car(2009, 'желтый', 'BMW', 'седан', 'сто сил', 'бензин', 'Германия', 250, 1)

        with self.assertRaises(Exception):
            self.M_Dealer.add_Car(2009, 'желтый', 'BMW', 'седан', 150, 'бензин', 899, 250, 1)


    #@unittest.skip('test_update_Car_price - испытан - отключен...')
    def test_update_Car_price(self):
        """
        Метод - обновление цены авто в БД
        """
        result = self.M_Dealer.update_Car_price(250, 10)
        self.assertEqual(result, 'Успешно')

        with self.assertRaises(Exception):
            self.M_Dealer.update_Car_price(250, -10)

        with self.assertRaises(Exception):
            self.M_Dealer.update_Car_price(0, 10)

        with self.assertRaises(Exception):
            self.M_Dealer.update_Car_price('', 10)

        with self.assertRaises(Exception):
            self.M_Dealer.update_Car_price(210, '')

        with self.assertRaises(Exception):
            self.M_Dealer.update_Car_price(230, 'id')

        with self.assertRaises(Exception):
            self.M_Dealer.update_Car_price('двести', 10)


    #@unittest.skip('test_update_Car_color - испытан - отключен...')
    def test_update_Car_color(self):
        """
        Метод - изменение цвета авто в БД
        """
        result = self.M_Dealer.update_Car_Color('оранжевый', 14)
        self.assertEqual(result, 'Успешно')

        with self.assertRaises(Exception):
            self.M_Dealer.update_Car_Color('', 14)

        with self.assertRaises(Exception):
            self.M_Dealer.update_Car_Color('зеленый', -14)

        with self.assertRaises(Exception):
            self.M_Dealer.update_Car_Color('23', 14)

class Test_Car(unittest.TestCase):
    """
    Тестирование нескольких методов класса Car (Авто)
    """
    def setUp(self):
        """
        Создание экземпляра класса Автомобиль
        """
        self.M_Car = Car(2010, 'серый', 'Jaguar', 'седан', 200, 'бензин', 'Великобритания', 400, 1)


    def test_get_buyed(self):
        """
        Метод - выяснить продано авто или нет (buyed == 1 - не продано)
        """
        result = self.M_Car.get_buyed()
        self.assertEqual(result, 1)

        with self.assertRaises(TypeError):
            self.M_Car.get_buyed(1)

    #@unittest.skip('test_set_buyed - испытан - отключен...')
    def test_set_buyed(self):
        """
        Метод - продать авто
        """
        result = self.M_Car.set_buyed(2)
        self.assertEqual(result, 'Успешно')

        with self.assertRaises(Exception):
            self.M_Car.set_buyed(-2)

        with self.assertRaises(Exception):
            self.M_Car.set_buyed('')

        with self.assertRaises(Exception):
            self.M_Car.set_buyed('m')

    #@unittest.skip('test_get_country - испытан - отключен...')
    def test_get_country(self):
        """
        Метод - узнать страну производства авто
        """
        result = self.M_Car.get_country()
        self.assertEqual(result, 'Великобритания')

        with self.assertRaises(TypeError):
            self.M_Car.get_country(1)


    def test_set_country(self):
        """
        Метод - изменить страну производства авто
        """
        result = self.M_Car.set_country('США')
        self.assertEqual(result, 'Успешно')

        with self.assertRaises(Exception):
            self.M_Car.set_country('')

        with self.assertRaises(Exception):
            self.M_Car.set_country('12345')

        with self.assertRaises(Exception):
            self.M_Car.set_country(12)


if __name__ == '__main__':
    unittest.main()























