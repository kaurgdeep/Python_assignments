from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^processform$',views.processform),
    url(r'^reset$', views.reset)
]