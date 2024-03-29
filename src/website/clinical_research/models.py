# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from mediastore.fields import MediaField, MultipleMediaField

LOCAL = 'local'
NATIONAL = 'national'
PRIVATE = 'private'
PRIVACY_CHOICES = (
    (LOCAL, _('Local')),
    (NATIONAL, _('National')),
    (PRIVATE, _('Private')),
)
class Clinical_Research(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey('accounts.User', null=True, blank=True,
        db_index=True,
        related_name='research')
    description = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=120, help_text="Enter a URL to a online source or simply write the publication name and Author")

    privacy = models.CharField(max_length=120, choices=PRIVACY_CHOICES)

    files = MultipleMediaField(sorted=True,
        limit_choices_to={'content_type__model':'download'},
        related_name='research_file_set',
        null=True, blank=True)

    url = models.URLField(null=True, blank=True, help_text="to share if coming from google docs/dropbox - permission will need to be open")

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        ordering = ('-date',)
        verbose_name = _('Research')
        verbose_name_plural = _('Research')

    def __unicode__(self):
        return self.title
