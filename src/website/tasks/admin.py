# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Task, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'local_mind', 'done', 'due_date', 'assigned_to', 'created_by',)
    list_filter = ('done',)
    inlines = [CommentInline]


admin.site.register(Task, TaskAdmin)
