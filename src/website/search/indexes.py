# -*- coding: utf-8 -*-
from haystack import site, indexes
from django.conf import settings


class BaseSearchIndex(indexes.RealTimeSearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField(indexed=False)
    modified = indexes.DateTimeField(model_attr='modified')

    def prepare_absolute_url(self, obj):
        return obj.get_absolute_url()

    def prepare_section(self, obj):
        return getattr(obj, 'section', '')

    def get_updated_field(self):
        if settings.DEBUG:
            return None
        return 'modified'

    def index_queryset(self):
        if hasattr(self.model, 'public'):
            return self.model.public.all()
        else:
            return self.model.objects.all()
