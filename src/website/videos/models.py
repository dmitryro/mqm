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


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    objects = GenericPublicManager()
    public = PublicOnlyManager()

    class Meta:
        ordering = ('name',)
        verbose_name = _(u'Tags')
        verbose_name_plural = _(u'Tags')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'document', (), {'tag_slug': self.slug}



class Video(models.Model):
    # content
    title = models.CharField(max_length=250)
    date = models.DateField(_('Date'))
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey('accounts.User', null=True, blank=True,
        db_index=True,
        related_name='videos')

    # media
    url = models.URLField(null=True, blank=True, help_text="Enter the full YouTube or Vimeo URL")

    # categorization
    tags = models.ManyToManyField(Tag, blank=True, symmetrical=False,)
    privacy = models.CharField(max_length=120, choices=PRIVACY_CHOICES)
    slug = models.SlugField(unique=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    # managers
    objects = GenericPublicManager()
    public = PublicOnlyManager()

    class Meta:
        verbose_name = _(u'Video')
        verbose_name_plural = _(u'Video')
        ordering = ('-date',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('videos', args=(self.slug,))
