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

    def send_message(self, message, phonenumber):
        '''
        Sned Message Virtual Method
        :param message: 消息体
        :param phonenumber: 电话号码
        :return:
        '''
        raise NotImplementedError('subclasses of BaseSMSBackend must override send_messages() method')
        pass

    def send_verify_code_message(self, username, verify_code, phonenumber):
        '''
        按照特定模板发送验证码
        :param username: 用户名
        :param verify_code: 验证码
        :param phonenumber: 电话号码
        :return:
        '''
        raise NotImplementedError('subclasses of BaseSMSBackend must override send_verify_code_message() method')
        pass
    pass
