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


class Branding(models.Model):
    # content
    title = models.CharField(max_length=250)
    date = models.DateField(_('Date'))

    # media
    file = MediaField(
        related_name='branding_file',
        limit_choices_to={'content_type__model':'download'},)
    url = models.URLField(null=True, blank=True, help_text="to share if coming from google docs/dropbox - permission will need to be open")

    #rating = .......
    privacy = models.CharField(max_length=120, choices=PRIVACY_CHOICES)
    slug = models.SlugField(unique=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    # managers
    objects = GenericPublicManager()
    public = PublicOnlyManager()

    class Meta:
        verbose_name = _(u'Branding')
        verbose_name_plural = _(u'Branding')
        ordering = ('-date',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('branding', args=(self.slug,))
