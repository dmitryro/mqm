# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Category, Growth

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {
        'slug': ('name',),
    }
    fieldsets = (
        (_('category details'), {
            'fields': (
                'name',
            ),
            'classes': ('wide',),
        }),
        (_('Categorisation'), {
            'fields': (
                'sort_value',
                'slug',
            ),
            'classes': ('wide',),
        }),
    )


class GrowthAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'privacy',)
    list_editable = ('privacy',)
    list_filter = ('privacy',)
    search_fields = ('title',)
    fieldsets = (
        (_('document'), {
            'fields': (
                'title',
                'date',
                'description',
            ),
            'classes': ('wide',),
        }),
        (_('Categorisation'), {
            'fields': (
                'category',
                'achieved',
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

admin.site.register(Category, CategoryAdmin)
admin.site.register(Growth, GrowthAdmin)
