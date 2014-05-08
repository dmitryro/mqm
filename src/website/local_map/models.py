# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager
from mediastore.fields import MediaField, MultipleMediaField



class Marker(models.Model):
    title = models.CharField(max_length=120)
    icon = MediaField(
        related_name='marker_image',
        limit_choices_to={'content_type__model': 'image'},)

    class Meta:
        verbose_name = _('Map Marker')
        verbose_name_plural = _('Map Markers')

    def __unicode__(self):
        return self.title


LOCAL = 'local'
NATIONAL = 'national'
PRIVATE = 'private'
PRIVACY_CHOICES = (
    (LOCAL, _('Local')),
    (NATIONAL, _('National')),
    (PRIVATE, _('Private')),
)

CURRENT_PARTNER = 'Current Partner'
PARTNER_OPPORTUNITY = 'Partner Opportunity'
RELATIONSHIP_CHOICES = (
    (CURRENT_PARTNER, _('Current Partner')),
    (PARTNER_OPPORTUNITY, _('Partner Opportunity')),
)

class Map(models.Model):
    name = models.CharField(max_length=120)
    address = models.TextField(null=True, blank=True)
    telephone = models.CharField(max_length=16,null=True, blank=True)
    email = models.CharField(max_length=120,null=True, blank=True)
    postcode = models.CharField(max_length=120, help_text="this is how we generate a map")
    marker = models.ForeignKey(Marker)
    relationship = models.CharField(max_length=120, choices=RELATIONSHIP_CHOICES)
    privacy = models.CharField(max_length=120, choices=PRIVACY_CHOICES)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Local Map')
        verbose_name_plural = _('Local Maps')

    def __unicode__(self):
        return self.name
