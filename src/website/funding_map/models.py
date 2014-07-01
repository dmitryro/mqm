# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)

from ..privacy import PrivacyMixin
from ..utils.models import PostcodeLocationMixin


# opportunity to get funding (updated predominately bt National Mind)
class Funding(PrivacyMixin, PostcodeLocationMixin, models.Model):
    local_mind = models.ForeignKey('local_minds.LocalMind', verbose_name=_('Local Mind'), null=True, blank=True, related_name='fundings')
    user = models.ForeignKey('accounts.User', verbose_name=_('User'), null=True, blank=True, related_name='fundings')

    slug = AutoSlugField(populate_from=('title',), unique=True)
    title = models.CharField(max_length=120)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    telephone = models.CharField(max_length=16,null=True, blank=True)
    email = models.CharField(max_length=120,null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    postcode = models.CharField(max_length=120, help_text="This to create a marker on the map")

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Funding Map')
        verbose_name_plural = _('Funding Map')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'fundings', (), {}
