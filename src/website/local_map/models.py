# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager

from ..privacy import PrivacyMixin
from ..utils.models import PostcodeLocationMixin


class Map(PrivacyMixin, PostcodeLocationMixin, models.Model):
    CURRENT_PARTNER = 'current-partner'
    PARTNER_OPPORTUNITY = 'partner-opportunity'
    RELATIONSHIP_CHOICES = (
        (CURRENT_PARTNER, _('Current Partner')),
        (PARTNER_OPPORTUNITY, _('Partner Opportunity')),
    )

    NATIONAL_CHARITY = 'National Charity'
    LOCAL_CHARITY = 'Local Charity'
    HOUSING_ASSOCIATION = 'Housing Association'
    LOCAL_AUTHORITY = 'Local Authority'
    PRIVATE_COMPANY = 'Local Company'
    NHS_BODY = 'NHS Body'
    ANOTHER_LOCAL_MIND = 'Another Local Mind'
    RETHINK = 'Rethink'
    RELATE = 'Relate'
    AGEUK = 'Age Uk'
    REACH = 'Reach'
    MACMILLAN = 'Macmillan'
    CAB = 'Cab'
    TURNING_POINT = 'Turning Point'
    MENCAP = 'Mencap'
    CRUSE = 'Cruse'
    SAMARITANS = 'Samaritans'
    FAMILY_ACTION = 'Family Action'
    NATIONAL_TRUST ='National Trust'
    YMCS = 'YMCA'
    CHILD_POVERTY_ACTION_GROUP = 'Child Poverty Action Group'
    ALTERNATIVES_TO_VIOLENCE_PROJECT = 'Alternatives to Voilence Project'
    CATEGORY_CHOICES = (
        (NATIONAL_CHARITY, _('National Charity')),
        (LOCAL_CHARITY, _('Local Charity')),
        (HOUSING_ASSOCIATION, _('Housing Association')),
        (LOCAL_AUTHORITY, _('Local Authority')),
        (PRIVATE_COMPANY, _('Local Company')),
        (NHS_BODY, _('NHS Body')),
        (ANOTHER_LOCAL_MIND, _('Another Local Mind')),
        (RETHINK, _('Rethink')),
        (RELATE, _('Relate')),
        (AGEUK, _('Age Uk')),
        (REACH, _('Reach')),
        (MACMILLAN, _('Macmillan')),
        (CAB, _('Cab')),
        (TURNING_POINT, _('Turning Point')),
        (MENCAP, _('Mencap')),
        (CRUSE, _('Cruse')),
        (SAMARITANS, _('Samaritans')),
        (FAMILY_ACTION, _('Family Action')),
        (NATIONAL_TRUST, _('National Trust')),
        (YMCS, _('YMCA')),
        (CHILD_POVERTY_ACTION_GROUP, _('Child Poverty Action Group')),
        (ALTERNATIVES_TO_VIOLENCE_PROJECT, _('Alternatives to Voilence Project')),
    )

    user = models.ForeignKey('accounts.User', verbose_name=_('Creator'))
    local_mind = models.ForeignKey('local_minds.LocalMind', related_name='partners')

    name = models.CharField(_('Name'), max_length=120)
    email = models.EmailField(_('Email'), max_length=120, blank=True)
    address = models.TextField(_('Address'), blank=True)
    telephone = models.CharField(_('Contact number'), max_length=16, blank=True)
    postcode = models.CharField(_('Postcode'), max_length=120, help_text=_('This to create a marker on the map.'))

    relationship = models.CharField(max_length=120, choices=RELATIONSHIP_CHOICES)
    website = models.URLField(_('Website'), blank=True)
    category = models.CharField(_('Type'), max_length=50, choices=CATEGORY_CHOICES)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('My Local Area')
        verbose_name_plural = _('My Local Area')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'local-map', (), {}

    @property
    def marker_icon(self):
        if not self.relationship or not self.category:
            return None
        file_template = '{base_path}/{relationship}/{category}.png'
        if self.relationship == self.CURRENT_PARTNER:
            relationship = 'current'
        elif self.relationship == self.PARTNER_OPPORTUNITY:
            relationship = 'potential'
        else:
            return None
        category = self.category.replace(' ', '-').lower()
        return os.path.join(
            settings.STATIC_URL,
            'assets',
            'img',
            'ui',
            'icons',
            'map-markers',
            relationship,
            '{}.png'.format(category))
