# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Tag, Video


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',)
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
        'user',
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
            ),
        }),
        (_('Media'), {
            'classes': ('wide',),
            'fields': (
                'url',
            ),
        }),
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'tags',
                'privacy',
                'user',
                'slug',
            ),
        }),
    )
    prepopulated_fields = {
        'slug': ('title',),
    }
    save_on_top = True

admin.site.register(Tag, TagAdmin)
admin.site.register(Video, VideoAdmin)
