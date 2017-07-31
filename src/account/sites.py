# -*- coding:utf-8 -*-
'''
    Author : Xuefei Chen
    Email : chenxuefei_pp@163.com
    Created on : 2017/7/29 19:12
'''
from django.contrib.admin import AdminSite
from django.core.mail import send_mail
from django.views.decorators.cache import never_cache


class AccountSite(AdminSite):
    """
    账户Site控制器
    """

    @never_cache
    def login(self, request, extra_context=None):

        pass


    pass
