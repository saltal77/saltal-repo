# coding: utf-8
__author__ = "saltal"

class Person:
    """
    Класс Клиент
    имеет методы изменения параметров -
    телефон и адрес
    метод печати всех данных клиента.
    имеет проверку на вхождение пустых значений в параметры -
    Имя, Адрес, Телефон.
    """
    def __init__(self, name, adress, tel):

        self.name = name
        self.adress = adress
        self.tel = tel
        if (not name or not adress or not tel):
            raise Exception('Внимание! Имя || Адрес || Телефон не могут быть пустыми')

    def __str__(self):
        return '{}, Адрес: {}, Телефон: {}'.format(self.name, self.adress, self.tel)
    @property
    def get_tel(self):
        return self.tel, self.name
    def set_tel(self, newTel):
        self.tel = newTel
    @property
    def get_adress(self):
        return self.adress
    def set_adress(self, newAdress):
        self.adress = newAdress
