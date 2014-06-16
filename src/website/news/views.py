# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from website.news.models import BaseNews, ExternalNews, PositiveNews
from website.views.generic import CommonPrivacyViewMixin


class PositiveNewsListView(CommonPrivacyViewMixin, ListView):
    queryset = PositiveNews.objects.order_by('-created')


positive_news_list = PositiveNewsListView.as_view()


class PositiveNewsDetailView(CommonPrivacyViewMixin, DetailView):
    queryset = PositiveNews.objects.order_by('-created')


positive_news_detail = PositiveNewsDetailView.as_view()
