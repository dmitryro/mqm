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


def category_count():
    return Category.objects.count()
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    # categorization
    sort_value = models.IntegerField(default=category_count,
        db_index=True)

    objects = GenericPublicManager()
    public = PublicOnlyManager()

    class Meta:
        ordering = ('sort_value',)
        verbose_name = _(u'Category')
        verbose_name_plural = _(u'Categories')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'document', (), {'category_slug': self.slug}



def tag_count():
    return Tag.objects.count()
class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    # categorization
    sort_value = models.IntegerField(default=tag_count,
        db_index=True)

    objects = GenericPublicManager()
    public = PublicOnlyManager()

    class Meta:
        ordering = ('sort_value',)
        verbose_name = _(u'Tags')
        verbose_name_plural = _(u'Tags')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'document', (), {'tag_slug': self.slug}



class Document(models.Model):
    # content
    title = models.CharField(max_length=250)
    date = models.DateField(_('Date'))

    # media
    file = MediaField(
        related_name='document_file',
        limit_choices_to={'content_type__model':'download'},)
    url = models.URLField(null=True, blank=True, help_text="to share if coming from google docs/dropbox - permission will need to be open")

    # categorization
    categories = models.ManyToManyField(Category, blank=True, symmetrical=False,)
    tags = models.ManyToManyField(Tag, blank=True, symmetrical=False,)
    #rating = .......
    privacy = models.CharField(max_length=120, choices=PRIVACY_CHOICES)
    slug = models.SlugField(unique=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    # managers
    objects = GenericPublicManager()
    public = PublicOnlyManager()

    class Meta:
        verbose_name = _(u'Document')
        verbose_name_plural = _(u'Documents')
        ordering = ('-date',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('document', args=(self.slug,))
