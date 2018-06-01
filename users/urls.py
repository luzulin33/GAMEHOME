#!/usr/local/python3/bin/python3
from django.conf.urls import url
from users import views
urlpatterns = [
    url(r'^register/', views.register)
]