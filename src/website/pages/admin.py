# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.db import models
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from website.pages.models import Page
from website.pages import get_model
from mediastore.admin import ModelAdmin
from website.utils.admin import TinyMCEAdminMixin


class PageAdminForm(forms.ModelForm):
    url = forms.RegexField(
        label=_('URL'),
        max_length=100,
        regex=r'^[-\w/\.]+$',
        help_text=_(
            u"Example: '/about/contact/'. Make sure to have leading "
            u"and trailing slashes."),
        error_message = _(
            u'This value must contain only letters, numbers, '
            u'underscores, dashes or slashes.'),
    )

    class Meta:
        model = Page


class PageAdmin(TinyMCEAdminMixin, ModelAdmin):
    form = PageAdminForm
    list_display = ('url', 'title', 'content_preview', 'is_public', 'pub_date')
    list_filter = ('is_public',)
    list_editable = ('is_public',)
    search_fields = ('url', 'title', 'content')
    date_hierarchy = 'created'

    fieldsets = (
        (None, {
            'fields': (
                'url',
                'title',
                'content',
                'is_public',
                'media',
            ),
        }),
        (_('Advanced options'), {
            'classes': ('collapse','wide'),
            'fields': ('pub_date', 'template_name'),
        }),
    )

    def content_preview(self, obj):
        value = obj.content
        value = strip_tags(value)
        if len(value) > 100:
            value = '%s ...' % value[:100]
        return value
    content_preview.short_description = _(u'Preview')


# Only register the default admin if the model is the default page model
# (this won't be true if there's a custom page app).
if get_model() is Page:
    admin.site.register(Page, PageAdmin)
