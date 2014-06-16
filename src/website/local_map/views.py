# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from website.local_map.models import Map
from website.views.generic import CommonPrivacyViewMixin, ListCreateView
from .forms import MapForm


class MapListView(CommonPrivacyViewMixin, ListCreateView):
    form_class = MapForm
    queryset = Map.objects.exclude(_latitude_postcode=None, _longitude_postcode=None)

    def get_form_kwargs(self):
        kwargs = super(MapListView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['model'] = self.queryset.model
        return super(MapListView, self).get_context_data(**kwargs)


map_list = MapListView.as_view()
