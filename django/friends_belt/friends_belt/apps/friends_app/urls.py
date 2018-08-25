from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^main$', views.main),
	url(r'^processReg$', views.processReg),
	url(r'^processLog$', views.processLog),
	url(r'^friends$', views.friends),
	url(r'^addFriend/(?P<user_id>\d+)/(?P<id>\d+)$', views.addFriend),
	url(r'^unfriend/(?P<user_id>\d+)/(?P<id>\d+)$', views.unfriend),
	url(r'^user/(?P<user_id>\d+)$', views.users),
	url(r'^logout$', views.logout),
    ]
