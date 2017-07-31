# -*- coding:utf-8 -*-
'''
    Author : Xuefei Chen
    Email : chenxuefei_pp@163.com
    Created on : 2017/7/30 12:26
'''
import random
from datetime import datetime

import re

from django.conf import settings

from opackage.aliyun.mns.account import Account
from opackage.aliyun.mns.mns_exception import MNSExceptionBase
from opackage.aliyun.mns.topic import DirectSMSInfo, TopicMessage
from opackage.sms.base import BaseSMSBackend


class AliSMSBackend(BaseSMSBackend):
    '''
    阿里云SMS实现
    '''

    def __init__(self, AccessKeyID=None, AccessKeySecret=None,
                 Endpoint=None, **kwargs):
        super(AliSMSBackend, self).__init__(**kwargs)

        self.Endpoint = Endpoint
        self.AccessKeySecret = AccessKeySecret
        self.AccessKeyID = AccessKeyID

        endpoint = settings.SMS_ENDPOINT if self.Endpoint is None else self.Endpoint
        accid = settings.SMS_ACCESSKEY_ID if self.AccessKeyID is None else self.AccessKeyID
        acckey = settings.SMS_ACCESSKEY_SECRET if self.AccessKeySecret is None else self.AccessKeySecret
        token = ''
        self.Account = Account(endpoint, accid, acckey, token, debug=False)
        topic_name = "sms.topic-cn-shenzhen"
        self.Topic = self.Account.get_topic(topic_name)

    def send_message(self, message):
        pass

    def send_verify_code_message(self, username, verify_code, phonenumber):
        phone_regex = re.compile(r'^1[3458]\d{9}$')
        if not phone_regex.match(phonenumber):
            raise RuntimeError('Phone number is invalid!')
        if not settings.SMS_SIGN_NAME or not settings.SMS_TEMPLATE_CODE:
            raise RuntimeError('Sign Name or Tempalte code is not set!')
        msg_body = '{0}{1}'.format(datetime.now().strftime('%Y%m%d%H%M%S'), random.randint(1000, 10000))
        direct_sms_attr = DirectSMSInfo(free_sign_name=settings.SMS_SIGN_NAME, template_code=settings.SMS_TEMPLATE_CODE, single=False)
        direct_sms_attr.add_receiver(receiver=phonenumber, params={u'name': username, u'code': verify_code})
        msg = TopicMessage(msg_body, direct_sms=direct_sms_attr)
        try:
            re_msg = self.Topic.publish_message(msg)
            print(
                "Publish Message Succeed. MessageBody:%s MessageID:%s" % (msg_body, re_msg.message_id)
            )
        except MNSExceptionBase as e:
            if e.type == "TopicNotExist":
                print(
                    "Topic not exist, please create it."
                )
            print(
                "Publish Message Fail. Exception:%s" % e
            )
        pass
