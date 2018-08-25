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
    url(r'^create_item$', views.create_item),
    url(r'^wish_item/(?P<item_id>\d+)$',views.wish_item),
    url(r'^addlist/(?P<item_id>\d+)$',views.addlist),
    url(r'^remove_list/(?P<item_id>\d+)$', views.remove_list),
    url(r'^others_item/(?P<item_id>\d+)$',views.wish_item),
    url(r'^delete/(?P<item_id>\d+)$', views.delete)


]                           