# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from django_publicmanager.managers import GenericPublicManager, \
    PublicOnlyManager
from mediastore.fields import MediaField, MultipleMediaField
from ..privacy import PrivacyMixin


def category_count():
    return Category.objects.count()
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    list_image = MediaField(
        related_name='document_category_image',
        limit_choices_to={'content_type__model': 'image'},null=True, blank=True)


    sort_value = models.IntegerField(default=category_count, db_index=True)

    class Meta:
        app_label = 'Callout'
        ordering = ('sort_value',)
        verbose_name = _(u'Category')
        verbose_name_plural = _(u'Categories')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('documents') + '?category=' + self.slug



class Question(PrivacyMixin, models.Model):
    local_mind = models.ForeignKey('local_minds.LocalMind', related_name='questions')
    user = models.ForeignKey('accounts.User', db_index=True, related_name='questions')

    question = models.CharField(max_length=140)
    date = models.DateField(null=True, blank=True)
    notifications = models.BooleanField(help_text=_('Notify me of updates'))

    categories = models.ManyToManyField(Category, verbose_name=_('Categories'),
                                        blank=True, related_name='questions')

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        app_label = 'Callout'
        verbose_name = _('Callout Question')
        verbose_name_plural = _('Callout Questions')

    def __unicode__(self):
        return unicode(self.question)

    @models.permalink
    def get_absolute_url(self):
        return 'questions', (self.pk,), {}

    @property
    def answers_count(self):
        if not hasattr(self, '_answers_count'):
            self._answers_count = self.answers.count()
        return self._answers_count


class Answer(models.Model):
    user = models.ForeignKey('accounts.User', db_index=True, related_name='answers')

    question = models.ForeignKey(Question, related_name='answers')

    answer = models.TextField()
    date = models.DateField(null=True, blank=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        app_label = 'Callout'
        verbose_name = _('Callout Answer')
        verbose_name_plural = _('Callout Answers')

    def __unicode__(self):
        return unicode(self.answer)

    @models.permalink
    def get_absolute_url(self):
        return 'questions', (self.question_id,), {}
