# -*- coding:utf-8 -*-
'''
    Author : Xuefei Chen
    Email : chenxuefei_pp@163.com
    Created on : 2017/7/27 10:01
'''

ENV_DJANGO_SETTINGS_DEV = "auth_backend.settings.dev"
ENV_DJANGO_SETTINGS_PROD = "auth_backend.settings.prod"

from auth_backend.settings.base import DEBUG

ENV_DJANGO_SETTINGS = ENV_DJANGO_SETTINGS_DEV if DEBUG else ENV_DJANGO_SETTINGS_PROD



