# coding: utf-8
__author__ = "saltal"
# Модуль - инициация автосалона, добавление авто и клиетов, продажа, печвть различных списков авто.
from libs.MDealer import Car_dealership

M_Dealer = Car_dealership('localhost','salon_saltal','root','astra')
#M_Dealer.stop_con()
#M_Dealer.sell_Car(5, 6)
#M_Dealer.sell_Lorry(7, 5)
#M_Dealer.update_Lorry_price(950, 2)
M_Dealer.printer_Cars()
#M_Dealer.printer_Selled_Cars()
#M_Dealer.add_Car(2010, 'белый', 'Citroen', 'седан', 100, 'бензин', 'Франция', 190, 1)
#M_Dealer.del_Car(7)
#M_Dealer.search_Cars('MAN')
#M_Dealer.update_Car_price(180, 4)
#M_Dealer.add_Lorry(2007, 'синий', 'Renault', 'грузовик', 400, 'бензин', 'Францияия', 600, 1, 11)
#M_Dealer.add_Client('Дмитрий Павлов', 'Москва, ул. Осенняя 34 - 42', ' +7-495-276-6675')
#M_Dealer.update_Client('Москва, Проспект Мира 113 -67 ', '+7-812-558-9636', 2)
#M_Dealer.del_Client(3)
#M_Dealer.print_Clients()
#M_Dealer.get_Client(5)
#M_Dealer.update_Car_Color('красный', 6)








