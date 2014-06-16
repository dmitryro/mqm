# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from website.local_map.models import Marker, Map
from website.privacy import PrivacyViewMixin


class MapList(PrivacyViewMixin, ListView):
    queryset = Map.objects.exclude(_latitude_postcode=None, _longitude_postcode=None)

    def get_context_data(self, **kwargs):
        kwargs['model'] = self.queryset.model
        return super(MapList, self).get_context_data(**kwargs)


map_list = MapList.as_view()
