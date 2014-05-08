# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager
from mediastore.fields import MediaField, MultipleMediaField




class Update(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)

    # media
    list_image = MediaField(
        related_name='update_list_image',
        limit_choices_to={'content_type__model': 'image'},null=True, blank=True)
    main_image = MediaField(
        related_name='update_main_image',
        limit_choices_to={'content_type__model': 'image'},null=True, blank=True)
    video = models.URLField(null=True, blank=True, help_text="paste the URL from Vimeo or YouTube here and we'll take care of the rest")

    #tags = ....

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('National Mind Updates')
        verbose_name_plural = _('National Mind Updates')

    def __unicode__(self):
        return self.title
