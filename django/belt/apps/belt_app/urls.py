from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index), 
    url(r'^processreg$',views.processreg),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^processlog$', views.processlog),
    url(r'^home$', views.home),
    url(r'^create$', views.create),
    url(r'^create_item$', views.create_item)
]