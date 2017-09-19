# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class AboutMe(models.Model):
    name = models.CharField(verbose_name='Название', max_length=20, default='Главная Страница')
    slogan1 = models.CharField(verbose_name='Слоган1', max_length=40)
    slogan2 = models.CharField(verbose_name='Слоган2', max_length=40)
    slogan3 = models.CharField(verbose_name='Слоган3', max_length=40)
    slogan4 = models.CharField(verbose_name='Слоган4', max_length=250,default='Слоган4' )
    about = models.CharField(verbose_name='Информация обо мне', max_length=300)

    def __str__(self):
       return u'{}'.format(self.name)
