from django.contrib import admin
from .models import AboutMe, MyLearning, MyJobs, Organizations


class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ['org_name', 'town', 'site', 'email']

class MyJobsAdmin(admin.ModelAdmin):
    list_display = ['name', 'year_on', 'position', 'flag']

class MyLearningAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'edu']


admin.site.register(AboutMe)
admin.site.register(MyLearning, MyLearningAdmin)
admin.site.register(MyJobs,  MyJobsAdmin)
admin.site.register(Organizations, OrganizationsAdmin)

