# -*- coding:utf-8 -*-
'''
    Author : Xuefei Chen
    Email : chenxuefei_pp@163.com
    Created on : 2017/7/28 21:35
'''
from django.conf.urls import url

from account.views import login

urlpatterns = [
    url(r'^login/', login),
]