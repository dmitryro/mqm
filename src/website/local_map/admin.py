# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Marker, Map


class MarkerAdmin(admin.ModelAdmin):
    list_display = (
        'title',)
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'title',
                'icon',
            ),
        }),
    )
    save_on_top = True



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
                'address',
                'postcode',
                'telephone',
                'email',
            ),
        }),
        (_('Media'), {
            'classes': ('wide',),
            'fields': (
                'marker',
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

admin.site.register(Marker, MarkerAdmin)
admin.site.register(Map, MapAdmin)
