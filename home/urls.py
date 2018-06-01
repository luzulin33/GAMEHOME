#!/usr/local/python3/bin/python3
from django.conf.urls import url
from home import views
urlpatterns = [
    url(r'^index/', views.index),
    url(r'^upload/', views.upload, name='upload'),

]