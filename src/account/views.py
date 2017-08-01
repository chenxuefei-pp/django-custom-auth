import logging
from django.shortcuts import render

logger = logging.getLogger('django.request')


class LoginView(object):
    pass


def login(request):
    logger.error('This is a logger')
    return render(request, 'account/login.html')
