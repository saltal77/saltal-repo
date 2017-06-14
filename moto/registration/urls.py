from django.conf.urls import url, include
from amsite.views import *
from .views import *

urlpatterns = [
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^registration/$', registration),
]