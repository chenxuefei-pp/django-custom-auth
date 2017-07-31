# -*- coding:utf-8 -*-
'''
    Author : Xuefei Chen
    Email : chenxuefei_pp@163.com
    Created on : 2017/7/31 18:23
'''
import sys

from auth_backend.settings.base import *
from backports.configparser import ConfigParser

cf = ConfigParser()
try:
    cf.read( DYNAMIC_ENV_FILE , encoding='utf-8')
except Exception as e:
    print('Read env file error: {0}'.format(e))
    sys.exit(-1)
    pass

# Aliyun SMS Setting
SMS_ACCESSKEY_ID = cf.get("sms", "SMS_ACCESSKEY_ID")
SMS_ACCESSKEY_SECRET = cf.get("sms", "SMS_ACCESSKEY_SECRET")
SMS_ENDPOINT = cf.get("sms", "SMS_ENDPOINT")
SMS_SIGN_NAME = cf.get("sms", "SMS_SIGN_NAME")
SMS_TEMPLATE_CODE = cf.get("sms", "SMS_TEMPLATE_CODE")

# Email Setting
EMAIL_HOST = cf.get("mail", "EMAIL_HOST")
EMAIL_PORT = cf.getint("mail", "EMAIL_PORT")
EMAIL_USE_SSL = cf.getboolean('mail','EMAIL_USE_SSL')
EMAIL_HOST_USER = cf.get("mail", "EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = cf.get("mail", "EMAIL_HOST_PASSWORD")

