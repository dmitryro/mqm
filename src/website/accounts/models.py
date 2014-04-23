# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group as _Group
from django.contrib.auth.models import User as _User
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class User(_User):
    job_title = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/')

    class Meta:
        verbose_name = _(u'User')
        verbose_name_plural = _(u'Users')

    def __unicode__(self):
        return self.username


class Group(_Group):
    class Meta:
        proxy = True


def create_user_data(sender, instance, created, **kwargs):
    if sender is _User and created:
        User.objects.create(user_ptr=instance)


post_save.connect(create_user_data, sender=_User)