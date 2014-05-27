# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager
from mediastore.fields import MediaField, MultipleMediaField
from ..privacy import PrivacyField


class Question(models.Model):
    local_mind = models.ForeignKey('local_minds.LocalMind', related_name='questions')

    question = models.CharField(max_length=140)
    date = models.DateField(null=True, blank=True)
    author = models.ForeignKey('accounts.User', null=True, blank=True,
        db_index=True,
        related_name='question')
    notifications = models.BooleanField(default=True)
    privacy = PrivacyField()

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    @models.permalink
    def get_absolute_url(self):
        return ('question', (self.pk,), {})


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.TextField()
    date = models.DateField(null=True, blank=True)
    author = models.ForeignKey('accounts.User', null=True, blank=True,
        db_index=True,
        related_name='answer')

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')

    @models.permalink
    def get_absolute_url(self):
        return ('answer', (self.pk,), {})
