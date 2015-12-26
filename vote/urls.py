
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view1, name='view1.html'),
]