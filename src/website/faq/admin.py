# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'date',
        #'author',
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
        #'author')
    search_fields = (
        'name',)
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'question',
                'answer',
                'date',
                #'author',
            ),
        }),
    )
    save_on_top = True


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
