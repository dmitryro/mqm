# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import ExternalNews, PositiveNews


class BaseNewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'author',
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
                'author',
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


class ExternalNewsAdmin(BaseNewsAdmin):
    pass


class PositiveNewsAdmin(BaseNewsAdmin):
    pass


admin.site.register(ExternalNews, ExternalNewsAdmin)
admin.site.register(PositiveNews, PositiveNewsAdmin)
