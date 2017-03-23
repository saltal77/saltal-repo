# coding: utf-8
__author__ = "saltal"

import random


class Lotto_Card:

    def __init__(self, name):
        self.lst2 = []
        self.lst3 = []
        self.lm = []
        self.name = name

    def __str__(self):
        """
        Печать Карточек Лото
        """
        self.lm = [self.lst2[:5], self.lst2[5:10], self.lst2[10:]]
        print("Карточка {}".format(self.name))
        print("-" * 26)
        for i in self.lm:
            print('----'.join(map(str, i)))
        print("-" * 26)
        return "{}".format('')

    def random_card(self):
        """
        Заполнение карточек Лото уникальными случайными числами
        """
        self.lst2 = random.sample(list(range(1,100)), 15)
        return        

    def count_X(self):
        """
        Подсчет количества выпавших чисел (боченков) в соответсвии с числами карточки  
        """
        return self.lst2.count("X")

    def compare(self, b):
        """
        Сравнеие карточек на выпавшие числа (боченки) 
        """
        a = None
        for i in self.lst2:
            if i == b:
                m = self.lst2.index(i)
                self.lst2[m] = 'X'
                a = 1
        return self.lst2, a

b = Lotto_Card("Компьютер") # Генерация карточки
c = Lotto_Card("Человек")

c.random_card() # заполение карточек числами
b.random_card()

print("Игра Лотто")
print(c)
print(b)

# Блок условий
q = None
count = 89

while c.count_X() < 15 and b.count_X() < 15:   
    q = input("Зачеркнуть('y') или продолжить('n') ? ")
    bk = random.randint(1, 90)

    if q == "y":
        print("Выбрано зачеркнуть")
        print("Боченок: ", bk, "осталось: ", count)
        c.compare(bk)
        b.compare(bk)
        count -=1           
        print(c)
        print(b)

    elif q == "n":            
        print("Выбрано продолжить")
        print("Боченок: ", bk, "осталось: ", count)
        if c.compare(bk)[-1] == 1:
            print("Выиграл Компьютер")
            break
        elif b.compare(bk)[-1] == 1:
            print("Выиграл Человек")
            break

    if q == "q":
        break

print("Игра окончена")

