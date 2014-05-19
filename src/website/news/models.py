# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager
from mediastore.fields import MediaField, MultipleMediaField

LOCAL = 'local'
NATIONAL = 'national'
PRIVATE = 'private'
PRIVACY_CHOICES = (
    (LOCAL, _('Local')),
    (NATIONAL, _('National')),
    (PRIVATE, _('Private')),
)
class External_News(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey('accounts.User', null=True, blank=True,
        db_index=True,
        related_name='external_news')
    description = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=120, help_text="Enter a URL to a online source or simply write the publication name and Author")

    privacy = models.CharField(max_length=120, choices=PRIVACY_CHOICES)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('External News')
        verbose_name_plural = _('External News')
        ordering = ('-date',)

    def __unicode__(self):
        return self.title


class Positive_News(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey('accounts.User', null=True, blank=True,
        db_index=True,
        related_name='positive_news')
    description = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=120)

    privacy = models.CharField(max_length=120, choices=PRIVACY_CHOICES)
    #tags = ....

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Positive News')
        verbose_name_plural = _('Positive News')
        ordering = ('-date',)

    def __unicode__(self):
        return self.title
