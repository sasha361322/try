from django.conf.urls import patterns, include, url
from django.conf.urls import url
from . import views



urlpatterns = [
    #url(r'^$', views.view1, name='votes.html'),
    url(r'^vote/get/(?P<vote_id>\d+)$', views.vote, name='vote.html'),
    url(r'^vote/login/$', views.vote, name='login.html'),
    url(r'^vote/reg/$', views.vote, name='reg.html'),
]