# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
import floppyforms.__future__ as forms

from ..common.forms import NodeForm
from .models import Document


class DocumentForm(NodeForm):
    class Meta:
        model = Document
        fields = (
            'title',
            'file',
            'url',
            'categories',
            'tags',
            'privacy',
        )

    def clean_url(self):
        file = self.cleaned_data.get('file')
        url = self.cleaned_data.get('url')
        if not file and not url:
            raise forms.ValidationError(
                _('You need to provide at least a file or a url.'))
        return url
