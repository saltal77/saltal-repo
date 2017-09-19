# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slogan1', 'slogan2']


admin.site.register(AboutMe)