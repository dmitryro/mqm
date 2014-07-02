# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Update, Openhub_Update
from website.utils.admin import TextEditor


class UpdateAdminForm(forms.ModelForm):
    class Meta:
        model = Update
        widgets = {
            'description': TextEditor(),
        }


class UpdateAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date')
    save_on_top = True
    form = UpdateAdminForm
    search_fields = (
        'title',
        'description',)
    fieldsets = (
        (_('General'), {
            'classes': ('wide',),
            'fields': (
                'title',
                'date',
                'description',
                #'slug',
            ),
        }),
        (_('Media'), {
            'classes': ('wide',),
            'fields': (
                'list_image',
                'main_image',
                'video',
            ),
        }),
    )
    save_on_top = True


class Openhub_UpdateAdminForm(forms.ModelForm):
    class Meta:
        model = Openhub_Update
        widgets = {
            'description': TextEditor(),
        }

class Openhub_UpdateAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date')
    save_on_top = True
    form = Openhub_UpdateAdminForm    
    search_fields = (
        'title',
        'description',)
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
    )
    save_on_top = True

admin.site.register(Update, UpdateAdmin)
admin.site.register(Openhub_Update, Openhub_UpdateAdmin)
