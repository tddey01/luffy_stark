#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from django.conf.urls import url
from app01.views import index

# app_name = 'app01'
print('读取路由信息')
urlpatterns = [
    url(r'^index/', index.index),
    url(r'^home/', index.home),
]
