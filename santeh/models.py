# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from random import randrange
from django.db import models

@python_2_unicode_compatible
class AboutMe(models.Model):
    name = models.CharField(verbose_name='Название', max_length=20, default='Главная Страница')
    slogan1 = models.CharField(verbose_name='Слоган1', max_length=40)
    slogan2 = models.CharField(verbose_name='Слоган2', max_length=40)
    slogan3 = models.CharField(verbose_name='Слоган3', max_length=40)
    slogan4 = models.CharField(verbose_name='Слоган4', max_length=250,default='Слоган4' )
    about = models.CharField(verbose_name='Информация обо мне', max_length=300)

    class Meta:
        verbose_name = u'Обо мне Главная страница'
        verbose_name_plural = u'Обо мне Главная страница'

    def __str__(self):
       return u'{}'.format(self.name)


@python_2_unicode_compatible
class Resume(models.Model):
    name = models.CharField(verbose_name='Название', max_length=20, default='Страница Обо мне')
    slogan1 = models.TextField(verbose_name='Со мной выгодно', max_length=200)
    slogan2 = models.TextField(verbose_name='Что получаете', max_length=200)
    slogan3 = models.TextField(verbose_name='Ответсвенный подход', max_length=200)
    about = models.TextField(verbose_name='Обо мне - кратко', max_length=500)

    class Meta:
        verbose_name = u'Обо мне Страница Обо мне'
        verbose_name_plural = u'Обо мне Страница Обо мне'

    def __str__(self):
        return u'{}'.format(self.name)


@python_2_unicode_compatible
class MainPageWorks(models.Model):
    name = models.CharField(verbose_name='Название', max_length=20, default='Название работы')
    text = models.CharField(verbose_name='Описание', max_length=40)
    foto = models.ImageField(verbose_name='Фото', upload_to='works', null=True)
    date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def delay(self):
        return randrange(300, 1200, 300)

    class Meta:
        verbose_name = u'Описание работ и фото Главная страница + Галерея'
        verbose_name_plural = u'Описание работ и фото Главная страница + Галерея'

    def __str__(self):
        return u'{} {}'.format(self.name, self.date)

@python_2_unicode_compatible
class Comment(models.Model):
    author = models.CharField(verbose_name='Автор', max_length=30)
    town = models.CharField(verbose_name='Город', max_length=100)
    text = models.TextField(verbose_name='Отзыв')
    date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    flag = models.BooleanField(verbose_name='Отобразить на сайте', default=False)

    class Meta:
        verbose_name = u'Отзывы заказчиков Страница отзывы'
        verbose_name_plural = u'Отзывы заказчиков Страница отзывы'

    def display(self):
        return self.flag

    def __str__(self):
        return u'{} {}'.format(self.author, self.town)

@python_2_unicode_compatible
class Interest(models.Model):
    theme = models.CharField(verbose_name='Тема', max_length=100)
    text = models.TextField(verbose_name='Статья')
    foto = models.ImageField(verbose_name='Фото_Картинка', upload_to='interest', null=True, blank=True)
    date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = u'Интересные статьи Страница интересное'
        verbose_name_plural = u'Интересные статьи Страница интересное'

    def __str__(self):
        return u'{}'.format(self.theme)

@python_2_unicode_compatible
class Discount(models.Model):
    act = models.CharField(verbose_name='Акция', max_length=100)
    text = models.TextField(verbose_name='Описание')
    foto = models.ImageField(verbose_name='Фото_Картинка', upload_to='discount', null=True, blank=True)
    date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = u'Акции Страница акции'
        verbose_name_plural = u'Акции Страница акции'

    # def foto_url(self):
    #     if self.foto and hasattr(self.foto, 'url'):
    #         return self.foto.url
    #     else:
    #         return '/static/images/default_img.jpg'

    def __str__(self):
        return u'{}'.format(self.act)


@python_2_unicode_compatible
class Service(models.Model):
    title = models.CharField(verbose_name='Название Работ', max_length=100)
    text = models.TextField(verbose_name='Описание')
    quanty = models.CharField(verbose_name='Величина Количество Объем', max_length=30, default='шт')
    price = models.DecimalField(verbose_name='Цена',max_digits=8, decimal_places=0, null=True, blank=True)

    class Meta:
        verbose_name = u'Перечень работ Страница Работы'
        verbose_name_plural = u'Перечень работ Страница Работы'

    def delay(self):
        return randrange(600, 1200, 200)

    def __str__(self):
        return u'{}'.format(self.title)



@python_2_unicode_compatible
class Order(models.Model):
    name = models.CharField(verbose_name='Имя отправителя', max_length=50)
    email = models.EmailField(verbose_name='Почта',max_length=80)
    tlf = models.CharField(verbose_name='Телефон', max_length=80, null=True)
    text = models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = u'Заявки Страница контакты'
        verbose_name_plural = u'Заявки Страница контакты'

    def __str__(self):
        return u'{} {}'.format(self.name, self.email)

