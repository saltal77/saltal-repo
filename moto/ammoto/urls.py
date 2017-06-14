from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from amsite.views import *

urlpatterns = [
    url(r'^$', site_view),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^welcome/', welcome_view),
    url(r'^character/', character_view),
    url(r'^exploit/', exploit_view),
    url(r'^review/', review_view),
    url(r'^revw/details/(\d+)$', review_details, name='review_details'),
    url(r'^motohistory/', motohistory_view),
    url(r'^marks/(\d+)/$', marks_view, name='marks_view'),
]

urlpatterns += [
    url(r'^admins/', include('admins.urls')),
    url(r'^user/', include('registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)