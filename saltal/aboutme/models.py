from django.db import models


class AboutMe(models.Model):

     name = models.CharField(verbose_name='Название', max_length=20, default='Главная')
     text1 = models.CharField(verbose_name='Имя + Родился и вырос', max_length=50)
     text2 = models.TextField(verbose_name='Остальное')

     def __str__(self):
         return '{}'.format(self.name)

class MyLearning(models.Model):

    name = models.CharField(verbose_name='Название', max_length=20, default='Учеба')
    year = models.PositiveIntegerField(verbose_name='Год', default=1)
    place = models.CharField(verbose_name='Учебное заведение', max_length=50)
    edu = models.CharField(verbose_name='Тип образования', max_length=50)

    def __str__(self):
        return '{} {}'.format(self.name, self.year)


class Organizations(models.Model):

    name = models.CharField(verbose_name='Название', max_length=20, default='Организация')
    town = models.CharField(verbose_name='Город', max_length=80)
    org_name = models.CharField(verbose_name='Название фирмы', max_length=80)
    site = models.URLField(verbose_name='Сайт фирмы', max_length=50)
    email = models.EmailField(verbose_name='Электронная почта', max_length=50)
    address = models.CharField(verbose_name='Адрес', max_length=128)
    desc = models.TextField(verbose_name='Описание деятельности')
    sert = models.ImageField(verbose_name='Сертификаты', upload_to='media', null=True)

    def __str__(self):
        return '{} '.format(self.org_name)


class MyJobs(models.Model):

    orgname = models.ForeignKey(Organizations, verbose_name='Организация', null=True)
    name = models.CharField(verbose_name='Название', max_length=20, default='Работа')
    year_on = models.PositiveIntegerField(verbose_name='Год начала работы', default=1)
    year_off = models.PositiveIntegerField(verbose_name='Год окончания работы', default=1)
    position = models.CharField(verbose_name='Должность', max_length=50, default='занимаемая должность')
    duties = models.TextField(verbose_name='Обязанности')
    flag = models.BooleanField(verbose_name='Отобразить на сайте', default=False)

    def display(self):
        return self.flag

    def __str__(self):
        return '{} {}'.format(self.name, self.orgname)
