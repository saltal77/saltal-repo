# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Класс Post с полями Название, Автор, Текст, Дата создания
# Через Метакласс меняем название Blog на Запись
# Выводм в админке название + время создания записи

class Post(models.Model):

    title = models.CharField(u'Заголовок', max_length=150)
    author = models.CharField(u'Автор',max_length=15, default='admin')
    text = models.TextField(u'Текст')
    create_date = models.DateTimeField(u'Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = u'Запись'
        verbose_name_plural = u'Записи'

    def __unicode__(self):
        return u'{} {}'.format(self.title, self.create_date)




