# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        #'region',
        #'organiser',
        'start',
        'end',
        'privacy')
    list_editable = ('privacy',)
    list_filter = ('privacy',)
    search_fields = (
        'name',)
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'title',
                'start',
                'end',
                'location',
                'postcode',
                #'region',
                #'organiser',
            ),
        }),
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'privacy',
                'slug',
            ),
        }),
        prepopulated_fields = {
        'slug': ('title',),
        }
    )
    save_on_top = True

admin.site.register(Event, EventAdmin)
