"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from snippets import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('snippets.urls')),
    url(r'^users/$', views.UserList.as_view(), name='users-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^api-auth/', include('rest_framework.urls')),
]

# # with viewSets we can use Routers for simple construction urls
#
# from rest_framework.routers import DefaultRouter
#
# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)
#
# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     url(r'^', include(router.urls))
# ]
