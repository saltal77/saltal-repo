# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santeh', '0005_mainpageworks_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, verbose_name='\u0410\u0432\u0442\u043e\u0440')),
                ('town', models.CharField(max_length=100, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('text', models.TextField(verbose_name='\u041e\u0442\u0437\u044b\u0432')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
            ],
        ),
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name': '\u041e\u0431\u043e \u043c\u043d\u0435', 'verbose_name_plural': '\u041e\u0431\u043e \u043c\u043d\u0435'},
        ),
    ]
