# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Todo, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class TodoAdmin(admin.ModelAdmin):
    list_display = ('text', 'project', 'revision', 'done', 'due_date', 'assigned_to', 'created_by',)
    list_filter = ('done', 'project',)
    inlines = [CommentInline]


admin.site.register(Todo, TodoAdmin)
