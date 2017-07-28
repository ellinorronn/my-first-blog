from django.conf.urls import url
from . import views

urlpatterns = [
#    url(r'^$', views.post_list, name='post_list'),
	url(r'^$', views.index, name='index'),
    url(r'^blog/post/(?P<pk>\d+)', views.post_detail, name='post_detail'),
    url(r'^blog/post/new', views.post_new, name='post_new'),
	url(r'^test', views.test, name='test'),
	url(r'^blog', views.blog, name='blog'),
]

