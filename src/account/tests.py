from django.core.mail import send_mail
from django.test import TestCase

# Create your tests here.


class SendEmailTests(TestCase):

    def test_send_email_message(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        message = 'This is a Test Value'
        print('Now Send Email')
        send_mail(
            'Subject here',
            'Here is the message.',
            '395470486@qq.com',
            ['chenxuefei_pp@163.com'],
            fail_silently=False
        )