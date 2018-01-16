from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^event_details$',views.eventDetails , name='event'),
    url(r'^(?P<userId>[0-9]+)/$', views.getEvent, name= 'getEvent'),
]