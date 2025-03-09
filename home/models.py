# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Aaaaabbb(models.Model):

    #__Aaaaabbb_FIELDS__
    aaab = models.CharField(max_length=255, null=True, blank=True)
    aaac = models.CharField(max_length=255, null=True, blank=True)

    #__Aaaaabbb_FIELDS__END

    class Meta:
        verbose_name        = _("Aaaaabbb")
        verbose_name_plural = _("Aaaaabbb")


class Bbbb(models.Model):

    #__Bbbb_FIELDS__
    bba = models.CharField(max_length=255, null=True, blank=True)
    bbc = models.CharField(max_length=255, null=True, blank=True)

    #__Bbbb_FIELDS__END

    class Meta:
        verbose_name        = _("Bbbb")
        verbose_name_plural = _("Bbbb")



#__MODELS__END
