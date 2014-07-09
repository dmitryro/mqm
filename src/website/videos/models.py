# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)

from ..privacy import PrivacyMixin


class Tag(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = _(u'Tags')
        verbose_name_plural = _(u'Tags')

    def __unicode__(self):
        return self.name


class Video(PrivacyMixin, models.Model):
    local_mind = models.ForeignKey('local_minds.LocalMind', verbose_name=_('Local Mind'), null=True, blank=True, related_name='videos')
    user = models.ForeignKey('accounts.User', verbose_name=_('User'), null=True, blank=True, related_name='videos')

    slug = AutoSlugField(populate_from=('title',), unique=True)
    title = models.CharField(max_length=250)
    date = models.DateField(_('Date'))
    description = models.TextField(null=True, blank=True)

    # media
    url = models.URLField(null=True, blank=True, help_text="Enter the full YouTube or Vimeo URL")

    # categorization
    tags = models.ManyToManyField(Tag, blank=True, symmetrical=False,)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _(u'Video')
        verbose_name_plural = _(u'Video')
        ordering = ('-date',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'videos', (self.slug,), {}
