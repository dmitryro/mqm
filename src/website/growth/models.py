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



class Growth(models.Model):
    # content
    title = models.CharField(max_length=250)
    date = models.DateField(_('Date'))
    description = models.TextField(null=True, blank=True)

    #categorisation
    achieved = models.BooleanField(default=False)
    category = models.ForeignKey(Category, blank=True)
    privacy = models.CharField(max_length=120, choices=PRIVACY_CHOICES)
    slug = models.SlugField(unique=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    # managers
    objects = GenericPublicManager()
    public = PublicOnlyManager()

    class Meta:
        verbose_name = _(u'Areas of Growth')
        verbose_name_plural = _(u'Areas of Growth')
        ordering = ('-date',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('growth', args=(self.slug,))
