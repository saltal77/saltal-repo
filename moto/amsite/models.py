from django.db import models

class Info(models.Model):

    name = models.CharField(verbose_name='Название', max_length=20, default='Главная')
    text = models.TextField(verbose_name='О мотоциклах')

    def __str__(self):
        return '{}'.format(self.name)


class Revw(models.Model):

    title = models.CharField(verbose_name='Название', max_length=20, unique=True)
    mark = models.ForeignKey('Mark')
    image = models.ImageField(verbose_name='Фото', blank=True, upload_to='img')
    text = models.TextField(verbose_name='Отзыв', blank=True)
    author = models.CharField(verbose_name='Автор', max_length=15, default='admin')
    rating = models.PositiveIntegerField(verbose_name='рейтинг', default=0)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.title,  self.author, self.create_date)


class Mark(models.Model):

    name = models.CharField(verbose_name='Название марки', max_length=20, unique=True)
    description = models.TextField(verbose_name='Описание марки', blank=True)

    def __str__(self):
        return '{}'.format(self.name)



class Descript(models.Model):

    title = models.CharField(verbose_name='Название', max_length=20, unique=True)
    mark = models.ForeignKey('Mark')
    text = models.TextField(verbose_name='Отзыв', blank=True)
    image = models.ImageField(verbose_name='Фото', blank=True, upload_to='img')

    def __str__(self):
        return '{} '.format(self.title)


class MotoStories(models.Model):

    title = models.CharField(verbose_name='Название', max_length=20, unique=True)
    mark = models.ForeignKey('Mark')
    image = models.ImageField(verbose_name='Фото', blank=True, upload_to='img')
    text = models.TextField(verbose_name='Событие', blank=True)
    author = models.CharField(verbose_name='Автор', max_length=15, default='admin')
    rating = models.PositiveIntegerField(verbose_name='рейтинг', default=0)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.title,  self.author, self.create_date)



class MotoExploit(models.Model):

    title = models.CharField(verbose_name='Название', max_length=20, unique=True)
    mark = models.ForeignKey('Mark')
    text = models.TextField(verbose_name='Опыт', blank=True)
    author = models.CharField(verbose_name='Автор', max_length=15, default='admin')

    def __str__(self):
        return '{} {}'.format(self.title,  self.author)

class MotoCharacter(models.Model):

    title = models.CharField(verbose_name='Название', max_length=20, unique=True)
    mark = models.ForeignKey('Mark')
    text = models.TextField(verbose_name='Опыт', blank=True)
    rating = models.PositiveIntegerField(verbose_name='рейтинг', default=0)

    def __str__(self):
        return '{}'.format(self.title)
