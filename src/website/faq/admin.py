# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Category, Question, Answer


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {
        'slug': ('name',),
    }
    fieldsets = (
        (_('category details'), {
            'fields': (
                'name',
                'list_image',
            ),
            'classes': ('wide',),
        }),
        (_('Categorisation'), {
            'fields': (
                'sort_value',
                'slug',
            ),
            'classes': ('wide',),
        }),
    )


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
                'local_mind',
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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
