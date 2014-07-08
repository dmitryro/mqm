# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager
from mediastore.fields import MediaField, MultipleMediaField
from taggit.managers import TaggableManager
from ..privacy import PrivacyMixin


class BaseNews(PrivacyMixin, models.Model):
    title = models.CharField(_('Title'), max_length=120)
    slug = AutoSlugField(populate_from=('title',), unique=True)
    date = models.DateField(_('Entry Date'), null=True, blank=True)
    user = models.ForeignKey('accounts.User', verbose_name=_('Author'))
    description = models.TextField(blank=True)
    tags = TaggableManager(blank=True)
    source = models.CharField(max_length=120, blank=True,
        help_text=_(
            'Enter a URL to a online source or simply write the publication '
            'name and author.'))

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        abstract = True
        ordering = ('-date',)

    def __unicode__(self):
        return self.title


class ExternalNews(BaseNews):
    local_mind = models.ForeignKey('local_minds.LocalMind', related_name='externalnews')
    image = MediaField(
        related_name='externalnews_image',
        limit_choices_to={'content_type__model': 'image'},null=True, blank=True)
    download = MediaField(
        related_name='externalnews_download',
        limit_choices_to={'content_type__model': 'download'},null=True, blank=True)

    class Meta:
        verbose_name = _('External News')
        verbose_name_plural = _('External News')
        ordering = ('-date',)

    @models.permalink
    def get_absolute_url(self):
        return 'external-news', (), {'slug': self.slug}


class PositiveNews(BaseNews):
    local_mind = models.ForeignKey('local_minds.LocalMind', related_name='positivenews')
    list_image = MediaField(
        related_name='positivenews_image',
        limit_choices_to={'content_type__model': 'image'},null=True, blank=True)
    download = MediaField(
        related_name='positivenews_download',
        limit_choices_to={'content_type__model': 'download'},null=True, blank=True)

    class Meta:
        verbose_name = _('Positive News')
        verbose_name_plural = _('Positive News')
        ordering = ('-date',)

    @models.permalink
    def get_absolute_url(self):
        return 'positive-news', (), {'slug': self.slug}
