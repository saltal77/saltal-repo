# coding: utf-8
__author__ = "saltal"

class Car:
    """
    Класс  Легковой Автомобиль
    имеет методы изменения параметров -
    год, цвет, тип, модель, тип двигателя, мощнсть, страна производства и т.д.
    имеет проверку на вхождение отрицательных значений в параметры -
    год, цена, мощность, id покупателя, метод печати всех параметров авто.
    """
    def __init__(self, year, color, model, a_type, power, fuel, country, price, buyed):

        self.year = year
        self.color = color
        self.model = model
        self.a_type = a_type
        self.power = power
        self.fuel = fuel
        self.country = country
        self.price = price
        self.buyed = buyed
        if(year < 0 or price < 0 or power < 0 or buyed < 0):
            raise Exception('Внимание! Год || Мощность || Цена не может быть менее нуля')

    @property
    def get_year(self):
        return self.year

    def set_year(self, newYear):
        self.year = newYear

    def get_color(self):
        return self.color

    def set_color(self, newColor):
        self.color = newColor

    @property
    def get_model(self):
        return self.model

    def set_model(self, newModel):
        self.model = newModel

    @property
    def get_type(self):
        return self.a_type

    def set_type(self, newType):
        self.a_type = newType

    def get_power(self):
        return self.power

    def set_power(self, newPower):
        self.power = newPower

    def get_fuel(self):
        return self.fuel

    def set_fuel(self, newFuel):
        self.fuel = newFuel

    def get_country(self):
        return self.country

    def set_country(self, newCountry):
        self.country = newCountry

    @property
    def get_price(self):
        return self.price

    def set_price(self, newPrice):
        self.price = newPrice

    def get_buyed(self):
        return self.buyed

    def set_buyed(self, newBuyed):
        self.buyed = newBuyed

    def __str__(self):
        return '{}, цвет {}, {} {} год, {} л.с., двигатель {}, страна производства {}, ' \
               'стоимость {} т.руб.'.format(self.model, self.color, self.a_type, self.year, self.power, self.fuel,
                self.country, self.price)


class Lorry(Car):
    """
    Класс грузовик наследуется от Класс Легковой Автомобиль
    имеет проверку на вхождение отрицательного параметра грузоподъемность
    и печать всех параметров грузовика.
    """
    def __init__(self, year,color, model, a_type, power, fuel, country, price, buyed, cargo):
        super().__init__(year, color, model, a_type, power, fuel, country, price, buyed)
        self.cargo = cargo
        if (cargo < 0):
            raise Exception('Внимание! грузоподъемность не может быть менее нуля')

    @property
    def get_cargo(self):
        return self.cargo

    def set_cargo(self, newCargo):
        self.cargo = newCargo

    def __str__(self):
        return '{}, цвет {}, {} {} год, {} л.с., двигатель {}, грузоподъемность {} т., страна ' \
               'производства {}, стоимость {} т.руб.'.format(self.model, self.color, self.a_type, self.year,
                self.power, self.fuel, self.cargo, self.country, self.price)
