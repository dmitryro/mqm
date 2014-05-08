# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager
from mediastore.fields import MediaField, MultipleMediaField


PRIVACY_CHOICES = (
    (LOCAL, _('Local')),
    (NATIONAL, _('National')),
    (PRIVATE, _('Private')),
)
class Funding(models.Model):
    title = models.CharField(max_length=120)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    telephone = models.CharField(max_length=16,null=True, blank=True)
    email = models.CharField(max_length=120,null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    postcode = models.CharField(max_length=120, help_text="this is how we generate a map")

    privacy = models.CharField(max_length=120, choices=PRIVACY_CHOICES)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Funding Map')
        verbose_name_plural = _('Funding Map')

    def __unicode__(self):
        return self.title
