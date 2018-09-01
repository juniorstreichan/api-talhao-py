from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^talhao/$', TalhaoList.as_view()),
    url(r'^talhao/(?P<id>[0-9]+)$', TalhaoDetail.as_view()),
]
