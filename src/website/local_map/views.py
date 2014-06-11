# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from website.local_map.models import Marker, Map


class MapList(ListView):
    queryset = Map.objects.all()

map_list = MapList.as_view()
