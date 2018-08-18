from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post_list/$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    
    url(r'^itnews_list/$', views.ItnewsListView.as_view(), name='itnews_list'),
    url(r'^itnews/(?P<pk>\d+)/$', views.ItnewsDetailView.as_view(), name='itnews_detail'),
    url(r'^itnews/new/$', views.ItnewsCreateView.as_view(), name='itnews_new'),
    url(r'^itnews/(?P<pk>\d+)/edit/$', views.ItnewsUpdateView.as_view(), name='itnews_edit'),
    
    url(r'^eventinfo_list/$', views.EventInfoListView.as_view(), name='eventinfo_list'),
    url(r'^eventinfo/(?P<pk>\d+)/$', views.EventInfoDetailView.as_view(), name='eventinfo_detail'),
    url(r'^eventinfo/new/$', views.EventInfoCreateView.as_view(), name='eventinfo_new'),
    url(r'^eventinfo/(?P<pk>\d+)/edit/$', views.EventInfoUpdateView.as_view(), name='eventinfo_edit'),
]