# -*- coding:utf-8 -*-
'''
    Author : Xuefei Chen
    Email : chenxuefei_pp@163.com
    Created on : 2017/7/30 11:53
'''


class BaseSMSBackend(object):
    """
    Base SMS Backend
    """

    def __init__(self, *args, **kwargs):
        pass

    def send_message(self, message):
        '''
        Sned Message Virtual Method
        '''
        raise NotImplementedError('subclasses of BaseSMSBackend must override send_messages() method')
        pass

    def send_verify_code_message(self, username, verify_code, phonenumber):
        raise NotImplementedError('subclasses of BaseSMSBackend must override send_verify_code_message() method')
        pass
    pass
