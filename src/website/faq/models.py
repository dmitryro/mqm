# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager
from mediastore.fields import MediaField, MultipleMediaField
from ..privacy import PrivacyMixin


class Question(PrivacyMixin, models.Model):
    local_mind = models.ForeignKey('local_minds.LocalMind', related_name='questions')
    user = models.ForeignKey('accounts.User', db_index=True, related_name='questions')

    question = models.CharField(max_length=140)
    date = models.DateField(null=True, blank=True)
    notifications = models.BooleanField(help_text=_('Notify me of updates'))

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Callout')
        verbose_name_plural = _('Callout')

    def __unicode__(self):
        return self.question

    @models.permalink
    def get_absolute_url(self):
        return 'questions', (self.pk,), {}


class Answer(models.Model):
    user = models.ForeignKey('accounts.User', db_index=True, related_name='answer')

    question = models.ForeignKey(Question, related_name='answers')

    answer = models.TextField()
    date = models.DateField(null=True, blank=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Callout Answer')
        verbose_name_plural = _('Callout Answers')

    @models.permalink
    def get_absolute_url(self):
        return ('answer', (self.pk,), {})
