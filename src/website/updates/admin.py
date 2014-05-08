# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Update


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

admin.site.register(Update, UpdateAdmin)
