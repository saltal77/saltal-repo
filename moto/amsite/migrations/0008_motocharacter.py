# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 08:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amsite', '0007_motoexploit'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotoCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='Название')),
                ('text', models.TextField(blank=True, verbose_name='Опыт')),
                ('rating', models.PositiveIntegerField(default=0, verbose_name='рейтинг')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amsite.Mark')),
            ],
        ),
    ]
