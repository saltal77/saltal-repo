from django.contrib import admin
from .models import Info, Revw, Mark, Descript, MotoStories, MotoExploit, MotoCharacter

class InfoAdmin(admin.ModelAdmin):
    list_display = ['name']

class RevwAdmin(admin.ModelAdmin):
    list_display = ['title', 'mark', 'author']

class MarkAdmin(admin.ModelAdmin):
    list_display = ['name']

class DescAdmin(admin.ModelAdmin):
    list_display = ['title']

class MotoStoriAdmin(admin.ModelAdmin):
    list_display = ['title']

class MotoExploitiAdmin(admin.ModelAdmin):
    list_display = ['title']

class MotoCharacterAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Info, InfoAdmin)
admin.site.register(Revw, RevwAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(Descript, DescAdmin)
admin.site.register(MotoStories, MotoStoriAdmin)
admin.site.register(MotoExploit, MotoExploitiAdmin)
admin.site.register(MotoCharacter, MotoCharacterAdmin)