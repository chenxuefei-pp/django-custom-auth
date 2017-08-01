# -*- coding:utf-8 -*-
'''
    Author : Xuefei Chen
    Email : chenxuefei_pp@163.com
    Created on : 2017/7/30 11:52
'''
from django.conf import settings
from django.utils.module_loading import import_string


def get_connection(backend=None,**kwargs):
    klass = import_string(backend or settings.SMS_BACKEND)
    return klass(**kwargs)
    pass


def send_verify_code_message(username, verify_code, phonenumber, connection=None):
    connection = connection or get_connection()
    connection.send_verify_code_message(username,verify_code,phonenumber)
    pass