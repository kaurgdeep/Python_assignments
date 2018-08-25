from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
     url(r'^processreg$', views.processreg),
    url(r'^friends$', views.success),
    url(r'^logout$', views.logout),
    url(r'^processlog$', views.processlog),
    url(r'^home$', views.home),   # This line has changed! Notice that urlpatterns is a list, the comma is in
]                            # anticipation of all the routes that will be coming soon
