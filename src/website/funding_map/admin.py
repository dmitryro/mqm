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
        'local_mind',
        'privacy')
    list_editable = ('privacy',)
    list_filter = ('privacy',)
    search_fields = ('title',)
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
                'user',
                'local_mind',
                'privacy',
            ),
        }),
    )
    save_on_top = True


admin.site.register(Funding, FundingAdmin)
