from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sects/(?P<sect_id>[0-9]+)/(?P<set_id>[0-9]+)$', views.sett),
    url(r'^sects/(?P<sect_id>[0-9]+)$', views.sect),
    url(r'^$', views.index),
]
