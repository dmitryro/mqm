# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Clinical_Research


class Clinical_ResearchAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'user',
        'privacy')
    list_editable = ('privacy',)
    list_filter = ('privacy',)
    search_fields = (
        'title',)
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
        (_('Media'), {
            'classes': ('wide',),
            'fields': (
                'files',
                'url',
            ),
        }),
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'privacy',
                'user',
            ),
        }),
    )
    save_on_top = True


admin.site.register(Clinical_Research, Clinical_ResearchAdmin)
