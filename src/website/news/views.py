# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from website.news.models import BaseNews, ExternalNews, PositiveNews
