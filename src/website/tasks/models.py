# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)


class Task(models.Model):
    local_mind = models.ForeignKey('local_minds.LocalMind', related_name='tasks')
    user = models.ForeignKey('accounts.User', verbose_name=_('Created by'),
                             related_name='created_tasks')

    slug = AutoSlugField(unique=True, populate_from='text')
    text = models.CharField(_('Description'), max_length=141, help_text=_('limited to 141 characters'))
    due_date = models.DateField(_('Due Date'), null=True, blank=True)

    done = models.BooleanField(default=False, db_index=True)
    done_date = models.DateTimeField(null=True, blank=True)

    sort_value = models.IntegerField(default=0, db_index=True)
    is_priority = models.BooleanField(default=False, db_index=True)
    assigned_to = models.ForeignKey('accounts.User', null=True, blank=True,
        db_index=True,
        related_name='tasks')

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        ordering = ('local_mind', 'sort_value',)
        verbose_name = _('To Do')
        verbose_name_plural = _('To Dos')

    def __unicode__(self):
        return self.text

    @models.permalink
    def get_absolute_url(self):
        return 'tasks', (), {}

    def comment_count(self):
        return self.comments.count()

    def mark_as_done(self, done=True):
        self.done = done
        self.save()



class Comment(models.Model):
    task = models.ForeignKey('Task', related_name='comments')

    user = models.ForeignKey('accounts.User', related_name='task_comments')
    text = models.TextField()

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __unicode__(self):
        return self.text
