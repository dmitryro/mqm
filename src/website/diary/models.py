# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager

LOCAL = 'local'
NATIONAL = 'national'
PRIVATE = 'private'
PRIVACY_CHOICES = (
    (LOCAL, _('Local')),
    (NATIONAL, _('National')),
    (PRIVATE, _('Private')),
)

class Event(models.Model):
    # content
    title = models.CharField(max_length=250)
    start = models.DateTimeField(_('Event Start Date/Time'))
    end = models.DateTimeField(_('Event End Date/Time'))
    location = models.CharField(max_length=250,null=True, blank=True)
    postcode = models.CharField(max_length=250,null=True, blank=True)

    # categorization
    #region = models.ForeignKey(User.Region)
    organiser = models.ForeignKey('accounts.User', null=True, blank=True,
        db_index=True,
        related_name='event')
    privacy = models.CharField(max_length=120, choices=PRIVACY_CHOICES)
    slug = models.SlugField(unique=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    # managers
    objects = GenericPublicManager()
    public = PublicOnlyManager()

    class Meta:
        verbose_name = _(u'Event')
        verbose_name_plural = _(u'Event')
        ordering = ('-start',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', args=(self.slug,))
