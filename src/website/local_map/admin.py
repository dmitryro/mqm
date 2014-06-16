# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Map


class MapAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'telephone',
        'email',
        'relationship',
        'privacy')
    list_editable = ('privacy',)
    list_filter = ('relationship', 'privacy',)
    search_fields = (
        'name',)
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'name',
                'local_mind',
                'user',
                'category',
                'address',
                'postcode',
                'telephone',
                'email',
            ),
        }),
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'relationship',
                'privacy',
            ),
        }),
    )
    save_on_top = True


admin.site.register(Map, MapAdmin)
