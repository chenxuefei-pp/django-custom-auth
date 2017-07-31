from datetime import date, datetime

import six
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.db import models
from six import python_2_unicode_compatible

from account.validators import MobileAsciiUsernameValidator, MobileUnicodeUsernameValidator


class UserManager(BaseUserManager):
    def create_user(self, umobile, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not umobile:
            raise ValueError('Users must have an email address')

        user = self.model(
            umobile=umobile,
            unickname=umobile
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, umobile, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            umobile,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


@python_2_unicode_compatible
class User(AbstractBaseUser,PermissionsMixin):
    GenderChoice = (
        (0, _('Male')),
        (1, _('Female'))
    )

    username_validator = MobileUnicodeUsernameValidator() if six.PY3 else MobileAsciiUsernameValidator()

    umobile = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_('User Mobile Phone Number'),
        help_text=_('Required 13 number.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that mobile phone number already exists."),
        },
    )
    uemail = models.EmailField(unique=True, verbose_name=_('User e-mail'), null=True, blank=True)
    unickname = models.CharField(max_length=128, unique=True, verbose_name=_('User Nickname'))

    urealname = models.CharField(max_length=128, verbose_name=_('User Realname'), null=True)
    ugender = models.IntegerField(verbose_name=_('User Gender'), choices=GenderChoice, default=0)
    ubirthday = models.DateField(verbose_name=_('User birthday'), default=date.today)

    ucountry = models.CharField(max_length=64, verbose_name=_('User Country'), default='')
    uprovince = models.CharField(max_length=64, verbose_name=_('User Province'), default='')
    ucity = models.CharField(max_length=64, verbose_name=_('User City'), default='')
    uaddress = models.TextField(verbose_name=_('User Address'), default='')

    ubio = models.TextField(verbose_name=_('User BIO'), default='')

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    EMAIL_FIELD = 'uemail'
    USERNAME_FIELD = 'umobile'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name_plural = _('CustomUser')
        verbose_name = _('CustomUsers')

    def __str__(self):
        return self.unickname

    def get_full_name(self):
        return self.urealname
        pass

    def get_short_name(self):
        return self.urealname
        pass

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser
