# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santeh', '0014_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='\u0426\u0435\u043d\u0430'),
        ),
    ]
