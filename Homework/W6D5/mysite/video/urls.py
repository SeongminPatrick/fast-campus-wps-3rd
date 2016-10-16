from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.video_list, name='video_list'),
    url(r'^video/(?P<pk>[0-9]+)/$', views.video_detail, name='video_detail'),
    url(r'^video/add/$', views.video_add, name='video_add'),
    url(r'^video/category/add/$', views.category_add, name='category_add'),
    url(r'^video/(?P<pk>[0-9]+)/edit/$', views.video_edit, name='video_edit'),
]
