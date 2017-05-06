 #coding: utf-8
__author__ = "saltal"

# Модуль -  автосалон GUI на основе TKinter, добавление авто и клиетов, продажа, вывод различных списков авто.
from tkinter import *
import hashlib
import re
from libs.MDealer import Car_dealership


M_Dealer = Car_dealership('localhost', 'salon_saltal', 'root', '1044470')

########################################################################################################################
# Окно авторизации
root_a = Tk()
root_a.title("Авторизация")
root_a.minsize(200, 120)
root_a.resizable(width=False, height=False)
label_login = Label(root_a, text="Логин", font="Arial 10")
label_password = Label(root_a, text="Пароль", font="Arial 10")
login = Entry(root_a, width=15, bg="lightyellow")
password = Entry(root_a, width=15, show='x', bg="lightyellow")
but_auth = Button(root_a, text="Войти", bg="lightblue", fg="black", font="Arial 11", width=10, height=1)
var_a = StringVar()
message_box_a = Message(root_a, textvariable=var_a, width=150)

########################################################################################################################
# Главное окно интерфейс администратор
def admin():

    root_a.destroy()
    root = Tk()
    root.title("Автосалон 'М-Дилер'")

    fra1 = Frame(root, width=500, height=100, bg="lightblue", bd=60)
    fra2 = Frame(root, width=500, height=100, bd=20)
    # Логотип
    logo = PhotoImage(file=".//libs//logo.gif")
    label_logo = Label(fra2, image=logo)
    label_logo.photo = logo
    label = Label(fra1, text="-=- M-Dealer Auto - our cars is the Best for you -=-", font="Georgia 11 bold", bg="lightblue")
    text_entry = Text(fra1, width=80, height=20, font="Verdana 10", wrap=WORD)
    # Виджет  текстовых сообщений работы программы
    var = StringVar()
    message_box = Message(fra1, textvariable=var, width=150, bg="lightblue") # relief=RAISED - тип края границ


    def printer_Cars(event):
        """
        Функция просмотра всех авто
        """
        cars_lst = M_Dealer.printer_Cars()
        text_entry.delete(0.0, END)
        text_entry.insert(0.0, '{:<3}{:<8}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}{:<8}'.format('Id', 'Год',
        'Цвет', 'Модель', 'Тип', 'Мощность л.с.', 'Двигатель', 'Страна', 'Цена тыс. руб.' + '\n'))
        text_entry.insert(2.0, '-' * 91 + '\n')
        for row in cars_lst:
            decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
            text_entry.insert(3.0, '{:<3}|{:<8}|{:<10}|{:<10}|{:<10}|{:<5}|{:<15}|{:<10}|{:<8} \n'.format(decoded_row[0],
                                            decoded_row[1], decoded_row[2], decoded_row[3], decoded_row[4], decoded_row[5],
                                            decoded_row[6], decoded_row[7], decoded_row[8]))
            #text_entry.insert(3.0, str(decoded_row).strip('()').replace('\'', '') + '\n')
        var.set('Список авто')


    def printer_Clients(event):
        """
         Функция просмотра всех клиентов
        """
        client_lst = M_Dealer.print_Clients()
        text_entry.delete(0.0, END)
        text_entry.insert(0.0, '{:<4}  {:<30}  {:<35}  {:>25}'. format('Id', 'Имя Фамилия', 'Адрес', 'Телефон' + '\n'))
        text_entry.insert(2.0, '-' * 91 + '\n')
        for row in client_lst:
            decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
            text_entry.insert(3.0, '{:<4}{:<25}{:>35}{:>25}'.format(decoded_row[0], decoded_row[1], decoded_row[2], decoded_row[3]) + '\n')
        var.set('Список клиентов')


    def upload_selled_Cars(event):
        """
        Выгрузка данных о проданных авто и клиентах в TXT файл с использованием многопоточности
        """
        M_Dealer.run_Tread_upload()
        var.set('Успешно...')


    def exit_main(event):
        """
        Функция закрыть окно
        """
        root.destroy()
    ################################################################################################################
    # Окно добаление пользователя
    def window_add_user(event):

        win_adduser = Toplevel(root, bd=10)
        win_adduser.title("Добвление пользователя")
        win_adduser.minsize(width=300, height=50)
        fra1 = Frame(win_adduser, width=250, height=45, bg="lightblue", bd=10)
        fra2 = Frame(win_adduser, width=250, height=45, bd=20)
        logo = PhotoImage(file=".//libs//logo.gif")
        label_logo = Label(fra2, image=logo)
        label_logo.photo = logo
        var1 = StringVar()
        message_box_adduser = Message(fra1, textvariable=var1, width=150, bg="lightblue")
        label_role = Label(fra1, text="Роль пользователя:", font="Arial 11", bg="lightblue")
        label_login = Label(fra1, text="Логин:", font="Arial 11", bg="lightblue")
        label_pass = Label(fra1, text="Пароль:", font="Arial 11", bg="lightblue")
        role_input = Entry(fra1, width=20, bd=3, bg="lightyellow")
        login_input = Entry(fra1, width=20, bd=3, bg="lightyellow")
        pass_input = Entry(fra1, width=20, bd=3, bg="lightyellow")


        # Проверка налету полей ввода при добавлении пользователя
        # log_check - проверка на количество символов в логине (не менее 5), role_check - проверка на заполнение тоько 0 или 1,
        #  pass_check - проверка на длинну пароля не менее 8 символов.
        def log_check(event):
            if len(login_input.get()) > 4:
                login_input['bg'] = 'lightgreen'
            else:
                login_input['bg'] = '#FF748A'
                var1.set('Логин не соответсвует политике не менее 5 символов')

        login_input.bind('<Any-KeyRelease>', log_check)


        def role_check(event):
            if role_input.get() == '1' or role_input.get() == '0':
                role_input['bg'] = 'lightgreen'
            else:
                role_input['bg'] = '#FF748A'
                var1.set('Роль имеет значения 1 или 0')

        role_input.bind('<Any-KeyRelease>', role_check)


        def pass_check(event):
            if len(pass_input.get()) > 7:
                pass_input['bg'] = 'lightgreen'
            else:
                pass_input['bg'] = '#FF748A'
                var1.set('Пароль должен иметь длинну не менее 8 символов')

        pass_input.bind('<Any-KeyRelease>', pass_check)


        def add_user(event):
            """
            Функция добавления пользователя программы с проверкой политики пароля регулярным выражением
            обязательно 3 цифры + символ + 4 буквы, в базу данных записывается только хэш пароля
            """
            role = role_input.get()
            login = login_input.get()
            password = pass_input.get()
            if not role.isalpha() and not login.isdigit():
                # '^\d{3}.\w{4}$' * match * 123abcde || '[A-Z][a-z]+\d{3}' * match * Abcde123
                result = re.findall(r'^\d{3}.\w{4}$', password)
                if result:
                    enc_pass = password.encode('utf-8')
                    md5_pass = hashlib.md5(enc_pass)
                    hash_pass = md5_pass.hexdigest()
                    M_Dealer.add_User(role, login, hash_pass)
                    var1.set('Успешно...')
                else:
                    var1.set('Пароль не отвечает политике 3 цифры/ символ/ 4 буквы')
            else:
                var1.set('Логиин не может быть числом, а роль буквой')


        def exit_add_user(event):
            win_adduser.destroy()

        but_adduser = Button(fra2, text="Добавить", width=20, height=2, bg="lightblue", font="Arial 10",
                         activebackground='lightgreen')
        but_exit = Button(fra2, text="Выход", width=20, height=2, bg="lightblue", font="Arial 10",
                          activebackground='lightgreen')

        but_adduser.bind('<Button-1>', add_user)
        but_exit.bind('<Button-1>', exit_add_user)

        fra1.pack(side='left')
        label_role.pack()
        role_input.pack()
        label_login.pack()
        login_input.pack()
        label_pass.pack()
        pass_input.pack()
        fra2.pack(side='left')
        but_adduser.pack()
        but_exit.pack()
        label_logo.pack(side='right')
        message_box_adduser.pack(side='left')

    ################################################################################################################
    # Окно добавить легковое авто
    def window_add_Cars(event):

        win_addcars = Toplevel(root, bd=10)
        win_addcars.title("Добвление авто")
        win_addcars.minsize(width=450, height=50)
        fra1 = Frame(win_addcars, width=250, height=45, bg="lightblue", bd=10)
        fra2 = Frame(win_addcars, width=250, height=45, bd=20)
        logo = PhotoImage(file=".//libs//logo.gif")
        label_logo = Label(fra2, image=logo)
        label_logo.photo = logo
        var1 = StringVar()
        message_box_addcars = Message(fra1, textvariable=var1, width=150, bg="lightblue")


        def add_auto(event):
            """
            Функция добавления авто с проверкой вводимых значений (целые числа)
            """
            try:
                year = int(year_input.get())
                power = int(power_input.get())
                price = int(price_input.get())
                color = color_input.get()
                model = model_input.get()
                a_type = a_type_input.get()
                fuel = fuel_input.get()
                country = country_input.get()
                if color.isalpha() and model.isalpha() and a_type.isalpha() and fuel.isalpha() and country.isalpha():
                    M_Dealer.add_Car(year, color, model, a_type, power, fuel, country, price, 1)
                    var1.set('Успешно добавлен')
                else:
                    var1.set('Внимание! Модель || Цвет || Тип авто || Страна || Тип двигателя  не должны быть числом. Внесите правильно все данные в поля.')
            except ValueError:
                #print('Внимание! Год || Мощность || Цена должны быть числом. Внесите все данные в поля.')
                var1.set('Внимание! Год || Мощность || Цена должны быть числом. Внесите все данные в поля.')


        def exit_add_cars(event):

            win_addcars.destroy()

        # Блокировка родительского окна
        #win_addcars.grab_set()

        # Назначение ярлыков
        label_year = Label(fra1, text="Год выпуска:", font="Arial 11", bg="lightblue")
        label_color = Label(fra1, text="Цвет:", font="Arial 11", bg="lightblue")
        label_model = Label(fra1, text="Модель:", font="Arial 11", bg="lightblue")
        label_a_type = Label(fra1, text="Тип кузова:", font="Arial 11", bg="lightblue")
        label_power = Label(fra1, text="Мощность:", font="Arial 11", bg="lightblue")
        label_fuel = Label(fra1, text="Тип двигателя (бензин / дизель):", font="Arial 11", bg="lightblue")
        label_country = Label(fra1, text="Страна произваодства:", font="Arial 11", bg="lightblue")
        label_price = Label(fra1, text="Цена:", font="Arial 11", bg="lightblue")
        # Назначение текстовых полей ввода
        year_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        color_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        model_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        a_type_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        power_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        fuel_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        country_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        price_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        # Назначение кнопок
        but_add = Button(fra2, text="Добавить", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')
        but_exit = Button(fra2, text="Выход", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')
        # Привязка кнопок
        but_add.bind('<Button-1>', add_auto)
        but_exit.bind('<Button-1>', exit_add_cars)
        # Отрисовка фреймов, ярлыков, полей, кнопок
        fra1.pack(side='left')
        label_year.pack()
        year_input.pack()
        label_model.pack()
        model_input.pack()
        label_color.pack()
        color_input.pack()
        label_a_type.pack()
        a_type_input.pack()
        label_power.pack()
        power_input.pack()
        label_fuel.pack()
        fuel_input.pack()
        label_country.pack()
        country_input.pack()
        label_price.pack()
        price_input.pack()
        fra2.pack(side='left')
        but_add.pack()
        but_exit.pack()
        label_logo.pack(side='right')
        message_box_addcars.pack(side='left')

    ###############################################################################################################
    # Окно добавление грузовика
    def window_add_Lorry(event):

        win_addlorry = Toplevel(root, bd=10)
        win_addlorry.title("Добвление авто")
        win_addlorry.minsize(width=450, height=50)
        fra1 = Frame(win_addlorry, width=250, height=45, bg="lightblue", bd=10)
        fra2 = Frame(win_addlorry, width=250, height=45, bd=20)
        logo = PhotoImage(file=".//libs//logo.gif")
        label_logo = Label(fra2, image=logo)
        label_logo.photo = logo
        var1 = StringVar()
        message_box_addlorry = Message(fra1, textvariable=var1, width=150, bg="lightblue")


        def add_lorry(event):

            try:
                year = int(year_input.get())
                power = int(power_input.get())
                price = int(price_input.get())
                cargo = float(cargo_input.get())
                color = color_input.get()
                model = model_input.get()
                a_type = a_type_input.get()
                fuel = fuel_input.get()
                country = country_input.get()
                if color.isalpha() and model.isalpha() and a_type.isalpha() and fuel.isalpha() and country.isalpha():
                    M_Dealer.add_Lorry(year, color, model, a_type, power, fuel, country, price, 1, cargo)
                    var1.set('Успешно добавлен')
                else:
                    var1.set('Внимание! Модель || Цвет || Тип авто || Страна || Тип двигателя  не должны быть числом. Внесите правильно все данные в поля.')
            except ValueError:
                #print('Внимание! Год || Мощность || Цена должны быть числом. Внесите все данные в поля.')
                var1.set('Внимание! Год || Мощность || Цена должны быть числом. Внесите правильно все данные в поля.')


        def exit_add_lorry(event):

            win_addlorry.destroy()

        #win_addlorry.grab_set()

        label_year = Label(fra1, text="Год выпуска:", font="Arial 11", bg="lightblue")
        label_color = Label(fra1, text="Цвет:", font="Arial 11", bg="lightblue")
        label_model = Label(fra1, text="Модель:", font="Arial 11", bg="lightblue")
        label_a_type = Label(fra1, text="Тип кузова:", font="Arial 11", bg="lightblue")
        label_power = Label(fra1, text="Мощность:", font="Arial 11", bg="lightblue")
        label_fuel = Label(fra1, text="Тип двигателя (бензин / дизель):", font="Arial 11", bg="lightblue")
        label_country = Label(fra1, text="Страна произваодства:", font="Arial 11", bg="lightblue")
        label_price = Label(fra1, text="Цена:", font="Arial 11", bg="lightblue")
        label_cargo = Label(fra1, text="Грузоподъемность:", font="Arial 11", bg="lightblue")

        year_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        color_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        model_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        a_type_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        power_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        fuel_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        country_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        cargo_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        price_input = Entry(fra1, width=40, bd=3, bg="lightyellow")

        but_add = Button(fra2, text="Добавить", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')
        but_exit = Button(fra2, text="Выход", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')

        but_add.bind('<Button-1>', add_lorry)
        but_exit.bind('<Button-1>', exit_add_lorry)

        fra1.pack(side='left')
        label_year.pack()
        year_input.pack()
        label_model.pack()
        model_input.pack()
        label_color.pack()
        color_input.pack()
        label_a_type.pack()
        a_type_input.pack()
        label_power.pack()
        power_input.pack()
        label_fuel.pack()
        fuel_input.pack()
        label_country.pack()
        country_input.pack()
        label_cargo.pack()
        cargo_input.pack()
        label_price.pack()
        price_input.pack()
        fra2.pack(side='left')
        but_add.pack()
        but_exit.pack()
        label_logo.pack(side='right')
        message_box_addlorry.pack(side='left')

    ###############################################################################################################
    # Окно удаление авто
    def window_del_Cars(event):

        win_delcars = Toplevel(root, bd=10)
        win_delcars.title("Удаление авто")
        win_delcars.minsize(width=250, height=50)
        fra1 = Frame(win_delcars, width=200, height=45, bg="lightblue", bd=10)
        fra2 = Frame(win_delcars, width=200, height=45, bd=20)
        var1 = StringVar()
        message_box_delcars = Message(fra1, textvariable=var1, width=150, bg="lightblue")


        def del_auto(event):
            """
            Функция удаления авто с проверкой значений (целые числа)
            """
            try:
                id_auto = int(id_input.get())
                M_Dealer.del_Car(id_auto)
                var1.set('Успешно удалено')
            except ValueError:
                #print('Внимание! Id авто должно быть числом')
                var1.set('Внимание! Id авто должно быть числом')


        def exit_del_auto(event):

            win_delcars.destroy()

        #win_delcars.grab_set()

        label_id = Label(fra1, text="Id авто:", font="Arial 11", bg="lightblue")
        id_input = Entry(fra1, width=10, bd=3, bg="lightyellow")

        but_add = Button(fra2, text="Удалить", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')
        but_exit = Button(fra2, text="Выход", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')

        but_add.bind('<Button-1>', del_auto)
        but_exit.bind('<Button-1>', exit_del_auto)

        fra1.pack(side='left')
        label_id.pack()
        id_input.pack()
        message_box_delcars.pack(side='left')
        fra2.pack(side='left')
        but_add.pack()
        but_exit.pack()

    #################################################################################################################
    # Удаление грузовика
    def window_del_Lorry(event):

        win_dellorry = Toplevel(root, bd=10)
        win_dellorry.title("Удаление грузовика")
        win_dellorry.minsize(width=250, height=50)
        fra1 = Frame(win_dellorry, width=200, height=45, bg="lightblue", bd=10)
        fra2 = Frame(win_dellorry, width=200, height=45, bd=20)
        var1 = StringVar()
        message_box_dellorry = Message(fra1, textvariable=var1, width=150, bg="lightblue")


        def del_lorry(event):

            try:
                id_lorry = int(id_input.get())
                M_Dealer.del_Lorry(id_lorry)
                var1.set('Успешно удалено')
            except ValueError:
                #print('Внимание! Id грузовика должно быть числом')
                var1.set('Внимание! Id грузовика должно быть числом')


        def exit_del_lorry(event):

            win_dellorry.destroy()

        #win_dellorry.grab_set()

        label_id = Label(fra1, text="Id грузовика:", font="Arial 11", bg="lightblue")
        id_input = Entry(fra1, width=10, bd=3, bg="lightyellow")

        but_add = Button(fra2, text="Удалить", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')
        but_exit = Button(fra2, text="Выход", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')

        but_add.bind('<Button-1>', del_lorry)
        but_exit.bind('<Button-1>', exit_del_lorry)

        fra1.pack(side='left')
        label_id.pack()
        id_input.pack()
        message_box_dellorry.pack(side='left')
        fra2.pack(side='left')
        but_add.pack()
        but_exit.pack()

    #################################################################################################################
    # Окно продажа авто
    def window_sell_Auto(event):

        win_sellcars = Toplevel(root, bd=10)
        win_sellcars.title("Продажа авто")
        win_sellcars.minsize(width=250, height=50)
        fra1 = Frame(win_sellcars, width=200, height=45, bg="lightblue", bd=20)
        fra2 = Frame(win_sellcars, width=200, height=45, bd=20)
        var1 = StringVar()
        # Список радиокнопок
        var2 = IntVar()
        var2.set(0)
        rad0 = Radiobutton(fra2, text="легковое", font="Arial 11", variable=var2, value=0)
        rad1 = Radiobutton(fra2, text="грузовое", font="Arial 11", variable=var2, value=1)
        message_box_sellcars = Message(fra1, textvariable=var1, width=150, bg="lightblue")


        def sell_car(event):
            """
            Функция продать легковое авто с проверкой значений ID (целые числа)
            """
            try:
                id_car = int(id_car_input.get())
                id_client = int(id_client_input.get())
                M_Dealer.sell_Car(id_client, id_car)
                var1.set('Успешно продано')
            except ValueError:
                #print('Внимание! Id  должно быть числом')
                var1.set('Внимание! Id  должно быть числом')


        def sell_lorry(event):
            """
            Функция продать грузовое авто с проверкой значений ID (целые числа)
            """
            try:
                id_car = int(id_car_input.get())
                id_client = int(id_client_input.get())
                M_Dealer.sell_Lorry(id_client, id_car)
                var1.set('Успешно продано')
            except ValueError:
                #print('Внимание! Id  должно быть числом')
                var1.set('Внимание! Id  должно быть числом')


        def sell(event):
            """
            Функция выбора продажи леговое или грузовое авто
            """
            if var2.get():
                sell_lorry('<Button-1>')
            else:
                sell_car('<Button-1>')


        def exit_sell_Auto(event):

            win_sellcars.destroy()

        #win_sellcars.grab_set()

        label_id_car = Label(fra1, text="Id авто:", font="Arial 11", bg="lightblue")
        label_id_client = Label(fra1, text="Id клиента:", font="Arial 11", bg="lightblue")
        label_type = Label(fra2, text="Тип авто:", font="Arial 11")
        id_client_input = Entry(fra1, width=10, bd=3, bg="lightyellow")
        id_car_input = Entry(fra1, width=10, bd=3, bg="lightyellow")

        but_sell = Button(fra2, text="Продать", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')
        but_exit = Button(fra2, text="Выход", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')

        but_sell.bind('<Button-1>', sell)
        but_exit.bind('<Button-1>', exit_sell_Auto)

        fra1.pack(side='left')
        label_id_car.pack()
        id_car_input.pack()
        label_id_client.pack()
        id_client_input.pack()

        message_box_sellcars.pack(side='left')
        fra2.pack(side='left')
        label_type.pack()
        rad0.pack()
        rad1.pack()
        but_sell.pack()
        but_exit.pack()

    #################################################################################################################
    # Окно добавление клиента
    def window_add_client(event):

        win_clnt = Toplevel(root, bd=10)
        win_clnt.title("Добвление клиента")
        win_clnt.minsize(width=500, height=50)
        fra1 = Frame(win_clnt, width=250, height=45, bg="lightblue", bd=10)
        fra2 = Frame(win_clnt, width=250, height=45, bd=20)


        def add_client(event):
            '''
            Функция добавление клиента с проверкой полей (имя - буквы, адрес- буквы и цифры)
            '''
            name = name_input.get()
            adress = adress_input.get()
            tel = tel_input.get()
            if not name.isdigit() and adress.isalnum() and not tel.isalpha():
                M_Dealer.add_Client(name, adress, tel)
                var1.set('Клиент добавлен')
            else:
                var1.set('Имя и адрес не должны быть числом, телефон не должен состоять из букв')


        def exit_client(event):

            win_clnt.destroy()

        #win_clnt.grab_set()

        var1 = StringVar()
        message_box_client = Message(fra1, textvariable=var1, width=150, bg="lightblue")
        label_name = Label(fra1, text="Имя Фамилия:", font="Arial 11", bg="lightblue")
        label_adress = Label(fra1, text="Адрес:", font="Arial 11", bg="lightblue")
        label_tel = Label(fra1, text="Телефон:", font="Arial 11", bg="lightblue")
        name_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        adress_input = Entry(fra1, width=40, bd=3, bg="lightyellow")
        tel_input = Entry(fra1, width=40, bd=3, bg="lightyellow")

        but_add = Button(fra2, text="Добавить", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')
        but_exit = Button(fra2, text="Выход", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')

        but_add.bind('<Button-1>', add_client)
        but_exit.bind('<Button-1>', exit_client)

        fra1.pack(side='left')
        label_name.pack()
        name_input.pack()
        label_adress.pack()
        adress_input.pack()
        label_tel.pack()
        tel_input.pack()
        fra2.pack(side='left')
        but_add.pack()
        but_exit.pack()
        message_box_client.pack(side='left')

    ################################################################################################################
    # Удаление клиента
    def window_del_client(event):

        win_dclnt = Toplevel(root, bd=10)
        win_dclnt.title("Удалить клиента")
        win_dclnt.minsize(width=250, height=50)
        fra1 = Frame(win_dclnt, width=200, height=45, bg="lightblue", bd=10)
        fra2 = Frame(win_dclnt, width=200, height=45, bd=20)


        def exit_del_client(event):

            win_dclnt.destroy()

        #win_dclnt.grab_set()


        def del_client(event):
            """
            Функция удаление клиента с проверкой значений ID - целое число
            """
            try:
                id_client = int(id_input.get())
                M_Dealer.del_Client(id_client)
                var1.set('Успешно удален')
            except ValueError:
                var1.set('Внимание! Id клиента должен быть числом')
                #print('Внимание! Id клиента должен быть числом')

        var1 = StringVar()
        message_box_client = Message(fra1, textvariable=var1, width=150, bg="lightblue")
        label_id = Label(fra1, text="ID клиента:", font="Arial 11", bg="lightblue")
        id_input = Entry(fra1, width=10, bd=3, bg="lightyellow")

        but_del = Button(fra2, text="Удалить", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')
        but_exit = Button(fra2, text="Выход", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')

        but_del.bind('<Button-1>', del_client)
        but_exit.bind('<Button-1>', exit_del_client)

        fra1.pack(side='left')
        label_id.pack()
        id_input.pack()
        fra2.pack(side='left')
        but_del.pack()
        but_exit.pack()
        message_box_client.pack(side='left')

    #################################################################################################################
    # Окно просмотр проданных авто
    def window_selled_cars(event):

        win_selledcars = Toplevel(root, bd=10)
        win_selledcars.title("Проданные авто")
        win_selledcars.minsize(width=250, height=50)
        fra1 = Frame(win_selledcars, width=200, height=45, bg="lightblue", bd=10)
        fra2 = Frame(win_selledcars, width=200, height=45, bd=20)
        logo = PhotoImage(file=".//libs//logo.gif")
        label_logo = Label(fra2, image=logo)
        label_logo.photo = logo
        label = Label(fra1, text="-=- M-Dealer Auto -=-", font="Georgia 11 bold", bg="lightblue")
        var1 = StringVar()
        message_box_selledcars = Message(fra2, textvariable=var1, width=150)


        def exit_selled(event):

            win_selledcars.destroy()

        #win_selledcars.grab_set()


        def printer_selled_Cars(event):
            """
            Функция просмотра всех проданных авто с их покупателями
            """
            cars_lst = M_Dealer.printer_Selled_Cars()
            text_entry_selled.delete(0.0, END)
            text_entry_selled.insert(0.0, '{:<5}{:<6}{:<8}{:<8}{:<15}{:<10}{:<8}{:<18}{:<10}'.format('Год',
            'Цвет', 'Модель', 'Тип', 'Мощность л.с.', 'Двигатель', 'Страна', 'Цена тыс. руб.', 'Грузоподъемность т.' + '\n'))
            text_entry_selled.insert(2.0, '-' * 128 + '\n')
            for row in cars_lst:
                decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                buyer = M_Dealer.get_Client(decoded_row[8])
                for row in buyer:
                    decoded_row2 = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                text_entry_selled.insert(3.0, str(decoded_row).strip('()').replace('\'', '') + '\n' + 'Покупатель: '
                                         + str(decoded_row2).strip('()').replace('\'', '') + '\n')
            var1.set('Список проданных авто и их покупателей')


        text_entry_selled = Text(fra1, width=80, height=20, font='Verdana 9', wrap=WORD)
        # Скролбар для текстового поля вывода всех проданных авто
        scrl = Scrollbar(fra1, command=text_entry_selled.yview)
        text_entry_selled.configure(yscrollcommand=scrl.set)

        but_exit = Button(fra2, text="Выход", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')
        but_selled_cars = Button(fra2, text="Просмотр", width=20, height=2, bg="lightblue", font="Arial 10", activebackground='lightgreen')

        but_exit.bind('<Button-1>', exit_selled)
        but_selled_cars.bind('<Button-1>', printer_selled_Cars)

        fra1.pack(side='left')
        label.pack()
        text_entry_selled.pack(side='left')
        scrl.pack(side='left', fill=Y)

        fra2.pack(side='left')
        but_selled_cars.pack()
        but_exit.pack()
        label_logo.pack()
        message_box_selledcars.pack(side='right')

    ##############################################################################################################
    # Кнопки главного окна администратор
    but_selled_crs = Button(fra2, text="Проданные авто", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_add_cars = Button(fra2, text="Добавить авто", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_del_cars = Button(fra2, text="Удалить авто", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_add_lorry = Button(fra2, text="Добавить грузовик", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_del_lorry = Button(fra2, text="Удалить грузовик", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_find_cars = Button(fra2, text="Все авто", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_sell_auto = Button(fra2, text="Продать авто", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_find_client = Button(fra2, text="Просмотр клиентов", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_add_client = Button(fra2, text="Добавить клиента", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_del_client = Button(fra2, text="Удалить клиента", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_upload_selled = Button(fra2, text="Выгрузка данных", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_add_users = Button(fra2, text="Добавить пользователя", width=20, height=1, bg="lightblue", font="Arial 10", activebackground='lightgreen')
    but_exit = Button(fra2, text="Выход", width=20, height=1, bg="lightblue", font="Arial 10 ", activebackground='lightgreen')
    # Привязка функций к кнопкам главного окна администратор
    but_add_cars.bind('<Button-1>', window_add_Cars)
    but_del_cars.bind('<Button-1>', window_del_Cars)
    but_find_cars.bind('<Button-1>', printer_Cars)
    but_find_client.bind('<Button-1>', printer_Clients)
    but_add_lorry.bind('<Button-1>', window_add_Lorry)
    but_del_lorry.bind('<Button-1>', window_del_Lorry)
    but_sell_auto.bind('<Button-1>', window_sell_Auto)
    but_add_client.bind('<Button-1>', window_add_client)
    but_del_client.bind('<Button-1>', window_del_client)
    but_exit.bind('<Button-1>', exit_main)
    but_selled_crs.bind('<Button-1>', window_selled_cars)
    but_add_users.bind('<Button-1>', window_add_user)
    but_upload_selled.bind('<Button-1>', upload_selled_Cars)
    # отрисовка главного окна администратор
    fra1.pack(side='left')
    label.pack()
    text_entry.pack(expand=YES, fill=BOTH)
    message_box.pack(side='left')
    fra2.pack(side='left')
    but_find_cars.pack()
    but_selled_crs.pack()
    but_add_cars.pack()
    but_del_cars.pack()
    but_add_lorry.pack()
    but_del_lorry.pack()
    but_sell_auto.pack()
    but_find_client.pack()
    but_add_client.pack()
    but_del_client.pack()
    but_add_users.pack()
    but_upload_selled.pack()
    but_exit.pack()
    label_logo.pack(side='right')

    root.mainloop()
########################################################################################################################
# Окно пользователя
def user():

    root_a.destroy()
    root = Tk()
    root.title("Автосалон 'М-Дилер'")

    fra1 = Frame(root, width=500, height=100, bg="lightblue", bd=60)
    fra2 = Frame(root, width=500, height=100, bd=20)
    # Логотип
    logo = PhotoImage(file=".//libs//logo.gif")
    label_logo = Label(fra2, image=logo)
    label_logo.photo = logo
    label = Label(fra1, text="-=- M-Dealer Auto - our cars is the Best for you -=-", font="Georgia 11 bold",
                  bg="lightblue")
    text_entry = Text(fra1, width=80, height=20, font="Verdana 10", wrap=WORD)
    # Виджет  текстовых сообщений работы программы
    var = StringVar()
    message_box = Message(fra1, textvariable=var, width=150, bg="lightblue")
    # Кнопки главного окна пользователь
    but_selled_crs = Button(fra2, text="Проданные авто", width=20, height=1, bg="lightblue", font="Arial 10",
                            activebackground='lightgreen')
    but_find_cars = Button(fra2, text="Все авто", width=20, height=1, bg="lightblue", font="Arial 10",
                           activebackground='lightgreen')
    but_sell_auto = Button(fra2, text="Продать авто", width=20, height=1, bg="lightblue", font="Arial 10",
                           activebackground='lightgreen')
    but_find_client = Button(fra2, text="Просмотр клиентов", width=20, height=1, bg="lightblue", font="Arial 10",
                             activebackground='lightgreen')
    but_upload_selled = Button(fra2, text="Выгрузка данных", width=20, height=1, bg="lightblue", font="Arial 10",
                               activebackground='lightgreen')
    but_exit = Button(fra2, text="Выход", width=20, height=1, bg="lightblue", font="Arial 10 ",
                      activebackground='lightgreen')


    def printer_Cars(event):
        """
        Функция просмотра всех авто
        """
        cars_lst = M_Dealer.printer_Cars()
        text_entry.delete(0.0, END)
        text_entry.insert(0.0, '{:<3}{:<8}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}{:<8}'.format('Id', 'Год',
        'Цвет', 'Модель', 'Тип', 'Мощность л.с.', 'Двигатель', 'Страна', 'Цена тыс. руб.' + '\n'))
        text_entry.insert(2.0, '-' * 91 + '\n')
        for row in cars_lst:
            decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
            text_entry.insert(3.0, '{:<3}|{:<8}|{:<10}|{:<10}|{:<10}|{:<5}|{:<15}|{:<10}|{:<8} \n'.format(decoded_row[0],
                                            decoded_row[1], decoded_row[2], decoded_row[3], decoded_row[4], decoded_row[5],
                                            decoded_row[6], decoded_row[7], decoded_row[8]))
            #text_entry.insert(3.0, str(decoded_row).strip('()').replace('\'', '') + '\n')
        var.set('Список авто')


    def printer_Clients(event):
        """
         Функция просмотра всех клиентов
        """
        client_lst = M_Dealer.print_Clients()
        text_entry.delete(0.0, END)
        text_entry.insert(0.0, '{:<4}  {:<30}  {:<35}  {:>25}'. format('Id', 'Имя Фамилия', 'Адрес', 'Телефон' + '\n'))
        text_entry.insert(2.0, '-' * 91 + '\n')
        for row in client_lst:
            decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
            text_entry.insert(3.0, '{:<4}{:<25}{:>35}{:>25}'.format(decoded_row[0], decoded_row[1], decoded_row[2], decoded_row[3]) + '\n')
        var.set('Список клиентов')


    def upload_selled_Cars(event):
        """
        Выгрузка данных о проданных авто и клиентах в TXT файл с использованием многопоточности
        """
        M_Dealer.run_Tread_upload()
        var.set('Успешно...')


    def exit_main(event):
        """
        Функция закрыть окно
        """
        root.destroy()


    # Окно продажа авто
    def window_sell_Auto(event):

        win_sellcars = Toplevel(root, bd=10)
        win_sellcars.title("Продажа авто")
        win_sellcars.minsize(width=250, height=50)
        fra1 = Frame(win_sellcars, width=200, height=45, bg="lightblue", bd=20)
        fra2 = Frame(win_sellcars, width=200, height=45, bd=20)
        var1 = StringVar()
        # Список радиокнопок
        var2 = IntVar()
        var2.set(0)
        rad0 = Radiobutton(fra2, text="легковое", font="Arial 11", variable=var2, value=0)
        rad1 = Radiobutton(fra2, text="грузовое", font="Arial 11", variable=var2, value=1)
        message_box_sellcars = Message(fra1, textvariable=var1, width=150, bg="lightblue")


        def sell_car(event):
            """
            Функция продать легковое авто с проверкой значений ID (целые числа)
            """
            try:
                id_car = int(id_car_input.get())
                id_client = int(id_client_input.get())
                M_Dealer.sell_Car(id_client, id_car)
                var1.set('Успешно продано')
            except ValueError:
                # print('Внимание! Id  должно быть числом')
                var1.set('Внимание! Id  должно быть числом')


        def sell_lorry(event):
            """
            Функция продать грузовое авто с проверкой значений ID (целые числа)
            """
            try:
                id_car = int(id_car_input.get())
                id_client = int(id_client_input.get())
                M_Dealer.sell_Lorry(id_client, id_car)
                var1.set('Успешно продано')
            except ValueError:
                print('Внимание! Id  должно быть числом')
                var1.set('Внимание! Id  должно быть числом')


        def sell(event):
            """
            Функция выбора продажи леговое или грузовое авто
            """
            if var2.get():
                sell_lorry('<Button-1>')
            else:
                sell_car('<Button-1>')


        def exit_sell_Auto(event):

            win_sellcars.destroy()

        # win_sellcars.grab_set()

        label_id_car = Label(fra1, text="Id авто:", font="Arial 11", bg="lightblue")
        label_id_client = Label(fra1, text="Id клиента:", font="Arial 11", bg="lightblue")
        label_type = Label(fra2, text="Тип авто:", font="Arial 11")
        id_client_input = Entry(fra1, width=10, bd=3, bg="lightyellow")
        id_car_input = Entry(fra1, width=10, bd=3, bg="lightyellow")

        but_sell = Button(fra2, text="Продать", width=20, height=2, bg="lightblue", font="Arial 10",
                          activebackground='lightgreen')
        but_exit = Button(fra2, text="Выход", width=20, height=2, bg="lightblue", font="Arial 10",
                          activebackground='lightgreen')

        but_sell.bind('<Button-1>', sell)
        but_exit.bind('<Button-1>', exit_sell_Auto)

        fra1.pack(side='left')
        label_id_car.pack()
        id_car_input.pack()
        label_id_client.pack()
        id_client_input.pack()

        message_box_sellcars.pack(side='left')
        fra2.pack(side='left')
        label_type.pack()
        rad0.pack()
        rad1.pack()
        but_sell.pack()
        but_exit.pack()

    #################################################################################################################
    # Окно просмотр проданных авто
    def window_selled_cars(event):

        win_selledcars = Toplevel(root, bd=10)
        win_selledcars.title("Проданные авто")
        win_selledcars.minsize(width=250, height=50)
        fra1 = Frame(win_selledcars, width=200, height=45, bg="lightblue", bd=10)
        fra2 = Frame(win_selledcars, width=200, height=45, bd=20)
        logo = PhotoImage(file=".//libs//logo.gif")
        label_logo = Label(fra2, image=logo)
        label_logo.photo = logo
        label = Label(fra1, text="-=- M-Dealer Auto -=-", font="Georgia 11 bold", bg="lightblue")
        var1 = StringVar()
        message_box_selledcars = Message(fra2, textvariable=var1, width=150)


        def exit_selled(event):

            win_selledcars.destroy()

        # win_selledcars.grab_set()


        def printer_selled_Cars(event):
            """
            Функция просмотра всех проданных авто с покупателями
            """
            cars_lst = M_Dealer.printer_Selled_Cars()
            text_entry_selled.delete(0.0, END)
            text_entry_selled.insert(0.0, '{:<5}{:<6}{:<8}{:<8}{:<15}{:<10}{:<8}{:<18}{:<10}'.format('Год',
                                                                                                     'Цвет',
                                                                                                     'Модель',
                                                                                                     'Тип',
                                                                                                     'Мощность л.с.',
                                                                                                     'Двигатель',
                                                                                                     'Страна',
                                                                                                     'Цена тыс. руб.',
                                                                                                     'Грузоподъемность т.' + '\n'))
            text_entry_selled.insert(2.0, '-' * 128 + '\n')
            for row in cars_lst:
                decoded_row = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                buyer = M_Dealer.get_Client(decoded_row[8])
                for row in buyer:
                    decoded_row2 = tuple([el.decode('utf-8') if type(el) is bytearray else el for el in row])
                text_entry_selled.insert(3.0, str(decoded_row).strip('()').replace('\'', '') + '\n' + 'Покупатель: '
                                         + str(decoded_row2).strip('()').replace('\'', '') + '\n')
            var1.set('Список проданных авто и их покупателей')


        text_entry_selled = Text(fra1, width=80, height=20, font='Verdana 9', wrap=WORD)
        # Скролбар для текстового поля вывода всех проданных авто
        scrl = Scrollbar(fra1, command=text_entry_selled.yview)
        text_entry_selled.configure(yscrollcommand=scrl.set)

        but_exit = Button(fra2, text="Выход", width=20, height=2, bg="lightblue", font="Arial 10",
                          activebackground='lightgreen')
        but_selled_cars = Button(fra2, text="Просмотр", width=20, height=2, bg="lightblue", font="Arial 10",
                                 activebackground='lightgreen')

        but_exit.bind('<Button-1>', exit_selled)
        but_selled_cars.bind('<Button-1>', printer_selled_Cars)

        fra1.pack(side='left')
        label.pack()
        text_entry_selled.pack(side='left')
        scrl.pack(side='left', fill=Y)

        fra2.pack(side='left')
        but_selled_cars.pack()
        but_exit.pack()
        label_logo.pack()
        message_box_selledcars.pack(side='right')

    ##############################################################################################################
    # Привязка функций к кнопкам главного окна пользователь
    but_find_cars.bind('<Button-1>', printer_Cars)
    but_find_client.bind('<Button-1>', printer_Clients)
    but_sell_auto.bind('<Button-1>', window_sell_Auto)
    but_exit.bind('<Button-1>', exit_main)
    but_selled_crs.bind('<Button-1>', window_selled_cars)
    but_upload_selled.bind('<Button-1>', upload_selled_Cars)
    # отрисовка главного окна пользователь
    fra1.pack(side='left')
    label.pack()
    text_entry.pack(expand=YES, fill=BOTH)
    message_box.pack(side='left')
    fra2.pack(side='left')
    but_find_cars.pack()
    but_selled_crs.pack()
    but_sell_auto.pack()
    but_find_client.pack()
    but_upload_selled.pack()
    but_exit.pack()
    label_logo.pack(side='right')

    root.mainloop()

# Отрисовка кнопок и полей окна авторизации , функции авторизации и чистки стиля полей ввода
def auth(event):
    """
    Функция авторизации пользователя в программе (проверяет хэш пароля с данными в базе)
    """
    lgn = login.get()
    psw = password.get()
    if psw.isalnum() or lgn.isalpha() or lgn.isalnum():
        enc_pasw = psw.encode('utf-8')
        md5_pasw = hashlib.md5(enc_pasw)
        hash_pasw = md5_pasw.hexdigest()
        answer = M_Dealer.auth_to(lgn, hash_pasw)
        if answer[0] == 0:
            user()
        if answer[0] == 1:
            admin()
        else:
            try:
                login['relief'] = 'solid'
                login['bg'] = 'lightgrey'
                password['relief'] = 'solid'
                password['bg'] = 'lightgrey'
                var_a.set('Не верный логин-пароль')
            except TclError:
                pass
    else:
        var_a.set('Не верно введены данные')


def clear_entry_log(event):
    """
    Функция очистки стиля текстовых полей ввода в случае не верного ввода данных
    """
    try:
        login['relief'] = 'sunken'
        login['bg'] = 'lightyellow'
    except TclError:
        pass


def clear_entry_pass(event):

    try:
        password['relief'] = 'sunken'
        password['bg'] = 'lightyellow'
    except TclError:
        pass
# Привязка текстовых полей ввода к функциям очистки полей
login.bind('<ButtonRelease>', clear_entry_log)
password.bind('<ButtonRelease>', clear_entry_pass)

but_auth.bind('<Button-1>', auth)
label_login.pack()
login.pack()
label_password.pack()
password.pack()
message_box_a.pack()
but_auth.pack()

root_a.mainloop()