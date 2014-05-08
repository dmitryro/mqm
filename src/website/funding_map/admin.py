# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Funding


class FundingAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'telephone',
        'email',
        'website',
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
                'start_date',
                'end_date',
                'description',
                'postcode',
                'telephone',
                'email',
                'website',
            ),
        }),
        (_('Categorisation'), {
            'classes': ('wide',),
            'fields': (
                'privacy',
            ),
        }),
    )
    save_on_top = True

admin.site.register(Funding, FundingAdmin)
