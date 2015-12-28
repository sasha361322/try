from django.conf.urls import patterns, include, url
from django.conf.urls import url
from . import views



urlpatterns = [
      url(r'^$', views.votes, name='votes.html'),
      url(r'^vote/get/(?P<vote_id>\d+)$', views.vote, name='vote.html'),
    ]