# -*- coding:utf-8 -*-
'''
    Author : Xuefei Chen
    Email : chenxuefei_pp@163.com
    Created on : 2017/7/27 20:14
'''
import re

import six
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


@deconstructible
class MobileUnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^1[3458]\d{9}$'
    message = _(
        'Enter a valid mobile phone number. This value may contain only 13 number.'
    )
    flags = re.UNICODE if six.PY3 else 0

@deconstructible
class MobileAsciiUsernameValidator(validators.RegexValidator):
    regex = r'^1[3458]\d{9}$'
    message = _(
        'Enter a valid mobile phone number. This value may contain only 13 number.'
    )
    flags = re.ASCII if six.PY3 else 0



if __name__ == '__main__':
    regex = r'^1[3458]\d{9}$'
    mo = u'15102801312'
    f = re.compile(regex).match(mo)
    print(f)