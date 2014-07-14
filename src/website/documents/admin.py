# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mediastore.admin import ModelAdmin


from .models import Category, Document


class CategoryAdmin(ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {
        'slug': ('name',),
    }
    fieldsets = (
        (_('category details'), {
            'fields': (
                'name',
                'list_image',
                'description',
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
    list_display = ('title', 'local_mind', 'user', 'privacy', 'created',)
    list_editable = ('privacy',)
    list_filter = ('privacy',)
    search_fields = ('title', 'tags',)
    filter_horizontal = ('categories',)
    fieldsets = (
        (_('document'), {
            'fields': (
                'title',
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
                'local_mind',
                'user',
                'privacy',
            ),
            'classes': ('wide',),
        }),
    )
    save_on_top = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Document, DocumentAdmin)
