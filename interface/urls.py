from django.conf.urls import url
from . import views

urlpatterns = [
    #/interface/
    url(r'^$', views.index, name='index'),

    #/interface/account_id/
    url(r'^(?P<account_id>[0-9]+)/$', views.show, name='show'), 
]
