# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)


class Todo(models.Model):
    #project = models.ForeignKey('projects.Project', related_name='todos')
    #revision = models.ForeignKey('revisions.Revision', null=True, blank=True, related_name='todos')

    slug = AutoSlugField(unique=True, populate_from='text')
    text = models.TextField()
    due_date = models.DateField(null=True, blank=True)

    done = models.BooleanField(default=False, db_index=True)
    done_date = models.DateTimeField(null=True, blank=True)

    sort_value = models.IntegerField(default=0, db_index=True)
    is_priority = models.BooleanField(default=False, db_index=True)
    assigned_to = models.ForeignKey('accounts.User', null=True, blank=True,
        db_index=True,
        related_name='todos')
    created_by = models.ForeignKey('accounts.User', related_name='created_todos')

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        ordering = ('sort_value',)
        verbose_name = _('Todo')
        verbose_name_plural = _('Todos')

    def __unicode__(self):
        return self.text

    def comment_count(self):
        return self.comments.count()


class Comment(models.Model):
    todo = models.ForeignKey('Todo', related_name='comments')

    text = models.TextField()
    created_by = models.ForeignKey('accounts.User', related_name='todo_comments')

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __unicode__(self):
        return self.text
