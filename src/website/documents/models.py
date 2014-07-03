# -*- coding: utf-8 -*-
from datetime import datetime
import os
import uuid

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager
from mediastore.fields import MediaField, MultipleMediaField
from taggit.managers import TaggableManager

from ..privacy.models import PrivacyMixin


def category_count():
    return Category.objects.count()
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    list_image = MediaField(
        related_name='document_category_image',
        limit_choices_to={'content_type__model': 'image'},null=True, blank=True)
        

    sort_value = models.IntegerField(default=category_count, db_index=True)

    class Meta:
        ordering = ('sort_value',)
        verbose_name = _(u'Category')
        verbose_name_plural = _(u'Categories')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('documents') + '?category=' + self.slug


def upload_path(instance, filename):
    now = datetime.utcnow()
    name, file_extension = os.path.splitext(filename)
    return os.path.join(
        'documents',
        now.strftime('%Y'),
        now.strftime('%m'),
        now.strftime('%d'),
        '{}{}'.format(uuid.uuid4(), file_extension))


class Document(PrivacyMixin, models.Model):
    local_mind = models.ForeignKey('local_minds.LocalMind', related_name='documents')
    user = models.ForeignKey('accounts.User', related_name='documents')

    title = models.CharField(_('Title'), max_length=250)
    slug = AutoSlugField(populate_from=('title',), unique=True)

    file = models.FileField(_('File'), null=True, blank=True, upload_to=upload_path)
    file_type = models.CharField(max_length=20, null=True, blank=True)

    url = models.URLField(_('URL'), null=True, blank=True, help_text=_(
        'to share if coming from google docs/dropbox - permission will be needed to open'))

    download_count = models.PositiveIntegerField(default=0)

    # categorization
    categories = models.ManyToManyField(Category, verbose_name=_('Categories'),
                                        blank=True, related_name='documents')
    tags = TaggableManager(blank=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _(u'Document')
        verbose_name_plural = _(u'Documents')
        ordering = ('-created',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'documents', (self.slug,), {}

    def get_download_url(self):
        if self.file:
            return self.file.url
        return self.url

    def save(self, *args, **kwargs):
        if self.file:
            __, extension = os.path.splitext(self.file.name)
            self.file_type = extension.lower().lstrip('.')
        else:
            self.file_type = None
        return super(Document, self).save(*args, **kwargs)
