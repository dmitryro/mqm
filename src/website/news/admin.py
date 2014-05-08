# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import External_News, Positive_News


class External_NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'privacy')
    list_editable = ('privacy',)
    list_filter = ('privacy',)
    search_fields = (
        'title', 'description',)
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'title',
                'date',
                'description',
                'source',
            ),
        }),
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'privacy',
            ),
        }),
    )
    save_on_top = True

class Positive_NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'privacy')
    list_editable = ('privacy',)
    list_filter = ('privacy',)
    search_fields = (
        'title', 'description',)
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'title',
                'date',
                'description',
                'source',
            ),
        }),
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'privacy',
            ),
        }),
    )
    save_on_top = True

admin.site.register(External_News, External_NewsAdmin)
admin.site.register(Positive_News, Positive_NewsAdmin)
