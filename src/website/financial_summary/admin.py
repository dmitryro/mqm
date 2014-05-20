# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Financial_Summary


class Financial_SummaryAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_no',
        'title',
        'ammount',
        'due_date')
    search_fields = (
        'title',)
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'invoice_no',
                'title',
                'description',
                'ammount',
                'paid',
            ),
        }),
        (_('Dates'), {
            'classes': ('wide',),
            'fields': (
                'sent_date',
                'due_date',
                'reminder_date',
            ),
        }),
    )
    save_on_top = True

admin.site.register(Financial_Summary, Financial_SummaryAdmin)
