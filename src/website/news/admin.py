# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import ExternalNews, PositiveNews
from website.utils.admin import TextEditor


class BaseNewsAdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'description': TextEditor(),
        }

class BaseNewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'user',
        'privacy')
    list_editable = ('privacy',)
    list_filter = ('privacy',)
    save_on_top = True
    form = BaseNewsAdminForm
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
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'privacy',
                'local_mind',
                'user',
            ),
        }),
    )
    save_on_top = True


class ExternalNewsAdmin(BaseNewsAdmin):
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'title',
                'date',
                'description',
                'source',
                'image',
                'download',
            ),
        }),
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'privacy',
                'local_mind',
                'user',
            ),
        }),
    )


class PositiveNewsAdmin(BaseNewsAdmin):
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'title',
                'date',
                'description',
                'source',
                'list_image',
                'download',
            ),
        }),
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'privacy',
                'local_mind',
                'user',
            ),
        }),
    )


admin.site.register(ExternalNews, ExternalNewsAdmin)
admin.site.register(PositiveNews, PositiveNewsAdmin)
