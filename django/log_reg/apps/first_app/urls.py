from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^processreg$', views.processreg),
    url(r'^processlog$', views.processlog),
    url(r'^index2$', views.index2),
    url(r'^logout$', views.logout)
      
]                            