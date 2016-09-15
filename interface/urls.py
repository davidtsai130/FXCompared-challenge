from django.conf.urls import url
from . import views

app_name = 'interface'

urlpatterns = [
    #/interface/
    url(r'^$', views.index, name='index'),

    #/interface/new/
    url(r'^new/$', views.new, name='new'),

    #/interface/account_id/
    url(r'^(?P<account_id>[0-9]+)/$', views.show, name='show'),
]
