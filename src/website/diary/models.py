# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)

from ..privacy import PrivacyMixin
from ..utils.models import PostcodeLocationMixin


class Event(PrivacyMixin, PostcodeLocationMixin, models.Model):
    user = models.ForeignKey('accounts.User', verbose_name=_('Organiser'), related_name='events')
    local_mind = models.ForeignKey('local_minds.LocalMind', verbose_name=_('Local Mind'), related_name='events')

    # content
    slug = AutoSlugField(populate_from=('title',))
    title = models.CharField(_('Title'), max_length=250)
    start = models.DateTimeField(_('Event Start Date/Time'))
    end = models.DateTimeField(_('Event End Date/Time'))
    location = models.CharField(_('Location'), max_length=250, null=True, blank=True)
    postcode = models.CharField(_('Postcode'), max_length=120, null=True, blank=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _(u'Event')
        verbose_name_plural = _(u'Events')
        ordering = ('-start',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'events', (self.slug,), {}
