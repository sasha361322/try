from django.conf.urls import patterns, include, url
from django.conf.urls import url
from . import views



urlpatterns = [
      url(r'^$', 'vote.views.votes'),
      url(r'^vote/get/(?P<vote_id>\d+)$', 'vote.views.vote'),
      url(r'^vote/addanswer/(?P<vote_id>\d+)/(\d%)$', 'vote.views.addanswer'),
    ]