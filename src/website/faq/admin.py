# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'date',
        'user',
        'notifications',
        'privacy')
    list_editable = ('privacy',)
    list_filter = ('privacy',)
    search_fields = (
        'name',)
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'question',
                'date',
                'user',
            ),
        }),
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'notifications',
                'privacy',
            ),
        }),
    )
    save_on_top = True


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'date',
        'user')
    search_fields = (
        'name',)
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'question',
                'answer',
                'date',
                'user',
            ),
        }),
    )
    save_on_top = True


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
