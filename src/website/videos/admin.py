# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Tag, Video


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name')
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'name',
                'slug',
            ),
        }),
    )
    save_on_top = True

class VideoAdmin(admin.ModelAdmin):
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
        (_('Media'), {
            'classes': ('wide',),
            'fields': (
                'url;,
            ),
        }),
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'tags',
                'privacy',
                'slug',
            ),
        }),
        prepopulated_fields = {
        'slug': ('title',),
        }
    )
    save_on_top = True

admin.site.register(External_News, External_NewsAdmin)
admin.site.register(Positive_News, Positive_NewsAdmin)
