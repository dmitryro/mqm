# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Category, Tag, Document


class CategoryAdmin(ModelAdmin):
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

class TagAdmin(ModelAdmin):
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


class DocumentAdmin(ModelAdmin):
    list_display = ('title', 'date', 'privacy',)
    list_editable = ('privacy',)
    list_filter = ('privacy',)
    search_fields = ('title', 'tags',)
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
                'categories',
                'tags',
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
admin.site.register(Tag, TagAdmin)
admin.site.register(Document, DocumentAdmin)
