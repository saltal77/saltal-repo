# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slogan1', 'slogan2']

class MainPageWorksAdmin(admin.ModelAdmin):
    list_display = ['name', 'text']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'town', 'flag']

class InterestAdmin(admin.ModelAdmin):
    list_display = ['theme']

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['act']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(MainPageWorks, MainPageWorksAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Resume)