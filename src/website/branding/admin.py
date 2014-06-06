# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Branding



class BrandingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'privacy',)
    list_editable = ('privacy',)
    list_filter = ('privacy',)
    search_fields = ('title',)
    fieldsets = (
        (_('document'), {
            'fields': (
                'title',
                'date',
            ),
            'classes': ('wide',),
        }),
        (_('media'), {
            'fields': (
                'file',
                'url',
            ),
            'classes': ('wide',),
        }),
        (_('Categorisation'), {
            'fields': (
                'privacy',
                'slug',
            ),
            'classes': ('wide',),
        }),
    )
    prepopulated_fields = {
        'slug': ('title',),
    }
    save_on_top = True


admin.site.register(Branding, BrandingAdmin)
