# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Tag, Video
from website.utils.admin import TextEditor


class VideoAdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'description': TextEditor(),
        }

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
    save_on_top = True
    form = VideoAdminForm
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
                'local_mind',
                'user',
            ),
        }),
    )
    save_on_top = True

admin.site.register(Tag, TagAdmin)
admin.site.register(Video, VideoAdmin)
