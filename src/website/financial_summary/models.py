# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager
from mediastore.fields import MediaField, MultipleMediaField


class Financial_Summary(models.Model):
    invoice_no = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    sent_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    reminder_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    ammount = models.CharField(max_length=120)

    paid = models.BooleanField(default=False)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Financial Map')
        verbose_name_plural = _('Financial Map')

    def __unicode__(self):
        return self.title
