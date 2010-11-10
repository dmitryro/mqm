# -*- coding: utf-8 -*-
from haystack import indexes
from haystack.sites import site
from django.conf import settings
from website.pages import get_model

Page = get_model()


class PageIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='content')
    absolute_url = indexes.CharField(indexed=False)
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    modified = indexes.DateTimeField(model_attr='modified')

    def prepare_absolute_url(self, obj):
        return obj.get_absolute_url()

    def get_query_set(self):
        return Page.public.all()

site.register(Page, PageIndex)
