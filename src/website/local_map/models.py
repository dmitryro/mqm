# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager
from mediastore.fields import MediaField, MultipleMediaField
from ..privacy import PrivacyField


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


class Map(models.Model):
    CURRENT_PARTNER = 'current-partner'
    PARTNER_OPPORTUNITY = 'partner-opportunity'
    RELATIONSHIP_CHOICES = (
        (CURRENT_PARTNER, _('Current Partner')),
        (PARTNER_OPPORTUNITY, _('Partner Opportunity')),
    )

    CATEGORY_CHOICES = ()

    local_mind = models.ForeignKey('local_minds.LocalMind', related_name='partners')

    name = models.CharField(_('Name'), max_length=120)
    email = models.EmailField(_('Email'), max_length=120, blank=True)
    address = models.TextField(_('Address'), blank=True)
    telephone = models.CharField(_('Contact number'), max_length=16, blank=True)
    postcode = models.CharField(_('Postcode'), max_length=120, blank=True,
        help_text=_('This is how we generate a map.'))
    relationship = models.CharField(max_length=120, choices=RELATIONSHIP_CHOICES, blank=True)
    website = models.URLField(_('Website'), blank=True)
    category = models.CharField(_('Type'), max_length=50, choices=CATEGORY_CHOICES, blank=True)

    privacy = PrivacyField()
    marker = models.ForeignKey(Marker, null=True, blank=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Local Map')
        verbose_name_plural = _('Local Maps')

    def __unicode__(self):
        return self.name
