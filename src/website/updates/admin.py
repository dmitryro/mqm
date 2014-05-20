# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Update, Openhub_Update


class UpdateAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date')
    search_fields = (
        'title',
        'description',)
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'title',
                'date',
                'description',
            ),
        }),
        (_('Media'), {
            'classes': ('wide',),
            'fields': (
                'list_image',
                'main_image',
                'video',
            ),
        }),
    )
    save_on_top = True

class Openhub_UpdateAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date')
    search_fields = (
        'title',
        'description',)
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
    )
    save_on_top = True

admin.site.register(Update, UpdateAdmin)
admin.site.register(Openhub_Update, Openhub_UpdateAdmin)
