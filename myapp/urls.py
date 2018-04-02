#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: urls.py
@time: 2018/4/1 12:32
'''
__author__ = 'lierl'

from . import views
from django.conf.urls import url, include

app_name='myapp'

urlpatterns = [
    url(r'^index/', views.index, name="index"),
    url(r'^login/', views.login, name="login"),
    url(r'^register/', views.register, name="register"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^confirm/', views.confirm, name="confirm"),
    url(r'^test/', views.testQuery, name="test"),
]