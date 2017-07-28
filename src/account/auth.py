# -*- coding:utf-8 -*-
'''
    Author : Xuefei Chen
    Email : chenxuefei_pp@163.com
    Created on : 2017/7/28 12:42
'''
from account.models import User


class MobileAuthBackend(object):

    def authenticate(self, umobile=None, password=None):
        try:
            user = User.objects.get(umobile__iexact=umobile)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None