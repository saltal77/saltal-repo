# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('santeh', '0004_mainpageworks'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpageworks',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
            preserve_default=False,
        ),
    ]
