from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.db import models
from six import python_2_unicode_compatible


@python_2_unicode_compatible
class User(AbstractBaseUser):
    GenderChoice = (
        (0, _('Male')),
        (1, _('Female'))
    )

    umobile = models.CharField(max_length=20, unique=True, verbose_name=_('User Mobile Phone Number'))
    uemail = models.CharField(max_length=64, unique=True, verbose_name=_('User e-mail'))
    urealname = models.CharField(max_length=128, verbose_name=_('User Realname'))
    unickname = models.CharField(max_length=128, verbose_name=_('User Nickname'))
    ugender = models.IntegerField(verbose_name=_('User Gender'), choices=GenderChoice)
    ubirthday = models.DateField(verbose_name=_('User birthday'))

    ucountry = models.CharField(max_length=64, verbose_name=_('User Country'))
    uprovince = models.CharField(max_length=64, verbose_name=_('User Province'))
    ucity = models.CharField(max_length=64, verbose_name=_('User City'))
    uaddress = models.TextField(verbose_name=_('User Address'))

    ubio = models.TextField(verbose_name=_('User BIO'))

    USERNAME_FIELD = 'umobile'
    REQUIRED_FIELDS = []

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
