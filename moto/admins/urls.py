from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', admins_work),
    url(r'^get_user_form/(\d+)/$', get_user_form),
    url(r'^create/user/(\d*)$', create_user),
    url(r'^delete/user/(\d+)/$', delete_user, name='delete_user'),
    url(r'review/$', AdminReview.as_view(), name='admin_review'),
    url(r'^create/review$', AdminReviewCreate.as_view(), name='review_create'),
    url(r'^delete/review/(?P<pk>\d+)$', AdminReviewDelete.as_view(), name='review_delete'),
    url(r'^update/review/(?P<pk>\d+)$', AdminReviewUpdate.as_view(), name='review_update'),
    url(r'^detail/review/(?P<pk>\d+)$', AdminReviewDetail.as_view(), name='admin_review_detail'),
]


